# Research: Kosten, runtime, observability en risico's — BB_06 Model Engines

**Researcher:** researcher-E
**Dimensie:** Kostenoptimalisatie, operationele runtime, observability, OWASP-risico's
**Datum:** 2026-04-27

## Samenvatting (1 zin)

LLM-kosten zijn reduceerbaar met 70–94% via een gelaagde aanpak (model-rightsizing → prompt caching → batch-API → prompt-trimmen), terwijl observability verder gaat dan latency/uptime omdat een HTTP 200 nog steeds een hallucinatoire respons kan bevatten.

## Bevindingen

### Kostenoptimalisatie — vijf hefbomen in volgorde van impact

**Hefboom 1: Model right-sizing (60–80% besparing, 1–2 weken)**
- Meest impactvolle stap: vervang frontier-model door passend mid-tier of budget-model
- Praktijkvoorbeeld: klantenservicebot op Claude Opus 4.5 ($15/$75) vs Llama 4 Scout ($0,06/maand voor 100K gesprekken): 69x prijsverschil [1]
- Selecteer altijd het goedkoopste model dat de kwaliteitsdrempel haalt [2]

**Hefboom 2: Prompt caching (50–90% besparing op input, 1–3 dagen)**
- Anthropic, OpenAI en Google ondersteunen prompt caching in hun API
- Vereiste: stabiele, herhalende prefix (system prompt, documentatie, codebase, gebruikersgeschiedenis)
- Audit-vraag: "Welk percentage van mijn input-tokens is identiek over verschillende aanroepen?" Als >20%: caching levert significante besparing [2]
- Gemini 2.5 Pro: cached input van $1,25 naar $0,31/MTok (75% korting)
- GPT-5.4: cached input van $2,50 naar $1,25/MTok (50% korting)
- Anthropic Sonnet 4.6: cached input $0,30/MTok vs $3,00/MTok (90% korting)
- Let op: lokale modellen (Ollama, vLLM) hebben geen ingebouwde API-caching — eigen implementatie vereist [3]

**Hefboom 3: Batch-API (50% besparing op batch-workloads, 1–2 weken)**
- OpenAI Batch API: 50% korting voor niet-realtime verzoeken
- Geschikt voor: nachtelijke verwerking, content-labeling, bulk-samenvatting, data-verrijking
- Vereiste: workload is niet tijdgevoelig; retries en idempotency vereist [4]

**Hefboom 4: Prompt-lengte trimmen (20–40% input-besparing)**
- Systematische prompt-compressie (redundante tokens verwijderen) 20–40% zonder kwaliteitsverlies [5]
- Elke token die je verwijdert is proportionele kostenverlaging

**Hefboom 5: Open-source migratie (50–90% bij schaal, 4–12 weken)**
- Migratie naar zelf-gehoste open-weight modellen (Llama 4, Mistral) bij hoge volumina
- Break-even afhankelijk van volume en hardware-kosten

### Kwantisatie (self-hosted inference)

| Techniek | Geheugenreductie | Snelheidsverbetering | Kwaliteitsverlies |
|----------|-----------------|---------------------|------------------|
| INT8-kwantisatie | 50% | 1,5–2x | <1% |
| INT4-kwantisatie (AWQ) | 75% | 2–3x | 1–3% |
| Kennisd distillatie | 40–60% | 2–3x | 2–5% |
| KV-cache kwantisatie | 30–50% (cache) | 1,3–1,8x | <1% |

Bronnen: [5, 6, 7] `verified`

**Kritische noot kwantisatie**: INT8 vermindert geheugen 4x maar versnelt inference alleen bij frameworks die INT8 native uitvoeren (TensorRT, ONNX Runtime, llama.cpp). Standaard PyTorch draait INT8 weights als FP32 — dat is puur verlies [3].

### Distillatie

Distillatie vervangt een 70B model door een gedistilleerd 7B model:
- Kostenreductie: 90% bij inferentie
- Kwaliteitsbehoud: 90–95% voor de specifieke taak
- Vereiste: goed gedefinieerde taak, duizenden kwaliteitsoutputs als trainingsdata, ML-infrastructuur [6]
- DistilBERT: 40% kleiner dan BERT, 97% van de prestaties behouden

### Speculative decoding

- Latencyverbetering 2–3x zonder kwaliteitsverlies
- Werkt door kleinere "draft" model te gebruiken om tokens te raden die het grote model vervolgens controleert
- Hoge implementatie-complexiteit — geschikt na andere optimalisaties zijn uitgeput

### Operationele runtime — latency-budgetten

Latency-budgetten bepalen gebruikerservaring [8, 9]:
- **>30 tokens/seconde streaming**: voelt instant voor de gebruiker
- **Sub-200 ms (TTFT)**: target voor interactieve toepassingen
- **P95 <10 seconden**: alert-drempel voor asynchrone LLM-calls
- Cascade-architecturen betalen latency-taks bij escalatie: drie-tier cascade = drie model-aanroepen voor het hoogste tier

