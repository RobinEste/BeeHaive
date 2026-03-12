# PLAN-007: Ingestion Pipeline voor Knowledge Items

**Issue:** #7
**Fase:** 2 — Knowledge Graph
**Status:** Draft v6 (Fase 1-3 done, kalibratie open)
**Datum:** 2026-03-09

---

## Overzicht

CLI-first ingestion pipeline die nieuwe knowledge items automatisch toevoegt aan de BeeHaive knowledge graph. De pipeline fetcht een bron-URL, scant op PII, laat een frontier LLM (Gemini) de tekst classificeren naar de BeeHaive-taxonomie (BuildingBlocks, Guardrails, Topics, Authors), en maakt een KnowledgeItem node aan met relaties.

**Scope:** Developer tooling voor Robin. API endpoint is out-of-scope tot er een frontend/admin-interface is.

### Strategie

~~De handmatige knowledge graph (34 gecureerde items) dient als ground truth. We ingesten dezelfde bronnen via LightRAG en vergelijken de resultaten.~~ **v5 pivot:** Lokaal LLM (vLLM + Qwen) bleek instabiel. LightRAG entity extraction als tussenstap is overbodig — een frontier LLM kan de taxonomie-classificatie rechtstreeks doen. **Gemini API** (Google AI Studio) vervangt de lokale LLM stack. De tekst is al PII-geredacteerd voordat deze naar de API gaat.

### Acceptatiecriteria (issue #7)

- [x] CLI script voor ingestion van nieuwe KnowledgeItems (`make ingest-item`)
- [x] Automatische relatie-detectie (BuildingBlock, Guardrail, Topic mapping)
- [x] Author-node PII-validatie (AVG Art. 6(1)(f) check bij natuurlijke personen)
- [x] Deduplicatie op source_url en titel
- [x] Logging en error handling
- [x] Preview/dry-run modus voor taxonomy mappings

### Definition of Done

1. `make ingest-item URL=... TITLE=... TYPE=...` draait end-to-end zonder errors
2. Taxonomy mapper haalt >= 70% precision op alle 34 bekende items
3. PII scanner detecteert 100% van email/telefoon in testset (>= 10 testcases)
4. Deduplicatie blokkeert re-insert van bestaand item op source_url
5. Preview modus toont voorgestelde mappings vóór commit
6. Go/no-go Fase 0: quick spike resultaat gedocumenteerd met besluit om door te gaan

---

## ~~LightRAG Internals~~ (vervallen in v5)

