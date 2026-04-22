# BB_01 Knowledge — AI-Geletterdheid als Organisatorische Discipline (2024-2026)

**Onderwerp:** Wat is de stand van AI-geletterdheid als organisatorische discipline, en welke patronen moet BB_01 dekken om elk checklist-item praktisch bruikbaar te maken?
**Datum:** 2026-04-22
**Researcher-rondes:** 1

---

## Executive Summary

AI-geletterdheid is in 2026 niet meer alleen een technische vaardigheid maar een organisatorische discipline met juridische, cognitieve en culturele dimensies. Drie convergerende signalen definiëren het speelveld:

**Rechtens verplicht:** EU AI Act Art. 4 verplicht "passende AI-geletterdheid" voor iedereen die AI-systemen inzet — niet alleen engineers, maar ook eindgebruikers, productmanagers en juridische teams. De definitie is bewust contextgebaseerd: de vereiste geletterdheid verschilt per rol, risicoclassificatie en toepassingsdomein [1].

**Empirisch urgenter dan gedacht:** De deskilling-paradox is in 2025 klinisch bewezen. Een Lancet-studie toonde dat ervaren endoscopisten na drie maanden AI-gebruik hun adenoom-detectiepercentage zagen dalen van 28.4% naar 22.4% bij procedures zónder AI — een absolute daling van 6 procentpunten [2]. Tegelijk verwerpt ~80% van de medewerkers actief AI-tools, gedreven door FOBO (Fear of Becoming Obsolete) eerder dan door technisch falen [3].

**Structureel onopgelost:** 95% van genAI-implementaties levert geen positieve ROI [4]. Niet door modelkwaliteit — maar door het ontbreken van governance, workflow-herontwerp en een leercultuur die individuele tool-productiviteit omzet in institutionele waardecreatie. Sivulka's elektriciteitsparallel treft doel: fabrieken in de jaren 1890 installeerden al elektromotoren zonder productiviteitswinst; pas na volledige herontwerp van de productielijn (1920s) kwam de waarde [5].

BB_01 Knowledge moet deze drie lagen adresseren: de regelgevingseis, de cognitieve bescherming, en de organisatorische transitie.

---

## 1. EU AI Act Art. 4 — Wat "passende geletterdheid" betekent

### De wettekst en reikwijdte

Art. 4 EU AI Act draagt providers en deployers op te zorgen dat personeel dat met AI-systemen werkt "een voldoende mate van AI-geletterdheid" bezit, "rekening houdend met hun technische kennis, ervaring, opleiding en training, en de context waarin de AI-systemen worden gebruikt" [1] (`verified`).

Drie operationele implicaties:

**1. Reikwijdte is breder dan IT.** De verplichting geldt voor iedereen die AI inzet — van callcenter-medewerker tot productmanager. Rol-specifieke trainingen zijn geen luxe maar juridische vereiste [1] (`verified`).

**2. Contextualiteit is de kern.** "Passende geletterdheid" voor een engineer verschilt fundamenteel van die voor een juridisch medewerker. De maatstaf: "Als een team niet kan uitleggen waarom een systeem laag-risico, transparantie-only of hoog-risico is, is het waarschijnlijk niet klaar om het te lanceren" [1] (`verified`).

**3. Handhaving is in opbouw.** In 2026 staat de handhavingscapaciteit van nationale markttoezichthouders nog in de opstartfase. Dit betekent niet dat compliance vrijblijvend is — hoog-risico AI-systemen vallen al onder volledige verplichtingen [1] (`inferred` — bron-103 beschrijft urgentie zonder concrete handhavingsboetes te noemen).

### Wat "goede training" inhoudt versus "slechte training"

> "Good training feels like engineering support. Bad training feels like someone reading a regulation at you." [1] (`verified`)

Werkende patronen per ITU Online [1] (`verified`):
- Rol-specifieke leerdoelen (engineers → documentatie; PM → use case classificatie; Legal → escalatie)
- Interactieve formats: scenario walkthroughs, tabletop exercises, mock audits, red-team reviews
- Meetsignalen: herhaalde vragen over risicoklasse, trage classificaties, audit-bevindingen

