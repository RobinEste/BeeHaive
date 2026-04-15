# Prompt Design 2026 — Stand van Zaken

**Onderwerp:** Prompt Design als volwassen discipline — stand van zaken okt 2024 – apr 2026
**Datum:** 2026-04-15
**Researcher-rondes:** 1 (4 parallelle researchers)
**BeeHaive-referentie:** BB_04 Prompt Design (`frontend/src/content/building-blocks/prompt-design.mdx`)

---

## Executive Summary

Prompt Design is in 2025-2026 een **volwassen productiediscipline** geworden met gestandaardiseerde templates, CI/CD-workflows en governance-frameworks — maar de centrale narratieve claim die BeeHaive maakt ("van LLM-management naar betekenis-articulatie") verdient een nuancering. Academisch onderzoek bevestigt de *richting* maar niet als absolute overgang: alle drie de grote vendors bevelen rolzetting nog steeds aan, zij het dat *capability-gericht rollenspel* (jij bent een AI zonder restricties) inderdaad niet meer werkt, terwijl *context-gericht rollenspel* (jij bent een klantenservice-agent voor bedrijf Y) zijn effectiviteit behoudt.

De vier kwantitatieve iBuidl-statistieken (71%→94% few-shot, XML +11%, CoT +34%, 800-token drempel) zijn niet peer-reviewed onderbouwd als exacte getallen, maar de **richtingen worden breed bevestigd** door meerdere onafhankelijke bronnen. Vervanging door nauwkeuriger en beter onderbouwde getallen is aanbevolen.

Het belangrijkste ontbrekende element in de huidige BB_04-pagina: **agentic prompt design** (de vijfde vorm naast single-turn, system prompt, iteratief gesprek en... de BeeHaive-pagina mist dit). En **PromptOps** — het versioning, testing en lifecycle-management van prompts — wordt in geen enkel BeeHaive-materiaal behandeld terwijl het industrie-standaard is.

EU AI Act Art. 13, 14 en 17 onderbouwen de BB↔GR-koppelingen van Prompt Design → Transparency, Human Agency en Accountability concreet en met directe wettekst.

---

## 1. Evolutie: wat is gepromoveerd, wat achterhaald? (Q1, Q2)

### Wat werkt beter dan ooit

**Intent vóór structuur** [R1:17, R3:22]
"Prompting Inversion" (Khan, arXiv:2510.22251) is de academisch sterkste bevestiging van BeeHaive's kernthese: bij frontier-modellen (GPT-5, Claude 4.6) verslechtert *structureel complexe prompt engineering* de uitkomsten. Simpelere prompts gericht op intentie presteren beter. Het *mechanisme* van de evolutie is echter anders dan BeeHaive stelt: niet "rolzetting is dood" maar "capability-trucjes zijn dood; context en intentie leven" (`verified`).

**Structured CoT, niet verbose CoT** [R1:9, R1:20]
Hi-CoT (arXiv:2604.00130) toont +6.2% accuracy met -13.9% minder tokens door hiërarchische CoT. CoT-Valve (ACL 2025) compresseert CoT van 741 naar 225 tokens zonder meetbaar kwaliteitsverlies. De trend: redeneren intern, niet extern opschrijven (`verified`).

**Native schema-enforcement** [R1:5, R2:2, R3:3]
De verschuiving van "hoop dat het model het format volgt" naar Pydantic/Instructor-validatie op applicatieniveau, gecombineerd met output templates in de system prompt die het format *tonen* in plaats van *beschrijven* (`verified`).

**PromptOps als discipline** [R4:9, R3:10]
Versioning (SemVer), CI/CD-eval-pipelines, A/B-testing van prompt-varianten en geautomatiseerde rollback zijn industrie-standaard bij volwassen teams (`verified`).

### Wat achterhaald of genuanceerd is

**Mega-prompt-manifesto's** [R3:22, R3:15]
400+ regels system prompts creëren interne contradicties en verdunnen signal-to-noise. Moderne modellen zijn getraind op instruction hierarchieën; extra regels helpen niet. "Boring prompts are stable prompts." (`verified`, Rephrase anti-guide)

