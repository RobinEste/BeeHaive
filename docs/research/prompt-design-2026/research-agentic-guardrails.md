# Research: Agentic Prompt Design + Guardrails — Prompt Design 2026

**Researcher:** researcher-4
**Dimensie:** Agentic prompt design + EU AI Act / guardrail-implicaties
**Datum:** 2026-04-15

## Samenvatting (1 zin)

Agentic prompt design vereist een fundamenteel andere architectuur dan chat-prompts — expliciete control flow, terminatiecondities en foutafhandeling — terwijl de EU AI Act (Art. 13, 14, 17, 19) en frameworks als OWASP LLM 2025, NIST AI RMF en ISO 42001 gezamenlijk eisen dat production system prompts auditeerbaar, versioned en met human oversight mechanismen zijn ontworpen.

---

## Bevindingen — Deel A: Agentic Prompt Design

### Hoe verschilt agentic van chat/single-turn prompt design? (Q4a)

`verified`

Een chat-prompt is instructie voor één antwoord; een agent-prompt is instructie voor een **proces** — minuten, uren of tientallen LLM-calls lang. De fundamentele architectuurverschillen [1][2][3]:

| Dimensie | Chat/single-turn | Agentic |
|---|---|---|
| Levensduur | Één call | Meerdere calls, long-running loops |
| State | Geen | Expliciete state tracking vereist |
| Foutafhandeling | Niet nodig | Kritisch — fouten propageren |
| Terminatie | Impliciet na respons | Expliciete stopcondities vereist |
| Tool-gebruik | Optioneel | Centraal design-concern |
| Instructie-stabiliteit | Eén keer gelezen | Drift over iteraties; prompt rot |

Paxrel (2026) formuleert het zo: "A chatbot prompt runs once. An agent prompt runs for minutes, hours, or days across dozens of LLM calls. The system prompt needs to be a durable set of instructions that guides behavior across this full loop, not just the first step." [3]

SitePoint (2026) noemt de kernverschuiving: van "How do I phrase this prompt?" naar "What is the state machine governing this agent's behavior?" en "What is the decision boundary for invoking each tool?" [2] Dit is wat ze "flow engineering" noemen: de discipline van het ontwerpen van control flow, state transitions en decision boundaries *rondom* LLM-calls, niet het optimaliseren van de calls zelf.

### Patronen: beslisbomen, determinisme, refuse, error-handling (Q4b)

`verified`

**De zes canonieke agentic design patterns** (gedocumenteerd door SitePoint 2026, Tianpan.co 2026, en Nibzard 2026) [2][4][5]:

1. **Prompt Chaining** — sequentiële pipeline van LLM-calls; output van stap N is input van stap N+1. Geschikt voor gedefinieerde, volgordelijke subtaken.
2. **Routing** — classificeer binnenkomende request en dispatch naar gespecialiseerde handler. Vermijdt monolithische system prompts.
3. **Parallelization** — splits onafhankelijke subtaken; of run dezelfde prompt meerdere keren met voting voor hogere betrouwbaarheid.
4. **Orchestrator-Workers** — centraal LLM plant en delegeert dynamisch aan worker-agents. Geschikt voor open-ended taken.
5. **Evaluator-Optimizer** (Reflection) — generate-critique-refine loop. Vergt expliciete iteratiecap of kwaliteitsdrempel om infinite loops te vermijden.
6. **ReAct (Reason + Act)** — wisselt reasoning traces af met tool-use actions. Standaard patroon voor multi-step informatieverzameling. [6]

**Beslisbomen en deterministische vs probabilistische beslissingen:**

Rephrase.it (2026) introduceert de key-pattern voor agentic decision logic [7]:
- **Stop conditions** zijn expliciete regels (task completion criteria, resource/cost limieten, confidence drempels)
- **Constraint framing** definieert wat een agent *niet* mag, niet alleen wat het moet
- **Confidence thresholds** forceren expliciete self-assessment vóór actie

Het ReAct-patroon als decision structure [7]:
```
Before every action, output:
REASON: What do I know? What is the current state?
NEXT ACTION: What am I about to do and why?
EXPECTED RESULT: What should happen?
CONTINGENCY: What will I do if that fails?
```
Dit maakt beslissingen auditeerbaar en reduceert hallucinations door het forceren van assumption-checking vóór commitment.

