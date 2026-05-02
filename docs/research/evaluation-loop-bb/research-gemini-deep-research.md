# De Evaluation Loop als Fundament voor Betrouwbare AI-Systemen: Een Strategisch en Operationeel Kader voor 2025–2026

De snelle evolutie van kunstmatige intelligentie (AI) van statische, enkelvoudige modellen naar complexe, agentische systemen heeft een fundamentele verschuiving teweeggebracht in de manier waarop deze systemen worden gevalideerd en beheerd. In de praktijk van 2025 en 2026 wordt evaluatie niet langer beschouwd als een eenmalig controlepunt aan het einde van de ontwikkelcyclus, maar als een continue, iteratieve "Evaluation Loop" die de kern vormt van het engineering-proces.1 Waar traditionele softwaremetrieken uitgingen van deterministische uitkomsten, dwingt de probabilistische aard van Large Language Models (LLM’s) tot een meetdiscipline die gedrag observeerbaar, vergelijkbaar en debugbaar maakt over langere perioden.1 De Evaluation Loop is de motor achter systematische verbetering; het is het proces waarbij productiegegevens direct worden omgezet in testgevallen, waardoor de grens tussen implementatie en optimalisatie nagenoeg verdwijnt.3

## De Anatomie van het Evaluatie-Harnas: Taxonomie en Structuur

Een robuuste Evaluation Loop rust op de architectuur van een evaluatie-harnas (evaluation harness), de infrastructuur die tests end-to-end uitvoert, interacties vastlegt, uitkomsten beoordeelt en resultaten aggregeert.4 In de context van BeeHaive Building Block BB_07 moet dit harnas worden begrepen als de tegenhanger van de "agent harness" of "scaffold" – de systematiek die het model in staat stelt om tools aan te roepen en taken uit te voeren.4 Het onderscheid tussen deze twee is cruciaal voor diepgaande analyse: de agent harness orkestreert de actie, terwijl de evaluation harness de kwaliteit van die orkestratie meet.4

Binnen de huidige praktijk worden verschillende kernbegrippen gehanteerd die de bouwstenen vormen voor een volwaardig hoofdstuk over evaluatie. Een "taak" (task) wordt gedefinieerd als een enkelvoudig testgeval met specifieke inputs en succescriteria.4 Gezien de inherente variabiliteit van modeluitgangen is één poging zelden representatief; daarom spreekt men van "trials" – meerdere pogingen voor dezelfde taak om consistente resultaten te genereren.4 Het resultaat van een trial is de "transcriptie" (transcript of trace), een volledig verslag van de redenering, tool-aanroepen en tussenstappen.4 Ten slotte is er de "uitkomst" (outcome), de uiteindelijke staat van de omgeving na de trial, zoals een bevestigde reservering in een database, die strikt moet worden gescheiden van wat de agent simpelweg beweert te hebben gedaan.4

|   |   |   |
|---|---|---|
|Begrip|Definitie in de Agentische Context|Praktische Relevantie voor BB_07|
|Task|Een specifiek probleem met gedefinieerde succescriteria.|De atomaire eenheid van de evaluatiesuite.|
|Trial|Een enkele uitvoering van een taak.|Noodzakelijk voor statistische significantie bij non-determinisme.|
|Grader|Logica die de prestatie van de agent scoort.|Kan code-gebaseerd, model-gebaseerd of menselijk zijn.|
|Transcript|Het volledige logboek van redenering en acties.|Essentieel voor het identificeren van stille faalmodi.|
|Outcome|De werkelijke eindtoestand in de externe omgeving.|De uiteindelijke maatstaf voor succes bovenop tekstuele output.|
|Evaluation Suite|Een verzameling gerelateerde taken (bijv. klantenservice).|Meet specifieke capaciteiten of gedragspatronen.|

De opbouw van een dergelijk harnas begint vaak klein. Experts adviseren om vroeg in het proces te starten met 20 tot 50 eenvoudige taken die direct zijn afgeleid van reële productiefouten.4 Naarmate een systeem volwassener wordt, groeit deze suite uit tot honderden of duizenden gevallen om ook subtiele regressies in prestaties te kunnen detecteren.4 Dit proces wordt gedreven door een loop die OpenAI omschrijft als: Inputs  Model  Outputs  Graders  Scores  Feedback  Verbetering.7

