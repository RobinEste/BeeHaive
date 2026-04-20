# Dynamic Context als informatie-architectuur 2024-2026

**BB_03 Deep Research Rapport**
**Datum:** 2026-04-20
**Researcher-rondes:** 1 (4 parallelle lanes)
**Verificatie-pass:** PASS-WITH-NOTES

---

## Executive Summary

Context engineering is in 2025 uitgegroeid tot een erkende informatica-discipline. De verschuiving van "prompt engineering" naar een breder paradigma waarbij de kwaliteit, timing en structuur van contextuele informatie de AI-prestaties meer bepalen dan modelkeuze of prompting-vaardigheid werd in 2025 geformaliseerd: Tobi Lütke (CEO Shopify) definieerde het op 19 juni 2025 als *"the art of providing all the context for the task to be plausibly solvable by the LLM"* [1] (`verified`), en Gartner riep het in juli 2025 uit tot strategische prioriteit boven prompt engineering [2] (`unverified` — via secondaire bron).

Voor BB_03 Dynamic Context zijn drie empirische waarschuwingen leidend:

1. **Context rot degradeert prestaties universeel** — alle 18 geteste frontier-modellen (inclusief GPT-4.1, Claude Opus 4, Gemini 2.5 Pro) vertonen meetbare prestatiedaling bij langere context. Informatie in het midden van de context krijgt 30%+ lagere nauwkeurigheid dan informatie aan begin of einde [3][4] (`verified`).

2. **Stale context faalt stilzwijgend** — een verouderde kennisbank retourneert structureel correcte, zelfverzekerd geformuleerde antwoorden zonder enige foutindicator. Monitoring en event-triggered re-indexing zijn vereist [5] (`verified`).

3. **PII in de index lekt onbedoeld** — zonder pre-indexering redactie kunnen normale retrieval-operaties gevoelige informatie in antwoorden opnemen [6][7] (`verified`).

De productiepartronen voor alle BB_03-checklist-items zijn beschikbaar en bewezen: hybride retrieval met contextual reranking (67% minder fouten), gedifferentieerde freshness-drempels per documentcategorie, en modulaire memory-lagen (Mem0 voor persistente personalisatie, Letta voor autonome agenten).

---

## Sectie 1: Context rot en de grenzen van het context window

### 1.1 Het universele degradatiemechanisme

Context rot — prestatiedegradatie naarmate het context window groeit — is empirisch vastgesteld op alle 18 geteste frontier-modellen in Chroma's 2025 onderzoek [3] (`verified`). Drie mechanismen werken samen:

**Lost-in-the-Middle effect** [4] (`verified`): informatie in positie 5-15 van een reeks documenten krijgt 30%+ lagere nauwkeurigheid dan informatie aan het begin of einde. Origineel gedocumenteerd door Liu et al. (Stanford, TACL 2023) en sindsdien gerepliceerd. Het gaat niet om een eigenaardigheid van één model maar om een structurele eigenschap van transformer-aandachtsmechanismen.

**Attention dilution** (`inferred` — mechanistisch argument, niet direct gemeten): bij 100K tokens berekent een transformer ~10 miljard paargewijze aandachtsrelaties. Softmax-normalisatie verdeelt aandacht over alle tokens, waardoor individuele signalen verdunnen [3].

**Distractor interference** (`verified`): semantisch vergelijkbare maar irrelevante content degradeert prestaties actief — bijzonder problematisch in grote kennisbanken met overlappend vocabulaire [3].

### 1.2 Empirische prestatieverliezen op frontier-modellen

Adobe Research (februari 2025), two-hop redenering bij stijgende contextlengte [8] (`verified`):

| Model | Nauwkeurigheid kort | Nauwkeurigheid lang | Daling |
|-------|--------------------|--------------------|--------|
| GPT-4o | 99% | 70% | −29% |
| Claude 3.5 Sonnet | 88% | 30% | −58% |
| Gemini 2.5 Flash | 94% | 48% | −46% |
| Llama 4 Scout | 82% | 22% | −60% |

Chroma (2025): vroege en late context haalt 85-95% nauwkeurigheid; midden-secties zakken naar 76-82% [3] (`verified`).

