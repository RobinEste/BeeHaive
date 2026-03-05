"""Seed the BeeHaive knowledge graph with initial data.

Usage:
    python backend/scripts/seed_graph.py

Idempotent — safe to run multiple times without creating duplicates.
"""

from app.graph.connection import get_session
from app.graph.schema import create_constraints
from app.graph.seed import seed_all


def main():
    print("Connecting to Neo4j...")

    with get_session() as session:
        print("Creating constraints...")
        create_constraints(session)

        print("\nSeeding data...")
        seed_all(session)

    print("\nDone!")


if __name__ == "__main__":
    main()
