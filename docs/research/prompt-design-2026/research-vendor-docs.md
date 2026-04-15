# Research: Vendor Docs — Prompt Design 2026

**Researcher:** researcher-2
**Dimensie:** Officiële vendor documentatie (Anthropic, OpenAI, Google)
**Datum:** 2026-04-15

## Samenvatting (1 zin)

Alle drie de frontier-model vendors (Anthropic, OpenAI, Google) convergen naar dezelfde kern-principes — helderheid, structurering met XML/Markdown, few-shot voorbeelden, en expliciete output-contracten — maar divergeren sterk in model-specifieke instructiearchitectuur en rolzetting.

---

## Bevindingen

### Anthropic — officiële guidance

**Bron:** `platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices` [1]
**Status:** verified (direct gescraped 2026-04-15)

Anthropic publiceert één centrale referentiepagina voor Claude Opus 4.6, Claude Sonnet 4.6 en Claude Haiku 4.5. De pagina is gedateerd als "living reference".

**Kern-principes:**

1. **Wees helder en direct** — Claude reageert goed op expliciete instructies. Anthropic gebruikt de metafoor van een "brilliant but new employee": geef context, leg doelen uit. Golden rule: laat een collega de prompt lezen; als die verward is, is Claude dat ook.

2. **XML-structurering** — XML-tags zijn de primaire structuratiemethode die Anthropic aanbeveelt: `<instructions>`, `<context>`, `<input>`, `<example>`, `<examples>`. Tags reduceren misinterpretatie bij complexe prompts met gemixte content.

3. **Few-shot examples** — Wrap voorbeelden in `<example>` tags. Aanbeveling: 3-5 voorbeelden, divers en relevant. Claude kan ook gevraagd worden zijn eigen voorbeelden te evalueren of te genereren.

4. **Rolzetting ("Give Claude a role")** — Anthropic raadt nog steeds aan om een rol te geven via het system prompt: *"You are a helpful coding assistant specializing in Python."* De formulering is dat het "focuses Claude's behavior and tone" — maar er is geen claim dat dit overbodig is geworden voor nieuwere modellen. [inferred: impliceert nog steeds waarde, niet verouderd verklaard op deze pagina]

5. **Long context** — Lange data bovenaan de prompt plaatsen, query onderaan ("Queries at the end can improve response quality by up to 30%"). Documenthierarchie via geneste XML-tags.

6. **Formatting controle** — Claude 4.x is meer direct en minder verbose dan vorige generaties. Instructies via expliciete proza-stijl ("Your response should be composed of smoothly flowing prose paragraphs") werken beter dan negaties ("Do not use markdown"). Matching van prompt-stijl aan gewenste output-stijl.

7. **Tool use** — Claude 4.5/4.6 zijn gevoeliger voor system prompt dan vorige modellen. Aggressive language ("CRITICAL: You MUST...") veroorzaakt nu overtriggering; normale formulering ("Use this tool when...") werkt beter.

8. **Thinking/reasoning** — Adaptive thinking (`thinking: {type: "adaptive"}`) voor Claude 4.6. Effort-parameter (low/medium/high/max) vervangt handmatige `budget_tokens`. Algemene instructies ("think thoroughly") presteren beter dan handmatig voorgeschreven stapsgewijze redenering.

9. **Prefill verouderd** — Prefilled responses op de laatste assistant turn zijn **deprecated** vanaf Claude 4.6. Meeste use cases van prefill zijn overbodig geworden door verbeterd instruction following.

10. **Migratieguidance** — Anthropic benadrukt dat "anti-laziness prompting" teruggeschroefd moet worden: Claude 4.6 is proacter dan vorige modellen.

**Opvallend verschil met GPT/Gemini:**
- Anthropic-specifiek: XML-tags als primaire structureringsmethode (niet Markdown headers).
- Claude-specifiek: voorkeur voor instructies over wat te *doen* i.p.v. wat *niet* te doen.
- Adaptive thinking (effort parameter) is Anthropic-eigen mechanisme.
- Prefill deprecatie is Anthropic-specifiek.

---

### OpenAI — officiële guidance

**Bronnen:**
- `developers.openai.com/api/docs/guides/prompt-engineering` [2] — verified
- `developers.openai.com/api/docs/guides/prompting` [3] — verified
- `developers.openai.com/api/docs/guides/prompt-guidance` (GPT-5.4) [4] — verified

**Structuur van een developer message (OpenAI officieel template):**

OpenAI publiceert op de prompt-engineering pagina een officiële aanbevolen structuur voor een `developer` message [2]:

> *"In general, a developer message will contain the following sections, usually in this order:*
> 1. **Identity** — describe purpose, communication style, high-level goals
> 2. **Instructions** — rules, what to do, what never to do
> 3. **Examples** — input/output voorbeelden (few-shot)
> 4. **Context** — aanvullende data, best gepositioneerd aan het einde"*

Dit is de dichtstbijzijnde officiële 4-onderdelen structuur van OpenAI. Een vijfde onderdeel (Edge Cases) wordt niet expliciet benoemd als template-element maar wel behandeld in de inhoud.

**Bericht-rollen:**
- OpenAI gebruikt `developer` + `user` + `assistant` rollen (niet meer `system`).
- `developer` berichten zijn hogerprioritair dan `user` berichten.
- `instructions` parameter (Responses API) heeft prioriteit boven `input`.

**Few-shot:**
- OpenAI raadt aan voorbeelden op te nemen in de `developer` message.
- Gebruik XML-tags voor afbakening: `<product_review id="example-1">`, `<assistant_response id="example-1">`.

**Reasoning models vs GPT models:**
- Reasoning models (o1, o3): geef hoog-niveau doelen, vertrouw het model. "Like a senior co-worker."
- GPT models (gpt-5, gpt-4.1): geef expliciete instructies. "Like a junior co-worker."

**GPT-5.4 specifieke guidance [4] (verified):**

GPT-5.4 prompt-guidance documentatie bevat expliciete XML-blokken als prompt-componenten:
- `<output_contract>` — gestructureerde output-definitie
- `<verbosity_controls>` — lengte-regulering
- `<tool_persistence_rules>` — tool-gebruik regels
- `<completeness_contract>` — voltooiingscriteria
- `<verification_loop>` — verificatie voor finale output
- `<research_mode>` — 3-pass research structuur (Plan → Retrieve → Synthesize)
- `<personality_and_writing_controls>` — persona + kanaal + register

**Reasoning effort (GPT-5.4):**
- `none` voor snelle, kostgevoelige taken
- `low` voor latensgevoelige taken
- `medium`/`high` voor echte redeneerbehoeften
- `xhigh` alleen voor lange agentic taken

**Opvallend:**
- OpenAI heeft de `system` rol hernoemd naar `developer` in de Responses API.
- Structuur van developer message is officieel gedocumenteerd (Identity/Instructions/Examples/Context).
- `reasoning_effort` is het OpenAI-equivalent van Anthropic's `effort` parameter.

---

### Google/Gemini — officiële guidance

**Bron:** `ai.google.dev/gemini-api/docs/prompting-strategies` [5] — verified (last updated 2026-04-09)

**Kern-principes (algemeen, Gemini 2.x en ouder):**

1. **Duidelijke en specifieke instructies** — Input types: question, task, entity, completion. Expliciete constraints en response format.
2. **Few-shot prompts** — Altijd aanbevolen. "We recommend to always include few-shot examples in your prompts. Prompts without few-shot examples are likely to be less effective." Consistente formatting essentieel.
3. **Context toevoegen** — Grounding in domeinspecifieke data.
4. **Opsplitsing in componenten** — Break-down instructions, chain prompts, aggregate responses.
5. **Model parameters** — Temperature, topK, topP, max output tokens, stop sequences.
6. **Grounding en code execution** — Google Search grounding en Python code execution als tools.

**Gemini 3 specifieke principes (nieuwste sectie):**

- **Wees precies en direct** — vermijd onnodige of overtuigende taal.
- **Gebruik consistente structuur** — XML-stijl tags (`<context>`, `<task>`) OF Markdown headers; kies één formaat en houd dat aan.
- **Verbosity controle** — Gemini 3 geeft standaard directe, efficiënte antwoorden. Wil je meer detail: vraag er expliciet om.
- **Prioriteer kritieke instructies** — Role-definities, output format en gedragsbeperkingen in de System Instruction of aan het begin van de user prompt.
- **Structuur voor lange context** — Geef alle context eerst; instructies/vragen helemaal aan het einde. "Based on the information above..."

**Gemini 3 officieel template:**

Google publiceert een volledig system instruction template voor Gemini 3 [5]:

```
<role>
You are Gemini 3, a specialized assistant for [Domain].
You are precise, analytical, and persistent.
</role>

<instructions>
1. Plan: Analyze the task and create a step-by-step plan.
2. Execute: Carry out the plan.
3. Validate: Review your output against the user's task.
4. Format: Present the final answer in the requested structure.
</instructions>

<constraints>
- Verbosity: [Low/Medium/High]
- Tone: [Formal/Casual/Technical]
</constraints>

<output_format>
1. Executive Summary
2. Detailed Response
</output_format>
```