**Error-handling en refuse-behavior:**

Nibzard (2026) en Rephrase.it (2026) beschrijven het Plan-Controlled-Execute patroon [5][7]:
- **Plan phase**: stel goals, stappen, verwachte tools, constraints en "done"-checks op
- **Controlled execution**: voer één stap tegelijk uit, observeer, beslis: stop / continue / escalate
- **Refuse-trigger**: als goal niet haalbaar binnen constraints → escalate naar human

Expliciete control flow template (Rephrase.it 2026) [7]:
```
SYSTEM: You are {AgentName}. Your job is to complete the task using tools safely.
CONTROL FLOW (must follow):
1) Understand: restate the goal in 1 sentence.
2) Plan: propose up to 5 steps. Name tools if needed.
3) Execute: perform one step at a time.
4) After each tool result, update STATE object.
5) Stop conditions:
   - If goal is satisfied → produce FINAL
   - If step limit reached → produce PARTIAL + reason
   - If uncertain about safety → STOP + ask human
```

**Anti-patronen (empirisch vastgesteld):** Een March 2025 analyse van 150+ multi-agent execution traces identificeerde 14 failure modes in drie categorieën: specification/system design failures, inter-agent misalignment failures, en task verification failures. Kernconclusie: de meeste failures komen van inter-agent interactie, niet van individuele model capability. Prompt engineering fixes verbeterden dit slechts ~14%. [4]

### Agentic system prompt templates (Q4c)

`verified`

**Paxrel's 10-patroon framework** voor agentic system prompts (2026) [3]:

| # | Pattern | Core idea | Complexiteit |
|---|---|---|---|
| 1 | Role + Constraints | Define wie de agent IS en wat het niet mag | Laag |
| 2 | Chain of Verification | Agent checkt output tegen checklist | Laag |
| 3 | Structured Output Enforcement | Expliciete JSON schema, geen deviaties | Laag |
| 4 | Tool Selection Heuristics | Wanneer welke tool te gebruiken | Medium |
| 5 | Error Recovery Instructions | Wat te doen bij mislukte tool calls | Medium |
| 6 | Guard Rails | Hard stops voor buiten-scope requests | Medium |
| 7 | Context Window Management | Wat in/uit context te houden | Medium |
| 8 | Progressive Disclosure | Fase-gated instructies, detail on demand | Medium |
| 9 | Memory Integration | Expliciete read/write regels voor persistent files | Medium |
| 10 | Self-Evaluation Loop | Agent scoort eigen output, herschrijft bij < drempel | Hoog |

Production agent prompts combineren typisch 4-7 van deze patterns. Structuur: Role+Constraints en GuardRails vormen de outer frame (altijd aanwezig, altijd bovenaan). Tool Selection en Error Recovery zijn de operationele middenlaag. Progressive Disclosure, Structured Output en Chain of Verification sturen de uitvoering. Self-Evaluation is de finale kwaliteitsgate.

**Nibzard's vier "immediately usable" patronen** (2026) [5]:
1. **Plan-Then-Execute** — scheidt planning van uitvoering; beschermt tegen prompt injection door user content pas in execution-phase te verwerken
2. **Inversion of Control** — de harness controleert wat de agent ziet en doet, niet de agent zelf
3. **Reflection Loop met objectieve checks** — geen "vibes-based" self-critique maar anchored aan tests, lints, schema validation
4. **Action Trace Monitoring** — elke actie gelogd met REASON, ACTION, EXPECTED_RESULT zodat drift detecteerbaar is

**Dynamic instruction retrieval** als emerging pattern: in plaats van één monolithische system prompt worden per stap minimale instructie-fragmenten opgehaald (Instruction-Tool Retrieval / ITR). Rephrase.it (2026) rapporteert dat dit "attention dilution" en derailment-kans significant reduceert bij long-running agents. [8]

### Relatie Prompt Design ↔ Evaluation Loop (Q7)

`verified`

De relatie is cyclisch en bidirectioneel: het prompt-ontwerp bepaalt de observeerbaarheid van agent-gedrag, en evaluatie-uitkomsten sturen prompt-revisies.

