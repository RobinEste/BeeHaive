# KNW-2026-025: Native render() boven externe markdown-parser

> **Categorie:** development
> **Datum:** 2026-03-30
> **Sessie-context:** BB detail-pagina's bouwen met Astro 5 content collections
> **Relevantie:** hoog

## Inzicht

Gebruik altijd de ingebouwde render-functie van je framework voordat je een externe parser toevoegt. Astro's `render()` levert zowel een `<Content />` component als een `headings` array — precies wat nodig was voor de ToC. De externe `marked` dependency was volledig overbodig.

## Context

Het oorspronkelijke plan introduceerde `marked` als devDependency om de MDX body te splitsen op `## ` headings via regex en apart te renderen. Dit creëerde een tweede markdown-render-pipeline naast Astro's eigen MDX-verwerking. Drie review agents (ARCH, FEAS, PM) signaleerden dit onafhankelijk als het zwaarste technische probleem.

## Geleerd

### Wat werkte
- Astro's `const { Content, headings } = await render(entry)` levert alles wat nodig is
- De `headings` array is direct bruikbaar voor de ToC (depth, slug, text)
- Eén render-pipeline betekent consistente output en minder onderhoud

### Wat niet werkte
- Raw `body` splitsen op regex `\n## ` en renderen via `marked` — fragiel, geen MDX-support, tweede parser
- CSS `:has()` selectors om secties apart te stylen — overkill voor 2 korte MDX-secties

### Waarom
Frameworks bieden meestal meer dan je denkt. De reflex "ik heb een npm package nodig" is vaak sterker dan de reflex "wat biedt mijn framework hier?". Bij Astro 5 is de Content Layer API significant verbeterd ten opzichte van v4 — documentatie lezen loont.

## Toepassing

Bij het bouwen van nieuwe pagina-types (Guardrail detail-pagina's, blog posts): check eerst `render()` output voordat je een parser toevoegt. Dit geldt breder: bij Next.js (MDX plugins), Nuxt (content module), SvelteKit (mdsvex) — elk framework heeft eigen content rendering die meestal volstaat.
