# Delta-analyse — Tool Integration onderzoeksbronnen

**Datum:** 2026-04-29
**Doel:** vergelijken van vijf parallelle onderzoeksbronnen voor BB_05 om te bepalen welke materialen `final.md` aanvullen of vervangen vóór `/bb-write`.

## Bronnen op tafel

| Bron | Bestand | Regels | Bronnen | Methode |
|------|---------|--------|---------|---------|
| Lokale researchers (Claude) | `final.md` | 257 | 23 (19 verified) | 3 parallelle agents → synthese + verificatiepass |
| Gemini Deep Research (web UI, jouw run) | `research-gemini-deep-research.md` | 382 | 48 | Google Gemini agentic deep-research |
| Gemini 3.1 Pro preview (CLI) | `research-gemini-3.1-pro.md.raw` | 206 | 11 | single-shot headless |
| Gemini 3 Pro preview (CLI) | `research-gemini-3-pro.md.raw` | 249 | 12 | single-shot headless |
| Gemini 2.5 Pro (CLI) | `research-gemini-2.5-pro.md.raw` | 142 | 18 | single-shot headless |

CLI-runs zijn synthetisch (geen actuele bronnen-URL's, vaak alleen domein-niveau). Alleen geschikt als secondary check, niet om te integreren.

De vergelijking gaat dus om **`final.md` versus Deep Research**.

## Overlap (beide bronnen behandelen het grondig)

- MCP als universele standaard, vendor-neutrale adapter, OAuth-flow
- Function calling basics + client vs. server-side tools
- Drie orchestratie-patronen: ReAct, Plan-Then-Execute, Programmatic Tool Calling
- OWASP LLM Top 10 — LLM01 prompt injection (direct/indirect), LLM06 excessive agency
- EU AI Act Art. 12 (record-keeping) + Art. 14 (human oversight)
- Circuit breaker, retry, exponential backoff als productiepatronen
- Tool description als primair stuursignaal
- Least privilege / RBAC op de executielaag
- HITL bij write-operaties
- Log-To-Leak / indirect prompt injection via tool descriptions

## Wat Deep Research extra heeft (waardevolle aanvullingen)

### Concrete getallen die `final.md` mist

- **Latency-budgets P50/P95** voor 3 niveaus:
  - Direct Model Call: P50 < 500ms, P95 < 1s
  - Single Agent met Tools: P50 < 2s, P95 < 4s
  - Multi-Agent: P50 < 3s, P95 < 6s
- **Tenacity-config in productie**: `wait_random_exponential(multiplier=0.25, max=6)`, `stop_after_attempt(4)`
- **Context bloat-omvang**: tot 150.000 tokens voor tool-definities bij grote catalogi
- **Plan-Then-Execute upfront kosten**: 3.000–4.500 tokens voor planningfase
- **Kostenreductie via patronen**: semantic caching 30–70%, intelligent model routing tot 80%

### Inhoudelijke uitbreidingen

- **CVE-2025-32711 (EchoLeak)** — concrete CVE-referentie voor MCP-kwetsbaarheid in Microsoft Copilot (genoemd in Deep Research, niet in `final.md`)
- **"Lethal trifecta"** als framing voor agent-risico: privé-data + onbetrouwbare content + externe acties
- **RUG Pull attack** als specifieke supply-chain term voor MCP
- **Vier-componenten Log-To-Leak structuur**: Trigger / Tool Binding / Justification / Pressure
- **DAG-based parallel search**: 3.6× performance improvement (RAG-MCP patroon)
- **Strict mode waarschuwing**: syntactisch correct ≠ semantisch correct — strikt schema garandeert structuur, niet juistheid van waardes
- **Half-open status** circuit breaker-beschrijving (gecontroleerde testverzoeken na cooldown)

### Industrie-positionering met getallen

- Anthropic Claude: >95% success rate op 5-staps agentic operations
- OpenAI: ~88% op complexe tool-ketens
- Google Gemini: ~75% op 5-staps orchestration ("flaky shapes" — JSON in markdown gewikkeld)
- Open-weights (DeepSeek R1/V3, Mistral Large 3) als kostenefficiënt alternatief voor air-gapped deployments
- Framework-typering:
  - LangChain/LangGraph: industry standard voor enterprise-orchestratie
  - CrewAI: multi-agent — hoge token-overhead, primair voor offline exploratief werk
  - LlamaIndex: RAG-specialist, vaak feeder voor LangGraph-orchestrator

### Nederland-specifieke regelgeving

- Nederlandse implementatiewet AI Act, ontwerp april 2026 (decentraal toezicht)
- LangSmith / LangGraph als concrete tools om Art. 12 logging-eisen technisch in te vullen

## Wat `final.md` extra heeft (Deep Research mist)

### Anthropic-specifieke productie-details

- Tool token-overhead: 313–346 tokens per tool in system prompt (Claude Opus 4.7)
- Computer Use: 466–499 tokens system overhead + 735 tokens per tool per call
- Server-side tools concreet benoemd: `web_search`, `code_execution`, `web_fetch`
- `is_error: true` protocol voor graceful degradation
- Strict mode op tool-niveau (`strict: true`) — Anthropic-spec
- Defer loading via `defer_loading: true` + Tool Search server tool

### Schema-design diepgang

- Naam-conventies: snake_case, action-oriented, max 64 tekens
- Anti-patroon: enumeratie-opties in description-tekst i.p.v. `enum`-constraint
- Nesting depth limit: 5 levels max
- `additionalProperties: false` om onverwachte velden te blokkeren
- Semantic versioning interpretatie voor tool-schemas: major (breaking parameter), minor (nieuwe optionele param), patch (description-verbetering)

### MCP-implementatiedetails

- Transport-keuzes: stdio voor dev, Streamable HTTP voor productie
- OAuth 2.1 voor remote MCP-servers, beschikbaar sinds maart 2025
- `tools/list`, `tools/call`, `notifications/tools/list_changed` als concrete API-calls
- Pattern: agents zelf exposen als MCP server (vendor-neutraal multi-agent)
- 5.000+ community MCP-servers per mei 2025

### Methodologische rigor

- Verificatiestatus per claim: `verified` / `inferred` / `unverified`
- Tegenstrijdigheden expliciet benoemd (MCP vs directe API, generiek vs specifiek, security vs productiviteit)
- Anti-patroon: tools alleen monitoren op uptime/latency — kwaliteit ontbreekt dan
- PromptInjectionShield-patroon: tool result scanning vóór context

### Operationele patronen

- Idempotency keys voor write-tools (voorkom dubbele transacties bij retry)
- Circuit breaker concrete drempels: LLM-API 50%/20 requests, externe API 30%/10 requests, cooldown 30s tot max 5min
- Timeout-tiers: LLM 30s standaard, complex 60s, inter-agent 10s, externe API 3–10s

## Aanbeveling — wat te doen vóór `/bb-write`

`final.md` is sterker op Anthropic-specifieke productiediepte en verificatie-methode. Deep Research is sterker op concrete benchmarks, latency-getallen, en industrie-positionering.

**Strategie: `final.md` als basis + chirurgische aanvullingen uit Deep Research.**

Kandidaat-aanvullingen voor `final.md` (geen volledige herschrijving, alleen toevoegen wat ontbreekt):

1. **Sectie "Betrouwbaarheid in productie"** — toevoegen:
   - Concrete latency-budgets P50/P95 per agent-niveau
   - Tenacity-config als concrete Python-snippet (multiplier=0.25, max=6, attempts=4)

2. **Sectie "Beveiliging"** — toevoegen:
   - CVE-2025-32711 (EchoLeak) als referentie
   - "Lethal trifecta" als didactisch framing-concept
   - 4-componenten Log-To-Leak structuur (Trigger/Binding/Justification/Pressure)
   - RUG Pull attack expliciet benoemen

3. **Sectie "Kosten en observability"** — toevoegen:
   - Semantic caching 30–70% besparing
   - Intelligent model routing tot 80% besparing
   - Context bloat-cijfer (150K tokens bij grote tool-catalogus)

4. **Nieuwe subsectie "Strict mode-waarschuwing"** in Schema-ontwerp:
   - Strict mode garandeert structuur, niet semantische correctheid
   - Onafhankelijke content-validatie blijft nodig

5. **Sectie "Tegenstrijdigheden en open vragen"** — uitbreiden:
   - Industrie-benchmarks (Claude 95% / OpenAI 88% / Gemini 75%) als concrete trade-off
   - Nederland-specifieke AI Act-implementatie (april 2026, decentraal toezicht)

**Niet overnemen** uit Deep Research:
- "Lethal trifecta" als term zonder bron-context (wordt in DR aan algemene security-blogs gekoppeld, geen peer-reviewed)
- Specifieke benchmark-percentages (95/88/75%) zonder bron-verificatie — markeren als `unverified` of weglaten
- Open-weights-vergelijkingen (DeepSeek/Mistral) — buiten scope BeeHaive (Anthropic-stack)

**CLI-runs (3.1-pro, 3-pro, 2.5-pro)**: archiveren in `archived/` of laten staan voor methodologische audit. Niet integreren — synthetisch en zonder concrete bronnen.

## Methodologische observaties

1. **Lokale researchers (Claude)** produceerden compactere output (257 vs 382 regels) maar met hogere bron-discipline (verificatiestatus per claim).
2. **Gemini Deep Research** geeft meer breedte (48 bronnen) en concrete getallen, maar zonder per-claim verificatie — inhoud die we overnemen moet alsnog gevalideerd via WebFetch.
3. **CLI single-shot Gemini** (zelfs Pro/3.x) is geen substituut voor agentic deep research — het mist de iteratieve search-loop die Deep Research wel heeft.
4. **Voor toekomstige BB's**: Deep Research draaien parallel aan lokale research is waardevol bij brede onderwerpen waar concrete benchmarks/getallen nodig zijn. Voor onderwerpen met sterke vendor-documentatie (zoals Tool Use op Anthropic) blijft de lokale researcher-aanpak superieur.
