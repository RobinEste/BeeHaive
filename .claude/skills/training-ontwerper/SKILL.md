---
name: training-ontwerper
description: >
  TRIGGER wanneer de gebruiker een nieuwe BeeHaive-training, -cursus of -workshop
  wil ontwerpen, een bestaand trainingsontwerp wil herzien, of vraagt om
  ontwerpkeuzes te onderbouwen ("hoe lang moeten video's zijn?",
  "cohort of self-paced?", "welke retentie-cadans?"). Niet voor: trainingsmateriaal
  zelf schrijven (modulecontent, slides, video-script) of TRAINING-DESIGN.md
  aanpassen.
type: capability
disable-model-invocation: true
---

# /training-ontwerper

Onderzoekgestuurd ontwerp van een concrete BeeHaive-training (pilot, cohort of workshop) op basis van het naslagwerk [`docs/research/TRAINING-DESIGN.md`](../../../docs/research/TRAINING-DESIGN.md). De skill produceert het *ontwerp* (formaat, cadans, modaliteitenmix, retentie-plan, meet-plan, AI-tutor-keuzes, planning), niet het lesmateriaal zelf.

**Verschil met de design-bijbel.** Het naslagwerk geeft per dimensie wat het onderzoek zegt en hoe sterk de evidence is. Deze skill maakt per dimensie de **keuze** voor één concrete training, met expliciete verwijzing terug naar het naslagwerk. De bijbel is generiek; het ontwerp-document is specifiek.

## Referenties

| Wanneer | Lees |
|---------|------|
| Per dimensie-keuze onderbouwen | `${CLAUDE_PROJECT_DIR}/docs/research/TRAINING-DESIGN.md` |
| Diepere bron per dimensie nodig | `${CLAUDE_PROJECT_DIR}/docs/research/training-design-2026-04/INDEX.md` |
| Ontwerp-document scaffolden | `${CLAUDE_SKILL_DIR}/assets/ontwerp-template.md` |

## Wanneer triggert deze skill

- "We willen een training opzetten voor X."
- "Ontwerp een cursus voor doelgroep Y."
- "Welke retentie-cadans past bij een 6-weeks training?"
- "Wat is de juiste cohort-grootte voor onze pilot?"
- Herzien van een bestaand ontwerp na pilot-feedback.

**Niet triggeren bij:**

- Schrijven van module-inhoud, slides of video-scripts (gebruik `/bb-write` voor BB/GR-content; voor losse module-tekst is geen aparte skill nodig).
- Wijzigen van `TRAINING-DESIGN.md` zelf (dat is een meta-update, geen ontwerp-actie).
- Marketingteksten of landingspagina's voor een training.

## Instructies

### Stap 1: Lees het naslagwerk en plaats jezelf in de huidige stand

Doe dit vóór je scope-vragen stelt of keuzes voorstelt. Reden: het naslagwerk bevat zowel de ontwerp-richtlijnen (H1–H8) als de anti-patroon-lijst (Bijlage A) en de checklist (Bijlage B). Zonder die volledige context glippen er aanbevelingen door die in het naslagwerk juist worden weerlegd (bv. leerstijlen, 70:20:10).

1. Lees `docs/research/TRAINING-DESIGN.md` integraal. Het document is ~900 regels en past in één Read-call.
2. Open `docs/research/training-design-2026-04/INDEX.md` zodat je weet welke deelrapporten bestaan voor diepere onderbouwing per dimensie.
3. Inventariseer relevante eerdere ontwerpen onder `docs/trainings/` (als de map bestaat). Lees de meest recente; deze skill is iteratief en hergebruik van eerdere keuzes is normaal.

Aan het eind van Stap 1: je kent de hoofdstuk-indeling H1 t/m H8 en de Bijlage B-checklist op naam. Die ga je in Stap 3 als ruggegraat gebruiken.

### Stap 2: Scope-vragen — geen ontwerp zonder context

Stel **maximaal 5 scope-vragen per ronde** voordat je ontwerpkeuzes voorstelt. Gebruik AskUserQuestion met concrete opties waar mogelijk. De minimale set:

1. **Doel** — wat moet de deelnemer aan het einde *kunnen*? (Skill-building, awareness, gedragsverandering, certificering — kies één primair doel.)
2. **Doelgroep** — rol(len), seniority, voorkennis-niveau, sector-mix? (Bestuurders, AI-leads, developers, juristen, beleidsmakers, gemixt?)
3. **Setting** — open inschrijving of in-company? (Bepaalt L4-meting-haalbaarheid en cohort-mix-strategie.)
4. **Duur en cadans** — totale doorlooptijd (2/4/6/8 weken)? Wekelijks of tweewekelijks?
5. **Pilot of productie** — eerste cohort als pilot met feedback-verplichting, of doorlopende productie?