### Schaalbaarheid en doorvoer

- **Continuous batching** (vLLM-standaard): verwerkt variabele lengtes samen; 2–5x throughput-verbetering bij gelijke hardware [6]
- **Adaptive batching**: eerste gebruiker wacht 100 ms op batch-fill; scheid batch-pad van realtime-pad
- **Model-versie-pinning vs auto-upgrade**:
  - Pinning: voorspelbaar gedrag, eenvoudiger compliance; risico: je mist beveiligingspatches en verbeteringen
  - Auto-upgrade: altijd recente kwaliteit; risico: stille gedragswijziging breekt downstream-logica
  - Aanbeveling: pin op major versie in productie; test upgrades in staging met eval-suite [8]

### Fallback-patronen

Bij model-uitval, rate-limiting of degradatie [10]:
- Primaire provider → fallback provider (bijv. Anthropic → OpenAI)
- Stap-down naar kleiner model in dezelfde provider-familie (Opus → Sonnet)
- Circuit breaker: stop escalatie naar dure fallback als foutpercentage te hoog
- Rate limit tracking: monitor `llm_rate_limit_hits_total` per model en provider

### Observability — vijf pijlers

Traditionele APM (latency, error-rate, throughput) is noodzakelijk maar onvoldoende: een HTTP 200 kan een hallucinatoire respons bevatten [9, 10]:

**Pijler 1: Request-logging**
- Elk API-call: model, input/output tokens, latency, HTTP-status, kosten, project-attribuut

**Pijler 2: Kostendashboard**
- Kosten per model, feature, gebruiker; uurlijkse/dagelijkse besteding; geprojecteerde maandkosten
- Pareto-analyse: vaak verbruikt 20% van gebruikers 80% van tokens

**Pijler 3: Prestatiemonitoring**
- Time to first token (TTFT), totale generatietijd, retrieval-latency
- P50/P95/P99 latency per model en pipeline-stap

**Pijler 4: Kwaliteitsmonitoring**
- LLM-as-judge op steekproef van productieverkeer (5–15%)
- Faithfulness-score, relevantiescores, guardrail-trigger-rate, refusal-rate
- Kwaliteitsdrift: 7-daagse trend antwoordlengte, 30-daagse refusal-trend

**Pijler 5: Budgetbewaking en alertering**
- Alert bij dagbudget-overschrijding (directe alert)
- Alert bij error-rate >1–5% (Slack / on-call)
- Alert bij latency P95 >10 seconden (Slack)
- Alert bij kwaliteitsscore onder drempel (Slack)
- Kostenspike detectie: kan prompt-injection-aanval of runaway agent-loop signaleren

### Vier correlaties die 80% van LLM-incidenten dekken [10]

| Patroon | Oorzaak |
|---------|---------|
| Latency stijgt + grounding-score daalt | Retrieval-degradatie |
| Latency stabiel + hallucinatie stijgt | Prompt- of modelwijziging |
| Escalatierate stijgt + kosten stijgen | Classifier drift |
| Provider-foutrate stijgt + fallback-rate stijgt | Upstream incident |

### OWASP LLM Top-10 (2025) — model-laag specifiek

**LLM03:2025 — Supply Chain** [11, 12]:
- LLM supply chains omvatten: foundation models, hosted APIs, fine-tuned modellen, RAG-databronnen, MCP-tools
- Kwetsbaarheden: manipuleerde pre-trained modellen (backdoors, biases), kwetsbare bibliotheken, vergiftigde datasets, ontbrekende provenance
- Mitigaties: checksums/hashes voor model-integriteit, gedetailleerde logging van datasets en trainingswijzigingen, vendor acceptance testing, ModelAudit voor statische model-scan

**LLM04:2025 — Data and Model Poisoning** [11, 12]:
- Pre-training, fine-tuning of embedding-data gemanipuleerd → backdoors, biases, kwetsbaarheden
- Bijzonder risico open-source: `pickle.loads()` met kwaadaardige code mogelijk
- Backdoors kunnen slapende agent-gedrag creëren (trigger-afhankelijk)
- Mitigaties: bias-detectie, consistentietests, red-teaming

**LLM07:2025 — System Prompt Leakage**:
- Confidentiële system-prompt kan via aanvallen of model-gedrag lekken
- Mitigatie: behandel system-prompt als niet-secret; beperk wat erin staat

### Model-cards en AI Bill of Materials

- **Model-cards**: beschrijven prestaties, beperkingen, trainingsdata, intended use — governance-instrument voor interne audittrails
- **AI-BOM (Bill of Materials)**: vergelijkbaar met software-BOM maar voor model-componenten — verplicht onder EU AI Act artikel 13 voor hoog-risico systemen `inferred`
- Trainingsdata-transparantie: Meta (Llama 4) en Mistral zijn relatief open; OpenAI/Anthropic/Google zijn geslotener over exacte trainingsdata-samenstelling

