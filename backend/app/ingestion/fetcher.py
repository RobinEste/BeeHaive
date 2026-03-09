"""Document fetcher for ingestion pipeline.

Fetches source documents from URLs with:
- SSRF prevention (private IP blocking, HTTPS-only)
- Rate limiting (1 req/sec)
- Retry with exponential backoff (max 3 attempts)
- Local file cache in data/fetched/

Source types:
- regulation / guideline / best_practice: HTML via httpx + trafilatura
- paper: PDF via RAG-Anything's process_document_complete()
"""

import hashlib
import ipaddress
import json
import logging
import socket
import threading
import time
from pathlib import Path

import httpx
import trafilatura

from app.ingestion.pii import redact_pii, scan_pii
from app.models.ingestion import FetchResult, SourceType

logger = logging.getLogger(__name__)

# Cache directory for fetched documents
CACHE_DIR = Path("data/fetched")

# Rate limiting state (thread-safe for asyncio.to_thread usage)
_rate_lock = threading.Lock()
_last_request_time: float = 0.0

# SSRF: blocked private IP ranges
_PRIVATE_NETWORKS = [
    ipaddress.ip_network("10.0.0.0/8"),
    ipaddress.ip_network("172.16.0.0/12"),
    ipaddress.ip_network("192.168.0.0/16"),
    ipaddress.ip_network("169.254.0.0/16"),
    ipaddress.ip_network("127.0.0.0/8"),
    ipaddress.ip_network("::1/128"),
    ipaddress.ip_network("fc00::/7"),
    ipaddress.ip_network("fe80::/10"),
]

MAX_RETRIES = 3
BACKOFF_BASE = 2.0  # seconds
CACHE_TTL_DAYS = 7  # AVG Art. 5(1)(e): storage limitation


def _url_hash(url: str) -> str:
    """Short hash for cache filenames."""
    return hashlib.sha256(url.encode()).hexdigest()[:12]


def _validate_url(url: str, allow_localhost: bool = False) -> None:
    """Validate URL against SSRF attacks.

    Raises ValueError if the URL is unsafe.
    """
    from urllib.parse import urlparse

    parsed = urlparse(url)

    # Only HTTPS allowed (except localhost in dev)
    if parsed.scheme != "https":
        if allow_localhost and parsed.scheme == "http" and parsed.hostname == "localhost":
            return
        raise ValueError(f"Only HTTPS URLs allowed, got: {parsed.scheme}")

    if not parsed.hostname:
        raise ValueError("URL has no hostname")

    # Resolve hostname and check against private IP ranges
    try:
        addr_infos = socket.getaddrinfo(parsed.hostname, None)
    except (socket.gaierror, OSError) as e:
        raise ValueError(f"DNS resolution failed for {parsed.hostname}: {e}")

    for addr_info in addr_infos:
        ip = ipaddress.ip_address(addr_info[4][0])
        for network in _PRIVATE_NETWORKS:
            if ip in network:
                raise ValueError(
                    f"URL resolves to private IP {ip} — blocked for SSRF prevention"
                )


def _rate_limit() -> None:
    """Enforce 1 request per second rate limit."""
    global _last_request_time
    with _rate_lock:
        now = time.monotonic()
        elapsed = now - _last_request_time
        if elapsed < 1.0:
            time.sleep(1.0 - elapsed)
        _last_request_time = time.monotonic()


def _get_cache_path(url: str) -> Path:
    """Get the cache file path for a URL."""
    return CACHE_DIR / f"{_url_hash(url)}.json"


def _read_cache(url: str) -> FetchResult | None:
    """Read a cached fetch result if it exists and is within TTL."""
    cache_path = _get_cache_path(url)
    if cache_path.exists():
        # Check TTL — remove expired cache files (AVG data retention)
        age_days = (time.time() - cache_path.stat().st_mtime) / 86400
        if age_days > CACHE_TTL_DAYS:
            logger.info("Cache expired for %s (%.0f days old)", url, age_days)
            cache_path.unlink(missing_ok=True)
            return None
        try:
            data = json.loads(cache_path.read_text())
            logger.info("Cache hit for %s", url)
            return FetchResult(**data)
        except (json.JSONDecodeError, KeyError):
            logger.warning("Corrupt cache for %s, removing", url)
            cache_path.unlink(missing_ok=True)
    return None


def _write_cache(url: str, result: FetchResult) -> None:
    """Write a fetch result to cache."""
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    cache_path = _get_cache_path(url)
    cache_path.write_text(result.model_dump_json(indent=2))


def fetch_html(url: str) -> FetchResult:
    """Fetch and extract text content from an HTML page.

    Uses trafilatura for content extraction (good for articles,
    blog posts, regulation pages).

    NOTE: This function is synchronous (httpx.get + time.sleep). It is
    designed for CLI usage (make ingest-item). If called from an async
    context (FastAPI), wrap in asyncio.to_thread() to avoid blocking.
    """
    _validate_url(url)

    # Check cache first
    cached = _read_cache(url)
    if cached:
        return cached

    last_error = None
    for attempt in range(MAX_RETRIES):
        _rate_limit()
        try:
            response = httpx.get(
                url,
                follow_redirects=False,
                timeout=30.0,
                headers={"User-Agent": "BeeHaive-Ingestion/0.1 (academic research)"},
            )
            if response.is_redirect:
                location = response.headers.get("location", "?")
                return FetchResult(
                    text="",
                    source_url=url,
                    fetch_status="failed",
                    metadata={"error": f"Redirect to {location} — not followed for SSRF safety"},
                )
            response.raise_for_status()

            text = trafilatura.extract(response.text)
            if not text:
                return FetchResult(
                    text="",
                    source_url=url,
                    fetch_status="failed",
                    metadata={"error": "trafilatura could not extract content"},
                )

            # AVG Art. 5(1)(c): redact PII before caching to disk
            pii_report = scan_pii(text)
            if not pii_report.error:
                text = redact_pii(text, pii_report)

            result = FetchResult(
                text=text,
                source_url=url,
                fetch_status="ok",
                metadata={
                    "content_length": len(text),
                    "status_code": response.status_code,
                },
            )
            _write_cache(url, result)
            return result

        except httpx.HTTPStatusError as e:
            last_error = f"HTTP {e.response.status_code}"
            logger.warning("Attempt %d failed for %s: %s", attempt + 1, url, last_error)
        except httpx.RequestError as e:
            last_error = str(e)
            logger.warning("Attempt %d failed for %s: %s", attempt + 1, url, last_error)

        if attempt < MAX_RETRIES - 1:
            backoff = BACKOFF_BASE ** (attempt + 1)
            time.sleep(backoff)

    return FetchResult(
        text="",
        source_url=url,
        fetch_status="failed",
        metadata={"error": last_error},
    )


def fetch_source(url: str, source_type: SourceType) -> FetchResult:
    """Fetch a source document based on its type.

    - regulation / guideline / best_practice: HTML extraction
    - paper: returns a stub — PDF processing is done via RAG-Anything
      in the pipeline orchestrator (requires async engine)
    """
    if source_type == "paper":
        # PDF processing requires RAG-Anything engine (async).
        # Return metadata-only result; pipeline handles PDF via engine.
        return FetchResult(
            text="",
            source_url=url,
            fetch_status="requires_pdf_processing",
            metadata={"source_type": "paper", "note": "PDF processing via RAG-Anything"},
        )

    return fetch_html(url)