**De PromptOps lifecycle** (Adaline 2026) definieert vijf fases [9]:
1. Experimentation (playground)
2. Versioning & tracking
3. Testing & evaluation
4. Controlled deployment
5. Production monitoring → terug naar fase 1

Kritisch principe: "When a production prompt fails, that failure becomes a new test case — creating a virtuous cycle where test coverage continuously improves." [9]

**Evaluatie-cyclus in practice** (Braintrust 2026) [10]:
1. Schrijf prompt
2. Score tegen real data (automated + human)
3. Identificeer failure patterns
4. Maak gerichte aanpassing
5. Re-evalueer — check ook voor regressions in eerder werkende cases
6. Deploy met CI/CD-gate (kwaliteitsdrempel)

Braintrust stelt: "The teams that build reliable prompts don't write better first drafts. They run more cycles." [10]

**Feedback loop structuur** (Travis Kroon / PromptOT 2026) [11][12]:
- **Capture**: log prompt versie, inputs, outputs, metadata, eval scores
- **Label**: categoriseer failures (tone, format, hallucination, tool error)
- **Analyse**: correleer scores met output-types, spot regressions per prompt versie
- **Refactor**: A/B test vóór productie; test op curated dataset
- **Re-evaluate**: monitor post-deploy gedrag

**Relatie tot BeeHaive BB_06 (Evaluation Loop):** Het evalueren van agent-prompts *is* een implementatie van de Evaluation Loop bouwsteen. De evaluatiecriteria voor agentic prompts zijn deels kwantitatief (task completion rate, tool call count, iterations to completion) en deels kwalitatief (was de reasoning coherent, waren escalation decisions correct). De feedback wordt terug-gerouteerd naar de prompt via versioned updates — dit is exact de "evaluate → update → deploy" cycle van BB_06.

---

## Bevindingen — Deel B: Guardrails / EU AI Act

### EU AI Act — relevante artikelen voor prompt design (Q8a)

`verified` — artikelteksten direct geverifieerd via artificialintelligenceact.eu en euaiact.com

De EU AI Act (Regulation (EU) 2024/1689) bevat geen expliciete verwijzing naar "system prompts" of "prompt design". De wet reguleert AI-*systemen* en hun providers/deployers, waarbij de system prompt als onderdeel van het systeem valt onder de volgende artikelen:

**Art. 13 — Transparency and Provision of Information to Deployers** (treedt in werking 2 augustus 2026):
> "High-risk AI systems shall be designed and developed in such a way as to ensure that their operation is sufficiently transparent to enable deployers to interpret a system's output and use it appropriately."

Art. 13(3)(b)(iv) vereist documentatie van "the technical capabilities and characteristics of the high-risk AI system to provide information that is relevant to explain its output." Een system prompt die de systeemuitkomsten fundamenteel bepaalt, valt onder deze documantatieplicht.

Art. 13(3)(f): "where relevant, a description of the mechanisms included within the high-risk AI system that allows deployers to properly collect, store and interpret the logs."

**Art. 14 — Human Oversight** (Art. 14(4)):
Vereist dat deployers in staat worden gesteld om:
- (a) capaciteiten en beperkingen te begrijpen en anomalieën te detecteren
- (b) automation bias te herkennen
- (c) outputs correct te interpreteren
- **(d) te besluiten de output te negeren, te overschrijven of te corrigeren**
- (e) het systeem te onderbreken via een 'stop button' of gelijkwaardige procedure

Implicatie voor prompt design: een system prompt die geen escalatie-mechanisme naar humans biedt, of die de human oversight capacity ondermijnt (bijv. door te instrueren altijd autonoom door te gaan), is potentieel non-compliant voor high-risk AI.

**Art. 17 — Quality Management System:**
Vereist een gedocumenteerd QMS inclusief:
- (a) strategie voor regulatory compliance
- (k) "systems and procedures for record-keeping of all relevant documentation and information"
- (m) "an accountability framework setting out the responsibilities of the management and other staff"

Een production system prompt is "relevant documentation" in de zin van Art. 17(1)(k). Versioning en review trails zijn daarmee een impliciete eis.

**Art. 19 — Automatically Generated Logs:**
Deployers van high-risk AI moeten automatisch gegenereerde logs minimaal 6 maanden bewaren (Art. 19 jo. Art. 26(5)-(6)). Dit raakt prompt design: prompts die gestructureerde STATE-output genereren per stap (zoals in de ReAct pattern) maken log-bewaring aanzienlijk effectiever.

