# Data Glossary — BeeHaive Ingestion Pipeline

**Versie:** v1.0
**Datum:** 2026-03-17
**Doelgroep:** Ontwikkelaars die de ingestion pipeline gebruiken of onderhouden

> **Onderhoud:** Deze glossary is afgeleid van `backend/app/ingestion/llm.py` (`_BUILDING_BLOCKS`, `_GUARDRAILS`). Bij taxonomiewijzigingen: update beide bestanden synchroon.

---

## Verwerkingsoverzicht

| Veld | Waarde |
|------|--------|
| **Verwerking** | Ingestion van publieke academische bronnen |
| **Grondslag** | AVG Art. 6(1)(f) — gerechtvaardigd belang |
| **Persoonsgegevens** | Auteursnamen (publiek), contactgegevens (geredacteerd) |
| **Bewaartermijn** | Zolang bron publiek beschikbaar is |
| **Reviewcyclus** | Jaarlijkse steekproefsgewijze controle (10% van bronnen) |

---

## LIA-samenvatting (Legitimate Interests Assessment)

| Onderdeel | Beoordeling |
|-----------|-------------|
| **Belang** | Kennisverspreiding over publiek beschikbare academische content ten behoeve van het BeeHaive AI knowledge framework |
| **Noodzaak** | Auteursnaam is onlosmakelijk verbonden met academische citatie — verwijdering zou bronvermelding onmogelijk maken |
| **Afweging** | Auteurs van publieke papers hebben de verwachting van publieke vermelding, mits contactgegevens geredacteerd zijn. Het risico voor betrokkenen is minimaal: alleen namen die reeds publiek zijn worden opgeslagen, en er is een bezwaarprocedure (Art. 21) |

---

## Bezwaarprocedure (Art. 21 AVG)

| Veld | Waarde |
|------|--------|
| **Mechanisme** | `blocked_authors.txt` configuratiebestand (`backend/app/ingestion/blocked_authors.txt`) |
| **Contactadres** | privacy@beehaive.org |
| **Doorlooptijd** | Maximaal 1 maand na ontvangst bezwaar |
| **Verificatie** | Verzoeker toont aan dat naam als auteur in het systeem staat |

Bij een bezwaar wordt de auteursnaam toegevoegd aan `blocked_authors.txt`. De pipeline stript vervolgens alle Author-mappings voor deze naam bij toekomstige ingesties. Bestaande Author-nodes moeten handmatig verwijderd worden uit Neo4j.

---

## Verwerkingshandelingen

### 1. Fetch

Ophalen bron-URL → tijdelijke opslag `data/fetched/` (7 dagen TTL, Art. 5(1)(e) — opslagbeperking).

- **Module:** `backend/app/ingestion/fetcher.py`
- **SSRF-bescherming:** HTTPS-only, private IP blocking, redirect blokkering
- **PII-redactie:** Email en telefoonnummers worden geredacteerd vóór caching

### 2. PII-scan

Hercontrole van de opgehaalde tekst op resterende PII.

- **Module:** `backend/app/ingestion/pii.py`
- **Fail-closed:** Scanner-fout blokkeert ingestion (`pii_scan_failed` status)
- **Post-redactie detectie:** Warning (tekst is al geredacteerd door fetcher)

### 3. Classificatie

Tekst naar Gemini API voor taxonomy mapping naar BuildingBlocks, Guardrails, Topics en Authors.

- **Module:** `backend/app/ingestion/llm.py`
- **Model:** Gemini 2.5 Flash
- **Input:** PII-geredacteerde tekst + titel + source_type
- **Output:** Lijst van `TaxonomyMapping` objecten met confidence score
- **Drempel:** Mappings met confidence < 0.7 worden gefilterd

### 4. Persistentie

KnowledgeItem node + relaties aanmaken in Neo4j.

- **Module:** `backend/app/graph/mutations.py`
- **Deduplicatie:** MERGE op `source_url` (uniqueness constraint)
- **Relaties:** `RELATES_TO` (BuildingBlock), `ADDRESSES` (Guardrail), `ABOUT` (Topic), `AUTHORED_BY` (Author)

### 5. RAG sync (optioneel)

Tekst naar LightRAG vector store voor RAG query retrieval.

- **Module:** `backend/app/rag/engine.py`
- **Opslag:** `rag_storage/` op lokale EU-hosting (Hetzner)
- **Non-fatal:** Falen blokkeert niet de hoofdingestie

---

## Verwerkers

| Verwerker | Dienst | Locatie | Doorgifte-mechanisme |
|-----------|--------|---------|---------------------|
| Google LLC | Gemini API — taxonomie-classificatie van brondocument-content | VS | Google Cloud DPA + SCCs |

---

## Data Flow Diagram

```
                    ┌─────────────┐
                    │  Bron-URL   │
                    └──────┬──────┘
                           │
                    ┌──────▼──────┐
                    │   Fetch     │  HTTPS-only, SSRF-safe
                    │ + PII redact│  Email/telefoon → [REDACTED]
                    └──────┬──────┘
                           │
                    ┌──────▼──────┐
                    │ data/fetched│  Cache (7d TTL)
                    └──────┬──────┘
                           │
                    ┌──────▼──────┐
                    │  PII scan   │  Fail-closed hercontrole
                    └──────┬──────┘
                           │
                    ┌──────▼──────┐
                    │  Dedup      │  URL exact + titel fuzzy
                    └──────┬──────┘
                           │
              ┌────────────▼────────────┐
              │   Gemini API (VS)       │  Classificatie
              │   PII-geredacteerde     │  → BuildingBlocks
              │   tekst als input       │  → Guardrails
              └────────────┬────────────┘  → Topics, Authors
                           │
                    ┌──────▼──────┐
                    │ blocked_    │  Art. 21 check
                    │ authors.txt │  Strip geblokkeerde auteurs
                    └──────┬──────┘
                           │
              ┌────────────┴────────────┐
              │                         │
       ┌──────▼──────┐          ┌──────▼──────┐
       │   Neo4j     │          │  LightRAG   │  (optioneel)
       │ Knowledge   │          │  Vector     │
       │ Graph (EU)  │          │  Store (EU) │
       └─────────────┘          └─────────────┘
```

---

## Taxonomie

### BuildingBlocks (7)

| Naam | Beschrijving |
|------|-------------|
| Knowledge | Kennisbronnen die het AI-systeem voedt |
| Client Blueprint | Klantprofiel en context |
| Dynamic Context | Real-time context voor AI-interacties |
| Prompt Design | Prompt engineering en templates |
| Tool Integration | Externe tools en API's |
| Model Engines | AI-modellen en configuratie |
| Evaluation Loop | Evaluatie en continue verbetering |

### Guardrails (7, gebaseerd op EU Trustworthy AI)

| Naam | EU-term |
|------|---------|
| Human Agency | Human agency & oversight |
| Robustness | Technical robustness & safety |
| Privacy | Privacy & data governance |
| Fairness | Diversity, non-discrimination & fairness |
| Transparency | Transparency |
| Well-being | Societal & environmental well-being |
| Accountability | Accountability |