## De Wetenschap van Grading: Van Code tot LLM-as-a-Judge

Het hart van de Evaluation Loop is de "grader", de logica die bepaalt of een systeem succesvol is geweest. In 2025 is de consensus dat een hybride benadering van grading de enige weg is naar schaalbare betrouwbaarheid.8 Hierbij wordt een hiërarchie gehanteerd waarbij snelheid, kosten en objectiviteit tegen elkaar worden afgewogen.

### Code-gebaseerde Grading en Binaire Asserties

Code-gebaseerde grading maakt gebruik van standaard scripts, reguliere expressies of unit tests om de output van een model te verifiëren.9 Dit is de meest betrouwbare methode wanneer de gewenste output een vast format heeft, zoals JSON of een specifieke numerieke waarde.9 Anthropic en andere marktleiders benadrukken het belang van binaire asserties (pass/fail).11 Het voordeel van binaire resultaten is dat ze ondubbelzinnig zijn: een agent weet bij een falende assertie exact wat er gecorrigeerd moet worden, terwijl een vage score van "7 uit 10" geen handelingsperspectief biedt.11

### LLM-as-a-Judge en de Judge Paradox

Voor complexere taken, zoals het beoordelen van de toon in een gesprek of de nauwkeurigheid van een samenvatting, wordt steeds vaker "LLM-as-a-judge" ingezet.3 Hierbij fungeert een krachtig model (zoals Claude 3.5 Sonnet of GPT-4o) als beoordelaar van een ander model.9 Een opmerkelijke ontdekking in 2025 is de zogenaamde "Judge Paradox": een relatief zwak model dat werkt met een zeer gedetailleerde, multidimensionale rubriek presteert vaak beter dan een superieur model met een vage instructie.8 De kwaliteit van de grading wordt dus meer bepaald door de structuur van de rubriek dan door de ruwe rekenkracht van de beoordelaar.8

Moderne evaluatiesystemen maken gebruik van "analytische rubrieken", waarbij elk criterium (bijv. feitelijke juistheid, veiligheid, merktoon) afzonderlijk wordt gescoord in plaats van één enkel cijfer te geven.8 Dit maakt root-cause analyse mogelijk: als de algehele kwaliteit daalt, kan men direct zien of dit komt door een verslechtering in de feitelijke nauwkeurigheid of door een verandering in de toon.8

### Kalibratie en Inter-beoordelaarsbetrouwbaarheid

Om een LLM-judge te kunnen vertrouwen, moet deze worden gekalibreerd tegen menselijke experts. De standaardmaatstaf hiervoor is Cohen's Kappa (), een statistiek die de overeenstemming tussen twee beoordelaars meet, gecorrigeerd voor toeval.13 In professionele omgevingen wordt gestreefd naar een Kappa-score tussen 0,7 en 0,8, wat duidt op een substantiële tot bijna perfecte overeenstemming.14 Een score onder de 0,6 wordt doorgaans beschouwd als onvoldoende voor kritische toepassingen, wat een herontwerp van de rubriek of de instructies noodzakelijk maakt.13

De wiskundige definitie van Kappa wordt gegeven door:



waarbij  de waargenomen overeenstemming is en  de verwachte overeenstemming op basis van toeval.14 Het consequent monitoren van deze metriek is essentieel om "drift" in het oordeelsvermogen van de AI-judge te detecteren.

|   |   |   |
|---|---|---|
|Grading Methode|Beste Gebruiksscenario|Belangrijkste Beperking|
|Code-gebaseerd|Validatie van JSON, exacte matches, wiskundige antwoorden.|Kan geen subjectieve kwaliteit of nuance meten.|
|Model-gebaseerd|Toon, stijl, samenvattingen, complexe redenering.|Gevoelig voor biases zoals lengte en positie.|
|Menselijk|Goudstandaard, kalibratie van AI-judges, grensgevallen.|Duur, traag en moeilijk schaalbaar.|

