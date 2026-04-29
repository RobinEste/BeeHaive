Onderzoeker: Gemini

Datum: 2026-04-29

Bronnen: 48

## Samenvatting (1 zin)

De integratie van tools in AI-systemen is in 2026 fundamenteel getransformeerd van gefragmenteerde API-koppelingen naar gestandaardiseerde, protocol-gedreven architecturen zoals het Model Context Protocol (MCP), waarbij de operationele nadruk is verschoven naar deterministische betrouwbaarheid via programmatische executie, strikte semantische contracten, en gelaagde mitigatiestrategieën tegen geavanceerde supply-chain en prompt-injectie aanvallen binnen enterprise-productieomgevingen.

## 1. Architectuurpatronen

De architectuur van agentische AI-systemen heeft zich in de periode 2024-2026 ontwikkeld van ad-hoc integraties en basale 'function calling' naar gestandaardiseerde, breed gedragen protocollen. Het fundamentele uitgangspunt is niet langer óf een Large Language Model (LLM) een externe tool kan aanroepen, maar hoe deze aanroepen schaalbaar, context-efficiënt en veilig kunnen worden georkestreerd in multi-agent ecosystemen.1 Waar eerdere experimenten strandden op schaalbaarheidsproblemen, kenmerkt de huidige enterprise-architectuur zich door een strikte scheiding tussen de redeneerlaag (het model) en de uitvoeringslaag (de infrastructuur).

Een van de meest invloedrijke verschuivingen is de adoptie van het Model Context Protocol (MCP). Geïntroduceerd door Anthropic eind 2024 en inmiddels ondergebracht bij de Linux Foundation, fungeert MCP als de "USB-C voor AI".2 MCP biedt een gestandaardiseerde client/server-architectuur voor bi-directionele communicatie tussen AI-agenten en externe databronnen, tools of prompts.4 Voor de komst van MCP vereiste de integratie van tools een  architectuur, waarbij elke modelaanbieder specifieke connectoren moest bouwen voor elke bedrijfsapplicatie. MCP heeft dit gereduceerd tot een  paradigma, wat de complexiteit van integraties drastisch verlaagt en natuurlijke taalinteracties met complexe infrastructuur mogelijk maakt.2 De roadmap voor MCP in 2026 richt zich specifiek op enterprise-schaalbaarheid. Waar vroege implementaties afhankelijk waren van lokale subprocessen via stdio of Server-Sent Events (SSE), evolueert het protocol nu naar 'stateless HTTP' transporten die robuust functioneren achter load balancers. Andere prioriteiten omvatten sessiemigratie, waarbij server herstarts transparant zijn voor actieve clients, en discoverability via .well-known endpoints voor automatische capaciteitsdetectie.6

Ondanks de standaardisatie via MCP ontstond er een nieuw knelpunt bij schaalvergroting: 'context bloat'. Traditionele implementaties laadden alle tool-definities en JSON-schema's direct in de context window van het model.9 Naarmate agenten toegang kregen tot duizenden tools, consumeerden deze definities soms tot wel 150.000 tokens per aanroep, wat resulteerde in torenhoge kosten en onacceptabele latentie. Bovendien moesten grote intermediaire resultaten, zoals een ruwe database-dump, via het model gepasseerd worden.9 Als antwoord hierop is het architectuurpatroon Programmatic Tool Calling, ook wel Code Execution with MCP genoemd, de productiestandaard geworden. In plaats van directe functie-aanroepen waarbij het LLM data ontvangt via de prompt, schrijft de agent dynamische code (bijvoorbeeld TypeScript of Python) in een streng beveiligde sandbox.9 Deze code interageert rechtstreeks met MCP-servers. Het stelt de agent in staat om 'progressive disclosure' toe te passen (slechts de benodigde directory's verkennen), massale datasets lokaal te filteren en transformeren, en uitsluitend een gecondenseerde samenvatting naar het taalmodel te retourneren. Dit reduceert het tokenverbruik drastisch, vermindert de 'Time-to-First-Token' (TTFT) omdat loops en if-statements deterministisch worden uitgevoerd in plaats van autoregressief door het model, en beschermt Personally Identifiable Information (PII) door ruwe data buiten het zicht van het LLM te houden.9

Naast de interface-architectuur is de orkestratie van het besluitvormingsproces cruciaal. Architecten in 2026 balanceren tussen drie dominante patronen:

- ReAct (Reasoning and Acting): Dit dynamische patroon interleaveert redenering en actie, waarbij de output van een tool onmiddellijk de volgende denkstap van het model voedt.10 Het is uiterst flexibel en ideaal voor eenmalige, context-afhankelijke zoekopdrachten met een lage 'Time-to-First-Action'.11 Echter, ReAct kampt met structurele zwaktes in productie: modellen raken vaak verstrikt in 'infinite loops' bij herhaaldelijke API-fouten en zijn inherent kwetsbaar voor indirecte prompt-injecties, omdat ongefilterde externe observaties direct in de redeneerlus worden opgenomen.11
    
- Plan-Then-Execute (P-t-E): Dit patroon scheidt de planningfase strikt van de uitvoeringsfase. Een geavanceerd 'Planner'-model genereert vooraf een volledige, statische actiegraaf (Directed Acyclic Graph), waarna een lichter 'Executor'-model of deterministische code de stappen iteratief afhandelt.10 P-t-E wordt beschouwd als de superieure keuze voor financiële rapportages, audit-gevoelige taken en hoog-risico omgevingen. Hoewel de initiële planningsfase kostbaar is (vaak tussen 3.000 en 4.500 tokens) en de upfront latentie verhoogt, forceert het Control-Flow Integrity (CFI). Omdat het plan is vergrendeld vóórdat onbetrouwbare tool-data wordt ingelezen, wordt logica-hijacking door kwaadaardige externe bronnen effectief geblokkeerd.11
    
- Agentic Tool Use / Hierarchical Supervisor-Worker: In complexe, multi-modale scenario's fungeert een orchestrator als supervisor die sub-taken delegeert naar gespecialiseerde 'worker'-agenten.14 Dit patroon maakt gebruik van reflexieve zelf-corrigerende loops waarbij een 'Verifier' (mens of AI) de output van een worker controleert voordat deze aan het eindresultaat wordt toegevoegd.15 Dit patroon biedt de hoogste accuraatheid voor complexe documentverwerking, maar vermenigvuldigt de kosten en latentie exponentieel.15
    

