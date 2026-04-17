# KNW-2026-039: Inhoudelijke vs redactionele relaties in kennisgraaf

> **Categorie:** architectuur
> **Datum:** 2026-04-17
> **Sessie-context:** Tool-nodes in Neo4j toevoegen voor de "Tools & Products" sectie op BB-detailpagina's
> **Relevantie:** hoog

## Inzicht

In een kennisgraaf waar je zowel *wat is relevant* als *wat tonen we* moet modelleren, scheid die twee als **aparte relatie-types** — niet als één relatie met een `is_featured` property. De inhoudelijke relatie (breed, algoritmisch afleidbaar) en de redactionele keuze (curatie door een mens) hebben fundamenteel andere semantiek en worden anders bevraagd.

## Context

BeeHaive's Tool-nodes zijn inhoudelijk relevant voor meerdere Building Blocks. Voorbeeld: *LangSmith* kan bij Prompt Design, Tool Integration én Evaluation Loop passen. Maar we willen 'm maar op één BB-pagina prominent tonen, om overlap en visuele vermoeidheid te voorkomen. Vraag: hoe modelleer je dat?

## Geleerd

### Wat werkte

- **Twee relaties**:
  - `(Tool)-[:RELATES_TO]->(BuildingBlock)` — inhoudelijke link, breed gezet (LangSmith heeft er 3)
  - `(Tool)-[:DISPLAYED_ON]->(BuildingBlock)` — redactionele keuze, smal gezet (LangSmith heeft er 1)
- De `DISPLAYED_ON` relatie draagt zelf metadata (`display_order` als property op de edge) — past natuurlijk in een graph, zou in een tabeldesign een join-tabel met composite key vereisen
- De frontend-API vraagt puur op `DISPLAYED_ON` (`/building-blocks/{name}/tools`) en krijgt alleen wat er hoort te staan. Een toekomstige "Alle tools voor X" pagina kan op `RELATES_TO` vragen en alle relevante tools tonen

### Wat niet werkte

- Alternatief: één `RELATES_TO` relatie met een `is_featured: boolean` property. Probleem: elke query moet die property meenemen, en "featured voor BB X" kan niet zonder aparte flag per BB — wat opnieuw naar twee-dimensionale metadata leidt
- Alternatief: curatie in de frontend (lijst van tool-slugs per BB). Probleem: editorial data leeft dan in code, niet in de graph waar ingestion-scripts hem zouden kunnen zetten

### Waarom

Neo4j's property graph model belooft juist dat *relaties eerste-klasse burgers zijn*. Als je relatie een fundamenteel andere betekenis heeft, gebruik een andere relatie-naam — niet een property die bepaalt hoe je de relatie moet lezen. Dat houdt queries scherp (MATCH op het relatie-type, niet op een WHERE-filter) en maakt het schema leesbaarder voor wie later meedoet.

## Toepassing

- **Elke kennisgraaf met curatie-laag**: KnowledgeItems, Tools, UseCases, Guidelines — zodra "tonen we dit op pagina X?" een beslissing is die losstaat van "is dit relevant voor X?", splits de relatie.
- **Regel van duim**: als een relatie een boolean-property heeft die alleen context-specifiek betekenis heeft, is dat een signaal dat het een aparte relatie wil zijn.
- **Edge-properties** (zoals `display_order` op `DISPLAYED_ON`) zijn een comfortabele plek voor metadata die strikt bij de relatie hoort, niet bij de endpoints — gebruik dat vrij.
