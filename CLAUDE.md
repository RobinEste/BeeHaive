# Claude Code Instructies - BeeHaive

Dit bestand bevat standaard werkafspraken voor dit project. **Claude leest dit bestand automatisch bij elke nieuwe sessie.**

---

## Leerstand & Communicatiestijl

> **Werkafspraak:** Robin leert actief mee tijdens het ontwikkelen. Claude legt bij elke stap uit wat er gebeurt.

### Wat dit betekent in de praktijk
- **Bij elk commando:** Leg kort uit wat het doet en waarom we het gebruiken
- **Bij code wijzigingen:** Beschrijf wat je verandert, welk patroon je toepast en waarom
- **Bij architectuurkeuzes:** Leg de afweging uit en waarom je voor deze aanpak kiest
- **Bij errors/problemen:** Leg uit wat de foutmelding betekent en hoe de oplossing werkt

---

## Workflow bij ontwikkeltaken

```
Ontwikkelen → Testen → /review → Fixes → Documentatie → Committen → Pushen
```

| Stap | Actie |
|------|-------|
| **Ontwikkelen** | Raadpleeg eerst bestaande code en documentatie |
| **Testen** | Run `make check` (of individueel: `make lint`, `make test`) na wijzigingen |
| **Code review** | Draai `/review` voor AI code review op de uncommitted changes |
| **Fixes** | Los eventuele review bevindingen op, draai `/compound` voor opgeloste patronen |
| **Documentatie** | Update ROADMAP.md, CHANGELOG.md en relevante docs |
| **Committen** | Nederlandse commit messages, conventional commits style |
| **Pushen** | Push naar GitHub na succesvolle tests |

---

## Documentatie Bijwerken

### Wanneer documentatie bijwerken
**Na elke succesvolle test van code wijzigingen**, update de relevante documentatie:
- Versienummer ophogen
- Datum bijwerken
- Changelog sectie updaten

### Bij afgeronde taken
- [ ] Update `ROADMAP.md` - vink voltooide taken af
- [ ] Update `CHANGELOG.md` - voeg wijzigingen toe onder juiste versie

### Knowledge Management

Het project heeft drie kennissystemen die samen een "compound learning loop" vormen:

| Systeem | Doel | Trigger |
|---------|------|---------|
| **Solution documents** (`docs/solutions/`) | Opgeloste code review patronen | `/compound` na `/review` |
| **Knowledge entries** (`docs/knowledge/`) | Sessie-inzichten per categorie | `/sessie-reflectie` |
| **Architecture Decision Records** (`docs/decisions/`) | Architectuurbeslissingen met rationale | Handmatig bij significante keuzes |

---

## Code Quality

### Altijd runnen voor commits
```bash
make check        # Alle blocking checks in een keer
make fix          # Auto-fix wat kan, dan checken
/review           # AI code review (bij significante wijzigingen)
```

---

## Git Workflow

### Commit messages
- **Taal:** Nederlands
- **Stijl:** Conventional commits
- **Format:** `type: beschrijving`

**Types:**
- `feat:` - Nieuwe functionaliteit
- `fix:` - Bug fix
- `docs:` - Documentatie wijzigingen
- `refactor:` - Code refactoring
- `style:` - Code formatting, linting
- `test:` - Tests toevoegen of aanpassen
- `chore:` - Build, dependencies, configuratie

---

## Project Structuur

```
BeeHaive/
├── frontend/              # Astro + React islands (beehaive.org)
│   ├── src/
│   │   ├── pages/         # Astro pagina's (blogs, framework, trainingen)
│   │   ├── components/    # Astro + React componenten
│   │   ├── layouts/       # Page layouts
│   │   └── content/       # Markdown/MDX content (blogs, kennisbank)
│   ├── public/            # Static assets
│   ├── astro.config.mjs
│   └── package.json
├── backend/               # Python FastAPI (API + AI pipeline)
│   ├── app/
│   │   ├── api/           # API endpoints
│   │   ├── services/      # Business logic + AI services
│   │   ├── models/        # Pydantic models + DB schemas
│   │   ├── graph/         # Neo4j knowledge graph queries
│   │   └── config/        # Settings en configuratie
│   ├── scripts/       # CLI scripts (seed, migraties)
│   ├── tests/
│   ├── pyproject.toml
│   └── Dockerfile
├── docs/                  # Technische documentatie
│   ├── knowledge/         # Sessie-kennisbank
│   ├── decisions/         # Architecture Decision Records
│   └── solutions/         # Compound learning
├── docker-compose.yml     # Neo4j + PostgreSQL + services
├── ROADMAP.md             # Project roadmap & taken
├── CHANGELOG.md           # Versie geschiedenis
└── README.md              # Project overzicht
```

### Tech Stack

| Component | Technologie | Doel |
|-----------|------------|------|
| Frontend | Astro + React islands | Website, blogs, trainingen |
| Backend API | Python FastAPI | API, AI pipeline, knowledge graph |
| Knowledge Graph | Neo4j Community | Knowledge items, relaties, doorzoekbaarheid |
| Relationele DB | PostgreSQL | Users, cursussen, betalingen |
| Auth | Auth.js (via Astro) | OAuth (Google, GitHub, etc.) |
| Betalingen | Mollie | iDEAL, creditcard (NL/EU) |
| Hosting | Hetzner | EU data residency |
| AI/LLM | Claude API | Content generatie, RAG |

---

## Slash Commands

Beschikbare Claude Code slash commands:

| Command | Beschrijving |
|---------|-------------|
| `/sessie-start` | Start een sessie: laadt context, roadmap, changelog + git status |
| `/sessie-eind` | Einde-sessie checklist: changes, docs, make check, werklog bijwerken |
| `/status` | Lichtgewicht statusoverzicht: git + roadmap + changelog |
| `/review` | Start AI code review met gespecialiseerde agents |
| `/audit` | Volledige codebase audit met agent teams |
| `/qa-gate` | Quality gate: make check + review in één stap |
| `/compound [finding-id]` | Leg opgelost review issue vast als solution document |
| `/sessie-reflectie` | Analyseer sessie en extraheer inzichten naar docs/knowledge/ |
| `/changelog [type: beschrijving]` | Voeg een entry toe aan CHANGELOG.md |
| `/review-stats` | Toon review statistieken en metrics |

---

## Checklist: Einde van sessie

- [ ] Alle code wijzigingen zijn klaar om te committen
- [ ] `/review` gedraaid op significante code wijzigingen
- [ ] `ROADMAP.md` is bijgewerkt (indien taken afgerond)
- [ ] `CHANGELOG.md` is bijgewerkt (bij elke feat/fix/refactor)
- [ ] Werklog bijgewerkt (`.claude/worklog.md`)
- [ ] Linting passed (geen errors)
