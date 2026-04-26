# Research: FDE, Iteratieve Blueprint, Prototype-driven & Playbook — BB_02 Client Blueprint

**Researcher:** researcher-fde
**Dimensie:** Forward Deployed Engineering, levend blueprint, prototype-tools, playbook-structuur (2024-2026)
**Datum:** 2026-04-26

## Samenvatting (1 zin)

Forward Deployed Engineering biedt een bewezen model voor snelle, embedded AI-implementatie bij klanten, maar kent significante beperkingen (schaalbaarheid, rolvervaging); prototype-tools als Lovable, v0, Bolt en Stitch zijn waardevol als gespreksanker maar riskant als validatie-surrogaat.

## Bevindingen

### 1. Forward Deployed Engineering: oorsprong en kernprincipes

**Oorsprong:** Palantir Technologies ontwikkelde het FDE-model (intern "Delta" genaamd) in de vroege jaren 2010. Tot circa 2016 had Palantir *meer* FDEs dan reguliere software-engineers. [1, 2]

Palantir's eigen definitie: "Dev: één capability, veel klanten; Delta: veel capabilities, één klant." [1] (`verified` via Pragmatic Engineer-artikel)

**Kernprincipes:**
- Een FDE is embedded bij de klant (tot 50% van de tijd ter plekke) en werkt ook aan het kernproduct
- Drie fasen: scoping (klantprobleem begrijpen) → validatie (oplossingen toetsen aan evaluatiecriteria) → implementatie (productie-oplossingen opleveren) [1]
- FDEs "werken met enorme onzekerheid, en wat klanten beschrijven komt vaak niet overeen met de realiteit van hun data" [1]
- Anders dan consultants: FDEs bouwen en deployen zelf, ze adviseren niet alleen

**AI FDE (2024-2026):** Palantir heeft het FDE-concept uitgebreid naar AI — de "AI FDE" is een interactieve agent die Foundry bedient via conversationele opdrachten. Tegelijkertijd is het de naam van een nieuwe FDE-rol bij Palantir specifiek voor GenAI-strategie en implementatie. [3] (`verified`)

### 2. FDE-model: wanneer werkt het

Effectief bij [1, 4]:
- Enterprise-klanten met complexe integratievragen
- AI/LLM-implementaties waar klantcontext cruciaal is
- Klanten die geblokkeerd worden door interne bureaucratie
- Situaties waar snelle prototyping en directe feedback-loops noodzakelijk zijn

Voorbeeld van succes: OpenAI en John Deere integreerden gepersonaliseerde interventies voor boeren binnen krappe tijdframes via FDE-model. [1] (`inferred` — via Pragmatic Engineer-samenvatting, niet directe primaire bron)

Marktbevestiging: FDE-vacatures stegen met >800% tussen januari en september 2025. Salesforce heeft zich gecommitteerd aan 1.000 FDEs. [4] (`verified` via SSO Network-artikel)

### 3. FDE-model: beperkingen en contra-perspectief

**Schaalbaarheidsgrens:** FDE-werk is per definitie klant-specifiek en niet schaalbaar als standaard productcapability. De verhouding FDE/klant maakt het model duurder dan product-led growth. [1] (`inferred`)

**Rolvervaging:** SVPG (Silicon Valley Product Group) signaleert verwarring tussen FDE, Solutions Architect, Sales Engineer en de nieuwe "Agent Engineer" — de grenzen vervagen. [1, 4] Salesforce's functieprofiel beschrijft "praktisch twee beroepen in één". (`inferred` — SVPG-pagina gaf 403-fout, maar Pragmatic Engineer citeert SVPG expliciet)

**Zelfbeheersing vereist:** succesvolle FDEs moeten actief "nee" zeggen en meeting-overload vermijden — het model creëert druk om alles voor elke klant op te lossen. [1] (`inferred`)

**Contra-perspectief van SVPG:** Marty Cagan (SVPG) is kritisch op het FDE-model omdat het het risico meebrengt dat klantspecifieke customisaties de productstrategie gaan dicteren in plaats van een coherente productvisie. (`inferred` — SVPG-positie bekend maar directe URL niet geverifieerd na 403-fout)

