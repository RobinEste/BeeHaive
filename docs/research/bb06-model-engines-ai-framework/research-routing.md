# Research: Routing- en hybride architecturen — BB_06 Model Engines

**Researcher:** researcher-C
**Dimensie:** Routing-strategieën, multi-model-architecturen, frameworks
**Datum:** 2026-04-27

## Samenvatting (1 zin)

Multi-model routing reduceert kosten met 60–83% met minimaal kwaliteitsverlies, mits goed geïmplementeerd — maar voegt ook complexiteit toe die alleen gerechtvaardigd is bij voldoende volumeverzoeken.

## Bevindingen

### Routing als kostenstrategie

Meerdere bronnen bevestigen: een multi-model routing-strategie reduceert LLM-kosten met 60–70% bij minimaal kwaliteitsverlies [1, 2]. Praktijkberekening uit [3]: na semantisch cachen + routing daalt een maandrekening van $3.730 naar ~$230 (94% reductie). `unverified` (zelfgerapporteerd door blogpost, geen onafhankelijke verificatie)

Gerapporteerd: 76% van inference-verzoeken hoeft een frontier-model niet te raken; 83% kostenreductie is haalbaar zonder merkbaar kwaliteitsverlies [4]. `unverified`

### Taxonomie van routing-strategieën

**1. Directe routing (intent-based)**
- Classificeer de inkomende aanvraag op categorie en route naar model dat best past
- Vereist: accuraat upfront classifier (<50 ms) die zelf latency toevoegt
- Geschikt voor: goed gedefinieerde categorieën met duidelijk tier-verschil

**2. Cascading (sequentieel-escalerend)**
- Stuur eerst naar goedkoopste model; escaleer naar duurder model als kwaliteitsdrempel niet gehaald
- Voordeel: geen accurate classifier vooraf nodig — werkt op confidence-signaal
- Nadeel: latency-taks bij escalatie (drie model-aanroepen in een drie-tier cascade)
- ETH Zurich (Dekoninck et al., 2024/2025) bewees optimale condities voor cascading en routing formeel [5, 6]

**3. Cascade routing (gecombineerd)**
- Hybride: route voor duidelijke gevallen, cascade voor de ambigueuze middenlaag
- Theoretisch optimaler dan zuivere routing of zuivere cascading [5, 6] `verified`

**4. Ensemble/voting**
- Stuur dezelfde aanvraag naar meerdere modellen; combineer uitkomsten via voting of fusie
- Gebruik oneven aantal modellen (drie of vijf) om gelijkspel te vermijden [7]
- Wanneer: hoge-inzet-beslissingen waar een fout meer kost dan 3x de inference-prijs
- Beperking: per definitie duur; alleen rechtvaardigen bij kritische use-cases

**5. Router-R1 / RL-getrainde routers (NeurIPS 2025)**
- Router is zelf een LLM die "denk"- en "route"-acties interleaved
- Dynamisch beslissen welke sub-modellen te activeren mid-chain
- Nog geen brede productie-adoptie; staat van de kunst eind 2025 [8]

### Routing-patronen per agent-architectuur (Anthropic)

Anthropic's "Building Effective Agents" (december 2024) definieert vijf workflow-patronen [9]:
1. Prompt Chaining
2. Routing
3. Parallelisatie
4. Orchestrator-Workers
5. Evaluator-Optimizer

Praktische toepassing voor modelkeuze [10]:
- Orchestrators (planners, synthesizers) → Opus of zwaarder model
- Workers (parallel uitvoerende taken) → Sonnet of kleiner
- Informatieverzamelaars → Haiku (5–10 parallel)

### Wanneer is multi-model-architectuur het waard?

Multi-model routing is gerechtvaardigd wanneer [1, 4, 7]:
- Volume hoog genoeg is (>10.000 verzoeken/maand als ruwe drempel — `inferred`)
- Er duidelijk onderscheid is tussen eenvoudige en complexe aanvragen
- Latency-budget voldoende is voor een classifier-stap

**Wanneer het alleen complexiteit toevoegt:**
- Kleine volumes (de overhead van routing-infrastructuur is dan hoger dan de besparing)
- Homogene werklast (alle verzoeken vergelijkbaar complex)
- Gebrek aan monitoring om routing-beslissingen te valideren

### Infrastructuur en frameworks (stand april 2026)

| Platform | Type | Beschrijving |
|----------|------|-------------|
| OpenRouter | Hosted gateway | Multi-provider routing, eenvoudige API |
| Martian | Hosted | Dynamische model-selectie op basis van complexity |
| LiteLLM | Open-source | Unified API over 100+ modellen |
| Not Diamond | Hosted | Complexity-aware routing |
| Amazon Bedrock IPR | Managed | GA 2025; routing binnen Bedrock-model-catalogus |
| vLLM Semantic Router | Open-source | Inference-niveau semantic routing, 2025 |

