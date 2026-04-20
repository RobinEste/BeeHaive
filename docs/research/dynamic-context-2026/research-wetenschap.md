# Research: Wetenschap — Dynamic Context als informatie-architectuur 2024-2026

**Researcher:** researcher-wetenschap
**Dimensie:** Context rot, U-curve, long-context benchmarks, re-ordering-effecten op frontier-modellen (2024-2026)
**Datum:** 2026-04-20

## Samenvatting (1 zin)

Context rot is een empirisch vastgesteld en universeel fenomeen op alle 18 geteste frontier-modellen (2025), met 30%+ nauwkeurigheidsverliezen voor informatie in het midden van de context, maar nieuwere modellen vertonen minder degradatie — wat het aanpassen van context-engineering strategieën urgent maakt.

## Bevindingen

### 1. Context rot — definitie en mechanismen

Context rot is de meetbare prestatiedegradatie die LLM's ervaren naarmate de input langer wordt, zelfs als het context window niet vol is [1]. Chroma's onderzoek (2025) documenteerde drie samengestelde mechanismen:

1. **Lost-in-the-Middle effect** (`verified`): informatie in het midden van de context krijgt 30%+ lagere nauwkeurigheid dan informatie aan het begin of einde. Oorspronkelijk gedocumenteerd door Liu et al. (Stanford/TACL, 2024) [2], bevestigd op alle 18 frontier-modellen in Chroma-onderzoek [1].

2. **Attention dilution** (`inferred`): bij 100K tokens berekent het model 10 miljard paargewijze relaties. Softmax-normalisatie zorgt ervoor dat elk aandachtsgewicht krimpt naarmate de context groeit [1].

3. **Distractor interference** (`verified`): semantisch vergelijkbare maar irrelevante content activeert sterk negatieve interferentie, met name bij code-zoektaken waar veel resultaten gedeeld vocabulaire hebben [1].

### 2. Empirische resultaten per frontier-model (2025)

Adobe Research (februari 2025) testte een two-hop redenering-taak over stijgende contextlengtes [3]:

| Model | Nauwkeurigheid kort | Nauwkeurigheid lang | Daling |
|-------|--------------------|--------------------|--------|
| GPT-4o | 99% | 70% | -29% |
| Claude 3.5 Sonnet | 88% | 30% | -58% |
| Gemini 2.5 Flash | 94% | 48% | -46% |
| Llama 4 Scout | 82% | 22% | -60% |

*Let op: dit zijn 2025-data voor specifieke modellen — 2026 frontier-modellen (Claude 4.7, GPT-5.4, Gemini 3) zijn hier niet direct gemeten. Degradatie is aangetoond maar absolute waarden zullen verschillen per model-versie.* (`unverified` voor 2026-specifieke modellen)

Chroma (2025): vroege en late context haalt 85-95% nauwkeurigheid, midden-secties zakken naar 76-82% [1].

### 3. Effectief bruikbaar context window

Empirische tests tonen dat modellen met 1M-token windows zelden meer dan 50-60% van dat window bruikbaar redenering ondersteunen [4] (`inferred` — gecombineerd uit meerdere bronnen):

| Model | Advertised | Praktische efficiëntie | Primaire beperking |
|-------|-----------|----------------------|-------------------|
| GPT-4.1 | 1M tokens | ~98% | Kosten bij schaal |
| Claude Opus 4 | 200K tokens | ~92% | KV cache limiet |
| Llama 4 Scout | 10M tokens | ~97% | Deployment overhead |
| Grok 3 | 1M tokens | 75-87% | Grootste gap |
| Gemini 2.5 Pro | 1M tokens | ~92% | Latency |

*Context kwaliteit > context window grootte* is het leidende principe voor enterprise AI in 2026 [4].

