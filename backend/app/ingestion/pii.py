"""PII scanner for ingestion pipeline.

Detects contact information (email addresses, phone numbers) in text.
Author names are NOT flagged — they fall under AVG Art. 6(1)(f) for
publicly available academic publications. See PLAN-007 for rationale.

Fail-closed: any scanner error blocks ingestion.
"""

import re

from app.models.ingestion import PIIFinding, PIIReport

# Email pattern — covers standard and academic formats
# e.g. user@example.com, j.doe@university.ac.uk
_EMAIL_PATTERN = re.compile(
    r"[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}",
)

# Phone pattern — international and NL formats
# e.g. +31 6 12345678, +1-555-123-4567, 06-12345678, (020) 1234567
_PHONE_PATTERN = re.compile(
    r"(?:"
    r"\+\d{1,3}[\s\-]?\(?\d{1,4}\)?[\s\-]?\d{3,4}[\s\-]?\d{3,4}"  # international
    r"|"
    r"\b\(?0\d{1,3}\)?[\s\-]?\d{3,4}[\s\-]?\d{3,4}\b"  # local with area code (0-prefix, NL)
    r"|"
    r"\b0\d[\s\-]?\d{8}\b"  # NL mobile (06-12345678)
    r")",
)


def scan_pii(text: str) -> PIIReport:
    """Scan text for PII (email addresses and phone numbers).

    Returns a PIIReport. On any internal error, the report's error field
    is set — callers must treat this as a block signal (fail-closed).
    """
    try:
        findings: list[PIIFinding] = []

        for match in _EMAIL_PATTERN.finditer(text):
            findings.append(
                PIIFinding(
                    pii_type="email",
                    start=match.start(),
                    end=match.end(),
                )
            )

        for match in _PHONE_PATTERN.finditer(text):
            findings.append(
                PIIFinding(
                    pii_type="phone",
                    start=match.start(),
                    end=match.end(),
                )
            )

        # Sort by position for consistent redaction order
        findings.sort(key=lambda f: f.start)

        # Remove overlapping findings (keep the longest match)
        filtered: list[PIIFinding] = []
        for f in findings:
            if filtered and f.start < filtered[-1].end:
                if (f.end - f.start) > (filtered[-1].end - filtered[-1].start):
                    filtered[-1] = f
            else:
                filtered.append(f)

        return PIIReport(findings=filtered)

    except Exception as e:
        return PIIReport(error=f"PII scan failed: {e}")


def redact_pii(text: str, report: PIIReport) -> str:
    """Replace detected PII with redaction markers.

    Processes findings in reverse order to preserve string positions.
    Always returns a new string object (never the original).
    """
    if report.error:
        raise ValueError(f"Cannot redact: PII scan had error: {report.error}")

    # Always create a new string object, even if no findings
    result = text[:]

    if not report.findings:
        return result

    # Redact in reverse order so positions stay valid
    for finding in reversed(report.findings):
        marker = f"[REDACTED_{finding.pii_type.upper()}]"
        result = result[:finding.start] + marker + result[finding.end:]

    return result
