# Research: Architectuur — Dynamic Context 2024-2026

**Researcher:** researcher-architectuur
**Dimensie:** RAG 2.0, GraphRAG, agentic memory (mem0/Letta/MemGPT), hybrid retrieval, MCP context provisioning
**Datum:** 2026-04-20

## Samenvatting (1 zin)

RAG evolueert van een vaste pipeline naar een "context engine" met intelligente routing, hybrid retrieval en modulaire memory-lagen; agentic memory (met name mem0) heeft productie-rijpheid bereikt, terwijl MCP de standaard wordt voor gestructureerde context-provisioning in multi-agent systemen.

## Bevindingen

### 1. RAG 2.0 — van pipeline naar context engine

RAG evolueert fundamenteel van een vaste ophaalstrategie naar een "Context Engine" met "intelligent retrieval" als kernfunctionaliteit [1]. Kernevoluties in 2025:

**PTI-pipelines (Parse-Transform-Index)** worden enterprise-standaard — het ongestructureerde equivalent van ETL/ELT [2]:
- Format parsing (PDF, documenten via DeepDoc)
- Semantische verrijking (samenvattingen, entiteiten, vraag-generatie)
- Hybrid indexering (vector + keyword + metadata)

**TreeRAG patroon** (`inferred`): ontkoppelt ophalen in twee fasen:
1. *Search* — fijngranulaire semantische matching
2. *Retrieve* — dynamische context-assemblage op basis van hiërarchische documentsamenvatting
Adresseert direct het Lost-in-the-Middle probleem door relevante fragmenten te combineren met omringende context [2].

**Hybrid search + cross-encoder reranking** werd de standaard architectuur in 2025, met 33-47% nauwkeurigheidsverbetering afhankelijk van querycomplexiteit [1].

### 2. Contextual Retrieval — Anthropic's doorbraak

Anthropic's Contextual Retrieval (2024) verbetert RAG door 50-100 token contextuele samenvattingen te prependen aan chunks vóór indexering [3] (`verified`):

| Aanpak | Retrievalfout-reductie |
|--------|----------------------|
| Contextual Embeddings alleen | 35% (5.7% → 3.7%) |
| + BM25 hybrid | 49% (5.7% → 2.9%) |
| + Reranking | 67% (5.7% → 1.9%) |

Preprocessingkosten via prompt caching: ~$1.02 per miljoen document-tokens [3]. Aanbeveling: Voyage of Gemini embeddings + contextual BM25 + reranking + ophalen van 20 chunks.

### 3. GraphRAG — relatie-gebaseerde retrieval

Microsoft's GraphRAG (open source, GitHub) bouwt kennisgrafen waarbij entiteiten nodes zijn en relaties edges, gecombineerd met vector search [4]:

- **80% vs 50% nauwkeurigheid** voor complexe queries vergeleken met traditionele RAG [4] (`unverified` — self-reported benchmark)
- **72-83% comprehensiveness** op globale vragen [4]
- **LazyGraphRAG** (juni 2025) reduceerde indexeringskosten tot 0.1% van oorspronkelijk, maakt het praktisch bruikbaar [4]
- **Zwakheid**: 16.6% nauwkeurigheidsval voor tijdsgevoelige queries vergeleken met traditionele RAG [4]
- Indexeringskosten: 3-5× hoger dan baseline RAG; vereist domeinspecifieke tuning

**Wanneer gebruiken:** multi-hop redenering, narratieve datasets, complexe relatienetwerken. Niet voor real-time of frequente updates.

### 4. Agentic Memory — productie-rijpheid

Agentic memory systemen behandelen context als persistente, gelaagde opslag buiten het context window [5][6]:

**Mem0** (mem0ai/mem0, ~48K GitHub stars, 14M downloads, april 2026 preprint) [5][6]:
- Extractiefase identificeert saillante feiten per berichtpaar → compact opgeslagen als natural language memories
- CRUD-bewerkingen: ADD / UPDATE / DELETE / NOOP op basis van vergelijking met bestaande memories
- 49.0% op LongMemEval (temporal, multi-hop, knowledge-update scenarios) [5]
- 26% verbetering ten opzichte van OpenAI baseline; 91% lagere p95-latentie; >90% tokenkosten besparing [6]
- SOC 2 + HIPAA compliance beschikbaar; AWS koos Mem0 als exclusive memory provider voor Agent SDK [6]
- **Beperking**: passieve extractie via semantisch zoeken; geen complexe multi-strategie retrieval [5]

**Letta (voorheen MemGPT)** [5]:
- Volledig agent runtime, niet alleen memory layer
- Drie-tier memory architectuur: Core Memory (context window = RAM), Archival Memory (persistent store), Recall Memory (conversation history)
- Zelf-editerende memory: agents cureren actief wat zij onthouden
- Visual debugging via Agent Development Environment
- **Beperking**: Python-only; significante architecturele lock-in; elke memory-operatie verbruikt inference tokens

**Productie-rijpheid oordeel** (`inferred`, op basis van multiple bronnen):
- Mem0: productie-rijp voor personalisatie, CS-agents, voice agents — bewezen bij enterprise-klanten
- Letta: productie-rijp voor autonome agent-systemen die geavanceerde self-managed memory vereisen
- Combinatie van beide patronen wordt aanbevolen voor complexe systemen [5]

### 5. MCP — gestandaardiseerde context-provisioning

Model Context Protocol (Anthropic, november 2024) standaardiseert hoe AI-systemen externe data en tools integreren [7] (`verified`):

