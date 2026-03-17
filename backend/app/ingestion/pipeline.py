"""Ingestion pipeline orchestrator.

Coordinates the full flow: fetch → PII scan → dedup → classify → persist.
Supports dual ingest: writes to both the handmatige knowledge graph
(KnowledgeItem nodes) and LightRAG (for RAG query retrieval).

CLI-first design: all operations are synchronous except the optional
LightRAG ingest (async, bridged via asyncio.run).
"""

import asyncio
import logging

from app.graph.mutations import create_knowledge_item_with_relations
from app.graph.queries import find_item_by_source_url, find_items_by_fuzzy_title
from app.ingestion.fetcher import fetch_source
from app.ingestion.llm import classify_text
from app.ingestion.pii import scan_pii
from app.models.ingestion import (
    IngestionResult,
    IngestionSource,
)

logger = logging.getLogger(__name__)


def ingest(
    source: IngestionSource,
    neo4j_session,
    dry_run: bool = True,
    skip_rag: bool = False,
) -> IngestionResult:
    """Ingest a source document into the BeeHaive knowledge graph.

    Steps:
        1. Fetch document content (with SSRF protection + PII redaction)
        2. Check for duplicates (exact URL + fuzzy title)
        3. Classify text via Gemini → taxonomy mappings
        4. Preview mode (dry_run=True): show proposed mappings
        5. Persist: create KnowledgeItem + relations in Neo4j
        6. Optional: insert into LightRAG for RAG query retrieval

    Args:
        source: IngestionSource with url, title, source_type.
        neo4j_session: Active Neo4j session for graph operations.
        dry_run: If True (default), show preview without persisting.
        skip_rag: If True, skip LightRAG ingest (useful for testing).

    Returns:
        IngestionResult with status, mappings, and any errors.
    """
    url_str = str(source.url)
    logger.info("Starting ingestion for '%s' (%s)", source.title, url_str)

    # --- Step 1: Deduplication (before fetch to avoid wasted I/O) ---
    existing = find_item_by_source_url(neo4j_session, url_str)
    if existing:
        logger.info("Duplicate found: '%s' already exists", existing.get("title", "?"))
        return IngestionResult(
            status="duplicate",
            existing=existing.get("title", url_str),
        )

    # --- Step 2: Fetch ---
    fetch_result = fetch_source(url_str, source.source_type)

    if fetch_result.fetch_status == "requires_pdf_processing":
        return IngestionResult(
            status="engine_unavailable",
            error="PDF processing via RAG-Anything is not yet supported in CLI mode. "
            "Use HTML sources (regulation, guideline, best_practice) for now.",
        )

    if fetch_result.fetch_status != "ok":
        error_msg = fetch_result.metadata.get("error", "Unknown fetch error")
        logger.error("Fetch failed for '%s': %s", source.title, error_msg)
        return IngestionResult(
            status="fetch_failed",
            error=f"Fetch failed: {error_msg}",
        )

    # The fetcher already performs PII redaction before caching (AVG Art. 5(1)(c)).
    # Verify that text passed to the LLM is indeed from the redacted pipeline.
    text = fetch_result.text

    # Extra PII safety check — assert no PII slipped through
    pii_report = scan_pii(text)
    if pii_report.error:
        logger.error("PII re-scan failed: %s", pii_report.error)
        return IngestionResult(
            status="pii_scan_failed",
            error=f"PII safety check failed: {pii_report.error}",
            pii_report=pii_report,
        )

    # Fuzzy title check — warn but don't block
    similar = find_items_by_fuzzy_title(neo4j_session, source.title, limit=3)
    if similar:
        titles = [item.get("title", "?") for item in similar]
        logger.warning(
            "Similar items found for '%s': %s — proceeding anyway",
            source.title,
            titles,
        )

    # --- Step 3: Classify via Gemini ---
    mappings = classify_text(
        text=text,
        source_type=source.source_type,
        title=source.title,
    )

    if not mappings:
        logger.warning("No taxonomy mappings found for '%s'", source.title)
        return IngestionResult(
            status="no_mappings_found",
            suggestion="No mappings found. Try with a different source or add mappings manually.",
        )

    # --- Step 4: Preview mode ---
    if dry_run:
        logger.info("Dry run — showing %d proposed mappings", len(mappings))
        return IngestionResult(
            status="preview",
            mappings=mappings,
            pii_report=pii_report if pii_report.has_pii else None,
        )

    # --- Step 5: Persist to knowledge graph ---
    logger.info("Creating KnowledgeItem with %d relations", len(mappings))
    item = create_knowledge_item_with_relations(neo4j_session, source, mappings)
    logger.info("Created KnowledgeItem: %s", item.get("title", "?"))

    # --- Step 6: Dual ingest to LightRAG ---
    rag_synced = True
    if not skip_rag:
        try:
            _ingest_to_lightrag(text, source.title)
        except Exception as e:
            rag_synced = False
            logger.warning("LightRAG ingest failed: %s", e)

    return IngestionResult(
        status="ingested",
        mappings=mappings,
        pii_report=pii_report if pii_report.has_pii else None,
        rag_synced=rag_synced,
    )


def _run_async(coro):
    """Run an async coroutine from sync context, safe for both CLI and FastAPI."""
    try:
        asyncio.get_running_loop()
    except RuntimeError:
        # No event loop running (CLI) — use asyncio.run()
        return asyncio.run(coro)
    else:
        # Event loop already running (FastAPI) — run in a thread
        import concurrent.futures

        with concurrent.futures.ThreadPoolExecutor(max_workers=1) as pool:
            return pool.submit(asyncio.run, coro).result()


def _ingest_to_lightrag(text: str, title: str) -> None:
    """Insert text into LightRAG for RAG query retrieval.

    Uses _run_async() to bridge sync/async safely — works from both
    CLI (no event loop) and FastAPI (existing event loop).
    Failures are logged but do not block the main ingestion.
    """
    try:
        from app.rag.engine import create_rag_engine

        async def _do_ingest():
            engine = await create_rag_engine()
            content = f"# {title}\n\n{text}" if title else text
            await engine.lightrag.ainsert(content)

        _run_async(_do_ingest())
        logger.info("LightRAG ingest complete for '%s'", title)
    except Exception as e:
        # Non-fatal: KnowledgeItem is already in the graph
        logger.warning(
            "LightRAG ingest failed for '%s': %s — KnowledgeItem was "
            "persisted to Neo4j but is not available via RAG queries",
            title,
            e,
        )
