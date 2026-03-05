# Changelog

Alle noemenswaardige wijzigingen aan dit project worden in dit bestand gedocumenteerd.

Het formaat is gebaseerd op [Keep a Changelog](https://keepachangelog.com/nl/1.0.0/).

---

## [Unreleased]

### Toegevoegd
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

