"""Seed data for the BeeHaive knowledge graph.

Contains the 7 BuildingBlocks, 7 Guardrails, and 47 KnowledgeItems
with related Topics and Author nodes sourced from the BeeHaive
Notion knowledge base.
"""

from app.models.schemas import DEFAULT_DISPLAY_ORDER

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

# Backwards-compatible aliases for tests
EXAMPLE_KNOWLEDGE_ITEM = {
    "title": "EU AI Act - Trustworthy AI Framework",
    "content": "The EU AI Act establishes a comprehensive framework for trustworthy artificial intelligence, defining requirements for high-risk AI systems and promoting human-centric AI development across the European Union.",
    "source_url": "https://digital-strategy.ec.europa.eu/en/policies/european-approach-artificial-intelligence",
    "source_type": "regulation",
    "is_current": True,
}
EXAMPLE_RELATIONS = {
    "building_block": "Knowledge",
    "guardrail": "Transparency",
    "topic": "Trustworthy AI",
    "author": "European Commission",
}

KNOWLEDGE_ITEMS = [
    # --- Regulation & Policy ---
    {
        "title": "EU AI Act - Trustworthy AI Framework",
        "content": "The EU AI Act establishes a comprehensive framework for trustworthy artificial intelligence, defining requirements for high-risk AI systems and promoting human-centric AI development across the European Union.",
        "summary_nl": "De EU AI Act is het eerste brede wettelijke kader voor betrouwbare AI. Het classificeert AI-systemen op risico, stelt harde eisen aan hoog-risico toepassingen en legt de basis voor menswaardige inzet van AI in Europa.",
        "curation_score": 10,
        "source_url": "https://digital-strategy.ec.europa.eu/en/policies/european-approach-artificial-intelligence",
        "source_type": "regulation",
        "is_current": True,
        "building_blocks": ["Knowledge"],
        "guardrails": ["Transparency", "Accountability"],
        "topics": ["Trustworthy AI", "EU AI Act"],
        "authors": ["European Commission"],
    },
    {
        "title": "Ethics Guidelines for Trustworthy AI (HLEG)",
        "content": "The High-Level Expert Group on AI defines seven key requirements for trustworthy AI: human agency and oversight, technical robustness and safety, privacy and data governance, transparency, diversity/non-discrimination/fairness, societal and environmental well-being, and accountability.",
        "summary_nl": "De High-Level Expert Group definieert zeven kernvereisten voor betrouwbare AI — menselijke controle, robuustheid, privacy, transparantie, diversiteit, welzijn en verantwoording. De directe bron voor de zeven guardrails die BeeHaive hanteert.",
        "curation_score": 9,
        "source_url": "https://digital-strategy.ec.europa.eu/en/library/ethics-guidelines-trustworthy-ai",
        "source_type": "regulation",
        "is_current": True,
        "building_blocks": ["Knowledge", "Evaluation Loop"],
        "guardrails": ["Human Agency", "Accountability", "Transparency"],
        "topics": ["Trustworthy AI", "AI Ethics"],
        "authors": ["European Commission HLEG"],
    },
    {
        "title": "ALTAI - Assessment List for Trustworthy AI",
        "content": "The ALTAI is a practical checklist tool for organisations to self-assess the trustworthiness of their AI systems under development. It operationalises the seven requirements of the Ethics Guidelines into concrete assessment questions.",
        "summary_nl": "Een praktische self-assessment checklist waarmee organisaties hun AI-systemen kunnen toetsen tegen de zeven kernvereisten. Maakt de abstracte HLEG-richtlijnen concreet en toepasbaar voor audit en governance.",
        "curation_score": 8,
        "source_url": "https://digital-strategy.ec.europa.eu/en/library/assessment-list-trustworthy-artificial-intelligence-altai-self-assessment",
        "source_type": "regulation",
        "is_current": True,
        "building_blocks": ["Evaluation Loop", "Knowledge"],
        "guardrails": ["Accountability", "Human Agency"],
        "topics": ["AI Assessment", "Trustworthy AI"],
        "authors": ["European Commission HLEG"],
    },
    # --- Prompt Design ---
    {
        "title": "Lakera.ai Ultimate Guide to Prompt Engineering 2025",
        "content": "Comprehensive guide covering advanced prompt engineering techniques with strong emphasis on safety and enterprise applications. Includes adversarial attack prevention, bias detection, evaluation frameworks, and systematic prompt structuring from basics to advanced.",
        "summary_nl": "Brede gids voor prompt engineering met sterke focus op enterprise-veiligheid: adversarial attack-preventie, bias-detectie, evaluatiekaders en systematische promptstructurering. Praktisch startpunt voor teams die prompts productierijp willen maken.",
        "curation_score": 9,
        "source_url": "https://www.lakera.ai/blog/prompt-engineering-guide",
        "source_type": "guideline",
        "is_current": True,
        "building_blocks": ["Prompt Design"],
        "guardrails": ["Robustness", "Transparency"],
        "topics": ["Prompt Engineering", "AI Safety"],
        "authors": ["Lakera AI"],
    },
    {
        "title": "PARTS Framework for Educational AI Prompting",
        "content": "Scientific research introducing the PARTS framework (Persona, Aim, Recipients, Theme, Structure) for designing educational AI prompts. Demonstrates how systematic prompt structuring with rubrics and exemplars significantly improves AI feedback quality.",
        "summary_nl": "Wetenschappelijk onderzoek dat het PARTS-framework introduceert (Persona, Aim, Recipients, Theme, Structure) voor educatieve AI-prompts. Laat zien dat systematische prompt-structuur met rubrics en voorbeelden de kwaliteit van AI-feedback aantoonbaar verbetert.",
        "curation_score": 5,
        "source_url": "https://www.tandfonline.com/doi/full/10.1080/00405841.2025.2528545",
        "source_type": "paper",
        "is_current": True,
        "building_blocks": ["Prompt Design", "Knowledge"],
        "guardrails": ["Fairness", "Transparency"],
        "topics": ["Prompt Engineering", "AI in Education"],
        "authors": ["Taylor & Francis"],
    },
    {
        "title": "Anthropic Constitutional AI Methodology",
        "content": "Technical guide on implementing Constitutional AI — a method where AI models use a set of ethical principles (a 'constitution') to self-evaluate and improve their outputs. Covers self-critique mechanisms, two-phase training, and natural language constitutions for responsible AI.",
        "summary_nl": "Methodologie waarin een AI-model een expliciete 'grondwet' van ethische principes gebruikt om zijn eigen output te beoordelen en verbeteren. Beschrijft self-critique, twee-fasen-training en hoe natuurlijke taal-constituties verantwoorde AI operationaliseren.",
        "curation_score": 7,
        "source_url": "https://www.anthropic.com/constitutional-ai",
        "source_type": "guideline",
        "is_current": True,
        "building_blocks": ["Prompt Design", "Evaluation Loop"],
        "guardrails": ["Human Agency", "Accountability", "Fairness"],
        "topics": ["Constitutional AI", "AI Ethics"],
        "authors": ["Anthropic"],
    },
    {
        "title": "IBM Prompt Engineering Best Practices 2025",
        "content": "Enterprise guide for systematic prompt engineering implementation. Covers progressive disclosure methodology, prompt lifecycle management (design-test-deploy-monitor), version control for prompts, governance structures, compliance monitoring, and scalability strategies.",
        "summary_nl": "Enterprise-gids voor het professionaliseren van prompt engineering: lifecycle-management (design→test→deploy→monitor), versiebeheer, governance en compliance-monitoring. Behandelt prompts als productie-artefact in plaats van losse tekststring.",
        "curation_score": 8,
        "source_url": "https://www.ibm.com/think/prompt-engineering",
        "source_type": "guideline",
        "is_current": True,
        "building_blocks": ["Prompt Design"],
        "guardrails": ["Accountability", "Robustness"],
        "topics": ["Prompt Engineering", "Enterprise AI"],
        "authors": ["IBM"],
    },
    {
        "title": "Prompt Engineering for Generative AI (O'Reilly)",
        "content": "Comprehensive handbook covering prompt engineering from theory to practice for GPT-4, Gemini, and Claude. Includes NLP fundamentals, multimodal prompting, code generation, token optimization, context management, few-shot learning, and fine-tuning vs prompting trade-offs.",
        "summary_nl": "Handboek dat prompt engineering breed behandelt — van NLP-fundamenten tot multimodaal prompten, codegeneratie, tokenoptimalisatie en de keuze tussen prompting en fine-tuning. Geschikt als naslagwerk over model- en promptgedrag heen.",
        "curation_score": 7,
        "source_url": "https://www.oreilly.com/library/view/prompt-engineering-for/9781098153427/",
        "source_type": "guideline",
        "is_current": True,
        "building_blocks": ["Prompt Design", "Model Engines"],
        "guardrails": ["Transparency", "Robustness"],
        "topics": ["Prompt Engineering"],
        "authors": ["O'Reilly Media"],
    },
    # --- Dynamic Context & RAG ---
    {
        "title": "DataNucleus Enterprise RAG Guide 2025",
        "content": "Enterprise guide for Retrieval Augmented Generation covering hybrid search (lexical + vector), reranking with cross-encoders, security trimming for document-level access control, metadata enrichment, grounding with citations, and continuous update strategies for dynamic knowledge bases.",
        "summary_nl": "Compleet enterprise-kader voor RAG: hybrid search (lexicaal + vector), cross-encoder reranking, security trimming op documentniveau, metadata-verrijking, citaten-grounding en update-strategieën voor dynamische kennisbanken. Moet-lezen voor context-architecten.",
        "curation_score": 9,
        "source_url": "https://datanucleus.dev/rag-and-agentic-ai/what-is-rag-enterprise-guide-2025",
        "source_type": "guideline",
        "is_current": True,
        "building_blocks": ["Dynamic Context"],
        "guardrails": ["Privacy", "Accountability"],
        "topics": ["RAG", "Enterprise AI"],
        "authors": ["DataNucleus"],
    },
    {
        "title": "DataCamp Context Engineering Guide",
        "content": "Technical guide introducing context engineering as the evolution beyond prompt engineering. Covers conversational workflows with context retention, memory-building techniques for stateful AI, agentic RAG patterns, multi-agent systems with context retention, and context poisoning prevention.",
        "summary_nl": "Introductie van context engineering als volgende stap na prompt engineering: context-retentie in conversaties, memory-opbouw voor stateful AI, agentic RAG-patronen en bescherming tegen context-poisoning. Goed startpunt voor het conceptuele onderscheid.",
        "curation_score": 7,
        "source_url": "https://www.datacamp.com/blog/context-engineering",
        "source_type": "guideline",
        "is_current": True,
        "building_blocks": ["Dynamic Context"],
        "guardrails": ["Transparency", "Robustness"],
        "topics": ["Context Engineering", "RAG"],
        "authors": ["DataCamp"],
    },
    {
        "title": "Dynamic Context Tuning Research (2025)",
        "content": "Research introducing Dynamic Context Tuning (DCT) combining attention-based context caching, LoRA-based retrieval for dynamic tool selection, and efficient context compression. Shows how agentic retrieval patterns use conversation history as context-aware input with parallel subquery execution.",
        "summary_nl": "Onderzoek naar Dynamic Context Tuning: attention-based context-caching, LoRA-gebaseerde retrieval voor tool-selectie en efficiënte context-compressie. Laat zien hoe agentic retrieval conversatiegeschiedenis gebruikt met parallelle subquery-uitvoering.",
        "curation_score": 6,
        "source_url": "https://arxiv.org/html/2506.11092v1",
        "source_type": "paper",
        "is_current": True,
        "building_blocks": ["Dynamic Context", "Model Engines"],
        "guardrails": ["Robustness"],
        "topics": ["Context Engineering", "AI Research"],
        "authors": ["arXiv Research"],
    },
    {
        "title": "EdenAI 2025 RAG Guide — Graph RAG and Self-RAG",
        "content": "Comprehensive overview of 2025 RAG innovations including Graph RAG integrating knowledge graphs for coherent responses, Golden-Retriever frameworks with reflection-based query augmentation, Self-RAG where models autonomously decide when retrieval is needed, and hybrid architectures.",
        "summary_nl": "Overzicht van de RAG-innovaties in 2025: Graph RAG met kennisgraph-integratie, Golden-Retriever met reflectie-gebaseerde query-augmentatie en Self-RAG waarin het model zelf bepaalt of retrieval nodig is. Bruikbaar om architectuurkeuzes te framen.",
        "curation_score": 6,
        "source_url": "https://www.edenai.co/post/the-2025-guide-to-retrieval-augmented-generation-rag",
        "source_type": "guideline",
        "is_current": True,
        "building_blocks": ["Dynamic Context"],
        "guardrails": ["Transparency"],
        "topics": ["Graph RAG", "RAG"],
        "authors": ["EdenAI"],
    },
    {
        "title": "Dynamic Knowledge Graphs Research (2025)",
        "content": "Peer-reviewed research on Dynamic Knowledge Graphs (DKGs) supporting continuous knowledge updates for temporal context management. Covers temporal relationship modeling, event-driven updates, time-aware reasoning, dynamic entity resolution, and predictive relationship modeling.",
        "summary_nl": "Peer-reviewed onderzoek naar Dynamic Knowledge Graphs die continue kennisupdates en temporele context ondersteunen. Behandelt temporele relatiemodellering, event-driven updates, time-aware reasoning en voorspellende relatiemodellen.",
        "curation_score": 5,
        "source_url": "https://arxiv.org/html/2310.04835v3",
        "source_type": "paper",
        "is_current": True,
        "building_blocks": ["Dynamic Context"],
        "guardrails": ["Transparency", "Accountability"],
        "topics": ["Knowledge Graphs", "AI Research"],
        "authors": ["arXiv Research"],
    },
    {
        "title": "Graph-Based Memory for Dynamic Context Management (Stanford)",
        "content": "Stanford research on graph-based memory systems for language models. Covers evolving semantic links, temporal knowledge graph integration, adaptive memory architectures, memory consolidation strategies, forgetting mechanisms, and context retrieval optimization using graph neural networks.",
        "summary_nl": "Stanford-onderzoek naar graph-based memory voor taalmodellen: evoluerende semantische links, temporele kennisgraph-integratie, adaptieve geheugen-architecturen en vergeetmechanismen. Theoretisch fundament voor stateful agent-geheugen.",
        "curation_score": 5,
        "source_url": "https://cs224r.stanford.edu/projects/pdfs/224r_final_project_report.pdf",
        "source_type": "paper",
        "is_current": True,
        "building_blocks": ["Dynamic Context"],
        "guardrails": ["Robustness"],
        "topics": ["Graph Memory", "Knowledge Graphs"],
        "authors": ["Stanford University"],
    },
    {
        "title": "Squirro Enterprise RAG Implementations",
        "content": "Enterprise case studies showing measurable RAG impact: European Bank saving €20M in 3 years through automated compliance, LinkedIn achieving 28.6% faster issue resolution, and Deutsche Telekom realizing 14% improvement in customer recommendations. Includes implementation timelines and ROI calculations.",
        "summary_nl": "Enterprise-casestudy's met meetbare RAG-impact: €20M besparing bij een Europese bank, 28,6% snellere issue-resolutie bij LinkedIn, 14% betere aanbevelingen bij Deutsche Telekom. Inclusief implementatie-tijdlijnen en ROI-berekeningen — nuttig voor business case-materiaal.",
        "curation_score": 4,
        "source_url": "https://www.compuvate.com/how-retrieval-augmented-generation-rag-systems-transform-enterprise-knowledge-management-in-2025/",
        "source_type": "best_practice",
        "is_current": True,
        "building_blocks": ["Dynamic Context"],
        "guardrails": ["Well-being", "Accountability"],
        "topics": ["Enterprise RAG", "AI ROI"],
        "authors": ["Compuvate"],
    },
    # --- Model Engines ---
    {
        "title": "Why Language Models Hallucinate (OpenAI)",
        "content": "OpenAI research analyzing the root causes of LLM hallucinations, distinguishing between training data gaps, reasoning failures, and confidence calibration issues. Provides insights into mitigation strategies including grounding, verification chains, and uncertainty quantification.",
        "summary_nl": "OpenAI-onderzoek naar de oorzaken van hallucinaties: gaten in trainingsdata, redeneerfouten en slecht gekalibreerd vertrouwen. Beschrijft mitigatie via grounding, verificatieketens en onzekerheidskwantificatie — essentieel om modelgedrag te begrijpen.",
        "curation_score": 9,
        "source_url": "https://openai.com/research/language-models-hallucinate",
        "source_type": "paper",
        "is_current": True,
        "building_blocks": ["Model Engines"],
        "guardrails": ["Accountability", "Transparency"],
        "topics": ["LLM Hallucinations", "AI Research"],
        "authors": ["OpenAI"],
    },
    # --- Tool Integration ---
    {
        "title": "Microsoft PyRIT — Python Risk Identification Toolkit",
        "content": "Open source toolkit for systematic AI safety testing. Provides automated red-teaming with thousands of adversarial prompts, bias detection across demographic groups, compliance reporting for EU AI Act, pre-built attack scenarios (prompt injection, jailbreaking, data extraction), and CI/CD integration.",
        "summary_nl": "Open-source toolkit voor systematisch AI-safety testen: geautomatiseerd red-teaming met duizenden adversarial prompts, bias-detectie, EU AI Act compliance-rapportage en kant-en-klare aanvalsscenario's (prompt injection, jailbreaking). CI/CD-integreerbaar.",
        "curation_score": 8,
        "source_url": "https://github.com/Azure/PyRIT",
        "source_type": "best_practice",
        "is_current": True,
        "building_blocks": ["Tool Integration", "Evaluation Loop"],
        "guardrails": ["Robustness", "Fairness"],
        "topics": ["AI Safety", "Red Teaming"],
        "authors": ["Microsoft"],
    },
    {
        "title": "Building AI Agents Safely: PII, Jailbreaks, and Real Guardrails",
        "content": "Practical guide on securing AI agents in production covering PII detection and prevention, jailbreak mitigation techniques, implementing real guardrails using the Guardrails AI framework, and protecting customer-facing chatbots and agents across industries.",
        "summary_nl": "Praktische gids om AI-agents veilig in productie te brengen: PII-detectie, jailbreak-mitigatie, concrete guardrails via het Guardrails AI-framework en bescherming van klantgerichte chatbots. Focus op operationele controles in plaats van theorie.",
        "curation_score": 7,
        "source_url": "https://jettro.dev/building-ai-agents-safely-pii-jailbreaks-and-real-guardrails-a52245a5c624",
        "source_type": "guideline",
        "is_current": True,
        "building_blocks": ["Tool Integration", "Prompt Design"],
        "guardrails": ["Privacy", "Robustness"],
        "topics": ["AI Safety", "AI Agents"],
        "authors": ["Jettro Coenradie"],
    },
    # --- Evaluation Loop ---
    {
        "title": "LangSmith — Prompt Development Lifecycle Platform",
        "content": "Professional platform for developing, testing and monitoring prompts in production. Provides version control for prompts, A/B testing for variant comparison, real-time performance monitoring, collaborative workflows, automated evaluation with custom metrics, and full AI workflow tracing.",
        "summary_nl": "Professioneel platform voor de prompt-lifecycle: versiebeheer, A/B-testing, real-time monitoring, geautomatiseerde evaluatie met custom metrics en end-to-end AI-workflow tracing. Brug tussen prompt-ontwikkeling en productie-observability.",
        "curation_score": 9,
        "source_url": "https://smith.langchain.com/",
        "source_type": "best_practice",
        "is_current": True,
        "building_blocks": ["Evaluation Loop", "Tool Integration"],
        "guardrails": ["Accountability", "Robustness"],
        "topics": ["AI Development Tools", "AI Monitoring"],
        "authors": ["LangChain"],
    },
    # --- Knowledge Graph Tools ---
    {
        "title": "Qdrant — Privacy-First Vector Database",
        "content": "Open source, self-hosted vector database prioritizing data sovereignty. Features advanced payload filtering, multi-vector support, distributed clustering, GDPR-compliant data handling, quantization for storage efficiency, fine-grained access controls, audit logging, and EU data residency guarantees.",
        "summary_nl": "Open-source, self-hosted vectordatabase met focus op datasoevereiniteit: payload-filtering, multi-vector support, AVG-conforme dataverwerking, fine-grained toegangscontrole en EU data residency. Directe keuze voor Europese RAG-implementaties.",
        "curation_score": 6,
        "source_url": "https://qdrant.tech/",
        "source_type": "best_practice",
        "is_current": True,
        "building_blocks": ["Dynamic Context", "Tool Integration"],
        "guardrails": ["Privacy"],
        "topics": ["Vector Databases", "Data Sovereignty"],
        "authors": ["Qdrant"],
    },
    # --- Client Blueprint ---
    {
        "title": "Hyacinth AI: 8 Essential Steps of AI Solution Design",
        "content": "Structured methodology for designing AI solutions covering problem framing, data assessment, architecture selection, prototype development, evaluation criteria definition, deployment planning, monitoring setup, and continuous improvement loops.",
        "summary_nl": "Gestructureerde methodologie voor het ontwerpen van AI-oplossingen: probleemafbakening, data-assessment, architectuurkeuze, prototyping, evaluatiecriteria, deployment en verbeterloops. Compact raamwerk voor de blueprint-fase van een project.",
        "curation_score": 9,
        "source_url": "https://hyacinth.ai/8-essential-steps-of-ai-solution-design/",
        "source_type": "guideline",
        "is_current": True,
        "building_blocks": ["Client Blueprint"],
        "guardrails": ["Accountability"],
        "topics": ["AI Solution Design"],
        "authors": ["Hyacinth AI"],
    },
    {
        "title": "Sparkco AI-Validated Templates Enterprise Blueprint 2025",
        "content": "Enterprise blueprint templates validated by AI for component identification checklists, stakeholder review processes, value proposition assessment, and implementation decision frameworks (buy vs. build). Provides ready-to-use templates for AI solution design and deployment.",
        "summary_nl": "Kant-en-klare enterprise-blueprint templates voor component-identificatie, stakeholder-review, value proposition en buy-vs-build beslissingen. Versnelt het opzetten van een gestructureerd klantvoorstel zonder vanaf nul te beginnen.",
        "curation_score": 8,
        "source_url": "https://sparkco.ai/blog/ai-validated-templates-enterprise-blueprint-2025",
        "source_type": "best_practice",
        "is_current": True,
        "building_blocks": ["Client Blueprint", "Tool Integration"],
        "guardrails": ["Accountability", "Transparency"],
        "topics": ["Enterprise AI", "AI Solution Design"],
        "authors": ["Sparkco AI"],
    },
    # --- Cross-cutting ---
    {
        "title": "Microsoft Azure Search RAG Overview",
        "content": "Official Microsoft guide for production-ready RAG on Azure covering document processing pipelines, embedding generation strategies, hybrid search implementations (lexical + semantic), semantic ranking, security integration with Azure AD, monitoring and analytics for production systems.",
        "summary_nl": "Officiële Microsoft-gids voor productierijpe RAG op Azure: documentverwerking, embeddings, hybrid search, semantic ranking, Azure AD-integratie en monitoring. Concrete referentie voor teams die binnen het Microsoft-ecosysteem werken.",
        "curation_score": 7,
        "source_url": "https://learn.microsoft.com/en-us/azure/search/retrieval-augmented-generation-overview",
        "source_type": "guideline",
        "is_current": True,
        "building_blocks": ["Dynamic Context", "Tool Integration"],
        "guardrails": ["Robustness", "Privacy"],
        "topics": ["RAG", "Cloud AI"],
        "authors": ["Microsoft"],
    },
    {
        "title": "O'Reilly Radar: Context Engineering with Drew Breunig",
        "content": "Expert podcast with Context Engineering Handbook author Drew Breunig discussing practical context engineering in enterprise environments, subject-matter expertise importance, common implementation challenges, organizational change requirements, human-AI collaboration, and quality assurance at scale.",
        "summary_nl": "Expertgesprek met Drew Breunig over context engineering in de praktijk: het belang van domeinexpertise, implementatieobstakels, organisatieverandering en mens-AI samenwerking op schaal. Strategische inzichten die de verbinding leggen tussen Knowledge en Dynamic Context.",
        "curation_score": 8,
        "source_url": "https://www.oreilly.com/radar/podcast/generative-ai-in-the-real-world-context-engineering-with-drew-breunig/",
        "source_type": "guideline",
        "is_current": True,
        "building_blocks": ["Dynamic Context", "Knowledge"],
        "guardrails": ["Transparency", "Human Agency"],
        "topics": ["Context Engineering"],
        "authors": ["O'Reilly Media", "Drew Breunig"],
    },
    # --- Recent Papers (March 2026) ---
    {
        "title": "AgentIR: Reasoning-Aware Retrieval for Deep Research Agents",
        "content": "Introduces a reasoning-aware retrieval paradigm for AI research agents that jointly embeds reasoning traces alongside search queries. The AgentIR-4B model achieves 68% accuracy on BrowseComp-Plus with open-weight agents, compared to 50% with conventional embedding models twice its size. Includes DR-Synth for generating training data from standard QA datasets.",
        "summary_nl": "Onderzoekspaper die reasoning-aware retrieval introduceert voor research-agents: redeneersporen worden samen met zoekqueries geëmbed. AgentIR-4B haalt 68% accuracy op BrowseComp-Plus — bijna 20 punten beter dan tweemaal zo grote conventionele modellen.",
        "curation_score": 5,
        "source_url": "https://arxiv.org/abs/2603.04384",
        "source_type": "paper",
        "is_current": True,
        "building_blocks": ["Dynamic Context"],
        "guardrails": ["Transparency", "Robustness"],
        "topics": ["AI Agents", "RAG", "AI Research"],
        "authors": ["Zijian Chen", "Akari Asai"],
    },
    {
        "title": "τ-Knowledge: Evaluating Conversational Agents over Unstructured Knowledge",
        "content": "Benchmarking framework for assessing conversational agents in knowledge-intensive settings with large unstructured document collections. Introduces τ-Banking (fintech customer support with ~700 interconnected documents). Even advanced models achieve only 25.5% success rates, revealing challenges in document retrieval from densely linked knowledge bases.",
        "summary_nl": "Benchmark voor conversationele agents op grote ongestructureerde documentcollecties. τ-Banking simuleert fintech-support met ~700 onderling verbonden documenten — zelfs toonaangevende modellen halen slechts 25,5% succesratio. Toont hoe zwaar retrieval in dichte kennisgrafen is.",
        "curation_score": 5,
        "source_url": "https://arxiv.org/abs/2603.04370",
        "source_type": "paper",
        "is_current": True,
        "building_blocks": ["Evaluation Loop", "Dynamic Context"],
        "guardrails": ["Accountability", "Robustness"],
        "topics": ["AI Evaluation", "Conversational AI"],
        "authors": ["Quan Shi", "Karthik Narasimhan"],
    },
    {
        "title": "Robustness of Agentic AI via Adversarially-Aligned Jacobian Regularization",
        "content": "Proposes AAJR for robust training of autonomous multi-agent LLM systems. Controls model sensitivity along adversarial directions rather than globally, permitting a larger class of policies while reducing performance loss. Establishes theoretical conditions for training stability and decouples robustness from expressivity limitations.",
        "summary_nl": "Onderzoek naar robuuste training van multi-agent LLM-systemen via Adversarially-Aligned Jacobian Regularization. Stuurt gevoeligheid gericht bij in plaats van globaal, zodat robuustheid niet ten koste gaat van expressiviteit. Relevant voor agent-betrouwbaarheid in productie.",
        "curation_score": 7,
        "source_url": "https://arxiv.org/abs/2603.04378",
        "source_type": "paper",
        "is_current": True,
        "building_blocks": ["Model Engines"],
        "guardrails": ["Robustness"],
        "topics": ["AI Safety", "AI Agents", "AI Research"],
        "authors": ["Furkan Mumcu", "Yasin Yilmaz"],
    },
    {
        "title": "Dual-Helix Governance for Reliable Agentic AI",
        "content": "Governance framework addressing five critical LLM limitations: context constraints, cross-session forgetting, stochasticity, instruction failure, and adaptation rigidity. Uses a knowledge graph structured around Knowledge, Behavior, and Skills tracks. Achieved 51% reduction in cyclomatic complexity in WebGIS application. Open-source via AgentLoom toolkit.",
        "summary_nl": "Governance-framework dat vijf LLM-beperkingen adresseert (contextlimiet, cross-session forgetting, stochasticiteit, instructie-falen, adaptatie-rigiditeit) via een kennisgraph rond Knowledge, Behavior en Skills. Boekte 51% minder complexiteit in een WebGIS-case. Open source via AgentLoom.",
        "curation_score": 7,
        "source_url": "https://arxiv.org/abs/2603.04390",
        "source_type": "paper",
        "is_current": True,
        "building_blocks": ["Dynamic Context", "Tool Integration"],
        "guardrails": ["Accountability", "Robustness"],
        "topics": ["AI Governance", "AI Agents", "Knowledge Graphs"],
        "authors": ["Boyuan Guan"],
    },
    {
        "title": "Memex(RL): Scaling Long-Horizon LLM Agents via Indexed Experience Memory",
        "content": "Indexed memory system for long-horizon LLM agents that avoids lossy compression. Maintains compact working context with structured summaries and stable indices while storing full-fidelity interactions in external database. MemexRL reinforcement learning framework optimizes storage and retrieval behaviors under context constraints.",
        "summary_nl": "Indexed memory-systeem voor long-horizon agents zonder lossy compression: compacte werkende context plus volledige interacties in een externe database. MemexRL optimaliseert opslag- en ophaalgedrag onder contextlimieten via reinforcement learning.",
        "curation_score": 5,
        "source_url": "https://arxiv.org/abs/2603.04257",
        "source_type": "paper",
        "is_current": True,
        "building_blocks": ["Dynamic Context"],
        "guardrails": ["Robustness"],
        "topics": ["AI Agents", "Context Engineering", "AI Research"],
        "authors": ["Zhenting Wang"],
    },
    {
        "title": "A Rubric-Supervised Critic from Sparse Real-World Outcomes",
        "content": "Framework for learning critic models from limited real-world interaction data. Introduces Critic Rubrics with 24 behavioral features from human-agent logs. Demonstrates effectiveness in best-of-N reranking on SWE-bench (15.9 point gain), early stopping with 83% fewer attempts, and training-time data curation through critic-selected trajectories.",
        "summary_nl": "Framework om critic-modellen te trainen op beperkte real-world data via Critic Rubrics met 24 gedragskenmerken. Levert 15,9 punt winst op SWE-bench reranking en 83% minder pogingen bij early stopping. Interessant voor evaluatieloops zonder groot gelabeld dataset.",
        "curation_score": 6,
        "source_url": "https://arxiv.org/abs/2603.03800",
        "source_type": "paper",
        "is_current": True,
        "building_blocks": ["Evaluation Loop"],
        "guardrails": ["Accountability", "Human Agency"],
        "topics": ["AI Evaluation", "AI Agents"],
        "authors": ["Xingyao Wang", "Graham Neubig"],
    },
    {
        "title": "Towards Realistic Personalization: Long-Horizon Preference Following",
        "content": "Introduces RealPref benchmark with 100 user profiles and 1,300 personalized preferences expressed through direct statements to subtle cues. Reveals that model performance deteriorates as conversations lengthen and preferences become nuanced. Models struggle to apply learned preferences to novel situations. Establishes groundwork for personalized AI assistants.",
        "summary_nl": "RealPref-benchmark met 100 gebruikersprofielen en 1.300 voorkeuren, van expliciet tot subtiel. Toont aan dat modelprestaties afnemen bij langere gesprekken en nuance — voorkeuren worden slecht toegepast op nieuwe situaties. Fundament voor realistische AI-assistenten.",
        "curation_score": 5,
        "source_url": "https://arxiv.org/abs/2603.04191",
        "source_type": "paper",
        "is_current": True,
        "building_blocks": ["Client Blueprint", "Dynamic Context"],
        "guardrails": ["Human Agency", "Fairness"],
        "topics": ["Personalization", "Conversational AI"],
        "authors": ["Qianyun Guo"],
    },
    {
        "title": "DMAST: Adversarial Safety Training for Multimodal Web Agents",
        "content": "Framework for robustifying multimodal web agents against cross-modal attacks. Discovers that attacks including visual components far outperform text-only injections. DMAST models agent-attacker dynamics through three training stages: imitation learning, supervised fine-tuning with zero-acknowledgment strategy, and adversarial reinforcement learning. Doubles task completion efficiency while mitigating risks.",
        "summary_nl": "Framework voor adversarial safety training van multimodale web-agents. Laat zien dat aanvallen met visuele componenten veel effectiever zijn dan text-only injection. Drie trainingsfases (imitation, supervised fine-tuning, adversarial RL) verdubbelen taakvoltooiing én mitigeren risico.",
        "curation_score": 6,
        "source_url": "https://arxiv.org/abs/2603.04364",
        "source_type": "paper",
        "is_current": True,
        "building_blocks": ["Tool Integration", "Model Engines"],
        "guardrails": ["Robustness", "Privacy"],
        "topics": ["AI Safety", "AI Agents"],
        "authors": ["Haoyu Liu"],
    },
    {
        "title": "EU AI Act 2026: Compliance Requirements for High-Risk AI Systems",
        "content": "From August 2, 2026, the EU AI Act's core framework becomes fully operational with comprehensive requirements for high-risk AI systems: risk management, data governance, technical documentation, record-keeping, transparency, human oversight, accuracy, robustness, and cybersecurity. Non-compliance can result in fines up to €35M or percentage of global turnover.",
        "summary_nl": "Operationele checklist voor de EU AI Act vanaf 2 augustus 2026: risicobeheer, datagovernance, technische documentatie, transparantie, menselijke controle, robuustheid en cybersecurity. Boetes tot €35M of een percentage van de wereldwijde omzet — directe input voor evaluatie en compliance.",
        "curation_score": 9,
        "source_url": "https://www.complianceandrisks.com/blog/eu-ai-act-compliance-requirements-for-companies-what-to-prepare-for-2026/",
        "source_type": "regulation",
        "is_current": True,
        "building_blocks": ["Knowledge", "Evaluation Loop"],
        "guardrails": ["Accountability", "Transparency", "Robustness", "Privacy", "Human Agency"],
        "topics": ["EU AI Act", "AI Compliance"],
        "authors": ["Compliance & Risks"],
    },
    {
        "title": "A-RAG: Scaling Agentic RAG via Hierarchical Retrieval Interfaces",
        "content": "Agentic RAG framework that exposes hierarchical retrieval interfaces directly to the model, representing a shift from static retrieval pipelines toward agent-driven, dynamic retrieval. The model autonomously decides how to traverse and query multiple retrieval layers for optimal information gathering.",
        "summary_nl": "Agentic RAG-framework dat hiërarchische retrieval-interfaces rechtstreeks aan het model blootstelt. Schuift van statische retrieval-pipelines naar agent-gedreven, dynamische retrieval waarin het model zelf bepaalt welke laag te bevragen.",
        "curation_score": 5,
        "source_url": "https://arxiv.org/abs/2602.03442",
        "source_type": "paper",
        "is_current": True,
        "building_blocks": ["Dynamic Context", "Tool Integration"],
        "guardrails": ["Transparency"],
        "topics": ["RAG", "AI Agents"],
        "authors": ["arXiv Research"],
    },
    # --- Knowledge (BB_01) — AI Literacy, Decision Intelligence, Deskilling ---
    {
        "title": "ITU Online — EU AI Act Compliance Training for AI Teams",
        "content": "Practical guide on operationalising EU AI Act Art. 4: 'appropriate AI literacy' is context-based and role-specific. Proposes working formats — scenario walkthroughs, tabletop exercises, mock audits, red-team reviews — over abstract legal text. Introduces the litmus test: 'If a team cannot explain why a system is low-risk, transparency-only or high-risk, it is not ready to launch.'",
        "summary_nl": "Praktische gids om EU AI Act Art. 4 operationeel te maken: 'passende AI-geletterdheid' is contextueel en rol-specifiek. Werkende formats zijn scenario walkthroughs, tabletop exercises, mock audits en red-team reviews — niet abstracte wettekst. Lakmoesproef: als een team niet kan uitleggen waarom een systeem laag/transparantie/hoog-risico is, is het niet klaar voor release.",
        "curation_score": 9,
        "source_url": "https://www.ituonline.com/blogs/practical-strategies-for-training-your-ai-team-on-eu-ai-act-compliance-requirements/",
        "source_type": "guideline",
        "is_current": True,
        "building_blocks": ["Knowledge", "Evaluation Loop"],
        "guardrails": ["Accountability", "Transparency", "Human Agency"],
        "topics": ["AI Literacy", "EU AI Act", "AI Compliance"],
        "authors": ["ITU Online"],
    },
    {
        "title": "OECD/EC — AI Literacy Framework (AILit)",
        "content": "Joint OECD and European Commission framework defining AI literacy across three dimensions: (1) knowledge and skills — understanding how AI works, using, co-creating; (2) attitudes and values — critical thinking, ethical reflection, responsible use; (3) cross-domain integration — embedding AI understanding in work processes rather than treating it as a separate subject. Provides a competence structure that BB_01 can map training outcomes to.",
        "summary_nl": "Gezamenlijk OECD/EC-kader dat AI-geletterdheid in drie dimensies definieert: kennis en vaardigheden (hoe AI werkt, gebruiken, co-creëren), attitudes en waarden (kritisch denken, ethische reflectie, verantwoord gebruik), en cross-domein integratie (verweven in werkprocessen, geen apart vak). Biedt de competentiestructuur waartegen BB_01 leerresultaten kan spiegelen.",
        "curation_score": 9,
        "source_url": "https://oecdedutoday.com/new-ai-literacy-framework-to-equip-youth-in-an-age-of-ai/",
        "source_type": "regulation",
        "is_current": True,
        "building_blocks": ["Knowledge"],
        "guardrails": ["Human Agency", "Transparency", "Fairness"],
        "topics": ["AI Literacy", "AI Education"],
        "authors": ["OECD", "European Commission"],
    },
    {
        "title": "Kozyrkov — The Most Valuable Skill for the AI Era",
        "content": "Cassie Kozyrkov argues that as AI takes over execution, the bottleneck shifts from the 'genie side' (tool mastery, prompt engineering) to the 'wish side' — knowing which problem to solve, for whom, and why. Frames AI as a 'thoughtlessness enabler': the same mechanism that accelerates good decisions amplifies bad ones. Decision Intelligence becomes the core organisational capability; tool-fluency alone is insufficient.",
        "summary_nl": "Cassie Kozyrkov stelt dat het knelpunt in het AI-tijdperk verschuift van de 'genie-kant' (tools, prompts) naar de 'wens-kant' — weten welk probleem je wilt oplossen, voor wie en waarom. AI is een 'thoughtlessness enabler': hetzelfde mechanisme dat goede beslissingen versnelt versterkt slechte. Decision Intelligence wordt de kerncapaciteit; tool-vaardigheid alleen is niet genoeg.",
        "curation_score": 10,
        "source_url": "https://decision.substack.com/p/whats-the-most-valuable-skill-for",
        "source_type": "essay",
        "is_current": True,
        "building_blocks": ["Knowledge", "Client Blueprint"],
        "guardrails": ["Human Agency", "Accountability"],
        "topics": ["Decision Intelligence", "AI Literacy"],
        "authors": ["Cassie Kozyrkov"],
    },
    {
        "title": "Kahneman & Klein — Conditions for Intuitive Expertise",
        "content": "Landmark paper (American Psychologist 2009, DOI 10.1037/a0016755) establishing the two conditions under which professional intuition is reliable: (1) a high-validity environment — stable, objectively identifiable cues predictive of outcomes; and (2) adequate opportunity to learn — practice with fast, consistent feedback. 'Subjective experience is not a reliable indicator of judgment accuracy.' The AI era directly threatens both conditions: AI alters the validity environment and breaks the feedback loops that calibrate expert intuition.",
        "summary_nl": "Fundamenteel artikel (American Psychologist 2009) dat twee voorwaarden voor betrouwbare professionele intuïtie vastlegt: een high-validity omgeving (stabiele, objectief identificeerbare cues) en voldoende leerkans (oefening met snelle, consistente feedback). 'Subjectieve ervaring is geen betrouwbare indicator voor de kwaliteit van een oordeel.' Het AI-tijdperk ondermijnt beide: AI verandert de geldigheidsomgeving en verbreekt de feedbackloops die expert-intuïtie ijken.",
        "curation_score": 9,
        "source_url": "https://pubmed.ncbi.nlm.nih.gov/19739881/",
        "source_type": "paper",
        "is_current": True,
        "building_blocks": ["Knowledge", "Evaluation Loop"],
        "guardrails": ["Human Agency", "Accountability"],
        "topics": ["Decision Intelligence", "Human Cognition"],
        "authors": ["Daniel Kahneman", "Gary Klein"],
    },
    {
        "title": "McKinsey.org — Human Skills for the 2026 AI-Driven Workplace",
        "content": "Positions meta-skills — the cognitive and social capacities to steer, interpret, and ethically assess AI output — as the real competitive advantage in 2026. Identifies four foundational AI mindsets: curiosity, adaptability, responsibility, human-centered thinking. Argues that tool-specific training decays fast; meta-skill investment compounds. 'Meta-skills are the real competitive advantage.'",
        "summary_nl": "Positioneert meta-skills — de cognitieve en sociale capaciteiten om AI-output te sturen, interpreteren en ethisch te beoordelen — als het echte concurrentievoordeel in 2026. Vier funderende AI-mindsets: nieuwsgierigheid, adaptiviteit, verantwoordelijkheid, mens-gecentreerd denken. Tool-specifieke training veroudert snel; investeringen in meta-skills compounden.",
        "curation_score": 8,
        "source_url": "https://www.mckinsey.org/dotorgblog/the-human-skills-you-will-need-to-thrive-in-2026s-ai-driven-workplace",
        "source_type": "essay",
        "is_current": True,
        "building_blocks": ["Knowledge"],
        "guardrails": ["Human Agency", "Accountability", "Fairness"],
        "topics": ["AI Literacy", "Human Skills", "Meta-skills"],
        "authors": ["McKinsey.org"],
    },
    {
        "title": "Lema — The Four Levels of AI Work",
        "content": "Chris Lema's progression model for institutional AI adoption: Level 1 Tool → Collaborator (mindset shift), Level 2 Throwaway output → Compounding assets (skills, frameworks, specifications, memory), Level 3 Ad-hoc → Operating agreements (explicit decision authority, human-in-the-loop pause points, escalation triggers, quality standards), Level 4 Interactions → Production architectures (multi-agent, multi-model designs). 'Define the operating agreement. Write it down. This is what separates people who use AI from people who work with AI.'",
        "summary_nl": "Progressiemodel voor institutionele AI-adoptie: L1 Tool → Collaborator (mentaliteitsshift), L2 Wegwerpoutput → Compounding Assets (skills, frameworks, memory), L3 Ad-hoc → Operating Agreements (expliciete besluitbevoegdheid, human-in-the-loop, escalatie, kwaliteitsnormen), L4 Interacties → Productiearchitecturen (multi-agent/model). Operating agreements zijn het concrete instrument waarmee expertise wordt geëxternaliseerd — de meeste organisaties blijven steken op L1.",
        "curation_score": 8,
        "source_url": "https://chrislema.com/the-four-levels-of-ai-work",
        "source_type": "essay",
        "is_current": True,
        "building_blocks": ["Knowledge", "Client Blueprint", "Tool Integration"],
        "guardrails": ["Accountability", "Human Agency"],
        "topics": ["Operating Agreements", "AI Adoption"],
        "authors": ["Chris Lema"],
    },
    {
        "title": "Dell'Acqua et al. — Navigating the Jagged Technological Frontier (BCG)",
        "content": "Pre-registered field experiment (n=758 BCG consultants, 2023) establishing the empirical basis for centaur/cyborg patterns. Within the frontier: +12.2% more tasks, +25.1% faster, +40% higher quality. Beyond the frontier: AI-users 19 percentage points less accurate than controls. Skill-levelling: weakest consultants gain +43%. 'On some tasks AI is immensely powerful, and on others it fails completely or subtly. And, unless you use AI a lot, you won't know which is which.' Knowing the frontier is learnable only through extensive practice.",
        "summary_nl": "Pre-geregistreerd veldexperiment (n=758 BCG-consultants, 2023) dat de empirische basis legt voor centaur/cyborg-patronen. Binnen de frontier: +12,2% meer taken, +25,1% sneller, +40% hogere kwaliteitsscore. Buiten de frontier: AI-gebruikers 19 procentpunten minder nauwkeurig. Skill-nivellering: zwakste consultants +43%. Je leert de jagged frontier alleen door uitgebreide praktijkervaring, niet door instructie.",
        "curation_score": 9,
        "source_url": "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4573321",
        "source_type": "paper",
        "is_current": True,
        "building_blocks": ["Knowledge", "Evaluation Loop"],
        "guardrails": ["Human Agency", "Accountability"],
        "topics": ["Human-AI Collaboration", "Jagged Frontier"],
        "authors": ["Fabrizio Dell'Acqua", "Ethan Mollick", "Hila Lifshitz-Assaf"],
    },
    {
        "title": "Dell'Acqua et al. — The Cybernetic Teammate (P&G)",
        "content": "Pre-registered field experiment (n=776 P&G professionals, 2025) on team-level AI augmentation. Findings: individual + AI ≈ team of two without AI (+0.37 SD quality, p<0.01); team + AI is 3× more likely to produce top-10% breakthrough solutions. AI balances disciplinary one-sidedness, yielding more cross-functional solutions. 'If you want to empower an individual to be as effective as a team, give them AI. But if you want to be in that top 10% of performers, a full human team plus AI seems like the recipe for success.'",
        "summary_nl": "Pre-geregistreerd veldexperiment (n=776 P&G-professionals, 2025) over AI-versterking op teamniveau. Individu + AI ≈ team van twee zonder AI (+0,37 SD kwaliteit, p<0,01); team + AI is 3× vaker in de top-10% doorbraakoplossingen. AI balanceert disciplinaire eenzijdigheid — levert meer cross-functionele oplossingen. Individuele productiviteit heeft een plafond dat alleen teams kunnen doorbreken.",
        "curation_score": 9,
        "source_url": "https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5188231",
        "source_type": "paper",
        "is_current": True,
        "building_blocks": ["Knowledge", "Client Blueprint"],
        "guardrails": ["Human Agency", "Well-being"],
        "topics": ["Human-AI Collaboration", "Team Performance"],
        "authors": ["Fabrizio Dell'Acqua", "Charles Ayoubi", "Hila Lifshitz-Assaf", "Raffaella Sadun", "Ethan Mollick", "Karim Lakhani"],
    },
    {
        "title": "Budzyń et al. — AI-Induced Deskilling in Colonoscopy (Lancet)",
        "content": "First clinical evidence of AI-induced deskilling in healthcare (Lancet Gastroenterology & Hepatology, Aug 2025). Study of 19 experienced endoscopists (>2,000 procedures each) across 4 Polish clinics: adenoma detection rate without AI fell from 28% before AI exposure to 22% after just three months of AI use. Statistically significant decline in a short window. 'To our knowledge this is the first study to suggest a negative impact of regular AI use on healthcare professionals' ability to complete a patient-relevant task.' Implication for BB_01: active skill maintenance without AI must be a deliberate policy, not an afterthought.",
        "summary_nl": "Eerste klinische bewijs van AI-geïnduceerde deskilling in de zorg (Lancet Gastroenterology & Hepatology, aug 2025). Studie bij 19 ervaren endoscopisten (>2.000 procedures elk) in 4 Poolse klinieken: adenoom-detectie zonder AI daalde van 28% vóór AI-blootstelling naar 22% na drie maanden AI-gebruik. Statistisch significant in een korte tijd. BB_01-implicatie: bewust competentieonderhoud zónder AI moet expliciet beleid zijn — geen bijzaak.",
        "curation_score": 10,
        "source_url": "https://www.statnews.com/2025/08/12/ai-deskilling-doctors-colonoscopy-study-lancet/",
        "source_type": "paper",
        "is_current": True,
        "building_blocks": ["Knowledge", "Evaluation Loop"],
        "guardrails": ["Human Agency", "Accountability", "Well-being"],
        "topics": ["Deskilling", "Human Cognition", "AI in Healthcare"],
        "authors": ["Krzysztof Budzyń et al."],
    },
    {
        "title": "Fortune/WalkMe — White-Collar Workers Quietly Rebelling Against AI",
        "content": "Global survey (n=3,750 across 14 countries, April 2026) showing 80% of white-collar workers actively avoid or reject AI tools — 54% bypassed AI in the last 30 days and worked manually; 33% did not use AI at all. Trust chasm: only 9% of workers trust AI for complex decisions vs. 61% of executives (52-point gap). Tool-adequacy gap: 88% of executives say tools are adequate; only 21% of workers agree (67 points). Driver is FOBO (Fear of Becoming Obsolete), not technical failure. Costs ~51 lost workdays per employee per year. BB_01 must address FOBO psychologically before technical training lands.",
        "summary_nl": "Wereldwijd onderzoek (n=3.750, 14 landen, april 2026): 80% van kenniswerkers vermijdt of verwerpt AI-tools actief — 54% omzeilde AI in afgelopen 30 dagen, 33% gebruikt AI helemaal niet. Trust chasm: 9% werknemers vertrouwt AI voor complexe beslissingen vs. 61% executives (52 punten). Tool-adequaatheidsgap: 88% executives zegt tools zijn adequaat, slechts 21% werknemers eens. Driver is FOBO (Fear of Becoming Obsolete), geen technisch falen. Kost ~51 verloren werkdagen per werknemer per jaar. BB_01 moet FOBO psychologisch adresseren vóór technische training zinvol is.",
        "curation_score": 9,
        "source_url": "https://fortune.com/2026/04/09/ai-backlash-quiet-quitting-fobo-obsolete-white-collar-rebellion/",
        "source_type": "news",
        "is_current": True,
        "building_blocks": ["Knowledge"],
        "guardrails": ["Well-being", "Human Agency", "Transparency"],
        "topics": ["AI Adoption", "FOBO", "Change Management"],
        "authors": ["Fortune", "WalkMe", "SAP"],
    },
    {
        "title": "Sivulka (a16z) — Institutional AI vs Individual AI",
        "content": "Formulates the productivity paradox: 'AI just made every individual 10x more productive. No company became 10x more valuable as a result. Where did the productivity go?' Draws the electricity parallel: New England textile mills installed electric motors in the 1890s but saw no productivity gain for ~30 years — until the assembly line radically redesigned the factory around the technology. Seven distinguishing factors of institutional AI: coordination, signal, objectivity, edge, outcomes, enablement, unprompted action. BB_01 must explicitly distinguish tool-fluency from institutional AI maturity.",
        "summary_nl": "Formuleert de productiviteitsparadox: 'AI maakte elk individu 10× productiever. Geen bedrijf werd 10× waardevoller. Waar ging de productiviteit naartoe?' Trekt de elektriciteitsparallel: New England textielfabrieken installeerden al in de jaren 1890 elektromotoren, maar 30 jaar lang geen productiviteitswinst — pas na radicaal herontwerp van de productielijn kwam de waarde. Zeven factoren van institutionele AI: coördinatie, signal, objectiviteit, edge, outcomes, enablement, unprompted action. BB_01 moet tool-vaardigheid expliciet scheiden van institutionele AI-volwassenheid.",
        "curation_score": 9,
        "source_url": "https://www.a16z.news/p/institutional-ai-vs-individual-ai",
        "source_type": "essay",
        "is_current": True,
        "building_blocks": ["Knowledge", "Client Blueprint"],
        "guardrails": ["Accountability", "Human Agency"],
        "topics": ["AI Adoption", "Enterprise AI", "Change Management"],
        "authors": ["George Sivulka", "Andreessen Horowitz"],
    },
    {
        "title": "McKinsey — Superagency in the Workplace",
        "content": "McKinsey report (Jan 2025) on the AI adoption gap between employees and leaders. Key findings: only 1% of companies describe themselves as 'mature' in AI implementation; the biggest barrier is not the employee — they are ready — but the leader; C-suite estimates 4% of employees use gen AI for 30%+ of daily work, reality is 3× higher; nearly half of employees want more formal training. Implication for BB_01: leadership change-enablement is the primary lever; employee training alone does not close the maturity gap.",
        "summary_nl": "McKinsey-rapport (jan 2025) over de AI-adoptiekloof tussen medewerkers en leiders. Kernbevindingen: slechts 1% van bedrijven noemt zichzelf 'matuur' in AI-implementatie; de grootste barrière is niet de medewerker (die is klaar) maar de leider; C-suite schat dat 4% van medewerkers gen AI gebruikt voor 30%+ dagelijks werk — werkelijkheid is 3× hoger; bijna de helft van medewerkers wil meer formele training. BB_01-implicatie: leiderschap als change-enabler is de primaire hefboom — training van medewerkers alleen sluit het maturity-gat niet.",
        "curation_score": 9,
        "source_url": "https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/superagency-in-the-workplace-empowering-people-to-unlock-ais-full-potential-at-work",
        "source_type": "report",
        "is_current": True,
        "building_blocks": ["Knowledge"],
        "guardrails": ["Human Agency", "Accountability"],
        "topics": ["AI Adoption", "Leadership", "Change Management"],
        "authors": ["McKinsey & Company"],
    },
    {
        "title": "KPMG — Agentic AI Untangled",
        "content": "KPMG framework (Jan 2026) identifying four agent archetypes organisations must design roles around: Taskers (defined repetitive tasks), Automators (complex workflow automation), Collaborators (dynamic digital teammates), and Orchestrators (intelligent control towers coordinating agents and resources). Humans shift to the orchestrator role — not 'I do part A and AI does part B' but 'I design the system that determines who does what and how results are evaluated.' 57% of organisations choose a blended build-and-buy approach. Centaur/cyborg as individual-task frames is insufficient for the agents era.",
        "summary_nl": "KPMG-kader (jan 2026) met vier agent-archetypes waaromheen organisaties rollen moeten ontwerpen: Taskers (gedefinieerde repetitieve taken), Automators (complexe workflow-automatisering), Collaborators (dynamische digitale teamgenoten) en Orchestrators (intelligente control towers die agents en resources coördineren). De mens verschuift naar de orchestrator-rol — niet 'ik doe deel A en AI deel B' maar 'ik ontwerp het systeem dat bepaalt wie wat doet en hoe resultaten worden beoordeeld'. Centaur/cyborg op taakniveau is onvoldoende voor het agents-tijdperk.",
        "curation_score": 8,
        "source_url": "https://kpmg.com/us/en/articles/2026/agentic-ai-untangled.html",
        "source_type": "report",
        "is_current": True,
        "building_blocks": ["Knowledge", "Client Blueprint", "Tool Integration"],
        "guardrails": ["Accountability", "Human Agency", "Robustness"],
        "topics": ["AI Agents", "Agentic AI", "Orchestration"],
        "authors": ["KPMG"],
    },
]


