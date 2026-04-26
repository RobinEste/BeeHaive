# BB_02 Client Blueprint: Patronen voor AI-oplossingen in 2024-2026

**Onderwerp:** Actuele patronen voor het ontwerpen van AI-oplossingen — van probleemkeuze tot architectuur, risico-inschatting, iteratieve validatie en prototype-driven blueprinting
**Datum:** 2026-04-26
**Researcher-rondes:** 1

---

## Executive Summary

De meerderheid van enterprise AI-pilots levert geen meetbaar resultaat — niet omdat de modellen slecht zijn, maar omdat het verkeerde probleem wordt aangepakt of het juiste probleem op de verkeerde manier wordt benaderd. Succesvolle AI-ontwerpen beginnen met de *beslissing*, niet met de technologie, en bouwen van simpel naar complex in plaats van andersom.

Drie patronen onderscheiden de 5% die slaagt van de rest. Ten eerste: een expliciete geschiktheidscheck vóór committering aan een architectuur — is dit eigenlijk een AI-probleem, en zo ja, welk type? Ten tweede: risico- en compliance-overwegingen als *ontwerpinput*, niet als afterthought (EU AI Act, HLEG, DPIA, OWASP). Ten derde: een iteratieve blueprint waarbij een prototype als gespreksanker dient voor stakeholder-alignment, maar nooit als surrogaat voor diepgaande probleemverkenning.

BB_02 moet deze drie patronen operationeel maken via een gestructureerde gespreksleidraad met concrete beslisregels per fase: van probleemframing via architectuurkeuze en risicocheck naar sign-off en iteratieplan.

---

## 1. Use Case-selectie: welk probleem is een AI-probleem?

### 1.1 Decision-first als vertrekpunt

Cassie Kozyrkov, voormalig Chief Decision Scientist bij Google, heeft het concept *decision intelligence* gepopulariseerd als het juiste vertrekpunt voor AI-initiatieven [1, 2]. De kernvraag is niet "welke AI kunnen we inzetten?" maar "welke beslissingen zijn het waard om beter te nemen?" (`verified`).

Dit lijkt vanzelfsprekend, maar de praktijk laat het tegendeel zien. Bedrijven die AI inzetten om "bij te blijven" of "aan de verwachting van de board te voldoen" starten op het verkeerde punt. Kozyrkov: "The purpose is important, and the purpose comes from people." [2]

**Blueprint-implicatie:** het eerste gesprek met de klant moet gaan over de beslissing of uitkomst die verbeterd moet worden, inclusief wie die beslissing neemt, hoe vaak, en wat de kosten zijn van een slechte beslissing.

### 1.2 AI-first vs. AI-augmented: twee legitieme vertrekpunten

"AI-first" betekent in Kozyrkov's definitie niet "AI voor alles" maar "bereid zijn het voorheen onmogelijke te heroverwegen" [1]. Twee legitieme vertrekpunten:

- **AI-augmented:** bestaande processen versnellen of verbeteren met AI-assistentie (de meeste enterprise use cases)
- **AI-first:** processen fundamenteel herdenken vanuit wat nu mogelijk is — Andrej Karpathy's "Software 3.0" waar prompts in natuurlijke taal de broncode vormen [3, 4]

Karpathy introduceerde Software 3.0 op 19 juni 2025 bij Y Combinator's AI Startup School. De progressie: Software 1.0 (expliciete code) → Software 2.0 (geleerde gewichten, neurale netwerken) → Software 3.0 (prompts als broncode, LLM als operating system). [3] (`verified` via meerdere onafhankelijke analyses)

Het risico van dit frame: niet alles wat *beschrijfbaar* is in taal is ook *betrouwbaar uitvoerbaar* door een LLM. Een blueprint moet dit onderscheid operationeel maken.

### 1.3 Het MIT-onderzoek: wat het zegt en wat niet

Het MIT NANDA-initiatief publiceerde in augustus 2025 het rapport *The GenAI Divide: State of AI in Business 2025* met de bevinding dat 95% van enterprise AI-pilots geen meetbaar P&L-resultaat levert [5]. Methodologie: 150 interviews, 350-persoons survey, analyse van 300 publieke implementaties.

**Nuance:** Marketing AI Institute signaleert methodologische zwaktes [6]:
- Succescriterium smal gedefinieerd (ROI binnen 6 maanden, deployment buiten pilotfase)
- Efficiëntiewinsten en kostenbesparingen niet meegeteld
- 52 interviews als statistische grondslag is te smal
- Rapportagevertekening waarschijnlijk

