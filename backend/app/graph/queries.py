"""Query functions for the BeeHaive knowledge graph.

All functions are read-only (MATCH/RETURN only) and use parameterized queries.
Neo4j exceptions propagate to the caller — the future API layer handles them.

Convention:
- List functions return [] when no results found
- Single-item functions return None when not found
"""


# --- Node listing queries ---


def get_all_building_blocks(session):
    """Return all BuildingBlock nodes, ordered by name."""
    def _query(tx):
        result = tx.run("MATCH (b:BuildingBlock) RETURN b ORDER BY b.name")
        return [dict(record["b"]) for record in result]
    return session.execute_read(_query)


def get_all_guardrails(session):
    """Return all Guardrail nodes, ordered by name."""
    def _query(tx):
        result = tx.run("MATCH (g:Guardrail) RETURN g ORDER BY g.name")
        return [dict(record["g"]) for record in result]
    return session.execute_read(_query)


def get_all_topics(session):
    """Return all Topic nodes, ordered by name."""
    def _query(tx):
        result = tx.run("MATCH (t:Topic) RETURN t ORDER BY t.name")
        return [dict(record["t"]) for record in result]
    return session.execute_read(_query)


def get_all_authors(session):
    """Return all Author nodes, ordered by name."""
    def _query(tx):
        result = tx.run("MATCH (a:Author) RETURN a ORDER BY a.name")
        return [dict(record["a"]) for record in result]
    return session.execute_read(_query)


# --- Single node lookups ---


def get_building_block(session, name):
    """Return a single BuildingBlock by name, or None if not found."""
    def _query(tx):
        result = tx.run(
            "MATCH (b:BuildingBlock {name: $name}) RETURN b",
            name=name,
        )
        record = result.single()
        return dict(record["b"]) if record else None
    return session.execute_read(_query)


def get_guardrail(session, name):
    """Return a single Guardrail by name, or None if not found."""
    def _query(tx):
        result = tx.run(
            "MATCH (g:Guardrail {name: $name}) RETURN g",
            name=name,
        )
        record = result.single()
        return dict(record["g"]) if record else None
    return session.execute_read(_query)


# --- Items by relation ---


def get_items_by_building_block(session, name):
    """Return KnowledgeItems linked to a BuildingBlock via RELATES_TO."""
    def _query(tx):
        result = tx.run(
            "MATCH (ki:KnowledgeItem)-[:RELATES_TO]->(b:BuildingBlock {name: $name}) "
            "RETURN ki ORDER BY ki.title",
            name=name,
        )
        return [dict(record["ki"]) for record in result]
    return session.execute_read(_query)


def get_items_by_guardrail(session, name):
    """Return KnowledgeItems linked to a Guardrail via ADDRESSES."""
    def _query(tx):
        result = tx.run(
            "MATCH (ki:KnowledgeItem)-[:ADDRESSES]->(g:Guardrail {name: $name}) "
            "RETURN ki ORDER BY ki.title",
            name=name,
        )
        return [dict(record["ki"]) for record in result]
    return session.execute_read(_query)


def get_items_by_topic(session, name):
    """Return KnowledgeItems linked to a Topic via ABOUT."""
    def _query(tx):
        result = tx.run(
            "MATCH (ki:KnowledgeItem)-[:ABOUT]->(t:Topic {name: $name}) "
            "RETURN ki ORDER BY ki.title",
            name=name,
        )
        return [dict(record["ki"]) for record in result]
    return session.execute_read(_query)


def get_items_by_author(session, name):
    """Return KnowledgeItems linked to an Author via AUTHORED_BY."""
    def _query(tx):
        result = tx.run(
            "MATCH (ki:KnowledgeItem)-[:AUTHORED_BY]->(a:Author {name: $name}) "
            "RETURN ki ORDER BY ki.title",
            name=name,
        )
        return [dict(record["ki"]) for record in result]
    return session.execute_read(_query)


# --- Detail & search queries ---


def get_item_with_relations(session, title):
    """Return a KnowledgeItem with all its relations, or None if not found.

    Returns a dict with the item properties plus nested lists:
    building_blocks, guardrails, topics, authors.
    """
    def _query(tx):
        result = tx.run(
            """
            MATCH (ki:KnowledgeItem {title: $title})
            OPTIONAL MATCH (ki)-[:RELATES_TO]->(bb:BuildingBlock)
            WITH ki, collect(bb) AS building_blocks
            OPTIONAL MATCH (ki)-[:ADDRESSES]->(gr:Guardrail)
            WITH ki, building_blocks, collect(gr) AS guardrails
            OPTIONAL MATCH (ki)-[:ABOUT]->(t:Topic)
            WITH ki, building_blocks, guardrails, collect(t) AS topics
            OPTIONAL MATCH (ki)-[:AUTHORED_BY]->(a:Author)
            RETURN ki, building_blocks, guardrails, topics,
                   collect(a) AS authors
            """,
            title=title,
        )
        record = result.single()
        if not record or record["ki"] is None:
            return None
        item = dict(record["ki"])
        item["building_blocks"] = [dict(bb) for bb in record["building_blocks"]]
        item["guardrails"] = [dict(gr) for gr in record["guardrails"]]
        item["topics"] = [dict(t) for t in record["topics"]]
        item["authors"] = [dict(a) for a in record["authors"]]
        return item
    return session.execute_read(_query)


def find_related_items(session, title):
    """Find items sharing at least one BuildingBlock, Guardrail or Topic (OR logic).

    Results are sorted by number of shared relations (most related first).
    """
    def _query(tx):
        result = tx.run(
            """
            MATCH (ki:KnowledgeItem {title: $title})
            MATCH (ki)-[:RELATES_TO|ADDRESSES|ABOUT]->(shared)<-[:RELATES_TO|ADDRESSES|ABOUT]-(other:KnowledgeItem)
            WHERE other <> ki
            RETURN other, count(shared) AS shared_count
            ORDER BY shared_count DESC, other.title
            LIMIT 25
            """,
            title=title,
        )
        return [dict(record["other"]) for record in result]
    return session.execute_read(_query)


def search_items(session, query):
    """Search KnowledgeItems by title or content using CONTAINS.

    Raises ValueError if query is shorter than 2 or longer than 200 characters.
    """
    if len(query) < 2:
        raise ValueError("Search query must be at least 2 characters")
    if len(query) > 200:
        raise ValueError("Search query must be at most 200 characters")

    def _query(tx):
        result = tx.run(
            """
            MATCH (ki:KnowledgeItem)
            WHERE toLower(ki.title) CONTAINS toLower($term)
               OR toLower(ki.content) CONTAINS toLower($term)
            RETURN ki ORDER BY ki.title
            LIMIT 50
            """,
            term=query,
        )
        return [dict(record["ki"]) for record in result]
    return session.execute_read(_query)
