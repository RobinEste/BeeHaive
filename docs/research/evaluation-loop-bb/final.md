# Evaluation Loop (BB_07) — Onderzoeksrapport

**Onderwerp:** Evaluation Loop voor AI-systemen — definitie, methoden, governance, tooling en anti-patronen
**Datum:** 2026-05-01
**Researcher-rondes:** 1 (stop-trigger: acceptatiecriteria volledig voldaan)
**Verificatiepass:** PASS-WITH-NOTES

---

## Executive Summary

De evaluation loop is de motor achter elke AI-oplossing die over tijd beter wordt. Toch is het de meest overgeslagen stap in AI-projecten: teams bouwen, deployen, en hopen. Zonder systematische evaluatie degradeert elk AI-systeem — niet dramatisch, maar stil, onzichtbaar.

In de AI-industrie convergeren Anthropic, OpenAI, AWS, Stanford en NIST op een gedeeld concept: een evaluation loop is een gesloten, terugkerende cyclus van meten, analyseren en verbeteren. Het *loop*-onderdeel is het onderscheidende kenmerk. Een eenmalige benchmark is geen loop. Een dashboard zonder actie is geen loop. De loop sluit pas wanneer bevindingen leiden tot aantoonbare veranderingen in prompts, modellen, data of processen.

Tegelijk is evaluatie een rijp, volwassen vakgebied geworden. Er zijn duidelijke primaire bronnen met werkdefinities, een toolinglandschap van meer dan een dozijn platforms, en een wettelijk kader (EU AI Act Art. 9, 10, 15, 17, 72; ISO/IEC 42001; NIST AI RMF) dat de evaluation loop voor hoog-risico AI-systemen verplicht stelt. Wat ontbreekt in de meeste praktijkimplementaties is niet kennis, maar discipline: de wil om de loop daadwerkelijk te sluiten.

---

## 1. Definitie: wat is een evaluation loop?

### 1.1 Woordelijke definities uit primaire bronnen

**Anthropic — "Demystifying Evals for AI Agents" (2025):**
> "An evaluation (or 'eval') is a test for an AI system: give an AI an input, then apply grading logic to its output to measure success." [1]

Anthropic onderscheidt zeven kernelementen: task, trial, grader, transcript, outcome, evaluation harness en evaluation suite. Het evaluator-optimizer patroon beschrijft de loop expliciet: *"one LLM call generates a response while another provides evaluation and feedback in a loop. This workflow is particularly effective when we have clear evaluation criteria, and when iterative refinement provides measurable value."* [2] (`verified`)

**OpenAI — Working with Evals (2025):**
> "Evaluations (often called evals) test model outputs to ensure they meet style and content criteria that you specify. Writing evals to understand how your LLM applications are performing against your expectations is an essential component to building reliable applications." [3]

OpenAI beschrijft de evaluation loop als een data-flywheel: *"log inputs, outputs, and outcomes; sample those logs on a schedule and automatically route ambiguous or costly cases to expert review. Add these expert judgements to your eval and error analysis, then use them to update prompts, tools, or models."* [3] (`verified`)

**OpenAI — "How evals drive the next chapter of AI for businesses" (november 2025):**
> "Evals [are] methods to measure and improve the ability of an AI system to meet expectations. Similar to product requirement documents, evals make fuzzy goals and abstract ideas specific and explicit." [4] (`inferred` — pagina gaf 403; beschrijving via zoekresultaten)

**AWS Prescriptive Guidance — "Creating evaluation loops for generative AI" (2025):**
> "The core of any successful generative AI PoC is a robust and repeatable development loop. This loop is the engine room where ideas are tested, prompts are refined, and quality is measured." [5] (`verified`)

**Stanford HELM — Holistic Evaluation of Language Models:**
> "Holistic Evaluation of Language Models (HELM) is an open source Python framework created by the Center for Research on Foundation Models (CRFM) at Stanford for holistic, reproducible and transparent evaluation of foundation models." [6]

HELM introduceert het begrip *evaluation harness*: de software-infrastructuur die modellen draait tegen meerdere benchmarks en resultaten aggregeert. Het framework meet 7 dimensies (accuracy, calibration, robustness, fairness, bias, toxicity, efficiency) over 60+ scenario's en 90+ modellen. (`verified`)

**NIST AI RMF 1.0 (januari 2023) — TEVV:**
> "TEVV tasks can provide insights relative to technical, societal, legal, and ethical standards or norms, and can assist with anticipating impacts and assessing and tracking emergent risks. As a regular process within an AI lifecycle, TEVV allows for both mid-course remediation and post-hoc risk management." [7] (`verified`)

**Google DeepMind:**
Google DeepMind hanteert geen expliciete definitie van "eval" als term maar benadert evaluatie via specifieke benchmarks (FACTS Grounding, DeepSearchQA, MRCR v2, Chess Text) met als filosofie het bevorderen van "development of LLMs that are both knowledgeable and trustworthy." [8] (`verified` — evals-pagina gecheckt; geen definitie gevonden)

