# KNW-2026-027: Statische data als API-placeholder pattern

> **Categorie:** development
> **Datum:** 2026-03-30
> **Sessie-context:** Guardrail-koppelingen op BB detail-pagina's vóór backend API
> **Relevantie:** hoog

## Inzicht

Wanneer de backend API nog niet bestaat, bouw de frontend met statische data in een apart TypeScript bestand dat dezelfde interface gebruikt als de toekomstige API-response. Dit maakt de migratie naar de API een één-bestand-vervanging in plaats van een refactoring van componenten.

## Context

De BB detail-pagina's moesten gekoppelde guardrails tonen, maar de Neo4j API (Fase 4) bestaat nog niet. In plaats van placeholder-blokken ("coming soon") of het uitstellen van de feature, is een `bb-guardrail-links.ts` aangemaakt met statische data die dezelfde `GuardrailLink` interface gebruikt als de toekomstige API-response. De component (`BBGuardrails.astro`) weet niet of de data statisch of dynamisch is.

## Geleerd

### Wat werkte
- Aparte TypeScript file met typed data (`Record<string, GuardrailLink[]>`)
- Component accepteert data via props, onafhankelijk van de bron
- Gebruiker ziet echte content in plaats van "coming soon"

### Wat niet werkte
- Placeholder secties ("binnenkort beschikbaar") — ondermijnt geloofwaardigheid (CCR-001 uit plan review)
- Data inline in de component — maakt migratie lastiger

### Waarom
Het verschil tussen "placeholder" en "statische versie" is groot voor de gebruikerservaring. Een placeholder zegt "dit is niet af". Statische data zegt "dit werkt, en het wordt straks nog slimmer". De migratie-effort is gelijk (vervang de data-bron), maar de tussentijdse waarde is veel hoger.

## Toepassing

Gebruik dit patroon wanneer:
- Frontend klaar is maar backend nog niet
- Data relatief stabiel is (guardrail-BB relaties veranderen zelden)
- De API-interface al bekend is of gedefinieerd kan worden

Verwijder het statische bestand zodra de API live is — laat het niet naast de API-call bestaan als dead code.