En een user prompt template:
```
<context>[documents/code/background]</context>
<task>[specific request]</task>
<final_instruction>Remember to think step-by-step before answering.</final_instruction>
```

**Thinking:**
- Gemini 2.5 en 3 genereren automatisch intern "thinking" tekst.
- "It's generally not necessary to have the model outline, plan, or detail reasoning steps in the returned response itself."
- Simpele prompts als "Think very hard before answering" kunnen prestaties verbeteren.

**Grounding performance:**
- Expliciete grounding-instructies aanbevolen voor Gemini 3 Flash.
- Kennis-cutoff datum expliciet in system instruction vermelden.

---

### Wat is model-invariant, wat model-specifiek?

**MODEL-INVARIANT (werkt overal):**

| Principe | Anthropic | OpenAI | Google |
|----------|-----------|--------|--------|
| Duidelijke, specifieke instructies | ✓ | ✓ | ✓ |
| Few-shot voorbeelden | ✓ (3-5) | ✓ | ✓ (altijd) |
| Context/grounding toevoegen | ✓ | ✓ | ✓ |
| Structurering met tags/markers | XML | XML + Markdown | XML of Markdown |
| Long context: data eerst, vraag last | ✓ | ✓ | ✓ |
| Positief formuleren (wat te doen) | ✓ | impliciet | impliciet |
| Output format expliciet specificeren | ✓ | ✓ | ✓ |
| Iteratief testen/evalueren | ✓ | ✓ | ✓ |

**MODEL-SPECIFIEK:**

| Aspect | Anthropic (Claude) | OpenAI (GPT-5.x) | Google (Gemini 3) |
|--------|-------------------|------------------|-------------------|
| Primaire structuur | XML-tags | XML + Markdown | XML OF Markdown |
| System prompt naam | `system` | `developer` (nieuw) | System Instruction |
| Reasoning controle | `effort` parameter (adaptive thinking) | `reasoning_effort` parameter | Automatisch (impliciet) |
| Prefill/completion | Deprecated | Niet standaard | Completion strategy |
| Expliciete rol-instructie | Aanbevolen | Aanbevolen (Identity sectie) | Aanbevolen (role tag) |
| Instructievolgorde | Instructies voor lange data | Identity→Instructions→Examples→Context | Role→Constraints→Context→Task |
| Tool-triggering | Normale taal, geen CAPS/MUST | Expliciete tool rules blokken | Agentic SI template |

---

### Officieel standpunt over rolzetting/persona

**Vraag:** Heeft Anthropic of OpenAI officieel verklaard dat "rolzetting/persona-prompts" minder nodig zijn met recente modellen?

**Anthropic:**
- De pagina `claude-prompting-best-practices` [1] beveelt rolzetting nog steeds aan: *"Give Claude a role... Even a single sentence makes a difference."*
- Geen expliciete verklaring dat rolzetting overbodig is geworden.
- De eerder genoemde URL `anthropic.com/research/claude-s-character` geeft een **404** [6] — `blocked`.
- [inferred] De verwijzing naar Claude's character/identiteit als een *inherent* kenmerk (eerder beschreven in Anthropic's model-spec) suggereert dat Claude minder afhankelijk is van extern opgelegde persona's voor basaal gedrag, maar rolzetting voor taakspecifieke sturing blijft aanbevolen.

**OpenAI:**
- GPT-5.4 guidance [4] en prompt-engineering [2]: Identity sectie in developer message is standaard aanbevolen.
- Reasoning models: "like a senior co-worker" — impliciet dat minder expliciete instructies nodig zijn voor redeneermodellen.
- Geen expliciete statement dat persona-prompts minder nodig zijn.

**Google:**
- Gemini 3 template [5] bevat een `<role>` tag als standaard onderdeel van het system instruction.
- "Prioritize critical instructions: Place essential behavioral constraints, role definitions (persona), and output format requirements in the System Instruction."
- Geen afschaffing van rolzetting gemeld.

