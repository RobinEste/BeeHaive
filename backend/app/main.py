"""BeeHaive API — FastAPI application entry point."""

from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api import building_blocks, guardrails, items
from app.dependencies import get_neo4j_driver


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    driver = get_neo4j_driver()
    driver.close()


app = FastAPI(
    title="BeeHaive API",
    description="AI Knowledge Framework — knowledge graph endpoints",
    version="0.1.0",
    lifespan=lifespan,
)

app.include_router(building_blocks.router, prefix="/api")
app.include_router(guardrails.router, prefix="/api")
app.include_router(items.router, prefix="/api")


@app.get("/health")
def health():
    return {"status": "ok"}