### BB_01 checklist-items die hieruit volgen

- [ ] Is de risicoclassificatie (laag/transparantie/hoog) van elk AI-systeem vastgelegd en kan elk teamlid dit uitleggen?
- [ ] Heeft elke rol een specifiek leerresultaat gedefinieerd voor AI Act compliance (niet generieke training)?
- [ ] Is er een update-mechanisme als het AI-systeem verandert of de regelgeving bijgesteld wordt?

---

## 2. Decision Intelligence — Oordeelsvermogen als kerncompetentie

### Kozyrkov's paradox: de meest waardevolle skill is het minst verbeterd

Cassie Kozyrkov (Decision Intelligence Substack, feb 2026) stelt dat het knelpunt in het AI-tijdperk verschuift van technische uitvoering naar menselijk oordeelsvermogen [6] (`verified`):

> "Judgment is the one area in which we've received the fewest upgrades since pen-and-paper improved our memory capacity." [6] (`verified`)

AI is een "thoughtlessness enabler": het versterkt zowel goed als slecht oordeelsvermogen. Een vaardige beslisser met AI wordt exceptioneel; een onvaardige beslisser met AI maakt grotere fouten sneller. Dit maakt oordeelsvermogen niet minder maar juist meer kritiek.

**Twee kanten van AI-gebruik:**
- **Genie-kant** (technische uitvoering, prompts genereren) — wordt steeds vaker door AI zelf gedaan
- **Wens-kant** (weten welk probleem je wilt oplossen, voor wie, waarom) — het knelpunt verschuift hiernaar

Implicatie voor BB_01: organisaties moeten investeren in "wisher-side capabilities" — het vermogen om AI de juiste vragen te stellen, niet alleen het vermogen om AI te bedienen [6] (`verified`).

### Kahneman & Klein — wanneer is intuïtie betrouwbaar?

Kahneman en Klein (American Psychologist, 2009) identificeerden twee voorwaarden voor betrouwbare professionele intuïtie [7] (`verified`):

1. **High-validity environment** — stabiele, objectief identificeerbare cues die voorspellend zijn voor uitkomsten
2. **Adequate opportunity to learn** — voldoende oefening met snelle, consistente feedback

> "Subjective experience is not a reliable indicator of judgment accuracy." [7] (`verified`)

**Vertaling naar het AI-tijdperk** (`inferred` — logisch gevolg van Kahneman-Klein + Mollick deskilling [2, 7]):
AI verandert de geldigheidsomgeving: taken die vroeger stabiele feedback gaven worden deels overgenomen door AI, waardoor professionals hun intuïtie voor taakmoeilijkheid verliezen. Iemand die nooit zelf schrijft verliest het gevoel voor wanneer een AI-tekst goed of slecht is.

**Implicatie voor BB_01:** Expliciete feedback-loops ontwerpen voor AI-gebruik — zodat medewerkers kunnen kalibreren wanneer hun intuïtie betrouwbaar is en wanneer AI-output gecheckt moet worden.

### Expertise externaliseren — het operating agreement model

Chris Lema's "Four Levels of AI Work" [8] (`verified`) beschrijft een progressiemodel:

- **Level 1:** Van tool naar collaborator
- **Level 2:** Van wegwerpoutput naar compounding assets (skills, frameworks, memory)
- **Level 3:** Van ad-hoc naar operating agreements (wie beslist wat, waar is menselijk oordeel vereist)
- **Level 4:** Van interacties naar productie-architecturen

Het kritieke inzicht: de meeste organisaties blijven op Level 1. Level 3 — operating agreements — is de kern van expertise-externalisatie.

Een operating agreement bevat [8] (`verified`):
- **Decision authority**: Claude stelt voor, mensen beslissen op strategie, stem, doelgroep
- **Human-in-the-loop pause points**: expliciete stappen die menselijke input vereisen
- **Visible reasoning**: als AI beslissingen neemt, moet het denken zichtbaar zijn
- **Escalation triggers**: wanneer stopt AI en vraagt het om input?
- **Quality standards**: expliciete checklists — wat betekent "klaar"?