### 1.2 Gesynthetiseerde werkdefinitie

Op basis van zeven primaire bronnen:

**Een evaluation loop is een gesloten, terugkerende cyclus waarin:**
1. AI-output wordt beoordeeld aan expliciete criteria via gestandaardiseerde taken en graders.
2. Bevindingen worden geanalyseerd op patronen en gaps.
3. Concrete verbeteracties worden doorgevoerd in prompts, modellen, data of processen.
4. De cyclus herstart — waarna de kwaliteitsverbetering aantoonbaar is.

Het *loop*-kenmerk is het onderscheidende element: een eenmalige benchmark, een CI/CD-test of een dashboard zijn géén evaluation loop tenzij bevindingen terugkoppelen naar aantoonbare actie.

### 1.3 Terminologische kaart

| Term | Context | Dominant bij |
|------|---------|-------------|
| eval(s) | Informele meervoud; productiegericht | Anthropic, OpenAI, industrie |
| evaluation | Formele enkelvoud | Academisch (NeurIPS, ACL, papers) |
| evaluation harness | Software-infrastructuur voor test-uitvoering | Stanford HELM, Inspect AI |
| eval pipeline | End-to-end data-flow van test naar resultaat | MLOps-teams |
| TEVV | Test, Evaluate, Verify, Validate | NIST AI RMF |
| evaluation loop | Gesloten cyclus met terugkoppeling | Industrie, AWS, dit rapport |
| post-market monitoring | Verplichte productie-evaluatie | EU AI Act |
| benchmark | Eenmalige meting op standaard dataset | Academisch |

### 1.4 Grensafbakening ten opzichte van aangrenzende begrippen

- **Observability**: het zichtbaar maken van wat intern in een systeem gebeurt (traces, logs, spans) — input voor de evaluation loop, niet de loop zelf.
- **Monitoring**: continu signaleren van afwijkingen in productie (latency, error rates, drift) — ook input, maar geen beoordeling van outputkwaliteit.
- **MLOps**: bredere discipline die de volledige levenscyclus van ML-modellen beheert; evaluation loop is een deelproces.
- **Benchmark**: eenmalige meting op standaard dataset — bouwsteen voor de loop, maar zelf niet cyclisch.

---

## 2. Productie-rijpe evaluation loop: zes fasen

Een volwaardige evaluatiecyclus bestaat uit zes fasen:

**Fase 1 — Pre-deploy offline eval**
Gecontroleerde testset, bekende expected outputs, geen echte gebruikers. Elke wijziging (prompt-update, modelwissel, context-aanpassing, toolkoppeling) triggert een run. Output: go/no-go beslissing voor deployment.

**Fase 2 — Shadow mode**
Nieuw model draait parallel aan productie. Responses worden vastgelegd maar *niet getoond* aan gebruikers. Analyse van kwaliteitsverschillen zonder gebruikersimpact. Verplicht startpunt voor elke significante modelwisseling of grote prompt-herziening. [16] (`verified`)

**Fase 3 — Canary release**
Na succesvolle shadow mode: 1% → 5% → 20% → 50% → 100% van echt verkeer. Metrics continu vergeleken met baseline. Bij overschrijding van vooraf gedefinieerde drempel: automatische rollback. Bij hoog-risico toepassingen: start op 0.1%. [16] (`verified`)

**Fase 4 — Post-deploy online evaluation**
Continue monitoring via:
- Impliciete feedback: klikgedrag, abandonment rate, herhalingsrate van dezelfde vraag (sterk signaal voor systemisch falen).
- Expliciete feedback: thumbs up/down, sterrenrating, correctie-acties.
- Escalatie-rate naar menselijke agent.

**Fase 5 — Drift monitoring**
Drie vormen van drift:
- *Data drift*: distributie van input-queries verschuift.
- *Concept drift*: de relatie tussen input en correct antwoord verandert (de werkelijkheid verandert, niet de applicatie).
- *Performance drift*: kwaliteitsmetrieken dalen zonder expliciete applicatiewijziging — de gevaarlijkste variant omdat er geen duidelijke trigger is.

**Fase 6 — Verbeteractie**
Bevindingen leiden tot aanpassingen: nieuwe prompts, andere modelversie, verbeterd retrieval, uitgebreide toolset. De cyclus herstart bij fase 1. Zonder deze stap is de loop open — en is evaluatie slechts rapportage-theater.

(`inferred` voor fasen 4-6 op basis van AWS, industrie-consensus en OpenAI data-flywheel beschrijving)

---

## 3. Kwaliteitsmetrieken

### 3.1 Taxonomie

**Referentie-gebaseerde methoden (met gold-answer):**

