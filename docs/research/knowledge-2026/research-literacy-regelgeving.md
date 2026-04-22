# Research: AI-Literacy & Regelgeving — BB_01 Knowledge

**Researcher:** lead agent (Lane 1)
**Dimensie:** EU AI Act Art. 4 handhaving, OECD AI Literacy Frameworks, internationale regelgevingstrends
**Datum:** 2026-04-22

## Samenvatting (1 zin)

EU AI Act Art. 4 verplicht "passende AI-geletterdheid" voor iedereen die AI-systemen inzet, maar de definitie is bewust open gelaten en handhaving staat in 2026 nog in de opstartfase — terwijl OECD en Europese Commissie een gezamenlijk literacy-framework bouwen dat drie dimensies onderscheidt (kennis/vaardigheden, attitudes/waarden, cross-vak-integratie).

## Bevindingen

### EU AI Act Art. 4 — tekst en reikwijdte

EU AI Act Art. 4 draagt providers en deployers op te zorgen dat personeel dat met AI-systemen werkt "een voldoende mate van AI-geletterdheid" bezit, "rekening houdend met hun technische kennis, ervaring, opleiding en training, en de context waarin de AI-systemen worden gebruikt" (`verified` via bron-103 [1]).

Kernimplicaties voor organisaties:
- De verplichting geldt voor **iedereen die AI-systemen inzet** — niet alleen AI-engineers. Dit omvat eindgebruikers, producteigenaren, juridische teams, QA (`verified` [1]).
- "Passende geletterdheid" is contextueel gedefinieerd: een callcenter-medewerker die een AI-gestuurde chatbot gebruikt heeft andere geletterdheidsverplichtingen dan een ML-engineer die het systeem ontwerpt.
- De **maatstaf** die bron-103 aanreikt: "Als een team niet kan uitleggen waarom een systeem laag-risico, transparantie-only of hoog-risico is, is het waarschijnlijk niet klaar om het te lanceren" (`inferred` — bron-103 interpreteert de wet, niet de wetgever zelf [1]).

Praktische vertaling naar trainingsontwerp (bron-103 [1]):
1. Rol-specifieke leerdoelen: engineers → documentatie; PM → use case classificatie; Legal → escalatie
2. Competentie-gebaseerde leerresultaten, niet abstracte wettekst
3. Interactieve formats: scenario walkthroughs, mock audits, red-team reviews
4. Meetsignalen: herhaalde vragen over risicoklasse, trage classificaties, audit-bevindingen

**Handhavingsstatus 2026:** De EU AI Act trad gefaseerd in werking; hoog-risico systemen vallen onder volledige verplichting; de handhavingscapaciteit van nationale markttoezichthouders is in opbouw (`inferred` — bron-103 dateert van april 2026 en beschrijft training als urgent maar suggereert geen handhavingsboetes in de praktijk [1]).

### OECD AI Literacy Framework (2025-2026)

OECD en Europese Commissie ontwikkelen samen een AI Literacy Framework voor primair en voortgezet onderwijs (`verified` [2]). Conceptversie gepubliceerd mei 2025; definitieve versie verwacht 2026.

Drie dimensies:
1. **Kennis en vaardigheden** — begrijpen hoe AI werkt, hoe tools te gebruiken, hoe te co-creëren
2. **Attitudes en waarden** — kritisch denken, ethische reflectie, verantwoordelijk gebruik
3. **Cross-vak integratie** — AI-begrip verweven in wiskunde, geschiedenis, informatica, sociale wetenschappen

Kernpunt: "Meer dan technische know-how" — het framework omvat kritisch denken, creativiteit en ethische implicaties (`verified` [2]).

Directe relevantie voor BB_01: de drie OECD-dimensies corresponderen met de bouwsteen-structuur van BB_01 (kennis → vaardigheden → attitude). De nadruk op cross-vak integratie suggereert dat AI-geletterdheid niet als apart vak/cursus kan worden afgedaan.

### OECD Skills Outlook 2025 — AI-geletterdheid op de arbeidsmarkt

Op basis van PIAAC Cycle 2-data (2023, n=landen×duizenden deelnemers) (`verified` [3]):

- De **overgrote meerderheid** van werknemers die aan AI worden blootgesteld heeft geen gespecialiseerde AI-vaardigheden nodig — slechts **algemeen begrip van AI**
- **Adaptief probleemoplossen** is de nieuwe kernvaardigheid (derde naast geletterdheid en gecijferdheid): vereist metacognitie, flexibiliteit en resource-selectie
- Metacognitie wordt expliciet beschreven als "precisely the metacognitive skills that AI struggles to replicate" (`verified` [3])
- **Training reproduceert ongelijkheid**: mensen uit achtergestelde milieus krijgen training gericht op machinebediening; bevoorrechte groepen krijgen projectmanagement en organisatievaardigheden

