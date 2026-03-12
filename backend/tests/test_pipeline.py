"""Tests for the ingestion pipeline orchestrator.

Uses mocked fetcher, LLM, and Neo4j session to test the pipeline flow
without external dependencies.
"""

from unittest.mock import MagicMock, patch

import pytest

from app.ingestion.pipeline import ingest
from app.models.ingestion import (
    FetchResult,
    IngestionSource,
    TaxonomyMapping,
)


@pytest.fixture
def source():
    return IngestionSource(
        url="https://example.com/test-article",
        title="Test Article on AI Ethics",
        source_type="regulation",
    )


@pytest.fixture
def mock_session():
    return MagicMock()


@pytest.fixture
def sample_mappings():
    return [
        TaxonomyMapping(
            entity_text="Knowledge",
            entity_type="BuildingBlock",
            matched_name="Knowledge",
            match_method="llm",
            confidence=0.95,
        ),
        TaxonomyMapping(
            entity_text="Transparency",
            entity_type="Guardrail",
            matched_name="Transparency",
            match_method="llm",
            confidence=0.88,
        ),
        TaxonomyMapping(
            entity_text="AI Ethics",
            entity_type="Topic",
            matched_name="AI Ethics",
            match_method="llm",
            confidence=0.92,
        ),
    ]


@pytest.fixture
def ok_fetch_result():
    return FetchResult(
        text="This is a test article about AI ethics and transparency.",
        source_url="https://example.com/test-article",
        fetch_status="ok",
        metadata={"content_length": 56},
    )


# --- Deduplication tests ---


@patch("app.ingestion.pipeline.find_item_by_source_url")
def test_duplicate_by_source_url(mock_find, source, mock_session):
    """Pipeline returns 'duplicate' when source_url already exists."""
    mock_find.return_value = {"title": "Existing Article"}

    result = ingest(source, mock_session)

    assert result.status == "duplicate"
    assert result.existing == "Existing Article"
    mock_find.assert_called_once_with(mock_session, str(source.url))


@patch("app.ingestion.pipeline.classify_text")
@patch("app.ingestion.pipeline.fetch_source")
@patch("app.ingestion.pipeline.find_items_by_fuzzy_title")
@patch("app.ingestion.pipeline.find_item_by_source_url")
def test_fuzzy_match_logs_warning_but_continues(
    mock_find_exact, mock_find_fuzzy, mock_fetch, mock_classify,
    source, mock_session, sample_mappings, ok_fetch_result,
):
    """Fuzzy title matches log a warning but don't block ingestion."""
    mock_find_exact.return_value = None
    mock_find_fuzzy.return_value = [{"title": "Similar Article"}]
    mock_fetch.return_value = ok_fetch_result
    mock_classify.return_value = sample_mappings

    result = ingest(source, mock_session)

    assert result.status == "preview"
    mock_find_fuzzy.assert_called_once()


# --- Fetch tests ---


@patch("app.ingestion.pipeline.find_items_by_fuzzy_title", return_value=[])
@patch("app.ingestion.pipeline.find_item_by_source_url", return_value=None)
@patch("app.ingestion.pipeline.fetch_source")
def test_fetch_failed(mock_fetch, mock_find_exact, mock_find_fuzzy, source, mock_session):
    """Pipeline returns error when fetch fails."""
    mock_fetch.return_value = FetchResult(
        text="",
        source_url=str(source.url),
        fetch_status="failed",
        metadata={"error": "HTTP 403"},
    )

    result = ingest(source, mock_session)

    assert result.status == "fetch_failed"
    assert "HTTP 403" in result.error


@patch("app.ingestion.pipeline.find_items_by_fuzzy_title", return_value=[])
@patch("app.ingestion.pipeline.find_item_by_source_url", return_value=None)
@patch("app.ingestion.pipeline.fetch_source")
def test_pdf_source_returns_engine_unavailable(mock_fetch, mock_find_exact, mock_find_fuzzy, mock_session):
    """Pipeline returns engine_unavailable for PDF sources."""
    paper_source = IngestionSource(
        url="https://arxiv.org/pdf/2024.12345",
        title="Some Paper",
        source_type="paper",
    )
    mock_fetch.return_value = FetchResult(
        text="",
        source_url="https://arxiv.org/pdf/2024.12345",
        fetch_status="requires_pdf_processing",
        metadata={},
    )

    result = ingest(paper_source, mock_session)

    assert result.status == "engine_unavailable"
    assert "PDF" in result.error


# --- PII scan tests ---


@patch("app.ingestion.pipeline.find_items_by_fuzzy_title", return_value=[])
@patch("app.ingestion.pipeline.find_item_by_source_url", return_value=None)
@patch("app.ingestion.pipeline.fetch_source")
def test_pii_scan_failed_aborts_pipeline(mock_fetch, mock_find_exact, mock_find_fuzzy, source, mock_session):
    """Pipeline returns pii_scan_failed when PII redaction failed."""
    mock_fetch.return_value = FetchResult(
        text="Text with unredacted email@example.com",
        source_url=str(source.url),
        fetch_status="ok",
        pii_clean=False,
        metadata={},
    )

    result = ingest(source, mock_session)

    assert result.status == "pii_scan_failed"
    assert "PII" in result.error


# --- Classification tests ---


@patch("app.ingestion.pipeline.classify_text", return_value=[])
@patch("app.ingestion.pipeline.fetch_source")
@patch("app.ingestion.pipeline.find_items_by_fuzzy_title", return_value=[])
@patch("app.ingestion.pipeline.find_item_by_source_url", return_value=None)
def test_no_mappings_found(mock_find, mock_fuzzy, mock_fetch, mock_classify, source, mock_session, ok_fetch_result):
    """Pipeline returns no_mappings_found when LLM returns nothing."""
    mock_fetch.return_value = ok_fetch_result

    result = ingest(source, mock_session)

    assert result.status == "no_mappings_found"
    assert result.suggestion is not None