> "Define the operating agreement. Write it down. This is what separates people who use AI from people who work with AI." [8] (`verified`)

### BB_01 checklist-items die hieruit volgen

- [ ] Is voor elk AI-ondersteund werkproces gedefinieerd welk besluit het systeem ondersteunt of neemt?
- [ ] Is er een expliciete eigenaar aangewezen voor elk besluit dat AI-output raakt?
- [ ] Is het operating agreement (decision authority, escalation triggers, quality standards) schriftelijk vastgelegd?
- [ ] Worden medewerkers getraind in het onderscheiden van taken waar hun intuïtie betrouwbaar is versus waar AI-verificatie vereist is?

---

## 3. Centaur/Cyborg Patronen — Stand van Zaken in het Agents-Tijdperk

### Het empirisch fundament — BCG/P&G studies

Dell'Acqua et al. (2023) met 758 BCG-consultants documenteerden de "jagged technological frontier" [9] (`verified`):

- Binnen frontier: 12.2% meer taken, 25.1% sneller, 40% hogere kwaliteit
- Buiten frontier: AI-gebruikers 19 procentpunten minder nauwkeurig dan controlegroep
- Skill-nivellering: zwakste consultants +43% met AI

De frontier is onzichtbaar — je kunt hem alleen leren kennen door uitgebreide AI-gebruikservaring, niet door instructie. Dit is het kern-argument voor waarom AI-geletterdheid ervaringsopbouw vereist naast conceptuele kennis.

Dell'Acqua et al. (2025) met 776 P&G professionals [10] (`verified`):
- Individu + AI = team (2 personen) zonder AI (+0.37 SD kwaliteit)
- Team + AI = 3x vaker top-10% doorbraakoplossingen
- AI balanceert disciplinaire eenzijdigheid: R&D-medewerkers produceerden cross-functionelere oplossingen

### Houden centaur/cyborg stand in 2026?

**Ja, als individueel workflow-kader.** De twee patronen beschrijven nog steeds hoe individuen het beste met AI werken:

- **Centaur** (duidelijke taakscheiding): sterk bij taken buiten de frontier, houdt menselijke competentie actief
- **Cyborg** (diepe integratie): effectief voor taken volledig binnen de frontier

**Onvoldoende voor de organisatorische laag.** In het agents-tijdperk verschuift de kritieke competentie van taakniveau naar systeemniveau:

KPMG (jan 2026) onderscheidt vier agent-archetypes [11] (`verified`): Taskers, Automators, Collaborators, Orchestrators. De mens verschuift naar de orchestrator-rol — niet "ik doe deel A en AI doet deel B" maar "ik ontwerp het systeem dat bepaalt wie wat doet."

WEF (2026) identificeert als open macro-vraag: "Who is responsible for decisions made by AI? Accountability sinks, agentic identity, legal liability" [4] (`verified`).

McKinsey (april 2026): "As agentic AI takes on more execution work, companies must also decide which capabilities they will deliberately build and sustain internally." [12] (`verified`)

> "Hiring determines where human judgment sits in the organization. Capability building determines whether AI amplifies that judgment or bypasses it." [12] (`verified`)

### BB_01 checklist-items die hieruit volgen

- [ ] Kennen medewerkers de jagged frontier voor hun eigen werktaken — weten ze waar AI sterk is en waar menselijk oordeel essentieel is?
- [ ] Is er een forum of mechanisme om frontier-kennis collectief te delen en bij te werken?
- [ ] Is voor elk AI-agent-systeem vastgelegd: wie is de accountable orchestrator, wat zijn de escalatiecriteria, hoe werkt toezicht?
- [ ] Is de organisatie in staat institutionele frontier-kennis te behouden als seniore medewerkers vertrekken?

---

## 4. Deskilling-Paradox — Wanneer Versterkt AI Expertise, Wanneer Erodeert Het

### Klinisch bewijs — de Lancet-studie

