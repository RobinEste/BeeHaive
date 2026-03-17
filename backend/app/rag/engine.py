"""RAG engine initialisation.

Creates and configures a RAGAnything instance backed by:
- Neo4j for graph storage (same instance as the knowledge graph)
- Gemini API for LLM (entity extraction) and embeddings (vector search)

Provider is configurable via env vars (see config.py / ADR-2026-003).

Usage:
    engine = await create_rag_engine()
    result = await engine.aquery("What is Trustworthy AI?", mode="hybrid")
"""

import asyncio
import os
import re

import numpy as np
import openai as _openai
from lightrag import LightRAG
from lightrag.utils import EmbeddingFunc
from raganything import RAGAnything, RAGAnythingConfig

from app.rag.config import (
    LLM_BASE_URL,
    LLM_API_KEY,
    LLM_MODEL,
    EMBEDDING_MODEL,
    EMBEDDING_DIM,
    EMBEDDING_MAX_TOKENS,
    RAG_WORKING_DIR,
)

# Shared OpenAI-compatible client — reused across LLM and embedding calls
_oai_client = _openai.AsyncOpenAI(api_key=LLM_API_KEY, base_url=LLM_BASE_URL)

# Singleton — initialised once, reused across requests
_engine: RAGAnything | None = None
_engine_lock = asyncio.Lock()


def _strip_thinking(text: str) -> str:
    """Strip LLM thinking blocks, keeping only the actual answer.

    Some models (Qwen, Gemini with thinking enabled) wrap reasoning in
    <think>...</think> tags. This function removes those blocks.
    """
    if not text:
        return text
    # Remove all <think>...</think> blocks (greedy within each block)
    stripped = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL)
    return stripped.strip() or text.strip()


async def _llm_func(prompt, system_prompt=None, history_messages=None, **kwargs):
    """LLM function that calls the configured API via OpenAI-compatible client.

    Bypasses openai_complete_if_cache entirely to avoid response_format issues.
    Strips thinking blocks from models that emit them (Qwen, Gemini).
    """
    if history_messages is None:
        history_messages = []

    # Strip LightRAG-specific kwargs that the API doesn't understand
    kwargs.pop("keyword_extraction", None)
    kwargs.pop("response_format", None)
    kwargs.pop("hashing_kv", None)

    messages = []
    if system_prompt:
        messages.append({"role": "system", "content": system_prompt})
    messages.extend(history_messages)
    messages.append({"role": "user", "content": prompt})

    response = await _oai_client.chat.completions.create(
        model=LLM_MODEL,
        messages=messages,
        max_tokens=kwargs.get("max_tokens", 2048),
    )

    if not response.choices:
        return ""
    result = response.choices[0].message.content or ""
    return _strip_thinking(result)


async def _embedding_func(texts: list[str]) -> list[list[float]]:
    """Embedding function via OpenAI-compatible client.

    Bypasses LightRAG's openai_embed to avoid dimension mismatch issues.
    Processes in batches of 64 to stay within API limits.
    """
    if not texts:
        return np.empty((0, EMBEDDING_DIM), dtype=np.float32)

    BATCH_SIZE = 64
    all_embeddings = []
    for i in range(0, len(texts), BATCH_SIZE):
        batch = texts[i : i + BATCH_SIZE]
        response = await _oai_client.embeddings.create(model=EMBEDDING_MODEL, input=batch)
        all_embeddings.extend([dp.embedding for dp in response.data])
    return np.array(all_embeddings, dtype=np.float32)


def _build_lightrag() -> LightRAG:
    """Create a LightRAG instance configured for Neo4j + external LLM API."""
    return LightRAG(
        working_dir=RAG_WORKING_DIR,
        graph_storage="Neo4JStorage",
        llm_model_func=_llm_func,
        embedding_func=EmbeddingFunc(
            embedding_dim=EMBEDDING_DIM,
            max_token_size=EMBEDDING_MAX_TOKENS,
            func=_embedding_func,
        ),
    )


async def create_rag_engine() -> RAGAnything:
    """Create and initialise the RAG engine (singleton).

    First call downloads/loads models and connects to Neo4j.
    Subsequent calls return the cached instance.
    """
    global _engine
    if _engine is not None:
        return _engine

    async with _engine_lock:
        # Double-check after acquiring lock
        if _engine is not None:
            return _engine

        lightrag = _build_lightrag()
        await lightrag.initialize_storages()

        from lightrag.kg.shared_storage import initialize_pipeline_status
        await initialize_pipeline_status()

        config = RAGAnythingConfig(
            working_dir=RAG_WORKING_DIR,
            enable_image_processing=False,   # enable later when vision model is added
            enable_table_processing=True,
            enable_equation_processing=False,
        )

        _engine = RAGAnything(
            lightrag=lightrag,
            llm_model_func=_llm_func,
            embedding_func=_embedding_func,
            config=config,
        )

        return _engine


async def get_rag_engine() -> RAGAnything:
    """FastAPI dependency — returns the initialised RAG engine."""
    try:
        return await create_rag_engine()
    except Exception as e:
        from fastapi import HTTPException
        raise HTTPException(
            status_code=503,
            detail="RAG engine niet beschikbaar. Controleer GEMINI_API_KEY en connectiviteit.",
        ) from e


async def ingest_text(engine: RAGAnything, text: str) -> None:
    """Ingest plain text into the knowledge graph via LightRAG."""
    await engine.lightrag.ainsert(text)


async def ingest_document(engine: RAGAnything, file_path: str) -> None:
    """Ingest a document (PDF, DOCX, etc.) via RAG-Anything."""
    await engine.process_document_complete(
        file_path=file_path,
        output_dir=os.path.join(RAG_WORKING_DIR, "parsed"),
    )


async def shutdown_engine() -> None:
    """Clean up the RAG engine singleton and its resources."""
    global _engine
    if _engine is not None and hasattr(_engine, "lightrag"):
        lightrag = _engine.lightrag
        if hasattr(lightrag, "finalize_storages"):
            await lightrag.finalize_storages()
    _engine = None
