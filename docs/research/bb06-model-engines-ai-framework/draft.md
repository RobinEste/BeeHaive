# BB_06 Model Engines — Onderzoeksrapport (draft)

**Onderwerp:** Model Engines als zesde bouwsteen van BeeHaive AI-framework
**Datum:** 2026-04-27
**Researcher-rondes:** 1 (parallel, 5 dimensies)

---

## Executive Summary

AI-modellen zijn de denk- en rekenkern van elke AI-oplossing — maar welk model je kiest, is een ontwerp-beslissing met verstrekkende gevolgen voor kosten, kwaliteit, latency, privacy en compliance. Het overheersende anti-patroon in 2026 is de reflex om overal het grootste, nieuwste frontier-LLM in te zetten. Dat is duurder, trager en minder verklaarbaar dan nodig — en het werkt niet voor de meerderheid van enterprise-taken.

Het modeltype-landschap is in 2026 uitgebreider dan ooit: naast algemene LLMs en reasoning-modellen zijn multimodale modellen, world models (voor robotica en simulatie), diffusiemodellen, embedding-modellen en klassieke ML-algoritmen allemaal legitieme architectuurcomponenten. De kern van goede model-engineering is dezelfde als de kern van goede software-engineering: kies het gereedschap dat past bij de taak — niet het meest indrukwekkende gereedschap in de kast.

De frontier-markt is ingrijpend veranderd. Claude Opus 4.7, GPT-5.4 en Gemini 3.1 Pro convergeren op redeneer-benchmarks tot op 0,2 procentpunt verschil. De werkelijke differentiatie zit in specifieke taakdomeinen (coding/agents voor Claude, webonderzoek voor GPT-5.4, kostprijs voor Gemini), prijsstelling (1.250x range van DeepSeek V3.2 op $0,14 tot GPT-5.4 Pro op $30/MTok input), EU-beschikbaarheid en governance. Multi-model routing — waarbij verzoeken worden verdeeld over goedkope en dure modellen naar complexiteit — reduceert kosten met 60–83% bij minimaal kwaliteitsverlies.

EU-data-soevereiniteit vereist meer dan een EU-regio kiezen: de US CLOUD Act maakt alle US-bedrijven kwetsbaar, ongeacht datacenter-locatie. Mistral is de enige frontier-provider met categoriale CLOUD-Act-immuniteit.

---

## 1. Modeltype-keuze als ontwerpvraag

### Het anti-patroon: één model voor alles

"Het grootste LLM overal" is een anti-patroon om drie redenen [research-modelkeuze, bron 1–6]:

1. **Kostenverschil**: een frontier-LLM kost $0,01–$0,50 per aanroep; klassiek ML $0,001–$0,01; regels nagenoeg nul. Bij 100.000 aanroepen per maand is het verschil €900–€45.000 per maand op dezelfde taak.
2. **Latency**: klassiek ML (10–100 ms) is 5–50x sneller dan een LLM (200 ms–5 s) bij gesloten, gestructureerde taken.
3. **Verklaarheid/auditabiliteit**: voor gereguleerde omgevingen (financiën, zorg, overheid) zijn classifiers en regressiemodellen statistisch valideerbaar; LLMs zijn juridisch nauwelijks auditeerbaar.

### Vier beslisfactoren

Elke model-selectie draait om vier factoren [bron 1, 2]:
1. **Taakcomplexiteit** — open-ended of gesloten/gedetermineerd?
2. **Kosten** — wat is de tolerabele prijs per aanroep bij het verwachte volume?
3. **Latency** — realtime (<200 ms) of asynchroon (seconden/minuten)?
4. **Privacy / data-residentie** — wat mag de data verlaten, en naar welk jurisdictiegebied?

### Diagnostische vragen: "Is dit een LLM-probleem?"

Gebruik deze vragen als filter voordat je een LLM kiest:

1. Is de uitvoer een gestructureerd getal of label? → probeer eerst klassiek ML of regels
2. Heb ik 1.000+ gelabelde voorbeelden? → klassiek ML is serieuze kandidaat
3. Moet het resultaat statistisch verklaarbaar zijn voor een auditor? → klassiek ML of regels
4. Is latency <100 ms een harde grens? → klassiek ML of gespecialiseerd model
5. Gaat het om tabellaire, historische data? → XGBoost/LightGBM eerst proberen
6. Is de taak open-ended, ongestructureerd, of bevat ze ambiguïteit? → LLM is geschikt
7. Is er onvoldoende gelabelde data voor een klassiek model? → LLM of few-shot

### De aanbevolen progressie

1. Begin met prompt engineering op een generalistisch model
2. Voeg RAG toe als kenniscontext ontbreekt
3. Gebruik fine-tuning alleen als laatste stap — vereist ≥1.000 kwaliteitsvoorbeelden en een meetbaar evaluatiecriterium [bron 3]
4. Fine-tuning zonder evaluatiepijplijn is "schieten in het donker"