*Noot: 2026-modelversies (Claude 4.7, GPT-5.4, Gemini 3) zijn niet in de beschikbare onderzoeksdata gemeten op onderzoeksdatum 2026-04-20. De degradatie-richting is consistent aangetoond; absolute waarden per modelversie variëren.* (`unverified` voor 2026-modellen)

### 1.3 Effectief bruikbaar context window

Context-kwaliteit overtreft context-grootte als ontwerpdoelstelling [9] (`inferred`). Enterprise-queries consumeren doorgaans 50K-100K tokens aan setup-context vóór daadwerkelijke redenering begint [9].

Frontier-model efficiëntie (2026, praktisch) [9] (`inferred` — aggregatie meerdere bronnen):

| Model | Geadverteerd | Praktische efficiëntie | Primaire beperking |
|-------|-------------|----------------------|-------------------|
| GPT-4.1 | 1M tokens | ~98% | Kosten bij schaal |
| Claude Opus 4 | 200K tokens | ~92% | KV-cache limiet |
| Gemini 2.5 Pro | 1M tokens | ~92% | Latency |
| Grok 3 | 1M tokens | 75-87% | Grootste gap |

**Over Forte's "25-50% bruikbaar" claim** (`blocked`): geen empirische primaire bron gevonden die dit exacte percentage als universele regel bevestigt. Beschikbare data wijst op model-afhankelijke efficiëntie. Praktisch advies voor BB_03: *organiseer context in minimum viable chunks, test empirisch per use case en model* — beter dan een universeel percentage te hanteren.

### 1.4 Multi-agent isolatie als architectuurpatroon

Multi-agent isolatie verbetert prestaties met 90.2% door zoekruis te bevatten in geïsoleerde context windows van subagents, in plaats van de primaire agent te vervuilen [3] (`verified`). Dit is het sterkste architectuurpatroon om context rot te mitigeren in agentic systemen.

---

## Sectie 2: Retrieval-architecturen — van RAG naar context engines

### 2.1 RAG evolueert naar intelligente context engines

RAG verschuift in 2025-2026 van een vaste ophaal-pipeline naar een "Context Engine" waarbij intelligente routing, hybride zoekstrategie en semantische verrijking de kern vormen [10] (`inferred`). Enterprise focus in 2026: pragmatische grootschalige adoptie waarbij RAG de fundamentele datalaag is voor alle AI-applicaties.

**PTI-pipelines (Parse-Transform-Index)** standaardiseren enterprise-ingestie [10]:
- Format parsing (PDF, ongestructureerde documenten)
- Semantische verrijking: samenvattingen, entiteit-extractie, vraag-generatie per chunk
- Hybride indexering: vector + keyword (BM25) + metadata filters

**Hybride search + cross-encoder reranking** is de standaard geworden in 2025, met 33-47% nauwkeurigheidsverbetering afhankelijk van querycomplexiteit [10] (`inferred`).

### 2.2 Contextual Retrieval — 67% minder retrievalfouten

Anthropic's Contextual Retrieval (2024) prepend 50-100 token contextuele samenvattingen aan chunks vóór indexering. Daardoor behoudt elk fragment zijn betekenis in isolatie — het lost-in-the-middle probleem op chunk-niveau [11] (`verified`):

| Aanpak | Reductie retrievalfouten |
|--------|--------------------------|
| Contextual Embeddings | 35% (5.7% → 3.7%) |
| + BM25 hybrid | 49% (5.7% → 2.9%) |
| + Reranking | 67% (5.7% → 1.9%) |

Kosten via prompt caching: ~$1.02 per miljoen document-tokens — economisch inzetbaar bij enterprise-schaal [11]. Aanbeveling: Voyage AI of Gemini embeddings + contextual BM25 + reranking + ophalen van 20 chunks.

### 2.3 GraphRAG voor complexe relatienetwerken

Microsoft's GraphRAG (open source) bouwt kennisgrafen waarbij entiteiten nodes en relaties edges zijn, gecombineerd met vector search [12] (`unverified` — nauwkeurigheidscijfers niet onafhankelijk geverifieerd; Microsoft docs bevatten geen kwantitatieve benchmarks):

- Verbeterde nauwkeurigheid voor multi-hop queries en globale vragen
- LazyGraphRAG (juni 2025) reduceerde indexeringskosten tot 0.1% van oorspronkelijk
- Zwakheid: 16.6% nauwkeurigheidsval voor tijdsgevoelige queries; 3-5× hogere initiële indexeringskosten
- Inzetbaar via Microsoft Discovery en Azure

