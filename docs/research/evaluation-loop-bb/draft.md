# Evaluation Loop (BB_07) — Draft onderzoeksrapport

**Onderwerp:** Evaluation Loop voor AI-systemen — definitie, methoden, governance, tooling en anti-patronen
**Datum:** 2026-05-01
**Researcher-rondes:** 1

---

## Executive Summary

De evaluation loop is de motor achter elke AI-oplossing die over tijd beter wordt. Toch is het de meest overgeslagen stap in AI-projecten: teams bouwen, deployen, en hopen. Zonder systematische evaluatie degradeert elk AI-systeem — niet dramatisch, maar stil.

In de AI-industrie convergeren Anthropic, OpenAI, AWS, Stanford en NIST op een gedeeld concept: een evaluation loop is een gesloten, terugkerende cyclus van meten, analyseren en verbeteren. Het *loop*-onderdeel is het onderscheidende kenmerk. Een eenmalige benchmark is geen loop. Een dashboard zonder actie is geen loop. De loop sluit pas wanneer bevindingen leiden tot aantoonbare veranderingen in prompts, modellen, data of processen.

Tegelijk is evaluatie een rijp, volwassen vakgebied geworden. Er zijn duidelijke primaire bronnen met werkdefinities, een toolinglandschap van meer dan een dozijn platformen, en een wettelijk kader (EU AI Act Art. 9, 10, 15, 17, 72; ISO/IEC 42001; NIST AI RMF) dat de loop voor hoog-risico AI-systemen verplicht stelt. Wat ontbreekt in de meeste praktijkimplementaties is niet kennis, maar discipline: de wil om de loop daadwerkelijk te sluiten.

---

## 1. Definitie: wat is een evaluation loop?

### 1.1 Woordelijke definities uit primaire bronnen

**Anthropic (2025):**
> "An evaluation (or 'eval') is a test for an AI system: give an AI an input, then apply grading logic to its output to measure success." [1]

Het evaluator-optimizer patroon wordt beschreven als: *"one LLM call generates a response while another provides evaluation and feedback in a loop. This workflow is particularly effective when we have clear evaluation criteria, and when iterative refinement provides measurable value."* [2]

**OpenAI (2025):**
> "Evaluations (often called evals) test model outputs to ensure they meet style and content criteria that you specify. Writing evals to understand how your LLM applications are performing against your expectations is an essential component to building reliable applications." [3]

OpenAI beschrijft de evaluation loop als een data-flywheel: *"log inputs, outputs, and outcomes; sample those logs on a schedule and automatically route ambiguous or costly cases to expert review. Add these expert judgements to your eval and error analysis, then use them to update prompts, tools, or models."* [3]

**OpenAI — Evals for businesses (november 2025):**
> "Evals [are] methods to measure and improve the ability of an AI system to meet expectations. Similar to product requirement documents, evals make fuzzy goals and abstract ideas specific and explicit." [4] (`inferred` — bron gaf 403; via zoekresultaten)

**AWS Prescriptive Guidance (2025):**
> "The core of any successful generative AI PoC is a robust and repeatable development loop. This loop is the engine room where ideas are tested, prompts are refined, and quality is measured." [5]

**Stanford HELM:**
> "Holistic Evaluation of Language Models (HELM) is an open source Python framework created by the Center for Research on Foundation Models (CRFM) at Stanford for holistic, reproducible and transparent evaluation of foundation models." [6]

HELM introduceert het begrip *evaluation harness*: de software-infrastructuur die modellen draait tegen meerdere benchmarks en resultaten aggregeert. Het framework meet 7 dimensies (accuracy, calibration, robustness, fairness, bias, toxicity, efficiency) over 60+ scenario's en 90+ modellen.

**NIST AI RMF 1.0 (2023):**
> "TEVV tasks can provide insights relative to technical, societal, legal, and ethical standards or norms, and can assist with anticipating impacts and assessing and tracking emergent risks. As a regular process within an AI lifecycle, TEVV allows for both mid-course remediation and post-hoc risk management." [7]

NIST introduceert TEVV (Test, Evaluate, Verify, Validate) als kernproces binnen de *Measure*-functie van het AI Risk Management Framework.

