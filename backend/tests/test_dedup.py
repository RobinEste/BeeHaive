"""Unit tests for deduplication queries.

Tests find_item_by_source_url and find_items_by_fuzzy_title.
These are integration tests requiring a running Neo4j instance.
"""

import pytest

from app.graph.queries import find_item_by_source_url, find_items_by_fuzzy_title


@pytest.mark.integration
class TestDeduplication:
    """Deduplication query tests — requires seeded Neo4j."""

    def test_find_by_source_url_found(self, session):
        """Known source_url from seed data should return the item."""
        url = "https://digital-strategy.ec.europa.eu/en/policies/european-approach-artificial-intelligence"
        result = find_item_by_source_url(session, url)
        assert result is not None
        assert result["title"] == "EU AI Act - Trustworthy AI Framework"

    def test_find_by_source_url_not_found(self, session):
        """Unknown URL should return None."""
        result = find_item_by_source_url(session, "https://nonexistent.example.com/paper")
        assert result is None

    def test_fuzzy_title_match(self, session):
        """Partial title match should return results."""
        results = find_items_by_fuzzy_title(session, "EU AI Act")
        assert len(results) >= 1
        titles = [r["title"] for r in results]
        assert any("EU AI Act" in t for t in titles)

    def test_fuzzy_title_no_match(self, session):
        """Completely unrelated title should return empty list."""
        results = find_items_by_fuzzy_title(session, "xyznonexistentxyz")
        assert results == []

    def test_fuzzy_title_respects_limit(self, session):
        """Results should be capped at the limit parameter."""
        results = find_items_by_fuzzy_title(session, "AI", limit=2)
        assert len(results) <= 2
