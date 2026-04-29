# Research: Praktijk & Ecosysteem — Tool Integration (BB_05)

**Researcher:** researcher-3
**Dimensie:** Toolkits (LangChain, LlamaIndex, MCP ecosystem), toolcategorieën, computer use, productielandschap
**Datum:** 2026-04-29

## Samenvatting (1 zin)

Het tool integration ecosysteem is gematureerd tot een gelaagd stack: tools zijn gecategoriseerd (RAG/search, code execution, databases, browser/RPA, APIs), frameworks (LangChain, LlamaIndex) leveren abstracties, MCP fungeert als universele adapter, en computer use is de catch-all voor systemen zonder API.

## Bevindingen

### 1. Toolcategorieën — het landscape

Het productielandschap kent vijf hoofdcategorieën tools: [1, 2] (`verified`)

**Categorie 1: Search & RAG** (meest ingezet)
- Webzoekopdrachten (Exa, Tavily, SerpAPI, Anthropic web_search server tool)
- Vector database queries (Pinecone, Weaviate, Qdrant, pgvector/PostgreSQL)
- Hybrid retrieval (keyword + vector + reranking)
- Semantische search over interne kennisbanken

Keuzecriterium: Pinecone voor managed/zero-ops; pgvector voor bestaande PostgreSQL-infra; Qdrant voor snelheid bij high-volume. [3] (`verified` — deploybase.ai directory)

**Categorie 2: Code Execution** (hoog risico, geïsoleerd vereist)
- Anthropic server tool: `code_execution` (sandboxed op Anthropic infrastructure)
- Zelf-gehoste sandbox (Docker, e2b, Daytona)
- Programmatic Tool Calling gebruikt `code_execution` als orchestratielaag

Veiligheidseis: code execution altijd in geïsoleerde sandbox. Nooit directe toegang tot host filesystem of netwerk zonder expliciete whitelist.

**Categorie 3: Databases & interne systemen**
- SQL-databases (query via ORM of parameterized queries; nooit raw SQL met user input)
- NoSQL/document stores
- CRM, ERP, ticketing systemen via REST API
- Interne kennisbanken

**Categorie 4: Browser & Computer Use**
- Playwright-gebaseerde browser agents (AgentQL, Hyperbrowser)
- Anthropic Computer Use tool (`computer_20251124`) — volledige desktop GUI
- Web scraping en data extractie

Computer use is de meest generieke maar ook de traagste optie (elke actie vereist screenshot roundtrip). Gebruik narrowere tools wanneer die beschikbaar zijn; reserveer computer use voor legacy software zonder API, visuele verificatiestappen, of workflows die meerdere desktop-apps overspannen. [4] (`verified` — Anthropic computer use docs)

**Categorie 5: Externe APIs & RPA**
- REST API calls (OAuth, API-key auth)
- Webhooks en event-driven integraties
- Robotic Process Automation voor legacy systemen
- Betalingen (Stripe, Mollie)
- Communicatie (Slack, email, SMS)

### 2. Frameworks: LangChain vs. LlamaIndex

**LangChain**: orchestratie-first. Sterk in agents, tool-calling, multi-turn planning, externe API-integraties. Ecosystem: 100+ tool-integrations, LangGraph voor stateful orchestration, LangSmith voor monitoring. [5] (`verified` — devtechinsights.com vergelijking)

Beste keuze wanneer:
- Agentic behavior centraal staat (plan, tool, observe, repeat)
- Multi-step task automation
- Orchestratie tussen meerdere LLMs en derde-diensten

**LlamaIndex**: RAG-first. Sterk in document-ingestie, chunking, indexing, retrieval quality, evaluatie. [5] (`verified`)

Beste keuze wanneer:
- Retrieval-kwaliteit kritisch is
- Documentverwerking en kennisbanken centraal staan
- Evaluatie van RAG-pipelines gewenst

**Productie-combo**: LlamaIndex voor ingestion & retrieval, LangChain voor orchestratie & agents. LlamaIndex retourneert de meest relevante docs; LangChain organiseert de multi-step flow. Beide frameworks hebben native MCP-integratie. [5] (`verified`)

