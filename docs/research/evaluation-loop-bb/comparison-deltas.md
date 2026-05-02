# Delta-analyse — Evaluation Loop onderzoeksbronnen

**Datum:** 2026-05-02
**Doel:** vergelijken van twee parallelle onderzoeksbronnen voor BB_07 om te bepalen welke materialen `final.md` aanvullen vóór `/bb-write`.

## Bronnen op tafel

| Bron | Bestand | Regels | Bronnen | Methode |
|------|---------|--------|---------|---------|
| Lokale researchers (Claude) | `final.md` | 453 | 30 (26 verified) | 3 parallelle agents → synthese + verificatiepass |
| Gemini Deep Research (web UI) | `research-gemini-deep-research.md` | 277 | 40+ | Google Gemini agentic deep-research |

## Overlap (beide bronnen behandelen het grondig)

- Definitie convergeert op *gesloten cyclus met terugkoppeling-naar-actie* (Anthropic, OpenAI, NIST, AWS)
- Anatomie evaluation harness: task / trial / grader / transcript / outcome / evaluation suite (Anthropic-taxonomie)
- HELM 7 dimensies: nauwkeurigheid, kalibratie, robuustheid, eerlijkheid, bias, toxiciteit, efficiëntie
- LLM-as-judge biases: positie-, lengte-, zelf-voorkeur, stijl-bias
- Cohen's Kappa 0.7–0.8 als productiestandaard
- EU AI Act Art. 9, 15, 72 als juridisch kader voor evaluation loop
- ISO/IEC 42001 Clause 9 (continue prestatie-evaluatie) en Clause 10 (continue verbetering)
- NIST AI RMF — TEVV als regulier lifecycle-proces
- Hybride grading-aanpak: code-based + LLM-as-judge + menselijk
- Anti-patronen: rapportage-theater, eval-set staleness, judge-contaminatie
- Tooling-landschap: LangSmith, Braintrust, Arize Phoenix, Langfuse

## Wat Gemini Deep Research extra heeft (waardevolle aanvullingen)

### Concrete productie-cases met getallen

- **Nippon India Mutual Fund**: AI-assistent nauwkeurigheid 75% → 90% door overstap van eenvoudige RAG naar continu geëvalueerd systeem; rapport-generatie van 2 dagen naar ~10 min.
- **Huron Health**: 90% nauwkeurigheid sentimentclassificatie via continue evaluatie tegen 10.000 handmatig geannoteerde notities per week.
- **Klarna**: PR-doorlooptijd verdubbeld door geautomatiseerde codekwaliteit- en compliance-hooks in dev-omgeving.

### Specifieke metrieken

- **36% tool-call faalpercentage** in complexe conversaties bij sommige frontier-modellen — "tool routing" als eval-eis.
- Variabiliteit als signaal: agent met 80% slaagkans + occasionele catastrofale fout < 75% maar stabieler systeem.

### Inhoudelijke uitbreidingen

- **"Production-to-eval loop"** als 2026 trend: tools zoals Braintrust zetten productie-traces met één klik om naar regressie-testcases. Vliegwieleffect waarbij systeem slimmer wordt naarmate het meer data verwerkt.
- **"Judge paradox"**: relatief zwak model met zeer gedetailleerde, multidimensionale rubric presteert beter dan superieur model met vage instructie. Kwaliteit van grading volgt structuur van rubric, niet ruwe rekenkracht van beoordelaar.
- **Analytische rubrieken**: elk criterium (feitelijke juistheid, veiligheid, merktoon) afzonderlijk gescoord in plaats van één cijfer — maakt root-cause analyse mogelijk bij kwaliteitsdaling.
- **Schadelijke manipulatie als eval-dimensie**: Google DeepMind 2025 onderzoek; meet "propensity" (neiging) en "efficacy" (effectiviteit) van manipulatie, vooral in zorg en financiën.
- **Pretrained domain knowledge hallucinations** als specifieke stille faalmodus: model vertrouwt op verouderde trainingsdata in plaats van meegeleverde context.
- **Context-drift** in multi-turn agentic conversaties als eval-eis.

### EU AI Act crosswalk uitgebreider

- **Art. 12 (Logging van Gebeurtenissen)**: bewaren van volledige trajecten met timestamps.
- **Art. 13 (Transparantie voor Deployers)**: interpretatierubrieken en uitlegbare redeneerstappen.
- **Art. 14 (Menselijk Toezicht)**: "Interrupt"-mechanismen en menselijke review-wachtrijen.
- Gemini geeft bondige tabel-mapping artikel ↔ vereiste ↔ vertaling-naar-loop.