# Tools live in ~/ODIN/resources/tools/ (cross-project); this list is the
# current hand-curated selection for the BeeHaive website. Later we'll move
# the source of truth to vault notes + an ingest_tool.py script.
#
# building_blocks: inhoudelijke relatie (tool is relevant voor deze BB)
# displayed_on:    redactionele keuze (verschijnt op de BB-pagina)
# display_order:   {bb_name: int} — volgorde binnen die BB-pagina
TOOLS = [
    {
        "slug": "langsmith",
        "name": "LangSmith",
        "category": "saas",
        "url": "https://smith.langchain.com/",
        "description": "End-to-end platform voor prompt-ontwikkeling: versiebeheer, A/B-testing, monitoring en evaluatie met custom metrics.",
        "building_blocks": ["Prompt Design", "Evaluation Loop", "Tool Integration"],
        "guardrails": ["Accountability", "Robustness"],
        "sources": ["https://smith.langchain.com/"],
        "displayed_on": ["Prompt Design"],
        "display_order": {"Prompt Design": 1},
    },
    {
        "slug": "langfuse",
        "name": "Langfuse",
        "category": "open_source",
        "url": "https://langfuse.com/",
        "description": "Open-source LLM observability en prompt management. Self-hosted alternatief voor LangSmith, met tracing, evals en prompt-versioning.",
        "building_blocks": ["Prompt Design", "Evaluation Loop"],
        "guardrails": ["Accountability", "Transparency"],
        "sources": [],
        "displayed_on": ["Prompt Design"],
        "display_order": {"Prompt Design": 2},
    },
    {
        "slug": "promptfoo",
        "name": "Promptfoo",
        "category": "open_source",
        "url": "https://www.promptfoo.dev/",
        "description": "Open-source framework voor geautomatiseerde prompt-evaluatie. Vergelijkt varianten op kwaliteit, veiligheid en regressie — CI/CD-integreerbaar.",
        "building_blocks": ["Prompt Design", "Evaluation Loop"],
        "guardrails": ["Robustness", "Accountability"],
        "sources": [],
        "displayed_on": ["Prompt Design"],
        "display_order": {"Prompt Design": 3},
    },
    {
        "slug": "guardrails-ai",
        "name": "Guardrails AI",
        "category": "framework",
        "url": "https://www.guardrailsai.com/",
        "description": "The AI Reliability Platform — Python-framework voor input/output-validatie rond prompts en agents: structuur-garanties, PII-filtering en jailbreak-detectie.",
        "building_blocks": ["Prompt Design", "Tool Integration"],
        "guardrails": ["Privacy", "Robustness"],
        "sources": [],
        "displayed_on": ["Prompt Design"],
        "display_order": {"Prompt Design": 4},
    },
    {
        "slug": "anthropic-workbench",
        "name": "Anthropic Workbench",
        "category": "saas",
        "url": "https://console.anthropic.com/workbench",
        "description": "Interactieve prompt-omgeving voor Claude: system prompts itereren, variabelen testen, modelvergelijking en direct exporten naar code.",
        "building_blocks": ["Prompt Design", "Model Engines"],
        "guardrails": ["Transparency"],
        "sources": [],
        "displayed_on": ["Prompt Design"],
        "display_order": {"Prompt Design": 5},
    },
    {
        "slug": "llamaindex",
        "name": "LlamaIndex",
        "category": "open_source",
        "url": "https://www.llamaindex.ai/",
        "description": "Data-framework voor RAG: 100+ connectors (Confluence, SharePoint, Notion, Drive), SentenceWindowNodeParser voor chunking en incremental sync op document-hashes — event-triggered re-indexing zonder full rebuild.",
        "building_blocks": ["Dynamic Context", "Knowledge"],
        "guardrails": ["Robustness", "Transparency"],
        "sources": ["https://towardsdatascience.com/grounding-your-llm-a-practical-guide-to-rag-for-enterprise-knowledge-bases/"],
        "displayed_on": ["Dynamic Context"],
        "display_order": {"Dynamic Context": 1},
    },
    {
        "slug": "weaviate",
        "name": "Weaviate",
        "category": "open_source",
        "url": "https://weaviate.io/",
        "description": "Vector-store met native hybrid search (vector + BM25 in één query), multi-tenancy per department, en access control op DB-niveau. Self-hosted in EU-infrastructuur mogelijk.",
        "building_blocks": ["Dynamic Context", "Knowledge"],
        "guardrails": ["Privacy", "Accountability"],
        "sources": ["https://weaviate.io/blog/chunking-strategies-for-rag"],
        "displayed_on": ["Dynamic Context"],
        "display_order": {"Dynamic Context": 2},
    },
    {
        "slug": "voyage-ai",
        "name": "Voyage AI",
        "category": "saas",
        "url": "https://www.voyageai.com/",
        "description": "Embedding-modellen voor RAG (voyage-3-large: 32K token context, top MTEB-prestaties). Domeinspecifieke varianten voor medisch/juridisch met 20-40% betere retrieval. Ook reranker beschikbaar.",
        "building_blocks": ["Dynamic Context"],
        "guardrails": ["Robustness"],
        "sources": ["https://www.anthropic.com/news/contextual-retrieval"],
        "displayed_on": ["Dynamic Context"],
        "display_order": {"Dynamic Context": 3},
    },
    {
        "slug": "cohere-rerank",
        "name": "Cohere Rerank",
        "category": "saas",
        "url": "https://cohere.com/rerank",
        "description": "Cross-encoder reranker die query + document samen leest voor echte semantische alignment. Combineert met Contextual Embeddings + BM25 tot 67% minder retrieval-fouten (Anthropic benchmark).",
        "building_blocks": ["Dynamic Context"],
        "guardrails": ["Robustness"],
        "sources": ["https://www.anthropic.com/news/contextual-retrieval"],
        "displayed_on": ["Dynamic Context"],
        "display_order": {"Dynamic Context": 4},
    },
    {
        "slug": "mem0",
        "name": "Mem0",
        "category": "open_source",
        "url": "https://mem0.ai/",
        "description": "Pluggable memory-layer voor AI-agents met passieve extractie, intelligente CRUD en semantische search. 26% betere accuracy + 91% lagere p95-latency vs. full-context. SOC 2 en HIPAA beschikbaar op managed tier.",
        "building_blocks": ["Dynamic Context"],
        "guardrails": ["Privacy", "Accountability"],
        "sources": ["https://arxiv.org/abs/2504.19413", "https://vectorize.io/articles/mem0-vs-letta"],
        "displayed_on": ["Dynamic Context"],
        "display_order": {"Dynamic Context": 5},
    },
    {
        "slug": "letta",
        "name": "Letta",
        "category": "open_source",
        "url": "https://www.letta.com/",
        "description": "Agent-runtime waar het hele AI-systeem binnen draait en de agent zelf zijn geheugen onderhoudt: Core (altijd in context), Recall (recente gesprekken), Archival (lange-termijn, semantisch doorzoekbaar). Open-source (Apache 2.0), self-hostbaar. Keuze bij autonome agents die zonder menselijk toezicht hun eigen geheugen cureren; nadeel is architecturele binding aan het Letta-runtime.",
        "building_blocks": ["Dynamic Context", "Tool Integration"],
        "guardrails": ["Accountability"],
        "sources": ["https://vectorize.io/articles/mem0-vs-letta"],
        "displayed_on": ["Dynamic Context"],
        "display_order": {"Dynamic Context": 6},
    },
    {
        "slug": "microsoft-presidio",
        "name": "Microsoft Presidio",
        "category": "open_source",
        "url": "https://microsoft.github.io/presidio/",
        "description": "PII-detectie en redactie voor pre-indexering: NER voor namen/locaties/organisaties, regel-gebaseerde filters voor BSN/IBAN/e-mail, deterministisch tokenizeren voor referentiële integriteit.",
        "building_blocks": ["Dynamic Context"],
        "guardrails": ["Privacy", "Accountability"],
        "sources": ["https://arxiv.org/abs/2412.04697"],
        "displayed_on": ["Dynamic Context"],
        "display_order": {"Dynamic Context": 7},
    },
    {
        "slug": "ragas",
        "name": "RAGAS",
        "category": "open_source",
        "url": "https://docs.ragas.io/",
        "description": "RAG-evaluatieframework dat vier kwaliteitsdimensies meet (faithfulness, answer relevancy, context recall en context precision), elk voor een ander failure-type. LLM-as-judge maakt het schaalbaar naar honderden queries zonder handmatig opgestelde referentieantwoorden.",
        "building_blocks": ["Dynamic Context", "Evaluation Loop"],
        "guardrails": ["Robustness", "Transparency"],
        "sources": ["https://towardsdatascience.com/grounding-your-llm-a-practical-guide-to-rag-for-enterprise-knowledge-bases/"],
        "displayed_on": ["Dynamic Context"],
        "display_order": {"Dynamic Context": 8},
    },
    # --- Knowledge (BB_01) tools ---
    {
        "slug": "elements-of-ai",
        "name": "Elements of AI",
        "category": "open_source",
        "url": "https://www.elementsofai.com/",
        "description": "Gratis online basiscursus AI-geletterdheid (University of Helsinki + Reaktor), beschikbaar in alle EU-talen. De-facto Europese standaard voor een breed AI-Literacy-fundament — geschikt als baseline-training om personeel te voldoen aan EU AI Act Art. 4, voorafgaand aan rol-specifieke verdieping.",
        "building_blocks": ["Knowledge"],
        "guardrails": ["Human Agency", "Accountability"],
        "sources": ["https://oecdedutoday.com/new-ai-literacy-framework-to-equip-youth-in-an-age-of-ai/"],
        "displayed_on": ["Knowledge"],
        "display_order": {"Knowledge": 1},
    },
    {
        "slug": "degreed",
        "name": "Degreed",
        "category": "saas",
        "url": "https://degreed.com/",
        "description": "Skills-intelligence platform dat AI-competenties per rol in kaart brengt, leerpaden personaliseert en voortgang meet. Maakt de competentiematrix concreet die de EU AI Act in abstracto eist — welke medewerker heeft welke AI-skills, waar zitten gaps, welk leerplan dicht ze.",
        "building_blocks": ["Knowledge"],
        "guardrails": ["Accountability", "Human Agency"],
        "sources": [],
        "displayed_on": ["Knowledge"],
        "display_order": {"Knowledge": 2},
    },
    {
        "slug": "cultureamp",
        "name": "Culture Amp",
        "category": "saas",
        "url": "https://www.cultureamp.com/",
        "description": "Employee-sentiment platform om FOBO, trust-chasm en adoptie-sentiment rond AI concreet te meten in plaats van te raden. Benchmarks maken de 52-punts vertrouwenskloof tussen leidinggevenden en medewerkers zichtbaar — voorwaarde voordat training überhaupt zinvol is.",
        "building_blocks": ["Knowledge"],
        "guardrails": ["Well-being", "Human Agency"],
        "sources": ["https://fortune.com/2026/04/09/ai-backlash-quiet-quitting-fobo-obsolete-white-collar-rebellion/"],
        "displayed_on": ["Knowledge"],
        "display_order": {"Knowledge": 3},
    },
    {
        "slug": "humanloop",
        "name": "Humanloop",
        "category": "saas",
        "url": "https://humanloop.com/",
        "description": "Rubric-based evaluation-platform waarmee experts hun kwaliteitscriteria kunnen externaliseren naar runnable rubrics die modellen en agents tegen toetsen. Operationaliseert Kozyrkov's 'define quality first' en Lema's operating-agreement-niveau: weg van gut feel, richting schriftelijke, testbare standaarden.",
        "building_blocks": ["Knowledge", "Evaluation Loop"],
        "guardrails": ["Accountability", "Human Agency", "Transparency"],
        "sources": [],
        "displayed_on": ["Knowledge"],
        "display_order": {"Knowledge": 4},
    },
    {
        "slug": "notion",
        "name": "Notion",
        "category": "saas",
        "url": "https://www.notion.so/",
        "description": "Generieke workspace die in enterprise-context vaak de plek is waar operating agreements, rubrics, frontier-observaties en team-playbooks daadwerkelijk leven. Niet AI-specifiek, en precies daarom geschikt: een operating agreement moet vindbaar en onderhoudbaar zijn waar mensen toch al samenwerken, niet in een aparte AI-silo.",
        "building_blocks": ["Knowledge"],
        "guardrails": ["Accountability", "Transparency"],
        "sources": [],
        "displayed_on": ["Knowledge"],
        "display_order": {"Knowledge": 5},
    },
]


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