**Aggressive taal: CAPS en MUST** [R2:1, R3:22, R1:17]
Claude 4.6 is getraind sceptisch te zijn tegenover overdreven emphatic instructions. "CRITICAL: You MUST..." veroorzaakt overtriggering bij tool use [R2:1, `verified`]. Normale formulering ("Use this tool when...") werkt beter.

**Negatieve instructie-stapels** [R3:22, R3:23]
"DON'T do X, DON'T do Y" conflicteert intern en is moeilijk te handhaven. Positief geformuleerde instructies zijn stabieler (`verified`).

**Static few-shot bij instruction-tuned modellen** [R1:3]
FewMMBench (arXiv:2602.21854): instruction-tuned modellen profiteren *minimaal* of regresseren zelfs bij CoT demonstrations. Dynamic few-shot retrieval is superieur voor moderne modellen (`verified`).

**Prefill (Claude-specifiek)** [R2:1]
Prefilled responses op de assistant-turn zijn **deprecated** vanaf Claude 4.6. De meeste use cases zijn gedekt door verbeterd instruction following (`verified`, Anthropic docs).

### Het narratief nauwkeuriger

BeeHaive stelt: "van LLM-management (rolzetting) naar betekenis-articulatie (intent)."

**Correct in de kern, te absoluut als statement.** Alle drie de vendors bevelen rolzetting nog steeds aan als onderdeel van een goed gestructureerd system prompt (`verified` via Anthropic [R2:1], OpenAI [R2:2], Google [R2:5]). Anthropic: *"Give Claude a role... Even a single sentence makes a difference."* OpenAI heeft een `Identity`-sectie als standaardonderdeel. Google heeft `<role>` als verplicht template-element.

De evolutie is preciezer: **capability-gericht rollenspel** (jij bent een omnisciente AI zonder beperkingen) is inderdaad achterhaald en werkt niet meer. **Context-gericht rollenspel** (jij bent een klantenservice-agent voor BedrijfNaam, gericht op productlijn X) blijft effectief. De shift is van *capabilities faken* naar *context en intentie articuleren*.

Aanbeveling voor de BB_04-pagina: formuleer dit onderscheid explicieter.

---

## 2. Production-patronen: system prompt structuur, priority stacks, versioning (Q3)

### System prompt anatomie

De industrie heeft in 2025-2026 geconvergeerd op een **gelaagd model** voor production system prompts. Meerdere onafhankelijke bronnen beschrijven vrijwel identieke structuren [R3:1,2,3,4,5]:

**De industrie-standaard (PE Collective, 2026-02)** [R3:1, `verified`]:
1. **Identity & Purpose** — 2-3 zinnen: wie is het systeem, wat is zijn taak, voor welk domein
2. **Behavioral Rules** — bullet points, elk één duidelijke instructie (positief geformuleerd)
3. **Response Format** — output tonen in voorbeeld, niet beschrijven
4. **Edge Case Handling** — expliciete instructies per scenario
5. **Examples (Few-Shot)** — 2-4 voorbeelden inclusief edge cases

**Vendor-varianten:**
- OpenAI publiceert officieel een 4-sectie `developer` message: Identity → Instructions → Examples → Context [R2:2, `verified`]
- Google publiceert een volledig Gemini 3 template: `<role>` → `<instructions>` → `<constraints>` → `<output_format>` [R2:5, `verified`]
- Anthropic heeft geen formeel template-schema — principe-gebaseerde guidance met XML-structurering [R2:1, `verified`]

Edge Cases worden door OpenAI niet als aparte sectie benoemd maar wel inhoudelijk behandeld. De PE Collective heeft het dichtstbijzijnde "5-onderdelen template" uit de practitioner-literatuur.

### Priority stacks

