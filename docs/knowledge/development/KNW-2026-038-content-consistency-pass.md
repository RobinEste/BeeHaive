# KNW-2026-038: Content consistency-pass na narrative-updates

> **Categorie:** development
> **Datum:** 2026-04-15
> **Sessie-context:** BB_04 Prompt Design pagina kreeg een narrative-herziening (van "rolzetting" naar "capability- vs context-rolzetting"). Checklist, quickStart en body werden aangepast. Pas bij expliciete consistency-pass viel op dat `evidence[2]` nog de oude term bevatte.
> **Relevantie:** hoog

## Inzicht

Content met meerdere lagen (frontmatter-checklist, quickStart, evidence-items, body-tekst, component-props) heeft het grootste inconsistency-risico bij items die in meerdere velden herhaald zijn. Bij een narrative-update moet elke plek waar de oude term voorkwam worden gecheckt — een enkele gemiste evidence-regel kan de centrale these tegenspreken. Plan daarom een aparte consistency-pass **na** alle inhoudelijke iteraties, niet als onderdeel ervan.

## Context

De Prompt Design BB-pagina werd in drie iteraties herzien op basis van deep research. Elke iteratie had eigen focus: narratief preciseren, agent-sectie uitbreiden, PromptOps + guardrails toevoegen. Na de drie iteraties werd op verzoek van de gebruiker een aparte "check de hele pagina" ronde gedaan. Die vond zeven inconsistencies:

- `evidence[2]` zei nog *"rol, context, instructies..."* terwijl checklist, quickStart en body inmiddels *"betekenis → context → instructies"* zeggen — het oude mentale model dat juist werd genuanceerd
- "EU AI Act (Art. 14)" in één sectie, maar bewust geen artikelnummers in guardrail-mapping
- Jargon wel uitgelegd op sommige plekken (tacit knowledge, hallucinations) maar kaal op andere (control flow, canary-deployments)

## Geleerd

### Wat werkte
- Een **expliciete consistency-pass als eigen stap** na alle inhoudelijke iteraties
- Als check-methode: lees de pagina als geheel en zoek actief naar gerepeteerde termen in checklist, evidence, frontmatter-velden, component-props en body
- Schrijf een lijstje van alle bevindingen eerst, los dan op in één batch edit

### Wat niet werkte
- Iteratie-per-iteratie checken — elke iteratie heeft eigen focus, termen buiten die focus worden overgeslagen
- Verwachten dat een `grep` op de oude term volstaat — oude termen kunnen in iets gevarieerde vorm staan ("rol" in een bullet vs. "rolzetting" in body)

### Waarom
Iteraties hebben scope-discipline: je werkt aan een specifiek onderdeel. Termen buiten die scope zijn per definitie niet in focus. Een consistency-pass verlegt de focus naar de pagina als geheel — je leest met een andere intentie ("klopt dit met elkaar?") dan bij een iteratie ("is dit goed geschreven?").

## Toepassing

Bij elke content-update die het centrale narratief of de kerntermen raakt:

1. **Plan de consistency-pass als expliciete stap** — niet als deel van de laatste iteratie, maar als aparte ronde na "klaar"
2. **Check minimaal deze plekken**: frontmatter (checklist, quickStart, evidence, auditExample, tagline), component-props, body-tekst, interne links en anchors
3. **Check op termen die een narrative-shift hebben ondergaan** — de oude term kan niet 1-op-1 gegrept worden als er synoniemen/vervoegingen zijn. Zoek ook op gerelateerde termen uit het oude model.
4. **Bundel de bevindingen** — lever ze als één lijst, fix ze in één batch. Nooit per-inconsistency committen; dat wekt de illusie van voortgang zonder de context te overzien.
5. **Cross-referenties**: guardrail-links, koppelingen tussen BB's of vergelijkbare kruisverwijzingen moeten óók matchen met de hoofd-pagina.

Gebruikelijke triggers voor deze pass:
- Narrative-herziening (term of centrale these verandert)
- Deep research dat bestaande claims corrigeert
- Cross-referenties naar gerelateerde pagina's toevoegen
- Voordat je publiceert / committeert op `main`
