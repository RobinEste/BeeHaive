## Prompt Design — Research Update 2026-04-03

### Samenvatting
De belangrijkste verschuiving in 2025-2026: **prompt engineering evolueert naar context engineering**. Anthropic definieert dit als het cureren van de volledige context-state (system prompts, tools, MCP, data, message history), niet alleen het schrijven van de prompt. Rolzetting is grotendeels achterhaald — modellen begrijpen context zelf. De focus verschuift naar intent, verwachtingen en kwaliteitscriteria.

### Belangrijkste bevindingen

1. **Context engineering als opvolger van prompt engineering** — Anthropic (2025-09), iBuidl (2026-03)
   - "Building with language models is becoming less about finding the right words and more about what configuration of context is most likely to generate the model's desired behavior"
   - Implicatie voor BeeHaive: de BB "Prompt Design" moet breder worden dan alleen de prompt — het gaat om het hele contextplaatje

2. **Rolzetting is achterhaald, intent is de kern** — iBuidl (2026-03), Anthropic (impliciet), BeeHaive content bevestigt dit al
   - "Elaborate persona prompts, manual chain-of-thought scaffolding for simple tasks — are now unnecessary overhead"
   - De huidige BeeHaive content beschrijft deze evolutie al correct, maar de checklist en quickStart gebruiken nog het oude "rol → context → instructies" patroon

3. **5-secties template voor production system prompts** — PE Collective (2026-02), AgentWiki (2026-03)
   - Identity & Purpose → Behavioral Rules → Response Format → Edge Cases → Examples
   - Priority stack: safety > accuracy > tone > personality

4. **Agentic prompt design is een nieuw sub-domein** — Anthropic (2025-09), PE Collective (2026-02)
   - Agent prompts zijn fundamenteel anders dan chat prompts: ontwerp voor een loop, niet een response
   - Compaction, structured note-taking en sub-agent architecturen als context management strategieën

### Statistieken & benchmarks

| Metric | Waarde | Bron | Datum | Verificatie |
|--------|--------|------|-------|-------------|
| CoT accuracy verbetering | +34% op multi-step reasoning | iBuidl Research | 2026-03 | Needs verification (single source) |
| Few-shot → structured output | 71% → 94% met 3 examples | iBuidl Research | 2026-03 | Needs verification (single source) |
| System prompt lengte drempel | >800 tokens verdunt adherentie | iBuidl Research | 2026-03 | Needs verification (single source) |
| XML vs JSON compliance | XML +11% op gemiddelde compliance | iBuidl Research | 2026-03 | Needs verification (single source) |

### Aanbevelingen voor content-update

- [ ] **Checklist bijwerken:** "rol → context → instructies → criteria → output" vervangen door intent-gebaseerd model ("doel → verwachtingen → context → criteria → output")
- [ ] **QuickStart bijwerken:** rolzetting-voorbeeld vervangen door intent-voorbeeld
- [ ] **Sectie toevoegen:** agentic prompt design — ontwerp voor loops, niet responses
- [ ] **5-secties template toevoegen:** als praktisch framework voor system prompts (Identity, Rules, Format, Edge Cases, Examples)
- [ ] **Statistieken toevoegen:** CoT +34%, few-shot 71%→94% (na verificatie met tweede bron)
- [ ] ~~Sectie context engineering~~ → verplaatst naar Dynamic Context research-run

### Open vragen

- De iBuidl statistieken (CoT +34%, few-shot 71%→94%, 800 token drempel) zijn van één bron — zoek bevestiging in een volgende run

### Afbakening met Dynamic Context

**Besluit:** Context engineering valt onder **Dynamic Context**, niet onder Prompt Design.
- **Prompt Design** = het schrijven van effectieve instructies (system prompts, few-shot, output formatting)
- **Dynamic Context** = het cureren van de volledige context-state (RAG, tools, MCP, message history, compaction)

Het Anthropic-artikel over context engineering (bron-001) is daarom ook getagd op Dynamic Context. De aanbeveling "sectie toevoegen: context engineering als evolutie" wordt verplaatst naar de Dynamic Context research-run.

### Bronnen

1. Anthropic Applied AI team (2025). Effective context engineering for AI agents. https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
2. PE Collective (2026). System Prompt Design Guide: Patterns That Work in Production. https://pecollective.com/blog/system-prompt-design-guide/
3. iBuidl Research (2026). Prompt Engineering Patterns That Actually Work in 2026. https://ibuidl.org/blog/prompt-engineering-patterns-2026-20260310
4. AgentWiki (2026). How to Structure System Prompts. https://agentwiki.org/how_to_structure_system_prompts
5. Sundeep Teki (2026). The Definitive Guide to Prompt Engineering. https://www.sundeepteki.org/advice/the-definitive-guide-to-prompt-engineering-from-principles-to-production
6. Anthropic (2026). Prompt engineering overview — Claude API Docs. https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

### Metadata

- Run: 1 (baseline)
- Tijdsvenster: 2025-04 — 2026-04
- Queries uitgevoerd: 3
- Bronnen geraadpleegd: 16 (search results)
- Bronnen geselecteerd: 6
- Bronnen gearchiveerd: 3 (bron-001, bron-002, bron-003)
- AI-assisted: ja (Claude Code + Exa + Firecrawl)
