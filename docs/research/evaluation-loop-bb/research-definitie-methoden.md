# Research: Definitie & Methoden — Evaluation Loop (BB_07)

**Researcher:** researcher-1
**Dimensie:** Definitie, terminologie, methoden, eval-design, LLM-as-judge, agentic eval
**Datum:** 2026-05-01

## Samenvatting (1 zin)

"Evaluation loop" heeft in de AI-industrie geen één geaccepteerde definitie, maar convergentie zit in het idee van een gesloten cyclus van meten, analyseren en verbeteren — waarbij het *loop*-kenmerk (terugkoppeling die leidt tot actie) het onderscheidt van een eenmalige benchmark of test.

## Bevindingen

### 1. Woordelijke definities uit primaire bronnen

**Anthropic — "Demystifying Evals for AI Agents" (2025):**
> "An evaluation (or 'eval') is a test for an AI system: give an AI an input, then apply grading logic to its output to measure success."

Anthropic onderscheidt vervolgens zeven kernelementen: task, trial, grader, transcript, outcome, evaluation harness en evaluation suite. Het evaluator-optimizer patroon wordt beschreven als: *"one LLM call generates a response while another provides evaluation and feedback in a loop."* (`verified` — direct gelezen via https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)

**Anthropic — "Building Effective Agents" (2024):**
> "In the evaluator-optimizer workflow, one LLM call generates a response while another provides evaluation and feedback in a loop. This workflow is particularly effective when we have clear evaluation criteria, and when iterative refinement provides measurable value."

