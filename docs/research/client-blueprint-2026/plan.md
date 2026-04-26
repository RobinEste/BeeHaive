# Onderzoeksplan: BB_02 Client Blueprint — van idee naar gestructureerd AI-ontwerp

**Slug:** client-blueprint-2026
**Aanmaakdatum:** 2026-04-26
**Status:** ✅ Afgerond — 2026-04-26

## Onderzoeksvraag

Wat zijn de actuele patronen (2024-2026) voor het ontwerpen van AI-oplossingen — van probleemkeuze tot architectuur, risico-inschatting en stakeholder-validatie — en welke moeten BB_02 dekken om elk checklist-item praktisch bruikbaar te maken?

Scope: het ontwerp-niveau tussen klantbehoefte en implementatie. Inclusief use case-selectie, architectuurpatronen, risk-by-design en iteratieve validatie. Buiten scope: BB_03 (data-architectuur in detail), BB_04 (prompts), BB_05 (tools), BB_06 (modelkeuze), BB_07 (eval-loop). Wel: hoe BB_02 deze andere BB's *aanstuurt* en samenbindt.

## Kernvragen

1. **Use case-selectie:** welke problemen zijn AI-problemen, en welke niet? Welke methodieken (decision-first, Karpathy's "Software 3.0", outcome-mapping) helpen vroeg te scopen? Wat zegt het MIT-onderzoek over de 95%-fail-rate van GenAI-pilots? (item 1)
2. **Doel & toetsbare output:** hoe vertaal je een vaag "we willen iets met AI" naar concrete, toetsbare succescriteria? (items 1 & 3)
3. **Architectuurpatronen:** Anthropic's 5 effective-agent-patronen, single-agent vs. multi-agent, agentic vs. workflow, MCP-architectuur — wanneer kies je wat? (items 2 & 5)
4. **Data, context, bronnen:** welke vragen stel je in de blueprint over RAG, knowledge graph, retrieval, en hoe verbind je dat met BB_03? (item 4)
5. **Risk-based design:** hoe gebruik je EU AI Act-risico-classificatie en HLEG Trustworthy AI als ontwerp-input? Wat zijn de bewezen patronen voor guardrails-by-design? (item 6)
6. **Iteratie & FDE:** wat houdt Forward Deployed Engineering precies in (Palantir-model), wanneer werkt het, wanneer niet? Hoe ziet een levend blueprint-document eruit? (item 7 + audit-example)
7. **Stakeholder-validatie:** welke patronen werken voor sign-off zonder de iteratie-snelheid te doden? (item 7)
8. **Prototype-driven blueprinting:** wat verandert er als je met de klant *kijkt* in plaats van *leest* — dat wil zeggen: een werkend (of half-werkend) prototype gebouwd in tools als Lovable, v0, Bolt, Google Stitch of Claude-Artifacts/Canvas — als blueprint-vehikel? Wanneer is dat productief, wanneer juist contraproductief?
9. **Playbook-structuur:** welke gespreks- en werkstructuur werkt om alle blueprint-elementen (doel, processen, output, data, tools, risico's, sign-off) systematisch met een klant door te lopen? Concrete templates of frameworks die in de praktijk werken.

## Strategie

**Scale decision:** Breed/complex multi-domein — 4 parallelle research-lanes
**Aantal researchers:** 4 (parallel via deep-research subagents)
**Geschatte rondes:** 1-2

**Dimensie-verdeling:**

- **Lane 1 — Use case-selectie & probleem-framing**
  Decision-first (Kozyrkov), Karpathy "Software 3.0", MIT-Lossless 95%-fail-studie, "AI-first vs. AI-augmented", outcome-mapping. Welke problemen *moet* je niet met AI willen oplossen.

- **Lane 2 — Architectuurpatronen voor AI-systemen**
  Anthropic "Building effective agents" (5 patronen), ReAct/Plan-Then-Execute, single→multi-agent decision matrix, MCP-architectuur, model-router-patroon. Wanneer kies je een workflow, wanneer een agent.

- **Lane 3 — Risk-based design & guardrails-by-design**
  EU AI Act risico-classificatie (unacceptable/high/limited/minimal) als design-input, HLEG Trustworthy AI 7-requirements als blueprint-checks, privacy-by-design + DPIA tijdens blueprint, OWASP LLM Top-10 voor threat modeling, quality criteria upfront (koppeling BB_07).

- **Lane 4 — Iteratieve blueprint, FDE, prototype-driven & playbook**
  Forward Deployed Engineering (Palantir): ontstaan, principes, beperkingen. Living blueprint vs. waterval-design-doc. One-pager vs. dik design-document. Stakeholder sign-off-cycli.
  Prototype-driven blueprinting: AI-prototyping-tools (Lovable, v0, Bolt, Google Stitch, Claude Artifacts/Canvas) als blueprint-vehikel — werkende UI als gespreks-anker in plaats van tekst-blueprint. Wanneer productief, wanneer schijn-zekerheid?
  Playbook/workflow-structuur: gestructureerde gespreksleidraad om alle blueprint-elementen met een klant door te lopen. Concrete templates die in de praktijk werken (bijv. Anthropic's "Building effective agents" workflows, Google's Agent Starter Kit, IDEO design-thinking-templates voor AI).

## Acceptatiecriteria

- [ ] Alle 7 BB_02-checklist-items beantwoord met ≥2 onafhankelijke bronnen
- [ ] Anthropic's 5 agent-patronen vergeleken met andere referentie-architecturen (Microsoft, Google, AWS) op overlap/verschillen
- [ ] EU AI Act risico-tier → blueprint-implicaties expliciet uitgewerkt (high-risk implicaties voor design)
- [ ] FDE als concept expliciet onderbouwd: definitie, oorsprong (Palantir), kernprincipes, beperkingen, alternatieven (geen overhype, ook contra-perspectief)
- [ ] MIT-Lossless 95% claim ondersteund of als "inferred" gelabeld
- [ ] ≥3 actuele AI-prototyping-tools (2025-2026) beschreven met sterktes/beperkingen voor blueprint-gebruik
- [ ] ≥1 concrete playbook-/workflow-template uit de praktijk uitgewerkt (anchored in een gepubliceerde bron, niet alleen Robin's intuïtie)
- [ ] Prototype-driven blueprinting: zowel productieve patronen als faalmodi (schijn-zekerheid, scope-lock-in op early UI) in beeld
- [ ] Tegenstrijdigheden tussen bronnen geïdentificeerd
- [ ] Geen single-source claims op kritieke findings

## Task Ledger

| ID | Owner | Taak | Status | Output |
|----|-------|------|--------|--------|
| T1 | researcher-usecase | Use case-selectie & probleem-framing | done | research-usecase-framing.md |
| T2 | researcher-architectuur | Architectuurpatronen AI-systemen | done | research-architectuur.md |
| T3 | researcher-risk | Risk-based design & guardrails-by-design | done | research-risk-design.md |
| T4 | researcher-fde | FDE, iteratieve blueprint & stakeholder-validatie | done | research-fde-iteratie.md |
| L1 | lead | Synthese + draft | done | draft.md |
| L2 | lead | Cite + verify + final | done | final.md |

## Verificatie-log (in te vullen tijdens uitvoering)

| Item | Methode | Status | Bewijs |
|------|---------|--------|--------|
| MIT 95% AI-pilot-fail | web fetch Fortune + Marketing AI Institute kritiek | verified + kritiek-gedocumenteerd | fortune.com/2025/08/18/... + marketingaiinstitute.com |
| Anthropic 5 agent-patronen authoritative bron | directe fetch anthropic.com/research/building-effective-agents | verified | anthropic.com/research/building-effective-agents |
| EU AI Act risico-tiers definitie | directe fetch artificialintelligenceact.eu | verified | artificialintelligenceact.eu/high-level-summary/ |
| FDE Palantir-oorsprong | directe fetch Pragmatic Engineer + SSO Network | verified | newsletter.pragmaticengineer.com/p/forward-deployed-engineers |
| HLEG Trustworthy AI 7 requirements | directe fetch EU Commission + ALTAI | verified | digital-strategy.ec.europa.eu + altai.insight-centre.org |
| AI-prototyping-tools landscape 2026 | NxCode vergelijking + Lenny's Newsletter | verified | nxcode.io + lennysnewsletter.com |
| Concreet AI-blueprint-playbook | WorkOS + AI-3P Framework + Stanford PDF (niet leesbaar) | partial — geen enkele kant-en-klare template gevonden | workos.com + towardsdatascience.com |

## Decision-log

- 2026-04-26 12:05 — Plan opgesteld op basis van BB_01/BB_03 plan-templates. 4 lanes gekozen op basis van checklist-coverage: lane 1 dekt items 1+3, lane 2 dekt items 2+5, lane 3 dekt items 4+6, lane 4 dekt item 7 en het iteratieve karakter.
- 2026-04-26 12:05 — Bewust geen aparte data-lane: BB_03 dekt dat al. Wel een check op cross-cut bij blueprint-vragen over data.
- 2026-04-26 12:15 — Robin akkoord met scope. Toevoeging op lane 4: prototype-driven blueprinting (AI-prototyping-tools als blueprint-vehikel) en playbook-/workflow-structuur als systematische gespreksleidraad. Reden: dit is Robin's eigen werkpraktijk en de huidige BB_02 mist dit perspectief volledig.
- 2026-04-26 12:15 — Robin levert na de research-fase een eigen Client-Blueprint-voorbeeld uit een ander project aan om naast de bevindingen te leggen. Vóór step 3 (MDX-uitbouw) inplannen.
