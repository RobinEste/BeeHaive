# Onderzoeksplan: BB_06 Model Engines — BeeHaive AI-framework

**Slug:** bb06-model-engines-ai-framework
**Aanmaakdatum:** 2026-04-27
**Status:** ✅ Afgerond

## Onderzoeksvraag

Welke kennis, patronen en heuristieken zijn nodig voor een Nederlands AI-framework (BeeHaive BB_06) over het kiezen, combineren en operationeel houden van AI-modellen? Doel: een grondig, geciteerd rapport dat dient als bronmateriaal voor het schrijven van de Building Block.

## Kernvragen

1. Wanneer kies je welk modeltype — en waarom is "het grootste LLM overal" een anti-patroon?
2. Welke modelcategorieën zijn relevant in 2026 (LLMs, reasoning, multimodaal, world models, diffusie, embedding, klassiek ML)?
3. Hoe verhouden de frontier-modellen (Anthropic, OpenAI, Google, Meta, Mistral, DeepSeek) zich in april 2026 op kwaliteit, prijs en EU-beschikbaarheid?
4. Welke routing- en hybride strategieën werken in de praktijk?
5. Welke EU-data-residentie en soevereiniteitsopties zijn er, en wat zijn de werkelijke beperkingen?
6. Welke concrete kostenoptimalisatie-technieken bestaan, met ordegrootte van besparingen?
7. Hoe ziet een robuuste operationele runtime eruit (latency, schaalbaarheid, observability)?
8. Wat zijn de risico's en beperkingen op model-niveau (hallucinaties, knowledge cutoffs, supply chain, governance)?

## Strategie

**Scale decision:** complex, multi-domein
**Aantal researchers:** 5 parallelle agents
**Geschatte rondes:** 2 (ronde 1 breed + ronde 2 voor gaps en verificatie)

**Dimensie-verdeling:**
- Researcher A: Modeltype-keuze als ontwerpvraag + klassiek-ML vs LLM diagnostiek (vragen 1 + deels 2)
- Researcher B: Frontier-landschap april 2026 — vergelijkende analyse van top-modellen (vraag 3)
- Researcher C: Routing-strategieën, hybride architecturen, frameworks (vraag 4)
- Researcher D: EU-data-residentie, soevereiniteit, lokale inference, AI Act compliance (vraag 5)
- Researcher E: Kostenoptimalisatie, operationele runtime, observability, risico's (vragen 6+7+8)

## Acceptatiecriteria

- [ ] Alle 8 kernvragen beantwoord met ≥2 onafhankelijke bronnen
- [ ] Frontier-modellen vergeleken met actuele prijzen (per miljoen tokens input/output)
- [ ] EU-specifieke context voor minstens 3 aanbieders
- [ ] Concrete anti-patronen met praktijkvoorbeelden
- [ ] Tegenstrijdigheden geïdentificeerd en geadresseerd
- [ ] Geen single-source claims op kritieke findings
- [ ] 5–7 ontwerp-regels voor Nederlandse AI-consultants als eindproduct

## Task Ledger

| ID | Owner | Taak | Status | Output |
|----|-------|------|--------|--------|
| T1 | researcher-A | Modeltype-keuze heuristieken + klassiek-ML vs LLM | ✅ | research-modelkeuze.md |
| T2 | researcher-B | Frontier-landschap april 2026 — vergelijking | ✅ | research-frontier.md |
| T3 | researcher-C | Routing, hybride architecturen, frameworks | ✅ | research-routing.md |
| T4 | researcher-D | EU-soevereiniteit, AI Act, lokale inference | ✅ | research-eu-soevereiniteit.md |
| T5 | researcher-E | Kosten, runtime, observability, risico's | ✅ | research-kosten-runtime.md |
| L1 | lead | Synthese + draft | ✅ | draft.md |
| L2 | lead | Cite + verify + final | ✅ | final.md |

## Verificatie-log

| Item | Methode | Status | Bewijs |
|------|---------|--------|--------|
| Frontier-modelprijzen | WebFetch naar aanbieders-pricing-pages | pending | — |
| EU AI Act model-verplichtingen | WebFetch GPAI-sectie AI Act | pending | — |
| Anthropic EU Bedrock beschikbaarheid | WebFetch AWS Bedrock regio-pagina | pending | — |

## Decision-log

- 2026-04-27 10:00 — 5 researchers gekozen (complex, multi-domein: 8 kernvragen, diverse bewijstypen). Dimensie E combineert kosten+runtime+risico om overlap met dimensie A te minimaliseren.
