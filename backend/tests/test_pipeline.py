"""Unit tests for ingestion pipeline orchestrator.

Tests the full flow with mocked dependencies (fetcher, LLM, Neo4j).
Covers: happy path, deduplication, dry-run, error handling, LightRAG ingest.
"""

from unittest.mock import MagicMock, patch

from app.ingestion.pipeline import ingest
from app.models.ingestion import (
    FetchResult,
    IngestionSource,
    PIIReport,
    TaxonomyMapping,
)


# --- Fixtures ---


def _source(url="https://example.com/paper", title="Test Paper", source_type="regulation"):
    return IngestionSource(url=url, title=title, source_type=source_type)


def _fetch_ok(text="Some academic text about AI governance and privacy."):
    return FetchResult(
        text=text,
        source_url="https://example.com/paper",
        fetch_status="ok",
        metadata={"content_length": len(text)},
    )


def _fetch_failed():
    return FetchResult(
        text="",
        source_url="https://example.com/paper",
        fetch_status="failed",
        metadata={"error": "HTTP 403"},
    )


def _fetch_pdf():
    return FetchResult(
        text="",
        source_url="https://example.com/paper.pdf",
        fetch_status="requires_pdf_processing",
        metadata={},
    )


def _mappings():
    return [
        TaxonomyMapping(
            entity_text="AI governance",
            entity_type="BuildingBlock",
            matched_name="Knowledge",
            match_method="llm",
            confidence=0.9,
        ),
        TaxonomyMapping(
            entity_text="privacy",
            entity_type="Guardrail",
            matched_name="Privacy",
            match_method="llm",
            confidence=0.85,
        ),
    ]


# --- Tests ---


class TestPipelineHappyPath:
    @patch("app.ingestion.pipeline._ingest_to_lightrag")
    @patch("app.ingestion.pipeline.create_knowledge_item_with_relations")
    @patch("app.ingestion.pipeline.classify_text")
    @patch("app.ingestion.pipeline.find_items_by_fuzzy_title")
    @patch("app.ingestion.pipeline.find_item_by_source_url")
    @patch("app.ingestion.pipeline.fetch_source")
    def test_full_commit_flow(
        self, mock_fetch, mock_dedup_url, mock_dedup_fuzzy,
        mock_classify, mock_create, mock_rag,
    ):
        mock_fetch.return_value = _fetch_ok()
        mock_dedup_url.return_value = None
        mock_dedup_fuzzy.return_value = []
        mock_classify.return_value = _mappings()
        mock_create.return_value = {"title": "Test Paper"}

        result = ingest(_source(), MagicMock(), dry_run=False)

        assert result.status == "ingested"
        assert len(result.mappings) == 2
        mock_create.assert_called_once()
        mock_rag.assert_called_once()

    @patch("app.ingestion.pipeline.classify_text")
    @patch("app.ingestion.pipeline.find_items_by_fuzzy_title")
    @patch("app.ingestion.pipeline.find_item_by_source_url")
    @patch("app.ingestion.pipeline.fetch_source")
    def test_dry_run_does_not_persist(
        self, mock_fetch, mock_dedup_url, mock_dedup_fuzzy, mock_classify,
    ):
        mock_fetch.return_value = _fetch_ok()
        mock_dedup_url.return_value = None
        mock_dedup_fuzzy.return_value = []
        mock_classify.return_value = _mappings()

        result = ingest(_source(), MagicMock(), dry_run=True)

        assert result.status == "preview"
        assert len(result.mappings) == 2

    @patch("app.ingestion.pipeline._ingest_to_lightrag")
    @patch("app.ingestion.pipeline.create_knowledge_item_with_relations")
    @patch("app.ingestion.pipeline.classify_text")
    @patch("app.ingestion.pipeline.find_items_by_fuzzy_title")
    @patch("app.ingestion.pipeline.find_item_by_source_url")
    @patch("app.ingestion.pipeline.fetch_source")
    def test_skip_rag_flag(
        self, mock_fetch, mock_dedup_url, mock_dedup_fuzzy,
        mock_classify, mock_create, mock_rag,
    ):
        mock_fetch.return_value = _fetch_ok()
        mock_dedup_url.return_value = None
        mock_dedup_fuzzy.return_value = []
        mock_classify.return_value = _mappings()
        mock_create.return_value = {"title": "Test Paper"}

        result = ingest(_source(), MagicMock(), dry_run=False, skip_rag=True)

        assert result.status == "ingested"
        mock_rag.assert_not_called()


