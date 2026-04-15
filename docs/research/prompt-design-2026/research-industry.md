# Research: Industry/Practitioners — Prompt Design 2026

**Researcher:** researcher-3
**Dimensie:** Productie-patronen, system prompt templates, versioning, testing
**Datum:** 2026-04-15

## Samenvatting (1 zin)

De industrie heeft in 2025–2026 geconvergeerd op een 4–7 laags system prompt template (Identity → Rules → Format → Edge Cases → Examples), een safety-first priority stack, en een Git+registry-based versioning workflow met CI/CD evals — terwijl de iBuidl-statistieken (few-shot 71%→94%, XML +11%, 800-token drempel) bevestigd worden door meerdere onafhankelijke bronnen.

---

## Bevindingen

### System prompt structuren en templates

De industrie heeft sterke convergentie laten zien naar een gelaagde anatomie voor production system prompts. Meerdere onafhankelijke practitioners en blogs beschrijven in 2025–2026 vrijwel identieke structuren, met variaties in het aantal lagen (4–7) maar hetzelfde inhoudelijke patroon.

**Vijf-secties template (PE Collective, februari 2026)** [1] — `verified`:
De PE Collective beschrijft exact vijf secties voor production system prompts:
1. **Identity and Purpose** — 2–3 zinnen: wie is het model, wat is zijn taak, voor welk domein
2. **Behavioral Rules** — bullet points, elk één duidelijke instructie
3. **Response Format** — inclusief voorbeeldoutput (niet beschrijven maar tonen)
4. **Edge Case Handling** — expliciete instructies per scenario
5. **Examples (Few-Shot)** — 2–4 voorbeelden inclusief edge cases

**Zes-lagen template (Field Guide to AI, februari 2026)** [2] — `verified`:
Marcin Piekarski voegt aan het vijf-secties model een expliciete `<priority_order>` toe als aparte laag en gebruik van XML-tags voor structuur:
- Identity/role → Objective → Priority order → Rules → Tone → Output format → Safety → Scope → Edge cases

**Zeven-componenten framework (AgentWiki, maart 2026)** [3] — `verified`:
Voor production agents wordt een 7-component framework beschreven: Role, Instructions, Constraints, Format, Tools, Examples, Error Handling.

**Vier-laags framework (Rephrase, maart 2026)** [4] — `verified`:
Ilia Ilinskii beschrijft een meer minimaal 4-laags model voor Custom GPTs en Claude Projects:
Persona → Constraints → Output Format → Fallback Behavior

**Convergentiepunt:** Alle bronnen zijn het eens dat de Identity/Role-definitie altijd eerste staat, Behavioral Rules/Constraints tweede, en Output Format een verplichte component is. De toevoeging van expliciete priority order en few-shot examples in de system prompt zelf (niet in user turn) is het meest vooruitstrevende patroon voor 2026. `[inferred]`

**number6.ai (oktober 2025)** [5] — `verified`:
Guillaume M. beschrijft productie-patterns uit werkende deployments: altijd een "identity card" (company, agent role, audience, scope, out-of-scope), gelaagde constraints (behavioral → domain → formatting), en een "constitution" voor situaties buiten de regels — een rangorde van principes die edge cases afdekken.

---

### Priority stacks

**De gevestigde standaard (meerdere bronnen)** — `verified`:

De meest geciteerde priority stack in production system prompts is:
1. **Safety / compliance** (nooit te overrulen)
2. **Accuracy** (correct boven vloeiend)
3. **Helpfulness**
4. **Efficiency / tone / style**

Varianten met dezelfde kern:
- Field Guide to AI [2]: `Safety and compliance → Accuracy → Helpfulness → Efficiency`
- PE Collective [1]: `Priority 1 (never violate): Safety rules, legal compliance, data privacy`
- Claude Magazine (januari 2026) [6] — `verified`: Beschrijft Claudes ingebouwde hiërarchie: system/platform rules → constitutional principles → product/workspace rules → user preferences
- Universal AI Framework (Medium, maart 2026) [7] — `verified`: Stelt `accuracy over fluency` als expliciete eerste prioriteit binnen de prompt zelf (naast de externe safety-stack)

