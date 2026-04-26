# BB_02 Client Blueprint: Actuele Patronen voor AI-oplossingen (2024-2026)

**Onderwerp:** Patronen voor het ontwerpen van AI-oplossingen — van probleemkeuze tot architectuur, risico-inschatting, iteratieve validatie en prototype-driven blueprinting
**Datum:** 2026-04-26
**Researcher-rondes:** 1
**Verificatie-pass:** PASS-WITH-NOTES (zie Open Vragen)

---

## Executive Summary

De meerderheid van enterprise AI-pilots levert geen meetbaar resultaat — niet omdat de modellen slecht zijn, maar omdat het verkeerde probleem wordt aangepakt of het juiste probleem op de verkeerde manier wordt benaderd. Het MIT NANDA-rapport (*The GenAI Divide: State of AI in Business 2025*, aug. 2025) rapporteert een 95% faalpercentage [5]; de methodologische onderbouwing van dat exacte getal is onvoldoende [6], maar de oorzaak die het benoemt is consistent met andere onafhankelijke analyses: een mismatch tussen AI-aanpak en bedrijfsprobleem. (`inferred` voor het exacte getal; `verified` voor de oorzaak-diagnose)

Drie patronen onderscheiden de initiatieven die slagen:

**1. Decision-first** — begin bij de beslissing die verbeterd moet worden, niet bij de technologie. Dit vereist een expliciete geschiktheidscheck vóór committering aan een architectuur.

**2. Risico en compliance als ontwerpinput** — EU AI Act-tier, HLEG-vereisten, DPIA en OWASP LLM-bedreigingen worden vastgesteld vóórdat architectuurkeuzes worden gemaakt, niet na de bouw.

**3. Iteratieve validatie met prototype als gespreksanker** — Forward Deployed Engineering-principes (embedded, iteratief, bouwen in plaats van adviseren) gecombineerd met prototype-tools als Lovable, v0, Bolt en Google Stitch als middel om stakeholder-alignment te versnellen, maar nooit als surrogaat voor het gesprek over doel, data en risico's.

BB_02 moet deze drie patronen operationeel maken via een gestructureerde gespreksleidraad met 10 concrete blueprint-elementen en een vroege geschiktheidscheck.

---

## 1. Use Case-selectie: welk probleem is een AI-probleem?

### 1.1 Decision-first als vertrekpunt

