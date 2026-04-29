# Tool Integration — BeeHaive Building Block BB_05 (Draft)

**Onderwerp:** Tool Integration — diepgaand onderzoek
**Datum:** 2026-04-29
**Researcher-rondes:** 1

---

## Executive Summary

Tool integration is de laag die AI-oplossingen van denkers naar doers maakt. Zonder tools kan een AI-model alleen tekst genereren. Met tools kan het een database bevragen, een API aanroepen, een bestand aanmaken, een formulier invullen, of een externe service aansturen. Die uitvoerende laag bepaalt wat de AI daadwerkelijk kan doen in de wereld — en hoe betrouwbaar, veilig en controleerbaar dat is.

De praktijk is in 2025–2026 snel gematureerd. Vroege function calling was fragiel: één JSON-schema, één aanroep, hopen dat het goed gaat. Moderne implementaties ondersteunen parallelle tool-uitvoering, duizenden tools in een catalogus, programmatische orchestratie, en een gestandaardiseerd koppelprotocol (Model Context Protocol) dat de integratie-overhead van tientallen uur naar uren reduceert. Tegelijk is de complexiteit gegroeid: elke integratie is een potentieel beveiligingsrisico, elke tool-aanroep is een systeemgrens die foutafhandeling, audit logging en toegangscontrole vereist.

Dit document behandelt de volledige breedte: hoe tool integration werkt, welke architectuurpatronen productiestabiel zijn, hoe tools worden beveiligd en gemonitord, en hoe je een toolset opbouwt die aansluit op de bredere AI-architectuur.

---

## Hoe function calling werkt: het fundamentele mechanisme

Tool integration is gebaseerd op een duidelijke scheiding van verantwoordelijkheden. Het model beslist welke tool aangeroepen moet worden, met welke parameters. De applicatie voert de tool uit. Het resultaat gaat terug naar het model, dat vervolgens verder redeneert.

Het model voert nooit zelf code uit [1]. Het retourneert een gestructureerd tool-call-blok; de applicatie is altijd in controle van de werkelijke uitvoering. Dit is een kritische veiligheidsgrens.

De stroom voor client-side tools (tools die in je eigen applicatie draaien):
1. Applicatie stuurt model een bericht met een `tools`-array: per tool de naam, beschrijving en JSON-schema van de parameters
2. Model retourneert een gestructureerd tool-call-blok met de geselecteerde tool en de ingevulde parameters
3. Applicatie voert de tool uit
4. Applicatie stuurt het resultaat terug naar het model
5. Model integreert het resultaat en vervolgt, tot de taak klaar is of een stoplimiet is bereikt