|   |   |   |   |   |
|---|---|---|---|---|
|Architectuurpatroon|Mechanisme|Primaire Voordelen|Primaire Nadelen / Risico's|Ideale Usecases|
|ReAct|Iteratieve cyclus van gedachte, actie en observatie|Lage Time-to-First-Action, adaptief op onverwachte data|Gevoelig voor infinite loops, hoge kwetsbaarheid voor prompt injectie|Informatie-zoekopdrachten, ad-hoc klantenservice chatbots|
|Plan-Then-Execute (P-t-E)|Volledige plan-generatie vooraf, gevolgd door sequentiële executie|Control-Flow Integrity, voorspelbaar, deterministisch, veilig|Hoge initiële tokenkosten, trage respons (latency), inflexibel bij runtime errors|Financiële rapportages, enterprise workflows, systeemwijzigingen|
|Programmatic Tool Calling|Agent genereert sandbox code die met tools interageert|Extreme token-efficiëntie bij grote data, PII isolatie, herbruikbare vaardigheden|Vereist complexe en veilige infrastructuur (VM's/Docker sandboxes)|Complexe data pipeline transformaties, ETL processen, massale database queries|

De keuze tussen deze patronen is geen technische voorkeur, maar een risico- en kostenafweging. Teams die P-t-E toepassen voor simpele klantvragen creëren onnodige overhead, terwijl het gebruik van ReAct voor infrastructuur-beheer leidt tot catastrofale veiligheidsrisico's en onvoorspelbare faalscenario's.11

## 2. Betrouwbaarheid

Naarmate AI-agenten evolueren van geïsoleerde experimenten naar kernsystemen in productie, stuiten organisaties op wat in de literatuur de Unreliability Tax wordt genoemd.13 Agentische systemen introduceren probabilistische onzekerheid in voorheen deterministische software-stacks. Een systeem dat 80% van de tijd correct functioneert, is indrukwekkend in een demo, maar waardeloos in een productieomgeving. De kosten in compute, latentie en engineering om deze faalkans te mitigeren, vormen de kern van moderne betrouwbaarheidsarchitectuur.13 De discipline van AgentOps richt zich op het beheer van de volledige levenscyclus van agenten, met een sterke nadruk op foutafhandeling, observability en graceful degradation.16

Een productie-rijp agent-systeem kent strenge acceptatiecriteria. Typische beschikbaarheidsdoelstellingen (uptime) liggen op 99%+ voor kritieke agenten, met responstijden (P50) onder de 2 seconden voor complexe workflows en P95-waarden onder de 5 seconden voor tool-aanroepen. Wanneer deze drempels worden overschreden, dient het systeem direct en veilig in te grijpen.17

Foutafhandeling en Retry-Strategieën De meest voorkomende faaloorzaken in productie zijn infrastructuur-gerelateerd: API-timeouts, rate limits (HTTP 429), en netwerkfouten.17 Wanneer een API faalt door overbelasting, resulteert het onmiddellijk en gelijktijdig herproberen door meerdere agenten in een 'thundering herd'-probleem, wat de downstream service definitief uitschakelt.19 De industriestandaard in 2025-2026 is het gebruik van exponential backoff met random jitter.19 In populaire frameworks zoals LangChain en LangGraph worden deze parameters expliciet gedefinieerd. Een typische productie-configuratie (bijvoorbeeld via de Python Tenacity bibliotheek) hanteert de volgende concrete waarden:

- Een initiële wachttijd en multiplier van 0.25 seconden (wait_random_exponential(multiplier=0.25, max=6)).
    
- Een toevoeging van 'jitter' (een kleine, willekeurige vertraging) om verzoeken te desynchroniseren.
    
- Een harde limiet op de wachttijd (maximaal 6 seconden per poging) om onacceptabele gebruikerslatentie te voorkomen.
    
- Een absolute stopsituatie na maximaal 4 tot 5 pogingen (stop_after_attempt(4)), waarbij de agent overschakelt op een fallback-strategie.20 Voor fouten van het model zelf, zoals malformed JSON of hallucinerende argumenten, dicteert de best practice een Retry-Classify Loop. In plaats van blinde retries, wordt de specifieke stacktrace of het validatie-uitzonderingsrapport als een correctie-prompt teruggevoerd naar het model. Interne benchmarks tonen aan dat één gerichte correctiepoging het merendeel van de formatteringsfouten oplost, terwijl verdere pogingen enkel budget verbranden.19
    

Circuit Breakers en Graceful Degradation Als een API of tool structureel onbereikbaar is, is het zinloos om resources te verspillen. Circuit breakers fungeren als veiligheidskleppen. Na een vooraf ingesteld aantal opeenvolgende fouten 'klapt' de stroomonderbreker open en wordt de tool uit de beschikbare set van de agent gehaald.17 Het systeem degradeert gracefully, wat betekent dat de agent via een fallback-flow ofwel een gecachte versie van de data raadpleegt, ofwel een alternatieve, veiligere tool gebruikt.17 Indien een kritiek proces faalt, escaleert het systeem naar een Human-in-the-Loop (HITL) escalatie-wachtrij in plaats van af te sluiten met een fatale crash.23 Periodiek laat de circuit breaker gecontroleerde testverzoeken door (half-open status) om te detecteren of de dienst is hersteld.19

Observability en State Management De non-deterministische aard van agenten vereist verregaande observability. Traditionele applicatie-logging (APM) is ontoereikend omdat het de semantische context van het LLM-besluit mist. Elke tool-aanroep, inclusief de verstrekte input, de ontvangen payload en de gegenereerde redenering (reasoning trace), moet worden vastgelegd met een unieke trace-ID, een agent-ID en een tijdstempel.19 Platformen zoals LangSmith of W&B Weave worden ingezet om deze complexe interacties inzichtelijk te maken en afwijkingen, zoals 'context overflow', in real-time te detecteren.23 Cruciaal voor betrouwbaarheid in asynchrone processen is state checkpointing. Met behulp van persistente oplossingen zoals PostgresSaver in LangGraph wordt de status van de conversatie en het geheugen van de agent na elke succesvolle stap weggeschreven.19 Mocht een pod in Kubernetes herstarten of een timeout optreden, dan hervat de agent het werk vanaf het laatste JSON-checkpoint, waardoor de herberekende kosten en duplicatie van API-aanroepen worden geminimaliseerd.19 Alarmering is eveneens geëvolueerd: systemen pauzeren automatisch wanneer de foutmarge (error rate) van een specifieke agent binnen een gedefinieerd tijdvak een kritieke drempel overschrijdt, om datacorruptie door 'rogue' operaties te voorkomen.19

|   |   |   |
|---|---|---|
|Parameters / Mechanismen|Implementatie in Productie|Voorbeeld / Threshold|
|Retry Strategie|Exponential Backoff met Jitter|wait_random_exponential(mult=0.25, max=6)|
|Maximum Attempts|Strikte limiet op pogingen bij netwerkfalen|stop_after_attempt(4)|
|Latency Targets|P95 drempels voor upstream API's|Max 5 seconden, daarna timeout genereren|
|State Persistence|Checkpointing na elke hoofdactie|LangGraph PostgresSaver of vector DB|
|Correctie LLM Fouten|Foutmelding teruggeven als prompt|Maximaal 1 correctiepoging per iteratie|

## 3. Beveiliging & governance

De introductie van tools en agentische autonomie heeft de traditionele perimeter-beveiliging van IT-systemen doorkruist. LLM's introduceren een paradigma waarbij ongestructureerde, onbetrouwbare tekst (uit e-mails, webpagina's of interne bestanden) functioneert als uitvoerbare code. De verdedigingsmechanismen moeten zich daarom aanpassen aan een landschap van semantische kwetsbaarheden.

De OWASP LLM Top 10 (Stand 2025-2026) In de herziene versie van de OWASP Top 10 voor Large Language Model Applications voor 2025 behoudt LLM01: Prompt Injection onverminderd de eerste positie.26 Beveiligingsexperts maken hierin een scherp onderscheid tussen directe en indirecte injecties. Directe injecties (jailbreaks, zoals 'DAN'-prompts) worden veroorzaakt door malafide gebruikers.28 Indirecte prompt-injecties (Cross Prompt Injection Attempts, of XPIA) zijn aanzienlijk gevaarlijker voor agenten. Hierbij is de kwaadaardige instructie verborgen in externe data, zoals een onschuldig lijkend document of website, die de agent via een tool inleest. Omdat het LLM geen onderscheid kan maken tussen systeeminstructies en ingelezen data, volgt het blindelings het verborgen commando op.26 Daarnaast ligt de nadruk op LLM06: Excessive Agency (waarbij een agent te veel privileges bezit en onbedoeld schadelijke acties uitvoert) en LLM02: Sensitive Information Disclosure (het lekken van PII of systeemcontext naar onbevoegden).27 Deze risico's vertakken zich direct naar de supply chain (LLM03), waarbij agenten afhankelijk zijn van onbeveiligde API-endpoints of gecompromitteerde tool-bibliotheken.26

De "Log-To-Leak" Aanval en MCP Kwetsbaarheden De standaardisatie via het Model Context Protocol (MCP) heeft onbedoeld een zeer geraffineerd nieuw aanvalsoppervlak gecreëerd, gedocumenteerd in kwetsbaarheden zoals CVE-2025-32711 (EchoLeak in Microsoft Copilot).32 Onderzoekers benoemen dit de Log-To-Leak aanval.33 Traditioneel lag de focus van verdediging bij de input (user prompt) of de output (content filtering). Bij MCP-systemen is de natuurlijke taalbeschrijving van tools in het registratiekanaal echter een blinde vlek gebleken.33

Bij een Log-To-Leak aanval compromitteert een aanvaller de metadata van een tool (bijvoorbeeld via een RUG Pull attack op een MCP registry, waarbij een legitieme tool wordt vervangen door een malafide kopie).30 De geïnjecteerde instructie in de tool-beschrijving bestaat uit vier strategische componenten:

1. Trigger: Bepaalt wanneer het model de kwaadaardige actie moet activeren.
    
2. Tool Binding: Koppelt de actie aan een specifieke (malafide) logging-tool, zodat de agent denkt dat deze essentieel is voor de workflow.
    
3. Justification: Biedt een overtuigende, beleidsmatige rechtvaardiging (bijv. "Voor compliance-redenen moeten alle gebruikersquery's lokaal worden gelogd").
    
4. Pressure: Forceert prioriteit boven andere veiligheidsinstructies.33
    

Als gevolg hiervan zal de agent autonoom en onmerkbaar de malafide logging-tool aanroepen met gevoelige tussenresultaten, wachtwoorden of bedrijfsgeheimen, wat resulteert in data-exfiltratie.33 Omdat de primaire taak van de agent niet verstoord wordt, is deze aanval nagenoeg ondetecteerbaar door reguliere monitoringsystemen.33 Het risico wordt versterkt in de "lethal trifecta" van agenten: toegang tot privé-data, verwerking van onbetrouwbare content, en de capaciteit om externe acties te initiëren.30

Mitigatiestrategieën voor Productie

Om deze complexe aanvalsvectoren het hoofd te bieden, eisen security-architecten een 'defense-in-depth' gelaagdheid voor tool-integratie:

- Principle of Least Privilege (PoLP): Rechten worden niet toegekend op agent-niveau, maar microscopisch op taak-niveau. Authenticatietokens mogen nooit als onbewerkte tekst in de context van het model worden opgeslagen of doorgestuurd; proxy's moeten de feitelijke API-keys injecteren.32
    
- Output-Side Command Validation & RBAC: Omdat injecties niet altijd te voorkomen zijn, moet een onafhankelijke deterministische policy engine fungeren als filter tussen de agent en de uitvoerende tool. Leesoperaties (GET) kunnen automatisch worden goedgekeurd, maar wijzigingsoperaties (POST, DELETE, shell commands) moeten categorisch worden geblokkeerd of door routering worden afgedwongen aan stringente permissies.11
    
- Human-in-the-Loop (HITL) voor Write Operations: Autonome agents mogen fundamenteel geen infrastructuurwijzigingen doorvoeren zonder expliciete menselijke goedkeuring, onafhankelijk van hoe verfijnd de detectiesystemen zijn.37
    

Governance en de EU AI Act (Artikel 12 en 14) De juridische realiteit dwingt in 2026 strikte compliance af via de EU Artificial Intelligence Act, welke lokaal in Nederland wordt geïmplementeerd met decentraal toezicht (ontwerpwet van april 2026).38 De wet specificeert verregaande verplichtingen voor agentische systemen gecategoriseerd als 'hoog-risico'.

