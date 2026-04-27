# BB_06 Model Engines — Eindrapport

**Onderwerp:** Model Engines als zesde bouwsteen van BeeHaive AI-framework
**Datum:** 2026-04-27
**Researcher-rondes:** 1 (5 parallelle dimensies) + verificatiepass
**Doelgroep:** AI-consultants, CTO's, AI-leads en technisch geletterde opdrachtgevers in Nederlandse organisaties

---

## Executive Summary

AI-modellen zijn de denk- en rekenkern van elke AI-oplossing — maar welk model je kiest, is een ontwerp-beslissing met verstrekkende gevolgen voor kosten, kwaliteit, latency, privacy en compliance. Het overheersende anti-patroon in 2026 is de reflex om overal het grootste, nieuwste frontier-LLM in te zetten. Dat is duurder, trager en minder verklaarbaar dan nodig, en het werkt niet voor de meerderheid van enterprise-taken.

Het modeltype-landschap is in 2026 breder dan ooit: naast algemene LLMs en reasoning-modellen zijn multimodale modellen, world models (voor robotica en simulatie), diffusiemodellen, embedding-modellen en klassieke ML-algoritmen allemaal legitieme architectuurcomponenten. De kern van goede model-engineering is dezelfde als de kern van goede software-engineering: kies het gereedschap dat past bij de taak, niet het meest indrukwekkende gereedschap in de kast.

De frontier-markt is ingrijpend veranderd. Claude Opus 4.7, GPT-5.4 en Gemini 3.1 Pro convergeren op reasoning-benchmarks tot op 0,2 procentpunt verschil op GPQA Diamond (~94% alle drie). De werkelijke differentiatie zit in specifieke taakdomeinen — coding/agents voor Claude, webonderzoek voor GPT-5.4, kostprijs voor Gemini — en in een prijsrange van 1.250x (DeepSeek V3.2 op $0,14 tot GPT-5.4 Pro op $30 per miljoen input-tokens). Multi-model routing reduceert kosten met 60–83% bij minimaal kwaliteitsverlies.

EU-data-soevereiniteit vereist meer dan een EU-regio kiezen. De US CLOUD Act maakt alle US-bedrijven kwetsbaar, ongeacht datacenter-locatie. Mistral is de enige frontier-provider met categoriale CLOUD-Act-immuniteit.

---

## 1. Modeltype-keuze als ontwerpvraag

### 1.1 Het anti-patroon

"Het grootste LLM overal" is een anti-patroon om drie redenen:

1. **Kostenverschil**: een frontier-LLM kost $0,01–$0,50 per aanroep; klassiek ML $0,001–$0,01; regels nagenoeg nul. Bij honderdduizend aanroepen per maand scheelt dit tussen de €900 en €45.000 per maand voor exact dezelfde taak (`verified`, [1, 4]).
2. **Latency**: klassiek ML (10–100 ms) is 5–50x sneller dan een LLM (200 ms–5 s) bij gesloten, gestructureerde taken (`verified`, [4]).
3. **Verklaarheid**: voor gereguleerde omgevingen zijn classifiers en regressiemodellen statistisch valideerbaar; LLMs zijn juridisch nauwelijks auditeerbaar (`verified`, [5]).

### 1.2 Vier beslisfactoren

Elke model-selectie draait om vier factoren (`verified`, [1, 2]):
1. **Taakcomplexiteit** — open-ended of gesloten/gedetermineerd?
2. **Kosten** — wat is de tolerabele prijs per aanroep bij het verwachte volume?
3. **Latency** — realtime (<200 ms) of asynchroon (seconden/minuten)?
4. **Privacy / data-residentie** — wat mag de data verlaten, en naar welk jurisdictiegebied?

Benchmarks (MMLU, HumanEval) correleren zwak met bedrijfsprestaties. Het enige zinvolle kwaliteitstest is een private evaluatie op 50–200 eigen representatieve voorbeelden (`verified`, [1, 3]).

### 1.3 Beslismatrix: LLM vs klassiek ML vs regels

| Dimensie | Regels | Klassiek ML | LLM |
|----------|--------|-------------|-----|
| Kosten per aanroep | Nagenoeg nul | $0,001–$0,01 | $0,01–$0,50+ |
| Setup-tijd | Dagen–weken | Weken–maanden | Uren–dagen |
| Nauwkeurigheid (afgebakende taken) | Perfect (als regels kloppen) | Hoog (met data) | Goed–hoog |
| Omgaan met ambiguïteit | Nee | Beperkt | Ja |
| Verklaarbaar / auditeerbaar | Uitstekend | Laag–gemiddeld | Zeer moeilijk |
| Latency | Sub-milliseconde | 10–100 ms | 200 ms–5 s |
| Databehoefte | Geen | 1.000–100.000+ gelabeld | Nul–weinig |

`verified` [4]

### 1.4 Diagnostische vragen: "Is dit een LLM-probleem?"

Gebruik deze vragen als filter vóór je een model kiest:

1. Is de uitvoer een gestructureerd getal of label? → Probeer eerst klassiek ML of regels
2. Heb ik 1.000+ gelabelde voorbeelden? → Klassiek ML is serieuze kandidaat
3. Moet het resultaat statistisch verklaarbaar zijn voor een auditor? → Klassiek ML of regels
4. Is latency <100 ms een harde grens? → Klassiek ML of gespecialiseerd model
5. Gaat het om tabellaire, historische data? → XGBoost/LightGBM eerst proberen
6. Is de taak open-ended of bevat ze ambiguïteit? → LLM is geschikt
7. Is er onvoldoende gelabelde data voor een klassiek model? → LLM of few-shot

### 1.5 Aanbevolen progressie