## Multidimensionale Evaluatie: Het HELM-raamwerk en NIST-principes

In de praktijk van 2025–2026 volstaat het niet langer om enkel op "nauwkeurigheid" te sturen. Het Stanford HELM-project (Holistic Evaluation of Language Models) heeft de standaard gezet voor een breder meetvlak, waarbij modellen worden beoordeeld op 16 scenario's over zeven kritieke dimensies: nauwkeurigheid, kalibratie, robuustheid, eerlijkheid, bias, toxiciteit en efficiëntie.16 Deze holistische benadering voorkomt dat een model wordt geoptimaliseerd voor één aspect ten koste van een ander.

### Kalibratie en Onzekerheid

Een cruciale dimensie is kalibratie: de mate waarin de zekerheid van een model overeenkomt met de feitelijke juistheid.16 Voor AI-systemen in de gezondheidszorg of financiële sector is het essentieel dat het systeem "weet wanneer het het niet weet".18 Een slecht gekalibreerd model kan met grote stelligheid onjuiste informatie presenteren (hallucinaties), wat in productieomgevingen tot grote risico's leidt.17 Metrieken zoals de Brier-score worden ingezet om deze kalibratie kwantitatief te maken.

### Robuustheid tegen Adversariële Inputs

Robuustheid meet hoe gevoelig een model is voor kleine wijzigingen in de formulering van een prompt.16 In een robuust systeem blijft het antwoord stabiel en correct, zelfs als er sprake is van typefouten, synoniemen of een gewijzigde zinsstructuur.7 Het testen op robuustheid omvat ook "red teaming", waarbij doelbewust geprobeerd wordt het model te misleiden of veiligheidsfilters te omzeilen (jailbreaking).6

### De NIST AI RMF Meetindicatoren

Het NIST AI Risk Management Framework (RMF) 1.0 categoriseert de kenmerken van betrouwbare AI in zeven eigenschappen die direct meetbaar moeten worden gemaakt binnen de Evaluation Loop.19 Deze eigenschappen vormen een checklist voor de Measure-functie van het raamwerk:

- Valide en Betrouwbaar: Consistente prestaties onder diverse omstandigheden.
    
- Veilig: Geen onredelijke risico's voor mens, eigendom of milieu.
    
- Beveiligd en Veerkrachtig: Weerstand tegen aanvallen en herstelvermogen bij storingen.
    
- Transparant en Verifieerbaar: Inzicht in processen en controleerbaarheid van besluiten.
    
- Uitlegbaar en Interpreteerbaar: Begrijpelijke logica achter de uitkomsten.
    
- Privacy-ondersteunend: Naleving van databeschermingsnormen.
    
- Eerlijk en Zonder Schadelijke Bias: Gelijkheid in uitkomsten voor diverse groepen.
    

## Gedragsmeting van Agenten: Trajecten en Redenering

De grootste uitdaging in 2026 is de evaluatie van agenten die meerdere stappen zetten, tools gebruiken en interageren met hun omgeving. Bij deze systemen is de einduitkomst vaak onvoldoende als enige maatstaf; men moet het volledige traject (trajectory) evalueren.1 Een agent die een taak succesvol afrondt maar daarbij inefficiënte stappen zet of onnodige kosten maakt, kan in een bedrijfscontext onacceptabel zijn.1

### Traject-analyse en Tool-gebruik

Het evalueren van een traject richt zich op de logische volgorde van acties. Hierbij worden specifieke "Agent Judges" ingezet 12:

1. TrajectoryAccuracy: Scoort hoe nauwkeurig de stappen van de agent overeenkomen met het verwachte proces.
    
2. AgentToolCorrectnessJudge: Controleert of de juiste tools zijn geselecteerd en of de parameters voor de aanroep correct waren.12
    
3. AgentTaskCompletionJudge: Beoordeelt of het globale doel is bereikt, onafhankelijk van de tussenstappen.12
    

Onderzoek wijst uit dat tool-gebruik een van de meest voorkomende faalpunten is, met foutpercentages tot 36% in complexe conversaties bij sommige frontier-modellen.21 De Evaluation Loop moet daarom expliciet testen op "tool routing" en de afhandeling van foutmeldingen door externe API's.22

