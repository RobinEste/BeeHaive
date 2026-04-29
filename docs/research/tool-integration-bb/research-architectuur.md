# Research: Architectuur & Patronen — Tool Integration (BB_05)

**Researcher:** researcher-1
**Dimensie:** Architectuur & patronen — function calling specs, MCP protocol, tool types, agentic tool use patronen
**Datum:** 2026-04-29

## Samenvatting (1 zin)

Tool integration heeft zich van een fragiel experiment (één JSON-schema, hoop-het-beste) ontwikkeld tot een rijpe productiepraktijk met gestandaardiseerde protocollen (MCP), parallelle tool execution, programmatische orchestratie en geteste architectuurpatronen.

## Bevindingen

### 1. Hoe function calling werkt: het fundamentele mechanisme

Function calling (ook: tool use) is het mechanisme waarmee een LLM zijn intentie declareert om een externe functie aan te roepen. Het model voert de functie zelf niet uit; het retourneert een gestructureerd tool-call-blok. De applicatie voert de functie uit en geeft het resultaat terug. [1] (`verified` — directe Anthropic-docs)

De stroom voor client-side tools:
1. Applicatie stuurt bericht met `tools`-array (naam, beschrijving, JSON-schema per tool)
2. Model retourneert `stop_reason: "tool_use"` + één of meer `tool_use`-blokken
3. Applicatie voert de tool uit
4. Applicatie stuurt `tool_result` terug naar model
5. Model integreert resultaat en vervolgt

Anthropic gebruikt `tool_use`-content-blocks met een `tool_use_id` voor matching. OpenAI gebruikt een vergelijkbaar `tools`-array-model. Beide APIs zijn conceptueel identiek; de veldnamen verschillen. [2] (`verified` — EngineersOfAI docs)

**Cruciale bevinding:** Het model besluit óf en welke tool aan te roepen op basis van de tool-beschrijving — de description-string is het primaire stuursignaal. Een vage beschrijving leidt direct tot verkeerde tool-selectie. [3] (`verified` — webcoderspeed.com)

### 2. Server-side vs. client-side tools

Anthropic maakt een expliciete scheiding: [1] (`verified`)
- **Client tools**: code draait in je eigen applicatie (user-defined tools, bash, text_editor, computer). Claude retourneert een tool_use-blok; jij voert uit.
- **Server tools**: Anthropic voert uit op eigen infrastructuur (web_search, code_execution, web_fetch, tool_search). Geen implementatie vereist aan de kant van de ontwikkelaar.

Voordeel van Anthropic-schema tools (bash, computer, text_editor): deze schema's zijn trained-in. Claude heeft geoptimaliseerd op duizenden succesvolle trajectories met exact deze tool signatures. Betrouwbaarheid is hoger dan met een zelfgebouwde equivalent. [4] (`verified` — Anthropic how-tool-use-works docs)

### 3. Programmatic Tool Calling (PTC) — nieuwe architectuurvorm 2025/2026

Traditioneel: voor elke tool-aanroep een roundtrip door het model. Met PTC schrijft Claude Python-code die meerdere tools aanroept, intermediate resultaten verwerkt, en één eindresultaat levert — alles binnen één turn. [5] (`verified` — Anthropic programmatic-tool-calling docs + AI Workflow Lab)

Voordelen:
- Drastisch minder latency bij multi-tool workflows
- Minder token-consumptie (intermediaire resultaten komen niet in het context window)
- Op agentic search benchmarks (BrowseComp, DeepSearchQA) was PTC de doorslaggevende factor voor betere prestaties dan menselijke experts

PTC vereist dat tools worden omgezet naar async Python functies. Code draait in een sandboxed container.

### 4. Parallelle tool execution

Moderne LLMs kunnen meerdere onafhankelijke tools simultaan aanroepen. Sequentieel (search → wacht → calculate → wacht) wordt vervangen door één batch. De applicatielaag moet alle `tool_use`-blokken verwerken en alle resultaten samen terugsturen. [2] (`verified`)

Praktische implicatie: de agentic loop moet itereren over *alle* `tool_use`-blokken, niet alleen de eerste.

### 5. Architectuurpatronen voor tool orchestratie

Vier productierelevante patronen: [6] (`verified` — brightlume.ai enterprise tool use)

