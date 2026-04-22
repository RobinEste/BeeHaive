# KNW-2026-053: Hover-tooltip op glossary-links verandert het inline-uitleg-patroon structureel

> **Categorie:** development
> **Datum:** 2026-04-22
> **Sessie-context:** Hover-tooltip-component (`GlossaryTooltip.astro`) toegevoegd aan BB-detail-pagina's; daarna moest schrijfstijl-bb.md een nieuwe §15 krijgen omdat bestaand inline-parenthese-patroon nu duplicaat werd
> **Relevantie:** hoog

## Inzicht

Schrijfstijlregels zijn niet onafhankelijk van de rendering-context. Zodra een hover-tooltip op `/begrippen#slug`-links de volledige definitie toont, wordt de gebruikelijke *"bij eerste gebruik inline uitleggen"*-regel (§1 parafrase) deels overbodig voor termen die in de glossary staan. `[MCP](/begrippen#mcp) — het Model Context Protocol` levert de lezer tweemaal dezelfde info: één keer in de parenthese, één keer in de tooltip bij hover. De patroon-keuze *wat-leg-je-inline-uit-vs-wat-laat-je-aan-glossary-over* wordt afhankelijk van of er een tooltip is. Wie de tooltip bouwt moet ook de inline-stijl herzien.

## Context

Bij het BB_03 Dynamic Context-herschrijven had ik consequent het patroon `[glossary-term](/begrippen#slug) — korte uitleg` toegepast: link plus parenthese. Dat was conform §1 van de schrijfstijlgids. Nadat de GlossaryTooltip-component was toegevoegd en alle definities client-side als tooltip verschenen, vroeg Robin: *"soms zie je in een website ook dat de definitie zichtbaar wordt als je op het woord gaat staan, kan dat ook?"*. Dat leidde tot implementatie, waarna bleek dat de inline parentheses nu letterlijk hetzelfde zeiden als de tooltip. Voorbeeld: `via [CDC — Change Data Capture](/begrippen#cdc)` bevat de expansie binnen de link-tekst zelf, terwijl de tooltip diezelfde expansie al toont — drievoudige herhaling op hover. Opruimen leverde concreet vrijere zinnen en betere leesbaarheid.

## Geleerd

### Wat werkte
- **Nieuwe §15-regel**: *"Sinds hover-tooltips op `/begrippen#slug`-links werken, toont de tooltip automatisch de volledige uitleg. Inline parenthese na de link is dan duplicaat. Link plaatsen en parenthese weglaten, tenzij de vloeiendheid van de zin echt lijdt onder de bondigheid."*
- **Scan-commando** om redundantie te vinden: `grep -nE '\[[^\]]+\]\(/begrippen#[^)]+\) (—|\()` — elke hit is een kandidaat voor opruimen.
- **Escape-clausule**: "tenzij de zin anders onleesbaar wordt". Niet blind alle parentheses wegvegen; soms draagt de parenthese bij aan ritme of disambiguatie.

### Wat niet werkte
- Stijlregels isoleren van rendering. De §1-regel "vakterm bij eerste gebruik uitleggen" is correct als er geen tooltip is; met tooltip wordt hij te streng. Zonder herziening bleven de pagina's cluttered met duplicate info.
- Aannemen dat toevoegen van een UX-feature alleen een "design-ding" is. In deze codebase raakt elke contentstijl-regel direct aan wat goed rendert. Als je iets toevoegt dat informatie oppervlakkig verandert (hover, tooltip, modal, progressive disclosure), moet je de schrijfregels opnieuw toetsen.

### Waarom
Content is geen platte tekst; hij wordt gerenderd binnen componenten die extra lagen kunnen toevoegen (tooltip, expand-on-click, sidenote-popup). Die lagen kunnen dezelfde informatie-functie vervullen als inline-parentheses, waardoor de stijlregel die de inline-parenthese voorschreef niet meer optimaal is. Schrijfregels zonder rendering-context zijn daarom inherent incompleet.

## Toepassing

Bij elke nieuwe UX-feature die content-informatie op een andere manier oppervlakkig maakt (tooltip, modal, drawer, hover-card, footnote-popup):

1. **Check welke schrijfstijlregels het raakt.** Parentheses, definities-op-eerste-gebruik, afkorting-expansies, voetnoten — alles wat de feature "ook al doet" wordt kandidaat voor opruimen.
2. **Werk de schrijfstijlgids bij** met een regel over wanneer de inline-vorm vervalt. Vergeet de escape-clausule niet ("tenzij zin-vloeiendheid lijdt" of equivalent).
3. **Draai een opruim-scan** over bestaande content om accumulatie van duplicate info weg te halen. Dat is een eenmalige investering met doorlopende winst.
4. **Omgekeerd**: als je een UX-feature verwijdert (tooltip uit, glossary weg), herstel dan de inline-uitleg — anders raakt informatie verloren.

Dit geldt breed: elke schrijfregel moet samen met zijn rendering-context worden onderhouden. Wie de layer bouwt, moet de layer-boven herzien.
