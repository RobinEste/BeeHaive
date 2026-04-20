# Dynamic Context als informatie-architectuur — Draft

**Onderwerp:** Dynamic Context (BB_03) als informatie-architectuur-discipline 2024-2026
**Datum:** 2026-04-20
**Researcher-rondes:** 1

---

## Executive Summary

Context engineering is in 2025 uitgegroeid tot een erkende informatica-discipline — de verschuiving van "prompt engineering" naar een breder paradigma waarbij de kwaliteit, timing en structuur van contextuele informatie de AI-prestaties meer bepalen dan modelkeuze of prompting-vaardigheid. Tobi Lütke (Shopify) definieerde het in juni 2025 als *"the art of providing all the context for the task to be plausibly solvable by the LLM,"* en Gartner verklaarde het in juli 2025 tot strategische prioriteit boven prompt engineering.

Voor BB_03 Dynamic Context betekent dit: de variabele laag die het model op uitvoeringstijd ontvangt uit externe bronnen is niet passief — ze vraagt actief architectuurbeslissingen over wat erin zit, wanneer het wordt vernieuwd, hoe het wordt opgehaald en hoe privacy wordt gewaarborgd. Drie empirische waarschuwingen sturen die beslissingen: (1) context rot degradeert prestaties op alle frontier-modellen zodra informatie in het midden van lange context belandt; (2) stale context faalt stilzwijgend, zonder waarschuwing; (3) PII in de index lekt onbedoeld via normale retrieval.

De productie-patronen zijn volwassen genoeg voor praktische toepassing: hybride retrieval met contextual reranking (67% minder retrievalfouten), event-triggered re-indexing, differentiële privacy voor gevoelige korpussen, en modulaire memory-lagen (mem0 voor persoonlijkheid/continuïteit, Letta voor autonome agenten).

---

## Sectie 1: Context rot en de grenzen van het context window

### 1.1 Het universele degradatie-probleem

Context rot — prestatiedegradatie naarmate het context window groeit — is empirisch vastgesteld op alle 18 geteste frontier-modellen in Chroma's 2025 onderzoek, inclusief GPT-4.1, Claude Opus 4 en Gemini 2.5 Pro [1] (`verified`). Drie mechanismen werken samen:

1. **Lost-in-the-Middle effect** [2] (`verified`): informatie in het midden van de context krijgt 30%+ lagere nauwkeurigheid dan informatie aan het begin of einde. Origineel gedocumenteerd door Liu et al. (Stanford, TACL 2024) en sindsdien gerepliceerd.

2. **Attention dilution** (`inferred`): bij 100K tokens berekent een transformer 10 miljard paargewijze aandachtsrelaties. Softmax-normalisatie verdeelt aandacht over alle tokens, waardoor individuele signalen verdunnen.

3. **Distractor interference** (`verified`): semantisch vergelijkbare maar irrelevante content degradeert prestaties actief — bijzonder problematisch in grote kennisbanken.

### 1.2 Concrete degradatie-data per model (2025)

Adobe Research (februari 2025) mat een two-hop redenering-taak bij stijgende contextlengte [3] (`verified`):

| Model | Nauwkeurigheid kort | Nauwkeurigheid lang | Daling |
|-------|--------------------|--------------------|--------|
| GPT-4o | 99% | 70% | -29% |
| Claude 3.5 Sonnet | 88% | 30% | -58% |
| Gemini 2.5 Flash | 94% | 48% | -46% |
| Llama 4 Scout | 82% | 22% | -60% |

*Noot: 2026-modelversies (Claude 4.7, GPT-5.4, Gemini 3) zijn niet in dit specifieke onderzoek gemeten — de degradatie-richting is consistent, maar absolute waarden zullen afwijken.* (`inferred`)

Chroma (2025): vroege en late context behaalt 85-95% nauwkeurigheid; midden-secties zakken naar 76-82% [1].

### 1.3 Effectief bruikbaar context window

Effectief bruikbaar context window is kleiner dan het geadverteerde maximum. Enterprise-queries consumeren 50K-100K tokens aan setup-context vóór redenering begint [4] (`inferred`). Frontier-model efficiëntie varieert: Claude Opus 4 ~92%, Gemini 2.5 Pro ~92%, GPT-4.1 ~98%, maar Grok 3 slechts 75-87% [4].

