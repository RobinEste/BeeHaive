# Hoofdstuk 3 — Architectuur en technische ontwerpkeuzes

## 3.1 Waarom dit hoofdstuk

De use-case staat (hoofdstuk 2). Nu volgt de architectuurkeuze: workflow of agent? RAG, fine-tuning of agent-tooling? Welke tools, via welk protocol? Anthropic's eigen richtlijn — *begin met het eenvoudigste dat werkt en voeg complexiteit alleen toe als evaluatie aantoont dat het noodzakelijk is* [9] — is hier de leidraad. Het meest gemaakte ontwerp-vergrijp in deze fase: een agent architecteren waar RAG voldoet.

> *"Start with a simple prompt chain optimized with retrieval and examples before adding complexity."*
> — Anthropic, *Building Effective Agents* [9]

> *"Treat agent-computer interfaces like human-computer interface design."*
> — Anthropic, *Building Effective Agents* [9]

## 3.2 Workflow of autonome agent?

### Wat hoort hier

Twee categorieën [9, 10]:

- **Workflow** — LLM's en tools in vooraf gedefinieerde codepaden. Voorspelbaar, debugbaar, goedkoper.
- **Autonome agent** — LLM met tools in een feedbacklus. Gereserveerd voor open-ended problemen waarbij het aantal stappen vooraf onbekend is.

**Vijf composable workflow-patronen** (Anthropic) [9]:

1. **Prompt Chaining** — sequentiële stappen; latency voor nauwkeurigheid.
2. **Routing** — input classificeren naar gespecialiseerde handlers.
3. **Parallelisatie** — sectioning (deeltaken) of voting (meerdere pogingen).
4. **Orchestrator-Workers** — centrale LLM decomposeert dynamisch en delegeert.
5. **Evaluator-Optimizer** — iteratieve verfijning met aparte evaluator.

**Multi-agent: alleen wanneer.** Anthropic's eigen multi-agent research-systeem presteert 90,2% beter dan single-agent op research-evaluatie, maar verbruikt ~15× meer tokens [11]. Geschikt voor: hoge parallelisatiepotentie, taken die één contextvenster overschrijden, complexe tool-integraties. *Niet* geschikt voor: taken die gedeelde context vereisen, zware inter-agent coördinatie, de meeste coderingstaken.

**Drie kerneigenschappen** voor elke implementatie [9]:

- **Eenvoud** in agent-ontwerp.
- **Transparantie** in planningsstappen — laat zien wat het systeem denkt te doen.
- **Tool-interface design** — investeer in tools zoals je in human-computer interfaces zou doen.

### Voorbeeld — Hexant: Prompt Chaining + Routing, geen agent

**Keuze:** workflow, geen autonome agent. **Patronen:** Prompt Chaining + Routing.

Argumentatie:

- Aantal stappen is voorspelbaar: classificeren → scoren → triangulatie-check → output. Geen open-ended problemen, dus geen agent-noodzaak.
- Volume per audit (~25 transcripten van ~6 uur opname) past niet in één LLM-call → chaining noodzakelijk.
- Heterogeniteit van transcripten (technische interviews vs. management-interviews) → routing pre-stap zinvol.
- Multi-agent niet gerechtvaardigd: gedeelde HLEG-context tussen alle deeltaken; kostenfactor 15× zonder bewezen kwaliteitsvoordeel.

**Concrete chaining-stappen voor de scoring-werkstroom:**

1. **Routing** — classificeer een transcript-segment als *technisch* (ICT, security, data) of *management* (governance, beleid, cultuur). Twee verschillende rubrics worden geactiveerd.
2. **Extractie** — uitspraken classificeren naar HLEG-dimensie + sterkte (sterk-bewijs / zwak-bewijs / signaal). LLM-call met JSON-schema-output.
3. **Per-dimensie-aggregatie** — alle gemarkeerde uitspraken voor één dimensie worden gebundeld; per dimensie wordt een voorlopige score (0-10) voorgesteld, met de top-3 onderbouwende fragmenten.
4. **Validatie** — deterministische checks: minimaal 3 evidence-fragmenten per score, geen score >8 zonder ten minste 2 sterk-bewijs-fragmenten, geen score <3 zonder expliciet "ontbreekt"-evidence.

### Template — invulblok

> [INVULLEN]
>
> **Workflow of autonome agent?**
> - Keuze: ...
> - Argumentatie: ...
>
> **Gekozen patroon(en) uit Anthropic's vijf**:
> - ...
> - ...
>
> **Multi-agent overwogen?** ja/nee — bij ja, toets aan drie criteria (parallelisatie, contextvenster, tool-complexiteit) en weeg 15×-tokenkosten.
>
> **Concrete stappen** (chaining/routing/parallelisatie):
> 1. ...
> 2. ...

## 3.3 Drie architectuurlagen: kennis, specialisatie, executie

### Wat hoort hier

Op een hoger niveau zijn er drie onderscheiden lagen [13, 14]:

| Laag | Aanpak | Best voor |
|------|--------|-----------|
| Kennislaag | RAG | Frequent veranderende kennis; actuele info zonder hertraining |
| Specialisatielaag | Fine-tuning | Stabiele domeinen; hoog volume, lage latency; gedrag inbakken |
| Executielaag | Agents | Bedrijfsprocessen *uitvoeren* via tools, niet alleen antwoorden |

Hybride architecturen (RAG + fine-tuning + agents) zijn het dominante patroon in 2026. De meest gemaakte fout: een agent bouwen waar RAG voldoet.

### Voorbeeld — Hexant

**Primair: Kennislaag (RAG).** Twee retrieval-stores:

- **HLEG-rubric-store** (vector-index over Hexant's HLEG-rubric + uitleg per criterium + voorbeeldscores). Klein corpus (~50 documenten), hoge precisie nodig.
- **Transcript-store per audit** (vector-index per audit, geïsoleerd; transcripten worden niet gedeeld tussen audits — vertrouwelijkheid). Per audit ~25 transcripten.

**Secundair: geen fine-tuning.** Volume te laag (~30 audits/jaar), generieke instructie-volg-modellen + RAG zijn afdoende. Heroverwogen indien volume groeit naar >100 audits/jaar.

**Geen agent.** Geen autonome handelingen; alle output gaat via senior-auditor-review.

### Template — invulblok

> [INVULLEN]
>
> **Primaire laag**: RAG / Fine-tuning / Agents — argumentatie: ...
> **Secundaire laag** (indien hybride): ...
> **Niet gekozen** (met reden): ...

## 3.4 MCP als tooling-standaard

### Wat hoort hier

Het Model Context Protocol (MCP), geïntroduceerd door Anthropic in november 2024, is de opkomende standaard voor agent-tool-integraties [12]. Client-server-architectuur op JSON-RPC 2.0; OpenAI adopteerde MCP in maart 2025; in december 2025 vendor-neutraal via de Agentic AI Foundation. Voor agent- of tool-systemen is MCP de default.

**Beveiligingsrisico's** (april 2025-onderzoek): prompt injection, tool-permission-misbruik voor data-exfiltratie, lookalike tools die vertrouwde tools kunnen vervangen [12]. Meenemen in hoofdstuk 4 (risico).

### Voorbeeld — Hexant: drie MCP-servers, alle read-only

| Server | Bron | Rechten | Doel |
|--------|------|---------|------|
| `mcp-hleg-rubric` | HLEG-rubric-store (PostgreSQL + pgvector) | read-only | Rubric-fragmenten ophalen voor classificatie en scoring |
| `mcp-transcripts` | Transcript-store per audit (geïsoleerd) | read-only, tenant-scoped | Transcript-fragmenten ophalen, alleen binnen huidige audit-tenant |
| `mcp-historische-rapporten` | Eerdere audit-rapporten (anonymized) | read-only | Voorbeeldscores en motivaties als few-shot voor de LLM |

Geen schrijfrechten. Geen e-mail- of agenda-tools. Geen tool die de scoring kan vrijgeven aan auditklant zonder senior-auditor-review.

### Template — invulblok

> [INVULLEN]
>
> | Server | Bron | Rechten | Doel |
> |--------|------|---------|------|
> | ... | ... | read-only / write / execute | ... |
> | ... | ... | ... | ... |
>
> **MCP gekozen?** ja/nee — bij nee, motivatie: ...

## 3.5 Begin-simpel-regel: beslisvolgorde

### Wat hoort hier

1. Begin met een enkele LLM-call met retrieval en voorbeelden.
2. Workflow-patroon alleen als die LLM-call aantoonbaar tekortschiet — kies dan het eenvoudigste van de vijf patronen dat past.
3. Agent alleen als geen vast pad volstaat én het aantal stappen vooraf onbekend is.
4. Multi-agent alleen na bewijs dat single-agent op één van de drie multi-agent-criteria struikelt.

### Voorbeeld — Hexant

Stap 1 (enkele call) faalt aantoonbaar bij volume: 25 transcripten × ~30 min audio = ~150 min audio-tekst per audit, ruim boven elk contextvenster. Daarom stap 2 (chaining + routing). Stap 3 (agent) overwogen voor het *dynamisch* kiezen van extra evidence-zoekopdrachten, maar afgewezen: het is geen open-ended probleem.

### Template — invulblok

> [INVULLEN]
>
> **Bewijs voor stap omhoog** (van enkele call → workflow, of workflow → agent): ...
> **Wat we expliciet *niet* doen** en waarom: ...

## 3.6 Cross-cutting check: hoofdstuk 3 ↔ hoofdstuk 4

Architectuur en risico zijn geen gescheiden domeinen. Een architectuurkeuze legt mitigatie-ruimte vast (geen agent → geen excessive agency); een risico-eis kan een architectuurkeuze afdwingen (data-residency-eis sluit bepaalde modellen uit). Na hoofdstuk 4 wordt deze sectie heroverwogen — wijzigingen genoteerd in 3.8.

## 3.7 Checklist hoofdstuk 3

- [ ] Workflow- of agent-keuze expliciet, met argumentatie.
- [ ] Gekozen patroon herleidbaar naar Anthropic's vijf.
- [ ] Multi-agent: niet gekozen tenzij alle drie criteria zijn getoetst en 15×-tokenkost expliciet aanvaard.
- [ ] Architectuurlaag (RAG / fine-tuning / agents) onderbouwd; niet-gekozen lagen expliciet vermeld met reden.
- [ ] Tools-tabel met protocol, rechten en doel per integratie; MCP overwogen, afwijking onderbouwd.
- [ ] Begin-simpel-regel zichtbaar gevolgd: bewijs voor elke complexiteits-stap.
- [ ] Drie kerneigenschappen (eenvoud, transparantie, tool-interface-design) zijn ontwerp-input, niet decoratie.

## 3.8 Literatuur (kerncitaten dit hoofdstuk)

- Anthropic, *Building Effective Agents* (research) [9].
- Anthropic Resources, *Building Effective AI Agents: Architecture Patterns* [10].
- Anthropic Engineering, *How We Built Our Multi-Agent Research System* [11].
- Anthropic, *Introducing the Model Context Protocol* [12].
- Orq.ai, *RAG Architecture Explained* [13].
- Techment, *RAG vs Fine-Tuning vs AI Agents* [14].

## 3.9 Status / laatste herziening

- Versie: 1.0
- Laatst bijgewerkt: 2026-04-28
- Wijzigingen sinds vorige versie: eerste vastlegging.