Optioneel afhankelijk van antwoorden:

- Welke BeeHaive-bouwstenen en -guardrails dekken we (alle 7+7 of een subset)?
- Wordt de AI-tutor onderdeel van de training of (nog) niet?
- Wat is het tarief en bedrijfsmodel (gratis pilot, gereduceerd, marktconform)?
- Capstone-deliverable: mini-governance-plan voor eigen organisatie of iets anders?

**Niet doen:** ontwerp-keuzes voorstellen zonder dat doel, doelgroep en duur expliciet zijn beantwoord. "Verzin er iets bij" leidt tot generiek ontwerp dat niet past.

### Stap 3: Per dimensie keuze maken met onderbouwing

Loop de checklist uit Bijlage B van het naslagwerk door, dimensie voor dimensie. Per ontwerpvraag:

1. Geef de **default-keuze** (wat het onderzoek aanbeveelt voor de geantwoorde scope).
2. Geef minimaal één **alternatief** wanneer er een legitieme reden is om af te wijken.
3. Verwijs expliciet naar het naslagwerk: `(zie TRAINING-DESIGN.md H1.3)`.
4. Markeer keuzes met **evidence-rating "te valideren"** als A/B-test-kandidaat — die hoorde je eigen evidence te genereren.

**Voorbeeld-uitkomst voor één dimensie:**

> **Cohort-grootte**
> Default: 12 deelnemers. Onderbouwing: live-discussie-sweet-spot is 10–20 (H1.3); voor pilot is ~10 het sweet spot voor signaal-diepte (H8.5). 12 zit veilig binnen die range met buffer voor uitval.
> Alternatief: 8 als de doelgroep zo specialistisch is dat 12 niet haalbaar is — accepteer dan minder peer-discussie-massa.

#### Verplichte dimensies (altijd doorlopen)

Loop deze hoofdstukken **op volgorde** door, ook als sommige keuzes triviaal lijken:

- **H1 Formaat & cadans** — cohort vs self-paced (H1.1), wekelijks ritme (H1.2), sessieduur en groepsgrootte (H1.3), flipped als default (H1.4), theorie-praktijk-verhouding (H1.5)
- **H2 Curriculum-structuur** — PBL als ruggegraat (H2.1), Knowles-vertaling (H2.2), scaffolding-tools (H2.3), blocked → interleaved (H2.4), capstone (H2.5)
- **H3 Modaliteitenmix** — geen VAK-frame (H3.1), Mayer-checklist (H3.2), materialenmix per format (H3.3), productie-eisen (H3.4)
- **H4 Didactische werkvormen** — worked examples (H4.1), peer-rubric (H4.2), live-werkvormen (H4.3), subgroep-trio's (H4.4)
- **H5 Retentie-mechanismen** — spaced-repetition-cadans (H5.1), retrieval na elke module (H5.2), interleaving-fase (H5.3), elaboration-prompt (H5.4), dual-coding-anker (H5.5), concrete review-cyclus (H5.6)
- **H6 Post-course continuïteit** — drip-cadans (H6.1), boosters (H6.2), community (H6.3), nieuwsbrief en blog (H6.4), if-then plans (H6.5)
- **H7 AI-tutor** — alleen als scope dit bevat: effectiviteit-check (H7.1), RAG-grounding (H7.2), Socratisch RTRI-prompt (H7.3), guardrails-architectuur (H7.4), cognitive-offloading-mitigaties (H7.5), AVG-checklist (H7.6)
- **H8 Meting & iteratie** — Kirkpatrick-meet-instrumenten (H8.1, H8.2), leading/lagging-indicators (H8.3), response-rate-mitigaties (H8.4), pilot-iteratie-cadans (H8.5)

#### Verplichte anti-patroon-check

Na de dimensie-pas: loop Bijlage A door en controleer dat het ontwerp-document geen van deze claims maakt:

- Geen leerstijlen-frame (A.1)
- Geen 70:20:10 als evidence-claim (A.2)
- Geen Learning Pyramid met percentages (A.3)
- Geen NPS als enig effect-bewijs (A.4)
- Geen overdreven percentage-claims over leertechnieken (A.5)

Als één van deze het ontwerp binnenglipt: vervang door de aanbevolen onderbouwing uit Bijlage A.

