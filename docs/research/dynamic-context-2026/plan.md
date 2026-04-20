# Onderzoeksplan: Dynamic Context als informatie-architectuur 2024-2026

**Slug:** dynamic-context-2026
**Aanmaakdatum:** 2026-04-20
**Status:** ✅ Afgerond

## Onderzoeksvraag

Wat is de stand van context engineering als informatie-architectuur-discipline (2024-2026), en welke patronen moet BB_03 dekken om elk checklist-item praktisch bruikbaar te maken?

## Kernvragen

1. Wanneer wordt context stale, en wie/wat bepaalt refresh-cadans? (BB_03 checklist item 1)
2. Hoe beslis je welke context geïnjecteerd wordt — routing, intent-detection? (item 2)
3. Hoe werkt retrieval-ranking, context-pruning en filter-strategieën? (item 3)
4. Hoe werkt PII-filtering in retrieval en data-lineage? (item 4, cross-cut GR Privacy)
5. Wat zijn de beste patronen voor chunking, embeddings, schema's en opslagformaat? (item 5)
6. Welke trigger-mechanismen en invalidation-strategieën bestaan voor automatisch/handmatig actualiseren? (item 6)
7. Hoe stem je hoeveelheid context af op het model — token-budget, U-curve, context rot? (item 7)
8. Wat is de productiestatus van agentic memory systems (mem0, Letta, MemGPT)?
9. Klopt Forte's "25-50% bruikbaar context window" empirisch?

## Strategie

**Scale decision:** complex multi-domein — 4 parallelle researchers
**Aantal researchers:** 4
**Geschatte rondes:** 1-2

**Dimensie-verdeling:**
- Researcher 1 (wetenschap): context rot, U-curve, long-context benchmarks, re-ordering-effecten op frontier-modellen (2024-2026)
- Researcher 2 (architectuur): RAG 2.0, GraphRAG, agentic memory (mem0/Letta/MemGPT), hybrid retrieval, MCP context provisioning
- Researcher 3 (praktijkpatronen): Willison's context engineering, Forte's PCM, enterprise KB-governance, chunking/embeddings/opslag
- Researcher 4 (privacy & kwaliteit): PII-filtering in retrieval, data-lineage, transparantie over contextbronnen

## Acceptatiecriteria

- [ ] Alle 7 BB_03-checklist-items beantwoord met ≥2 onafhankelijke bronnen
- [ ] U-curve / context rot status op 2026 frontier modellen vastgesteld
- [ ] Forte's "25-50%" claim geëvalueerd (onderbouwd of vager geformuleerd)
- [ ] Agentic memory rijpheid beoordeeld met concrete case studies of benchmarks
- [ ] PII-filtering patronen beschreven met ≥1 concrete implementatie
- [ ] Tegenstrijdigheden geïdentificeerd en geadresseerd
- [ ] Geen single-source claims op kritieke findings

## Task Ledger

| ID | Owner | Taak | Status | Output |
|----|-------|------|--------|--------|
| T1 | researcher-wetenschap | U-curve, context rot, long-context benchmarks 2024-2026 | done | research-wetenschap.md |
| T2 | researcher-architectuur | RAG 2.0, GraphRAG, agentic memory, MCP | done | research-architectuur.md |
| T3 | researcher-praktijk | Context engineering patronen, KB-governance, opslag | done | research-praktijkpatronen.md |
| T4 | researcher-privacy | PII-filtering retrieval, data-lineage, transparantie | done | research-privacy-kwaliteit.md |
| L1 | lead | Synthese + draft | done | draft.md |
| L2 | lead | Cite + verify + final | done | final.md |

## Verificatie-log

| Item | Methode | Status | Bewijs |
|------|---------|--------|--------|
| U-curve empirische status 2026 | web search + fetch | pending | — |
| Forte "25-50%" claim | web fetch bronnen | pending | — |
| mem0/Letta productie-rijpheid | web search + fetch | pending | — |
| PII-filtering implementaties | web search | pending | — |

## Decision-log

- 2026-04-20 10:00 — Output-directory hergebruikt (brainstorm.md bestond al, geen slug-collision). Geen nieuw aanmaken nodig.
- 2026-04-20 10:00 — Vendor-docs lane weggelaten conform brainstorm-beslissing; architectuur krijgt eigen lane.
- 2026-04-20 10:00 — Lane 4 (privacy) focust op BB_03; aantekening gemaakt om guardrail-relevante insights te labelen voor latere sync.
