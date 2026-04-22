# KNW-2026-051: Pseudonimiseren vs anonimiseren — het juridische verschil maakt compliance-eisen conditioneel

> **Categorie:** avg-privacy
> **Datum:** 2026-04-22
> **Sessie-context:** BB_03 Dynamic Context lees-review — Robin signaleerde dat het evidence-item "register van geredigeerde persoonsgegevens en data-herkomst" gepresenteerd werd als universele eis, terwijl dat alleen geldt bij pseudonimisering, niet bij echte anonimisering
> **Relevantie:** hoog

## Inzicht

Pseudonimisering en anonimisering worden in de praktijk door elkaar gebruikt, maar hebben fundamenteel verschillende AVG-status. **Pseudonimisering** (AVG art. 4 lid 5) houdt een sleutel tot de persoon; data blijft persoonsgegeven, AVG-plichten blijven gelden, en alle rechten (inzage, vergetelheid, verwerkingsregister) zijn *uitvoerbaar* omdat de mapping bestaat. **Volledige anonimisering** (AVG overweging 26) ontdoet data onomkeerbaar van identificerende kenmerken; data valt buiten de AVG, en de bovenstaande rechten zijn niet alleen niet-vereist maar ook *niet-uitvoerbaar* — je kunt een verwijderverzoek niet honoreren als je niet meer weet welk record bij welke persoon hoort.

Gevolg: compliance-checklists die deze twee op één hoop gooien leveren ofwel verkeerde eisen (anonimisering kan niet voldoen aan art. 17) ofwel valse geruststelling (pseudonimisering laat plichten bestaan die je misschien niet ziet).

## Context

De evidence-lijst van BB_03 Dynamic Context bevatte de formulering: *"Register van geredigeerde persoonsgegevens en data-herkomst: elk antwoord is traceerbaar naar het bronfragment, het moment van indexering en de verwijderlog"*. Robin vroeg: *"Is dit een gegeven of kan hier ook van afgeweken worden?"*, en na de eerste uitleg: *"Maar dit is toch alleen zo als je pseudonimiseerd, als je anonimiseert kun je dit niet doen."* Dat was precies de juridische nuance: het item gold universeel alleen als we aannemen dat er PII bij zit; bij anonimisering vervalt zowel de plicht als de mogelijkheid.

## Geleerd

### Wat werkte
- **Conditioneel formuleren** van het evidence-item: *"Bij pseudonimisering: register met mapping persoon ↔ pseudoniem en data-herkomst per antwoord (bronfragment, moment van indexering, verwijderlog), zodat AVG-rechten op inzage en vergetelheid uitvoerbaar zijn. Bij volledige anonimisering vervalt dit; geanonimiseerde data is geen persoonsgegeven meer."*
- **Een aparte body-subsectie** "Pseudonimiseren is niet hetzelfde als anonimiseren" die het verschil juridisch uitlegt (art. 15, 17, 30 + overweging 26) én praktisch (welke keuze past wanneer).
- **De praktische vuistregel benoemen**: voor RAG is pseudonimisering meestal het aangewezen pad, omdat je verbanden tussen documenten wilt behouden (zelfde BSN = zelfde pseudoniem). Volledige anonimisering is strenger maar ook beperkender.

### Wat niet werkte
- Universele formulering. *"Register van geredigeerde persoonsgegevens"* leek rond, maar gaf lezer de indruk dat dit bij élk AI-systeem verplicht is — ook wanneer er geen PII of wanneer er volledige anonimisering is.
- Stap 2 "persoonsgegevens in vrije tekst redigeren" (NER) wordt makkelijk verward met anonimiseren. Redigeren van namen maakt tekst níet automatisch anoniem als combinaties (postcode + geboortedatum) nog herleidbaar zijn.

### Waarom
De AVG kent geen tussenstatus. Je data is of persoonsgegeven (alle plichten) of niet (geen plichten). Pseudonimisering is een *beveiligingsmaatregel* binnen de persoonsgegeven-categorie, geen overstap ernaar-buiten. Anonimisering is wel een overstap, maar alleen als je aantoonbaar élk identificatiepad hebt afgesneden — inclusief combinaties en context-reconstructie. Dat is technisch moeilijk en wordt in de praktijk overschat.

## Toepassing

Bij elke BB-pagina, AI-architectuur-ontwerp of compliance-checklist waar persoonsgegevens in RAG/kennisbank voorkomen:

1. **Maak compliance-items conditioneel op de gekozen beschermingsmaatregel.** Formuleer: "Bij pseudonimisering: ..."; "Bij volledige anonimisering: dit vervalt"; "Zonder PII in deze bron: n.v.t.".
2. **Positioneer pseudonimisering vs anonimisering als een bedrijfsbeslissing, geen IT-keuze.** De keuze heeft directe AVG-gevolgen en bepaalt welke rechten uitvoerbaar blijven. Laat een jurist of DPO meelezen.
3. **Wees expliciet over wat redigeren (NER) oplevert**: het is pseudonimisering-achtig zolang niet alle (in)direct identificerende kenmerken en combinaties weg zijn. Anders is het niet anoniem, alleen minder-identificeerbaar.
4. **Leg de juridische verwijzing eenmaal goed uit** (art. 15 = inzage, art. 17 = vergetelheid, art. 30 = verwerkingsregister, overweging 26 = definitie anoniem) en koppel daar je check-items aan. Dat maakt later onderhoud en audit makkelijker dan losse items.
