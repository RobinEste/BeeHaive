# Changelog

Alle noemenswaardige wijzigingen aan dit project worden in dit bestand gedocumenteerd.

Het formaat is gebaseerd op [Keep a Changelog](https://keepachangelog.com/nl/1.0.0/).

---

## [Unreleased]

### Toegevoegd
- RAG pipeline met RAG-Anything/LightRAG en vLLM-MLX (#5)
  - Query endpoint (hybrid retrieval + LLM generatie)
  - Text en document ingest endpoints (PDF, DOCX, PPTX, TXT, MD)
  - Fail-closed API key auth met RAG_DEV_MODE escape hatch
  - Embedding batching (64), Qwen thinking-tag stripping
  - ADR-2026-002: lokaal LLM model keuze (Qwen3.5-9B-4bit)
- Security hardening: filename sanitisatie, timing-safe auth, shutdown guard
- Codebase audit met 5 gespecialiseerde agents (28 bevindingen)
- GitHub issues voor audit findings: #18 (security), #19 (tests), #20 (architectuur), #21 (privacy)
- FastAPI API-laag met 13 REST endpoints op de knowledge graph query-laag (#4)
- Pydantic response models voor BuildingBlock, Guardrail, KnowledgeItem, Topic, Author
- Neo4j session dependency injection via FastAPI Depends()
- `make run` target voor uvicorn dev server
- Project opgezet met Claude Code framework
- Projectstructuur voor Astro + FastAPI + Neo4j stack
- Knowledge management (docs/knowledge/, decisions/, solutions/)
- AI code review pipeline (code-review/)
- Query-laag voor knowledge graph: 13 read-only Cypher functies (queries.py)
- Case-insensitive zoeken met toLower + CONTAINS + LIMIT 50
- Gerelateerde items via gedeeld navigatiepatroon + LIMIT 25
- 21 integration tests voor alle query functies
- Makefile targets: lint, test, check, fix
- Pytest marker registratie voor integration tests

