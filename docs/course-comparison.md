# BeeHaive vs. Course Notebook: What We Adopted and What We Did Differently

**Context:** This document compares the BeeHaive knowledge graph implementation with the [Advanced Knowledge Graphs notebook](https://github.com/hamzafarooq/multi-agent-course/blob/main/Module_4_Knowledge_Graphs/Knowledge_Graphs/Knowledge_Graphs_Advanced_Version.ipynb) from Module 4 of the Multi-Agent Course.

BeeHaive is an AI governance knowledge framework that models 7 building blocks + 7 EU Trustworthy AI guardrails as a Neo4j graph. The course notebook builds a hotel recommendation system with Graph RAG.

---

## What We Adopted from the Course

### 1. Neo4j as the Graph Database

Both use Neo4j with the official Python driver and Docker for local development. We followed the same setup pattern: Docker Compose with persistent volumes, Bolt protocol on port 7687, and browser UI on 7474.

### 2. MERGE for Idempotent Data Seeding

The course uses `MERGE` operations (via APOC) to safely insert entities without duplicates. We adopted the same pattern — all our seed functions use `MERGE` so `make graph-seed` can be run repeatedly without side effects.

### 3. Uniqueness Constraints

The course relies on unique entity names for MERGE operations. We formalized this with explicit `CREATE CONSTRAINT IF NOT EXISTS` statements for all 5 node types (BuildingBlock, Guardrail, KnowledgeItem, Topic, Author).

### 4. Multi-Hop Relationship Traversal

The course demonstrates multi-hop queries for hotel → amenity → nearby attraction chains. We use the same pattern for our "find related items" feature: `KnowledgeItem → shared node ← other KnowledgeItem`, traversing through shared BuildingBlocks, Guardrails, or Topics.

### 5. Parameterized Queries

The course uses parameterized Cypher to prevent injection. We adopted this strictly — every query in `queries.py` uses `$parameter` syntax with no exceptions (unlike `schema.py` which uses f-strings for DDL, a deliberate and documented choice).

### 6. APOC Plugin

Both setups enable the APOC plugin. The course uses it for dynamic label assignment; we have it available for future advanced operations.

---

## What We Did Differently

### 1. No LLM-Driven Entity Extraction — Hand-Curated Schema Instead

**Course:** Uses GPT-4o with JSON mode to extract entities and relationships from unstructured text (hotel descriptions → structured triplets). The schema emerges partly from the LLM output.

**BeeHaive:** We define a fixed, hand-curated schema upfront. The 7 building blocks and 7 guardrails are domain constants from the EU AI Act framework — they don't need to be "discovered" by an LLM. Our seed data is explicit Python dictionaries, not LLM extractions.

**Why:** Our domain has a well-defined ontology. LLM extraction adds non-determinism that we don't need for structured governance frameworks. We plan to use LLM extraction later for the ingestion pipeline (Step 7), where we'll process unstructured documents into KnowledgeItems.

### 2. No Vector Embeddings (Yet) — String Search as MVP

**Course:** Uses OpenAI's `text-embedding-ada-002` to create vector embeddings, stores them in Neo4j's HNSW index, and retrieves via `db.index.vector.queryNodes()` for semantic similarity search.

**BeeHaive:** We use `toLower() CONTAINS toLower($term)` for case-insensitive substring matching, limited to 50 results. No embeddings, no vector index.

**Why:** This is a deliberate MVP choice. Our knowledge graph currently has 17 nodes — vector search adds complexity without value at this scale. We have a dedicated roadmap item (#5) for adding vector embeddings and full-text search when the graph grows beyond ~1000 items.

### 3. No LangChain — Pure Neo4j Driver

**Course:** Uses LangChain's `Neo4jVector` integration for vector retrieval and LLM chaining, plus LangChain's prompt templates for Text2Cypher.

**BeeHaive:** We use the bare `neo4j` Python driver with `session.execute_read()` and inner `_query(tx)` closures. No framework abstractions.

**Why:** LangChain adds a large dependency tree for functionality we don't need yet. Our query layer is 13 focused functions with explicit Cypher — easy to test, debug, and optimize. When we add RAG (Step 5), we'll evaluate whether LangChain or a lighter alternative makes sense.

### 4. No Text2Cypher — Template Queries Instead

**Course:** Implements a Text2Cypher pattern where natural language queries are converted to Cypher by an LLM using the graph schema as context.

**BeeHaive:** We use 13 pre-defined query functions that map directly to planned API endpoints. No dynamic Cypher generation.

**Why:** Text2Cypher is powerful but risky for production: generated queries can be slow, incorrect, or expose unintended data. Our template approach guarantees read-only, bounded, optimized queries. Each function has integration tests. For our use case (structured framework navigation + search), predefined queries cover all needs.

### 5. No `__Entity__` Base Label — Typed Nodes Only

**Course:** Applies a base `__Entity__` label to all nodes alongside type-specific labels. This enables unified vector indexing across heterogeneous types.

**BeeHaive:** Each node has only its type label (`BuildingBlock`, `Guardrail`, `KnowledgeItem`, `Topic`, `Author`). No shared base label.

**Why:** The `__Entity__` pattern is needed for cross-type vector search. Since we don't use vector indexing yet, the extra label would add complexity without benefit. If we add vector search later, we'll consider this pattern.

### 6. Cartesian Product Prevention with WITH+collect()

**Course:** Doesn't explicitly address the cartesian product problem (the hotel schema has simpler 1:N relationships that don't cause multiplicative joins).

**BeeHaive:** Our `get_item_with_relations()` fetches a KnowledgeItem with 4 different relationship types (BuildingBlocks, Guardrails, Topics, Authors). We use `WITH ki, collect(bb) AS building_blocks` between each `OPTIONAL MATCH` to prevent the cartesian product that would otherwise occur (7 × 7 × N × M intermediate rows).

**Why:** This is a real-world graph query pitfall. With 7 BuildingBlocks × 7 Guardrails already in our seed data, an unguarded query returns 49 duplicate rows instead of 1. The WITH+collect() pattern keeps it at O(n) instead of O(n^m).

### 7. Shared-Node Navigation Pattern for Related Items

**Course:** Uses direct relationship traversal for recommendations (hotel → amenity matching).

**BeeHaive:** Our `find_related_items()` uses a bidirectional shared-node pattern:
```cypher
MATCH (ki)-[:RELATES_TO|ADDRESSES|ABOUT]->(shared)<-[:RELATES_TO|ADDRESSES|ABOUT]-(other)
WHERE other <> ki
RETURN other, COUNT(DISTINCT shared) AS shared_count
ORDER BY shared_count DESC
LIMIT 25
```
This finds items sharing any combination of BuildingBlocks, Guardrails, or Topics, ranked by how many they share.

**Why:** This gives us a "more like this" feature without embeddings — purely structural similarity based on graph topology. It's efficient (single traversal, no EXISTS subqueries) and produces intuitive relevance ranking.

### 8. Strict Read-Only Query Layer

**Course:** Mixes reads and writes in the same workflow (extraction → MERGE → query → answer).

**BeeHaive:** `queries.py` contains exclusively read-only queries (MATCH/RETURN only). Writes live in `seed.py` and the future ingestion pipeline. This is an explicit architectural boundary.

**Why:** Separation of concerns. The query layer is consumed by API endpoints that should never modify data. This makes security auditing straightforward — you can verify at a glance that no query function can alter the graph.

### 9. Integration Tests Against Real Neo4j

**Course:** The notebook is interactive — you run cells and inspect output manually.

**BeeHaive:** We have 21 pytest integration tests with `@pytest.mark.integration` markers. Tests use module-scoped driver fixtures and function-scoped sessions. All tests run via `make test` against a real Neo4j instance with seed data.

**Why:** Automated testing is essential for a production codebase. Since Cypher queries can't be meaningfully unit-tested with mocks (the query semantics depend on Neo4j's engine), integration tests against a real database are the right approach.