**ReAct (meest gebruikt)**: Reden → Actie (tool call) → Observatie → herhaal. Het model redeneert wat te doen, roept een tool aan, observeert het resultaat, en verwerkt dat in de volgende stap. Meest stabiel in productie.

**Router + Specialisten**: Een klein, snel model routeert naar een gespecialiseerde handler. Het grote model wordt alleen ingezet waar nodig. Kostenefficiënt bij hoog volume.

**Plan-Then-Execute**: Scheid de planfase van de uitvoeringsfase. Het plan wordt vastgelegd voordat user-content en tool-resultaten in beeld komen. Kritisch voor prompt injection-preventie.

**Parallelle Decomposition**: Taak opgesplitst in onafhankelijke subtaken die simultaan worden uitgevoerd. Vereist dat subtaken daadwerkelijk disjoint zijn.

Productie-agents combineren typisch meerdere patronen. Routing voor classificatie, ReAct voor uitvoering, Plan-Then-Execute als veiligheidslaag. [6] (`inferred` — brightlume.ai + overige bronnen)

### 6. Tool schema design — de kritische interface

Het JSON-schema is het contract tussen het LLM en de tool. Kwaliteit van het schema bepaalt kwaliteit van de tool-selectie. [3, 7] (`verified`)

Best practices voor tool schemas:
- **Naam**: snake_case, action-oriented (`get_customer_orders`, niet `data`), max 64 tekens
- **Beschrijving**: vertel wanneer de tool te gebruiken en wanneer niet ("Use this when X. Do not use for Y")
- **Parameters**: gebruik `enum` voor eindige valueset (elimineert hallucinaties); gebruik `integer` wanneer gehele getallen vereist; mark required expliciet
- **Constraints**: valideer format, lengte, bereik in het schema zelf
- **`additionalProperties: false`**: voorkom onverwachte velden
- **`strict: true`** (Anthropic): garandeert dat Claude's tool calls altijd exact het schema matchen [1] (`verified`)

Anti-patroon: schema's met meer dan 5 nesting-levels zijn minder betrouwbaar. Vage descriptions leiden tot onjuiste tool-selectie. Te veel tools tegelijk in context verhoogt cognitieve belasting. [3] (`inferred`)

### 7. Tool Search en deferred loading

Bij catalogi met tientallen tot honderden tools is het onpraktisch om alle schemas tegelijk in de context te laden. Anthropic's Tool Search tool laat Claude zoeken in een tool-catalogus. Tools met `defer_loading: true` worden niet upfront geladen. Cruciaal: deferred loading behoudt de prompt-cache; nieuwe tools kunnen worden toegevoegd zonder de cache-entry te invalideren. [1] (`verified`)

Tool namespacing (groepeer tools per business domain) reduceert cognitieve belasting op het model, maakt governance eenvoudiger (permissions per namespace), en verbetert observability (track tool usage per domein). [6] (`verified` — brightlume.ai)

### 8. Model Context Protocol (MCP)

MCP is een open standaard (Anthropic, november 2024) voor het koppelen van AI-assistenten aan externe systemen. Geadopteerd door OpenAI, Google, Microsoft en tientallen toolvendors. [8] (`verified` — anthropic.com/news + agentic-academy.ai)

Architectuur: JSON-RPC 2.0 protocol tussen drie rollen:
- **Host**: LLM-applicatie die verbindingen initieert
- **Client**: connector binnen de host
- **Server**: service die capabilities aanbiedt

Transport: stdio (development), Streamable HTTP (productie). De Streamable HTTP transport (geïntroduceerd in de 2025-11-25 spec) verving het eerdere HTTP+SSE dual-endpoint design — een significante vereenvoudiging. [9] (`verified` — agentic-academy.ai MCP deep dive)

MCP-tools worden gediscovered via `tools/list`, aangeroepen via `tools/call`. Servers kunnen `notifications/tools/list_changed` sturen bij runtime-wijzigingen.

**Productie-status MCP:** De march 2025 release voegde OAuth 2.1 toe (voor identity flows op remote servers) en maakte remote, production-grade MCP deployments haalbaar. Door mei 2025 waren er meer dan 5.000 community-contributed MCP servers. Cloudflare's Workers-integratie maakt MCP-servers cloud-native en globally accessible. [9, 10] (`verified`)

