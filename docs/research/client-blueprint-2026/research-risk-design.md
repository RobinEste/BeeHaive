# Research: Risk-based Design & Guardrails-by-Design — BB_02 Client Blueprint

**Researcher:** researcher-risk
**Dimensie:** EU AI Act risico-tiers, HLEG Trustworthy AI, privacy-by-design, OWASP LLM Top-10 (2024-2026)
**Datum:** 2026-04-26

## Samenvatting (1 zin)

Effectief risico-gebaseerd AI-ontwerp vereist dat regulatoire classificatie (EU AI Act), ethische vereisten (HLEG/ALTAI) en technische beveiligingsrisico's (OWASP LLM Top-10) als ontwerpinput worden meegenomen vóórdat architectuurkeuzes worden gemaakt.

## Bevindingen

### 1. EU AI Act: vier risico-tiers als ontwerpinput

De EU AI Act (inwerking getreden 1 augustus 2024, meeste regels van toepassing vanaf 2 augustus 2026) hanteert een risico-gebaseerd kader [1, 2]:

**Tier 1 — Onaanvaardbaar risico (verboden):**
- Sociale scoringsystemen
- Manipulatieve AI die menselijke vrije wil ondermijnt
- Realtime gezichtsherkenning in openbare ruimtes (met beperkte uitzonderingen voor ordehandhaving)
- Emotieherkenning op de werkvloer

(`verified` via directe fetch EU AI Act high-level summary)

**Tier 2 — Hoog risico (zwaarste verplichtingen, design-fase-verplicht):**
Systemen die ernstig risico vormen voor gezondheid, veiligheid of fundamentele rechten. Categorieën (Annex III) [1]:
- Biometrie (remote identificatie, emotieherkenning, gevoelig attribuut-inferentie)
- Kritieke infrastructuur (veiligheidscomponenten in digitale, verkeers-, nutssystemen)
- Onderwijs (toelatingsbeslissingen, leerbeoordelingen, gedragsmonitoring)
- Werkgelegenheid (werving, promotie, prestatiebeoordeling)
- Essentiële diensten (uitkeringsrecht, kredietwaardigheid, noodoproep-dispatching)
- Ordehandhaving (crimineel risico, bewijsevaluatie, verdachtenprofiling)
- Migratie/grenscontrole (visumbeslissingen, irreguliere migratie-assessment)
- Rechtspraak (juridische interpretatie, verkiezingsinvloed-detectie)

(`verified` via directe fetch EU AI Act high-level summary)

**Tier 3 — Beperkt risico (transparantieverplichting):**
Ontwikkelaars moeten AI-gebruik onthullen aan eindgebruikers (chatbots, deepfakes).

**Tier 4 — Minimaal risico:**
Grotendeels ongereguleerd; inclusief de meeste huidige applicaties zoals spamfilters en video-game-AI.

### 2. Design-verplichtingen voor hoog-risico systemen

Providers van hoog-risico AI-systemen moeten implementeren [1]:
1. Risicomanagementsystemen gedurende de volledige productlevenscyclus
2. Datagovernance voor kwaliteit en representativiteit
3. Technische documentatie die compliance aantoont
4. Automatische event-logging voor incident tracking
5. Gebruikersinstructies die deployer-compliance mogelijk maken
6. Human oversight-mogelijkheden
7. Nauwkeurigheids-, robuustheids- en cybersecurity-standaarden
8. Kwaliteitsmanagementsystemen

**Blueprint-implicatie:** voor hoog-risico toepassingen moeten deze 8 verplichtingen als checklist-items in het BB_02-blueprint staan, bij voorkeur als "ontwerp-gates" vóór architectuurkeuzes.

### 3. HLEG Trustworthy AI: 7 vereisten als blueprint-checks

De Europese High-Level Expert Group on AI (HLEG) publiceerde de Ethics Guidelines for Trustworthy AI (2019/2020) — nog steeds de leidende referentie voor ethisch AI-ontwerp [3]. De 7 vereisten:

1. **Human Agency and Oversight** — AI moet menselijke controle ondersteunen
2. **Technical Robustness and Safety** — betrouwbaar en veilig functioneren
3. **Privacy and Data Governance** — bescherming van persoonsgegevens
4. **Transparency** — uitlegbaarheid van beslissingen
5. **Diversity, Non-discrimination and Fairness** — geen onrechtvaardige bias
6. **Societal and Environmental Well-being** — maatschappelijke impact
7. **Accountability** — verantwoordelijkheidsmechanismen

