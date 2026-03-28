# KNW-2026-023: Analyse Agent-Skills-for-Context-Engineering voor Dynamic Context

**Datum:** 2026-03-28
**Bron:** [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering)
**Doel:** Bepalen welke patronen en inzichten we kunnen overnemen voor BeeHaive's building block "Dynamic Context" (BB_03)

---

## 1. Samenvatting externe repo

De repo bevat 13 "Agent Skills" die context engineering principes aanleren voor productie-grade AI-systemen. Elke skill is een SKILL.md file met instructies, code-voorbeelden en referenties. Het geheel volgt een **progressive disclosure** patroon: bij initialisatie laden alleen skill-namen en -beschrijvingen; de volledige inhoud laadt pas wanneer een skill wordt geactiveerd.

De repo is academisch geciteerd (Peking University, 2026) en heeft 14.4k stars.

### Relevante skills voor Dynamic Context

| Skill | Kern | Relevantie voor BeeHaive |
|-------|------|--------------------------|
| **context-fundamentals** | Anatomie van context, plaatsing-strategie, aandachtsmechanismen | Hoog - fundamentele ontwerpprincipes |
| **context-degradation** | 5 faalpatronen (lost-in-middle, poisoning, distraction, confusion, clash) | Hoog - diagnostiek en preventie |
| **context-optimization** | KV-cache, observation masking, compaction, partitioning | Hoog - direct toepasbaar op RAG-pipeline |
| **context-compression** | 3 compressie-strategieën met kwaliteitsmetrieken | Medium - voor lange sessies |
| **memory-systems** | Framework-vergelijking (Mem0, Zep/Graphiti, Letta, Cognee, LangMem) | Medium - we hebben al Neo4j + LightRAG |
| **filesystem-context** | Filesystem als overflow voor context window | Laag - meer voor IDE-agents |
| **bdi-mental-states** | BDI cognitief model (Beliefs, Desires, Intentions) | Laag - academisch interessant, nog niet praktisch |

---

## 2. Concrete inzichten om over te nemen

### 2.1 Context Window Budget Management

**Inzicht:** Een 200K-token model begint al te degraderen rond 120-140K tokens. Effectieve capaciteit is 60-70% van de geadverteerde window size.

**Toepassing BeeHaive:**
- Onze RAG-pipeline (`backend/app/rag/engine.py`) gebruikt LightRAG met `max_tokens=2048` per LLM-call. Dit is conservatief en goed.
- **Actie:** Implementeer een token-budget tracker in de RAG query-flow die bijhoudt hoeveel tokens system prompt + retrieved chunks + user query + conversatiegeschiedenis innemen. Stel een hard maximum in op 70% van het modelmaximum.

```python
# Conceptueel - toe te voegen aan backend/app/rag/
class ContextBudget:
    def __init__(self, model_max_tokens: int):
        self.max_effective = int(model_max_tokens * 0.70)  # 70% regel
        self.allocations = {
            "system_prompt": 0,
            "retrieved_chunks": 0,
            "client_blueprint": 0,
            "conversation_history": 0,
            "user_query": 0,
        }

    def fits(self, component: str, tokens: int) -> bool:
        total = sum(self.allocations.values()) + tokens
        return total <= self.max_effective
```

### 2.2 Placement-Aware Context Strategie

**Inzicht:** Informatie aan het begin en einde van context krijgt 85-95% recall; het midden zakt naar 76-82% (U-shaped attention curve, Liu et al. 2023).

**Toepassing BeeHaive:**
- Bij het samenstellen van de RAG-context: plaats **system prompt + client blueprint** aan het begin, **user query + instructies** aan het einde.
- Retrieved chunks in het midden zijn acceptabel als ze worden voorafgegaan door structurele markers (headers, bullet points).
- **Actie:** Definieer een vaste context-volgorde in de RAG query builder:

```
1. [BEGIN] System prompt + rolverdeling
2. [BEGIN] Client Blueprint (als beschikbaar)
3. [MIDDEN] Retrieved knowledge chunks (met headers)
4. [EINDE] Conversatiegeschiedenis (laatste 3-5 turns)
5. [EINDE] User query + output instructies
```

### 2.3 Vijf Degradatiepatronen als Diagnostisch Framework

**Inzicht:** Context falen valt in 5 herkenbare patronen, elk met eigen signalen en oplossingen.

**Toepassing BeeHaive:** Bouw deze patronen in als diagnostische checks in de Evaluation Loop (BB_07):

| Patroon | Signaal | BeeHaive-mitigatie |
|---------|---------|-------------------|
| **Lost-in-middle** | Correcte data genegeerd | Placement-strategie (2.2) |
| **Context poisoning** | Verouderde kennisitems corrumperen output | `valid_until` timestamps op KnowledgeItems + periodieke invalidatie |
| **Context distraction** | Irrelevante chunks verlagen kwaliteit | Relevance threshold op RAG retrieval (cosine > 0.7) |
| **Context confusion** | Model mixt taken/instructies | Taak-isolatie per RAG query (geen multi-task context) |
| **Context clash** | Tegenstrijdige bronnen | Source priority rules in knowledge graph (recency + authority) |

### 2.4 Observation Masking voor Tool Outputs

**Inzicht:** Tool outputs consumeren 80%+ van tokens in typische agent-trajecten. Na verwerking vervangen door compacte referenties: `[Obs:{ref_id} elided. Key: {summary}]`

**Toepassing BeeHaive:**
- Wanneer we AI content generation endpoints bouwen (Stap 11 op roadmap), moeten tussenresultaten van tools (Neo4j queries, RAG retrievals) na verwerking worden gecomprimeerd.
- **Actie:** In de toekomstige agent/chat service, implementeer een `mask_observation()` functie die tool outputs boven 500 tokens vervangt door een samenvatting + referentie-ID.

### 2.5 Just-in-Time Context Loading (Progressive Disclosure)

**Inzicht:** Laad context pas wanneer het relevant is voor de huidige taak, niet van tevoren. "Stuffing everything into context is expensive and degrades attention quality."

**Toepassing BeeHaive:**
- Onze RAG-pipeline doet dit al deels (query-based retrieval). Maar het Client Blueprint en conversatiegeschiedenis worden mogelijk volledig geladen.
- **Actie:** Implementeer selectieve loading:
  - Client Blueprint: laad alleen de velden relevant voor de huidige query-categorie
  - Conversatiegeschiedenis: laad maximaal de laatste 5 turns + een gecomprimeerde samenvatting van eerdere turns
  - Knowledge chunks: maximaal 5-7 chunks per query, gesorteerd op relevantie

### 2.6 Memory Architecture Escalatiepad

**Inzicht:** Begin simpel, escaleer alleen wanneer retrieval-kwaliteit aantoonbaar degradeert:
1. **Prototype** → filesystem/JSON
2. **Scale** → vector store + metadata
3. **Complex reasoning** → knowledge graph + temporal validity
4. **Full control** → self-managing memory

**Toepassing BeeHaive:**
- Wij zitten al op stap 3 (Neo4j knowledge graph + LightRAG vector search). Dit is correct voor ons domein (multi-hop reasoning over building blocks, guardrails, topics).
- **Actie:** Overweeg temporal validity toe te voegen aan KnowledgeItems. Regulaties en best practices veranderen over tijd. Voeg `valid_from` en `valid_until` properties toe aan het Neo4j schema zodat verouderde kennis automatisch wordt uitgefilterd of gemarkeerd.

```cypher
// Uitbreiding op bestaand schema
MATCH (i:KnowledgeItem)
WHERE i.valid_until IS NOT NULL AND i.valid_until < date()
SET i.status = 'expired'
```

### 2.7 Retrieval-Strategie Hybride Aanpak

**Inzicht:** Combineer semantic (embedding similarity) + keyword + graph traversal voor beste accuracy. Zep's hybride aanpak bereikt 90% latency-reductie door alleen relevante subgraphs op te halen.