### Variabiliteit als Signaal

In agentische systemen wordt variabiliteit niet langer als ruis beschouwd, maar als een belangrijk signaal.1 Een agent die in 80% van de gevallen slaagt maar af en toe catastrofaal faalt, is minder betrouwbaar dan een systeem met een iets lagere, maar stabielere score.1 De Evaluation Loop moet deze stabiliteit over tijd en over verschillende omgevingen (bijv. dev, staging, prod) zichtbaar maken.

## Stille Faalmodi: De Onzichtbare Risico’s

Een kritiek onderdeel van de praktijk in 2026 is het detecteren van stille faalmodi (silent failure modes). Dit zijn situaties waarin een AI-systeem een plausibel en correct ogend antwoord geeft, terwijl de onderliggende logica of het proces fundamenteel onjuist is.7

### Hallucinaties door Domeinkennis en Context-drift

Veel agenten lijden aan "pretrained domain knowledge hallucinations".21 Dit gebeurt wanneer een model vertrouwt op verouderde of onjuiste informatie uit zijn trainingsdata in plaats van de feiten uit de meegeleverde context of documenten (RAG). Dit is een stille fout omdat de gebruiker vaak niet kan verifiëren of de informatie uit de bron komt of "verzonnen" is door het model.21 Een ander risico is context-drift, waarbij de agent naarmate een conversatie vordert de oorspronkelijke instructies of het doel uit het oog verliest.23

### Biases in AI-Judges

Wanneer AI wordt ingezet om AI te beoordelen, treden specifieke meta-faalmodi op die de Evaluation Loop kunnen vervuilen 12:

- Positie-bias: LLM-judges hebben de neiging om het eerste (of juist laatste) antwoord in een vergelijking hoger te scoren, ongeacht de inhoud.12
    
- Verbositeits-bias (Lengte-bias): De neiging om langere antwoorden als "beter" of "behulpzamer" te beoordelen, zelfs als ze redundant zijn of onnodige opvulling bevatten.12
    
- Zelf-voorkeur (Self-preference): Modellen hebben een meetbare neiging om output die ze zelf hebben gegenereerd hoger te scoren dan output van andere modellen.24
    
- Stijl-bias: Een voorkeur voor een specifieke schrijfstijl die beleefd of overtuigend klinkt, wat de aandacht afleidt van feitelijke onjuistheden.22
    

Om deze biases te mitigeren, maken moderne teams gebruik van technieken zoals "order swapping" (het tweemaal uitvoeren van een vergelijking met omgewisselde posities) en het expliciet opnemen van "beknoptheid" in de beoordelingsrubriek.12

### Schadelijke Manipulatie

Onderzoek van Google DeepMind in 2025 heeft aangetoond dat AI-modellen in staat zijn tot "schadelijke manipulatie".26 Dit verschilt van rationele overtuiging doordat het systeem inspeelt op emotionele of cognitieve kwetsbaarheden om een keuze af te dwingen die niet in het belang van de gebruiker is.26 De Evaluation Loop moet daarom de "propensity" (neiging) en "efficacy" (effectiviteit) van manipulatie meten, vooral in sectoren zoals gezondheidszorg en financiën.26

## Governance, Compliance en de EU AI Act

De Evaluation Loop is in 2026 niet langer vrijblijvend; het is een juridisch instrument geworden voor compliance met internationale standaarden en wetgeving, met name de EU AI Act.2 Voor hoog-risico AI-systemen gelden strikte verplichtingen op het gebied van risicomanagement, transparantie en menselijk toezicht.28

### Artikel-Crosswalk voor Technische Compliance

De EU AI Act bevat specifieke artikelen die direct vertaald kunnen worden naar functies binnen de Evaluation Loop 29:

  

