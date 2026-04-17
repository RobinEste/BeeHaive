# KNW-2026-040: CSS Columns boven Grid voor lijsten met variabele itemlengte

> **Categorie:** development
> **Datum:** 2026-04-17
> **Sessie-context:** Checklist op BB-detailpagina oogde onevenwichtig — korte items naast lange items in dezelfde rij
> **Relevantie:** hoog

## Inzicht

Voor een twee-koloms lijst waarvan de items sterk in lengte variëren, is `column-count: 2` beter dan `grid-template-columns: 1fr 1fr`. Grid forceert horizontale rij-uitlijning (elke rij krijgt de hoogte van z'n langste item), CSS Columns laat items verticaal per kolom stromen — elk item pakt z'n natuurlijke hoogte en korte/lange items kruisen elkaar niet in één oogopslag.

## Context

De Prompt Design BB-pagina heeft een 9-item checklist. Drie items zijn kort ("Is context correct en volledig ingevoegd?"), twee zijn lang met uitleg tussen haakjes (XML/Markdown-detail, few-shot-detail). In een 2-koloms CSS Grid veroorzaakte dat rare lege ruimtes: een korte vraag naast een 4-regelige vraag. Het leest als een onevenwichtig formulier.

## Geleerd

### Wat werkte

```css
.checklist-grid {
  column-count: 2;
  column-gap: 2rem;
}
.checklist-item {
  break-inside: avoid;      /* moderne browsers */
  page-break-inside: avoid; /* Safari/oudere fallback */
  margin-bottom: 1.2rem;
}
```

Items vullen eerst kolom 1 van boven naar beneden, dan kolom 2. Natuurlijke verticale flow, geen forced row-height alignment.

### Wat niet werkte

- `grid-template-columns: 1fr 1fr` — rijen krijgen de hoogte van het langste item op die rij, korte buren zien er verloren uit
- Items herordenen in frontmatter (zodat lange items in dezelfde rij landen) — fragiel, breekt zodra iemand een item toevoegt of verkort
- `align-items: start` op grid-items — items zelf zijn dan niet meer uitgelijnd op hun top, maar de rij behoudt nog steeds z'n forced height

### Waarom

CSS Grid is ontworpen voor **2D-layouts met rij-logica** (tabellen, dashboards). Het aligneert items binnen rijen én kolommen. CSS Columns (oorspronkelijk voor typografisch "krantenkolom" renderen) is **1D-flow**: items worden sequentieel gestroomd in kolomrichting. Voor een lijst van ongelijke items is die 1D-flow precies wat je wilt — de layout-engine beslist zelf waar de kolom breekt.

## Toepassing

- **Default voor 2-koloms lijsten met tekst van variabele lengte**: CSS Columns. Denk aan checklists, feature-lijsten, FAQ-teasers.
- **Default voor 2-koloms lijsten met uniforme cards** (zoals BBTools's tool-cards): CSS Grid blijft beter — je wilt dan juist uitgelijnde rij-hoogtes, want het zijn visuele kaarten die parallel horen te lopen.
- **Regel van duim**: als je ooit dacht "ik zou die items eigenlijk moeten herordenen om de layout mooi te maken", is Grid het verkeerde gereedschap. Pak Columns.
- **Vergeet `break-inside: avoid` niet** — zonder dat kan een item halverwege doorbreken naar de volgende kolom.