---

## 2. Het modeltype-landschap in 2026

### 2.1 Algemene LLMs en reasoning-modellen

**Algemene LLMs** zijn getraind op brede tekstcorpora en kunnen uiteenlopende taalkundige taken aan zonder expliciete trainingsinstructies per taak. Ze zijn het juiste gereedschap voor: vrije-tekst-generatie, samenvatting, vraagbeantwoording, code-generatie, documentanalyse en conversatie.

**Reasoning-modellen** (extended thinking): Claude Opus 4.7 met extended thinking, OpenAI o3/o3-mini, GPT-5.4 met "thinking-mode". Ze reserveren rekentijd voor expliciete redenering voor ze een antwoord geven. Sterk bij: wiskundige bewijzen, multi-stap-planning, wiskundecompetities, complexe code-architectuur. Nadeel: significant hogere latency en kosten (o3 Pro: $150/MTok input). Gebruik alleen als de kwaliteitsverbetering meetbaar en gerechtvaardigd is.

### 2.2 Multimodale en vision-language-modellen

Verwerken tekst, beeld (en soms audio/video) in één model. Voorbeelden: Claude Sonnet 4.6 (tekst + beeld), Gemini 3.1 Pro (tekst + beeld + video native), GPT-5.4 (tekst + beeld).

Toepassingen: document-begrip (PDFs met grafieken), productafbeeldingsanalyse, formulierverwerking, medische beeldherkenning, kwaliteitscontrole in productieprocessen.

**Wanneer wel**: input is inherent visueel; tekst-only beschrijving verliest te veel informatie.
**Wanneer niet**: voor zuivere teksttaken — ze zijn duurder dan tekst-only modellen.

### 2.3 World models — opkomend voor robotica en simulatie

World models modelleren hoe de wereld reageert op acties. Ze zijn relevant voor enterprise-organisaties die werken met robotica, autonome systemen of simulatie.

**Meta V-JEPA 2** (juni 2025) [primaire bron: ai.meta.com/vjepa]:
- 1,2 miljard parameters; getraind op 1M+ uur video
- Zero-shot robotbesturing in nieuwe omgevingen na slechts 62 uur unlabeled robotdata
- MIT-licentie, open-source
- Toepassingen: robotica, autonome navigatie, fysieke AI-agents

**Google DeepMind Genie 3** (augustus 2025) [primaire bron: deepmind.google]:
- Eerste real-time interactief world model met fysisch accurate 3D-omgevingen
- Toepassingen: training van agents, simulatie-omgevingen, educatie, gaming

**NVIDIA Cosmos** (CES 2025, primaire bron: nvidia.com/en-gb/ai/cosmos):
- Drie modelcategorieën: Predict (toestand-simulatie), Transfer (sim-to-real overdracht), Reason (fysica-bewust redeneren)
- 2 miljoen downloads; enterprise-adoptie bij 1X, Agility Robotics, Figure AI (humanoid robotics), Uber, XPENG (autonome voertuigen)
- Getraind op 9.000 biljoen tokens uit 20 miljoen uur real-world data
- Toepassingen: synthetische trainingsdata genereren, gevaarlijke/zeldzame scenario's simuleren, industriële productie-optimalisatie

**Voor de meeste Nederlandse organisaties in 2026**: world models zijn nog niet operationeel relevant buiten robotica, autonome voertuigen en specifieke industriële simulatiecontexten. Oriënteer; volg de ontwikkeling; wacht met inzetten.

### 2.4 Diffusiemodellen voor beeld en video

Stable Diffusion 3, DALL-E 3, Midjourney v7 (beeld); Sora (OpenAI), Veo 3 (Google DeepMind), Runway Gen-3 (video).

Toepassingen: marketingvisualisaties, productafbeeldingen, prototyping van UI-designs, video-content productie.

**Wanneer wel**: creatieve visuele productie is kernbehoefte; volume is te hoog voor menselijke designers.
**Wanneer niet**: juridische en financiële documenten; sterk-gereguleerde sectoren waar visuele outputs auditeerbaar moeten zijn.

### 2.5 Embedding-modellen

Zetten tekst om naar numerieke vectoren voor semantische vergelijking. Onmisbaar voor: RAG (Retrieval-Augmented Generation), semantisch zoeken, clustering, anomaliedetectie.

Voorbeelden: text-embedding-3-large (OpenAI), Voyage-3 (Anthropic), Gemini Text Embedding.

Kosten: significant lager dan generatieve LLMs — typisch $0,0001–$0,002/MTok.

**Wanneer**: altijd als je RAG gebruikt; voor document-retrieval, kennisgraaf-populatie, semantische deduplicatie.

### 2.6 Klassieke en gespecialiseerde ML-modellen

XGBoost, LightGBM, Random Forest, BERT-classifiers, ARIMA/Prophet voor tijdreeksen.