class TestPipelineDeduplication:
    @patch("app.ingestion.pipeline.find_item_by_source_url")
    @patch("app.ingestion.pipeline.fetch_source")
    def test_exact_url_duplicate_blocked(self, mock_fetch, mock_dedup_url):
        mock_fetch.return_value = _fetch_ok()
        mock_dedup_url.return_value = {"title": "Existing Paper"}

        result = ingest(_source(), MagicMock())

        assert result.status == "duplicate"
        assert result.existing == "Existing Paper"

    @patch("app.ingestion.pipeline.classify_text")
    @patch("app.ingestion.pipeline.find_items_by_fuzzy_title")
    @patch("app.ingestion.pipeline.find_item_by_source_url")
    @patch("app.ingestion.pipeline.fetch_source")
    def test_fuzzy_title_match_warns_but_proceeds(
        self, mock_fetch, mock_dedup_url, mock_dedup_fuzzy, mock_classify,
    ):
        mock_fetch.return_value = _fetch_ok()
        mock_dedup_url.return_value = None
        mock_dedup_fuzzy.return_value = [{"title": "Similar Paper"}]
        mock_classify.return_value = _mappings()

        result = ingest(_source(), MagicMock(), dry_run=True)

        # Should still proceed (fuzzy match is a warning, not a block)
        assert result.status == "preview"


class TestPipelineErrors:
    @patch("app.ingestion.pipeline.fetch_source")
    def test_fetch_failure(self, mock_fetch):
        mock_fetch.return_value = _fetch_failed()

        result = ingest(_source(), MagicMock())

        assert result.status == "fetch_failed"
        assert "HTTP 403" in result.error

    @patch("app.ingestion.pipeline.fetch_source")
    def test_pdf_not_supported_in_cli(self, mock_fetch):
        mock_fetch.return_value = _fetch_pdf()

        result = ingest(
            _source(url="https://example.com/paper.pdf", source_type="paper"),
            MagicMock(),
        )

        assert result.status == "engine_unavailable"
        assert "PDF" in result.error

    @patch("app.ingestion.pipeline.classify_text")
    @patch("app.ingestion.pipeline.find_items_by_fuzzy_title")
    @patch("app.ingestion.pipeline.find_item_by_source_url")
    @patch("app.ingestion.pipeline.fetch_source")
    def test_no_mappings_found(
        self, mock_fetch, mock_dedup_url, mock_dedup_fuzzy, mock_classify,
    ):
        mock_fetch.return_value = _fetch_ok()
        mock_dedup_url.return_value = None
        mock_dedup_fuzzy.return_value = []
        mock_classify.return_value = []  # No mappings

        result = ingest(_source(), MagicMock())

        assert result.status == "no_mappings_found"
        assert result.suggestion is not None

    @patch("app.ingestion.pipeline.scan_pii")
    @patch("app.ingestion.pipeline.fetch_source")
    def test_pii_scan_error_blocks(self, mock_fetch, mock_scan):
        mock_fetch.return_value = _fetch_ok()
        mock_scan.return_value = PIIReport(error="Scanner crashed")

        result = ingest(_source(), MagicMock())

        assert result.status == "pii_scan_failed"
        assert "Scanner crashed" in result.error


class TestLightRAGIngest:
    @patch("app.ingestion.pipeline._ingest_to_lightrag")
    @patch("app.ingestion.pipeline.create_knowledge_item_with_relations")
    @patch("app.ingestion.pipeline.classify_text")
    @patch("app.ingestion.pipeline.find_items_by_fuzzy_title")
    @patch("app.ingestion.pipeline.find_item_by_source_url")
    @patch("app.ingestion.pipeline.fetch_source")
    def test_lightrag_failure_does_not_block(
        self, mock_fetch, mock_dedup_url, mock_dedup_fuzzy,
        mock_classify, mock_create, mock_rag,
    ):
        """LightRAG failure should not prevent KnowledgeItem creation."""
        mock_fetch.return_value = _fetch_ok()
        mock_dedup_url.return_value = None
        mock_dedup_fuzzy.return_value = []
        mock_classify.return_value = _mappings()
        mock_create.return_value = {"title": "Test Paper"}
        mock_rag.side_effect = Exception("LightRAG connection failed")

        # Should not raise — LightRAG is non-fatal
        result = ingest(_source(), MagicMock(), dry_run=False)

        assert result.status == "ingested"
        mock_create.assert_called_once()