**Google DeepMind:**
Google DeepMind hanteert geen expliciete definitie van "eval" als term, maar benadert evaluatie via specifieke benchmarks (FACTS Grounding, DeepSearchQA, MRCR v2, Chess Text) met als filosofie: het promoten van "development of LLMs that are both knowledgeable and trustworthy." [8] (`verified` — evals-pagina gecheckt; geen definitie gevonden)

### 1.2 Gesynthetiseerde werkdefinitie

Op basis van bovenstaande bronnen:

**Een evaluation loop is een gesloten, terugkerende cyclus waarin:**
1. AI-output wordt beoordeeld aan expliciete criteria via gestandaardiseerde taken en graders.
2. Bevindingen worden geanalyseerd op patronen en gaps.
3. Concrete verbeteracties worden doorgevoerd in prompts, modellen, data of processen.
4. De cyclus herstart — waarna kwaliteitsverbetering aantoonbaar is.

Het *loop*-kenmerk is het onderscheidende element. Een eenmalige benchmark is géén evaluation loop. Een CI/CD-test is géén evaluation loop. De loop is pas volledig wanneer bevindingen teruggekoppeld worden naar actie én de volgende meting de verbetering bevestigt.

### 1.3 Terminologische kaart

| Term | Context | Dominant bij |
|------|---------|-------------|
| eval(s) | Informele meervoud; productiegericht | Anthropic, OpenAI, industrie |
| evaluation | Formele enkelvoud | Academisch (NeurIPS, ACL) |
| evaluation harness | Software-infrastructuur voor test-uitvoering | Stanford HELM, Inspect AI |
| eval pipeline | End-to-end data-flow van test naar resultaat | MLOps-teams |
| TEVV | Test, Evaluate, Verify, Validate | NIST AI RMF |
| evaluation loop | Gesloten cyclus met terugkoppeling | Industrie, AWS, dit rapport |
| post-market monitoring | Verplichte productie-evaluatie | EU AI Act |
| benchmark | Eenmalige meting op standaard dataset | Academisch |

### 1.4 Grensafbakening

- **Observability**: het zichtbaar maken van wat intern in een systeem gebeurt (traces, logs, spans) — input voor de evaluation loop, niet de loop zelf.
- **Monitoring**: continu signaleren van afwijkingen in productie (latency, error rates, drift) — ook input, maar geen beoordeling van outputkwaliteit.
- **MLOps**: bredere discipline; evaluation loop is een deelproces.
- **Benchmark**: eenmalige meting op standaard dataset — bouwsteen, maar niet cyclisch.

---

## 2. Productie-rijpe evaluation loop: fasen

Een volwaardige evaluatiecyclus bestaat uit zes fasen:

**Fase 1 — Pre-deploy offline eval**
Gecontroleerde testset, bekende expected outputs, geen echte gebruikers. Alle wijzigingen (prompt-update, modelwissel, context-aanpassing) triggeren een run. Output: go/no-go beslissing voor deployment.

**Fase 2 — Shadow mode**
Nieuw model draait parallel aan productie. Responses worden vastgelegd maar niet getoond aan gebruikers. Analyse van kwaliteitsverschillen zonder gebruikersimpact. Startpunt voor elke significante modelwisseling of grote prompt-herziening. [16]

**Fase 3 — Canary release**
Na succesvolle shadow mode: 1% → 5% → 20% → 50% → 100% van echt verkeer. Metrics worden continu vergeleken met baseline. Bij overschrijding van vooraf gedefinieerde drempel: automatische rollback. Bij hoog-risico toepassingen: start op 0.1%. [16]

**Fase 4 — Post-deploy online evaluation**
Continue monitoring via impliciete feedback (klikgedrag, abandonment rate, herhalingsrate van dezelfde vraag) en expliciete feedback (thumbs up/down, sterrenrating, correctie-acties). Escalatie-rate naar menselijke agent is een van de sterkste signalen voor systemisch falen.

**Fase 5 — Drift monitoring**
Detectie van drie vormen van drift:
- *Data drift*: distributie van input-queries verschuift.
- *Concept drift*: de relatie tussen input en correct antwoord verandert (de werkelijkheid verandert).
- *Performance drift*: kwaliteitsmetrieken dalen zonder expliciete applicatiewijziging.