Naast client-side tools bestaan server-side tools: tools die draaien op de infrastructuur van de aanbieder (zoals Anthropic's web_search, code_execution, web_fetch). De applicatie hoeft die niet zelf te implementeren; de resultaten komen direct terug [1].

Een cruciaal detail: het model selecteert tools op basis van de tool-*beschrijving* — de description-string in het schema. Een vage beschrijving leidt direct tot verkeerde tool-selectie. De kwaliteit van de beschrijving is even bepalend als de kwaliteit van de tool-implementatie zelf [3].

---

## Schema-ontwerp: het contract tussen model en tool

Het JSON-schema is de enige taal waarmee het model weet wat een tool doet, wanneer het die moet gebruiken, en met welke parameters. Een slecht schema produceert systematische en onvoorspelbare fouten; een goed schema is de basis van betrouwbare tool-selectie [7, 3].

Best practices voor tool schemas:

**Naam**: gebruik snake_case, action-oriented (`get_customer_orders`, niet `data`). Max 64 tekens. Beschrijf de actie, niet de implementatie.

**Beschrijving**: vertel wanneer de tool te gebruiken én wanneer niet. "Use this when the user asks to send an email. Do not use for reading or searching emails." Een beschrijving is de enige instructie die het model krijgt bij de keuze.

**Parameters**:
- Gebruik `enum` voor eindige waardelijsten — dit elimineert hallucinaties waar het model waarden verzint die niet bestaan
- Gebruik `integer` wanneer gehele getallen vereist zijn, niet `number`
- Markeer `required` expliciet
- Voeg constraints toe in het schema zelf (maxLength, minimum/maximum, format)
- Gebruik `additionalProperties: false` om onverwachte velden te blokkeren

**Strict mode** (Anthropic): met `strict: true` op een tool-definitie garandeert Claude dat zijn tool-calls altijd exact het schema matchen — geen best-effort, maar schema-conformantie [1].

Anti-patronen: meer dan 5 nesting-levels (minder betrouwbaar), te veel tools tegelijk in context (cognitieve overbelasting), enumeratieopties in de tekst van een beschrijving i.p.v. in een `enum`-constraint.

Naarmate de tool-catalogus groeit (10+ tools) wordt schema-versioning kritisch. Behandel tool-schemas als code: versiebeheer in Git, pull requests, semantic versioning. `major` bij breaking changes (parameternaam wijzigt), `minor` bij nieuwe optionele parameters, `patch` bij beschrijvingsverbeteringen [9].

---

## Architectuurpatronen voor tool orchestratie

Enkelvoudige tool-aanroepen zijn bouwstenen. Productiesystemen hebben orchestratie nodig: patronen voor het koppelen van tools, routing van requests, en state-management over meerdere stappen.

**ReAct (Reason + Act)** is het meest stabiele productiepatroon [6, 2]. Het model redeneert wat te doen, roept een tool aan, observeert het resultaat, en verwerkt dat in de volgende stap. Eenvoudig, auditeerbaar, breed ondersteund.

**Parallelle tool execution**: moderne modellen kunnen meerdere onafhankelijke tools simultaan aanroepen. Sequentieel wachten wordt vervangen door één batch. De applicatielaag moet alle tool-call-blokken verwerken en alle resultaten samen terugsturen [1].

**Router + Specialisten**: een klein, snel model classificeert het inkomende verzoek en routeert naar een gespecialiseerde handler. Het grote, dure model wordt alleen ingezet waar nodig. Kostenefficiënt bij hoog volume.

**Plan-Then-Execute**: scheid de planfase van de uitvoeringsfase. Het model ontwerpt een stappenplan zonder user-content erbij; pas in de uitvoeringsfase komen tool-resultaten en user-invoer in beeld. Kritisch voor prompt injection-preventie [2].

**Programmatic Tool Calling (PTC)**: Claude schrijft Python-code die meerdere tools aanroept, intermediate resultaten verwerkt, en één eindresultaat levert — binnen één turn. De code draait in een sandboxed container. Voordelen: drastisch minder latency bij multi-tool workflows, minder token-consumptie (intermediaire resultaten komen niet in context), en meetbaar betere prestaties op agentic benchmarks [1].

**Tool namespacing**: groepeer tools per business domain (bijv. `hr.get_employee`, `finance.approve_invoice`). Dit reduceert de cognitieve belasting op het model (minder tools om over te redeneren), maakt governance eenvoudiger (permissions per namespace), en verbetert observability (track usage per domein) [6].

---

## Toolcategorieën en trade-offs

Vijf hoofdcategorieën tools met hun specifieke afwegingen:

**Search & RAG**: de meest ingezette categorie. Webzoekopdrachten, vector database queries, hybrid retrieval (keyword + vector + reranking). Kies een managed vector database (Pinecone) voor zero-ops; kies pgvector als PostgreSQL al in de stack zit. Hybrid retrieval presteert doorgaans beter dan pure vector search: combineer altijd met keyword-filtering en reranking.

**Code Execution**: hoog risico, geïsoleerde omgeving altijd vereist. Anthropic's server-side `code_execution` tool draait in een sandbox op Anthropic's infrastructuur. Zelf-gehoste sandboxen (Docker) geven meer controle maar meer operationele last. Code execution nooit directe toegang geven tot host filesystem of netwerk zonder expliciete whitelist.

**Databases & interne systemen**: query via ORM of parameterized queries; nooit raw SQL met user input. Schrijf-operaties vereisen expliciete transactieafhandeling. Voor high-volume read-queries: overweeg read-only tool-gebruikers met beperkte database-rechten.

**Browser & Computer Use**: van gerichte browser-automatisering (AgentQL, Playwright) tot volledige desktop-controle via Anthropic's Computer Use tool. Computer use is de catch-all voor systemen zonder API — legacy software, visuele verificatiestappen, multi-desktop-app workflows. Nadeel: traag (elke actie vereist screenshot-roundtrip). Gebruik narrowere tools wanneer beschikbaar; reserveer computer use voor wat anders niet kan [4]. Verplicht: geïsoleerde container of VM.

**Externe APIs & RPA**: REST-calls, webhooks, betalingen, communicatieplatforms. Let op authenticatiescopes (least privilege), idempotentie bij retries, en rate limiting aan de kant van de externe dienst.

---

## Betrouwbaarheid in productie: vijf patronen

Tools falen altijd op het verkeerde moment. Netwerken time-outen. APIs geven 429-errors. Modellen hallucineren tool-parameters. Robuuste foutafhandeling is geen luxe maar de basisconditie voor production-grade tool integration.

**Retry met exponential backoff + jitter**: 3 retries voor transitoire fouten (rate limits, timeouts, 5xx). Maximaal 1–2 retries bij kwaliteitsfouten — meer retries leveren dezelfde hallucinatie. Geen retry bij permanente fouten (401/403, 400, context window overflow) [1, 2].

**Circuit breaker**: na N mislukkingen over een tijdvenster wordt de verbinding "geopend" — verzoeken falen direct zonder de service te bereiken. Fail in microseconds i.p.v. 30 seconden spinner. Drie staten: CLOSED (normaal), OPEN (weigert alles), HALF-OPEN (test herstel). Parameters uit productie: voor LLM APIs drempel 50% failures over 20 requests; voor externe APIs 30% over 10 requests. Cooldown: start 30 seconden, exponential backoff tot max 5 minuten [1].

**Timeout management**: elke externe call heeft een expliciete timeout. LLM standaard 30 seconden; complexe redenering 60 seconden; inter-agent communicatie 10 seconden; externe API's 3–10 seconden afhankelijk van de service [1].

**Fallback mechanismes**: goedkoper model → cached response → gedeeltelijke response met uitleg → human escalation → "service niet beschikbaar". Semantisch: niet-urgente acties uitstellen, onzekere uitkomsten naar menselijke review routeren.

**Graceful degradation via `is_error`**: een falende tool stuurt `is_error: true` terug in het tool-resultaat zodat het model het falen ziet en kan compenseren — vraag om verduidelijking, probeer alternatieve aanpak, of rapporteer de beperking. Goede foutberichten zijn geen nice-to-have: ze zijn de instructie die het model gebruikt voor herstel [1, 5].

Bewijs: consistent geïmplementeerde error handling verhoogde agentbetrouwbaarheid in een gedocumenteerde productiecasus van 87% naar 99.2% [5].

---

## Beveiliging: de executielaag verdedigt, niet het model

De meest bepalende beveiligingsles voor tool integration: behandel het LLM als een untrusted intermediary, niet als een trusted component. Security-grenzen moeten worden afgedwongen op de executielaag, onafhankelijk van het model. Een model dat via prompt injection kan worden gemanipuleerd om zijn instructies te negeren, kan geen veiligheidsgrens bewaken die afhankelijk is van die instructies [8].

**LLM01: Prompt Injection — de hoogste prioriteit** [6]:

Directe injectie: een gebruiker probeert via input het model om te leiden.
Indirecte injectie: een tool retourneert content die kwaadaardige instructies bevat — een webpagina, document, API-response, of MCP-tool-beschrijving. Dit is de gevaarlijkste variant.

Reële aanval (Log-To-Leak): een aanvaller injecteert instructies in de *beschrijving* van een MCP-tool, die de agent dwingen een logging-tool aan te roepen om alle interacties te exfiltreren — user queries, tool responses, agent replies [7].

Mitigaties:
- Scan tool-resultaten voor injection-patronen vóór ze het model context ingaan (PromptInjectionShield-patroon)
- Plan-Then-Execute: scheid planfase (zonder user-content en tool-resultaten) van uitvoeringsfase
- Output screening: beoordeel de output van het model vóór die doorgaat naar downstream tools
- Sla credentials nooit op in de system prompt — injectie kan die uitlezen

**LLM06: Excessive Agency**: implementeer Role-Based Access Control per agent. Een claims-verwerkende agent mag `approve_claim` aanroepen; een klantenservice-agent niet. RBAC wordt afgedwongen op de executielaag, niet via model-instructies [6].

**LLM07: System Prompt Leakage**: privilege separation en authorization bounds checks moeten deterministisch en auditeerbaar zijn, buiten de LLM. Het model-aanbeveling over wat wel of niet mag, is niet voldoende als veiligheidscontrole [6].

**Idempotentie voor write-tools**: tools die data schrijven moeten idempotent zijn of idempotency keys gebruiken. Retries bij netwerkstoringen mogen geen dubbele transacties, dubbele e-mails, of dubbele betalingen veroorzaken.

---

## Audit logging en EU AI Act compliance

Audit logging voor AI-tool integration gaat verder dan traditionele access logs. Per model-interactie moet vastgelegd worden [8]:
- Geverifieerde gebruikersidentiteit en session-ID
- Interactie-samenvatting
- Elke tool-aanroep met volledige parameters
- Elk opgehaald document met ID en gevoeligheidsclassificatie
- Autorisatiebeslissingen inclusief weigeringen
- Output-classificatie (voldoet de output aan verwachte patronen)

Dit is geen optionele keuze voor high-risk AI-systemen in Europa. De EU AI Act (Reg. 2024/1689) stelt per 2 augustus 2026 specifieke vereisten voor high-risk systemen [11]:

**Art. 12 — Record-Keeping**: automatische logging die traceerbaarheid mogelijk maakt. Logs moeten malfunctions en performance drift identificeren, tamper-resistant zijn, minimaal 6 maanden bewaard worden.

**Art. 14 — Human Oversight**: systemen moeten menselijk toezicht mogelijk maken, inclusief de mogelijkheid om te onderbreken via stop-knoppen of override-mechanismes. Een agent zonder expliciete stopcondities en kill-switch is in high-risk contexten niet-compliant.

Praktisch: transformeer audit logging van een forensisch instrument naar een actief detectiesysteem. Anomaliealerts op afwijkende tool-parameters, retrieval-pieken, en output-filter-trigramraten — voordat incidenten plaatsvinden, niet erna [8].

---

## Model Context Protocol: de universele adapter

MCP is het open standaardprotocol (Anthropic, 2024) voor het koppelen van AI-assistenten aan externe systemen. Geadopteerd door OpenAI, Google, Microsoft en tientallen toolvendors. Meer dan 5.000 community-contributed servers [9].

MCP definiëert een stateful, JSON-RPC 2.0-gebaseerde communicatie tussen host (de LLM-applicatie), client (de connector), en server (de tool-implementatie). Tools worden gediscovered via `tools/list`; aanroepen verlopen via `tools/call`; servers sturen `notifications/tools/list_changed` bij runtime-wijzigingen.

Waarom MCP in productie:
- **Één definitie, overal**: MCP-conforme tools werken in LangChain, LlamaIndex, en directe API-implementaties zonder aanpassing
- **Dynamische discovery**: tools kunnen worden toegevoegd of verwijderd zonder herstart
- **Standaard auth**: OAuth 2.1 voor remote MCP servers (beschikbaar sinds maart 2025)
- **Onderhoud**: teams die hun tool-libraries migreerden naar MCP rapporteerden aanzienlijke reductie in onderhoudslast [10]

Transport: gebruik stdio voor development (eenvoudig, debuggable); Streamable HTTP voor productie (remote access, multi-client, OAuth 2.1).

Geavanceerd patroon: agents kunnen zichzelf exposen als MCP server — andere agents roepen hen aan over hetzelfde protocol. Dit creëert een vendor-neutraal multi-agent ecosysteem [7].

---

## Kosten en observability

Tools verbruiken tokens en geld buiten het LLM-model-gebruik om. Elke tool-definitie in de `tools`-array kost input-tokens; bij Claude Opus 4.7 voegt één tool ~313–346 extra system prompt tokens toe. Server-side tools (web_search) hebben usage-based pricing [1].

Kostenbeheer:
- Deferred loading: tools met `defer_loading: true` worden niet upfront in de context geladen
- Tool Search: laat het model zelf in een catalogus zoeken — alleen de gevonden tool wordt geladen
- Prompt caching: tool schemas worden gecached; cache-hit wanneer de tools-array niet wijzigt
- Minimale tools per request: geef de agent alleen de tools die relevant zijn voor de huidige taak

Observability-pijlers voor tool integration [8]:
1. **Traces per tool call**: welke tool, parameters, latency, resultaat
2. **Token-tracking**: input- en output-tokens per aanroep
3. **Kwaliteitsmetrieken**: taak-succespercentage, error rates, retry counts per tool

Anti-patroon: tools alleen monitoren op uptime en latency. Een tool met 95% uptime maar 20% onjuiste resultaten is een productiefout die je zonder kwaliteitsmonitoring nooit ziet.

---

## Tegenstrijdigheden en open vragen

**Geen fundamentele tegenstrijdigheden** gevonden tussen de onderzochte bronnen. De drie primaire spanningsvelden:

1. **MCP vs. directe API-integratie**: MCP verlaagt onderhoudslast significant, maar voegt een indirectielaag toe. Voor simpele, stabiele integraties met één dienst kan directe API-integratie eenvoudiger zijn. MCP wint bij schaal en diversiteit.

2. **Generieke vs. specifieke tools**: computer use is de meest generieke tool (kan alles wat een mens kan), maar ook de traagste en moeilijkst te beveiligen. Narrowere, API-gebaseerde tools zijn sneller, goedkoper en veiliger — maar vereisen dat de doelservice een API heeft.

3. **Beveiliging vs. productiviteit**: strenger RBAC en meer validatie vergroot veiligheid maar verhoogt ook de implementatiecomplexiteit. De juiste granulariteit hangt af van risicoclassificatie van het systeem.

## Open vragen

- Welke EU AI Act high-risk categorieën zijn van toepassing op specifieke tool integration implementaties? (Vergt juridische beoordeling per use case)
- Hoe verhouden MCP's security-model en Anthropic's tool trust levels zich bij multi-tenant productie-deployments?
- Exacte token-overhead van computer use (niet gedocumenteerd in gelezen bronnen)

---

## Sources (preliminary)

1. Anthropic Tool Use Docs — https://docs.anthropic.com/en/docs/tool-use
2. Brightlume AI — Enterprise Tool Use Patterns — https://brightlume.ai/blog/tool-use-patterns-enterprise-ai-agents
3. Webcoderspeed — Designing AI Agent Tools — https://webcoderspeed.com/blog/scaling/ai-agent-tool-design
4. Anthropic — Computer Use — https://docs.anthropic.com/en/docs/agents-and-tools/computer-use
5. Athenic — Error Handling for Production AI Agents — https://getathenic.com/blog/error-handling-reliability-patterns-production-ai-agents
6. OWASP LLM Top 10 2025 — https://owasp.org/www-project-top-10-for-large-language-model-applications/assets/PDF/OWASP-Top-10-for-LLMs-v2025.pdf
7. OpenReview — Log-To-Leak Framework — https://openreview.net/pdf/c2567f59e9e1559bede97fb86ef23287d3b3b5bd.pdf
8. Kiteworks — Securing LLM Apps — https://www.kiteworks.com/cybersecurity-risk-management/prompt-injection-credential-theft-ai-trust/
9. agnt.one — MCP for AI Agents — https://agnt.one/blog/the-model-context-protocol-for-ai-agents
10. Iterathon — Advanced Function Calling 2026 — https://iterathon.tech/blog/advanced-function-calling-tool-composition-production-agents-2026
11. AUTHENSOR — EU AI Act Compliance — https://github.com/AUTHENSOR/AUTHENSOR/blob/main/docs/eu-ai-act-compliance.md
