# BeeHaive

AI knowledge framework voor verantwoorde AI-implementatie, gebaseerd op 7 bouwstenen en 7 EU Trustworthy AI guardrails.

## Wat is BeeHaive?

BeeHaive helpt organisaties bij het implementeren van AI op een verantwoorde manier. Het framework combineert:

- **7 Bouwstenen** — Knowledge, Client Blueprint, Dynamic Context, Prompt Design, Tool Integration, Model Engines, Evaluation Loop
- **7 Guardrails** — gebaseerd op de EU AI Act: Human Agency, Robustness, Privacy, Fairness, Transparency, Well-being, Accountability

Kennis uit diverse bronnen (regelgeving, papers, video's, best practices) wordt opgeslagen in een knowledge graph en ontsloten via een website, API en trainingsportaal.

## Tech Stack

| Component | Technologie |
|-----------|------------|
| Frontend | Astro + React islands |
| Backend API | Python FastAPI |
| Knowledge Graph | Neo4j Community |
| Relationele DB | PostgreSQL |
| RAG Pipeline | RAG-Anything (LightRAG) |
| LLM (self-hosted) | Qwen 3.5 via vLLM |
| Embeddings | bge-m3 of gte-Qwen2 via vLLM |
| Auth | Auth.js (via Astro) |
| Betalingen | Mollie (iDEAL, creditcard) |
| Hosting | Hetzner (EU data residency) |

## Project Status

| Fase | Status |
|------|--------|
| Fase 1: Project Foundation | ✅ Compleet |
| Fase 2: Knowledge Graph | 🟡 In progress |
| Fase 3: Frontend Website | 🔴 Te doen |
| Fase 4: Backend API | 🔴 Te doen |
| Fase 5: Training Portal | 🔴 Te doen |
| Fase 6: Betalingen & Launch | 🔴 Te doen |

Zie [ROADMAP.md](ROADMAP.md) voor het volledige overzicht met issue-referenties.

## Wat is er klaar?

- Neo4j knowledge graph met 7 BuildingBlocks, 7 Guardrails, Topics, Authors en KnowledgeItems
- 13 read-only Cypher query functies (parameterized, case-insensitive search, related items)
- 21 integration tests
- Makefile met lint, test, check en fix targets

## Quickstart

### Vereisten

- Python 3.13+
- Docker (voor Neo4j)

### Setup

```bash
# Virtual environment en dependencies
make setup

# Neo4j starten en seed data laden
make graph-up
make graph-seed

# Tests draaien
make check
```

### Makefile targets

| Target | Beschrijving |
|--------|-------------|
| `make setup` | Virtual environment + dependencies installeren |
| `make graph-up` | Neo4j starten via Docker Compose |
| `make graph-seed` | Schema + seed data laden in Neo4j |
| `make lint` | Ruff linting |
| `make test` | Integration tests (vereist draaiende Neo4j) |
| `make check` | Lint + test in één keer |
| `make fix` | Auto-fix linting issues |

## Architectuur

```
BeeHaive/
├── frontend/              # Astro + React islands (beehaive.org)
├── backend/               # Python FastAPI + Neo4j query-laag
│   ├── app/
│   │   ├── graph/         # Neo4j connection, schema, seed, queries
│   │   └── config/        # Environment configuratie
│   └── tests/             # Integration tests
├── docs/                  # Technische documentatie
│   ├── knowledge/         # Sessie-inzichten per categorie
│   ├── decisions/         # Architecture Decision Records
│   ├── solutions/         # Compound learning (opgeloste patronen)
│   └── course-comparison.md  # Vergelijking met Multi-Agent Course
├── docker-compose.yml     # Neo4j + services
├── Makefile               # Build targets
├── ROADMAP.md             # Roadmap met issue-referenties
└── CHANGELOG.md           # Versiegeschiedenis
```

## Bronnen & Multimodale Content

BeeHaive verwerkt diverse brontypen als KnowledgeItems:

- **Tekst** — EU regelgeving, papers, guidelines, best practices
- **PDF** — rapporten, whitepapers
- **Video** — YouTube talks, conferenties, tutorials (via RAG-Anything)
- **Tabellen/grafieken** — gestructureerde data uit documenten en presentaties

De RAG pipeline (RAG-Anything, gebouwd op LightRAG) combineert multimodale parsing met graph-based hybrid retrieval (vector + graph traversal).

## Privacy & Data Residency

- Alle productiedata blijft binnen de EU (Hetzner)
- LLM en embeddings draaien self-hosted via vLLM — geen data naar externe services
- AVG/GDPR compliant by design
- Zie [globale privacy policy](https://github.com/RobinEste/BeeHaive/blob/main/CLAUDE.md) voor details

## Cursus Context

Dit project wordt parallel ontwikkeld als werkstuk voor de [Multi-Agent Course](https://github.com/hamzafarooq/multi-agent-course) (Module 4: Knowledge Graphs). Zie [docs/course-comparison.md](docs/course-comparison.md) voor een vergelijking van aanpakken.