**Art. 50 — Transparency Obligations for Certain AI Systems** (geldt ook voor niet-high-risk, maar conversational AI):
> Providers must ensure that natural persons interacting with AI systems are informed they are communicating with an AI.

Dit is primair van toepassing op chatbots en real-time synthesized content, niet rechtstreeks op system prompt governance.

**Scope-caveat**: Art. 13, 14, 17 zijn alleen van toepassing op **high-risk AI systems** (Annex III categorieën: biometrics, critical infrastructure, onderwijs, werk, essentiële services, rechtshandhaving, migratie, rechtsbedeling, democratie). Voor de meeste BeeHaive-use-cases (kennisframework, trainingen) is dit niet automatisch high-risk. Voor gebruik in HR, juridisch of gezondheidszorg-context wél. [13][14]

### Transparency-verplichtingen (Q8b)

`inferred` + `verified` (art. tekst geverifieerd, mapping naar prompts is inference)

Art. 13 eist "sufficiently transparent" operatie van het systeem voor deployers. Dit impliceert:

1. **System prompt moet documenteerbaar zijn**: Als de system prompt het systeemgedrag fundamenteel bepaalt, en het systeem high-risk is, moet de werking van die prompt aantoonbaar zijn voor deployers (Art. 13(2): "instructions for use in an appropriate digital format...that include concise, complete, correct and clear information").

2. **Prompt-logging bij high-risk**: Art. 12 (Record-Keeping) eist dat high-risk systemen automatisch logs genereren die traceability mogelijk maken. Art. 19 stelt minimale bewaartermijn op 6 maanden. Een system prompt die machine-leesbare STATE-updates genereert per stap maakt dit technisch haalbaar.

3. **Uitlegbaarheid van outputs**: Art. 13(3)(b)(iv) — "information that is relevant to explain its output." Dit is relevant voor agentic systems waarbij de system prompt de redeneerrouties bepaalt. Een prompt die Chain-of-Thought of ReAct reasoning forceert, verhoogt de intrinsieke uitlegbaarheid.

Applied AI Best Practices rapport (2025) verbindt Art. 13 en ISO/IEC 6254 (explainability): "The less technically adept the user, the more effort is required to fulfil the transparency obligations." [15]

**Geen expliciete eis tot openbaar maken van system prompts**: Art. 13 eist documentatie naar deployers, niet openbaarmaking naar het publiek. OWASP LLM07:2025 (System Prompt Leakage) identificeert overigens het omgekeerde risico: system prompts die te veel blootgeven vormen een veiligheidsrisico. [16]

### Human Agency — prompt-patronen die menselijke controle bevorderen (Q8c)

`verified` (Art. 14 geverifieerd; patronen als `inferred` gebaseerd op mapping)

**Art. 14(4)(d) en (e)** vereisen technisch dat humans outputs kunnen overschrijven en het systeem kunnen stoppen. Dit vertaalt naar concrete prompt-design vereisten:

**Patronen die menselijke controle BEVORDEREN:**
- **Expliciete escalation triggers**: "If confidence < threshold OR action has irreversible consequences → STOP and ask human" (Art. 14(4)(d) compliant)
- **Structured reasoning output**: ReAct/Chain-of-Thought maakt agentic beslissingen auditeerbaar, wat automaton-bias-herkenning door humans ondersteunt (Art. 14(4)(b))
- **Expliciete autonomie-grenzen**: "U hebt toestemming voor A, B en C. Voor D en E altijd menselijk goedkeuring vragen." Dit limiteert excessive agency.
- **Step-level STATE-output**: "Na elke stap, output een STATE JSON" maakt drift door humans detecteerbaar
- **Inversion of Control**: de harness (niet de agent) beslist wat de agent mag zien/doen; de prompt beschrijft wat de harness van de agent verwacht

**Patronen die menselijke controle ONDERMIJNEN:**
- Instructies als "complete the task autonomously without interruption" zonder stopcondities
- Ontbreken van confidence thresholds → agent gaat door ook bij lage zekerheid
- Geen escalation path → agent probeert onmogelijke taken af te ronden in plaats van te escaleren
- Monolithische system prompts zonder opties voor harness-niveau controls

