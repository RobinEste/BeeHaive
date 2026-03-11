"""Unit tests for the Gemini taxonomy mapper.

All tests use mocked Gemini responses — no API key needed.
"""

from unittest.mock import MagicMock, patch

import pytest

from app.ingestion.llm import (
    BUILDING_BLOCKS,
    CONFIDENCE_THRESHOLD,
    GUARDRAILS,
    _validate_mapping,
    classify_text,
)


# --- _validate_mapping tests ---


class TestValidateMapping:
    def test_valid_building_block(self):
        result = _validate_mapping(
            {"entity_type": "BuildingBlock", "matched_name": "Knowledge", "confidence": 0.9}
        )
        assert result is not None
        assert result.entity_type == "BuildingBlock"
        assert result.matched_name == "Knowledge"
        assert result.match_method == "llm"

    def test_valid_guardrail(self):
        result = _validate_mapping(
            {"entity_type": "Guardrail", "matched_name": "Privacy", "confidence": 0.85}
        )
        assert result is not None
        assert result.entity_type == "Guardrail"
        assert result.matched_name == "Privacy"

    def test_valid_topic(self):
        result = _validate_mapping(
            {"entity_type": "Topic", "matched_name": "RAG", "confidence": 0.8}
        )
        assert result is not None
        assert result.entity_type == "Topic"
        assert result.matched_name == "RAG"

    def test_valid_author(self):
        result = _validate_mapping(
            {"entity_type": "Author", "matched_name": "John Doe", "confidence": 0.95}
        )
        assert result is not None
        assert result.entity_type == "Author"

    def test_below_confidence_threshold(self):
        result = _validate_mapping(
            {"entity_type": "Topic", "matched_name": "RAG", "confidence": 0.5}
        )
        assert result is None

    def test_exactly_at_threshold(self):
        result = _validate_mapping(
            {"entity_type": "Topic", "matched_name": "RAG", "confidence": CONFIDENCE_THRESHOLD}
        )
        assert result is not None

    def test_unknown_building_block(self):
        result = _validate_mapping(
            {"entity_type": "BuildingBlock", "matched_name": "NonExistent", "confidence": 0.9}
        )
        assert result is None

    def test_unknown_guardrail(self):
        result = _validate_mapping(
            {"entity_type": "Guardrail", "matched_name": "NonExistent", "confidence": 0.9}
        )
        assert result is None

    def test_unknown_entity_type(self):
        result = _validate_mapping(
            {"entity_type": "Unknown", "matched_name": "Foo", "confidence": 0.9}
        )
        assert result is None

    def test_empty_matched_name(self):
        result = _validate_mapping(
            {"entity_type": "Topic", "matched_name": "", "confidence": 0.9}
        )
        assert result is None

    def test_whitespace_matched_name(self):
        result = _validate_mapping(
            {"entity_type": "Topic", "matched_name": "   ", "confidence": 0.9}
        )
        assert result is None


# --- classify_text tests ---


def _make_mock_response(raw_mappings: list[dict]):
    """Create a mock Gemini response with parsed output."""
    response = MagicMock()
    response.parsed = [MagicMock(**m, model_dump=lambda m=m: m) for m in raw_mappings]
    return response