**Fase 6 — Verbeteractie en heropleiding**
Bevindingen leiden tot aanpassingen: nieuwe prompts, andere modelversie, verbeterd retrieval, uitgebreide toolset. De cyclus herstart bij fase 1. Zonder deze stap is de loop open — en is evaluatie slechts rapportage-theater.

(`verified` voor fasen 2-3 via [16]; fasen 4-6 `inferred` op basis van AWS en industrie-consensus)

---

## 3. Kwaliteitsmetrieken: taxonomie

### 3.1 Referentie-gebaseerde methoden (met gold-answer)

| Methode | Wanneer | Valkuil |
|---------|---------|---------|
| Exact Match | Deterministische outputs (SQL, JSON, code) | Inflexibel; werkt niet bij open-ended taken |
| BLEU/ROUGE | Vertaling, samenvatting | Correleert slecht met menselijk oordeel |
| BERTScore | Semantische gelijkenis; parafrasering herkennen | Mist kritische details ondanks hoge score |
| LLM-as-judge met rubric | Open-ended taken; productieschaal | Vereist kalibratie; bias-gevoelig |

### 3.2 Referentie-vrije methoden (zonder gold-answer)

| Methode | Wanneer | Valkuil |
|---------|---------|---------|
| Regex/text-stats | Formaat-validatie (JSON geldig? lengte in range?) | Eenvoudig te passeren; meet vorm, niet inhoud |
| Model-based classifiers | Toxicity, PII-detectie, sentiment | Domein-specifieke blinde vlekken |
| LLM-as-judge | Beoordeling op beschreven criteria | Zelfde biases als judge-model |

**Productieaanbeveling:** combineer deterministische checks (snel, goedkoop) + LLM-as-judge (voor nuance) + periodieke menselijke steekproef (kalibratie). Een 75-90% match tussen judge en menselijk label wordt als productierijp beschouwd. (`inferred` — op basis van Evidently AI en Arize) [11]

---

## 4. Eval-set design

### 4.1 Grootte en samenstelling

| Parameter | Richtlijn |
|-----------|-----------|
| Minimale startset | 20-50 cases voor eerste testset |
| Productie-betrouwbaar | 100-500 cases |
| Hoog-risico (medisch, juridisch) | 1.000+ cases |
| Samenstelling | 60-70% happy-path, 20-30% edge cases, 5-10% adversarial |

**Golden dataset**: een gecureerde, versioned collectie van prompts, inputs, contexten en verwachte uitkomsten die de source of truth vormt voor kwaliteitsmeting. Versiebeheer is verplicht: elke schema- of labelwijziging wordt getraceerd. (`inferred` — Maxim AI, Evidently AI) [via zoekresultaten]

### 4.2 Synthetische data

Synthetische data versnelt opbouw van eval-sets, maar heeft risico's:
- Gebruik niet hetzelfde model voor generatie én validatie.
- Valideer via SME-review; "silver-to-gold" promotie via human-in-the-loop.
- Periodieke decontaminatie: overlap-checks met trainingsdata.

### 4.3 Data-contaminatie als stille faalmodus

Eval-set leakage in trainingsdata is een gedocumenteerd probleem. ICML 2025 toont 5-15% absolute accuracy drops wanneer contaminatie wordt verwijderd. GSM8K laat een gedocumenteerde drop van 13% zien. [12] (`verified`) Gevolg: het model "weet" de antwoorden, scoort hoog op de benchmark maar generaliseert niet. Oplossing: AntiLeakBench-aanpak (constructie van samples met expliciete nieuwe kennis afwezig van trainingsdata). [13]

---

## 5. LLM-as-judge: kalibratie en biases

### 5.1 Cohen's Kappa als kalibratiemaat

Cohen's Kappa (κ) meet inter-rater overeenstemming gecorrigeerd voor toeval:

| κ-waarde | Interpretatie | Productie-geschiktheid |
|----------|--------------|----------------------|
| < 0.40 | Slecht | Niet — criteria of judge-prompt herzien |
| 0.40-0.60 | Matig | Exploratie; niet voor productie |
| 0.60-0.80 | Goed | Productiegeschikt voor niet-kritische toepassingen |
| > 0.80 | Uitstekend | Vereist voor hoog-risico of compliance-gevoelige systemen |

