"""Pydantic response models for the BeeHaive API."""

from pydantic import BaseModel


class BuildingBlock(BaseModel):
    name: str
    description: str
    checklist: list[str]


class Guardrail(BaseModel):
    name: str
    eu_term: str
    description: str
    checklist: list[str]


class Topic(BaseModel):
    name: str


class Author(BaseModel):
    name: str


class KnowledgeItem(BaseModel):
    title: str
    content: str
    summary_nl: str | None = None
    source_url: str | None = None
    source_type: str | None = None
    is_current: bool | None = None
    curation_score: int = 0


class KnowledgeItemDetail(KnowledgeItem):
    building_blocks: list[BuildingBlock]
    guardrails: list[Guardrail]
    topics: list[Topic]
    authors: list[Author]
