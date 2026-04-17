"""Pydantic response models for the BeeHaive API."""

from typing import Literal

from pydantic import BaseModel

ToolCategory = Literal["open_source", "framework", "enterprise", "saas"]

# Used as the fallback value when a Tool-DISPLAYED_ON relation has no
# display_order — sorts such tools to the back of the list.
DEFAULT_DISPLAY_ORDER = 99


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


class Tool(BaseModel):
    slug: str
    name: str
    category: ToolCategory
    url: str
    description: str
    display_order: int = DEFAULT_DISPLAY_ORDER
