"""Unit tests for Gemini taxonomy mapper.

Tests classify_text() with mocked Gemini responses.
Covers: structured output parsing, confidence filtering, validation
of BuildingBlock/Guardrail names, fallback on API errors.
"""

import json
from unittest.mock import MagicMock, patch

from app.ingestion.llm import classify_text, _validate_mapping


# --- Helpers ---


def _mock_gemini_response(mappings: list[dict]) -> MagicMock:
    """Create a mock Gemini response with structured output."""
    response = MagicMock()
    response.text = json.dumps({"mappings": mappings})
    return response


def _bb_mapping(name="Knowledge", confidence=0.9):
    return {
        "entity_text": "knowledge management",
        "entity_type": "BuildingBlock",
        "matched_name": name,
        "confidence": confidence,
    }


def _gr_mapping(name="Privacy", confidence=0.85):
    return {
        "entity_text": "data protection",
        "entity_type": "Guardrail",
        "matched_name": name,
        "confidence": confidence,
    }


def _topic_mapping(name="RAG", confidence=0.8):
    return {
        "entity_text": "retrieval augmented generation",
        "entity_type": "Topic",
        "matched_name": name,
        "confidence": confidence,
    }


def _author_mapping(name="European Commission", confidence=0.95):
    return {
        "entity_text": "European Commission",
        "entity_type": "Author",
        "matched_name": name,
        "confidence": confidence,
    }


# --- _validate_mapping tests ---


class TestValidateMapping:
    def test_valid_building_block(self):
        result = _validate_mapping(_bb_mapping())
        assert result is not None
        assert result.entity_type == "BuildingBlock"
        assert result.matched_name == "Knowledge"
        assert result.match_method == "llm"

    def test_valid_guardrail(self):
        result = _validate_mapping(_gr_mapping())
        assert result is not None
        assert result.entity_type == "Guardrail"
        assert result.matched_name == "Privacy"

    def test_valid_topic(self):
        result = _validate_mapping(_topic_mapping())
        assert result is not None
        assert result.entity_type == "Topic"

    def test_valid_author(self):
        result = _validate_mapping(_author_mapping())
        assert result is not None
        assert result.entity_type == "Author"

    def test_unknown_building_block_rejected(self):
        result = _validate_mapping(_bb_mapping(name="Nonexistent Block"))
        assert result is None

    def test_unknown_guardrail_rejected(self):
        result = _validate_mapping(_gr_mapping(name="Nonexistent Guardrail"))
        assert result is None

    def test_unknown_entity_type_rejected(self):
        result = _validate_mapping({
            "entity_text": "test",
            "entity_type": "UnknownType",
            "matched_name": "test",
            "confidence": 0.9,
        })
        assert result is None

    def test_confidence_clamped_to_range(self):
        result = _validate_mapping(_bb_mapping(confidence=1.5))
        assert result is not None
        assert result.confidence == 1.0

        result = _validate_mapping(_bb_mapping(confidence=-0.5))
        assert result is not None
        assert result.confidence == 0.0

    def test_all_building_block_names_accepted(self):
        names = [
            "Knowledge", "Client Blueprint", "Dynamic Context",
            "Prompt Design", "Tool Integration", "Model Engines",
            "Evaluation Loop",
        ]
        for name in names:
            result = _validate_mapping(_bb_mapping(name=name))
            assert result is not None, f"BuildingBlock '{name}' should be valid"

    def test_all_guardrail_names_accepted(self):
        names = [
            "Human Agency", "Robustness", "Privacy", "Fairness",
            "Transparency", "Well-being", "Accountability",
        ]
        for name in names:
            result = _validate_mapping(_gr_mapping(name=name))
            assert result is not None, f"Guardrail '{name}' should be valid"


# --- classify_text tests ---