Implicatie voor BB_01: AI-geletterdheid als organisatiediscipline moet differentiëren naar rol en context (in lijn met Art. 4), maar het basisniveau (metacognitie, probleemoplossing) is universeel.

### Workday/Hanover Research — medewerkerperspectieven (2025)

Survey onder 2.500 werknemers in 22 landen (`verified` [4]):
- 83% gelooft dat AI het belang van uniek menselijke vaardigheden verhoogt
- 81% erkent dat AI de vereiste vaardigheden verandert
- 93% van actieve AI-gebruikers zegt AI hen in staat stelt zich te richten op strategisch werk
- **Kloof**: 82% van medewerkers gelooft dat behoefte aan menselijke interactie intensiveert; slechts 65% van managers deelt die overtuiging

Meest waardevolle en minst vervangbare vaardigheden: ethisch besluitvormen, relatieopbouw, emotionele intelligentie, conflictresolutie (`verified` [4]).

### Internationale regelgevingstrends

EU HLEG "Ethische Richtsnoeren voor Betrouwbare KI" (2019) definiëren 7 vereisten voor betrouwbare KI (`verified` [5]): menselijke controle, technische robuustheid, privacy, transparantie, non-discriminatie, welzijn, verantwoordingsplicht. Dit document is de feitelijke norm achter EU AI Act en de BeeHaive guardrails.

Kernprincipe dat direct naar BB_01 vertaalt: "Bij betrouwbare KI gaat het niet om het afvinken van elementen op een lijst, maar om het voortdurend vaststellen en verwezenlijken van vereisten" — wat impliceert dat AI-geletterdheid een continu leerproces is, geen eenmalige training (`verified` [5]).

## Evidence Table

| # | Bron | URL | Type | Key claim | Confidence |
|---|------|-----|------|-----------|------------|
| 1 | ITU Online — EU AI Act Compliance Training | https://www.ituonline.com/blogs/practical-strategies-for-training-your-ai-team-on-eu-ai-act-compliance-requirements/ | secondary | Rol-specifieke training, maatstaf voor AI-geletterdheid | high |
| 2 | OECD/EC — AI Literacy Framework 2025 | https://oecdedutoday.com/new-ai-literacy-framework-to-equip-youth-in-an-age-of-ai/ | primary (institutional) | 3 dimensies AI-literacy, cross-vak integratie | high |
| 3 | OECD Skills Outlook 2025 | https://www.oecd.org/en/publications/2025/12/oecd-skills-outlook-2025_ac37c7d4.html | primary (institutional) | Adaptief probleemoplossen als kernvaardigheid, metacognitie | high |
| 4 | Workday/Hanover Research 2025 | https://www.prnewswire.com/news-releases/new-global-research-from-workday-reveals-ai-will-ignite-a-human-skills-revolution-302349887.html | secondary (self-reported) | 83% menselijke skills worden belangrijker, top-4 vaardigheden | medium (zelfrapportage) |
| 5 | EU HLEG Trustworthy AI Guidelines | https://ec.europa.eu/digital-single-market/en/high-level-expert-group-artificial-intelligence | primary | 7 vereisten betrouwbare KI, continueel proces | high |

## Coverage Status

- **Gecheckt direct:** bron-103, bron-039, bron-013, bron-019, bron-097 — alle volledig gelezen
- **Blijft onzeker:** exacte handhavingsboetes en -uitkomsten EU AI Act Art. 4 in 2026 — geen concrete casuïstiek gevonden in de bronnen
- **Niet afgerond:** directe URL-verificatie van Art. 4 wettekst via eur-lex.europa.eu (niet opgezocht; bron-103 samenvatting als proxy gebruikt)

## Sources

1. ITU Online — "EU AI Act Compliance Training For AI Teams" — https://www.ituonline.com/blogs/practical-strategies-for-training-your-ai-team-on-eu-ai-act-compliance-requirements/
2. OECD Education Today — "New AI Literacy Framework to Equip Youth in an Age of AI" — https://oecdedutoday.com/new-ai-literacy-framework-to-equip-youth-in-an-age-of-ai/
3. OECD — "OECD Skills Outlook 2025: Building the Skills of the 21st Century for All" — https://www.oecd.org/en/publications/2025/12/oecd-skills-outlook-2025_ac37c7d4.html
4. Workday/Hanover Research — "Elevating Human Potential: The AI Skills Revolution" — https://www.prnewswire.com/news-releases/new-global-research-from-workday-reveals-ai-will-ignite-a-human-skills-revolution-302349887.html
5. EU HLEG — "Ethische Richtsnoeren voor Betrouwbare KI" — https://ec.europa.eu/digital-single-market/en/high-level-expert-group-artificial-intelligence