**Wanneer superieur aan LLMs** [bron 4, 5]:
- Tabellaire gestructureerde data (churn, fraude, voorraadbeheer, kredietscores)
- Tijdreeksen met duidelijke patronen (energieverbruik, productieforecast, sensordata)
- Hoge-volume classificatie (content-moderatie, transactie-labeling) — 100x goedkoper per aanroep
- Gereguleerde omgevingen waar statistisch valideren verplicht is
- Latency-kritische toepassingen (<100 ms)

**Kernregel**: als je een gestructureerd getal of label wilt voorspellen op basis van historische data, begin dan bij XGBoost — niet bij een LLM.

---

## 3. Frontier-landschap april 2026

### 3.1 Prijsoverzicht

*Alle prijzen per miljoen tokens input/output, tenzij anders vermeld. Bronnen: APIScout, jangwook.net, fungies.io — geverifieerd april 2026.*

**Anthropic Claude:**

| Model | Input $/MTok | Output $/MTok | Context |
|-------|-------------|--------------|---------|
| Claude Opus 4.7 | $5,00 | $25,00 | 1M tokens |
| Claude Sonnet 4.6 | $3,00 | $15,00 | 1M tokens |
| Claude Haiku 4.5 | $0,25 | $1,25 | 200K tokens |

**OpenAI GPT-5-familie:**

| Model | Input $/MTok | Output $/MTok | Context |
|-------|-------------|--------------|---------|
| GPT-5.4 | $2,50 | $15,00 | 400K–1M tokens |
| GPT-5.4 Pro | $30,00 | $180,00 | 1M tokens |
| GPT-5 Mini | $0,25 | $2,00 | 500K tokens |
| GPT-5 Nano | $0,05 | $0,40 | 128K tokens |
| O3 Pro | $150,00 | — | 128K |

**Google Gemini:**

| Model | Input $/MTok | Output $/MTok | Context |
|-------|-------------|--------------|---------|
| Gemini 3.1 Pro (≤200K) | $2,00 | $12,00 | 2M tokens |
| Gemini 3.1 Pro (>200K) | $4,00 | $18,00 | 2M tokens |
| Gemini 2.5 Flash | $0,15 | $0,60 | 1M tokens |
| Gemini 2.5 Flash-Lite | $0,10 | $0,40 | 1M tokens |

**Meta Llama 4 (open-source):**

| Model | Via API $/MTok input | Context |
|-------|---------------------|---------|
| Llama 4 Scout | $0,11–$0,25 | 328K–10M tokens |
| Llama 4 Maverick | $0,15–$0,35 | 1M tokens |

**Mistral (EU-nativo):**

| Model | Input $/MTok | Output $/MTok |
|-------|-------------|--------------|
| Mistral Large 3 | ~$1,00–$2,00 | ~$3,00 |
| Mistral Small 3.2 | $0,06 | $0,18 |
| Mistral Nemo | $0,02 | $0,04 |

**DeepSeek:**

| Model | Input $/MTok | Output $/MTok |
|-------|-------------|--------------|
| DeepSeek V3.2 | $0,14–$0,28 | $0,28–$0,42 |
| DeepSeek R1 | $0,55 | $2,19 |

Het prijsverschil tussen duurste en goedkoopste: 1.250x (DeepSeek V3.2 $0,14 vs GPT-5.4 Pro $30 per MTok input). [bron aisecuritygateway]

### 3.2 Benchmark-vergelijking: geen universele winnaar

Convergentie op benchmark-niveau: Claude Opus 4.7, GPT-5.4 en Gemini 3.1 Pro liggen op GPQA Diamond (graduate-level redeneren) binnen 0,2 procentpunt van elkaar (~94%). De werkelijke differentiatie is taak-specifiek:

| Taaktype | Beste model | Score/maatstaf |
|----------|------------|----------------|
| Productie-code / SWE-bench Pro | Claude Opus 4.7 | 64,3% |
| Tool-zware agents / MCP | Claude Opus 4.7 | 77,3% MCP-Atlas |
| Desktop-automatisering | Claude Opus 4.7 | 78,0% OSWorld |
| Webonderzoek / BrowseComp | GPT-5.4 | 89,3% (+10 punten) |
| Kostenefficiënte doorvoer | Gemini 3.1 Pro | $2/$12 per MTok |
| Meertalige kennis | Gemini 3.1 Pro | 92,6% MMMLU |
| Budget-redeneren | DeepSeek R1 | 97,3% MATH-500 bij 90% lagere kosten |

[bron: SpectrumAILab vergelijking april 2026]

**Spanningsanalyse**: Anthropic promoot Claude Opus 4.7 als superior op coding en agents; OpenAI benadrukt GPT-5.4's webonderzoek en ecosystem-breedte; Google Gemini benadrukt kostprijs en context-window. Alle drie zijn correct voor hun eigen sterkste dimensie — maar geen enkele claim geldt universeel.

