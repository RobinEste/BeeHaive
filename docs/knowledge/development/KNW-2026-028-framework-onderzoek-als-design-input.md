# KNW-2026-028: Framework-onderzoek als design-input voor component-architectuur

> **Categorie:** development
> **Datum:** 2026-03-30
> **Sessie-context:** 15 frameworks geanalyseerd vóór het bouwen van BB detail-pagina's
> **Relevantie:** hoog

## Inzicht

Onderzoek van 10-15 vergelijkbare sites vóór het bouwen levert concrete, bewezen design patterns op die je anders pas na meerdere iteraties zou ontdekken. De investering (2-3 uur research) bespaart meerdere refactoring-rondes.

## Context

Vóór het bouwen van de BB detail-pagina's zijn 15 frameworks geanalyseerd in drie categorieën: AI-frameworks (IBM, Microsoft, Google PAIR, OECD, ALTAI), design/docs (Stripe, Next.js, Tailwind, Linear, Anthropic), en methodologie (SAFe, TOGAF, ITIL 4, Design Council, NIST). Elk werd beoordeeld op volledigheid, UX, vormgeving en onderhoudbaarheid.

## Geleerd

### Wat werkte
- Drie parallelle research agents (elk 5 sites) leverden in ~12 minuten een volledig overzicht
- Concrete patterns: sticky ToC (Tailwind), evidence deliverables (NIST), CardGroup (Anthropic), text-wrap balance (Linear)
- Het combineren van patterns uit verschillende domeinen (AI + docs + methodologie) leverde een rijker resultaat dan alleen naar concurrenten kijken

### Wat niet werkte
- Geen enkel framework had alles — de waarde zit in het combineren van het beste uit elk
- Sommige patterns (interactieve assessment met radar chart) waren te ambitieus voor Fase A

### Waarom
De meeste component-architectuur-beslissingen zijn niet uniek. Sticky ToC's, prev/next navigatie, section-based layouts — dit zijn opgeloste problemen. Door bestaande oplossingen te bestuderen voorkom je het heruitvinden van het wiel en krijg je meteen de randgevallen mee (responsive gedrag, accessibility, scroll-spy implementatie).

## Toepassing

Doe een framework-scan bij:
- Nieuwe pagina-types (Guardrail pages, blog, training portal)
- Complexe UI-componenten (dashboards, wizards, onboarding flows)
- Design system uitbreidingen

Structureer de scan in 3 categorieën: directe concurrenten, best-in-class docs/design, en aangrenzende domeinen. Drie parallelle agents van elk 5 sites is een goede balans tussen diepte en snelheid.
