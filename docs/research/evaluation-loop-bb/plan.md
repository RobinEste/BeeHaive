# Onderzoeksplan: Evaluation Loop (BB_07) — BeeHaive Building Block

**Slug:** evaluation-loop-bb
**Aanmaakdatum:** 2026-05-02
**Status:** 🔄 In progress

## Budget & stop-criteria

```yaml
max_rounds: 2              # harde bovengrens op researcher-rondes
token_budget_kt: 180       # totaal input+output tokens (kT) over alle rondes
stop_on_no_new_urls: true  # stop als ronde N geen nieuwe URLs oplevert t.o.v. N-1
```

Stop wanneer **één** criterium voldoet. Lead agent logt welk criterium triggerde in `## Decision-log`.

## Onderzoeksvraag

Wat is de stand van de praktijk rondom Evaluation Loop voor AI-systemen in 2025–2026, en hoe kan BeeHaive Building Block BB_07 worden uitgebouwd tot een diepgaand, praktisch en goed onderbouwd hoofdstuk vergelijkbaar met BB_03 (Dynamic Context), BB_04 (Prompt Design), BB_05 (Tool Integration) en BB_06 (Model Engines)?

De huidige BB_07 bevat slechts een introductie van ~150 woorden. Het onderzoek moet voldoende materiaal opleveren voor 6–7 BBDisclosure-secties met praktijkdiepgang (elk 300–600 woorden), inclusief minstens één sectie over governance/compliance en één over stille faalmodi.

## Kernvragen

1. **Wat is de geaccepteerde definitie van "Evaluation Loop" / "AI eval" / "evals" in de AI-wereld in 2025–2026?** Onderzoek expliciet:
   - Welke term wordt waar gebruikt: *eval*, *evaluation*, *evals*, *evaluation harness*, *evaluation loop*, *eval pipeline*. Verschilt het tussen academisch (NeurIPS/ACL papers, HELM, BIG-Bench) en industrie (Anthropic, OpenAI, Google DeepMind, Meta)?
   - Welke autoritatieve bronnen geven een werkdefinitie? Anthropic's "Building evals" guidance, OpenAI Evals/Cookbook, Google's eval-framework, het Stanford HELM-project, NIST AI RMF, ISO/IEC 42001, EU AI Act-terminologie.
   - Wat is het *minimale* kenmerk dat iets tot een "evaluation loop" maakt (vs. een one-shot test, vs. een benchmark)? De *loop*-component (continu, gesloten cyclus met verbeteractie) onderscheidt het van een eenmalige eval.
   - Is er een convergerende of juist divergerende definitie? Citeer bestaande definities woordelijk (4–8 stuks) en synthetiseer een werkdefinitie die cross-bronnen recht doet.
   - Hoe verhoudt Evaluation Loop zich tot aangrenzende termen: *observability*, *monitoring*, *MLOps*, *AgentOps*, *quality assurance*? Waar zit de grens?

2. **Wat is een productie-rijpe evaluation loop in 2025–2026?** Welke fasen bevat hij (pre-deploy offline eval, shadow mode, canary, post-deploy online eval, drift monitoring), en welke ontwerpkeuzes bepalen of de loop daadwerkelijk leidt tot verbetering in plaats van rapportage-theater?

3. **Hoe meet je kwaliteit en betrouwbaarheid van niet-deterministische AI-output?** Welke metrieken zijn de praktijkstandaard (exact-match, semantic similarity, rubric-scoring, LLM-as-judge), wanneer falen ze, en hoe ga je om met reproduceerbaarheid en statistische significantie bij kleine eval-sets?

4. **Hoe ontwerp je een eval-set?** Grootte, diversiteit, edge-cases, regressie-cases, golden datasets vs. synthetisch gegenereerde data. Wat zijn de bekende valkuilen (eval-set leakage in trainingsdata, overfitting op eval-criteria, judge-bias)?

5. **LLM-as-judge: hoe kalibreer je een rechter-model?** Cohen's Kappa, inter-rater reliability, judge-bias (positie-, lengte-, zelf-voorkeur). Welke targets zijn gangbaar (0.6 / 0.7 / 0.8) en wanneer is een mens onvermijdelijk in de lus?

6. **Hoe evalueer je multi-turn en agentic systemen?** Eind-tot-eind taakuitvoering vs. tussenstappen, trajectory evaluation, tool-call-correctness, plan-quality. Verschil met single-turn eval.

7. **Wat zijn de operationele patronen voor continue evaluatie in productie?** Online evaluation (klik-feedback, escalatie-rate, user-rating), shadow mode, canary releases, A/B-testing van prompts/modellen, drift-detectie (data drift, concept drift, performance drift).

8. **Wat zijn de governance- en compliance-eisen?** EU AI Act Art. 9 (risk management), Art. 10 (data governance, bias monitoring), Art. 15 (accuracy/robustness), Art. 17 (quality management system), Art. 72 (post-market monitoring). Hoe vertaalt dit zich naar concrete eval-architectuur en bewaartermijnen?

