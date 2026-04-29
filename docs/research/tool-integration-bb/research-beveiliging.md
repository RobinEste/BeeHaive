# Research: Betrouwbaarheid & Beveiliging — Tool Integration (BB_05)

**Researcher:** researcher-2
**Dimensie:** Error handling, timeouts, circuit breakers, OWASP LLM tool-gerelateerde risico's, prompt injection via tools, audit logging, EU AI Act compliance
**Datum:** 2026-04-29

## Samenvatting (1 zin)

Productierobuustheid voor tool integration vraagt om drie lagen: technische betrouwbaarheid (retry/circuit breaker/timeout/fallback), beveiligingscontroles die op de executielaag worden afgedwongen en niet op LLM-instructies vertrouwen, en compliance-logging die voldoet aan EU AI Act Art. 12 voor high-risk systemen (deadline augustus 2026).

## Bevindingen

### 1. Technische betrouwbaarheid: de vijf patronen

**Patroon 1: Retry met exponential backoff**

LLM API's falen 1–5% van de tijd door rate limits, timeouts en server errors. Implementeer retry met jitter om thundering-herd te voorkomen. Vuistregels uit productie: [1, 2] (`verified`)
- 3 retries voor transitoire fouten (rate limits HTTP 429, timeouts, server errors 5xx)
- Maximaal 1–2 retries bij kwaliteitsfouten (hallucinaties) — meer retries leveren dezelfde hallucinatie
- Geen retry bij permanente fouten (HTTP 401/403, HTTP 400, context window overflow)

**Patroon 2: Circuit Breaker**

Circuit breakers voorkomen cascade-falen door direct te weigeren zodra een drempel is overschreden. Drie staten: CLOSED (normaal), OPEN (weigert alles), HALF-OPEN (test één request). [2, 3] (`verified`)

Productie-parameters (uit case studies): [1] (`verified`)
- LLM API calls: failure threshold 50% over 20 requests of 60 seconden
- Externe API's: threshold 30% over 10 requests (doorgaans betrouwbaarder)
- Cooldown: start op 30 seconden, exponential backoff tot max 5 minuten
- Voordeel: fail in microseconds i.p.v. 30 seconden spinner

**Patroon 3: Timeout management**

Elke externe call heeft een expliciete timeout. Geen uitzondering. [1] (`verified`)

| Operatie | Aanbevolen timeout |
|----------|-------------------|
| LLM standaard prompt | 30 seconden |
| LLM complexe redenering | 60 seconden |
| Inter-agent communicatie | 10 seconden |
| Externe API data retrieval | 5 seconden |
| Externe API actie uitvoering | 10 seconden |
| Tool execution (individueel) | 3–10 seconden afhankelijk van service |

**Patroon 4: Fallback mechanismes**

Fallback-hiërarchie bij tool-falen: [4] (`verified`)
1. Goedkoper model / alternatieve implementatie
2. Cached response (voor read-only tools)
3. Gedeeltelijke response met uitleg van beperking
4. Human escalation
5. "Service tijdelijk niet beschikbaar"

Semantische fallbacks — stel niet-urgente acties uit, route onzekere uitkomsten naar menselijke review.

**Patroon 5: Graceful degradation**

Ontwerp systemen zodat een falende tool de agent-loop niet blokkeert. Stel `is_error: true` in de `tool_result` zodat het model het falen ziet en kan compenseren — vraag om verduidelijking, probeer alternatieve aanpak, of rapporteer de beperking. [5] (`verified` — Anthropic tutorial docs)

Bewijs: Correct geïmplementeerde error handling verhoogde agentbetrouwbaarheid van 87% naar 99.2% in een gedocumenteerde case. [4] (`verified` — getathenic.com)

### 2. OWASP LLM Top 10 — tool-relevante risico's

**LLM01: Prompt Injection (hoogste prioriteit)** [6] (`verified` — owasp.org PDF 2025)

Directe aanval: een kwaadaardige gebruiker probeert via tool-input het model om te leiden.
Indirecte aanval: een tool retourneert content die instructies bevat (bijv. een webpagina, document, of API-response). De meest gevaarlijke variant voor tool integration.

Concrete aanval (Log-To-Leak): een aanvaller injecteert in de *beschrijving* van een MCP-tool instructies die de agent dwingen een logging-tool aan te roepen om alle interacties te exfiltreren. [7] (`verified` — OpenReview paper)

Mitigatiestrategie:
- Behandel het LLM als een untrusted intermediary, niet als trusted component [8] (`verified` — kiteworks.com)
- Voer security controls af op de executielaag, onafhankelijk van het model
- Scan tool results voor injection-patronen vóór ze het LLM context in gaan (PromptInjectionShield-patroon) [9] (`verified` — github.com/aden-hive)
- Plan-Then-Execute: scheid planfase (zonder user content) van uitvoeringsfase
- Output screening: beoordeel de output van het model vóór die doorgaat naar downstream tools

