"""Unit tests for PII scanner.

Tests email and phone detection, redaction, and fail-closed behaviour.
Minimum 10 testcases per Definition of Done (PLAN-007).
"""

import pytest

from app.ingestion.pii import scan_pii, redact_pii
from app.models.ingestion import PIIReport


# --- Email detection ---


def test_scan_standard_email():
    report = scan_pii("Contact us at info@example.com for details.")
    assert len(report.findings) == 1
    assert report.findings[0].pii_type == "email"
    assert report.findings[0].start == 14
    assert report.findings[0].end == 30


def test_scan_academic_email():
    report = scan_pii("Author: j.doe@university.ac.uk")
    assert len(report.findings) == 1
    assert report.findings[0].pii_type == "email"


def test_scan_multiple_emails():
    text = "Send to alice@example.org or bob@test.nl"
    report = scan_pii(text)
    emails = [f for f in report.findings if f.pii_type == "email"]
    assert len(emails) == 2


def test_scan_email_with_plus():
    report = scan_pii("user+tag@gmail.com")
    assert len(report.findings) == 1
    assert report.findings[0].pii_type == "email"


# --- Phone detection ---


def test_scan_dutch_mobile():
    report = scan_pii("Bel 06-12345678 voor info.")
    phones = [f for f in report.findings if f.pii_type == "phone"]
    assert len(phones) == 1


def test_scan_international_phone():
    report = scan_pii("Call +31 6 12345678")
    phones = [f for f in report.findings if f.pii_type == "phone"]
    assert len(phones) == 1


def test_scan_us_phone():
    report = scan_pii("Phone: +1-555-123-4567")
    phones = [f for f in report.findings if f.pii_type == "phone"]
    assert len(phones) == 1


def test_scan_phone_with_area_code():
    report = scan_pii("Kantoor: (020) 1234567")
    phones = [f for f in report.findings if f.pii_type == "phone"]
    assert len(phones) == 1


# --- No PII ---


def test_scan_no_pii():
    text = "The EU AI Act establishes a risk-based framework for artificial intelligence."
    report = scan_pii(text)
    assert not report.has_pii
    assert len(report.findings) == 0
    assert report.error is None


def test_scan_empty_text():
    report = scan_pii("")
    assert not report.has_pii
    assert report.error is None


# --- Mixed PII ---


def test_scan_mixed_pii():
    text = "Contact: admin@beehaive.org, phone +31 20 1234567"
    report = scan_pii(text)
    types = {f.pii_type for f in report.findings}
    assert "email" in types
    assert "phone" in types


# --- Redaction ---


def test_redact_email():
    text = "Contact info@example.com for details."
    report = scan_pii(text)
    redacted = redact_pii(text, report)
    assert "info@example.com" not in redacted
    assert "[REDACTED_EMAIL]" in redacted
    assert "for details." in redacted


def test_redact_phone():
    text = "Call 06-12345678 now."
    report = scan_pii(text)
    redacted = redact_pii(text, report)
    assert "06-12345678" not in redacted
    assert "[REDACTED_PHONE]" in redacted


def test_redact_preserves_clean_text():
    text = "No PII here, just academic content about AI governance."
    report = scan_pii(text)
    redacted = redact_pii(text, report)
    assert redacted == text


def test_redact_multiple_findings():
    text = "Email: a@b.com, phone: 06-12345678, email: c@d.nl"
    report = scan_pii(text)
    redacted = redact_pii(text, report)
    assert "a@b.com" not in redacted
    assert "c@d.nl" not in redacted
    assert "06-12345678" not in redacted


# --- Fail-closed ---


def test_redact_with_error_raises():
    """Redaction must refuse to proceed if the scan had an error."""
    error_report = PIIReport(error="Scanner crashed")
    with pytest.raises(ValueError, match="Cannot redact"):
        redact_pii("some text", error_report)


# --- Position tracking ---


def test_findings_sorted_by_position():
    text = "End: x@y.nl. Start: a@b.com."
    report = scan_pii(text)
    positions = [f.start for f in report.findings]
    assert positions == sorted(positions)