### 3. MCP Ecosysteem in productie

**Status 2026:** MCP is geadopteerd als de-facto standaard voor tool-koppeling door OpenAI, Google, Microsoft, Cloudflare en tientallen tool-vendors. Meer dan 5.000 community-contributed servers. [6] (`verified` — agnt.one)

**Pre-built connectors:** Anthropic biedt een repository van pre-built connectors (GitHub, Slack, Google Drive). API-first bedrijven (Stripe, GitHub, Postman) zien MCP als primair distribution channel. [6] (`verified`)

**Productie-deployment:** 
- Development: stdio transport (eenvoudig, direct debuggable)
- Productie: Streamable HTTP transport (remote access, multi-client support, OAuth 2.1)
- Cloudflare Workers: MCP servers als cloud-native dienst, globally accessible

**Agents als MCP servers:** Een agent kan zichzelf als MCP server exposen — andere agents kunnen hem aanroepen over hetzelfde protocol. Hierdoor ontstaat een vendor-neutraal multi-agent ecosysteem. [7] (`verified` — mcp-agent.com)

### 4. Computer Use in productie

Anthropic's computer use maakt het mogelijk voor Claude om een volledig desktop-systeem te bedienen via screenshots, muisklikken en toetsaanslagen. [4] (`verified`)

Implementatievereisten:
- Docker-container voor isolatie (verplicht veiligheidseis)
- Agent loop: Claude vraagt actie → applicatie voert uit → screenshot terug → herhaal
- Beveiligingseis: Anthropic adviseert om computer use te beperken tot een geïsoleerde VM of container; verbinding met kritische systemen te vermijden

Toevoeging van andere tools naast computer use via dezelfde `tools`-array is mogelijk (bash tool, text editor tool, custom tools).

Praktisch gebruik:
- Legacy software zonder API
- Workflows die meerdere desktop-applicaties overspannen
- Visuele verificatiestappen (screenshots vergelijken)

Beperking: langzamer dan API-gebaseerde integraties. Computer use als catch-all, niet als eerste keuze.

### 5. Observability en monitoring

Productie-observability voor tool integration rust op drie pijlers: [5, 8] (`verified` — devtechinsights.com + AI Platforms 2026 guide)

1. **Traces per tool call**: welke tool aangeroepen, met welke parameters, hoe lang, wat retourneerde het
2. **Token-tracking**: input- en output-tokens per tool-aanroep (tools-array consumeert tokens)
3. **Kwaliteitsmetrieken**: taak-succespercentage per tool, error rates, retry counts

Tooling:
- LangSmith (LangChain native, uitstekende traces)
- Langfuse (open source alternatief)
- Datadog AI Observability
- Platform-native: Vertex AI monitoring, Azure AI Foundry telemetry

**Anti-patroon**: tools alleen monitoren op latency en beschikbaarheid, niet op kwaliteit. Een tool die 95% uptime heeft maar 20% verkeerde resultaten levert, is een productiefout die je zonder kwaliteitsmonitoring niet ziet.

### 6. Tooling voor schema-management en versioning

Naarmate tool-catalogi groeien (10+ tools) worden schema-management en versioning kritisch. [9] (`inferred` — brightlume.ai + meerdere bronnen)

Best practices:
- Behandel tool-schemas als code: versiebeheer in Git, pull requests voor wijzigingen
- Semantic versioning voor schema-updates: *major* bij breaking changes (parameternaam wijzigt), *minor* bij nieuwe optionele parameters, *patch* bij beschrijvingsverbeteringen
- Schema-registry voor dynamische discovery (vergelijkbaar met PromptOps voor prompts)
- Test suite per tool: happy path + edge cases + adversarial inputs (prompt injection tests)

**MCP als schema-management oplossing**: één MCP-conforme definitie werkt overal. Dynamische tool discovery via `tools/list_changed` notifications.

### 7. Kosten van tool integration