**LLM06: Excessive Agency** [6] (`inferred` — OWASP docs + brightlume.ai)

AI-systemen die meer bevoegdheden hebben dan nodig. Mitigatie: Role-Based Access Control (RBAC) per agent: een claims-verwerkende agent mag `approve_claim` aanroepen; een klantenservice-agent niet.

**LLM07: System Prompt Leakage** [6] (`verified` — owasp.org)

Sla credentials nooit op in de system prompt. Security controls mogen niet afhangen van system prompt-instructies — injectie kan die omzeilen. Privilege separation, authorization bounds checks moeten deterministisch en auditeerbaar zijn, buiten de LLM.

### 3. Audit logging — wat vastleggen?

Audit logging voor AI-tools gaat verder dan traditionele access logs. Minimale inhoud per model-interactie: [8] (`verified` — kiteworks.com)
- Authenticated user identity en session ID
- Interactie-samenvatting (niet per se de volledige prompt, maar genoeg om het type te identificeren)
- **Elke tool call**, met de complete parameter-set
- **Elk document opgehaald**, met document-ID en gevoeligheidsclassificatie
- Autorisatiebeslissingen per operatie (inclusief weigeringen)
- Output-classificatie (voldoet de output aan verwachte patronen, of triggerde het output filters)

Anomaliedectie op basis van audit logs (actief, niet alleen forensisch): tool calls met afwijkende path-parameters, retrieval-patronen die afwijken van gedragsbaselines, output filter trigger rates. [8] (`verified`)

Technisch: Microsoft Agent Governance Toolkit implementeert Merkle audit chain (SHA-256 hash chaining) + CloudEvents v1.0 voor tamper-evident audit trail. [10] (`verified` — github.com/microsoft/agent-governance-toolkit)

### 4. EU AI Act compliance voor tool integration

**Tijdlijn:** High-risk systeem-verplichtingen per 2 augustus 2026. [11] (`verified` — github AUTHENSOR docs)

**Art. 12 — Record-Keeping en Logging:**
Voor high-risk AI-systemen: automatische logging die traceerbaarheid mogelijk maakt. Logs moeten malfunctions en performance drift identificeren, tamper-resistant zijn. Minimale retentie: 6 maanden.

Specifiek voor agent-systemen (Art. 12):
- Elke beslissing gelogd (inclusief tool-calls en hun redenering)
- Traceerbaarheid: reconstructie van hoe een beslissing tot stand kwam
- Input-recording: wat triggerde elke actie
- Duration-tracking: wanneer de agent actief was

**Art. 14 — Human Oversight:**
Systemen moeten ontworpen zijn voor effectief menselijk toezicht. Inclusief:
- Mogelijkheid om anomalieën te detecteren
- Automation bias voorkomen
- Interveniëren/onderbreken via stop-knoppen of override-mechanismes

Praktische implicatie voor tool integration: een agent zonder expliciete stopcondities en kill-switch is in high-risk contexten mogelijk non-compliant. [5] (`inferred` — OWASP + EU AI Act alignment)

Tooling die dit automatiseert: Protectron.ai (LangChain/CrewAI callbacks), Agent ID (gateway-layer), Difinity.ai (runtime enforcement gateway). [11, 12, 13] (`unverified` — zelfrapportage door vendors)

### 5. Least privilege principe voor tools

Elke agent krijgt alleen de tools die nodig zijn voor zijn specifieke taak. Implementeer op de executielaag (niet via model-instructies): [6, 14] (`verified` — OWASP + brightlume.ai)
- RBAC per agent: definieer welke agents welke tools mogen aanroepen
- Namespace-gebaseerde permissions
- Rate limiting per tool per agent
- Monitoring voor abuse-patronen

Anti-patroon: één superagent met toegang tot alle tools — hoog blast-radius bij prompt injection of misfunctioning.

### 6. Idempotentie en veilige tool-design

Tools die data schrijven moeten idempotent zijn waar mogelijk. Anders kunnen retries bij network failures data corrupteren. [3] (`verified` — webcoderspeed.com)

Onderscheid:
- Read-only tools: veilig voor retry
- Write tools (betalingen, database-mutaties): idempotency keys vereist
- Destructive tools (delete, send email): menselijke bevestiging vereist vóór uitvoering

## Evidence Table

