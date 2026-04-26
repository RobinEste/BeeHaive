# Research: Architectuurpatronen voor AI-systemen — BB_02 Client Blueprint

**Researcher:** researcher-architectuur
**Dimensie:** Architectuurpatronen, single/multi-agent beslismatrix, MCP, RAG vs fine-tuning (2024-2026)
**Datum:** 2026-04-26

## Samenvatting (1 zin)

Anthropic's 5 composable workflow-patronen bieden een bewezen besliskader voor AI-architectuur, waarbij de kernregel is: begin met het eenvoudigste dat werkt en voeg complexiteit alleen toe als evaluatie aantoont dat het noodzakelijk is.

## Bevindingen

### 1. Anthropic's 5 Workflow-patronen + Autonome Agents

Anthropic publiceerde "Building Effective Agents" als authoritative referentie-architectuur [1, 2]. Het document onderscheidt twee categorieën:

**Workflows** (LLMs en tools in vooraf gedefinieerde codepaden):

1. **Prompt Chaining:** Sequentiële LLM-calls waarbij elke stap de output van de vorige verwerkt. Ideaal voor decomposeerbare taken die latency inruilen voor nauwkeurigheid (bijv. marketingcopy genereren → vertalen → kwaliteitscheck). (`verified`)

2. **Routing:** Input classificeren naar gespecialiseerde downstream-handlers. Best inzetbaar bij heterogene taken waarbij verschillende categorieën een aparte aanpak vereisen (bijv. klantvragen routeren op type). (`verified`)

3. **Parallelisatie:** Meerdere LLM-calls simultaan uitvoeren via *sectioning* (parallelle deeltaken) of *voting* (meerdere pogingen, meerderheid wint). Nuttig wanneer deelwerk snelheid kan verhogen of meerdere perspectieven betrouwbaarheid verbeteren. (`verified`)

4. **Orchestrator-Workers:** Een centrale LLM decomposeert taken dynamisch en delegeert naar workers. Geschikt voor onvoorspelbare deeltaken waarbij de werklast afhangt van de input (bijv. multi-bestand codewijzigingen). (`verified`)

5. **Evaluator-Optimizer:** Iteratieve verfijning waarbij één LLM genereert en een andere feedback geeft. Effectief wanneer duidelijke evaluatiecriteria bestaan en menselijk-achtige iteratie de output verbetert. (`verified`)

**Autonome Agents** (LLMs met tools in feedbacklus, minimale human intervention): gereserveerd voor open-ended problemen "waarbij het moeilijk of onmogelijk is om het benodigde aantal stappen van tevoren te voorspellen" [1]. (`verified`)

### 2. De kernregel: begin simpel

Anthropic's fundamentele richtlijn: *start met een eenvoudige LLM-call geoptimaliseerd met retrieval en voorbeelden. Voeg complexiteit alleen toe wanneer eenvoudigere oplossingen aantoonbaar tekortkomen.* [1] (`verified`)

Drie kerneigenschappen voor implementatie [1]:
- **Eenvoud:** houd agent-ontwerp simpel
- **Transparantie:** laat planningsstappen expliciet zien
- **Tool-interface design:** investeer evenveel in tools als in prompts

In Anthropic's eigen SWE-bench agent werd meer tijd besteed aan tool-optimalisatie dan aan algehele prompt-optimalisatie. ("Treat agent-computer interfaces like human-computer interface design.") (`verified` via directe fetch)

### 3. Single-agent vs. Multi-agent: beslismatrix

Anthropic's eigen multi-agent research system biedt concrete benchmarking-data [3]:
- Multi-agent (Claude Opus 4 als lead + Claude Sonnet 4 subagents) presteert 90,2% beter dan single-agent Claude Opus 4 op hun interne research-evaluatie
- Nadeel: multi-agent verbruikt ~15× meer tokens dan chat-interacties

**Multi-agent is geschikt voor [3]:**
- Taken met hoge parallelisatiepotentieel
- Informatie die één contextvenster overschrijdt
- Complexe tool-integraties

**Multi-agent is *niet* geschikt voor [3]:**
- Taken die gedeelde context vereisen tussen alle agents
- Zware inter-agent coördinatie-afhankelijkheden
- De meeste coderingstaken (onvoldoende paralleliseerbare componenten)

(`verified` via directe fetch Anthropic engineering-artikel)

### 4. MCP: Model Context Protocol als architectuurstandaard

Anthropic introduceerde het Model Context Protocol (MCP) in november 2024 als open standaard voor AI-tool-integraties [4]. Kernarchitectuur:

- **Client-server architectuur** geïnspireerd op Language Server Protocol (LSP)
- **JSON-RPC 2.0** als onderliggend berichtenformaat
- **MCP Servers:** lichtgewicht applicaties die specifieke backend-capabilities exposen (databases, APIs, filesystems)
- **MCP Clients:** AI-applicaties die verbinding maken met servers

Adoptie-momentum [4]: 97M+ maandelijkse SDK-downloads per medio 2025; server-downloads groeiden van ~100.000 in november 2024 naar 8 miljoen in april 2025. OpenAI adopteerde MCP officieel in maart 2025. In december 2025 gedelegeerd aan de Agentic AI Foundation (AAIF) — daarmee vendor-neutraal.

**Architectuurregel voor blueprint:** MCP is de standaard tooling-laag voor agent-systemen. In een blueprint dient de vraag "welke tools heeft de agent nodig en via welke interface?" beantwoord te worden met MCP als default protocol. (`inferred` op basis van adoptiedata en ecosystem-positie)