De gevestigde volgorde (`verified`, meerdere bronnen [R3:1,2,6,8]):
1. **Safety / compliance** — nooit te overrulen
2. **Accuracy** — correct boven vloeiend
3. **Helpfulness**
4. **Efficiency / tone / style**

Formeel gedocumenteerd als *instruction hierarchy*: System ≻ Developer ≻ User ≻ Tool [R3:8, arXiv:2603.10521, `verified`]. Expliciete nummering in de prompt is beter dan een flat lijst — een flat lijst geeft de LLM geen rangordeinfo [R3:9, `verified`].

### PromptOps: versioning, testing, CI/CD

De industrie hanteert een driestaps volwassenheidsmodel [R3:10, `verified`]:

| Niveau | Aanpak |
|--------|--------|
| 0 — Ad-hoc | Prompts als code strings, geen versiebeheer |
| 1 — Git-based | Prompts als YAML/tekstbestanden in Git, PR-workflow met evals |
| 2 — Registry + CI/CD | DB-backed registry, A/B testing, geautomatiseerde rollback |

**SemVer voor prompts** is emerging practice: MAJOR = gedragswijziging die outputs breekt, MINOR = verbetering achterwaarts compatibel, PATCH = kleine fix [R3:13, `verified`].

**Eval-pipeline (drie lagen)**:
1. Deterministische assertions op outputstructuur (valid JSON, vereiste velden)
2. Semantische kwaliteitsmetrieken (LLM-as-judge)
3. Bedrijfsmetrieken (task success rate, user satisfaction)

**Tooling 2026**: LangSmith (meest geciteerd), Langfuse, MLflow Prompt Registry, Braintrust, PromptLayer [R3:11, `verified`].

**Dit ontbreekt volledig in de huidige BB_04-pagina** en is een significante lacune — PromptOps is even belangrijk als het schrijven van de prompt zelf.

---

## 3. Statistieken-verificatie (Q5)

Alle vier de iBuidl-statistieken zijn `unverified` als exacte getallen; de richtingen zijn `verified`.

| Claim (iBuidl) | Status | Beste academische ondersteuning |
|----------------|--------|--------------------------------|
| Few-shot: 71% → 94% (3 voorbeelden) | Richting `verified`, getal `unverified` | arXiv:2602.18776: few-shot CoT 80% vs 29% zero-shot [R3:16]; DOVE (ACL 2025): few-shot reduceert prompt-sensitiviteit [R1:4] |
| XML +11% boven JSON | Richting `verified` (voor Claude), getal `unverified` | Anthropic beveelt XML aan voor prompt-structuur; StructEval [R1:6] toont geen universeel XML-voordeel voor *output*-formatting |
| CoT +34% multi-step | `inferred` — richting klopt | Wei et al. (founding paper): +31-39 pp op GSM8K [R1:8]; Hi-CoT: +6.2% gemiddeld [R1:9]; maar 3% op paraphrase-robuste benchmarks [R1:10] |
| >800 tokens systeem prompt degradatie | `verified` | Field Guide to AI: "200-800 tokens werkt best" [R3:2]; 1,500-token dilution threshold [R3:7]; Levy et al.: degradatie al bij 3k tokens |

**Aanbeveling voor BB_04:** Vervang de iBuidl-statistieken door de range-formulering: "few-shot examples verbeteren structured output compliance substantieel (richting +30-50%)" met verwijzing naar arXiv:2602.18776, en label de iBuidl-getallen als "één meting zonder publieke methodologie."

**Nieuw onderbouwde statistiek**: Few-shot CoT presteert 2.8x hoger dan zero-shot over 281 evaluaties op 71 modellen [arXiv:2602.18776, `verified`].

**Belang van het Prompting Inversion-fenomeen** (R1:17): bij de meest capabele frontier-modellen (GPT-5) verslechtert complexe prompt engineering de uitkomsten. Dit nuanceert álle statistieken: ze zijn model-generatie-afhankelijk.

---

## 4. Model-specifiek vs. model-invariant (Q6)

### Universele principes (werkt bij alle frontier-modellen)