(`inferred` — Landis & Koch 1977 als klassieke bron; κ-drempels niet in één primaire AI-bron gecombineerd) [via ACL 2025]

### 5.2 Bekende biases

- **Lengte-bias**: langere antwoorden scoren hoger, ongeacht kwaliteit. [14]
- **Positie-bias**: antwoord als eerste getoond scoort beter.
- **Zelf-voorkeur**: hetzelfde model als judge en kandidaat — inflated scores. [14]
- **Stijl-bias**: voorkeur voor formeel taalgebruik boven feitelijke accuraatheid.

**Mitigatie**: gebruik een ander model als judge (nooit hetzelfde); overweeg een ensemble van meerdere judge-modellen; combineer Cohen's Kappa met semantische cosinus-similarity voor dubbele validatie. [arxiv 2512.20352]

### 5.3 Wanneer een mens onvermijdelijk is

- Hoog-risico beslissingen (medisch, juridisch, HR).
- Eerste kalibratie van nieuwe rubric (minimaal 50 human-labeled seed examples).
- Wanneer judge-model alignment niet is bewezen voor het specifieke domein.

---

## 6. Agentic en multi-turn evaluatie

### 6.1 Fundamenteel verschil

| Aspect | Single-turn | Agentic/multi-turn |
|--------|------------|-------------------|
| Input → output | Direct | Input → trajectory (N stappen) → finale state |
| Grading | Op eindresultaat | Op elke laag van het pad |
| Foutpropagatie | Geïsoleerd | Fouten propageren door het pad |
| Sandboxing | Niet nodig | Noodzakelijk (tool-uitvoering) |
| Reproduceerbaarheid | Eenvoudig | Uitdagend (non-deterministisch pad) |

### 6.2 Trajectory-evaluation metrics

Op basis van TRAJECT-Bench (arxiv 2510.04550) en LangChain AgentEvals:
- **Trajectory Exact-Match**: het pad is identiek aan de verwachte route (strikte modus).
- **Trajectory Inclusion**: vereiste tools worden aangeroepen in de juiste volgorde.
- **Tool Selection Accuracy**: juiste tool gekozen voor de taak.
- **Tool Parameter Accuracy**: correcte parameters meegegeven.
- **Multi-turn Function Calling Accuracy**: across meerdere beurten consistent.
- **Tool Call Error Rate**: percentage mislukte tool-aanroepen. [9] (`verified`)

### 6.3 Amazon-lessen (praktijk)

Amazon evalueerde een agentic shopping assistant op: topic adherence (blijft agent in scope?), faithfulness (consistent met conversatiegeschiedenis?), tool-call correctness en escalatie-rate. Slecht gedefinieerde tool-schemas zijn de grootste bron van agentic fouten. [10] (`verified`)

---

## 7. Governance en compliance

### 7.1 EU AI Act — vier pilaren voor evaluation

**Art. 9 — Risicobeheer**: verplicht een *"continuous iterative process throughout the entire lifecycle"*. Tests moeten met *"prior defined metrics and probabilistic thresholds"* worden uitgevoerd. Vóór marktplaatsing en periodiek daarna. [1 — governance]

**Art. 10 — Data governance**: bias-detectie en -mitigatie zijn verplicht. Datasets moeten representatief zijn voor de inzetomgeving. Datamanagement-documentatie is verplicht onderdeel van technische documentatie. [2 — governance]

**Art. 15 — Nauwkeurigheid en robuustheid**: nauwkeurigheidsniveaus en -metrics moeten gedocumenteerd zijn in gebruikersinstructies. Continu-lerende systemen moeten feedback-loop-contaminatie voorkomen (output mag niet ongecontroleerd in volgende training). [3 — governance]

**Art. 72 — Post-market monitoring**: actief en systematisch relevante prestatiedata verzamelen gedurende de gehele levensduur. Gebaseerd op formeel post-market monitoring plan. **Inwerkingtredingsdatum: 2 augustus 2026.** [4 — governance] (`verified`)

### 7.2 ISO/IEC 42001:2023