class TestClassifyText:
    @patch("app.ingestion.llm._get_client")
    def test_basic_classification(self, mock_get_client):
        mock_client = MagicMock()
        mock_get_client.return_value = mock_client
        mock_client.models.generate_content.return_value = _mock_gemini_response([
            _bb_mapping(),
            _gr_mapping(),
            _topic_mapping(),
            _author_mapping(),
        ])

        result = classify_text("Some AI text about knowledge", "paper", "Test Paper")

        assert len(result) == 4
        assert mock_client.models.generate_content.call_count == 1
        types_found = {m.entity_type for m in result}
        assert types_found == {"BuildingBlock", "Guardrail", "Topic", "Author"}

    @patch("app.ingestion.llm._get_client")
    def test_confidence_threshold_filtering(self, mock_get_client):
        mock_client = MagicMock()
        mock_get_client.return_value = mock_client
        mock_client.models.generate_content.return_value = _mock_gemini_response([
            _bb_mapping(confidence=0.9),   # above threshold
            _gr_mapping(confidence=0.5),   # below threshold
            _topic_mapping(confidence=0.3),  # below threshold
        ])

        result = classify_text("Some text", "regulation", "Test")

        assert len(result) == 1
        assert result[0].entity_type == "BuildingBlock"

    @patch("app.ingestion.llm._get_client")
    def test_custom_confidence_threshold(self, mock_get_client):
        mock_client = MagicMock()
        mock_get_client.return_value = mock_client
        mock_client.models.generate_content.return_value = _mock_gemini_response([
            _bb_mapping(confidence=0.5),
            _gr_mapping(confidence=0.3),
        ])

        result = classify_text(
            "Some text", "regulation", "Test", confidence_threshold=0.4
        )

        assert len(result) == 1
        assert result[0].confidence == 0.5

    @patch("app.ingestion.llm._get_client")
    def test_invalid_building_block_filtered_out(self, mock_get_client):
        mock_client = MagicMock()
        mock_get_client.return_value = mock_client
        mock_client.models.generate_content.return_value = _mock_gemini_response([
            _bb_mapping(name="Hallucinated Block"),
            _gr_mapping(),  # valid
        ])

        result = classify_text("Some text", "guideline", "Test")

        assert len(result) == 1
        assert result[0].entity_type == "Guardrail"

    @patch("app.ingestion.llm._get_client")
    def test_empty_text_returns_empty(self, mock_get_client):
        result = classify_text("", "paper", "Test")
        assert result == []
        mock_get_client.assert_not_called()

    @patch("app.ingestion.llm._get_client")
    def test_whitespace_only_text_returns_empty(self, mock_get_client):
        result = classify_text("   \n\t  ", "paper", "Test")
        assert result == []

    @patch("app.ingestion.llm.time.sleep")  # don't actually sleep in tests
    @patch("app.ingestion.llm._get_client")
    def test_api_error_returns_empty_after_retries(self, mock_get_client, mock_sleep):
        mock_client = MagicMock()
        mock_get_client.return_value = mock_client
        mock_client.models.generate_content.side_effect = Exception("API error")

        result = classify_text("Some text", "paper", "Test")

        assert result == []
        # 1 initial + 2 retries = 3 calls
        assert mock_client.models.generate_content.call_count == 3

    @patch("app.ingestion.llm._get_client")
    def test_empty_mappings_from_api(self, mock_get_client):
        mock_client = MagicMock()
        mock_get_client.return_value = mock_client
        mock_client.models.generate_content.return_value = _mock_gemini_response([])

        result = classify_text("Some text", "best_practice", "Test")

        assert result == []

    @patch("app.ingestion.llm._get_client")
    def test_all_match_methods_are_llm(self, mock_get_client):
        mock_client = MagicMock()
        mock_get_client.return_value = mock_client
        mock_client.models.generate_content.return_value = _mock_gemini_response([
            _bb_mapping(),
            _topic_mapping(),
        ])

        result = classify_text("Some text", "paper", "Test")

        for mapping in result:
            assert mapping.match_method == "llm"

    @patch("app.ingestion.llm._get_client")
    def test_topics_and_authors_accept_any_name(self, mock_get_client):
        """Topics and Authors are free-form — any name should be accepted."""
        mock_client = MagicMock()
        mock_get_client.return_value = mock_client
        mock_client.models.generate_content.return_value = _mock_gemini_response([
            _topic_mapping(name="Completely Novel Topic"),
            _author_mapping(name="Unknown Author XYZ"),
        ])

        result = classify_text("Some text", "paper", "Test")

        assert len(result) == 2
        assert result[0].matched_name == "Completely Novel Topic"
        assert result[1].matched_name == "Unknown Author XYZ"

    @patch("app.ingestion.llm._get_client")
    def test_duplicate_mappings_deduplicated(self, mock_get_client):
        """Multiple mappings for same (entity_type, matched_name) keep highest confidence."""
        mock_client = MagicMock()
        mock_get_client.return_value = mock_client
        mock_client.models.generate_content.return_value = _mock_gemini_response([
            _bb_mapping(name="Knowledge", confidence=0.85),
            _bb_mapping(name="Knowledge", confidence=0.95),
            _bb_mapping(name="Knowledge", confidence=0.90),
            _bb_mapping(name="Model Engines", confidence=0.80),
        ])

        result = classify_text("Some text", "paper", "Test")

        # Knowledge should appear once with highest confidence (0.95)
        knowledge = [m for m in result if m.matched_name == "Knowledge"]
        assert len(knowledge) == 1
        assert knowledge[0].confidence == 0.95

        # Model Engines should also appear once
        engines = [m for m in result if m.matched_name == "Model Engines"]
        assert len(engines) == 1

        assert len(result) == 2
