# Plan Review Log — PLAN-007 Ingestion Pipeline

## Metadata
- **Plan:** docs/plans/PLAN-007-ingestion-pipeline.md
- **Rondes:** 3
- **Datum ronde 1:** 2026-03-08
- **Datum ronde 2:** 2026-03-08
- **Datum ronde 3:** 2026-03-08
- **Eindstatus:** Verwerkt in v4

## Ronde 1

### Pre-flight synthese

| Agent | Oordeel | Kernpunt |
|-------|---------|----------|
| PM | yes (voorbehoud) | Roadmap-conform maar scope 3x groter dan issue #7 |
| ARCH | unclear | Structurele fragmentatie, modules zonder package-strategie |
| SECADV | no | SSRF en Cypher injection niet geadresseerd |
| AVGADV | yes (beperkt) | PII-scanner positief, Art. 6(1)(f) uitwerking ontbreekt |
| FEAS | haalbaar met risico's | Post-insert tagging werkt niet, embedding dedup ontbreekt |
| CCR | no | Overgeëngineerd voor 34 items, waarde pas in fase 4 |

### Filter stats

41 input → 26 gemerged → 5 relevantie-gefilterd → 15 finaal (7 must, 7 should, 1 nice)

### Bevindingen + beslissingen

| # | ID | Agent(s) | Classificatie | Aandachtspunt | Beslissing |
|---|-----|----------|---------------|---------------|------------|
| 1 | MERGED-001 | PM, CCR | must_address | Scope 3x groter dan issue #7 | Verwerkt: gereduceerd naar 4 fasen, comparison tool → eenmalig script, API endpoint out-of-scope |
| 2 | MERGED-002 | PM | must_address | Geen Definition of Done | Verwerkt: concrete DoD toegevoegd (5 criteria) |
| 3 | MERGED-003 | SECADV | must_address | SSRF via fetcher | Verwerkt: URL-validatie + SSRF-preventie in Fase 1.1 |
| 4 | MERGED-004 | SECADV, ARCH | must_address | Cypher injection + queries buiten queries.py | Verwerkt: design constraint "alle Cypher in graph/, geparametriseerd" |
| 5 | MERGED-005 | FEAS | must_address | Post-insert tagging werkt niet | Verwerkt: **ongeldig na LightRAG-analyse** — source_id property biedt native traceerbaarheid. LightRAG internals sectie toegevoegd. |
| 6 | MERGED-006 | FEAS, PM | must_address | Embedding dedup infrastructuur ontbreekt | Verwerkt: content embedding dedup → toekomstige uitbreiding. Nu: source_url + titel dedup. |
| 7 | MERGED-007 | ARCH | must_address | Modules buiten package-structuur | Verwerkt: app/ingestion/ package + module-structuur sectie |
| 8 | MERGED-008 | ARCH, FEAS | should_consider | Namespace collision twee grafen | **Gedowngraded na LightRAG-analyse:** workspace-labels isoleren al. Gedocumenteerd in LightRAG Internals sectie. |
| 9 | MERGED-009 | AVGADV | should_consider | Author-node AVG onvolledig | Verwerkt: belangenafweging + bezwaarprocedure + is_organization in Fase 1.3 |
| 10 | MERGED-010 | PM | should_consider | Geen go/no-go moment | Verwerkt: expliciet go/no-go na Fase 2 (>= 50% entity matches) |
| 11 | MERGED-011 | ARCH | should_consider | Engine singleton integratie | **Gedowngraded na analyse:** create_rag_engine() werkt al buiten FastAPI |
| 12 | MERGED-012 | CCR | should_consider | Geen feedback loop bij mappings | Verwerkt: dry-run/preview modus als default in pipeline |
| 13 | MERGED-013 | FEAS | should_consider | Sync/async mismatch | Verwerkt: gedocumenteerd in risicotabel + LightRAG Internals sectie |
| 14 | MERGED-014 | SECADV, FEAS | should_consider | PII scanner faalgedrag | Verwerkt: fail-closed gedrag + bekende beperkingen gedocumenteerd |
| 15 | MERGED-015 | ARCH, PM | nice_to_have | API endpoint overlapt | Verwerkt: API endpoint out-of-scope in v2 |

### Correcties na LightRAG broncode-analyse

Twee bevindingen bleken (deels) ongeldig na inspectie van de LightRAG broncode:

1. **MERGED-005 (post-insert tagging):** LightRAG slaat `source_id` op per entity-node. Entities zijn traceerbaar per bron zonder extra tagging.
2. **MERGED-008 (namespace collision):** LightRAG gebruikt workspace-labels als primair filter. De handmatige graph labels (`BuildingBlock`, `Guardrail`) overlappen niet met LightRAG labels (`base` + entity_type).

Een **LightRAG Internals** referentiesectie is toegevoegd aan het plan zodat toekomstige reviews deze context hebben.

## Ronde 2

### Pre-flight synthese