Toepassingsdomein: complexe multi-hop redenering, narratieve datasets, kennisnetwerken. Niet geschikt voor frequent-veranderende of real-time data.

### 2.4 Intent-detectie en query-routing

Semantische routing classificeert user-intent en routeert naar gespecialiseerde kennisbronnen of retrieval-strategieën [13] (`inferred`):
- Praktisch maximum: 5-20 topics per router voor beheerbaarheid
- Amazon's REIC (EMNLP 2025): RAG-versterkte intent-classificatie overtreft fine-tuning bij klantenservice-schaal zonder hertraining [14] (`verified`)
- Adaptieve retrieval met reinforcement learning optimaliseert real-time bronkeuze op basis van querycomplexiteit [13]

---

## Sectie 3: Chunking, embeddings en context-opslag

### 3.1 Chunking — de meest onderschatte kwaliteitsvariable

Chunking-kwaliteit heeft meer impact op systeemprestaties dan LLM-keuze of embedding-model [15] (`inferred` — geciteerd als vuistregel in meerdere enterprise-gidsen). Aanbevelingen per documenttype [15][16]:

| Documenttype | Aanbevolen chunk-grootte | Overlappercentage |
|--------------|-------------------------|-------------------|
| Algemene tekst | 256-512 tokens | 20-30% |
| Policies/runbooks | Hiërarchisch: paragraaf index, sectie generatie | n.v.t. |
| Code/technische docs | 1.000-1.500 tokens | 10-20% |
| Chat-logs | 200-400 tokens | minimaal |

**Agentic chunking** (2025): AI-agent beslist dynamisch hoe documenten worden gesplitst op basis van structuur, dichtheid en content [16] (`inferred`).

Kwaliteitsvalidatie: handmatig review van ~50 willekeurige chunks om te controleren of elk fragment zelfstandig betekenisvol is als potentieel antwoord [15].

### 3.2 Embedding-modellen

Kritische architectuurregel: gebruik het **zelfde embedding-model** voor indexering én querying — anders verlies je de mathematische coherentie van de vectorruimte [15] (`verified`).

Aanbevelingen (2025-2026):
- **Voyage AI voyage-3-large**: beste MTEB-prestaties, 32K token context, $0.06/M tokens [16] (`inferred`)
- **BAAI/bge-large-en-v1.5**: open-source, lokale deployment voor regulated environments [15] (`verified`)
- Domeinspecifieke modellen voor medisch/juridisch gebruik: 20-40% betere retrieval-nauwkeurigheid dan generieke modellen [16]

### 3.3 Memory-lagen voor agenten

Three-tier architectuur voor agentic memory [10][17]:
1. **Working Memory**: huidige interactiestatus (in context window — vluchtig)
2. **Episodic Memory**: historische interacties (externe opslag — persistent)
3. **Semantic Memory**: geabstraheerde lessen, patronen en voorkeure (derived — langst-levend)

---

## Sectie 4: Agentic memory — productie-rijpheid

### 4.1 Mem0 — productie-rijpe personalisatielaag

Mem0 (mem0ai/mem0, ~48K GitHub stars, 14M downloads) biedt een pluggable memory layer voor bestaande agent-frameworks [17] (`verified`):

- **Extractiefase**: identificeert saillante feiten per berichtpaar → compact opgeslagen als natural language memories
- **Intelligente CRUD**: ADD / UPDATE / DELETE / NOOP op basis van vergelijking met bestaande memories (bijv. stadsverhuizing triggert automatisch DELETE van oude locatie)
- **LongMemEval benchmark**: 49.0% op temporele, multi-hop en knowledge-update scenarios [17]
- **Efficiëntie**: 26% verbetering t.o.v. OpenAI baseline; 91% lagere p95-latentie; >90% tokenkosten bespaard [18] (`verified`)
- **Compliance**: SOC 2 + HIPAA beschikbaar; AWS koos Mem0 als exclusive memory provider voor Agent SDK [18]
- **Beperking**: passieve semantische extractie; geen complexe multi-strategie retrieval voor complexe analyse [17]