| # | Bron | URL | Type | Key claim | Confidence |
|---|------|-----|------|-----------|------------|
| 1 | AI Workflow Lab — Resilience Patterns | https://aiworkflowlab.dev/article/ai-agent-resilience-production-retry-fallback-circuit-breaker-python | secondary | circuit breaker parameters, timeout tiers | high |
| 2 | enricopiovano.com — LLM Error Handling | https://enricopiovano.com/blog/llm-error-handling-resilience-production | secondary | retry patterns, circuit breaker theory | medium |
| 3 | agentcenter.cloud — Error Handling | https://agentcenter.cloud/blogs/ai-agent-error-handling-resilient-pipelines | secondary | retry vs. circuit breaker gebruik | medium |
| 4 | getathenic.com — Error Handling Patterns | https://getathenic.com/blog/error-handling-reliability-patterns-production-ai-agents | secondary | 87% → 99.2% betrouwbaarheids-case | medium |
| 5 | Anthropic — Build a tool-using agent tutorial | https://console.anthropic.com/docs/en/agents-and-tools/tool-use/build-a-tool-using-agent | primary | is_error protocol, graceful degradation | high |
| 6 | OWASP Top 10 for LLM Applications 2025 | https://owasp.org/www-project-top-10-for-large-language-model-applications/assets/PDF/OWASP-Top-10-for-LLMs-v2025.pdf | primary | LLM01, LLM06, LLM07 risico's | high |
| 7 | OpenReview — Log-To-Leak Framework | https://openreview.net/pdf/c2567f59e9e1559bede97fb86ef23287d3b3b5bd.pdf | primary | MCP tool description injection aanval | high |
| 8 | kiteworks.com — Securing LLM Apps | https://www.kiteworks.com/cybersecurity-risk-management/prompt-injection-credential-theft-ai-trust/ | secondary | audit log inhoud, SIEM integration | high |
| 9 | github.com/aden-hive — PromptInjectionShield | https://github.com/aden-hive/hive/issues/3792 | primary | PromptInjectionShield patroon | high |
| 10 | microsoft/agent-governance-toolkit | https://github.com/microsoft/agent-governance-toolkit/blob/main/docs/compliance/owasp-llm-top10-mapping.md | secondary | Merkle audit chain implementatie | high |
| 11 | AUTHENSOR — EU AI Act Compliance | https://github.com/AUTHENSOR/AUTHENSOR/blob/main/docs/eu-ai-act-compliance.md | secondary | Art. 12 vereisten, retentie | high |
| 12 | Protectron.ai | https://protectron.ai/for-agents | self-reported | Art. 12 agent logging | low |
| 13 | Difinity.ai | https://www.difinity.ai/compliance/eu-ai-act | self-reported | runtime enforcement gateway | low |
| 14 | brightlume.ai — Enterprise Tool Use | https://brightlume.ai/blog/tool-use-patterns-enterprise-ai-agents | secondary | RBAC per agent, namespace permissions | high |

## Coverage Status

- **Gecheckt direct:** Bronnen 1, 5, 6, 7, 8, 9, 10, 11 — volledig gelezen
- **Blijft onzeker:** Exacte implementatiedetails van vendor tooling (Protectron, Difinity, Agent ID) — zelfrapportage
- **Niet afgerond:** Gedetailleerde vergelijking EU AI Act vs. GDPR Art. 22 automated decision-making

## Sources

1. AI Workflow Lab — AI Agent Resilience Production Guide — https://aiworkflowlab.dev/article/ai-agent-resilience-production-retry-fallback-circuit-breaker-python
2. Enrico Piovano — Error Handling & Resilience for LLM Applications — https://enricopiovano.com/blog/llm-error-handling-resilience-production
3. AgentCenter — AI Agent Error Handling — https://agentcenter.cloud/blogs/ai-agent-error-handling-resilient-pipelines
4. Athenic — Error Handling and Reliability Patterns for Production AI Agents — https://getathenic.com/blog/error-handling-reliability-patterns-production-ai-agents
5. Anthropic — Build a tool-using agent (tutorial) — https://console.anthropic.com/docs/en/agents-and-tools/tool-use/build-a-tool-using-agent
6. OWASP — Top 10 for LLM Applications 2025 — https://owasp.org/www-project-top-10-for-large-language-model-applications/assets/PDF/OWASP-Top-10-for-LLMs-v2025.pdf
7. OpenReview — Log-To-Leak: Privacy Attacks via MCP Tool Descriptions — https://openreview.net/pdf/c2567f59e9e1559bede97fb86ef23287d3b3b5bd.pdf
8. Kiteworks — Securing LLM Apps: Prompt Injection and Credential Theft — https://www.kiteworks.com/cybersecurity-risk-management/prompt-injection-credential-theft-ai-trust/
9. aden-hive/hive — PromptInjectionShield feature — https://github.com/aden-hive/hive/issues/3792
10. microsoft/agent-governance-toolkit — OWASP mapping — https://github.com/microsoft/agent-governance-toolkit/blob/main/docs/compliance/owasp-llm-top10-mapping.md
11. AUTHENSOR — EU AI Act Compliance Documentation — https://github.com/AUTHENSOR/AUTHENSOR/blob/main/docs/eu-ai-act-compliance.md
12. Protectron.ai — EU AI Act for Agents — https://protectron.ai/for-agents
13. Difinity.ai — EU AI Act Compliance Platform — https://www.difinity.ai/compliance/eu-ai-act
14. Brightlume AI — Tool Use Patterns for Enterprise AI Agents — https://brightlume.ai/blog/tool-use-patterns-enterprise-ai-agents