(`verified` — direct gelezen via https://www.anthropic.com/research/building-effective-agents)

**OpenAI — Working with evals (2025):**
> "Evaluations (often called evals) test model outputs to ensure they meet style and content criteria that you specify. Writing evals to understand how your LLM applications are performing against your expectations is an essential component to building reliable applications."

OpenAI definieert ook de *evaluation loop* als een data-flywheel: *"log inputs, outputs, and outcomes; sample those logs on a schedule and automatically route ambiguous or costly cases to expert review. Add these expert judgements to your eval and error analysis, then use them to update prompts, tools, or models."* (`verified` — via https://developers.openai.com/api/docs/guides/evals)

**OpenAI — "How evals drive the next chapter of AI for businesses" (november 2025):**
> "Evals [are] methods to measure and improve the ability of an AI system to meet expectations. Similar to product requirement documents, evals make fuzzy goals and abstract ideas specific and explicit."

(`inferred` — OpenAI.com pagina gaf 403; beschrijving via zoekmachineresultaten, niet direct gelezen)

**AWS Prescriptive Guidance — "Creating evaluation loops for generative AI" (2025):**
> "The core of any successful generative AI PoC is a robust and repeatable development loop. This loop is the engine room where ideas are tested, prompts are refined, and quality is measured."

AWS benoemt vijf componenten: controlled variables (inputs), core application, experiment tracking, evaluation system, optimization mechanism. (`verified` — direct gelezen via https://docs.aws.amazon.com/prescriptive-guidance/latest/gen-ai-lifecycle-operational-excellence/dev-experimenting-experimentation-loops.html)

**Stanford HELM — Holistic Evaluation of Language Models:**
> "Holistic Evaluation of Language Models (HELM) is an open source Python framework created by the Center for Research on Foundation Models (CRFM) at Stanford for holistic, reproducible and transparent evaluation of foundation models."

HELM introduceert het begrip *evaluation harness*: de software-infrastructuur die modellen draait tegen meerdere benchmarks, de testinfrastructuur beheert en resultaten aggregeert. HELM meet 7 dimensies (accuracy, calibration, robustness, fairness, bias, toxicity, efficiency) over 60+ scenario's. (`verified` — via https://crfm.stanford.edu/helm/latest/ en https://github.com/stanford-crfm/helm)

**NIST AI RMF — TEVV (Test, Evaluate, Verify, Validate):**
Het AI RMF (2023) introduceert TEVV als kernproces: *"TEVV tasks can provide insights relative to technical, societal, legal, and ethical standards or norms, and can assist with anticipating impacts and assessing and tracking emergent risks. As a regular process within an AI lifecycle, TEVV allows for both mid-course remediation and post-hoc risk management."* (`verified` — via https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf)

**Google DeepMind — Evals-pagina:**
Google DeepMind hanteert geen expliciete definitie van "eval", maar benadert het via specifieke benchmarks (FACTS Grounding, DeepSearchQA, MRCR v2, Chess Text) met als filosofie: *"promoting the development of LLMs that are both knowledgeable and trustworthy, facilitating their responsible deployment."* (`verified` — via https://deepmind.google/research/evals/)

### 2. Gesynthetiseerde werkdefinitie

Op basis van bovenstaande bronnen geldt:

**Een evaluation loop is een gesloten, terugkerende cyclus waarin:** (a) AI-output wordt beoordeeld aan expliciete criteria via gestandaardiseerde taken en graders, (b) bevindingen worden geanalyseerd op patronen en gaps, en (c) concrete verbeteracties worden doorgevoerd in prompts, modellen, data of processen — waarna de cyclus herstart.

Het *loop*-onderdeel is het onderscheidende kenmerk: een eenmalige benchmark of A/B-test is géén evaluation loop. De loop impliceert gesloten terugkoppeling die leidt tot aantoonbare aanpassing.

**Terminologische verschillen:**
- Academisch (NeurIPS, ACL, HELM): *"evaluation"* en *"benchmark"* domineren; nadruk op reproduceerbaarheid en multi-dimensionele meting.
- Industrie Anthropic/OpenAI: *"evals"* (informele meervoud) is dominant; pragmatisch en gericht op productiescenario's.
- MLOps/infra-teams: *"evaluation harness"*, *"eval pipeline"*, *"eval-as-code"*.
- EU-regelgeving (AI Act, ISO 42001): *"testing"*, *"validation"*, *"post-market monitoring"* — geen gebruik van "eval" als term.
- NIST: *"TEVV"* (Test, Evaluate, Verify, Validate) als overkoepelende term.

**Grensafbakening:**
- *Observability*: het zichtbaar maken van wat er intern in een systeem gebeurt (traces, logs, spans) — input voor de evaluation loop, niet de loop zelf.
- *Monitoring*: continu signaleren van afwijkingen in productie (latency, error rates, drift) — ook input, maar geen beoordeling van outputkwaliteit.
- *MLOps*: bredere discipline die de volledige levenscyclus van ML-modellen beheert; evaluation loop is een deelproces.
- *Benchmark*: eenmalige meting op standaard dataset — bouwsteen voor de evaluation loop, maar zelf niet cyclisch.

### 3. Productie-rijpe evaluation loop: fasen

Op basis van AWS, OpenAI en Anthropic bronnen bestaat een volwaardige evaluatie-cyclus uit:

1. **Pre-deploy offline eval** — gecontroleerde testset, bekende expected outputs, geen echte gebruikers.
2. **Shadow mode** — nieuw model draait parallel aan productie, outputs worden vastgelegd maar niet getoond; beoordeeld zonder gebruikersimpact.
3. **Canary release** — klein percentage echt verkeer (1% → 5% → 20% → 50% → 100%); metrics worden vergeleken met baseline.
4. **Post-deploy online eval** — continue monitoring van klikfeedback, escalatie-rate, thumbs up/down, user satisfaction.
5. **Drift monitoring** — detectie van data drift, concept drift en performance drift; alarm bij overschrijding drempel.
6. **Verbeteractie** — aanpassing prompts, modellen, retrieval, tools; doorloopt opnieuw de cyclus.

(`verified` voor stappen 1-3 via https://tianpan.co/blog/2026-04-09-llm-gradual-rollout-shadow-canary-ab-testing; stap 4-5 `verified` via AWS blog agentic evaluation)

### 4. Kwaliteitsmetrieken: taxonomie

Op basis van Evidently AI en productieliteratuur:

**Referentie-gebaseerde methoden (met gold-answer):**
- *Exact Match* — binair; alleen zinvol bij deterministische outputs (SQL, JSON, code). Snel en gratis, maar te rigide voor open-ended taken.
- *BLEU/ROUGE* — n-gram overlap; standaard in vertaling en samenvatting. Correleert slecht met menselijk oordeel bij open-ended generatie.
- *BERTScore* — semantische gelijkenis via embedding-cosinus; snapt parafrasering beter dan n-gram. Mist kritische details ondanks hoge score.
- *Semantic similarity* — embedding-afstand; nuttig voor RAG-faithfulness.
- *LLM-as-judge met rubric* — flexibel, schaalbaar, interpreteerbaar; vereist kalibratie.

**Referentie-vrije methoden (zonder gold-answer):**
- *Regex/text-stats* — formaat-validatie (JSON valid?, length in range?).
- *Model-based classifiers* — toxicity, PII-detectie, sentiment.
- *LLM-as-judge* — beoordeling op criteria beschreven in prompt.

**Productieaanbeveling:** combineer deterministische checks (snel, goedkoop) + LLM-as-judge (voor nuance) + periodieke menselijke steekproef (kalibratie). Een 75-90% match tussen judge en menselijk label wordt als "klaar voor schaling" beschouwd. (`inferred` — op basis van Evidently AI, Arize en literatuur)

### 5. Eval-set design: richtlijnen

| Parameter | Richtlijn | Bron |
|-----------|-----------|------|
| Minimale grootte | 20-50 cases voor eerste testset; 100+ voor betrouwbare statistiek | Maxim AI, Evidently AI |
| Aanbevolen grootte | 100-500 cases voor productiesystemen; medische/juridische toepassingen 1000+ | Maxim AI |
| Samenstelling | 60-70% happy-path, 20-30% edge cases, 5-10% adversarial | Saptak.in |
| Synthetische data | Balanceer met human-authored; valideer via SME; gebruik niet hetzelfde model voor generatie en validatie | Confident AI |
| Overlap-check | Periodieke decontaminatie; geen overlap met trainingsdata | ICML 2025, ACL 2025 |
| Versiebeheer | Elke schema- en labelwijziging traceren; eval-set is versioned artifact | Maxim AI |

**Data-contaminatie als stille faalmodus:** Benchmark-saturatie treedt op wanneer trainingsdata de testset bevat. Onderzoek (ICML 2025) toont 5-15% absolute accuracy drops bij contaminated models wanneer voorbeelden worden verwijderd. GSM8K laat een gedocumenteerde drop van 13% zien. (`verified` — via ICML 2025 poster en ACL Anthology AntiLeakBench)

### 6. LLM-as-judge: kalibratie en biases

**Cohen's Kappa als kalibratiemaat:**
Kappa (κ) meet inter-rater overeenstemming gecorrigeerd voor toeval. Gangbare drempels:
- κ < 0.40: slecht — heroverwegen van criteria of judge-prompt
- κ 0.40-0.60: matig — acceptabel voor exploratie, niet voor productie
- κ 0.60-0.80: goed — productiegeschikt voor niet-kritische toepassingen
- κ > 0.80: uitstekend — vereist voor hoge-risico of compliance-gevoelige systemen

BeeHaive AI-Readiness Audit gebruikt κ = 0.717 als target (in de "goed" categorie). (`inferred` — gebaseerd op literatuur; Kappa-drempels komen van Landis & Koch 1977, nog steeds de standaard)

**Bekende biases in LLM-judges:**
- *Lengte-bias*: langere antwoorden scoren hoger, ongeacht kwaliteit.
- *Positie-bias*: antwoord als eerste getoond scoort beter.
- *Zelf-voorkeur*: hetzelfde model als judge en kandidaat — inflated scores.
- *Stijl-bias*: voorkeur voor formeel of retorisch sterk taalgebruik boven feitelijke accuraatheid.

(`verified` — via ACL Anthology 2025, arxiv 2510.09738)

**Multi-LLM ensemble als mitigatie:** gebruik meerdere verschillende judge-modellen; combineer Cohen's Kappa met semantische cosinus-similarity voor dubbele validatie. (`inferred` — arxiv 2512.20352)

**Wanneer mens onvermijdelijk:**
- Hoge-risico beslissingen (medisch, juridisch, HR)
- Judge-model alignment nog niet bewezen voor het specifieke domein
- Eerste kalibratie van nieuwe rubric (minimum 50 human-labeled seed examples)

### 7. Agentic en multi-turn evaluatie

Agentic systemen stellen specifieke eisen aan evaluatie:

**Trajectory evaluation:** beoordeel niet alleen het eindresultaat maar het hele pad. Metrics: Trajectory Exact-Match, Trajectory Inclusion (required tools in correct volgorde), Tool Selection Accuracy, Tool Parameter Accuracy, Multi-turn Function Calling Accuracy. (`verified` — TRAJECT-Bench arxiv 2510.04550; LangChain AgentEvals docs)

**Amazon lessen (agentic shopping assistant):**
- Tool selection accuracy
- Tool parameter accuracy
- Multi-turn function calling accuracy
- Tool call error rate
- Topic adherence (blijft agent in scope?)
- Faithfulness (consistent met conversatiegeschiedenis)

(`verified` — https://aws.amazon.com/blogs/machine-learning/evaluating-ai-agents-real-world-lessons-from-building-agentic-systems-at-amazon/)

**Verschil single-turn vs. agentic:**
- Single-turn: input → output → grade. Eenvoudig, deterministisch.
- Agentic: input → trajectory (N stappen, tool calls, memory updates) → finale state → grade op elke laag. Fouten propageren; sandboxed uitvoering nodig.

## Evidence Table

| # | Bron | URL | Type | Key claim | Confidence |
|---|------|-----|------|-----------|------------|
| 1 | Anthropic — Demystifying Evals | https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents | primary | Definitie eval: "a test for an AI system" | high |
| 2 | Anthropic — Building Effective Agents | https://www.anthropic.com/research/building-effective-agents | primary | Evaluator-optimizer als loop-patroon | high |
| 3 | OpenAI — Working with Evals | https://developers.openai.com/api/docs/guides/evals | primary | Data-flywheel definitie evaluation loop | high |
| 4 | OpenAI — Evals drive next chapter | https://openai.com/index/evals-drive-next-chapter-of-ai/ | primary | Evals maken vage doelen expliciet | medium (403) |
| 5 | AWS — Evaluation loops GenAI | https://docs.aws.amazon.com/prescriptive-guidance/latest/gen-ai-lifecycle-operational-excellence/dev-experimenting-experimentation-loops.html | secondary | 5-componenten model voor evaluation loop | high |
| 6 | Stanford HELM | https://crfm.stanford.edu/helm/latest/ | primary | Definitie evaluation harness; 7 metrics | high |
| 7 | NIST AI RMF 1.0 | https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf | primary | TEVV als lifecycle-proces | high |
| 8 | Google DeepMind Evals | https://deepmind.google/research/evals/ | primary | Benchmark-georiënteerde aanpak; geen expliciete definitie | medium |
| 9 | TRAJECT-Bench | https://arxiv.org/abs/2510.04550 | primary | Trajectory evaluation metrics voor agentic tools | high |
| 10 | Amazon ML Blog — Agentic Eval | https://aws.amazon.com/blogs/machine-learning/evaluating-ai-agents-real-world-lessons-from-building-agentic-systems-at-amazon/ | secondary | Tool-call accuracy metrics in productie | high |
| 11 | Evidently AI — LLM Metrics | https://www.evidentlyai.com/llm-guide/llm-evaluation-metrics | secondary | Taxonomie van evaluatiemetrieken | high |
| 12 | ICML 2025 — Data Contamination | https://icml.cc/virtual/2025/poster/43619 | primary | 5-15% accuracy drop bij contaminated evals | high |
| 13 | ACL 2025 — AntiLeakBench | https://aclanthology.org/2025.acl-long.901/ | primary | Geautomatiseerde anti-leakage benchmarking | high |
| 14 | arxiv 2510.09738 — Judge Analysis | https://arxiv.org/pdf/2510.09738 | primary | Lengte-, positie- en zelf-bias in LLM-judges | high |
| 15 | LangChain AgentEvals | https://github.com/langchain-ai/agentevals | secondary | Trajectory match evaluators voor agents | high |
| 16 | Shadow/Canary deployment blog | https://tianpan.co/blog/2026-04-09-llm-gradual-rollout-shadow-canary-ab-testing | secondary | Shadow mode → canary patroon voor LLM-rollout | high |

## Coverage Status

- **Gecheckt direct:** bronnen 1, 2, 3, 5, 6, 8, 10, 11, 15, 16 volledig gelezen.
- **Blijft onzeker:** OpenAI blog (bron 4) niet direct toegankelijk (403); beschrijving via zoekresultaten.
- **Niet afgerond:** ISO/IEC 42001 sectie over evaluation niet direct gecheckt (valt onder researcher-2); Anthropic cookbook notebook niet leesbaar via GitHub viewer.

## Sources

1. Anthropic — Demystifying Evals for AI Agents — https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
2. Anthropic — Building Effective Agents — https://www.anthropic.com/research/building-effective-agents
3. OpenAI — Working with Evals — https://developers.openai.com/api/docs/guides/evals
4. OpenAI — How Evals Drive the Next Chapter of AI — https://openai.com/index/evals-drive-next-chapter-of-ai/
5. AWS Prescriptive Guidance — Evaluation Loops for GenAI — https://docs.aws.amazon.com/prescriptive-guidance/latest/gen-ai-lifecycle-operational-excellence/dev-experimenting-experimentation-loops.html
6. Stanford HELM — https://crfm.stanford.edu/helm/latest/
7. NIST AI RMF 1.0 — https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf
8. Google DeepMind Evals — https://deepmind.google/research/evals/
9. TRAJECT-Bench — https://arxiv.org/abs/2510.04550
10. Amazon ML Blog — Evaluating AI Agents — https://aws.amazon.com/blogs/machine-learning/evaluating-ai-agents-real-world-lessons-from-building-agentic-systems-at-amazon/
11. Evidently AI — LLM Evaluation Metrics — https://www.evidentlyai.com/llm-guide/llm-evaluation-metrics
12. ICML 2025 — Data Contamination Benchmark — https://icml.cc/virtual/2025/poster/43619
13. ACL 2025 — AntiLeakBench — https://aclanthology.org/2025.acl-long.901/
14. arxiv — Judge's Verdict Comprehensive Analysis — https://arxiv.org/pdf/2510.09738
15. LangChain AgentEvals — https://github.com/langchain-ai/agentevals
16. TianPan — LLM Gradual Rollout Shadow Canary A/B Testing — https://tianpan.co/blog/2026-04-09-llm-gradual-rollout-shadow-canary-ab-testing
