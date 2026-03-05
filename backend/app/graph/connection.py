from contextlib import contextmanager

from neo4j import GraphDatabase

from app.config import NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD


def get_driver():
    """Create a Neo4j driver instance."""
    return GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))


@contextmanager
def get_session():
    """Context manager that yields a Neo4j session and closes the driver after use."""
    driver = get_driver()
    try:
        with driver.session() as session:
            yield session
    finally:
        driver.close()
