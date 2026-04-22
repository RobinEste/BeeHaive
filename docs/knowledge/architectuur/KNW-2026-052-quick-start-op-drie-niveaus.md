# KNW-2026-052: Quick Start op drie niveaus — strategisch, tactisch, operationeel

> **Categorie:** architectuur
> **Datum:** 2026-04-22
> **Sessie-context:** BB_03 Dynamic Context lees-review — Robin vroeg de Privacy-sectie top-down te benaderen met drie rol-niveaus, en trok die structuur vervolgens door naar de Quick Start van de BB-frontmatter
> **Relevantie:** hoog

## Inzicht

Content die een *framework* of *bouwsteen* beschrijft heeft meerdere lezersrollen tegelijk: directie beslist *of* er geïnvesteerd wordt, domain-owners bepalen *hoe* het georganiseerd wordt, developers bouwen de technische *wat*. Een Quick Start die alleen op operationeel niveau staat ("begin met chunking", "structureer je prompt") laat de eerste twee rollen in de kou staan — ze weten niet wat hun eerste stap is. De structurele oplossing is elke Quick Start expliciet in drie niveau-stappen formuleren: **strategisch** (bedrijfs-/directiebeslissing), **tactisch** (eigenaarschap, beleid, organisatie), **operationeel** (concrete technische handeling). Elke stap is "de eerste logische stap op dát niveau". Labels (`Strategisch:`, `Tactisch:`, `Operationeel:`) in de tekst zelf, niet impliciet.

## Context

BB_03 Dynamic Context had oorspronkelijk drie operationele Quick Start-stappen: *"Begin met chunking"*, *"Voeg contextuele annotatie toe"*, *"Definieer staleness per categorie"*. Allemaal techniek. Robin vroeg bij de Privacy-sectie om top-down te werken ("strategisch/tactisch/operationeel"), en merkte vervolgens op: *"laten we dit ook in quick start doen, zodat iedereen iets heeft om te doen"*. Het herschrijven legde direct bloot dat één niveau ontbrak: de strategische laag (wie beslist eigenlijk óf AI dit mag doen, en met welk privacy-regime). Zonder die stap ontbreekt de rechtvaardiging voor alle techniek erbenden.

## Geleerd

### Wat werkte
- **Labels in de tekst zelf**, niet alleen impliciet in de volgorde: `Strategisch:`, `Tactisch:`, `Operationeel:`. Lezer ziet direct "dit is voor mijn rol" of "dit is niet voor mij" zonder te hoeven raden.
- **Eerste logische stap op dát niveau**, niet het eindplaatje. Strategisch is niet "ontwerp je hele governance", maar "beslis per kennisbron of PII erin mag". Concreet, klein, meteen te doen.
- **Test: als je maar één of twee niveaus kunt formuleren**, begrijp je zelf de feature nog niet volledig. Dat was in BB_04 Prompt Design een zichtbaar signaal — alle drie bestaande stappen waren operationeel, wat suggereerde dat de strategische/tactische dimensies nog niet waren gearticuleerd.
- **Dezelfde drie-niveau-structuur in body-secties** waar actie-imperatieven zitten (Privacy "Filteren aan de voorkant"-sectie had vier operationele stappen, één daarvan was eigenlijk organisatorisch — dat werd zichtbaar bij het top-down herordenen).

### Wat niet werkte
- Originele Quick Starts met alleen techniek. Leesbaar voor developers, onbruikbaar voor managers en directie die niet weten wat zij morgen kunnen doen.
- "Strategisch/tactisch/operationeel" als impliciete volgorde zonder labels — lezer moet te veel moeite doen om zijn eigen rol te vinden.

### Waarom
Een framework-bouwsteen beïnvloedt altijd meerdere rollen, niet alleen de uitvoerder. De business-case wordt strategisch beslist, de organisatie tactisch ingericht, de uitvoering operationeel gebouwd. Als content maar één van die lagen serveert, valt het framework voor 2/3 van de lezers af. De drie-niveau-structuur maakt expliciet wat anders impliciet in het hoofd van de schrijver zat.

## Toepassing

Bij elke Quick Start, elke "hoe pak je dit aan"-sectie in een BB, GR, ADR of playbook:

1. **Formuleer drie stappen op drie niveaus** (strategisch, tactisch, operationeel) met expliciete labels in de tekst.
2. **Elke stap beschrijft de eerste logische stap op dát niveau.** Niet het einde, de eerste.
3. **Test: kun je alle drie formuleren?** Zo nee: begrijp je de feature nog niet volledig — de ontbrekende laag is een gat in je analyse.
4. **Dezelfde structuur is bruikbaar in body-secties**, niet alleen frontmatter. Vraag bij elke actie-imperatief: is dit een strategische/tactische/operationele stap? Als meerdere niveaus dooreen lopen, herverdeel ze.
5. **Vastgelegd in schrijfstijl-bb.md §18** voor BB/GR-teksten. Generaliseerbaar naar elke publieksgerichte framework-content.