| Methode | Wanneer geschikt | Valkuil |
|---------|-----------------|---------|
| Exact Match | Deterministische outputs (SQL, JSON, code) | Inflexibel; niet geschikt voor open-ended |
| BLEU/ROUGE | Vertaling, samenvatting | Correleert slecht met menselijk oordeel bij open-ended |
| BERTScore | Semantische gelijkenis; parafrasering | Mist kritische details ondanks hoge score |
| LLM-as-judge met rubric | Open-ended taken; productieschaal | Vereist kalibratie; bias-gevoelig |

**Referentie-vrije methoden (zonder gold-answer):**

| Methode | Wanneer geschikt | Valkuil |
|---------|-----------------|---------|
| Regex / text-stats | Formaat-validatie | Meet vorm, niet inhoud |
| Model-based classifiers | Toxicity, PII-detectie | Domein-specifieke blinde vlekken |
| LLM-as-judge | Beoordeling op beschreven criteria | Zelfde biases als het judge-model |

**Productieaanbeveling**: combineer deterministische checks (snel, gratis) + LLM-as-judge (voor nuance) + periodieke menselijke steekproef (kalibratie). Een 75-90% match tussen judge en menselijk label wordt als productierijp beschouwd. (`inferred` — Evidently AI, Arize) [11]

### 3.2 Instance-specifieke rubrieken (2025-trend)

De doorbraak in 2025 is de verschuiving van generieke rubrieken naar *instance-specifieke rubrieken*: elke conversatie krijgt een eigen rubric van 10-40 criteria. OpenAI's HealthBench (2025) is een voorbeeld van deze aanpak, waarbij evaluatie verschuift van stijlbeoordeling naar rigoureuze inhoudsmeting. (`inferred` — via zoekresultaten Adnan Masood blog)

---

## 4. Eval-set design

### 4.1 Grootte-richtlijnen

| Fase | Grootte | Toelichting |
|------|---------|-------------|
| Eerste testset | 20-50 cases | Snel starten; kan suboptimaal zijn |
| Productie-betrouwbaar | 100-500 cases | Statistisch significante resultaten |
| Hoog-risico (medisch, juridisch) | 1.000+ cases | Kleinere sets geven false confidence |

(`inferred` — Maxim AI, Evidently AI via zoekresultaten; geen single primary source met exacte aantallen)

### 4.2 Samenstelling

- 60-70% happy-path (veelvoorkomende, goed-geformeerde queries)
- 20-30% edge cases (ongebruikelijke, ambigue of complexe inputs)
- 5-10% adversarial (inputs die het systeem proberen te misleiden)

### 4.3 Golden dataset vs. synthetische data

Een *golden dataset* is een gecureerde, versioned collectie van prompts, inputs, contexten en verwachte uitkomsten die de source of truth vormt. Versiebeheer is verplicht: elke schema- of labelwijziging wordt getraceerd als een nieuw experiment.

Synthetische data versnelt opbouw maar heeft risico's: gebruik niet hetzelfde model voor generatie én validatie. Promoveer "silver" synthetische data naar "gold" via human-in-the-loop QA (SME-review).

### 4.4 Data-contaminatie als stille faalmodus

Eval-set leakage in trainingsdata is een gedocumenteerd probleem. ICML 2025 toont 5-15% absolute accuracy drops wanneer gecontamineerde voorbeelden worden verwijderd. GSM8K laat een gedocumenteerde drop van 13% zien. [12] (`verified`) Het model "weet" de antwoorden, scoort hoog op de benchmark maar generaliseert niet.

Oplossing: periodieke overlap-checks met trainingsdata; de AntiLeakBench-aanpak construeert samples met expliciete nieuwe kennis die afwezig is in trainingsdata. [13] (`verified`)

---

## 5. LLM-as-judge: kalibratie en biases

### 5.1 Cohen's Kappa als kalibratiemaat

Cohen's Kappa (κ) meet inter-rater overeenstemming gecorrigeerd voor toeval. Gangbare interpretatiedrempels (Landis & Koch 1977):

| κ-waarde | Interpretatie | Productie-geschiktheid |
|----------|--------------|----------------------|
| < 0.40 | Slecht | Niet — criteria of judge-prompt herzien |
| 0.40-0.60 | Matig | Exploratie; niet voor productie |
| 0.60-0.80 | Goed | Productiegeschikt voor niet-kritische toepassingen |
| > 0.80 | Uitstekend | Vereist voor hoog-risico of compliance-gevoelige systemen |

(`inferred` — Landis & Koch is de klassieke bron; geen single primaire AI-bron combineert deze drempels expliciet voor AI-productiesystemen) [14]

### 5.2 Bekende biases

- **Lengte-bias**: langere antwoorden scoren hoger, ongeacht kwaliteit. [14] (`verified`)
- **Positie-bias**: antwoord als eerste getoond scoort beter.
- **Zelf-voorkeur**: hetzelfde model als judge én kandidaat — inflated scores. [14]
- **Stijl-bias**: voorkeur voor formeel taalgebruik boven feitelijke accuraatheid.

