# Skill: Project Conventions — BeeHaive

## Wanneer relevant

Altijd geladen — bevat de project-specifieke afspraken die niet in generieke skills staan.

## Naamgevingsconventies

### Database & Models

| Type | Conventie | Voorbeeld |
|------|-----------|-----------|
| Model namen | PascalCase, enkelvoud | `KnowledgeItem` |
| Tabel namen | snake_case, meervoud | `knowledge_items` |
| Veldnamen | snake_case | `created_at` |
| Foreign keys | `{model}_id` | `building_block_id` |
| Timestamps | `{action}_at` | `created_at`, `updated_at` |
| Booleans | `is_` of `has_` prefix | `is_published` |

### Neo4j Nodes & Relationships

| Type | Conventie | Voorbeeld |
|------|-----------|-----------|
| Node labels | PascalCase, enkelvoud | `KnowledgeItem`, `BuildingBlock` |
| Relationship types | SCREAMING_SNAKE_CASE | `RELATES_TO`, `BELONGS_TO` |
| Properties | camelCase | `createdAt`, `sourceUrl` |

## Architectuur-patronen

### Frontend (Astro + React)
- Astro pagina's voor statische content (blogs, framework info)
- React islands voor interactieve componenten (auth, training portal)
- Content collections voor blogs en kennisbank artikelen

### Backend (FastAPI)
- Router → Service → Repository patroon
- Pydantic models voor request/response schemas
- Dependency injection voor database sessions

### Knowledge Graph (Neo4j)
- 7 BuildingBlock nodes (Knowledge, Client Blueprint, etc.)
- 7 Guardrail nodes (Human Agency, Robustness, etc.)
- KnowledgeItem nodes met typed relaties naar bouwstenen en guardrails

## Git & Workflow conventies

### Commit messages

- **Taal:** Nederlands
- **Format:** Conventional commits: `type: beschrijving`
- **Types:** `feat:`, `fix:`, `docs:`, `refactor:`, `style:`, `test:`, `chore:`

### Documentatie-verplichting

Bij elke wijziging checken:
- `CHANGELOG.md` — bij elke feat/fix/refactor
- `ROADMAP.md` — bij afgeronde taken

### CI/CD

- `make check` moet slagen voor push
- Conventional commit format verplicht

## Review-criteria

### Wat te checken

- Volgen nieuwe models/nodes de naamgevingsconventies?
- Zijn Neo4j queries parameterized (geen string concatenation)?
- Zijn loading/error/empty states aanwezig in frontend code?
- Volgt de commit message conventional commits + Nederlands?
- Worden persoonsgegevens niet naar externe services gestuurd zonder anonimisering?

### Wat NIET te checken

- Test bestanden mogen `assert`, `print`, en hardcoded strings gebruiken
- Config bestanden zijn uitgesloten van linting

---

## Style Guide: DO/DON'T

### Python — Neo4j Queries

**DO:**
```python
# Parameterized query - veilig tegen injection
result = session.run(
    "MATCH (k:KnowledgeItem)-[:RELATES_TO]->(b:BuildingBlock {name: $name}) RETURN k",
    name=building_block_name
)
```

**DON'T:**
```python
# String concatenation - kwetsbaar voor injection!
result = session.run(
    f"MATCH (k:KnowledgeItem)-[:RELATES_TO]->(b:BuildingBlock {{name: '{name}'}}) RETURN k"
)
```

### Python — FastAPI Endpoints

**DO:**
```python
@router.get("/knowledge-items/{item_id}")
async def get_knowledge_item(
    item_id: str,
    graph: Neo4jSession = Depends(get_graph_session),
) -> KnowledgeItemResponse:
    item = await knowledge_service.get_by_id(graph, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Knowledge item niet gevonden")
    return item
```

**DON'T:**
```python
@router.get("/knowledge-items/{item_id}")
async def get_knowledge_item(item_id):  # Geen type hints, geen dependency injection
    graph = Neo4jSession()  # Geen DI, moeilijk testbaar
    return graph.run(f"MATCH (k) WHERE k.id = '{item_id}' RETURN k")  # Onveilig!
```

---

## Review Pruning Principe

> "Would removing this rule cause Claude to make mistakes?" — Als het antwoord nee is, verwijder de regel.
> *— Anthropic Best Practices*

Agents moeten alleen findings rapporteren die de auteur **daadwerkelijk blij zou maken om te ontdekken**:

- **Rapporteer WEL:** Concrete bugs, security kwetsbaarheden, data integrity issues, ontbrekende auth, Neo4j injection
- **Rapporteer NIET:** Style preferences die de linter al afdwingt, "zou beter kunnen" suggesties, theoretische issues zonder concreet scenario