Clause 9 vereist drie kernelementen:
1. Doorlopende monitoring en meting.
2. Interne audit minimaal jaarlijks (vaker bij hoog-risico AI).
3. Managementbeoordeling door topmanagement.

Certificering 3 jaar geldig met jaarlijkse surveillance. [5-6 — governance] (`verified`)

### 7.3 NIST AI RMF — TEVV

TEVV is een *regulier lifecycle-proces*: niet eenmalig, maar terugkerend. De *Measure*-functie gebruikt "quantitative, qualitative, or mixed-method tools, techniques, and methodologies to analyze, assess, benchmark, and monitor AI risk." [7 — governance] (`verified`)

### 7.4 Nederlandse toezichtsstructuur

Vijf primaire toezichthouders voor de EU AI Act in Nederland: AP, RDI, ACM, AFM, DNB. Tien in totaal inclusief sectorale autoriteiten (IGJ, NZa, Inspectie Onderwijs). Focus AP in 2025: transparantie, standaardisatie, auditing, governance, non-discriminatie. [8-10 — governance] (`verified`)

---

## 8. Tools en platforms (2025-2026)

### 8.1 Overzicht

| Tool | Type | Sterkste domein | Prijs |
|------|------|----------------|-------|
| DeepEval | OSS framework | Brede LLM eval; Pytest; CI/CD | Free / $19.99/user |
| Ragas | OSS framework | RAG-specifieke metrics | Free |
| Inspect AI (AISI) | OSS framework | Sandboxed agentic evals; auditeerbaar | Free |
| LangSmith | SaaS | LangChain/LangGraph; trajectory scoring | $39/seat/mo |
| W&B Weave | SaaS | Agent trace observability | $60/mo |
| Braintrust | SaaS | CI/CD pipeline gates; AI prompt-optimalisatie | $249/mo (onbeperkt) |
| Humanloop | SaaS | Niet-technische samenwerking | op aanvraag |
| Arize Phoenix | OSS/SaaS | OpenTelemetry-native; self-hostbaar | Free / $50/mo |
| Comet Opik | SaaS | Automatische prompt-optimalisatie | $19/mo |

[1 — tooling] (`verified`)

### 8.2 Beslisheuristiek

- Engineering-team, Pytest-cultuur, CI/CD gates: **DeepEval + Braintrust**
- RAG-pipeline: **Ragas + Langfuse of Arize Phoenix**
- Agentic systemen, sandboxed uitvoering, auditeerbaar: **Inspect AI**
- LangChain/LangGraph ecosystem: **LangSmith**
- Vendor-neutraal, self-hosted, OpenTelemetry: **Arize Phoenix**
- Niet-technische product managers mee in loop: **Humanloop**

---

## 9. Anti-patronen

**1. Vibe-checking** — AI-output op gevoel beoordelen via een paar voorbeelden. Niet schaalbaar; geen statistische basis.

**2. Demo-driven development** — Eval-set bestaat uit precies de cases die aan het management worden getoond. Systeem scoort 95% op eval maar faalt in 30% van echte gevallen.

**3. Single-metric tunnel-vision** — Optimaliseren op één metric (ROUGE, BLEU) terwijl andere dimensies (safety, faithfulness, bias) worden genegeerd. Goodhart's Law: *"When a measure becomes a target, it ceases to be a good measure."* [8 — tooling] (`verified`)

**4. Eval-set staleness** — Eval-set wordt eenmalig aangemaakt en nooit bijgewerkt. Na 6-12 maanden mist de set nieuwe productfeatures en gebruikerspatronen.

**5. Judge-model contaminatie** — Hetzelfde model als judge en kandidaat. Zelf-voorkeur leidt tot systematisch hoge scores. Gebruik altijd een ander model als judge.

**6. Only happy path** — Eval-set bevat alleen succesvolle gevallen; edge cases en adversarial inputs ontbreken. Systeem lijkt 98% nauwkeurig maar faalt bij onverwachte inputs.

**7. Eval-set leakage** — Benchmarkdata komt terecht in trainingsdata. Model "weet" de antwoorden; generaliseert niet. [12] (`verified`)

**8. Rapportage-theater** — De loop produceert dashboards maar geen beslissingen. Metrics worden bijgehouden zonder dat bevindingen leiden tot aanpassingen. De loop is open.

