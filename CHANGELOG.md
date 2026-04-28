# Changelog

Alle noemenswaardige wijzigingen aan dit project worden in dit bestand gedocumenteerd.

Het formaat is gebaseerd op [Keep a Changelog](https://keepachangelog.com/nl/1.0.0/).

---

## [Unreleased]

### Toegevoegd (sessie 2026-04-28)
- Training-design naslagwerk `docs/research/TRAINING-DESIGN.md` (#33) — 894-regels synthese van zes onderzoeksrapporten (didactiek, retentie, AI-tutor) tot per-dimensie ontwerpkeuzes met evidence-rating en BeeHaive-vertaling; checklist per nieuwe training in Bijlage B; anti-patroon-lijst in Bijlage A (VAK, 70:20:10, Learning Pyramid)
- Lokale skill `/training-ontwerper` (`.claude/skills/training-ontwerper/`) — produceert concrete training-ontwerpen in `docs/trainings/<datum>/ontwerp.md` op basis van het naslagwerk, met scope-vragen, dimensie-loop en hard goedkeuringsgate

## [0.2.0] - 2026-04-20

### Toegevoegd (sessie 2026-04-17)
- Research-sectie dynamisch op BB-detailpagina (#23 Fase B deel 1) — build-time fetch van KnowledgeItems uit Neo4j, top 3 per BB gesorteerd op `curation_score DESC, title`, graceful fallback op lege state bij API-uitval
- `KnowledgeItem` uitgebreid met `curation_score` (int, default 0) + `summary_nl` (str, optional); alle 34 seed-items voorzien van Nederlandse samenvatting en editorial score
- `Tool` node-label in Neo4j met `DISPLAYED_ON` curation-relatie (met `display_order` op de edge) naast `RELATES_TO` / `ADDRESSES` / `REFERENCES` — scheidt redactionele keuze van inhoudelijke breedte
- Tools & Products sectie op BB-detailpagina (2-koloms card-grid, max 4 op de pagina + "Alle tools voor X" link) — 5 tools voor Prompt Design: LangSmith, Langfuse, Promptfoo, Guardrails AI, Anthropic Workbench
- Automatische NL-samenvatting in ingestion pipeline via Gemini (stap 4b tussen classify en persist); `ingest_item.py` ondersteunt `--summary-nl` en `--curation-score` CLI-overrides
- `gemini_client.py` shared helper — lazy client-init hergebruikt door taxonomie-classifier en summarizer
- `ToolCategory` als Pydantic `Literal[open_source, framework, enterprise, saas]`, matching frontend union
- `DEFAULT_DISPLAY_ORDER` constant gedeeld tussen seed, Cypher query en Pydantic schema
- Build-time parallel fetch in `getStaticPaths`: Research + Tools per BB via nested `Promise.all`

### Gewijzigd (sessie 2026-04-17)
- BB-detailpagina sectie-volgorde: UseCases → Tools → Guardrails → Research (eerst "hoe", dan "grenzen", dan "verdieping")
- Checklist layout: CSS Grid (2-kol row-major) → CSS Columns (per-kolom verticaal) — items van ongelijke lengte botsen niet meer naast elkaar
- Section-titles geharmoniseerd: "Hiermee werk je in de praktijk" → "Uit onze toolkit" (parallel met "Uit onze kennisbank"); hardcoded "AI-Readiness Audit" → "Een voorbeeld uit de praktijk"
- Strong in prose: `color: inherit` i.p.v. `var(--text)` zodat H3-kopjes visueel blijven primen boven bold body-fragmenten
- `get_items_by_building_block` sorteert nu op `coalesce(curation_score, 0) DESC, title`
- `IngestionSource` uitgebreid met optionele `summary_nl` + `curation_score` (None-sentinel beschermt bestaande editorial keuzes bij re-ingest via `coalesce` in `ON MATCH SET`)
- Prompt Design content-consistency: body "MLflow Prompt Registry" → "Promptfoo" (matcht Tools-sectie); checklist items 4 en 5 ingekort; few-shot terminologie verhuisd van checklist naar disclosure "De system prompt"
- Guardrails AI tool-beschrijving gebruikt nu eigen positionering "The AI Reliability Platform" om verwarring met BeeHaive EU-guardrails te vermijden

### Toegevoegd
- `MISSIE.md` v0.3 — projectmissie met drie-vlakken-samenhang (BB↔BB, GR↔GR, BB↔GR) en Noblesse Oblige principes (mens-centrisch, eerlijk over grenzen, readiness eerst, de hele organisatie een stem)
- Deep research audit trail `docs/research/prompt-design-2026/` — 4 parallelle researchers (~40 bronnen) als basis voor de verrijking van BB_04
- `resources/frameworks/prompt-design.md` atom — framework-snapshot voor cross-project gebruik
- `BBDisclosure.astro` — herbruikbare component voor inklapbare secties met native `<details>/<summary>`, auto-slug id, deep-link auto-open, teal-accent styling
- BB_04 Prompt Design — vijf uitklapbare inhoudssecties (Evolutie, Vormen, Agentic flow engineering, PromptOps, In de praktijk) met tussenkopjes in teal
- Agentic prompt design-sectie met control flow (REASON/NEXT ACTION/EXPECTED RESULT/CONTINGENCY), verplichte stopcondities, Plan-Then-Execute, zes canonieke patronen, deterministisch-waar-mogelijk
- PromptOps-sectie — versioning (Git → registry → CI/CD), 3-laags eval-pipeline, canary-deployments, koppeling met Evaluation Loop (BB_06)
- `GuardrailCode` union type in `bb-guardrail-links.ts` voor compile-time typo-detectie

### Gewijzigd
- BB_04 Prompt Design narratief: onderscheid capability- vs context-rolzetting; onbevestigde iBuidl-statistieken vervangen door onderbouwde formuleringen; XML als Claude-specifieke best practice gepositioneerd
- Guardrail-mapping voor Prompt Design: Fairness vervangen door Accountability; relevance-teksten aangescherpt zonder EU AI Act artikelnummers (toegankelijkheid boven technische accuratesse)
- `BBProseSection.astro` CSS: H3-styling toegevoegd (1.1rem teal), custom teal bullets voor ul-lijsten, teal ::marker voor ol-lijsten, strong-labels in list-items in teal
- CSS-selectors aangescherpt naar `.prose > :global(h2)` (direct child) zodat nested H2's binnen `<summary>` niet verborgen worden

- Building Block detail-pagina's met 7 secties (#23, Fase A)
  - Dynamic routing: `/framework/{slug}` voor alle 7 BBs
  - Hero met SVG/PNG icons uit gedeelde `bb-icons.ts`, breadcrumb, quote
  - Checklist (2-kolom grid, teal vinkjes) + Evidence deliverables (NIST-patroon)
  - Quick Start (genummerde stappen cards), Voorbeeld: AI-Readiness Audit
  - Statische guardrail-koppelingen: 3 relevante guardrails per BB met relevantie-uitleg
  - CTA sectie naar AI-readiness audit
  - Sticky Table of Contents met IntersectionObserver scroll-spy (desktop)
  - Prev/next navigatie + cross-links naar alle 7 BBs
  - Floating "terug naar boven" knop op mobiel
  - Geconsolideerde componenten: BBIcon, BBProseSection (generiek), gedeelde section IDs
  - Content schema uitgebreid: `evidence` array per BB
- Footer: copyright 2026, tagline "Het framework voor succesvolle en verantwoorde AI-implementaties"

### Gewijzigd
- BuildingBlocksGrid: cards zijn nu klikbare links naar `/framework/{slug}`, icons via gedeeld BBIcon component
- Nav: active state via `startsWith()` (werkt voor sub-routes)
- globals.css: `text-wrap: balance` op headlines, `.bb-section` utility class

### Verwijderd
- youth-care-booking subproject (verplaatst naar apart project)

### Eerder toegevoegd
- Astro frontend met Luminous Dark design system (#8)
  - 4 pagina's (homepage, framework, kennisbank, over), 8 componenten, Tailwind config
  - Self-hosted fonts (Space Grotesk + Space Mono) via @fontsource (GDPR-compliant)
  - Content Collections: 7 Building Block + 7 Guardrail MDX bestanden met Zod schema's
  - Interactieve workflow visualisatie (React): Waarom/Hoe/Wat tabs, auto-play, BB-tags per stap
  - AI-Readiness Audit als primaire use case met Evaluation Loop per processtap
  - Quotes per pagina (Mollick, Amodei, Kozyrkov, Fei-Fei Li) + per BB
  - Achtergrondfotos via Unsplash met donkere overlay
  - Mobiel responsive: KnowledgeGraph schaalt mee, hero layout past zich aan
  - Hero redesign: nieuwe subtekst, chip boven model, quote bovenaan
  - `prefers-reduced-motion` media query (WCAG 2.1 AA)

### Gewijzigd
- CSS-duplicatie opgeschoond: ~285 regels verwijderd, globale utility classes
- Tekst leesbaarheid verhoogd: --text-dim 0.90, --text-muted 0.72
- Sectie-padding geüniformeerd (7rem → 4rem)
- CTA buttons consistent: btn-gold zelfde grootte als btn-primary
- ROADMAP: Fase 2 compleet, Fase 3 in progress, issues #22/#23 toegevoegd

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