**Mitigatie**: gebruik een *ander* model als judge (nooit hetzelfde). Overweeg een ensemble van meerdere judge-modellen gecombineerd met cosinus-similarity voor dubbele validatie. (`inferred` — arxiv multi-LLM thematic analysis paper)

### 5.3 De Judge Paradox: rubric-kwaliteit > judge-kracht

Een opmerkelijke ontdekking in 2025: een relatief zwak model met een gedetailleerde, multidimensionale rubric presteert systematisch beter dan een superieur model met een vage instructie. De kwaliteit van grading wordt gedomineerd door de *structuur* van de rubric, niet door de ruwe rekenkracht van de beoordelaar. (`inferred` — Gemini Deep Research, mei 2026)

Dit ondersteunt de praktijk van **analytische rubrieken**: elk criterium (feitelijke juistheid, veiligheid, merktoon, beknoptheid) afzonderlijk gescoord in plaats van één enkel cijfer. Voordeel: bij kwaliteitsdaling kan root-cause-analyse direct aanwijzen of de degradatie zit in feitelijkheid of in toon — niet in een vaag "lager cijfer".

### 5.4 Wanneer een mens onvermijdelijk is

- Hoog-risico beslissingen (medisch, juridisch, HR).
- Eerste kalibratie van een nieuwe rubric (minimaal 50 human-labeled seed examples).
- Wanneer judge-model alignment voor het specifieke domein niet bewezen is.

---

## 6. Agentic en multi-turn evaluatie

### 6.1 Fundamenteel verschil met single-turn

| Aspect | Single-turn | Agentic/multi-turn |
|--------|------------|-------------------|
| Evaluatiescope | Input → output | Input → trajectory (N stappen) → finale state |
| Grading | Op eindresultaat | Op elke laag van het pad |
| Foutpropagatie | Geïsoleerd | Fouten propageren door het pad heen |
| Sandboxing | Niet nodig | Noodzakelijk (tool-uitvoering in isolatie) |
| Reproduceerbaarheid | Eenvoudig | Uitdagend (non-deterministisch pad) |

### 6.2 Trajectory-evaluation metrics

Op basis van TRAJECT-Bench [9] en LangChain AgentEvals [15]:

- **Trajectory Exact-Match**: het pad is identiek aan de verwachte route (strikte modus).
- **Trajectory Inclusion**: vereiste tools worden aangeroepen in de juiste volgorde.
- **Tool Selection Accuracy**: juiste tool gekozen voor de taak.
- **Tool Parameter Accuracy**: correcte parameters meegegeven.
- **Multi-turn Function Calling Accuracy**: consistentie over meerdere beurten.
- **Tool Call Error Rate**: percentage mislukte tool-aanroepen.

(`verified` — TRAJECT-Bench arxiv 2510.04550)

### 6.3 Praktijkles: Amazon shopping assistant

Amazon evalueerde een agentic shopping assistant op: tool-selection accuracy, tool-parameter accuracy, multi-turn function calling accuracy, topic adherence (blijft agent in scope?), faithfulness (consistent met conversatiegeschiedenis?) en escalatie-rate. Kernles: *slecht gedefinieerde tool-schemas zijn de grootste bron van agentic fouten*. Productie-monitoring vereist real-time dashboards en geautomatiseerde anomaly-detectie met drempelwaarden. [10] (`verified`)

### 6.4 Het tool-call-faalpercentage als primaire eval-metriek

Onderzoek wijst uit dat tool-gebruik een van de meest voorkomende faalpunten is in agentic systemen, met **foutpercentages tot 36% in complexe conversaties** bij sommige frontier-modellen. (`inferred` — Gemini Deep Research, mei 2026) De evaluation loop moet daarom expliciet testen op:

- *Tool routing*: wordt de juiste tool gekozen voor de taak?
- *Foutafhandeling*: hoe gaat de agent om met API-fouten van externe diensten?
- *Variabiliteit als signaal*: een agent met 80% slaagkans + occasionele catastrofale fout is in productie minder betrouwbaar dan een agent met 75% slaagkans en stabiel gedrag.

### 6.5 Stille faalmodi specifiek voor agentic systemen

Twee categorieën die regulier eval-design onvoldoende afvangt:

- **Pretrained domain knowledge hallucinations**: het model vertrouwt op verouderde of onjuiste informatie uit zijn trainingsdata in plaats van de feiten uit de meegeleverde context (RAG). De gebruiker kan vaak niet verifiëren of een bewering uit de bron komt of "verzonnen" is. Eval-eis: faithfulness-checks moeten expliciet de bron-tracebility toetsen, niet alleen de plausibiliteit.
- **Context-drift in multi-turn**: naarmate een conversatie vordert, verliest de agent de oorspronkelijke instructies of het doel uit het oog. Eval-eis: long-trajectory tests met scope-adherence-checks per beurt.

(`inferred` — Gemini Deep Research, mei 2026)

---

## 7. Governance en compliance