OWASP LLM06:2025 — **Excessive Agency**: "An LLM-based system is often granted a degree of agency by its developer – the ability to call functions... An LLM-based system should be granted only the minimum level of functionality required." Dit is de prompt-design vertaling van Art. 14: het least-privilege principe voor agent capabilities. [16]

Het OWASP Agentic Threats document (2025) introduceert "dynamic intervention thresholds" — het idee dat de mate van human oversight *variabel* kan zijn op basis van risico, confidence en context. Dit sluit aan bij Art. 14(3): "oversight measures shall be commensurate with the risks, level of autonomy and context of use." [17]

### Accountability — governance voor production prompts (Q8d)

`verified` (Art. 17 geverifieerd; governance-implicaties deels `inferred`)

**Art. 17 Quality Management System** is het meest directe accountability-kader voor production system prompts. Het vereist:
- Gedocumenteerde policies, procedures en instructies
- Record-keeping systemen voor "all relevant documentation and information" (Art. 17(1)(k))
- Accountability framework voor management en staff (Art. 17(1)(m))

**Art. 25 — Responsibilities Along the AI Value Chain** (niet rechtstreeks geciteerd maar `inferred` relevant): als een deployer een system prompt schrijft op een foundation model van een provider, draagt de deployer verantwoordelijkheid voor de instructies die ze aan het systeem geven. De provider draagt verantwoordelijkheid voor de model-capabilities; de deployer voor hoe die capabilities worden aangestuurd.

**Praktische governance-implicaties voor production system prompts** (inferred, ondersteund door Art. 17 + appliedAI.de best practices rapport) [15]:
1. **Versioning**: system prompts moeten versied zijn (git of equivalent) met tijdstempel en auteur
2. **Review trails**: wijzigingen aan production prompts vereisen review-proces (vergelijkbaar met code review)
3. **Change risk assessment**: ingrijpende prompt-wijzigingen zijn equivalent aan "production changes" — require risk assessment
4. **Rollback capability**: als een prompt-wijziging ongewenste uitkomsten geeft, moet rollback mogelijk zijn
5. **Verantwoordelijke eigenaar**: iemand is expliciet eigenaar van elke production system prompt

Adaline's PromptOps guide (2026) beschrijft dit als "PromptOps": "Ad-hoc prompt management doesn't scale — it creates coordination chaos, deployment risks, and compliance gaps." [9] Dit is de operationalisering van Art. 17(1)(k).

**Hyperproof EU AI Act Guide (2026)** stelt expliciet: "Maintaining technical documentation (Article 11), risk-management plans, and contributing to the EU-wide database for high-risk systems under Article 71. These pillars form the foundation of AI governance, ensuring compliance, ethical use, and ongoing accountability." [14]

### NIST AI RMF / ISO 42001 / OWASP LLM (Q9)

`verified`

**NIST AI RMF (AI 100-1, januari 2023; 2025 updates)**

Het NIST AI RMF gebruikt vier functies: Govern, Map, Measure, Manage. Geen expliciete verwijzing naar "system prompts" in de kerntekst, maar:

- **GOVERN** — "Establish the policies, culture, accountability structures, and processes." GOVERN 1.1: "Legal and regulatory requirements involving AI are understood, managed, and documented." De system prompt als instructie-mechanisme valt onder de accountability-structuren die GOVERN vereist. [18]
- **MEASURE** — Continueus monitoren van AI-systeem performance. Dit impliceert dat prompt-wijzigingen als "production changes" worden behandeld met voor- en na-metingen.
- March 2025 NIST update (NIST AI 100-2e2025) breidt uit naar generative AI en LLM-specifieke dreigingen, inclusief prompt injection als bedreigingscategorie. [18]

NIST AI RMF bevat een crosswalk naar ISO 42001, wat beide frameworks verbindt.

**ISO/IEC 42001:2023 — AI Management System Standard**

De eerste wereldwijde AI management system standaard (december 2023). Gebruikt Plan-Do-Check-Act methodologie. Annex A bevat 42 control objectives in 9 topics. Specifiek relevant voor prompt design:
- **A.2.1** (Scoping): definieer doel en vereisten van AI systeem — inclusief instructiestructuur
- **A.7.3** (AI system monitoring): continueus monitoren van performance — inclusief prompt-effectiviteit
- **Risico-assessment** (section 6): StackAware's ISO 42001 risk assessment identificeerde prompt injection als specifieke kwetsbaarheid [19]