**Beveiligingsrisico's (niet negeren):** In april 2025 identificeerden security-onderzoekers prompt injection, tool-permissions die data-exfiltratie mogelijk maken, en lookalike tools die vertrouwde tools kunnen vervangen. [4] (`verified`)

### 5. RAG vs. Fine-tuning vs. Agents: architectuurlagen

Enterprise-AI-architectuur bestaat uit drie onderscheiden lagen [5, 6]:
- **RAG (kennislaag):** dynamische toegang tot actuele informatie zonder model-hertraining. Best voor frequent veranderende kennis (regelgeving, productdocumentatie, operationele data)
- **Fine-tuning (specialisatielaag):** stabiel domeingedrag inbakken. Best voor statische domeinen met hoog volume/lage latency
- **Agents (executielaag):** processen uitvoeren via tools. Best wanneer het doel is bedrijfsprocessen te *uitvoeren* in plaats van *vragen te beantwoorden*

Dominante patroon 2026: hybride architectuur die RAG + fine-tuning + agents combineert. ~60% van enterprise AI-implementaties gebruikt hybride architecturen [5]. (`unverified` — op basis van marktanalyses zonder directe URL-verificatie)

**Blueprint-implicatie:** in BB_02 moet de vraag "welke architectuurlaag?" expliciet gesteld worden per use case. De meest gemaakte fout: een agent bouwen waar RAG voldoende is.

### 6. Vergelijking met andere referentie-architecturen

Anthropic's 5 patronen worden onafhankelijk bevestigd door andere grote spelers:

- **Anthropic** (Building Effective Agents): 5 workflow-patronen + autonomous agents [1]
- **Microsoft** (AI Decision Framework): vergelijkbare focus op routing, orchestratie, en evaluatiecriteria [7]
- **Google/AWS** (diverse publicaties): vergelijkbare orchestrator-worker en parallelisatiepatronen zichtbaar in hun agent starter kits

(`inferred` — Microsoft en Google/AWS architecturen bevestigen dezelfde basispatronen; geen directe vergelijkende bron gevonden met alle vier partijen naast elkaar)

Opvallende consensus: alle grote spelers benadrukken dat multi-agent complexiteit pas gerechtvaardigd is na bewijs dat een simpeler patroon tekortschiet.

## Evidence Table

| # | Bron | URL | Type | Key claim | Confidence |
|---|------|-----|------|-----------|------------|
| 1 | Anthropic — Building Effective Agents (research) | https://www.anthropic.com/research/building-effective-agents | primary | 5 workflow-patronen, kernprincipes, beslisregels | high |
| 2 | Anthropic — Building Effective Agents (resources) | https://resources.anthropic.com/building-effective-agents | primary | Architectuurpatronen en implementatieframeworks | high |
| 3 | Anthropic Engineering — Multi-agent research system | https://www.anthropic.com/engineering/multi-agent-research-system | primary | 90.2% prestatieverbetering, 15x token-gebruik, wanneer werkt het | high |
| 4 | Anthropic — Introducing the Model Context Protocol | https://www.anthropic.com/news/model-context-protocol | primary | MCP architectuur, adoptie, beveiligingsrisico's | high |
| 5 | Orq.ai — RAG Architecture Explained | https://orq.ai/blog/rag-architecture | secondary | RAG vs fine-tuning vs agents architectuurlagen | medium |
| 6 | Techment — RAG vs Fine-Tuning vs AI Agents LLM Strategy | https://www.techment.com/blogs/rag-vs-fine-tuning-vs-ai-agents-llm-strategy/ | secondary | Drie-lagenmodel, 60% hybride architecturen | medium |
| 7 | Microsoft — AI Decision Framework (GitHub) | https://github.com/microsoft/Microsoft-AI-Decision-Framework | primary | Vergelijkbare patronen, governance-focus | medium |

## Coverage Status

- **Gecheckt direct:** bronnen 1 (Anthropic research), 3 (multi-agent engineering), volledig gefetcht en gelezen
- **Blijft onzeker:** 60% hybride-architectuur-claim (marktrapport, niet direct geverifieerd); Microsoft en Google/AWS patroonvergelijking indirect
- **Niet afgerond:** IBM MCP-architectuurpatronen artikel (403-fout bij fetch); directe vergelijking Anthropic/Microsoft/Google naast elkaar

## Sources

1. Anthropic — Building Effective Agents — https://www.anthropic.com/research/building-effective-agents
2. Anthropic Resources — Building Effective AI Agents: Architecture Patterns — https://resources.anthropic.com/building-effective-agents
3. Anthropic Engineering — How We Built Our Multi-Agent Research System — https://www.anthropic.com/engineering/multi-agent-research-system
4. Anthropic — Introducing the Model Context Protocol — https://www.anthropic.com/news/model-context-protocol
5. Orq.ai — RAG Architecture Explained: A Comprehensive Guide [2026] — https://orq.ai/blog/rag-architecture
6. Techment — RAG vs Fine-Tuning vs AI Agents: Choosing the Right LLM Strategy — https://www.techment.com/blogs/rag-vs-fine-tuning-vs-ai-agents-llm-strategy/
7. Microsoft — Microsoft AI Decision Framework (GitHub) — https://github.com/microsoft/Microsoft-AI-Decision-Framework
8. AetherLink — RAG, MCP and Agentic AI: Architecture Patterns for 2026 — https://aetherlink.ai/en/blog/rag-mcp-and-agentic-ai-architecture-patterns-for-2026