### 7.1 EU AI Act: vier evaluatiepilaren voor hoog-risico AI

**Art. 9 — Risicobeheer:**
Verplicht een *"continuous iterative process throughout the entire lifecycle"*. Tests moeten worden uitgevoerd met *"prior defined metrics and probabilistic thresholds appropriate to the intended purpose"*. Vóór marktplaatsing én periodiek daarna. Data uit post-marktmonitoring (Art. 72) moet worden geanalyseerd. [17] (`verified`)

**Art. 10 — Data governance:**
Bias-detectie en -mitigatie zijn verplicht: *"appropriate measures to detect, prevent and mitigate possible biases."* Datasets moeten representatief zijn voor de specifieke inzetomgeving. Datamanagement-documentatie is verplicht onderdeel van technische documentatie. [18] (`verified`)

**Art. 12 — Logging van gebeurtenissen:**
Automatische logging van events gedurende de levenscyclus. Voor de evaluation loop betekent dit: bewaren van volledige trajecten (traces) met timestamps, niet alleen eindscores. Capability-eis (wat het systeem moet kunnen vastleggen). Bewaartermijn staat in Art. 19 (providers, ≥6 mnd) en Art. 26 lid 6 (deployers).

**Art. 13 — Transparantie voor deployers:**
Verplicht dat deployers de instructies en eigenschappen van het systeem kunnen begrijpen. Voor de eval-loop: interpretatierubrieken en uitlegbare redeneerstappen, niet alleen een "score 7/10". Sluit aan op Stap 5.3 (analytische rubrieken).

**Art. 14 — Menselijk toezicht:**
Hoogrisico-systemen moeten menselijk ingrijpen mogelijk maken. Voor de eval-loop: *interrupt*-mechanismen (kill-switch) en menselijke review-wachtrijen voor escalatie zijn ontwerp-eisen. Sluit aan op trajectory-evaluation (sectie 6) met escalatie-rate als reguliere metriek.

**Art. 15 — Nauwkeurigheid en robuustheid:**
Nauwkeurigheidsniveaus en -metrics moeten gedocumenteerd zijn in gebruikersinstructies. Continu-lerende systemen moeten feedback-loop-contaminatie voorkomen: productie-output mag niet ongecontroleerd de volgende trainingscyclus beïnvloeden. [19] (`verified`)

**Art. 72 — Post-market monitoring:**
Actief en systematisch relevante prestatiedata verzamelen gedurende de *gehele levensduur* van het systeem. Verplicht op basis van een formeel post-market monitoring plan (onderdeel van technische documentatie). De Europese Commissie moest vóór 2 februari 2026 een template publiceren. **Inwerkingtredingsdatum: 2 augustus 2026.** [20] (`verified`)

**Bewaartermijnen:**
- Technische documentatie (incl. testresultaten): 10 jaar na marktplaatsing. (`inferred` — standaard termijn Art. 18; niet gecontroleerd in originele wettekst)
- Logs en registraties: minimaal over de periode van gebruik; sectorspecifiek langer (medisch: levensduur apparaat).
- Post-marktmonitoringplan: verplicht op te leveren aan toezichthouder op aanvraag.

### 7.2 ISO/IEC 42001:2023

Clause 9 (Performance Evaluation) vereist:
1. Doorlopende monitoring en meting van het AI Management System.
2. Interne audit minimaal jaarlijks (Clause 9.2.1); vaker bij hoog-risico AI.
3. Managementbeoordeling door topmanagement.

Certificering 3 jaar geldig met jaarlijkse surveillance-audit en hercertificering in jaar 3. [21] (`verified`)

### 7.3 NIST AI RMF — TEVV als regulier proces

TEVV (Test, Evaluate, Verify, Validate) is expliciet een *regulier lifecycle-proces*, niet eenmalig. De *Measure*-functie gebruikt "quantitative, qualitative, or mixed-method tools, techniques, and methodologies to analyze, assess, benchmark, and monitor AI risk." [7] (`verified`)

### 7.4 Nederlandse toezichtsstructuur (per mei 2026)

Vijf primaire toezichthouders EU AI Act in Nederland:
- **AP** (Autoriteit Persoonsgegevens) — privacy en grondrechten
- **RDI** (Rijksdienst voor Digitale Infrastructuur) — digitale infrastructuur
- **ACM** (Autoriteit Consument en Markt) — consumentenrecht
- **AFM** (Autoriteit Financiële Markten) — financiële sector
- **DNB** (De Nederlandsche Bank) — bancaire sector

Aanvullend (sectoraal): IGJ (zorg), NZa (zorgbekostiging), Inspectie Onderwijs. [23-24] (`verified`)

Focus AP in 2025: transparantie, standaardisatie, auditing, governance, non-discriminatie en AI-geletterdheid. Nederlandse Implementatiewet AI-verordening verwacht Q4 2026.

---

## 8. Tools en platforms

### 8.1 Overzicht 2025-2026

