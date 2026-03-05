"""Seed data for the BeeHaive knowledge graph.

Contains the 7 BuildingBlocks, 7 Guardrails, and 1 example KnowledgeItem
with related Topic and Author nodes.
"""

BUILDING_BLOCKS = [
    {
        "name": "Knowledge",
        "description": "Het fundament: alle kennis die het AI-systeem voedt. Documenten, transcripts, whitepapers, artikelen en interne kennisbanken worden gestructureerd opgeslagen en doorzoekbaar gemaakt.",
        "checklist": [
            "Kennisbronnen geïdentificeerd en gecategoriseerd",
            "Ingestion pipeline opgezet voor nieuwe content",
            "Knowledge graph relaties gedefinieerd",
            "Zoekfunctionaliteit geïmplementeerd",
            "Versioning en actualiteit tracking actief",
        ],
    },
    {
        "name": "Client Blueprint",
        "description": "Een gestructureerd profiel van de klant of gebruiker. Bevat context over doelen, branche, kennisniveau en voorkeuren zodat AI-output relevant en gepersonaliseerd is.",
        "checklist": [
            "Klantprofiel schema gedefinieerd",
            "Relevante contextvelden geïdentificeerd",
            "Profiel wordt meegestuurd bij AI-interacties",
            "Privacy-by-design toegepast op profieldata",
            "Profiel kan worden bijgewerkt door gebruiker",
        ],
    },
    {
        "name": "Dynamic Context",
        "description": "Real-time context die meegegeven wordt aan het AI-model. Combineert kennisbank-resultaten, klantprofiel en conversatiegeschiedenis tot een optimale prompt-context.",
        "checklist": [
            "Context window strategie bepaald",
            "RAG pipeline levert relevante chunks",
            "Klantprofiel wordt dynamisch ingeladen",
            "Conversatiegeschiedenis wordt meegenomen",
            "Context prioritering geïmplementeerd",
        ],
    },
    {
        "name": "Prompt Design",
        "description": "Gestructureerde prompt templates en chains die consistente, hoogwaardige AI-output garanderen. Bevat system prompts, few-shot examples en output formatting.",
        "checklist": [
            "System prompts gedefinieerd per use case",
            "Prompt templates zijn versioneerd",
            "Few-shot examples beschikbaar",
            "Output format specificaties aanwezig",
            "Prompt testing en evaluatie opgezet",
        ],
    },
    {
        "name": "Tool Integration",
        "description": "Externe tools en APIs die het AI-systeem kan aanroepen. Denk aan zoekfuncties, calculaties, database queries en externe services die de AI-capabilities uitbreiden.",
        "checklist": [
            "Beschikbare tools geïnventariseerd",
            "Tool schemas gedefinieerd (function calling)",
            "Error handling per tool geïmplementeerd",
            "Rate limiting en fallbacks geconfigureerd",
            "Tool gebruik wordt gelogd voor evaluatie",
        ],
    },
    {
        "name": "Model Engines",
        "description": "De AI-modellen die worden ingezet. Keuze voor het juiste model per taak (cost/quality/speed trade-off), inclusief fallback strategieën en model routing.",
        "checklist": [
            "Modellen geselecteerd per use case",
            "Cost/quality/speed afweging gedocumenteerd",
            "Fallback model geconfigureerd",
            "Model versies gepind voor reproduceerbaarheid",
            "EU data residency gewaarborgd",
        ],
    },
    {
        "name": "Evaluation Loop",
        "description": "Continue evaluatie van AI-output kwaliteit. Meet relevantie, accuraatheid en gebruikerstevredenheid. Feedback loops zorgen voor iteratieve verbetering.",
        "checklist": [
            "Evaluatiemetrieken gedefinieerd",
            "Automated evaluations opgezet",
            "Gebruikersfeedback wordt verzameld",
            "A/B testing framework beschikbaar",
            "Resultaten worden teruggekoppeld naar kennisbank",
        ],
    },
]

