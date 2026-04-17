"""Gemini-based NL summary generator for ingestion pipeline.

Produces a 2-3 sentence Dutch summary of a KnowledgeItem, tailored to the
BeeHaive audience. Runs after taxonomy classification and before persistence.
Returns None on any failure (non-fatal: the item still gets persisted, just
without a summary_nl attribute).

PII safety: callers must ensure text is PII-redacted before calling
generate_nl_summary(). This module does NOT perform PII checks.
"""

import logging
import os
import time

from google.genai import types

from app.ingestion.gemini_client import get_gemini_client

logger = logging.getLogger(__name__)

_SUMMARY_MODEL = os.getenv("GEMINI_SUMMARY_MODEL", "gemini-3.1-pro-preview")
_MAX_RETRIES = 2
_BACKOFF_BASE = 2.0
_TIMEOUT_SECONDS = 30
_MAX_INPUT_CHARS = 30_000

_SYSTEM_PROMPT = """Je schrijft Nederlandstalige samenvattingen voor de BeeHaive-kennisbank.

BeeHaive is een AI-framework met 7 Building Blocks en 7 EU Trustworthy AI Guardrails, \
gericht op consultants en teams die verantwoord met AI willen werken. Lezers zijn \
technisch onderlegd maar willen snel de kern snappen van een bron.

Schrijf een samenvatting van 2 tot 3 zinnen (maximaal ~55 woorden) die:
- de kern van de bron weergeeft in helder Nederlands
- benoemt waarom de bron relevant is voor een BeeHaive-lezer
- géén marketingtaal of superlatieven gebruikt
- vakjargon gebruikt waar het correcter is dan een Nederlandse vertaling \
(bijvoorbeeld: RAG, prompt engineering, agent, guardrail)

Geef ALLEEN de samenvatting terug als platte tekst. Geen titel, geen voorvoegsel, \
geen aanhalingstekens.
"""


def generate_nl_summary(text: str, title: str) -> str | None:
    """Generate a 2-3 sentence Dutch summary for a KnowledgeItem.

    Args:
        text: PII-redacted source text.
        title: The item title (kept in original language — do not translate).

    Returns:
        The NL summary as a stripped string, or None on failure.
    """
    if not text.strip():
        logger.warning("generate_nl_summary called with empty text")
        return None

    truncated = text[:_MAX_INPUT_CHARS]
    if len(text) > _MAX_INPUT_CHARS:
        logger.info(
            "Text truncated from %d to %d chars for summarization",
            len(text), _MAX_INPUT_CHARS,
        )

    user_prompt = f"Titel: {title}\n\n{truncated}"

    last_error: str | None = None
    for attempt in range(_MAX_RETRIES + 1):
        try:
            client = get_gemini_client()
            response = client.models.generate_content(
                model=_SUMMARY_MODEL,
                contents=user_prompt,
                config=types.GenerateContentConfig(
                    system_instruction=_SYSTEM_PROMPT,
                    temperature=0.3,
                    http_options=types.HttpOptions(timeout=_TIMEOUT_SECONDS * 1000),
                ),
            )

            if not response.text:
                logger.warning(
                    "Gemini returned empty response (content filter?) for '%s'",
                    title,
                )
                return None

            summary = response.text.strip()
            # Strip surrounding quotes the model sometimes still adds
            if len(summary) >= 2 and summary[0] in {'"', "'"} and summary[-1] == summary[0]:
                summary = summary[1:-1].strip()

            if not summary:
                return None

            logger.info("Summarized '%s' (%d chars)", title or "(untitled)", len(summary))
            return summary

        except Exception as e:
            last_error = str(e)
            if attempt < _MAX_RETRIES:
                backoff = _BACKOFF_BASE ** (attempt + 1)
                logger.warning(
                    "Gemini summarize attempt %d failed: %s. Retrying in %.0fs",
                    attempt + 1, last_error, backoff,
                )
                time.sleep(backoff)
            else:
                logger.error(
                    "Gemini summarize failed after %d attempts: %s",
                    _MAX_RETRIES + 1, last_error,
                )

    return None
