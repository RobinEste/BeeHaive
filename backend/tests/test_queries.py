"""Integration tests for knowledge graph queries.

Requires a running Neo4j instance with seed data.
Run: make graph-up && make graph-seed && make test
"""

import pytest

from app.graph.queries import (
    find_related_items,
    get_all_authors,
    get_all_building_blocks,
    get_all_guardrails,
    get_all_topics,
    get_building_block,
    get_guardrail,
    get_item_with_relations,
    get_items_by_author,
    get_items_by_building_block,
    get_items_by_guardrail,
    get_items_by_topic,
    search_items,
)
from app.graph.seed import (
    BUILDING_BLOCKS,
    EXAMPLE_KNOWLEDGE_ITEM,
    EXAMPLE_RELATIONS,
    GUARDRAILS,
)

EXAMPLE_TITLE = EXAMPLE_KNOWLEDGE_ITEM["title"]

pytestmark = pytest.mark.integration


class TestListQueries:
    def test_get_all_building_blocks_count(self, session):
        result = get_all_building_blocks(session)
        assert len(result) == len(BUILDING_BLOCKS)

    def test_get_all_guardrails_count(self, session):
        result = get_all_guardrails(session)
        assert len(result) == len(GUARDRAILS)

    def test_get_all_topics(self, session):
        result = get_all_topics(session)
        assert len(result) == 1
        assert result[0]["name"] == EXAMPLE_RELATIONS["topic"]

    def test_get_all_authors(self, session):
        result = get_all_authors(session)
        assert len(result) == 1
        assert result[0]["name"] == EXAMPLE_RELATIONS["author"]


class TestSingleNodeLookups:
    def test_get_building_block_found(self, session):
        result = get_building_block(session, EXAMPLE_RELATIONS["building_block"])
        assert result is not None
        assert result["name"] == EXAMPLE_RELATIONS["building_block"]
        assert "description" in result
        assert "checklist" in result

    def test_get_building_block_not_found(self, session):
        result = get_building_block(session, "Nonexistent")
        assert result is None

    def test_get_guardrail_found(self, session):
        result = get_guardrail(session, EXAMPLE_RELATIONS["guardrail"])
        assert result is not None
        assert result["name"] == EXAMPLE_RELATIONS["guardrail"]
        assert "eu_term" in result

    def test_get_guardrail_not_found(self, session):
        result = get_guardrail(session, "Nonexistent")
        assert result is None


class TestItemsByRelation:
    def test_items_by_building_block(self, session):
        result = get_items_by_building_block(session, EXAMPLE_RELATIONS["building_block"])
        assert len(result) == 1
        assert result[0]["title"] == EXAMPLE_TITLE

    def test_items_by_guardrail(self, session):
        result = get_items_by_guardrail(session, EXAMPLE_RELATIONS["guardrail"])
        assert len(result) == 1
        assert result[0]["title"] == EXAMPLE_TITLE

    def test_items_by_topic(self, session):
        result = get_items_by_topic(session, EXAMPLE_RELATIONS["topic"])
        assert len(result) == 1

    def test_items_by_author(self, session):
        result = get_items_by_author(session, EXAMPLE_RELATIONS["author"])
        assert len(result) == 1

    def test_items_by_nonexistent_building_block(self, session):
        result = get_items_by_building_block(session, "Nonexistent")
        assert result == []


class TestDetailAndSearch:
    def test_get_item_with_relations(self, session):
        result = get_item_with_relations(session, EXAMPLE_TITLE)
        assert result is not None
        assert result["title"] == EXAMPLE_TITLE
        assert len(result["building_blocks"]) >= 1
        assert len(result["guardrails"]) >= 1
        assert len(result["topics"]) >= 1
        assert len(result["authors"]) >= 1

    def test_get_item_with_relations_not_found(self, session):
        result = get_item_with_relations(session, "Nonexistent Item")
        assert result is None

    def test_search_items_found(self, session):
        result = search_items(session, "EU")
        assert len(result) >= 1
        assert any(EXAMPLE_TITLE == item["title"] for item in result)

    def test_search_items_not_found(self, session):
        result = search_items(session, "nonexistent_xyz")
        assert result == []

    def test_search_items_too_short(self, session):
        with pytest.raises(ValueError, match="at least 2 characters"):
            search_items(session, "x")

    def test_search_items_too_long(self, session):
        with pytest.raises(ValueError, match="at most 200 characters"):
            search_items(session, "a" * 201)

    def test_find_related_items(self, session):
        # With only 1 KnowledgeItem in seed data, there are no related items
        result = find_related_items(session, EXAMPLE_TITLE)
        assert isinstance(result, list)

    def test_find_related_items_not_found(self, session):
        result = find_related_items(session, "Nonexistent Item")
        assert result == []