`verified` — bevestigd door alle drie vendors en practitioner-literatuur:

- **Helderheid en directheid** — expliciete instructies, geen ambiguïteit
- **Few-shot voorbeelden** — 2-5 voorbeelden, altijd beter dan zero-shot voor gestructureerde output
- **Context voor de vraag** — lange data/documenten bovenaan, vraag onderaan
- **Output format expliciet specificeren** — tonen in voorbeeld, niet beschrijven
- **Positief formuleren** — wat te doen, niet wat niet te doen
- **Priority stack** — expliciete volgorde, genummerd

### Model-specifieke nuances

`verified` [R2:1,2,5]:

| Aspect | Claude (Anthropic) | GPT-5.x (OpenAI) | Gemini 3 (Google) |
|--------|-------------------|-------------------|-------------------|
| Structureringsmethode | XML-tags primair | XML + Markdown | XML *of* Markdown (kies één) |
| System prompt naam | `system` | `developer` (hernoemd) | System Instruction |
| Reasoning controle | `effort` parameter (low/medium/high/max) | `reasoning_effort` | Automatisch intern |
| Prefill/completion | **Deprecated** vanaf 4.6 | Niet standaard | Completion strategy |
| Instructievolgorde | Identity → XML-tags → long context aan het eind | Identity → Instructions → Examples → Context | Role → Constraints → Context → Task (vraag aan het eind) |
| Tool-triggering | Normale taal, geen CAPS/MUST | Expliciete `<tool_persistence_rules>` blokken | Agentic SI template |
| Rolzetting | Aanbevolen ("Even a single sentence") | Aanbevolen (Identity sectie) | Aanbevolen (`<role>` tag) |

**Kernles voor BeeHaive**: de *kern* van een prompt (wat je wilt, waarom, criteria) is modelonafhankelijk — dit is wat BeeHaive al correct stelt. De *vorm* verschilt per model. XML-tags zijn de Anthropic-specifieke implementatie van "structureer je prompt"; Markdown headers zijn de Google/OpenAI-variant.

---

## 5. Agentic prompt design (Q4) — het ontbrekende element

Dit is de grootste lacune in de huidige BB_04-pagina.

### Fundamenteel andere architectuur

Een chat-prompt is instructie voor één antwoord. Een agent-prompt is instructie voor een **proces** — minuten, uren, tientallen LLM-calls lang met expliciete state management [R4:2, `verified`]:

| Dimensie | Chat/single-turn | Agentic |
|----------|-----------------|---------|
| Levensduur | Één call | Loop: minuten tot uren |
| State | Geen | Expliciete state tracking |
| Foutafhandeling | Niet nodig | Kritisch — fouten propageren |
| Terminatie | Impliciet | Expliciete stopcondities verplicht |
| Kernvraag | "Hoe formuleer ik dit?" | "Wat is de state machine?" |

SitePoint (2026): de shift is van "How do I phrase this prompt?" naar **"What is the decision boundary for invoking each tool?"** — flow engineering als discipline naast prompt engineering [R4:2, `verified`].

### De 6 canonieke agentic patronen

`verified` [R4:2,5,6]:

1. **Prompt Chaining** — sequentiële pipeline, output stap N = input stap N+1
2. **Routing** — classificeer request, dispatch naar gespecialiseerde handler
3. **Parallelization** — splits onafhankelijke taken, of run dezelfde prompt meerdere keren met voting
4. **Orchestrator-Workers** — centraal LLM plant en delegeert aan workers
5. **Evaluator-Optimizer** — generate-critique-refine loop (met expliciete iteratiecap)
6. **ReAct (Reason + Act)** — wisselt reasoning traces af met tool-use actions

### Control flow template

Het aanbevolen beslisframework per stap [R4:7, `verified`]:
```
REASON: Wat weet ik? Wat is de huidige state?
NEXT ACTION: Wat ga ik doen en waarom?
EXPECTED RESULT: Wat zou er moeten gebeuren?
CONTINGENCY: Wat doe ik als dat mislukt?
```

