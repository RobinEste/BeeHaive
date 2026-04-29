# Provenance: Tool Integration (BB_05) — BeeHaive Building Block

**Datum:** 2026-04-29
**Skill:** /deep-research
**Primair artifact:** `final.md`

## Bronverantwoording

| # | Bron | URL | Claim | Status |
|---|------|-----|-------|--------|
| 1 | Anthropic Tool Use Docs | https://docs.anthropic.com/en/docs/tool-use | function calling mechanisme, client vs server, strict mode, pricing | verified |
| 2 | Anthropic — How tool use works | https://platform.claude.com/docs/en/agents-and-tools/tool-use/how-tool-use-works | Anthropic-schema trained-in tools | verified |
| 3 | Anthropic PTC docs | https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling | PTC, BrowseComp/DeepSearchQA prestaties | verified |
| 4 | Anthropic Computer Use | https://platform.claude.com/docs/en/docs/agents-and-tools/computer-use | Docker isolatie, screenshot-roundtrip, 735 tokens/tool | verified |
| 5 | Anthropic — Build agent tutorial | https://console.anthropic.com/docs/en/agents-and-tools/tool-use/build-a-tool-using-agent | is_error protocol, graceful degradation | verified |
| 6 | MCP Tools concept | https://modelcontextprotocol.info/docs/concepts/tools/ | MCP tools/list, tools/call, error handling | verified |
| 7 | AI Workflow Lab — Function Calling Guide | https://aiworkflowlab.dev/article/llm-tool-use-function-calling-production-basic-integration-advanced-orchestration | PTC, tool search, parallelle execution | verified |
| 8 | Brightlume AI — Enterprise Tool Use | https://brightlume.ai/blog/tool-use-patterns-enterprise-ai-agents | ReAct, namespacing, RBAC, orchestratie patronen | verified |
| 9 | Webcoderspeed — AI Agent Tool Design | https://webcoderspeed.com/blog/scaling/ai-agent-tool-design | JSON schema best practices, error messages | verified |
| 10 | Agentic Academy — MCP Deep Dive | https://agentic-academy.ai/posts/mcp-deep-dive/ | MCP transport, OAuth 2.1, OpenAI/Google/Microsoft adoptie | verified |
| 11 | AI Workflow Lab — Resilience Guide | https://aiworkflowlab.dev/article/ai-agent-resilience-production-retry-fallback-circuit-breaker-python | circuit breaker parameters, timeout tiers | verified |
| 12 | OWASP LLM Top 10 2025 | https://owasp.org/www-project-top-10-for-large-language-model-applications/assets/PDF/OWASP-Top-10-for-LLMs-v2025.pdf | LLM01, LLM06, LLM07 | verified |
| 13 | OpenReview — Log-To-Leak | https://openreview.net/pdf/c2567f59e9e1559bede97fb86ef23287d3b3b5bd.pdf | MCP tool description injection aanval | verified |
| 14 | Kiteworks — Securing LLM Apps | https://www.kiteworks.com/cybersecurity-risk-management/prompt-injection-credential-theft-ai-trust/ | audit log inhoud, executielaag | verified |
| 15 | aden-hive PromptInjectionShield | https://github.com/aden-hive/hive/issues/3792 | tool result scanning patroon | verified |
| 16 | AUTHENSOR EU AI Act | https://github.com/AUTHENSOR/AUTHENSOR/blob/main/docs/eu-ai-act-compliance.md | Art. 12/14 vereisten, deadline 2026 | verified |
| 17 | Anthropic MCP Announcement | https://www.anthropic.com/news/model-context-protocol | MCP introductie | verified |
| 18 | agnt.one — MCP for AI Agents | https://agnt.one/blog/the-model-context-protocol-for-ai-agents | 5000+ servers, adoptie | inferred |
| 19 | mcp-agent.com | https://mcp-agent.com/ | agents als MCP servers | verified |
| 20 | Iterathon — Advanced Function Calling | https://iterathon.tech/blog/advanced-function-calling-tool-composition-production-agents-2026 | 70% maintenance reduction na MCP | unverified |
| 21 | Athenic — Error Handling | https://getathenic.com/blog/error-handling-reliability-patterns-production-ai-agents | 87%→99.2% betrouwbaarheid | unverified |
| 22 | DeployBase AI Tools Directory | https://deploybase.ai/articles/ai-tools-directory | vector DB vergelijking | verified |
| 23 | DevTechInsights LangChain vs LlamaIndex | https://devtechinsights.com/langchain-vs-llamaindex-2025/ | framework vergelijking | verified |

## Verificatieoverzicht

- **Totaal bronnen geraadpleegd:** 23
- **Bronnen geaccepteerd (na URL-check):** 23
- **Bronnen verworpen:** 0 (geen dode links gevonden)

**Claim-verdeling:**
- `verified`: 19
- `inferred`: 2
- `unverified`: 2
- `blocked`: 0

## Researcher-rondes

| Ronde | Datum | # researchers | Nieuwe bronnen | Nieuwe claims |
|-------|-------|---------------|----------------|---------------|
| 1 | 2026-04-29 | 3 | 23 | ~45 |

## Externe agents

Geen externe agents gebruikt. `--with-gemini` flag niet gezet.

## Verificatie-pass

**Uitkomst:** PASS

**FATAL issues gefixt:** geen — alle kritieke claims hebben primaire bronnen
**MAJOR issues in Open Vragen:** EU AI Act high-risk applicabiliteit vereist juridische beoordeling per use case (vermeld in final.md § Open vragen)
**MINOR issues geaccepteerd:**
- 70% maintenance reduction na MCP-migratie: zelfrapportage, geen onafhankelijke validatie — gemarkeerd als `unverified`
- 87%→99.2% betrouwbaarheid: zelfrapportage, consistent met literatuur — gemarkeerd als `unverified`
- 5000+ MCP servers: secondary bron, consistent met adoptieberichtgeving — gemarkeerd als `inferred`

## Geblokkeerde verificaties

Geen volledig geblokkeerde verificaties. Twee URL-redirects verwerkt:
- `https://docs.anthropic.com/en/docs/agents-and-tools/computer-use` → redirect naar `https://platform.claude.com/docs/en/docs/agents-and-tools/computer-use` (gevolgd, content geverifieerd)

## PII-notitie

Geen bronnen met persoonlijke profielen of PII verwerkt. Alle geciteerde auteurs zijn institutionele/organisatie-namen.

## Gerelateerde bestanden

- Plan: `plan.md`
- Research files: `research-architectuur.md`, `research-beveiliging.md`, `research-ecosysteem.md`
- Reflection: `reflection-round-1.md`
- Draft: `draft.md`
- Final: `final.md`