De *95%-claim is als harde statistiek onbetrouwbaar* (`inferred` — kritiek goed onderbouwd). De onderliggende oorzaak die meerdere onafhankelijke analyses bevestigen, is echter consistent: mismatch tussen AI-aanpak en werkelijk bedrijfsprobleem.

### 1.4 Geschiktheidscriteria: wanneer wel, wanneer niet

AI is geschikt wanneer [7, 8]:
- Het probleem te complex is voor deterministische regels (veel variabelen, edge cases)
- De gewenste output beschrijfbaar maar niet volledig specificeerbaar in code is
- Data beschikbaar en voldoende representatief is
- Een zekere foutmarge in output acceptabel is
- De klant het doel kan kwantificeren (bijv. "van 3 dagen naar 5 minuten voor 200 beslissingen/jaar à €5.000 per beslissing")

AI is *niet* geschikt wanneer:
- Een BI-dashboard of rule-based automatisering volstaat
- De benodigde data niet bestaat of niet toegankelijk is
- Foutmarge nul moet zijn zonder human oversight
- Het doel niet kwantificeerbaar is ("betere beslissingen" is geen meetcriterium)

Het **AI-3P Assessment Framework** (People–Process–Product) biedt een kwantitatief scoringsmodel als vroege filter [8]:
- Gewogen score: People (40%) × Process (35%) × Product (25%)
- 80-100: bouwen starten; 60-79: piloot met guardrails; 0-59: risico's eerst mitigeren

(`verified` via directe fetch Towards Data Science-artikel [8])

---

## 2. Architectuurpatronen: wanneer kies je wat?

### 2.1 Anthropic's 5 Patronen als referentiekader

Anthropic's "Building Effective Agents" is de meest geciteerde autoritatieve bron voor AI-architectuurpatronen [9, 10]. Het beschrijft vijf werkstroompatronen plus autonome agents:

**Werkstroompatronen** (vooraf gedefinieerde codepaden):
1. **Prompt Chaining** — sequentieel, deelbaar, latency ↔ nauwkeurigheid
2. **Routing** — classificeer input naar gespecialiseerde handlers
3. **Parallelisatie** — simultane LLM-calls via sectioning of voting
4. **Orchestrator-Workers** — centrale LLM decomposeert dynamisch naar workers
5. **Evaluator-Optimizer** — iteratieve verfijning met ingebouwde evaluator

**Autonome Agents** — LLMs met tools in feedbacklus, gereserveerd voor open-ended problemen waarbij het aantal benodigde stappen niet vooraf bepaalbaar is. (`verified` via directe fetch [9])

Alle patronen delen drie kerneigenschappen: eenvoud, transparantie, en zorgvuldig tool-interface design ("behandel de agent-computer interface zoals human-computer interface design"). [9]

### 2.2 De kernregel: begin simpel

Anthropic's fundamentele richtlijn: start met een eenvoudige LLM-call geoptimaliseerd met retrieval en voorbeelden. Voeg complexiteit alleen toe wanneer eenvoudigere oplossingen aantoonbaar tekortkomen en evaluatie dit bewijst. [9] (`verified`)

**Concreet besliscriterium:** multi-agent is gerechtvaardigd wanneer:
- Taken zware parallelisatiepotentie hebben
- Informatie een enkel contextvenster overschrijdt
- Complexe tool-integraties vereist zijn

Multi-agent is *niet* geschikt voor:
- Taken die gedeelde context vereisen tussen alle agents
- Zware inter-agent coördinatie
- De meeste coderingstaken (onvoldoende paralleliseerbare componenten)

Anthropic's eigen multi-agent research system behaalt 90,2% betere prestaties dan single-agent op hun interne research-evaluatie, maar verbruikt ~15× meer tokens. [11] (`verified` via directe fetch)

### 2.3 MCP: de standaard tooling-laag

Het Model Context Protocol (MCP), geïntroduceerd door Anthropic in november 2024, is de opkomende standaard voor agent-tool-integraties [12]. Client-server architectuur op basis van JSON-RPC 2.0. Adoptie: 97M+ maandelijkse SDK-downloads medio 2025; OpenAI adopteerde MCP officieel in maart 2025; in december 2025 vendor-neutraal gemaakt via de Agentic AI Foundation.

**Beveiligingsrisico's zijn reëel:** in april 2025 identificeerden security-onderzoekers prompt injection, tool-permission-misbruik voor data-exfiltratie, en lookalike tools die vertrouwde tools kunnen vervangen. [12]