| Agent | Oordeel | Kernpunt |
|-------|---------|----------|
| PM | yes | Scope en DoD goed afgebakend |
| ARCH | yes | Structuur helder, LightRAG Internals sectie nuttig |
| SECADV | yes | SSRF en Cypher constraints adequaat |
| AVGADV | yes (voorbehoud) | Verwerkingsregister ontbreekt als deliverable |
| FEAS | yes (voorbehoud) | source_id/file_path verwarring in queries |
| CCR | yes | Scope realistisch na reductie |

### Filter stats

8 input → 3 finaal (2 must, 1 should)

### Bevindingen + beslissingen

| # | ID | Agent(s) | Classificatie | Aandachtspunt | Beslissing |
|---|-----|----------|---------------|---------------|------------|
| 1 | FEAS-001 | FEAS | must_address | source_id bevat chunk-IDs, niet bron-URLs. file_path is de juiste property voor traceerbaarheid. | Verwerkt: alle source_id-referenties gecorrigeerd naar file_path in LightRAG Internals en query-voorbeelden |
| 2 | AVGADV-007 | AVGADV | must_address | Verwerkingsregister (DATA_GLOSSARY.md) niet als deliverable opgenomen | Verwerkt: verwerkingsregister toegevoegd als Fase 4.2 deliverable |
| 3 | AVGADV-008 | AVGADV | should_consider | PII scanner overgedimensioneerd voor publieke academische bronnen | Verwerkt: PII scanner vereenvoudigd naar email + telefoon regex. NER voor namen, BSN en IBAN verwijderd. Art. 6(1)(f) onderbouwing versterkt. |

### Conclusie

Alle bevindingen verwerkt in v3. Geen openstaande must-address items.

## Ronde 3 (verificatie)

### Pre-flight synthese

| Agent | Oordeel | Kernpunt |
|-------|---------|----------|
| PM | yes | Roadmap-conform, scope past bij huidige fase |
| ARCH | yes | Past in bestaande architectuur |
| SECADV | yes | SSRF, Cypher injection, fail-closed adequaat |
| AVGADV | yes | Art. 6(1)(f) onderbouwd, verwerkingsregister aanwezig |
| FEAS | yes | Technisch haalbaar |
| CCR | unclear | Complexiteit mogelijk disproportioneel voor 34 items |

### Filter stats

28 input → 15 finaal (1 must, 14 should) — 3 gemerged, 1 hard excluded, 5 relevantie-gefilterd, 4 afgecapt

### Bevindingen + beslissingen

| # | ID | Agent(s) | Classificatie | Aandachtspunt | Beslissing |
|---|-----|----------|---------------|---------------|------------|
| 1 | ARCH-001 | ARCH, FEAS | must_address | Write-functies breken read-only conventie queries.py | Verwerkt: graph/mutations.py voor writes, queries.py blijft read-only |
| 2 | ARCH-002 | ARCH, FEAS | should_consider | Pipeline mixt sync/async zonder bridge | Verwerkt: asyncio.to_thread() expliciet in pseudocode |
| 3 | ARCH-004 | ARCH, FEAS | should_consider | Geen early-fail als engine niet beschikbaar | Verwerkt: engine check als stap 0 in pipeline |
| 4 | FEAS-003 | FEAS | should_consider | ingest_text() wrapper mist file_paths | Verwerkt: pipeline roept ainsert() direct aan, gedocumenteerd waarom |
| 5 | FEAS-004 | FEAS | should_consider | trafilatura ongeschikt voor PDF | Verwerkt: process_document_complete() voor papers |
| 6 | PM-001 | PM | should_consider | Go/no-go niet in DoD | Verwerkt: DoD-item 6 toegevoegd |
| 7 | PM-002 | PM | should_consider | Steekproef 10/34 statistisch zwak | Verwerkt: alle 34 items als testset |
| 8 | CCR-001 | CCR | should_consider | Oplossing disproportioneel | Bewust niet: complexiteit is investering in schaalbaarheid |
| 9 | CCR-002 | CCR | should_consider | Go/no-go te laat, sunk cost | Verwerkt: Fase 0 quick spike met 3-5 items |
| 10 | CCR-003 | CCR | should_consider | Silent failures bij 0 entities/mappings | Verwerkt: status no_mappings_found + needs_review |
| 11 | AVGADV-011 | AVGADV | should_consider | Assert ge-redacte tekst naar LightRAG | Verwerkt: assert in pipeline pseudocode |
| 12 | AVGADV-009 | AVGADV | should_consider | Bewaartermijn mist reviewcyclus | Verwerkt: jaarlijkse steekproefsgewijze controle |
| 13 | AVGADV-010 | AVGADV | should_consider | Inzagerecht Art. 15 niet geadresseerd | Bewust niet: impliciet via bestaande Neo4j queries |
| 14 | SECADV-002 | SECADV | should_consider | Content ongevalideerd naar LightRAG | Verwerkt: entity output validatie in pipeline |
| 15 | SECADV-004 | SECADV | should_consider | Cleanup niet afgedwongen bij fout | Verwerkt: try/finally cleanup in fetcher |

### Conclusie

13 van 15 bevindingen verwerkt in v4. 2 bewust niet verwerkt (CCR-001: proportionaliteit geaccepteerd, AVGADV-010: inzagerecht impliciet). Geen openstaande must-address items. Plan goedgekeurd voor implementatie.
