# Hoofdstuk 8 — Cross-bouwsteen-overzicht

## 8.1 Waarom dit hoofdstuk

BB_02 (Client Blueprint) is geen gesloten document. Hij is de contract-laag waarop de andere zes BeeHaive-bouwstenen aansluiten: BB_01 (Knowledge), BB_03 (Dynamic Context), BB_04 (Prompt Design), BB_05 (Tool Integration), BB_06 (Model Engines), BB_07 (Evaluation Loop). Een blueprint die zijn cross-bouwsteen-koppelingen niet expliciteert leidt tot dubbel werk in latere fasen of, erger, tot inconsistenties tussen bouwstenen. Dit hoofdstuk legt per BB vast welke ontwerpkeuze in BB_02 doorwerkt naar welke ontwerpkeuze in de andere bouwsteen.

## 8.2 BB_01 — Knowledge

### Wat hoort hier

BB_01 gaat over de kennislaag: hoe wordt domeinkennis geformaliseerd, gestructureerd en versioneerd zodat AI er deterministisch mee kan werken? De link met BB_02: de kennisbronnen die in het AI Solution Canvas (hoofdstuk 2.2 stap 5) als *Main Inputs* worden genoemd, zijn de input voor BB_01.

**Vragen die BB_02 aan BB_01 doorgeeft:**

- Welke kennisbron-categorieën zijn nodig (rubric, voorbeelden, eerdere outputs)?
- Welke versie-discipline geldt (semver, dated revisions, change-log)?
- Welke autoriteits-tier (gezaghebbend / aanvullend / illustratief)?

### Voorbeeld — Hexant

- *HLEG-rubric*: gezaghebbende kennislaag. BB_01-eis: machine-leesbaar (JSON), versiebeheerd, change-log per criterium, eigenaarschap bij Knowledge Management Hexant.
- *Eerdere audit-rapporten*: aanvullende kennislaag (few-shot voor LLM). BB_01-eis: anonimisering, tagging op HLEG-dimensie en sterkte.
- *Transcripten*: niet langetermijn-kennis, ten minste 90 dagen bewaard, per audit geïsoleerd. Hoort niet in BB_01 als blijvende kennis.

## 8.3 BB_03 — Dynamic Context

### Wat hoort hier

BB_03 gaat over context-engineering: hoe wordt de juiste informatie just-in-time aan een LLM-call meegegeven, met aandacht voor context-venster, retrieval-strategie en compaction. De link met BB_02: de RAG-stores en retrieval-rechten uit hoofdstuk 3 (architectuur, MCP-tabel) worden door BB_03 geconcretiseerd in retrieval-strategie en context-bouw.

**Vragen die BB_02 aan BB_03 doorgeeft:**

- Welke RAG-stores zijn aanwezig (uit hoofdstuk 3)?
- Welke retrieval-rechten gelden per store (read-only, tenant-scoped, etc.)?
- Welke context-budget is beschikbaar per LLM-call (uit BB_06)?

### Voorbeeld — Hexant

- *Twee retrieval-stores*: HLEG-rubric (klein corpus, hoge precisie) + transcript-store per audit (geïsoleerd, tenant-scoped). BB_03 ontwerpt: per LLM-call eerst rubric-fragmenten retrieven, daarna relevante transcript-fragmenten, in vaste volgorde.
- *Context-budget*: ~30K tokens per call (afhankelijk van model-keuze BB_06). BB_03 dwingt: rubric-fragmenten max 5K tokens, transcript-fragmenten max 20K, system-prompt + instructie max 5K.
- *Compaction*: niet nodig in v1 (single-shot per dimensie); revisits gebeuren via fresh retrieval, niet via context-stapeling.

## 8.4 BB_04 — Prompt Design

### Wat hoort hier

BB_04 gaat over het ontwerp van de prompt-laag: rol-instructie, taakbeschrijving, output-schema, voorbeelden, en de iteratieve verfijning daarvan. De link met BB_02: de extractie-, scoring- en validatie-stappen uit hoofdstuk 3 (architectuur, paragraaf 3.2) zijn de chain-componenten waarvoor BB_04 de prompts ontwerpt.

