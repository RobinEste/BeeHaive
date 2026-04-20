# Provenance: Dynamic Context als informatie-architectuur 2024-2026

**Datum:** 2026-04-20
**Skill:** /deep-research
**Primair artifact:** `final.md`

## Bronverantwoording

| # | Bron | URL | Claim | Status |
|---|------|-----|-------|--------|
| 1 | Tobi Lütke tweet juni 2025 | https://x.com/tobi/status/1935533422589399127 | "Context engineering is the art of providing all the context..." | verified |
| 2 | Atlan — Context Engineering 2026 | https://atlan.com/know/what-is-context-engineering/ | Gartner "context engineering is in" juli 2025; 91% adoptie 5% governance | unverified |
| 3 | Chroma Research / Morph | https://www.morphllm.com/context-rot | 18 modellen universele degradatie; 30%+ drop midden; 90.2% multi-agent verbetering | verified |
| 4 | Liu et al. TACL 2023 | https://arxiv.org/abs/2307.03172 | U-curve positie-effect; significant voor alle modellen | verified |
| 5 | Atlan — Freshness Scoring | https://atlan.com/know/llm-knowledge-base-freshness-scoring/ | 4 freshness-dimensies; staleness-drempels per categorie; CDC vs batch | verified |
| 6 | Protecto.ai — AI Data Privacy | https://www.protecto.ai/blog/ai-data-privacy/ | PII lekkagerisico in RAG; filterstrategieën | unverified |
| 7 | Arxiv 2412.04697 — DP-RAG | https://arxiv.org/abs/2412.04697 | Superieure prestaties bij ε≈10; privacy-budget allocatie | verified |
| 8 | Understanding AI (Timothy Lee) | https://www.understandingai.org/p/context-rot-the-emerging-challenge | Adobe Research data; model-specifieke percentages; Chroma-naam voor "context rot" | verified |
| 9 | Atlan — Context Window Limitations | https://atlan.com/know/llm-context-window-limitations/ | Efficiëntietabel per model; enterprise queries 50K-100K tokens setup | inferred |
| 10 | RAGFlow — From RAG to Context | https://ragflow.io/blog/rag-review-2025-from-rag-to-context | RAG → context engine evolutie; hybrid search 33-47%; PTI-pipelines; TreeRAG | inferred |
| 11 | Anthropic — Contextual Retrieval | https://www.anthropic.com/news/contextual-retrieval | 67% reductie retrievalfouten; $1.02/M tokens preprocessing | verified |
| 12 | Microsoft GraphRAG | https://microsoft.github.io/graphrag/ | GraphRAG open source; LazyGraphRAG; qualitative claims | unverified |
| 13 | Medium / RAG Router 2025 | https://medium.com/@tim_pearce/building-a-rag-router-in-2025-e0e9d99efe44 | Semantic router; 5-20 topics max | inferred |
| 14 | Amazon/ACL 2025 — REIC | https://arxiv.org/abs/2506.00210 | RAG-enhanced intent classification overtreft fine-tuning | verified |
| 15 | Towards Data Science — RAG enterprise | https://towardsdatascience.com/grounding-your-llm-a-practical-guide-to-rag-for-enterprise-knowledge-bases/ | Chunking impact; RAGAS metrics; incremental re-indexing; traceerbaarheid | verified |
| 16 | Weaviate — Chunking Strategies | https://weaviate.io/blog/chunking-strategies-for-rag | Chunk-grootte aanbevelingen; agentic chunking | inferred |
| 17 | Vectorize.io — Mem0 vs Letta 2026 | https://vectorize.io/articles/mem0-vs-letta | Productie-rijpheid; 49.0% LongMemEval; enterprise beperkingen | verified |
| 18 | Arxiv 2504.19413 — Mem0 paper | https://arxiv.org/abs/2504.19413 | 26% verbetering; 91% lagere latentie; AWS partnership; SOC 2 HIPAA | verified |
| 19 | Wikipedia — Model Context Protocol | https://en.wikipedia.org/wiki/Model_Context_Protocol | 5.800+ servers; drie context-datatypes; beveiligingsrisico's | unverified |
| 20 | Arxiv 2508.17222 — GraphRAG Privacy | https://arxiv.org/pdf/2508.17222 | GraphRAG verhoogt PII-reconstructierisico | verified |
| 21 | ScienceDirect — Entity perturbation | https://www.sciencedirect.com/science/article/abs/pii/S0306457325000913 | Privacy-utility tradeoff; entiteitsperturbatie | verified |
| 22 | Aparavi — Data Protection AI 2026 | https://aparavi.com/whitepapers/reinventing-data-protection-for-the-ai-era-2026-whitepaper/ | Data lineage voor AI-context | unverified |
| 23 | Simon Willison — Agentic Patterns | https://simonwillison.net/2026/Feb/23/agentic-engineering-patterns/ | Agentic engineering def; TDD met coding agents | verified |

