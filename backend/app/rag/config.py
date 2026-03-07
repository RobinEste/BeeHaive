"""RAG pipeline configuration.

Centralises all settings for the vLLM-MLX server and RAG-Anything/LightRAG.
Values come from environment variables with sensible dev defaults.
"""

import os

# vLLM-MLX server (runs locally on Apple Silicon)
VLLM_BASE_URL = os.getenv("VLLM_BASE_URL", "http://localhost:8100/v1")
VLLM_API_KEY = os.getenv("VLLM_API_KEY", "dummy-key")

# Model names (must match what vLLM-MLX is serving)
LLM_MODEL = os.getenv("LLM_MODEL", "mlx-community/Qwen3.5-9B-4bit")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "mlx-community/multilingual-e5-large-mlx")

# Embedding dimensions for multilingual-e5-large
EMBEDDING_DIM = int(os.getenv("EMBEDDING_DIM", "1024"))
EMBEDDING_MAX_TOKENS = int(os.getenv("EMBEDDING_MAX_TOKENS", "512"))

# LightRAG / RAG-Anything storage
RAG_WORKING_DIR = os.getenv("RAG_WORKING_DIR", "./rag_storage")