### 3.3 Praktijkverschillen vs benchmarks

Benchmarks (MMLU, HumanEval) correleren zwak met bedrijfsprestaties. Het enige zinvolle kwaliteitstest is een private evaluatie op 50–200 eigen representatieve voorbeelden [bron core.cz, llmgateway.io]. Specifieke discrepanties:
- GPT-5.4 overtreft benchmarks op webonderzoek (BrowseComp +10 punten vs naaste concurrent)
- Claude Opus 4.7 domineert agentic coding terwijl andere reasoning-metrics nagenoeg gelijk zijn
- DeepSeek R1 haalt 97,3% op MATH-500 bij 90% lagere prijs — maar trainingsdata-transparantie is beperkter dan westerse providers

### 3.4 Tierindeling als architectuurkader

| Tier | Modellen | Gebruik | % van aanroepen |
|------|---------|---------|-----------------|
| Frontier | Claude Opus 4.7, GPT-5.4 | Complexe redenering, agentic workflows | ~5% |
| Pro | Sonnet 4.6, GPT-5 | Dagelijks professioneel werk, code | ~35% |
| Standaard | Haiku 4.5, Gemini 2.5 Flash | Balanced speed/quality | ~30% |
| Budget | GPT-5 Nano, DeepSeek V3.2 | Classificatie, hoog volume | ~30% |
| Lokaal | Llama 4, Mistral Large 3 self-hosted | Privacy, offline, onbeperkt | Situationeel |

---

## 4. Routing- en hybride strategieën

### 4.1 De vier routing-patronen

**Direct routing** (intent-based):
- Classificeer inkomende aanvraag (<50 ms) en route naar juiste model-tier
- Vereist accurate classifier; werkt goed bij duidelijk onderscheid tussen categorieën
- Infrastructuur: LiteLLM (open-source), OpenRouter, Martian, Not Diamond

**Cascading** (sequentieel-escalerend):
- Stuur eerst naar goedkoopste model; escaleer alleen als kwaliteitsdrempel niet gehaald
- Voordeel: geen upfront classifier; werkt op confidence-signaal
- Nadeel: latency-taks bij escalatie (drie aanroepen in een drie-tier cascade)

**Cascade routing** (gecombineerd):
- Route voor duidelijke gevallen; cascade voor ambigueuze middenlaag
- Theoretisch optimaler dan zuivere routing of cascading [ETH Zurich, 2024/2025]
- Praktisch beste keuze bij gemengde werklast

**Ensemble/voting**:
- Stuur naar meerdere modellen; combineer via voting of fusie
- Gebruik oneven aantal modellen (3 of 5) om gelijkspel te vermijden
- Alleen rechtvaardigen bij hoge-inzet-beslissingen (kosten 3x of meer per aanroep)

### 4.2 Kostenimpact

Multi-model routing reduceert LLM-kosten met 60–83% bij minimaal kwaliteitsverlies, bevestigd door meerdere praktijkbronnen [bron routing-research]. Een representatief voorbeeld: 76% van inference-aanroepen hoeft een frontier-model niet te raken.

Praktijkcalculatie: na semantische caching + routing + prompt-compressie daalt een maandrekening van €3.730 naar ~€230 (94% reductie) — dit is een specifiek casusrapport en contextueel.

### 4.3 Anthropic's aanbeveling: start simpel

Anthropic's "Building Effective Agents" (december 2024): begin met de eenvoudigste workflow die werkt. Voeg orchestratie en routing toe alleen als bewijs bestaat dat het nodig is.

In multi-agent-architecturen: Opus voor orchestrators (planners, synthesizers); Sonnet voor parallel uitvoerende workers; Haiku voor informatieverzamelaars (5–10 parallel).

### 4.4 Wanneer multi-model-architectuur niet de moeite waard is

Multi-model-routing voegt complexiteit toe die gerechtvaardigd moet worden:
- Kleine volumes: routing-infrastructuur-overhead > besparingen
- Homogene werklast: alle aanvragen vergelijkbaar complex
- Gebrek aan monitoring: zonder observability zie je niet of routing goed werkt
- Latency-kritisch: cascading kan latency verergeren bij drie-tier escalatie

---

## 5. EU-data-residentie en soevereiniteit

### 5.1 CLOUD Act — de juridische kern

De US CLOUD Act machtigt US-autoriteiten om data op te eisen bij US-bedrijven, ook wanneer die data op EU-servers staat. Dit maakt "EU-regio kiezen" onvoldoende voor werkelijke data-soevereiniteit bij US-providers [bron devto, Julien Simon]. `verified`

Alle grote cloud-AI-providers — AWS Bedrock, Azure OpenAI, Google Vertex AI, plus API-providers Anthropic en OpenAI — zijn US-bedrijven en vallen onder de CLOUD Act.

