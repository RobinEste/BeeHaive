# BeeHaive — Project Overview (Audit Context)

## Wat is BeeHaive?
AI knowledge framework voor website, cursussen en knowledge graph. Domein: beehaive.org.

## Tech Stack
| Component | Technologie |
|-----------|------------|
| Backend API | Python FastAPI |
| Knowledge Graph | Neo4j Community |
| Relationele DB | PostgreSQL (gepland) |
| RAG Pipeline | RAG-Anything / LightRAG + vLLM-MLX |
| LLM | Qwen3.5-9B-4bit (lokaal, Apple Silicon) |
| Embeddings | multilingual-e5-large-mlx (lokaal) |
| Hosting | Hetzner (EU) |

## Module Structuur
- `backend/app/api/` — FastAPI endpoints (building_blocks, guardrails, items, rag)
- `backend/app/graph/` — Neo4j connection, schema, queries, seed data
- `backend/app/rag/` — RAG engine (singleton), auth, config
- `backend/app/models/` — Pydantic schemas
- `backend/scripts/` — CLI scripts (seed_graph)
- `backend/tests/` — pytest tests

## Huidige Fase
Vroege ontwikkeling — knowledge graph query layer en RAG pipeline net opgezet. Geen frontend code nog. Geen PostgreSQL/SQLAlchemy nog. Geen auth systeem behalve simpele API key op RAG endpoints.

## Belangrijke Patronen
- Neo4j driver via `get_neo4j_driver()` dependency
- RAG engine singleton met `asyncio.Lock` voor thread-safe init
- Fail-closed API key auth met `RAG_DEV_MODE` escape hatch
- vLLM-MLX als OpenAI-compatible lokale inference server