**Vragen die BB_02 aan BB_04 doorgeeft:**

- Welke chain-stappen zijn er (uit hoofdstuk 3)?
- Welke output-schema's per stap?
- Welke few-shot-bronnen (uit BB_01)?
- Welke guardrails uit hoofdstuk 4 moeten in de prompt zelf worden afgedwongen?

### Voorbeeld — Hexant

Drie prompts:

- *Extractie-prompt* — input: transcript-fragment + HLEG-rubric. Output: JSON met dimensie, sterkte, citatie. Guardrail: geen vrije tekst, alleen schema.
- *Scoring-prompt* — input: aggregaat van extractie-output per dimensie. Output: score (0-10) + top-3 evidence + motivatie. Guardrail: bij score >8 minstens 2 sterk-bewijs, bij <3 expliciete "ontbreekt"-evidence.
- *Validatie-prompt* — niet een LLM-call maar deterministische post-check (zie 4.6).

## 8.5 BB_05 — Tool Integration

### Wat hoort hier

BB_05 gaat over het ontwerp en de implementatie van tools (MCP-servers, externe API's, deterministische functies) die de AI aanroept. De link met BB_02: de MCP-tabel uit hoofdstuk 3.4 is de input-specificatie voor BB_05.

**Vragen die BB_02 aan BB_05 doorgeeft:**

- Welke MCP-servers zijn nodig (tabel 3.4)?
- Welke rechten per server (read-only / write / execute)?
- Welke beveiligings-eisen uit hoofdstuk 4 (LLM06 Excessive Agency, LLM03 Supply Chain)?
- Welke tenant-scoping-regels?

### Voorbeeld — Hexant

Drie MCP-servers (uit 3.4):

- `mcp-hleg-rubric` — read-only over HLEG-rubric-store. BB_05-eis: cache-invalidatie bij rubric-update.
- `mcp-transcripts` — read-only, tenant-scoped per audit. BB_05-eis: tenant-id verplicht; cross-tenant test in I3.
- `mcp-historische-rapporten` — read-only over geanonimiseerde rapporten. BB_05-eis: anonimisering-validatie bij elke call.

Geen tools met schrijfrechten of externe communicatie. Audit-trail per tool-call vereist (uit 4.6).

## 8.6 BB_06 — Model Engines

### Wat hoort hier

BB_06 gaat over de keuze, configuratie en routering van LLM-engines: welk model voor welke stap, welke temperature, welke residency, welke kostenstructuur. De link met BB_02: de architectuurkeuze (hoofdstuk 3) en de risk-eisen (hoofdstuk 4) bepalen samen de model-shortlist.

**Vragen die BB_02 aan BB_06 doorgeeft:**

- Welke LLM-stappen zijn er (chain-componenten uit BB_04)?
- Welke EU-residency-eis (uit hoofdstuk 4 + AI BOM in 7.3)?
- Welke kosten-grens (uit hoofdstuk 2.2 stap 7, Impact Estimation)?
- Welke kwaliteits-eisen per stap (extractie ≠ scoring ≠ validatie)?

### Voorbeeld — Hexant

- *Extractie-stap*: hoog volume per audit (~25 transcripten × 50 fragmenten = 1250 calls), kwaliteit redelijk acceptabel (recall ≥ 0,75 in I1), kosten dominant. BB_06 overweegt een efficiënt instructie-volgmodel met EU-residency.
- *Scoring-stap*: laag volume (~7 dimensies × 30 audits/jaar), kwaliteit cruciaal (inter-auditor-variatie ≤ ±0,8). BB_06 overweegt het sterkste beschikbare reasoning-model met EU-residency.
- *Routing*: simpel — extractie-model voor extractie, scoring-model voor scoring; geen dynamische routing in v1.

Concrete model-keuze: voorbehouden aan BB_06 onderzoek (hoofdstuk 6 BB_06).

## 8.7 BB_07 — Evaluation Loop

### Wat hoort hier

BB_07 gaat over de continue evaluatie van het systeem in productie: eval-sets, drift-detectie, regressie-tests, productie-monitoring. De link met BB_02: de eval-set uit hoofdstuk 6.4 is de start-versie waarvan BB_07 de evolutie en de productie-monitoring overneemt.

**Vragen die BB_02 aan BB_07 doorgeeft:**

- Welke eval-set is opgebouwd in I0-I4 (uit hoofdstuk 6.4)?
- Welke succescriteria gelden in productie (uit hoofdstuk 0 + 6)?
- Welke drift-signalen moeten worden gemonitord?
- Welke regressie-criteria bij model-upgrade (zie 7.3 AI BOM update-cadans)?

### Voorbeeld — Hexant

- *Eval-set*: 50 cases na I0; verwacht 80+ cases na I2 (uitgebreid voor zwakker scorende dimensie); doorlopend uitgebreid in productie zodra een case "interessant verschil" oplevert.
- *Productie-criteria*: inter-auditor-variatie ≤ ±0,8 (gemeten via random sample van 5 audits per kwartaal), scoring-tijd 4-6u/audit (gemeten per audit), zero kritieke incidenten (LLM02-lekken, prompt-injection-effect).
- *Drift-signalen*: gemiddelde score per dimensie wijkt af tussen kwartalen (mogelijk model-upgrade-effect of rubric-evolutie); eval-set-prestatie valt onder ondergrens (model-upgrade nodig).
- *Regressie-criteria bij model-upgrade*: hertest tegen volledige eval-set; ≥ baseline-prestatie op alle dimensies; geen regressie ≥0,5 punt op een individuele dimensie.

## 8.8 Cross-cutting overzicht — Hexant

| BB | Belangrijkste input vanuit BB_02 | Eigenaar |
|----|----------------------------------|----------|
| BB_01 | HLEG-rubric machine-leesbaar; voorbeeld-rapporten getagd | Knowledge Management Hexant |
| BB_03 | Twee RAG-stores; tenant-scoping; context-budget per call | BeeHaive-bouwer + IT Hexant |
| BB_04 | Drie prompts (extractie, scoring) + één deterministische validatie | BeeHaive-bouwer |
| BB_05 | Drie MCP-servers, alle read-only; tenant-id verplicht | BeeHaive-bouwer |
| BB_06 | Twee modellen (efficiënt + reasoning), EU-residency | BeeHaive + AI-Comité (model-keuze) |
| BB_07 | Eval-set start v1.0 (50 cases); productie-monitoring per kwartaal | AI-Comité Hexant |

## 8.9 Template — invulblok

> [INVULLEN]
>
> | BB | Belangrijkste input vanuit BB_02 | Eigenaar |
> |----|----------------------------------|----------|
> | BB_01 (Knowledge) | ... | ... |
> | BB_03 (Dynamic Context) | ... | ... |
> | BB_04 (Prompt Design) | ... | ... |
> | BB_05 (Tool Integration) | ... | ... |
> | BB_06 (Model Engines) | ... | ... |
> | BB_07 (Evaluation Loop) | ... | ... |

## 8.10 Checklist hoofdstuk 8

- [ ] Per BB (01, 03-07) is concreet benoemd welke input vanuit BB_02 doorwerkt.
- [ ] Per BB is een eigenaar benoemd; geen lege "TBD"-velden.
- [ ] Cross-cutting overzicht-tabel volledig ingevuld.
- [ ] Inconsistenties tussen hoofdstukken (bijv. tussen MCP-tabel 3.4 en BB_05-input) zijn weggewerkt.
- [ ] Cross-cutting checks uit hoofdstukken 3, 4, 6, 7 zijn niet in conflict met dit overzicht.

## 8.11 Status / laatste herziening

- Versie: 1.0
- Laatst bijgewerkt: 2026-04-28
- Wijzigingen sinds vorige versie: eerste vastlegging.