**Blueprint-regel:** voor agent-systemen is MCP de default tooling-keuze. De vraag "welke tools heeft de agent nodig, via welke interface?" is een eerste-orde architectuurvraag die in het blueprint beantwoord moet worden.

### 2.4 RAG vs. Fine-tuning vs. Agents: drie architectuurlagen

Enterprise AI-architectuur kent drie onderscheiden lagen [13, 14]:
- **RAG (kennislaag):** dynamische toegang tot actuele informatie; best voor frequent veranderende kennis. In productie gebruikt door 51% van enterprise AI-deployments [13] (`unverified` — marktcijfer via samenvatting zonder directe URL)
- **Fine-tuning (specialisatielaag):** stabiel domeingedrag inbakken; best voor statische domeinen met hoge volume/lage latency
- **Agents (executielaag):** bedrijfsprocessen uitvoeren via tools; best wanneer het doel is te *handelen*, niet te *antwoorden*

Hybride architectuur (RAG + fine-tuning + agents) is het dominante patroon in 2026. (`inferred` via meerdere bronnen)

De meest gemaakte fout in de blueprint-fase: een agent architecteren waar RAG voldoende is.

---

## 3. Risk-based Design: compliance als ontwerpinput

### 3.1 EU AI Act: vier tiers als eerste filter

De EU AI Act (inwerking 1 augustus 2024, meeste regels gelden per 2 augustus 2026) hanteert vier risico-tiers [15]:

**Tier 1 — Verboden:** sociale scoring, manipulatieve AI, realtime gezichtsherkenning in openbare ruimtes, emotieherkenning op werkvloer. (`verified`)

**Tier 2 — Hoog risico (zwaarste design-verplichtingen):** biometrie, kritieke infrastructuur, onderwijs (toelating/beoordeling), werkgelegenheid (werving/promotie), essentiële diensten (krediet, uitkeringen), ordehandhaving, migratie/grens, rechtspraak. (`verified`)

**Tier 3 — Beperkt risico:** chatbots, deepfakes — transparantieverplichting naar gebruiker.

**Tier 4 — Minimaal risico:** spamfilters, video-game-AI — grotendeels ongereguleerd.

Design-verplichtingen voor hoog-risico systemen (Tier 2) [15]:
1. Risicomanagementsystemen gedurende de volledige levenscyclus
2. Datagovernance: kwaliteit en representativiteit
3. Technische documentatie voor compliance
4. Automatische event-logging
5. Gebruikersinstructies voor deployer-compliance
6. Human oversight-mogelijkheden
7. Nauwkeurigheids-, robuustheids- en cybersecurity-standaarden
8. Kwaliteitsmanagementsystemen

(`verified` via directe fetch EU AI Act high-level summary)

**Blueprint-implicatie:** de EU AI Act-tier is een vroege vraag in de blueprint — vóórdat architectuurkeuzes worden gemaakt. Hoog-risico AI vereist 8 design-gates die in het blueprint uitgewerkt moeten worden.

### 3.2 HLEG Trustworthy AI: 7 vereisten als blueprint-checks

De HLEG Ethics Guidelines for Trustworthy AI (EU, 2019/2020) benoemen 7 vereisten die als ontwerp-checklist fungeren [16]:

1. Human Agency and Oversight
2. Technical Robustness and Safety
3. Privacy and Data Governance
4. Transparency
5. Diversity, Non-discrimination and Fairness
6. Societal and Environmental Well-being
7. Accountability

De **ALTAI-checklist** (Assessment List for Trustworthy AI) vertaalt deze 7 vereisten naar een praktische, interactieve zelfbeoordelingschecklist op altai.insight-centre.org [17]. (`verified`)

**Blueprint-implicatie:** de ALTAI-checklist is direct inzetbaar als onderdeel van het blueprint-gesprek voor elke AI-implementatie, ongeacht het risiconiveau.

### 3.3 DPIA: verplicht voor de meeste AI-systemen

Voor AI-systemen is een Data Protection Impact Assessment (DPIA) in de meeste gevallen verplicht onder de GDPR [18]: "In de overgrote meerderheid van gevallen zal het gebruik van AI een type verwerking betreffen dat waarschijnlijk een hoog risico inhoudt voor de rechten en vrijheden van individuen." (`verified` via ICO-bron)