def seed_knowledge_items(tx):
    """Create KnowledgeItems with all relationships. Idempotent via MERGE."""
    topics = set()
    authors = set()

    for item in KNOWLEDGE_ITEMS:
        # Create KnowledgeItem node
        tx.run(
            """
            MERGE (ki:KnowledgeItem {title: $title})
            SET ki.content = $content,
                ki.summary_nl = $summary_nl,
                ki.source_url = $source_url,
                ki.source_type = $source_type,
                ki.is_current = $is_current,
                ki.curation_score = $curation_score,
                ki.created_at = datetime()
            """,
            title=item["title"],
            content=item["content"],
            summary_nl=item.get("summary_nl"),
            source_url=item["source_url"],
            source_type=item["source_type"],
            is_current=item["is_current"],
            curation_score=item.get("curation_score", 0),
        )

        # Create Topic nodes and relationships
        for topic in item["topics"]:
            topics.add(topic)
            tx.run(
                """
                MATCH (ki:KnowledgeItem {title: $title})
                MERGE (t:Topic {name: $topic})
                MERGE (ki)-[:ABOUT]->(t)
                """,
                title=item["title"],
                topic=topic,
            )

        # Create Author nodes and relationships
        for author in item["authors"]:
            authors.add(author)
            tx.run(
                """
                MATCH (ki:KnowledgeItem {title: $title})
                MERGE (a:Author {name: $author})
                MERGE (ki)-[:AUTHORED_BY]->(a)
                """,
                title=item["title"],
                author=author,
            )

        # Create BuildingBlock relationships
        for bb in item["building_blocks"]:
            tx.run(
                """
                MATCH (ki:KnowledgeItem {title: $title})
                MATCH (bb:BuildingBlock {name: $bb_name})
                MERGE (ki)-[:RELATES_TO]->(bb)
                """,
                title=item["title"],
                bb_name=bb,
            )

        # Create Guardrail relationships
        for gr in item["guardrails"]:
            tx.run(
                """
                MATCH (ki:KnowledgeItem {title: $title})
                MATCH (gr:Guardrail {name: $gr_name})
                MERGE (ki)-[:ADDRESSES]->(gr)
                """,
                title=item["title"],
                gr_name=gr,
            )

    return len(KNOWLEDGE_ITEMS), len(topics), len(authors)


