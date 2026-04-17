"""Shared Gemini client for ingestion-time LLM calls.

Both the taxonomy classifier (llm.py) and the NL summarizer (summarizer.py)
reuse the same lazy-initialised client instance so the google-genai SDK and
GEMINI_API_KEY env var are configured in exactly one place.
"""

import os

from google import genai


class GeminiUnavailable(RuntimeError):
    """Raised when GEMINI_API_KEY is missing or the client cannot initialise."""


_client: genai.Client | None = None


def get_gemini_client() -> genai.Client:
    global _client
    if _client is None:
        api_key = os.getenv("GEMINI_API_KEY", "")
        if not api_key:
            raise GeminiUnavailable(
                "GEMINI_API_KEY is not set. "
                "Get a key at https://aistudio.google.com/apikey"
            )
        _client = genai.Client(api_key=api_key)
    return _client
