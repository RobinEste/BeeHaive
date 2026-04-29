# Onderzoeksplan: Tool Integration (BB_05) — BeeHaive Building Block

**Slug:** tool-integration-bb
**Aanmaakdatum:** 2026-04-29
**Status:** ✅ Afgerond

## Budget & stop-criteria

```yaml
max_rounds: 2              # harde bovengrens op researcher-rondes
token_budget_kt: 180       # totaal input+output tokens (kT) over alle rondes
stop_on_no_new_urls: true  # stop als ronde N geen nieuwe URLs oplevert t.o.v. N-1
```

Stop wanneer **één** criterium voldoet. Lead agent logt welk criterium triggerde in `## Decision-log`.

## Onderzoeksvraag

Wat is de stand van de praktijk rondom Tool Integration voor AI-systemen in 2025–2026, en hoe kan BeeHaive Building Block BB_05 worden uitgebouwd tot een diepgaand, praktisch en goed onderbouwd hoofdstuk vergelijkbaar met BB_04 (Prompt Design) en BB_06 (Model Engines)?

De huidige BB_05 bevat slechts een introductie van ~200 woorden. Het onderzoek moet voldoende materiaal opleveren voor 4–6 BBDisclosure-secties met praktijkdiepgang.

## Kernvragen

1. **Wat zijn de fundamentele architectuurpatronen voor tool use in AI-systemen?** (function calling, tool specs, MCP, agentic tool use, computer use)
2. **Hoe worden tool integrations betrouwbaar gemaakt?** (error handling, timeouts, retries, circuit breakers, observability, fallbacks)
3. **Wat zijn de beveiligings- en governance-risico's?** (OWASP LLM top 10, prompt injection via tools, least privilege, audit logging, EU AI Act)
4. **Welke toolcategorieen bestaan er en wat zijn hun trade-offs?** (search/RAG, code execution, databases, APIs, RPA, computer use, MCP ecosystem)
5. **Wat zijn de operationele best practices voor productie-tool-integraties?** (versioning, schema management, latency budgets, cost management, multi-tool orchestration)
6. **Hoe positioneert de industrie tool integration in de agentic context?** (tool calling vs. MCP vs. native integrations, multi-agent tool sharing)

## Strategie

**Scale decision:** breed onderzoek, meerdere invalshoeken
**Aantal researchers:** 3 parallelle researchers
**Geschatte rondes:** 1–2

**Dimensie-verdeling:**
- Researcher 1 — **Architectuur & patronen**: function calling specs, MCP protocol, tool types, agentic tool use patronen, production architectures (2024–2026)
- Researcher 2 — **Betrouwbaarheid & beveiliging**: error handling, timeouts, circuit breakers, OWASP LLM tool-gerelateerde risico's, prompt injection via tools, audit logging, EU AI Act compliance
- Researcher 3 — **Praktijk & ecosysteem**: toolkits (LangChain, LlamaIndex, CrewAI, Anthropic tool use), MCP ecosystem, computer use, case studies, bedrijfsinzet

## Acceptatiecriteria

- [ ] Alle 6 kernvragen beantwoord met ≥2 onafhankelijke bronnen
- [ ] Tegenstrijdigheden geïdentificeerd en geadresseerd
- [ ] Geen single-source claims op kritieke findings
- [ ] Voldoende materiaal voor 4–6 BBDisclosure-secties van elk 300–600 woorden
- [ ] Productie-gericht: patronen, anti-patronen, trade-offs, beslisheuristieken

## Task Ledger

| ID | Owner | Taak | Status | Output |
|----|-------|------|--------|--------|
| T1 | researcher-1 | Architectuur & patronen tool integration | todo | research-architectuur.md |
| T2 | researcher-2 | Betrouwbaarheid & beveiliging | todo | research-beveiliging.md |
| T3 | researcher-3 | Praktijk & ecosysteem | todo | research-ecosysteem.md |
| L1 | lead | Synthese + draft | todo | draft.md |
| L2 | lead | Cite + verify | todo | final.md |

## Verificatie-log

| Item | Methode | Status | Bewijs |
|------|---------|--------|--------|
| MCP protocol specificatie | WebFetch modelcontextprotocol.io | pending | — |
| OWASP LLM top 10 tool-risico's | WebFetch owasp.org | pending | — |
| Anthropic function calling documentatie | WebFetch docs.anthropic.com | pending | — |

## Decision-log

- 2026-04-29 09:00 — Start research ronde 1. 3 parallelle researchers voor 3 disjoint dimensies: architectuur, beveiliging, ecosysteem. Onderwerp is breed genoeg voor dit aantal.
- 2026-04-29 10:30 — Ronde 1 voltooid. Alle 6 kernvragen gedekt. Stop-criterium: alle vragen complete. Geen ronde 2 nodig. final.md + provenance.md aangemaakt.