- > 5.800 community MCP-servers beschikbaar in april 2025 [7]
- MCP definieert: data-ingestie & transformatie, contextuele metadata-tagging, AI-interoperabiliteit
- Parallel tool execution en server-side agent loops (2025 spec) [7]
- **Beveiligingsproblemen**: prompt injection, tool-permissies, lookalike-tools (security rapport april 2025) [7]

Voor context-provisioning biedt MCP drie datatypes: Domain Knowledge (traditionele RAG), Tool Metadata (geïndexeerde tool-beschrijvingen tegen "choice paralysis"), Conversation State (historische interactiedata) [2].

### 6. Chunking strategieën en embedding-keuzes

Chunking heeft meer impact op systeemprestaties dan LLM-keuze of embedding model [8] (`inferred`):

**Optimale chunk-groottes** per type [8][9]:
- Algemeen: 256-512 tokens (100-200 woorden) met 20-30% overlap
- Policies/runbooks: hiërarchisch (paragraaf voor index, sectie voor generatie)
- Code/technische docs: 1.000-1.500 tokens
- Chat logs: 200-400 tokens

**Embedding-modellen** (2025):
- Voyage AI voyage-3-large: beste MTEB-resultaten, 32K token context, $0.06/M tokens (2.2× goedkoper dan OpenAI) [9]
- BAAI/bge-large-en-v1.5: open-source, lokale deployment voor regulated environments [8]
- Kritische regel: zelfde model voor indexering en querying [8]

**Agentic chunking**: AI-agent beslist dynamisch hoe documenten worden gesplitst op basis van structuur, dichtheid en content [9].

## Evidence Table

| # | Bron | URL | Type | Key claim | Confidence |
|---|------|-----|------|-----------|------------|
| 1 | RAGFlow — From RAG to Context 2025 | https://ragflow.io/blog/rag-review-2025-from-rag-to-context | secondary | RAG → context engine evolutie; hybrid search 33-47% verbetering | high |
| 2 | RAGFlow (zelfde) | idem | secondary | TreeRAG patroon; PTI pipelines; context provisioning typen | high |
| 3 | Anthropic — Contextual Retrieval | https://www.anthropic.com/news/contextual-retrieval | primary | 67% reductie retrievalfouten; $1.02/M tokens preprocessing | high |
| 4 | Microsoft GraphRAG | https://microsoft.github.io/graphrag/ en https://www.microsoft.com/en-us/research/project/graphrag/ | primary | 80% vs 50% nauwkeurigheid; LazyGraphRAG kosten | medium |
| 5 | Vectorize.io — Mem0 vs Letta 2026 | https://vectorize.io/articles/mem0-vs-letta | secondary | Productie-rijpheid vergelijking; benchmarks; use cases | high |
| 6 | Arxiv 2504.19413 — Mem0 productie-ready paper | https://arxiv.org/abs/2504.19413 | primary | 26% verbetering; 91% lagere latentie; AWS partnership | high |
| 7 | Model Context Protocol Wikipedia / spec | https://en.wikipedia.org/wiki/Model_Context_Protocol | secondary | MCP adoptie, beveiligingsproblemen | medium |
| 8 | Towards Data Science — RAG enterprise guide | https://towardsdatascience.com/grounding-your-llm-a-practical-guide-to-rag-for-enterprise-knowledge-bases/ | secondary | Chunking impact; embedding-regels; governance metrics | high |
| 9 | Weaviate — Chunking strategies for RAG | https://weaviate.io/blog/chunking-strategies-for-rag | primary | Chunk-grootte aanbevelingen; agentic chunking | high |

## Coverage Status

- **Gecheckt direct:** [1][2] RAGFlow (volledig), [3] Anthropic contextual retrieval (volledig), [5] Vectorize mem0 vs Letta (volledig), [8] Towards Data Science (volledig)
- **Niet direct gecheckt:** [4] GraphRAG benchmarks (via search; Microsoft GitHub publiek), [6] Arxiv paper (via search snippet), [9] Weaviate chunking (via search)
- **Blijft onzeker:** GraphRAG nauwkeurigheidscijfers zijn Microsoft self-reported; MCP beveiligingsstatus evolueert snel
- **Niet afgerond:** directe verificatie van Voyage AI MTEB-positie in 2026 (nieuwste modellen); MemGPT research.memgpt.ai directe fetch mislukt

## Sources

1. RAGFlow — From RAG to Context: 2025 Year-End Review — https://ragflow.io/blog/rag-review-2025-from-rag-to-context
2. (idem, meerdere bevindingen)
3. Anthropic — Contextual Retrieval — https://www.anthropic.com/news/contextual-retrieval
4. Microsoft GraphRAG — https://microsoft.github.io/graphrag/ en https://www.microsoft.com/en-us/research/project/graphrag/
5. Vectorize.io — Mem0 vs Letta (MemGPT): AI Agent Memory Compared 2026 — https://vectorize.io/articles/mem0-vs-letta
6. Arxiv — Mem0: Building Production-Ready AI Agents (april 2025) — https://arxiv.org/abs/2504.19413
7. Wikipedia — Model Context Protocol — https://en.wikipedia.org/wiki/Model_Context_Protocol
8. Towards Data Science — Grounding Your LLM: Enterprise Knowledge Bases — https://towardsdatascience.com/grounding-your-llm-a-practical-guide-to-rag-for-enterprise-knowledge-bases/
9. Weaviate — Chunking Strategies for RAG — https://weaviate.io/blog/chunking-strategies-for-rag
