"""Gemini-based taxonomy classifier for ingestion pipeline.

Classifies text into the BeeHaive taxonomy (BuildingBlocks, Guardrails,
Topics, Authors) using Gemini 3.1 Pro with structured output.

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

from google.genai import types

from app.ingestion.gemini_client import get_gemini_client
from app.models.ingestion import EntityType, SourceType, TaxonomyMapping

logger = logging.getLogger(__name__)

# Model for classification
_CLASSIFY_MODEL = os.getenv("GEMINI_CLASSIFY_MODEL", "gemini-3.1-pro-preview")

# Confidence threshold — mappings below this are logged but not returned
_CONFIDENCE_THRESHOLD = 0.7

# Retry config
_MAX_RETRIES = 2
_BACKOFF_BASE = 2.0
_TIMEOUT_SECONDS = 30

# The BeeHaive taxonomy — must match seed.py exactly
_BUILDING_BLOCKS = {
    "Knowledge": (
        "Het samenspel van ervaring, vaardigheden, inzichten en attitude waarmee mensen "
        "informatie, tools, AI-modellen en processen effectief inzetten. De centrale "
        "competentielaag: technische kennis, proces-/taakgerichte expertise, en domeinspecifiek "
        "begrip van context, regels en betekenis. "
        "Checklist: domeinkennis, begrip AI-mogelijkheden én beperkingen, ervaring met "
        "prompt-gebruik, vaardigheid met tooling, bewustzijn van risico's/bias/kwaliteit, "
        "leercultuur, rolverdeling. "
        "Niet: documenten of data zelf (→ Dynamic Context), tools (→ Tool Integration)."
    ),
    "Client Blueprint": (
        "Een gestructureerde, end-to-end beschrijving van een AI-oplossing binnen een "
        "specifieke klantcontext: doel, processen, gebruikersinteracties, agent-workflows, "
        "datastromen en gewenste output. De brug tussen klantbehoefte en AI-architectuur. "
        "Checklist: doel helder/afgebakend, processen/rollen/interacties beschreven, "
        "output concreet en toetsbaar, data/context/bronnen duidelijk, agents/tools uitgewerkt, "
        "risico's en randvoorwaarden benoemd, afgestemd met stakeholders. "
        "Niet: algemene methodologieën zonder concrete AI-oplossingscontext."
    ),
    "Dynamic Context": (
        "De actuele, taak- of domeinspecifieke informatie die een AI-oplossing tijdens "
        "uitvoering ontvangt uit een knowledge base, dataset of externe bron. De variabele "
        "laag bovenop het vaste systeemontwerp: inhoud kan voortdurend worden aangepast. "
        "Checklist: bronbestanden actueel, duidelijk welke context wanneer ingevoegd, "
        "irrelevante/verouderde context uitgesloten, privacy/datakwaliteit geborgd, "
        "context gestructureerd opgeslagen, hoeveelheid afgestemd op model (tokens/limits). "
        "Niet: vaste systeemprompts (→ Prompt Design), menselijke expertise (→ Knowledge)."
    ),
    "Prompt Design": (
        "De systematische praktijk van het ontwerpen, structureren, testen en verfijnen "
        "van prompts — inclusief rol, context, instructies, criteria en voorbeelden — "
        "om AI-modellen consistente, relevante en betrouwbare output te laten produceren. "
        "Checklist: heldere taakdefinitie, logische opbouw (rol→context→instructies→criteria→output), "
        "correcte context, few-shot voorbeelden, formatting/output-structuur, edge-case testing, "
        "periodieke herziening. "
        "Niet: platforms die prompts beheren (→ Tool Integration)."
    ),
    "Tool Integration": (
        "Het koppelen van externe systemen, databronnen, API's en software-tools aan een "
        "AI-oplossing, zodat het model niet alleen antwoorden genereert maar ook acties "
        "uitvoert, informatie ophaalt of processen aanstuurt. "
        "Checklist: tools/systemen in kaart, APIs stabiel/gedocumenteerd/veilig, acties "
        "afgebakend, foutafhandeling, logging/controle, fallback-mechanismen. "
        "Inclusief: vector DBs, monitoring-platforms, test-toolkits, RPA, domeinapplicaties."
    ),
    "Model Engines": (
        "De AI-modellen en runtime-omgevingen die de kernfunctionaliteit aandrijven. "
        "Elk type model dat input verwerkt: taalmodellen, redeneermodellen, vision-modellen, "
        "embedding-modellen, classificatiemodellen. Omvat het model zelf (architectuur, "
        "parameters, trainingsbasis) én de operationele laag (runtime, APIs, optimalisaties). "
        "Checklist: juiste modeltype per taak, latency/kosten/schaalbaarheid, inzicht in "
        "trainingsbasis/beperkingen, function calling/reasoning/tools support, "
        "veilige runtime, fallback-modellen, getest met prompts en context. "
        "Niet: teksten die een model gebruiken zonder over modelkeuze/-werking te gaan."
    ),
    "Evaluation Loop": (
        "De systematische, terugkerende cyclus waarin kwaliteit, betrouwbaarheid en "
        "veiligheid van een AI-oplossing wordt gemeten aan de hand van expliciete criteria, "
        "resultaten worden geanalyseerd en gerichte verbeteringen worden doorgevoerd. "
        "Combineert gestructureerde evaluaties (testcases, datasets, metrics, LLM-as-judge, "
        "menselijke beoordeling) met continue monitoring. "
        "Checklist: evaluatiecriteria/metrics vooraf gedefinieerd, representatieve testcases, "
        "automatische/handmatige beoordeling, fouten vastgelegd/geanalyseerd, "
        "verbeteracties, risico's/bias gemonitord, periodiek (niet eenmalig). "
        "Niet: eenmalige benchmarkresultaten of methodologie-evaluaties."
    ),
}

_GUARDRAILS = {
    "Human Agency": (
        "AI-systemen moeten mensen versterken zodat zij weloverwogen beslissingen kunnen "
        "nemen. Menselijke controle via HITL (elke beslissing controleren), HOTL (toezicht "
        "op autonoom systeem), HIC (kaders vooraf bepalen). "
        "Checklist: eindverantwoordelijkheid vastgelegd, impactvolle beslissingen met "
        "menselijke controle, AI-gebruik zichtbaar in interface, override-mogelijkheden, "
        "training tegen over-reliance. "
        "Niet: elk systeem waar mensen betrokken zijn."
    ),
    "Robustness": (
        "AI-systemen moeten veerkrachtig en veilig zijn: veilig functioneren met nood-/terugvalplan, "
        "accuraat, betrouwbaar en reproduceerbaar. "
        "Checklist: systematische tests (functioneel, edge-cases, adversarial), fail-safes bij "
        "time-outs/fouten, kwaliteitsmonitoring (factuality, guardrail-violations, latencies), "
        "rollback-mogelijkheden, incident-responsproces. "
        "Niet: elke vermelding van 'veilig' of 'betrouwbaar' zonder concrete maatregelen."
    ),
    "Privacy": (
        "Naast privacy en gegevensbescherming ook datagovernance: dataminimalisatie, "
        "datakwaliteit, legitimiteit, eigenaarschap, beveiligde toegang. "
        "Checklist: beleid welke data wél/niet verwerkt, dataminimalisatie in prompts/RAG/tools, "
        "logging zonder onnodige persoonsgegevens, datastromen gedocumenteerd, "
        "bewaartermijnen, DSAR-procedures, bijzondere persoonsgegevens uitgesloten. "
        "Niet: algemene dataverwerking zonder privacyfocus."
    ),
    "Fairness": (
        "Het systeem voorkomt systematische benadeling en ondersteunt inclusie en gelijke behandeling. "
        "Checklist: bias-impact geïdentificeerd, testen met diverse persona's (leeftijd, regio, "
        "taalniveau), feedbackmechanisme voor discriminerende output, gevoelige kenmerken "
        "alleen met duidelijke reden, bias-risico's gedocumenteerd met mitigaties. "
        "Niet: elke vermelding van 'eerlijkheid' in algemene zin."
    ),
    "Transparency": (
        "Het moet helder zijn dát en hóe AI wordt ingezet, welke data en modellen zijn gebruikt "
        "en hoe een antwoord tot stand komt. "
        "Checklist: gebruikers geïnformeerd over AI-inzet, bronverwijzingen bij antwoorden, "
        "uitleglaag (hoe antwoord tot stand kwam), modelkaart/systeemkaart, onzekerheid "
        "expliciet benoemd, wijzigingen gedocumenteerd, documentatie toegankelijk. "
        "Breed toepasbaar: alles wat beschrijft HOE of WAAROM AI tot een resultaat komt."
    ),
    "Well-being": (
        "Het systeem draagt bij aan maatschappelijk welzijn en houdt rekening met milieu-impact "
        "en langetermijneffecten. "
        "Checklist: maatschappelijke doelen expliciet, impactscan uitgevoerd, digitale inclusie "
        "(toegankelijkheid, taalniveau), macro-effecten gevolgd, energie-/compute-footprint "
        "gemeten, efficiënte modelstrategie, function creep bewaakt. "
        "Niet: elke business case zonder maatschappelijke dimensie."
    ),
    "Accountability": (
        "Duidelijk wie verantwoordelijk is voor ontwerp, inzet, beheer en uitkomsten van het "
        "AI-systeem, en hoe daarop kan worden toegezien. "
        "Checklist: eigenaarschap vastgelegd (product-owner, data-owner, security-officer), "
        "EU-principes gekoppeld aan controls, wijzigingslogboek voor modellen/prompts/datasets, "
        "periodieke audits (ALTAI), klachtenproces met afhandelingstermijn. "
        "Niet: elke tekst die 'verantwoordelijkheid' noemt zonder governance-structuur."
    ),
}

_SYSTEM_PROMPT = """Je bent een taxonomie-classifier voor het BeeHaive AI knowledge framework.

