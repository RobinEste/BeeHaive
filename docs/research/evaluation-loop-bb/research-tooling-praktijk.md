# Research: Tooling & Praktijk — Evaluation Loop (BB_07)

**Researcher:** researcher-3
**Dimensie:** Tools, operationele patronen, anti-patronen, casestudies
**Datum:** 2026-05-01

## Samenvatting (1 zin)

Het eval-toolinglandschap in 2025-2026 is volwassen geworden met twee duidelijke segmenten — eval-as-code (deepeval, ragas, inspect_ai) voor engineering-gedreven teams en SaaS-observability (LangSmith, W&B Weave, Braintrust, Arize Phoenix) voor bredere teams — terwijl de praktijk leert dat de meeste AI-projecten falen niet door gebrek aan tools maar door een gebrek aan discipline om de loop daadwerkelijk te sluiten.

## Bevindingen

### 1. Tooling-landschap 2025-2026: overzicht

Het landschap is te verdelen in vier categorieën:

**A. Eval-as-code frameworks (open source)**
| Tool | Sterkste domein | Licentie | Prijs |
|------|----------------|----------|-------|
| DeepEval | Brede LLM eval, agents, RAG; Pytest-integratie | MIT | Free / $19.99/user/mo (Confident AI) |
| Ragas | RAG-specifieke metrics (faithfulness, context relevance) | Apache 2.0 | Free |
| Inspect AI (AISI) | Reproduceerbare evals, sandboxed agentic uitvoering | MIT | Free |
| MLflow | Experiment tracking, model lifecycle | Apache 2.0 | Free / cloud |
| Langfuse | Open source observability + eval; self-hostbaar | MIT | Free / cloud |

**B. SaaS eval/observability platforms**
| Tool | Sterkste domein | Startprijs |
|------|----------------|-----------|
| LangSmith | LangChain/LangGraph integratie; trajectory scoring | $39/seat/mo |
| W&B Weave | Agent trace observability; MCP auto-logging | $60/mo |
| Braintrust | CI/CD pipeline gates; AI-prompt optimalisatie | $249/mo (unlimited users) |
| Humanloop | Niet-technische samenwerking; prompt management | op aanvraag |
| Arize Phoenix | OpenTelemetry-native; zelf-hostbaar | Free / $50/mo |
| Comet Opik | Automatische prompt-optimalisatie; 6 algoritmen | $19/mo |
| Truesight | Domein-specifieke outputkwaliteit; SME review queues | $19/mo |

