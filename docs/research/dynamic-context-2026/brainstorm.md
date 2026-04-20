# Brainstorm: Dynamic Context (BB_03) deep-research scope

**Datum:** 2026-04-20
**Skill-context:** `/brainstorm` → feeds `/deep-research` Stap 1
**Precedent:** `docs/research/prompt-design-2026/` (BB_04 treatment)
**Pad-afwijking:** co-located met research-pakket (ipv `docs/specs/`) zodat alles bij elkaar blijft

## Context

BB_03 Dynamic Context-pagina is thin (`frontend/src/content/building-blocks/dynamic-context.mdx`, 39 regels, alleen definitie + praktijk-paragraaf). BB_04 Prompt Design kreeg een volwaardig deep-research pakket dat resulteerde in 5 disclosure-secties op de BB-pagina (Evolutie, Vormen, Agentic flow, PromptOps, In de praktijk). BB_03 verdient pariteit voordat we andere BBs uitrollen via het 5-stappen ritme.

Eerdere research-baseline is gearchiveerd in vault: `bron-080` (PCM synthese Forte+Bertus), `bron-081` (Forte AI Second Brain webinar), `bron-082` (Liu 2024 *Lost in the Middle*). Die bronnen zijn **anker, niet dekking** — voor 2026-pariteit moet nieuw materiaal bij, met focus op:
- frontier-model-updates van context rot (Claude 4.7, GPT-5.4, Gemini 3)
- agentic memory systems (mem0, Letta, MemGPT)
- enterprise KB-governance en refresh-patronen

## Beslissing

**Afbakening** — strikte informatie-architectuur. Volgt uit gebruiker-definities:

- **BB_03 Dynamic Context** = data/informatie die het model op uitvoeringstijd ontvangt uit knowledge base, dataset of externe bron. Variabele laag bovenop vast systeemontwerp.
- **BB_01 Knowledge** = menselijke competentielaag (ervaring, vaardigheden, attitude, rolverdeling, leercultuur). Volledig buiten scope van deze research.

**Lanes, sub-vragen, claims** — zie Ontwerp-sectie hieronder.

**Output** — volledig pakket (plan + final + 4 research-files + provenance) in `docs/research/dynamic-context-2026/`.

## Ontwerp

### Hoofdonderzoeksvraag

Wat is de stand van context engineering als informatie-architectuur-discipline (2024-2026), en welke patronen moet BB_03 dekken om elk checklist-item praktisch bruikbaar te maken?

### Sub-vragen — gemapt op BB_03 checklist

| # | Checklist-item | Sub-vraag voor research |
|---|---|---|
| 1 | Bronbestanden actueel? | Wanneer wordt context stale? Wie/wat bepaalt refresh-cadans? |
| 2 | Welke context wanneer? | Hoe beslis je welke context geïnjecteerd wordt? (routing, intent-detection) |
| 3 | Irrelevante/verouderde context uitsluiten? | Retrieval-ranking, context-pruning, filter-strategieën |
| 4 | Privacy/datakwaliteit? | PII-filtering in retrieval, data-lineage (cross-cut GR Privacy) |
| 5 | Structurering/opslag? | Chunking, embeddings, schema's, opslagformaat |
| 6 | Automatisch/handmatig actualiseren? | Trigger-mechanismen, invalidation-strategieën |
| 7 | Hoeveelheid context afgestemd op model? | Token-budget, context window ≠ bruikbaar, U-curve/context rot |

### Research-lanes (4 parallelle researchers)

Domein-specifiek — géén hergebruik van BB_04-dimensies (vendor-docs-lane is dun voor context: minder vendor-specifieke adviezen dan bij prompt design).

| Lane | Dimensie | Scope | Anker-bronnen |
|------|----------|-------|---------------|
| 1 | **Wetenschap** | context rot, U-curve, long-context benchmarks, re-ordering-effecten op frontier-modellen | `bron-082` + 2025-2026 vervolgonderzoek |
| 2 | **Architectuur** | RAG 2.0, GraphRAG, agentic memory (mem0/Letta/MemGPT), hybrid retrieval, MCP context provisioning | — nieuw materiaal — |
| 3 | **Praktijkpatronen** | Willison's context engineering, Forte's PCM, Mollick's *Co-Intelligence*, enterprise KB-governance | `bron-080`, `bron-081` |
| 4 | **Privacy & kwaliteit** | PII-filtering in retrieval, data-lineage, transparantie over contextbronnen | cross-cut GR Privacy + GR Transparency |

