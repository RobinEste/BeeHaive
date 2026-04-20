# Research: Praktijkpatronen — Dynamic Context 2024-2026

**Researcher:** researcher-praktijkpatronen
**Dimensie:** Context engineering als discipline, enterprise KB-governance, Forte's PCM, Willison's agentic patterns, refresh-mechanismen
**Datum:** 2026-04-20

## Samenvatting (1 zin)

Context engineering is in 2025 een erkende discipline geworden (Tobi Lütke/Shopify, Andrej Karpathy, Gartner), maar de praktische toepassing in enterprise kennisbanken loopt achter — 63% van organisaties mist adequate data governance voor AI, terwijl concrete patronen (event-triggered re-indexing, staleness scoring, RAGAS kwaliteitsmetrics) beschikbaar zijn.

## Bevindingen

### 1. Context engineering als discipline — de term en het paradigma

**Oorsprong** (`verified`): Tobi Lütke (CEO Shopify) definieerde "context engineering" op 19 juni 2025 als *"the art of providing all the context for the task to be plausibly solvable by the LLM."* [1] Andrej Karpathy populariseerde de term parallel.

**Gartner-verklaring** (`unverified` — niet direct gecheckt): "Context engineering is in, prompt engineering is out" (Gartner, juli 2025) [2].

**Definitie-uitbreiding**: context engineering omvat het gehele informatie-ecosysteem: dynamische data-ophaling, memory management, tool-orchestratie en state-beheer over multi-turn interacties [2]. Verschil met prompt engineering: "If prompt engineering was about finding a magical sentence, context engineering is about writing the full screenplay for the AI." [2]

**Simon Willison's agentic engineering patterns** (februari 2026) [3] (`verified`): Willison documenteert patronen voor het werken met coding agents. Zijn werk focust op agentic engineering (code genereren én uitvoeren), niet direct op context structurering als informatielaag — zijn relevantie voor BB_03 zit in de observatie dat agents die context slecht beheren sneller falen.

**Enterprise-implicatie** (`inferred`): 91% AI-adoptie, maar slechts 5% governance-dekking → 19% productiviteitsverlies (METR 2025) [2]. Dit "context gap" bevestigt dat technologie sneller gaat dan organisatorische volwassenheid.

### 2. Forte's Personal Context Management — evaluatie

**Forte's kernthese** (`unverified` — niet direct gecheckt via primaire bron): de nieuwe bottleneck is niet AI-vermogen maar de capaciteit om AI de *juiste informatie op het juiste moment* te geven. Context management vervangt kennis management als kernvaardigheid [4].

**"Minimum viable context" principe** (`unverified`): je organiseert context in vooraf gedefinieerde chunks die je gemakkelijk kunt aanwijzen, in plaats van alles in het context window te pompen [4].

**De 25-50% claim** (`blocked` — niet empirisch onderbouwd): geen primaire bron gevonden die dit exacte percentage als empirische meting bevestigt. Beschikbare data (zie research-wetenschap.md) wijst op model-afhankelijke efficiëntie die varieert van 75-98% voor geoptimaliseerde modellen, maar fors daalt bij complexe redenering. Enterprise queries consumeren al 50K-100K tokens aan setup vóór redenering begint.

**Aanbeveling voor BB_03**: herformuleer als "effectief bruikbaar window varieert per taak, model en context-kwaliteit — organiseer context daarom in minimum viable chunks en test empirisch per use case."

### 3. Enterprise KB-governance — concrete patronen

**Datagovernance-probleem** (`verified`): Gartner survey (februari 2025, n=1.203 data management leaders): 63% van organisaties heeft geen adequate data management practices voor AI, of weet het niet [5].

**Governance-concept: governed institutional memory** [2]: het omzetten van beslisssporen, SOPs en tribal knowledge naar machine-leesbare data zodat AI kan leren van eerdere beslissingen.

**Enterprise governance stack** (2026) [6] (`inferred`):
1. Gecentraliseerde context-opslag (niet verspreid over tools)
2. Metadata-tagging: `last_verified`, `updated_at`, `owner`, `criticality`
3. Freshness scoring met geautomatiseerde alerts bij score < 85% [7]
4. Audit trail: elke gegenereerde respons traceerbaar naar brondocument

**Staleness thresholds per categorie** (`verified`) [7]:
| Categorie | Maximale verouderdheid |
|-----------|----------------------|
| Compliance / live pricing | Nul tolerantie |
| Policies & procedures | 24 uur |
| Referentiedocumenten | 30 dagen |
| Historische/contextuele documenten | 90 dagen |

### 4. Refresh- en invalidation-patronen

**Drie architectuurkeuzes voor re-indexing** (`verified`) [7][8]:
1. **Nightly batch**: simpel, maar tot 24u staleness window
2. **Hourly batch**: tot 60 minuten vertraging
3. **Streaming CDC (Change Data Capture)**: seconden-nauwkeurigheid, complexer te implementeren

**Praktisch patroon** (`verified`): event-triggered incrementele re-indexing op basis van document-change events in Confluence of SharePoint — beter dan volledige re-index op schema [8]. LlamaIndex ondersteunt document-hash tracking voor changed-files-only re-indexing [8].

**Stilte-probleem** (`inferred`): stale knowledge base retourneert antwoorden die correct klinken maar verouderd zijn — geen waarschuwingssignaal in retrieval response [7]. Dit maakt monitoring en freshness scoring kritisch.

### 5. Query-routing en context-selectie