ISO 42001 biedt geen specifieke normen voor prompt design, maar de AIMS-structuur impliceert dat production system prompts onderdeel zijn van het gedocumenteerde AI system lifecycle management. ISO 42001 en EU AI Act zijn complementair: ISO 42001 versnelt EU AI Act compliance. [20]

**OWASP LLM Top 10 2025** — meest directe governance-bron voor prompt design als risicovector:

| OWASP Item | Relevantie voor prompt design |
|---|---|
| **LLM01:2025 Prompt Injection** | System prompt moet input/output filtering instrueren; least-privilege scope; adversarial testing instructies | `verified` [16] |
| **LLM06:2025 Excessive Agency** | Prompt moet expliciet de scope van agent-acties limiteren; minimize permissions in de instructie | `verified` [16] |
| **LLM07:2025 System Prompt Leakage** | System prompt bevat potentieel gevoelige instructies; niet injecteren via user-zijde; expliciet niet reproduceren | `verified` [16] |

OWASP LLM01:2025 mitigatie-strategieën die direct als prompt design guidelines gelden [16]:
1. "Provide specific instructions about the model's role, capabilities, and limitations within the system prompt" (constraint framing)
2. "Enforce strict adherence to the system prompt" (persistent instructions over user override)
3. Implement input/output filtering (harness-niveau, niet prompt-niveau)
4. Enforce privilege control (least-privilege agency)

**OWASP Agentic AI Threats & Mitigations (2025)** is een afzonderlijk document specifiek voor agentic systemen [17]:
- Identificeert **Goal Manipulation** (gradual plan injection) als agentic-specifieke bedreiging: aanvallers modificeren incrementeel het planning framework van een agent over tijd
- Mitigatie: "Split work into plan, controlled execution, and replan gates" (Plan-Then-Execute patroon)
- "Develop advanced human-AI interaction frameworks and adaptive trust mechanisms" — dynamic intervention thresholds

**ArXiv SoK paper (2026)**: systematische survey van agentic LLM security introduceert specifieke governance aanbeveling: "Treat prompt/policy updates and new capabilities as production changes: perform risk assessments, update CBAC/sandbox scopes, roll out with feature flags/canaries, and monitor for regressions in security metrics. **Record versions and hashes of prompts, policies, and tool manifests** for reproducibility and post-incident analysis." [21]

---

## Evidence Table

