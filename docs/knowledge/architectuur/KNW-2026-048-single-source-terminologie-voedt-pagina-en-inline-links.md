# KNW-2026-048: Single source voor terminologie voedt zowel glossary-pagina als inline links

> **Categorie:** architectuur
> **Datum:** 2026-04-21
> **Sessie-context:** Opzet van `frontend/src/data/begrippen.ts` als typed data-module die zowel `/begrippen`-pagina rendert als inline term-referenties in BB/GR-content voedt via `[term](/begrippen#slug)`-links.
> **Relevantie:** hoog

## Inzicht

Wanneer dezelfde terminologie op meerdere plekken in een codebase verschijnt (content-pagina's, UI-componenten, inline uitleg, zoekfunctie, API-responses), mag er exact **één** plek zijn waar de definitie leeft. Alle andere weergaves lezen uit die bron. Typed TS-module aan front-end zijde is een lichtgewicht patroon dat werkt zonder database en zonder runtime-fetches — de build-time garandeert dat glossary-pagina, inline-links en component-labels nooit uit sync raken.

## Context

Bij BB_03 werden termen als *context window*, *RAG*, *MCP*, *lost-in-the-middle*, etc. op drie plekken gebruikt:

1. Als korte uitleg in BB-content (inline, gelinkt naar glossary-anker)
2. Als expliciete entry op de `/begrippen` pagina
3. Potentieel in toekomstige zoekfunctionaliteit en in de kennisbank-filter

Als die drie plekken afzonderlijke definities onderhouden, drijven ze onvermijdelijk uit elkaar: een redactie-ronde update de inline-uitleg maar vergeet de glossary, of andersom. De klassieke drift.

De gekozen oplossing: `frontend/src/data/begrippen.ts` exporteert een `BEGRIPPEN: Term[]`-array met typed entries. De glossary-pagina (`begrippen.astro`) importeert de array en rendert elke entry als `<dt>` + `<dd>`. Inline-links in de BB-MDX-content linken naar `/begrippen#<slug>`, waarbij de slug-waarde exact de `Term.slug`-waarde is.

## Geleerd

### Wat werkte

- **Typed interface met slug als primary key.** De TypeScript-compiler vangt typfouten in slugs tijdens `astro check`. Een link naar `/begrippen#agent` werkt alleen als `agent` ook in de data-module staat.
- **Helpers in dezelfde file** (`termBySlug`, `termenByCategorie`, `CATEGORIE_LABELS`) houden de API compact voor de pagina die rendert.
- **Metadata als data** — `CATEGORIE_INTROS` en `CATEGORIE_VOLGORDE` staan in dezelfde module. Voorkomt dat de pagina hardgecodeerde strings bevat die ook elders nodig zijn.
- **Cross-references in data** (`zieOok: string[]`) — de pagina rendert "Zie ook"-links automatisch en de data-module zelf valideert impliciet dat ze naar bestaande slugs wijzen (in toekomst eenvoudig uit te breiden met een runtime-check).

### Wat niet werkte

- **Eerdere neiging om de glossary in MDX te schrijven** (één `.mdx` bestand met alle termen als `##`-secties) — dat geeft wél hashes, maar geen machine-leesbare data om elders te hergebruiken. MDX is presentatielaag, geen datalaag.
- **Dumps in een README of markdown-tabel** — voor een begrippenlijst die uitbreidbaar is en cross-referenties heeft, schaalt dat niet: elke wijziging vereist handmatige update van tabellen.

### Waarom

Content die op meerdere plekken verschijnt, heeft een **bronplek** nodig om drift te voorkomen. Voor content op enterprise-schaal is dat vaak een database; voor statische sites met tientallen termen is een typed data-module in de front-end codebase het eenvoudigste dat werkt:

- **Build-time validatie** — TypeScript + Astro checken consistentie zonder runtime-fetch
- **Git-tracked** — elke wijziging komt door code-review
- **Geen infra-overhead** — geen extra service, geen sync-pipeline, geen cache-invalidatie
- **Uitbreidbaar** — als er later een Neo4j-koppeling komt, kan de TS-module de data vandaar lezen zonder dat de consumers (pagina, MDX) veranderen

Bij tienduizenden entries of editoriale workflows (redacteuren die geen code willen aanraken) zou deze keuze kiepen — dan is een headless CMS of database het juiste niveau. Voor 28–200 termen die door developers onderhouden worden, is de TS-module optimaal.

## Toepassing

**Wanneer toepassen:**

- Content-site met gedeelde terminologie (glossary + pagina-uitleg + UI-labels + filter-opties)
- 20–500 items; bij meer: overweeg database-backed CMS
- Editors zijn developers of getrainde markdown-schrijvers (niet redacteuren zonder git-toegang)

**Concrete implementatie-checklist:**

1. **TypeScript-interface** definiëren met required velden + optionele uitbreidingen:
   ```ts
   interface Term { slug: string; naam: string; engels?: string; uitleg: string; categorie: Categorie; zieOok?: string[]; }
   ```
2. **Categorieën als string-union**, niet als free-form — voorkomt typos
3. **Labels en introducties als maps** (`Record<Categorie, string>`) — geen hardgecodeerde strings in de rendering-pagina
4. **Helpers** (`termBySlug`, `termenByCategorie`, `alleSlugs`) voor consumers
5. **Naming-disciplines**: `slug` kebab-case, `naam` NL, `engels` optioneel cursief — vast in de gids (zie KNW-2026-046)
6. **Link-patroon** in MDX: `[term](/begrippen#<slug>)` — slug komt 1-op-1 uit data-module
7. **Anchor-IDs** in de glossary-pagina: `id={term.slug}` + `scroll-margin-top` voor sticky-header-compensatie
8. **Target-highlight** (`.term:target { border-left-color: gold }`) zodat binnenkomer via anchor de juiste entry ziet oplichten

**Anti-patronen om te vermijden:**

- Termen in componentcode hardcoded als `<span>Token</span>` — trek ze naar de data-module
- Termen in JSON/YAML zonder typing — misbruik van data-layer
- Aparte files per term — te versnipperd voor dit volume

**Koppeling met andere KNW-entries:**

- KNW-2026-018 (Single source of truth voor LLM-gestuurde classificatie) — zelfde principe, andere domein
- KNW-2026-026 (Gedeelde constanten voor cross-component referenties) — constanten-laag voor cross-component wiring
- KNW-2026-047 (Inline uitleg → glossary-links na rijpheid) — de bijbehorende redactionele workflow
