"""Shared fixtures for BeeHaive integration tests.

Requires a running Neo4j instance with seed data.
Start with: make graph-up && make graph-seed
"""

import pytest
from app.graph.connection import get_driver


@pytest.fixture(scope="module")
def driver():
    """Module-scoped Neo4j driver — shared across tests in a module."""
    drv = get_driver()
    yield drv
    drv.close()


@pytest.fixture()
def session(driver):
    """Function-scoped Neo4j session — fresh session per test."""
    with driver.session() as s:
        yield s
