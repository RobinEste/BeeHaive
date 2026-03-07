# BeeHaive

AI knowledge framework — website, cursussen, knowledge graph. beehaive.org.

## Tech Stack

| Component | Technologie |
|-----------|------------|
| Frontend | Astro + React islands |
| Backend API | Python FastAPI |
| Knowledge Graph | Neo4j Community |
| Relationele DB | PostgreSQL |
| Auth | Auth.js (via Astro) |
| Betalingen | Mollie (iDEAL, creditcard) |
| Hosting | Hetzner (EU) |
| AI/LLM | Claude API |

## Development

```bash
make check    # Alle quality gates
make fix      # Auto-fix
```

## Structuur

```
frontend/
  src/
    pages/         # Astro pagina's (blogs, framework, trainingen)
    components/    # Astro + React componenten
    content/       # Markdown/MDX content
backend/
  app/
    api/           # API endpoints
    services/      # Business logic + AI services
    graph/         # Neo4j knowledge graph queries
docker-compose.yml # Neo4j + PostgreSQL + services
```
