# Training Design — onderzoekgestuurd ontwerp-naslagwerk

> **Versie:** 1.0 — 2026-04-28
> **Bronlaag:** [`training-design-2026-04/INDEX.md`](training-design-2026-04/INDEX.md) en de zes deelrapporten daarin.
> **Status:** levend document. Bij nieuwe research of nieuwe ervaring uit een pilot wordt dit document bijgewerkt, niet vervangen.

---

## Hoe dit document te gebruiken

Dit is **geen implementatieplan voor één specifieke training**. Het is een ontwerp-naslagwerk dat per ontwerpvraag samenvat wat het onderzoek zegt, hoe sterk de evidence is, en hoe het zich vertaalt naar BeeHaive. Bij elke nieuwe training, opleiding of cursus die we opzetten, raadplegen we dit document om beslissingen te onderbouwen.

**Drie gebruikspatronen:**

1. **Vooraf, bij ontwerp:** loop de hoofdstukken in volgorde door en kies bewust per dimensie. Bijlage B bevat een checklist die de keuzes structureert.
2. **Tijdens ontwerp, bij twijfel:** zoek de specifieke ontwerpvraag op (`Wanneer wel/niet?` of `Open keuzes`) en lees alleen dat blok.
3. **Achteraf, bij iteratie:** vergelijk pilot-resultaten met de hier verzamelde evidence en update zowel het training-ontwerp als dit document waar de ervaring afwijkt van het verwachte effect.

**Wat dit document niet is:**

- Geen marketing-document. De evidence-ratings zijn eerlijk, ook waar het ongemakkelijk is (zie Bijlage A: neuromythes).
- Geen volledige literatuurstudie. Voor de volledige bronvermelding per uitspraak: zie de zes deelrapporten in `training-design-2026-04/`.
- Geen stappenplan. Er staat geen "week 33 start cohort 1" in. Dat type planning hoort in een apart project- of pilot-document.

**Verwijzing-conventie.** Inline verwijzingen `[01]` t/m `[06]` corresponderen met de zes deelrapporten:

- [`01`](training-design-2026-04/01-didactiek-pbl.md) — PBL & andragogiek
- [`02`](training-design-2026-04/02-didactiek-multimodaal.md) — Multimodaliteit & materialenmix
- [`03`](training-design-2026-04/03-didactiek-blended-pilot.md) — Blended, cohort, pilot, Kirkpatrick
- [`04`](training-design-2026-04/04-retentie-memory.md) — Memory, spacing, retrieval, interleaving
- [`05`](training-design-2026-04/05-retentie-postcourse.md) — Post-course retentie
- [`06`](training-design-2026-04/06-ai-tutor.md) — AI-tutor, RAG, guardrails, AVG, meting

---

## Evidence-ratings: wat betekenen ze

Elke aanbeveling in dit document krijgt één van vier ratings. Behandel dat als kompas, niet als zekerheid.

| Rating | Betekenis | Voorbeeld |
|---|---|---|
| **Zeer sterk** | Meta-analytisch onderbouwd over decennia, herhaaldelijk gerepliceerd in diverse contexten | Spaced repetition, retrieval practice, implementation intentions |
| **Sterk** | Meerdere consistente studies of grote meta-analyses, soms met scope-beperkingen | Flipped classroom (g≈0.58–0.73), cohort-completion vs self-paced |
| **Matig** | Theoretisch goed onderbouwd, beperkt empirisch werk in de specifieke setting | Exacte drip-email-cadans, peer-community-format ROI online B2B |
| **Te valideren** | Theorie-extrapolatie of B2C-evidence die we naar B2B-volwassen-pro's vertalen | AI-tutor-effectiviteit voor governance-pro's, BeeHaive-specifieke adoptie |

**Praktijkregel:** bij een **zeer sterke** aanbeveling is het verstandig om expliciet te onderbouwen waarom je ervan afwijkt. Bij **te valideren** is het verstandig om expliciet meet-instrumentatie in te bouwen om eigen evidence op te bouwen.

---

## Hoofdstuk 1 — Trainingsformaat & cadans

### 1.1 Cohort versus self-paced

**Ontwerpvraag.** Bouwen we een cohort-gebaseerde training (vaste start- en einddatum, groep loopt samen op) of een self-paced cursus (deelnemer bepaalt eigen tempo)?

**Wat het onderzoek zegt.** Het verschil in voltooiingscijfers is dramatisch [03]:

| Format | Completion-rate |
|---|---|
| Self-paced MOOC (Coursera, Udemy) | 3–15% |
| Cohort-based (Maven, Section, Reforge) | 75–88% |

Mechanismen die dit verschil verklaren: aanspreekbaarheid door zichtbaarheid, tijd-urgentie door start- en einddatum, groepsdruk en peer-leren, en directe toegang tot een levende facilitator. Voor BeeHaive geldt aanvullend dat we in pilot-fase product-market-fit valideren; cohort-feedback is dichter en bruikbaarder dan asynchrone self-paced data.

**Evidence-sterkte.** Sterk.

**BeeHaive-vertaling.**

- Cohort is het uitgangspunt voor elke nieuwe training, zeker in pilot-fase.
- Self-paced kan secundair worden aangeboden zodra een cohort-versie minstens tweemaal succesvol is gedraaid en het materiaal stabiel is. Verwacht dan 3–15% completion (de range voor self-paced MOOCs) en ontwerp het bedrijfsmodel daarop, niet op de cohort-cijfers.

**Open keuzes per training.**

- Cohort-grootte (zie 1.3).
- Open inschrijving versus in-company (in-company maakt L4-meting haalbaar).
- Frequentie van cohorts (eens per kwartaal? maandelijks? rolling?).

### 1.2 Cadans en wekelijks ritme

**Wat het onderzoek zegt.** Voor professionals werkt een wekelijks ritme [03]: vaak genoeg om de aanspreekbaarheid vast te houden, niet zo vaak dat het een tweede baan wordt. Tweewekelijks is haalbaar; minder dan dat verdampt de groepsdruk. Een wekelijks contactmoment hoeft geen lange live-sessie te zijn: een korte synchrone sessie van 45–60 minuten plus een asynchrone deadline werkt.

**Evidence-sterkte.** Matig (gebaseerd op cohort-platform-praktijk, geen RCT).

**BeeHaive-vertaling.**

- Wekelijks ritme als default.
- Eén live moment per week van 45–60 minuten, plus een asynchrone deadline (peer review, eigen-werk-opdracht, retrieval-quiz).
- Vermijd "zwart gat"-weken. Als een week onverhoopt zonder sync valt (vakantie, feestdag), vervang door een korte ingesproken update of asynchrone discussie.

### 1.3 Sessieduur en groepsgrootte

**Wat het onderzoek zegt** [03]:

- **Duur synchrone sessie:** 45–60 minuten optimaal. Maximum 90 minuten met een pauze. Boven de 90 minuten zet digitale vermoeidheid in (Zoom-fatigue) en daalt informatie-opname.
- **Groepsgrootte live:** 10 minimum, 20 maximum. Onder de 8 ontstaat te weinig peer-kritische massa voor discussie; boven de 20 verdwijnt individuele interactie en wordt het een webinar.

**Evidence-sterkte.** Matig (overweging-richtlijnen vanuit synchrone-onderwijspraktijk).

**BeeHaive-vertaling.**

- Live-sessies plannen op 60 minuten, met buffer voor 15 extra minuten Q&A na afloop.
- Cohort-grootte 10 tot 20. Bij hoge inschrijving: splits in twee parallelle groepen, niet één grote groep.
- Bij interactieve onderdelen (rolspel met guardrails, peer review): subgroepen van 3–5 binnen de live-sessie.

