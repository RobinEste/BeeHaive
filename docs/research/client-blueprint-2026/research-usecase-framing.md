# Research: Use Case-selectie & Probleem-framing — BB_02 Client Blueprint

**Researcher:** researcher-usecase
**Dimensie:** Use case-selectie, beslismodellen, AI-geschiktheid, probleem-framing (2024-2026)
**Datum:** 2026-04-26

## Samenvatting (1 zin)

Succesvolle AI-use-case-selectie begint met de beslisser—niet met het model—en vraagt om een expliciete geschiktheidscheck vóór committering, omdat de meerderheid van enterprise AI-pilots faalt door een mismatch tussen probleem en aanpak.

## Bevindingen

### 1. Decision-first: Kozyrkov's probleem-frame

Cassie Kozyrkov (voormalig Chief Decision Scientist Google, nu CEO van Kozyr) heeft het concept van *decision intelligence* gepopulariseerd als vertrekpunt voor AI-initiatieven [1]. De kern: begin niet met "welke AI kunnen we inzetten?" maar met "welke beslissingen zijn het waard om beter te nemen?" (`verified` — meerdere onafhankelijke samenvattingen van Kozyrkov's werk beschikbaar).

Kozyrkov stelt drie criteria voor de evaluatie van AI-systemen [1, 2]:
1. Identificeer het doel van het AI-systeem
2. Beoordeel de beschikbaarheid en kwaliteit van data
3. Valideer of het AI-systeem werkt zoals beoogd

De quote die haar positie samenvat: "The purpose is important, and the purpose comes from people." (`verified` via Acceldata-artikel dat haar keynote parafraseert [2]).

**Implicatie voor BB_02:** het blueprint-gesprek moet beginnen met de beslissing die verbeterd moet worden, niet met de technologie.

### 2. AI-first vs. AI-augmented: het verschil in vertrekpunt

"AI-first" betekent in Kozyrkov's definitie *niet* "AI voor alles" maar "bereid zijn het onmogelijke te heroverwegen" [1, 2]. Bedrijven die AI inzetten om "bij te blijven" begrijpen dit concept verkeerd. (`inferred` — Kozyrkov's eigen uitleg via meerdere artikelen consistent).

De onderscheiding:
- **AI-augmented:** bestaande processen versnellen/verbeteren met AI-assistentie
- **AI-first:** processen herdenken vanuit wat nu wél mogelijk is door AI

Beide zijn legitieme startpunten, maar vereisen een andere blueprint-benadering. Voor BB_02 is het expliciteren van dit onderscheid bij de klant een eerste stap.

### 3. Karpathy's Software 3.0: wat verandert er fundamenteel

Andrej Karpathy introduceerde het concept "Software 3.0" in een keynote op Y Combinator's AI Startup School op 19 juni 2025 [3]. De progressie:
- **Software 1.0:** expliciete instructies (code)
- **Software 2.0:** geleerde gewichten (neurale netwerken)
- **Software 3.0:** prompts in natuurlijke taal als broncode

De implicatie voor probleem-framing: in Software 3.0 zijn veel taken die eerder code vereisten nu te formuleren als een prompt + completie. Dit verandert de geschiktheidsvraag: niet "kan een algoritme dit?" maar "kan je de gewenste output beschrijven in taal?" (`verified` — keynote van Karpathy gedocumenteerd in meerdere bronnen [3, 4]).

Risico van dit frame: het kan leiden tot overschatting van AI-geschiktheid. Niet alles dat *beschrijfbaar* is in taal is ook *betrouwbaar uitvoerbaar* door een LLM. BB_02 moet dit onderscheid operationeel maken.

### 4. MIT-onderzoek: 95% faalpercentage — claim en nuance

Het MIT NANDA-initiatief publiceerde in augustus 2025 het rapport *The GenAI Divide: State of AI in Business 2025* [5]. De bevinding die viral ging: "95% van enterprise AI-pilots levert geen meetbaar P&L-resultaat."

**Methodologie:** 150 interviews met leidinggevenden, survey bij 350 medewerkers, analyse van 300 publieke AI-implementaties [5]. (`verified` via Fortune-artikel met directe rapportdetails)

**Nuance (kritiek):** Paul Roetzer van Marketing AI Institute bestempelt de 95%-claim als methodologisch onbetrouwbaar [6]:
- Succescriterium was eng gedefinieerd: deployment buiten pilotfase met meetbare KPI's én ROI binnen 6 maanden
- Efficiëntiewinsten, kostenbesparingen en klantretentie-verbeteringen werden genegeerd
- Slechts 52 interviews als grondslag voor de kwantitatieve claim
- Rapportagevertekening waarschijnlijk (bedrijven delen faalcijfers niet graag)

**Conclusie voor BB_02:** de 95%-claim is `inferred` als richtinggevend maar niet als harde statistiek. Wél valide: de onderliggende oorzaak — een mismatch tussen AI-inzet en bedrijfsprobleem — is consistent terug te vinden in meerdere onafhankelijke analyses. Het is de *reden* die telt, niet het exacte getal.

### 5. Concrete geschiktheidscriteria: wanneer wél, wanneer niet

Uit meerdere bronnen destilleerbaar is een praktische criteria-set voor geschiktheidscheck:

**AI is geschikt wanneer [7, 8]:**
- Het probleem is te complex voor deterministische regels (veel variabelen, edge cases)
- De gewenste output beschrijfbaar is maar niet volledig specificeerbaar in code
- Data beschikbaar en voldoende representatief is
- Foutmarge in output acceptabel is (geen zero-tolerance systemen tenzij human-in-loop)
- Het patroon in de data stabieler is dan de beslissingsregels die mensen nu hanteren

