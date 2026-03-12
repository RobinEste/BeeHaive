"""CLI script for ingesting a single knowledge item into BeeHaive.

Usage:
    make ingest-item URL="https://..." TITLE="Paper Title" TYPE=paper
    make ingest-item URL="https://..." TITLE="Paper Title" TYPE=paper COMMIT=1

Default is dry-run (preview). Pass COMMIT=1 to write to Neo4j.

Source types: paper, regulation, guideline, best_practice
"""

import argparse
import logging
import sys
from typing import get_args

from app.graph.connection import get_session
from app.ingestion.pipeline import ingest
from app.models.ingestion import IngestionSource, SourceType

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s  %(name)s  %(message)s",
)
logger = logging.getLogger(__name__)

VALID_TYPES = get_args(SourceType)


def _format_mappings(mappings) -> str:
    """Format taxonomy mappings for terminal output."""
    lines = []
    grouped = {}
    for m in mappings:
        grouped.setdefault(m.entity_type, []).append(m)

    for entity_type in ("BuildingBlock", "Guardrail", "Topic", "Author"):
        items = grouped.get(entity_type, [])
        if items:
            lines.append(f"  {entity_type}:")
            for m in items:
                lines.append(f"    - {m.matched_name} (confidence: {m.confidence:.2f})")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Ingest a knowledge item into BeeHaive")
    parser.add_argument("--url", required=True, help="Source URL (HTTPS)")
    parser.add_argument("--title", required=True, help="Item title")
    parser.add_argument("--type", required=True, choices=VALID_TYPES, dest="source_type", help="Source type")
    parser.add_argument("--commit", action="store_true", help="Write to Neo4j (default: dry-run preview)")
    args = parser.parse_args()

    dry_run = not args.commit

    source = IngestionSource(
        url=args.url,
        title=args.title,
        source_type=args.source_type,
    )

    mode = "PREVIEW (dry-run)" if dry_run else "COMMIT"
    print(f"\n{'='*60}")
    print(f"BeeHaive Ingestion — {mode}")
    print(f"{'='*60}")
    print(f"  URL:   {source.url}")
    print(f"  Title: {source.title}")
    print(f"  Type:  {source.source_type}")
    print(f"{'='*60}\n")

    try:
        with get_session() as session:
            result = ingest(source, session, dry_run=dry_run)
    except ValueError as e:
        print(f"CONFIGURATION ERROR: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"ERROR: {e}")
        sys.exit(1)

    # Display result
    if result.status == "duplicate":
        print(f"DUPLICATE: Item already exists as '{result.existing}'")
        sys.exit(1)

    elif result.status == "preview":
        print("Proposed taxonomy mappings:\n")
        print(_format_mappings(result.mappings))
        print(f"\n  Total: {len(result.mappings)} mappings")
        print("\nRe-run with --commit to write to Neo4j.")

    elif result.status == "ingested":
        print("Successfully ingested! Taxonomy mappings:\n")
        print(_format_mappings(result.mappings))
        print(f"\n  Total: {len(result.mappings)} mappings written to Neo4j.")

    elif result.status == "no_mappings_found":
        print(f"NO MAPPINGS: {result.suggestion}")
        sys.exit(1)

    elif result.status == "engine_unavailable":
        print(f"NOT SUPPORTED: {result.error}")
        sys.exit(1)

    else:
        print(f"FAILED ({result.status}): {result.error}")
        sys.exit(1)


if __name__ == "__main__":
    main()
