"""API endpoints for KnowledgeItems, Topics, Authors and Search."""

from fastapi import APIRouter, Depends, HTTPException, Query
from neo4j import Session

from app.dependencies import get_db
from app.graph.queries import (
    find_related_items,
    get_all_authors,
    get_all_topics,
    get_item_with_relations,
    get_items_by_author,
    get_items_by_topic,
    search_items,
)
from app.models.schemas import Author, KnowledgeItem, KnowledgeItemDetail, Topic

router = APIRouter(tags=["items"])


# --- Topics ---


@router.get("/topics", response_model=list[Topic])
def list_topics(db: Session = Depends(get_db)):
    return get_all_topics(db)


@router.get("/topics/{name}/items", response_model=list[KnowledgeItem])
def list_items_for_topic(name: str, db: Session = Depends(get_db)):
    return get_items_by_topic(db, name)


# --- Authors ---


@router.get("/authors", response_model=list[Author])
def list_authors(db: Session = Depends(get_db)):
    return get_all_authors(db)


@router.get("/authors/{name}/items", response_model=list[KnowledgeItem])
def list_items_for_author(name: str, db: Session = Depends(get_db)):
    return get_items_by_author(db, name)


# --- KnowledgeItems ---


@router.get("/items/{title}", response_model=KnowledgeItemDetail)
def read_item(title: str, db: Session = Depends(get_db)):
    item = get_item_with_relations(db, title)
    if item is None:
        raise HTTPException(status_code=404, detail=f"KnowledgeItem '{title}' not found")
    return item


@router.get("/items/{title}/related", response_model=list[KnowledgeItem])
def list_related_items(title: str, db: Session = Depends(get_db)):
    item = get_item_with_relations(db, title)
    if item is None:
        raise HTTPException(status_code=404, detail=f"KnowledgeItem '{title}' not found")
    return find_related_items(db, title)


# --- Search ---


@router.get("/search", response_model=list[KnowledgeItem])
def search(q: str = Query(min_length=2, max_length=200), db: Session = Depends(get_db)):
    return search_items(db, q)