**Conclusie:** Geen van de drie vendors heeft officieel verklaard dat rolzetting/persona-prompts overbodig zijn. Alle drie bevelen het nog steeds aan als onderdeel van een goed gestructureerd system prompt. Het verschil is dat *nieuwere modellen minder afhankelijk zijn van kunstmatige personas* voor basisgedrag (Anthropic's model-spec achtergrond), maar domein-specifieke rolzetting blijft effectief. [inferred/unverified voor Anthropic character-artikel specifiek, verified voor de prompting guidelines]

---

### Officiële system prompt structuur

**Vraag:** Heeft een van de vendors een 5-onderdelen template (Identity/Rules/Format/Edge Cases/Examples) gepubliceerd?

**OpenAI — 4-onderdelen template [2] (verified):**

OpenAI heeft officieel een 4-sectie structuur gepubliceerd voor een `developer` message:
1. **Identity** — doel, communicatiestijl, high-level goals
2. **Instructions** — regels, wat te doen, wat nooit te doen
3. **Examples** — few-shot voorbeelden
4. **Context** — aanvullende data (aan het einde)

Edge Cases worden niet als aparte sectie benoemd, maar wel inhoudelijk behandeld (bijv. via `<missing_context_gating>`, `<default_follow_through_policy>` blokken in GPT-5.4 guidance).

**Google Gemini 3 — volledig template [5] (verified):**

Google publiceert een vollediger system instruction template:
1. `<role>` — wie het model is
2. `<instructions>` — Plan/Execute/Validate/Format stappenplan
3. `<constraints>` — verbosity, tone
4. `<output_format>` — structuur van het antwoord

Plus een separaat user prompt template met `<context>`, `<task>`, `<final_instruction>`.

**Anthropic — geen formeel template-schema [1] (verified):**

Anthropic publiceert geen expliciete genummerde template-structuur. De guidance beschrijft technieken los van elkaar (rol, XML-tags, examples, context-positie), maar presenteert ze niet als een geordend template. [inferred: Anthropic's benadering is meer principe-gebaseerd dan template-gebaseerd]

**Conclusie:** Geen van de drie vendors publiceert exact een 5-onderdelen template met "Edge Cases" als benoemd onderdeel. OpenAI komt het dichtst in de buurt met een officieel 4-sectie model. Google heeft het uitgebreidste gepubliceerde template.

---

## Evidence Table

| # | Bron | URL | Type | Key claim | Confidence |
|---|------|-----|------|-----------|------------|
| 1 | Anthropic Prompting Best Practices | https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices | Officiële docs | XML-structurering, rol, few-shot, long context, prefill deprecated | verified |
| 2 | OpenAI Prompt Engineering | https://developers.openai.com/api/docs/guides/prompt-engineering | Officiële docs | 4-sectie template, developer/user rollen, few-shot, reasoning vs GPT | verified |
| 3 | OpenAI Prompting Overview | https://developers.openai.com/api/docs/guides/prompting | Officiële docs | Prompt caching, system role = developer, reusable prompts | verified |
| 4 | OpenAI Prompt Guidance GPT-5.4 | https://developers.openai.com/api/docs/guides/prompt-guidance | Officiële docs | XML blokken als prompt componenten, reasoning effort, completeness contracts | verified |
| 5 | Google Gemini Prompt Design Strategies | https://ai.google.dev/gemini-api/docs/prompting-strategies | Officiële docs | Few-shot altijd aanbevolen, Gemini 3 template, thinking automatisch | verified |
| 6 | Anthropic Claude's Character | https://www.anthropic.com/research/claude-s-character | Research blog | Claim over inherente identiteit en minder afhankelijkheid van persona-prompts | blocked (404) |

---

## Coverage Status

| Vraag | Status | Notities |
|-------|--------|---------|
| Q1: Anthropic officiële guidance | Volledig gedekt | claude-prompting-best-practices gescraped |
| Q2: OpenAI officiële guidance | Volledig gedekt | prompt-engineering + prompt-guidance gescraped |
| Q3: Google Gemini guidance | Volledig gedekt | prompting-strategies gescraped (updated 2026-04-09) |
| Q4: Model-invariant vs model-specifiek | Gedekt (inferred analyse) | Op basis van vergelijking van de drie bronnen |
| Q5: Rolzetting/persona minder nodig | Gedeeltelijk | Anthropic character-artikel 404; overige bronnen bevelen rolzetting aan |
| Q6: 5-onderdelen system prompt template | Gedekt | OpenAI 4-sectie officieel; Google volledig template; Anthropic geen formeel schema |

---

## Sources

1. Anthropic. *Prompting best practices.* platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices — Scraped 2026-04-15, cached 2026-04-15T07:36.
2. OpenAI. *Prompt engineering.* developers.openai.com/api/docs/guides/prompt-engineering — Scraped 2026-04-15.
3. OpenAI. *Prompting.* developers.openai.com/api/docs/guides/prompting — Scraped 2026-04-15, cached 2026-04-14.
4. OpenAI. *Prompt guidance for GPT-5.4.* developers.openai.com/api/docs/guides/prompt-guidance — Scraped 2026-04-15, cached 2026-04-15T09:50.
5. Google. *Prompt design strategies.* ai.google.dev/gemini-api/docs/prompting-strategies — Scraped 2026-04-15, last updated 2026-04-09 UTC.
6. Anthropic. *Claude's character.* www.anthropic.com/research/claude-s-character — **404 Not Found** (blocked).
