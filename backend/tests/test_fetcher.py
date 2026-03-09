"""Unit tests for document fetcher.

Tests SSRF prevention, URL validation, caching, and fetch logic.
HTTP calls are mocked to avoid external dependencies.
"""

from unittest.mock import patch, MagicMock

import pytest

from app.ingestion.fetcher import _validate_url, fetch_source


# --- SSRF prevention ---


def test_reject_http_url():
    with pytest.raises(ValueError, match="Only HTTPS"):
        _validate_url("http://example.com")


def test_accept_https_url():
    """HTTPS URLs with public IPs should pass validation."""
    # Mock DNS to return a public IP
    with patch("socket.getaddrinfo") as mock_dns:
        mock_dns.return_value = [(None, None, None, None, ("93.184.216.34", 0))]
        _validate_url("https://example.com")  # Should not raise


def test_reject_private_ip_10():
    with patch("socket.getaddrinfo") as mock_dns:
        mock_dns.return_value = [(None, None, None, None, ("10.0.0.1", 0))]
        with pytest.raises(ValueError, match="private IP"):
            _validate_url("https://internal.example.com")


def test_reject_private_ip_172():
    with patch("socket.getaddrinfo") as mock_dns:
        mock_dns.return_value = [(None, None, None, None, ("172.16.0.1", 0))]
        with pytest.raises(ValueError, match="private IP"):
            _validate_url("https://internal.example.com")


def test_reject_private_ip_192():
    with patch("socket.getaddrinfo") as mock_dns:
        mock_dns.return_value = [(None, None, None, None, ("192.168.1.1", 0))]
        with pytest.raises(ValueError, match="private IP"):
            _validate_url("https://internal.example.com")


def test_reject_localhost_ip():
    with patch("socket.getaddrinfo") as mock_dns:
        mock_dns.return_value = [(None, None, None, None, ("127.0.0.1", 0))]
        with pytest.raises(ValueError, match="private IP"):
            _validate_url("https://localhost")


def test_reject_link_local():
    with patch("socket.getaddrinfo") as mock_dns:
        mock_dns.return_value = [(None, None, None, None, ("169.254.1.1", 0))]
        with pytest.raises(ValueError, match="private IP"):
            _validate_url("https://metadata.example.com")


def test_allow_localhost_in_dev():
    """Dev mode should allow http://localhost."""
    _validate_url("http://localhost:8000", allow_localhost=True)  # Should not raise


def test_reject_no_hostname():
    with pytest.raises(ValueError, match="no hostname"):
        _validate_url("https://")


def test_reject_dns_failure():
    with patch("socket.getaddrinfo", side_effect=OSError("DNS failed")):
        with pytest.raises(ValueError, match="DNS resolution failed"):
            _validate_url("https://nonexistent.example.com")


# --- fetch_source routing ---


def test_fetch_source_paper_returns_stub():
    """Papers need PDF processing via RAG-Anything, so fetch_source returns a stub."""
    result = fetch_source("https://arxiv.org/abs/2401.12345", "paper")
    assert result.fetch_status == "requires_pdf_processing"
    assert result.text == ""


def test_fetch_source_html_types(monkeypatch):
    """Non-paper types should route through HTML fetching."""
    mock_result = MagicMock()
    monkeypatch.setattr("app.ingestion.fetcher.fetch_html", lambda url: mock_result)
    for source_type in ["regulation", "guideline", "best_practice"]:
        result = fetch_source("https://example.com/page", source_type)
        assert result is mock_result