### Stap 4: Schrijf het ontwerp-document

**Locatie:**

```
docs/trainings/YYYY-MM-DD-<korte-naam>/ontwerp.md
```

Voorbeeld: `docs/trainings/2026-05-15-pilot-governance-leads/ontwerp.md`. Maak de bovenliggende `docs/trainings/`-map als die nog niet bestaat.

**Werkwijze:**

1. Lees `${CLAUDE_SKILL_DIR}/assets/ontwerp-template.md` — dit is de canonieke 10-secties-template.
2. Kopieer naar de doel-locatie en vul per sectie in op basis van de keuzes uit Stap 3.
3. Vervang de `<naam>`-, `<korte-naam>`- en `vX.Y`-placeholders door concrete waarden; vul Status op `concept` en Datum op vandaag.

**Schrijfregels voor het ontwerp-document:**

- Elke ontwerpkeuze heeft één regel onderbouwing met verwijzing naar `TRAINING-DESIGN.md H<nummer>`.
- "Te valideren"-keuzes komen óók in sectie 9 als A/B-test-kandidaat terecht.
- "Open punten" mag niet leeg zijn in een eerste-versie-ontwerp; minimaal 2 punten benoemd. Als je er geen 2 kunt bedenken: het ontwerp is óf incompleet óf overspecified — heroverweeg.

### Stap 5: Goedkeuring vragen

Vóór uitvoering: vraag de gebruiker expliciet of het ontwerp goedgekeurd is, en welke open punten nog beantwoord moeten worden voor de eerste pilot start. Dit is een hard gate; niet doorzetten naar uitvoeringswerk zonder bevestiging.

## Gotchas

- **Naslagwerk overslaan voelt verleidelijk** — vooral wanneer de scope-vraag al lijkt op een eerder ontwerp. Niet doen. Het naslagwerk wordt periodiek bijgewerkt na pilot-feedback; recent gewijzigde aanbevelingen mis je anders.
- **"Cohort van 10" als reflex** — pilot-target is 10, productie-cohort is 10–20 (zie H1.3, H8.5). Verwar pilot-grootte niet met productie-grootte als de scope al richting productie schuift.
- **AI-tutor-secties uitstellen leidt tot "AVG doen we straks"** — de AVG-vereisten (DPIA, TTL, EU-hosting, opt-in) zijn juridisch vereist, geen ontwerp-keuze. Skip H7.6 nooit, ook als de AI-tutor pas in fase 2 wordt uitgerold.
- **"Te valideren"-rating en gewone keuze in één regel** — een keuze die op evidence-rating "te valideren" leunt moet expliciet in sectie 9 als A/B-test-kandidaat genoemd worden, anders verdwijnt het in de uitvoering en bouw je geen eigen evidence op.
- **Anti-patronen sluipen via klant-language** — een opdrachtgever die "voor visuele leerders" of "70-20-10" gebruikt is normaal; herformuleer naar de Bijlage A-onderbouwing in plaats van de term over te nemen, zelfs als de klant het herhaalt.
- **Output-template lijkt "leeg invullen"** — de template is een skelet; per sectie hoort 3–6 regels echte inhoud, niet één bullet per veld. Een ontwerp van 50 regels is bijna altijd te dun.

## Anti-rationalisatie

| Rationalisatie | Weerlegging |
|---|---|
| "Dit is een pilot, het mag wat losser" | Pilot is precies waar de meest disciplinaire feedback-loops nodig zijn; losheid in ontwerp leidt tot onleesbare resultaten. |
| "Het naslagwerk lezen kost te veel context" | 900 regels is één Read-call. Skip nooit. |
| "Doelgroep is duidelijk genoeg" | "Professionals" is niet duidelijk. CIO, juriste en developer hebben verschillende vooronderstellingen. |
| "We hoeven Kirkpatrick niet, we voelen wel of het werkt" | Reaction-niveau-bias; entertainerige trainers scoren hoog op gevoel, niet op leren (zie Bijlage A.4). |
| "AI-tutor doen we later" | Prima, maar leg in het ontwerp uit *wanneer* en met welke evaluatiecriteria. Niet stilzwijgend uitstellen. |

## Onderhoud van deze skill

- Wanneer `TRAINING-DESIGN.md` een major revisie krijgt: update Stap 3-verwijzingen en Bijlage A-namen indien gewijzigd.
- Wanneer een pilot oplevert dat een aanbeveling niet werkte: log in `docs/trainings/<datum>/retro.md` en update zowel het naslagwerk als de skill als de afwijking structureel blijkt.