### 5.2 Providers naar EU-soevereiniteitspositie

| Provider | HQ | CLOUD Act | EU-regio beschikbaar | Beste voor |
|----------|-----|-----------|---------------------|-----------|
| Mistral AI | Parijs, FR | Nee (EU-bedrijf) | Standaard (Paris) | Strengste compliance |
| Anthropic | San Francisco | Ja | Via AWS EU-regio's | Enterprise met EU-SCC |
| OpenAI | San Francisco | Ja | Enterprise (IE, DE, NL) | Enterprise met DPA |
| Google | Mountain View | Ja | Vertex AI EU-boundary | Configureerbaar sterkste |
| Meta Llama 4 self-hosted | — | Niet van toepassing | Eigen infra | Volledige controle |

**Mistral-caveat**: Mistral heeft US-investeerders (a16z, Salesforce Ventures). CLOUD Act-blootstelling via investeerdersrelaties is juridisch ongetest [Julien Simon, 2026]. `unverified`

### 5.3 AWS European Sovereign Cloud

AWS lanceerde in 2025 de European Sovereign Cloud met directe Amazon Bedrock-toegang (Anthropic, Meta, Mistral, Amazon-modellen). Haalt niet het niveau van SecNumCloud (hoogste Franse overheidsnorm). Praktische keuze voor organisaties die Bedrock willen maar EU-data-residency nodig hebben.

### 5.4 Lokale inference — volledige controle

| Tool | Type | Gebruik |
|------|------|---------|
| Ollama | Lokale runtime | Eenvoudige installatie, breed model-support |
| vLLM | Production serving | Hoge doorvoer, continuous batching |
| TGI (HuggingFace) | Production serving | Geoptimaliseerd voor HF-modellen |
| llama.cpp | CPU + GPU | Low-hardware-requirement, Llama 4 Scout op M4 Mac |

Kwaliteits- en feature-beperkingen "EU-only":
1. Mistral Large 3 benadert maar overtreft niet consistent Claude Opus 4.7/GPT-5.4 op alle taken
2. Agentic tooling (MCP, computer-use) is minder ver bij EU-native providers
3. Real-time updates en RLHF zijn minder mature bij self-hosted opties
4. Mistral Large 3 kost ~70% minder dan GPT-5.4 op vergelijkbare tiers — dit compenseert deels de kwaliteitskloof

### 5.5 EU AI Act — modellaag-verplichtingen

GPAI-model-providers (artikel 53 EU AI Act, van kracht aug. 2025/2026):
- Technische documentatie verplicht
- Trainingsdata-samenvatting en copyright-compliance
- Voor modellen met "systemisch risico" (art. 55): veiligheidsevaluaties

Voor Nederlandse AI-consultants: werk met providers die GPAI-conformiteitsdocumentatie kunnen aanleveren. Mistral publiceert compliance-templates en audittrail-tooling specifiek voor EU AI Act.

DORA (financiële sector) en EHDS (gezondheidszorg) kennen aanvullende data-lokalisatieverplichtingen die API-gebruik bij US-providers in principe uitsluiten voor kritieke systemen.

---

## 6. Kostenoptimalisatie

### 6.1 Vijf hefbomen in volgorde van impact

| Hefboom | Besparing | Implementatietijd |
|---------|-----------|------------------|
| Model right-sizing | 60–80% | 1–2 weken |
| Prompt caching | 50–90% op input | 1–3 dagen |
| Batch-API migratie | 50% op batch-workloads | 1–2 weken |
| Prompt-lengte trimmen | 20–40% op input | 1–2 weken |
| Open-source migratie | 50–90% bij schaal | 4–12 weken |

### 6.2 Prompt caching — concrete cijfers

Gecachede input-kortingen bij grote providers:
- Anthropic Sonnet 4.6: van $3,00 naar $0,30/MTok (90% korting)
- Gemini 2.5 Pro: van $1,25 naar $0,31/MTok (75% korting)
- GPT-5.4: van $2,50 naar $1,25/MTok (50% korting)

Vereiste: stabiele, herhalende prefix. Als >20% van input-tokens identiek is over aanroepen: caching levert significante besparing.

Bij lokale modellen (Ollama, vLLM, llama.cpp): API-prompt-caching bestaat niet — eigen implementatie vereist (hash context, sla embeddings op).

### 6.3 Kwantisatie (self-hosted)

| Techniek | Geheugenreductie | Snelheidswinst | Kwaliteitsverlies |
|----------|-----------------|----------------|------------------|
| INT8 | 50% | 1,5–2x | <1% |
| INT4 (AWQ) | 75% | 2–3x | 1–3% |
| Kennisd. distillatie | 40–60% | 2–3x | 2–5% |

Kritisch: INT8 versnelt alleen bij native-support (TensorRT, ONNX Runtime, llama.cpp). Standaard PyTorch draait INT8 als FP32 — is dan puur overhead.