Samenloop EU AI Act en DPIA: de Fundamental Rights Impact Assessment (FRIA) van de AI Act en de GDPR-DPIA overlappen maar zijn niet identiek — dit creëert dubbeling en compliance-onzekerheid voor hoog-risico AI. [19] (`verified`)

Blueprint-vragen voor privacy-by-design:
- Welke persoonsgegevens, voor welk doel, op welke rechtsgrondslag?
- DPIA vereist? (default: ja)
- Data minimization: wordt alleen verwerkt wat noodzakelijk is?
- Welke rechten van betrokkenen zijn van toepassing?

### 3.4 OWASP LLM Top-10 2025: threat modeling in de blueprint-fase

De OWASP Top-10 voor LLM-applicaties 2025 [20] biedt een threat modeling-kader voor de blueprint-fase. Meest relevante risico's:

- **Prompt Injection (LLM01):** input manipuleert model om instructies te negeren → input/output-filtering
- **Sensitive Information Disclosure (LLM06):** PII of vertrouwelijke data lekt via output → output-screening
- **Vector and Embedding Weaknesses (LLM08, nieuw 2025):** RAG-systeem- en vector-DB-kwetsbaarheden
- **System Prompt Leakage (LLM09, nieuw 2025):** interne systeem-prompts blootgesteld

Voor agentic systemen publiceerde OWASP in late 2025 een aparte Top-10. (`inferred` — vermeld in zoekresultaat, directe URL niet geverifieerd)

**Guardrails-by-design principe:** verdediging in de diepte — input-filtering, gedragsconstrainering, output-validatie, privilege-scheiding (least privilege), monitoring en logging. Guardrails zijn geen afterthought maar ontwerpparameter.

---

## 4. Iteratieve Blueprint: FDE, Prototype-driven & Playbook

### 4.1 Forward Deployed Engineering: het model en zijn grenzen

Palantir ontwikkelde het FDE-model ("Delta") in de vroege jaren 2010; tot 2016 had Palantir meer FDEs dan reguliere software-engineers [21]. Kernprincipe: "Dev: één capability, veel klanten; Delta: veel capabilities, één klant."

**Drie FDE-fasen (OpenAI-model) [21]:**
1. Scoping — klantprobleem begrijpen
2. Validatie — oplossingen toetsen aan evaluatiecriteria
3. Implementatie — productie-oplossingen opleveren

FDE-aanpak is effectief bij: enterprise-klanten met complexe integratievraagstukken, AI/LLM-implementaties waar klantcontext cruciaal is, situaties waar snelle iteratie en directe feedback noodzakelijk zijn. [21, 22] (`verified`)

**Beperkingen en contra-perspectief:**
- **Schaalbaarheidsgrens:** FDE-werk is klant-specifiek en niet schaalbaar als standaard productcapability [21] (`inferred`)
- **Rolvervaging:** de grens tussen FDE, Solutions Architect, Sales Engineer en Agent Engineer vervaagt — Salesforce's FDE-profiel beschrijft "praktisch twee beroepen in één" [22] (`inferred`)
- **SVPG-kritiek (Marty Cagan):** klant-specifieke customisaties riskeren de productstrategie te dicteren in plaats van een coherente productvisie [21] (`inferred` — SVPG-positie via Pragmatic Engineer geciteerd)

**Blueprint-implicatie voor BB_02:** FDE-*principes* (embedded, iteratief, bouw ipv adviseer) zijn waardevol als werkwijze voor de blueprint-fase. Het volledige FDE-model is niet de default voor elke opdracht — BB_02 moet onderscheid maken wanneer embedded iteratie nodig is vs. wanneer een klassieke discovery-fase voldoet.

### 4.2 Prototype-driven blueprinting: sterktes en faalmodi

Vier tools domineren het 2026-landschap als prototype-instrument [23, 24, 25]:

| Tool | Sterk voor | Faalmodus |
|------|-----------|-----------|
| **Google Stitch** | Live ideation, multi-richting UI-verkenning, meetings | Geen backend — misleidend voor complexe businesslogica |
| **v0 by Vercel** | Developer-teams, production-ready React-componenten | Alleen React/Next.js; componenten ≠ applicaties |
| **Lovable** | Non-technische stakeholders, full-stack MVP-validatie | Vendor lock-in; klanten overschatten gereedheid |
| **Bolt.new** | Snelste output, live demo in meetings, mobile + web | Token-kosten onvoorspelbaar; eerste output is ruw |
| **Claude Artifacts** | Enkelvoudige component, snel te delen PoC | Geen persistente state, beperkt tot één artefact |