- Artikel 12 (Record-Keeping): Vereist onweerlegbare traceerbaarheid via automatische logboekregistratie gedurende de levensduur van het systeem. Dit eist niet slechts systeemlogs, maar specifieke datapunten: de exacte start- en eindtijd van elk gebruik, de identificatie van de referentiedatabase die is geraadpleegd (cruciaal voor RAG-operaties), en de precieze invoergegevens die tot een output hebben geleid.42 Tools zoals LangSmith en LangGraph vervullen deze wettelijke verplichtingen door full reasoning traces en timestamp-gebaseerde opslag te leveren.24
    
- Artikel 14 (Human Oversight): Legt vast dat hoog-risico systemen zodanig ontworpen moeten zijn, inclusief gepaste interface-tools, dat menselijk toezicht te allen tijde gegarandeerd is om veiligheidsrisico's en schendingen van fundamentele rechten in te dammen.43 In agent-architecturen vertaalt zich dit naar systemen met HITL annotation queues, ingebouwde webhooks die het proces pauzeren bij lage confidence-scores, en interfaces die de redeneerstappen van het model expliciteren voor een supervisor.17 Zonder deze mechanismen zijn autonome agenten binnen de Europese ruimte niet legaal inzetbaar.
    

## 4. Toolcategorieën & trade-offs

De evaluatie van tool-integraties in 2026 vereist een diepgaand begrip van de asymmetrische trade-offs tussen capaciteit, operationele kosten, latentie en risico. Er bestaat geen universeel model; architecten selecteren tools op basis van het beoogde takenprofiel.

1. Search & RAG (Retrieval-Augmented Generation)

- Wanneer gebruiken: Noodzakelijk voor fact-checking, het ontsluiten van actuele marktinformatie en het overbruggen van kennishiaten in het LLM via interne of externe corpora.11
    
- Trade-offs en Latentie: Web- en documentzoekopdrachten zijn intensief I/O-gebonden. Het sequentieel uitvoeren van zoekopdrachten levert funeste latentie op. Optimalisatie wordt bereikt door de agent parallelle zoekstrategieën te laten ontwerpen via Directed Acyclic Graphs (DAGs), wat prestatieverbeteringen tot 3.6x kan realiseren.11 Om prompt bloat te voorkomen, past men 'RAG-MCP' toe, waarbij semantische retrieval het kaf van het koren scheidt vóórdat de tekst het LLM bereikt, waardoor enkel uiterst relevante tool-beschrijvingen overblijven.45
    
- Beveiligingsrisico: Systemen die data van het openbare internet of ongestructureerde bedrijfsdocumenten verwerken, zijn extreem kwetsbaar voor indirecte prompt-injectie (XPIA). Om de "lethal trifecta" te doorbreken, moeten Search- en RAG-tools strikt als 'read-only' geclassificeerd worden. De agent mag tijdens een onderzoekstaak onder geen beding tegelijkertijd actieve 'write'-tools (zoals het verzenden van e-mails of wijzigen van databases) tot zijn beschikking hebben.11
    

2. Code Execution en Calculaties

- Wanneer gebruiken: Voor wiskundige bewerkingen, massale data-verwerking (zoals het analyseren van 10.000 rijen in een CSV), of complexe logische transformaties die via autoregressieve LLM-inferentie inherent onbetrouwbaar zijn.9
    
- Trade-offs en Kosten: Code-executie levert ongekende token-efficiëntie op. In plaats van ruwe data door de context window te sturen, genereert de agent een iteratief script (bijv. Python) dat de data extern verwerkt en uitsluitend het berekende resultaat of de grafiek retourneert.9
    
- Beveiligingsrisico: Het fundament van dit voordeel is tevens het grootste risico: Remote Code Execution (RCE). Een 'defense-in-depth' benadering is onvermijdelijk. Gegenereerde code moet geïsoleerd worden uitgevoerd in geëphemereerde Docker-sandboxes of externe virtuele machines, versterkt met strenge netwerk- en cpu-restricties, om te voorkomen dat agent-gegenereerde code het host-besturingssysteem overneemt of netwerkpoorten scant.9
    

3. Databases en Interne API's

- Wanneer gebruiken: Voor het inzien of wijzigen van gestructureerde administratieve systemen, CRM-platforms en financiële grootboeken.14
    
- Trade-offs en Beveiliging: De praktijk heeft aangetoond dat het geven van directe SQL-toegang ('Text-to-SQL') aan een agent onverantwoord is vanwege hallucinerende joins, syntaxisfouten en destructieve DROP TABLE-verzoeken.8 De productiestandaard vereist dat databasetoegang verloopt via MCP-servers die fungeren als strikte ORM- of REST-API wrappers, waarbij enkel gedefinieerde CRUD-operaties zijn gepermitteerd.8
    
- Role-Based Access Control (RBAC): De capaciteiten van de agent worden dynamisch beperkt per taak. Een agent in de rol van 'DataAnalyst' ontvangt lokaal slechts leesrechten, en kan de database onmogelijk manipuleren, zelfs als een prompt-injectie dit zou dicteren.11
    

4. Browser Automation en Computer Use

- Wanneer gebruiken: Als uiterste middel ("last resort") voor integratie met gesloten, verouderde systemen zonder toegankelijke API's, of bij visuele UI-taken. Pioniers zoals Anthropic (Linux VM Computer Use) en OpenAI (Operator / Computer Using Agent) leiden deze categorie.46
    
- Trade-offs en Kosten: Dit is met afstand de traagste en duurste categorie. Omdat 'Computer Use' steunt op het continu analyseren van screenshots om muis- en toetsenbordacties te sturen, verbruikt het massale hoeveelheden image-tokens. Een eenvoudige interactiecyclus kan moeiteloos tienduizenden tokens per minuut verbranden.46 Daarnaast is de latentie immens vanwege de noodzakelijke visuele feedback-loops.
    
- Beveiliging: De implementatie verschilt fundamenteel: OpenAI beperkt zijn 'Operator' tot web-browsing binnen een door OpenAI beheerde cloud-omgeving, terwijl Anthropic volledige desktop-toegang levert op klantomgevingen. Het laatste eist buitengewone technische isolatie (VPC's, proxy's) om te voorkomen dat de agent autonoom kwaadaardige applicaties op het host-systeem downloadt en uitvoert.46
    

5. Externe 3rd-Party MCP-Servers

- Wanneer gebruiken: Voor pijlsnelle integratie met algemene platforms zoals GitHub, Slack, of ServiceNow zonder handmatige connectoren te onderhouden.4
    
- Trade-offs en Risico's: Hoewel dit de ontwikkelingskosten minimaliseert, ontstaat er een afhankelijkheid van externe pakketbeheerders. Dit introduceert het risico op supply-chain aanvallen en RUG Pull-exploits, waarbij een aanvaller een vertrouwde externe tool via een update onopgemerkt vervangt door een malafide versie, waardoor het AI-systeem onmiddellijk gecompromitteerd raakt zonder dat er aanpassingen aan het LLM of de prompts nodig waren.30
    

## 5. Operationele best practices

Een agentisch systeem dat conceptueel goed is ontworpen, zal falen als de operationele parameters (AgentOps) tekortschieten. De operationele standaard in 2026 omvat rigoureuze afspraken omtrent versioning, datastructuren en kostenbeheersing.

Schema Versioning en Namespacing In agentische netwerken fungeren tool-definities niet als documentatie voor ontwikkelaars, maar als harde API-contracten voor het taalmodel. Een kleine wijziging in de verwachte parameterstructuur kan het model desoriënteren en een productiepijplijn blokkeren. De industriestandaard is de strikte toepassing van Semantic Versioning (SemVer). Een verhoging van v1.8.5 naar v1.9.0 communiceert een toevoeging (additive) waardoor orkestrators de update veilig en automatisch kunnen doorvoeren, terwijl een wijziging naar v2.0.0 (breaking change) eist dat het systeem de integratie tijdelijk opschort of test via een canary-fase.50 Voor grootschalige systemen is namespacing essentieel. Interne evaluaties bij grote aanbieders tonen aan dat het gebruik van specifieke prefixen of suffixen (bijv. finance_retrieve_invoice in plaats van retrieve_invoice) een non-triviale en significante impact heeft op de selectienauwkeurigheid van het model.52 Op infrastructuurniveau worden Kubernetes-namespaces gebruikt, versterkt met Resource Quota's en Network Policies (ingress/egress), om de netwerk-isolatie tussen multi-tenant workloads in stand te houden.53 De tool-beschrijving (description) fungeert niet als bijzaak, maar vormt het meest kritieke stuursignaal voor de agent om te bepalen wanneer en met welke intentie een gereedschap gehanteerd moet worden.25

JSON Schema Strict Mode Omdat LLM's inherently vrije tekst genereren, is het extraheren van voorspelbare datastructuren historisch problematisch geweest. Om dit te mitigeren bieden providers zoals OpenAI en Google native JSON Schema Strict Mode (via de response_format API).54 Dit garandeert dat de gegenereerde structuur syntactisch 100% klopt met het aangeleverde Pydantic- of JSON-schema.57 Echter, empirische benchmarks uit 2025 en 2026 waarschuwen dat strict mode een vals gevoel van veiligheid kan creëren. Hoewel het interface misuse (zoals foutieve veldnamen of missende attributen) succesvol elimineert, adresseert het geenszins semantic misuse.58 Lokale, goedkopere of open-weights modellen zijn in staat syntactisch perfecte JSON af te leveren waarvan de datawaardes, ratio's en argumenten volledig gehallucineerd of logisch onjuist zijn.58 Strict mode stroomlijnt de parsering, maar vervangt nooit onafhankelijke logische content-validatie in productie.