---

## Summary Table

| Aspect | Course Notebook | BeeHaive | Reason |
|--------|----------------|----------|--------|
| Graph DB | Neo4j + Docker | Neo4j + Docker | Same ✓ |
| Driver | neo4j Python + LangChain | neo4j Python (bare) | Less dependencies |
| Schema | LLM-extracted + fixed types | Fully hand-curated | Domain is well-defined |
| Seeding | MERGE via APOC | MERGE via driver | Same pattern ✓ |
| Embeddings | OpenAI ada-002 + HNSW | None (MVP) | Not needed at current scale |
| Search | Vector similarity + Text2Cypher | toLower CONTAINS | Simpler, sufficient for now |
| Query style | Dynamic (LLM-generated Cypher) | Template (13 fixed functions) | Predictable, testable, secure |
| Base label | `__Entity__` on all nodes | Type-only labels | No vector index yet |
| Cartesian prevention | Not addressed | WITH+collect() pattern | Required for multi-relation joins |
| Related items | Direct traversal | Shared-node navigation + ranking | Structural similarity without embeddings |
| Write/read separation | Mixed | Strict separation | Security & maintainability |
| Testing | Interactive notebook | 21 automated integration tests | Production readiness |
| Frameworks | LangChain, OpenAI | None (bare driver) | Minimal dependencies |

---

## What's Coming Next

Our roadmap includes several features that will bring us closer to the course's advanced patterns:

1. **FastAPI endpoints** (#4) — REST API on top of the query layer
2. **RAG pipeline with vector embeddings** (#5) — This is where we'll add embeddings and potentially LangChain
3. **Ingestion pipeline** (#7) — LLM-driven entity extraction for new knowledge items (similar to the course's approach)
4. **Full-text search** — Replacing CONTAINS with Neo4j full-text indexes

The current implementation is a solid, tested foundation. The course's advanced patterns (embeddings, Text2Cypher, LLM extraction) are planned for later phases where they'll add real value at scale.

### Update: RAG-Anything as the RAG Foundation

After evaluating the options, we've decided to adopt **RAG-Anything** (built on LightRAG, also referenced in the course) as the foundation for our RAG pipeline and ingestion system. Key reasons:

- **Multimodal support**: We want to process YouTube videos (talks, conferences on EU AI Act) as knowledge items — not just text. RAG-Anything handles video, PDF, slides, tables, and images out-of-the-box.
- **Graph-based RAG**: LightRAG's hybrid retrieval (vector + graph traversal) aligns with our existing Neo4j knowledge graph.
- **Course alignment**: Using RAG-Anything lets us apply course concepts directly and use this project as coursework.
- **Self-hosted stack**: Everything can run on our own infrastructure (Hetzner) for EU data residency — Qwen 3.5 via vLLM for LLM, bge-m3 for embeddings, Whisper for transcription.

**Open challenge**: RAG-Anything builds its own knowledge graph schema. We need a strategy for integrating it with our hand-curated BeeHaive graph (BuildingBlocks, Guardrails, Topics, Authors).
