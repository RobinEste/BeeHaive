# KNW-2026-057: Numerieke claims uit tabellen expliciet uitwerken in proza

> **Categorie:** development
> **Datum:** 2026-04-25
> **Sessie-context:** BB_01 Knowledge tweede lees-review — proza zei *"De trust chasm is 52 punten"* na een tabel met executives-versus-werknemers cijfers. Robin: *"Wat bedoel je hiermee?"*
> **Relevantie:** midden

## Inzicht

Wanneer in proza een getal staat dat is afgeleid uit een tabel ("De trust chasm is 52 punten"), moet die afleiding expliciet zijn — anders moet de lezer terug naar de tabel en zelf rekenen, met het risico dat hij de verkeerde rijen pakt of de bewering niet kan valideren. De norm: noem zowel input-waarden als verschil ("een vertrouwenskloof van 52 procentpunten — 61% versus 9%"), zodat de berekening in één visueel sweep zichtbaar is. Vermijd tegelijk het muntten van nieuwe jargontermen ("trust chasm", "X-gap") als gangbaar Nederlands volstaat.

## Context

Een tabel in BB_01 toonde verschillen tussen executives en werknemers in vertrouwen in AI:

| Meting | Uitkomst |
|--------|----------|
| Werknemers vertrouwt AI voor complexe beslissingen | 9% |
| Executives vertrouwt AI voor complexe beslissingen | 61% |
| Executives: tools zijn adequaat | 88% |
| Werknemers: tools zijn adequaat | 21% |

De proza erna zei alleen: *"De trust chasm is 52 punten; de tool-adequaatheidsgap 67 punten."* Robin vroeg wat dat betekende. De getallen waren berekeningen (61% − 9% = 52, en 88% − 21% = 67), maar de proza dwong de lezer om zelf:
1. De juiste rijen te vinden in de tabel
2. De aftrekking uit te voeren
3. Te vertrouwen dat de auteur de juiste rijen koos

Bovendien gebruikte de proza Engels jargon ("trust chasm", "tool-adequaatheidsgap") voor wat eigenlijk gewoon "verschil" of "kloof" is.

Aangepast naar: *"Tussen leiders en medewerkers gaapt een vertrouwenskloof van 52 procentpunten in AI voor complexe beslissingen (61% versus 9%), en een kloof van 67 procentpunten in het oordeel of de tools voldoen (88% versus 21%)."*

## Geleerd

### Wat werkte
- Expliciet uitschrijven met parenthetische berekening: "(X% versus Y%)" maakt de berekening visueel direct verifieerbaar.
- Engels jargon ("trust chasm") vervangen door Nederlandse beschrijving ("vertrouwenskloof").
- Combineren van meerdere getallen uit dezelfde tabel in één zin met dezelfde structuur — de lezer ziet het patroon.

### Wat niet werkte
- Aanname dat de lezer de tabeldata vasthoudt en de berekening parallel uitvoert. Niemand doet dat.
- Jargontermen die de lezer niet eerder heeft gezien, geïntroduceerd zonder definitie.
- Het verschil benoemen zonder de input-waarden — de bewering is dan niet falsifieerbaar voor de lezer.

### Waarom
Een tabel is een aparte visuele eenheid. Ogen leven niet automatisch terug naar de juiste rij wanneer een getal in proza valt. De cognitieve overhead om "trust chasm = 52" te valideren is hoog: scrol terug, zoek de rijen, doe de aftrekking, vertrouw de auteur. Het muntten van termen als "trust chasm" voegt daar een extra laag ondoorzichtigheid aan toe; de lezer moet niet alleen het getal valideren maar ook de definitie van de term raden.

## Toepassing

Bij proza die een getal uit een tabel of dataset haalt:

1. **Schrijf de berekening als parenthetische uitwerking**: "(X% versus Y%)" of "(X uit Y)". De lezer kan in één blik valideren.
2. **Vermijd nieuwgemunte jargontermen** ("trust chasm", "X-gap", "Y-divide") als basis Nederlands volstaat ("verschil", "kloof", "afstand").
3. **Bij meerdere getallen uit dezelfde tabel**: combineer in één zin met dezelfde structuur, zodat het patroon visueel zichtbaar wordt.
4. **Test door zelf de zin te lezen zonder de tabel**: kun je de bewering bevestigen? Zo nee, voeg de berekening toe.
5. **Specifiek voor BeeHaive content**: deze regel geldt vooral voor BB-pagina's met onderzoeksdata-tabellen (jagged frontier %, FOBO-cijfers, deskilling-percentages). Elk getal dat in proza wordt aangehaald: input-waarden + berekening tonen.