**Blueprint-implicatie voor BB_02:** FDE-principes (embedded, iteratief, bouw-ipv-adviseer) zijn waardevol als *werkwijze* voor de blueprint-fase, maar het volledig FDE-model is niet de default aanpak voor elke AI-opdracht. BB_02 moet onderscheid maken: wanneer is een FDE-aanpak nodig, wanneer is een klassiekere discovery-fase afdoende?

### 4. AI-prototyping-tools als blueprint-vehikel: sterktes en faalmodi

Vier tools domineren het 2026-landschap als prototype-instrument voor klantgesprekken [5, 6, 7]:

**Google Stitch (gelanceerd Google I/O 2025)**
- Hoge-fidelity UI vanuit prompts, "Vibe Design mode" voor meerdere richtingen tegelijk [5]
- Voice canvas voor live ideation in meetings — klanten zien concepten ontstaan
- Beperking: geen backend; alleen UI-designs — misleidend voor complexe processen
- Beperking: nog Google Labs-status (maart 2026) — onzekerheid voor enterprise-klanten

(`verified` via NxCode vergelijkingsartikel)

**v0 by Vercel**
- Genereert productie-kwaliteit React/Tailwind componenten (shadcn/ui) [5]
- Sterk voor developer-teams; code direct inzetbaar in codebase
- Beperking: alleen React/Next.js — klanten met andere stacks voelen zich buitengesloten
- Beperking: componenten, geen applicaties — verleidt tot verkeerd scope-begrip

**Lovable**
- Full-stack: van idee naar deployed app zonder code schrijven [5, 6]
- Genereert TypeScript/React + Supabase backend + authenticatie + custom domain
- Beperking: vendor lock-in, latere migratie kostbaar
- Beperking: klanten geloven soms een productie-ready app te hebben; vaak nog refinement nodig

**Bolt.new**
- Draait volledig in browser (WebContainers) — nul lokale setup [5]
- $40M ARR bewijst dat browser-gebaseerd AI-development levensvatbaar is
- Beperking: token-gebaseerde kosten moeilijk te voorspellen
- Beperking: eerste output is vaak een ruwe versie; verwachtingsmanagement noodzakelijk

**Claude Artifacts / Claude Design**
- Artifacts: snel interactieve component of proof-of-concept, te delen binnen 10 minuten [5]
- Claude Design (claude.ai/design): research preview april 2026
- Sterk voor één-component demos en verkennende gesprekken

(`verified` via NxCode Vibe Design Tools vergelijking 2026)

### 5. Prototype-driven blueprinting: wanneer productief, wanneer contraproductief

**Productief wanneer [7, 8]:**
- Als gespreks*anker* in plaats van tekst-blueprint — klant ziet en reageert op iets concreets
- Voor feature-verkenning vóór ontwikkeling: "je kunt directe feedback krijgen van klanten zonder tijd te verspillen aan een volledige versie"
- Voor alignment tussen niet-technische stakeholders over functionele scope
- Als aanname-invalidatie-instrument: het prototype laat zien wat *niet* werkt, niet alleen wat kan

**Contraproductief wanneer [7, 8]:**
- Als surrogaat voor diepgaand gebruikersonderzoek — polished UI creëert schijn-zekerheid
- Als productiecode-equivalent — klanten overschatten gereedheid: "scope lock-in op vroege UI"
- Wanneer de businesslogica complex is — prototype mist backend-realiteit volledig
- Als validatie zonder criteria: "als je geen evaluatiecriteria hebt, valideert een prototype niets"

**Kritische waarschuwing:** alle vier de tools genereren oppervlakkig gepolijste UIs die strategische vragen (gebruikersonderzoek, businesslogica-validatie, A/B-test setup) niet beantwoorden. [6]

Lenny's Newsletter advies: "AI is geen vervanging voor kritisch denken; menselijk oordeel is nog steeds noodzakelijk om gegenereerde inzichten te interpreteren en geïnformeerde productbeslissingen te nemen." [8] (`verified` via directe fetch Lenny's Newsletter)

**Blueprint-regel voor BB_02:** prototype = discovery-instrument, niet validatie-eindpunt. Een prototype mag nooit de discussie over doel, sucescriteria, data en risico's vervangen — het versnelt die discussie.