Cassie Kozyrkov (voormalig Chief Decision Scientist Google, nu CEO Kozyr) heeft het concept *decision intelligence* gepopulariseerd als het juiste vertrekpunt voor AI-initiatieven [1, 2]. De kernvraag is niet "welke AI kunnen we inzetten?" maar "welke beslissingen zijn het waard om beter te nemen?" (`verified` via meerdere onafhankelijke artikelen over Kozyrkov's werk)

Kozyrkov formuleert drie evaluatiecriteria voor AI-systemen [2]:
1. Identificeer het doel van het AI-systeem
2. Beoordeel de beschikbaarheid en kwaliteit van data
3. Valideer of het AI-systeem werkt zoals beoogd

"The purpose is important, and the purpose comes from people." [2] (`verified`)

**Blueprint-implicatie:** het eerste gesprek met de klant begint bij de beslissing of uitkomst die verbeterd moet worden — inclusief wie die beslissing neemt, hoe vaak, en wat de kosten zijn van een slechte beslissing.

### 1.2 AI-first vs. AI-augmented: twee legitieme vertrekpunten

"AI-first" betekent in Kozyrkov's definitie niet "AI voor alles" maar "bereid zijn het voorheen onmogelijke te heroverwegen" [1, 2] — niet inzetten om "bij te blijven." (`verified`)

Twee legitieme vertrekpunten voor een BB_02-gesprek:
- **AI-augmented:** bestaande processen versnellen of verbeteren met AI-assistentie (meeste enterprise use cases)
- **AI-first:** processen fundamenteel herdenken vanuit wat nu mogelijk is

Andrej Karpathy introduceerde het kader hiervoor als "Software 3.0" op 19 juni 2025 op Y Combinator's AI Startup School [3, 4]: de progressie van expliciete code (1.0) via geleerde gewichten (2.0) naar prompts als broncode (3.0), met de LLM als operating system. (`verified` via meerdere onafhankelijke analyses van de keynote)

Risico: niet alles wat *beschrijfbaar* is in taal is ook *betrouwbaar uitvoerbaar* door een LLM. BB_02 moet dit onderscheid operationeel maken.

### 1.3 Het MIT-onderzoek: wat het zegt en wat niet

Het MIT NANDA-initiatief publiceerde in augustus 2025 *The GenAI Divide: State of AI in Business 2025* met de bevinding dat ~95% van enterprise AI-pilots geen meetbaar P&L-resultaat levert [5]. Methodologie: 150 interviews met leidinggevenden, 350-persoons survey, analyse van 300 publieke implementaties.

**Kritiek:** Marketing AI Institute (Paul Roetzer) signaleert methodologische beperkingen [6] (`verified` via directe fetch):
- Succescriterium smal: deployment buiten pilotfase met ROI binnen 6 maanden
- Efficiëntiewinsten en kostenbesparingen niet meegeteld
- 52 interviews als statistische grondslag voor kwantitatieve claim
- Rapportagevertekening waarschijnlijk

**Conclusie voor BB_02:** de 95%-claim is als harde statistiek `inferred` (richtinggevend, niet betrouwbaar). De onderliggende oorzaak — mismatch tussen AI-inzet en bedrijfsprobleem — is `verified` als consistent bevinding uit meerdere onafhankelijke analyses.

### 1.4 Geschiktheidscriteria: wanneer AI, wanneer niet

**AI is geschikt wanneer [7, 8]:**
- Het probleem te complex is voor deterministische regels (veel variabelen, uitzonderingsgevallen)
- De gewenste output beschrijfbaar maar niet volledig specificeerbaar in code is
- Data beschikbaar en voldoende representatief is
- Een zekere foutmarge acceptabel is
- Het doel kwantificeerbaar is ("van 3 dagen naar 5 minuten voor 200 beslissingen/jaar")

**AI is niet geschikt wanneer:**
- Een BI-dashboard of rule-based automatisering voldoet
- De benodigde data niet bestaat of niet toegankelijk is
- Foutmarge nul moet zijn zonder human oversight
- Het doel niet kwantificeerbaar is ("betere beslissingen" is geen criterium) [7]

**AI-3P Assessment Framework** (Marina Tosic, Towards Data Science, 24 sep. 2025) [8] biedt een kwantitatief scoringsmodel (`verified` via directe fetch):
- Gewogen score: People (40%) × Process (35%) × Product (25%), schaal 0-100
- 80-100: bouwen starten; 60-79: piloot met guardrails; 0-59: risico's eerst mitigeren
- Implementatietemplates beschikbaar in GitHub-repo van de auteur

---

## 2. Architectuurpatronen: wanneer kies je wat?

### 2.1 Anthropic's 5 Patronen als referentiekader

Anthropic's "Building Effective Agents" is de meest geciteerde autoritatieve bron voor AI-architectuurpatronen [9, 10]. Het beschrijft vijf werkstroompatronen plus autonome agents (`verified` via directe fetch):

**Werkstroompatronen** (LLMs en tools in vooraf gedefinieerde codepaden):
1. **Prompt Chaining** — sequentiële LLM-calls; deelbaar in stappen; latency ruilt voor nauwkeurigheid
2. **Routing** — classificeer input naar gespecialiseerde downstream-handlers
3. **Parallelisatie** — simultane LLM-calls via sectioning (parallelle deeltaken) of voting (meerdere pogingen)
4. **Orchestrator-Workers** — centrale LLM decomposeert dynamisch en delegeert aan workers; geschikt voor onvoorspelbare werklast
5. **Evaluator-Optimizer** — iteratieve verfijning met ingebouwde evaluator; effectief wanneer duidelijke evaluatiecriteria bestaan

**Autonome Agents** — LLMs met tools in feedbacklus, gereserveerd voor open-ended problemen "waarbij het moeilijk of onmogelijk is om het benodigde aantal stappen van tevoren te voorspellen." [9]

Drie kerneigenschappen voor alle implementaties [9]:
- **Eenvoud** in agent-ontwerp
- **Transparantie** in planningsstappen
- **Tool-interface design** ("behandel de agent-computer interface zoals human-computer interface design" — Anthropic besteedde meer tijd aan tool-optimalisatie dan aan algehele prompt-optimalisatie in hun SWE-bench agent)

### 2.2 De kernregel: begin simpel

Anthropic's fundamentele richtlijn: start met een eenvoudige LLM-call geoptimaliseerd met retrieval en voorbeelden. Voeg complexiteit alleen toe wanneer eenvoudigere oplossingen aantoonbaar tekortkomen. [9] (`verified`)

**Multi-agent is gerechtvaardigd wanneer [11]:**
- Taken zware parallelisatiepotentie hebben
- Informatie een enkel contextvenster overschrijdt
- Complexe tool-integraties vereist zijn

**Multi-agent is niet geschikt voor [11]:**
- Taken die gedeelde context vereisen tussen alle agents
- Zware inter-agent coördinatie
- De meeste coderingstaken

Anthropic's eigen multi-agent research system presteert 90,2% beter dan single-agent Claude Opus 4 op hun interne research-evaluatie, maar verbruikt ~15× meer tokens dan chat-interacties [11]. (`verified` via directe fetch)

### 2.3 MCP: de standaard tooling-laag

Het Model Context Protocol (MCP), geïntroduceerd door Anthropic op 25 november 2024 [12] (`verified` via directe fetch), is de opkomende standaard voor agent-tool-integraties. Client-server architectuur op basis van JSON-RPC 2.0. Adoptie: 97M+ maandelijkse SDK-downloads medio 2025; OpenAI adopteerde MCP officieel in maart 2025; in december 2025 vendor-neutraal gemaakt via de Agentic AI Foundation.

**Beveiligingsrisico's (niet negeren):** in april 2025 identificeerden security-onderzoekers prompt injection, tool-permission-misbruik voor data-exfiltratie, en lookalike tools die vertrouwde tools kunnen vervangen. [12]

**Blueprint-regel:** voor agent-systemen is MCP de default tooling-keuze. De vraag "welke tools heeft de agent nodig, via welke interface?" is een eerste-orde architectuurvraag in het blueprint.

### 2.4 RAG vs. Fine-tuning vs. Agents: drie architectuurlagen

Enterprise AI-architectuur kent drie onderscheiden lagen [13, 14]:

| Laag | Aanpak | Best voor |
|------|--------|-----------|
| **Kennislaag** | RAG | Frequent veranderende kennis; actuele informatie zonder model-hertraining |
| **Specialisatielaag** | Fine-tuning | Stabiele domeinen; hoog volume / lage latency; gedragspatronen inbakken |
| **Executielaag** | Agents | Bedrijfsprocessen *uitvoeren* via tools; handelen, niet alleen antwoorden |

Hybride architectuur (RAG + fine-tuning + agents) is het dominante patroon in 2026 (`inferred` via meerdere bronnen). De meest gemaakte fout in de blueprint-fase: een agent architecteren waar RAG voldoende is.

---

## 3. Risk-based Design: compliance als ontwerpinput

### 3.1 EU AI Act: vier tiers als eerste filter

De EU AI Act (inwerking 1 augustus 2024; meeste regels gelden per 2 augustus 2026) [15] (`verified` via directe fetch EU AI Act high-level summary):

**Tier 1 — Verboden:** sociale scoring, manipulatieve AI die menselijke vrije wil ondermijnt, realtime gezichtsherkenning in openbare ruimtes, emotieherkenning op de werkvloer.

**Tier 2 — Hoog risico (zwaarste design-verplichtingen):** biometrie, kritieke infrastructuur, onderwijs (toelating, beoordeling, gedragsmonitoring), werkgelegenheid (werving, promotie, prestatiebeoordeling), essentiële diensten (krediet, uitkeringen, noodoproep-dispatching), ordehandhaving, migratie/grens, rechtspraak.

**Tier 3 — Beperkt risico:** chatbots, deepfakes — transparantieverplichting naar gebruiker.

**Tier 4 — Minimaal risico:** spamfilters, video-game-AI — grotendeels ongereguleerd.

Design-verplichtingen voor Tier 2 (hoog risico) [15] (`verified`):
1. Risicomanagementsystemen gedurende de volledige levenscyclus
2. Datagovernance: kwaliteit en representativiteit
3. Technische documentatie voor compliance
4. Automatische event-logging voor incident tracking
5. Gebruikersinstructies voor deployer-compliance
6. Human oversight-mogelijkheden
7. Nauwkeurigheids-, robuustheids- en cybersecurity-standaarden
8. Kwaliteitsmanagementsystemen

**Blueprint-implicatie:** de EU AI Act-tier wordt vroeg in het blueprint bepaald — vóórdat architectuurkeuzes worden gemaakt. Tier 2 vereist 8 design-gates in het blueprint.

### 3.2 HLEG Trustworthy AI: 7 vereisten als blueprint-checks

De HLEG Ethics Guidelines for Trustworthy AI [16] (`verified` via Europese Commissie-bron) benoemen 7 vereisten:

1. Human Agency and Oversight
2. Technical Robustness and Safety
3. Privacy and Data Governance
4. Transparency
5. Diversity, Non-discrimination and Fairness
6. Societal and Environmental Well-being
7. Accountability

De **ALTAI-checklist** (Assessment List for Trustworthy AI, HLEG 2020) vertaalt deze 7 vereisten naar een interactieve zelfbeoordelingschecklist op altai.insight-centre.org [17] (`verified` via directe fetch — pagina bestaat en beschrijft het framework correct). Inzetbaar als onderdeel van het blueprint-gesprek voor elke AI-implementatie.

### 3.3 DPIA: verplicht voor de meeste AI-systemen

Voor AI-systemen is een Data Protection Impact Assessment (DPIA) in de meeste gevallen verplicht onder de GDPR [18]: "In de overgrote meerderheid van gevallen zal het gebruik van AI een type verwerking betreffen dat waarschijnlijk een hoog risico inhoudt voor de rechten en vrijheden van individuen." (`verified` via ICO — UK Information Commissioner's Office)

Samenloop EU AI Act en DPIA: de AI Act's Fundamental Rights Impact Assessment (FRIA) en de GDPR-DPIA overlappen maar zijn niet identiek — dit creëert dubbeling en compliance-onzekerheid voor hoog-risico AI [19]. (`verified`)

Blueprint-vragen privacy-by-design:
- Welke persoonsgegevens, voor welk doel, op welke rechtsgrondslag?
- DPIA vereist? (default: ja, tenzij aantoonbaar niet van toepassing)
- Data minimization: alleen verwerken wat noodzakelijk is?
- Welke rechten van betrokkenen zijn van toepassing (inzage, bezwaar, uitleg bij geautomatiseerde beslissingen)?

### 3.4 OWASP LLM Top-10 2025: threat modeling in de blueprint-fase

OWASP publiceerde de Top-10 voor LLM Applications 2025 op 17 november 2024 [20] (`verified` via directe fetch):

1. **LLM01 — Prompt Injection:** kwaadaardige input manipuleert het model om instructies te negeren
2. **LLM02 — Sensitive Information Disclosure:** PII of vertrouwelijke data lekt via output
3. **LLM03 — Supply Chain:** kwetsbaarheden in trainings- en deploymentsketens
4. **LLM04 — Data and Model Poisoning:** manipulatie tijdens pre-training of fine-tuning
5. **LLM05 — Improper Output Handling:** onvoldoende validatie/sanitisatie van output
6. **LLM06 — Excessive Agency:** systemen met te veel autonomie zonder adequate checks
7. **LLM07 — System Prompt Leakage:** blootstelling van interne systeem-prompts met gevoelige instructies
8. **LLM08 — Vector and Embedding Weaknesses:** kwetsbaarheden in RAG-systemen en vector databases
9. **LLM09 — Misinformation:** LLM-output als betrouwbare bron presenteren terwijl het dat niet is
10. **LLM10 — Unbounded Consumption:** ongecontroleerd resource-gebruik

**Guardrails-by-design principe:** verdediging in de diepte — input-filtering, gedragsconstrainering (strikte rol-instructies, taakbeperking), output-validatie met deterministische code, privilege-scheiding (least privilege voor agents), monitoring en logging. Guardrails zijn geen afterthought maar ontwerpparameter.

---

## 4. Iteratieve Blueprint: FDE, Prototype-driven & Playbook

### 4.1 Forward Deployed Engineering: het model en zijn grenzen

Palantir ontwikkelde het FDE-model (intern "Delta") in de vroege jaren 2010; tot circa 2016 had Palantir meer FDEs dan reguliere software-engineers [21] (`verified` via Pragmatic Engineer). Kernprincipe: "Dev: één capability, veel klanten; Delta: veel capabilities, één klant."

**Drie fasen (OpenAI FDE-model) [21]:**
1. Scoping — klantprobleem begrijpen
2. Validatie — oplossingen toetsen aan evaluatiecriteria
3. Implementatie — productie-oplossingen opleveren

"FDEs werken met enorme onzekerheid, en wat klanten beschrijven komt vaak niet overeen met de realiteit van hun data." [21] (`verified`)

FDE-aanpak is effectief bij: enterprise-klanten met complexe integratievragen, AI/LLM-implementaties waar klantcontext cruciaal is, situaties waar snelle iteratie en directe feedback noodzakelijk zijn. [21, 22]

Marktbevestiging: FDE-vacatures stegen met >800% tussen januari en september 2025; Salesforce committeert zich aan 1.000 FDEs [22]. (`verified`)

**Beperkingen en contra-perspectief:**
- **Schaalbaarheidsgrens:** FDE-werk is klant-specifiek en niet schaalbaar als standaard productcapability [21] (`inferred`)
- **Rolvervaging:** de grens tussen FDE, Solutions Architect, Sales Engineer en Agent Engineer vervaagt; Salesforce's FDE-profiel beschrijft "praktisch twee beroepen in één" [22] (`inferred`)
- **SVPG-kritiek (Marty Cagan):** klant-specifieke customisaties riskeren de productstrategie te dicteren in plaats van een coherente productvisie [21] (`inferred` — SVPG-positie geciteerd via Pragmatic Engineer, directe SVPG-bron gaf 403-fout)

**Blueprint-implicatie:** FDE-*principes* (embedded, iteratief, bouwen ipv adviseren) zijn waardevol als werkwijze voor de blueprint-fase. Het volledige FDE-model is niet de default voor elke opdracht. BB_02 moet onderscheid maken: wanneer is embedded iteratie nodig, wanneer volstaat een klassieke discovery-fase?

### 4.2 AI-prototyping-tools als blueprint-vehikel: sterktes en faalmodi

Vier tools domineren het 2026-landschap als prototype-instrument voor klantgesprekken [23, 24, 25] (`verified` via NxCode tool-vergelijking en Lenny's Newsletter):

| Tool | Sterk als blueprint-vehikel | Faalmodus in blueprint-context |
|------|----------------------------|-------------------------------|
| **Google Stitch** (Google I/O 2025) | Live ideation, multi-richtingUX-verkenning, voice canvas in meetings | Geen backend — misleidend voor complexe businesslogica; Labs-status schept onzekerheid |
| **v0 by Vercel** | Production-ready React-componenten; developer-team alignment | Alleen React/Next.js; componenten ≠ applicaties; technisch publiek noodzakelijk |
| **Lovable** | Full-stack MVP (TypeScript + Supabase + auth + hosting); non-technische stakeholders | Vendor lock-in; klanten overschatten gereedheid; design-kwaliteit secundair |
| **Bolt.new** | Snelste output; live demo in meeting; browser — nul setup | Token-kosten onvoorspelbaar bij iteratie; eerste output is ruw |
| **Claude Artifacts** | Enkelvoudige interactieve component; PoC delen in 10 minuten | Geen persistente state; beperkt tot één artefact |

**Prototype is productief als [24, 25]:**
- Gespreksanker: klant ziet en reageert op iets concreets in plaats van een tekstdocument
- Aanname-invalidatie: prototype laat zien wat *niet* werkt, niet alleen wat kan
- Versnelling van scope-verkenning vóór architectuurcommitment

**Prototype is contraproductief als [24, 25]:**
- Surrogaat voor gebruikersonderzoek — gepolijste UI creëert schijn-zekerheid over probleemvalidatie
- Validatie zonder criteria — "als je geen evaluatiecriteria hebt, valideert een prototype niets"
- Vervanging voor het gesprek over doel, data en risico's

"AI is geen vervanging voor kritisch denken; menselijk oordeel is nog steeds noodzakelijk om gegenereerde inzichten te interpreteren en geïnformeerde productbeslissingen te nemen." [25] (`verified`)

**Kritische waarschuwing:** alle vier de tools genereren oppervlakkig gepolijste UIs die strategische vragen (gebruikersonderzoek, businesslogica-validatie, A/B-test setup) niet beantwoorden. [24]

**Blueprintregel:** prototype = discovery-instrument, niet validatie-eindpunt. Het versnelt de discussie over doel, sucescriteria, data en risico's — maar vervangt die discussie niet.

### 4.3 Playbook-structuur: 10 verplichte blueprint-elementen

Op basis van gesynthetiseerde bevindingen uit alle vier research-lanes zijn 10 elementen noodzakelijk voor een compleet blueprint-gesprek:

**Blok A — Doel en sucescriteria**
1. **Doel** — welke beslissing of uitkomst wordt verbeterd? Wie neemt die beslissing, hoe vaak? [1, 2]
2. **Sucescriteria** — kwantificeerbaar: "van X naar Y voor Z gevallen per jaar à €N per geval" [7]

**Blok B — Processen en output**
3. **Processen** — welke bestaande processen raken dit? wie is betrokken? wat verandert er voor hen?
4. **Output** — wat produceert het systeem, voor wie, in welk formaat, met welke kwaliteitsvereisten?

**Blok C — Data en integraties**
5. **Data** — welke data is nodig, beschikbaar, representatief? privacy-rechtsgrondslag? DPIA-trigger? [18]
6. **Tools/integraties** — welke systemen moet het AI-systeem bereiken? MCP-kandidaten? [12]

**Blok D — Risico's en compliance**
7. **Risico's** — EU AI Act-tier [15], HLEG/ALTAI-check [16, 17], OWASP-threats [20], DPIA [18]

**Blok E — Architectuur en iteratie**
8. **Architectuur** — workflow of agent? RAG, fine-tuning of agents? MCP-tooling? [9, 11, 12, 13]
9. **Iteratieplan** — wat is de eerste versie? hoe wordt gevalideerd? sucescriteria per iteratie?

**Blok F — Governance**
10. **Sign-off** — wie geeft akkoord, op welke criteria, wanneer?

**Vroege geschiktheidscheck (vóór Blok A):**
Anthropic's drie-signalen framework [26]:
- Complexe besluitvorming die contextueel varieert? (→ routing of agent)
- Regelonderhoud dat developer-tijd vereist bij elke wijziging? (→ LLM vervangt regel-engine)
- Ongestructureerde data (natural language, documenten, conversaties)? (→ RAG of agent)

AI-3P vroege filter [8]: score op People (40%), Process (35%), Product (25%) → Bouwen / Piloot met guardrails / Risico's eerst aanpakken.

---

## Tegenstrijdigheden en open vragen

**Tegenstrijdigheid 1: MIT 95% vs. methodologische kritiek**
Het MIT NANDA-rapport (aug. 2025) claimt 95% AI-pilot-falen [5]; Marketing AI Institute (Paul Roetzer) betoogt dat de methodologie dit getal niet ondersteunt [6]. Beide zijn gedocumenteerd. Conclusie: het exacte getal is onbetrouwbaar, de oorzaak-diagnose (mismatch probleem-aanpak) is bevestigd door andere onafhankelijke bronnen.

**Tegenstrijdigheid 2: FDE als best practice vs. schaalbaarheidsgrens**
Explosieve groei van FDE-vacatures (+800% in 2025) suggereert breed draagvlak [22]; SVPG (Cagan) waarschuwt dat het model productstrategie kan ondermijnen [21]. BB_02 moet dit spanningsveld expliciteren: FDE-principes zijn waardevol, het volledige FDE-model is niet de default.

**Tegenstrijdigheid 3: prototype als gespreksanker vs. schijn-zekerheid**
Prototype-tools verlagen de drempel voor concrete demo's, maar creëren daarmee ook het risico van overschatting van gereedheid. Beide zijn tegelijkertijd waar — het verschil zit in het gebruik, niet in de tool.

## Open vragen

**MAJOR:**
- **Concrete gepubliceerde playbook-template** — geen enkel gecheckt openbaar document biedt een compleet, klant-gebruik klare discovery-template voor AI-blueprints (Anthropic, Google, IDEO niet gevonden als openbaar gepubliceerd). De 10 blueprint-elementen in dit rapport zijn gesynthetiseerd uit meerdere bronnen maar niet ontleend aan één primaire template-bron.
- **Stanford Enterprise AI Playbook (51 cases)** — PDF niet tekstueel leesbaar via fetch; bevindingen (73% bewust klein gestart, 63% pilot-als-experiment) zijn via zoekresultaat-samenvatting beschikbaar maar niet direct geverifieerd vanuit de primaire tekst.

**MINOR:**
- OWASP Agentic AI Top-10 (OWASP, late 2025) — vermeld in zoekresultaat maar directe URL niet geverifieerd. Relevant voor agentic systemen in BB_02.
- SVPG-kritiek op FDE — geciteerd via Pragmatic Engineer maar directe SVPG-pagina gaf 403-fout. Positie consistent beschreven maar niet direct geverifieerd.

---

## Sources

Alle bronnen geraadpleegd op 2026-04-26. Verificatiestatus per claim staat inline (`verified` / `inferred` / `unverified`).

### Use Case-selectie & Probleem-framing

- [Kozyrkov — AI-First Leadership: Rethinking Decision-making in the Age of AI (INFORMS Analytics Magazine)](https://pubsonline.informs.org/do/10.1287/LYTX.2025.02.02n/full/) — Decision-first framework, drie evaluatiecriteria [1]
- [Acceldata — Cassie Kozyrkov on What AI Really Means for Enterprise Leaders](https://www.acceldata.io/blog/cassie-kozyrkov-on-what-it-really-means-to-be-ai-first-key-takeaways-for-enterprise-leaders) — AI-first definitie, "purpose comes from people" [2]
- [Inference by Sequoia — Karpathy's Software 3.0 and the New AI Stack](https://inferencebysequoia.substack.com/p/andrej-karpathys-software-30-and) — Software 3.0 keynote YC AI Startup School 19 juni 2025 [3]
- [Medium (Ben Pouladian) — Andrej Karpathy on Software 3.0: Software in the Age of AI](https://medium.com/@ben_pouladian/andrej-karpathy-on-software-3-0-software-in-the-age-of-ai-b25533da93b6) — LLM als OS-metafoor [4]
- [Fortune — MIT report: 95% of generative AI pilots at companies are failing (aug. 2025)](https://fortune.com/2025/08/18/mit-report-95-percent-generative-ai-pilots-at-companies-failing-cfo/) — MIT NANDA rapport, methodologie [5]
- [Marketing AI Institute — That Viral MIT Study Claiming 95% of AI Pilots Fail? Don't Believe the Hype](https://www.marketingaiinstitute.com/blog/mit-study-ai-pilots) — Methodologische kritiek, Paul Roetzer [6]
- [Microsoft — Microsoft AI Decision Framework (GitHub)](https://github.com/microsoft/Microsoft-AI-Decision-Framework) — Kwantificeerbaarheidscriterium, governance-focus [7]
- [Towards Data Science — Introducing the AI-3P Assessment Framework (Marina Tosic, 24 sep. 2025)](https://towardsdatascience.com/the-ai-3p-assessment-framework/) — People-Process-Product scoringsmodel [8]

### Architectuurpatronen

- [Anthropic — Building Effective Agents (research)](https://www.anthropic.com/research/building-effective-agents) — 5 workflow-patronen, drie kerneigenschappen, begin-simpel-regel [9]
- [Anthropic Resources — Building Effective AI Agents: Architecture Patterns and Implementation Frameworks](https://resources.anthropic.com/building-effective-agents) — Uitgebreide architectuurhandleiding [10]
- [Anthropic Engineering — How We Built Our Multi-Agent Research System](https://www.anthropic.com/engineering/multi-agent-research-system) — 90,2% prestatieverbetering, 15x token-gebruik, wanneer multi-agent werkt en niet [11]
- [Anthropic — Introducing the Model Context Protocol (25 nov. 2024)](https://www.anthropic.com/news/model-context-protocol) — MCP architectuur, adoptie, beveiligingsrisico's [12]
- [Orq.ai — RAG Architecture Explained: A Comprehensive Guide [2026]](https://orq.ai/blog/rag-architecture) — Drie architectuurlagen, hybride patronen [13]
- [Techment — RAG vs Fine-Tuning vs AI Agents: Choosing the Right LLM Strategy](https://www.techment.com/blogs/rag-vs-fine-tuning-vs-ai-agents-llm-strategy/) — Drie-lagenmodel, beslismatrix [14]

### Risk-based Design

- [EU AI Act — High-Level Summary (artificialintelligenceact.eu)](https://artificialintelligenceact.eu/high-level-summary/) — Vier risico-tiers, Annex III categorieën, Tier 2 design-verplichtingen [15]
- [European Commission — Ethics Guidelines for Trustworthy AI (HLEG)](https://digital-strategy.ec.europa.eu/en/library/ethics-guidelines-trustworthy-ai) — HLEG 7 vereisten [16]
- [ALTAI — Assessment List for Trustworthy AI (interactieve tool)](https://altai.insight-centre.org/) — HLEG zelfbeoordelingschecklist [17]
- [ICO — Accountability and governance implications of AI (GDPR guidance)](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/artificial-intelligence/guidance-on-ai-and-data-protection/what-are-the-accountability-and-governance-implications-of-ai/) — DPIA-verplichting voor AI-systemen [18]
- [TechGDPR — Data protection digest: AI Act and GDPR study (nov. 2025)](https://techgdpr.com/blog/data-protection-digest-03112025-new-ai-act-and-gdpr-study-personal-data-stored-on-blockchain/) — FRIA vs. DPIA overlap en dubbeling [19]
- [OWASP — Top 10 for LLM Applications 2025 (gepubliceerd 17 nov. 2024)](https://genai.owasp.org/llm-top-10/) — Volledige LLM Top-10 2025 [20]
- [Getmaxim.ai — The Complete AI Guardrails Implementation Guide for 2026](https://www.getmaxim.ai/articles/the-complete-ai-guardrails-implementation-guide-for-2026/) — Guardrails implementatie, defence in depth [aanvullend]

### FDE, Iteratieve Blueprint & Playbook

- [Pragmatic Engineer — What are Forward Deployed Engineers, and why are they so in demand?](https://newsletter.pragmaticengineer.com/p/forward-deployed-engineers) — FDE origine (Palantir "Delta"), kernprincipes, drie fasen, schaalbaarheidsgrens, SVPG-vermelding [21]
- [SSO Network — Forward Deployed Engineers: Turning AI Promise into Progress](https://www.ssonetwork.com/intelligent-automation/columns/forward-deployed-engineers-guide) — 800% vacature-stijging, Salesforce 1.000 FDEs, rolvervaging [22]
- [NxCode — Vibe Design Tools 2026: Stitch vs v0 vs Lovable vs Bolt Compared](https://www.nxcode.io/resources/news/vibe-design-tools-compared-stitch-v0-lovable-2026) — Tool-vergelijking, sterktes en faalmodi per tool [23]
- [NxCode — Google Stitch vs v0 vs Lovable 2026](https://www.nxcode.io/resources/news/google-stitch-vs-v0-vs-lovable-ai-app-builder-2026) — Strategisch inzetbaarheidsoverzicht [24]
- [Lenny's Newsletter — A Guide to AI Prototyping for Product Managers](https://www.lennysnewsletter.com/p/a-guide-to-ai-prototyping-for-product) — Wanneer productief, tool-keuze, kritische kanttekening [25]
- [WorkOS — Enterprise AI Agent Playbook: What Anthropic and OpenAI Reveal](https://workos.com/blog/enterprise-ai-agent-playbook-what-anthropic-and-openai-reveal-about-building-production-ready-systems) — Drie-signalen framework voor agent-geschiktheid [26]
- [Stanford Digital Economy Lab — Enterprise AI Playbook: Lessons from 51 Successful Deployments (Pereira, Graylin, Brynjolfsson, 2026)](https://digitaleconomy.stanford.edu/app/uploads/2026/03/EnterpriseAIPlaybook_PereiraGraylinBrynjolfsson.pdf) — 73% bewust klein gestart, 63% pilot-als-experiment (`inferred` — PDF niet tekstueel leesbaar) [aanvullend]

### Kerncitaten

- Kozyrkov: *"The purpose is important, and the purpose comes from people."* — Acceldata interview [2]
- Anthropic: *"Start with a simple prompt chain optimized with retrieval and examples before adding complexity."* — Building Effective Agents [9]
- Pragmatic Engineer (over FDE): *"FDEs work with enormous uncertainty, and often what clients describe doesn't match the reality of their data."* — [21]
- Lenny's Newsletter: *"AI is not a substitute for critical thinking; human judgment is still necessary to interpret generated insights and make informed product decisions."* — [25]
