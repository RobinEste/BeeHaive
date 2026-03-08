"""Shared fixtures for BeeHaive integration tests.

Requires a running Neo4j instance with seed data.
Start with: make graph-up && make graph-seed
"""

import pytest
from neo4j.exceptions import ServiceUnavailable

from app.graph.connection import get_driver


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
    """Module-scoped Neo4j driver — skips all tests if Neo4j is unreachable."""
    if not _neo4j_available():
        pytest.skip("Neo4j not available — start with: make graph-up && make graph-seed")
    drv = get_driver()
    yield drv
    drv.close()


@pytest.fixture()
def session(driver):
    """Function-scoped Neo4j session — fresh session per test."""
    with driver.session() as s:
        yield s