def seed_tools(tx):
    """Create Tool nodes with taxonomy + curation relationships. Idempotent via MERGE."""
    for tool in TOOLS:
        tx.run(
            """
            MERGE (t:Tool {slug: $slug})
            SET t.name = $name,
                t.category = $category,
                t.url = $url,
                t.description = $description,
                t.updated_at = datetime()
            """,
            slug=tool["slug"],
            name=tool["name"],
            category=tool["category"],
            url=tool["url"],
            description=tool["description"],
        )

        # RELATES_TO: inhoudelijke link met BuildingBlocks
        for bb in tool.get("building_blocks", []):
            tx.run(
                """
                MATCH (t:Tool {slug: $slug})
                MATCH (b:BuildingBlock {name: $bb_name})
                MERGE (t)-[:RELATES_TO]->(b)
                """,
                slug=tool["slug"],
                bb_name=bb,
            )

        # ADDRESSES: Guardrails het tool mitigeert/ondersteunt
        for gr in tool.get("guardrails", []):
            tx.run(
                """
                MATCH (t:Tool {slug: $slug})
                MATCH (g:Guardrail {name: $gr_name})
                MERGE (t)-[:ADDRESSES]->(g)
                """,
                slug=tool["slug"],
                gr_name=gr,
            )

        # REFERENCES: links naar KnowledgeItems (via source_url)
        for source_url in tool.get("sources", []):
            tx.run(
                """
                MATCH (t:Tool {slug: $slug})
                MATCH (ki:KnowledgeItem {source_url: $url})
                MERGE (t)-[:REFERENCES]->(ki)
                """,
                slug=tool["slug"],
                url=source_url,
            )

        # DISPLAYED_ON: redactionele keuze per BB-pagina, met display_order
        display_order = tool.get("display_order", {})
        for bb in tool.get("displayed_on", []):
            order = display_order.get(bb, DEFAULT_DISPLAY_ORDER)
            tx.run(
                """
                MATCH (t:Tool {slug: $slug})
                MATCH (b:BuildingBlock {name: $bb_name})
                MERGE (t)-[r:DISPLAYED_ON]->(b)
                SET r.display_order = $order
                """,
                slug=tool["slug"],
                bb_name=bb,
                order=order,
            )

    return len(TOOLS)


def seed_all(session):
    """Run all seed functions. Idempotent via MERGE statements."""
    total = 0

    count = session.execute_write(seed_building_blocks)
    print(f"  BuildingBlocks: {count}")
    total += count

    count = session.execute_write(seed_guardrails)
    print(f"  Guardrails: {count}")
    total += count

    items, topics, authors = session.execute_write(seed_knowledge_items)
    print(f"  KnowledgeItems: {items}")
    print(f"  Topics: {topics}")
    print(f"  Authors: {authors}")
    total += items + topics + authors

    count = session.execute_write(seed_tools)
    print(f"  Tools: {count}")
    total += count

    print(f"\n  Total: {total} nodes seeded")
    return total
