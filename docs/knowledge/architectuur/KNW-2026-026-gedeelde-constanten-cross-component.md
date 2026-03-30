# KNW-2026-026: Gedeelde constanten voor cross-component referenties

> **Categorie:** architectuur
> **Datum:** 2026-03-30
> **Sessie-context:** BB detail-pagina's met sticky ToC en sectie-componenten
> **Relevantie:** hoog

## Inzicht

Wanneer meerdere componenten naar dezelfde ID's, slugs of keys verwijzen, extraheer deze als gedeelde constanten in een apart bestand. Dit voorkomt stille drift waarbij een ID in component A verandert maar component B de oude waarde behoudt.

## Context

De BB detail-pagina's hebben een sticky Table of Contents die section-ID's (`checklist`, `quick-start`, `voorbeeld`, etc.) gebruikt om naar secties te scrollen. Dezelfde ID's staan hardcoded in 7 afzonderlijke componenten. Bij de /simplify review werd gesignaleerd dat dit drie bronnen van waarheid creëerde: de ToC, de componenten, en de eyebrow-tekst waarvan BBProseSection het ID afleidt.

## Geleerd

### Wat werkte
- `bb-sections.ts` als single source of truth: exporteert `BB_SECTIONS` object en `BB_SECTION_LIST` array
- Componenten importeren hun ID uit dezelfde bron als de ToC
- TypeScript `as const` maakt de waarden type-safe

### Wat niet werkte
- Hardcoded strings in zowel ToC als componenten — drift-risico bij elke wijziging
- BBProseSection die het ID afleidde van de eyebrow-tekst via `.toLowerCase().replace()` — fragiel

### Waarom
Stringly-typed cross-references zijn een klassieke bron van stille bugs. Het probleem manifesteert zich pas als een gebruiker klikt op een ToC-link die naar niets scrollt — geen build-error, geen runtime-error, gewoon gebroken UX.

## Toepassing

Pas dit toe wanneer:
- Een ToC/navigatie verwijst naar sectie-ankers in andere componenten
- Meerdere componenten dezelfde enum-waarden of keys gebruiken (bijv. route-paden, event-namen)
- ID's worden gegenereerd op basis van user-facing tekst (altijd fragiel)

Het patroon is framework-onafhankelijk: een gedeeld constants-bestand werkt in React, Vue, Svelte, en Astro.