### 6.4 Distillatie

Een 70B model destilleren naar een 7B model voor een specifieke taak:
- Kostenreductie: 90% bij inferentie
- Kwaliteitsbehoud: 90–95% voor de specifieke taak
- Vereiste: ≥duizenden kwaliteits-outputs als trainingsdata + ML-infrastructuur
- DistilBERT-precedent: 40% kleiner dan BERT, 97% van prestaties behouden

### 6.5 Wanneer is zelf-hosten goedkoper dan API?

Break-even afhankelijk van volume en hardware, maar als vuistregel: boven ~500K–1M tokens/dag verschuift de schaal richting self-hosting voor niet-frontier-modellen. Hardware-investering: $15.000–$50.000 voor een on-premise Llama 4-deployment, versus cloud-API-kosten die $10.000–$30.000/maand kunnen bereiken bij intensief gebruik.

---

## 7. Operationele runtime

### 7.1 Latency-budgetten

- **>30 tokens/seconde streaming**: voelt instant voor de eindgebruiker
- **Time to first token (TTFT) <200 ms**: target voor interactieve toepassingen
- **P95 <10 seconden**: alert-drempel voor asynchrone LLM-aanroepen
- **P99 als primaire SLA-maatstaf**: p50 en p95 verbergen staart-latency die gebruikers écht ervaren

### 7.2 Versie-pinning vs auto-upgrade

| Aanpak | Voordeel | Risico |
|--------|----------|--------|
| Versie-pinning | Voorspelbaar gedrag; eenvoudiger compliance | Mist beveiligingspatches en verbeteringen |
| Auto-upgrade | Altijd recente kwaliteit | Stille gedragswijziging breekt downstream-logica |

Aanbeveling: pin op major versie in productie; test upgrades in staging met eval-suite voordat je uitrolt.

### 7.3 Fallback-patronen

Bij model-uitval, rate-limiting of degradatie:
- Primaire provider → fallback provider (Anthropic → OpenAI of omgekeerd)
- Stap-down naar kleiner model in dezelfde familie (Opus → Sonnet → Haiku)
- Circuit-breaker: stop escalatie naar dure fallback als foutpercentage te hoog is
- Monitor `fallback_activation_rate` — stijging signaleert upstream incident

### 7.4 Observability — vijf pijlers

LLM-observability gaat verder dan traditionele APM: een HTTP 200 kan een hallucinatoire respons bevatten. Je hebt kwaliteitsmetrieken nodig naast infrastructuurmetrieken.

**Minimale metriekenset:**

| Categorie | Metriek | Reden |
|-----------|---------|-------|
| Latency | TTFT, totale generatietijd, P50/P95/P99 | Gebruikerservaring en bottleneck-identificatie |
| Kosten | Tokens per aanroep (input + output), kosten per aanroep per model | Budget-bewaking en anomaliedetectie |
| Kwaliteit | LLM-as-judge score (steekproef 5–15%), guardrail-trigger-rate | Regressies detecteren |
| Betrouwbaarheid | Error-rate per type, retry-rate, fallback-activatie-rate | Provideringsstabiliteit |
| Drift | 7-daagse trend antwoordlengte, 30-daagse refusal-trend, embedding-verdriftdetectie | Stille degradatie signaleren |

**Vier incident-correlaties die 80% van LLM-incidenten dekken:**
1. Latency stijgt + grounding-score daalt → retrieval-degradatie
2. Latency stabiel + hallucinatie stijgt → prompt- of modelwijziging
3. Escalatierate stijgt + kosten stijgen → classifier drift
4. Provider-foutrate stijgt + fallback-rate stijgt → upstream incident

**Alert-drempels:**
- Dagbudget overschreden: directe alert
- Error-rate >1–5%: on-call notificatie
- P95 latency >10 seconden: Slack-notificatie
- Kwaliteitsscore onder drempel: Slack-notificatie
- Kostenspike: kan prompt-injection of runaway agent-loop signaleren

---

## 8. Risico's en beperkingen op model-niveau

### 8.1 Knowledge cutoffs

LLMs hebben een trainingsdatum; informatie na die datum ontbreekt. Mitigaties:
- RAG met up-to-date kennisbronnen voor feitelijke taken
- Expliciete datum-context meegeven in system-prompt
- Reasoning-modellen zonder externe tools zijn niet geschikt voor actuele informatiebehoeften

### 8.2 Hallucinatie-profielen

| Modeltype | Hallucinatie-risico | Mitigatie |
|-----------|--------------------|-----------| 
| Grote LLMs | Matig-hoog voor feitelijke claims | RAG, grounding-checks, citations |
| Reasoning-modellen | Lager voor redeneer-taken; risico bij feitenkennis blijft | RAG bij feitenafhankelijke taken |
| World models | Fysische fouten (verkeerde fysica in simulatie) | Verificatie in echte omgeving; niet productie-ready zonder validatie |
| Klassiek ML | Geen taal-hallucinatie; kan wel out-of-distribution falen | Drift-monitoring, feature-validatie |

