"""FastAPI dependencies for the BeeHaive API."""

from collections.abc import Generator

from neo4j import Session

from app.graph.connection import get_driver

_driver = None


def get_neo4j_driver():
    """Lazy-initialised singleton Neo4j driver."""
    global _driver
    if _driver is None:
        _driver = get_driver()
    return _driver


def get_db() -> Generator[Session, None, None]:
    """Yield a Neo4j session, then close it. Used as FastAPI Depends()."""
    driver = get_neo4j_driver()
    with driver.session() as session:
        yield session