Tools hebben een kostencomponent die buiten het LLM-model-gebruik valt: [1] (`verified` — Anthropic pricing docs)

- Tools-array tokens: elke tool-definitie telt als input-tokens
- Bij Claude Opus 4.7 voegt 1 tool ~313–346 extra system prompt tokens toe
- Server tools (web_search): usage-based pricing per uitgevoerde search
- Tool results in context: kunnen context window snel vullen bij lange responses

Kostenbeheer:
- Deferred loading (tools niet upfront laden)
- Tool Search server tool (lazy loading van grote catalogi)
- Prompt caching: tool schemas worden gecached (cache-hit als tool-lijst niet wijzigt)
- Minimal tools per request: geef agent alleen tools die relevant zijn voor de huidige taak

## Evidence Table

| # | Bron | URL | Type | Key claim | Confidence |
|---|------|-----|------|-----------|------------|
| 1 | Anthropic Tool Reference | https://console.anthropic.com/docs/en/agents-and-tools/tool-use/tool-reference | primary | server vs. client tools, pricing, defer_loading | high |
| 2 | xAI Docs — Tools Overview | https://docs.x.ai/docs/guides/tools/overview | primary | toolcategorieen (built-in vs. function calling) | medium |
| 3 | DeployBase — AI Tools Directory | https://deploybase.ai/articles/ai-tools-directory | secondary | vector DB vergelijking, RAG tools | medium |
| 4 | Anthropic — Computer Use | https://docs.anthropic.com/en/docs/agents-and-tools/computer-use | primary | computer use implementatievereisten, veiligheid | high |
| 5 | DevTechInsights — LangChain vs LlamaIndex | https://devtechinsights.com/langchain-vs-llamaindex-2025/ | secondary | framework vergelijking, combo-gebruik | medium |
| 6 | agnt.one — MCP Standard | https://agnt.one/blog/the-model-context-protocol-for-ai-agents | secondary | MCP adoptie, pre-built connectors, 5000+ servers | medium |
| 7 | mcp-agent.com | https://mcp-agent.com/ | secondary | agents als MCP servers | medium |
| 8 | AIToolsBusiness — AI Agent Platforms 2026 | https://aitoolsbusiness.com/ai-agents-platforms/ | secondary | observability tooling, platform vergelijking | medium |
| 9 | Brightlume AI — Enterprise Tool Use | https://brightlume.ai/blog/tool-use-patterns-enterprise-ai-agents | secondary | schema versioning, RBAC, namespacing | high |

## Coverage Status

- **Gecheckt direct:** Bronnen 1, 4, 5 — volledig gelezen; overige via highlights
- **Blijft onzeker:** Specifieke pricing van computer use token overhead (niet vermeld in gelezen docs)
- **Niet afgerond:** Gedetailleerde vergelijking van RPA-tools (UiPath, Windmill) als AI tool integration layer

## Sources

1. Anthropic — Tool Reference — https://console.anthropic.com/docs/en/agents-and-tools/tool-use/tool-reference
2. xAI Docs — Tools Overview — https://docs.x.ai/docs/guides/tools/overview
3. DeployBase — AI Tools Directory (393 tools, 59 categories) — https://deploybase.ai/articles/ai-tools-directory
4. Anthropic — Computer Use — https://docs.anthropic.com/en/docs/agents-and-tools/computer-use
5. DevTechInsights — LangChain vs LlamaIndex (2026) — https://devtechinsights.com/langchain-vs-llamaindex-2025/
6. agnt.one — Model Context Protocol for AI Agents — https://agnt.one/blog/the-model-context-protocol-for-ai-agents
7. mcp-agent.com — Build Agents with MCP — https://mcp-agent.com/
8. AIToolsBusiness — AI Agent Platforms 2026 — https://aitoolsbusiness.com/ai-agents-platforms/
9. Brightlume AI — Tool Use Patterns for Enterprise AI Agents — https://brightlume.ai/blog/tool-use-patterns-enterprise-ai-agents
