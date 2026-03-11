"""Gemini-based taxonomy classifier for the BeeHaive knowledge graph.

Classifies text into BeeHaive taxonomy entities (BuildingBlocks, Guardrails,
Topics, Authors) using Google's Gemini 2.5 Flash via the google-genai SDK.

Text is PII-redacted before being sent to the API (see fetcher.py).
"""

import logging
import os
import time

from google import genai
from google.genai import types

from app.models.ingestion import SourceType, TaxonomyMapping

logger = logging.getLogger(__name__)

GEMINI_MODEL = "gemini-2.5-flash-preview-05-20"
CONFIDENCE_THRESHOLD = 0.7
REQUEST_TIMEOUT = 30
MAX_RETRIES = 2

# The BeeHaive taxonomy — used in the system prompt for classification.
BUILDING_BLOCKS = {
    "Knowledge": "Het fundament: alle kennis die het AI-systeem voedt. Documenten, whitepapers, artikelen en kennisbanken.",
    "Client Blueprint": "Gestructureerd profiel van de klant/gebruiker. Context over doelen, branche, kennisniveau.",
    "Dynamic Context": "Real-time context voor het AI-model. Combineert kennisbank, klantprofiel en conversatie.",
    "Prompt Design": "Gestructureerde prompt templates en chains voor consistente AI-output.",
    "Tool Integration": "Externe tools en APIs die het AI-systeem kan aanroepen.",
    "Model Engines": "De AI-modellen die worden ingezet, inclusief fallback en routing.",
    "Evaluation Loop": "Continue evaluatie van AI-output kwaliteit en feedback loops.",
}

GUARDRAILS = {
    "Human Agency": "Mensen behouden controle over AI-beslissingen, oversight en interventie.",
    "Robustness": "Technisch robuust, veilig en betrouwbaar. Bescherming tegen fouten en aanvallen.",
    "Privacy": "Persoonsgegevens beschermd conform AVG/GDPR. Data minimalisatie.",
    "Fairness": "Eerlijke, niet-discriminerende AI-output. Aandacht voor bias.",
    "Transparency": "Transparant over wanneer en hoe AI wordt ingezet. Bronvermelding.",
    "Well-being": "Draagt bij aan maatschappelijk welzijn, minimaliseert milieu-impact.",
    "Accountability": "Duidelijke verantwoordelijkheid, audit trails en governance.",
}

SYSTEM_PROMPT = """You are a taxonomy classifier for the BeeHaive AI knowledge framework.

Given a text (title + content), classify it into the BeeHaive taxonomy.

## BuildingBlocks (match 1-3 that are most relevant)
{building_blocks}

## Guardrails (match 1-3 that are most relevant)
{guardrails}

## Topics
Extract 1-5 topic keywords from the text. Use short, specific terms (e.g. "RAG", "AI Ethics", "EU AI Act"). Reuse existing topics when appropriate.

## Authors
Extract author names from the text. Only include names explicitly mentioned as authors. For organisations, use the organisation name. Do NOT invent authors.

## Rules
- Only return mappings you are confident about (confidence >= 0.7)
- For BuildingBlocks and Guardrails: match against the EXACT names listed above
- For Topics: use concise, reusable terms
- For Authors: use the name as written in the source
- Return an empty array if the text is not classifiable
""".format(
    building_blocks="\n".join(f"- **{k}**: {v}" for k, v in BUILDING_BLOCKS.items()),
    guardrails="\n".join(f"- **{k}**: {v}" for k, v in GUARDRAILS.items()),
)

# Structured output schema for Gemini
RESPONSE_SCHEMA = types.Schema(
    type=types.Type.ARRAY,
    items=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "entity_type": types.Schema(
                type=types.Type.STRING,
                enum=["BuildingBlock", "Guardrail", "Topic", "Author"],
            ),
            "matched_name": types.Schema(type=types.Type.STRING),
            "confidence": types.Schema(type=types.Type.NUMBER),
        },
        required=["entity_type", "matched_name", "confidence"],
    ),
)