**Over de "25-50% bruikbaar" claim van Forte** (`blocked`): er bestaat geen empirische primaire bron voor dit exacte percentage als universele regel. De beschikbare data toont model-afhankelijke efficiëntie. De claim is beter te herformuleren als: *"effectief bruikbaar window varieert per taak, model en context-kwaliteit — organiseer context in minimum viable chunks en test empirisch."*

### 1.4 Implicaties voor context-architectuur

Context-kwaliteit overtreft context-grootte als ontwerpdoelstelling [4] (`inferred`). Multi-agent isolatie verbetert prestaties met 90.2% door zoekruis in geïsoleerde context windows te bevatten in plaats van de primaire agent te vervuilen [1] (`verified`).

---

## Sectie 2: Retrieval-architecturen — van RAG naar context engines

### 2.1 RAG 2.0: de evolutie

RAG evolueert van een vaste pipeline naar een "Context Engine" met intelligente routing als kernfunctionaliteit [5] (`inferred`). De enterprise focus verschuift in 2026 naar pragmatische grootschalige adoptie met RAG als de fundamentele data-laag voor alle AI-applicaties.

**Hybride search + cross-encoder reranking** is de standaard architectuur geworden (2025), met 33-47% nauwkeurigheidsverbetering afhankelijk van querycomplexiteit [5] (`inferred`).

**PTI-pipelines (Parse-Transform-Index)** standaardiseren enterprise-ingestie [5]:
- Format parsing (PDF, ongestructureerde documenten)
- Semantische verrijking (samenvattingen, entiteiten, vraag-generatie per chunk)
- Hybrid indexering: vector + keyword + metadata

### 2.2 Contextual Retrieval — de doorbraak van Anthropic

Anthropic's Contextual Retrieval (2024) verbetert RAG fundamenteel door 50-100 token contextuele samenvattingen te prependen aan chunks vóór indexering [6] (`verified`):

| Aanpak | Reductie retrievalfouten |
|--------|------------------------|
| Contextual Embeddings | 35% (5.7% → 3.7%) |
| + BM25 hybrid | 49% (5.7% → 2.9%) |
| + Reranking | 67% (5.7% → 1.9%) |

Preprocessingkosten: ~$1.02 per miljoen document-tokens via prompt caching [6]. Dit maakt de techniek economisch inzetbaar bij enterprise-schaal.

### 2.3 GraphRAG — voor complexe relaties

Microsoft's GraphRAG bouwt kennisgrafen naast vector-opslag [7] (`unverified` — Microsoft self-reported):
- 80% vs 50% nauwkeurigheid voor complexe multi-hop queries vergeleken met traditionele RAG
- 72-83% comprehensiveness op globale vragen
- LazyGraphRAG (juni 2025) reduceerde indexeringskosten tot 0.1% van oorspronkelijk
- Zwakheid: 16.6% nauwkeurigheidsval voor tijdsgevoelige queries; 3-5× hogere indexeringskosten

Toepassingsdomein: multi-hop redenering, narratieve datasets, complexe kennisnetwerken. Niet geschikt voor frequent-veranderende data.

### 2.4 Intent-detectie en query-routing

Semantische routing classificeert user-intent en routeert naar gespecialiseerde kennisbronnen of retrieval-strategieën [8][9] (`inferred`). Praktisch maximum: 5-20 topics per router voor beheerbaarheid [8]. Amazon's REIC (EMNLP 2025): RAG-versterkte intent-classificatie overtreft fine-tuning bij klantenservice-schaal zonder hertraining [9] (`verified`).

---

## Sectie 3: Context-opslag, chunking en embeddings

### 3.1 Chunking als kwaliteitskritieke keuze

Chunking-kwaliteit heeft meer impact op systeem prestaties dan LLM-keuze of embedding model [10] (`inferred`). Vuistregels:

| Documenttype | Aanbevolen chunk-grootte |
|--------------|-------------------------|
| Algemene tekst | 256-512 tokens, 20-30% overlap |
| Policies/runbooks | Hiërarchisch: paragraaf voor index, sectie voor generatie |
| Code/technische docs | 1.000-1.500 tokens |
| Chat-logs | 200-400 tokens |

