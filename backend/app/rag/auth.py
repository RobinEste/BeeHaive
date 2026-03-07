"""Simple API key authentication for RAG endpoints.

Temporary solution until full auth middleware is implemented (Stap 10, #10).
Set RAG_API_KEY in .env to enable. Set RAG_DEV_MODE=true to allow open access in dev.
"""

import hmac
import logging
import os

from fastapi import HTTPException, Security
from fastapi.security import APIKeyHeader

_logger = logging.getLogger(__name__)
_api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False)
_RAG_API_KEY = os.getenv("RAG_API_KEY")
_DEV_MODE = os.getenv("RAG_DEV_MODE", "false").lower() == "true"

if not _RAG_API_KEY and not _DEV_MODE:
    _logger.warning("RAG_API_KEY niet gezet en RAG_DEV_MODE niet actief — RAG endpoints geblokkeerd")


async def require_api_key(api_key: str | None = Security(_api_key_header)) -> str:
    """Validate API key. Fail-closed: blocks if no key configured unless dev mode."""
    if _RAG_API_KEY is None:
        if _DEV_MODE:
            return "dev-mode"
        raise HTTPException(status_code=503, detail="RAG API key niet geconfigureerd")
    if not hmac.compare_digest(api_key or "", _RAG_API_KEY):
        raise HTTPException(status_code=401, detail="Ongeldige of ontbrekende API key")
    return api_key