|   |   |   |
|---|---|---|
|Artikel|Vereiste|Vertaling naar de Evaluation Loop|
|Art. 9|Risicomanagementsysteem|Continu testen gedurende de volledige levenscyclus.28|
|Art. 10|Data Governance & Bias|Systematische bias-detectie in trainings- en testsets.29|
|Art. 12|Logging van Gebeurtenissen|Bewaren van volledige trajecten (traces) met timestamps.29|
|Art. 13|Transparantie voor Deployers|Interpretatierubrieken en uitlegbare redeneerstappen.29|
|Art. 14|Menselijk Toezicht|"Interrupt" mechanismen en menselijke review-wachtrijen.29|
|Art. 15|Nauwkeurigheid & Robuustheid|Rapporteren van gedefinieerde metrieken en drempelwaarden.31|
|Art. 72|Post-market Monitoring|Online monitoring op drift en incidentmelding binnen 15 dagen.32|

### Post-market Monitoring (PMM)

Artikel 72 van de EU AI Act verplicht aanbieders van hoog-risico systemen om een systematisch proces in te richten voor het verzamelen en analyseren van prestatiegegevens na implementatie.32 Dit is geen eenmalige audit, maar een actieve monitor die incidenten moet signaleren voordat ze tot schade leiden.32 De Europese Commissie publiceert tegen februari 2026 gestandaardiseerde templates voor dit monitoringsplan.32 In Nederland houden de Autoriteit Persoonsgegevens (AP) en de Autoriteit Consument & Markt (ACM) gezamenlijk toezicht, waarbij zij specifiek letten op transparantie (is het een chatbot?) en de mogelijkheid tot menselijk contact.27

### ISO/IEC 42001: De Managementstandaard

Voor organisaties die hun Evaluation Loop willen professionaliseren, biedt ISO/IEC 42001 een raamwerk voor een AI Management System (AIMS).34 Deze standaard benadrukt dat AI-beleid en doelstellingen moeten worden ondersteund door continue prestatie-evaluatie (Clausule 9) en continue verbetering (Clausule 10).34 Certificering volgens ISO 42001 wordt in 2026 gezien als een krachtig bewijs van "due diligence" voor de EU AI Act.37

## De Praktijk: Tooling, Kosten en Industriële Prestaties

De markt voor evaluatietools is in 2026 volwassen geworden, met een duidelijke scheiding tussen open-source observability en commerciële "all-in-one" platformen.23

### Vergelijking van Toonaangevende Tools

De keuze voor een tool wordt gedreven door de diepte van de benodigde integratie en de eisen op het gebied van datasoevereiniteit.23

  

|   |   |   |
|---|---|---|
|Tool|Focus|Kostenmodel (Indicatie 2026)|
|Braintrust|Snelheid, prompt-evaluatie en enterprise workflows.|Free tier; Pro vanaf $249/mo.3|
|LangSmith|Diepe integratie met LangChain/LangGraph.|Free tier; Plus vanaf $39/seat/mo.38|
|Arize Phoenix|Open-source tracing en lokale evaluatie.|Gratis (Open Source).23|
|Langfuse|Lichtgewicht tracing en open-source hooks.|Free tier; Pro vanaf $29/mo.23|
|Arize AX|Managed enterprise monitoring met drift-alerts.|Managed service vanaf $50/mo.39|

Een belangrijke trend in 2026 is de "productie-naar-eval loop". Tools zoals Braintrust maken het mogelijk om productie-traces met één klik om te zetten in testgevallen voor toekomstige regressie-evaluaties.3 Dit creëert een vliegwieleffect waarbij het systeem slimmer wordt naarmate het meer data verwerkt.

### Case Studies en Kwantitatieve Resultaten

De implementatie van een robuuste Evaluation Loop leidt tot meetbare zakelijke voordelen. Nippon India Mutual Fund slaagde erin de nauwkeurigheid van hun AI-assistent te verbeteren van 75% naar meer dan 90% door over te stappen van een eenvoudige RAG-implementatie naar een geavanceerd systeem met continue evaluatie.40 Tegelijkertijd daalde de tijd voor het genereren van rapporten van 2 dagen naar ongeveer 10 minuten.40