Latency Budgets en Orkestratie Tijd is een kritieke variabele; in applicaties zoals voice-agents, waar de menselijke conversatiedrempel laag ligt, dwingt de architectuur strikte 'latency budgets' af.60 Benchmark-targets voor enterprise agenten in 2026 zijn onverbiddelijk:

- Direct Model Call (Simpele extracties): P50 latentie onder de 500 milliseconden, P95 onder de 1 seconde.
    
- Single Agent met Tools: P50 onder de 2 seconden, P95 onder de 4 seconden.
    
- Multi-Agent Orchestration: P50 onder de 3 seconden, P95 onder de 6 seconden.18 Elke toevoeging van redeneerlussen (Reflexion) of 'worker-agents' verbetert de accuraatheid (vaak naar 95%+ succes), maar vertraagt de workflow dramatisch.13 Architecten bewaken de balans door een Thinking Budget te configureren; het systeem dynamiseert het aantal toegestane denkstappen afhankelijk van de benodigde snelheid versus prioriteit.13
    

Kosten-Management en Intelligent Routing Waar traditionele software via een voorspelbaar SaaS-model verloopt, introduceren agentische loops verborgen exponentiële 'variabele intelligentie' kosten, grotendeels gedreven door extreme context window uitbreidingen (soms groter dan 100.000 tokens voor complexe tool-definities).13 Een ongeoptimaliseerde pipeline kan probleemloos duizenden dollars per maand verbranden op repetitieve foutieve redeneringen.48 De best practices voor kostenreductie omvatten:

1. Response en Semantic Caching: Het integreren van semantische vector-caching. Als een inkomende taak 90% overeenkomt met een eerdere opgeloste taak, levert de cache het antwoord zonder de API te belasten. Verwachte besparingen: 30-70%.61
    
2. Prompt en Context Caching: Het hergebruiken van gestructureerde tool-schema's, systeemprompts en langdurige RAG-documenten (ondersteund door Anthropic en OpenAI caching) bespaart aanzienlijk op input-tokens en latentie over meerdere interactierondes.56
    
3. Intelligent Model Routing: (Bijv. via RouteLLM). Een goedkope 'classifier'-agent analyseert het inkomende verzoek. Complexe redeneervragen gaan naar top-tier modellen (GPT-5.5 of Claude Opus), terwijl simpele aggregaties of extracties onmiddellijk worden gedelegeerd naar snelle, lichte modellen (Gemini Flash of Claude Haiku). Dit reduceert de operationele kosten tot 80% vergeleken met platte model-deployments.62
    

## 6. Industrie-positionering

In 2026 kenmerkt het AI-infrastructuurlandschap zich door sterke, asymmetrische specialisaties van de voornaamste 'Foundation Model' aanbieders en orkestratie-frameworks. Platformen concurreren niet langer puur op intelligentie (MMLU-scores), maar op de inbedding van agentische werkstromen, betrouwbaarheid in lange cycli, en de mate van vendor lock-in.

Foundation Model Providers

- Anthropic (Claude): Anthropic profileert zich onbetwist als de marktleider op het vlak van deterministische agent-orkestratie, bedrijfszekerheid, en ecosysteem-standaardisatie.54 Door het initiëren van het open Model Context Protocol (MCP) en het bieden van een uiterst 'schoon' tool-use schema, leveren de Claude-modellen (Sonnet/Opus) exceptionele prestaties voor lange asynchrone processen. In rigoureuze benchmarks (zoals complexe 5-staps agentische operaties) noteert Claude de hoogste scoringsgraad (vaak >95% success rate), grotendeels te danken aan de capaciteit om niet te 'ontsporen' bij opeenvolgende tool-aanroepen en de diepte van de gecontroleerde 'extended thinking' protocollen.54
    
- OpenAI (GPT): OpenAI blijft de marktleider op het vlak van brede ecosystemen en multimodale functionaliteit.65 Hun positionering steunt op verticale integratie. Door krachtige 'native' oplossingen te bieden zoals de Assistants API, proberen ze RAG, state management en code execution af te schermen binnen hun eigen ecosysteem.66 De specifieke agentische modellen, zoals GPT-5.4 en GPT-5.5, beschikken over formidabele JSON Strict Mode garanties en domineren complexe analytische computer-operaties. Echter, benchmarks plaatsen OpenAI net onder Anthropic wat betreft stabiele multi-tool orkestratie (met een success rate rond de 88% op complexe ketens).54
    
- Google Gemini: Google benut de enorme schaal en rekenkracht van het Vertex AI enterprise platform.54 Gemini's positionering draait bijna uitsluitend rond massale contextverwerking; met context windows van meer dan 1 miljoen (of theoretisch 2+ miljoen) tokens kan het model fungeren als een verwerkingsmotor voor immens grote documentenbestanden.56 Echter, op het niveau van precieze tool-integratie vertoont Gemini nog regelmatig 'flaky shapes' (waarbij JSON-antwoorden foutief in markdown worden gewikkeld), wat de betrouwbaarheid op 5-staps orkestraties verlaagt naar een relatief bescheiden 75%.54
    

Open-Weights en Frameworks Naast de giganten positioneren open-weights modellen zoals DeepSeek R1/V3 en Mistral Large 3 zich als formidabele, uiterst kostenefficiënte uitdagers voor taken waar chain-of-thought redenering essentieel is, zonder de enorme overheadkosten van de API-giganten, cruciaal voor air-gapped deployments in sectoren met strikte privacy-eisen.54

Het applicatielandschap om deze modellen heen heeft de taak van orkestratie grotendeels weggenomen bij de modellen en overgeheveld naar gespecialiseerde orchestrators.

- LangChain & LangGraph: Beschouwd als de onbetwiste industriestandaard voor enterprise-orkestratie. Waar LangChain functioneert als de verzameling componenten, biedt de grafen-architectuur van LangGraph de hard benodigde persisterende 'state', 'time-travel debugging' en native Human-in-the-Loop mechanismen voor compliancy. In latency-benchmarks opereert LangGraph superieur in termen van responstijd en token-efficiëntie bij gerichte taken.3
    
- CrewAI & AutoGen: Positioneren zich exclusief op multi-agent processen, waarbij verschillende persona's (agenten) met elkaar in overleg treden. Hoewel CrewAI de instapdrempel aanzienlijk verlaagt, tonen benchmarks aan dat de interne communicatieloops een extreme impact hebben op het tokenverbruik en de latentie, zelfs voor triviale operaties. Hierdoor wordt het primair aanbevolen voor offline exploratieve data-analyse in plaats van reactieve productie-applicaties.73
    
- LlamaIndex: Consolideert zijn reputatie door zich exclusief te richten op geavanceerde RAG (Retrieval-Augmented Generation) integraties, vaak functionerend als de toeleverancier van context voor een LangGraph-orkestrator, resulterend in een zeer weerbare en modulaire hybride enterprise stack.73
    

## Belangrijkste bevindingen

- De Standaardisatie via MCP en Code Execution: De overstap naar het Model Context Protocol heeft de integratie-complexiteit (van N×M naar N+M connecties) fundamenteel vereenvoudigd. Omdat tool-definities enorme context windows consumeren (vaak 150.000+ tokens), transformeert enterprise-orkestratie naar 'Code Execution'. Hierbij schrijft de agent deterministische sandbox-code in plaats van directe interactie met API's, wat de TTFT versnelt, context-bloat voorkomt, en PII buiten de redeneerlaag isoleert.
    
