"""Gemini-based taxonomy classifier for ingestion pipeline.

Classifies text into the BeeHaive taxonomy (BuildingBlocks, Guardrails,
Topics, Authors) using Gemini 2.5 Flash with structured output.

Uses the google-genai SDK directly (not OpenAI-compatible) because native
Gemini structured output with response_schema gives more reliable parsing
than the OpenAI compatibility layer.

PII safety: callers must ensure text is PII-redacted before calling
classify_text(). This module does NOT perform PII checks.
"""

import logging
import os
import time
from typing import Any

from google import genai
from google.genai import types

from app.models.ingestion import EntityType, SourceType, TaxonomyMapping

logger = logging.getLogger(__name__)

# Gemini client — initialised lazily
_client: genai.Client | None = None

# Model for classification
_CLASSIFY_MODEL = os.getenv("GEMINI_CLASSIFY_MODEL", "gemini-2.5-flash")

# Confidence threshold — mappings below this are logged but not returned
_CONFIDENCE_THRESHOLD = 0.7

# Retry config
_MAX_RETRIES = 2
_BACKOFF_BASE = 2.0
_TIMEOUT_SECONDS = 30

# The BeeHaive taxonomy — must match seed.py exactly
_BUILDING_BLOCKS = {
    "Knowledge": "Het fundament: kennisbronnen, documenten, data die het AI-systeem voedt.",
    "Client Blueprint": "Klantprofiel en context — wie is de gebruiker, wat is het doel.",
    "Dynamic Context": "Real-time context: sessie-informatie, recente interacties, omgevingsvariabelen.",
    "Prompt Design": "Prompt engineering: instructies, templates, few-shot examples.",
    "Tool Integration": "Externe tools en API's die het AI-systeem kan aanroepen.",
    "Model Engines": "De AI-modellen zelf: selectie, configuratie, fine-tuning.",
    "Evaluation Loop": "Evaluatie en feedback: kwaliteitsmetrieken, menselijke feedback, continue verbetering.",
}

_GUARDRAILS = {
    "Human Agency": "Menselijke controle en oversight over AI-beslissingen (EU: Human agency & oversight).",
    "Robustness": "Technische robuustheid, veiligheid en betrouwbaarheid (EU: Technical robustness & safety).",
    "Privacy": "Privacy en datagovernance, AVG-compliance (EU: Privacy & data governance).",
    "Fairness": "Diversiteit, non-discriminatie en eerlijkheid (EU: Diversity, non-discrimination & fairness).",
    "Transparency": "Transparantie, uitlegbaarheid en traceerbaarheid (EU: Transparency).",
    "Well-being": "Maatschappelijk en ecologisch welzijn (EU: Societal & environmental well-being).",
    "Accountability": "Verantwoording, auditability en governance (EU: Accountability).",
}

_SYSTEM_PROMPT = """Je bent een taxonomie-classifier voor het BeeHaive AI knowledge framework.

Je taak: classificeer de gegeven tekst naar de BeeHaive-taxonomie.

## Building Blocks (7 stuks)
{building_blocks}

## Guardrails (7 stuks — gebaseerd op EU Trustworthy AI)
{guardrails}

## Regels
1. Match BuildingBlocks en Guardrails ALLEEN op de exacte namen hierboven.
2. Extraheer Topics als korte termen (1-3 woorden, Engels). Max 5 topics.
3. Extraheer Authors (organisaties of personen). Gebruik de naam zoals in de tekst.
4. Geef per mapping een confidence score (0.0-1.0).
5. Wees selectief: alleen mappings die duidelijk uit de tekst volgen.
6. Een tekst kan meerdere BuildingBlocks en Guardrails raken.
""".format(
    building_blocks="\n".join(
        f"- **{name}**: {desc}" for name, desc in _BUILDING_BLOCKS.items()
    ),
    guardrails="\n".join(
        f"- **{name}**: {desc}" for name, desc in _GUARDRAILS.items()
    ),
)

# Structured output schema for Gemini
_RESPONSE_SCHEMA = types.Schema(
    type=types.Type.OBJECT,
    properties={
        "mappings": types.Schema(
            type=types.Type.ARRAY,
            items=types.Schema(
                type=types.Type.OBJECT,
                properties={
                    "entity_text": types.Schema(
                        type=types.Type.STRING,
                        description="The text fragment that triggered this mapping",
                    ),
                    "entity_type": types.Schema(
                        type=types.Type.STRING,
                        enum=["BuildingBlock", "Guardrail", "Topic", "Author"],
                        description="The taxonomy category",
                    ),
                    "matched_name": types.Schema(
                        type=types.Type.STRING,
                        description="The canonical name in the BeeHaive taxonomy",
                    ),
                    "confidence": types.Schema(
                        type=types.Type.NUMBER,
                        description="Confidence score between 0.0 and 1.0",
                    ),
                },
                required=["entity_text", "entity_type", "matched_name", "confidence"],
            ),
        ),
    },
    required=["mappings"],
)


def _get_client() -> genai.Client:
    """Get or create the Gemini client (lazy init)."""
    global _client
    if _client is None:
        api_key = os.getenv("GEMINI_API_KEY", "")
        if not api_key:
            raise ValueError(
                "GEMINI_API_KEY is not set. "
                "Get a key at https://aistudio.google.com/apikey"
            )
        _client = genai.Client(api_key=api_key)
    return _client


