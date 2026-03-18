# Changelog

Alle noemenswaardige wijzigingen aan dit project worden in dit bestand gedocumenteerd.

Het formaat is gebaseerd op [Keep a Changelog](https://keepachangelog.com/nl/1.0.0/).

---

## [Unreleased]

### Toegevoegd
- Kalibratiescript, DATA_GLOSSARY, blocked_authors + Gemini 3.1 Pro upgrade (#7)
  - `calibrate_mapper.py` — valideert taxonomy mapper tegen seed.py (BB 77%, GR 74% precision)
  - `DATA_GLOSSARY.md` — verwerkingsregister met LIA, bezwaarprocedure Art. 21, data flow diagram
  - `blocked_authors.txt` + fail-secure check in pipeline (Art. 21 AVG)
  - Gemini 3.1 Pro als default classifier (was 2.5 Flash)
  - BB/GR definities afgestemd op Notion framework-beschrijvingen
  - seed.py Knowledge-labels herzien naar Notion-definitie (menselijke expertise)
  - `make calibrate` target, PLAN-007 v7
- Ingestion pipeline fase 2-3: taxonomy mapper, orchestrator, CLI, dual ingest (#7)
  - `llm.py` — Gemini 2.5 Flash taxonomy classifier met structured output
  - `pipeline.py` — orchestrator: dedup → fetch → PII → classify → persist → LightRAG
  - `ingest_item.py` — CLI met preview/commit modus (`make ingest-item`)
  - Dual ingest: items gaan naar zowel Neo4j (knowledge graph) als LightRAG (RAG queries)
  - Mapping-dedup per (entity_type, matched_name), hoogste confidence behouden
  - Async-safe bridge (`_run_async`) voor CLI + FastAPI compatibiliteit
  - `rag_synced` veld signaleert gefaalde LightRAG ingest
  - RAG config gemigreerd van vLLM-MLX naar Gemini API (ADR-2026-003)
  - `google-genai` dependency toegevoegd
  - 31 unit tests (21 LLM + 10 pipeline), /review met 6 findings — alle gefixt
- Ingestion pipeline fase 1: fetcher, PII scanner, graph mutations (#7)
  - Document fetcher met SSRF-preventie (HTTPS-only, private IP blocking, redirect blokkering)
  - Thread-safe rate limiter (1 req/sec) met retry + exponential backoff
  - PII scanner (fail-closed, email+phone regex, overlap filter, AVG-conform)
  - Cache met PII-redactie vóór persistentie (AVG Art. 5(1)(c))
  - Graph mutations: batched UNWIND, MERGE op source_url, ON MATCH SET voor heringest
  - Deduplicatie queries: exact source_url match + fuzzy title search
  - 34 tests, 3 review-rondes (21 findings gefixt)
- Knowledge graph uitgebreid met 34 KnowledgeItems (#6)
  - 24 items uit Notion: papers, regulations en best practices per building block
  - 10 recente papers (maart 2026): agentic RAG, AI governance, evaluatie, robustness
  - Seed functie herstructureerd voor meerdere relaties per item
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

### Gewijzigd
- Integration tests gebruiken nu geïsoleerd _TEST_ dataset (onafhankelijk van productie seed)