---

## 10. Verhouding tot andere BeeHaive-bouwstenen

| Bouwsteen | Rol in evaluation loop |
|-----------|----------------------|
| BB_01 Knowledge | Levert eval-criteria: wat zijn de juiste antwoorden? Knowledge Graph als ground truth. |
| BB_02 Client Blueprint | Bepaalt succescriteria: welke outputs zijn voor de klant waardevol? |
| BB_03 Dynamic Context | Wordt geëvalueerd op grounding: haalt de context de juiste informatie op? |
| BB_04 Prompt Design | Wordt regression-tested: elke prompt-update triggert een eval-run. |
| BB_05 Tool Integration | Evalueert tool-call correctness: juiste tool, juiste parameters, juiste volgorde. |
| BB_06 Model Engines | Modelvergelijking via evals: welk model presteert het best op deze use case? |
| BB_07 Evaluation Loop | Overkoepelt alle andere bouwstenen: de motor die verbetering aantoonbaar maakt. |

---

## Tegenstrijdigheden en open vragen

**Geen fundamentele tegenstrijdigheden** gevonden tussen primaire bronnen op kernzaken. Terminologische differentiatie (eval vs. TEVV vs. monitoring) is reëel maar complementair.

**Open vragen:**
- Exacte Cohen's Kappa-drempel voor AI-productiesystemen: geen single primary source stelt een specifiek getal. BeeHaive's 0.717 is een verdedigbare praktijkkeuze, niet een industrie-standaard.
- Art. 17 (kwaliteitsmanagementsysteem) niet direct in primaire brontekst gecheckt; beschrijving via zoekresultaten.
- Exacte bewaartermijnen voor eval-sets zijn niet expliciet benoemd in de EU AI Act-tekst (alleen technische documentatie generiek).

---

## Sources

### Definitie & methoden
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
12. ICML 2025 — Data Contamination — https://icml.cc/virtual/2025/poster/43619
13. ACL 2025 — AntiLeakBench — https://aclanthology.org/2025.acl-long.901/
14. arxiv — Judge's Verdict — https://arxiv.org/pdf/2510.09738
15. LangChain AgentEvals — https://github.com/langchain-ai/agentevals
16. TianPan — LLM Gradual Rollout — https://tianpan.co/blog/2026-04-09-llm-gradual-rollout-shadow-canary-ab-testing

### Governance
17. EU AI Act Art. 9 — https://artificialintelligenceact.eu/article/9/
18. EU AI Act Art. 10 — https://artificialintelligenceact.eu/article/10/
19. EU AI Act Art. 15 — https://artificialintelligenceact.eu/article/15/
20. EU AI Act Art. 72 — https://artificialintelligenceact.eu/article/72/
21. ISO/IEC 42001 — CSA Audit Lessons — https://cloudsecurityalliance.org/blog/2025/05/08/iso-42001-lessons-learned-from-auditing-and-implementing-the-framework
22. ISO/IEC 42001 — AWS — https://aws.amazon.com/blogs/security/ai-lifecycle-risk-management-iso-iec-420012023-for-ai-governance/
23. AP/RDI — Supervisie AI NL — https://www.autoriteitpersoonsgegevens.nl/en/current/ap-and-rdi-supervision-of-ai-systems-requires-cooperation-and-must-be-arranged-quickly
24. Pinsent Masons — 10 Dutch Regulators — https://www.pinsentmasons.com/out-law/news/ai-compliance-overseen-10-dutch-regulators

### Tooling & praktijk
25. Goodeye Labs — Top eval tools 2026 — https://www.goodeyelabs.com/articles/top-ai-agent-evaluation-tools-2026
26. Braintrust — LLM Eval Platforms — https://www.braintrust.dev/articles/best-llm-evaluation-platforms-2025
27. Arize Phoenix Docs — https://arize.com/docs/phoenix
28. Inspect AI — https://inspect.aisi.org.uk/
29. GitHub deepeval — https://github.com/confident-ai/deepeval
30. Collinear — Goodhart's Law in AI — https://blog.collinear.ai/p/gaming-the-system-goodharts-law-exemplified-in-ai-leaderboard-controversy
