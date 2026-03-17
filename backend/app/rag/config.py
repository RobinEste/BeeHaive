"""RAG pipeline configuration.

Centralises all settings for the LLM/embedding API and RAG-Anything/LightRAG.
Values come from environment variables with sensible dev defaults.

Default provider: Gemini via OpenAI-compatible endpoint (ADR-2026-003).
"""

import os

# LLM API (OpenAI-compatible endpoint)
# Default: Gemini 2.5 Flash via Google AI Studio
LLM_BASE_URL = os.getenv(
    "LLM_BASE_URL",
    "https://generativelanguage.googleapis.com/v1beta/openai/",
)
LLM_API_KEY = os.getenv("GEMINI_API_KEY", "")
LLM_MODEL = os.getenv("LLM_MODEL", "gemini-2.5-flash")

# Embedding model (same OpenAI-compatible endpoint)
# Default: Gemini text-embedding-004 (768 dimensions)
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "text-embedding-004")
EMBEDDING_DIM = int(os.getenv("EMBEDDING_DIM", "768"))
EMBEDDING_MAX_TOKENS = int(os.getenv("EMBEDDING_MAX_TOKENS", "2048"))

# LightRAG / RAG-Anything storage
RAG_WORKING_DIR = os.getenv("RAG_WORKING_DIR", "./rag_storage")
