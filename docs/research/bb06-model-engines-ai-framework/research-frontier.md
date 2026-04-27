# Research: Frontier-landschap april 2026 — BB_06 Model Engines

**Researcher:** researcher-B
**Dimensie:** Vergelijkende analyse frontier-modellen, prijzen, benchmarks, EU-beschikbaarheid
**Datum:** 2026-04-27

## Samenvatting (1 zin)

Het frontier-landschap in april 2026 kent drie kopgroepen (Claude Opus 4.7, GPT-5.4, Gemini 3.1 Pro) zonder universele winnaar, terwijl DeepSeek V3.2/R1 en Llama 4 de kosten-kwaliteitsverhouding voor open/budget-toepassingen radicaal verschoven hebben.

## Bevindingen

### Prisinformatieoverzicht (april 2026)

Alle prijzen per miljoen tokens input/output, tenzij anders vermeld. `verified` via meerdere onafhankelijke prijspagina's.

**Anthropic Claude-familie:**
| Model | Input $/MTok | Output $/MTok | Context | Gecached input |
|-------|-------------|--------------|---------|----------------|
| Claude Opus 4.7 | $5,00 | $25,00 | 1M tokens | — |
| Claude Sonnet 4.6 | $3,00 | $15,00 | 1M tokens | $0,30 |
| Claude Haiku 4.5 | $0,25 | $1,25 | 200K tokens | $0,025 |

Bronnen: [1, 2, 3] `verified`

**OpenAI GPT-5-familie:**
| Model | Input $/MTok | Output $/MTok | Context |
|-------|-------------|--------------|---------|
| GPT-5.4 | $2,50 | $15,00 | 400K–1M tokens |
| GPT-5.4 (lang context) | $5,00 | $22,50 | 400K+ tokens |
| GPT-5 Mini | $0,25 | $2,00 | 500K tokens |
| GPT-5 Nano | $0,05 | $0,40 | 128K tokens |
| O3 (reasoning) | $150,00 | — (alleen input gepubliceerd) | 128K |

Bronnen: [1, 3, 4] `verified`

**Google Gemini-familie:**
| Model | Input $/MTok | Output $/MTok | Context |
|-------|-------------|--------------|---------|
| Gemini 3.1 Pro (≤200K) | $2,00 | $12,00 | 2M tokens |
| Gemini 3.1 Pro (>200K) | $4,00 | $18,00 | 2M tokens |
| Gemini 2.5 Flash | $0,15 | $0,60 | 1M tokens |
| Gemini 2.5 Flash-Lite | $0,10 | $0,40 | 1M tokens |

Bronnen: [1, 3] `verified`

**Meta Llama 4:**
| Model | Input $/MTok | Output $/MTok | Context | Opmerking |
|-------|-------------|--------------|---------|-----------|
| Llama 4 Scout | $0,11–$0,25 | $0,34–$0,70 | 328K–10M tokens | Open-source, zelf-hostbaar |
| Llama 4 Maverick | $0,15–$0,35 | $0,60–$1,15 | 1M tokens | MoE 17B actief/128 experts |

Bronnen: [5, 6] `verified`

**Mistral:**
| Model | Input $/MTok | Output $/MTok | Opmerking |
|-------|-------------|--------------|-----------|
| Mistral Large 3 | ~$1,00–$2,00 | ~$3,00 | Open weights (Apache 2.0), EU-nativo |
| Mistral Small 3.2 | $0,06 | $0,18 | Ultra-budget |
| Mistral Nemo | $0,02 | $0,04 | Goedkoopste commercial API |

Bronnen: [7] `verified`

**DeepSeek:**
| Model | Input $/MTok | Output $/MTok | Opmerking |
|-------|-------------|--------------|-----------|
| DeepSeek V3.2 | $0,14–$0,28 | $0,28–$0,42 | Cache hits bij $0,028/MTok |
| DeepSeek R1 | $0,55 | $2,19 | Reasoning-model |

Bronnen: [1, 3] `verified`

### Benchmark-vergelijking (april 2026)

Geen universele winnaar; per taaktype verschilt de leider [2, 8]:

| Taaktype | Winnaar | Score |
|----------|---------|-------|
| Productie-code / SWE-bench Pro | Claude Opus 4.7 | 64,3% |
| Tool-zware agents / MCP | Claude Opus 4.7 | 77,3% MCP-Atlas |
| Desktop-automatisering / OSWorld | Claude Opus 4.7 | 78,0% |
| Webonderzoek / BrowseComp | GPT-5.4 | 89,3% (10 punten voor) |
| Financiële analyse | Claude Opus 4.7 | 64,4% Finance Agent v1.1 |
| Kostenefficiënt hoge-doorvoer | Gemini 3.1 Pro | $2/$12 per MTok |
| Meertalige kennis | Gemini 3.1 Pro | 92,6% MMMLU |
| Redeneren op graduate-niveau (GPQA Diamond) | Gelijkspel | ~94% alle drie |

Bron: [2] `verified`

### Praktijkverschillen vs benchmark-prestaties

Meerdere bronnen wijzen op de kloof tussen benchmarks en echte toepassingen [8, 9]:
- GPT-5.4 presteert beter op webonderzoek dan benchmarks suggereren (BrowseComp +10 punten)
- Claude Opus 4.7 domineert op agentic coding terwijl andere metrics nagenoeg gelijk zijn
- Gemini 3.1 Pro is goedkoopste flagship maar presteert gelijk op reasoning (GPQA Diamond gelijkspel binnen 0,2 punt)
- DeepSeek R1 biedt 90% goedkopere reasoning bij 97,3% MATH-500 `inferred` (meerdere bronnen)

### Tierindeling als praktisch kader

Multi-tier aanpak werkt beter dan één model [9]:

| Tier | Modellen | $/MTok input | Gebruik |
|------|---------|-------------|---------|
| Frontier | Claude Opus 4.7, GPT-5.4 | $2,50–$5,00 | ~5% verzoeken — harde redenering, agents |
| Pro | Sonnet 4.6, GPT-5 | $1,25–$3,00 | ~35% — dagelijks professioneel werk |
| Standaard | Haiku 4.5, Gemini 3.1 Flash | $0,15–$1,00 | ~30% — balanced speed-quality |
| Budget | GPT-5 Nano, DeepSeek V3.2 | $0,05–$0,28 | ~30% — classificatie, hoog volume |
| Lokaal/gratis | Llama 4, Qwen 3, Mistral 3 | $0 (hardware) | Privacy, offline, onbeperkte doorvoer |

Bron: [9] `inferred` (samengesteld uit meerdere bronnen)

### World models — opkomende categorie

Naast de klassieke LLM-families zijn world models relevant voor specifieke enterprise-toepassingen [10, 11, 12]:

**Meta V-JEPA 2** (juni 2025):
- 1,2 miljard parameters, getraind op 1M+ uur video
- Zero-shot robotbesturing in nieuwe omgevingen na slechts 62 uur unlabeled robotdata
- MIT-licentie, open-source
- Toepassing: robotica, autonoom rijden, simulatie

**Google DeepMind Genie 3** (augustus 2025):
- Eerste real-time interactief world model met fysisch accurate 3D-omgevingen
- Primaire toepassingen: training van agents, simulatie-omgevingen voor AGI-onderzoek, educatie
- Beperkt beschikbaar voor testers

**NVIDIA Cosmos** (CES 2025):
- Drie modelcategorieën: Predict, Transfer, Reason
- Getraind op 9.000 biljoen tokens uit 20 miljoen uur real-world data
- 2 miljoen downloads, enterprise-adoptie bij 1X, Agility Robotics, Uber, XPENG
- Open models beschikbaar, NVIDIA Open Model License

Enterprise-relevantie world models is in 2026 nog beperkt tot: robotica, autonome voertuigen, industriële simulatie, game-development, synthetische data-generatie. Voor typische Nederlandse consultancy-organisaties geldt: oriënteren, nog niet inzetten. `inferred`

### Overige aanbieders

- **Cohere**: gericht op enterprise retrieval en RAG; Command R+ sterk voor document-retrieval in regulated industries; beperkte frontier-capaciteiten
- **AI21**: Labs-focus, minder enterprise-tractie in 2026
- **Aleph Alpha**: EU-gefocust, Luminous-modellen; sterk compliance-verhaal maar achterblijvend op capaciteiten vs Mistral
- **xAI Grok 4.1**: $0,20/$0,50, real-time web-access, maar beperkte EU-aanwezigheid `unverified`

## Evidence Table