Bron: [8] `verified`

### Anti-patronen in routing

1. **Classifier-latency valt weg**: als de classifier >50 ms kost, verdwijnt de latency-winst
2. **Cascade bij harde latency-eisen**: drie-tier cascade kan het slechts zijn (drie aanroepen) voor realtime UX
3. **Routing zonder monitoring**: je ziet pas dat de classifier drift als de kwaliteit al daalt
4. **Te vroeg hybride**: start altijd met de eenvoudigste aanpak die werkt [9]

## Evidence Table

| # | Bron | URL | Type | Key claim | Confidence |
|---|------|-----|------|-----------|------------|
| 1 | RajatAI — Choose LLM for Business 2026 | https://rajatgautam.com/blog/choose-llm-for-business/ | secondary | 60–70% kostenreductie via routing | medium |
| 2 | dev.to — Multi-Model LLM Routing | https://dev.to/elenarevicheva/multi-model-llm-routing-why-76-of-your-inference-shouldnt-touch-gpt-4-3867 | secondary | 83% cost reduction met routing | medium |
| 3 | pockit.tools — Cut LLM API Costs 90% | https://pockit.tools/blog/reduce-llm-api-costs-caching-routing-optimization-guide/ | secondary | Praktijkcalculatie: $3730 → $230/maand | low |
| 4 | dev.to — Multi-Model LLM Routing (94% reduction) | https://dev.to/elenarevicheva/multi-model-llm-routing-why-76-of-your-inference-shouldnt-touch-gpt-4-3867 | secondary | 76% verzoeken hoeven geen frontier-model | medium |
| 5 | MLIR Proceedings — Unified Routing and Cascading | https://proceedings.mlr.press/v267/dekoninck25a.html | primary | Bewijs cascade routing optimaal boven pure routing/cascading | high |
| 6 | ETH SRI Lab — Cascade Routing paper | http://www.srl.inf.ethz.ch/publications/dekoninck2024cascaderouting | primary | Theoretische optimaliteitsbewijzen routing en cascading | high |
| 7 | GrizzlyPeak — Multi-Model Router Patterns | https://www.grizzlypeaksoftware.com/library/multi-model-architectures-router-patterns-lmlktp56 | secondary | Ensemble: gebruik oneven aantal modellen | medium |
| 8 | Zylos Research — AI Agent Model Routing 2026 | https://zylos.ai/research/2026-03-02-ai-agent-model-routing | secondary | Infrastructuur-overzicht, Router-R1 NeurIPS 2025 | medium |
| 9 | Anthropic — Building Effective Agents (2024) | https://www.anthropic.com/research/building-effective-agents | primary | 5 workflow-patronen; start simpel | high |
| 10 | ReadySolutions — Sub-Agent Orchestration Patterns | https://readysolutions.ai/blog/2026-04-18-sub-agent-orchestration-patterns-claude/ | secondary | Opus voor orchestrators, Sonnet voor workers | medium |

## Coverage Status

- **Gecheckt direct:** routing-patronen bevestigd via academische papers (ETH Zurich) en praktijkbronnen
- **Blijft onzeker:** exacte kostenreductiepercentages zijn zelfgerapporteerd en contextafhankelijk
- **Niet afgerond:** LangChain Router en LlamaIndex router specifieke documentatie niet direct gecheckt

## Sources

1. RajatAI — How to Choose the Right LLM for Your Business 2026 — https://rajatgautam.com/blog/choose-llm-for-business/
2. dev.to (Elena Revicheva) — Multi-Model LLM Routing — https://dev.to/elenarevicheva/multi-model-llm-routing-why-76-of-your-inference-shouldnt-touch-gpt-4-3867
3. pockit.tools — How to Cut LLM API Costs by 90% — https://pockit.tools/blog/reduce-llm-api-costs-caching-routing-optimization-guide/
4. Tianpan.co — LLM Routing and Model Cascades — https://tianpan.co/blog/2025-11-03-llm-routing-model-cascades
5. MLIR Proceedings — A Unified Approach to Routing and Cascading for LLMs — https://proceedings.mlr.press/v267/dekoninck25a.html
6. ETH SRI Lab — Cascade Routing — http://www.srl.inf.ethz.ch/publications/dekoninck2024cascaderouting
7. GrizzlyPeak Software — Multi-Model Architectures: Router Patterns — https://www.grizzlypeaksoftware.com/library/multi-model-architectures-router-patterns-lmlktp56
8. Zylos Research — AI Agent Model Routing and Dynamic Model Selection 2026 — https://zylos.ai/research/2026-03-02-ai-agent-model-routing
9. Anthropic — Building Effective Agents — https://www.anthropic.com/research/building-effective-agents
10. ReadySolutions — Sub-Agent Orchestration Patterns Claude 2026 — https://readysolutions.ai/blog/2026-04-18-sub-agent-orchestration-patterns-claude/