Budzyń et al. (Lancet Gastroenterology & Hepatology, aug 2025) [2] (`verified`):
- 19 ervaren endoscopisten (elk >2.000 procedures), 4 Poolse klinieken
- Adenoom-detectie zonder AI: vóór AI-blootstelling 28.4%, ná AI-blootstelling 22.4%
- Absolute daling: 6 procentpunten (~21% relatief) in slechts 3 maanden

Dit is niet anekdotisch — het is de eerste klinische studie die een causale keten laat zien: AI-blootstelling → cognitieve offloading → vermindering van actieve diagnosevaardigheid.

Gerlich (Societies, jan 2025) [13] (`verified`, met voorbehoud voor methodologische beperkingen) vond in een survey-studie (n=666, VK) een correlatiecoëfficiënt van r=-0.68 tussen frequent AI-gebruik en kritische denkvaardigheden.

### Wanneer versterkt AI expertise?

Op basis van het corpus (`inferred` uit meerdere bronnen):

**AI versterkt expertise wanneer:**
- De frontier bekend is — de professional weet welke taken AI aankan en welke niet
- Human-in-the-loop bewust is ingebouwd — actieve supervisie, niet passief akkoord gaan
- Er expliciete oefening plaatsvindt zónder AI voor kritieke vaardigheden
- Feedback-loops intact zijn — professionals krijgen snel te horen wanneer hun oordeel afweek van de uitkomst

**AI erodeert expertise wanneer:**
- Autonomie van AI zo hoog is dat mensen stoppen met nadenken ("falling asleep at the wheel" [9])
- Feedback-signalen verdwijnen — de uitkomst wordt aan AI toegeschreven, niet aan menselijke input
- Organisaties skill-nivellering verwarren met expertise-behoud (schwakke consultants +43%, maar frontier-kennis van seniors verdwijnt)
- Cognitieve offloading sluipend optreedt zonder bewuste monitoring

**De deskilling-paradox samengevat:** AI-gebruik op de korte termijn verhoogt gemiddelde prestaties. Op de lange termijn, zonder actief tegenbeleid, erodeert het de expertisebasis die nodig is voor taken buiten de frontier én voor supervisie van AI-systemen zelf.

### BB_01 checklist-items die hieruit volgen

- [ ] Is er beleid voor het actief onderhouden van kritieke vaardigheden zónder AI, ook als AI die taak aankan?
- [ ] Zijn de vaardigheden die het meest kwetsbaar zijn voor deskilling geïdentificeerd per rol/domein?
- [ ] Is er een monitor-mechanisme om deskilling-signalen te detecteren (bijv. kwaliteitsdaling bij AI-vrije procedures)?
- [ ] Worden nieuwe medewerkers blootgesteld aan taken zonder AI voordat ze AI-assistentie krijgen (expertise-opbouw-eerste principe)?

---

## 5. Leercultuur en Organisatorische Adoptie

### Het adoptieparadox

Fortune/WalkMe/SAP (april 2026, n=3.750, 14 landen) [3] (`verified`):
- 80% van medewerkers vermijdt of verwerpt actief AI-tools
- Trust chasm: 9% medewerkers vertrouwt AI voor complexe beslissingen vs. 61% executives
- Motivatie: FOBO (Fear of Becoming Obsolete), niet technisch falen

McKinsey (jan 2025) [14] (`verified`):
- Slechts 1% van organisaties noemt zichzelf "mature" in AI-implementatie
- Grootste barrière is niet de medewerker (die is klaar) maar de leider (die stuurt niet snel genoeg)
- Bijna helft van medewerkers wil meer formele training

### De institutionele versus individuele kloof

Sivulka's elektriciteitsparallel [5] (`verified`) is het sterkste kader voor het onderscheid:

Individuele AI maakt medewerkers 10x productiever. Organisaties worden niet 10x waardevoller. De kloof zit in de institutionele laag: coördinatie, signaal-van-ruis-scheiding, objectiviteit, accountability, change management.

