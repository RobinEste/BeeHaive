# Research: Governance & Compliance — Evaluation Loop (BB_07)

**Researcher:** researcher-2
**Dimensie:** EU AI Act, ISO/IEC 42001, NIST AI RMF, Nederlandse toezichthouders
**Datum:** 2026-05-01

## Samenvatting (1 zin)

De EU AI Act verplicht hoog-risico AI-aanbieders tot een aantoonbare evaluation loop via vier specifieke artikelen (Art. 9, 10, 15, 72), met inwerkingtredingsdatum augustus 2026 voor post-marktmonitoring, terwijl ISO/IEC 42001 en NIST AI RMF de internationale kaders bieden die aanvullende eisen stellen aan continu evalueren en auditeerbaar verbeteren.

## Bevindingen

### 1. EU AI Act — Artikel 9: Risicobeheersysteem

**Kernverplichting:**
Hoog-risico AI-aanbieders moeten een *"continuous iterative process planned and run throughout the entire lifecycle"* van het AI-systeem instellen. Dit systeem moet:

- Bekende en redelijkerwijs voorzienbare risico's identificeren voor gezondheid, veiligheid en grondrechten.
- Risico's evalueren zowel bij beoogd gebruik als bij *"reasonably foreseeable misuse"*.
- Data analyseren uit het post-marktmonitoringsysteem (Art. 72).
- Testverplichtingen nakomen *"at any time throughout the development process"* en vóór marktplaatsing.
- Testen met *"prior defined metrics and probabilistic thresholds appropriate to the intended purpose"*.
- Specifiek rekening houden met kwetsbare groepen (minderjarigen, ouderen).