**Agentic chunking** (2025): AI-agent beslist dynamisch hoe documenten worden gesplitst op basis van structuur, dichtheid en content [11] (`inferred`).

### 3.2 Embedding-modellen

Gouden regel: gebruik hetzelfde embedding-model voor indexering én querying [10] (`verified`).

Aanbevelingen (2025):
- Voyage AI voyage-3-large: best op MTEB, 32K token context, $0.06/M tokens [11] (`inferred`)
- BAAI/bge-large-en-v1.5: open-source, voor regulated environments zonder externe API [10] (`verified`)
- Domeinspecifieke modellen voor medisch/juridisch gebruik: 20-40% betere retrieval-nauwkeurigheid [11]

### 3.3 Context-opslag architectuur

Memory-lagen voor agenten onderscheiden zich in drie typen [5][12]:
1. **Working memory**: huidige interactiestatus (in context window)
2. **Episodic memory**: historische interacties (externe opslag)
3. **Semantic memory**: geabstraheerde lessen uit eerdere sessies

---

## Sectie 4: Agentic memory — productie-rijpheid

### 4.1 Mem0 — de meest ingezette memory layer

Mem0 (mem0ai/mem0, ~48K GitHub stars, 14M downloads, april 2026 preprint) biedt een pluggable memory layer voor bestaande agent-frameworks [12][13] (`verified`):

- Extractiefase identificeert saillante feiten → compact opgeslagen als natural language memories
- CRUD: ADD / UPDATE / DELETE / NOOP op basis van vergelijking met bestaande memories
- 49.0% op LongMemEval (temporal, multi-hop, knowledge-update scenarios) [12]
- 26% verbetering t.o.v. OpenAI baseline; 91% lagere p95-latentie; >90% tokenkosten bespaard [13]
- SOC 2 + HIPAA compliant; AWS koos Mem0 als exclusive memory provider voor Agent SDK [13]
- Beperking: passieve extractie; geen complexe multi-strategie retrieval voor complexe queries [12]

### 4.2 Letta (voorheen MemGPT) — voor autonome agenten

Letta positioneert memory als expliciete eerste-klas component van agent-state [12] (`verified`):
- Drie-tier architectuur: Core Memory (in context = RAM), Archival Memory, Recall Memory
- Agents beheren hun eigen memory actief (self-editing)
- Beperking: Python-only; architecturele lock-in; elke memory-operatie kost inference tokens

**Productie-oordeel** (`inferred`): Mem0 is productie-rijp voor personalisatie, CS-agents, voice agents. Letta voor autonome agenten die geavanceerde self-managed memory vereisen. Combinatie aanbevolen voor complexe systemen.

### 4.3 MCP als standaard voor context-provisioning

Model Context Protocol (Anthropic, november 2024) standaardiseert context-provisioning voor multi-agent systemen [14] (`verified`):
- >5.800 community MCP-servers beschikbaar (april 2025)
- Drie context-datatypes: Domain Knowledge, Tool Metadata, Conversation State
- Beveiligingsrisico's (april 2025): prompt injection, tool-exfiltratie, lookalike-tools [14]

---

## Sectie 5: Context actualisering en kwaliteitsborging

### 5.1 Staleness — het stille falen

Verouderde context faalt stilzwijgend: het systeem retourneert structureel correcte, zelfverzekerd geformuleerde antwoorden op basis van verouderde informatie zonder waarschuwing [15] (`verified`).

Freshness heeft vier meetbare dimensies [15]:
1. Content Age — tijd sinds laatste menselijke verificatie
2. Embedding Lag — vertraging tussen bronupdate en index-refresh
3. Stale Retrieval Rate — fractie queries die verouderde documenten retourneren
4. Coverage Drift — percentage corpus voorbij staleness-drempel

### 5.2 Staleness-drempels per categorie

| Categorie | Maximale verouderdheid |
|-----------|----------------------|
| Compliance / live pricing | Nul tolerantie |
| Policies & procedures | 24 uur |
| Referentiedocumenten | 30 dagen |
| Historische/contextuele materialen | 90 dagen |

(`verified` [15])

### 5.3 Re-indexing patronen

| Aanpak | Staleness window | Complexiteit |
|--------|-----------------|--------------|
| Nightly batch | Tot 24u | Laag |
| Hourly batch | Tot 60 min | Laag-midden |
| Streaming CDC | Seconden | Hoog |