### 8.3 OWASP LLM Top-10 — model-laag

**LLM03:2025 — Supply Chain:**
- Kwetsbaarheden via: manipuleerde pre-trained modellen, vergiftigde datasets, kwetsbare bibliotheken, MCP-tools
- Open-source modellen van HuggingFace kunnen backdoors bevatten via malicious pickling bij modelladen
- Mitigaties: checksums/hashes voor model-integriteit; vendor acceptance testing; ModelAudit voor statische scan; gedetailleerde logging van alle trainingswijzigingen

**LLM04:2025 — Data and Model Poisoning:**
- Pre-training, fine-tuning of embedding-data gemanipuleerd → backdoors, biases
- Backdoors kunnen slapend zijn: model gedraagt zich normaal totdat een trigger actief is
- Mitigatie: bias-detectietests, consistentietests over grote prompts, red-teaming

**LLM07:2025 — System Prompt Leakage:**
- Confidentiële system-prompt kan via aanvallen of model-gedrag lekken
- Behandel system-prompt als non-secret; beperk gevoelige informatie erin

### 8.4 Model-cards en AI Bill of Materials

- **Model-cards**: beschrijven prestaties, beperkingen, trainingsdata, intended use — governance-instrument voor audittrails
- **AI-BOM (Bill of Materials)**: modelcomponenten documenteren vergelijkbaar met software-BOM — verplicht onder EU AI Act art. 13 voor hoog-risico systemen
- Trainingsdata-transparantie: Meta (Llama 4) en Mistral zijn relatief open; OpenAI/Anthropic/Google zijn geslotener
- DeepSeek: sterke prestaties, maar Chinese herkomst en beperkte trainingsdata-transparantie is een risicofactor voor Nederlandse overheids- en defensie-organisaties

---

## Tegenstrijdigheden en open vragen

**Tegenstrijdigheid 1: EU-soevereiniteit van Mistral**
Mistral wordt gepresenteerd als categorisch veilig voor CLOUD Act. Maar Mistral heeft US-investeerders (a16z, Salesforce Ventures), wat potentiële CLOUD Act-blootstelling via investeerdersrelaties creëert. Dit is juridisch ongetest [Julien Simon, 2026]. Nederlandse juridische afdeling moet dit beoordelen bij hoog-gevoelige toepassingen.

**Tegenstrijdigheid 2: kostenbesparingspercentages**
Claims van 60–94% kostenreductie via routing en caching zijn overwegend zelfgerapporteerd door blog-auteurs. Ze zijn plausibel maar sterk context-afhankelijk. Behandel als ordegrootte, niet als garantie.

**Tegenstrijdigheid 3: benchmarks vs praktijk**
Alle frontier-aanbieders betwisten elkaars benchmarks. De enige betrouwbare maatstaf is een private evaluatie op eigen data en taken. Benchmarks zijn indicatief voor het selecteren van kandidaat-modellen; niet voor het nemen van de definitieve keuze.

**Open vraag**: DeepSeek-modellen bieden indrukwekkende prijs-kwaliteit maar Chinese herkomst en beperkte transparantie. Welke organisaties in de NL-publieke of financiële sector kunnen of mogen ze inzetten? Vereist rechtsgutachten.

**Open vraag**: World models zijn voor de meeste NL-organisaties nog niet operationeel relevant. Wanneer wordt de drempel bereikt dat Genie 3 of Cosmos enterprise-inzetbaar is buiten robotica? Verwachte horizon: 2027–2028 voor bredere toepassingen. `inferred`

---

## Synthese: 7 ontwerpregels voor de Nederlandse AI-consultant

1. **Kies op taak, niet op trend.** De eerste vraag is niet "welk model?", maar "is dit een LLM-probleem, een klassiek-ML-probleem, of een dashboard-probleem?" Stel de diagnostische vragen voordat je een model kiest.

2. **Vertrouw geen enkele benchmark.** Evalueer modellen altijd op 50–200 eigen representatieve voorbeelden. Benchmarks zijn voor het selecteren van kandidaten, niet voor de definitieve keuze.

3. **Bouw model-agnostisch.** Models veranderen elke drie maanden. Een goede evaluatiepijplijn vertelt je wanneer het tijd is om te wisselen — en model-agnostische architectuur maakt die wissel een kwestie van uren, niet maanden.

4. **Tier je stack.** Gebruik frontier-modellen voor ~5% van aanroepen (harde redenering, agents); mid-tier voor het dagelijkse werk; budget- en lokale modellen voor hoge-volume eenvoudige taken. Een multi-tier aanpak reduceert kosten met 60–80% bij gelijkblijvende kwaliteit.

