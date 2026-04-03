# Cross-Project Taxonomie Mapping

**Versie:** v1.0
**Datum:** 2026-04-03
**Issue:** #29

Mapping van Bastionclaw use-case taxonomie en Natural Intelligence artikel-tags naar BeeHaive Building Blocks (BB) en Guardrails (GR).

---

## Bastionclaw → BeeHaive

### AI-categorie → Building Blocks

| AI-categorie | Primaire BB | Secundaire BB |
|-------------|-------------|---------------|
| LLM | Model Engines | Prompt Design |
| computer-vision | Model Engines | — |
| predictive | Model Engines | Evaluation Loop |
| NLP | Model Engines | Prompt Design |
| robotics | Tool Integration | Model Engines |
| recommendation | Model Engines | Dynamic Context |
| document-processing | Dynamic Context | Tool Integration |
| speech | Model Engines | — |
| process-mining | Evaluation Loop | Tool Integration |
| multimodal | Model Engines | Dynamic Context |

### Procescategorie → Building Blocks

| Procescategorie | Primaire BB | Secundaire BB |
|----------------|-------------|---------------|
| klantenservice | Client Blueprint | Prompt Design |
| operaties | Client Blueprint | Tool Integration |
| compliance | Client Blueprint | Evaluation Loop |
| rapportage | Dynamic Context | Evaluation Loop |
| HR | Client Blueprint | Knowledge |
| finance | Client Blueprint | Dynamic Context |
| marketing | Prompt Design | Client Blueprint |
| R&D | Knowledge | Evaluation Loop |
| supply-chain | Tool Integration | Client Blueprint |
| productie | Tool Integration | Model Engines |
| administratie | Tool Integration | Dynamic Context |
| besluitvorming | Knowledge | Evaluation Loop |

### Impacttype → Guardrails

| Impacttype | Primaire GR | Secundaire GR |
|-----------|-------------|---------------|
| tijdsbesparing | — | — |
| kostenbesparing | — | — |
| kwaliteitsverbetering | Robustness | — |
| schaalbaarheid | Robustness | — |
| compliance | Accountability | Transparency |
| klanttevredenheid | Well-being | — |
| medewerkertevredenheid | Well-being | Human Agency |
| innovatie | — | — |

### Implementatiefase → Guardrail-relevantie

| Fase | Extra GR-aandacht |
|------|-------------------|
| concept | Transparency, Human Agency |
| PoC | Robustness, Privacy |
| pilot | Fairness, Accountability |
| productie | Alle guardrails |
| schaal | Alle guardrails, extra Well-being |

---

## Natural Intelligence → BeeHaive

### Bakjes → Building Blocks & Guardrails

| Bakje | Primaire BB | Primaire GR |
|-------|-------------|-------------|
| mensenwerk | Knowledge | Human Agency |
| ai-robotics | Model Engines | Robustness |
| mens-of-ai | Knowledge | Human Agency, Fairness |
| nieuw-werk | Client Blueprint | Well-being |

### Vaardigheden → Building Blocks & Guardrails

| Vaardigheid | BB | GR |
|------------|----|----|
| samenwerken-met-ai | Knowledge | Human Agency |
| ai-fluency | Knowledge | — |
| oordeelsvermogen-judgment | Knowledge | Human Agency |
| ai-output-beoordelen | Evaluation Loop | Human Agency |
| probleem-framing | Client Blueprint | — |
| creatief-denken | Prompt Design | — |
| teams-van-agents-leiden | Tool Integration | Human Agency |
| ai-inzet-beoordelen | Knowledge | Human Agency |
| workflow-redesign | Client Blueprint | — |
| agentic-engineering | Tool Integration | Accountability |
| trust-architectuur | — | Accountability, Transparency |
| complementariteit-ontwerp | Client Blueprint | Human Agency |
| deskilling-bewustzijn | Knowledge | Well-being |
| epistemia-herkenning | Evaluation Loop | Transparency |
| ai-mindsets | Knowledge | — |
| co-learning | Knowledge | Human Agency |
| awareness-pause-reframe | — | Human Agency |

### Thema's → Guardrails

| Thema | Primaire GR | Secundaire GR |
|-------|-------------|---------------|
| ethiek | Fairness | Transparency |
| governance | Accountability | Transparency |
| complementariteit | Human Agency | — |
| deskilling | Human Agency | Well-being |
| structurele-ongelijkheid | Fairness | Well-being |
| onderwijs | Well-being | Human Agency |
| arbeidsmarkt | Well-being | Fairness |
| productiviteit | — | — |
| carriere-ladder | Fairness | Well-being |
| gebroken-ladder-2 | Fairness | Well-being |

---

## Samenvatting: dekking per BB/GR

### Building Blocks — bronnen

| BB | Bastionclaw (via) | Natural Intelligence (via) |
|----|-------------------|---------------------------|
| **Knowledge** | R&D, HR, besluitvorming | mensenwerk, mens-of-ai, vaardigheden (6x) |
| **Client Blueprint** | klantenservice, operaties, compliance, HR, finance, supply-chain | nieuw-werk, probleem-framing, workflow-redesign, complementariteit-ontwerp |
| **Dynamic Context** | recommendation, document-processing, rapportage, finance, administratie | — |
| **Prompt Design** | LLM, NLP, klantenservice, marketing | creatief-denken |
| **Tool Integration** | robotics, process-mining, supply-chain, productie, administratie | teams-van-agents-leiden, agentic-engineering |
| **Model Engines** | LLM, computer-vision, predictive, NLP, speech, multimodal, recommendation, productie | ai-robotics |
| **Evaluation Loop** | predictive, process-mining, compliance, rapportage, R&D, besluitvorming | ai-output-beoordelen, epistemia-herkenning |

### Guardrails — bronnen

| GR | Bastionclaw (via) | Natural Intelligence (via) |
|----|-------------------|---------------------------|
| **Human Agency** | medewerkertevredenheid, concept-fase | mensenwerk, mens-of-ai, vaardigheden (8x), thema's (3x) |
| **Robustness** | kwaliteitsverbetering, schaalbaarheid, PoC-fase | ai-robotics |
| **Privacy** | PoC-fase | — |
| **Fairness** | pilot-fase | mens-of-ai, ethiek, structurele-ongelijkheid, carriere-ladder, gebroken-ladder-2 |
| **Transparency** | compliance, concept-fase | ethiek, governance, trust-architectuur, epistemia-herkenning |
| **Well-being** | klanttevredenheid, medewerkertevredenheid, schaal-fase | nieuw-werk, onderwijs, arbeidsmarkt, deskilling, structurele-ongelijkheid |
| **Accountability** | compliance | governance, agentic-engineering, trust-architectuur |

---

## Blinde vlekken

| BB/GR | Observatie |
|-------|-----------|
| **Dynamic Context** | Geen NI-bronnen — logisch, NI gaat over menselijke vaardigheden, niet RAG/queries |
| **Privacy** | Minimaal gedekt — alleen indirect via Bastionclaw PoC-fase. Overweeg gerichte bronnen toe te voegen |
| **Robustness** | Beperkt vanuit NI — NI focust op menselijke kant, niet technische robuustheid |