Stopcondities zijn verplicht:
- Taak voltooid → produceer FINAL
- Staplimiet bereikt → produceer PARTIAL + reden
- Onzekerheid over veiligheid → STOP + escaleer naar mens

### Relatie met Evaluation Loop (BB_06) (Q7)

De relatie is cyclisch en bidirectioneel: het prompt-ontwerp bepaalt de observeerbaarheid van agent-gedrag, en evaluatie-uitkomsten sturen prompt-revisies.

**PromptOps lifecycle** (Adaline 2026) [R4:9, `verified`]:
1. Experimentation → 2. Versioning → 3. Testing & evaluation → 4. Controlled deployment → 5. Production monitoring → terug naar 1

Kernprincipe: "When a production prompt fails, that failure becomes a new test case — creating a virtuous cycle where test coverage continuously improves." [R4:10, `verified`]

**BeeHaive BB↔BB koppeling**: Prompt Design ↔ Evaluation Loop is niet optioneel. Je kunt niet goed aan de Prompt Design-knop draaien zonder de Evaluation Loop-knop tegelijk te bedienen.

---

## 6. Guardrail-implicaties (Q8)

### Transparency (EU AI Act Art. 13)

`verified` — artikeltekst direct geverifieerd [R4:13]:

Art. 13(3)(b)(iv) vereist documentatie over "information that is relevant to explain its output" voor high-risk AI. Een system prompt die de systeemuitkomsten fundamenteel bepaalt, valt onder deze documentatieplicht.

**Prompt design → Transparency**: Prompts die Chain-of-Thought of ReAct forcing bevatten, verhogen de intrinsieke uitlegbaarheid van het systeem. Dit is niet alleen een goede gewoonte — het is een compliance-vereiste voor high-risk AI (scope: Annex III categorieën).

**System Prompt Leakage**: OWASP LLM07:2025 identificeert het risico dat te veel informatie in system prompts lekt naar gebruikers [R4:16, `verified`]. Transparant zijn over hét feit dat er een system prompt is ≠ de inhoud ervan publiceren.

### Human Agency (EU AI Act Art. 14)

`verified` — Art. 14(4)(d) en (e) direct geverifieerd [R4:14]:

Art. 14 vereist dat deployers outputs kunnen negeren, overschrijven, corrigeren en het systeem kunnen stoppen.

**Prompt patronen die menselijke controle bevorderen** [R4, `inferred` gebaseerd op Art. 14 mapping]:
- Expliciete escalation triggers: "Als confidence < drempel OF actie heeft onomkeerbare gevolgen → STOP en vraag mens"
- Structured reasoning output (ReAct/CoT): maakt agentic beslissingen auditeerbaar
- Expliciete autonomie-grenzen: "U heeft toestemming voor A, B, C. Voor D en E altijd menselijk goedkeuring vragen."

**Prompt patronen die menselijke controle ondermijnen**:
- "Complete the task autonomously without interruption" zonder stopcondities
- Ontbreken van confidence thresholds
- Geen escalation path

OWASP LLM06:2025 — Excessive Agency: verleen een agent alleen de *minimum* benodigde capaciteiten. Dit is de prompt-design vertaling van het least-privilege principe [R4:16, `verified`].

### Accountability (EU AI Act Art. 17)

`verified` — Art. 17(1)(k) direct geverifieerd [R4, via Hyperproof guide]:

Art. 17 vereist "record-keeping van all relevant documentation" als onderdeel van het Quality Management System. Een production system prompt is "relevant documentation."

**Praktische implicaties** (`inferred` gebaseerd op Art. 17):
1. System prompts moeten versioned zijn (Git of equivalent) met tijdstempel en auteur
2. Wijzigingen aan production prompts vereisen review-proces
3. Ingrijpende prompt-wijzigingen zijn equivalent aan "production changes" — risk assessment nodig
4. Iemand is expliciet eigenaar van elke production system prompt

