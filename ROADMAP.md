# BeeHaive - Roadmap & Status Overzicht

**Laatst bijgewerkt:** 2026-04-28

---

## Project Status Samenvatting

| Fase | Status | Beschrijving |
|------|--------|--------------|
| **Fase 1: Project Foundation** | ✅ Compleet | Projectstructuur, repo, basis tooling |
| **Fase 2: Knowledge Graph** | ✅ Compleet | Neo4j opzetten, knowledge items modelleren, ingestion pipeline |
| **Fase 3: Frontend Website** | 🟡 In progress | Astro site, framework pagina's, blog systeem |
| **Fase 4: Backend API** | 🔴 Te doen | FastAPI, Neo4j integratie, AI content generatie |
| **Fase 5: Training Portal** | 🔴 Te doen | OAuth, cursusstructuur, voortgang tracking |
| **Fase 6: Betalingen & Launch** | 🔴 Te doen | Mollie integratie, deployment op Hetzner |
| **Ops & Kwaliteit** | 🔴 Te doen | Security, testing, architectuur, privacy, API hardening |

**Legenda:** ✅ Compleet | 🟡 In progress | 🔴 Te doen | 📋 Gepland

---

## Stappen & Issues

### Fase 1: Project Foundation ✅

- [x] ✅ Stap 1: Project scaffolding en structuur (#1)
- [x] ✅ Stap 2: Neo4j schema, constraints en seed data (#2)
- [x] ✅ Stap 3: Query-laag voor knowledge graph (#3)

### Fase 2: Knowledge Graph ✅

- [x] ✅ Stap 5: RAG pipeline met vector embeddings en full-text search (#5)
- [x] ✅ Stap 6: Knowledge graph uitbreiden met meer bronnen en items (#6)
- [x] ✅ Stap 7: Ingestion pipeline voor knowledge items (#7) — Compleet: fetcher, PII, mutations, Gemini 3.1 Pro mapper, orchestrator, CLI, dual ingest, kalibratie (BB 77%/GR 74%), DATA_GLOSSARY, blocked_authors.

### Fase 3: Frontend Website 🟡

- [x] ✅ Stap 8: Astro frontend opzetten met basis pagina's (#8) — Compleet: 4 pagina's, 8 componenten, Luminous Dark design system, Tailwind, self-hosted fonts.
- [x] Stap 8c Fase A: BB detail-pagina's met 7 secties (#23) — Compleet: 7 pagina's, 10 componenten, guardrail-koppelingen, evidence, CTA, sticky ToC.
- [x] Stap 8c Fase B deel 1: Research-sectie dynamisch (#23) — Build-time fetch uit Neo4j, top 3 per BB op curation_score, NL-samenvattingen, graceful fallback.
- [x] Stap 8c Fase B deel 2: Tools & Products sectie (#23) — Tool node-label met DISPLAYED_ON curatie-relatie, 2-koloms card-grid met max 4 + "alle tools" link.
- [ ] Stap 8c Fase B deel 3: BB↔GR relaties dynamiseren (#23) — wacht tot alle BBs zijn ingevuld via 5-stappen ritme.
- [x] Prompt Design (BB_04) volledig af volgens 5-stappen ritme — deep research, bronnen, teksten, consistency-pass, tools.
- [x] Dynamic Context (BB_03) volledig af volgens 5-stappen ritme — inclusief lees-review door Robin, pseudonimiseren/anonimiseren-nuance, Forte-quote.
- [x] Knowledge (BB_01) volledig af volgens 5-stappen ritme — EU AI Act Art. 4, Decision Intelligence, operating agreements, jagged frontier, deskilling-paradox, FOBO.
- [ ] Overige BBs uitbouwen via 5-stappen ritme — Client Blueprint, Tool Integration, Model Engines, Evaluation Loop.
- [ ] Stap 8b: Workflow visualisatie met React Flow (#22)
- [ ] Frontend: design nice-to-haves — framework overview, hero accent, nav active state (#27)
- [ ] Stap 9: Blog systeem met content collecties (#9)

### Fase 4: Backend API 🔴

- [x] ✅ Stap 4: FastAPI endpoints op basis van query-laag (#4)
- [ ] Stap 10: Auth middleware voor API — JWT (#10)
- [ ] Stap 11: AI content generatie endpoints (#11)

### Fase 5: Training Portal 🔴

- [x] ✅ Training-design naslagwerk (#33) — Compleet: `docs/research/TRAINING-DESIGN.md` (894 regels) met evidence-onderbouwde ontwerpkeuzes per dimensie (formaat, curriculum, modaliteiten, retentie, AI-tutor, meting) + zes deelrapporten in `training-design-2026-04/`. Lokale skill `/training-ontwerper` om concrete pilot-ontwerpen te produceren.
- [ ] Stap 12: OAuth integratie — Auth.js via Astro (#12)
- [ ] Stap 13: Cursusstructuur en leermodules (#13) — gebruik `/training-ontwerper` voor structuur-keuzes
- [ ] Stap 14: Voortgang tracking voor trainingen (#14)

### Fase 6: Betalingen & Launch 🔴

- [ ] Stap 15: Mollie betalingsintegratie (#15)
- [ ] Stap 16: Deployment op Hetzner (#16)

### Ops & Kwaliteit 🔴

- [ ] Ops: API hardening — auth, rate limiting, input validatie, file upload limits (#17)
- [ ] Security hardening fase 2: auth, Cypher validatie, config (#18)
- [ ] Test suite opzetten: RAG, auth, API endpoints, coverage (#19)
- [ ] Architectuur consolidatie: dual session, config, paginatie (#20)
- [ ] Privacy-by-design: AI Act transparantie, retentie, audit trail (#21)
- [ ] Verbeteren context engineering: token budget, placement-strategie, degradatiepatronen (#25)
- [ ] Content: Business Glossary — consistente terminologie across site, blogs en trainingen (#28)
- [ ] Content: Kennisbank verrijking per BB/GR — NI-artikelen + Bastionclaw use-cases, wekelijkse verwerking (#29)
- [ ] Bronnen migreren naar canonical schema — NL keys, flat tags, taxonomie-namespace (#30)

---

## Kritiek Pad

Wat moet er nu gebeuren om vooruit te komen?

1. **Eerstvolgende:** Overige BBs uitbouwen via 5-stappen ritme — deep research → bronnen → teksten → consistency-pass → tools
2. **Daarna:** BB↔GR relaties dynamiseren in knowledge graph (#23 Fase B deel 3)
3. **Vervolgens:** Workflow visualisatie met React Flow (#22), Blog systeem (#9), Bastionclaw Use Cases koppelen

---

## Key Insights

- BeeHaive is een knowledge framework met 7 bouwstenen + 7 EU Trustworthy AI guardrails
- Tech stack: Astro + React islands (frontend), FastAPI (backend), Neo4j + PostgreSQL (data)
- Alle data in EU (Hetzner), betalingen via Mollie (NL)
- Content wordt deels AI-gegenereerd (blogs, nieuwsbrieven) op basis van knowledge graph
