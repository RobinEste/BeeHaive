"""Pipeline orchestrator for BeeHaive knowledge item ingestion.

Ties together: fetch -> dedup check -> Gemini classify -> preview/commit to Neo4j.
Designed for CLI usage (sync, one item at a time).
"""

import logging

from neo4j import Session

from app.graph.mutations import create_knowledge_item_with_relations
from app.graph.queries import find_item_by_source_url, find_items_by_fuzzy_title
from app.ingestion.fetcher import fetch_source
from app.ingestion.llm import classify_text
from app.models.ingestion import IngestionResult, IngestionSource

logger = logging.getLogger(__name__)


def ingest(source: IngestionSource, session: Session, *, dry_run: bool = True) -> IngestionResult:
    """Run the full ingestion pipeline for a single knowledge item.

    Args:
        source: The item to ingest (url, title, source_type).
        session: Neo4j session for graph operations.
        dry_run: If True (default), show preview without writing to graph.

    Returns:
        IngestionResult with status and mappings.
    """
    url = str(source.url)
    logger.info("Starting ingestion for '%s' (%s)", source.title, url)

    # 1. Deduplication check (before fetching to save time/bandwidth)
    existing = find_item_by_source_url(session, url)
    if existing:
        logger.info("Duplicate found: '%s'", existing["title"])
        return IngestionResult(
            status="duplicate",
            existing=existing["title"],
        )

    fuzzy_matches = find_items_by_fuzzy_title(session, source.title)
    if fuzzy_matches:
        titles = [m["title"] for m in fuzzy_matches]
        logger.warning("Fuzzy title matches found: %s", titles)

    # 2. Fetch document content
    fetch_result = fetch_source(url, source.source_type)

    if fetch_result.fetch_status == "requires_pdf_processing":
        return IngestionResult(
            status="engine_unavailable",
            error="PDF processing not yet supported in CLI pipeline. Use HTML sources or add content manually.",
        )

    if fetch_result.fetch_status != "ok":
        error_msg = fetch_result.metadata.get("error", "Unknown fetch error")
        logger.error("Fetch failed for '%s': %s", url, error_msg)
        return IngestionResult(
            status="fetch_failed",
            error=f"Fetch failed: {error_msg}",
        )

    # 2b. PII scan check — abort if PII redaction failed (AVG Art. 5(1)(c))
    if not fetch_result.pii_clean:
        logger.error("PII scan failed for '%s' — aborting to prevent PII leakage", url)
        return IngestionResult(
            status="pii_scan_failed",
            error="PII scan failed — aborting to prevent unredacted PII reaching external APIs.",
        )

    # 3. Taxonomy mapping via Gemini
    mappings = classify_text(
        fetch_result.text,
        source.source_type,
        title=source.title,
    )

    if not mappings:
        return IngestionResult(
            status="no_mappings_found",
            suggestion="No taxonomy mappings found. Try a different source or map manually.",
        )

    # 4. Preview mode — return proposed mappings without writing
    if dry_run:
        logger.info("Dry-run: %d mappings proposed for '%s'", len(mappings), source.title)
        return IngestionResult(
            status="preview",
            mappings=mappings,
        )

    # 5. Create KnowledgeItem + relations in Neo4j
    create_knowledge_item_with_relations(session, source, mappings)
    logger.info("Ingested '%s' with %d relations", source.title, len(mappings))

    return IngestionResult(
        status="ingested",
        mappings=mappings,
    )
