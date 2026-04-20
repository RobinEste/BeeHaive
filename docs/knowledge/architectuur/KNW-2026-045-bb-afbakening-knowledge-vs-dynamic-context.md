# KNW-2026-045: BB_01 Knowledge vs BB_03 Dynamic Context — mens-laag vs informatie-laag

> **Categorie:** architectuur
> **Datum:** 2026-04-20
> **Sessie-context:** Deep-research scope-alignment voor BB_03 via `/brainstorm`. Eerste framing-poging gebruikte klassieke info-architectuur ("stabiel vs. runtime info") die door de gebruiker werd gecorrigeerd met de werkelijke BeeHaive-definities.
> **Relevantie:** hoog

## Inzicht

In het BeeHaive-framework is **Knowledge (BB_01)** de **menselijke competentielaag** — ervaring, vaardigheden, attitude, rolverdeling, leercultuur — niet het "stabiele informatie-fundament" dat klassieke data-architectuur zou suggereren. **Dynamic Context (BB_03)** is de **informatie-laag** — data, retrieval, context-injection, token-budget. Ze staan op **verschillende assen** (mens vs. systeem-informatie), niet op één as van "stabiel vs. dynamisch". Deze afbakening is cruciaal voor scope-bepaling van alle BB-research en inhouds-werkzaamheden en wijkt af van wat een nieuw team-lid uit standaard data-architectuur zou verwachten.

## Context

Bij het opzetten van de Dynamic Context deep-research stelde ik als afbakening voor: *"Knowledge = stabiele info-fundament, Dynamic Context = runtime info-laag."* De gebruiker corrigeerde dit met de werkelijke definities:

- **Knowledge-checklist** heeft items over *"Hebben betrokkenen voldoende domeinkennis?", "Is er begrip van AI-mogelijkheden én beperkingen?", "Is er ervaring met prompt-gebruik?", "Is er een leercultuur?", "Is rolverdeling duidelijk?"* — allemaal mens-gericht.
- **Dynamic Context-checklist** heeft items over *"Zijn bronbestanden actueel?", "Wordt irrelevante context uitgesloten?", "Zijn privacy- en datakwaliteitsaspecten geborgd?", "Is de hoeveelheid context afgestemd op tokens?"* — allemaal informatie/systeem-gericht.

Nul overlap. Afbakening werd strak en helder zodra de correcte framing voorlag.

## Geleerd

### Wat werkte
- Direct de gebruiker-definities + checklist-items als primaire bron voor afbakening nemen
- Controleren "gaan deze items over mensen of over informatie" als sanity-check

### Wat niet werkte
- Aannemen dat BB-namen één-op-één mappen op standaard termen uit aangrenzende domeinen (information retrieval, data management, RAG-architectuur)
- Logica-gedreven afleiden ("Knowledge = staticish, Dynamic = runtime") zonder de feitelijke checklist-items te raadplegen

### Waarom
BeeHaive's MISSIE (v0.3) is mens-centrisch — "de hele organisatie een stem", Noblesse Oblige, "AI vertrouwen" als actief werkwoord. Knowledge als "menselijke competentielaag" sluit daar logisch bij aan. Een pure info-architectuur-framing zou het mens-centrische karakter van het framework platdrukken en BB_01 reduceren tot "knowledge base CRUD".

De afbakening is dus geen technische maar een **conceptuele keuze** gedreven door de missie.

## Toepassing

### Bij alle BB-research en inhouds-werkzaamheden

**BB_01 Knowledge** = mens/organisatie:
- Wie begrijpt wat van het domein en van AI
- Wie doet welke rol in de AI-flow (ontwerper, reviewer, operator, eigenaar)
- Hoe leert en verbetert de organisatie zich
- Relevante guardrails: Well-being, Human-Agency, Accountability

**BB_03 Dynamic Context** = informatie-stromen:
- Wat stroomt er in (dataset, knowledge base, externe API)
- Hoe actueel, hoe gefilterd, hoe gestructureerd
- Hoe past het in het token-budget
- Relevante guardrails: Privacy, Transparency

### Raakvlakken elders (niet in BB_01/BB_03)

- **BB_05 Tool Integration** — *tools* die context ophalen (RAG-frameworks, MCP-servers). BB_03 = *wat* stroomt, BB_05 = *met welk gereedschap*
- **BB_06 Evaluation Loop** — meten of context de output-kwaliteit verbetert
- **GR Privacy** — welke data mag in context (doorsnijdt BB_03 lane 4)
- **GR Transparency** — herleidbaarheid van contextbronnen

### Bij twijfel

Check de BB-checklist-items voor het onderwerp:
- Gaan de items over **mensen**? → BB_01
- Gaan de items over **informatie/data/systeem**? → BB_03
- Gaan ze over **tools/software**? → BB_05

### Aanbeveling

Deze afbakening rechtvaardigt een ADR (Architecture Decision Record) omdat:

1. Hij conceptueel afwijkt van wat standaard data-architectuur suggereert
2. Hij de scope bepaalt van alle toekomstige BB-research
3. Hij voorkomt dat nieuwe team-leden BB_01 en BB_03 verwarren als "stabiele info vs. runtime info"

**Actie:** overweeg `/adr` om dit vast te leggen als `ADR-2026-XXX — BB_01 Knowledge vs BB_03 Dynamic Context afbakening`.