**AI is *niet* geschikt wanneer:**
- Een simpele BI-dashboard of regelgebaseerde automatisering voldoet
- De benodigde data niet bestaat of niet toegankelijk is
- Foutmarge nul moet zijn (levenskritische systemen zonder human oversight)
- Het doel niet kwantificeerbaar is ("betere beslissingen" zonder meetcriterium)

De AI-3P Assessment Framework (People-Process-Product) biedt een kwantitatief scoringsmodel [8]:
- Gewogen score: People (40%) × Process (35%) × Product (25%)
- Score 80-100: bouwen kan starten; 60-79: piloot met guardrails; 0-59: risico's eerst mitigeren

(`verified` via directe fetch van het Towards Data Science-artikel [8])

### 6. Outcome-mapping als vertaalmethode

Microsoft's AI Decision Framework benoemt als kerncriterium het kwantificeerbaarheidseis: "Als je de impact niet in euro's kunt uitdrukken, is de use case nog niet gereed voor prioritering." [7] (`inferred` via zoekresultaat-samenvatting)

Concrete formulering die werkt: "Het terugbrengen van de vraag-naar-antwoord-tijd van 3 dagen naar 5 minuten voor 200 beslissingen per jaar à €5.000 verbetering per beslissing" — dat is een blueprint-waardige formulering; "betere beslissingen" is dat niet.

## Evidence Table

| # | Bron | URL | Type | Key claim | Confidence |
|---|------|-----|------|-----------|------------|
| 1 | Kozyrkov — AI-First Leadership (INFORMS Analytics Magazine) | https://pubsonline.informs.org/do/10.1287/LYTX.2025.02.02n/full/ | secondary | Decision-first framework, drie evaluatiecriteria | medium |
| 2 | Acceldata — Kozyrkov on What AI Means for Leadership | https://www.acceldata.io/blog/cassie-kozyrkov-on-what-it-really-means-to-be-ai-first-key-takeaways-for-enterprise-leaders | secondary | AI-first definitie, purpose comes from people | medium |
| 3 | Karpathy — Software 3.0 (YC AI Startup School, 19 juni 2025) | https://inferencebysequoia.substack.com/p/andrej-karpathys-software-30-and | secondary | Software 3.0 keynote, prompts als broncode | high |
| 4 | Medium — Karpathy Software 3.0 analyse | https://medium.com/@ben_pouladian/andrej-karpathy-on-software-3-0-software-in-the-age-of-ai-b25533da93b6 | secondary | LLM als OS-metafoor, SW 3.0 eating 1.0/2.0 | medium |
| 5 | Fortune — MIT 95% AI Pilot Failure rapport | https://fortune.com/2025/08/18/mit-report-95-percent-generative-ai-pilots-at-companies-failing-cfo/ | secondary | MIT NANDA rapport aug 2025, methodologie 150 interviews | high |
| 6 | Marketing AI Institute — kritiek op MIT-studie | https://www.marketingaiinstitute.com/blog/mit-study-ai-pilots | secondary | Methodologische beperkingen 95%-claim | high |
| 7 | Microsoft AI Decision Framework (GitHub) | https://github.com/microsoft/Microsoft-AI-Decision-Framework | primary | Governance, data, kwantificeerbaarheidscriterium | medium |
| 8 | Towards Data Science — AI-3P Assessment Framework | https://towardsdatascience.com/the-ai-3p-assessment-framework/ | primary | People-Process-Product scoringsmodel | high |

## Coverage Status

- **Gecheckt direct:** bronnen 3, 5, 6, 8 direct gefetcht en gelezen
- **Blijft onzeker:** Kozyrkov's exacte drie criteria (meerdere parafrasen, originele bron niet direct gefetcht); MIT-rapport zelf niet direct gelezen (via Fortune-samenvatting)
- **Niet afgerond:** Karpathy's originele keynote-transcript niet direct opgehaald (secondaire bronnen consistent)

## Sources

1. Kozyrkov — AI-First Leadership: Rethinking Decision-making in the Age of AI (INFORMS) — https://pubsonline.informs.org/do/10.1287/LYTX.2025.02.02n/full/
2. Acceldata — Cassie Kozyrkov on What AI Really Means for Leadership — https://www.acceldata.io/blog/cassie-kozyrkov-on-what-it-really-means-to-be-ai-first-key-takeaways-for-enterprise-leaders
3. Inference by Sequoia — Karpathy's Software 3.0 and the New AI Stack — https://inferencebysequoia.substack.com/p/andrej-karpathys-software-30-and
4. Medium (Ben Pouladian) — Andrej Karpathy on Software 3.0: Software in the Age of AI — https://medium.com/@ben_pouladian/andrej-karpathy-on-software-3-0-software-in-the-age-of-ai-b25533da93b6
5. Fortune — MIT report: 95% of generative AI pilots at companies are failing — https://fortune.com/2025/08/18/mit-report-95-percent-generative-ai-pilots-at-companies-failing-cfo/
6. Marketing AI Institute — That Viral MIT Study Claiming 95% of AI Pilots Fail? Don't Believe the Hype — https://www.marketingaiinstitute.com/blog/mit-study-ai-pilots
7. Microsoft — Microsoft AI Decision Framework (GitHub) — https://github.com/microsoft/Microsoft-AI-Decision-Framework
8. Towards Data Science — Introducing the AI-3P Assessment Framework — https://towardsdatascience.com/the-ai-3p-assessment-framework/