1. Begin met prompt engineering op een generalistisch model
2. Voeg RAG toe als kenniscontext ontbreekt
3. Gebruik fine-tuning alleen als laatste stap — vereist ≥1.000 kwaliteitsvoorbeelden en een meetbaar evaluatiecriterium
4. Fine-tuning zonder evaluatiepijplijn is "schieten in het donker" (`verified`, [3])

---

## 2. Het modeltype-landschap in 2026

### 2.1 Algemene LLMs

Getraind op brede tekstcorpora; geschikt voor: vrije-tekst-generatie, samenvatting, vraagbeantwoording, code-generatie, documentanalyse, conversatie. De brede standaardkeuze voor open-ended taalkundige taken.

### 2.2 Reasoning-modellen (extended thinking)

Claude Opus 4.7 met extended thinking, OpenAI o3/o3-mini, GPT-5.4 in thinking-mode. Reserveren rekentijd voor expliciete redenering. Sterk bij: wiskundige bewijzen, multi-stap-planning, complexe code-architectuur. Nadeel: hogere latency en kosten (o3 Pro: $150/MTok input). Gebruik alleen als de kwaliteitsverbetering meetbaar en gerechtvaardigd is (`inferred`, [6]).

### 2.3 Multimodale en vision-language-modellen

Verwerken tekst, beeld en soms audio/video in één model. Voorbeelden: Claude Sonnet 4.6, Gemini 3.1 Pro (tekst + beeld + video native), GPT-5.4. Toepassingen: document-begrip, productafbeeldingsanalyse, formulierverwerking, medische beeldherkenning.

**Wanneer wel**: input is inherent visueel; tekst-only beschrijving verliest te veel informatie.
**Wanneer niet**: zuivere teksttaken — multimodale modellen zijn duurder dan tekst-only varianten.

### 2.4 World models — opkomend voor robotica en simulatie

World models modelleren hoe de wereld reageert op acties. Relevant voor enterprise-organisaties die werken met robotica, autonome systemen of industriële simulatie.

**Meta V-JEPA 2** (juni 2025, primaire bron: ai.meta.com/vjepa) (`verified`):
- 1,2 miljard parameters; getraind op 1M+ uur video
- Zero-shot robotbesturing in nieuwe omgevingen na slechts 62 uur unlabeled robotdata
- MIT-licentie, open-source
- Toepassingen: robotica, autonoom rijden, simulatie

**Google DeepMind Genie 3** (augustus 2025, primaire bron: deepmind.google) (`verified`):
- Eerste real-time interactief world model met fysisch accurate 3D-omgevingen
- Toepassingen: training van agents, simulatie-omgevingen, educatie, gaming
- Beperkt beschikbaar voor testers

**NVIDIA Cosmos** (CES 2025, primaire bron: nvidia.com/en-gb/ai/cosmos) (`verified`):
- Drie modelcategorieën: Predict (toestandsimulatie), Transfer (sim-to-real overdracht), Reason (fysica-bewust redeneren)
- 2 miljoen downloads; enterprise-adoptie bij 1X, Agility Robotics, Figure AI (humanoid robotics), Uber, XPENG (autonome voertuigen)
- Getraind op 9.000 biljoen tokens uit 20 miljoen uur real-world data
- Toepassingen: synthetische trainingsdata genereren, gevaarlijke of zeldzame scenario's simuleren, industriële productie-optimalisatie

**Voor de meeste Nederlandse organisaties in 2026**: world models zijn nog niet operationeel relevant buiten robotica, autonome voertuigen en specifieke industriële simulatiecontexten. Oriënteer; volg de ontwikkeling; wacht met inzetten (`inferred`).

### 2.5 Diffusiemodellen voor beeld en video

Stable Diffusion 3, DALL-E 3, Midjourney v7 (beeld); Sora (OpenAI), Veo 3 (Google DeepMind), Runway Gen-3 (video). Toepassingen: marketingvisualisaties, productafbeeldingen, UI-prototyping, video-content. Niet geschikt voor gereguleerde sectoren waar visuele outputs auditeerbaar moeten zijn.

### 2.6 Embedding-modellen

Zetten tekst om naar numerieke vectoren voor semantische vergelijking. Onmisbaar voor RAG, semantisch zoeken, clustering en anomaliedetectie. Kosten: significant lager dan generatieve LLMs — typisch $0,0001–$0,002/MTok. Gebruik altijd als je RAG implementeert.

### 2.7 Klassieke en gespecialiseerde ML-modellen

XGBoost, LightGBM, Random Forest, BERT-classifiers, ARIMA/Prophet voor tijdreeksen. Superieur aan LLMs bij (`verified`, [4, 5]):
- Tabellaire gestructureerde data (churn, fraude, voorraadbeheer, kredietscores)
- Tijdreeksen met duidelijke patronen (energieverbruik, productieforecast, sensordata)
- Hoge-volume classificatie (content-moderatie, transactie-labeling) — 100x goedkoper per aanroep
- Gereguleerde omgevingen waar statistisch valideren verplicht is
- Latency-kritische toepassingen (<100 ms)

**Kernregel**: als je een gestructureerd getal of label wilt voorspellen op basis van historische data, begin bij XGBoost — niet bij een LLM.

---

## 3. Frontier-landschap april 2026

### 3.1 Prijsoverzicht

*Alle prijzen per miljoen tokens input/output. Geverifieerd via APIScout, jangwook.net, fungies.io, aicostcheck.com — april 2026.*

**Anthropic Claude** (`verified`, [6, 7]):

| Model | Input $/MTok | Output $/MTok | Context |
|-------|-------------|--------------|---------|
| Claude Opus 4.7 | $5,00 | $25,00 | 1M tokens |
| Claude Sonnet 4.6 | $3,00 | $15,00 | 1M tokens |
| Claude Haiku 4.5 | $0,25 | $1,25 | 200K tokens |

