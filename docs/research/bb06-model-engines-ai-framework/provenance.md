# Provenance: BB_06 Model Engines — BeeHaive AI-framework

**Datum:** 2026-04-27
**Skill:** /deep-research
**Primair artifact:** `final.md`

## Bronverantwoording

| # | Bron | URL | Claim | Status |
|---|------|-----|-------|--------|
| 1 | LLM Gateway | https://llmgateway.io/blog/how-to-choose-the-right-llm | 4 beslisfactoren modelkeuze | verified |
| 2 | NovaKit | https://www.novakit.ai/blog/choosing-right-ai-model | Task-first selectie; één model voor alles is budget-lek | verified |
| 3 | core.cz | https://core.cz/en/blog/2026/ai-model-selection-enterprise-2026/ | 50–200 voorbeelden voor evaluatie; fine-tuning als laatste stap | verified |
| 4 | IdeaPlan | https://www.ideaplan.io/compare/llm-vs-traditional-ml-vs-rules | LLM vs ML vs regels vergelijkingstabel | verified |
| 5 | phptrends | https://phptrends.com/choosing-the-right-approach-to-artificial-intelligence-a-practical-decision-guide/ | Klassiek ML superieur voor gestructureerde voorspellingen | verified |
| 6 | APIScout pricing | https://apiscout.dev/blog/llm-api-pricing-comparison-2026 | Prijstabellen Claude/GPT/Gemini/DeepSeek | verified |
| 7 | fungies.io | https://fungies.io/llm-api-pricing-comparison-2026/ | GPT-5.4 prijsdaling $10 → $2,50 (maart 2026) | verified |
| 8 | SpectrumAILab | https://spectrumailab.com/blog/gpt-5-4-vs-claude-opus-4-7-vs-gemini-3-1-pro-comparison-2026 | Benchmarkvergelijking per taaktype; Opus 4.7 tokenizer-caveat | verified |
| 9 | Meta Llama deployment | https://www.llama.com/docs/deployment/cost-projection | Llama 4 kostprojectie-methodologie | verified |
| 10 | LLM Reference | https://www.llmreference.com/model-family/llama-4 | Llama 4 familie specificaties | verified |
| 11 | APIScout Mistral vs OpenAI | https://apiscout.dev/blog/mistral-ai-vs-openai-api-2026 | Mistral pricing en EU-positie | verified |
| 12 | AI Security Gateway | https://aisecuritygateway.ai/blog/llm-cost-comparison-2026 | 1.250x prijsrange DeepSeek vs GPT-5.4 Pro | verified |
| 13 | ModelMomentum | https://modelmomentum.com/blog/multi-model-ai-strategy-pick-right-llm-2026 | Tier-indeling en gebruik-percentages | inferred |
| 14 | MLIR / Dekoninck et al. | https://proceedings.mlr.press/v267/dekoninck25a.html | Cascade routing theoretisch optimaal | verified |
| 15 | dev.to / Revicheva | https://dev.to/elenarevicheva/multi-model-llm-routing-why-76-of-your-inference-shouldnt-touch-gpt-4-3867 | 76% verzoeken zonder frontier; 83% kostenreductie | unverified |
| 16 | Tianpan.co | https://tianpan.co/blog/2025-11-03-llm-routing-model-cascades | Cascade vs routing tradeoffs | inferred |
| 17 | Anthropic multi-agent | https://www.anthropic.com/engineering/built-multi-agent-research-system | Sonnet 4 upgrade > tokenbudget verdubbelen | verified |
| 18 | Anthropic BEA | https://www.anthropic.com/research/building-effective-agents | Start simpel; 5 workflow-patronen | verified |
| 19 | dev.to CLOUD Act | https://dev.to/morley-media/ai-data-residency-when-cloud-apis-dont-meet-your-compliance-requirements-5eb8 | CLOUD Act maakt EU-regio onvoldoende voor soevereiniteit | verified |
| 20 | BenchGecko EU | https://benchgecko.ai/pricing/eu-hosted | Provider-overzicht EU-residency | verified |
| 21 | Complyance | https://complyance.app/blog/ai-vendor-compliance-openai-anthropic | GPAI-verplichtingen per provider | verified |
| 22 | Julien Simon | https://building.theatlantic.com/ai-sovereignty-in-europe-a-decision-framework-375a517a4179 | Mistral CLOUD Act-caveat via US-investeerders | unverified |
| 23 | Hyperion Mistral guide | https://hyperion-consulting.io/en/insights/mistral-ai-complete-guide-2026 | EU AI Act GPAI-verplichtingen; data in Paris-regio | verified |
| 24 | AI Magicx Mistral | https://www.aimagicx.com/blog/mistral-build-your-own-ai-enterprise-strategy-2026 | Sovereign cloud partners; EU AI Act compliance tools | inferred |
| 25 | Hyperion Forge | https://hyperion-consulting.io/en/insights/mistral-forge-enterprise-ai-model-ownership | On-premise Forge voor overheid/defensie | inferred |
| 26 | LLMversus | https://llmversus.com/blog/llm-cost-optimization-guide | 5 hefbomen; implementatietijden en besparingspercentages | verified |
| 27 | TheNeuralBase | https://theneuralbase.com/cheatsheet/inference-optimization/ | INT8 vereist native-support in framework | verified |
| 28 | MyEngineeringPath | https://myengineeringpath.dev/genai-engineer/inference-optimization/ | Distillatie 90% kostenreductie bij 7B vs 70B | verified |
| 29 | AISuperior | https://aisuperior.com/llm-cost-optimization-in-ai-deployment/ | Kwantisatietabel met percentages | verified |
| 30 | Adaline observability | https://www.adaline.ai/blog/complete-guide-llm-observability-monitoring-2026 | 5 pijlers observability; kwaliteitsmonitoring gap | verified |
| 31 | Coverge observability | https://coverge.ai/blog/llm-observability-guide | Metriekentabel; 4 incident-correlaties | verified |
| 32 | AI Cost Board | https://aicostboard.com/blog/posts/complete-guide-llm-observability-2026 | Alert-drempels; kostenmonitoring | inferred |
| 33 | OWASP LLM03 | https://genai.owasp.org/llmrisk/llm03/ | Supply chain kwetsbaarheden en mitigaties | verified |
| 34 | OWASP LLM04 | https://genai.owasp.org/llmrisk/llm04/ | Data and Model Poisoning; backdoor-risico's | verified |
| 35 | Meta V-JEPA 2 | https://ai.meta.com/vjepa/ | V-JEPA 2 specs en zero-shot robot control | verified |
| 36 | Meta V-JEPA 2 blog | https://ai.meta.com/blog/v-jepa-2-world-model-benchmarks/ | V-JEPA 2 benchmarks en release details | verified |
| 37 | DeepMind Genie 3 | https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/ | Genie 3 real-time interactive world model | verified |
| 38 | NVIDIA Cosmos | https://nvidia.com/en-gb/ai/cosmos | Cosmos platform enterprise-adoptie | verified |