**Over Forte's "25-50% bruikbaar" claim:** er bestaat geen directe empirische onderbouwing voor dit exacte percentage als universele regel. De beschikbare data wijst op model-afhankelijke efficiëntie, typisch 75-98% voor geoptimaliseerde modellen maar met forse dalingen bij complexe redenering. Enterprise queries consumeren 50K-100K tokens aan setup-context voordat redenering begint [4]. De Forte-claim is niet falsifieerbaar in zijn huidige formulering — het is beter te herformuleren als: *"Effectief bruikbaar window varieert per taak, modelversie en context-kwaliteit."* (`inferred`)

### 4. Context rot in agentic systemen

60% van de agent-tijd wordt besteed aan context ophalen in plaats van redenering [1]. Taakduur-verdubbeling verviervoudigt foutpercentages door cumulatieve context-accumulatie [1]. (`verified` — Chroma onderzoek)

**Multi-agent isolatie** verbetert prestaties met 90.2%: subagents bevatten zoekruis in geïsoleerde context windows in plaats van de primaire agent te vervuilen [1]. (`verified`)

### 5. Temporele context — context staleness

Modellen worden niet automatisch bijgewerkt wanneer bronbestanden veranderen. Context-veroudering vindt drie mechanismen:

1. **Model knowledge cutoff**: ingebakken kennis wordt stale (los van context-window)
2. **Index-lag**: vectorindex loopt achter op bronupdates (tot 24u bij batch-reindex)
3. **Session decay**: binnen een sessie accumuleren verouderde teksten bij gebrek aan invalidation [5]

## Evidence Table

| # | Bron | URL | Type | Key claim | Confidence |
|---|------|-----|------|-----------|------------|
| 1 | Chroma Research 2025 — Context Rot Guide | https://www.morphllm.com/context-rot | secondary | 18 modellen tonen universele degradatie; 30%+ drop midden-positie | high |
| 2 | Liu et al. (Stanford/TACL 2024) — Lost in the Middle | https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00638/119630/ | primary | U-curve positie-effect; significant voor alle geteste modellen | high |
| 3 | Understanding AI (Timothy Lee) — Context Rot challenge 2025 | https://www.understandingai.org/p/context-rot-the-emerging-challenge | secondary | Adobe Research data; model-specifieke percentages | high |
| 4 | Atlan — LLM Context Window Limitations 2026 | https://atlan.com/know/llm-context-window-limitations/ | secondary | Frontier model efficiency tabel; enterprise-gebruik patronen | medium |
| 5 | Atlan — LLM Knowledge Base Freshness Scoring | https://atlan.com/know/llm-knowledge-base-freshness-scoring/ | secondary | Freshness metrics, staleness thresholds | medium |

## Coverage Status

- **Gecheckt direct:** [1] morphllm.com (volledig gelezen), [3] understandingai.org (volledig gelezen), [4] atlan context window (volledig gelezen), [5] atlan freshness (volledig gelezen)
- **Niet direct gecheckt:** [2] Liu et al. TACL paper (abstract en samenvatting via morphllm); arXiv preprint beschikbaar op https://arxiv.org/abs/2307.03172
- **Blijft onzeker:** 2026-specifieke data voor Claude 4.7, GPT-5.4, Gemini 3 (niet beschikbaar of niet gepubliceerd); Forte's 25-50% claim kon niet empirisch worden geverifieerd
- **Niet afgerond:** directe benchmark-vergelijking van 2026 frontier-modellen op long-context taken (geen publieke benchmarks gevonden voor Claude 4.7 specifiek)

## Sources

1. Chroma Research / Morph — Context Rot Complete Guide — https://www.morphllm.com/context-rot
2. Liu et al. — Lost in the Middle (TACL 2024) — https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00638/119630/Lost-in-the-Middle-How-Language-Models-Use-Long-Contexts (arXiv: https://arxiv.org/abs/2307.03172)
3. Timothy Lee / Understanding AI — Context Rot Emerging Challenge 2025 — https://www.understandingai.org/p/context-rot-the-emerging-challenge
4. Atlan — LLM Context Window Limitations 2026 — https://atlan.com/know/llm-context-window-limitations/
5. Atlan — LLM Knowledge Base Freshness Scoring — https://atlan.com/know/llm-knowledge-base-freshness-scoring/