Let op: Claude Opus 4.7 levert een nieuwe tokenizer die 1,0–1,35x meer tokens gebruikt dan Opus 4.6 afhankelijk van content — een effectieve kostenstijging van 10–35% ondanks gelijke stickerprijzen (`verified`, [8]).

**OpenAI GPT-5-familie** (`verified`, [6, 7]):

| Model | Input $/MTok | Output $/MTok | Context |
|-------|-------------|--------------|---------|
| GPT-5.4 | $2,50 | $15,00 | 400K–1M tokens |
| GPT-5.4 (lang context >272K) | $5,00 | $22,50 | 400K+ tokens |
| GPT-5.4 Pro | $30,00 | $180,00 | 1M tokens |
| GPT-5 Mini | $0,25 | $2,00 | 500K tokens |
| GPT-5 Nano | $0,05 | $0,40 | 128K tokens |
| O3 Pro (reasoning) | $150,00 | — | 128K |

GPT-5.4 verlaagde zijn prijs in maart 2026 van $10 naar $2,50 per MTok input — een directe reactie op DeepSeek-druk (`verified`, [7]).

**Google Gemini** (`verified`, [6, 7]):

| Model | Input $/MTok | Output $/MTok | Context |
|-------|-------------|--------------|---------|
| Gemini 3.1 Pro (≤200K) | $2,00 | $12,00 | 2M tokens |
| Gemini 3.1 Pro (>200K) | $4,00 | $18,00 | 2M tokens |
| Gemini 2.5 Flash | $0,15 | $0,60 | 1M tokens |
| Gemini 2.5 Flash-Lite | $0,10 | $0,40 | 1M tokens |

**Meta Llama 4 (open-source)** (`verified`, [9, 10]):

| Model | Via API $/MTok input | Context | Opmerkingen |
|-------|---------------------|---------|-------------|
| Llama 4 Scout | $0,11–$0,25 | 328K–10M tokens | MoE 17B actief; zelf-hostbaar |
| Llama 4 Maverick | $0,15–$0,35 | 1M tokens | MoE 17B actief / 128 experts |

**Mistral (EU-nativo)** (`verified`, [11]):

| Model | Input $/MTok | Output $/MTok | Licentie |
|-------|-------------|--------------|---------|
| Mistral Large 3 | ~$1,00–$2,00 | ~$3,00 | Apache 2.0 (open weights) |
| Mistral Small 3.2 | $0,06 | $0,18 | Apache 2.0 |
| Mistral Nemo | $0,02 | $0,04 | Apache 2.0 |

**DeepSeek** (`verified`, [6]):

| Model | Input $/MTok | Output $/MTok | Opmerkingen |
|-------|-------------|--------------|-------------|
| DeepSeek V3.2 | $0,14–$0,28 | $0,28–$0,42 | Cache hits bij $0,028/MTok |
| DeepSeek R1 | $0,55 | $2,19 | Reasoning-model |

Het totale prijsverschil tussen goedkoopste en duurste: 1.250x (DeepSeek V3.2 $0,14 vs GPT-5.4 Pro $30 per MTok input) (`verified`, [12]).

### 3.2 Benchmark-vergelijking: geen universele winnaar

Convergentie op reasoning-benchmarks: Claude Opus 4.7, GPT-5.4 en Gemini 3.1 Pro liggen op GPQA Diamond (graduate-level redeneren) binnen 0,2 procentpunt (~94%). De werkelijke differentiatie is taak-specifiek (`verified`, [8]):

| Taaktype | Beste model | Score |
|----------|------------|-------|
| Productie-code / SWE-bench Pro | Claude Opus 4.7 | 64,3% |
| Tool-zware agents / MCP-Atlas | Claude Opus 4.7 | 77,3% |
| Desktop-automatisering / OSWorld | Claude Opus 4.7 | 78,0% |
| Webonderzoek / BrowseComp | GPT-5.4 | 89,3% (+10 punten) |
| Financiële analyse | Claude Opus 4.7 | 64,4% Finance Agent v1.1 |
| Kostenefficiënte doorvoer | Gemini 3.1 Pro | $2/$12 per MTok |
| Meertalige kennis | Gemini 3.1 Pro | 92,6% MMMLU |
| Graduate-level redeneren (GPQA Diamond) | Gelijkspel | ~94% alle drie |

**Spanningsanalyse**: Anthropic benadrukt coding en agents; OpenAI benadrukt webonderzoek en ecosystem-breedte; Google benadrukt kostprijs en context-window. Alle drie zijn correct voor hun sterkste dimensie — geen enkele claim geldt universeel.

**Praktijkdiscrepantie**: Claude Opus 4.7 liet een regressie zien op BrowseComp (83,7% → 79,3% vs Opus 4.6). Op webonderzoek is Opus 4.6 beter dan Opus 4.7 — een upgrade is hier een verslechtering (`verified`, [8]).

### 3.3 Overige aanbieders

- **Cohere**: sterk op enterprise-retrieval (Command R+); beperkte frontier-capaciteiten
- **Aleph Alpha**: EU-gefocust; achterblijvend op capaciteiten vs Mistral
- **DeepSeek**: indrukwekkende prijs-kwaliteit; Chinese herkomst en beperkte trainingsdata-transparantie is een risicofactor voor NL overheids- en defensie-organisaties (`inferred`)
- **xAI Grok 4.1**: $0,20/$0,50, real-time web-access; beperkte EU-aanwezigheid (`unverified`)

### 3.4 Tierindeling als architectuurkader