(`verified` via zoekresultaat met directe Europese Commissie-bron [3])

**ALTAI-checklist:** de Assessment List for Trustworthy AI (ALTAI, HLEG 2020) vertaalt deze 7 vereisten naar een praktische zelfbeoordelingschecklist voor ontwikkelaars en deployers [4]. Beschikbaar als interactieve webversie op altai.insight-centre.org.

**Blueprint-implicatie voor BB_02:** de ALTAI-checklist is een bewezen instrument dat direct inzetbaar is als onderdeel van het blueprint-gesprek. Elke van de 7 vereisten genereert concrete ontwerpvragen die vroeg in het proces gesteld moeten worden.

### 4. Privacy-by-design en DPIA voor AI-systemen

Privacy-by-design (PbD) is een GDPR-verplichting voor risicovolle verwerkingen. Voor AI-systemen is een Data Protection Impact Assessment (DPIA) in de meeste gevallen verplicht [5]:

"In de overgrote meerderheid van gevallen zal het gebruik van AI een type verwerking betreffen dat waarschijnlijk een hoog risico inhoudt voor de rechten en vrijheden van individuen, en daarmee de wettelijke verplichting tot het uitvoeren van een DPIA triggeren." [5] (`verified` via ICO-bron en GDPR Local)

**Samenloop EU AI Act en DPIA:** de EU AI Act introduceert Fundamental Rights Impact Assessments (FRIA's) voor hoog-risico-AI, die vaak overlappen met GDPR-DPIA's maar een andere scope, toezichthouder en procedurele vereisten hebben. Dit creëert dubbeling en onzekerheid [6]. (`verified` via TechGDPR-artikel)

**Blueprint-vragen voor privacy-by-design:**
- Welke persoonsgegevens worden verwerkt, voor welk doel?
- Is er een rechtsgronding (toestemming, gerechtvaardigde belang, contractnoodzaak)?
- Is een DPIA vereist? (default: ja, tenzij aantoonbaar niet van toepassing)
- Hoe wordt minimale gegevensverwerking gewaarborgd (data minimization)?
- Welke rechten van betrokkenen zijn van toepassing (inzage, bezwaar, uitleg bij geautomatiseerde beslissingen)?

### 5. OWASP LLM Top-10 2025: threaten-modelling voor AI-systemen

OWASP publiceerde in 2024/2025 een bijgewerkte Top-10 voor LLM-applicaties [7, 8]. De meest relevante voor blueprint-fase:

**LLM01 — Prompt Injection:** aanvallen waarbij kwaadaardige input het model ertoe brengt zijn instructies te negeren. Mitigatie: input/output-filtering, privilege-scheiding. (`verified`)

**LLM02 — Insecure Output Handling:** niet-gevalideerde LLM-output die downstream schade veroorzaakt. Mitigatie: output-validatie met deterministische code.

**LLM06 — Sensitive Information Disclosure:** het lekken van PII of vertrouwelijke data via modeloutput. Mitigatie: data-governance, output-screening.

**LLM08 — Vector and Embedding Weaknesses (nieuw 2025):** kwetsbaarheden in RAG-systemen en vector databases. (`verified`)

**LLM09 — System Prompt Leakage (nieuw 2025):** blootstelling van interne systeem-prompts met gevoelige instructies, credentials of operationele logica. (`verified`)

**Agentic AI Top-10 (OWASP late 2025):** OWASP publiceerde een aparte Top-10 specifiek voor agentic AI-systemen waar LLMs autonoom plannen, beslissen en multi-step taken uitvoeren met externe tools. [7] (`inferred` — vermeld in zoekresultaat, directe URL niet geverifieerd)

**Blueprint-implicatie voor BB_02:** threat modeling op basis van de OWASP LLM Top-10 is een standaard onderdeel van de risk-check in de blueprint-fase. Voor agentic systemen: ook de agentic OWASP-lijst.

### 6. Guardrails-by-design: verdediging in de diepte

Effectieve guardrails zijn gelaagd [7, 9]:
- **Input-filtering:** kwaadaardige of out-of-scope inputs blokkeren vóór verwerking
- **Gedragsconstrainering:** strikte rol-instructies, taakbeperking, instructie-override-resistentie
- **Output-validatie:** output-requirements specificeren, formaat-validatie met deterministische code
- **Privilege-scheiding:** agents krijgen minimale noodzakelijke rechten (principle of least privilege)
- **Monitoring en logging:** alle agent-acties loggen voor incident-response

**Architectuurprincipe:** guardrails zijn geen afterthought maar ontwerpparameter — ze beïnvloeden architectuurkeuzes (bijv. sandboxing, human-in-the-loop triggers, rollback-mechanismen).

## Evidence Table

| # | Bron | URL | Type | Key claim | Confidence |
|---|------|-----|------|-----------|------------|
| 1 | EU AI Act — High-Level Summary | https://artificialintelligenceact.eu/high-level-summary/ | primary | Vier risico-tiers, Annex III categorieën, design-verplichtingen | high |
| 2 | Trail ML — EU AI Act Risk Classifications | https://www.trail-ml.com/blog/eu-ai-act-how-risk-is-classified | secondary | Risico-tiers toelichting | medium |
| 3 | European Commission — Ethics Guidelines for Trustworthy AI | https://digital-strategy.ec.europa.eu/en/library/ethics-guidelines-trustworthy-ai | primary | HLEG 7 vereisten | high |
| 4 | ALTAI — Assessment List for Trustworthy AI | https://altai.insight-centre.org/ | primary | HLEG zelfbeoordelingschecklist | high |
| 5 | ICO — Accountability and governance implications of AI | https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/artificial-intelligence/guidance-on-ai-and-data-protection/what-are-the-accountability-and-governance-implications-of-ai/ | primary | DPIA-verplichting voor AI | high |
| 6 | TechGDPR — Data protection digest: AI Act and GDPR study | https://techgdpr.com/blog/data-protection-digest-03112025-new-ai-act-and-gdpr-study-personal-data-stored-on-blockchain/ | secondary | FRIA vs DPIA overlap en dubbeling | medium |
| 7 | OWASP — Top 10 for LLM Applications 2025 | https://genai.owasp.org/resource/owasp-top-10-for-llm-applications-2025/ | primary | LLM Top-10 2025, nieuwe entries Vector/System Prompt | high |
| 8 | OWASP — LLM Top-10 website | https://genai.owasp.org/llm-top-10/ | primary | OWASP LLM project overzicht | high |
| 9 | Getmaxim.ai — Complete AI Guardrails Implementation Guide 2026 | https://www.getmaxim.ai/articles/the-complete-ai-guardrails-implementation-guide-for-2026/ | secondary | Guardrails implementatie, verdediging in de diepte | medium |

## Coverage Status

- **Gecheckt direct:** EU AI Act high-level summary (directe fetch), OWASP LLM Top-10 2025 (via zoekresultaat met directe URL)
- **Blijft onzeker:** OWASP Agentic AI Top-10 (late 2025, vermeld maar directe URL niet geverifieerd); HLEG ALTAI interactieve tool niet zelf gebruikt
- **Niet afgerond:** GDPR Local DPIA-gids niet direct gefetcht; directe EU AI Act artikel 6 niet gelezen (high-level summary voldoende voor blueprint-niveau)

## Sources

1. EU AI Act — High-Level Summary — https://artificialintelligenceact.eu/high-level-summary/
2. Trail ML — EU AI Act: How Risk Is Classified — https://www.trail-ml.com/blog/eu-ai-act-how-risk-is-classified
3. European Commission — Ethics Guidelines for Trustworthy AI (HLEG) — https://digital-strategy.ec.europa.eu/en/library/ethics-guidelines-trustworthy-ai
4. ALTAI — Assessment List for Trustworthy AI — https://altai.insight-centre.org/
5. ICO — Accountability and governance implications of AI (GDPR guidance) — https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/artificial-intelligence/guidance-on-ai-and-data-protection/what-are-the-accountability-and-governance-implications-of-ai/
6. TechGDPR — Data protection digest: AI Act and GDPR (nov 2025) — https://techgdpr.com/blog/data-protection-digest-03112025-new-ai-act-and-gdpr-study-personal-data-stored-on-blockchain/
7. OWASP — Top 10 for LLM Applications 2025 — https://genai.owasp.org/resource/owasp-top-10-for-llm-applications-2025/
8. OWASP — LLM Top-10 Archive — https://genai.owasp.org/llm-top-10/
9. Getmaxim.ai — The Complete AI Guardrails Implementation Guide for 2026 — https://www.getmaxim.ai/articles/the-complete-ai-guardrails-implementation-guide-for-2026/
10. GDPR Local — Conducting a DPIA: Best Practices for AI Systems — https://gdprlocal.com/conducting-a-dpia-best-practices-for-ai-systems/
