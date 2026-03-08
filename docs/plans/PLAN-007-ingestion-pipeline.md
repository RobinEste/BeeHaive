# PLAN-007: Ingestion Pipeline voor Knowledge Items

**Issue:** #7
**Fase:** 2 — Knowledge Graph
**Status:** Draft v4 (post-review ronde 3)
**Datum:** 2026-03-08

---

## Overzicht

CLI-first ingestion pipeline die nieuwe knowledge items automatisch toevoegt aan de BeeHaive knowledge graph. De pipeline fetcht een bron-URL, scant op PII, ingest via LightRAG voor entity extraction, mapt geëxtraheerde entities naar de BeeHaive-taxonomie (BuildingBlocks, Guardrails, Topics), en maakt een KnowledgeItem node aan met relaties.

**Scope:** Developer tooling voor Robin. API endpoint is out-of-scope tot er een frontend/admin-interface is.

### Strategie

De handmatige knowledge graph (34 gecureerde items) dient als ground truth. We ingesten dezelfde bronnen via LightRAG, vergelijken de resultaten via een eenmalig script, en gebruiken die inzichten om de taxonomy mapper te kalibreren.

### Acceptatiecriteria (issue #7)

- [ ] CLI script voor ingestion van nieuwe KnowledgeItems (`make ingest-item`)
- [ ] Automatische relatie-detectie (BuildingBlock, Guardrail, Topic mapping)
- [ ] Author-node PII-validatie (AVG Art. 6(1)(f) check bij natuurlijke personen)
- [ ] Deduplicatie op source_url en titel
- [ ] Logging en error handling
- [ ] Preview/dry-run modus voor taxonomy mappings

### Definition of Done

1. `make ingest-item URL=... TITLE=... TYPE=...` draait end-to-end zonder errors
2. Taxonomy mapper haalt >= 70% precision op alle 34 bekende items
3. PII scanner detecteert 100% van email/telefoon in testset (>= 10 testcases)
4. Deduplicatie blokkeert re-insert van bestaand item op source_url
5. Preview modus toont voorgestelde mappings vóór commit
6. Go/no-go Fase 0: quick spike resultaat gedocumenteerd met besluit om door te gaan

---

## LightRAG Internals (referentie)

> Deze sectie documenteert hoe LightRAG werkt in Neo4j, zodat de pipeline-implementatie hier correct op aansluit.

### Node-structuur

LightRAG slaat entities op met een **multi-label patroon**:

```cypher
MERGE (n:`{workspace_label}` {entity_id: $entity_id})
SET n += $properties
SET n:`{entity_type}`
```

Elke entity-node heeft:
- **Label 1:** workspace-label (default `base`, configureerbaar via `NEO4J_WORKSPACE` env var)
- **Label 2:** entity_type (dynamisch, bijv. `Person`, `Organization`, `Document`)

### Entity properties

| Property | Type | Beschrijving |
|----------|------|-------------|
| `entity_id` | string | Unieke identifier binnen workspace |
| `entity_type` | string | Type (Person, Organization, etc.) |
| `description` | string | Beschrijving |
| `source_id` | string | Chunk-referenties (format: `chunk-abc<SEP>chunk-def`). **Niet bruikbaar voor bron-lookup.** |
| `file_path` | string | **Bron-URL of bestandspad** — dit is de property voor traceerbaarheid per bron |
| `created_at` | integer | Unix timestamp |

### Relaties

```cypher
MERGE (source)-[r:DIRECTED]-(target)
SET r += {weight, description, keywords, source_id, file_path, created_at}
```

### Traceerbaarheid via file_path

`ainsert()` retourneert een `track_id` (string) voor monitoring. Elke geëxtraheerde entity krijgt:
- `file_path`: de bron-URL (meegegeven via `file_paths=[source_url]`) — **gebruik dit voor bron-lookup**
- `source_id`: interne chunk-referenties (`chunk-abc<SEP>chunk-def`) — niet bruikbaar voor bron-lookup

Na ingestion kun je entities per bron opvragen:

```cypher
MATCH (n:`base`) WHERE n.file_path CONTAINS $source_url RETURN n
```

**Gevolg:** Post-insert Cypher tagging is niet nodig. LightRAG biedt native traceerbaarheid per bron via `file_path`.

### Graph-isolatie

De handmatige graph en LightRAG graph leven in dezelfde Neo4j maar zijn geïsoleerd:

| Aspect | Handmatige graph | LightRAG graph |
|--------|-----------------|----------------|
| Labels | `BuildingBlock`, `Guardrail`, `KnowledgeItem`, `Topic`, `Author` | `base` + dynamische entity_type |
| Queries | `graph/queries.py` (sync, geparametriseerd) | LightRAG intern (async, geparametriseerd) |
| Indexen | Uniqueness constraints op `.name`/`.title` | B-tree + full-text index op `base.entity_id` |
| Relaties | `RELATES_TO`, `ADDRESSES`, `ABOUT`, `AUTHORED_BY` | `DIRECTED` |

Alle LightRAG queries filteren op het workspace-label. Er is geen overlap met de handmatige graph labels. Extra mitigatie: stel `NEO4J_WORKSPACE=beehaive_rag` in voor expliciete scheiding.

### Async-architectuur

LightRAG is volledig async (`AsyncGraphDatabase`). De bestaande `graph/queries.py` is sync. De pipeline moet beide aanspreken — gebruik `asyncio.to_thread()` voor sync queries, of migreer naar `neo4j.AsyncSession`.

---

## Fase 0: Quick Spike — LightRAG Geschiktheid

**Doel:** Vooraf valideren of LightRAG bruikbare entities extraheert uit academische bronnen, vóórdat pipeline-code wordt geschreven.

### 0.1 Handmatige test

- Kies 3-5 representatieve items uit seed.py (mix van paper, regulation, best_practice)
- Fetch handmatig de brontekst
- Voer `engine.lightrag.ainsert(text, file_paths=[url])` uit in een Python REPL
- Inspecteer de geëxtraheerde entities: `MATCH (n:\`base\`) WHERE n.file_path CONTAINS $url RETURN n`
- Vergelijk visueel met de handmatige relaties in seed.py

### 0.2 Go/no-go

- **Go:** LightRAG extraheert herkenbare entities (personen, concepten, organisaties) die overlappen met de handmatige taxonomie → ga door naar Fase 1
- **No-go:** LightRAG produceert voornamelijk ruis of irrelevante entities → heroverweeg aanpak (directe LLM-extractie via Claude/Qwen prompt)
- **Documenteer** het resultaat en de beslissing

---

## Fase 1: Source Document Fetcher + PII Scanner

**Doel:** Bronnen downloaden en PII-scan voorbereiden.

### 1.1 Document fetcher module

Nieuw bestand: `backend/app/ingestion/fetcher.py`

- Functie `fetch_source(url: str, source_type: str) -> FetchResult`
  - `regulation` / `guideline` / `best_practice`: HTML via httpx + trafilatura (content extraction)
  - `paper`: PDF via `engine.process_document_complete()` (RAGAnything heeft native PDF-support via docling). Trafilatura is ongeschikt voor PDF.
  - Toekomstig: `video` (YouTube transcript)
- `FetchResult` dataclass: `text`, `metadata`, `source_url`, `fetch_status`
- Rate limiting (1 req/sec), retry (max 3, exponential backoff)
- Cache in `data/fetched/` (in `.gitignore`)
- **Cleanup:** `try/finally` — bestanden worden opgeruimd na afloop van de pipeline, ongeacht succes of falen. Bij `pii_scan_failed`: bronbestand direct verwijderen.

**Security — URL-validatie (SSRF-preventie):**
- Alleen `https://` schema toestaan (behalve localhost in dev)
- Na DNS-resolve: private IP-ranges blokkeren (10.x, 172.16-31.x, 192.168.x, 169.254.x, 127.x)
- `max_redirects=0` of redirect-targets valideren tegen dezelfde allowlist
- Optioneel: domain-allowlist voor bekende bronnen (arxiv.org, eur-lex.europa.eu, etc.)

