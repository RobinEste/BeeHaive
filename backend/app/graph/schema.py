"""Neo4j schema definition: constraints and indexes for BeeHaive knowledge graph."""

CONSTRAINTS = [
    ("BuildingBlock", "name"),
    ("Guardrail", "name"),
    ("KnowledgeItem", "title"),
    ("Topic", "name"),
    ("Author", "name"),
]


def create_constraints(session):
    """Create uniqueness constraints. Idempotent — safe to run multiple times."""
    for label, prop in CONSTRAINTS:
        constraint_name = f"unique_{label.lower()}_{prop}"
        session.run(
            f"CREATE CONSTRAINT {constraint_name} IF NOT EXISTS "
            f"FOR (n:{label}) REQUIRE n.{prop} IS UNIQUE"
        )
    print(f"  {len(CONSTRAINTS)} uniqueness constraints ensured")