| # | Bron | URL | Type | Key claim | Confidence |
|---|---|---|---|---|---|
| 1 | Bits-Bytes-NN: Evolution of Agentic Patterns | https://bits-bytes-nn.github.io/insights/agentic-ai/2026/04/05/evolution-of-ai-agentic-patterns-en.html | Practitioner artikel | Paradigma-shift 2022→2026: prompt → context → harness engineering | Medium |
| 2 | SitePoint: Definitive Guide Agentic Design Patterns 2026 | https://www.sitepoint.com/the-definitive-guide-to-agentic-design-patterns-in-2026/ | Practitioner gids | 6 canonieke patterns, flow engineering vs prompt engineering | Hoog |
| 3 | Paxrel: 10 Patterns Agent Prompts 2026 | https://paxrel.com/blog-ai-agent-prompts | Practitioner gids | 10 production-ready prompt patterns met templates | Hoog |
| 4 | Tianpan.co: Agentic Engineering Patterns | https://tianpan.co/blog/2026-02-05-agentic-engineering-patterns-while-loop-easy-part | Practitioner artikel | 150+ trace analyse; meeste failures = inter-agent, niet model | Medium |
| 5 | Nibzard: Agentic AI Handbook | https://nibzard.com/agentic-handbook | Practitioner gids | 8 categorieën agentic patterns; 4 foundational patronen | Hoog |
| 6 | MD Sanwar Hossain: Agentic Design Patterns 2026 | https://mdsanwarhossain.me/blog-agentic-ai-design-patterns.html | Practitioner artikel | ReAct, CoT, ToT, Reflexion, Plan-Execute patronen met pseudocode | Medium |
| 7 | Rephrase.it: Decision-Making Prompts voor Agents | https://rephrase-it.com/blog/decision-making-prompts-for-ai-agents | Practitioner artikel | Stop conditions, constraint framing, ReAct als decision structure | Medium |
| 8 | Rephrase.it: Prompt Patterns Production | https://rephrase-it.com/blog/prompt-patterns-for-ai-agents-that-dont-break-in-production | Practitioner artikel | Control flow expliciteren, testable STATE output, dynamic policy assembly | Medium |
| 9 | Adaline: Complete Guide PromptOps 2026 | https://www.adaline.ai/blog/complete-guide-prompt-engineering-operations-promptops-2026 | Practitioner gids | PromptOps lifecycle, versioning, CI/CD gates voor prompts | Hoog |
| 10 | Braintrust: Prompt Optimization Loop | https://www.braintrust.dev/articles/prompt-optimization-loop | Practitioner gids | 5-stap cyclus; production failures → test cases | Hoog |
| 11 | PromptOT: Feedback Loops Improve Prompt Quality | https://www.promptot.com/blog/feedback-loops-improve-prompt-quality | Practitioner artikel | Wekelijkse feedback cycles: 2.1x sneller kwaliteitsverbetering | Medium |
| 12 | Travis Kroon: Feedback Loops That Improve Prompts | https://traviskroon.com/designing-feedback-loops-that-actually-improve-prompts/ | Practitioner artikel | 5-fase structuur: capture → label → analyse → refactor → re-evaluate | Medium |
| 13 | EU AI Act Art. 13 (verified) | https://artificialintelligenceact.eu/article/13/ | Primaire bron | Transparency vereisten high-risk AI; instructies voor deployers | Hoog |
| 14 | EU AI Act Art. 14 (verified) | https://www.euaiact.com/article/14 | Primaire bron | Human oversight vereisten; override/stop capability | Hoog |
| 15 | Applied AI: Best Practices EU AI Act | https://www.appliedai.de/uploads/files/Best-Practices-for-Implementing-the-EU-AI-Act_2025-07-02-092027_vwvf.pdf | Governance rapport | Art. 13 → ISO 6254 mapping; transparency template voor deployers | Hoog |
| 16 | OWASP LLM Top 10 2025 | https://genai.owasp.org/llm-top-10/ + https://genai.owasp.org/llmrisk/llm01-prompt-injection/ | Primaire bron | LLM01 Prompt Injection, LLM06 Excessive Agency, LLM07 System Prompt Leakage mitigaties | Hoog |
| 17 | OWASP Agentic AI Threats & Mitigations (2025) | https://www.aigl.blog/content/files/2025/04/Agentic-AI---Threats-and-Mitigations.pdf | Framework document | Goal manipulation, dynamic intervention thresholds, Plan-Then-Execute mitigatie | Hoog |
| 18 | NIST AI RMF Playbook | https://www.nist.gov/itl/ai-risk-management-framework/nist-ai-rmf-playbook | Primaire bron | GOVERN/MAP/MEASURE/MANAGE functies; 2025 update: prompt injection als dreigingscategorie | Hoog |
| 19 | Elevate Consult: ISO 42001 7-stappen implementatie | https://elevateconsult.com/insights/iso-42001-implementation-7-steps/ | Implementatiegids | ISO 42001 Annex A controls; prompt injection als geïdentificeerde kwetsbaarheid | Medium |
| 20 | Prompt Security: ISO 42001 | https://prompt.security/blog/understanding-the-iso-iec-42001 | Practitioner artikel | ISO 42001 + EU AI Act complementair; audit logging vereist | Medium |
| 21 | ArXiv SoK: Attack Surface Agentic AI (2026) | https://www.arxiv.org/pdf/2603.22928 | Wetenschappelijk paper | "Record versions and hashes of prompts, policies, and tool manifests" | Hoog |
| 22 | Hyperproof: Ultimate Guide EU AI Act (2026) | https://hyperproof.io/ultimate-guide-to-the-eu-ai-act/ | Governance gids | Art. 17 QMS, Art. 19 logs 6 maanden bewaren, Art. 11 technische documentatie | Medium |
| 23 | EU Parliament: Interplay AI Act + EU Digital Framework | https://www.europarl.europa.eu/RegData/etudes/STUD/2025/778575/ECTI_STU(2025)778575_EN.pdf | EU Parliament studie | Art. 26(5)-(6) deployer logs 6 maanden; accountability in lifecycle rollen | Hoog |