**Best practice**: event-triggered incrementele re-indexing op document-change events (Confluence, SharePoint) — effectiever dan volledig re-index op schema [16] (`verified`). LlamaIndex native connectors volgen document-hashes en herindexeren alleen gewijzigde bestanden [16].

Composite freshness score < 85% → automatische alerts; < 70% → optionele gebruikerswaarschuwing [15] (`verified`).

### 5.4 RAGAS kwaliteitsmetrics

Evalautie-framework voor productie-RAG [16]:
- Faithfulness > 0.90
- Answer Relevancy > 0.85
- Context Recall > 0.80
- Context Precision > 0.75

Fallback bij retrieval score < 0.55: retourneer "geen betrouwbaar antwoord" [16] (`verified`).

---

## Sectie 6: Privacy, PII en data-lineage

### 6.1 PII-lekkagerisico

RAG-outputs riskeren PII-lekkage zonder extra safeguards [17][18] (`verified`). Twee mechanismen: directe extractie-aanvallen en onbedoelde lekkage via fragmenten. GraphRAG verhoogt dit risico omdat relaties tussen entiteiten expliciet zijn opgeslagen [19] (`verified`).

### 6.2 Filterstrategieën

Pre-indexering is de effectiefste laag [17][18]:
- Redacteer PII/PHI vóór opname in de vectorstore
- Deterministisch tokeniseren voor gestructureerde identifiers (BSN, e-mail)
- Contextuele redactie voor vrije tekst

Differentiële privacy (DP-RAG, arxiv 2412.04697): spendeert privacy-budget alleen op tokens die gevoelige informatie vereisen; superieure prestaties bij ε≈10 [18] (`verified`).

Entiteitsperturbatie: scherpere similarity-drempels verminderen extractie-aanvallen maar verlagen systeemprestaties — expliciete tradeoff [20] (`verified`).

### 6.3 Data-lineage

GDPR-relevante vereisten voor context-lineage [16][21]:
1. Document-provenance: welke bronnen zijn opgehaald per respons?
2. Embedding-timestamp: wanneer zijn vectors aangemaakt?
3. Deletion-audit: vectoren verwijderd na erasure-verzoek
4. Purpose-alignment: gebruik aligned met oorspronkelijk verzameldoel

---

## Tegenstrijdigheden en open vragen

**Tegenstrijdigheid 1 — Forte's percentage vs. empirische data**: Forte's "25-50% bruikbaar context window" staat haaks op recente model-efficiëntie-data die 75-98% efficiency toont voor geoptimaliseerde modellen bij eenvoudige taken. De tegenstrijdigheid is deels oplosbaar: de data laat zien dat *complexe redenering-taken* bij lange context sterk degraderen, terwijl *eenvoudige retrieval-taken* relatief goed presteren. Forte's claim lijkt contextueel gemotiveerd door een specifiek gebruik-scenario, niet als universele wet.

**Tegenstrijdigheid 2 — GraphRAG nauwkeurigheidscijfers**: Microsoft's 80% claim is self-reported en niet onafhankelijk gerepliceerd in de geraadpleegde bronnen. Behoud scepticisme over precieze percentages.

**Open vraag 1**: Hoe verhoudt context rot zich op de specifieke 2026-modellen (Claude 4.7, GPT-5.4, Gemini 3)? Geen directe benchmarks gevonden — mogelijk niet publiek gepubliceerd op onderzoeksdatum.

**Open vraag 2**: Moet lane 4 (Privacy) ook de Privacy/Transparency guardrail-pagina's voeden? Aanbeveling: ja — differentiële privacy architectuur en GDPR-doelbinding zijn guardrail-content; PII-redactie als PTI-stap en citatie-traceerbaarheid zijn BB_03-content.

## Open vragen

1. 2026 frontier-model specifieke context-rot benchmarks niet beschikbaar (Claude 4.7, GPT-5.4 Gemini 3 — geen publieke data op onderzoeksdatum 2026-04-20)
2. Forte's primaire bron voor 25-50% claim niet gevonden — niet te verifiëren zonder toegang tot zijn cursusmateriaal
3. MCP-beveiligingsstatus is in actieve ontwikkeling; aanbevelingen kunnen verouderd zijn binnen maanden