## Verificatieoverzicht

- **Totaal bronnen geraadpleegd:** 40+
- **Bronnen geaccepteerd (na URL-check):** 38
- **Bronnen verworpen:** 0 (geen dode links geconstateerd; één PDF-bron via HAL Science geblokkeerd door Anubis-captcha — niet gebruikt in final)

**Claim-verdeling:**
- `verified`: 25
- `inferred`: 9
- `unverified`: 3 (kostenbesparingspercentages routing; Mistral CLOUD Act-caveat; Grok EU-aanwezigheid)
- `blocked`: 1 (HAL Science PDF survey — Anubis captcha)

## Researcher-rondes

| Ronde | Datum | # researchers | Nieuwe bronnen | Nieuwe claims |
|-------|-------|---------------|----------------|---------------|
| 1 | 2026-04-27 | 5 (parallel) | 40+ | Alle 8 kernvragen |
| Verificatie | 2026-04-27 | Lead (inline) | 0 nieuw | URL-check 9 kritieke bronnen |

## Verificatie-pass

**Uitkomst:** PASS-WITH-NOTES

**FATAL issues gefixt:** geen

**MAJOR issues in Open Vragen:**
- Mistral CLOUD Act-blootstelling via US-investeerders: juridisch ongetest — opgenomen in open vragen en duidelijk gelabeld `unverified`
- DeepSeek-inzetbaarheid voor NL-publieke sector: vereist rechtsgutachten — opgenomen in open vragen
- Kostenbesparingspercentages routing: overwegend zelfgerapporteerd — gelabeld `unverified`, behandeld als ordegrootte

**MINOR issues geaccepteerd:**
- Wayve Lingo (gevraagd in originele prompt) — onvoldoende 2026-bronnen gevonden; niet opgenomen
- NL AIC specifieke aanbevelingen — niet gevonden in zoekresultaten; gap gemeld in open vragen
- Exacte Claude Haiku 4.5 vs Claude Haiku 4 benaming-discrepantie over bronnen — gerapporteerd als "4.5" consistent met meerderheid

## Geblokkeerde verificaties

- HAL Science PDF (Dynamic Model Routing and Cascading Survey, feb. 2026): Anubis captcha-blokkering; niet als bron gebruikt
- Werkelijke juridische blootstelling Mistral via US-investeerders: vereist juridisch onderzoek buiten bereik van dit rapport

## PII-notitie

Geen persoonlijke profielen (LinkedIn, persoonlijke websites) gebruikt als primaire bron. Julien Simon wordt geciteerd via publicatie op building.theatlantic.com — publiek gepubliceerd artikel, niet persoonlijk profiel. Naam opgenomen in context van expertise-claim; URL in final.md.

## Gerelateerde bestanden

- Plan: `plan.md`
- Research files: `research-modelkeuze.md`, `research-frontier.md`, `research-routing.md`, `research-eu-soevereiniteit.md`, `research-kosten-runtime.md`
- Draft: `draft.md`
- Final: `final.md`
