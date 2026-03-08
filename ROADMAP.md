# BeeHaive - Roadmap & Status Overzicht

**Laatst bijgewerkt:** 2026-03-08

---

## Project Status Samenvatting

| Fase | Status | Beschrijving |
|------|--------|--------------|
| **Fase 1: Project Foundation** | ✅ Compleet | Projectstructuur, repo, basis tooling |
| **Fase 2: Knowledge Graph** | 🟡 In progress | Neo4j opzetten, knowledge items modelleren, ingestion pipeline |
| **Fase 3: Frontend Website** | 🔴 Te doen | Astro site, framework pagina's, blog systeem |
| **Fase 4: Backend API** | 🔴 Te doen | FastAPI, Neo4j integratie, AI content generatie |
| **Fase 5: Training Portal** | 🔴 Te doen | OAuth, cursusstructuur, voortgang tracking |
| **Fase 6: Betalingen & Launch** | 🔴 Te doen | Mollie integratie, deployment op Hetzner |
| **Ops & Kwaliteit** | 🔴 Te doen | Security, testing, architectuur, privacy, API hardening |

**Legenda:** ✅ Compleet | 🟡 In progress | 🔴 Te doen | 📋 Gepland

---

## Stappen & Issues

### Fase 1: Project Foundation ✅

- [x] Stap 1: Project scaffolding en structuur (#1)
- [x] Stap 2: Neo4j schema, constraints en seed data (#2)
- [x] Stap 3: Query-laag voor knowledge graph (#3)

### Fase 2: Knowledge Graph 🟡

- [x] Stap 5: RAG pipeline met vector embeddings en full-text search (#5)
- [x] Stap 6: Knowledge graph uitbreiden met meer bronnen en items (#6)
- [ ] Stap 7: Ingestion pipeline voor knowledge items (#7)

### Fase 3: Frontend Website 🔴

- [ ] Stap 8: Astro frontend opzetten met basis pagina's (#8)
- [ ] Stap 9: Blog systeem met content collecties (#9)

### Fase 4: Backend API 🔴

- [x] Stap 4: FastAPI endpoints op basis van query-laag (#4)
- [ ] Stap 10: Auth middleware voor API — JWT (#10)
- [ ] Stap 11: AI content generatie endpoints (#11)

### Fase 5: Training Portal 🔴

- [ ] Stap 12: OAuth integratie — Auth.js via Astro (#12)
- [ ] Stap 13: Cursusstructuur en leermodules (#13)
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

---

## Kritiek Pad

Wat moet er nu gebeuren om vooruit te komen?

1. **Eerstvolgende:** Ingestion pipeline voor knowledge items (#7)
2. **Daarna:** Astro frontend opzetten met basis pagina's (#8)
3. **Vervolgens:** Blog systeem met content collecties (#9)

---

## Key Insights

- BeeHaive is een knowledge framework met 7 bouwstenen + 7 EU Trustworthy AI guardrails
- Tech stack: Astro + React islands (frontend), FastAPI (backend), Neo4j + PostgreSQL (data)
- Alle data in EU (Hetzner), betalingen via Mollie (NL)
- Content wordt deels AI-gegenereerd (blogs, nieuwsbrieven) op basis van knowledge graph