| Tier | Modellen | Gebruik | % aanroepen |
|------|---------|---------|------------|
| Frontier | Claude Opus 4.7, GPT-5.4 | Complexe redenering, agentic workflows | ~5% |
| Pro | Sonnet 4.6, GPT-5 | Dagelijks professioneel werk, code | ~35% |
| Standaard | Haiku 4.5, Gemini 2.5 Flash | Balanced speed/quality | ~30% |
| Budget | GPT-5 Nano, DeepSeek V3.2 | Classificatie, hoog volume | ~30% |
| Lokaal | Llama 4, Mistral Large 3 self-hosted | Privacy, offline, onbeperkt | Situationeel |

`inferred` uit meerdere bronnen [6, 8, 13]

---

## 4. Routing- en hybride strategieën

### 4.1 De vier routing-patronen

**Direct routing** (intent-based):
- Classificeer inkomende aanvraag (<50 ms) en route naar juiste model-tier
- Vereist accurate classifier; werkt goed bij duidelijk onderscheid tussen categorieën
- Infrastructuur: LiteLLM (open-source), OpenRouter, Martian, Not Diamond, Amazon Bedrock IPR

**Cascading** (sequentieel-escalerend):
- Stuur eerst naar goedkoopste model; escaleer alleen als kwaliteitsdrempel niet gehaald
- Voordeel: geen upfront classifier; werkt op confidence-signaal
- Nadeel: latency-taks bij escalatie

**Cascade routing** (gecombineerd):
- Route voor duidelijke gevallen; cascade voor ambigueuze middenlaag
- Theoretisch optimaler dan zuivere routing of cascading (`verified`, Dekoninck et al. ETH Zurich 2024/2025, [14])
- Praktisch beste keuze bij gemengde werklast

**Ensemble/voting**:
- Stuur naar meerdere modellen; combineer via voting of fusie
- Gebruik oneven aantal modellen (3 of 5) om gelijkspel te vermijden
- Alleen rechtvaardigen bij hoge-inzet-beslissingen (kosten 3x of meer per aanroep)

### 4.2 Kostenimpact

Multi-model routing reduceert LLM-kosten met 60–83% bij minimaal kwaliteitsverlies (`unverified`, meerdere zelfgerapporteerde bronnen [15, 16]). Behandel als ordegrootte. Een representatief voorbeeld: 76% van inference-aanroepen hoeft een frontier-model niet te raken.

Anthropic's eigen multi-agent onderzoekssysteem toont: upgraden van Claude Sonnet 3.7 naar Sonnet 4 levert meer prestatiewinst dan het verdubbelen van het tokenbudget — model-kwaliteit weegt zwaarder dan extra tokens (`verified`, [17]).

### 4.3 Anthropic's aanbeveling: start simpel

"Building Effective Agents" (december 2024, `verified`, [18]): begin met de eenvoudigste workflow die werkt. Voeg orchestratie en routing toe alleen als bewijs bestaat dat het nodig is.

In multi-agent-architecturen:
- Opus voor orchestrators (planners, synthesizers) — lange redeneerketens
- Sonnet voor parallel uitvoerende workers
- Haiku voor informatieverzamelaars (5–10 parallel)

### 4.4 Wanneer multi-model-architectuur niet de moeite waard is

Multi-model-routing voegt complexiteit toe die gerechtvaardigd moet worden:
- Kleine volumes: routing-infrastructuur-overhead > besparingen
- Homogene werklast: alle aanvragen vergelijkbaar complex
- Gebrek aan monitoring: zonder observability zie je niet of routing goed werkt
- Latency-kritisch: cascading kan latency verergeren bij drie-tier escalatie

---

## 5. EU-data-residentie en soevereiniteit

### 5.1 CLOUD Act — de juridische kern

De US CLOUD Act machtigt US-autoriteiten om data op te eisen bij US-bedrijven, ook wanneer die data op EU-servers staat. "EU-regio kiezen" is onvoldoende voor werkelijke data-soevereiniteit bij US-providers (`verified`, [19, 20]).

Alle grote cloud-AI-providers (AWS Bedrock, Azure OpenAI, Google Vertex AI) en API-providers (Anthropic, OpenAI) zijn US-bedrijven en vallen onder de CLOUD Act.

### 5.2 Providers naar EU-soevereiniteitspositie

| Provider | HQ | CLOUD Act | EU-regio | Beste voor |
|----------|-----|-----------|---------|-----------|
| Mistral AI | Parijs, FR | Nee (EU-bedrijf) | Paris + Sweden (standaard) | Strengste compliance |
| Anthropic | San Francisco | Ja | Via AWS EU (IE, DE, FR) | Enterprise met EU-SCC |
| OpenAI | San Francisco | Ja | Enterprise (IE, DE, NL) | Enterprise met DPA |
| Google Vertex AI | Mountain View | Ja | BE, NL, DE, FI, PL, IT, FR | Configureerbaar sterkste |
| Meta Llama 4 self-hosted | — | N.v.t. | Eigen infra | Volledige controle |

`verified` [20, 21]

**Mistral-caveat**: Mistral heeft US-investeerders (a16z, Salesforce Ventures). CLOUD Act-blootstelling via investeerdersrelaties is juridisch ongetest (`unverified`, [22]). Laat NL juridische afdeling beoordelen bij hoog-gevoelige toepassingen.

### 5.3 AWS European Sovereign Cloud

AWS lanceerde in 2025 de European Sovereign Cloud met directe Amazon Bedrock-toegang (Anthropic, Meta, Mistral, Amazon-modellen). Haalt niet het niveau van SecNumCloud (hoogste Franse overheidsnorm). Praktische keuze voor organisaties die Bedrock willen maar EU-data-residency nodig hebben (`inferred`, [22]).

### 5.4 Lokale / on-premise inference

| Tool | Type | Gebruik |
|------|------|---------|
| Ollama | Lokale runtime | Eenvoudige installatie, breed model-support |
| vLLM | Production serving | Hoge doorvoer, continuous batching |
| TGI (HuggingFace) | Production serving | Geoptimaliseerd voor HF-modellen |
| llama.cpp | CPU + GPU | Low-hardware-requirement; Llama 4 Scout op M4 Mac |