### 1.4 Flipped classroom als default

**Wat het onderzoek zegt.** Meta-analyses (Sciencedirect 2023 en 2025, second-order meta-analyse) geven flipped classroom een gewogen effect-grootte van g ≈ 0.58 tot 0.73 [03]. Het mechanisme: theorie wordt vooraf zelf geconsumeerd (video, tekst, podcast), live tijd wordt besteed aan toepassing, peer feedback en debat. Theorie-monoloog tijdens live-tijd is in deze setting verspilling.

**Evidence-sterkte.** Sterk.

**BeeHaive-vertaling.**

- Default: alle theorie-content asynchroon vooraf. Live-tijd is gereserveerd voor casuïstiek, peer review, AMA, en rolspel met guardrails.
- Voor elke live-sessie wordt expliciet gemarkeerd welk asynchroon materiaal vooraf bekeken/gelezen moet zijn.
- Bot-driven check: korte retrieval-quiz aan begin van live-sessie kan dienen als gate (zie 5.2).

### 1.5 Theorie-praktijk-verhouding

**Wat het onderzoek zegt.** Het populaire 70:20:10-model is **niet** evidence-based [01]. Het komt uit self-reports van ongeveer 200 executives (Lombardo, Eichinger, McCall in de jaren tachtig). Training Industry, CCL en peer-reviewed analyse (Tandfonline 2021) noemen het expliciet een intuïtieve verdeelsleutel, geen empirisch ratio. Voor blended training met professionals werkt circa 30% theorie en 70% toepassing als richtlijn.

**Evidence-sterkte.** Matig (richting is goed onderbouwd vanuit andragogiek; exacte ratio is heuristiek).

**BeeHaive-vertaling.**

- Mik op 30% theorie, 70% toepassing in contacturen.
- Theorie zoveel mogelijk self-paced (flipped); toepassing in live-tijd en in eigen-werk-opdrachten.
- Vermijd 70:20:10 als marketing-claim. Schrap "leren gebeurt 70% on-the-job" uit alle externe communicatie.

---

## Hoofdstuk 2 — Curriculum-structuur

### 2.1 Project-based learning als ruggegraat

**Ontwerpvraag.** Bouwen we content-eerst (curriculum dat onderwerpen behandelt) of probleem-eerst (curriculum gebouwd rond projecten van deelnemers)?