def _validate_mapping(raw: dict[str, Any]) -> TaxonomyMapping | None:
    """Validate and convert a raw mapping dict to a TaxonomyMapping.

    Returns None if the mapping is invalid (wrong entity_type, unknown
    BuildingBlock/Guardrail name, etc.).
    """
    entity_type = raw.get("entity_type", "")
    matched_name = raw.get("matched_name", "").strip()
    confidence = raw.get("confidence", 0.0)

    if not matched_name:
        logger.debug("Skipping mapping with empty matched_name")
        return None

    # Validate entity_type
    valid_types: set[EntityType] = {"BuildingBlock", "Guardrail", "Topic", "Author"}
    if entity_type not in valid_types:
        logger.debug("Skipping unknown entity_type: %s", entity_type)
        return None

    # Validate matched_name for fixed taxonomy entities
    if entity_type == "BuildingBlock" and matched_name not in _BUILDING_BLOCKS:
        logger.warning(
            "LLM returned unknown BuildingBlock '%s' — skipping", matched_name
        )
        return None
    if entity_type == "Guardrail" and matched_name not in _GUARDRAILS:
        logger.warning(
            "LLM returned unknown Guardrail '%s' — skipping", matched_name
        )
        return None

    # Clamp confidence to [0, 1]
    confidence = max(0.0, min(1.0, float(confidence)))

    return TaxonomyMapping(
        entity_text=raw.get("entity_text", ""),
        entity_type=entity_type,
        matched_name=matched_name,
        match_method="llm",
        confidence=confidence,
    )


def classify_text(
    text: str,
    source_type: SourceType,
    title: str = "",
    confidence_threshold: float = _CONFIDENCE_THRESHOLD,
) -> list[TaxonomyMapping]:
    """Classify text into the BeeHaive taxonomy via Gemini.

    Args:
        text: PII-redacted source text to classify.
        source_type: Type of source (paper, regulation, etc.).
        title: Optional title for additional context.
        confidence_threshold: Minimum confidence to include a mapping.

    Returns:
        List of TaxonomyMapping objects with confidence >= threshold.
        Returns empty list on API failure (graceful degradation).
    """
    if not text.strip():
        logger.warning("classify_text called with empty text")
        return []

    # Truncate very long texts — Gemini Flash handles ~1M tokens but
    # we don't need the full text for classification
    max_chars = 30_000
    truncated = text[:max_chars]
    if len(text) > max_chars:
        logger.info("Text truncated from %d to %d chars for classification", len(text), max_chars)

    user_prompt = f"Titel: {title}\nType: {source_type}\n\n{truncated}"

    last_error: str | None = None
    for attempt in range(_MAX_RETRIES + 1):
        try:
            client = _get_client()
            response = client.models.generate_content(
                model=_CLASSIFY_MODEL,
                contents=user_prompt,
                config=types.GenerateContentConfig(
                    system_instruction=_SYSTEM_PROMPT,
                    response_mime_type="application/json",
                    response_schema=_RESPONSE_SCHEMA,
                    temperature=0.1,
                    http_options=types.HttpOptions(timeout=_TIMEOUT_SECONDS * 1000),
                ),
            )

            # Parse structured output
            import json

            if not response.text:
                logger.warning(
                    "Gemini returned empty response (content filter?) for '%s'",
                    title,
                )
                return []

            raw_data = json.loads(response.text)
            raw_mappings = raw_data.get("mappings", [])

            # Validate, filter, and deduplicate
            all_mappings: list[TaxonomyMapping] = []
            below_threshold: list[tuple[str, str, float]] = []
            seen: dict[tuple[str, str], float] = {}

            for raw in raw_mappings:
                mapping = _validate_mapping(raw)
                if mapping is None:
                    continue
                if mapping.confidence < confidence_threshold:
                    below_threshold.append(
                        (mapping.entity_type, mapping.matched_name, mapping.confidence)
                    )
                    continue

                # Dedup per (entity_type, matched_name) — keep highest confidence
                key = (mapping.entity_type, mapping.matched_name)
                if key in seen:
                    if mapping.confidence <= seen[key]:
                        continue
                    # Replace with higher confidence version
                    all_mappings = [
                        m for m in all_mappings
                        if (m.entity_type, m.matched_name) != key
                    ]
                seen[key] = mapping.confidence
                all_mappings.append(mapping)

            if below_threshold:
                logger.info(
                    "Filtered %d mappings below threshold %.1f: %s",
                    len(below_threshold),
                    confidence_threshold,
                    below_threshold,
                )

            logger.info(
                "Classified '%s': %d mappings (BB=%d, GR=%d, Topic=%d, Author=%d)",
                title or "(untitled)",
                len(all_mappings),
                sum(1 for m in all_mappings if m.entity_type == "BuildingBlock"),
                sum(1 for m in all_mappings if m.entity_type == "Guardrail"),
                sum(1 for m in all_mappings if m.entity_type == "Topic"),
                sum(1 for m in all_mappings if m.entity_type == "Author"),
            )
            return all_mappings

        except Exception as e:
            last_error = str(e)
            if attempt < _MAX_RETRIES:
                backoff = _BACKOFF_BASE ** (attempt + 1)
                logger.warning(
                    "Gemini classify attempt %d failed: %s. Retrying in %.0fs",
                    attempt + 1,
                    last_error,
                    backoff,
                )
                time.sleep(backoff)
            else:
                logger.error(
                    "Gemini classify failed after %d attempts: %s",
                    _MAX_RETRIES + 1,
                    last_error,
                )

    # Graceful degradation: return empty mappings
    return []
