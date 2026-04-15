# Architecture Decision Records — Index

> **Versie:** 1.0
> **Laatst bijgewerkt:** 2026-03-09

Dit is de centrale index van alle Architecture Decision Records (ADRs). Elke entry beschrijft een architectuurbeslissing: welk probleem er was, welke opties zijn overwogen, en waarom voor deze oplossing is gekozen.

## Hoe dit werkt

1. Bij een architectuurkeuze wordt een ADR aangemaakt via `docs/decisions/TEMPLATE.md`
2. Het ADR krijgt een ID in het formaat `ADR-YYYY-NNN` (bijv. `ADR-2026-001`)
3. Het bestand wordt opgeslagen als `docs/decisions/ADR-YYYY-NNN.md`
4. Deze index wordt bijgewerkt met de nieuwe entry
5. `/sessie-reflectie` kan suggereren om beslissingen als ADR vast te leggen

## Decision Records

| ID | Titel | Status | Datum |
|----|-------|--------|-------|
| ADR-2026-001 | Tech stack keuze: Astro + FastAPI + Neo4j | geaccepteerd | 2026-03-04 |
| ADR-2026-002 | RAG pipeline: RAG-Anything + vLLM-MLX + Neo4j workspace-isolatie | deels vervangen | 2026-03-05 |
| ADR-2026-003 | Externe LLM API's in plaats van lokaal LLM | geaccepteerd | 2026-03-09 |
| ADR-2026-004 | BBDisclosure als herbruikbaar content-patroon voor BB detail-pagina's | geaccepteerd | 2026-04-15 |
| ADR-2026-005 | MDX-import per pagina boven globale mdxComponents-config voor BB-content | geaccepteerd | 2026-04-15 |

## Statistieken

| Status | Aantal |
|--------|--------|
| geaccepteerd | 4 |
| voorgesteld | 0 |
| ter bespreking | 0 |
| deels vervangen | 1 |
| ingetrokken | 0 |
| **Totaal** | **5** |