**Prototype is productief als [24, 25]:**
- Gespreksanker voor stakeholder-alignment (klant ziet en reageert op iets concreets)
- Aanname-invalidatie-instrument (prototype laat zien wat *niet* werkt)
- Versnelling van scope-verkenning vóór commitment aan architectuur

**Prototype is contraproductief als [24, 25]:**
- Surrogaat voor gebruikersonderzoek (polished UI creëert schijn-zekerheid)
- Equivalent aan validatie zonder criteria ("als je geen evaluatiecriteria hebt, valideert een prototype niets")
- Vervanging voor het gesprek over doel, data en risico's

Lenny's Newsletter: "AI is geen vervanging voor kritisch denken; menselijk oordeel is nog steeds noodzakelijk om gegenereerde inzichten te interpreteren en geïnformeerde productbeslissingen te nemen." [25] (`verified`)

**Kritische waarschuwing:** alle vier de tools genereren oppervlakkig gepolijste UIs die strategische vragen (gebruikersonderzoek, businesslogica-validatie, A/B-test setup) niet beantwoorden. [24]

**Blueprintregel:** prototype = discovery-instrument, niet validatie-eindpunt. Het versnelt de discussie over doel, sucescriteria, data en risico's — maar vervangt die discussie niet.

### 4.3 Playbook-structuur: 10 blueprint-elementen

Op basis van alle onderzochte bronnen zijn 10 elementen noodzakelijk voor een volledig blueprint-gesprek. Elke klant-sessie moet deze dekken:

1. **Doel** — welke beslissing of uitkomst wordt verbeterd? (Kozyrkov's decision-first [1, 2])
2. **Sucescriteria** — kwantificeerbaar: "van X naar Y voor Z gevallen per jaar" (Microsoft AI Decision Framework [7])
3. **Processen** — welke bestaande processen raken dit? wie is betrokken?
4. **Output** — wat produceert het systeem, voor wie, in welk formaat?
5. **Data** — welke data is nodig, beschikbaar, representatief? DPIA-trigger? [18]
6. **Tools/integraties** — welke systemen moet het AI-systeem bereiken? MCP-kandidaten? [12]
7. **Risico's** — EU AI Act-tier [15], HLEG-check [16, 17], OWASP-threats [20], DPIA [18]
8. **Architectuur** — workflow of agent? RAG, fine-tuning of agents? [9, 13, 14]
9. **Iteratieplan** — wat is de eerste versie? hoe wordt gevalideerd? welke sucescriteria per iteratie?
10. **Sign-off** — wie moet akkoord geven, op welke criteria, wanneer?

Aanvullend gestructureerde geschiktheidscheck via Anthropic's drie-signalen framework [26]:
- Complexe besluitvorming die contextueel varieert?
- Regelonderhoud dat developer-tijd vereist bij elke wijziging?
- Ongestructureerde data (natural language, documenten, conversaties)?

En AI-3P vroege filter [8]: score op People (40%), Process (35%), Product (25%) → Bouwen / Piloot met guardrails / Risico's eerst.

---

## Tegenstrijdigheden en open vragen

**Tegenstrijdigheid 1: MIT 95% vs. methodologische kritiek**
Het MIT NANDA-rapport claimt 95% AI-pilot-falen; Marketing AI Institute betoogt dat de methodologie onvoldoende is voor deze claim. Beide staan. De oorzaak die ze gemeenschappelijk hebben (mismatch probleem-aanpak) is echter consistent met andere bronnen.

**Tegenstrijdigheid 2: FDE als best practice vs. schaalbaarheidsgrens**
De explosieve groei van FDE-vacatures (+800% in 2025) suggereert breed draagvlak, terwijl SVPG waarschuwt dat het model productstrategie kan ondermijnen. BB_02 moet dit spanningsveld expliciteren: wanneer is FDE-achtige embedded iteratie de juiste aanpak?

**Tegenstrijdigheid 3: prototype als gespreksanker vs. schijn-zekerheid**
Tools als Lovable en Bolt verlagen de drempel voor concrete UI-demo's significant, maar creëren daarmee ook het risico dat klanten de gereedheid overschatten. Beide zijn waar tegelijkertijd.

## Open vragen

- **Concrete IDEO of Google design-thinking templates voor AI-discovery** zijn niet gevonden als gepubliceerde, openbare bron. Anthropic's eigen client-discovery-template bestaat niet als openbaar document. De 10 blueprint-elementen hierboven zijn gesynthetiseerd uit meerdere bronnen maar niet ontleend aan één gepubliceerde template.
- **OWASP Agentic AI Top-10 (late 2025)** — vermeld in zoekresultaat maar directe URL niet geverifieerd. Relevantie voor BB_02 is hoog wanneer het gaat om agentic systemen.
- **Stanford Enterprise AI Playbook (51 cases)** — PDF was niet tekstueel leesbaar via fetch. De bevindingen zijn via zoekresultaat-samenvatting beschikbaar maar niet direct geverifieerd uit de primaire tekst.

---

## Sources (werklijst voor verificatie)

1. Kozyrkov — AI-First Leadership (INFORMS) — https://pubsonline.informs.org/do/10.1287/LYTX.2025.02.02n/full/
2. Acceldata — Kozyrkov on What AI Means for Leadership — https://www.acceldata.io/blog/cassie-kozyrkov-on-what-it-really-means-to-be-ai-first-key-takeaways-for-enterprise-leaders
3. Inference by Sequoia — Karpathy's Software 3.0 — https://inferencebysequoia.substack.com/p/andrej-karpathys-software-30-and
4. Medium (Pouladian) — Karpathy Software 3.0 — https://medium.com/@ben_pouladian/andrej-karpathy-on-software-3-0-software-in-the-age-of-ai-b25533da93b6
5. Fortune — MIT 95% AI Pilot Failure — https://fortune.com/2025/08/18/mit-report-95-percent-generative-ai-pilots-at-companies-failing-cfo/
6. Marketing AI Institute — Kritiek MIT-studie — https://www.marketingaiinstitute.com/blog/mit-study-ai-pilots
7. Microsoft AI Decision Framework — https://github.com/microsoft/Microsoft-AI-Decision-Framework
8. Towards Data Science — AI-3P Assessment Framework — https://towardsdatascience.com/the-ai-3p-assessment-framework/
9. Anthropic — Building Effective Agents — https://www.anthropic.com/research/building-effective-agents
10. Anthropic Resources — Building Effective AI Agents — https://resources.anthropic.com/building-effective-agents
11. Anthropic Engineering — Multi-agent research system — https://www.anthropic.com/engineering/multi-agent-research-system
12. Anthropic — Introducing MCP — https://www.anthropic.com/news/model-context-protocol
13. Orq.ai — RAG Architecture 2026 — https://orq.ai/blog/rag-architecture
14. Techment — RAG vs Fine-Tuning vs AI Agents — https://www.techment.com/blogs/rag-vs-fine-tuning-vs-ai-agents-llm-strategy/
15. EU AI Act — High-Level Summary — https://artificialintelligenceact.eu/high-level-summary/
16. European Commission — HLEG Ethics Guidelines — https://digital-strategy.ec.europa.eu/en/library/ethics-guidelines-trustworthy-ai
17. ALTAI — Assessment List for Trustworthy AI — https://altai.insight-centre.org/
18. ICO — Accountability and governance implications of AI — https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/artificial-intelligence/guidance-on-ai-and-data-protection/what-are-the-accountability-and-governance-implications-of-ai/
19. TechGDPR — AI Act and GDPR study — https://techgdpr.com/blog/data-protection-digest-03112025-new-ai-act-and-gdpr-study-personal-data-stored-on-blockchain/
20. OWASP — Top 10 for LLM Applications 2025 — https://genai.owasp.org/resource/owasp-top-10-for-llm-applications-2025/
21. Pragmatic Engineer — Forward Deployed Engineers — https://newsletter.pragmaticengineer.com/p/forward-deployed-engineers
22. SSO Network — Forward Deployed Engineers Guide — https://www.ssonetwork.com/intelligent-automation/columns/forward-deployed-engineers-guide
23. NxCode — Vibe Design Tools 2026 — https://www.nxcode.io/resources/news/vibe-design-tools-compared-stitch-v0-lovable-2026
24. NxCode — Google Stitch vs v0 vs Lovable 2026 — https://www.nxcode.io/resources/news/google-stitch-vs-v0-vs-lovable-ai-app-builder-2026
25. Lenny's Newsletter — AI Prototyping for Product Managers — https://www.lennysnewsletter.com/p/a-guide-to-ai-prototyping-for-product
26. WorkOS — Enterprise AI Agent Playbook — https://workos.com/blog/enterprise-ai-agent-playbook-what-anthropic-and-openai-reveal-about-building-production-ready-systems