**Toepassing BeeHaive:**
- LightRAG biedt al hybride retrieval modes (`local`, `global`, `hybrid`, `naive`, `mix`).
- **Actie:** Standaardiseer op `hybrid` mode voor de RAG API. Voeg graph-aware filtering toe: als een query duidelijk over een specifieke BuildingBlock of Guardrail gaat, filter dan eerst via Neo4j relaties voordat je de vector search doet.

### 2.8 Compressie met Kwaliteitsbewaking

**Inzicht:** Anchored Iterative Summarization behoudt de hoogste kwaliteit (3.70/5.0) bij 98.6% compressie. Cruciaal: artifact trails (file paths, beslissingen, specifieke identifiers) zijn het zwakste punt bij alle compressiemethoden.

**Toepassing BeeHaive:**
- Relevant voor toekomstige chat/sessie-functionaliteit.
- **Actie:** Bij het implementeren van conversatie-compressie, gebruik anchored summarization met expliciete secties voor:
  - Sessie-intentie
  - Genoemde KnowledgeItems en BuildingBlocks (exact bewaren)
  - Genomen beslissingen
  - Volgende stappen

---

## 3. Wat we NIET overnemen (en waarom)

| Concept | Reden om niet over te nemen |
|---------|---------------------------|
| **Filesystem-based context** | Relevant voor IDE-agents (Claude Code, Cursor), niet voor onze web-API architectuur |
| **BDI Mental States** | Academisch interessant (RDF → Beliefs/Desires/Intentions), maar te complex voor huidige fase |
| **Hosted Agents / Sandboxing** | Wij draaien geen background coding agents |
| **KV-Cache optimalisatie** | Infra-level optimalisatie; relevant wanneer we self-hosted models draaien, nu niet met Gemini API |
| **Plugin/Marketplace structuur** | Hun `.claude-plugin/` en `.plugin/` structuur is specifiek voor IDE-agent ecosystemen |
| **LLM-as-Judge evaluation** | Interessant maar hoort bij Evaluation Loop (BB_07), niet bij Dynamic Context |

---

## 4. Implementatie-prioriteiten voor Dynamic Context

### Fase 1 - Quick wins (bestaande code verbeteren)

1. **Token budget tracking** in RAG query flow
2. **Placement-aware context assembly** (vaste volgorde system→blueprint→chunks→history→query)
3. **Relevance threshold** op RAG retrieval (filter chunks met lage similarity)
4. **Standaardiseer hybrid retrieval mode**

### Fase 2 - Medium-term (nieuwe functionaliteit)

5. **Temporal validity** op KnowledgeItems (`valid_from`, `valid_until`)
6. **Context degradation diagnostics** als onderdeel van Evaluation Loop
7. **Selective Client Blueprint loading** (alleen relevante velden per query-categorie)

### Fase 3 - Toekomst (bij chat/agent functionaliteit)

8. **Observation masking** voor tool outputs in agent flows
9. **Conversatie-compressie** met anchored iterative summarization
10. **Source priority rules** voor conflictresolutie bij tegenstrijdige bronnen

---

## 5. Conclusie

De Agent-Skills-for-Context-Engineering repo biedt een sterk **conceptueel framework** dat direct aansluit bij BeeHaive's Dynamic Context building block. De belangrijkste waarde zit niet in code (het zijn pseudocode-voorbeelden), maar in:

1. **De 70%-regel** voor effectieve context capaciteit
2. **Placement-aware strategie** (U-shaped attention curve)
3. **Het 5-patronen diagnostisch framework** voor context degradatie
4. **Just-in-time loading** als ontwerpprincipe
5. **Temporal validity** voor veranderende kennis

BeeHaive's bestaande architectuur (Neo4j + LightRAG + Gemini) is al een solide basis. De repo helpt ons deze basis te verfijnen met bewezen context engineering principes, met name rond budgettering, plaatsing en kwaliteitsbewaking van de context die we aan het model aanbieden.