Lokale inference elimineert alle externe datatransfers. Beperkingen t.o.v. cloud-API:
- Kwaliteitskloof: Mistral Large 3 zelf-gehost benadert maar overtreft niet consistent Claude Opus 4.7/GPT-5.4 op alle taken (`inferred`)
- Agentic tooling (MCP, computer-use) minder volwassen bij EU-native providers
- Hardware-investering: $15.000–$50.000 voor on-premise Llama 4-deployment; break-even vs cloud-API bij ~$10.000–$30.000/maand cloud-kosten (`inferred`, [9])

### 5.5 EU AI Act — model-verplichtingen

GPAI-model-providers (artikel 53 EU AI Act, grotendeels van kracht augustus 2025) (`verified`, [23, 24]):
- Technische documentatie verplicht
- Trainingsdata-samenvatting en copyright-compliance
- Voor modellen met "systemisch risico" (art. 55): veiligheidsevaluaties

**DORA** (financiële sector) en **EHDS** (Europese Gezondheidsdata Ruimte) kennen aanvullende data-lokalisatieverplichtingen die API-gebruik bij US-providers in principe uitsluiten voor kritieke systemen.

Mistral publiceert compliance-templates en audittrail-tooling specifiek voor EU AI Act (`inferred`, [24]).

### 5.6 Werkelijke beperkingen "EU-only"-architectuur

1. Mistral Large 3 kost ~70% minder dan GPT-5.4 op vergelijkbare tiers — compenseert deels de kwaliteitskloof
2. Agentic tooling (MCP, computer-use) is minder ver bij EU-native providers
3. Real-time updates en RLHF zijn minder mature bij self-hosted opties
4. Mistral's Forge biedt dedicated on-premise training-optie voor gevoelige organisaties (overheid, defensie) (`inferred`, [25])

---

## 6. Kostenoptimalisatie

### 6.1 Vijf hefbomen in volgorde van impact

| Hefboom | Typische besparing | Implementatietijd |
|---------|-------------------|------------------|
| Model right-sizing | 60–80% | 1–2 weken |
| Prompt caching | 50–90% op input | 1–3 dagen |
| Batch-API migratie | 50% op batch-workloads | 1–2 weken |
| Prompt-lengte trimmen | 20–40% op input | 1–2 weken |
| Open-source migratie | 50–90% bij schaal | 4–12 weken |

`verified` [26]

### 6.2 Prompt caching — concrete kortingen

Gecachede input-kortingen bij grote providers (`verified`, [6, 7]):
- Anthropic Sonnet 4.6: $3,00 → $0,30/MTok (90% korting)
- Gemini 2.5 Pro: $1,25 → $0,31/MTok (75% korting)
- GPT-5.4: $2,50 → $1,25/MTok (50% korting)

Vereiste: stabiele, herhalende prefix. Als >20% van input-tokens identiek is over aanroepen: caching levert significante besparing (`verified`, [26]).

Bij lokale modellen (Ollama, vLLM, llama.cpp): API-prompt-caching bestaat niet — eigen implementatie vereist (`verified`, [27]).

### 6.3 Kwantisatie (self-hosted)

| Techniek | Geheugenreductie | Snelheidswinst | Kwaliteitsverlies |
|----------|-----------------|----------------|------------------|
| INT8 | 50% | 1,5–2x | <1% |
| INT4 (AWQ) | 75% | 2–3x | 1–3% |
| Kennisd. distillatie | 40–60% | 2–3x | 2–5% |
| KV-cache kwantisatie | 30–50% (cache) | 1,3–1,8x | <1% |

`verified` [28, 29]

Kritisch: INT8 versnelt alleen bij native-support (TensorRT, ONNX Runtime, llama.cpp). Standaard PyTorch draait INT8 als FP32 — is dan puur overhead (`verified`, [27]).

### 6.4 Distillatie

Een 70B model destilleren naar een 7B model voor een specifieke taak (`verified`, [28]):
- Kostenreductie: 90% bij inferentie
- Kwaliteitsbehoud: 90–95% voor de specifieke taak
- Vereiste: goed gedefinieerde taak + duizenden kwaliteits-outputs als trainingsdata + ML-infrastructuur

### 6.5 Wanneer is self-hosting goedkoper dan API?

Break-even verschuift richting self-hosting boven ~500K–1M tokens/dag voor niet-frontier-modellen (`inferred`). Hardware-investering: $15.000–$50.000 voor on-premise Llama 4-deployment; versus cloud-API-kosten die $10.000–$30.000/maand kunnen bereiken bij intensief gebruik (`inferred`, [9]).

---

## 7. Operationele runtime

### 7.1 Latency-budgetten

| Drempel | Betekenis |
|---------|-----------|
| >30 tokens/seconde streaming | Voelt instant voor de eindgebruiker |
| TTFT <200 ms | Target voor interactieve toepassingen |
| P95 <10 seconden | Alert-drempel voor asynchrone LLM-aanroepen |
| P99 als SLA-primaire maatstaf | P50 en P95 verbergen staart-latency die gebruikers écht ervaren |

`inferred` [30, 31]

### 7.2 Versie-pinning vs auto-upgrade

| Aanpak | Voordeel | Risico |
|--------|----------|--------|
| Versie-pinning | Voorspelbaar gedrag; eenvoudiger compliance | Mist beveiligingspatches en verbeteringen |
| Auto-upgrade | Altijd recente kwaliteit | Stille gedragswijziging breekt downstream-logica |

Aanbeveling: pin op major versie in productie; test upgrades in staging met eval-suite voordat je uitrolt (`inferred`).

### 7.3 Fallback-patronen

