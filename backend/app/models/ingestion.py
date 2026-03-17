"""Pydantic models for the ingestion pipeline."""

from typing import Literal

from pydantic import BaseModel, Field, HttpUrl

SourceType = Literal["paper", "regulation", "guideline", "best_practice"]
PIIType = Literal["email", "phone"]
FetchStatus = Literal["ok", "failed", "fallback", "requires_pdf_processing"]
EntityType = Literal["BuildingBlock", "Guardrail", "Topic", "Author"]
MatchMethod = Literal["exact", "fuzzy", "llm"]
IngestionStatus = Literal[
    "ingested",
    "duplicate",
    "preview",
    "fetch_failed",
    "pii_scan_failed",
    "engine_unavailable",
    "no_mappings_found",
    "entity_validation_failed",
]


class IngestionSource(BaseModel):
    """Input for the ingestion pipeline."""

    url: HttpUrl
    title: str = Field(min_length=1)
    source_type: SourceType


class FetchResult(BaseModel):
    """Result of fetching a source document."""

    text: str
    source_url: str
    fetch_status: FetchStatus
    pii_clean: bool = True
    metadata: dict = Field(default_factory=dict)


class PIIFinding(BaseModel):
    """A single PII detection in text.

    Does NOT store the original PII value (AVG Art. 5(1)(c) data minimisation).
    Only position and type are retained for redaction.
    """

    pii_type: PIIType
    start: int
    end: int


class PIIReport(BaseModel):
    """Result of a PII scan."""

    findings: list[PIIFinding] = []
    error: str | None = None

    @property
    def has_pii(self) -> bool:
        return len(self.findings) > 0


class TaxonomyMapping(BaseModel):
    """A mapping from an extracted entity to a BeeHaive taxonomy node."""

    entity_text: str
    entity_type: EntityType
    matched_name: str
    match_method: MatchMethod
    confidence: float = 1.0


class IngestionResult(BaseModel):
    """Result of the full ingestion pipeline."""

    status: IngestionStatus
    error: str | None = None
    existing: str | None = None
    mappings: list[TaxonomyMapping] = []
    pii_report: PIIReport | None = None
    entities: list[dict] = []
    suggestion: str | None = None
    rag_synced: bool = True
