"""Write operations for the BeeHaive knowledge graph.

Separated from queries.py to maintain read/write isolation (KNW-2026-006).
All Cypher queries use parameterized values ($param syntax). Label/relation
names may use f-strings ONLY from the hardcoded _RELATION_MAP.
No user-supplied values in f-strings. No Cypher outside graph/.
"""

import logging

logger = logging.getLogger(__name__)

# Entity type → Neo4j relation type + target label
_RELATION_MAP = {
    "BuildingBlock": ("RELATES_TO", "BuildingBlock"),
    "Guardrail": ("ADDRESSES", "Guardrail"),
    "Topic": ("ABOUT", "Topic"),
    "Author": ("AUTHORED_BY", "Author"),
}


def create_knowledge_item_with_relations(session, source, mappings):
    """Create a KnowledgeItem node with taxonomy relations.

    Uses batched UNWIND queries per relation type to avoid N+1 queries.

    Args:
        session: Neo4j session
        source: IngestionSource with url, title, source_type
        mappings: list of TaxonomyMapping with entity_type and matched_name

    Returns:
        dict with the created KnowledgeItem properties
    """
    def _write(tx):
        # Create the KnowledgeItem node
        result = tx.run(
            """
            MERGE (ki:KnowledgeItem {source_url: $source_url})
            ON CREATE SET
                ki.title = $title,
                ki.title_lower = toLower($title),
                ki.source_type = $source_type,
                ki.is_current = true,
                ki.created_at = datetime()
            ON MATCH SET
                ki.title = $title,
                ki.title_lower = toLower($title),
                ki.source_type = $source_type,
                ki.updated_at = datetime()
            RETURN ki
            """,
            title=source.title,
            source_url=str(source.url),
            source_type=source.source_type,
        )
        record = result.single()
        if not record:
            raise RuntimeError(f"Failed to create KnowledgeItem: {source.title}")

        # Group mappings by entity type for batched UNWIND queries
        grouped: dict[str, list[str]] = {}
        for mapping in mappings:
            grouped.setdefault(mapping.entity_type, []).append(mapping.matched_name)

        # Batch create relations per type using UNWIND
        for entity_type, names in grouped.items():
            if entity_type not in _RELATION_MAP:
                logger.warning(
                    "Unknown entity_type '%s' skipped for item '%s' — "
                    "update _RELATION_MAP if this is intentional",
                    entity_type, source.title,
                )
                continue
            rel_type, label = _RELATION_MAP[entity_type]

            # Topic and Author nodes are created on-demand (MERGE).
            # BuildingBlock and Guardrail must already exist (MATCH).
            if entity_type in ("Topic", "Author"):
                tx.run(
                    f"""
                    MATCH (ki:KnowledgeItem {{source_url: $source_url}})
                    UNWIND $names AS name
                    MERGE (t:{label} {{name: name}})
                    MERGE (ki)-[:{rel_type}]->(t)
                    """,
                    source_url=str(source.url),
                    names=names,
                )
            else:
                rel_result = tx.run(
                    f"""
                    MATCH (ki:KnowledgeItem {{source_url: $source_url}})
                    UNWIND $names AS name
                    MATCH (t:{label} {{name: name}})
                    MERGE (ki)-[r:{rel_type}]->(t)
                    RETURN count(r) AS created
                    """,
                    source_url=str(source.url),
                    names=names,
                )
                created = rel_result.single()["created"]
                if created < len(names):
                    missing = len(names) - created
                    logger.warning(
                        "%d/%d %s relations created (%d target nodes not found)",
                        created, len(names), entity_type, missing,
                    )

        return dict(record["ki"])

    return session.execute_write(_write)
