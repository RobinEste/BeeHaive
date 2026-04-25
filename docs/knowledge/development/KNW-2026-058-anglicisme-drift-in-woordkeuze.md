# KNW-2026-058: Anglicisme-drift in woordkeuze — sibling van em-dash drift

> **Categorie:** development
> **Datum:** 2026-04-25
> **Sessie-context:** BB_01 Knowledge tweede lees-review — Robin flagde meerdere anglicismen achter elkaar: *"litmustest"*, *"contradictoir"*, *"amplificeren"*, *"rubberstamp"*, *"versioneerd"*. Stijlgids-bb noemt al "vermijd Engelstalig vakjargon", maar het sluipt elke keer terug
> **Relevantie:** midden

## Inzicht

Net als bij interpunctie ([KNW-2026-050](../development/KNW-2026-050-em-dash-drift-bij-ai-schrijvers.md): em-dash drift) heeft AI-assistentie in NL-content een hardnekkige neiging tot Engels jargon waar gangbare Nederlandse alternatieven bestaan. Dezelfde mechaniek (training-corpus overstemt geformuleerde regel), maar een andere categorie: dit is geen interpunctie maar woordkeuze. Vereist een eigen, eigen mechanische check — de em-dash-scan vangt het niet, en de algemene stijlgids-regel is te abstract om in concept-fase te triggeren.

## Context

Tijdens BB_01 Knowledge lees-review werden in één sessie meerdere Engelse leenwoorden gevlagd waar Nederlands gangbaar was:

| Engels jargon | Nederlands |
|---------------|-----------|
| litmustest | lakmoesproef |
| contradictoir | tegenstrijdig |
| amplificeren | versterken |
| rubberstamp | (geen NL-vorm — vervangen door "formaliteit zonder werkelijk oordeel") |
| versioneerd | versiebeheer (verbgebruik vermeden) |
| compoundert | "zich opstapelt" / "kennis en instrumenten die zich opbouwen" |

Stijlgids-bb (`/Users/robin/.claude/agents/shared/schrijfstijl-bb.md`) noemt al *"vermijd Engelstalig vakjargon waar Nederlandse equivalenten bestaan"*, maar in concept-voorstellen sluiten ze toch elke keer in. Het patroon overlapt met KNW-050 (em-dash drift), maar:

- **KNW-050** = interpunctie (mechanisch te scannen op ` — `)
- **KNW-058** = woordkeuze (geen mechanische scan; vereist NL-taalkennis)

## Geleerd

### Wat werkte
- Robin's per-instance flag (*"X is geen NL woord"*) werkt direct en voedt een groeiende lijst.
- Mensen herkennen anglicismen vrijwel onmiddellijk; het is een lees-check, niet een schrijf-check.
- Bij elke flag direct vervangen én begrijpen waarom (bijv. "rubberstamp" niet vertalen maar omschrijven, omdat de NL-vorm niet bestaat).

### Wat niet werkte
- Vertrouwen op de stijlgids-regel "vermijd Engels jargon". Te abstract om tijdens generatie te triggeren — modellen kiezen op semantische passendheid in de mix-context, niet op "is dit gangbaar Nederlands".
- Een algemene scan met regex of pattern-match: anglicismen herkennen vereist Nederlandse taalkennis, geen patroon-detectie.
- Vertrouwen dat één gevlagde term het probleem oplost ("nu weet ik het"). De volgende alinea heeft een nieuwe.

### Waarom
LLMs zijn getraind op een corpus waarin Engels vakjargon vrijuit in NL-tekst voorkomt (academisch NL, tech-NL, consultancy-NL, vertaalde managementliteratuur). Het model leest die mix als normaal. Tijdens generatie kiest het model dan een term op basis van semantische passendheid in de mix-context, niet op basis van "is dit gangbaar Nederlands voor deze doelgroep". Dit verschilt van em-dash drift in mechaniek (woordkeuze versus interpunctie), maar de oorzaak is identiek: trainings-artefact dat geformuleerde regels overstemt.

## Toepassing

Bij elke NL-schrijfopdracht waar lezerstaal centraal staat:

1. **Bouw een groeiende drift-lijst per project op** met bekende anglicisme-equivalenten (lakmoesproef, tegenstrijdig, versterken, ...). Scan elke concept-tekst hierop. Voeg nieuwe vondsten direct toe.
2. **Mens-leesronde door iemand met sterke NL-taalkennis is essentieel.** AI ziet anglicismen niet zelf; de tekst leest voor het model correct.
3. **Bij flag van een nieuw anglicism**: vraag of er een gangbare NL-vorm is. Zo nee (zoals "rubberstamp"): omschrijf, niet vertalen.
4. **Behandel als sibling van em-dash drift** ([KNW-2026-050](./KNW-2026-050-em-dash-drift-bij-ai-schrijvers.md)) — beide zijn diep ingebakken trainings-artefacten die per categorie een eigen check nodig hebben. De Toepassing-stap 4 van KNW-050 voorspelt dit ("zelfde principe geldt voor andere ingebakken Engelse gewoonten"); dit KNW operationaliseert het voor woordkeuze.
5. **Specifiek voor BeeHaive content**: voeg gevlagde anglicismen toe aan `schrijfstijl-bb.md` als groeiende lijst, niet alleen als algemene regel. Concrete voorbeelden voorkomen herhaalde flags op dezelfde termen.
