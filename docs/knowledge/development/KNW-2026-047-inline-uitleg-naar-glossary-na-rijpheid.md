# KNW-2026-047: Inline uitleg eerst, glossary-links pas na rijpheid

> **Categorie:** development
> **Datum:** 2026-04-21
> **Sessie-context:** BB_03 Dynamic Context-pagina; tijdens revisie werden ~25 technische termen inline uitgelegd (parenthese bij eerste voorkomen). Pas na voltooiing van de pagina is een `/begrippen`-glossary opgezet en zijn de lange parenthese-uitleggen vervangen door links.
> **Relevantie:** hoog

## Inzicht

Begin een content-serie niet met een glossary: je weet nog niet welke termen werkelijk cruciaal zijn en welke formulering voor de lezer werkt. Leg termen eerst **inline** uit in de eerste pilot-pagina('s), laat daar de formulering uitkristalliseren, en extraheer pas **ná** de pilot de stabiele definities naar een glossary. Vervang dan de inline-uitleg door links. Andersom (vooraf glossary, dan pagina's linken) levert abstracte definities op die niet passen bij hoe de term op de pagina wordt gebruikt.

## Context

Tijdens BB_03 werd elke technische term (context window, RAG, MCP, tokens, embedding, chunks, data-lineage, freshness, CDC, DP-RAG, NER, lost-in-the-middle, etc.) bij eerste voorkomen uitgelegd in een parenthese — vaak ~10–20 woorden per term. Dat maakte de pagina leesbaar maar zwaar: elke alinea werd onderbroken door uitlegzinnen die voor één type lezer redundant waren.

Na afloop bleek dat er een duidelijk patroon zat: ~28 termen die meermaals voorkwamen, met inmiddels **gevalideerde** formuleringen (die alle revisies hadden doorstaan). Die 28 termen zijn toen geëxtraheerd naar `frontend/src/data/begrippen.ts` als single source, met een `/begrippen`-pagina die ze publiceert, én in de BB-pagina's werden de zware parenthese-uitleggen vervangen door korte linkteksten `[term](/begrippen#slug)`.

## Geleerd

### Wat werkte

- **Termen in context laten kristalliseren.** Pas wanneer een term drie keer was herschreven voordat de parenthese "klopte", was de formulering stabiel genoeg voor een glossary-entry.
- **Extractie in één keer, aan het einde.** Niet halverwege al beginnen met een glossary — de termen die zich in de eerste 40% van de pagina aandienden waren qua formulering nog niet stabiel.
- **Inline-blijven bij termen met pagina-specifieke betekenis.** Niet alle termen uit de parentheses moesten naar de glossary. Sommige (zoals *approval chains*, *sub-agent architectuur*, *transformer-attention*) waren context-specifiek en zijn inline gebleven.
- **Vervanging met behoud van minimale context** in de link: `[context window](/begrippen#context-window) van het model` leest beter dan puur `[context window](/begrippen#context-window)` zonder enige contextzin.

### Wat niet werkte

- **Eerdere vage instinctieve aanname** dat een glossary vooraf zou moeten worden opgezet. In een eerder project (NI) is dat geprobeerd en bleek de glossary uiteindelijk niet aan te sluiten bij de content-formuleringen — entries werden ongebruikt of moesten achteraf herschreven.
- **Inline-uitleg weghalen bij tweede/derde voorkomen op dezelfde pagina**: een paar gevallen bleken toch verwarrend omdat de disclosure-structuur zelfstandig leesbaar is (BB-pagina's hebben uitklapbare secties). Eerste voorkomen op elke **disclosure** aanhouden was een werkbaar compromis.

### Waarom

Terminologie wordt in een content-serie ontdekt, niet verzonnen. Wat een technische term precies "doet" in jouw narratief, wordt pas duidelijk terwijl je het eerste verhaal uitschrijft. Tot dat moment zijn glossary-definities een gok. Na het schrijven (en herschrijven en herschrijven) heb je **getest welke formuleringen werken** voor de lezer die je voor ogen hebt — die formuleringen zijn dan kandidaat voor single-source opname.

De omgekeerde volgorde (glossary eerst, dan pagina's schrijven) leidt tot één van twee problemen:
1. Pagina's komen te dicht op de glossary-formulering te zitten ("we hebben daar al gedefinieerd dat X…") en verliezen narratieve flow
2. Pagina's wijken af van glossary-formuleringen, waardoor de glossary meteen verouderd is

## Toepassing

**Stappenplan:**

1. **Pilot-pagina schrijven zonder glossary**; termen inline uitleggen bij eerste voorkomen
2. **Correctie-rondes laten plaatsvinden** tot termen stabiel geformuleerd zijn (zie KNW-2026-046)
3. **Inventariseer termen** die ≥2x voorkomen of die meerdere pagina's zullen raken
4. **Extraheer naar single source** (typed TS-module, YAML-file, database — afhankelijk van stack). Include `zieOok`-crossreferences indien zinvol.
5. **Render glossary-pagina** uit die single source
6. **Vervang inline-uitleg in pagina('s)** door links naar glossary-ankers, met **zeer korte** contextzin rond de link (2–5 woorden). Laat de diepere uitleg in de glossary.
7. **Houd glossary uitbreidbaar**: elke volgende pilot-pagina voegt 3–8 termen toe; single source zorgt dat pagina + inline-links automatisch meegroeien.

**Wanneer inline houden (niet extraheren):**

- Context-specifieke termen die nergens anders terugkomen
- Termen die hun betekenis krijgen *in samenhang met* de pagina-context (losse definitie zou betekenisloos zijn)
- Termen die slechts één keer op de hele site voorkomen

**Koppeling met andere KNW-entries:**

- KNW-2026-018 (Single source of truth voor LLM-gestuurde classificatie) — hetzelfde principe, andere toepassing
- KNW-2026-026 (Gedeelde constanten voor cross-component referenties) — glossary-file is een instance hiervan voor content