**Fallback:** Bij paywall/403 → gebruik bestaande `content` uit seed.py als ground truth.

### 1.2 Batch fetch script

Nieuw bestand: `backend/scripts/fetch_sources.py`

- Itereert over `KNOWLEDGE_ITEMS` uit `seed.py`
- Slaat resultaten op als JSON per item
- Logging: welke URLs gelukt/gefaald
- Makefile target: `make fetch-sources`

### 1.3 PII scanner (contactgegevens)

Nieuw bestand: `backend/app/ingestion/pii.py`

De pipeline verwerkt uitsluitend publiek beschikbare academische bronnen. Auteursnamen vallen onder AVG Art. 6(1)(f) (zie onder) en hoeven niet geanonimiseerd te worden. De PII scanner richt zich daarom alleen op **contactgegevens** die niet thuishoren in de knowledge graph:

- Regex-detectie: email-adressen, telefoonnummers
- `scan_pii(text: str) -> PIIReport`
- `redact_pii(text: str, report: PIIReport) -> str`
- **Fail-closed:** bij PII-scanner error → blokkeer ingestion, status `pii_scan_failed`

**AVG Art. 6(1)(f) — Author-nodes:**

Belangenafweging:
- **Gerechtvaardigd belang:** kennisdeling over publiek beschikbare academische werken
- **Noodzaak:** bronvermelding en kennisnavigatie
- **Afweging:** publieke auteurs van academische publicaties hebben redelijke verwachting van naamsvermelding. Namen anonimiseren zou de academische waarde ondermijnen.

Implementatie:
- `is_organization: bool` property op Author-nodes
- Publieke auteurs (arXiv-profiel, institutionele pagina) → opnemen met naam
- Contactgegevens (email, telefoon) → altijd redacten
- **Bezwaarprocedure (Art. 21):** `blocked_authors` lijst. Bij bezwaar: Author-node anonimiseren, naam op blocklist zodat heringestion niet opnieuw aanmaakt.

---

## Fase 2: RAG Ingestion + Vergelijking (samengevoegd)

**Doel:** De 34 bronnen door LightRAG sturen en het resultaat vergelijken met de handmatige graph. Dit is een eenmalige kalibratiestap.

### 2.1 Batch ingest script

Nieuw bestand: `backend/scripts/ingest_and_compare.py`

- Leest gefetchte documenten uit `data/fetched/`
- Per item:
  1. PII scan + redact
  2. `engine.lightrag.ainsert(clean_text, file_paths=[source_url])` — LightRAG tagt entities automatisch met `file_path`
  3. Na insert: query `MATCH (n:\`base\`) WHERE n.file_path CONTAINS $source_url RETURN n` om geëxtraheerde entities op te halen
  4. Vergelijk met handmatige relaties uit seed.py (fuzzy match via rapidfuzz)
- Output: vergelijkingsrapport per item (JSON + human-readable)
- Makefile target: `make ingest-compare`

### 2.2 Go/no-go evaluatie

Na de batch ingest, beoordeel:
- **>= 50% bruikbare entity matches:** ga door naar Fase 3 (taxonomy mapper)
- **< 50%:** heroverweeg aanpak — mogelijk directe LLM-extractie (Claude/Qwen prompt) zonder LightRAG-tussenstap voor taxonomy mapping

Dit is een expliciet beslismoment. Documenteer het resultaat.

---

## Fase 3: Taxonomy Mapper + Pipeline

**Doel:** Geautomatiseerde pipeline die een URL omzet naar een KnowledgeItem met taxonomie-relaties.

### 3.1 Mapping rules engine

Nieuw bestand: `backend/app/ingestion/taxonomy.py`