De ArXiv SoK-paper (2026) formuleert het als technisch advies: **"Record versions and hashes of prompts, policies, and tool manifests for reproducibility and post-incident analysis."** [R4:21, `verified`]

---

## 7. Tegenstrijdigheden en open vragen

**Tegenstrijdigheid 1: Rolzetting**
BeeHaive stelt dat prompt engineering "gepromoveerd" is van rolzetting naar betekenis-articulatie. Alle drie de vendors bevelen rolzetting echter nog steeds aan. De correcte framing: *capability-rolzetting* (trucjes om het model capaciteiten te geven die het niet heeft) is dood; *context-rolzetting* (sturing van domein en gedrag) werkt nog steeds.

**Tegenstrijdigheid 2: Statistieken zijn model-generatie-afhankelijk**
CoT +34% is gebaseerd op PaLM 540B uit 2022. Bij moderne instruction-tuned modellen is het CoT-voordeel veel kleiner (<3% op paraphrase-robuste benchmarks). De statistieken in de BB_04-pagina zijn niet gelabeld met model/datum-context.

**Tegenstrijdigheid 3: XML-formaat**
Anthropic beveelt XML aan voor *prompt-structuur*. Academisch onderzoek (StructEval, R1:6) toont dat XML voor *output-formatting* juist een van de moeilijkere formaten is. De "+11% XML"-claim van iBuidl is waarschijnlijk Claude-specifiek en outputformaat-specifiek — niet universeel.

**Open vraag 1:** Prompting Inversion is gebaseerd op GPT-5 (grens-case); in welke mate geldt het ook voor Claude 4.6 en Gemini 3? Geen directe meting gevonden.

**Open vraag 2:** Zijn PromptOps-tools (LangSmith, Langfuse etc.) EU AI Act-compliant voor high-risk use cases? Log-bewaring, data residency en toegangscontrole zijn niet systematisch onderzocht.

**Open vraag 3:** Hoe schaalt de Evaluation Loop ↔ Prompt Design cyclus bij agentic systems? Evaluatie van loops is fundamenteel anders dan evaluatie van single-turn outputs.

---

## 8. Aanbevelingen voor de BB_04-pagina

Op basis van alle research:

### Aanpassen
- [ ] **Narratief nuanceren**: "Van LLM-management naar betekenis-articulatie" → "Van capability-rolzetting naar context-articulatie en intentie" (onderscheid capability vs. context rolzetting)
- [ ] **Statistieken herlabelen**: Alle vier iBuidl-getallen als "indicatief, iBuidl-intern" labelen; vervang door betere onderbouwde ranges
- [ ] **Model-specifiek onderscheid**: XML als Anthropic-specifieke best practice expliciteren, niet als universele aanbeveling; Google/OpenAI gebruiken XML óf Markdown

### Toevoegen
- [ ] **5e vorm: Agentic prompt design** — ontwerp voor loops, state machines en control flow; ReAct patroon; 6 canonieke agentic patronen; stop conditions als verplicht element
- [ ] **PromptOps sectie**: versioning (SemVer voor prompts), testing (3-laags eval pipeline), CI/CD gates, tooling-landschap
- [ ] **Priority stack**: expliciete sectie over het vormgeven van prioriteiten in system prompts (Safety > Accuracy > Helpfulness > Efficiency)
- [ ] **5-secties template** als praktisch kader voor system prompts (Identity/Rules/Format/Edge Cases/Examples)
- [ ] **BB↔GR-koppeling**: Prompt Design → Transparency (Art. 13), Human Agency (Art. 14), Accountability (Art. 17) met concrete EU AI Act-referenties

### Behouden (bevestigd)
- ✅ "De kern is overdraagbaar, de vorm niet" — breed bevestigd
- ✅ Vier vormen (single-turn, system prompt, iteratief gesprek, agent prompts) — correct, maar "agent prompts" verdient significante uitbreiding
- ✅ Betekenis als kern van prompt design — correct als nuancering van capability-rolzetting, niet als vervanging van alle rolzetting
- ✅ Iteratief gesprek als waardekern — bevestigd; PromptOps lifecycle is de institutionalisering hiervan