class TestClassifyText:
    @patch("app.ingestion.llm._get_client")
    def test_successful_classification(self, mock_get_client):
        raw = [
            {"entity_type": "BuildingBlock", "matched_name": "Knowledge", "confidence": 0.9},
            {"entity_type": "Guardrail", "matched_name": "Transparency", "confidence": 0.85},
            {"entity_type": "Topic", "matched_name": "AI Ethics", "confidence": 0.8},
            {"entity_type": "Author", "matched_name": "Jane Smith", "confidence": 0.95},
        ]
        mock_client = MagicMock()
        mock_client.models.generate_content.return_value = _make_mock_response(raw)
        mock_get_client.return_value = mock_client

        result = classify_text("Some text about AI", "paper", "Test Paper")

        assert len(result) == 4
        assert result[0].matched_name == "Knowledge"
        assert result[1].matched_name == "Transparency"
        assert result[2].matched_name == "AI Ethics"
        assert result[3].matched_name == "Jane Smith"
        assert all(m.match_method == "llm" for m in result)

    @patch("app.ingestion.llm._get_client")
    def test_filters_low_confidence(self, mock_get_client):
        raw = [
            {"entity_type": "BuildingBlock", "matched_name": "Knowledge", "confidence": 0.9},
            {"entity_type": "Topic", "matched_name": "Vague", "confidence": 0.3},
        ]
        mock_client = MagicMock()
        mock_client.models.generate_content.return_value = _make_mock_response(raw)
        mock_get_client.return_value = mock_client

        result = classify_text("Some text", "paper")

        assert len(result) == 1
        assert result[0].matched_name == "Knowledge"

    @patch("app.ingestion.llm._get_client")
    def test_filters_invalid_building_block(self, mock_get_client):
        raw = [
            {"entity_type": "BuildingBlock", "matched_name": "FakeBlock", "confidence": 0.9},
            {"entity_type": "Topic", "matched_name": "Valid Topic", "confidence": 0.8},
        ]
        mock_client = MagicMock()
        mock_client.models.generate_content.return_value = _make_mock_response(raw)
        mock_get_client.return_value = mock_client

        result = classify_text("Some text", "regulation")

        assert len(result) == 1
        assert result[0].matched_name == "Valid Topic"

    @patch("app.ingestion.llm._get_client")
    def test_empty_text_returns_empty(self, mock_get_client):
        result = classify_text("", "paper")
        assert result == []
        mock_get_client.assert_not_called()

    @patch("app.ingestion.llm._get_client")
    def test_whitespace_text_returns_empty(self, mock_get_client):
        result = classify_text("   ", "paper")
        assert result == []

    @patch("app.ingestion.llm._get_client")
    def test_api_failure_returns_empty(self, mock_get_client):
        mock_client = MagicMock()
        mock_client.models.generate_content.side_effect = Exception("API down")
        mock_get_client.return_value = mock_client

        result = classify_text("Some text", "paper")

        assert result == []
        # Should have retried MAX_RETRIES + 1 times
        assert mock_client.models.generate_content.call_count == 3

    @patch("app.ingestion.llm._get_client")
    def test_none_parsed_returns_empty(self, mock_get_client):
        mock_client = MagicMock()
        response = MagicMock()
        response.parsed = None
        mock_client.models.generate_content.return_value = response
        mock_get_client.return_value = mock_client

        result = classify_text("Some text", "paper")

        assert result == []

    @patch("app.ingestion.llm._get_client")
    def test_empty_parsed_returns_empty(self, mock_get_client):
        mock_client = MagicMock()
        mock_client.models.generate_content.return_value = _make_mock_response([])
        mock_get_client.return_value = mock_client

        result = classify_text("Some text", "paper")

        assert result == []

    @patch("app.ingestion.llm._get_client")
    def test_all_building_blocks_accepted(self, mock_get_client):
        """Every known BuildingBlock name should be accepted."""
        for name in BUILDING_BLOCKS:
            raw = [{"entity_type": "BuildingBlock", "matched_name": name, "confidence": 0.9}]
            mock_client = MagicMock()
            mock_client.models.generate_content.return_value = _make_mock_response(raw)
            mock_get_client.return_value = mock_client

            result = classify_text("text", "paper")
            assert len(result) == 1, f"BuildingBlock '{name}' should be accepted"

    @patch("app.ingestion.llm._get_client")
    def test_all_guardrails_accepted(self, mock_get_client):
        """Every known Guardrail name should be accepted."""
        for name in GUARDRAILS:
            raw = [{"entity_type": "Guardrail", "matched_name": name, "confidence": 0.9}]
            mock_client = MagicMock()
            mock_client.models.generate_content.return_value = _make_mock_response(raw)
            mock_get_client.return_value = mock_client

            result = classify_text("text", "paper")
            assert len(result) == 1, f"Guardrail '{name}' should be accepted"

    def test_missing_api_key_raises(self):
        with patch.dict("os.environ", {}, clear=True):
            with pytest.raises(ValueError, match="GEMINI_API_KEY"):
                classify_text("text", "paper")

    @patch("app.ingestion.llm.time.sleep")
    @patch("app.ingestion.llm._get_client")
    def test_retry_with_backoff(self, mock_get_client, mock_sleep):
        mock_client = MagicMock()
        mock_client.models.generate_content.side_effect = [
            Exception("429 rate limit"),
            _make_mock_response(
                [{"entity_type": "Topic", "matched_name": "AI", "confidence": 0.9}]
            ),
        ]
        mock_get_client.return_value = mock_client

        result = classify_text("text", "paper")

        assert len(result) == 1
        mock_sleep.assert_called_once_with(2)  # 2^(0+1)