**Wat het onderzoek zegt.** PBL is over meerdere meta-analyses en reviews heen consistent positief: hogere toepassing en transfer, betere retentie, hogere motivatie [01]. Voor professionals werkt PBL extra goed omdat zij intrinsiek-doelgericht leren vanuit een probleem in eigen werkcontext (Knowles' principe 5: orientation to learning is problem-centered, niet content-centered).

Belangrijke nuance: open-ended PBL zonder structuur faalt. Recent werk (IES; Boardman 2025; Framework for Scaffolding 2013; meta-analyse 2023) toont dat scaffolding cruciaal is.

**Evidence-sterkte.** Sterk voor PBL als principe; zeer sterk voor scaffolding-noodzaak.

**BeeHaive-vertaling.**

- Elke deelnemer start dag 1 met een **eigen governance-vraagstuk uit eigen organisatie**. Dat vraagstuk is gedurende de hele training de rode draad.
- Per bouwsteen of guardrail: worked example → eigen toepassing → peer review → coach- of bot-feedback.
- Capstone-deliverable is een mini-governance-plan voor de eigen organisatie; dit is geen extra opdracht maar de natuurlijke optelsom van de wekelijkse toepassingen.

### 2.2 Andragogiek (Knowles) als ontwerpprincipe

**Wat het onderzoek zegt.** De zes Knowles-principes zijn in 2024–2025 niet weerlegd, wel gerelativeerd [01]: ze fungeren als ontwerpprincipes, niet als getestte theorie. Meta-analytische evidentie voor de zes als geheel ontbreekt. Ze werken **als** je ze vertaalt naar concrete designkeuzes.

De zes principes:

1. **Need to know:** volwassenen willen weten waarom ze iets moeten leren.
2. **Zelfconcept:** volwassenen zijn zelfsturend; behandel hen niet als kinderen.
3. **Eerdere ervaring:** bouw voort op wat ze al weten en kunnen.
4. **Readiness:** leren wanneer ze er klaar voor zijn (probleem in werk).
5. **Orientation to learning:** probleem-centered, niet content-centered.
6. **Intrinsieke motivatie:** extrinsieke prikkels werken minder goed.

**Evidence-sterkte.** Matig (principes zijn ontwerp-heuristieken; concrete vertalingen zijn afzonderlijk onderbouwd).

**BeeHaive-vertaling per principe.**

- Principe 1: elke module opent met een 2–3 zin "waarom dit nu" (concrete consequentie als deelnemer dit níet beheerst).
- Principe 2: self-paced theorie staat klaar; deelnemer kiest tempo en volgorde binnen de week. Geen verplichte volgorde van video-clips.
- Principe 3: intake-survey vraagt naar bestaande ervaring per bouwsteen; de bot kan op basis daarvan extra context wegfilteren.
- Principe 4: het eigen governance-vraagstuk uit 2.1 is de readiness-anker.
- Principe 5: zie 2.1.
- Principe 6: vermijd gamification-voor-eigen-bestwil; intrinsieke driver is de kwaliteit van het eigen project.

### 2.3 Scaffolding: hoe gestructureerd is gestructureerd genoeg

**Wat het onderzoek zegt.** Drie soorten scaffolding zijn empirisch nodig om PBL te laten werken [01]:

- **Voorgestructureerde templates** per bouwsteen of guardrail (de "project canvas"-aanpak).
- **Wekelijkse check-ins** synchroon, kort, in subgroepen van 3–5.
- **Rubric-based peer review** (zoals SWoRD). Ongestructureerde peer feedback is slecht; gestructureerde rubric-based peer feedback verbetert zowel reviewer als ontvanger meetbaar.

**Evidence-sterkte.** Sterk.

**BeeHaive-vertaling.**

- Per bouwsteen: één canvas-template (PDF of MDX) met velden die deelnemer invult voor eigen organisatie.
- Per guardrail: één checklist-template met implementatievragen.
- Peer review-rubrics per opdracht: 4–6 criteria, elk met een 3-puntsschaal en concrete prompts ("wat is het sterkste punt?", "wat is de grootste blinde vlek?").
- Wekelijks subgroep-moment van 30–45 min in groepjes van 3–5.

### 2.4 Blocked introductie, daarna interleaved cases

**Ontwerpvraag.** Behandelen we de zeven bouwstenen en zeven guardrails één voor één, of door elkaar?

**Wat het onderzoek zegt.** Een belangrijke nuance uit 2025-onderzoek (MDPI Behavioral Sciences) [04]: voor het leren van een **regel** is blocked practice soms beter; voor **categorie-discriminatie op basis van similariteit** is interleaving beter. Rohrer & Taylor (2010): leerlingen scoorden 77% interleaved versus 38% blocked op een rekenkundige discriminatie-taak. Het mechanisme is discriminatief contrast: je moet waarnemen welk concept van toepassing is.

**Evidence-sterkte.** Sterk voor categorie-discriminatie; gemengd voor regelgebaseerd leren.

**BeeHaive-vertaling.**

- **Fase 1 (blocked introductie):** elke bouwsteen of guardrail krijgt een eigen blok waarin het concept wordt geïntroduceerd. Dit is regel-leren: "wat is bouwsteen 4 en wanneer pas je het toe."
- **Fase 2 (interleaved cases):** zodra het hele framework is geïntroduceerd, volgen cases waarin deelnemers moeten herkennen welke bouwsteen of guardrail van toepassing is. Cases komen door elkaar uit verschillende sectoren (zorg, overheid, retail) en raken meerdere bouwstenen tegelijk.

Voor een 4–8-weeks curriculum: weken 1–4 blocked, weken 5–8 interleaved. Voor een korter format (2–3 weken): blocked introductie van 60–70% van de tijd, daarna interleaved.

### 2.5 Capstone als transfer-mechanisme

**Wat het onderzoek zegt.** Elaboratie en transfer worden versterkt wanneer deelnemers nieuwe informatie koppelen aan eigen werkcontext [04]. Dunlosky et al. (2013) geeft elaboratieve interrogatie en self-explanation een matige utility-rating: positief, minder robuust dan spacing en retrieval, maar krachtig wanneer concreet gekoppeld aan eigen ervaring.

**Evidence-sterkte.** Matig-sterk.

**BeeHaive-vertaling.**

- Capstone is een mini-governance-plan voor de eigen organisatie van de deelnemer. Inhoud: één bouwsteen-toepassing per kernproces, plus een prioriteitenlijst van guardrails.
- Capstone wordt gepresenteerd in laatste live-sessie (peer audience), niet alleen ingeleverd op papier.
- Capstone dient als L2-meting (zie 8.2).

---

## Hoofdstuk 3 — Modaliteitenmix

### 3.1 De VAK-vraag: waarom we leerstijlen niet gebruiken

**Wat het onderzoek zegt.** VAK is een neuromyth [02]:

- Pashler et al. (2008): geen empirische steun voor de meshing-hypothese.
- Newton (2015, *Frontiers in Psychology*): 89% van recente hoger-onderwijs-publicaties ondersteunt VAK ondanks afwezigheid van bewijs; 93% van docenten gelooft in leerstijlen.
- Frontiers meta-analyse (2024): na aggregatie nog steeds geen meetbaar matching-effect.

Mensen hebben **voorkeuren**: dat is iets anders dan dat ze beter leren in die modaliteit voor willekeurig materiaal. Een instructie voor het monteren van een kast leert iedereen beter met beeld plus tekst, ongeacht "stijl".

**Evidence-sterkte.** Zeer sterk (consensus, decennia).

**BeeHaive-vertaling.**

- We gebruiken een multimodale mix, maar niet vanwege leerstijlen.
- In communicatie naar deelnemers en opdrachtgevers nooit het frame "auditieve leerders / visuele leerders". Wel wel het frame keuzevrijheid, toegankelijkheid, retrieval-cues.

### 3.2 Wat wel werkt: dual coding plus Mayer

**Wat het onderzoek zegt.**

- **Dual Coding (Paivio 1971; Clark & Paivio 1991; recent bevestigd):** informatie die gelijktijdig via verbaal en visueel kanaal wordt gecodeerd, krijgt twee retrieval-cues, dus betere recall (picture superiority effect). Recente retentiestudies (2024) laten zien dat dual-coded lessen de vergeetcurve afvlakken [02].
- **Mayer's Cognitive Theory of Multimedia Learning** (12 principes, editie 2021, meer dan 200 experimenten) [02]:

| # | Principe | Wat het zegt |
|---|---|---|
| 1 | Coherence | Verwijder irrelevant beeld, muziek of tekst |
| 2 | Signaling | Markeer kernpunten visueel |
| 3 | Redundancy | Geen woord-voor-woord ondertiteling plus narratie |
| 4 | Spatial contiguity | Plaats label naast het ding |
| 5 | Temporal contiguity | Beeld en spraak gelijktijdig |
| 6 | Segmenting | Deel instructie op in user-paced chunks |
| 7 | Pre-training | Introduceer begrippen vooraf |
| 8 | Modality | Spreek tekst uit, toon beeld (niet tekst-op-tekst) |
| 9 | Multimedia | Beeld plus woorden beter dan alleen woorden |
| 10 | Personalization | Conversational tone ("jij") |
| 11 | Voice | Menselijke stem beter dan synthetisch (verschil kleiner met moderne TTS) |
| 12 | Image | Pratend hoofd is optioneel; voegt niet altijd toe |

**Evidence-sterkte.** Zeer sterk (Mayer is een van de best-onderbouwde frameworks in instructional design).

**BeeHaive-vertaling.** Elke zelfgemaakte video, elke infographic en elke long-form-tekst wordt vóór publicatie tegen de Mayer-checklist gehouden (zie Bijlage B punt 3.x).

### 3.3 Materialenmix per format

| Format | Wanneer het best werkt | Ontwerp-richtlijnen |
|---|---|---|
| **Long-form tekst** | Diepte, nuance, zelf-tempo, terugzoekbaar. Voor complex en lang materiaal wint print/tekst op retentie en kritische analyse, mits de lezer vaardig is. | 1.500–4.000 woorden, duidelijke H2/H3-structuur, samenvattingsblokken, downloadbaar als PDF. |
| **Flashcards / spaced repetition** | Feiten, definities, jargon, framework-componenten. De zeven bouwstenen plus zeven guardrails zijn perfect materiaal. Sterkste evidence (Rowland 2014, g=0.50; Adesope 2017, 217 studies). | Korte vraag, kort antwoord, één concept per kaart. Anki/Leitner-cadans (1, 3, 7, 14, 35, 90 dagen). |
| **Podcasts** | Commute, herhaling via ander kanaal, storytelling, interviews met praktijkcases. MDPI 2024: effectief voor intentional en incidental learning. | 15–30 minuten, één kernidee plus 1–2 cases. Niet de primaire theoriebron. |
| **Infographics** | Overzicht, relaties, samenhang. Het 7+7-framework-schema is ideaal. PMC 2022: verhoogt engagement, retentie en recall, onderbouwd vanuit dual coding. | Eén boodschap per infographic, visueel hiërarchisch, witruimte, scanbaar in onder de 30 seconden, bruikbaar los van tekst. |
| **Video** | Demonstratie (AI-tool live), human connection, procedures. Guo / MIT-analyse van 6,9M MOOC-video-sessies: engagement zakt dramatisch na 6 minuten. | **2–5 minuten** per clip ideaal (microlearning). Talking head optioneel. Script volgens coherence en signaling. |

**Evidence-sterkte.** Sterk per format.

### 3.4 Algemene productie-eisen

- **Audio is non-negotiable.** Publiek vergeeft wankele beeldkwaliteit, geen slechte audio. Investeer in een goede microfoon vóór een goede camera.
- **Geen achtergrondmuziek onder spraak** (Coherence-principe).
- **Accessibility als kwaliteitsnorm:** transcripties bij elke video en podcast, alt-tekst bij elke infographic, leesniveau B1–B2 voor Nederlandstalige professionals. B1–B2 dient om cognitieve belasting te beheersen; het is geen aanname over het niveau van de lezer.
- **Redundantie in het juiste formaat:** dezelfde kernboodschap van een bouwsteen in tekst, video, flashcard en infographic. Niet vier keer dezelfde informatie, wel vier keer dezelfde kern in vier modaliteiten. Dit is dual coding plus retrieval practice, niet leerstijlen.

### 3.5 Eerlijke framing richting opdrachtgever

Wanneer een opdrachtgever vraagt om "verschillende modaliteiten omdat sommigen visuele leerders zijn":

> Wij leveren de multimodale mix die je wilt: tekst, audio, video, infographics. Maar het werkt niet omdat sommige mensen auditieve leerders zijn. Het werkt omdat (a) variatie de cognitieve belasting verlaagt, (b) herhaling via een ander kanaal de retrieval-cues verdubbelt (dual coding), (c) toegankelijkheid verhoogt voor wie tijdelijk in de auto, achter laptop of met dyslexie leert, en (d) keuzevrijheid de motivatie verhoogt. Effectief om sterkere redenen dan de neuromyth.

---

## Hoofdstuk 4 — Didactische werkvormen

### 4.1 Worked examples plus eigen toepassing

**Wat het onderzoek zegt.** Worked examples (volledig uitgewerkte voorbeeld-cases) verlagen cognitive load voor beginners. Combineren met eigen toepassing zorgt voor de transfer-stap [01].

**Evidence-sterkte.** Sterk (Sweller's Cognitive Load Theory).

**BeeHaive-vertaling.**

- Per bouwsteen: minimaal één volledig uitgewerkte case (fictief of geanonimiseerd) als worked example.
- Direct gevolgd door de eigen-toepassing-opdracht: pas dit toe op je eigen organisatie.
- Voor gevorderden: minder worked example, meer fading (alleen gedeeltelijk uitgewerkt; deelnemer vult in).

### 4.2 Peer review met rubric

**Wat het onderzoek zegt.** Ongestructureerde peer feedback is slecht; gestructureerde, rubric-based peer review verbetert zowel reviewer als ontvanger meetbaar [01]. Het mechanisme: de reviewer moet criteria expliciet toepassen, dat is elaboratie.

**Evidence-sterkte.** Sterk.

**BeeHaive-vertaling.**

- Elke ingeleverde opdracht wordt door 2 peers gereviewd via een rubric met 4–6 criteria.
- Rubric-prompts zijn concreet ("Welke aanname zou ik aanvechten?") niet abstract ("Beoordeel kwaliteit").
- Reviewer ontvangt de feedback van zijn peers op zijn review (meta-feedback) een keer per cohort, om review-vaardigheid expliciet te ontwikkelen.

### 4.3 Synchrone live-werkvormen

Geen monoloog. De live-tijd wordt besteed aan een mix van:

- **Casus-debat** in subgroepen, plenair terugkoppelen.
- **AMA** (ask me anything) voor het laatste kwartier.
- **Rolspel met guardrails:** één deelnemer speelt de bestuurder die om een onverantwoorde AI-toepassing vraagt; de ander oefent de guardrail-respons.
- **Peer-presentaties:** 5 minuten presentatie van eigen-werk-vraagstuk, gevolgd door 5 minuten vragen.
- **Live retrieval:** open vraag aan de groep zonder voorbereidingstijd, antwoorden in chat, daarna bespreken.

### 4.4 Subgroepen en kleine cohorten

**Wat het onderzoek zegt.** Voor live discussie zijn subgroepen van 3–5 optimaal: groot genoeg voor variatie, klein genoeg voor individuele bijdrage [01][03].

**BeeHaive-vertaling.**

- Vaste subgroep-trio's voor de duur van de cohort. Bouwt vertrouwen voor diepere feedback.
- Roteren alleen als groepsdynamiek vastloopt of als deelnemers het zelf aanvragen.

---

## Hoofdstuk 5 — Retentie-mechanismen

### 5.1 Spaced repetition als ruggegraat

**Wat het onderzoek zegt.** De Cepeda-meta-analyse (839 assessments over 317 experimenten) toont onomstotelijk aan dat spaced practice beter werkt dan massed [04]. Vuistregel uit Cepeda et al. (2008): **optimaal interval ≈ 10–20% van de gewenste retentietermijn**.

| Gewenste retentie | Optimaal interval (eerste herhaling) |
|---|---|
| 1 week | 1 dag |
| 1 maand | 3–6 dagen |
| 6 maanden | 3–4 weken |
| 1 jaar | 3–5 weken |

Het Leitner-systeem en Anki's SM-2-algoritme zijn praktische implementaties: correcte kaarten verschuiven naar langere intervallen (1d → 3d → 7d → 16d → 35d), foute kaarten vallen terug naar interval 1.

Marketing-claims dat spaced repetition retentie "met 200% verhoogt" zijn overdreven; de peer-reviewed literatuur spreekt van medium-tot-grote effect-sizes.

**Evidence-sterkte.** Zeer sterk.

**BeeHaive-vertaling.**

- Per bouwsteen en per guardrail: een micro-deck van 8–15 flashcards (definitie, voorbeeld, tegenvoorbeeld, toepassingsvraag).
- Cursusbot implementeert Leitner-flow op dag 1, 3, 7, 16, 35, 90 voor kern-concepten.
- Communiceer expliciet aan deelnemers: "5 minuten per dag is effectiever dan 1 uur per week."
- Bot kan kaarten semi-automatisch genereren uit cursusnotities met RAG-grounding, maar onderwerp ze aan menselijke review vóór ze in productie gaan.

### 5.2 Retrieval practice als afsluiting van elke module

**Wat het onderzoek zegt.** Roediger & Karpicke (2006, 2008) lieten zien dat actief terughalen dramatisch beter is dan herlezen. Rowland (2014) vond een medium-to-large effect (g = 0.50) in meta-analyse [04]. Belangrijk: zonder feedback werkt het testing effect alleen als praktijktest-accuracy boven 50% is, anders versterk je fouten.

Kernboodschap: **testing is leren, niet meten**.

**Evidence-sterkte.** Zeer sterk.

**BeeHaive-vertaling.**

- Elke module eindigt niet met een samenvatting maar met 3–5 vrije-ophaalvragen.
- Voorbeeld-prompts: "Beschrijf in eigen woorden waarom guardrail X de risico's van bouwsteen Y afdekt." Of: "Wat zijn de drie kernvragen die een governance-owner moet stellen voor bouwsteen Z?"
- Bot stelt spontane terugblikvragen op dag 7 en dag 21: "Twee dagen geleden hebben we bouwsteen 3 behandeld. Kun je zonder terug te kijken de drie kernvragen formuleren?"
- Alle quizzes zijn lage-stakes (geen cijfer), met directe feedback. Quizzes met cijfer triggeren risicoaversie en daarmee minder leren.

### 5.3 Interleaving voor categorie-discriminatie

Zie 2.4 voor curriculum-vertaling. Belangrijke ontwerpregel: in een interleaved-blok komen casussen door elkaar uit verschillende sectoren, niet per sector gegroepeerd. Dit dwingt deelnemers tot herkennen ("welke bouwsteen is hier het meest relevant"), wat de discriminatieve vaardigheid traint die in de praktijk nodig is.

**Evidence-sterkte.** Sterk voor categorie-discriminatie; gemengd voor regel-leren (zie 2.4).

### 5.4 Elaboration: koppel aan eigen context

**Wat het onderzoek zegt.** Dunlosky et al. (2013) gaf elaboratieve interrogatie en self-explanation een matige utility-rating. Werkt het best wanneer deelnemers nieuwe informatie koppelen aan eigen werkcontext [04].

**Evidence-sterkte.** Matig-sterk.

**BeeHaive-vertaling.**

- Elke module bevat de prompt: "Geef een voorbeeld uit je eigen organisatie waar deze bouwsteen of guardrail wel of niet wordt toegepast."
- Bot doet door-vragen: "Waarom is bouwsteen 4 nodig in een organisatie zonder model governance?", niet "wat is bouwsteen 4".
- Self-explanation als vast onderdeel van de capstone (zie 2.5).

### 5.5 Dual coding (kort)

Volledig uitgewerkt in 3.2 en deelrapport [02]. Vertaling voor retentie:

- Eén consistente infographic per bouwsteen of guardrail als visueel ankerpunt.
- Eén overkoepelend framework-diagram waarin alle 7+7 in relatie staan; deelnemers zien dit elke week terug.

**Evidence-sterkte.** Matig-sterk.

### 5.6 Concrete review-cyclus voor BeeHaive (4–8 weken curriculum)

| Tijdpunt | Mechanisme | Vorm |
|---|---|---|
| Dag 1 | Eerste blootstelling | Module-content (video, tekst) |
| Dag 1 (avond) | Eerste retrieval | 3 flashcards in bot |
| Dag 3 | Tweede retrieval | Bot-prompt: "wat herinner je je nog?" |
| Dag 7 | Derde retrieval plus elaboration | Wekelijkse live-sessie + open ophaalvraag |
| Dag 21 | Cross-module retrieval | Interleaved casus (week 5+) |
| Dag 60 | Booster-retrieval | Drip-email met 1 quizvraag |
| Dag 120 | Late-retrieval | Bot-check-in voor lange-termijn-anker |

---

## Hoofdstuk 6 — Post-course continuïteit

### 6.1 Drip-emails als reactivatie-mechanisme

**Wat het onderzoek zegt.** Meer dan 70% van deelnemers van betaalde cursussen haakt af binnen 2 weken zonder reactivatie (LearnWorlds, Learning Revolution 2025) [05]. De forgetting-curve-literatuur onderbouwt waarom een drip-schedule werkt: reactivatie net vóór een vergetingsdip.

**Evidence-sterkte.** Matig (sterke theoretische basis vanuit spacing en testing effect; specifieke email-cadans is grotendeels marketing-literatuur, geen RCT).

**BeeHaive-vertaling: drip-cadans post-course.**

| Dag | Inhoud | Lengte |
|---|---|---|
| 1 | "Waar begin je: 3 acties deze week" plus 1 flashcard | ~200 woorden |
| 3 | Retrieval-quiz (1 open vraag, antwoord pas zichtbaar bij klik) | zeer kort |
| 7 | Praktijk-case gelinkt aan bouwsteen 1 | ~400 woorden |
| 14 | Implementation intention-prompt: "Welk moment in je week ga je guardrail X toepassen?" | 100 woorden plus form |
| 30 | Booster-quiz (5 vragen) plus link naar community | ~5 minuten |
| 60 | Nieuwe case plus reflectievraag | ~400 woorden |
| 90 | Zelfassessment: wat pas je daadwerkelijk toe? | survey |

**Niet doen.** Kalender-gedreven mails ("hé het is donderdag!"). Wel: mijlpalen-gedreven mails (een week na elke afgesloten module, een maand na laatste module, etc.).

### 6.2 Booster-sessies: maand 1 en maand 3

**Wat het onderzoek zegt.** Transfer E-Booster onderzoek (Hawaii): deelnemers met online booster-interventies scoorden significant hoger op kennis-retentie [05]. BizLibrary: zonder booster vergeet men ongeveer 70% binnen 24 uur.

**Evidence-sterkte.** Matig-sterk (kleinere studies, consistent richtingeffect).

**BeeHaive-vertaling.**

- **Maand 1 booster:** 60-minuten live online sessie, 10–15 deelnemers. Format: elk 3 minuten over "wat heb ik toegepast, waar loop ik tegenaan", collectieve probleemoplossing.
- **Maand 3 booster:** 90-minuten sessie, diepere casuïstiek, eventueel gasten (ervaringsdeskundigen of klanten van deelnemers).
- **Optioneel maand 6:** alumni-event, lichter format, netwerk-gericht.

### 6.3 Community en peer-learning

**Wat het onderzoek zegt.** APA meta-analyse 2021: peer-interactie heeft een significant positief effect op leren, gemiddeld medium effect-size [05]. Mechanisme: peer-instruction triggert retrieval en diepe verwerking.

**Schrap uit marketing.** De "Learning Pyramid" (Dale's cone, met de claim 90% door te onderwijzen) is bekend maar **niet** empirisch onderbouwd. Het onderliggende principe (teaching others = retrieval plus elaboration) is wel solide.

**Evidence-sterkte.** Sterk principe; matige evidence voor specifieke online-format-ROI.

**BeeHaive-vertaling.**

- Besloten community per cohort (Slack, Discord of Circle). Niet één grote alumni-community waar nieuwe cohorten in verzanden.
- "Guardrail-van-de-maand": één alumni-facilitator leidt discussie. Roteert om de maand.
- AI-bot leest mee (met expliciete consent): signaleert herhaal-vragen die kunnen worden omgezet in een FAQ of nieuwe content.

### 6.4 Blog of nieuwsbrief als herhaalkanaal

**Wat het onderzoek zegt.** Lange-termijn engagement via nieuwe content is spaced exposure plus elaboration. Minder direct bewijs voor retentie, mechanismen zijn dezelfde als drip-emails [05].

**Evidence-sterkte.** Matig.

**BeeHaive-vertaling.**

- Maandelijkse nieuwsbrief met één case study, één tool-update, één vraag uit de community.
- Blogs per bouwsteen of guardrail; gelinkt vanuit drip-mails en bot-antwoorden zodat herhaalde blootstelling natuurlijk gebeurt.

### 6.5 Implementation intentions (Gollwitzer)

**Wat het onderzoek zegt.** Gollwitzer & Sheeran's meta-analyse (94 studies): **if-then plans** leveren een medium-to-large effect (d = 0.65) op doelrealisatie [05]. Vorm: "Als [situatie X], dan doe ik [gedrag Y]."

**Evidence-sterkte.** Zeer sterk.

**BeeHaive-vertaling.**

- Elke module eindigt met een if-then prompt. Voorbeeld: "Als een collega voorstelt om een LLM in productie te zetten zonder evaluatie, dan stel ik guardrail 3 voor."
- Deze zinnen worden in de bot opgeslagen; bot herinnert eraan op dag 14 en dag 60.
- Tijdens booster-sessies maand 1 en 3: expliciet checken of if-then-plans gerealiseerd zijn; zo niet, herformuleren naar concretere trigger.

---

## Hoofdstuk 7 — AI-tutor: ontwerp, guardrails, privacy

### 7.1 Effectiviteit-status: gemengd, niet wonderlijk

**Wat het onderzoek zegt** [06]:

**Positief signaal:**

- **Khanmigo** (mixed-methods, 69 undergrad physics, *Journal of Teaching and Learning* 2025): significante learning gains in alle condities, geen significant verschil tussen Khanmigo en Google. Studenten waarderen step-by-step guidance.
- **Harvard CS50 Duck** (Malan et al., SIGCSE 2024): grootschalige deployment, sterk positieve feedback ("alsof ik een persoonlijke TA heb"). Geen RCT; vooral kwalitatief.
- **Duolingo Max** (interne data): 34% betere grammatica-retentie met "Explain My Answer", 15% hogere course completion. Bedrijfsdata, niet peer-reviewed.
- **Rori** (Ghana, WhatsApp math tutor): peer-reviewed RCT, 1 uur per week → effect-size equivalent aan een extra schooljaar.

**Tegenbewijs:**

- **University of Pennsylvania** (Turkse high school, 2024): ChatGPT-gebruikers losten 48% meer oefenproblemen correct op, maar scoorden 17% lager op een conceptueel begrip-test. Cognitive-offloading-waarschuwing.
- **MDPI en Frontiers in Psychology** (2025): frequent AI-gebruik correleert negatief met critical thinking, gemedieerd door cognitive offloading, vooral bij jongeren.

**Eerlijke inschatting.** AI-tutors zijn geen wondermiddel. Ze zijn vooral effectief als **scaffolding-tool die actief denkwerk uitlokt**, niet als antwoord-leverancier.

**Evidence-sterkte.** Sterk dat AI-tutors *kunnen* werken; **te valideren** dat ze werken voor BeeHaive's doelgroep (volwassen governance-pro's).

### 7.2 RAG over cursusmateriaal: grounding

**Wat het onderzoek zegt** (uit 2025 reviews; MEGA-RAG, MetaRAG) [06]:

- **Grounding = antwoorden verankeren aan verifieerbare documenten.** Zonder grounding hallucineren LLM's.
- **Citaties per claim:** elk feitelijk statement verwijst naar een cursusbron (module, sectie, video-timestamp).
- **"Weet ik niet"-gedrag:** bot zegt expliciet wanneer retrieval niets relevants oplevert; gebruik een confidence-threshold.
- **Dual-pathway retrieval** (dense + sparse + knowledge graph): KG-RAG reduceerde hallucinaties met 18% in biomedische QA. Past goed bij BeeHaive's Neo4j-knowledge-graph.

**Evidence-sterkte.** Sterk en snel evoluerend.

**BeeHaive-vertaling.**

- Alle cursuscontent in een vector-store: video-transcripts, slides, MDX-content uit `frontend/src/content`, plus de Neo4j-knowledge-graph van het framework.
- Citatie-vorm: "(BB_03, sectie 'Risicoclassificatie')" of "(GR_05, paragraaf 2)".
- Confidence-fallback: bij lage retrieval-score zegt de bot "dit valt buiten mijn cursusinhoud; ik raad je aan deze vraag aan een moderator te stellen."

### 7.3 Socratisch scaffolden: never give the answer

**Wat het onderzoek zegt.** Structurele prompts ("clarify → justify → counterexample → synthesize") plus de regel "**Never give the student the answer**" in de system prompt produceren meetbaar meer zelf-reflectie en kritisch denken [06].

**System-prompt template (RTRI-framework):**

```
ROLE
Je bent een Socratische tutor voor BeeHaive's AI-governance cursus.

TASK
Help de cursist concepten te begrijpen door vragen te stellen, geen
directe antwoorden.

REQUIREMENTS
- Geef nooit een volledig antwoord op een open vraag.
- Begin met een verhelderende tegenvraag.
- Geef hints in 3 niveaus:
    1. context
    2. gerelateerd concept
    3. gedeeltelijke hint
- Pas na 3 pogingen van de cursist mag je een fragment van het
  antwoord geven.

INSTRUCTIONS
- Blijf binnen de 7 bouwstenen + 7 guardrails.
- Citeer de bron bij elke feitelijke claim.
- Als de cursist vraagt om "los deze casus voor me op", weiger
  vriendelijk en bied scaffolding aan.
```

**Evidence-sterkte.** Sterk (Socratic Playground for Learning, Evolutionary RL Socratic tutor: critical thinking-frequency ongeveer 3x hoger dan supervised fine-tuning baseline).

### 7.4 Guardrails-architectuur

**Wat het onderzoek zegt.** Best-practice patronen (2025 literatuur, Arthur AI, Confident AI, Datadog) [06]:

- **Pre-LLM guardrails (input-filtering):** blokkeer verzoeken om volledige essays of huiswerk op te lossen, vragen buiten scope (politiek, andere frameworks).
- **Post-LLM guardrails (output-filtering):** controleer of antwoord een citaat bevat, of antwoord boven X tokens een scaffolding-vraag bevat, of er PII in zit.
- **LLM-as-judge evaluatie:** een tweede model beoordeelt of antwoord Socratisch is en grounded.
- **Domain boundary:** expliciete lijst van in-scope topics (de 7+7) plus een escalatie-naar-moderator-pad.

**Evidence-sterkte.** Sterk (industrie-best-practice; geen RCT-evidence maar consensus).

**BeeHaive-vertaling.**

- Guardrails-AI library (Python) in `backend/app/services`. Policies als YAML.
- Logging van alle guardrail-triggers voor wekelijkse review.
- "Eet je eigen hondenbrood": de guardrails op onze eigen tutor-bot zijn een illustratie van de 7 BeeHaive-guardrails in praktijk.

### 7.5 Cognitive offloading voorkomen

**Wat het onderzoek zegt.** Over-reliance op AI verlaagt concept-begrip (UPenn studie, 17% lager) [06]. Mitigaties:

- **Reflection prompts:** "Leg het antwoord in eigen woorden uit" na bot-interactie.
- **AI-free sessies:** zelftests zonder botgebruik (zichtbaar gelogd).
- **Delayed testing:** quiz op dag 7 over concepten die op dag 1 met bot besproken zijn, zonder botgebruik.
- **Transparantie over gebruik:** deelnemers zien hun eigen "bot-dependency-score" als zachte nudge.

**Evidence-sterkte.** Matig-sterk (mechanisme is goed onderbouwd; specifieke mitigatie-effecten zijn nog beperkt onderzocht).

**BeeHaive-vertaling.**

- Bot weigert vriendelijk bij directe antwoord-vragen op casus-opdrachten.
- Wekelijkse delayed quiz zonder bot-toegang.
- "Bot-dependency-score" als opt-in dashboard-feature, niet automatisch zichtbaar voor anderen.

### 7.6 AVG en privacy: niet onderhandelbaar

**Wat het onderzoek zegt** (2025–2026 guides) [06]:

- **EU-hosting verplicht** voor gevoelige conversaties. BeeHaive zit al goed met Hetzner.
- **Data-minimalisatie:** bewaar chat-logs zo kort mogelijk (default 30–90 dagen; 1 jaar is al lang).
- **Recht op vergeten:** expliciete delete-functie per gebruiker.
- **Geïnformeerde consent:** duidelijk tonen dat deelnemer met AI chat, wat wordt opgeslagen, waarvoor gebruikt.
- **DPIA verplicht** voor AI-systemen die persoonsgegevens verwerken (overlap EU AI Act en AVG).
- **Encryptie in transit en at rest** voor alle conversation-data.
- **Geen gebruik van deelnemer-data voor LLM-training** zonder aparte opt-in.
- **Processor-agreements** met LLM-provider (Anthropic): zero-data-retention-endpoints aanvragen waar mogelijk.

**Evidence-sterkte.** Juridisch vereist, niet optioneel.

**BeeHaive-vertaling.**

- Postgres-tabel `chat_sessions` met TTL van 90 dagen (configureerbaar per gebruiker).
- DPIA-document als onderdeel van governance-documentatie (eet je eigen hondenbrood).
- Privacy-policy expliciet: conversaties worden alleen gebruikt voor kwaliteitsverbetering, nooit voor training van derde-partij-modellen.

---

## Hoofdstuk 8 — Meting en iteratie

### 8.1 Kirkpatrick met nuance

**Wat het onderzoek zegt.** Kirkpatrick's vier niveaus (1959, herzien in "New World" model 2016) [03][06]:

1. **Reaction:** tevredenheid (NPS, CSAT).
2. **Learning:** wat weten of kunnen ze nu? (pre/post-assessment, retrieval).
3. **Behavior:** wat doen ze anders op hun werk? (3–6 maanden later).
4. **Results:** meetbare business-impact.

**Belangrijke kritieken (Kirkpatrick Partners erkent dit zelf, 2024-updates Alzate):**

- Niveau 1 correleert zwak met daadwerkelijke performance. "Ze vonden het leuk" ≠ "ze leren beter" ≠ "ze doen het beter". Entertainerige trainers scoren hoger op reaction maar niet op learning.
- Niveau 3 en 4 zijn vaak buiten het bereik van de opleider (organisatiecontext bepaalt mee).

**Evidence-sterkte.** Sterk als framework; specifieke metrieken voor AI-governance-training zijn nieuw en moeten zelf gevalideerd worden.

### 8.2 Praktisch meet-framework voor BeeHaive

| Niveau | Meet-instrument | Wanneer | Target |
|---|---|---|---|
| 1 | NPS plus 3 open vragen ("wat werkt / wat mist / wat snijden") | Na elke module en aan het eind | NPS ≥ 30 oké, ≥ 50 goed |
| 2 | Retrieval-quizzes per bouwsteen + capstone-rubric + delayed post-tests dag 30/60/90 | Continu plus eind plus delayed | Quiz-gemiddelde > 70%; capstone-rubric apart |
| 3 | Zelfrapportage plus korte case-interview 3 maanden later | 3 maanden na afsluiting | ≥ 60% geeft concreet voorbeeld van toepassing |
| 4 | Optioneel, organisatie-gebonden; alleen bij in-company | 6 maanden | Case per case |

### 8.3 Leading versus lagging indicators

| Type | Indicator |
|---|---|
| Leading | % deelnemers dat binnen 30 dagen een governance-document heeft opgesteld |
| Leading | Aantal if-then plans dat is uitgevoerd (zelfrapportage) |
| Leading | Bot-engagement-frequency (proxy voor actieve verwerking — let op offloading-risico) |
| Leading | Community-posts per deelnemer |
| Leading | Delayed-quiz-score dag 60 |
| Lagging | Adoptie van BeeHaive-framework in de organisatie (jaarlijkse alumni-survey) |
| Lagging | Door deelnemers gerapporteerde voorkomen AI-incidenten |
| Lagging | NPS en retentie voor vervolgcursussen |

### 8.4 Response-rates: realistische verwachting

**Wat het onderzoek zegt.** Response-rates dalen van ongeveer 80% (direct na sessie) naar 20–40% (delayed) [06]. Mitigaties:

- Korte surveys (max 5 minuten).
- Incentives (bijvoorbeeld een aanvullende resource na invullen).
- AI-bot kan survey conversationeel aanbieden — hogere response.

### 8.5 Iteratie-ritme rond pilot

**Wat het onderzoek zegt** [03]:

- Pilot van ~10 deelnemers is sweet spot: genoeg signaal, hoge feedback-diepte. Bij 5 mis je variatie; bij 25 verdrinkt het in ruis.
- **Bij voorkeur gemengd** in eerste pilot: verschillende sectoren en rollen, om PMF breder te testen.
- Gratis of sterk gereduceerd tarief, in ruil voor feedbackverplichting (diepte-interview na elke module).
- **PMF-signaal** (productled framework): cohort-retentie voor vervolgmodules, plus de Sean Ellis-vraag: "Hoe teleurgesteld zou je zijn als BeeHaive niet meer zou bestaan?". Target: meer dan 40% zegt "heel teleurgesteld" → PMF.
- Van pilot naar 50: herhaal eerst met cohort 2 (~15 deelnemers) met aanpassingen vóór schaling. Premature schaling is meest voorkomende fout.

**Iteratie-cadans:**

- Na elke module: 30-min retro met 2–3 deelnemers.
- Na afloop pilot: volledige decompositie per bouwsteen — wat snijden, wat verlengen, wat van modaliteit wisselen.

**Evidence-sterkte.** Matig (cohort-platform-praktijk; geen RCT).

---

## Bijlage A — Anti-patronen en neuromythes

Drie hardnekkige claims om uit alle BeeHaive-marketing en -content te schrappen, met de feitelijke onderbouwing:

### A.1 VAK / leerstijlen

**Claim.** "Sommige mensen zijn visuele leerders, anderen auditief, anderen kinesthetisch; matching aan voorkeursstijl verbetert leren."

**Waarom fout.** Pashler et al. (2008) en Newton (2015) en Frontiers meta-analyse (2024): geen empirische steun voor de meshing-hypothese [02]. Mensen hebben voorkeuren; dat is iets anders dan dat ze beter leren in die modaliteit.

**Vervang door.** "We gebruiken meerdere modaliteiten omdat (a) variatie cognitive load verlaagt, (b) herhaling via een ander kanaal de retrieval-cues verdubbelt (dual coding), (c) het toegankelijkheid verhoogt voor diverse contexten."

### A.2 70:20:10

**Claim.** "70% van leren gebeurt on-the-job, 20% sociaal, 10% formeel."

**Waarom fout.** Komt uit self-reports van ongeveer 200 executives (Lombardo, Eichinger, McCall, jaren tachtig). Geen empirische ratio [01].

**Vervang door.** "Voor blended training met professionals werkt circa 30% theorie en 70% toepassing als richtlijn, niet als wet."

### A.3 Learning Pyramid (Dale's cone met percentages)

**Claim.** "We onthouden 10% van wat we lezen, 20% van wat we horen, 90% van wat we onderwijzen."

**Waarom fout.** Niet empirisch onderbouwd. De percentages zijn na de oorspronkelijke piramide toegevoegd zonder bron [05].

**Vervang door.** "Onderwijzen aan anderen werkt omdat het retrieval en elaboration combineert (twee zeer sterk onderbouwde mechanismen)."

### A.4 "Ze vonden het leuk dus het werkt"

**Claim.** Hoge NPS of CSAT als bewijs van leereffect.

**Waarom fout.** Kirkpatrick-niveau 1 correleert zwak met niveau 2 en 3. Entertainerige trainers scoren hoger op reaction, niet op learning [03].

**Vervang door.** Niveau-1-meting alleen gecombineerd met niveau-2-meting (retrieval-score, capstone-rubric) en niveau-3-zelfrapportage rapporteren.

### A.5 Spaced repetition "verhoogt retentie met 200%"

**Claim.** Dramatische percentages-uitspraken in marketing.

**Waarom fout.** Peer-reviewed literatuur spreekt van medium-tot-grote effect-sizes; specifieke percentages variëren sterk per setting [04].

**Vervang door.** "Spaced repetition is een van de sterkst onderbouwde leertechnieken (meta-analytisch, decennia onderzoek)."

---

## Bijlage B — Checklist nieuwe training-opzet

Loop bij elke nieuwe training (of substantiële revisie) deze keuzes expliciet door. Per dimensie: kies en onderbouw met verwijzing naar het bijbehorende hoofdstuk.

### B.1 Formaat

- [ ] Cohort-grootte vastgesteld (10–20)? — H1.3
- [ ] Cohort versus self-paced gekozen? — H1.1
- [ ] Cadans bepaald (wekelijks default)? — H1.2
- [ ] Live-sessies op 60 minuten geprogrammeerd? — H1.3
- [ ] Flipped classroom als default toegepast? — H1.4
- [ ] Theorie-praktijk-ratio circa 30:70 in contacturen? — H1.5

### B.2 Curriculum

- [ ] Elke deelnemer heeft eigen governance-vraagstuk uit eigen organisatie? — H2.1
- [ ] Knowles-principes vertaald naar concrete designkeuzes per principe? — H2.2
- [ ] Scaffolding-tools aanwezig (canvas-templates, peer-rubrics, check-ins)? — H2.3
- [ ] Blocked introductie gevolgd door interleaved cases? — H2.4
- [ ] Capstone als transfer-mechanisme gepland? — H2.5

### B.3 Modaliteiten

- [ ] Geen leerstijlen-frame in marketing of content? — H3.1, A.1
- [ ] Mayer's 12 principes als checklist op video en infographics? — H3.2
- [ ] Per bouwsteen of guardrail: tekst + video + flashcards + infographic? — H3.3
- [ ] Audio-kwaliteit gecheckt (microfoon, geen achtergrondmuziek)? — H3.4
- [ ] Transcripties bij elke video en podcast? — H3.4
- [ ] Leesniveau B1–B2 in Nederlandstalige content? — H3.4

### B.4 Didactische werkvormen

- [ ] Worked example per bouwsteen of guardrail? — H4.1
- [ ] Peer review met rubric (4–6 criteria, concrete prompts)? — H4.2
- [ ] Live-sessies bevatten geen monoloog maar interactieve werkvormen? — H4.3
- [ ] Vaste subgroep-trio's voor de duur van de cohort? — H4.4

### B.5 Retentie

- [ ] Spaced-repetition-cadans ingericht (1, 3, 7, 16, 35, 90 dagen)? — H5.1
- [ ] Modules eindigen met 3–5 vrije-ophaalvragen? — H5.2
- [ ] Interleaved cases vanaf moment alle bouwstenen geïntroduceerd zijn? — H5.3
- [ ] Elaboration-prompt per module ("voorbeeld uit eigen organisatie")? — H5.4
- [ ] Eén infographic per bouwsteen of guardrail als visueel ankerpunt? — H5.5
- [ ] Concrete review-cyclus uitgewerkt voor de specifieke cursusduur? — H5.6

### B.6 Post-course

- [ ] Drip-cadans dag 1, 3, 7, 14, 30, 60, 90 ingericht? — H6.1
- [ ] Booster-sessies maand 1 en maand 3 geprogrammeerd? — H6.2
- [ ] Per-cohort community ingericht (geen alumni-mengelmoes)? — H6.3
- [ ] Maandelijkse nieuwsbrief en blog-cadans? — H6.4
- [ ] If-then plans aan eind van elke module, opgeslagen in bot? — H6.5

### B.7 AI-tutor

- [ ] RTRI-system-prompt opgesteld (Role/Task/Requirements/Instructions)? — H7.3
- [ ] RAG-grounding op alle cursuscontent (MDX, slides, transcripts, KG)? — H7.2
- [ ] Citaties verplicht bij elke feitelijke claim? — H7.2
- [ ] "Weet ik niet"-gedrag bij lage retrieval-confidence? — H7.2
- [ ] Pre- en post-LLM-guardrails geïmplementeerd? — H7.4
- [ ] LLM-as-judge-evaluatie als kwaliteitscheck? — H7.4
- [ ] Cognitive-offloading-mitigaties aanwezig (delayed testing, AI-free sessies)? — H7.5
- [ ] EU-hosting (Hetzner), TTL 90 dagen, DPIA, opt-in voor data-gebruik? — H7.6
- [ ] A/B-test bot-aan vs. bot-uit gepland voor eigen evidence-base? — H7.1

### B.8 Meting

- [ ] Kirkpatrick-meet-instrumenten per niveau gedefinieerd? — H8.1, H8.2
- [ ] Leading- en lagging-indicators vastgesteld? — H8.3
- [ ] Delayed post-tests dag 30/60/90 gepland? — H8.2
- [ ] Response-rate-mitigaties (kort, conversationeel via bot)? — H8.4
- [ ] Pilot-grootte ~10 voor eerste run, ~15 voor tweede? — H8.5
- [ ] PMF-vraag (Sean Ellis) na pilot? — H8.5
- [ ] 30-min retro na elke module met 2–3 deelnemers? — H8.5

### B.9 Anti-patronen

- [ ] Geen VAK / leerstijlen in marketing? — A.1
- [ ] Geen 70:20:10 als evidence-claim? — A.2
- [ ] Geen Learning Pyramid met percentages? — A.3
- [ ] Geen NPS als enig bewijs van effect? — A.4
- [ ] Geen overdreven percentage-claims over leertechnieken? — A.5

---

## Bijlage C — Bron-aggregaat

Voor de volledige bronvermelding per uitspraak: zie de zes deelrapporten. Hier de top-bronnen per dimensie als snelle ingang.

### Spaced repetition en retrieval practice

- Cepeda et al. (2008) Spacing effects in learning — meta-analyse 839 assessments. [`04`](training-design-2026-04/04-retentie-memory.md)
- Roediger & Karpicke (2006, 2008) Power of testing memory — testing effect.
- Rowland (2014) — meta-analyse, g=0.50.
- Dunlosky et al. (2013) — Improving Students' Learning with Effective Learning Techniques.

### Multimedia en dual coding

- Mayer (2021) Cognitive Theory of Multimedia Learning — 12 principes, >200 experimenten. [`02`](training-design-2026-04/02-didactiek-multimodaal.md)
- Clark & Paivio (1991) Dual Coding and Education.
- Newton (2015) Learning Styles Myth is Thriving — Frontiers in Psychology.
- Frontiers (2024) — meta-analyse leerstijlen-meshing-hypothese.

### Flipped classroom en cohort

- Sciencedirect (2025) Second-order meta-analysis flipped classroom (g≈0.58–0.73). [`03`](training-design-2026-04/03-didactiek-blended-pilot.md)
- Open Praxis (2024) MOOC completion rates.
- a16z / Maven — Cohorts are King.
- Boston College CTE — Synchronous Online Sessions.

### PBL en andragogiek

- Clair (2024) Andragogy: Past and Present Potential — *New Directions for Adult and Continuing Education*. [`01`](training-design-2026-04/01-didactiek-pbl.md)
- CDC (2024) Adult Learning Principles.
- IES — Intelligent Scaffolding for Peer Reviews.
- ATD — 70:20:10 Where is the Evidence.

### Implementation intentions en post-course

- Gollwitzer & Sheeran (2006) Meta-analysis Implementation Intentions, d=0.65. [`05`](training-design-2026-04/05-retentie-postcourse.md)
- APA (2021) Peer interaction meta-analysis.
- Transfer E-Booster Study — ScholarSpace Hawaii.

### AI-tutors en RAG

- Liu et al. — Teaching CS50 with AI (SIGCSE 2024). [`06`](training-design-2026-04/06-ai-tutor.md)
- J-PAL — AI-Powered Tutoring Khanmigo.
- Rori (Ghana) — peer-reviewed RCT WhatsApp math tutor.
- UPenn (2024) — ChatGPT cognitive offloading studie.
- MEGA-RAG, MetaRAG (2025) — RAG-grounding evaluatie.
- Arthur AI, Confident AI, Datadog — guardrails best-practices.

### Privacy / AVG

- moinAI, Premai, Quickchat (2026) — GDPR-compliant chatbot guides.
- EU AI Act + AVG overlap — DPIA-vereisten.

### Kirkpatrick en meting

- Kirkpatrick Partners — The Kirkpatrick Model (originele 1959, herzien 2016).
- AllenComm (Mar 2026) — Corporate Training Metrics Beyond Completions.
- ProductLed — Framework for Driving PMF Through Pilots.

---

## Onderhoud van dit document

Dit document is een levende synthese. Werk het bij wanneer:

- Nieuwe research uitkomt die een aanbeveling versterkt of weerlegt.
- Een eigen pilot data oplevert die afwijkt van de verwachte effect-sizes (pas zowel het training-ontwerp als dit document aan).
- De BeeHaive-stack of -content significant verandert (bijvoorbeeld nieuwe bouwstenen of guardrails worden toegevoegd).

Bij grotere updates: bump de versienummer in de header en log de wijziging in een korte changelog onder dit kopje.

### Changelog

- **1.0 (2026-04-28)** — initiële versie op basis van zes deelrapporten van april 2026.
