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

## BB/GR-content schrijven

Bij schrijven of substantieel herzien van `frontend/src/content/building-blocks/*.mdx` of `frontend/src/content/guardrails/*.mdx`: roep de skill `/bb-write` aan vóór de eerste Write/Edit. Die laadt de stijlgids en dwingt een pre-write-scan af.

Drie hard rules die altijd gelden, ook bij kleine edits:

1. **Geen losse em-dashes** in NL-tekst. Em-dashes alleen in paren rond een tussenzin. Vervang door `:` (expliciteert), `;` (gelijkwaardige delen) of `,` (korte toevoeging). Engelse citaten mogen em-dashes behouden.
2. **Na vetgedrukt onderwerp `:`, geen `—`**. Voorbeeld: `**Tier 2, hoog risico**:` niet `**Tier 2 — Hoog risico**:`.
3. **Koppen in gewone-woorden-toets**. Vermijd `-architectuur`, `-engine`, `-tijdperk`, `-pijplijn` in koppen.

Volledige gids: `.claude/schrijfstijl-bb.md` (18 secties; lees minimaal §1, §4, §8, §10, §13, §14, §17, §18 vóór een BB/GR-sessie).