WEF (2026) [4] (`verified`) formuleert vier imperatieven voor succes:
1. AI-vluchtigheid organisatiebreed bouwen — AI als samenwerkingspartner, niet als tool
2. Carrièrepaden herontwerpen — non-lineaire paden, skills-based doorgroei, institutionele kennisoverdracht bewaren
3. Culturele dividenden meten — minder burn-out, sneller leren, meer engagement
4. Governance-infrastructuur vóór schaling — accountability, explainability, bias/fairness

### Werkende patronen voor een AI-leercultuur

Op basis van het corpus (`inferred` uit meerdere bronnen — geen RCT-bewijs; patronen gebaseerd op convergentie van praktijkgerichte bronnen):

1. **Rol-specifieke leerresultaten** — geen generieke AI-training, maar expliciete competentiedoelen per functie [1]
2. **Frontier-leren door gebruik** — de grens van AI-capaciteiten is alleen te kennen door uitgebreide praktijkervaring [9]
3. **Psychologische veiligheid** — FOBO adresseren voordat adoptie-training zinvol is [3, 14]
4. **Operating agreements expliciteren** — wie beslist wat, waar is menselijk oordeel vereist [8]
5. **Compounding assets bouwen** — skills, frameworks en memory die elke AI-sessie waardevoller maken [8]
6. **Actief competentieonderhoud** — bewust taken zónder AI oefenen voor cruciale vaardigheden [2, 9]
7. **Leiderschap als primaire enabler** — change management vanuit top, niet vanuit IT-afdeling [14]

### BB_01 checklist-items die hieruit volgen

- [ ] Is FOBO (angst voor veroudering) als adoptiebarrière geïdentificeerd en geadresseerd in het veranderplan?
- [ ] Zijn leidinggevenden getraind in het actief sturen van AI-adoptie (niet delegeren aan IT)?
- [ ] Is er een mechanisme om frontier-kennis collectief te bouwen en te delen (niet alleen individuele tool-vaardigheid)?
- [ ] Wordt de overgang van individuele AI-productiviteit naar institutionele waardecreatie expliciet begeleid?
- [ ] Zijn culturele dividenden (burn-out-reductie, leertempo, engagement) meetbaar gemaakt als aanvulling op ROI-metrics?

---

## 6. OECD-Kader — AI-Geletterdheid als Driedimensionale Competentie

OECD en Europese Commissie definiëren AI-geletterdheid langs drie dimensies [15] (`verified`):

1. **Kennis en vaardigheden** — begrijpen hoe AI werkt, gebruiken, co-creëren
2. **Attitudes en waarden** — kritisch denken, ethische reflectie, verantwoordelijk gebruik
3. **Cross-domein integratie** — AI-begrip niet als apart vak maar verweven in werkprocessen

OECD Skills Outlook 2025 identificeert **adaptief probleemoplossen** als nieuwe kernvaardigheid (naast geletterdheid en gecijferdheid): de combinatie van flexibiliteit, resource-selectie en metacognitie [16] (`verified`). Metacognitie wordt expliciet beschreven als "precisely the metacognitive skills that AI struggles to replicate."

**Implicatie voor BB_01:** De drie OECD-dimensies bieden een vaardigheidsstructuur voor BB_01-content. AI-geletterdheid als organisatiediscipline moet alle drie dimensies adresseren — niet alleen tool-vaardigheid.

---

## Tegenstrijdigheden en Open Vragen

**Tegenstrijdigheid 1: Skill-nivellering vs. expertise-erosie**
AI nivelleert vaardigheidsverschillen (zwakste consultants +43%), maar erodeert tegelijk de expertise van top-performers voor taken buiten de frontier. Op organisatieniveau: meer gemiddelde prestaties maar minder differentiërende topexpertise. BB_01 moet beide effecten benoemen en organisaties helpen kiezen welk niveau ze willen beschermen.

**Tegenstrijdigheid 2: Medewerkers zijn klaar, leiders zijn de bottleneck**
McKinsey: medewerkers gebruiken AI al 3x meer dan leiders denken. Tegelijk: Fortune/WalkMe: 80% verwerpt AI-tools actief. Dit is niet per se contradictoir (verschillende populaties, tijdsmomenten, sectoren) maar vraagt om nuancering in BB_01: adoptie-readiness is heterogeen, één-maat-past-allen werkt niet.