> LightRAG entity extraction is vervangen door directe Gemini API classificatie. De LightRAG graph (`base` label) en RAG pipeline (#5) blijven ongewijzigd en functioneren onafhankelijk. De ingestion pipeline schrijft alleen naar de handmatige graph (`KnowledgeItem`, `BuildingBlock`, etc.).

## ~~Fase 0: Quick Spike~~ (vervallen in v5)

> Quick spike was bedoeld om LightRAG entity extraction te valideren. Met directe LLM-classificatie via Gemini is deze stap overbodig.

---

## Fase 1: Source Document Fetcher + PII Scanner ✅

**Status:** Done (commit 63cdccd, 2026-03-09). 34 tests, 3 review-rondes.

Gebouwd:
- `ingestion/fetcher.py` — SSRF-safe document fetcher (HTTPS-only, private IP blocking, rate limiter, PII-redactie vóór cache)
- `ingestion/pii.py` — Fail-closed PII scanner (email + phone regex, overlap filter)
- `models/ingestion.py` — Pydantic models (IngestionSource, FetchResult, PIIFinding, PIIReport, TaxonomyMapping, IngestionResult)
- `graph/mutations.py` — KnowledgeItem + relaties aanmaken (batched UNWIND, MERGE op source_url)
- `graph/queries.py` — Deduplicatie queries (find_item_by_source_url, find_items_by_fuzzy_title)
- `graph/schema.py` — Uniqueness constraint op KnowledgeItem.source_url

**AVG Art. 6(1)(f) — Author-nodes:** Publieke auteurs opnemen met naam. Contactgegevens altijd redacten. Bezwaarprocedure via `blocked_authors` lijst (Art. 21).

---

## Fase 2: Gemini Taxonomy Mapper

**Doel:** Een module die tekst naar de BeeHaive-taxonomie classificeert via de Gemini API.

### 2.1 Gemini client module

Nieuw bestand: `backend/app/ingestion/llm.py`

- Functie `classify_text(text: str, source_type: SourceType) -> list[TaxonomyMapping]`
- Gebruikt `google-genai` Python SDK (Google AI Studio)
- Model: **Gemini 2.5 Flash** (snel, goedkoop, goed in structured output)
- API key via environment variable `GEMINI_API_KEY`
- **Structured output:** response_schema met Pydantic model, zodat de response altijd parseerbaar is

### 2.2 Prompt design

System prompt bevat:
- De 7 BuildingBlocks met korte beschrijving
- De 7 Guardrails met korte beschrijving
- Instructie om Topics en Authors te extraheren
- Output format: JSON array van `{entity_type, matched_name, confidence}`

User prompt: de (geredacteerde) tekst + titel + source_type.

**Confidence drempel:** alleen mappings met confidence >= 0.7 worden doorgezet. Lager → gelogd maar niet opgeslagen.

### 2.3 Fallback en rate limiting

- **Timeout:** 30 seconden per request
- **Retry:** max 2 met exponential backoff bij 429/500
- **Fallback bij API falen:** return lege mappings + status `llm_unavailable` — het KnowledgeItem wordt wel aangemaakt maar zonder relaties. Log warning.
- **Rate limiting:** Gemini free tier = 15 RPM voor Flash. Bij betaald: 2000 RPM. Pipeline is CLI-first (één item per keer), dus geen issue.

### 2.4 Kalibratie

Eenmalig script: `backend/scripts/calibrate_mapper.py`

- Draait de mapper over de 34 bestaande items (tekst uit seed.py content)
- Vergelijkt output met bestaande relaties in Neo4j (ground truth)
- Rapporteert precision/recall per entity type
- **Doel:** >= 70% precision op BuildingBlock en Guardrail mappings
- **Prompt tuning:** pas de system prompt aan op basis van de resultaten

---

## Fase 3: Pipeline Orchestrator + CLI ✅

**Status:** Done (2026-03-12). 11 tests, lint clean.

Gebouwd:
- `ingestion/pipeline.py` — orchestrator: dedup → fetch → classify → preview/commit
  - Dedup check vóór fetch (bespaart bandbreedte)
  - Fuzzy title match waarschuwt maar blokkeert niet
  - Dry-run is default (veilige standaard)
- `scripts/ingest_item.py` — CLI entry point met argparse
- `tests/test_pipeline.py` — 11 unit tests (alle mocked)

```bash
make ingest-item URL="https://..." TITLE="Paper Title" TYPE=regulation           # dry-run
make ingest-item URL="https://..." TITLE="Paper Title" TYPE=regulation COMMIT=1   # schrijf naar Neo4j
```

---

## Fase 4: Tests + Documentatie

### 4.1 Tests

Reeds gebouwd (Fase 1):
- ✅ `tests/test_pii.py`: 17 unit tests PII scanner
- ✅ `tests/test_fetcher.py`: 12 unit tests SSRF/fetcher
- ✅ `tests/test_dedup.py`: 5 integration tests deduplicatie

Gebouwd (Fase 2-3):
- ✅ `tests/test_llm.py`: 23 unit tests Gemini taxonomy mapper
- ✅ `tests/test_pipeline.py`: 11 unit tests pipeline orchestrator

### 4.2 Verwerkingsregister

Update `docs/DATA_GLOSSARY.md` met de ingestion pipeline als verwerkingsactiviteit:
- **Verwerking:** Ingestion van publieke academische bronnen
- **Grondslag:** AVG Art. 6(1)(f) — gerechtvaardigd belang
- **Persoonsgegevens:** auteursnamen (publiek), contactgegevens (ge-redact)
- **Bewaartermijn:** zolang bron publiek beschikbaar is
- **Reviewcyclus:** jaarlijkse steekproefsgewijze controle (10% van bronnen) of deze nog publiek beschikbaar zijn. Bij verwijderde bron: Author-node anonimiseren tenzij gekoppeld aan andere publieke bronnen.
- **Bezwaarprocedure:** `blocked_authors` lijst (Art. 21)

### 4.3 Makefile targets

| Target | Beschrijving |
|--------|-------------|
| `make fetch-sources` | Download bronnen van de 34 seed items |
| `make ingest-compare` | Ingest 34 items via LightRAG + vergelijk met handmatige graph |
| `make ingest-item URL=... TITLE=... TYPE=...` | Ingest één nieuw item (default: dry-run) |

---

## Module-structuur

```
backend/app/ingestion/
  __init__.py
  fetcher.py        # ✅ URL fetching + SSRF-preventie + PII-redactie vóór cache
  pii.py            # ✅ PII scanner + redactie (fail-closed)
  llm.py            # ✅ Gemini taxonomy classifier (Fase 2)
  pipeline.py       # ✅ Pipeline orchestrator (Fase 3)

backend/app/graph/
  queries.py        # ✅ Read-only queries + dedup (find_item_by_source_url, fuzzy_title)
  mutations.py      # ✅ Write operations (create_knowledge_item_with_relations)
  schema.py         # ✅ Constraints (incl. KnowledgeItem.source_url uniqueness)

backend/app/models/
  ingestion.py      # ✅ Pydantic models (IngestionSource, FetchResult, PIIFinding, etc.)

backend/scripts/
  ingest_item.py    # CLI entry point (Fase 3)
  calibrate_mapper.py  # Eenmalig kalibratiescript (Fase 2)
```

**Design constraints:**
- Alle Cypher queries geparametriseerd ($param syntax). Label/relation names via hardcoded `_RELATION_MAP` alleen.
- Geen Cypher buiten `graph/`. Read/write scheiding (KNW-2026-006).

---

## Sequencing

```
Fase 1 (Fetcher + PII + Mutations + Dedup) ✅ DONE
  └─→ Fase 2 (Gemini Taxonomy Mapper) ✅ DONE (23 tests)
        └─→ Fase 3 (Pipeline Orchestrator + CLI) ✅ DONE (11 tests)
Fase 4 (Tests + Docs) ── kalibratie + verwerkingsregister nog open
```

API endpoint out-of-scope.

---

## Risico's

| Risico | Impact | Mitigatie |
|--------|--------|-----------|
| Source URLs niet bereikbaar (paywall, 403) | Onvolledige kalibratie | Fallback op `content` uit seed.py |
| Gemini API niet beschikbaar / rate limit | Pipeline blokkeert | Graceful degradation: KnowledgeItem zonder relaties + warning |
| Gemini classificatie kwaliteit onvoldoende | Slechte taxonomy mappings | Kalibratie tegen 34 ground truth items; prompt tuning |
| SSRF via fetcher | Security breach | ✅ Geïmplementeerd: HTTPS-only + private IP blokkade + redirect blokkering |
| PII naar externe API | Privacy breach | ✅ Gemitigeerd: tekst is PII-geredacteerd vóór Gemini call |

---

## Technische afhankelijkheden

- Neo4j draait (docker-compose)
- ~~vLLM-MLX draait voor Qwen 3.5 + embeddings~~ (vervallen in v5)
- **Gemini API key** (Google AI Studio) via `GEMINI_API_KEY` env var
- Python packages: ✅ httpx, trafilatura, rapidfuzz + **nieuw:** google-genai
