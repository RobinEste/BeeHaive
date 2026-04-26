# KNW-2026-059: Externe framework-typen niet uit context reconstrueren — primaire bron eerst

> **Type:** failure
> **Categorie:** process
> **Datum:** 2026-04-26
> **Sessie-context:** BB_02 Client Blueprint — eerste-concept noemde verzonnen unFIX value-stream-typen
> **Relevantie:** hoog

## Inzicht

Bij het schrijven van content over externe frameworks (unFIX, Anthropic-patronen, EU AI Act, OWASP, Gartner) is een plausibel-klinkende reconstructie uit context gevaarlijk. Engelse frameworks hebben specifieke benamingen die niet uit "wat logisch lijkt" af te leiden zijn. Pre-write feiten-check tegen primaire bron is niet optioneel.

## Failure Autopsy

### Decision

In de eerste-concept-versie van BB_02 BBDisclosure 1 ("Toegevoegde waarde voor de klant is hét uitgangspunt") werden de unFIX value-stream-typen genoemd als: **Customer Stream, Internal Stream, Innovation Stream, Operational Stream**. Deze klonken plausibel binnen de organisatorische framing van het concept, maar werden niet geverifieerd tegen de primaire bron `unfix.com/value-streams`. De seed.py KI "Appelo — unFIX Value Streams" werd met dezelfde typen ingevuld. Beide gingen door alle reviews (eigen pre-write-scan + astro check + commit + push).

Werkelijke unFIX-typen volgens primaire bron: **Product Value Stream, Service Value Stream, Event Value Stream, Project Value Stream**. Volledig andere taxonomie.

### Why it hurt

- **Inhoudelijke onjuistheid live op origin/main**: één commit met fout, één fix-commit. De fout zat ~30 minuten op main staan met push.
- **Tijd in herstel**: WebFetch op unfix.com om te verifiëren, MDX-tekst herwoorden inclusief uitbreiden met Appelo's eigenlijke definitie en SAFe-deviatie, seed.py KI corrigeren, Neo4j herseeden, extra commit.
- **Vertrouwens-kost**: Robin's vraag "Wat is de definitie van een value-stream die Appelo hanteert en verschilt die van onze definitie?" was niet "klopt dit" maar "wat is dit?" — en juist díe vraag onthulde dat ik iets had opgeschreven dat niet klopte. Lees-review als laatste verdedigingslinie werkte; eerdere stappen niet.
- **Skill-impact**: aanleiding voor /bb-write Stap 6.8 (inhoudelijke-feiten-check) — pre-existing schade dus deels compenseerbaar door procedure-aanpassing.

### What to do instead

1. **Bij elke claim over een extern framework** (typeringen, nummeringen, fasen, namen, datums): primaire bron raadplegen of een lokaal `verified`-stempel zoeken vóór schrijven. Geen reconstructie uit context.
2. **Cheap signal**: als de naam alfabetisch logisch klinkt of past bij wat je verwacht, verhoogt dat het risico op verzinning, niet de waarschijnlijkheid van waarheid.
3. **Concrete check-volgorde**:
   - Eerst lokale `docs/research/<slug>/`-pakketten — zoek `verified`-stempel of citaat uit primaire bron
   - Dan WebFetch op de primaire URL (framework-eigen site, niet wikipedia/blog)
   - Pas dan opschrijven, met bron-URL bij de claim
4. **Pre-write-scan-uitbreiding (Stap 6.8 in /bb-write)**: voor elk extern-framework-claim moet je expliciet de primaire-bron-URL kunnen noemen voordat je het opschrijft. Als je dat niet kunt, schrap de claim of label hem `inferred`.

## Geleerd

### Wat werkte

- **Lees-review als laatste linie**: Robin's vraag onthulde de fout binnen één review-cyclus.
- **Snelle correctie-loop**: Edit + verify + reseed + commit + push in <5 minuten zodra de fout gediagnostiseerd was.
- **Skill-uitbreiding direct doorgevoerd**: /bb-write Stap 6.8 toegevoegd in zelfde sessie, met expliciete vermelding van deze incident.

### Wat niet werkte

- **Pre-write-scan op feiten ontbrak**: /bb-write skill had alleen tekst-stijl-scans (em-dash, vetgedrukt, kop-toets), geen feit-verificatie.
- **Plausibiliteit verwarde met juistheid**: Customer/Internal/Innovation/Operational klonk als een coherente taxonomie, dus geen alarmbel.
- **Citaat-format verhulde de risico**: door het tussen *italics* te zetten leek het op een geverifieerde uitspraak.

### Waarom

LLM's reconstrueren plausibele structuren uit context — ook waar feiten geverifieerd moeten worden. Engelse frameworks hebben naamconventies die niet door logica af te leiden zijn. Zonder expliciete primaire-bron-stap glipt verzinning door.

## Toepassing

- **Bij /bb-write Stap 6.8 elke keer toepassen**: voor elk extern-framework-claim primaire-bron-URL kunnen noemen.
- **Voor andere BB's met extern-framework-content** (Tool Integration: MCP-features, Anthropic-patronen; Model Engines: model-naamgeving en versies; Evaluation Loop: eval-frameworks zoals RAGAS, LangSmith): zelfde discipline.
- **Bij twijfel labelen als `inferred`**: liever een eerlijk inferred-stempel dan een verzonnen autoriteit.