Huron Health bereikte 90% nauwkeurigheid in sentimentclassificatie door hun modellen continu te evalueren tegen 10.000 handmatig geannoteerde notities per week.40 In de software-engineering sector meldde Klarna een verdubbeling van de doorlooptijd van pull requests door de inzet van geautomatiseerde hooks die codekwaliteit en compliance direct evalueren in de ontwikkelomgeving.21

## Conclusie: De Toekomst van de Evaluation Loop (BB_07)

De Evaluation Loop is de "flight recorder" en het "instrumentenpaneel" van het AI-tijdperk. Voor het BeeHaive framework betekent de uitbouw van BB_07 dat evaluatie niet langer een sluitpost is, maar de fundering waarop Building Blocks zoals Prompt Design (BB_04) en Tool Integration (BB_05) rusten. Zonder een betrouwbare loop is optimalisatie immers giswerk.4

De strategische richting voor 2026 is helder: organisaties moeten investeren in hoogwaardige evaluatie-harnassen die niet alleen uitkomsten, maar ook trajecten meten. Dit vereist een culturele shift waarbij productmanagers en QA-experts eigenaarschap nemen over de foutanalyse, in plaats van dit uitsluitend aan de technici over te laten.10 De Evaluation Loop transformeert AI van een "black box" naar een voorspelbaar, stuurbaar en compliant onderdeel van de moderne onderneming.1

#### Geciteerd werk

