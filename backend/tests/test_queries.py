"""Integration tests for knowledge graph queries.

Uses isolated _TEST_ prefixed data from conftest.py fixtures.
Tests are independent of production seed data.

Requires a running Neo4j instance.
Run: make graph-up && make test
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
from tests.conftest import (
    TEST_BUILDING_BLOCKS,
    TEST_GUARDRAILS,
    TEST_KNOWLEDGE_ITEMS,
)

pytestmark = pytest.mark.integration


class TestListQueries:
    def test_get_all_building_blocks_contains_test_data(self, session):
        result = get_all_building_blocks(session)
        names = {r["name"] for r in result}
        for bb in TEST_BUILDING_BLOCKS:
            assert bb["name"] in names

    def test_get_all_guardrails_contains_test_data(self, session):
        result = get_all_guardrails(session)
        names = {r["name"] for r in result}
        for gr in TEST_GUARDRAILS:
            assert gr["name"] in names

    def test_get_all_topics_contains_test_data(self, session):
        result = get_all_topics(session)
        names = {r["name"] for r in result}
        assert "_TEST_AI Ethics" in names
        assert "_TEST_RAG" in names
        assert "_TEST_Privacy" in names

    def test_get_all_authors_contains_test_data(self, session):
        result = get_all_authors(session)
        names = {r["name"] for r in result}
        assert "_TEST_European Commission" in names
        assert "_TEST_Author One" in names
        assert "_TEST_Author Two" in names


class TestSingleNodeLookups:
    def test_get_building_block_found(self, session):
        result = get_building_block(session, "_TEST_Knowledge")
        assert result is not None
        assert result["name"] == "_TEST_Knowledge"
        assert "description" in result
        assert "checklist" in result

    def test_get_building_block_not_found(self, session):
        result = get_building_block(session, "Nonexistent")
        assert result is None

    def test_get_guardrail_found(self, session):
        result = get_guardrail(session, "_TEST_Transparency")
        assert result is not None
        assert result["name"] == "_TEST_Transparency"
        assert "eu_term" in result

    def test_get_guardrail_not_found(self, session):
        result = get_guardrail(session, "Nonexistent")
        assert result is None


class TestItemsByRelation:
    def test_items_by_building_block(self, session):
        # All 3 test items relate to _TEST_Knowledge
        result = get_items_by_building_block(session, "_TEST_Knowledge")
        titles = {r["title"] for r in result}
        assert len(result) == 3
        for item in TEST_KNOWLEDGE_ITEMS:
            assert item["title"] in titles

    def test_items_by_building_block_partial(self, session):
        # Only 1 test item relates to _TEST_Evaluation
        result = get_items_by_building_block(session, "_TEST_Evaluation")
        assert len(result) == 1
        assert result[0]["title"] == "_TEST_RAG Pipeline Design"

    def test_items_by_guardrail(self, session):
        # 2 test items address _TEST_Transparency
        result = get_items_by_guardrail(session, "_TEST_Transparency")
        titles = {r["title"] for r in result}
        assert len(result) == 2
        assert "_TEST_EU AI Act Framework" in titles
        assert "_TEST_RAG Pipeline Design" in titles

    def test_items_by_topic(self, session):
        # 2 test items are about _TEST_AI Ethics
        result = get_items_by_topic(session, "_TEST_AI Ethics")
        assert len(result) == 2

    def test_items_by_author(self, session):
        result = get_items_by_author(session, "_TEST_European Commission")
        assert len(result) == 1
        assert result[0]["title"] == "_TEST_EU AI Act Framework"

    def test_items_by_nonexistent_building_block(self, session):
        result = get_items_by_building_block(session, "Nonexistent")
        assert result == []


class TestDetailAndSearch:
    def test_get_item_with_relations(self, session):
        result = get_item_with_relations(session, "_TEST_RAG Pipeline Design")
        assert result is not None
        assert result["title"] == "_TEST_RAG Pipeline Design"
        assert len(result["building_blocks"]) == 2
        assert len(result["guardrails"]) == 2
        assert len(result["topics"]) == 2
        assert len(result["authors"]) == 1

    def test_get_item_with_relations_not_found(self, session):
        result = get_item_with_relations(session, "Nonexistent Item")
        assert result is None

    def test_search_items_found(self, session):
        result = search_items(session, "_TEST_")
        assert len(result) >= 3
        titles = {r["title"] for r in result}
        assert "_TEST_EU AI Act Framework" in titles

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
        # _TEST_EU AI Act and _TEST_RAG Pipeline share building_block and guardrail
        result = find_related_items(session, "_TEST_EU AI Act Framework")
        assert isinstance(result, list)
        assert len(result) >= 1
        titles = {r["title"] for r in result}
        assert "_TEST_RAG Pipeline Design" in titles

    def test_find_related_items_not_found(self, session):
        result = find_related_items(session, "Nonexistent Item")
        assert result == []
