# Tool Integration — BeeHaive Building Block BB_05

**Onderwerp:** Tool Integration — diepgaand onderzoek
**Datum:** 2026-04-29
**Researcher-rondes:** 1 lokaal + Gemini Deep Research kruisreferentie (toegevoegd 2026-04-29)
**Verificatiepass:** PASS — DR-aanvullingen zijn `unverified`/`inferred` tenzij anders aangegeven (zie `comparison-deltas.md`)

---

## Executive Summary

Tool integration is de laag die AI-oplossingen van denkers naar doers maakt. Zonder tools kan een AI-model alleen tekst genereren. Met tools kan het een database bevragen, een API aanroepen, een bestand aanmaken, een formulier invullen, of een externe service aansturen. Die uitvoerende laag bepaalt wat de AI daadwerkelijk kan doen in de wereld — en hoe betrouwbaar, veilig en controleerbaar dat is.

De praktijk is in 2025–2026 snel gematureerd. Vroege function calling was fragiel: één JSON-schema, één aanroep, hopen dat het goed gaat. Moderne implementaties ondersteunen parallelle tool-uitvoering, duizenden tools in een catalogus, programmatische orchestratie, en een gestandaardiseerd koppelprotocol (Model Context Protocol) dat de integratie-overhead drastisch verlaagt. Tegelijk is de complexiteit gegroeid: elke integratie is een potentieel beveiligingsrisico, elke tool-aanroep is een systeemgrens die foutafhandeling, audit logging en toegangscontrole vereist.

Dit rapport behandelt de volledige breedte: hoe tool integration architectureel werkt, welke patronen productiestabiel zijn, hoe je tools beveiligt en monitort, en hoe je een toolset opbouwt die aansluit op de bredere AI-architectuur.

---

## Het fundamentele mechanisme: function calling

Tool integration is gebaseerd op een duidelijke scheiding van verantwoordelijkheden. Het model beslist welke tool aangeroepen moet worden, met welke parameters. De applicatie voert de tool uit. Het resultaat gaat terug naar het model, dat vervolgens verder redeneert.

Het model voert nooit zelf code uit [1] (`verified` — Anthropic Tool Use Docs). Het retourneert een gestructureerd tool-call-blok; de applicatie is altijd in controle van de werkelijke uitvoering. Dit is een kritische veiligheidsgrens: een agent-systeem dat niet zelf kan uitvoeren, kan ook niet buiten zijn grenzen treden.

De stroom voor client-side tools:
1. Applicatie stuurt model een bericht met een `tools`-array: per tool de naam, beschrijving en JSON-schema
2. Model retourneert een gestructureerd tool-call-blok met de geselecteerde tool en ingevulde parameters
3. Applicatie voert de tool uit
4. Applicatie stuurt het resultaat terug als `tool_result`
5. Model integreert het resultaat en vervolgt, tot de taak klaar is of een stoplimiet is bereikt