- De 'Unreliability Tax' vereist AgentOps Precisie: Fouttolerantie is niet langer gebaseerd op lineaire retries. Strikte parameters zoals 'exponential backoff met jitter' (max. 4 pogingen, vertraging < 6 sec) en circuit breakers voorkomen het 'thundering herd'-effect en verplichten het systeem tot graceful degradation. Checkpointing via grafen-frameworks (zoals LangGraph's PostgresSaver) vermijdt de herberekende kosten van vastgelopen multi-turn workflows.
    
- Het Onzichtbare Gevaar van 'Log-To-Leak' (MCP Kwetsbaarheid): Via MCP ontstaat een nieuw, kritiek aanvalsoppervlak waarbij de kwaadaardige payload niet afkomstig is van de gebruiker, maar geïnjecteerd wordt via de metadata (tool descriptions) van een gecompromitteerde MCP-server (RUG Pull). De agent wordt ongemerkt geprest ('Pressure' en 'Tool Binding') om een log-tool te activeren en data te exfiltreren. Dit dwingt architecten tot het afdwingen van output-side command validation en harde restricties ('Least Privilege') via onafhankelijke policy engines.
    
- Jurisprudentie Verankerd in de Architectuur (AI Act): De EU AI Act, concreet via implementaties zoals de Nederlandse toezichtswet van april 2026, verbiedt in feite de inzet van niet-auditeerbare ReAct-loops voor hoog-risico beslissingen. Artikel 12 eist cryptografische bewaring van timestamps, redeneersporen en reference-databases, terwijl Artikel 14 implementatie dicteert van harde Human-in-the-Loop (HITL) systemen met gepaste pauze-webhooks vóór het uitvoeren van state-modificerende handelingen.
    
- De Architecturale Triage (Kosten vs. Latency vs. Veiligheid): P-t-E (Plan-Then-Execute) wordt algemeen beschouwd als het meest veilige en traceerbare orkestratiepatroon ter bescherming tegen indirecte prompt injecties, ten koste van hoge upfront planningkosten (3000+ tokens). Operationeel dwingt de massale tokenconsumptie bedrijven tot gelaagde kostenmitigatie: het semantisch cachen van responses en het toepassen van 'Intelligent Model Routing' (waarbij simpele extracties naar goedkope, snelle modellen worden doorgestuurd) realiseert kostenreducties tot ruim 80% zonder kwaliteitsverlies, een onmisbare tactiek voor een duurzame productieomgeving in 2026.
    

## Bronnen

4 [https://www.splunk.com/en_us/blog/artificial-intelligence/top-10-ai-trends-2025-how-agentic-ai-and-mcp-changed-it.html](https://www.splunk.com/en_us/blog/artificial-intelligence/top-10-ai-trends-2025-how-agentic-ai-and-mcp-changed-it.html) 1 [https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/three-tiers-of-agentic-ai---and-when-to-use-none-of-them/4510377](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/three-tiers-of-agentic-ai---and-when-to-use-none-of-them/4510377) 9 [https://www.anthropic.com/engineering/code-execution-with-mcp](https://www.anthropic.com/engineering/code-execution-with-mcp) 5 [https://developers.redhat.com/articles/2025/08/12/how-build-simple-agentic-ai-server-mcp](https://developers.redhat.com/articles/2025/08/12/how-build-simple-agentic-ai-server-mcp) 2 [https://en.wikipedia.org/wiki/Model_Context_Protocol](https://en.wikipedia.org/wiki/Model_Context_Protocol) 7 [https://modelcontextprotocol.io/development/roadmap](https://modelcontextprotocol.io/development/roadmap) 16 [https://www.uipath.com/blog/ai/agent-ops-operationalizing-ai-agents-for-enterprise](https://www.uipath.com/blog/ai/agent-ops-operationalizing-ai-agents-for-enterprise) 19 [https://fast.io/resources/ai-agent-error-handling/](https://fast.io/resources/ai-agent-error-handling/) 23 [https://medium.com/online-inference/best-practices-for-building-effective-ai-agents-and-multi-agent-systems-2c7fe11c9605](https://medium.com/online-inference/best-practices-for-building-effective-ai-agents-and-multi-agent-systems-2c7fe11c9605) 22 [https://dev.to/pockit_tools/7-patterns-that-stop-your-ai-agent-from-going-rogue-in-production-5hb1](https://dev.to/pockit_tools/7-patterns-that-stop-your-ai-agent-from-going-rogue-in-production-5hb1) 17 [https://vatsalshah.in/blog/10-best-practices-reliable-ai-agents](https://vatsalshah.in/blog/10-best-practices-reliable-ai-agents) 31 [https://owasp.org/www-project-top-10-for-large-language-model-applications/](https://owasp.org/www-project-top-10-for-large-language-model-applications/) 26 [https://trydeepteam.com/docs/frameworks-owasp-top-10-for-llms](https://trydeepteam.com/docs/frameworks-owasp-top-10-for-llms) 27 [https://genai.owasp.org/llm-top-10/](https://genai.owasp.org/llm-top-10/) 43 [https://artificialintelligenceact.eu/article/14/](https://artificialintelligenceact.eu/article/14/) 42 [https://artificialintelligenceact.eu/article/12/](https://artificialintelligenceact.eu/article/12/) 44 [https://www.tandfonline.com/doi/full/10.1080/17579961.2023.2245683](https://www.tandfonline.com/doi/full/10.1080/17579961.2023.2245683) 24 [https://www.langchain.com/blog/langsmith-langchain-oss-eu-ai-act](https://www.langchain.com/blog/langsmith-langchain-oss-eu-ai-act) 65 [https://www.mindstudio.ai/blog/anthropic-vs-openai-vs-google-agent-strategy](https://www.mindstudio.ai/blog/anthropic-vs-openai-vs-google-agent-strategy) 70 [https://www.datastudios.org/post/chatgpt-vs-google-gemini-vs-anthropic-claude-comprehensive-comparison-report-capabilities-perfo](https://www.datastudios.org/post/chatgpt-vs-google-gemini-vs-anthropic-claude-comprehensive-comparison-report-capabilities-perfo) 46 [https://artificialanalysis.ai/agents](https://artificialanalysis.ai/agents) 33 [https://openreview.net/forum?id=UVgbFuXPaO](https://openreview.net/forum?id=UVgbFuXPaO) 28 [https://genai.owasp.org/llmrisk/llm01-prompt-injection/](https://genai.owasp.org/llmrisk/llm01-prompt-injection/) 36 [https://www.paloaltonetworks.com/cyberpedia/what-is-a-prompt-injection-attack](https://www.paloaltonetworks.com/cyberpedia/what-is-a-prompt-injection-attack) 32 [https://arxiv.org/html/2509.10540v1](https://arxiv.org/html/2509.10540v1) 52 [https://www.anthropic.com/engineering/writing-tools-for-agents](https://www.anthropic.com/engineering/writing-tools-for-agents) 14 [https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns) 18 [https://www.aviso.com/blog/how-to-evaluate-ai-agents-latency-cost-safety-roi](https://www.aviso.com/blog/how-to-evaluate-ai-agents-latency-cost-safety-roi) 3 [https://www.digitalapplied.com/blog/mcp-vs-langchain-vs-crewai-agent-framework-comparison](https://www.digitalapplied.com/blog/mcp-vs-langchain-vs-crewai-agent-framework-comparison) 75 [https://www.trixlyai.com/blogs/langchain-vs-llamaindex-vs-autogen-vs-crewai-which-framework-actually-ships-in-2026](https://www.trixlyai.com/blogs/langchain-vs-llamaindex-vs-autogen-vs-crewai-which-framework-actually-ships-in-2026) 73 [https://www.turing.com/resources/ai-agent-frameworks](https://www.turing.com/resources/ai-agent-frameworks) 8 [https://clickhouse.com/blog/how-to-build-ai-agents-mcp-12-frameworks](https://clickhouse.com/blog/how-to-build-ai-agents-mcp-12-frameworks) 13 [https://online.stevens.edu/blog/hidden-economics-ai-agents-token-costs-latency/](https://online.stevens.edu/blog/hidden-economics-ai-agents-token-costs-latency/) 60 [https://www.twilio.com/en-us/blog/developers/best-practices/guide-core-latency-ai-voice-agents](https://www.twilio.com/en-us/blog/developers/best-practices/guide-core-latency-ai-voice-agents) 76 [https://galileo.ai/blog/hidden-cost-of-agentic-ai](https://galileo.ai/blog/hidden-cost-of-agentic-ai) 58 [https://arxiv.org/html/2603.13404v1](https://arxiv.org/html/2603.13404v1) 57 [https://agenta.ai/blog/the-guide-to-structured-outputs-and-function-calling-with-llms](https://agenta.ai/blog/the-guide-to-structured-outputs-and-function-calling-with-llms) 59 [https://medium.com/@lyx_62906/which-cheap-and-oss-llms-actually-produce-valid-json-9b002e106b6d](https://medium.com/@lyx_62906/which-cheap-and-oss-llms-actually-produce-valid-json-9b002e106b6d) 20 [https://medium.com/@Praxen/7-retry-timeout-rules-for-langchain-tools-760d1a4dd69d](https://medium.com/@Praxen/7-retry-timeout-rules-for-langchain-tools-760d1a4dd69d) 25 [https://www.digitalapplied.com/blog/langchain-ai-agents-guide-2025](https://www.digitalapplied.com/blog/langchain-ai-agents-guide-2025) 21 [https://sparkco.ai/blog/mastering-retry-logic-agents-a-deep-dive-into-2025-best-practices](https://sparkco.ai/blog/mastering-retry-logic-agents-a-deep-dive-into-2025-best-practices) 33 [https://openreview.net/forum?id=UVgbFuXPaO](https://openreview.net/forum?id=UVgbFuXPaO) 30 [https://www.netskope.com/blog/securing-llm-superpowers-the-invisible-backdoors-in-mcp](https://www.netskope.com/blog/securing-llm-superpowers-the-invisible-backdoors-in-mcp) 77 [https://www.docker.com/blog/mcp-horror-stories-github-prompt-injection/](https://www.docker.com/blog/mcp-horror-stories-github-prompt-injection/) 78 [https://developer.microsoft.com/blog/protecting-against-indirect-injection-attacks-mcp](https://developer.microsoft.com/blog/protecting-against-indirect-injection-attacks-mcp) 53 [https://rafay.co/ai-and-cloud-native-blog/mastering-kubernetes-namespaces-advanced-isolation-resource-management-and-multi-tenancy-strategies](https://rafay.co/ai-and-cloud-native-blog/mastering-kubernetes-namespaces-advanced-isolation-resource-management-and-multi-tenancy-strategies) 11 [https://arxiv.org/pdf/2509.08646](https://arxiv.org/pdf/2509.08646) 12 [https://www.getmaxim.ai/articles/a-practitioners-guide-to-prompt-engineering-in-2025/](https://www.getmaxim.ai/articles/a-practitioners-guide-to-prompt-engineering-in-2025/) 10 [https://arxiv.org/html/2509.06278v1](https://arxiv.org/html/2509.06278v1) 54 [https://renezander.com/guides/llm-api-comparison/](https://renezander.com/guides/llm-api-comparison/) 79 [https://arxiv.org/html/2604.17125v1](https://arxiv.org/html/2604.17125v1) 37 [https://arxiv.org/html/2604.15368v1](https://arxiv.org/html/2604.15368v1) 34 [https://www.researchgate.net/publication/403975846_LogJack_Indirect_Prompt_Injection_Through_Cloud_Logs_Against_LLM_Debugging_Agents](https://www.researchgate.net/publication/403975846_LogJack_Indirect_Prompt_Injection_Through_Cloud_Logs_Against_LLM_Debugging_Agents) 35 [https://openreview.net/pdf?id=UVgbFuXPaO](https://openreview.net/pdf?id=UVgbFuXPaO) 45 [https://huggingface.co/papers?q=RAG](https://huggingface.co/papers?q=RAG) 66 [https://github.com/miptgirl/miptgirl_medium/blob/main/dspy_rlm/dspy_rlm.ipynb](https://github.com/miptgirl/miptgirl_medium/blob/main/dspy_rlm/dspy_rlm.ipynb) 67 [https://medium.com/data-science-at-microsoft/ai-agent-frameworks-demystified-key-features-use-cases-and-lessons-learned-260a70744b96](https://medium.com/data-science-at-microsoft/ai-agent-frameworks-demystified-key-features-use-cases-and-lessons-learned-260a70744b96) 38 [https://www.loyensloeff.com/insights/news--events/news/dutch-implementation-of-the-ai-act-decentralised-ai-supervision/](https://www.loyensloeff.com/insights/news--events/news/dutch-implementation-of-the-ai-act-decentralised-ai-supervision/) 39 [https://www.nldigitalgovernment.nl/overview/artificial-intelligence-ai/ai-act/](https://www.nldigitalgovernment.nl/overview/artificial-intelligence-ai/ai-act/) 40 [https://business.gov.nl/regulations/ai-act/](https://business.gov.nl/regulations/ai-act/) 41 [https://www.government.nl/documents/publications/2025/09/04/ai-act-guide](https://www.government.nl/documents/publications/2025/09/04/ai-act-guide) 50 [https://talent500.com/blog/semantic-versioning-explained-guide/](https://talent500.com/blog/semantic-versioning-explained-guide/) 51 [https://workos.com/blog/software-versioning-guide](https://workos.com/blog/software-versioning-guide) 61 [https://blog.premai.io/llm-cost-optimization-8-strategies-that-cut-api-spend-by-80-2026-guide/](https://blog.premai.io/llm-cost-optimization-8-strategies-that-cut-api-spend-by-80-2026-guide/) 63 [https://www.pluralsight.com/resources/blog/ai-and-data/how-cut-llm-costs-with-metering](https://www.pluralsight.com/resources/blog/ai-and-data/how-cut-llm-costs-with-metering) 62 [https://www.reddit.com/r/LangChain/comments/1rtqraf/how_are_you_handling_llm_costs_in_production/](https://www.reddit.com/r/LangChain/comments/1rtqraf/how_are_you_handling_llm_costs_in_production/) 48 [https://towardsdatascience.com/agentic-ai-how-to-save-on-tokens/](https://towardsdatascience.com/agentic-ai-how-to-save-on-tokens/) 49 [https://amnic.com/blogs/anthropic-api-pricing](https://amnic.com/blogs/anthropic-api-pricing) 80 [https://www.anthropic.com/research/building-effective-agents](https://www.anthropic.com/research/building-effective-agents) 47 [https://workos.com/blog/anthropics-computer-use-versus-openais-computer-using-agent-cua](https://workos.com/blog/anthropics-computer-use-versus-openais-computer-using-agent-cua) 72 [https://github.com/salttechno/LLM-Model-Comparison-2026](https://github.com/salttechno/LLM-Model-Comparison-2026) 55 [https://www.glukhov.org/llm-performance/benchmarks/structured-output-comparison-popular-llm-providers/](https://www.glukhov.org/llm-performance/benchmarks/structured-output-comparison-popular-llm-providers/) 71 [https://strapi.io/blog/ai-apis-developers-comparison](https://strapi.io/blog/ai-apis-developers-comparison) 56 [https://www.syncfusion.com/blogs/post/top-llm-api-comparison-2026](https://www.syncfusion.com/blogs/post/top-llm-api-comparison-2026) 64 [https://iternal.ai/llm-selection-guide](https://iternal.ai/llm-selection-guide) 68 [https://www.mindstudio.ai/blog/gpt-5-5-review-developers-builders](https://www.mindstudio.ai/blog/gpt-5-5-review-developers-builders) 69 [https://www.buildfastwithai.com/blogs/gpt-5-5-review-2026](https://www.buildfastwithai.com/blogs/gpt-5-5-review-2026) 74 [https://aimultiple.com/agentic-frameworks](https://aimultiple.com/agentic-frameworks) 15 [https://arxiv.org/abs/2603.22651](https://arxiv.org/abs/2603.22651) 9 [https://www.anthropic.com/engineering/code-execution-with-mcp](https://www.anthropic.com/engineering/code-execution-with-mcp) 6 [https://blog.modelcontextprotocol.io/posts/2026-mcp-roadmap/](https://blog.modelcontextprotocol.io/posts/2026-mcp-roadmap/) 33 [https://openreview.net/forum?id=UVgbFuXPaO](https://openreview.net/forum?id=UVgbFuXPaO) 19 [https://fast.io/resources/ai-agent-error-handling/](https://fast.io/resources/ai-agent-error-handling/) 11 [https://arxiv.org/pdf/2509.08646](https://arxiv.org/pdf/2509.08646) 54 [https://renezander.com/guides/llm-api-comparison/](https://renezander.com/guides/llm-api-comparison/)

#### Geciteerd werk

1. Three tiers of Agentic AI - and when to use none of them | Microsoft ..., geopend op april 29, 2026, [https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/three-tiers-of-agentic-ai---and-when-to-use-none-of-them/4510377](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/three-tiers-of-agentic-ai---and-when-to-use-none-of-them/4510377)
    
2. Model Context Protocol - Wikipedia, geopend op april 29, 2026, [https://en.wikipedia.org/wiki/Model_Context_Protocol](https://en.wikipedia.org/wiki/Model_Context_Protocol)
    
3. MCP vs LangChain vs CrewAI: Agent Framework Comparison 2026 - Digital Applied, geopend op april 29, 2026, [https://www.digitalapplied.com/blog/mcp-vs-langchain-vs-crewai-agent-framework-comparison](https://www.digitalapplied.com/blog/mcp-vs-langchain-vs-crewai-agent-framework-comparison)
    
4. Top 10 AI Trends 2025: How Agentic AI and MCP Changed IT | Splunk, geopend op april 29, 2026, [https://www.splunk.com/en_us/blog/artificial-intelligence/top-10-ai-trends-2025-how-agentic-ai-and-mcp-changed-it.html](https://www.splunk.com/en_us/blog/artificial-intelligence/top-10-ai-trends-2025-how-agentic-ai-and-mcp-changed-it.html)
    
5. How to build a simple agentic AI server with MCP | Red Hat Developer, geopend op april 29, 2026, [https://developers.redhat.com/articles/2025/08/12/how-build-simple-agentic-ai-server-mcp](https://developers.redhat.com/articles/2025/08/12/how-build-simple-agentic-ai-server-mcp)
    
6. The 2026 MCP Roadmap | Model Context Protocol Blog, geopend op april 29, 2026, [https://blog.modelcontextprotocol.io/posts/2026-mcp-roadmap/](https://blog.modelcontextprotocol.io/posts/2026-mcp-roadmap/)
    
7. Roadmap - Model Context Protocol, geopend op april 29, 2026, [https://modelcontextprotocol.io/development/roadmap](https://modelcontextprotocol.io/development/roadmap)
    
8. How to build AI agents with MCP: 12 framework comparison (2025) - ClickHouse, geopend op april 29, 2026, [https://clickhouse.com/blog/how-to-build-ai-agents-mcp-12-frameworks](https://clickhouse.com/blog/how-to-build-ai-agents-mcp-12-frameworks)
    
9. Code execution with MCP: building more efficient AI agents \ Anthropic, geopend op april 29, 2026, [https://www.anthropic.com/engineering/code-execution-with-mcp](https://www.anthropic.com/engineering/code-execution-with-mcp)
    
10. TableMind: An Autonomous Programmatic Agent for Tool-Augmented Table Reasoning, geopend op april 29, 2026, [https://arxiv.org/html/2509.06278v1](https://arxiv.org/html/2509.06278v1)
    
11. Architecting Resilient LLM Agents: A Guide to Secure Plan ... - arXiv, geopend op april 29, 2026, [https://arxiv.org/pdf/2509.08646](https://arxiv.org/pdf/2509.08646)
    
12. A Practitioner's Guide to Prompt Engineering in 2025 - Maxim AI, geopend op april 29, 2026, [https://www.getmaxim.ai/articles/a-practitioners-guide-to-prompt-engineering-in-2025/](https://www.getmaxim.ai/articles/a-practitioners-guide-to-prompt-engineering-in-2025/)
    
13. The Hidden Economics of AI Agents: Managing Token Costs and Latency Trade-offs, geopend op april 29, 2026, [https://online.stevens.edu/blog/hidden-economics-ai-agents-token-costs-latency/](https://online.stevens.edu/blog/hidden-economics-ai-agents-token-costs-latency/)
    
14. AI Agent Orchestration Patterns - Azure Architecture Center - Microsoft Learn, geopend op april 29, 2026, [https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns)
    
15. [2603.22651] Benchmarking Multi-Agent LLM Architectures for Financial Document Processing: A Comparative Study of Orchestration Patterns, Cost-Accuracy Tradeoffs and Production Scaling Strategies - arXiv, geopend op april 29, 2026, [https://arxiv.org/abs/2603.22651](https://arxiv.org/abs/2603.22651)
    
16. Technical Tuesday: AgentOps and operationalizing AI agents for the enterprise - UiPath, geopend op april 29, 2026, [https://www.uipath.com/blog/ai/agent-ops-operationalizing-ai-agents-for-enterprise](https://www.uipath.com/blog/ai/agent-ops-operationalizing-ai-agents-for-enterprise)
    
17. 10 Best Practices for Reliable AI Agent Systems - Vatsal Shah, geopend op april 29, 2026, [https://vatsalshah.in/blog/10-best-practices-reliable-ai-agents](https://vatsalshah.in/blog/10-best-practices-reliable-ai-agents)
    
18. How to Evaluate AI Agents: Latency, Cost, Safety, ROI | Aviso Blog, geopend op april 29, 2026, [https://www.aviso.com/blog/how-to-evaluate-ai-agents-latency-cost-safety-roi](https://www.aviso.com/blog/how-to-evaluate-ai-agents-latency-cost-safety-roi)
    
19. AI Agent Error Handling: Best Practices & Patterns for 2025 | Fastio, geopend op april 29, 2026, [https://fast.io/resources/ai-agent-error-handling/](https://fast.io/resources/ai-agent-error-handling/)
    
20. 7 Retry + Timeout Rules for LangChain Tools | by Praxen - Medium, geopend op april 29, 2026, [https://medium.com/@Praxen/7-retry-timeout-rules-for-langchain-tools-760d1a4dd69d](https://medium.com/@Praxen/7-retry-timeout-rules-for-langchain-tools-760d1a4dd69d)
    
21. Mastering Retry Logic Agents: A Deep Dive into 2025 Best Practices - Sparkco, geopend op april 29, 2026, [https://sparkco.ai/blog/mastering-retry-logic-agents-a-deep-dive-into-2025-best-practices](https://sparkco.ai/blog/mastering-retry-logic-agents-a-deep-dive-into-2025-best-practices)
    
22. 7 Patterns That Stop Your AI Agent From Going Rogue in Production - DEV Community, geopend op april 29, 2026, [https://dev.to/pockit_tools/7-patterns-that-stop-your-ai-agent-from-going-rogue-in-production-5hb1](https://dev.to/pockit_tools/7-patterns-that-stop-your-ai-agent-from-going-rogue-in-production-5hb1)
    
23. Best practices for building effective AI agents and multi-agent systems - Medium, geopend op april 29, 2026, [https://medium.com/online-inference/best-practices-for-building-effective-ai-agents-and-multi-agent-systems-2c7fe11c9605](https://medium.com/online-inference/best-practices-for-building-effective-ai-agents-and-multi-agent-systems-2c7fe11c9605)
    
24. How LangSmith and LangChain OSS Help You Meet EU AI Act Requirements, geopend op april 29, 2026, [https://www.langchain.com/blog/langsmith-langchain-oss-eu-ai-act](https://www.langchain.com/blog/langsmith-langchain-oss-eu-ai-act)
    
25. LangChain AI Agents: Complete Implementation Guide 2025 - Digital Applied, geopend op april 29, 2026, [https://www.digitalapplied.com/blog/langchain-ai-agents-guide-2025](https://www.digitalapplied.com/blog/langchain-ai-agents-guide-2025)
    
26. OWASP Top 10 for LLMs 2025 | DeepTeam by Confident AI - The LLM Red Teaming Framework, geopend op april 29, 2026, [https://trydeepteam.com/docs/frameworks-owasp-top-10-for-llms](https://trydeepteam.com/docs/frameworks-owasp-top-10-for-llms)
    
27. LLMRisks Archive - OWASP Gen AI Security Project, geopend op april 29, 2026, [https://genai.owasp.org/llm-top-10/](https://genai.owasp.org/llm-top-10/)
    
28. LLM01:2025 Prompt Injection - OWASP Gen AI Security Project, geopend op april 29, 2026, [https://genai.owasp.org/llmrisk/llm01-prompt-injection/](https://genai.owasp.org/llmrisk/llm01-prompt-injection/)
    
29. Prompt Injection Detection: Securing AI Systems Against Malicious Actors - Salesforce, geopend op april 29, 2026, [https://www.salesforce.com/blog/prompt-injection-detection/](https://www.salesforce.com/blog/prompt-injection-detection/)
    
30. Securing LLM Superpowers: The Invisible Backdoors in MCP - Netskope, geopend op april 29, 2026, [https://www.netskope.com/blog/securing-llm-superpowers-the-invisible-backdoors-in-mcp](https://www.netskope.com/blog/securing-llm-superpowers-the-invisible-backdoors-in-mcp)
    
31. OWASP Top 10 for Large Language Model Applications, geopend op april 29, 2026, [https://owasp.org/www-project-top-10-for-large-language-model-applications/](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
    
32. EchoLeak: The First Real-World Zero-Click Prompt Injection Exploit in a Production LLM System - arXiv, geopend op april 29, 2026, [https://arxiv.org/html/2509.10540v1](https://arxiv.org/html/2509.10540v1)
    
33. Log-To-Leak: Prompt Injection Attacks on Tool-Using LLM Agents via Model Context Protocol | OpenReview, geopend op april 29, 2026, [https://openreview.net/forum?id=UVgbFuXPaO](https://openreview.net/forum?id=UVgbFuXPaO)
    
34. LogJack: Indirect Prompt Injection Through Cloud Logs Against LLM Debugging Agents, geopend op april 29, 2026, [https://www.researchgate.net/publication/403975846_LogJack_Indirect_Prompt_Injection_Through_Cloud_Logs_Against_LLM_Debugging_Agents](https://www.researchgate.net/publication/403975846_LogJack_Indirect_Prompt_Injection_Through_Cloud_Logs_Against_LLM_Debugging_Agents)
    
35. PROMPT INJECTION ATTACKS ON TOOL-USING LLM AGENTS VIA MODEL CONTEXT PROTOCOL - OpenReview, geopend op april 29, 2026, [https://openreview.net/pdf?id=UVgbFuXPaO](https://openreview.net/pdf?id=UVgbFuXPaO)
    
36. What Is a Prompt Injection Attack? [Examples & Prevention] - Palo Alto Networks, geopend op april 29, 2026, [https://www.paloaltonetworks.com/cyberpedia/what-is-a-prompt-injection-attack](https://www.paloaltonetworks.com/cyberpedia/what-is-a-prompt-injection-attack)
    
37. LogJack: Indirect Prompt Injection Through Cloud Logs Against LLM Debugging Agents, geopend op april 29, 2026, [https://arxiv.org/html/2604.15368v1](https://arxiv.org/html/2604.15368v1)
    
38. Dutch implementation of the AI Act: decentralised AI supervision | Loyens & Loeff, geopend op april 29, 2026, [https://www.loyensloeff.com/insights/news--events/news/dutch-implementation-of-the-ai-act-decentralised-ai-supervision/](https://www.loyensloeff.com/insights/news--events/news/dutch-implementation-of-the-ai-act-decentralised-ai-supervision/)
    
39. AI Act - Digital Government, geopend op april 29, 2026, [https://www.nldigitalgovernment.nl/overview/artificial-intelligence-ai/ai-act/](https://www.nldigitalgovernment.nl/overview/artificial-intelligence-ai/ai-act/)
    
40. Rules for working with safe AI | Business.gov.nl, geopend op april 29, 2026, [https://business.gov.nl/regulations/ai-act/](https://business.gov.nl/regulations/ai-act/)
    
41. AI Act Guide | Publication - Government.nl, geopend op april 29, 2026, [https://www.government.nl/documents/publications/2025/09/04/ai-act-guide](https://www.government.nl/documents/publications/2025/09/04/ai-act-guide)
    
42. Article 12: Record-Keeping | EU Artificial Intelligence Act, geopend op april 29, 2026, [https://artificialintelligenceact.eu/article/12/](https://artificialintelligenceact.eu/article/12/)
    
43. Article 14: Human Oversight | EU Artificial Intelligence Act, geopend op april 29, 2026, [https://artificialintelligenceact.eu/article/14/](https://artificialintelligenceact.eu/article/14/)
    
44. Full article: 'Human oversight' in the EU artificial intelligence act: what, when and by whom?, geopend op april 29, 2026, [https://www.tandfonline.com/doi/full/10.1080/17579961.2023.2245683](https://www.tandfonline.com/doi/full/10.1080/17579961.2023.2245683)
    
45. Daily Papers - Hugging Face, geopend op april 29, 2026, [https://huggingface.co/papers?q=RAG](https://huggingface.co/papers?q=RAG)
    
46. General Work AI Agents Comparison, geopend op april 29, 2026, [https://artificialanalysis.ai/agents](https://artificialanalysis.ai/agents)
    
47. Anthropic's Computer Use versus OpenAI's Computer Using Agent (CUA) - WorkOS, geopend op april 29, 2026, [https://workos.com/blog/anthropics-computer-use-versus-openais-computer-using-agent-cua](https://workos.com/blog/anthropics-computer-use-versus-openais-computer-using-agent-cua)
    
48. Agentic AI: How to Save on Tokens | Towards Data Science, geopend op april 29, 2026, [https://towardsdatascience.com/agentic-ai-how-to-save-on-tokens/](https://towardsdatascience.com/agentic-ai-how-to-save-on-tokens/)
    
49. Anthropic API Pricing Explained: How to Estimate and Control LLM Costs - Amnic, geopend op april 29, 2026, [https://amnic.com/blogs/anthropic-api-pricing](https://amnic.com/blogs/anthropic-api-pricing)
    
50. Semantic Versioning Explained: Rules, Benefits & Best Practices - Talent500, geopend op april 29, 2026, [https://talent500.com/blog/semantic-versioning-explained-guide/](https://talent500.com/blog/semantic-versioning-explained-guide/)
    
51. From 1.0.0 to 2025.4: Making sense of software versioning - WorkOS, geopend op april 29, 2026, [https://workos.com/blog/software-versioning-guide](https://workos.com/blog/software-versioning-guide)
    
52. Writing effective tools for AI agents—using AI agents - Anthropic, geopend op april 29, 2026, [https://www.anthropic.com/engineering/writing-tools-for-agents](https://www.anthropic.com/engineering/writing-tools-for-agents)
    
53. Mastering Kubernetes Namespaces: Advanced Isolation, Resource Management, and Multi-Tenancy Strategies - Rafay, geopend op april 29, 2026, [https://rafay.co/ai-and-cloud-native-blog/mastering-kubernetes-namespaces-advanced-isolation-resource-management-and-multi-tenancy-strategies](https://rafay.co/ai-and-cloud-native-blog/mastering-kubernetes-namespaces-advanced-isolation-resource-management-and-multi-tenancy-strategies)
    
54. LLM API Comparison 2026: Best API for Production - René Zander, geopend op april 29, 2026, [https://renezander.com/guides/llm-api-comparison/](https://renezander.com/guides/llm-api-comparison/)
    
55. Structured output comparison across popular LLM providers - OpenAI, Gemini, Anthropic, Mistral and AWS Bedrock - Rost Glukhov, geopend op april 29, 2026, [https://www.glukhov.org/llm-performance/benchmarks/structured-output-comparison-popular-llm-providers/](https://www.glukhov.org/llm-performance/benchmarks/structured-output-comparison-popular-llm-providers/)
    
56. Best LLM APIs in 2026: Comparing OpenAI, Claude, Gemini, Azure, Bedrock, Mistral & DeepSeek | Syncfusion Blogs, geopend op april 29, 2026, [https://www.syncfusion.com/blogs/post/top-llm-api-comparison-2026](https://www.syncfusion.com/blogs/post/top-llm-api-comparison-2026)
    
57. The guide to structured outputs and function calling with LLMs - Agenta, geopend op april 29, 2026, [https://agenta.ai/blog/the-guide-to-structured-outputs-and-function-calling-with-llms](https://agenta.ai/blog/the-guide-to-structured-outputs-and-function-calling-with-llms)
    
58. Schema First Tool APIs for LLM Agents: A Controlled Study of Tool Misuse, Recovery, and Budgeted Performance - arXiv, geopend op april 29, 2026, [https://arxiv.org/html/2603.13404v1](https://arxiv.org/html/2603.13404v1)
    
59. Which Cheap and OSS LLMs Actually Produce Valid JSON (in 12/2025)? | by Lyx | Medium, geopend op april 29, 2026, [https://medium.com/@lyx_62906/which-cheap-and-oss-llms-actually-produce-valid-json-9b002e106b6d](https://medium.com/@lyx_62906/which-cheap-and-oss-llms-actually-produce-valid-json-9b002e106b6d)
    
60. Core Latency in AI Voice Agents | Twilio, geopend op april 29, 2026, [https://www.twilio.com/en-us/blog/developers/best-practices/guide-core-latency-ai-voice-agents](https://www.twilio.com/en-us/blog/developers/best-practices/guide-core-latency-ai-voice-agents)
    
61. LLM Cost Optimization: 8 Strategies That Cut API Spend by 80% (2026 Guide) - Prem AI, geopend op april 29, 2026, [https://blog.premai.io/llm-cost-optimization-8-strategies-that-cut-api-spend-by-80-2026-guide/](https://blog.premai.io/llm-cost-optimization-8-strategies-that-cut-api-spend-by-80-2026-guide/)
    
62. How are you handling LLM costs in production? What's actually working? - Reddit, geopend op april 29, 2026, [https://www.reddit.com/r/LangChain/comments/1rtqraf/how_are_you_handling_llm_costs_in_production/](https://www.reddit.com/r/LangChain/comments/1rtqraf/how_are_you_handling_llm_costs_in_production/)
    
63. Meter before you manage: How to cut LLM costs by up to 85% | Pluralsight, geopend op april 29, 2026, [https://www.pluralsight.com/resources/blog/ai-and-data/how-cut-llm-costs-with-metering](https://www.pluralsight.com/resources/blog/ai-and-data/how-cut-llm-costs-with-metering)
    
64. The Definitive LLM Selection & Benchmarks Guide - Iternal Technologies, geopend op april 29, 2026, [https://iternal.ai/llm-selection-guide](https://iternal.ai/llm-selection-guide)
    
65. Anthropic vs OpenAI vs Google: Three Different Bets on the Future of AI Agents | MindStudio, geopend op april 29, 2026, [https://www.mindstudio.ai/blog/anthropic-vs-openai-vs-google-agent-strategy](https://www.mindstudio.ai/blog/anthropic-vs-openai-vs-google-agent-strategy)
    
66. miptgirl_medium/dspy_rlm/dspy_rlm.ipynb at main · miptgirl/miptgirl_medium - GitHub, geopend op april 29, 2026, [https://github.com/miptgirl/miptgirl_medium/blob/main/dspy_rlm/dspy_rlm.ipynb](https://github.com/miptgirl/miptgirl_medium/blob/main/dspy_rlm/dspy_rlm.ipynb)
    
67. AI agent frameworks demystified: Key features, use cases, and lessons learned - Medium, geopend op april 29, 2026, [https://medium.com/data-science-at-microsoft/ai-agent-frameworks-demystified-key-features-use-cases-and-lessons-learned-260a70744b96](https://medium.com/data-science-at-microsoft/ai-agent-frameworks-demystified-key-features-use-cases-and-lessons-learned-260a70744b96)
    
68. GPT-5.5 vs Claude Opus 4.7 vs Gemini 3.1 Pro for Builders - MindStudio, geopend op april 29, 2026, [https://www.mindstudio.ai/blog/gpt-5-5-review-developers-builders](https://www.mindstudio.ai/blog/gpt-5-5-review-developers-builders)
    
69. GPT-5.5 Review: Benchmarks, Pricing & Vs Claude (2026) - Build Fast with AI, geopend op april 29, 2026, [https://www.buildfastwithai.com/blogs/gpt-5-5-review-2026](https://www.buildfastwithai.com/blogs/gpt-5-5-review-2026)
    
70. ChatGPT vs Google Gemini vs Anthropic Claude: Comprehensive Comparison & Report. Capabilities, performance, accuracy, speed, multimodal abilities, coding skills, integrations, user experience and more - Data Studios, geopend op april 29, 2026, [https://www.datastudios.org/post/chatgpt-vs-google-gemini-vs-anthropic-claude-comprehensive-comparison-report-capabilities-perfo](https://www.datastudios.org/post/chatgpt-vs-google-gemini-vs-anthropic-claude-comprehensive-comparison-report-capabilities-perfo)
    
71. Technical Comparison: Top 7 AI APIs for Full-Stack Developers, geopend op april 29, 2026, [https://strapi.io/blog/ai-apis-developers-comparison](https://strapi.io/blog/ai-apis-developers-comparison)
    
72. GitHub - salttechno/LLM-Model-Comparison-2026: Compare 16 LLMs for enterprise use in 2026: GPT-4.1, Claude 4.5, Gemini 2.5, Llama 4, DeepSeek, Mistral. Pricing, benchmarks, context windows, API features. CC BY 4.0., geopend op april 29, 2026, [https://github.com/salttechno/LLM-Model-Comparison-2026](https://github.com/salttechno/LLM-Model-Comparison-2026)
    
73. A Detailed Comparison of Top 6 AI Agent Frameworks in 2026 - Turing, geopend op april 29, 2026, [https://www.turing.com/resources/ai-agent-frameworks](https://www.turing.com/resources/ai-agent-frameworks)
    
74. Top 5 Open-Source Agentic AI Frameworks in 2026 - AIMultiple, geopend op april 29, 2026, [https://aimultiple.com/agentic-frameworks](https://aimultiple.com/agentic-frameworks)
    
75. LangChain vs LlamaIndex vs AutoGen vs CrewAI: Which Framework Actually Ships in 2026? - Blogs - Trixly AI Solutions, geopend op april 29, 2026, [https://www.trixlyai.com/blogs/langchain-vs-llamaindex-vs-autogen-vs-crewai-which-framework-actually-ships-in-2026](https://www.trixlyai.com/blogs/langchain-vs-llamaindex-vs-autogen-vs-crewai-which-framework-actually-ships-in-2026)
    
76. The Hidden Costs of Agentic AI: Why 40% of Projects Fail Before Production - Galileo AI, geopend op april 29, 2026, [https://galileo.ai/blog/hidden-cost-of-agentic-ai](https://galileo.ai/blog/hidden-cost-of-agentic-ai)
    
77. MCP Horror Stories: The GitHub Prompt Injection Data Heist - Docker, geopend op april 29, 2026, [https://www.docker.com/blog/mcp-horror-stories-github-prompt-injection/](https://www.docker.com/blog/mcp-horror-stories-github-prompt-injection/)
    
78. Protecting against indirect prompt injection attacks in MCP - Microsoft for Developers, geopend op april 29, 2026, [https://developer.microsoft.com/blog/protecting-against-indirect-injection-attacks-mcp](https://developer.microsoft.com/blog/protecting-against-indirect-injection-attacks-mcp)
    
79. A Cascaded Hybrid Defense Architecture for Prompt Injection Detection in MCP-Based Systems - arXiv, geopend op april 29, 2026, [https://arxiv.org/html/2604.17125v1](https://arxiv.org/html/2604.17125v1)
    
80. Building Effective AI Agents - Anthropic, geopend op april 29, 2026, [https://www.anthropic.com/research/building-effective-agents](https://www.anthropic.com/research/building-effective-agents)
    

**