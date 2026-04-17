"""Unit tests for the Gemini NL summarizer."""

from unittest.mock import MagicMock, patch

from app.ingestion.summarizer import generate_nl_summary


def _mock_response(text: str) -> MagicMock:
    response = MagicMock()
    response.text = text
    return response


class TestGenerateNlSummary:
    @patch("app.ingestion.summarizer.get_gemini_client")
    def test_basic_summary(self, mock_get_client):
        mock_client = MagicMock()
        mock_client.models.generate_content.return_value = _mock_response(
            "Compacte Nederlandstalige samenvatting van de bron."
        )
        mock_get_client.return_value = mock_client

        result = generate_nl_summary(text="Source text", title="Paper Title")

        assert result == "Compacte Nederlandstalige samenvatting van de bron."

    @patch("app.ingestion.summarizer.get_gemini_client")
    def test_strips_surrounding_quotes(self, mock_get_client):
        mock_client = MagicMock()
        mock_client.models.generate_content.return_value = _mock_response(
            '"Een samenvatting tussen dubbele aanhalingstekens."'
        )
        mock_get_client.return_value = mock_client

        result = generate_nl_summary(text="Source", title="Title")

        assert result == "Een samenvatting tussen dubbele aanhalingstekens."

    @patch("app.ingestion.summarizer.get_gemini_client")
    def test_empty_text_returns_none(self, mock_get_client):
        result = generate_nl_summary(text="", title="Title")

        assert result is None
        mock_get_client.assert_not_called()

    @patch("app.ingestion.summarizer.get_gemini_client")
    def test_whitespace_only_text_returns_none(self, mock_get_client):
        result = generate_nl_summary(text="   \n  ", title="Title")

        assert result is None
        mock_get_client.assert_not_called()

    @patch("app.ingestion.summarizer.get_gemini_client")
    def test_empty_response_returns_none(self, mock_get_client):
        mock_client = MagicMock()
        mock_client.models.generate_content.return_value = _mock_response("")
        mock_get_client.return_value = mock_client

        result = generate_nl_summary(text="Source", title="Title")

        assert result is None

    @patch("app.ingestion.summarizer.time.sleep")
    @patch("app.ingestion.summarizer.get_gemini_client")
    def test_api_error_returns_none_after_retries(self, mock_get_client, mock_sleep):
        mock_client = MagicMock()
        mock_client.models.generate_content.side_effect = RuntimeError("API outage")
        mock_get_client.return_value = mock_client

        result = generate_nl_summary(text="Source", title="Title")

        assert result is None
        assert mock_client.models.generate_content.call_count == 3