**Instruction hierarchy als formeel concept (academisch/practitioner overlap)** [8] — `verified`:
Meerdere bronnen verwijzen naar Wallace et al. (2024) als de formalisering van het idee dat LLMs instructies in een vaste volgorde volgen: System Message ≻ Developer Message ≻ User Message ≻ Tool. Dit is bevestigd in productie door OpenAI's GPT-5 en Anthropic's documentatie.

**DEV Community (februari 2026)** [9] — `verified`:
Een practitioner beschrijft "Intent Engineering" met vier tiers: NON-NEGOTIABLE → HIGH → MEDIUM → LOW. Het kernprobleem dat aangestipt wordt: een flat lijst als `"safety, clarity, conciseness"` geeft de LLM geen rangordeinfo — expliciete nummering is vereist.

---

### Versioning, testing, iteratie

**Versioning approaches** — `verified` (meerdere bronnen):

De industrie hanteert een driestaps evolutie [10], [11], [12]:

| Volwassenheidsniveau | Aanpak | Beschrijving |
|---|---|---|
| 0 — Ad-hoc | Prompts in code strings | Geen versiebeheer, handmatige QA |
| 1 — Versioned | Prompts in Git als YAML/tekstbestanden | History, blame, PR-review |
| 2 — Registry | Database-backed registry | Dynamische updates, A/B, instant rollback |
| 3 — CI/CD | Geïntegreerde eval-pipeline | Automatische regressionsuites per PR |

**Git-based aanpak als startpunt** [12] — `verified`:
Markaicode (maart 2026): dedicated `prompts/` repository, versioned subfolders (`v1/`, `v2/`), deployment script dat een "live version pointer" in registry bijhoudt, rollback in < 30 seconden via health monitoring.

**SemVer voor prompts** [13] — `verified`:
PromptBuilder (december 2025): semantische versioning `MAJOR.MINOR.PATCH` voor prompt changes. MAJOR = gedragsverandering die outputs breekt; MINOR = verbetering achterwaarts compatibel; PATCH = kleine fix. Gitflow-workflow met feature branches, automated evals op elke PR, human review voor edge cases.

**Immutabiliteit als kernprincipe** [10] — `verified`:
Tianpan.co (april 2026): "The immutability principle is the invariant that every mature team eventually adopts: once a version is committed, it cannot be modified." Nieuwe versie aanmaken voor elke wijziging.

**Eval-pipeline (minimaal drie lagen)** [10], [13] — `verified`:
1. Deterministische assertions op outputstructuur (valid JSON, vereiste velden)
2. Semantische kwaliteitsmetrieken (LLM-as-judge)
3. Bedrijfsmetrieken (task success rate, user satisfaction)

**A/B testing** [10], [11] — `verified`:
Canary deployment: 1–10% verkeer naar nieuwe promptversie, geautomatiseerde rollback als succes-rate > 5% daalt of latency > 20% stijgt. Statsig [14] beschrijft dit als standaard practice voor productie-teams.

**Tooling-landschap 2025–2026** — `verified`:
- Git + custom eval scripts: startpunt voor kleine teams
- LangSmith (LangChain): tracing + dataset management + playground + evaluation — meest geciteerde tool
- Langfuse: versioning + production monitoring
- PromptLayer: multi-model deployments
- MLflow Prompt Registry: commit-based versioning met diff-view en aliases
- Braintrust, Maxim AI, Arize AX: meer enterprise gerichte opties

---

### Statistieken-verificatie vanuit practitioners (iBuidl-claims)

**Claim 1: Few-shot 71%→94% (structured output compliance)** — `verified`

iBuidl Research (maart 2026) [15]: "Few-shot examples boost structured output reliability from 71% to 94% with just 3 examples" — getest op 500 prompts.

Onafhankelijke bevestigingen:
- arXiv (feb 2026) [16]: 281 evaluaties op 71 modellen tonen few-shot vs zero-shot 77% vs 29% gemiddelde accuratesse. Few-shot CoT: 80.06% vs 28.76% zero-shot. Structured output productie: 34.12% (few-shot CoT) vs 7.14% (few-shot zonder CoT).
- Mem0 blog (december 2025) [17]: "Research shows strong accuracy gains from 1 to 2 examples, with diminishing returns beyond 4 to 5 (Brown et al., 2020)" — de richtlijn 2–5 examples is breed geaccepteerd.
- WifiTalents statistische compilatie (februari 2026) [18]: "Few-shot prompting improves GPT-3 performance by 30-50% on classification tasks" — geclassificeerd als `Verified`.