Bij model-uitval, rate-limiting of degradatie:
- Primaire provider → fallback provider (Anthropic → OpenAI of omgekeerd)
- Stap-down naar kleiner model in dezelfde familie (Opus → Sonnet → Haiku)
- Circuit-breaker: stop escalatie naar dure fallback als foutpercentage te hoog
- Monitor `fallback_activation_rate` — stijging signaleert upstream incident

`inferred` [31]

### 7.4 Observability — vijf pijlers

LLM-observability gaat verder dan traditionele APM: een HTTP 200 kan een hallucinatoire respons bevatten (`verified`, [30, 31, 32]).

**Minimale metriekenset:**

| Categorie | Metriek | Reden |
|-----------|---------|-------|
| Latency | TTFT, totale generatietijd, P50/P95/P99 | Gebruikerservaring en bottleneck |
| Kosten | Tokens per aanroep (input + output), kosten per model | Budget en anomaliedetectie |
| Kwaliteit | LLM-as-judge score (steekproef 5–15%), guardrail-trigger-rate | Regressies detecteren |
| Betrouwbaarheid | Error-rate per type, retry-rate, fallback-activatie-rate | Provider-stabiliteit |
| Drift | 7-daagse trend antwoordlengte, embedding-verdriftdetectie | Stille degradatie |

**Vier incident-correlaties die 80% van LLM-incidenten dekken** (`verified`, [31]):

| Patroon | Oorzaak |
|---------|---------|
| Latency stijgt + grounding-score daalt | Retrieval-degradatie |
| Latency stabiel + hallucinatie stijgt | Prompt- of modelwijziging |
| Escalatierate stijgt + kosten stijgen | Classifier drift |
| Provider-foutrate stijgt + fallback-rate stijgt | Upstream incident |

**Alert-drempels** (`inferred`, [30, 31, 32]):
- Dagbudget overschreden: directe alert
- Error-rate >1–5%: on-call notificatie
- P95 latency >10 seconden: Slack-notificatie
- Kwaliteitsscore onder drempel: Slack-notificatie
- Kostenspike: kan prompt-injection of runaway agent-loop signaleren

---

## 8. Risico's en beperkingen op model-niveau

### 8.1 Knowledge cutoffs

LLMs hebben een trainingsdatum; actuele informatie ontbreekt. Mitigaties: RAG met up-to-date kennisbronnen, expliciete datum-context in system-prompt, reasoning-modellen zonder externe tools niet inzetten voor actuele informatiebehoeften.

### 8.2 Hallucinatie-profielen

| Modeltype | Hallucinatie-risico | Mitigatie |
|-----------|---------------------|-----------|
| Grote LLMs | Matig-hoog voor feitelijke claims | RAG, grounding-checks, citations |
| Reasoning-modellen | Lager bij redeneer-taken; feitenrisico blijft | RAG bij feitenafhankelijke taken |
| World models | Fysische fouten in simulatie | Verificatie in echte omgeving verplicht |
| Klassiek ML | Geen taal-hallucinatie; out-of-distribution mogelijk | Drift-monitoring, feature-validatie |

`inferred` uit meerdere bronnen

### 8.3 OWASP LLM Top-10 (2025) — model-laag

**LLM03:2025 — Supply Chain** (`verified`, [33]):
- Kwetsbaarheden via: manipuleerde pre-trained modellen, vergiftigde datasets, kwetsbare bibliotheken, MCP-tools
- Open-source modellen van HuggingFace kunnen backdoors bevatten via malicious pickling bij modelladen
- Mitigaties: checksums/hashes voor model-integriteit; vendor acceptance testing; ModelAudit voor statische scan; gedetailleerde logging van alle trainingswijzigingen

**LLM04:2025 — Data and Model Poisoning** (`verified`, [34]):
- Pre-training, fine-tuning of embedding-data gemanipuleerd → backdoors, biases
- Backdoors kunnen slapend zijn: model gedraagt zich normaal totdat een trigger actief is (sleeper agent)
- Mitigatie: bias-detectietests, consistentietests, red-teaming

**LLM07:2025 — System Prompt Leakage**:
- Confidentiële system-prompt kan via aanvallen of model-gedrag lekken
- Behandel system-prompt als non-secret; beperk gevoelige informatie erin

### 8.4 Model-cards en AI Bill of Materials

- **Model-cards**: beschrijven prestaties, beperkingen, trainingsdata, intended use — governance-instrument voor audittrails
- **AI-BOM**: modelcomponenten documenteren vergelijkbaar met software-BOM — verplicht onder EU AI Act art. 13 voor hoog-risico systemen (`inferred`)
- Trainingsdata-transparantie: Meta (Llama 4) en Mistral relatief open; OpenAI/Anthropic/Google geslotener
- **DeepSeek-risicofactor**: Chinese herkomst + beperkte trainingsdata-transparantie is risicofactor voor NL overheids- en defensieorganisaties (`inferred`)

---

## Tegenstrijdigheden en open vragen

**Tegenstrijdigheid 1: EU-soevereiniteit van Mistral**
Mistral wordt gepresenteerd als categorisch veilig voor CLOUD Act. Maar Mistral heeft US-investeerders (a16z, Salesforce Ventures), wat potentiële blootstelling via investeerdersrelaties creëert. Dit is juridisch ongetest [22]. Nederlandse juridische afdeling moet dit beoordelen bij hoog-gevoelige toepassingen.

**Tegenstrijdigheid 2: kostenbesparingspercentages**
Claims van 60–94% kostenreductie via routing en caching zijn overwegend zelfgerapporteerd. Ze zijn plausibel maar sterk context-afhankelijk. Behandel als ordegrootte, niet als garantie.

