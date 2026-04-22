# KNW-2026-050: Em-dash drift — AI-schrijvers vallen terug op Engelse interpunctie, ook in NL-regels

> **Categorie:** development
> **Datum:** 2026-04-22
> **Sessie-context:** BB_03 Dynamic Context lees-review met Robin — 76 keer het patroon `**term** —` gecorrigeerd naar `**term**:`, daarna BB_01 Knowledge en BB_04 Prompt Design nog ~40 keer
> **Relevantie:** hoog

## Inzicht

Claude (en vergelijkbare modellen) heeft em-dashes diep ingebakken vanuit Engelstalige training. In Nederlandse tekst leidt dit tot een hardnekkig foutpatroon: losse em-dashes waar een komma, puntkomma of dubbele punt hoort, en vooral `**vet woord** —` na bullet-labels waar NL `**vet woord**:` eist. Nog opvallender: **het model maakt deze fout zelfs terwijl hij de regel uitlegt of een voorstel formuleert dat de regel implementeert**. Dat maakt het geen incidentele vergissing maar een trainings-artefact dat actieve tegen-maatregelen vereist.

## Context

Tijdens de BB_03-lees-review identificeerde Robin het patroon `**X** —` (bold gevolgd door em-dash gevolgd door definitie) op 76 plekken in één bestand. Na vastlegging in de stijlgids werd in de volgende iteratie hetzelfde patroon ook in andere BB-bestanden gevonden (~40). Nog tekenender: toen Robin vroeg om de Quick Start op drie niveaus te herschrijven — direct nadat de em-dash-regel was aangescherpt — gebruikte het voorstel opnieuw losse em-dashes. Robin: *"Let op bij de aanpassingen in quick start: daar gebruik je weer '-', blijft lastig he."*

## Geleerd

### Wat werkte
- Een programmatische scan met Python (`line.count(' — ') % 2 == 1`) om losse em-dashes te detecteren. Geen interpretatie, gewoon een teller; alles met oneven aantal is verdacht.
- Een meta-regel in de stijlgids die expliciet waarschuwt dat de fout terugkomt in eigen concept-voorstellen: *"Voor je een concept-zin, herschreven alinea of Quick Start-voorstel presenteert: scan je eigen tekst op ` — ` en vervang eerst."*
- Het onderscheid dubbel-vs-enkel: em-dashes zijn geldig als ze een tussenzin omsluiten (dubbel, begin én eind), maar losstaand bijna altijd fout in NL. Deze regel is goed te grepen.

### Wat niet werkte
- Vertrouwen op "ik heb de regel nu uitgelegd" — de volgende zin die het model produceerde had er alweer één in.
- Generieke stijlregels zonder concrete check-commando. "Gebruik em-dashes spaarzaam" is onvoldoende specifiek; een reviewer moet weten wanneer precies wel/niet.

### Waarom
Em-dashes zijn in Engelstalige content (en dus in het trainingscorpus) de geprefereerde interpunctie voor zin-koppels, parenthetische uitweidingen en definities-na-term. In Nederlandse tekst worden ze veel spaarzamer gebruikt; daar zijn `:`, `;`, `,` en simpelweg zin-opbreken de conventie. De ingebakken Engelse voorkeur overstemt de geformuleerde NL-regel, tenzij er een *mechanische* check bij zit.

## Toepassing

Bij elke NL-schrijfopdracht in de codebase:

1. **Leg de regel expliciet mechanisch vast** — niet "spaarzaam" maar "zoek in diff op ` — ` en elke hit moet dubbel zijn, anders herformuleren".
2. **Voer een em-dash-count uit als laatste stap**, vóór commit en vóór het presenteren van een concept-voorstel. Klein Python-snippet volstaat.
3. **Behandel het als training-artefact, niet als incidentele slordigheid.** Planning rekening houden: elke substantiële NL-schrijftekst levert tientallen em-dash-correcties op. Budgetteer tijd ervoor of automatiseer vroeg.
4. **Zelfde principe geldt voor andere diep-ingebakken Engelse gewoonten**: letterlijk vertaalde idiomen ("alles en de keukenkraan", "aan het einde van de dag"), Engelse bullet-labels in NL-contexten, Engelse afkortingen zonder expansie. Elke categorie heeft een eigen check nodig.