- `TaxonomyMapper` class:
  - **Statische mapping:** synoniemen → BuildingBlocks/Guardrails
    - Bijv. "RAG" → "Dynamic Context", "GDPR" / "AVG" → "Privacy"
  - **Fuzzy matching:** voor Topics en Authors (rapidfuzz, drempel 0.85)
  - **LLM-assisted (optioneel, graceful degradation):** voor ambigue gevallen, Qwen via vLLM-MLX
    - Als vLLM niet beschikbaar → fallback naar statisch+fuzzy, log warning
    - Prompt bevat de 7 BuildingBlocks en 7 Guardrails als context

### 3.2 Deduplicatie

Read-queries in `backend/app/graph/queries.py`, write-queries in nieuw bestand `backend/app/graph/mutations.py` (geparametriseerd, $param syntax):

**queries.py** (read-only, bestaande conventie behouden):
- `find_item_by_source_url(session, url) -> KnowledgeItem | None`
- `find_items_by_fuzzy_title(session, title, limit=5) -> list[KnowledgeItem]`

**mutations.py** (nieuw, write-operaties):
- `create_knowledge_item_with_relations(session, source, mappings)`

Dedup-strategie:
1. **Exacte match** op `source_url` → blokkeer, return bestaand item
2. **Titel similarity** (rapidfuzz, drempel 0.85) → markeer als `needs_review`
3. Content embedding dedup → **toekomstige uitbreiding** (vereist embedding-opslag, bijv. Neo4j vector index)

### 3.3 Pipeline orchestrator

Nieuw bestand: `backend/app/ingestion/pipeline.py`

```python
class IngestionPipeline:
    async def ingest(self, source: IngestionSource, dry_run: bool = False) -> IngestionResult:
        # 0. Engine availability check (fail-fast vóór fetch)
        try:
            engine = await create_rag_engine()
        except Exception as e:
            return IngestionResult(status="engine_unavailable", error=str(e))

        # 1. Fetch document content
        content = await self.fetcher.fetch(source.url, source.source_type)

        # 2. PII scan + redact (fail-closed)
        pii_report = self.pii_scanner.scan(content.text)
        if pii_report.error:
            return IngestionResult(status="pii_scan_failed", error=pii_report.error)
        clean_text = self.pii_scanner.redact(content.text, pii_report)
        assert clean_text is not content.text  # PII-redactie moet altijd een nieuw object opleveren

        # 3. Deduplication check (sync → async bridge)
        existing = await asyncio.to_thread(find_item_by_source_url, session, source.url)
        if existing:
            return IngestionResult(status="duplicate", existing=existing.title)

        # 4. RAG ingestion — direct via engine.lightrag (niet via ingest_text() wrapper,
        #    die file_paths niet doorgeeft)
        track_id = await engine.lightrag.ainsert(clean_text, file_paths=[source.url])

        # 5. Retrieve extracted entities via file_path
        entities = await get_entities_by_file_path(session, source.url)

        # 6. Taxonomy mapping
        mappings = self.taxonomy_mapper.map(entities)

        # 6b. Minimum-kwaliteitscheck
        if not entities or not mappings:
            return IngestionResult(status="no_mappings_found", entities=entities,
                                   suggestion="Handmatig mappen of bron opnieuw proberen")

        # 6c. Entity output validatie (sanity check)
        for entity in entities:
            if len(entity.get("entity_id", "")) > 500:
                return IngestionResult(status="entity_validation_failed",
                                       error="Entity ID onverwacht lang")

        # 7. Preview mode — toon voorgestelde mappings, wacht op bevestiging
        if dry_run:
            return IngestionResult(status="preview", mappings=mappings)

        # 8. Create KnowledgeItem + relations (sync → async bridge)
        await asyncio.to_thread(create_knowledge_item_with_relations, session, source, mappings)
        return IngestionResult(status="ingested", mappings=mappings, pii_report=pii_report)
```

**Sync/async bridge:** Alle functies uit `graph/queries.py` en `graph/mutations.py` zijn sync (`session.execute_read`/`execute_write`). In de async pipeline worden ze aangeroepen via `await asyncio.to_thread(fn, session, ...)`.