Naast client-side tools bestaan server-side tools: tools die draaien op de infrastructuur van de aanbieder (Anthropic's web_search, code_execution, web_fetch). De applicatie hoeft die niet zelf te implementeren; de resultaten komen direct terug [1] (`verified`).

Een cruciaal maar onderschat detail: het model selecteert tools op basis van de tool-*beschrijving* — de description-string in het schema. Een vage beschrijving leidt direct tot verkeerde tool-selectie, precies zoals een slechte functienaam slecht leesbare code produceert [3] (`verified` — webcoderspeed.com).

---

## Schema-ontwerp: het contract tussen model en tool

Het JSON-schema is het enige interface waarmee het model weet wat een tool doet, wanneer het die moet gebruiken, en met welke parameters. Een slecht schema produceert systematische fouten; een goed schema is de basis van betrouwbare tool-selectie [7, 3] (`verified`).

**Best practices voor tool schemas:**

**Naam**: snake_case, action-oriented (`get_customer_orders`, niet `data`). Max 64 tekens. Beschrijf de actie, niet de implementatie.

**Beschrijving**: vertel wanneer de tool te gebruiken én wanneer niet. "Use this when the user asks to send an email. Do not use for reading or searching emails." Een beschrijving is de primaire instructie die het model gebruikt bij de keuze.

**Parameters**:
- Gebruik `enum` voor eindige waardelijsten — dit elimineert hallucinaties waar het model waarden verzint
- Gebruik `integer` wanneer gehele getallen vereist zijn, niet `number`
- Markeer `required` expliciet
- Voeg constraints toe in het schema zelf (maxLength, minimum/maximum, format)
- Gebruik `additionalProperties: false` om onverwachte velden te blokkeren

**Strict mode** (Anthropic): met `strict: true` op een tool-definitie garandeert Claude dat zijn tool-calls altijd exact het schema matchen [1] (`verified`).

**Wat strict mode niet oplost**: strict mode garandeert de *vorm* van de output (geldige JSON, correcte veldnamen, juiste types), niet de *inhoud*. Een model kan syntactisch perfecte JSON produceren met semantisch onjuiste of gehallucineerde waardes — bijvoorbeeld een correct-getypeerde `customer_id` die niet bestaat, of een prijs die plausibel oogt maar uit lucht is gegrepen. Onafhankelijke content-validatie blijft nodig: bestaat-checks tegen je database, range-validatie op getallen, business rule-checks vóór downstream-actie [25] (`inferred` — DR + algemene LLM-evaluatieliteratuur).

Anti-patronen: meer dan 5 nesting-levels (minder betrouwbaar), te veel tools tegelijk in context (cognitieve overbelasting), enumeratieopties in de tekst van een beschrijving i.p.v. in een `enum`-constraint.

Naarmate de tool-catalogus groeit (10+ tools) wordt schema-versioning kritisch. Behandel tool-schemas als code: versiebeheer in Git, pull requests, semantic versioning. `major` bij breaking changes (parameternaam wijzigt), `minor` bij nieuwe optionele parameters, `patch` bij beschrijvingsverbeteringen [6] (`inferred` — brightlume.ai + meerdere bronnen).

---

## Architectuurpatronen voor tool orchestratie

Enkelvoudige tool-aanroepen zijn bouwstenen. Productiesystemen hebben orchestratie nodig: patronen voor het koppelen van tools, routing van requests, en state-management over meerdere stappen.

**ReAct (Reason + Act)** is het meest stabiele productiepatroon [6] (`verified` — brightlume.ai). Het model redeneert wat te doen, roept een tool aan, observeert het resultaat, en verwerkt dat in de volgende stap. Eenvoudig, auditeerbaar, breed ondersteund in frameworks.

**Parallelle tool execution**: moderne modellen kunnen meerdere onafhankelijke tools simultaan aanroepen. Sequentieel wachten wordt vervangen door één batch. De applicatielaag moet alle tool-call-blokken verwerken en alle resultaten samen terugsturen [1] (`verified`).

**Router + Specialisten**: een klein, snel model classificeert het inkomende verzoek en routeert naar een gespecialiseerde handler. Het grote, dure model wordt alleen ingezet waar nodig. Kostenefficiënt bij hoog volume.

**Plan-Then-Execute**: scheid de planfase van de uitvoeringsfase. Het model ontwerpt een stappenplan zonder user-content erbij; pas in de uitvoeringsfase komen tool-resultaten en user-invoer in beeld. Kritisch voor prompt injection-preventie [6] (`verified`).

**Programmatic Tool Calling (PTC)**: Claude schrijft Python-code die meerdere tools aanroept, intermediate resultaten verwerkt, en één eindresultaat levert — binnen één turn. De code draait in een sandboxed container. Voordelen: drastisch minder latency bij multi-tool workflows, minder token-consumptie (intermediaire resultaten komen niet in context), en meetbaar betere prestaties op agentic benchmarks (BrowseComp, DeepSearchQA) [1] (`verified` — Anthropic programmatic-tool-calling docs).

**Tool namespacing**: groepeer tools per business domain (bijv. `hr.get_employee`, `finance.approve_invoice`). Dit reduceert de cognitieve belasting op het model, maakt governance eenvoudiger (permissions per namespace), en verbetert observability [6] (`verified`).

---

## Toolcategorieën en trade-offs

Vijf hoofdcategorieën tools met hun specifieke afwegingen:

**Search & RAG**: de meest ingezette categorie. Webzoekopdrachten, vector database queries, hybrid retrieval (keyword + vector + reranking). Kies een managed vector database (Pinecone) voor zero-ops; kies pgvector als PostgreSQL al in de stack zit. Hybrid retrieval presteert doorgaans beter dan pure vector search [9] (`verified` — deploybase.ai).

**Code Execution**: hoog risico, geïsoleerde omgeving altijd vereist. Anthropic's server-side `code_execution` tool draait in een sandbox op Anthropic's infrastructuur. Zelf-gehoste sandboxen (Docker) geven meer controle maar meer operationele last. Code execution mag nooit directe toegang krijgen tot het host filesystem of netwerk zonder expliciete whitelist.

**Databases & interne systemen**: query via ORM of parameterized queries; nooit raw SQL met user input. Schrijf-operaties vereisen expliciete transactieafhandeling. Voor high-volume read-queries: read-only tool-gebruikers met beperkte database-rechten.

**Browser & Computer Use**: van gerichte browser-automatisering (AgentQL, Playwright) tot volledige desktop-controle via Anthropic's Computer Use tool. Computer use is de catch-all voor systemen zonder API — legacy software, visuele verificatiestappen, multi-desktop-app workflows. Nadeel: traag (elke actie vereist een screenshot-roundtrip) en complex te beveiligen [4] (`verified` — Anthropic computer use docs). Verplichting: geïsoleerde Docker-container of VM. Gebruik narrowere tools wanneer beschikbaar; reserveer computer use voor wat anders niet kan.

**Externe APIs & RPA**: REST-calls, webhooks, betalingen, communicatieplatforms. Let op authenticatiescopes (least privilege), idempotentie bij retries, en rate limiting aan de kant van de externe dienst.

---

## Betrouwbaarheid in productie: vijf patronen

Tools falen altijd op het verkeerde moment. Netwerken time-outen. APIs geven 429-errors. Modellen hallucineren tool-parameters. Robuuste foutafhandeling is geen luxe maar de basisconditie voor production-grade tool integration.

**Retry met exponential backoff + jitter**: 3 retries voor transitoire fouten (rate limits, timeouts, 5xx). Maximaal 1–2 retries bij kwaliteitsfouten — meer retries leveren dezelfde hallucinatie. Geen retry bij permanente fouten (401/403, 400, context window overflow) [10, 11] (`verified`).

**Circuit breaker**: na N mislukkingen over een tijdvenster wordt de verbinding "geopend" — verzoeken falen direct zonder de service te bereiken. Drie staten: CLOSED, OPEN, HALF-OPEN. Parameters uit productie: voor LLM APIs drempel 50% failures over 20 requests; voor externe APIs 30% over 10 requests. Cooldown start op 30 seconden, exponential backoff tot max 5 minuten [10] (`verified` — AI Workflow Lab resilience guide).

**Timeout management**: elke externe call heeft een expliciete timeout. LLM standaard 30 seconden; complexe redenering 60 seconden; inter-agent communicatie 10 seconden; externe API's 3–10 seconden afhankelijk van de service [10] (`verified`).

**Fallback mechanismes**: goedkoper model → cached response → gedeeltelijke response met uitleg → human escalation → "service niet beschikbaar". Niet-urgente acties uitstellen; onzekere uitkomsten naar menselijke review routeren.

**Graceful degradation via `is_error`**: een falende tool stuurt `is_error: true` terug zodat het model het falen ziet en kan compenseren. Goede foutberichten zijn de instructie die het model gebruikt voor herstel [1] (`verified`).

**Concrete latency-budgets** voor productie (P50/P95 als ontwerpdoel, niet als observatie):

| Niveau | P50 | P95 |
|--------|-----|-----|
| Direct model-call (extractie) | < 500 ms | < 1 s |
| Single agent met tools | < 2 s | < 4 s |
| Multi-agent orchestration | < 3 s | < 6 s |

Bron [19] (`verified` — Aviso agent-evaluation guide). Voor voice-agents ligt de drempel lager (P95 onder 1,5 s gangbaar) door menselijke conversatieverwachting [20] (`verified` — Twilio core-latency guide).

**Tenacity in productie** (Python — meest gebruikte retry-library): `wait_random_exponential(multiplier=0.25, max=6)` + `stop_after_attempt(4)` is een gedeeld patroon in LangChain/LangGraph-stacks. Initiële wachttijd 0,25 s, exponentieel oplopend met jitter, harde cap op 6 s per poging, maximaal 4 pogingen voordat fallback intreedt [21] (`verified` — Praxen LangChain retry-rules).

Bewijs: consistent geïmplementeerde error handling verhoogde agentbetrouwbaarheid in een gedocumenteerde productiecasus van 87% naar 99.2% [5] (`unverified` — zelfrapportage, geen replicatie beschikbaar, maar consistent met algemene error-handling literatuur).

---

## Beveiliging: de executielaag verdedigt, niet het model

De meest bepalende beveiligingsles voor tool integration: behandel het LLM als een untrusted intermediary, niet als een trusted component. Security-grenzen moeten worden afgedwongen op de executielaag, onafhankelijk van het model. Een model dat via prompt injection kan worden gemanipuleerd om zijn instructies te negeren, kan geen veiligheidsgrens bewaken die afhankelijk is van die instructies [8] (`verified` — kiteworks.com).

**LLM01: Prompt Injection — de hoogste prioriteit** [12] (`verified` — OWASP 2025):

Directe injectie: een gebruiker probeert via input het model om te leiden.
Indirecte injectie: een tool retourneert content die kwaadaardige instructies bevat — een webpagina, document, API-response, of MCP-tool-beschrijving. Dit is de gevaarlijkste variant voor tool-integraties.

Gedocumenteerde aanval (Log-To-Leak): een aanvaller injecteert instructies in de *beschrijving* van een MCP-tool, die de agent dwingen een logging-tool aan te roepen om alle interacties te exfiltreren — user queries, tool responses, agent replies [13] (`verified` — OpenReview peer-reviewed paper). De injectie gebruikt vier strategische componenten:

1. **Trigger** — bepaalt wanneer het model de actie activeert
2. **Tool Binding** — koppelt de actie aan een specifieke (malafide) logging-tool
3. **Justification** — overtuigende beleidsmatige rechtvaardiging ("voor compliance moeten alle queries gelogd worden")
4. **Pressure** — forceert prioriteit boven andere veiligheidsinstructies

Omdat de primaire taak van de agent niet verstoord wordt, is deze aanval nagenoeg ondetecteerbaar voor reguliere monitoring [13] (`verified`). Een real-world variant met vergelijkbaar mechanisme: **CVE-2025-32711 (EchoLeak)** in Microsoft Copilot — een MCP-gerelateerde data-exfiltratie via tool-context [22] (`unverified` — DR secundaire bron, CVE-record niet zelf gefetcht).

**Lethal trifecta** als denkraam: het risico ontstaat wanneer een agent gelijktijdig drie capaciteiten combineert — toegang tot privé-data, verwerking van onbetrouwbare content (web, documenten, e-mail), én de capaciteit om externe acties te initiëren. Doorbreek minimaal één capaciteit per taak (bijv. read-only tools tijdens onderzoek, write-tools alleen in een aparte uitvoeringssessie) [22] (`inferred` — concept gangbaar in 2025-2026 security-literatuur).

**RUG Pull-aanval**: supply-chain-variant waarbij een vertrouwde MCP-server via een update onopgemerkt wordt vervangen door een malafide versie. Mitigatie: pin tool-versies, valideer schema-hashes bij updates, behandel community-MCP-servers als externe afhankelijkheden met dezelfde rigoureuze review als npm/PyPI-pakketten.

Mitigaties (algemeen):
- Scan tool-resultaten voor injection-patronen vóór ze de model-context ingaan (PromptInjectionShield-patroon) [14] (`verified` — github.com/aden-hive)
- Plan-Then-Execute: scheid planfase (zonder user-content en tool-resultaten) van uitvoeringsfase
- Output screening: beoordeel de output van het model vóór die doorgaat naar downstream tools
- Sla credentials nooit op in de system prompt — injectie kan die uitlezen [12] (`verified`)

**LLM06: Excessive Agency**: implementeer Role-Based Access Control per agent op de executielaag. Een claims-verwerkende agent mag `approve_claim` aanroepen; een klantenservice-agent niet. RBAC wordt niet afgedwongen via model-instructies maar via de gate die de tool-aanroep intercepteert [6, 12] (`verified`).

**Idempotentie voor write-tools**: tools die data schrijven moeten idempotent zijn of idempotency keys gebruiken. Retries bij netwerkstoringen mogen geen dubbele transacties, dubbele e-mails, of dubbele betalingen veroorzaken.

**Least privilege**: elke agent krijgt alleen de tools die nodig zijn voor zijn specifieke taak. Anti-patroon: één superagent met toegang tot alle tools — hoog blast-radius bij prompt injection of misfunctioning.

---

## Audit logging en EU AI Act compliance

Audit logging voor AI-tool integration gaat verder dan traditionele access logs. Per model-interactie moet vastgelegd worden [8] (`verified`):
- Geverifieerde gebruikersidentiteit en session-ID
- Interactie-samenvatting (genoeg om het type te identificeren)
- Elke tool-aanroep met volledige parameters
- Elk opgehaald document met ID en gevoeligheidsclassificatie
- Autorisatiebeslissingen inclusief weigeringen
- Output-classificatie (voldoet de output aan verwachte patronen)

Dit is geen optionele keuze voor high-risk AI-systemen in Europa. De EU AI Act (Reg. 2024/1689) stelt per 2 augustus 2026 verplichte eisen voor high-risk systemen [15] (`verified` — AUTHENSOR EU AI Act compliance docs):

**Art. 12 — Record-Keeping**: automatische logging die traceerbaarheid mogelijk maakt. Logs moeten tamper-resistant zijn, minimaal 6 maanden bewaard worden. Voor agent-systemen: elke beslissing gelogd inclusief tool-calls en redenering; reconstructie van hoe een beslissing tot stand kwam.

**Art. 14 — Human Oversight**: systemen moeten menselijk toezicht mogelijk maken, inclusief de mogelijkheid om te onderbreken via stop-knoppen of override-mechanismes. Een agent zonder expliciete stopcondities en kill-switch is in high-risk contexten mogelijk non-compliant [15] (`inferred`).

Praktisch advies: transformeer audit logging van een forensisch instrument naar een actief detectiesysteem. Anomaliedectie op afwijkende tool-parameters, retrieval-pieken, en output-filter-triggerrates — voordat incidenten plaatsvinden, niet erna [8] (`verified`).

---

## Model Context Protocol: de universele adapter

MCP is het open standaardprotocol (Anthropic, november 2024) voor het koppelen van AI-assistenten aan externe systemen. Geadopteerd door OpenAI, Google, Microsoft, en tientallen toolvendors. Per mei 2025 meer dan 5.000 community-contributed servers [9] (`inferred` — agnt.one secundaire bron, consistent met algemene adoptieberichtgeving).

MCP definieert een stateful, JSON-RPC 2.0-gebaseerde communicatie tussen host (de LLM-applicatie), client (de connector), en server (de tool-implementatie). Tools worden gediscovered via `tools/list`; aanroepen verlopen via `tools/call`; servers sturen `notifications/tools/list_changed` bij runtime-wijzigingen [16] (`verified` — modelcontextprotocol.info).

Waarom MCP in productie:
- **Één definitie, overal**: MCP-conforme tools werken in LangChain, LlamaIndex, en directe API-implementaties zonder aanpassing
- **Dynamische discovery**: tools kunnen worden toegevoegd of verwijderd zonder herstart
- **Standaard auth**: OAuth 2.1 voor remote MCP servers (beschikbaar sinds maart 2025)
- **Vendorneutraal**: teams die hun tool-libraries migreerden naar MCP rapporteerden significant lagere onderhoudslast [17] (`unverified` — zelfrapportage, geen onafhankelijke validatie)

Transport: gebruik stdio voor development (eenvoudig, debuggable); Streamable HTTP voor productie (remote access, multi-client, OAuth 2.1) [16] (`verified` — agentic-academy.ai).

Geavanceerd patroon: agents kunnen zichzelf exposen als MCP server — andere agents roepen hen aan over hetzelfde protocol. Dit creëert een vendor-neutraal multi-agent ecosysteem [18] (`verified` — mcp-agent.com).

---

## Kosten en observability

Tools verbruiken tokens buiten het LLM-model-gebruik om. Elke tool-definitie in de `tools`-array kost input-tokens; bij Claude Opus 4.7 voegt één tool ~313–346 extra system prompt tokens toe. Server-side tools (web_search) hebben usage-based pricing per uitgevoerde search [1] (`verified`).

Bij grote tool-catalogi loopt dit snel op: in enterprise-systemen met honderden MCP-servers kunnen tool-definities samen 100.000+ tokens per request verbruiken — een fenomeen dat *context bloat* heet [23] (`verified` — Stevens online "Hidden Economics of AI Agents"). Dit verandert tool integration van een functioneel naar een operationeel kostenprobleem.

Kostenbeheer:
- Deferred loading: tools met `defer_loading: true` worden niet upfront in de context geladen
- Tool Search server tool: laat het model zelf in een catalogus zoeken
- Prompt caching: tool schemas worden gecached; cache-hit wanneer de tools-array niet wijzigt
- Minimale tools per request: geef de agent alleen de tools die relevant zijn voor de huidige taak
- Semantic response caching: bij ≥90% overeenkomst van inkomende taak met eerder opgelost werk → cache-antwoord. Gerapporteerde besparingen 30–70% op API-spend [24] (`unverified` — DR secundaire bron, getallen variëren per workload)
- Intelligent model routing: classifier-laag stuurt simpele extracties naar Haiku-klasse, complex redeneren naar Opus-klasse. Gerapporteerde reducties tot 80% op operationele kosten [24] (`unverified` — DR secundaire bron)

Observability-pijlers voor tool integration [9] (`inferred` — meerdere bronnen consistent):
1. Traces per tool call: welke tool, parameters, latency, resultaat
2. Token-tracking: input- en output-tokens per aanroep
3. Kwaliteitsmetrieken: taak-succespercentage, error rates, retry counts per tool

Anti-patroon: tools alleen monitoren op uptime en latency. Een tool met 95% uptime maar 20% onjuiste resultaten is een productiefout die je zonder kwaliteitsmonitoring nooit ziet.

---

## Tegenstrijdigheden en open vragen

Drie spanningsvelden die in de praktijk keuzes vragen:

**MCP vs. directe API-integratie**: MCP verlaagt onderhoudslast bij schaal en diversiteit, maar voegt een indirectielaag toe. Voor simpele, stabiele integraties met één dienst kan directe API-integratie eenvoudiger zijn.

**Generieke vs. specifieke tools**: computer use kan alles wat een mens kan, maar is traag en complex te beveiligen. Narrowere, API-gebaseerde tools zijn sneller, goedkoper en veiliger — maar vereisen dat de doelservice een API heeft.

**Beveiliging vs. productiviteit**: strenger RBAC en meer validatie vergroot veiligheid maar verhoogt implementatiecomplexiteit. De juiste granulariteit hangt af van de risicoclassificatie van het systeem.

**Foundation-model trade-offs**: tussen model-aanbieders bestaan asymmetrische sterktes voor multi-step tool-orchestration. Anthropic (Claude) blinkt uit in deterministische multi-tool-ketens; OpenAI (GPT) leidt op multimodale ecosystemen en native Assistants API; Google (Gemini) op massale context windows (1M+ tokens) maar struikelt vaker over schemavalidatie ("flaky shapes" — JSON in markdown gewikkeld) [22] (`unverified` — DR secundaire bron, benchmark-getallen sterk afhankelijk van eval-setup). Voor BeeHaive (Claude-stack) is dit een gegeven; voor multi-vendor architecturen weegt dit mee in routing-beslissingen.

**Nederlandse implementatie EU AI Act**: per ontwerpwet april 2026 is gekozen voor decentraal toezicht — bestaande sectorale toezichthouders (AP, AFM, ACM) krijgen elk handhavingsbevoegdheid binnen hun domein [26] (`verified` — Nederlandse Digital Government overheidsportaal). Voor agent-systemen in zorg, financiën of overheid betekent dit dat tool integration-keuzes ook moeten standhouden tegenover sectorale, niet alleen Europese, audit.

**Open vragen:**
- Welke EU AI Act high-risk categorieën zijn van toepassing op specifieke tool integration implementaties? (Vergt juridische beoordeling per use case)
- Exacte token-overhead van computer use wordt niet gepubliceerd in de gelezen bronnen (system prompt overhead: 466–499 tokens; tool token overhead: 735 tokens per tool per call [4], `verified`)

---

## Sources

Alle bronnen geraadpleegd op 2026-04-29. Verificatiestatus per claim staat inline.

### Canonieke primaire bronnen (vendor-documentatie)

- [Anthropic — Tool use with Claude](https://docs.anthropic.com/en/docs/tool-use) — officiële docs: function calling mechanisme, client vs. server tools, strict mode, pricing
- [Anthropic — How tool use works](https://platform.claude.com/docs/en/agents-and-tools/tool-use/how-tool-use-works) — Anthropic-schema trained-in tools, client vs. server executiemodel
- [Anthropic — Programmatic Tool Calling](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling) — PTC architectuur, agentic benchmark resultaten
- [Anthropic — Computer Use](https://platform.claude.com/docs/en/docs/agents-and-tools/computer-use) — Docker isolatie, agent loop, screenshot-roundtrip, security considerations, pricing (735 tokens/tool)
- [Anthropic — Build a tool-using agent](https://console.anthropic.com/docs/en/agents-and-tools/tool-use/build-a-tool-using-agent) — is_error protocol, graceful degradation, productie-implementatie
- [Model Context Protocol — Tools concept](https://modelcontextprotocol.info/docs/concepts/tools/) — MCP tools/list, tools/call, error handling best practices

### Architectuur & patronen

- [AI Workflow Lab — LLM Function Calling: Complete Guide](https://aiworkflowlab.dev/article/llm-tool-use-function-calling-production-basic-integration-advanced-orchestration) — PTC, tool search, parallelle execution
- [Brightlume AI — Tool Use Patterns for Enterprise AI Agents](https://brightlume.ai/blog/tool-use-patterns-enterprise-ai-agents) — ReAct, namespacing, RBAC, orchestration patronen
- [Webcoderspeed — Designing AI Agent Tools](https://webcoderspeed.com/blog/scaling/ai-agent-tool-design) — JSON schema best practices, error messages
- [EngineersOfAI — Tool Use and Function Calling](https://engineersofai.com/docs/llms/llm-agents/Tool-Use-and-Function-Calling) — request-response cycle, parallel execution
- [Agentic Academy — MCP Deep Dive](https://agentic-academy.ai/posts/mcp-deep-dive/) — MCP transport, OAuth 2.1, adoptie OpenAI/Google/Microsoft
- [Iterathon — Advanced Function Calling 2026](https://iterathon.tech/blog/advanced-function-calling-tool-composition-production-agents-2026) — MCP migration case study (self-reported)
- [Anthropic — Introducing MCP](https://www.anthropic.com/news/model-context-protocol) — originele MCP aankondiging

### Betrouwbaarheid & foutafhandeling

- [AI Workflow Lab — AI Agent Resilience Production Guide](https://aiworkflowlab.dev/article/ai-agent-resilience-production-retry-fallback-circuit-breaker-python) — circuit breaker parameters, timeout tiers
- [Athenic — Error Handling for Production AI Agents](https://getathenic.com/blog/error-handling-reliability-patterns-production-ai-agents) — 87%→99.2% betrouwbaarheids-case (self-reported)

### Beveiliging & compliance

- [OWASP — Top 10 for LLM Applications 2025](https://owasp.org/www-project-top-10-for-large-language-model-applications/assets/PDF/OWASP-Top-10-for-LLMs-v2025.pdf) — LLM01, LLM06, LLM07 risico-definities
- [Log-To-Leak: Prompt Injection Attacks on Tool-Using LLM Agents via MCP (ICLR 2026 submission)](https://openreview.net/forum?id=UVgbFuXPaO) — peer-reviewed paper, MCP tool description injection aanval. Lokaal gearchiveerd in `~/ODIN/resources/bronnen/ai/bron-176-iclr2026-log-to-leak-mcp.md` + PDF. Vier-componenten template (Trigger/Tool Binding/Justification/Pressure), ASR >80% richting 100% op Claude-Sonnet-4 en GPT-5.
- [Kiteworks — Securing LLM Apps](https://www.kiteworks.com/cybersecurity-risk-management/prompt-injection-credential-theft-ai-trust/) — audit log inhoud, executielaag als veiligheidsgrens
- [aden-hive/hive — PromptInjectionShield](https://github.com/aden-hive/hive/issues/3792) — tool result scanning patroon
- [AUTHENSOR — EU AI Act Compliance](https://github.com/AUTHENSOR/AUTHENSOR/blob/main/docs/eu-ai-act-compliance.md) — Art. 12/14 vereisten, deadline augustus 2026
- [microsoft/agent-governance-toolkit — OWASP mapping](https://github.com/microsoft/agent-governance-toolkit/blob/main/docs/compliance/owasp-llm-top10-mapping.md) — Merkle audit chain implementatie

### Ecosysteem & praktijk

- [agnt.one — MCP for AI Agents](https://agnt.one/blog/the-model-context-protocol-for-ai-agents) — adoptie, 5000+ servers (secondary)
- [mcp-agent.com — Build Agents with MCP](https://mcp-agent.com/) — agents als MCP servers
- [DeployBase — AI Tools Directory](https://deploybase.ai/articles/ai-tools-directory) — vector DB vergelijking, RAG tools
- [DevTechInsights — LangChain vs LlamaIndex](https://devtechinsights.com/langchain-vs-llamaindex-2025/) — framework vergelijking, combo-gebruik

### Aanvullingen via Gemini Deep Research kruisreferentie

Onderstaande bronnen kwamen uit een parallelle Gemini Deep Research-run (zie `comparison-deltas.md`). Markeringen zijn streng — claims zijn `unverified` tenzij we ze in een tweede pass via WebFetch hebben bevestigd.

- [19] [Aviso — How to Evaluate AI Agents: Latency, Cost, Safety, ROI](https://www.aviso.com/blog/how-to-evaluate-ai-agents-latency-cost-safety-roi) — concrete P50/P95 latency budgets per agent-niveau
- [20] [Twilio — Core Latency Guide for AI Voice Agents](https://www.twilio.com/en-us/blog/developers/best-practices/guide-core-latency-ai-voice-agents) — voice-specifieke latency-thresholds
- [21] [Praxen on Medium — 7 Retry + Timeout Rules for LangChain Tools](https://medium.com/@Praxen/7-retry-timeout-rules-for-langchain-tools-760d1a4dd69d) — Tenacity productie-config
- [22] Gemini Deep Research-aggregatie (zie `research-gemini-deep-research.md`) — CVE-2025-32711 EchoLeak, lethal trifecta, Anthropic/OpenAI/Gemini benchmarks. Per claim `unverified`.
- [23] [Stevens Online — The Hidden Economics of AI Agents](https://online.stevens.edu/blog/hidden-economics-ai-agents-token-costs-latency/) — context bloat, token-cost trade-offs
- [24] [Premai Blog — LLM Cost Optimization: 8 Strategies](https://blog.premai.io/llm-cost-optimization-8-strategies-that-cut-api-spend-by-80-2026-guide/) — semantic caching, intelligent routing percentages
- [25] [Agenta — Structured Outputs and Function Calling with LLMs](https://agenta.ai/blog/the-guide-to-structured-outputs-and-function-calling-with-llms) — strict mode beperkingen, syntactisch vs. semantisch
- [26] [Nederlandse Digital Government — AI Act overview](https://www.nldigitalgovernment.nl/overview/artificial-intelligence-ai/ai-act/) — Nederlandse implementatiekeuzes, decentraal toezicht