### Tool-pricing 2026

- Braintrust Pro: vanaf $249/mo (matcht onze final.md)
- LangSmith Plus: vanaf $39/seat/mo (matcht)
- Langfuse Pro: vanaf $29/mo (NIEUW in onze data)
- Arize AX: managed service vanaf $50/mo (NIEUW)

## Wat `final.md` extra heeft (Gemini Deep Research mist)

### Concrete eval-set sizing

- 20-50 cases (eerste testset)
- 100-500 cases (productie-betrouwbaar)
- 1.000+ cases (hoog-risico)
- Samenstelling: 60-70% happy-path / 20-30% edge / 5-10% adversarial

### AntiLeakBench-aanpak

- ICML 2025 paper: 5-15% absolute accuracy drops bij gecontamineerde evals
- ACL 2025 AntiLeakBench: methodologie voor automatische anti-leakage benchmark-constructie
- GSM8K: 13% gedocumenteerde drop

### Inspect AI (UK AISI) als compliance-keuze

- Sandboxed agentic evals via Docker
- Reproduceerbaar en auditeerbaar
- Sterkste OSS-keuze voor compliance-teams die evals als productie-infrastructuur behandelen

### Trajectory metrics specifieker

- TRAJECT-Bench (arxiv 2510.04550): trajectory exact-match, trajectory inclusion
- LangChain AgentEvals: tool selection accuracy, tool parameter accuracy, multi-turn function calling accuracy
- Amazon shopping assistant praktijkles: *slecht gedefinieerde tool-schemas zijn de grootste bron van agentic fouten*

### Nederlandse toezichtsstructuur compleet

- 5 primaire AI Act-toezichthouders: AP, RDI, ACM, AFM, DNB
- Sectoraal: IGJ (zorg), NZa (zorgbekostiging), Inspectie van het Onderwijs
- Implementatiewet AI-verordening verwacht Q4 2026
- AP focus 2025: transparantie, standaardisatie, auditing, governance, non-discriminatie, AI-geletterdheid

### Acht anti-patronen geënumereerd

- Vibe-checking, Demo-driven development, Single-metric tunnel-vision, Eval-set staleness, Judge-model contaminatie, Only happy path, Eval-set leakage, Rapportage-theater
- Goodhart's Law expliciet gekoppeld aan single-metric optimization

### Instance-specifieke rubrieken

- OpenAI HealthBench (2025): per conversatie eigen rubric van 10-40 criteria
- Verschuiving van stijlbeoordeling naar inhoudsmeting

### Zes-fasen productie-loop

- Pre-deploy offline → Shadow mode → Canary release (1% → 5% → 20% → 50% → 100%) → Post-deploy online → Drift monitoring → Verbeteractie
- Drift-taxonomie: data drift / concept drift / performance drift (laatste het gevaarlijkst)

## Conclusie — wat in `final.md` integreren

**Toevoegen aan final.md** (Gemini-uniek, waardevol voor BB):

1. **Productie-cases sectie** met Nippon (75→90%), Huron Health (90% sentiment, 10k notes/wk), Klarna (PR-doorlooptijd) — concrete ROI-getallen voor de "Quick Start" en "AuditExample".
2. **36% tool-call faalpercentage** als argument voor verplichte tool-routing eval.
3. **"Production-to-eval loop"** als 2026 trend in Tools/Platforms-sectie — uitbreiding van anti-pattern *eval-set staleness*.
4. **"Judge paradox"** in LLM-as-judge sectie: rubric-kwaliteit dominant boven judge-model-kracht.
5. **Manipulatie-propensity** als eval-dimensie in HELM 7 → uitbreiden naar 8 dimensies voor 2026.
6. **Pretrained domain knowledge hallucinations** + **context-drift** als stille faalmodi-categorie.
7. **EU AI Act Art. 12, 13, 14** toevoegen aan crosswalk-tabel naast bestaande Art. 9/10/15/17/72.

**Géén integratie nodig** (Gemini-content die in final.md al sterker is uitgewerkt):

- Cohen's Kappa-tabel
- Tooling-overzicht (final.md heeft betere split open-source/SaaS + Inspect AI)
- Bias-categorieën LLM-judge
- Anti-patronen (final.md heeft 8 vs Gemini ~4)

**Conclusie**: Gemini's grootste toegevoegde waarde zit in *concrete productie-cases met getallen*, *2026-trends* (production-to-eval loop, manipulatie-eval), en *complete EU AI Act crosswalk*. Deze drie clusters integreren in `final.md` voordat `/bb-write` start.