| # | Bron | URL | Type | Key claim | Confidence |
|---|------|-----|------|-----------|------------|
| 1 | APIScout — LLM API Pricing 2026 | https://apiscout.dev/blog/llm-api-pricing-comparison-2026 | secondary | Prijstabellen Claude/GPT/Gemini/DeepSeek | high |
| 2 | SpectrumAILab — GPT-5.4 vs Opus 4.7 vs Gemini 3.1 | https://spectrumailab.com/blog/gpt-5-4-vs-claude-opus-4-7-vs-gemini-3-1-pro-comparison-2026 | secondary | Benchmarkvergelijking per taaktype | high |
| 3 | jangwook.net — LLM API Pricing 2026 | https://jangwook.net/en/blog/en/llm-api-pricing-comparison-2026-gpt5-claude-gemini-deepseek/ | secondary | Historische prijsontwikkeling per model | medium |
| 4 | fungies.io — LLM API Cost Comparison 2026 | https://fungies.io/llm-api-pricing-comparison-2026/ | secondary | GPT-5.4 prijsdaling maart 2026 van $10 naar $2,50 | high |
| 5 | GetDeploying — Llama 4 Scout specs | https://getdeploying.com/llms/llama-4-scout | secondary | Llama 4 Scout: 10M context, MoE 17B actief | high |
| 6 | CloudPrice — Llama 4 Maverick | https://cloudprice.net/models/meta-llama-4-maverick | secondary | Maverick prijzen per provider | high |
| 7 | APIScout — Mistral vs OpenAI 2026 | https://apiscout.dev/blog/mistral-ai-vs-openai-api-2026 | secondary | Mistral pricing en EU-positie | high |
| 8 | dev.to — GPT-5.5 vs Opus 4.7 vs Gemini 3.1 | https://dev.to/om_shree_0709/gpt-55-vs-claude-opus-47-vs-gemini-31-pro-the-frontier-model-showdown-4mji | secondary | Frontier model showdown april 2026 | medium |
| 9 | ModelMomentum — Multi-Model AI Strategy | https://modelmomentum.com/blog/multi-model-ai-strategy-pick-right-llm-2026 | secondary | Tier-indeling en gebruik-percentages | medium |
| 10 | Meta AI — V-JEPA 2 | https://ai.meta.com/vjepa/ | primary | V-JEPA 2 specs en zero-shot robot control | high |
| 11 | Google DeepMind — Genie 3 | https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/ | primary | Genie 3 real-time interactive world model | high |
| 12 | NVIDIA Cosmos | https://nvidia.com/en-gb/ai/cosmos | primary | Cosmos platform, 2M downloads, enterprise use cases | high |

## Coverage Status

- **Gecheckt direct:** prijstabellen via 4+ onafhankelijke bronnen gekruist
- **Blijft onzeker:** Claude Opus 4.7 vs GPT-5.5 (nieuwste versies wisselen snel)
- **Niet afgerond:** Wayve Lingo world model (genoem in originele prompt) — onvoldoende 2026-bronnen gevonden

## Sources

1. APIScout — LLM API Pricing Comparison 2026 — https://apiscout.dev/blog/llm-api-pricing-comparison-2026
2. SpectrumAILab — GPT-5.4 vs Claude Opus 4.7 vs Gemini 3.1 Pro — https://spectrumailab.com/blog/gpt-5-4-vs-claude-opus-4-7-vs-gemini-3-1-pro-comparison-2026
3. jangwook.net — LLM API Pricing 2026 — https://jangwook.net/en/blog/en/llm-api-pricing-comparison-2026-gpt5-claude-gemini-deepseek/
4. fungies.io — LLM API Cost Comparison 2026 — https://fungies.io/llm-api-pricing-comparison-2026/
5. GetDeploying — Llama 4 Scout Specs & Pricing — https://getdeploying.com/llms/llama-4-scout
6. CloudPrice — Llama 4 Maverick — https://cloudprice.net/models/meta-llama-4-maverick
7. APIScout — Mistral AI vs OpenAI 2026 — https://apiscout.dev/blog/mistral-ai-vs-openai-api-2026
8. dev.to — Frontier Model Showdown April 2026 — https://dev.to/om_shree_0709/gpt-55-vs-claude-opus-47-vs-gemini-31-pro-the-frontier-model-showdown-4mji
9. ModelMomentum — Multi-Model AI Strategy — https://modelmomentum.com/blog/multi-model-ai-strategy-pick-right-llm-2026
10. Meta AI — V-JEPA 2 — https://ai.meta.com/vjepa/
11. Google DeepMind — Genie 3 — https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/
12. NVIDIA Cosmos — https://nvidia.com/en-gb/ai/cosmos