## Evidence Table

| # | Bron | URL | Type | Key claim | Confidence |
|---|------|-----|------|-----------|------------|
| 1 | AI Security Gateway — LLM Cost Comparison 2026 | https://aisecuritygateway.ai/blog/llm-cost-comparison-2026 | secondary | Llama 4 Scout $6,50/maand vs Claude Sonnet $450/maand bij 100K gesprekken | medium |
| 2 | LLMversus — LLM Cost Optimization Playbook 2026 | https://llmversus.com/blog/llm-cost-optimization-guide | secondary | 5 hefbomen, volgorde en besparingspercentages | high |
| 3 | TheNeuralBase — Inference Optimization Cheat Sheet | https://theneuralbase.com/cheatsheet/inference-optimization/ | secondary | Kwantisatie vereist native INT8-support in framework | medium |
| 4 | FastTool — Prompt Caching & Batch API 2026 | https://fasttool.app/blog/prompt-caching-batch-api-cost-reduction-2026 | secondary | Batch API: 50% korting; caching vereist stabiele prefix | high |
| 5 | AISuperior — LLM Cost Optimization 2026 | https://aisuperior.com/llm-cost-optimization-in-ai-deployment/ | secondary | Kwantisatietabel: INT8 50% geheugen, INT4 75%, distillatie 40–60% | high |
| 6 | MyEngineeringPath — LLM Inference Optimization | https://myengineeringpath.dev/genai-engineer/inference-optimization/ | secondary | Distillatie 90% kostenreductie bij 7B vs 70B; continuous batching | high |
| 7 | Seenos.ai — LLM Inference Optimization | https://seenos.ai/llm-optimization/llm-inference-optimization | secondary | Kwantisatietabel, speculative decoding, distillatie | medium |
| 8 | Anthropic — Trustworthy Agents in Practice | https://www.anthropic.com/research/trustworthy-agents | primary | Versiepinning, fallback-patronen, betrouwbare agents | high |
| 9 | Adaline — Complete Guide LLM Observability 2026 | https://www.adaline.ai/blog/complete-guide-llm-observability-monitoring-2026 | secondary | 5 pijlers observability; kwaliteitsmonitoring gap | high |
| 10 | Coverge — LLM Observability Guide | https://coverge.ai/blog/llm-observability-guide | secondary | Metriekentabel per categorie; 4 incident-correlaties | high |
| 11 | OWASP GenAI — LLM03:2025 Supply Chain | https://genai.owasp.org/llmrisk/llm03/ | primary | Supply chain kwetsbaarheden definitie en mitigaties | high |
| 12 | OWASP GenAI — LLM04:2025 Data and Model Poisoning | https://genai.owasp.org/llmrisk/llm04/ | primary | Trainingsdata-vergiftiging en backdoor-risico's | high |

## Coverage Status

- **Gecheckt direct:** OWASP-pagina's direct gelezen; kostenpercentages gekruist via meerdere bronnen
- **Blijft onzeker:** exacte besparingspercentages zijn sterk context-afhankelijk; meeste claims zijn zelfgerapporteerd
- **Niet afgerond:** specifieke Anthropic/OpenAI prompt-caching API-documentatie niet direct opgehaald

## Sources

1. AI Security Gateway — LLM API Cost Comparison 2026 — https://aisecuritygateway.ai/blog/llm-cost-comparison-2026
2. LLMversus — LLM Cost Optimization: The Complete 2026 Playbook — https://llmversus.com/blog/llm-cost-optimization-guide
3. TheNeuralBase — Inference Optimization Cheat Sheet — https://theneuralbase.com/cheatsheet/inference-optimization/
4. FastTool — Prompt Caching & Batch API Cost Reduction 2026 — https://fasttool.app/blog/prompt-caching-batch-api-cost-reduction-2026
5. AISuperior — LLM Cost Optimization in AI Deployment 2026 — https://aisuperior.com/llm-cost-optimization-in-ai-deployment/
6. MyEngineeringPath — LLM Inference Optimization 2026 — https://myengineeringpath.dev/genai-engineer/inference-optimization/
7. Seenos.ai — LLM Inference Optimization: Cut Latency 50% & Cost 60% — https://seenos.ai/llm-optimization/llm-inference-optimization
8. Anthropic — Trustworthy Agents in Practice — https://www.anthropic.com/research/trustworthy-agents
9. Adaline — Complete Guide to LLM Observability & Monitoring 2026 — https://www.adaline.ai/blog/complete-guide-llm-observability-monitoring-2026
10. Coverge — LLM Observability Guide — https://coverge.ai/blog/llm-observability-guide
11. OWASP GenAI — LLM03:2025 Supply Chain — https://genai.owasp.org/llmrisk/llm03/
12. OWASP GenAI — LLM04:2025 Data and Model Poisoning — https://genai.owasp.org/llmrisk/llm04/