Je taak: classificeer de gegeven tekst naar de BeeHaive-taxonomie.

## Building Blocks (7 stuks)
{building_blocks}

## Guardrails (7 stuks — gebaseerd op EU Trustworthy AI)
{guardrails}

## Regels
1. Match BuildingBlocks en Guardrails ALLEEN op de exacte namen hierboven.
2. Wees STRIKT selectief: map alleen waar de tekst substantieel over gaat.
3. Typisch 1-2 BuildingBlocks en 1-2 Guardrails per tekst. Meer dan 3 is zeldzaam.
4. Als een tekst meerdere Guardrails OPSOMT (bv. overzichtsartikel), map alleen de Guardrails die de tekst inhoudelijk uitdiept — niet alle genoemde.
5. Extraheer Topics als korte termen (1-3 woorden, Engels). Max 5 topics.
6. Extraheer Authors (organisaties of personen). Gebruik de naam zoals in de tekst.
7. Geef per mapping een confidence score (0.0-1.0). Gebruik het VOLLEDIGE bereik: tangentieel = 0.2-0.4, redelijk verband = 0.5-0.6, duidelijk primair onderwerp = 0.7-0.8, kernonderwerp = 0.9+. Bij twijfel: geef 0.6.

## Veelgemaakte fouten — let extra op:
- **Knowledge** gaat over menselijke expertise en competentie, NIET over documenten, papers of databronnen. Een paper over RAG is geen Knowledge — het kan wel Dynamic Context of Tool Integration zijn.
- **Evaluation Loop** is ALLEEN wanneer de tekst beschrijft hoe je een evaluatiesysteem BOUWT of INRICHT (metrics kiezen, A/B testing opzetten, feedback loops implementeren). NIET voor: teksten die benchmarkresultaten presenteren, een methodologie evalueren, monitoring terloops noemen, of testing als onderdeel van een groter verhaal bespreken. De meeste teksten zijn GEEN Evaluation Loop.
- **Model Engines** gaat over modelkeuze en -werking, NIET over teksten die een model gebruiken.
- **Tool Integration** gaat over tools als PRODUCT (platforms, SDKs, databases). Een tekst die tools als onderdeel van een breder framework bespreekt is niet automatisch Tool Integration.
- **Robustness** gaat over concrete veiligheidsmaatregelen, NIET over elke vermelding van 'veilig'.