**Waarom niet `ingest_text()` wrapper:** De bestaande `ingest_text()` in `rag/engine.py` roept `ainsert(text)` aan zonder `file_paths` parameter. De pipeline roept `engine.lightrag.ainsert()` direct aan met `file_paths=[source.url]` voor traceerbaarheid. Dit is een bewuste keuze — de wrapper is voor de API endpoints, de pipeline heeft een ander aanroeppad.

### 3.4 CLI script

Nieuw bestand: `backend/scripts/ingest_item.py`

```bash
make ingest-item URL="https://arxiv.org/abs/..." TITLE="Paper Title" TYPE=paper
# Standaard: dry-run (preview). Bevestig met --commit
make ingest-item URL="..." TITLE="..." TYPE=paper COMMIT=1
```

---

## Fase 4: Tests + Documentatie

### 4.1 Tests

- `tests/test_pii.py`: unit tests PII scanner (>= 10 testcases)
  - Email-detectie (standaard, academisch format, edge cases)
  - Telefoonnummer-detectie (NL, internationaal)
  - Fail-closed bij error
  - Tekst zonder PII → geen wijzigingen
- `tests/test_taxonomy.py`: unit tests taxonomy mapper (>= 15 testcases)
  - Bekende synoniemen
  - Fuzzy matching grensgevallen
  - Graceful degradation zonder LLM
- `tests/test_dedup.py`: unit tests deduplicatie (mocked Neo4j)
  - source_url exact match
  - Titel fuzzy match
- `tests/test_pipeline.py`: integration test met test-document (indien Neo4j beschikbaar)

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

Alle nieuwe code in `backend/app/ingestion/` package:

```
backend/app/ingestion/
  __init__.py
  fetcher.py        # URL fetching + SSRF-preventie
  pii.py            # PII scanner + redactie
  taxonomy.py       # TaxonomyMapper (statisch + fuzzy + LLM)
  pipeline.py       # IngestionPipeline orchestrator
```

**Cypher queries** — read/write gescheiden:
- `graph/queries.py` (read-only, bestaande conventie) — nieuwe functies: `find_item_by_source_url()`, `find_items_by_fuzzy_title()`
- `graph/mutations.py` (nieuw, write-operaties) — `create_knowledge_item_with_relations()`
- **Design constraint:** alle Cypher queries geparametriseerd ($param syntax). Geen f-strings of string concatenatie voor Cypher. Geen Cypher buiten `graph/`.

**Pydantic models** in `models/ingestion.py`:
- `IngestionSource`, `IngestionResult`, `PIIReport`, `TaxonomyMapping`

**Scripts** in `backend/scripts/`:
- `fetch_sources.py`, `ingest_and_compare.py`, `ingest_item.py`

---

## Sequencing

```
Fase 0 (Quick Spike — 3-5 items handmatig door LightRAG, go/no-go)
  └─→ Fase 1 (Fetcher + PII)
        └─→ Fase 2 (Ingest 34 items + vergelijking)
              └─→ Fase 3 (Taxonomy Mapper + Pipeline + CLI)
Fase 4 (Tests) ── parallel met Fase 3
```

Totaal: 5 fasen (Fase 0 is een snelle handmatige validatie, geen code). API endpoint out-of-scope.

---

## Risico's

| Risico | Impact | Mitigatie |
|--------|--------|-----------|
| Source URLs niet bereikbaar (paywall, 403) | Onvolledige vergelijking | Fallback op `content` uit seed.py |
| Qwen 3.5 9B kwaliteit onvoldoende | Slechte entity extraction | Go/no-go na Fase 2; Claude API als fallback (alleen ge-redacte tekst) |
| Sync/async mismatch (queries.py vs LightRAG) | Runtime errors | `asyncio.to_thread()` voor sync queries, of migreer naar AsyncSession |
| SSRF via fetcher | Security breach | URL-allowlist + private IP blokkade (zie Fase 1.1) |

---

## Technische afhankelijkheden

- Neo4j draait (docker-compose)
- vLLM-MLX draait voor Qwen 3.5 + embeddings
- Nieuwe Python packages: httpx, trafilatura, rapidfuzz
