"""Shared fixtures for BeeHaive integration tests.

Uses an isolated test dataset with _TEST_ prefix so tests are independent
of the production seed data. The dataset is created once per module and
cleaned up afterwards.

Requires a running Neo4j instance.
Start with: make graph-up
"""

import pytest
from neo4j.exceptions import ServiceUnavailable

from app.graph.connection import get_driver

# ---------------------------------------------------------------------------
# Isolated test dataset — small, known, prefixed with _TEST_
# ---------------------------------------------------------------------------
TEST_BUILDING_BLOCKS = [
    {
        "name": "_TEST_Knowledge",
        "description": "Test building block: knowledge",
        "checklist": ["item1"],
    },
    {
        "name": "_TEST_Evaluation",
        "description": "Test building block: evaluation",
        "checklist": ["item1"],
    },
]

TEST_GUARDRAILS = [
    {
        "name": "_TEST_Transparency",
        "eu_term": "Transparency",
        "description": "Test guardrail: transparency",
        "checklist": ["item1"],
    },
    {
        "name": "_TEST_Privacy",
        "eu_term": "Privacy & data governance",
        "description": "Test guardrail: privacy",
        "checklist": ["item1"],
    },
]

TEST_KNOWLEDGE_ITEMS = [
    {
        "title": "_TEST_EU AI Act Framework",
        "content": "Test content about the EU AI Act framework.",
        "source_url": "https://test.example.com/eu-ai-act",
        "source_type": "regulation",
        "is_current": True,
        "building_blocks": ["_TEST_Knowledge"],
        "guardrails": ["_TEST_Transparency"],
        "topics": ["_TEST_AI Ethics"],
        "authors": ["_TEST_European Commission"],
    },
    {
        "title": "_TEST_RAG Pipeline Design",
        "content": "Test content about RAG pipeline architecture.",
        "source_url": "https://test.example.com/rag-pipeline",
        "source_type": "paper",
        "is_current": True,
        "building_blocks": ["_TEST_Knowledge", "_TEST_Evaluation"],
        "guardrails": ["_TEST_Transparency", "_TEST_Privacy"],
        "topics": ["_TEST_AI Ethics", "_TEST_RAG"],
        "authors": ["_TEST_Author One"],
    },
    {
        "title": "_TEST_Privacy Guidelines",
        "content": "Test content about privacy in AI systems.",
        "source_url": "https://test.example.com/privacy",
        "source_type": "best_practice",
        "is_current": True,
        "building_blocks": ["_TEST_Knowledge"],
        "guardrails": ["_TEST_Privacy"],
        "topics": ["_TEST_Privacy"],
        "authors": ["_TEST_Author Two"],
    },
]


def _seed_test_data(tx):
    """Create isolated test nodes with _TEST_ prefix."""
    for bb in TEST_BUILDING_BLOCKS:
        tx.run(
            "MERGE (b:BuildingBlock {name: $name}) "
            "SET b.description = $description, b.checklist = $checklist",
            **bb,
        )
    for gr in TEST_GUARDRAILS:
        tx.run(
            "MERGE (g:Guardrail {name: $name}) "
            "SET g.eu_term = $eu_term, g.description = $description, "
            "g.checklist = $checklist",
            **gr,
        )
    for item in TEST_KNOWLEDGE_ITEMS:
        tx.run(
            """
            MERGE (ki:KnowledgeItem {title: $title})
            SET ki.content = $content,
                ki.source_url = $source_url,
                ki.source_type = $source_type,
                ki.is_current = $is_current,
                ki.created_at = datetime()
            """,
            title=item["title"],
            content=item["content"],
            source_url=item["source_url"],
            source_type=item["source_type"],
            is_current=item["is_current"],
        )
        for topic in item["topics"]:
            tx.run(
                "MATCH (ki:KnowledgeItem {title: $title}) "
                "MERGE (t:Topic {name: $topic}) "
                "MERGE (ki)-[:ABOUT]->(t)",
                title=item["title"],
                topic=topic,
            )
        for author in item["authors"]:
            tx.run(
                "MATCH (ki:KnowledgeItem {title: $title}) "
                "MERGE (a:Author {name: $author}) "
                "MERGE (ki)-[:AUTHORED_BY]->(a)",
                title=item["title"],
                author=author,
            )
        for bb in item["building_blocks"]:
            tx.run(
                "MATCH (ki:KnowledgeItem {title: $title}) "
                "MATCH (bb:BuildingBlock {name: $bb_name}) "
                "MERGE (ki)-[:RELATES_TO]->(bb)",
                title=item["title"],
                bb_name=bb,
            )
        for gr in item["guardrails"]:
            tx.run(
                "MATCH (ki:KnowledgeItem {title: $title}) "
                "MATCH (gr:Guardrail {name: $gr_name}) "
                "MERGE (ki)-[:ADDRESSES]->(gr)",
                title=item["title"],
                gr_name=gr,
            )


def _cleanup_test_data(tx):
    """Remove all nodes with _TEST_ prefix and their relationships."""
    tx.run("MATCH (n) WHERE n.name STARTS WITH '_TEST_' DETACH DELETE n")
    tx.run("MATCH (n) WHERE n.title STARTS WITH '_TEST_' DETACH DELETE n")


def _neo4j_available() -> bool:
    """Check if Neo4j is reachable (with short timeout)."""
    drv = None
    try:
        drv = get_driver()
        drv.verify_connectivity()
        return True
    except (ServiceUnavailable, OSError):
        return False
    finally:
        if drv is not None:
            drv.close()


@pytest.fixture(scope="module")
def driver():
    """Module-scoped Neo4j driver with isolated test data.

    Creates _TEST_ prefixed nodes before any tests run and removes
    them afterwards, so tests are independent of the production seed.
    """
    if not _neo4j_available():
        pytest.skip("Neo4j not available — start with: make graph-up")
    drv = get_driver()
    with drv.session() as s:
        s.execute_write(_cleanup_test_data)  # clean slate
        s.execute_write(_seed_test_data)
    yield drv
    with drv.session() as s:
        s.execute_write(_cleanup_test_data)
    drv.close()


@pytest.fixture()
def session(driver):
    """Function-scoped Neo4j session — fresh session per test."""
    with driver.session() as s:
        yield s