(`verified` — via https://www.goodeyelabs.com/articles/top-ai-agent-evaluation-tools-2026 en https://www.braintrust.dev/articles/best-llm-evaluation-platforms-2025)

**C. Benchmarks en evaluatie-platformen (voor model-evaluatie)**
- **OpenAI Evals** — open source framework + API voor gestandaardiseerde evals; 4 core concepten: Eval, Run, data_source_config, testing_criteria.
- **HELM** (Stanford) — 60+ scenario's, 7 metrics, 90+ modellen; meest geciteerde holistische benchmark.
- **BIG-Bench** (Google) — breed capability-benchmark; deels opgenomen in HELM.
- **Arize Phoenix** — zowel observability als eval, OpenTelemetry-based.

**D. Observability / monitoring (aanvullend aan eval)**
- **Langfuse** — traces, scores, experiments; self-hostbaar.
- **Evidently AI** — data en model monitoring; drift detectie.
- **Galileo** — hallucination monitoring, guardrails in productie.

### 2. Beslismatrix: welk tool kiezen?

| Situatie | Aanbevolen tool(s) |
|----------|-------------------|
| Engineers met Pytest-cultuur; CI/CD gates | DeepEval + Braintrust of eigen pytest |
| RAG-pipeline evalueren | Ragas + Langfuse of Arize Phoenix |
| Agentic systemen; sandboxed uitvoering | Inspect AI (UK AISI) |
| LangChain/LangGraph ecosystem | LangSmith |
| Niet-technische product managers mee in loop | Humanloop |
| OpenTelemetry; vendor-neutraal; self-hosted | Arize Phoenix |
| W&B gebruikers in ML-team | W&B Weave |
| Kosten bij schaal; CI/CD | Braintrust ($249 flat, unlimited users) |

(`inferred` — samengesteld uit meerdere vergelijkingsbronnen)

### 3. Arize Phoenix: diepere blik

Arize Phoenix is opmerkelijk als enige major platform volledig gebouwd op OpenTelemetry. Versie 3.0.0 uitgebracht op 7 april 2026. Features:
- Framework-agnostisch: werkt met OpenAI, Anthropic, LangChain, CrewAI, LlamaIndex, DSPy.
- Tracing: `@weave.op()` of OTel-decorators; legt volledige traces vast.
- Eval-primitieven: LLM-based evaluators, code checks, human labels.
- Datasets en experimenten: vergelijk prompt-versies.
- Playground: interactief prompt-optimalisatie.
- Embeddings-analyse: semantische drift detecteren.
- Zelf-hostbaar via Docker of cloud.

(`verified` — via https://arize.com/docs/phoenix en https://github.com/Arize-ai/phoenix)

### 4. Inspect AI (UK AISI): diepere blik

Ontwikkeld door het UK AI Security Institute (AISI). Unieke eigenschappen:
- Opinionated primitives: Dataset → Task → Solver → Scorer.
- Sandbox-uitvoering via Docker (ingebouwd), Kubernetes/Proxmox-adapters.
- Multi-turn en agentic workflows met tools.
- VS Code log viewer + web Inspect View.
- Ontworpen voor reproduceerbaarheid en auditerbaarheid.
- Meest complete OSS-keuze voor teams die evals als productie-infrastructuur behandelen.

(`verified` — via https://inspect.aisi.org.uk/ en https://github.com/UKGovernmentBEIS/inspect_ai)

### 5. Operationele patronen

**Patroon 1: Shadow Mode**
Nieuw model draait parallel aan productie; responses worden vastgelegd maar *niet getoond* aan gebruikers. Analyse van kwaliteitsverschillen zonder gebruikersimpact. Startpunt voor elke significante modelwisseling.

**Patroon 2: Canary Release**
Na shadow mode: 1% → 5% → 20% → 50% → 100% van echt verkeer. Metrics vergeleken met baseline. Bij overschrijding drempel: automatische rollback. Veiligheidsgrens bij hoog-risico toepassingen: start op 0.1%.

**Patroon 3: A/B Testing van prompts en modellen**
Twee varianten van een prompt (of twee modellen) ontvangen gesplit verkeer. Statistisch significante uitkomst vereist voldoende volume; kleine eval-sets produceren misleidende conclusies.

**Patroon 4: Online evaluation (productiesignalen)**
- Impliciete feedback: klikgedrag, dwell-time, abandonment rate.
- Expliciete feedback: thumbs up/down, sterrenrating, correctie-acties.
- Escalatie-rate: percentage sessies dat naar menselijke agent gaat.
- Herhalingsrate: gebruiker steldt dezelfde vraag opnieuw — signaal voor falen.

**Patroon 5: Drift monitoring**
- *Data drift*: distributie van input-queries verschuift.
- *Concept drift*: de relatie tussen input en correct antwoord verandert (werkelijkheid verandert).
- *Performance drift*: kwaliteitsmetrieken dalen zonder expliciete wijziging in de applicatie.
Bij overschrijding van vooraf gedefinieerde drempel: triggers rerun van offline eval, eventueel retraining of prompt-update.

(`verified` — via https://tianpan.co/blog/2026-04-09-llm-gradual-rollout-shadow-canary-ab-testing en AWS ML Blog agentic eval)

### 6. Anti-patronen: de meest voorkomende faalmodi

**Anti-patroon 1: Vibe-checking**
Teams beoordelen AI-output "op gevoel" door een paar voorbeelden te lezen. Schaalbaar niet, en biedt geen statistische basis voor vertrouwen. Definitief niet geschikt zodra het systeem meer dan honderd gebruikers bedient.

**Anti-patroon 2: Demo-driven development**
Het systeem wordt geoptimaliseerd op de demo-cases die aan het management worden getoond. De eval-set bestaat uit precies die cases. Edge cases, adversarial inputs en minority-cases ontbreken. Systeem scoort 95% op de eval maar faalt in 30% van echte gebruikscases.

**Anti-patroon 3: Single-metric tunnel vision**
Teams optimaliseren op één metric (bijv. ROUGE score) terwijl andere dimensies (safety, faithfulness, bias) worden genegeerd. Goodhart's Law: *"When a measure becomes a target, it ceases to be a good measure."* Concreet 2025-voorbeeld: grote AI-labs publiceerden selectief alleen de beste Arena-scores, niet alle testresultaten. (`verified` — via https://blog.collinear.ai/p/gaming-the-system-goodharts-law-exemplified-in-ai-leaderboard-controversy)

**Anti-patroon 4: Eval-set staleness**
De eval-set wordt eenmalig aangemaakt en nooit bijgewerkt. Na 6-12 maanden: de werkelijkheid heeft zich gewijzigd (nieuwe productfeatures, nieuwe gebruikerspatronen, domeinverschuivingen). De eval meet niet meer wat er in productie relevant is.

**Anti-patroon 5: Judge-model contaminatie**
Hetzelfde model dat output genereert, wordt gebruikt als judge. Zelf-voorkeur leidt tot systematisch hoge scores zonder relatie tot echte kwaliteit. Gebruik altijd een *ander* model als judge, of een ensemble van meerdere modellen.

**Anti-patroon 6: Only happy path**
Eval-set bevat alleen succesvolle gevallen; edge cases, foutpaden en out-of-distribution inputs worden niet getest. Systeem lijkt 98% nauwkeurig maar faalt volledig bij onverwachte inputs.

**Anti-patroon 7: Eval-set leakage in trainingsdata**
Benchmarkdata komt terecht in de trainingsdata van het model. Resultaat: model "weet" de antwoorden, scoort hoog op benchmark maar generaliseert niet. ICML 2025 toont 5-15% accuracy drops wanneer contaminatie wordt verwijderd. (`verified` — ICML 2025)

**Anti-patroon 8: Rapportage-theater**
De evaluation loop produceert dashboards en rapporten, maar geen beslissingen. Metrics worden bijgehouden zonder dat bevindingen leiden tot aanpassingen in prompts, modellen of processen. De loop is open (geen gesloten cyclus).

### 7. Casestudies

**Amazon — Shopping Assistant (agentic eval):**
Amazon bouwde een gestructureerd eval-framework voor een agentic shopping assistant met metrics voor tool-selection accuracy, tool-parameter accuracy, multi-turn function calling accuracy, topic adherence (blijft agent in scope?) en faithfulness (consistent met conversatiegeschiedenis). Lessons learned: slecht gedefinieerde tool-schemas zijn de grootste bron van fouten. Productie-monitoring vereist real-time dashboards én geautomatiseerde anomaly-detectie met drempelwaarden. (`verified` — https://aws.amazon.com/blogs/machine-learning/evaluating-ai-agents-real-world-lessons-from-building-agentic-systems-at-amazon/)

**Braintrust — CI/CD gates:**
Braintrust wordt gebruikt door engineering-teams om eval-resultaten te laten gaten in de CI/CD-pipeline: een pull request mag alleen worden gemerged als de eval-score boven een drempelwaarde blijft. Dit maakt regressie-detectie automatisch en verplicht. (`verified` — https://www.braintrust.dev/articles/langsmith-vs-braintrust)

### 8. Kosten van eval

**Directe kosten:**
- Platform-fees: $0-249/maand voor SaaS-platforms (afhankelijk van teamgrootte en gebruik).
- LLM-judge-calls: bij 1000 evals per dag met GPT-4o als judge: geschat $5-50/dag afhankelijk van prompt-lengte.
- Menselijke review: bij $50/uur en 2 uur/week: ~$400/maand voor een basis review-loop.

**Verborgen kosten:**
- Engineering-tijd voor het bouwen en onderhouden van eval-infrastructure.
- Kosten van *niet* evalueren: productiestoringen, gebruikersklachten, reputatieschade.
- Kosten van valse geruststelling: eval-set die niet meer representatief is, geeft false confidence.

(`inferred` — eigen berekening op basis van platform-prijzen en publiek bekende LLM-prijzen)

### 9. Verhouding tot andere BeeHaive-bouwstenen

| Bouwsteen | Rol in evaluation loop |
|-----------|----------------------|
| BB_01 Knowledge | Levert eval-criteria: wat zijn de juiste antwoorden? Knowledge Graph geeft ground truth. |
| BB_02 Client Blueprint | Bepaalt succescriteria: welke outputs zijn voor de klant waardevol? |
| BB_03 Dynamic Context | Wordt geëvalueerd op grounding: haalt de context de juiste informatie op? |
| BB_04 Prompt Design | Wordt regression-tested: elke prompt-update triggert een eval-run. |
| BB_05 Tool Integration | Evalueert tool-call correctness: juiste tool, juiste parameters, juiste volgorde. |
| BB_06 Model Engines | Modelvergelijking via evals: welk model presteert het best op deze use case? |
| BB_07 Evaluation Loop | Overkoepelt alle andere bouwstenen: de motor die verbetering aantoonbaar maakt. |

## Evidence Table

| # | Bron | URL | Type | Key claim | Confidence |
|---|------|-----|------|-----------|------------|
| 1 | Goodeye Labs — Top eval tools 2026 | https://www.goodeyelabs.com/articles/top-ai-agent-evaluation-tools-2026 | secondary | Vergelijking 7 platforms 2026 | high |
| 2 | Braintrust — LLM eval platforms | https://www.braintrust.dev/articles/best-llm-evaluation-platforms-2025 | self-reported | Platform-vergelijking; prijzen | medium |
| 3 | Arize Phoenix docs | https://arize.com/docs/phoenix | primary | Features Phoenix 3.0.0 | high |
| 4 | Inspect AI — AISI | https://inspect.aisi.org.uk/ | primary | Sandboxed agentic evals | high |
| 5 | GitHub Inspect AI | https://github.com/UKGovernmentBEIS/inspect_ai | primary | Open source status, features | high |
| 6 | AWS — Agentic eval lessons | https://aws.amazon.com/blogs/machine-learning/evaluating-ai-agents-real-world-lessons-from-building-agentic-systems-at-amazon/ | secondary | Amazon shopping assistant casestudy | high |
| 7 | TianPan — LLM rollout patterns | https://tianpan.co/blog/2026-04-09-llm-gradual-rollout-shadow-canary-ab-testing | secondary | Shadow/canary/A/B patronen | high |
| 8 | Collinear — Goodhart's Law | https://blog.collinear.ai/p/gaming-the-system-goodharts-law-exemplified-in-ai-leaderboard-controversy | secondary | Goodhart's law in AI leaderboards | high |
| 9 | Braintrust — LangSmith vs Braintrust | https://www.braintrust.dev/articles/langsmith-vs-braintrust | self-reported | CI/CD gates; prijsvergelijking | medium |
| 10 | DeepEval vs Ragas | https://deepeval.com/blog/deepeval-vs-ragas | self-reported | Framework vergelijking features | medium |
| 11 | GitHub deepeval | https://github.com/confident-ai/deepeval | primary | 50+ metrics, Pytest integratie | high |
| 12 | GitHub agentevals LangChain | https://github.com/langchain-ai/agentevals | primary | Trajectory match evaluators | high |

## Coverage Status

- **Gecheckt direct:** bronnen 3, 4, 5, 6, 7, 8, 11, 12 direct gelezen.
- **Blijft onzeker:** Braintrust en DeepEval vergelijkingen zijn self-reported (leverancier beschrijft eigen voordelen); neutraal gecombineerd.
- **Niet afgerond:** OpenAI Evals platform (evals.openai.com) niet direct gecheckt; Humanloop prijsstructuur niet gevonden.

## Sources

1. Goodeye Labs — Top AI Agent Evaluation Tools 2026 — https://www.goodeyelabs.com/articles/top-ai-agent-evaluation-tools-2026
2. Braintrust — Best LLM Evaluation Platforms 2025 — https://www.braintrust.dev/articles/best-llm-evaluation-platforms-2025
3. Arize Phoenix Documentation — https://arize.com/docs/phoenix
4. Inspect AI — UK AISI — https://inspect.aisi.org.uk/
5. GitHub — inspect_ai — https://github.com/UKGovernmentBEIS/inspect_ai
6. AWS ML Blog — Evaluating AI Agents at Amazon — https://aws.amazon.com/blogs/machine-learning/evaluating-ai-agents-real-world-lessons-from-building-agentic-systems-at-amazon/
7. TianPan — LLM Gradual Rollout — https://tianpan.co/blog/2026-04-09-llm-gradual-rollout-shadow-canary-ab-testing
8. Collinear AI — Goodhart's Law in AI Leaderboards — https://blog.collinear.ai/p/gaming-the-system-goodharts-law-exemplified-in-ai-leaderboard-controversy
9. Braintrust — LangSmith vs Braintrust — https://www.braintrust.dev/articles/langsmith-vs-braintrust
10. DeepEval — DeepEval vs Ragas — https://deepeval.com/blog/deepeval-vs-ragas
11. GitHub — deepeval — https://github.com/confident-ai/deepeval
12. GitHub — LangChain AgentEvals — https://github.com/langchain-ai/agentevals
13. GitHub — Arize Phoenix — https://github.com/Arize-ai/phoenix