### 4.2 Letta (voorheen MemGPT) — voor autonome agenten

Letta positioneert memory als expliciete eerste-klas agent-state component [17] (`verified`):
- **Drie-tier architectuur**: Core Memory (in context window = RAM), Archival Memory (persistent), Recall Memory (conversation history)
- **Self-editing memory**: agents cureren actief wat zij onthouden, inclusief verwijderen van verouderde feiten
- **Visual debugging** via Agent Development Environment
- **Beperkingen**: Python-only; significante architecturele lock-in; elke memory-operatie kost inference tokens

**Productie-rijpheid** (`inferred`):
- Mem0: productie-rijp voor personalisatie, CS-agents, voice agents, B2B copilots
- Letta: productie-rijp voor autonome agenten die geavanceerde self-managed memory vereisen
- Combinatie aanbevolen voor complexe systemen

### 4.3 MCP — standaard voor context-provisioning

Model Context Protocol (Anthropic, november 2024) standaardiseert hoe AI-systemen externe data en tools integreren [19] (`verified`):
- >5.800 community MCP-servers beschikbaar (april 2025)
- Drie context-datatypes: Domain Knowledge (RAG), Tool Metadata (tool-retrieval), Conversation State
- **Beveiligingsrisico's** (april 2025, actief probleem): prompt injection, tool-exfiltratie via permissiecombinaties, lookalike-tools [19]
- Context-governance moet MCP-serverautorisatie omvatten

---

## Sectie 5: Context actualisering en kwaliteitsborging

### 5.1 Het stille falen van stale context

Verouderde context faalt stilzwijgend: structureel correcte, zelfverzekerd geformuleerde antwoorden op basis van verouderde informatie — géén waarschuwingssignaal in de retrieval-response [5] (`verified`). Dit maakt monitoring en proactieve governance essentieel.

Vier freshness-dimensies [5] (`verified`):
1. **Content Age** — tijd sinds laatste menselijke verificatie/update
2. **Embedding Lag** — vertraging tussen bronupdate en vector-index refresh
3. **Stale Retrieval Rate** — fractie queries met verouderde documenten
4. **Coverage Drift** — percentage corpus voorbij staleness-drempel

### 5.2 Staleness-drempels per documentcategorie

| Categorie | Maximale verouderdheid |
|-----------|----------------------|
| Compliance / live pricing | Nul tolerantie |
| Policies & procedures | 24 uur |
| Referentiedocumenten | 30 dagen |
| Historische/contextuele materialen | 90 dagen |

(`verified` [5])

Composite freshness score < 85% → automatische alerts; < 70% → gebruikerswaarschuwing [5] (`verified`).

### 5.3 Re-indexing patronen

| Aanpak | Staleness window | Toepasselijkheid |
|--------|-----------------|-----------------|
| Nightly batch | Tot 24u | Statische kennisbanken |
| Hourly batch | Tot 60 min | Semi-dynamisch |
| Streaming CDC | Seconden | Compliance-kritisch / live pricing |

**Best practice** [15] (`verified`): event-triggered incrementele re-indexing op document-change events (Confluence, SharePoint) — effectiever dan volledig herindex op schema. LlamaIndex native connectors traceren document-hashes en herindexeren alleen gewijzigde bestanden.

### 5.4 Evaluatiemetrics voor productie-RAG

RAGAS-framework [15] (`verified`):
- Faithfulness > 0.90 (hallucinatie-preventie)
- Answer Relevancy > 0.85
- Context Recall > 0.80
- Context Precision > 0.75

Fallback bij retrieval score < 0.55: retourneer "geen betrouwbaar antwoord gevonden" in plaats van onbetrouwbaar antwoord genereren [15] (`verified`).

---

## Sectie 6: Privacy, PII en data-lineage

### 6.1 PII-lekkagerisico's in RAG

RAG-outputs riskeren PII-lekkage zonder extra privacy-safeguards [6][7] (`verified`). Twee aanvalsscenario's: directe extractie-aanvallen en onbedoelde lekkage via opgehaalde fragmenten.

**GraphRAG verhoogt dit risico** [20] (`verified`): kennisgrafen slaan relaties tussen entiteiten expliciet op, waardoor PII-reconstructie mogelijk is die bij vector-zoekopdrachten niet zou slagen.

