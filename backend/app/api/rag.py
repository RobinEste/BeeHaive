"""API endpoints for RAG pipeline — query and ingest."""

import os
import re
import tempfile
from typing import Literal

from fastapi import APIRouter, Depends, HTTPException, UploadFile
from pydantic import BaseModel, Field
from raganything import RAGAnything

from app.rag.auth import require_api_key
from app.rag.engine import get_rag_engine
from app.rag.engine import ingest_text as engine_ingest_text
from app.rag.engine import ingest_document as engine_ingest_document

router = APIRouter(prefix="/rag", tags=["rag"])

RAGMode = Literal["local", "global", "hybrid", "naive", "mix"]
ALLOWED_EXTENSIONS = {".pdf", ".docx", ".pptx", ".txt", ".md"}
MAX_UPLOAD_SIZE = 50 * 1024 * 1024  # 50 MB


class RAGQueryRequest(BaseModel):
    question: str = Field(min_length=1)
    mode: RAGMode = "hybrid"


class RAGQueryResponse(BaseModel):
    answer: str
    mode: RAGMode


class IngestTextRequest(BaseModel):
    text: str = Field(min_length=1)
    description: str | None = None


class IngestResponse(BaseModel):
    status: Literal["ok"] = "ok"
    message: str


@router.post("/query", response_model=RAGQueryResponse)
async def rag_query(
    req: RAGQueryRequest,
    engine: RAGAnything = Depends(get_rag_engine),
    _key: str = Depends(require_api_key),
):
    """Query the knowledge graph using RAG (hybrid retrieval + LLM generation)."""
    try:
        answer = await engine.aquery(req.question, mode=req.mode)
    except Exception as exc:
        raise HTTPException(
            status_code=502,
            detail="RAG query mislukt — controleer of vLLM-MLX en Neo4j bereikbaar zijn.",
        ) from exc
    if answer is None:
        answer = "No answer could be generated from the available knowledge."
    return RAGQueryResponse(answer=answer, mode=req.mode)


@router.post("/ingest/text", response_model=IngestResponse)
async def ingest_text_endpoint(
    req: IngestTextRequest,
    engine: RAGAnything = Depends(get_rag_engine),
    _key: str = Depends(require_api_key),
):
    """Ingest plain text into the knowledge graph."""
    try:
        await engine_ingest_text(engine, req.text)
    except Exception as exc:
        raise HTTPException(
            status_code=502,
            detail="Text ingest mislukt — controleer of vLLM-MLX en Neo4j bereikbaar zijn.",
        ) from exc
    return IngestResponse(message="Text ingested successfully")


@router.post("/ingest/document", response_model=IngestResponse)
async def ingest_document_endpoint(
    file: UploadFile,
    engine: RAGAnything = Depends(get_rag_engine),
    _key: str = Depends(require_api_key),
):
    """Ingest a document (PDF, DOCX, etc.) into the knowledge graph."""
    filename = os.path.basename(file.filename or "")
    if not filename or not re.match(r"^[\w.\- ]+$", filename):
        raise HTTPException(status_code=400, detail="Ongeldige bestandsnaam")
    suffix = os.path.splitext(filename)[1].lower()
    if suffix not in ALLOWED_EXTENSIONS:
        raise HTTPException(status_code=400, detail=f"Bestandstype '{suffix}' niet toegestaan")

    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        size = 0
        while chunk := await file.read(8192):
            size += len(chunk)
            if size > MAX_UPLOAD_SIZE:
                os.unlink(tmp.name)
                raise HTTPException(status_code=413, detail="Bestand te groot (max 50 MB)")
            tmp.write(chunk)
        tmp_path = tmp.name

    try:
        await engine_ingest_document(engine, tmp_path)
    except Exception as exc:
        os.unlink(tmp_path)
        raise HTTPException(
            status_code=502,
            detail="Document ingest mislukt — controleer of vLLM-MLX en Neo4j bereikbaar zijn.",
        ) from exc
    finally:
        if os.path.exists(tmp_path):
            os.unlink(tmp_path)