**Open source frameworks (eval-as-code):**

| Tool | Sterkste domein | Licentie |
|------|----------------|----------|
| DeepEval | Brede LLM eval; 50+ metrics; Pytest; CI/CD | MIT |
| Ragas | RAG-specifieke metrics (faithfulness, context relevance) | Apache 2.0 |
| Inspect AI (UK AISI) | Sandboxed agentic evals; reproduceerbaar; auditeerbaar | MIT |
| MLflow | Experiment tracking; model lifecycle | Apache 2.0 |
| Langfuse | Observability + eval; self-hostbaar | MIT |

**SaaS platforms:**

| Tool | Sterkste domein | Startprijs |
|------|----------------|-----------|
| LangSmith | LangChain/LangGraph; trajectory scoring | $39/seat/mo |
| W&B Weave | Agent trace observability | $60/mo |
| Braintrust | CI/CD gates; AI prompt-optimalisatie; flat pricing | $249/mo (unlimited users) |
| Humanloop | Niet-technische samenwerking; prompt management | op aanvraag |
| Arize Phoenix | OpenTelemetry-native; self-hostbaar; v3.0 (apr 2026) | Free / $50/mo |
| Comet Opik | Automatische prompt-optimalisatie | $19/mo |

(`verified` voor prijzen bij Goodeye Labs [25]; platformkeuzes `inferred` op basis van meerdere vergelijkingsbronnen)

### 8.2 Beslisheuristiek

| Situatie | Aanbevelen |
|----------|-----------|
| Engineering-team; Pytest-cultuur; CI/CD gates | DeepEval + Braintrust |
| RAG-pipeline evalueren | Ragas + Langfuse of Arize Phoenix |
| Agentic systemen; sandboxed uitvoering; auditeerbaar | Inspect AI (UK AISI) |
| LangChain/LangGraph ecosystem | LangSmith |
| Vendor-neutraal; self-hosted; OpenTelemetry | Arize Phoenix |
| Niet-technische product managers mee in loop | Humanloop |

### 8.3 Arize Phoenix: opmerkelijk

Enige major platform volledig op OpenTelemetry gebouwd. Framework-agnostisch: werkt met OpenAI, Anthropic, LangChain, CrewAI, LlamaIndex, DSPy. Versie 3.0.0 uitgebracht april 2026. Zelf-hostbaar via Docker. [27] (`verified`)

### 8.4 Inspect AI: bijzonder voor compliance-teams

Ontwikkeld door het UK AI Security Institute (AISI). Sandbox-uitvoering via Docker; reproduceerbaar; auditeerbaar. Meest complete OSS-keuze voor teams die evals als productie-infrastructuur behandelen en moeten aantonen aan toezichthouders. [28] (`verified`)

---

## 9. Anti-patronen: acht faalmodi

**1. Vibe-checking**
AI-output op gevoel beoordelen via een paar voorbeelden. Niet schaalbaar; geen statistische basis. Definitief niet geschikt zodra het systeem meer dan honderd gebruikers bedient.

**2. Demo-driven development**
Eval-set bestaat uit precies de cases die aan het management worden getoond. Systeem scoort 95% op eval maar faalt in 30% van echte gebruikscases. Edge cases, adversarial inputs en minority-cases ontbreken.

**3. Single-metric tunnel-vision**
Optimaliseren op één metric terwijl andere dimensies (safety, faithfulness, bias) worden genegeerd. Goodhart's Law: *"When a measure becomes a target, it ceases to be a good measure."* [30] Concreet 2025-voorbeeld: grote AI-labs publiceerden selectief alleen de beste Arena-scores.

**4. Eval-set staleness**
Eval-set wordt eenmalig aangemaakt en nooit bijgewerkt. Na 6-12 maanden: de werkelijkheid heeft zich gewijzigd. De eval meet niet meer wat er in productie relevant is.

**5. Judge-model contaminatie**
Hetzelfde model als judge én als kandidaat. Zelf-voorkeur leidt tot systematisch hoge scores. Gebruik altijd een *ander* model als judge, of een ensemble.

**6. Only happy path**
Eval-set bevat alleen succesvolle gevallen. Systeem lijkt 98% nauwkeurig maar faalt volledig bij onverwachte inputs.

**7. Eval-set leakage in trainingsdata**
Benchmarkdata komt terecht in trainingsdata. Model "weet" de antwoorden; generaliseert niet. ICML 2025: 5-15% accuracy drops wanneer contaminatie wordt verwijderd. [12] (`verified`)

**8. Rapportage-theater**
De loop produceert dashboards maar geen beslissingen. Metrics worden bijgehouden zonder dat bevindingen leiden tot aanpassingen in prompts, modellen of processen. De loop is open — gesloten was het criterium.