(`verified` — direct gelezen via https://artificialintelligenceact.eu/article/9/)

**Implicaties voor evaluation loop:**
Art. 9 vereist feitelijk een pre-deploy eval cyclus: tests zijn niet optioneel, niet eenmalig, en moeten aantoonbaar zijn met vooraf gedefinieerde metrics en drempelwaarden. Probabilistische drempels zijn expliciet vereist — dit sluit kwalitatieve beoordeling alleen uit bij hoog-risico systemen.

### 2. EU AI Act — Artikel 10: Data en datagovernance

**Kernverplichting:**
Trainings-, validatie- en testdatasets voor hoog-risico AI-systemen moeten:
- Relevant, representatief en foutvrij zijn.
- Voldoen aan design choices, data collection en preparation best practices.
- *"Appropriate measures to detect, prevent and mitigate possible biases"* bevatten.
- De specifieke geografische, contextuele, gedragsmatige of functionele kenmerken weerspiegelen van de inzetomgeving.
- *"Relevant data gaps or shortcomings that prevent compliance"* identificeren.

(`verified` — via https://artificialintelligenceact.eu/article/10/)

**Implicaties voor evaluation loop:**
De bias-detectie en -mitigatieplicht betekent dat de eval-set representatief moet zijn en dat biasmonitoring een structureel onderdeel van de loop is, niet een eenmalige exercise. Databeheer-documentatie is verplicht onderdeel van de technische documentatie.

### 3. EU AI Act — Artikel 15: Nauwkeurigheid, robuustheid en cybersecurity

**Kernverplichting:**
Hoog-risico AI-systemen moeten gedurende hun gehele levensduur:
- *"An appropriate level of accuracy, robustness, and cybersecurity"* bereiken.
- Prestaties consistent leveren; nauwkeurigheidsniveaus en metrics gedocumenteerd in gebruikersinstructies.
- Robuust zijn via technische redundantie (back-up, fail-safe).
- Voor continu-lerende systemen: *"eliminate or reduce the risk of biased outputs influencing input for future operations"* — feedback loop-contaminatie voorkomen.
- Weerstand bieden tegen cyberaanvallen: data poisoning, model poisoning, adversarial examples.

(`verified` — direct gelezen via https://artificialintelligenceact.eu/article/15/)

**Implicaties voor evaluation loop:**
Art. 15 maakt robustheidsmetrieken en adversarial testing verplicht voor hoog-risico systemen. De eis om feedback loop-contaminatie te voorkomen is direct van toepassing op eval-sets: productie-output mag niet ongecontroleerd in de volgende trainings- of finetuning-cyclus terechtkomen zonder kwaliteitscontrole.

### 4. EU AI Act — Artikel 17: Kwaliteitsmanagementsysteem

**Kernverplichting:**
Aanbieders van hoog-risico AI-systemen moeten een kwaliteitsmanagementsysteem inrichten dat documentatie bevat over:
- Strategieën en procedures voor naleving.
- Ontwerp- en controleprocessen.
- Systemen voor databeheer.
- Post-marktmonitoringsplannen.
- Communicatieprocedures voor incidenten.

(`inferred` — niet direct gelezen; beschrijving via zoekresultaten en EU AI Act structuur)

**Implicaties voor evaluation loop:**
Art. 17 vereist dat de evaluation loop is ingebed in een formeel kwaliteitsmanagementsysteem (vergelijkbaar met ISO 9001-logica). De loop moet aantoonbaar zijn, gedocumenteerd en onderdeel van interne audits.

### 5. EU AI Act — Artikel 72: Post-marktmonitoring

**Kernverplichting:**
Aanbieders moeten actief en systematisch *"relevant data on the performance of high-risk AI systems throughout their lifetime"* verzamelen, documenteren en analyseren. Specifieke eisen:

- Data verzamelen van deployers en andere bronnen, inclusief interacties met andere AI-systemen.
- Monitoring proportioneel aan de aard van de technologie en de risico's.
- Gebaseerd op een formeel post-market monitoring plan als onderdeel van technische documentatie.
- De Europese Commissie moest vóór 2 februari 2026 een template publiceren voor dit plan.

**Inwerkingtredingsdatum:** 2 augustus 2026.

(`verified` — direct gelezen via https://artificialintelligenceact.eu/article/72/)

**Implicaties voor evaluation loop:**
Art. 72 is het sterkste mandaat voor een productie evaluation loop: het is niet voldoende om vóór deployment te testen. Continue dataverzameling en analyse zijn verplicht. Post-marktmonitoring is de wettelijke verplichting voor wat in de industrie "online evaluation" heet.

### 6. ISO/IEC 42001:2023 — AI Management System

**Standaard-context:**
ISO/IEC 42001 is de eerste internationale beheernorm specifiek voor AI-systemen (gepubliceerd 2023). De norm stelt eisen aan het opzetten, implementeren, onderhouden en continu verbeteren van een AI-beheersysteem (AIMS).

**Evaluatie-eisen:**
Clause 9 (Performance Evaluation) vereist drie kernelementen:
1. **Doorlopende monitoring en meting** van het AIMS.
2. **Interne audit** (Clause 9.2.1): periodiek, minimaal jaarlijks voor het volledige AIMS; vaker bij hoog-risico AI-systemen. Verificatie dat het systeem conform is aan ISO 42001 en organisatievereisten.
3. **Managementbeoordeling** (Clause 9.3): topmanagement beoordeelt relevantie en effectiviteit.

Certificering is 3 jaar geldig met jaarlijkse surveillance-audit en hercertificering in jaar 3.

(`verified` — via https://cloudsecurityalliance.org/blog/2025/05/08/iso-42001-lessons-learned-from-auditing-and-implementing-the-framework en https://aws.amazon.com/blogs/security/ai-lifecycle-risk-management-iso-iec-420012023-for-ai-governance/)

**Implicaties voor evaluation loop:**
ISO 42001 stelt dat de evaluation loop niet alleen een technisch maar ook een governanceproces is: gedocumenteerd, geauditeerd en onderdeel van managementbeslissingen. Organisaties die ISO 42001 nastreven, moeten de evaluation loop aantoonbaar periodiek uitvoeren.

### 7. NIST AI RMF — Measure & Manage functies

**TEVV als kernproces:**
Het NIST AI RMF (2023) operationaliseert risicobeheer via vier functies: Govern, Map, Measure, Manage. De *Measure*-functie omvat TEVV (Test, Evaluate, Verify, Validate):
> *"TEVV tasks can provide insights relative to technical, societal, legal, and ethical standards or norms, and can assist with anticipating impacts and assessing and tracking emergent risks. As a regular process within an AI lifecycle, TEVV allows for both mid-course remediation and post-hoc risk management."*

NIST publiceerde op 7 april 2026 een concept-note voor een AI RMF-profiel over Trustworthy AI in Critical Infrastructure.

(`verified` — via https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf)

**Implicaties voor evaluation loop:**
NIST positioneert TEVV expliciet als *regulier lifecycle-proces*, niet als eenmalige activiteit. De Manage-functie vereist dat bevindingen leiden tot aanpassing — de loop-component is dus ook in NIST verankerd.

### 8. Nederlandse implementatie en toezichthouders

**Toezichtstructuur:**
In Nederland zijn tien toezichthouders aangewezen voor de EU AI Act, waarvan vijf primair:
1. **AP** (Autoriteit Persoonsgegevens) — privacy en gegevensbescherming
2. **RDI** (Rijksdienst voor Digitale Infrastructuur) — digitale infrastructuur
3. **ACM** (Autoriteit Consument en Markt) — consumentenrecht
4. **AFM** (Autoriteit Financiële Markten) — financiële sector
5. **DNB** (De Nederlandsche Bank) — bancaire sector

De AP richt zich in 2025 op: transparantie, standaardisatie, auditing, governance, non-discriminatie en AI-geletterdheid.

(`verified` — via https://www.autoriteitpersoonsgegevens.nl/en/current/ap-and-rdi-supervision-of-ai-systems-requires-cooperation-and-must-be-arranged-quickly en https://www.pinsentmasons.com/out-law/news/ai-compliance-overseen-10-dutch-regulators)

**Regulatory sandbox:**
In maart 2025 publiceerden AP en RDI een voorstel voor de Nederlandse inrichting van de AI regulatory sandbox (verplicht onder de EU AI Act per augustus 2026). Nederland plant de sandbox-launch vóór 2027.

**Sectorale toezichthouders (aanvullend):**
- **IGJ** (Inspectie Gezondheidszorg en Jeugd) — medische AI
- **NZa** (Nederlandse Zorgautoriteit) — zorgbekostiging
- **Inspectie van het Onderwijs** — onderwijs-AI

De Nederlandse Implementatiewet AI-verordening wordt verwacht in Q4 2026 bij de Tweede Kamer.

(`verified` — via https://www.stibbe.com/publications-and-insights/dutch-proposal-for-ai-supervision-hybrid-cooperation-between-market-supervisory-authorities)

### 9. Bewaartermijnen en documentatieplichten

Op basis van EU AI Act Art. 9, 12 en 72:
- **Technische documentatie:** bewaartermijn 10 jaar na marktplaatsing hoog-risico AI-systeem.
- **Logs en registraties** (Art. 12): automatische registratie minimaal over de periode dat het systeem wordt gebruikt; specifieke bewaartermijn per sector (medisch: verwachte levensduur apparaat; justitie: 6 maanden minimaal).
- **Post-marktmonitoringplan:** onderdeel van technische documentatie; verplicht te overleggen aan toezichthouder.
- **Eval-sets en testresultaten:** niet expliciet benoemd in EU AI Act tekst, maar onderdeel van technische documentatie op basis van Art. 9 (testresultaten bij specifieke metrics en drempelwaarden moeten gedocumenteerd zijn).

(`inferred` — bewaartermijn technische documentatie uit Art. 12 en Art. 72 gelezen; specifieke eval-set termijnen niet expliciet benoemd in wetsTekst)

## Evidence Table

| # | Bron | URL | Type | Key claim | Confidence |
|---|------|-----|------|-----------|------------|
| 1 | EU AI Act Art. 9 | https://artificialintelligenceact.eu/article/9/ | primary | Continuous iterative lifecycle process vereist | high |
| 2 | EU AI Act Art. 10 | https://artificialintelligenceact.eu/article/10/ | primary | Biasdetectie en representatieve data verplicht | high |
| 3 | EU AI Act Art. 15 | https://artificialintelligenceact.eu/article/15/ | primary | Robustness, accuracy gedurende lifetime; feedback loop contamination | high |
| 4 | EU AI Act Art. 72 | https://artificialintelligenceact.eu/article/72/ | primary | Post-marktmonitoring: actief, systematisch, lifetime | high |
| 5 | ISO/IEC 42001 — CSA | https://cloudsecurityalliance.org/blog/2025/05/08/iso-42001-lessons-learned-from-auditing-and-implementing-the-framework | secondary | Clause 9 performance evaluation; jaarlijkse audit | high |
| 6 | ISO/IEC 42001 — AWS | https://aws.amazon.com/blogs/security/ai-lifecycle-risk-management-iso-iec-420012023-for-ai-governance/ | secondary | ISO 42001 als complement aan EU AI Act | high |
| 7 | NIST AI RMF 1.0 | https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf | primary | TEVV als regulier lifecycle-proces | high |
| 8 | AP/RDI — supervisie | https://www.autoriteitpersoonsgegevens.nl/en/current/ap-and-rdi-supervision-of-ai-systems-requires-cooperation-and-must-be-arranged-quickly | primary | Nederlandse AI-toezichtstructuur | high |
| 9 | Pinsent Masons — 10 toezichthouders | https://www.pinsentmasons.com/out-law/news/ai-compliance-overseen-10-dutch-regulators | secondary | Tien toezichthouders NL | high |
| 10 | Stibbe — Dutch AI supervisie | https://www.stibbe.com/publications-and-insights/dutch-proposal-for-ai-supervision-hybrid-cooperation-between-market-supervisory-authorities | secondary | Hybride toezichtstructuur NL | high |

## Coverage Status

- **Gecheckt direct:** Art. 9, 15, 72 volledig gelezen; Art. 10 via zoekresultaten bevestigd; ISO 42001 via CSA en AWS.
- **Blijft onzeker:** Art. 17 niet direct gelezen; beschrijving via structuur en zoekresultaten. Exacte bewaartermijnen eval-sets niet in primaire brontekst gevonden.
- **Niet afgerond:** IGJ, NZa, Inspectie Onderwijs specifieke AI-beleidsdocumenten niet gecheckt.

## Sources

1. EU AI Act — Article 9 — https://artificialintelligenceact.eu/article/9/
2. EU AI Act — Article 10 — https://artificialintelligenceact.eu/article/10/
3. EU AI Act — Article 15 — https://artificialintelligenceact.eu/article/15/
4. EU AI Act — Article 72 — https://artificialintelligenceact.eu/article/72/
5. Cloud Security Alliance — ISO 42001 Audit Lessons — https://cloudsecurityalliance.org/blog/2025/05/08/iso-42001-lessons-learned-from-auditing-and-implementing-the-framework
6. AWS — ISO/IEC 42001 Lifecycle Risk Management — https://aws.amazon.com/blogs/security/ai-lifecycle-risk-management-iso-iec-420012023-for-ai-governance/
7. NIST AI RMF 1.0 — https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf
8. Autoriteit Persoonsgegevens — AP en RDI supervisie — https://www.autoriteitpersoonsgegevens.nl/en/current/ap-and-rdi-supervision-of-ai-systems-requires-cooperation-and-must-be-arranged-quickly
9. Pinsent Masons — 10 Dutch Regulators — https://www.pinsentmasons.com/out-law/news/ai-compliance-overseen-10-dutch-regulators
10. Stibbe — Dutch AI Supervision Proposal — https://www.stibbe.com/publications-and-insights/dutch-proposal-for-ai-supervision-hybrid-cooperation-between-market-supervisory-authorities