## Verificatieoverzicht

- **Totaal bronnen geraadpleegd:** 23
- **Bronnen geaccepteerd (na URL-check):** 22
- **Bronnen verworpen** (dode link, onverifiëerbaar): 0
- **Bronnen met directe fetch-verificatie:** 13
- **Bronnen via search-snippets (niet volledig gelezen):** 10

**Claim-verdeling:**
- `verified`: 13
- `inferred`: 5
- `unverified`: 5
- `blocked`: 1 (Forte's 25-50% claim)

## Researcher-rondes

| Ronde | Datum | # Researchers | Nieuwe bronnen | Nieuwe claims |
|-------|-------|---------------|----------------|---------------|
| 1 | 2026-04-20 | 4 (wetenschap, architectuur, praktijk, privacy) | 23 | ~60 |

Geen tweede ronde nodig — alle 7 BB_03-checklist-items beantwoord, geen significante gaten geïdentificeerd.

## Verificatie-pass

**Uitkomst:** PASS-WITH-NOTES

**FATAL issues gefixt:** geen

**MAJOR issues in Open Vragen:**
1. GraphRAG nauwkeurigheidscijfers (80% vs 50%) niet in officiële Microsoft docs gevonden — gelabeld `unverified`. Kan gebruikt worden als directie (complexe queries profiteren), niet als exacte metric.
2. 2026-modelversies (Claude 4.7, GPT-5.4, Gemini 3) niet direct gebenchmarkt — expliciete noot in rapport.

**MINOR issues geaccepteerd:**
1. Gartner-quote via secondaire bron (Atlan) — plausibel maar niet direct geverifieerd.
2. Forte's PCM primaire bronnen (bron-080/081) zijn vault-lokaal en konden niet worden gefetcht — 25-50% claim `blocked` conform integriteitsregels.
3. Arxiv 2508.17222 (GraphRAG Privacy) dateert augustus 2025 — na primair tijdvenster, maar relevant en opgenomen.

## Geblokkeerde verificaties

- **Forte's "25-50% bruikbaar context window"**: primaire bron is vault-lokaal (bron-080/081, webinar transcripts). Niet publiek toegankelijk voor fetch. Claim is niet empirisch onderbouwbaar op basis van publieke bronnen.
- **MIT Press TACL directe URL (403)**: https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00638/ gaf 403-fout. Geverifieerd via arXiv-preprint (identieke paper, open access).
- **Milvus context rot blog**: redirect-fout (>10 redirects). Informatie opgenomen via arXiv en morphllm.com equivalenten.

## PII-notitie

Geen PII-bronnen in dit onderzoek. Alle geciteerde bronnen zijn publieke web-content. Geen LinkedIn of persoonlijke profielen gebruikt.

## Gerelateerde bestanden

- Plan: `plan.md`
- Research files: `research-wetenschap.md`, `research-architectuur.md`, `research-praktijkpatronen.md`, `research-privacy-kwaliteit.md`
- Draft: `draft.md`
- Final: `final.md`