def _get_client() -> genai.Client:
    """Create a Gemini client. Raises ValueError if API key is missing."""
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError(
            "GEMINI_API_KEY not set. Get one at https://aistudio.google.com/apikey"
        )
    return genai.Client(api_key=api_key)


def _validate_mapping(raw: dict) -> TaxonomyMapping | None:
    """Validate a single raw mapping from Gemini output.

    Returns None if the mapping is invalid (unknown entity type,
    unknown BuildingBlock/Guardrail name, or below confidence threshold).
    """
    entity_type = raw.get("entity_type")
    matched_name = raw.get("matched_name", "").strip()
    confidence = raw.get("confidence", 0.0)

    if not matched_name or confidence < CONFIDENCE_THRESHOLD:
        return None

    # Validate that BuildingBlock/Guardrail names match the taxonomy
    if entity_type == "BuildingBlock" and matched_name not in BUILDING_BLOCKS:
        logger.warning("Unknown BuildingBlock from LLM: %s", matched_name)
        return None
    if entity_type == "Guardrail" and matched_name not in GUARDRAILS:
        logger.warning("Unknown Guardrail from LLM: %s", matched_name)
        return None
    if entity_type not in ("BuildingBlock", "Guardrail", "Topic", "Author"):
        logger.warning("Unknown entity_type from LLM: %s", entity_type)
        return None

    return TaxonomyMapping(
        entity_text=matched_name,
        entity_type=entity_type,
        matched_name=matched_name,
        match_method="llm",
        confidence=confidence,
    )


def classify_text(
    text: str, source_type: SourceType, title: str = ""
) -> list[TaxonomyMapping]:
    """Classify text into BeeHaive taxonomy entities via Gemini.

    Args:
        text: The (PII-redacted) document text.
        source_type: Type of source (paper, regulation, etc.).
        title: Optional title for additional context.

    Returns:
        List of validated TaxonomyMappings above confidence threshold.
        Returns empty list on API failure (graceful degradation).
    """
    if not text.strip():
        return []

    user_prompt = f"Title: {title}\nType: {source_type}\n\nText:\n{text[:8000]}"

    client = _get_client()

    for attempt in range(MAX_RETRIES + 1):
        try:
            response = client.models.generate_content(
                model=GEMINI_MODEL,
                contents=user_prompt,
                config=types.GenerateContentConfig(
                    system_instruction=SYSTEM_PROMPT,
                    response_mime_type="application/json",
                    response_schema=RESPONSE_SCHEMA,
                    temperature=0.1,
                    http_options=types.HttpOptions(timeout=REQUEST_TIMEOUT * 1000),
                ),
            )

            raw_mappings = response.parsed
            if raw_mappings is None:
                logger.warning("Gemini returned no parseable response")
                return []

            mappings = []
            for raw in raw_mappings:
                # response.parsed returns model objects; convert to dict
                raw_dict = (
                    raw if isinstance(raw, dict) else raw.model_dump()
                    if hasattr(raw, "model_dump") else dict(raw)
                )
                validated = _validate_mapping(raw_dict)
                if validated:
                    mappings.append(validated)
                else:
                    logger.debug(
                        "Mapping below threshold or invalid: %s", raw_dict
                    )

            logger.info(
                "Classified '%s': %d mappings (from %d raw)",
                title or text[:50],
                len(mappings),
                len(raw_mappings),
            )
            return mappings

        except Exception as e:
            if attempt < MAX_RETRIES:
                wait = 2 ** (attempt + 1)
                logger.warning(
                    "Gemini API error (attempt %d/%d): %s. Retrying in %ds.",
                    attempt + 1,
                    MAX_RETRIES + 1,
                    e,
                    wait,
                )
                time.sleep(wait)
            else:
                logger.error(
                    "Gemini API failed after %d attempts: %s", MAX_RETRIES + 1, e
                )
                return []