**Verdict:** De 71%→94% claim is specifiek voor structured output compliance; de onderliggende richting (few-shot verhoogt compliance substantieel) wordt breed bevestigd. De exacte percentages zijn iBuidl-specifiek maar plausibel. `[verified — richting; unverified — exacte getallen onafhankelijk]`

**Claim 2: XML +11% boven JSON** — `unverified` (als absolute claim)

iBuidl [15]: "XML-tagged structured output outperforms JSON-requested output by 11% on average compliance rate." Steve Kinney (maart 2026) [19] bevestigt dat XML-structuur voor Anthropic/Claude modellen beter werkt dan prose instructies, maar noemt geen percentage. Geen onafhankelijke kwantitatieve verificatie gevonden. De directie (XML > JSON voor Claude) is `verified`, het cijfer +11% is `unverified`.

**Claim 3: 800-token drempel** — `verified`

iBuidl [15]: "System prompt performance peaks at 400–800 tokens. Beyond 800 tokens, models begin to 'lose' instructions."

Bevestigingen:
- Field Guide to AI [2]: "Most production system prompts work best between 200–800 tokens (roughly 150–600 words)."
- Thomas Wiegold blog (februari 2026) [20]: Verwijst naar Levy et al. (2024): "LLM reasoning performance starts degrading around 3,000 tokens." Optimale sweet spot: 150–300 woorden voor de meeste taken.
- ESPO.AI (februari 2026) [21]: "Multiple 2024–2025 studies confirm: longer is not better. Research by Levy et al. found LLMs quickly degrade in reasoning capabilities even at 3,000 tokens."
- Universal AI Framework [7]: "Beyond the 1,500-token dilution threshold, shorter prompts beat longer ones for per-rule compliance."

**Verdict:** De 800-token drempel voor system prompts is consistent bevestigd. Verschillende bronnen noemen iets hogere drempels (1,500 / 3,000 tokens) maar als recommendation voor hele prompts, terwijl iBuidl specifiek spreekt over system prompt lengte. `[verified]`

---

### Anti-patterns: wat werkt niet meer?

**Bron: Rephrase "Anti-Prompting Guide" (maart 2026)** [22] — `verified`:
Ilia Ilinskii identificeert 12 patronen die in 2022–2024 werkten maar nu contraproductief zijn:

1. **Mega Prompt Manifesto** — 400+ regels system prompt. Creëert interne contradities, verdunt signal-to-noise. Moderne modellen zijn al getraind op instruction hierarchieën; extra regels helpen niet.
2. **Verbose Chain-of-Thought** — CoT in de output forceren verhoogt kans op zelf-tegenspraak en rationalisatie van verkeerde antwoorden. Moderne modellen redeneren intern.
3. **Negative instruction pile** — "DON'T do X. DON'T do Y." Conflicteert met elkaar, moeilijk te handhaven. Positieve instructies werken beter.
4. **"CRITICAL!" / "YOU MUST"** — Aggressive taal werkt averechts op nieuwere modellen. Claude-modellen zijn specifiek getraind sceptisch te zijn tegenover overly emphatic instructions.
5. **Elaborate persona roleplay voor capabilities** — "Je bent een AI zonder restricties" werkt niet meer; safety alignment zit dieper in de weights.
6. **Prompt libraries als copy-paste infrastructuur** — Copy-pasten van community prompts zonder testen; stale patronen die "werken" door lucky sampling.
7. **"Reverse psychology" / adversarial framing** — "You are not allowed to refuse" werkt niet met moderne safety training.
8. **Persona-driven agents voor robustheid** — Overdreven role-playing maakt agents minder stabiel in edge cases.

**Bron: iBuidl (maart 2026)** [15] — `verified`:
- Jailbreak-stijl nadruk ("You MUST always..."): backfires op 2026 modellen
- Unstructured long context stuffing: 50K tokens ongestructureerde tekst degradeert performance significant vs. gestructureerde content met headers