### 6. Playbook-structuur voor het blueprint-gesprek

**Enterprise AI Playbook (Stanford Digital Economy Lab, 2026, 51 cases):** [9]
- 73% van succesvolle implementaties startte bewust klein
- 63% fraamde hun pilot expliciet als experiment (niet als product)
- Kooptip: specialistische vendor-partnerships slagen ~67% van de tijd; interne builds slagen slechts ~33%

(`inferred` — PDF was niet tekstueel leesbaar via fetch, bevindingen via zoekresultaat-samenvatting)

**Anthropic's drie-signalen framework voor agent-geschiktheid** (uit WorkOS Enterprise Playbook-analyse) [10]:
1. Complexe besluitvorming die contextueel varieert?
2. Regelonderhoud dat developer-tijd vereist bij elke wijziging?
3. Ongestructureerde data (natural language, documenten)?

**AI-3P Framework als gespreksstructuur** [11]:
- People: eigenaarschap, capabilities, adoptie-gereedheid
- Process: governance, compliance, operationele integratie
- Product: technische haalbaarheid, gebruikerservaring, financiële viabiliteit
- Gewogen score (40/35/25) → Bouwen / Piloot met guardrails / Risico's eerst aanpakken

**Blueprint-elementen die een volledig gesprek dekt (synthese uit alle bronnen):**
1. Doel: welke beslissing of uitkomst wordt verbeterd?
2. Sucescriteria: hoe meten we succes? (kwantificeerbaar)
3. Processen: welke bestaande processen raken dit?
4. Output: wat produceert het systeem, voor wie?
5. Data: welke data is nodig, beschikbaar, representatief?
6. Tools/integraties: welke systemen moet het AI-systeem bereiken?
7. Risico's: EU AI Act tier, HLEG-check, OWASP-threats, DPIA-trigger?
8. Architectuur: workflow of agent? RAG of fine-tuning of agent?
9. Iteratieplan: hoe ziet de eerste versie eruit, hoe wordt gevalideerd?
10. Sign-off: wie moet akkoord geven, op welke criteria?

## Evidence Table

| # | Bron | URL | Type | Key claim | Confidence |
|---|------|-----|------|-----------|------------|
| 1 | Pragmatic Engineer — What are Forward Deployed Engineers | https://newsletter.pragmaticengineer.com/p/forward-deployed-engineers | primary | FDE origine, kernprincipes, drie fasen, rolvervaging | high |
| 2 | Palantir — AI FDE Overview | https://www.palantir.com/docs/foundry/ai-fde/overview | primary | AI FDE definitie, Foundry-integratie | medium |
| 3 | Palantir — Forward Deployed AI Engineer job | https://jobs.lever.co/palantir/636fc05c-d348-4a06-be51-597cb9e07488 | primary | AI FDE rol definitie 2024-2025 | medium |
| 4 | SSO Network — Forward Deployed Engineers Guide | https://www.ssonetwork.com/intelligent-automation/columns/forward-deployed-engineers-guide | secondary | 800% vacature-stijging, Salesforce 1000 FDEs | high |
| 5 | NxCode — Vibe Design Tools Compared 2026 | https://www.nxcode.io/resources/news/vibe-design-tools-compared-stitch-v0-lovable-2026 | secondary | Tool-vergelijking Stitch/v0/Lovable/Bolt, sterktes/beperkingen | high |
| 6 | NxCode — Google Stitch vs v0 vs Lovable 2026 | https://www.nxcode.io/resources/news/google-stitch-vs-v0-vs-lovable-ai-app-builder-2026 | secondary | Strategisch inzetbaarheidsoverzicht per tool | medium |
| 7 | Lenny's Newsletter — A Guide to AI Prototyping for Product Managers | https://www.lennysnewsletter.com/p/a-guide-to-ai-prototyping-for-product | primary | Wanneer productief, tool-keuze, kritische kanttekening | high |
| 8 | Medium (Anna Arteeva) — Choosing your AI prototyping stack | https://annaarteeva.medium.com/choosing-your-ai-prototyping-stack-lovable-v0-bolt-replit-cursor-magic-patterns-compared-9a5194f163e9 | secondary | Toolstack-vergelijking, faalmodi | medium |
| 9 | Stanford Digital Economy Lab — Enterprise AI Playbook (51 cases) | https://digitaleconomy.stanford.edu/app/uploads/2026/03/EnterpriseAIPlaybook_PereiraGraylinBrynjolfsson.pdf | primary | 73% bewust klein gestart, 63% pilot-als-experiment, vendor vs. intern | medium (PDF niet tekstueel leesbaar, bevindingen via samenvatting) |
| 10 | WorkOS — Enterprise AI Agent Playbook | https://workos.com/blog/enterprise-ai-agent-playbook-what-anthropic-and-openai-reveal-about-building-production-ready-systems | secondary | Drie-signalen framework, vijf composable patronen | high |
| 11 | Towards Data Science — AI-3P Assessment Framework | https://towardsdatascience.com/the-ai-3p-assessment-framework/ | primary | People-Process-Product scoringsmodel als gespreksstructuur | high |