5. **Cachen voor je iets anders optimaliseert.** Prompt caching is de snelste en eenvoudigste kostenoptimalisatie (50–90% op input in 1–3 dagen). Doe dit eerst.

6. **EU-data-soevereiniteit vereist juridische helderheid.** CLOUD Act maakt EU-regio's van US-providers onvoldoende voor echte soevereiniteit. Voor gevoelige data: Mistral (direct of via EU-cloud), open-weight zelf-hosten, of een juridisch beoordeeld cloud-soevereiniteitskader. Geef dit helder terug aan de opdrachtgever.

7. **Observeer kwaliteit, niet alleen uptime.** Een HTTP 200 kan een hallucinatie zijn. Voer kwaliteitsmetrieken in (LLM-as-judge steekproef 5–15%), stel kwaliteitsalerts in, en correleer latency-, kosten- en kwaliteitssignalen om incidenten te diagnosticeren.

---

## Sources (draft — ter verificatie)

1. LLM Gateway — How to Choose the Right LLM 2026 — https://llmgateway.io/blog/how-to-choose-the-right-llm
2. NovaKit — Choosing the Right AI Model: Decision Framework 2026 — https://www.novakit.ai/blog/choosing-right-ai-model
3. core.cz — Enterprise AI Model Selection 2026 — https://core.cz/en/blog/2026/ai-model-selection-enterprise-2026/
4. IdeaPlan — LLM vs Traditional ML vs Rules — https://www.ideaplan.io/compare/llm-vs-traditional-ml-vs-rules
5. phptrends — Practical AI Decision Guide — https://phptrends.com/choosing-the-right-approach-to-artificial-intelligence-a-practical-decision-guide/
6. APIScout — LLM API Pricing 2026 — https://apiscout.dev/blog/llm-api-pricing-comparison-2026
7. SpectrumAILab — GPT-5.4 vs Opus 4.7 vs Gemini 3.1 Pro — https://spectrumailab.com/blog/gpt-5-4-vs-claude-opus-4-7-vs-gemini-3-1-pro-comparison-2026
8. jangwook.net — LLM API Pricing 2026 — https://jangwook.net/en/blog/en/llm-api-pricing-comparison-2026-gpt5-claude-gemini-deepseek/
9. fungies.io — LLM API Cost Comparison 2026 — https://fungies.io/llm-api-pricing-comparison-2026/
10. Meta AI — V-JEPA 2 — https://ai.meta.com/vjepa/
11. Meta AI Blog — V-JEPA 2 Benchmarks — https://ai.meta.com/blog/v-jepa-2-world-model-benchmarks/
12. Google DeepMind — Genie 3 — https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/
13. NVIDIA Cosmos — https://nvidia.com/en-gb/ai/cosmos
14. MLIR Proceedings — Unified Routing and Cascading for LLMs — https://proceedings.mlr.press/v267/dekoninck25a.html
15. Anthropic — Building Effective Agents — https://www.anthropic.com/research/building-effective-agents
16. Anthropic — How We Built Our Multi-Agent Research System — https://www.anthropic.com/engineering/built-multi-agent-research-system
17. dev.to — AI Data Residency Compliance — https://dev.to/morley-media/ai-data-residency-when-cloud-apis-dont-meet-your-compliance-requirements-5eb8
18. Hyperion — Mistral AI Guide for European Enterprises — https://hyperion-consulting.io/en/insights/mistral-ai-complete-guide-2026
19. Medium (Julien Simon) — AI Sovereignty in Europe — https://building.theatlantic.com/ai-sovereignty-in-europe-a-decision-framework-375a517a4179
20. BenchGecko — EU-Hosted LLMs — https://benchgecko.ai/pricing/eu-hosted
21. Complyance — EU AI Act Vendor Compliance — https://complyance.app/blog/ai-vendor-compliance-openai-anthropic
22. LLMversus — LLM Cost Optimization Playbook 2026 — https://llmversus.com/blog/llm-cost-optimization-guide
23. MyEngineeringPath — LLM Inference Optimization — https://myengineeringpath.dev/genai-engineer/inference-optimization/
24. OWASP GenAI — LLM03:2025 Supply Chain — https://genai.owasp.org/llmrisk/llm03/
25. OWASP GenAI — LLM04:2025 Data and Model Poisoning — https://genai.owasp.org/llmrisk/llm04/
26. Adaline — Complete Guide LLM Observability 2026 — https://www.adaline.ai/blog/complete-guide-llm-observability-monitoring-2026
27. Coverge — LLM Observability Guide — https://coverge.ai/blog/llm-observability-guide
28. GetDeploying — Llama 4 Scout Specs 2026 — https://getdeploying.com/llms/llama-4-scout
29. CloudPrice — Llama 4 Maverick — https://cloudprice.net/models/meta-llama-4-maverick
30. APIScout — Mistral vs OpenAI 2026 — https://apiscout.dev/blog/mistral-ai-vs-openai-api-2026