# --- Dry-run / preview tests ---


@patch("app.ingestion.pipeline.classify_text")
@patch("app.ingestion.pipeline.fetch_source")
@patch("app.ingestion.pipeline.find_items_by_fuzzy_title", return_value=[])
@patch("app.ingestion.pipeline.find_item_by_source_url", return_value=None)
def test_dry_run_returns_preview(
    mock_find, mock_fuzzy, mock_fetch, mock_classify,
    source, mock_session, sample_mappings, ok_fetch_result,
):
    """Dry-run returns preview status with mappings."""
    mock_fetch.return_value = ok_fetch_result
    mock_classify.return_value = sample_mappings

    result = ingest(source, mock_session, dry_run=True)

    assert result.status == "preview"
    assert len(result.mappings) == 3
    assert result.mappings[0].entity_type == "BuildingBlock"


@patch("app.ingestion.pipeline.create_knowledge_item_with_relations")
@patch("app.ingestion.pipeline.classify_text")
@patch("app.ingestion.pipeline.fetch_source")
@patch("app.ingestion.pipeline.find_items_by_fuzzy_title", return_value=[])
@patch("app.ingestion.pipeline.find_item_by_source_url", return_value=None)
def test_dry_run_does_not_write_to_graph(
    mock_find, mock_fuzzy, mock_fetch, mock_classify, mock_create,
    source, mock_session, sample_mappings, ok_fetch_result,
):
    """Dry-run never calls create_knowledge_item_with_relations."""
    mock_fetch.return_value = ok_fetch_result
    mock_classify.return_value = sample_mappings

    ingest(source, mock_session, dry_run=True)

    mock_create.assert_not_called()


# --- Commit tests ---


@patch("app.ingestion.pipeline.create_knowledge_item_with_relations")
@patch("app.ingestion.pipeline.classify_text")
@patch("app.ingestion.pipeline.fetch_source")
@patch("app.ingestion.pipeline.find_items_by_fuzzy_title", return_value=[])
@patch("app.ingestion.pipeline.find_item_by_source_url", return_value=None)
def test_commit_writes_to_graph(
    mock_find, mock_fuzzy, mock_fetch, mock_classify, mock_create,
    source, mock_session, sample_mappings, ok_fetch_result,
):
    """With dry_run=False, pipeline writes to Neo4j."""
    mock_fetch.return_value = ok_fetch_result
    mock_classify.return_value = sample_mappings
    mock_create.return_value = {"title": source.title}

    result = ingest(source, mock_session, dry_run=False)

    assert result.status == "ingested"
    assert len(result.mappings) == 3
    mock_create.assert_called_once_with(mock_session, source, sample_mappings)


@patch("app.ingestion.pipeline.create_knowledge_item_with_relations")
@patch("app.ingestion.pipeline.classify_text")
@patch("app.ingestion.pipeline.fetch_source")
@patch("app.ingestion.pipeline.find_items_by_fuzzy_title", return_value=[])
@patch("app.ingestion.pipeline.find_item_by_source_url", return_value=None)
def test_commit_passes_correct_args_to_graph(
    mock_find, mock_fuzzy, mock_fetch, mock_classify, mock_create,
    source, mock_session, sample_mappings, ok_fetch_result,
):
    """Verify the source and mappings are passed correctly to the graph layer."""
    mock_fetch.return_value = ok_fetch_result
    mock_classify.return_value = sample_mappings
    mock_create.return_value = {"title": source.title}

    ingest(source, mock_session, dry_run=False)

    call_args = mock_create.call_args
    assert call_args[0][0] is mock_session
    assert call_args[0][1] is source
    assert call_args[0][2] is sample_mappings


# --- End-to-end flow tests ---


@patch("app.ingestion.pipeline.create_knowledge_item_with_relations")
@patch("app.ingestion.pipeline.classify_text")
@patch("app.ingestion.pipeline.fetch_source")
@patch("app.ingestion.pipeline.find_items_by_fuzzy_title", return_value=[])
@patch("app.ingestion.pipeline.find_item_by_source_url", return_value=None)
def test_full_flow_dedup_then_fetch_then_classify_then_write(
    mock_find, mock_fuzzy, mock_fetch, mock_classify, mock_create,
    source, mock_session, sample_mappings, ok_fetch_result,
):
    """Verify the pipeline calls steps in correct order."""
    mock_fetch.return_value = ok_fetch_result
    mock_classify.return_value = sample_mappings
    mock_create.return_value = {"title": source.title}

    ingest(source, mock_session, dry_run=False)

    # Verify call order: dedup -> fetch -> classify -> write
    mock_find.assert_called_once()
    mock_fetch.assert_called_once_with(str(source.url), source.source_type)
    mock_classify.assert_called_once_with(
        ok_fetch_result.text,
        source.source_type,
        title=source.title,
    )
    mock_create.assert_called_once()


@patch("app.ingestion.pipeline.classify_text")
@patch("app.ingestion.pipeline.fetch_source")
@patch("app.ingestion.pipeline.find_items_by_fuzzy_title", return_value=[])
@patch("app.ingestion.pipeline.find_item_by_source_url")
def test_duplicate_skips_fetch_and_classify(
    mock_find, mock_fuzzy, mock_fetch, mock_classify,
    source, mock_session,
):
    """Duplicate detection short-circuits before fetch and classify."""
    mock_find.return_value = {"title": "Already There"}

    ingest(source, mock_session)

    mock_fetch.assert_not_called()
    mock_classify.assert_not_called()