---

## Coverage Status

| Onderzoeksvraag | Status | Kwaliteit |
|---|---|---|
| Q4a: Agentic vs chat/single-turn | Volledig gedekt | Hoog — meerdere bronnen consistent |
| Q4b: Beslisbomen, determinisme, refuse, error-handling | Volledig gedekt | Hoog — concrete templates geverifieerd |
| Q4c: Agentic system prompt templates | Volledig gedekt | Hoog — Paxrel 10-patronen, Nibzard 4-patronen |
| Q7: Relatie Prompt Design ↔ Evaluation Loop | Volledig gedekt | Hoog — PromptOps lifecycle, feedback loop structuren |
| Q8a: EU AI Act relevante artikelen | Gedekt | Hoog — Art. 13, 14, 17, 19 direct geverifieerd |
| Q8b: Transparency-verplichtingen | Gedekt | Medium — mapping naar prompts is inference |
| Q8c: Human Agency prompt-patronen | Gedekt | Medium — Art. 14 geverifieerd, patronen inferred |
| Q8d: Accountability governance production prompts | Gedekt | Medium — Art. 17 geverifieerd, operationalisering inferred |
| Q9: NIST / ISO 42001 / OWASP | Gedekt | Hoog — OWASP 2025 direct geverifieerd; NIST+ISO via secundaire bronnen |

**Gaps:**
- EU AI Act Art. 52 (niet relevant gebleken — gaat over classificatieprocedure GPAI modellen met systemisch risico, niet over prompt design)
- NIST AI 100-1 PDF niet direct gelezen (toegang geblokkeerd); gedekt via secondary sources
- ISO 42001 volledige tekst is betaald standaard; gedekt via implementatiegidsen

---

## Sources

1. https://bits-bytes-nn.github.io/insights/agentic-ai/2026/04/05/evolution-of-ai-agentic-patterns-en.html
2. https://www.sitepoint.com/the-definitive-guide-to-agentic-design-patterns-in-2026/
3. https://paxrel.com/blog-ai-agent-prompts
4. https://tianpan.co/blog/2026-02-05-agentic-engineering-patterns-while-loop-easy-part
5. https://nibzard.com/agentic-handbook
6. https://mdsanwarhossain.me/blog-agentic-ai-design-patterns.html
7. https://rephrase-it.com/blog/decision-making-prompts-for-ai-agents
8. https://rephrase-it.com/blog/prompt-patterns-for-ai-agents-that-dont-break-in-production
9. https://www.adaline.ai/blog/complete-guide-prompt-engineering-operations-promptops-2026
10. https://www.braintrust.dev/articles/prompt-optimization-loop
11. https://www.promptot.com/blog/feedback-loops-improve-prompt-quality
12. https://traviskroon.com/designing-feedback-loops-that-actually-improve-prompts/
13. https://artificialintelligenceact.eu/article/13/
14. https://www.euaiact.com/article/14
15. https://www.appliedai.de/uploads/files/Best-Practices-for-Implementing-the-EU-AI-Act_2025-07-02-092027_vwvf.pdf
16. https://genai.owasp.org/llm-top-10/ en https://genai.owasp.org/llmrisk/llm01-prompt-injection/
17. https://www.aigl.blog/content/files/2025/04/Agentic-AI---Threats-and-Mitigations.pdf
18. https://www.nist.gov/itl/ai-risk-management-framework/nist-ai-rmf-playbook
19. https://elevateconsult.com/insights/iso-42001-implementation-7-steps/
20. https://prompt.security/blog/understanding-the-iso-iec-42001
21. https://www.arxiv.org/pdf/2603.22928
22. https://hyperproof.io/ultimate-guide-to-the-eu-ai-act/
23. https://www.europarl.europa.eu/RegData/etudes/STUD/2025/778575/ECTI_STU(2025)778575_EN.pdf
24. https://www.euaiact.com/article/17
25. https://artificialintelligenceact.eu/article/13
26. https://www.iso.org/standard/42001