9. **Welke tools en platforms zijn de gangbare standaard in 2026?** LangSmith, W&B Weave, Braintrust, Humanloop, Arize Phoenix, OpenAI Evals, ragas, deepeval, inspect_ai. Wat zijn de trade-offs (open source vs. SaaS, eval-as-code vs. GUI, kostenmodel)?

10. **Wat zijn de meest voorkomende anti-patronen?** Vibe-checking, demo-driven development, single-metric tunnel-vision, eval-set staleness, judge-model contaminatie, "we evalueren alleen happy path", Goodhart's law in eval-design.

11. **Hoe verhoudt Evaluation Loop zich tot de andere zes BeeHaive-bouwstenen?** Knowledge (BB_01) levert eval-criteria; Client Blueprint (BB_02) bepaalt succescriteria; Dynamic Context (BB_03) wordt geëvalueerd op grounding; Prompt Design (BB_04) wordt regression-tested; Tool Integration (BB_05) op tool-correctness; Model Engines (BB_06) op modelvergelijking.

## Strategie

**Scale decision:** breed onderzoek, drie parallelle dimensies
**Aantal researchers:** 3 parallelle researchers
**Geschatte rondes:** 1–2

**Dimensie-verdeling:**
- Researcher 1 — **Definitie & methoden**: Kernvraag 1 (definitie-zoektocht inclusief woordelijke citaten van Anthropic, OpenAI, Google DeepMind, HELM, NIST AI RMF, ISO 42001), Kernvragen 2–6 (eval-design, dataset-construction, LLM-as-judge calibration, multi-turn/agentic eval)
- Researcher 2 — **Governance & compliance**: Kernvraag 8 (EU AI Act Art. 9/10/15/17/72, ISO/IEC 42001, NIST AI RMF, post-market monitoring, bewaartermijnen), Nederlandse implementatie en sectorale toezichthouders (AP, AFM, ACM, IGJ, NZa, Inspectie van het Onderwijs)
- Researcher 3 — **Tooling & praktijk**: Kernvraag 9 (LangSmith / W&B Weave / Braintrust / Humanloop / Arize Phoenix / OpenAI Evals / ragas / deepeval / inspect_ai), Kernvraag 7 (operationele patronen), Kernvraag 10 (anti-patronen), case studies van eval-loops in productie (bv. Anthropic, OpenAI, ServiceNow, Klarna), kosten van eval

## Task Ledger

| ID | Owner | Taak | Status | Output |
|----|-------|------|--------|--------|
| T1 | researcher-1 | Definitie & methoden (KV 1-6) | done | research-definitie-methoden.md |
| T2 | researcher-2 | Governance & compliance (KV 8) | done | research-governance.md |
| T3 | researcher-3 | Tooling & praktijk (KV 7, 9-11) | done | research-tooling-praktijk.md |
| L1 | lead | Synthese + draft | done | draft.md |
| L2 | lead | Cite + verify + final | done | final.md |

## Decision-log

- 2026-05-01 12:00 — Ronde 1 gestart; 3 parallelle researchers gedispatcht.
- 2026-05-01 14:00 — Ronde 1 afgerond. Stop-criterium: `rounds_completed >= 1` + acceptatiecriteria voldaan. Alle 11 kernvragen beantwoord, 7 woordelijke definities voor KV1, voldoende materiaal voor 6-7 BBDisclosures. Geen ronde 2 nodig.

## Acceptatiecriteria

- [ ] Alle 11 kernvragen beantwoord met ≥2 onafhankelijke bronnen
- [ ] **Specifiek voor Kernvraag 1**: minstens 4–8 woordelijke definities uit primaire bronnen (Anthropic, OpenAI, Google, NIST, ISO, academische papers), plus een gesynthetiseerde werkdefinitie die uitlegt wat de gemene deler is en waar de bronnen verschillen. Geef expliciet aan welke term ("eval", "evaluation", "evaluation loop") in welke context dominant is.
- [ ] Tegenstrijdigheden geïdentificeerd en geadresseerd (single-source claims gemarkeerd)
- [ ] Voldoende materiaal voor 6–7 BBDisclosure-secties van elk 300–600 woorden
- [ ] Productiegericht: patronen, anti-patronen, trade-offs, beslisheuristieken
- [ ] Specifieke aandacht voor stille faalmodi (eval-set leakage, judge-bias, drift zonder alarm) — eval is bij uitstek gevoelig voor "we meten iets, dus het is goed"
- [ ] Concrete numerieke richtlijnen waar mogelijk (eval-set grootte, Cohen's Kappa targets, P50/P95-budgetten, drift-thresholds)
- [ ] Inhoudelijke verankering: minstens één primaire bron per harde claim over benchmarks, releasedata, marktposities, wettelijke artikelen
- [ ] Wettelijk-artikel-precisie: bij EU AI Act-citaties exact artikel noemen (Art. 9 ≠ Art. 17 ≠ Art. 72), niet generiek "EU AI Act"