**Tegenstrijdigheid 3: benchmarks vs praktijk**
Claude Opus 4.7 liet een regressie zien op BrowseComp (83,7% → 79,3%) t.o.v. Opus 4.6. Een modelupgrade is niet altijd beter voor alle taken. Evalueer altijd op eigen taken vóór je migreeert.

**Open vraag — DeepSeek**: welke NL-publieke of financiële organisaties kunnen DeepSeek-modellen rechtmatig inzetten? Vereist rechtsgutachten.

**Open vraag — World models**: wanneer overschrijden Genie 3 of Cosmos de drempel voor brede enterprise-inzetbaarheid buiten robotica? Verwachte horizon: 2027–2028 (`inferred`).

---

## Synthese: 7 ontwerpregels voor de Nederlandse AI-consultant

**Regel 1: Kies op taak, niet op trend.**
De eerste vraag is niet "welk model?", maar "is dit een LLM-probleem, een klassiek-ML-probleem, of een dashboard-probleem?" Gebruik de diagnostische vragen. XGBoost op tabellaire data overtreft een LLM in kosten, latency en verklaarheid.

**Regel 2: Vertrouw geen enkele benchmark.**
Evalueer modellen altijd op 50–200 eigen representatieve voorbeelden. MMLU en HumanEval correleren zwak met bedrijfsprestaties. Claude Opus 4.7 regredeerde op webonderzoek, terwijl het verbeterde op coding — een upgrade kan een verslechtering zijn voor jouw specifieke taak.

**Regel 3: Bouw model-agnostisch.**
Models veranderen elke drie maanden. Een goede evaluatiepijplijn vertelt je wanneer het tijd is om te wisselen — en model-agnostische architectuur (bijv. via LiteLLM of een eigen gateway) maakt die wissel een kwestie van uren, niet maanden.

**Regel 4: Tier je stack.**
Gebruik frontier-modellen voor ~5% van aanroepen (harde redenering, agents); mid-tier voor het dagelijkse werk; budget- en lokale modellen voor hoge-volume eenvoudige taken. Multi-tier aanpak reduceert kosten met 60–80% bij gelijkblijvende kwaliteit.

**Regel 5: Cachen vóór je iets anders optimaliseert.**
Prompt caching is de snelste en eenvoudigste kostenoptimalisatie (50–90% op input in 1–3 dagen implementatietijd). Stel de vraag: "Welk percentage van mijn input-tokens is identiek over aanroepen?" Als >20%: implementeer caching eerst.

**Regel 6: EU-data-soevereiniteit vereist juridische helderheid.**
CLOUD Act maakt EU-regio's van US-providers onvoldoende voor echte soevereiniteit. Voor gevoelige data: Mistral direct (of via EU-cloud-partners), open-weight zelf-hosten (Llama 4, Mistral Large 3), of een juridisch beoordeeld cloud-soevereiniteitskader. Communiceer dit helder naar de opdrachtgever — de keuze voor een model heeft juridische gevolgen.

**Regel 7: Observeer kwaliteit, niet alleen uptime.**
Een HTTP 200 kan een hallucinatie zijn. Voer kwaliteitsmetrieken in (LLM-as-judge steekproef 5–15%), stel kwaliteitsalerts in, en correleer latency-, kosten- en kwaliteitssignalen om incidenten te diagnosticeren. Vier correlaties dekken 80% van LLM-incidenten.

---

## Sources

Alle bronnen geraadpleegd op 2026-04-27. Verificatiestatus per claim staat inline.

### Modeltype-keuze en besliskaders

- [1] LLM Gateway — How to Choose the Right LLM for Your Use Case in 2026 — https://llmgateway.io/blog/how-to-choose-the-right-llm
- [2] NovaKit — Choosing the Right AI Model: A Decision Framework for 2026 — https://www.novakit.ai/blog/choosing-right-ai-model
- [3] core.cz — How to Choose the Right AI Model for Enterprise Deployment in 2026 — https://core.cz/en/blog/2026/ai-model-selection-enterprise-2026/
- [4] IdeaPlan — LLM vs Traditional ML vs Rules: When to Use Each — https://www.ideaplan.io/compare/llm-vs-traditional-ml-vs-rules
- [5] phptrends — Choosing the Right Approach to AI: A Practical Decision Guide — https://phptrends.com/choosing-the-right-approach-to-artificial-intelligence-a-practical-decision-guide/

### Frontier-modellen en prijzen

- [6] APIScout — LLM API Pricing Comparison 2026 — https://apiscout.dev/blog/llm-api-pricing-comparison-2026
- [7] fungies.io — LLM API Cost Comparison 2026 — https://fungies.io/llm-api-pricing-comparison-2026/
- [8] SpectrumAILab — GPT-5.4 vs Claude Opus 4.7 vs Gemini 3.1 Pro [2026] — https://spectrumailab.com/blog/gpt-5-4-vs-claude-opus-4-7-vs-gemini-3-1-pro-comparison-2026
- [9] Meta Llama — Cost Projection Guide — https://www.llama.com/docs/deployment/cost-projection
- [10] LLM Reference — Llama 4 Family — https://www.llmreference.com/model-family/llama-4
- [11] APIScout — Mistral AI vs OpenAI API 2026 — https://apiscout.dev/blog/mistral-ai-vs-openai-api-2026
- [12] AI Security Gateway — LLM API Cost Comparison 2026 — https://aisecuritygateway.ai/blog/llm-cost-comparison-2026
- [13] ModelMomentum — Multi-Model AI Strategy 2026 — https://modelmomentum.com/blog/multi-model-ai-strategy-pick-right-llm-2026

### World models (primaire bronnen)

- [14-A] Meta AI — V-JEPA 2 — https://ai.meta.com/vjepa/
- [14-B] Meta AI Blog — V-JEPA 2 Benchmarks — https://ai.meta.com/blog/v-jepa-2-world-model-benchmarks/
- [14-C] Google DeepMind — Genie 3: A New Frontier for World Models — https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/
- [14-D] NVIDIA Cosmos — https://nvidia.com/en-gb/ai/cosmos