**Tegenkracht (2026-trend): Production-to-eval loop**
Tools zoals Braintrust maken het mogelijk om productie-traces met één klik om te zetten in regressie-testcases voor de eval-set. Dit creëert een vliegwieleffect waarbij de eval-set automatisch meegroeit met de werkelijkheid in productie — directe mitigatie tegen *eval-set staleness* (anti-pattern 4). (`inferred` — Gemini Deep Research, mei 2026)

---

## 10. Verhouding tot de andere BeeHaive-bouwstenen

De evaluation loop is de overkoepelende bouwsteen die alle andere verbindt:

| Bouwsteen | Rol in de evaluation loop |
|-----------|--------------------------|
| BB_01 Knowledge | Levert eval-criteria: de Knowledge Graph is de ground truth voor wat juiste antwoorden zijn. |
| BB_02 Client Blueprint | Bepaalt succescriteria: welke outputs zijn voor de klant daadwerkelijk waardevol? |
| BB_03 Dynamic Context | Wordt geëvalueerd op grounding: haalt de context de juiste informatie op, in de juiste volgorde? |
| BB_04 Prompt Design | Wordt regression-tested: elke prompt-update triggert automatisch een eval-run. |
| BB_05 Tool Integration | Evalueert tool-call correctness: juiste tool, juiste parameters, juiste volgorde. |
| BB_06 Model Engines | Modelvergelijking via evals: welk model presteert het best op déze use case en eval-criteria? |
| BB_07 Evaluation Loop | Overkoepelt alle andere bouwstenen: de motor die verbetering aantoonbaar maakt. |

---

## 11. Productie-cases met meetbare ROI

Drie publiek gedocumenteerde cases waarbij een evaluation loop tot meetbaar bedrijfsresultaat leidde (`inferred` — Gemini Deep Research, mei 2026):

- **Nippon India Mutual Fund**: AI-assistent nauwkeurigheid van 75% → >90% door overstap van eenvoudige RAG naar continu geëvalueerd systeem. Rapport-generatietijd van 2 dagen naar ~10 minuten.
- **Huron Health**: 90% nauwkeurigheid op sentimentclassificatie via continue evaluatie tegen 10.000 handmatig geannoteerde notities per week.
- **Klarna**: doorlooptijd van pull requests verdubbeld door geautomatiseerde codekwaliteit- en compliance-hooks die direct evalueren in de ontwikkelomgeving.

Gemene deler: de loop sloot pas wanneer evaluatie expliciet gekoppeld werd aan een verbeteractie (RAG-upgrade, judge-kalibratie tegen menselijke labels, dev-time gates) — niet wanneer alleen dashboards werden ingericht.

---

## Open vragen

- **Cohen's Kappa productiedrempel**: geen single primaire AI-bron stelt een specifiek getal als standaard. De 0.717-keuze van BeeHaive is een verdedigbare praktijkkeuze, niet een industrie-standaard.
- **Art. 17 kwaliteitsmanagementsysteem**: niet direct in primaire brontekst gecheckt; beschrijving via zoekresultaten.
- **Exacte bewaartermijnen eval-sets**: niet expliciet in EU AI Act-tekst voor eval-resultaten specifiek; alleen technische documentatie generiek (10 jaar).
- **Instance-specifieke rubrieken in productie**: opkomende trend (OpenAI HealthBench 2025); beperkte productieliteratuur beschikbaar.

---

## Sources

Alle bronnen geraadpleegd op 2026-05-01. Verificatiestatus per claim staat inline (`verified` / `inferred` / `unverified`).

### Primaire definities en methoden