### Primaire claims om te onderbouwen

- **U-curve / context rot op 2026 frontier modellen** (Claude 4.7, GPT-5.4, Gemini 3) — update op `bron-082`. Test of effect zwakker/sterker is geworden.
- **"25-50% bruikbaar context window"** (Forte, onbewezen) — empirisch onderbouwen of vager formuleren.
- **Persona/domein-splitsing effectiviteit** — is Forte's context-stack-claim empirisch toetsbaar?
- **Agentic memory productie-rijpheid** — hype of werkend paradigma? Case studies voor mem0/Letta/MemGPT.

### Output-structuur

```
docs/research/dynamic-context-2026/
├── brainstorm.md          # dit document
├── plan.md                # /deep-research Stap 1
├── research-wetenschap.md
├── research-architectuur.md
├── research-praktijkpatronen.md
├── research-privacy-kwaliteit.md
├── draft.md               # intermediate
├── final.md               # gepubliceerd rapport
└── provenance.md          # audit trail
```

### Tijdvenster

2024-2026 primair. Landmark-uitzonderingen: Liu 2024 (TACL paper, juli 2023 preprint), Forte PKM-tijdperk (2016+) als noodzakelijke achtergrond.

## Alternatieven overwogen

- **Hergebruik BB_04-dimensies** (academisch / industrie / vendor-docs / agentic-guardrails). **Afgewezen:** vendor-docs is dun voor context (minder vendor-specifieke adviezen); architectuur is juist groot en verdient eigen lane.
- **Lichter pakket (3 lanes)**. **Afgewezen:** pariteit met BB_04 is expliciete doelstelling; minder diepte = minder waarde voor de BB-pagina.
- **Laat afbakening emergeren uit research** (overlap met Knowledge BB_01 tolereren). **Afgewezen:** gebruikerdefinities lossen afbakening al op; emergentie zou scope-drift riskeren naar de mens-laag.

## Randgevallen

- **Overlap met BB_05 Tool Integration** — context-tools (RAG-frameworks, MCP-servers) vallen in beide. Afbakening: BB_03 = *wat* stroomt er in, BB_05 = *met welk gereedschap*. Cross-links expliciet op BB-pagina.
- **Overlap met GR Privacy/Transparency** — lane 4 snijdt mee. Research-output voor lane 4 labelt expliciet welke insights naar BB_03 vs. naar de guardrails gaan.
- **Bron-082 veroudering** — frontier-modellen 2026 kunnen U-curve hebben verzwakt. Als research dat aantoont → belangrijke narratieve update voor BB-pagina.
- **Forte's onbewezen cijfers** — als 25-50%-claim niet onderbouwbaar is, moet synthese eerlijk rapporteren + alternatieve formulering voorstellen (géén aannemen zonder bron).

## Migratiepad

Deze research voedt:

1. **BB_03 mdx-update** — 39 → ~150 regels, 4-5 disclosure-secties (stap 3 van 5-stappen ritme)
2. **Nieuwe bronnen in vault** via `/bron-archiveren` — top 3-5 per lane (stap 2 van ritme, en eerste live-test van de nieuwe skill)
3. **Bestaande bronnen verrijken** — `bron-080/081/082` krijgen nieuwe verbanden vanuit 2026-inzichten

## Open vragen

- Moet lane 4 (Privacy & kwaliteit) óók de Privacy/Transparency guardrail-pagina's voeden, of puur BB_03? → beslissing bij synthese op basis van volume.
- Vendor-specifieke context-features (Claude Projects, ChatGPT Custom Instructions, Gemini gemen) — aparte sub-vraag of onder lane 2? → voorstel: onder lane 2 als sectie "vendor-context-features".