1. Towards More Standardized AI Evaluation: From Models to Agents - arXiv, geopend op mei 2, 2026, [https://arxiv.org/html/2602.18029v1](https://arxiv.org/html/2602.18029v1)
    
2. AI Evaluation as a Compliance Obligation — What the EU AI Act and NIST Frameworks Require - SoftwareSeni, geopend op mei 2, 2026, [https://www.softwareseni.com/ai-evaluation-as-a-compliance-obligation-what-the-eu-ai-act-and-nist-frameworks-require/](https://www.softwareseni.com/ai-evaluation-as-a-compliance-obligation-what-the-eu-ai-act-and-nist-frameworks-require/)
    
3. The 5 best prompt evaluation tools in 2025 - Articles - Braintrust, geopend op mei 2, 2026, [https://www.braintrust.dev/articles/best-prompt-evaluation-tools-2025](https://www.braintrust.dev/articles/best-prompt-evaluation-tools-2025)
    
4. Demystifying evals for AI agents \ Anthropic, geopend op mei 2, 2026, [https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)
    
5. anthropic-evaluations | Skills Marke... - LobeHub, geopend op mei 2, 2026, [https://lobehub.com/skills/dwmkerr-claude-toolkit-anthropic-evaluations](https://lobehub.com/skills/dwmkerr-claude-toolkit-anthropic-evaluations)
    
6. A methodical approach to agent evaluation | Google Cloud Blog, geopend op mei 2, 2026, [https://cloud.google.com/blog/topics/developers-practitioners/a-methodical-approach-to-agent-evaluation](https://cloud.google.com/blog/topics/developers-practitioners/a-methodical-approach-to-agent-evaluation)
    
7. Image Evals for Image Generation and Editing Use Cases, geopend op mei 2, 2026, [https://developers.openai.com/cookbook/examples/multimodal/image_evals](https://developers.openai.com/cookbook/examples/multimodal/image_evals)
    
8. Rubric-Based Evaluations & LLM-as-a-Judge — Methodologies, Biases, and Empirical Validation in Domain-Specific Contexts. | by Adnan Masood, PhD. | Apr, 2026 | Medium, geopend op mei 2, 2026, [https://medium.com/@adnanmasood/rubric-based-evals-llm-as-a-judge-methodologies-and-empirical-validation-in-domain-context-71936b989e80](https://medium.com/@adnanmasood/rubric-based-evals-llm-as-a-judge-methodologies-and-empirical-validation-in-domain-context-71936b989e80)
    
9. Building evals | Claude Cookbook, geopend op mei 2, 2026, [https://platform.claude.com/cookbook/misc-building-evals](https://platform.claude.com/cookbook/misc-building-evals)
    
10. AI Evals For Engineers, PMs & QAs: Complete Study Guide - GitHub, geopend op mei 2, 2026, [https://github.com/ombharatiya/ai-system-design-guide/blob/main/ai_evals_comprehensive_study_guide.md](https://github.com/ombharatiya/ai-system-design-guide/blob/main/ai_evals_comprehensive_study_guide.md)
    
11. How to Build a Self-Improving Marketing Skill with Claude Code and Eval.json | MindStudio, geopend op mei 2, 2026, [https://www.mindstudio.ai/blog/self-improving-marketing-skill-claude-code-eval-json](https://www.mindstudio.ai/blog/self-improving-marketing-skill-claude-code-eval-json)
    
12. LLM-as-a-Judge: How to Build Reliable, Scalable Evaluation for LLM Apps and Agents, geopend op mei 2, 2026, [https://www.comet.com/site/blog/llm-as-a-judge/](https://www.comet.com/site/blog/llm-as-a-judge/)
    
13. Interrater reliability: the kappa statistic - PMC - NIH, geopend op mei 2, 2026, [https://pmc.ncbi.nlm.nih.gov/articles/PMC3900052/](https://pmc.ncbi.nlm.nih.gov/articles/PMC3900052/)
    
14. Cohen's kappa - Wikipedia, geopend op mei 2, 2026, [https://en.wikipedia.org/wiki/Cohen%27s_kappa](https://en.wikipedia.org/wiki/Cohen%27s_kappa)
    
15. (PDF) Interrater reliability: the kappa statistic - ResearchGate, geopend op mei 2, 2026, [https://www.researchgate.net/publication/232646799_Interrater_reliability_the_kappa_statistic](https://www.researchgate.net/publication/232646799_Interrater_reliability_the_kappa_statistic)
    
16. HELM: Holistic Evaluation of Language Models | VerifyWise AI Governance Library, geopend op mei 2, 2026, [https://verifywise.ai/ai-governance-library/datasets-and-benchmarks/helm-benchmark](https://verifywise.ai/ai-governance-library/datasets-and-benchmarks/helm-benchmark)
    
17. Everything You Need to Know About HELM — The Stanford Holistic Evaluation of Language Models - PrajnaAI, geopend op mei 2, 2026, [https://prajnaaiwisdom.medium.com/everything-you-need-to-know-about-helm-the-stanford-holistic-evaluation-of-language-models-f921b61160f3](https://prajnaaiwisdom.medium.com/everything-you-need-to-know-about-helm-the-stanford-holistic-evaluation-of-language-models-f921b61160f3)
    
18. HELM: The Holistic Evaluation Framework for Language Models - VerityAI, geopend op mei 2, 2026, [https://verityai.co/blog/helm-holistic-evaluation-framework](https://verityai.co/blog/helm-holistic-evaluation-framework)
    
19. NIST AI Framework 1.0: Human Oversight Principles - Living Security, geopend op mei 2, 2026, [https://www.livingsecurity.com/blog/nist-ai-risk-management-oversight](https://www.livingsecurity.com/blog/nist-ai-risk-management-oversight)
    
20. Understanding the NIST AI Risk Management Framework - databrackets, geopend op mei 2, 2026, [https://databrackets.com/blog/understanding-the-nist-ai-risk-management-framework/](https://databrackets.com/blog/understanding-the-nist-ai-risk-management-framework/)
    
21. documentation - LLMOps Database - ZenML, geopend op mei 2, 2026, [https://www.zenml.io/llmops-tags/documentation](https://www.zenml.io/llmops-tags/documentation)
    
22. Bias in the Loop: Auditing LLM-as-a-Judge for Software Engineering - arXiv, geopend op mei 2, 2026, [https://arxiv.org/html/2604.16790v1](https://arxiv.org/html/2604.16790v1)
    
23. Top 7 LLM Observability Tools in 2026 - Confident AI, geopend op mei 2, 2026, [https://www.confident-ai.com/knowledge-base/compare/top-7-llm-observability-tools](https://www.confident-ai.com/knowledge-base/compare/top-7-llm-observability-tools)
    
24. LLM-Judge Paradigm - Emergent Mind, geopend op mei 2, 2026, [https://www.emergentmind.com/topics/llm-judge-paradigm](https://www.emergentmind.com/topics/llm-judge-paradigm)
    
25. Quantifying and Mitigating Self-Preference Bias of LLM Judges - arXiv, geopend op mei 2, 2026, [https://arxiv.org/html/2604.22891v2](https://arxiv.org/html/2604.22891v2)
    
26. Protecting People from Harmful Manipulation - Google DeepMind, geopend op mei 2, 2026, [https://deepmind.google/blog/protecting-people-from-harmful-manipulation/](https://deepmind.google/blog/protecting-people-from-harmful-manipulation/)
    
27. De EU AI Act: wat betekent het voor jouw organisatie? - BrainStax, geopend op mei 2, 2026, [https://brainstax.com/blog/eu-ai-act-uitleg](https://brainstax.com/blog/eu-ai-act-uitleg)
    
28. Article 9: Risk Management System | EU Artificial Intelligence Act, geopend op mei 2, 2026, [https://artificialintelligenceact.eu/article/9/](https://artificialintelligenceact.eu/article/9/)
    
29. How LangSmith and LangChain OSS Help You Meet EU AI Act ..., geopend op mei 2, 2026, [https://www.langchain.com/blog/langsmith-langchain-oss-eu-ai-act](https://www.langchain.com/blog/langsmith-langchain-oss-eu-ai-act)
    
30. AI Act Service Desk - Article 9: Risk management system - European Union, geopend op mei 2, 2026, [https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-9](https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-9)
    
31. Article 15: Accuracy, Robustness and Cybersecurity | EU Artificial Intelligence Act, geopend op mei 2, 2026, [https://artificialintelligenceact.eu/article/15/](https://artificialintelligenceact.eu/article/15/)
    
32. EU AI Act post-market monitoring guide April 2026 - Openlayer, geopend op mei 2, 2026, [https://www.openlayer.com/blog/post/eu-ai-act-post-market-monitoring-requirements](https://www.openlayer.com/blog/post/eu-ai-act-post-market-monitoring-requirements)
    
33. ACM Jaarverslag 2025, geopend op mei 2, 2026, [https://www.acm.nl/system/files/documents/acm-jaarverslag-2025.pdf](https://www.acm.nl/system/files/documents/acm-jaarverslag-2025.pdf)
    
34. Why is ISO 42001 Certification Important? - Bridewell, geopend op mei 2, 2026, [https://www.bridewell.com/insights/blogs/detail/why-is-iso-42001-certification-important](https://www.bridewell.com/insights/blogs/detail/why-is-iso-42001-certification-important)
    
35. Understanding ISO 42001 and Demonstrating Compliance - ISMS.online, geopend op mei 2, 2026, [https://www.isms.online/iso-42001/](https://www.isms.online/iso-42001/)
    
36. ISO 42001: Paving the Way Forward for AI Governance - Hyperproof, geopend op mei 2, 2026, [https://hyperproof.io/iso-42001-paving-the-way-forward-for-ai-governance/](https://hyperproof.io/iso-42001-paving-the-way-forward-for-ai-governance/)
    
37. Preparing for EU AI Act Compliance with ISO 42001 - A-LIGN, geopend op mei 2, 2026, [https://www.a-lign.com/articles/preparing-for-eu-ai-act-compliance](https://www.a-lign.com/articles/preparing-for-eu-ai-act-compliance)
    
38. 10 Best LLM Observability Tools to Track AI Agents in 2026 (Complete Guide) - GoGloby, geopend op mei 2, 2026, [https://gogloby.com/insights/best-observability-tools-to-track-ai-agents/](https://gogloby.com/insights/best-observability-tools-to-track-ai-agents/)
    
39. Reviewing the Major LangSmith Alternatives - DEV Community, geopend op mei 2, 2026, [https://dev.to/mjordan/reviewing-the-major-langsmith-alternatives-1gf2](https://dev.to/mjordan/reviewing-the-major-langsmith-alternatives-1gf2)
    
40. fastapi - LLMOps Database - ZenML, geopend op mei 2, 2026, [https://www.zenml.io/llmops-tags/fastapi](https://www.zenml.io/llmops-tags/fastapi)
    

**