- [1] [Anthropic — Demystifying Evals for AI Agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) — Definitie eval; zeven kernelementen van evaluation harness
- [2] [Anthropic — Building Effective Agents](https://www.anthropic.com/research/building-effective-agents) — Evaluator-optimizer patroon als loop
- [3] [OpenAI — Working with Evals](https://developers.openai.com/api/docs/guides/evals) — Definitie evals; data-flywheel evaluation loop
- [4] [OpenAI — How Evals Drive the Next Chapter of AI](https://openai.com/index/evals-drive-next-chapter-of-ai/) — Evals als methode om verwachtingen te specificeren (`inferred` — 403)
- [5] [AWS Prescriptive Guidance — Evaluation Loops for GenAI](https://docs.aws.amazon.com/prescriptive-guidance/latest/gen-ai-lifecycle-operational-excellence/dev-experimenting-experimentation-loops.html) — 5-componenten model voor evaluation loop
- [6] [Stanford HELM](https://crfm.stanford.edu/helm/latest/) — Evaluation harness definitie; 7 dimensies; 60+ scenario's
- [7] [NIST AI RMF 1.0](https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf) — TEVV als regulier lifecycle-proces
- [8] [Google DeepMind Evals](https://deepmind.google/research/evals/) — Benchmark-georiënteerde aanpak; geen expliciete definitie

### Agentic evaluatie

- [9] [TRAJECT-Bench](https://arxiv.org/abs/2510.04550) — Trajectory evaluation metrics voor agentic tool-gebruik
- [10] [Amazon ML Blog — Evaluating AI Agents](https://aws.amazon.com/blogs/machine-learning/evaluating-ai-agents-real-world-lessons-from-building-agentic-systems-at-amazon/) — Praktijklessen agentic shopping assistant

### Metrics en kalibratie

- [11] [Evidently AI — LLM Evaluation Metrics](https://www.evidentlyai.com/llm-guide/llm-evaluation-metrics) — Taxonomie evaluatiemetrieken
- [12] [ICML 2025 — Data Contamination](https://icml.cc/virtual/2025/poster/43619) — 5-15% accuracy drop bij contaminated evals
- [13] [ACL 2025 — AntiLeakBench](https://aclanthology.org/2025.acl-long.901/) — Geautomatiseerde anti-leakage benchmarking
- [14] [arxiv — Judge's Verdict: Comprehensive Analysis](https://arxiv.org/pdf/2510.09738) — Lengte-, positie- en zelf-bias in LLM-judges
- [15] [LangChain AgentEvals](https://github.com/langchain-ai/agentevals) — Trajectory match evaluators

### Deployment patronen

- [16] [TianPan — LLM Gradual Rollout: Shadow, Canary, A/B](https://tianpan.co/blog/2026-04-09-llm-gradual-rollout-shadow-canary-ab-testing) — Shadow mode en canary release patronen

### Governance en compliance

- [17] [EU AI Act Art. 9 — Risk Management System](https://artificialintelligenceact.eu/article/9/) — Continuous iterative lifecycle process; prior defined metrics
- [18] [EU AI Act Art. 10 — Data and Data Governance](https://artificialintelligenceact.eu/article/10/) — Bias-detectie en representatieve datasets
- [19] [EU AI Act Art. 15 — Accuracy, Robustness and Cybersecurity](https://artificialintelligenceact.eu/article/15/) — Feedback loop-contaminatie voorkomen
- [20] [EU AI Act Art. 72 — Post-Market Monitoring](https://artificialintelligenceact.eu/article/72/) — Post-marktmonitoring; inwerkingtredingsdatum 2 aug 2026
- [21] [Cloud Security Alliance — ISO 42001 Audit Lessons](https://cloudsecurityalliance.org/blog/2025/05/08/iso-42001-lessons-learned-from-auditing-and-implementing-the-framework) — Clause 9; jaarlijkse audit
- [22] [AWS — ISO/IEC 42001 Lifecycle Risk Management](https://aws.amazon.com/blogs/security/ai-lifecycle-risk-management-iso-iec-420012023-for-ai-governance/) — ISO 42001 als complement EU AI Act
- [23] [Autoriteit Persoonsgegevens — AP en RDI Supervisie](https://www.autoriteitpersoonsgegevens.nl/en/current/ap-and-rdi-supervision-of-ai-systems-requires-cooperation-and-must-be-arranged-quickly) — Nederlandse AI-toezichtstructuur
- [24] [Pinsent Masons — 10 Dutch Regulators](https://www.pinsentmasons.com/out-law/news/ai-compliance-overseen-10-dutch-regulators) — Tien toezichthouders NL

### Tools en platforms

- [25] [Goodeye Labs — Top AI Eval Tools 2026](https://www.goodeyelabs.com/articles/top-ai-agent-evaluation-tools-2026) — Vergelijking 7 platforms; pricing
- [26] [Braintrust — Best LLM Evaluation Platforms 2025](https://www.braintrust.dev/articles/best-llm-evaluation-platforms-2025) — Platform-vergelijking (`self-reported`)
- [27] [Arize Phoenix Documentation](https://arize.com/docs/phoenix) — Features; versie 3.0.0; OpenTelemetry
- [28] [Inspect AI — UK AISI](https://inspect.aisi.org.uk/) — Sandboxed agentic evals; auditeerbaar
- [29] [GitHub — deepeval](https://github.com/confident-ai/deepeval) — 50+ metrics; Pytest-integratie

### Anti-patronen

- [30] [Collinear AI — Goodhart's Law in AI Leaderboards](https://blog.collinear.ai/p/gaming-the-system-goodharts-law-exemplified-in-ai-leaderboard-controversy) — Goodhart's Law; selectieve score-publicatie

### Kerncitaten

- Anthropic: *"An evaluation (or 'eval') is a test for an AI system: give an AI an input, then apply grading logic to its output to measure success."* — [1]
- OpenAI: *"Evals make fuzzy goals and abstract ideas specific and explicit."* — [4]
- AWS: *"This loop is the engine room where ideas are tested, prompts are refined, and quality is measured."* — [5]
- NIST: *"As a regular process within an AI lifecycle, TEVV allows for both mid-course remediation and post-hoc risk management."* — [7]
- EU AI Act Art. 9: *"continuous iterative process planned and run throughout the entire lifecycle."* — [17]
- Goodhart's Law: *"When a measure becomes a target, it ceases to be a good measure."* — [30]