## Coverage Status

- **Gecheckt direct:** bronnen 1 (Pragmatic Engineer FDE, directe fetch), 5 (NxCode tool-vergelijking, directe fetch), 7 (Lenny's Newsletter, directe fetch), 10 (WorkOS, directe fetch), 11 (AI-3P, directe fetch)
- **Blijft onzeker:** SVPG-kritiek op FDE (403-fout bij directe fetch, maar citaten via Pragmatic Engineer betrouwbaar); Stanford PDF niet tekstueel leesbaar (bevindingen via zoekresultaat-samenvatting); Palantir AI FDE Overview niet direct gelezen
- **Niet afgerond:** concrete IDEO of Google design-thinking templates voor AI-discovery niet gevonden als specifieke gepubliceerde bron; Anthropic's eigen client-discovery-template bestaat niet als openbaar document

## Sources

1. Pragmatic Engineer — What are Forward Deployed Engineers, and why are they so in demand? — https://newsletter.pragmaticengineer.com/p/forward-deployed-engineers
2. Palantir — AI FDE Overview — https://www.palantir.com/docs/foundry/ai-fde/overview
3. Palantir — Forward Deployed AI Engineer (Lever job listing) — https://jobs.lever.co/palantir/636fc05c-d348-4a06-be51-597cb9e07488
4. SSO Network — Forward Deployed Engineers: Turning AI Promise into Progress — https://www.ssonetwork.com/intelligent-automation/columns/forward-deployed-engineers-guide
5. NxCode — Vibe Design Tools 2026: Stitch vs v0 vs Lovable vs Bolt Compared — https://www.nxcode.io/resources/news/vibe-design-tools-compared-stitch-v0-lovable-2026
6. NxCode — Google Stitch vs v0 vs Lovable 2026: Which AI App Builder Should You Use? — https://www.nxcode.io/resources/news/google-stitch-vs-v0-vs-lovable-ai-app-builder-2026
7. Lenny's Newsletter — A Guide to AI Prototyping for Product Managers — https://www.lennysnewsletter.com/p/a-guide-to-ai-prototyping-for-product
8. Medium (Anna Arteeva) — Choosing your AI Prototyping Stack — https://annaarteeva.medium.com/choosing-your-ai-prototyping-stack-lovable-v0-bolt-replit-cursor-magic-patterns-compared-9a5194f163e9
9. Stanford Digital Economy Lab — The Enterprise AI Playbook: Lessons from 51 Successful Deployments — https://digitaleconomy.stanford.edu/app/uploads/2026/03/EnterpriseAIPlaybook_PereiraGraylinBrynjolfsson.pdf
10. WorkOS — Enterprise AI Agent Playbook: What Anthropic and OpenAI Reveal — https://workos.com/blog/enterprise-ai-agent-playbook-what-anthropic-and-openai-reveal-about-building-production-ready-systems
11. Towards Data Science — Introducing the AI-3P Assessment Framework — https://towardsdatascience.com/the-ai-3p-assessment-framework/
12. Salesforce — Forward Deployed Engineer: 5 Skills for This New Role — https://www.salesforce.com/blog/forward-deployed-engineer/
