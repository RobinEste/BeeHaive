"""API endpoints for Guardrails."""

from fastapi import APIRouter, Depends, HTTPException
from neo4j import Session

from app.dependencies import get_db
from app.graph.queries import (
    get_all_guardrails,
    get_guardrail,
    get_items_by_guardrail,
)
from app.models.schemas import Guardrail, KnowledgeItem

router = APIRouter(prefix="/guardrails", tags=["guardrails"])


@router.get("", response_model=list[Guardrail])
def list_guardrails(db: Session = Depends(get_db)):
    return get_all_guardrails(db)


@router.get("/{name}", response_model=Guardrail)
def read_guardrail(name: str, db: Session = Depends(get_db)):
    gr = get_guardrail(db, name)
    if gr is None:
        raise HTTPException(status_code=404, detail=f"Guardrail '{name}' not found")
    return gr


@router.get("/{name}/items", response_model=list[KnowledgeItem])
def list_items_for_guardrail(name: str, db: Session = Depends(get_db)):
    gr = get_guardrail(db, name)
    if gr is None:
        raise HTTPException(status_code=404, detail=f"Guardrail '{name}' not found")
    return get_items_by_guardrail(db, name)