### 6.2 Pre-indexering als meest effectieve filterstrategie

Pre-indexering redactie is effectiever dan post-retrieval filtering — PII die in de index zit is al opgeslagen en kan worden opgehaald [6] (`verified`):

1. **Deterministisch tokeniseren** voor gestructureerde identifiers (BSN, e-mail, IBAN)
2. **Contextuele redactie** voor vrije tekst
3. **Retrieval-filters** die gevoelige entiteiten uitsluiten op query-tijd
4. **Goedkeuringsworkflows** voor nieuwe kennisbronnen

**Differentiële privacy (DP-RAG)** [7] (`verified`): spendeert privacy-budget uitsluitend op tokens die gevoelige informatie vereisen. Superieure prestaties ten opzichte van niet-RAG baselines bij ε≈10 over diverse modellen en datasets.

**Privacy-utility tradeoff** [21] (`verified`): scherpere similarity-drempels verminderen PII-extractie-aanvallen maar verlagen systeemprestaties. Expliciete tradeoff die per use case gecalibreerd moet worden.

### 6.3 Data-lineage als GDPR-architectuurvereiste

Elke gegenereerde respons traceerbaar naar brondocument is non-negotiable voor gereguleerde sectoren [15] (`verified`). GDPR-relevante lineage-componenten:

1. **Document-provenance**: welke bronnen zijn opgehaald per respons?
2. **Embedding-timestamp**: wanneer zijn de vectors aangemaakt? (verouderde embeddings traceerbaar)
3. **Deletion-audit**: vectoren verwijderd na erasure-verzoek (recht op vergetelheid)
4. **Purpose-alignment**: gebruik aligned met oorspronkelijk verzameldoel (GDPR doelbinding)

**Observability-vereiste** (`inferred`): audit-trails moeten aantonen hoe pipelines PII hebben gemaskeerd, welke bronnen welke antwoorden hebben gevoed, en wanneer gecachte vectors zijn verwijderd [22].

---

## Tegenstrijdigheden

**Tegenstrijdigheid 1 — Forte's 25-50% vs. empirische efficiëntiedata**: Forte's "25-50% bruikbaar context window" staat haaks op recente model-efficiëntie-data (75-98% bij eenvoudige taken op geoptimaliseerde modellen). De spanning is deels oplosbaar: eenvoudige retrieval-taken presteren goed over lange context, terwijl complexe redenering-taken (twee-hop, multi-stap) fors degraderen. Forte's claim is contextueel gemotiveerd door een specifiek gebruik-scenario, maar als universele wet niet onderbouwbaar. (`blocked` voor de exacte claim)

**Tegenstrijdigheid 2 — GraphRAG nauwkeurigheidscijfers**: Percentages als "80% vs 50%" zijn niet terug te vinden in de officiële Microsoft GraphRAG documentatie — de officiële docs bevatten alleen kwalitatieve beschrijvingen. Behandel als `unverified` tot onafhankelijke replicatie beschikbaar is.

---

## Open vragen

1. **2026-modelversies**: Context rot op Claude 4.7, GPT-5.4, Gemini 3 — geen publieke benchmarks beschikbaar op onderzoeksdatum 2026-04-20. Degradatie-richting consistent; absolute waarden onbekend.
2. **Forte's primaire bron**: De 25-50%-claim is niet traceerbaar naar een empirisch onderzoek zonder toegang tot zijn cursusmateriaal (bron-080/081 zijn vault-lokaal).
3. **MCP-beveiliging**: Actief evoluerend risico-landschap; aanbevelingen kunnen binnen maanden verouderen.
4. **Lane 4 guardrail-sync**: Differentiële privacy architectuur en GDPR-doelbinding zijn primair Privacy Guardrail-content; geadviseerd wordt dit bij synthese van de guardrail-pagina's te benutten.

---

## Sources

Alle bronnen geraadpleegd op 2026-04-20. Verificatiestatus per claim staat inline.

### Canonieke primaire bronnen

