# Onderzoeksplan: Prompt Design 2026 — de volwassen discipline

**Slug:** `prompt-design-2026`
**Aanmaakdatum:** 2026-04-15
**Status:** 🟡 In uitvoering

## Onderzoeksvraag

Wat is de actuele stand van zaken rond Prompt Design (okt 2024 – apr 2026), gemeten langs de 8 focusvragen die de BeeHaive BB_04-pagina onderbouwen, verrijken en valideren? Specifiek: klopt het BeeHaive-narratief "van LLM-management naar betekenis-articulatie", zijn de pilot-statistieken reproduceerbaar, en welke productie-patronen, agentic design-principes en guardrail-implicaties zijn nu gevestigd?

## Kernvragen (8)

1. Welke technieken zijn gepromoveerd / achterhaald de afgelopen 12-18 maanden?
2. Klopt het narratief "van LLM-management naar betekenis-articulatie"? Bevestigd of genuanceerd?
3. Welke production-patterns zijn standaard voor system prompts (5-secties template, priority stacks, versioning, testing)?
4. Agentic prompt design: beslisbomen, deterministische vs probabilistische beslissing, loop-ontwerp, refuse/error-handling?
5. Zijn de iBuidl-statistieken reproduceerbaar? few-shot 71%→94% (3 examples), XML +11% vs JSON, CoT +34%, 800-token drempel?
6. Hoe verschilt prompt design per frontier-model (Claude, GPT-5, Gemini 2.5/3)? Wat blijft invariant, wat is model-specifiek?
7. Relatie Prompt Design ↔ andere BeeHaive-bouwstenen (Evaluation Loop, Knowledge)?
8. Guardrail-implicaties: Transparency, Human Agency, Accountability voor production prompts?

## Strategie

**Scale decision:** complex, multi-domein → 4 parallelle researchers
**Geschatte rondes:** 1 (mogelijk 2 als statistieken-verificatie zwak is)

**Dimensie-verdeling:**
- **R1 — Academisch/foundational:** arXiv-papers, ACL/EMNLP, benchmarks, evaluatiestudies. Focus: zijn de iBuidl-statistieken reproduceerbaar? Wat zegt peer-reviewed onderzoek over few-shot, CoT, output-formatting? Tijdsvenster 2024-10 → 2026-04.
- **R2 — Official vendor docs:** Anthropic, OpenAI, Google officiële prompt-engineering docs en release notes. Focus: officiële best practices, hoe verschilt het per model, wat is modelonafhankelijk? Inclusief Anthropic prompt-engineering-docs, OpenAI guide, Google Gemini prompting.
- **R3 — Industry/practitioners:** productie-patronen, system prompt templates, versioning, testing, priority stacks. Gevestigde tech blogs met provenance (PE Collective, Anthropic engineering blog, engineering-blogs van bedrijven). Tijdsvenster 2024-10 → 2026-04.
- **R4 — Agentic + guardrails:** agentic prompt design specificiek, EU AI Act-implicaties, Transparency/Human Agency/Accountability voor prompt design in productie.

## Afbakening

Context engineering, memory, tool selection, RAG → NIET in scope (zie `resources/frameworks/context-engineering.md`).
BeeHaive pilot-run `docs/research/2026-04-03-bb-prompt-design.md` is startpunt — niet opnieuw doen, wel uitbreiden.
Uitgesloten brontypen: YouTube, LinkedIn, X/Twitter, Reddit, Quora, GitHub issues.

## Acceptatiecriteria

- [ ] Focusvragen 1-4 beantwoord met ≥2 onafhankelijke bronnen
- [ ] Statistieken (Q5): geaccepteerd, genuanceerd of verworpen op basis van ≥2 bronnen
- [ ] Q6 (model-verschillen) heeft concrete voorbeelden per model
- [ ] Q7 (relatie andere BBs) minimaal 2 concrete koppelingen onderbouwd
- [ ] Q8 (guardrails) gekoppeld aan EU AI Act-tekst of officieel beleidsdocument

## Task Ledger

| ID | Owner | Taak | Status | Output |
|----|-------|------|--------|--------|
| T1 | researcher-academisch | arXiv-papers, benchmarks, statistieken-verificatie | todo | research-academisch.md |
| T2 | researcher-vendor-docs | Officiële docs Anthropic/OpenAI/Google | todo | research-vendor-docs.md |
| T3 | researcher-industry | Production-patterns, system prompt templates, testing | todo | research-industry.md |
| T4 | researcher-agentic-guardrails | Agentic prompt design + EU AI Act guardrails | todo | research-agentic-guardrails.md |
| L1 | lead | Synthese + draft | todo | draft.md |
| L2 | lead | Cite + verify | todo | final.md |
| L3 | lead | Atom naar resources/frameworks/ | todo | resources/frameworks/prompt-design.md |

## Verificatie-log

| Item | Methode | Status | Bewijs |
|------|---------|--------|--------|
| few-shot 71%→94% (iBuidl) | cross-source R1+R2 | pending | — |
| XML +11% vs JSON | cross-source R1+R3 | pending | — |
| CoT +34% multi-step | cross-source R1 | pending | — |
| 800-token system prompt drempel | cross-source R1+R3 | pending | — |

## Decision-log

- 2026-04-15 10:30 — Output in BeeHaive docs/research/ (i.p.v. claude-code-framework) omdat BeeHaive pilot-research er al staat + BeeHaive de primaire afnemer is. Eindsynthese als atom naar `resources/frameworks/prompt-design.md`.