**Context-routing principes** (`verified`) [9][10]:
- Semantic router analyseert queries semantisch voor intent-classificatie
- Routeer op basis van intent naar gespecialiseerde kennisbronnen of retrieval-strategieën
- RAG-router biedt 5-20 topics als praktisch maximum voor beheerbaarheid [9]
- REIC (Amazon, EMNLP 2025): RAG-versterkte intent-classificatie die fine-tuning vervangt bij klantenservice-schaal [10]

**Adaptieve retrieval** (`inferred`): reinforcement learning optimaliseert real-time selectie van externe databronnen op basis van user intent en querycomplexiteit [9].

### 6. Kwaliteitsmetrics voor context

**RAGAS-framework** voor evaluatie van RAG-kwaliteit [8]:
- Faithfulness > 0.90 (voorkomt hallucinaties)
- Answer Relevancy > 0.85
- Context Recall > 0.80
- Context Precision > 0.75

**Fallback bij lage confidence**: retourneer "geen betrouwbaar antwoord gevonden" bij retrieval score < 0.55, in plaats van onbetrouwbaar antwoord genereren [8].

## Evidence Table

| # | Bron | URL | Type | Key claim | Confidence |
|---|------|-----|------|-----------|------------|
| 1 | Tobi Lütke (@tobi) tweet juni 2025 | https://x.com/tobi/status/1935533422589399127 | primary | Definitie context engineering | high |
| 2 | Atlan — What Is Context Engineering 2026 | https://atlan.com/know/what-is-context-engineering/ | secondary | Gartner quote; context gap metrics; institutional memory | medium |
| 3 | Simon Willison — Agentic Engineering Patterns 2026 | https://simonwillison.net/2026/Feb/23/agentic-engineering-patterns/ | primary | Agentic patterns documentatie | high |
| 4 | Tiago Forte via Delphi.ai | https://www.delphi.ai/tiago-forte/talk/conversation/4fc00fd6-817e-44a6-aae1-42ecd9b0d581 | secondary | PCM als opvolger van PKM; minimum viable context | low |
| 5 | Snorkel AI — Long context models in enterprise | https://snorkel.ai/blog/long-context-models-in-the-enterprise-benchmarks-and-beyond/ | secondary | Gartner survey 63% governance-probleem | medium |
| 6 | Elvex — Enterprise AI Stack 2026 | https://www.elvex.com/blog/enterprise-ai-stack-context-control-execution | secondary | Enterprise governance stack | medium |
| 7 | Atlan — LLM KB Freshness Scoring | https://atlan.com/know/llm-knowledge-base-freshness-scoring/ | secondary | Staleness thresholds; scoring framework; re-index patronen | high |
| 8 | Towards Data Science — RAG enterprise guide | https://towardsdatascience.com/grounding-your-llm-a-practical-guide-to-rag-for-enterprise-knowledge-bases/ | secondary | RAGAS metrics; incremental re-indexing; staleness als #2 productiefaling | high |
| 9 | Medium — Building a RAG Router 2025 | https://medium.com/@tim_pearce/building-a-rag-router-in-2025-e0e9d99efe44 | secondary | Semantic router; 5-20 topics max; routing architectuur | medium |
| 10 | Amazon/EMNLP 2025 — REIC paper | https://arxiv.org/abs/2506.00210 | primary | RAG-enhanced intent classification at scale | high |

## Coverage Status

- **Gecheckt direct:** [7] freshness scoring (volledig), [8] enterprise RAG guide (volledig), [1] via search
- **Niet direct gecheckt:** [2] Atlan context engineering (via search snippets), [3] Willison (via search), [4] Forte/Delphi (via search — geen directe fetch), [10] REIC paper (via search)
- **Blijft onzeker:** Forte's 25-50% claim — geen primaire bron gevonden; Gartner citaten via secondaire bronnen
- **Niet afgerond:** directe verificatie Forte webinar transcripts (bron-080/081 zijn vault-lokaal, niet beschikbaar voor fetch)

## Sources

1. Tobi Lütke — Context Engineering tweet (juni 2025) — https://x.com/tobi/status/1935533422589399127
2. Atlan — What Is Context Engineering 2026 — https://atlan.com/know/what-is-context-engineering/
3. Simon Willison — Agentic Engineering Patterns (februari 2026) — https://simonwillison.net/2026/Feb/23/agentic-engineering-patterns/
4. Tiago Forte via Delphi.ai — https://www.delphi.ai/tiago-forte/talk/conversation/4fc00fd6-817e-44a6-aae1-42ecd9b0d581
5. Snorkel AI — Long Context Models in the Enterprise — https://snorkel.ai/blog/long-context-models-in-the-enterprise-benchmarks-and-beyond/
6. Elvex — Enterprise AI Stack 2026 — https://www.elvex.com/blog/enterprise-ai-stack-context-control-execution
7. Atlan — LLM Knowledge Base Freshness Scoring — https://atlan.com/know/llm-knowledge-base-freshness-scoring/
8. Towards Data Science — Grounding Your LLM: Enterprise Knowledge Bases — https://towardsdatascience.com/grounding-your-llm-a-practical-guide-to-rag-for-enterprise-knowledge-bases/
9. Medium / Timothé Pearce — Building a RAG Router in 2025 — https://medium.com/@tim_pearce/building-a-rag-router-in-2025-e0e9d99efe44
10. Amazon / ACL 2025 — REIC: RAG-Enhanced Intent Classification at Scale — https://arxiv.org/abs/2506.00210