- [1] Tobi Lütke — "Context engineering" definitie-tweet (19 juni 2025) — https://x.com/tobi/status/1935533422589399127
- [4] Liu et al. — Lost in the Middle: How Language Models Use Long Contexts (TACL 2023) — https://arxiv.org/abs/2307.03172 (MIT Press: https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00638/119630/)
- [11] Anthropic — Contextual Retrieval (2024) — https://www.anthropic.com/news/contextual-retrieval
- [12] Microsoft GraphRAG — https://microsoft.github.io/graphrag/ en https://www.microsoft.com/en-us/research/project/graphrag/
- [18] Chhikara et al. — Mem0: Building Production-Ready AI Agents (Arxiv 2504.19413, april 2025) — https://arxiv.org/abs/2504.19413
- [7] Arxiv — Privacy-Preserving RAG with Differential Privacy (2412.04697, v2 2025) — https://arxiv.org/abs/2412.04697
- [20] Arxiv — Exposing Privacy Risks in Graph RAG (2508.17222, 2025) — https://arxiv.org/pdf/2508.17222
- [21] ScienceDirect / ACM — Mitigating Privacy Risks in RAG via Entity Perturbation (2025) — https://www.sciencedirect.com/science/article/abs/pii/S0306457325000913
- [14] Amazon/ACL 2025 — REIC: RAG-Enhanced Intent Classification at Scale — https://arxiv.org/abs/2506.00210

### Context rot en benchmarks

- [3] Chroma Research / Morph — Context Rot: Complete Guide (2025) — https://www.morphllm.com/context-rot
- [8] Timothy Lee / Understanding AI — Context Rot: The Emerging Challenge (2025) — https://www.understandingai.org/p/context-rot-the-emerging-challenge
- [9] Atlan — LLM Context Window Limitations 2026 — https://atlan.com/know/llm-context-window-limitations/

### Architectuur en RAG

- [10] RAGFlow — From RAG to Context: 2025 Year-End Review — https://ragflow.io/blog/rag-review-2025-from-rag-to-context
- [13] Medium / Timothé Pearce — Building a RAG Router in 2025 — https://medium.com/@tim_pearce/building-a-rag-router-in-2025-e0e9d99efe44
- [17] Vectorize.io — Mem0 vs Letta: AI Agent Memory Compared 2026 — https://vectorize.io/articles/mem0-vs-letta
- [19] Wikipedia — Model Context Protocol — https://en.wikipedia.org/wiki/Model_Context_Protocol

### Enterprise praktijk en governance

- [2] Atlan — What Is Context Engineering 2026 — https://atlan.com/know/what-is-context-engineering/
- [5] Atlan — LLM Knowledge Base Freshness Scoring — https://atlan.com/know/llm-knowledge-base-freshness-scoring/
- [15] Towards Data Science — Grounding Your LLM: Enterprise Knowledge Bases — https://towardsdatascience.com/grounding-your-llm-a-practical-guide-to-rag-for-enterprise-knowledge-bases/
- [16] Weaviate — Chunking Strategies for RAG (2025) — https://weaviate.io/blog/chunking-strategies-for-rag
- [22] Aparavi — Reinventing Data Protection for the AI Era 2026 — https://aparavi.com/whitepapers/reinventing-data-protection-for-the-ai-era-2026-whitepaper/
- [6] Protecto.ai — AI Data Privacy Concepts & Best Practices — https://www.protecto.ai/blog/ai-data-privacy/
- [Atlan Data Quality] Atlan — LLM Knowledge Base Data Quality — https://atlan.com/know/llm-knowledge-base-data-quality/
- [Simon Willison] Simon Willison — Agentic Engineering Patterns (februari 2026) — https://simonwillison.net/2026/Feb/23/agentic-engineering-patterns/
- [Snorkel AI] Snorkel AI — Long Context Models in the Enterprise — https://snorkel.ai/blog/long-context-models-in-the-enterprise-benchmarks-and-beyond/

### Kerncitaten

- Tobi Lütke: *"Context engineering is the art of providing all the context for the task to be plausibly solvable by the LLM."* — x.com/tobi/status/1935533422589399127
- Chroma Research: *"All 18 models degrade with length — even frontier models like GPT-4.1, Claude Opus 4, and Gemini 2.5 Pro."* — morphllm.com/context-rot
- Anthropic: *"Context must be treated as a finite resource with diminishing marginal returns."* — via understandingai.org/p/context-rot-the-emerging-challenge
- Atlan: *"Context quality matters more than context window size."* — atlan.com/know/llm-context-window-limitations/