**Tegenstrijdigheid 3: ROI-claims**
WEF: 95% genAI-implementaties zonder positieve ROI. a16z: enterprises laten wél reële AI-inroads zien met duidelijke ROI. Beide kunnen waar zijn: het verschil ligt in het type use case, implementatieaanpak en maturiteitsniveau. BB_01 moet eerlijk zijn over wat bewezen is versus aspirationeel.

**Open vraag 1:** Wat is de empirische ROI van AI-training als geïsoleerde interventie? Er bestaat geen RCT die training-kwaliteit direct koppelt aan business-ROI. BB_01 kan dit eerlijk benoemen: training is noodzakelijk maar niet voldoende.

**Open vraag 2:** Hoe veranderen centaur/cyborg-patronen bij volledig autonome agents? De onderzoeksevidentie is nog dunner dan de onderzoeksevidentie voor de oorspronkelijke patronen.

**Open vraag 3:** Wat zijn de langetermijn-deskilling-effecten? De Lancet-studie mat slechts 3 maanden. Zijn effects reversibel? Onder welke condities?

---

## Sources (draft — te verifiëren in Stap 6)

1. ITU Online — EU AI Act Compliance Training — https://www.ituonline.com/blogs/practical-strategies-for-training-your-ai-team-on-eu-ai-act-compliance-requirements/
2. Budzyń et al. — Lancet 2025 — https://www.thelancet.com/journals/langas/article/PIIS2468-1253(25)00133-5/abstract
3. Fortune/WalkMe — White Collar Rebellion — https://fortune.com/2026/04/09/ai-backlash-quiet-quitting-fobo-obsolete-white-collar-rebellion/
4. WEF — AI at Work 2026 — (PDF bron-094)
5. Sivulka — Institutional AI vs Individual AI — https://www.a16z.news/p/institutional-ai-vs-individual-ai
6. Kozyrkov — Most Valuable Skill for AI Era — https://decision.substack.com/p/whats-the-most-valuable-skill-for
7. Kahneman & Klein — Conditions for Intuitive Expertise — https://pubmed.ncbi.nlm.nih.gov/19739881/
8. Lema — Four Levels of AI Work — (PDF bron-093)
9. Dell'Acqua et al. — Jagged Frontier BCG 2023 — https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4573321
10. Dell'Acqua et al. — Cybernetic Teammate P&G 2025 — https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5188231
11. KPMG — Agentic AI Untangled — https://kpmg.com/us/en/articles/2026/agentic-ai-untangled.html
12. McKinsey — Tech Workforce AI-First Era — https://www.mckinsey.com/capabilities/mckinsey-technology/our-insights/designing-an-end-to-end-technology-workforce-for-the-ai-first-era
13. Gerlich — AI Tools in Society — https://www.mdpi.com/2075-4698/15/1/6
14. McKinsey — Superagency in the Workplace — https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/superagency-in-the-workplace-empowering-people-to-unlock-ais-full-potential-at-work
15. OECD/EC — AI Literacy Framework — https://oecdedutoday.com/new-ai-literacy-framework-to-equip-youth-in-an-age-of-ai/
16. OECD — Skills Outlook 2025 — https://www.oecd.org/en/publications/2025/12/oecd-skills-outlook-2025_ac37c7d4.html
17. EU HLEG — Trustworthy AI Guidelines — https://ec.europa.eu/digital-single-market/en/high-level-expert-group-artificial-intelligence
18. Workday/Hanover Research — Elevating Human Potential — https://www.prnewswire.com/news-releases/new-global-research-from-workday-reveals-ai-will-ignite-a-human-skills-revolution-302349887.html
19. McKinsey — Building Foundations Agentic AI — https://www.mckinsey.com/capabilities/mckinsey-technology/our-insights/building-the-foundations-for-agentic-ai-at-scale