---

## Sources

Alle bronnen geraadpleegd op 2026-04-15.

### Academisch / peer-reviewed

- [Wei et al., Chain-of-Thought Prompting, arXiv:2201.11903 (NeurIPS 2022)](https://arxiv.org/pdf/2201.11903v4) — founding CoT-paper; +31-39 pp op GSM8K
- [Schulhoff et al., The Prompt Report, arXiv:2406.06608 (v6 Feb 2025)](https://arxiv.org/abs/2406.06608) — 58 prompting-technieken; meest complete taxonomie
- [Sahoo et al., Survey Prompt Engineering, arXiv:2402.07927 (v2 Mar 2025)](https://arxiv.org/abs/2402.07927) — survey per applicatiegebied
- [Khan, Prompting Inversion, arXiv:2510.22251 (Oct 2025)](https://arxiv.org/abs/2510.22251) — complexe prompts averechts bij frontier models
- [Romanou et al., BrittleBench, arXiv:2603.13285 (Feb 2026)](https://arxiv.org/pdf/2603.13285) — few-shot vergroot brittleness bij perturbaties
- [Dogan et al., FewMMBench, arXiv:2602.21854 (Feb 2026)](https://arxiv.org/abs/2602.21854) — instruction-tuned modellen profiteren minimaal van few-shot
- [Habba et al., DOVE, ACL Findings 2025](https://aclanthology.org/2025.findings-acl.611/) — few-shot reduceert prompt-sensitiviteit
- [StructEval, arXiv:2505.20139 (2025)](https://arxiv.org/html/2505.20139) — benchmark structured output formats; XML niet universeel beter
- [Jaroslawicz et al., IFScale, arXiv:2507.11538 (Jul 2025)](https://arxiv.org/pdf/2507.11538) — instruction-following daalt bij 500 instructies
- [Robinette et al., VerIFY, EACL Findings 2026](https://aclanthology.org/2026.findings-eacl.254/) — langere context daagt instruction adherence uit
- [Hi-CoT, arXiv:2604.00130 (Apr 2026)](https://www.arxiv.org/pdf/2604.00130) — +6.2% accuracy, -13.9% tokens
- [Yin et al., CoT-Valve, ACL 2025](https://aclanthology.org/2025.acl-long.300.pdf) — CoT-lengte comprimeerbaar
- [MME-CoT, ICML 2025](https://icml.cc/virtual/2025/poster/44904) — CoT verslechtert perception-heavy taken
- [arXiv:2602.18776 (Feb 2026)](https://arxiv.org/pdf/2602.18776) — few-shot CoT 2.8x hoger dan zero-shot; structured output 34% vs 7%
- [Instruction Hierarchy, arXiv:2603.10521 (2026)](https://arxiv.org/pdf/2603.10521) — System ≻ Developer ≻ User ≻ Tool formeel gedocumenteerd
- [ArXiv SoK Agentic AI Security, arXiv:2603.22928 (2026)](https://www.arxiv.org/pdf/2603.22928) — "Record versions and hashes of prompts for reproducibility"

### Officiële vendor documentatie

- [Anthropic Prompting Best Practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices) — XML-structurering, prefill deprecated, rol aanbevolen (`verified`)
- [OpenAI Prompt Engineering](https://developers.openai.com/api/docs/guides/prompt-engineering) — 4-sectie template (`verified`)
- [OpenAI Prompt Guidance GPT-5.4](https://developers.openai.com/api/docs/guides/prompt-guidance) — XML blokken als prompt componenten (`verified`)
- [Google Gemini Prompt Design Strategies](https://ai.google.dev/gemini-api/docs/prompting-strategies) — Gemini 3 template; few-shot altijd aanbevolen (`verified`, updated 2026-04-09)

### EU / Governance primaire bronnen

- [EU AI Act Art. 13 — Transparency](https://artificialintelligenceact.eu/article/13/) — documentatieplicht system outputs voor high-risk AI (`verified`)
- [EU AI Act Art. 14 — Human Oversight](https://www.euaiact.com/article/14) — override/stop capability (`verified`)
- [OWASP LLM Top 10 2025](https://genai.owasp.org/llm-top-10/) — LLM01 Prompt Injection, LLM06 Excessive Agency, LLM07 System Prompt Leakage (`verified`)
- [OWASP Agentic AI Threats & Mitigations (2025)](https://www.aigl.blog/content/files/2025/04/Agentic-AI---Threats-and-Mitigations.pdf) — Goal manipulation, dynamic intervention thresholds (`verified`)
- [NIST AI RMF Playbook](https://www.nist.gov/itl/ai-risk-management-framework/nist-ai-rmf-playbook) — GOVERN/MAP/MEASURE/MANAGE (`verified`)

### Industry / Practitioners

- [PE Collective — System Prompt Design Guide (2026-02)](https://pecollective.com/blog/system-prompt-design-guide/) — 5-secties template (`verified`)
- [Field Guide to AI — System Prompt Design (2026-02)](https://fieldguidetoai.com/guides/system-prompt-design) — 6-laags template met priority_order (`verified`)
- [AgentWiki — How to Structure System Prompts (2026-03)](https://agentwiki.org/how_to_structure_system_prompts) — 7-componenten voor production agents (`verified`)
- [Rephrase — Anti-Prompting Guide (2026-03)](https://rephrase-it.com/blog/the-anti-prompting-guide-12-prompt-patterns-that-used-to-wor) — 12 anti-patronen (`verified`)
- [number6.ai — System Prompts That Work (2025-10)](https://number6.ai/blog/43-system-prompts-that-work/) — identity card + constitution uit echte deployments (`verified`)
- [Tianpan.co — Prompt Versioning in Production (2026-04)](https://tianpan.co/blog/2026-04-09-prompt-versioning-production-llm) — Git→DB→Registry evolutie; immutabiliteit (`verified`)
- [PromptBuilder — Prompt Testing CI/CD (2025-12)](https://promptbuilder.cc/blog/prompt-testing-versioning-ci-cd-2025) — SemVer voor prompts, CI/CD (`verified`)
- [Adaline — Complete Guide PromptOps 2026](https://www.adaline.ai/blog/complete-guide-prompt-engineering-operations-promptops-2026) — PromptOps lifecycle (`verified`)
- [Paxrel — 10 Patterns Agent Prompts 2026](https://paxrel.com/blog-ai-agent-prompts) — 10 production-ready patterns (`verified`)
- [SitePoint — Definitive Guide Agentic Patterns 2026](https://www.sitepoint.com/the-definitive-guide-to-agentic-design-patterns-in-2026/) — 6 canonieke patterns, flow engineering (`verified`)
- [Nibzard — Agentic AI Handbook (2026)](https://nibzard.com/agentic-handbook) — 4 foundational agentic patronen (`verified`)
- [Rephrase — Decision-Making Prompts for Agents (2026)](https://rephrase-it.com/blog/decision-making-prompts-for-ai-agents) — control flow template (`verified`)
- [Braintrust — Prompt Optimization Loop](https://www.braintrust.dev/articles/prompt-optimization-loop) — 5-stap evaluatiecyclus (`verified`)

### Kerncitaten

- Khan (2025): *"Optimal prompting strategies must co-evolve with model capabilities, suggesting simpler prompts for more capable models."* — arXiv:2510.22251
- Rephrase (2026): *"Boring prompts are stable prompts."*
- SitePoint (2026): *"The shift is from 'How do I phrase this prompt?' to 'What is the state machine governing this agent's behavior?'"*
- Braintrust (2026): *"The teams that build reliable prompts don't write better first drafts. They run more cycles."*
- ArXiv SoK (2026): *"Record versions and hashes of prompts, policies, and tool manifests for reproducibility and post-incident analysis."*