**Migratievoordeel:** Teams die hun tool-library migreerden naar MCP zagen 70% reductie in onderhoudslast — één MCP-conforme tool werkt overal. [11] (`verified` — iterathon.tech case studie)

## Evidence Table

| # | Bron | URL | Type | Key claim | Confidence |
|---|------|-----|------|-----------|------------|
| 1 | Anthropic Tool Use Docs | https://docs.anthropic.com/en/docs/tool-use | primary | client vs. server tools, strict mode, pricing | high |
| 2 | EngineersOfAI — Tool Use Guide | https://engineersofai.com/docs/llms/llm-agents/Tool-Use-and-Function-Calling | secondary | request-response cycle, parallel tool execution | high |
| 3 | Webcoderspeed — Tool Design | https://webcoderspeed.com/blog/scaling/ai-agent-tool-design | secondary | JSON schema best practices, error messages | medium |
| 4 | Anthropic How Tool Use Works | https://platform.claude.com/docs/en/agents-and-tools/tool-use/how-tool-use-works | primary | Anthropic-schema trained-in tools | high |
| 5 | AI Workflow Lab — Function Calling Guide | https://aiworkflowlab.dev/article/llm-tool-use-function-calling-production-basic-integration-advanced-orchestration | secondary | PTC, tool search, parallel execution | high |
| 6 | Brightlume AI — Enterprise Tool Use | https://brightlume.ai/blog/tool-use-patterns-enterprise-ai-agents | secondary | ReAct, namespacing, RBAC, orchestration patronen | high |
| 7 | Scalifiai — Function Calling Best Practices | https://www.scalifiai.com/blog/function-calling-tool-call-best-practices | secondary | schema design, naming conventions | medium |
| 8 | Anthropic MCP Announcement | https://www.anthropic.com/news/model-context-protocol | primary | MCP introductie, open standaard | high |
| 9 | Agentic Academy — MCP Deep Dive | https://agentic-academy.ai/posts/mcp-deep-dive/ | secondary | transport, OAuth 2.1, spec evolutie | high |
| 10 | MCP Official Site | https://modelcontextprotocol.info/ | primary | MCP specs, tools concept | high |
| 11 | Iterathon — Advanced Function Calling | https://iterathon.tech/blog/advanced-function-calling-tool-composition-production-agents-2026 | secondary | MCP migration 70% maintenance reduction | medium |

## Coverage Status

- **Gecheckt direct:** Bronnen 1, 4, 5, 8, 9, 10 — volledig gelezen
- **Blijft onzeker:** Exacte benchmarkdata voor PTC (gelezen via highlights, niet volledig rapport)
- **Niet afgerond:** Vergelijking OpenAI Responses API vs. Anthropic MCP connector (buiten scope van deze researcher)

## Sources

1. Anthropic — Tool use with Claude — https://docs.anthropic.com/en/docs/tool-use
2. EngineersOfAI — Tool Use and Function Calling — https://engineersofai.com/docs/llms/llm-agents/Tool-Use-and-Function-Calling
3. Webcoderspeed — Designing AI Agent Tools — https://webcoderspeed.com/blog/scaling/ai-agent-tool-design
4. Anthropic — How tool use works — https://platform.claude.com/docs/en/agents-and-tools/tool-use/how-tool-use-works
5. AI Workflow Lab — LLM Function Calling: Complete Guide — https://aiworkflowlab.dev/article/llm-tool-use-function-calling-production-basic-integration-advanced-orchestration
6. Brightlume AI — Tool Use Patterns for Enterprise AI Agents — https://brightlume.ai/blog/tool-use-patterns-enterprise-ai-agents
7. Scalifiai — Design Best Practices of AI Function Calling — https://www.scalifiai.com/blog/function-calling-tool-call-best-practices
8. Anthropic — Introducing the Model Context Protocol — https://www.anthropic.com/news/model-context-protocol
9. Agentic Academy — What Is MCP? A Practitioner's Guide — https://agentic-academy.ai/posts/mcp-deep-dive/
10. Model Context Protocol Official — Tools Concept — https://modelcontextprotocol.info/docs/concepts/tools/
11. Iterathon — Advanced Function Calling Tool Composition Production Agents 2026 — https://iterathon.tech/blog/advanced-function-calling-tool-composition-production-agents-2026