## Voorbeelden

Tekst: "The EU AI Act establishes a comprehensive framework for trustworthy AI, defining requirements for high-risk AI systems."
→ BuildingBlock: Knowledge (kennisbron voor het framework)
→ Guardrails: Transparency, Accountability
NIET: Model Engines, Evaluation Loop. NIET alle 7 guardrails.

Tekst: "Open source toolkit for systematic AI safety testing with adversarial prompts, bias detection, and CI/CD integration."
→ BuildingBlocks: Tool Integration (het is een tool/toolkit), Evaluation Loop (systematisch testen)
→ Guardrails: Robustness (aanvalsbestendigheid), Fairness (bias detectie)
NIET: Model Engines (gaat niet over modelkeuze). NIET: Knowledge.

Tekst: "Professional platform for developing, testing and monitoring prompts with version control, A/B testing, and real-time monitoring."
→ BuildingBlocks: Evaluation Loop (A/B testing, monitoring), Tool Integration (het is een platform)
→ Guardrails: Accountability (monitoring, versioning), Robustness (productie-monitoring)

Tekst: "Open source vector database prioritizing data sovereignty with GDPR-compliant data handling and EU data residency."
→ BuildingBlocks: Dynamic Context (vector search voor context), Tool Integration (database tool)
→ Guardrail: Privacy (GDPR, data sovereignty)

Tekst: "Comprehensive handbook covering prompt engineering from theory to practice, including token optimization, context management, and fine-tuning trade-offs."
→ BuildingBlocks: Prompt Design (kernonderwerp), Model Engines (fine-tuning trade-offs)
→ Guardrails: Transparency (het boek legt uit hoe technieken werken), Robustness (token optimization, context management)
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
            client = get_gemini_client()
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
