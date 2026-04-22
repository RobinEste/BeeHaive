# KNW-2026-054: Quote-sourcing — kies een citaat dat specifiek over de BB gaat, niet over het overkoepelende concept

> **Categorie:** development
> **Datum:** 2026-04-22
> **Sessie-context:** BB_03 Dynamic Context-quote vervangen van Tobi Lütke (over context engineering breed) naar Tiago Forte (specifiek over context-curatie en -levering)
> **Relevantie:** midden

## Inzicht

Als een BB (of GR, of sectie) een specifiek onderdeel van een breder vakgebied beschrijft, moet de openings-quote óók over dat specifieke onderdeel gaan — niet over het overkoepelende concept. BB_03 Dynamic Context is één van twee lagen van "context engineering" (de andere is Prompt Design). Tobi Lütke's beroemde quote definieerde context engineering in zijn totaliteit. Op BB_03 leek hij misleidend: de lezer kan denken dat "context engineering = Dynamic Context", terwijl de pagina zelf uitlegt dat Dynamic Context slechts één van zes componenten is. Tiago Forte's formulering *"The new bottleneck isn't intelligence, time, or attention. It's curating and delivering the right context to AI"* is direct over het curatie-en-leveringsprobleem dat BB_03 centraal stelt — dat valt niet over de statische laag die Prompt Design afdekt.

## Context

BB_03 opende met Lütke's quote. Robin leste de pagina, zag dat we elders expliciet maken dat context engineering beide BB's (03 en 04) omvat, en constateerde: *"Ik vind de quote bovenaan nog niet goed genoeg: bovendien is die breder dan dynamic context. Hebben we nog alternatieven?"* Zoeken in `docs/research/dynamic-context-2026/` leverde drie BB_03-specifieke kandidaten (Atlan, Anthropic, Chroma). Zoeken in NI-bronnen (vault) leverde twee extra (Tiago Forte, Ethan Mollick). Forte won op twee criteria: (1) semantisch bijna letterlijke echo van de tagline *"De juiste informatie op het juiste moment"*, en (2) Forte is al in onze onderzoeksbronnen als auteur van Personal Context Management, wat directe link geeft naar bron-080.

## Geleerd

### Wat werkte
- **Expliciete specificiteits-check**: is deze quote *over* de BB, of over het *bredere vakgebied waar de BB in zit*? Eerste is goed, tweede vaak misleidend.
- **Tagline-echo-test**: past de quote qua kernbegrip bij de tagline? De tagline is al BB-specifiek; als de quote daar letterlijk of bijna-letterlijk bij aansluit, versterken ze elkaar.
- **Bron-gedekte-autoriteit**: kies bij voorkeur iemand die al elders in je kennisbank/onderzoek als expert is ingebed. Forte → bron-080 (PCM). Zo koppel je de quote aan bewezen inhoudelijk gezag.
- **Alternatieven-lijst** met korte plus/min per kandidaat: helpt Robin sneller kiezen dan één-optie-voorleggen.

### Wat niet werkte
- Een beroemde quote kiezen vanwege naamsbekendheid, terwijl de inhoud breder is dan de BB. Lütke is bekender dan Forte, maar Forte past beter.
- Aannemen dat "de eerste quote die in research-documenten staat" de juiste is. Vaak staan er meerdere en moet je actief kiezen op specificiteit.

### Waarom
Een hero-quote is een signaal-versterker. Als hij over een breder concept gaat dan de pagina zelf, stuurt hij lezers in een richting die de rest van de pagina moet corrigeren. Dat is inefficiënt en potentieel verwarrend. Specifiek-passende quotes versterken de focus van de pagina en maken de tagline geloofwaardiger in plaats van concurreren ermee.

## Toepassing

Bij elke BB/GR-pagina, blogpost of andere publicatie met een openings-quote:

1. **Formuleer eerst wat deze pagina specifiek beweert** (niet wat het bredere vakgebied beweert). Schrijf een zin van 10-15 woorden.
2. **Zoek een quote die overlappt met die specifieke bewering**, niet met het bredere kader. Eerst in eigen onderzoekspakket, daarna in vault-bronnen, dan externe bronnen.
3. **Lezers-test**: vraag een lezer *"waar gaat deze pagina over?"* na alleen de quote + tagline te hebben gezien. Als het antwoord breder is dan de pagina zelf, is de quote te breed.
4. **Bij twijfel**: geef 2-3 kandidaten aan de redacteur (of aan Robin) met expliciete plus-min, niet één optie. De keuze is subjectief genoeg dat deliberate afweging de moeite waard is.
5. **Bron moet verifieerbaar zijn**: liefst publiek URL + datum. Als geen URL bestaat (PDF, webinar), noteer dat expliciet in de provenance van de research.