GUARDRAILS = [
    {
        "name": "Human Agency",
        "eu_term": "Human agency & oversight",
        "description": "Mensen behouden controle over AI-beslissingen. Het systeem ondersteunt menselijke autonomie en biedt mogelijkheden voor oversight en interventie.",
        "checklist": [
            "Gebruiker kan AI-suggesties overrulen",
            "Kritieke beslissingen vereisen menselijke goedkeuring",
            "Uitleg beschikbaar bij elke AI-output",
            "Opt-out mogelijkheid voor AI-features",
            "Escalatieprocedure naar menselijke expert",
        ],
    },
    {
        "name": "Robustness",
        "eu_term": "Technical robustness & safety",
        "description": "Het systeem is technisch robuust, veilig en betrouwbaar. Bescherming tegen fouten, aanvallen en onverwacht gedrag.",
        "checklist": [
            "Input validatie op alle AI-inputs",
            "Fallback bij model failures",
            "Rate limiting en abuse prevention",
            "Monitoring en alerting actief",
            "Disaster recovery plan aanwezig",
        ],
    },
    {
        "name": "Privacy",
        "eu_term": "Privacy & data governance",
        "description": "Persoonsgegevens en klantdata worden beschermd conform AVG/GDPR. Data minimalisatie, purpose limitation en transparante dataverwerking.",
        "checklist": [
            "Data processing inventory bijgehouden",
            "Persoonsgegevens blijven binnen EU",
            "Data minimalisatie toegepast bij LLM calls",
            "Gebruiker kan data inzien en verwijderen",
            "Privacy impact assessment uitgevoerd",
        ],
    },
    {
        "name": "Fairness",
        "eu_term": "Diversity, non-discrimination & fairness",
        "description": "AI-output is eerlijk en niet-discriminerend. Bewuste aandacht voor bias in data, modellen en output.",
        "checklist": [
            "Training data gecontroleerd op bias",
            "Output monitoring op discriminerende patronen",
            "Diverse testgroep voor evaluatie",
            "Bias mitigatie strategieën geïmplementeerd",
            "Klachtenprocedure voor unfaire output",
        ],
    },
    {
        "name": "Transparency",
        "eu_term": "Transparency",
        "description": "Het systeem is transparant over wanneer en hoe AI wordt ingezet. Gebruikers weten dat ze met AI interacteren en begrijpen de basis van beslissingen.",
        "checklist": [
            "AI-gebruik duidelijk gecommuniceerd",
            "Bronvermelding bij AI-gegenereerde content",
            "Model en versie informatie beschikbaar",
            "Uitleg van AI-redenering beschikbaar",
            "Documentatie van AI-systeem publiek toegankelijk",
        ],
    },
    {
        "name": "Well-being",
        "eu_term": "Societal & environmental well-being",
        "description": "Het systeem draagt bij aan maatschappelijk welzijn en minimaliseert negatieve impact op milieu en samenleving.",
        "checklist": [
            "Energieverbruik van AI-calls gemonitord",
            "Efficiënte modelkeuze (niet altijd het grootste model)",
            "Positieve impact op gebruikers meetbaar",
            "Geen manipulatieve patronen in AI-interactie",
            "Duurzaamheidsrapportage beschikbaar",
        ],
    },
    {
        "name": "Accountability",
        "eu_term": "Accountability",
        "description": "Duidelijke verantwoordelijkheid voor AI-beslissingen. Audit trails, logging en governance structuren zorgen voor verantwoording.",
        "checklist": [
            "Audit trail van alle AI-beslissingen",
            "Verantwoordelijke persoon aangewezen",
            "Governance structuur gedocumenteerd",
            "Periodieke review van AI-systeem",
            "Incident response procedure aanwezig",
        ],
    },
]

EXAMPLE_KNOWLEDGE_ITEM = {
    "title": "EU AI Act - Trustworthy AI Framework",
    "content": "The EU AI Act establishes a comprehensive framework for trustworthy artificial intelligence, defining requirements for high-risk AI systems and promoting human-centric AI development across the European Union.",
    "source_url": "https://digital-strategy.ec.europa.eu/en/policies/european-approach-artificial-intelligence",
    "source_type": "whitepaper",
    "is_current": True,
}

EXAMPLE_RELATIONS = {
    "building_block": "Knowledge",
    "guardrail": "Transparency",
    "topic": "Trustworthy AI",
    "author": "European Commission",
}


def seed_building_blocks(tx):
    """Create or update BuildingBlock nodes."""
    for bb in BUILDING_BLOCKS:
        tx.run(
            "MERGE (b:BuildingBlock {name: $name}) "
            "SET b.description = $description, b.checklist = $checklist",
            name=bb["name"],
            description=bb["description"],
            checklist=bb["checklist"],
        )
    return len(BUILDING_BLOCKS)


def seed_guardrails(tx):
    """Create or update Guardrail nodes."""
    for gr in GUARDRAILS:
        tx.run(
            "MERGE (g:Guardrail {name: $name}) "
            "SET g.eu_term = $eu_term, g.description = $description, "
            "g.checklist = $checklist",
            name=gr["name"],
            eu_term=gr["eu_term"],
            description=gr["description"],
            checklist=gr["checklist"],
        )
    return len(GUARDRAILS)


def seed_example_knowledge_item(tx):
    """Create the example KnowledgeItem with all relationship types."""
    ki = EXAMPLE_KNOWLEDGE_ITEM
    rel = EXAMPLE_RELATIONS

    tx.run(
        """
        MERGE (ki:KnowledgeItem {title: $title})
        SET ki.content = $content,
            ki.source_url = $source_url,
            ki.source_type = $source_type,
            ki.is_current = $is_current,
            ki.created_at = datetime()

        MERGE (t:Topic {name: $topic})
        MERGE (a:Author {name: $author})

        WITH ki, t, a
        MATCH (bb:BuildingBlock {name: $building_block})
        MATCH (gr:Guardrail {name: $guardrail})

        MERGE (ki)-[:RELATES_TO]->(bb)
        MERGE (ki)-[:ADDRESSES]->(gr)
        MERGE (ki)-[:ABOUT]->(t)
        MERGE (ki)-[:AUTHORED_BY]->(a)
        """,
        title=ki["title"],
        content=ki["content"],
        source_url=ki["source_url"],
        source_type=ki["source_type"],
        is_current=ki["is_current"],
        topic=rel["topic"],
        author=rel["author"],
        building_block=rel["building_block"],
        guardrail=rel["guardrail"],
    )
    return 3  # 1 KnowledgeItem + 1 Topic + 1 Author


def seed_all(session):
    """Run all seed functions. Idempotent via MERGE statements."""
    total = 0

    count = session.execute_write(seed_building_blocks)
    print(f"  BuildingBlocks: {count}")
    total += count

    count = session.execute_write(seed_guardrails)
    print(f"  Guardrails: {count}")
    total += count

    count = session.execute_write(seed_example_knowledge_item)
    print(f"  KnowledgeItem + Topic + Author: {count}")
    total += count

    print(f"\n  Total: {total} nodes seeded")
    return total
