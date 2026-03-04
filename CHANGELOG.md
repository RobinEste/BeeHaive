# Changelog

Alle noemenswaardige wijzigingen aan dit project worden in dit bestand gedocumenteerd.

Het formaat is gebaseerd op [Keep a Changelog](https://keepachangelog.com/nl/1.0.0/).

---

## [Unreleased]

### Toegevoegd
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