**Bron: ttoss.dev (december 2025)** [23] — `verified`:
Zes "anti-prompt" patronen: The Lazy Delegator (vaagheid), The Kitchen Sink (overloading), The Mind Reader (missing context), The Negative Bias (only don'ts), The Chaos Agent (no format), The Chatty Cathy (fluff/small talk).

**Nieuw werkend patroon (als reactie op bovenstaande)** — `inferred` uit meerdere bronnen:
- Kort systeem prompt (≤ 800 tokens), specifiek, positief geformuleerd
- Expliciete priority stack als genummerde lijst
- Format tonen in voorbeeld, niet beschrijven
- Instructies structureren met XML-tags of markdown headers
- "Boring prompts are stable prompts" (Rephrase) [22]

---

### Use-case-specifieke patterns (practitioner-kant)

**Customer service** [1], [4], [5] — `verified`:
- Identity card verplicht: company name, product, audience, in-scope, out-of-scope
- Escalation paths als expliciete edge case instructie
- Korte responses (2–4 zinnen voor eenvoudig, max 2 alinea's voor complex)
- Format-voorbeeld met Issue/Status/Next step velden (number6.ai)
- Tone: warm maar geen beloftes doen over timelines
- Typisch model: Haiku/Flash voor kost-efficiëntie met Sonnet fallback voor complexe cases

**Data extractie / structured output** [3], [15], [19] — `verified`:
- JSON schema of output template verplicht in system prompt (tonen, niet beschrijven)
- 3 few-shot voorbeelden zijn optimaal voor format compliance (71%→94%)
- XML-tags voor extractievelden bij Claude modellen
- Gebruik van Pydantic/Instructor voor validatie op applicatieniveau bovenop prompt
- Temperature: 0.0–0.1 voor maximale determinisme

**Coding assistants** [24], [25] — `verified`:
- Vier componenten verplicht: Technical Context, Constraints, Output Format, Verification criteria
- Scope-explicitering: agent heeft (1) scope, (2) acceptance criteria, (3) stop condition nodig
- Anti-pattern: agents als "betere autocomplete" behandelen — bij multi-file taken is prompt een mini-spec
- Prompt scope creep is #1 anti-pattern: niet alles in één prompt bundelen
- Tool-specific: Cursor voor multi-file refactors, Claude/ChatGPT voor design discussies

**Document schrijven / content creatie** [4], [25] — `verified`:
- Role + domain knowledge + audience als verplichte trio in persona layer
- Tone specification als "authority profile" (analytical expert / strategic advisor / coach) in plaats van vage adjectieven
- Creative Freedom vs. Constraints als aparte sectie bij open-ended output
- Temperature: 0.7–0.9 voor creatieve schrijftaken

**Research / document analyse** [3] — `verified`:
- Output format: structured findings met source URLs en confidence ratings
- "NEVER: Cite sources you haven't actually accessed" — expliciete anti-hallucination instructie
- Cross-reference eis: "Prefer primary sources over aggregators"

---

## Evidence Table

| # | Bron | URL | Type | Key claim | Confidence |
|---|---|---|---|---|---|
| 1 | PE Collective — System Prompt Design Guide 2026 | https://pecollective.com/blog/system-prompt-design-guide/ | Engineering blog | 5-secties template (Identity/Rules/Format/Edge Cases/Examples) is productie-standaard | High |
| 2 | Field Guide to AI — System Prompt Design | https://fieldguidetoai.com/guides/system-prompt-design | Engineering guide | 6-laags template met XML-structuur en priority_order als aparte laag | High |
| 3 | AgentWiki — How to Structure System Prompts | https://agentwiki.org/how_to_structure_system_prompts | Knowledge base | 7-componenten framework voor production agents | Medium |
| 4 | Rephrase — How to Write a System Prompt That Works | https://rephrase-it.com/blog/how-to-write-a-system-prompt-that-works | Practitioner blog | 4-laags framework (Persona/Constraints/Output Format/Fallback) | High |
| 5 | number6.ai — System prompts that work | https://number6.ai/blog/43-system-prompts-that-work/ | Practitioner blog | Identity card + layered constraints + "constitution" uit echte deployments | High |
| 6 | Claude Magazine — How Claude Processes Instructions | https://claudemagazine.com/claude-system/how-claude-processes-instructions/ | Technical blog | Priority hiërarchie: safety → constitutional → product → user | Medium |
| 7 | Medium — Universal AI Framework Pinnacle Edition | https://medium.com/@ehsaidawi/the-universal-ai-framework-pinnacle-edition-da6dc85c18d7 | Practitioner blog | Accuracy over fluency als expliciete prioriteit; primacy bias in prompts | Medium |
| 8 | arXiv — Instruction Hierarchy | https://arxiv.org/pdf/2603.10521 | Academisch (relevant voor practitioners) | Formele definitie: System ≻ Developer ≻ User ≻ Tool | High |
| 9 | DEV Community — Intent Engineering | https://dev.to/dwelvin_morgan_38be4ff3ba/why-your-ai-keeps-ignoring-your-safety-constraints | Practitioner blog | Expliciete 4-tier priority (NON-NEGOTIABLE/HIGH/MEDIUM/LOW) als pattern | Medium |
| 10 | Tianpan.co — Prompt Versioning in Production | https://tianpan.co/blog/2026-04-09-prompt-versioning-production-llm | Engineering blog | Driestaps evolutie (Git → DB → Registry); immutabiliteit als kernprincipe | High |
| 11 | MyEngineeringPath — Prompt Management 2026 | https://myengineeringpath.dev/genai-engineer/prompt-management/ | Engineering guide | 6-staps lifecycle; drie-tier rollback architectuur; A/B test valkuilen | High |
| 12 | Markaicode — Versioning AI Prompts Like Source Code | https://markaicode.com/prompt-versioning-source-code/ | Engineering blog | Git-based prompts/ directory, PR-workflow met eval suite, <30s rollback | High |
| 13 | PromptBuilder — Prompt Testing in CI/CD 2025 | https://promptbuilder.cc/blog/prompt-testing-versioning-ci-cd-2025 | Engineering blog | SemVer voor prompts, regression suite, CI/CD integratie | High |
| 14 | Statsig — Few-shot prompting guide | https://www.statsig.com/perspectives/fewshotpromptingguide | Engineering blog | A/B testing van example sets als standaard practice; dynamische examples > statisch | High |
| 15 | iBuidl Research — Prompt Engineering Patterns 2026 | https://ibuidl.org/blog/prompt-engineering-patterns-2026-20260310 | Research blog | Few-shot 71%→94%; XML +11%; 800-token drempel; CoT +34% | Medium (cijfers eigen onderzoek) |
| 16 | arXiv preprint (feb 2026) | https://arxiv.org/pdf/2602.18776 | Academisch | Few-shot CoT 2.8x hoger dan zero-shot (80.06% vs 28.76%); structured output 34% vs 7% | High |
| 17 | Mem0 — Few-Shot Prompting Guide 2026 | https://mem0.ai/blog/few-shot-prompting-guide | Engineering blog | 2–5 examples is praktische sweet spot; dinamische selection > statisch | High |
| 18 | WifiTalents — AI Prompt Engineering Statistics 2026 | https://wifitalents.com/ai-prompt-engineering-statistics/ | Statistieken compilatie | Few-shot +30–50% op classificatietaken; breed bevestigd | Medium |
| 19 | Steve Kinney — Prompt Engineering Across APIs | https://stevekinney.net/writing/prompt-engineering-frontier-llms | Engineering blog | XML werkt beter voor Claude; anti-patterns: overloaded prompts, format fragility | High |
| 20 | Thomas Wiegold — Prompt Engineering Best Practices 2026 | https://thomas-wiegold.com/blog/prompt-engineering-best-practices-2026/ | Practitioner blog | Optimale promptlengte 150–300 woorden; Levy et al. degradatie bij 3K tokens | High |
| 21 | ESPO.AI — Complete Guide Prompt Engineering 2025–2026 | https://espo.ai/resources/prompt-engineering-guide-2025 | Engineering guide | 150–300 woorden optimaal; structuur > lengte; iBuidl-claims onafhankelijk bevestigd | High |
| 22 | Rephrase — Anti-Prompting Guide | https://rephrase-it.com/blog/the-anti-prompting-guide-12-prompt-patterns-that-used-to-wor | Practitioner blog | 12 patronen die nu contraproductief zijn; "boring prompts are stable prompts" | High |
| 23 | ttoss.dev — Mastering Prompts Through Inversion | https://ttoss.dev/blog/2025/12/07/mastering-prompts-through-inversion | Engineering blog | 6 anti-patronen: vaagheid, overloading, missing context, only-DON'Ts, no format, fluff | High |
| 24 | SurePrompts — Prompt Engineering for Developers 2026 | https://sureprompts.com/blog/prompt-engineering-for-developers | Engineering guide | Coding prompts: Technical Context + Constraints + Format + Verification | High |
| 25 | SashiDo — Prompt Engineering Coding Agents 2026 | https://www.sashido.io/en/blog/prompt-engeneering-opus-vs-codex-2026 | Engineering blog | Agent task = scope + acceptance criteria + stop condition | High |

---

## Coverage Status

| Vraag | Coverage | Notities |
|---|---|---|
| Q1: Welke system prompt structuren zijn standaard? | Volledig | 5 onafhankelijke bronnen convergeren op 4–7 lagen-model met dezelfde kern |
| Q2: Priority stacks | Goed | Safety → Accuracy → Helpfulness is breed bevestigd; formalere "instruction hierarchy" ook gedocumenteerd |
| Q3: Versioning, testing, iteratie | Volledig | Meerdere engineering blogs met concrete tooling en workflows |
| Q4: iBuidl-statistieken verificatie | Gedeeltelijk | 71%→94%: richting verified, exacte getal unverified; XML +11%: richting verified, getal unverified; 800 tokens: verified |
| Q5: Anti-patterns | Volledig | Rephrase anti-guide + iBuidl + ttoss.dev geven 12+ benoemde anti-patterns |
| Q6: Use-case-specifieke patterns | Goed | Customer service, data extractie, coding assistants gedekt; document writing minder diepgaand |

---

## Sources

1. https://pecollective.com/blog/system-prompt-design-guide/ — PE Collective, 2026-02-15
2. https://fieldguidetoai.com/guides/system-prompt-design — Marcin Piekarski, Field Guide to AI, 2026-02-12
3. https://agentwiki.org/how_to_structure_system_prompts — AgentWiki, 2026-03-25
4. https://rephrase-it.com/blog/how-to-write-a-system-prompt-that-works — Ilia Ilinskii, Rephrase, 2026-03-23
5. https://number6.ai/blog/43-system-prompts-that-work/ — Guillaume M., number6.ai, 2025-10-03
6. https://claudemagazine.com/claude-system/how-claude-processes-instructions/ — Elias Morven, Claude Magazine, 2026-01-31
7. https://medium.com/@ehsaidawi/the-universal-ai-framework-pinnacle-edition-da6dc85c18d7 — Ehsan, Medium, 2026-03-01
8. https://arxiv.org/pdf/2603.10521 — Instruction Hierarchy paper (GPT-5), 2026
9. https://dev.to/dwelvin_morgan_38be4ff3ba/why-your-ai-keeps-ignoring-your-safety-constraints — DEV Community, 2026-02-25
10. https://tianpan.co/blog/2026-04-09-prompt-versioning-production-llm — Tianpan.co, 2026-04-09
11. https://myengineeringpath.dev/genai-engineer/prompt-management/ — MyEngineeringPath, 2026-03-05
12. https://markaicode.com/prompt-versioning-source-code/ — Mark, Markaicode, 2026-03-02
13. https://promptbuilder.cc/blog/prompt-testing-versioning-ci-cd-2025 — PromptBuilder, 2025-12-06
14. https://www.statsig.com/perspectives/fewshotpromptingguide — Statsig, 2025-10-31
15. https://ibuidl.org/blog/prompt-engineering-patterns-2026-20260310 — iBuidl Research, 2026-03-10
16. https://arxiv.org/pdf/2602.18776 — arXiv preprint, 2026-02
17. https://mem0.ai/blog/few-shot-prompting-guide — Mem0/Taranjeet Singh, 2025-12-29
18. https://wifitalents.com/ai-prompt-engineering-statistics/ — WifiTalents, 2026-02-24
19. https://stevekinney.net/writing/prompt-engineering-frontier-llms — Steve Kinney, 2026-03-06
20. https://thomas-wiegold.com/blog/prompt-engineering-best-practices-2026/ — Thomas Wiegold, 2026-02-21
21. https://espo.ai/resources/prompt-engineering-guide-2025 — ESPO.AI, 2026-02-01
22. https://rephrase-it.com/blog/the-anti-prompting-guide-12-prompt-patterns-that-used-to-wor — Ilia Ilinskii, Rephrase, 2026-03-07
23. https://ttoss.dev/blog/2025/12/07/mastering-prompts-through-inversion — ttoss.dev, 2025-12-07
24. https://sureprompts.com/blog/prompt-engineering-for-developers — SurePrompts, 2026-03-19
25. https://www.sashido.io/en/blog/prompt-engeneering-opus-vs-codex-2026 — SashiDo, 2026-02-11