### Routing en multi-agent architectuur

- [14] MLIR Proceedings — A Unified Approach to Routing and Cascading for LLMs (Dekoninck et al.) — https://proceedings.mlr.press/v267/dekoninck25a.html
- [15] dev.to — Multi-Model LLM Routing: Why 76% of Your Inference Shouldn't Touch GPT-4 — https://dev.to/elenarevicheva/multi-model-llm-routing-why-76-of-your-inference-shouldnt-touch-gpt-4-3867
- [16] Tianpan.co — LLM Routing and Model Cascades: How to Cut AI Costs — https://tianpan.co/blog/2025-11-03-llm-routing-model-cascades
- [17] Anthropic — How We Built Our Multi-Agent Research System (jun. 2025) — https://www.anthropic.com/engineering/built-multi-agent-research-system
- [18] Anthropic — Building Effective Agents (dec. 2024) — https://www.anthropic.com/research/building-effective-agents

### EU-soevereiniteit en compliance

- [19] dev.to — AI Data Residency: When Cloud APIs Don't Meet Your Compliance Requirements — https://dev.to/morley-media/ai-data-residency-when-cloud-apis-dont-meet-your-compliance-requirements-5eb8
- [20] BenchGecko — EU-Hosted LLMs & GDPR Compliant AI Model Providers — https://benchgecko.ai/pricing/eu-hosted
- [21] Complyance — Is Your AI Vendor EU AI Act Compliant? — https://complyance.app/blog/ai-vendor-compliance-openai-anthropic
- [22] Medium / Julien Simon — AI Sovereignty in Europe: A Decision Framework — https://building.theatlantic.com/ai-sovereignty-in-europe-a-decision-framework-375a517a4179
- [23] Hyperion Consulting — The Definitive Mistral AI Guide for European Enterprises 2026 — https://hyperion-consulting.io/en/insights/mistral-ai-complete-guide-2026
- [24] AI Magicx — Mistral's Build Your Own AI Strategy — https://www.aimagicx.com/blog/mistral-build-your-own-ai-enterprise-strategy-2026
- [25] Hyperion Consulting — Mistral Forge: Own Your AI Model — https://hyperion-consulting.io/en/insights/mistral-forge-enterprise-ai-model-ownership

### Kostenoptimalisatie en inference

- [26] LLMversus — LLM Cost Optimization: The Complete 2026 Playbook — https://llmversus.com/blog/llm-cost-optimization-guide
- [27] TheNeuralBase — Inference Optimization Cheat Sheet — https://theneuralbase.com/cheatsheet/inference-optimization/
- [28] MyEngineeringPath — LLM Inference Optimization 2026 — https://myengineeringpath.dev/genai-engineer/inference-optimization/
- [29] AISuperior — LLM Cost Optimization in AI Deployment 2026 — https://aisuperior.com/llm-cost-optimization-in-ai-deployment/

### Observability en runtime

- [30] Adaline — Complete Guide to LLM Observability & Monitoring 2026 — https://www.adaline.ai/blog/complete-guide-llm-observability-monitoring-2026
- [31] Coverge — LLM Observability Guide 2026 — https://coverge.ai/blog/llm-observability-guide
- [32] LLM AI Cost Board — Complete Guide to LLM Observability 2026 — https://aicostboard.com/blog/posts/complete-guide-llm-observability-2026

### Beveiligingsrisico's (OWASP)

- [33] OWASP GenAI — LLM03:2025 Supply Chain — https://genai.owasp.org/llmrisk/llm03/
- [34] OWASP GenAI — LLM04:2025 Data and Model Poisoning — https://genai.owasp.org/llmrisk/llm04/

### Aanvullend

- [35] Zylos Research — AI Agent Model Routing and Dynamic Model Selection 2026 — https://zylos.ai/research/2026-03-02-ai-agent-model-routing
- [36] GrizzlyPeak Software — Multi-Model Architectures: Router Patterns — https://www.grizzlypeaksoftware.com/library/multi-model-architectures-router-patterns-lmlktp56
- [37] FastTool — Prompt Caching & Batch API Cost Reduction 2026 — https://fasttool.app/blog/prompt-caching-batch-api-cost-reduction-2026
- [38] CloudPrice — Llama 4 Maverick — https://cloudprice.net/models/meta-llama-4-maverick
- [39] GetDeploying — Llama 4 Scout Specs 2026 — https://getdeploying.com/llms/llama-4-scout
- [40] RajatAI — How to Choose the Right LLM for Your Business 2026 — https://rajatgautam.com/blog/choose-llm-for-business/

### Kerncitaten

- Dekoninck et al. (ETH Zurich, 2024/2025): *"Cascade routing consistently outperforms both routing and cascading across a variety of settings, improving both output quality and lowering computational cost."* — https://proceedings.mlr.press/v267/dekoninck25a.html
- Anthropic (jun. 2025): *"Upgrading to Claude Sonnet 4 is a larger performance gain than doubling the token budget on Claude Sonnet 3.7. Multi-agent architectures effectively scale token usage for tasks that exceed the limits of single agents."* — https://www.anthropic.com/engineering/built-multi-agent-research-system
- SpectrumAILab (apr. 2026): *"Three models. Three different bets. No overlapping winner."* — https://spectrumailab.com/blog/gpt-5-4-vs-claude-opus-4-7-vs-gemini-3-1-pro-comparison-2026
- Julien Simon (jan. 2026): *"Mistral's position is stronger than US-native providers, but do not assume categorical immunity."* — https://building.theatlantic.com/ai-sovereignty-in-europe-a-decision-framework-375a517a4179
