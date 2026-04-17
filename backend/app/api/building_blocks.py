"""API endpoints for BuildingBlocks."""

from fastapi import APIRouter, Depends, HTTPException
from neo4j import Session

from app.dependencies import get_db
from app.graph.queries import (
    get_all_building_blocks,
    get_building_block,
    get_items_by_building_block,
    get_tools_for_building_block,
)
from app.models.schemas import BuildingBlock, KnowledgeItem, Tool

router = APIRouter(prefix="/building-blocks", tags=["building-blocks"])


@router.get("", response_model=list[BuildingBlock])
def list_building_blocks(db: Session = Depends(get_db)):
    return get_all_building_blocks(db)


@router.get("/{name}", response_model=BuildingBlock)
def read_building_block(name: str, db: Session = Depends(get_db)):
    bb = get_building_block(db, name)
    if bb is None:
        raise HTTPException(status_code=404, detail=f"BuildingBlock '{name}' not found")
    return bb


@router.get("/{name}/items", response_model=list[KnowledgeItem])
def list_items_for_building_block(name: str, db: Session = Depends(get_db)):
    bb = get_building_block(db, name)
    if bb is None:
        raise HTTPException(status_code=404, detail=f"BuildingBlock '{name}' not found")
    return get_items_by_building_block(db, name)


@router.get("/{name}/tools", response_model=list[Tool])
def list_tools_for_building_block(name: str, db: Session = Depends(get_db)):
    bb = get_building_block(db, name)
    if bb is None:
        raise HTTPException(status_code=404, detail=f"BuildingBlock '{name}' not found")
    return get_tools_for_building_block(db, name)
