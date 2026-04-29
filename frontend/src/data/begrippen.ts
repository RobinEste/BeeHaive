/**
 * Begrippen — single source of truth voor de /begrippen pagina
 * en voor in-line term-links vanuit BB- en GR-pagina's.
 *
 * Bron: .claude/schrijfstijl-bb.md §4. Groeit per BB/GR die we afronden.
 */

export type Categorie =
  | 'ai-basis'
  | 'retrieval'
  | 'geheugen'
  | 'kwaliteit'
  | 'privacy';

export interface Term {
  slug: string;
  naam: string;
  engels?: string;
  uitleg: string;
  categorie: Categorie;
  zieOok?: string[];
}

export const CATEGORIE_LABELS: Record<Categorie, string> = {
  'ai-basis': 'AI-basis',
  retrieval: 'Retrieval & kennis',
  geheugen: 'Geheugen & koppeling',
  kwaliteit: 'Kwaliteit & actualiteit',
  privacy: 'Privacy & governance',
};

export const CATEGORIE_INTROS: Record<Categorie, string> = {
  'ai-basis':
    'De fundamenten: wat is een taalmodel eigenlijk, en welke bouwsteentjes komen in bijna elke AI-context terug.',
  retrieval:
    'Hoe AI-systemen informatie uit een kennisbank of documenten halen om hun antwoord op te baseren.',
  geheugen:
    'Hoe AI-systemen informatie onthouden over gesprekken, sessies en externe tools heen.',
  kwaliteit:
    'Wat er typisch misgaat in de context-laag van een AI-systeem, en hoe je dat kunt meten.',
  privacy:
    'Technieken en principes om persoonsgegevens en herkomst van antwoorden onder controle te houden.',
};

export const BEGRIPPEN: Term[] = [
  // ─── AI-basis ──────────────────────────────────────────────────────
  {
    slug: 'agent',
    naam: 'Agent',
    uitleg:
      'AI-systeem dat zelfstandig acties uitvoert: redeneert, gebruikt tools en bepaalt op basis van tussenresultaten de volgende stap. In tegenstelling tot een chatbot, die één vraag per keer beantwoordt, stuurt een agent een hele cyclus aan.',
    categorie: 'ai-basis',
    zieOok: ['prompt', 'context-window'],
  },
  {
    slug: 'prompt',
    naam: 'Prompt',
    uitleg:
      'De instructie die je aan een AI-model geeft: een vraag, opdracht of set met aanwijzingen, inclusief de context waarbinnen het model moet werken.',
    categorie: 'ai-basis',
    zieOok: ['token', 'context-window'],
  },
  {
    slug: 'system-prompt',
    naam: 'System prompt',
    uitleg:
      'De overkoepelende instructie die het gedrag van een AI-systeem over álle gesprekken heen stuurt — in tegenstelling tot een single-turn prompt die maar één interactie bestuurt. Een system prompt formuleert doel, toon, afhandeling van onverwachte situaties en een prioriteitenladder (welke regel wint als er conflict is). De drie grote AI-leveranciers (Anthropic, OpenAI, Google) bevelen system prompts expliciet aan voor iedere productie-toepassing.',
    categorie: 'ai-basis',
    zieOok: ['prompt', 'few-shot'],
  },
  {
    slug: 'few-shot',
    naam: 'Few-shot prompting',
    uitleg:
      'Techniek waarbij je 2–5 diverse voorbeelden van ideale input-outputparen in de prompt meegeeft, zodat het model zich kalibreert op gedrag dat moeilijk in expliciete regels te vangen is. Werkt bijzonder goed voor gestructureerde output, toon-matching en niche-classificatie. Tegenhanger: zero-shot (geen voorbeelden, alleen instructie).',
    categorie: 'ai-basis',
    zieOok: ['prompt', 'system-prompt'],
  },
  {
    slug: 'token',
    naam: 'Token',
    uitleg:
      'Het stukje tekst waarin een taalmodel tekst opbreekt om ermee te kunnen rekenen. Eén token is grofweg 3 tot 4 letters; 1 miljoen tokens komt ongeveer overeen met 750.000 woorden.',
    categorie: 'ai-basis',
    zieOok: ['context-window', 'prompt'],
  },
  {
    slug: 'context-window',
    naam: 'Context window',
    uitleg:
      'De hoeveelheid tekst die een taalmodel in één keer kan verwerken, uitgedrukt in tokens. Alles wat je het model stuurt — prompt, eerdere gesprekshistorie, opgehaalde documenten — moet samen binnen dit window passen.',
    categorie: 'ai-basis',
    zieOok: ['token', 'context-rot'],
  },
  {
    slug: 'hallucinatie',
    naam: 'Hallucinatie',
    uitleg:
      'Antwoord van een AI-model waarin feiten worden verzonnen die plausibel klinken maar niet kloppen. Een model dat "liever iets zegt dan niets" produceert hallucinaties — vaak met volle zelfverzekerdheid.',
    categorie: 'ai-basis',
    zieOok: ['rag', 'faithfulness'],
  },
  {
    slug: 'degradeert',
    naam: 'Degraderen',
    uitleg:
      'In kwaliteit achteruitgaan. Bij AI-modellen vaak gebruikt voor output die slechter wordt naarmate de context langer wordt, of voor een kennisbank die verouderd raakt zonder dat iemand het merkt.',
    categorie: 'ai-basis',
    zieOok: ['context-rot', 'stale-context'],
  },
  {
    slug: 'jagged-frontier',
    naam: 'Jagged frontier',
    engels: 'Jagged frontier',
    uitleg:
      'De onvoorspelbare, taakafhankelijke grens tussen wat AI goed kan en waar het subtiel faalt. Onderzoek van Dell’Acqua et al. (Harvard/BCG, 2023) liet zien dat consultants buiten die grens 19 procentpunten minder nauwkeurig werden als ze AI gebruikten. Je leert de frontier niet uit handleiding of training — alleen door uitgebreide praktijkervaring met reflectie op wat werkte en wat niet.',
    categorie: 'ai-basis',
    zieOok: ['hallucinatie', 'operating-agreement'],
  },
  {
    slug: 'operating-agreement',
    naam: 'Operating agreement',
    engels: 'Operating agreement',
    uitleg:
      'Een schriftelijke afspraak per AI-ondersteund proces waarin staat wie welk besluit neemt, waar human-in-the-loop zit, welke escalatietriggers gelden en hoe "klaar" eruit ziet. Door Chris Lema gepositioneerd als de overgang van ad-hoc AI-gebruik naar volwassen samenwerking: "This is what separates people who use AI from people who work with AI." Het is het concrete instrument waarmee expertise wordt geëxternaliseerd zodat een AI-systeem ermee kan werken.',
    categorie: 'ai-basis',
    zieOok: ['jagged-frontier', 'fobo'],
  },
  {
    slug: 'fobo',
    naam: 'FOBO',
    engels: 'Fear of Becoming Obsolete',
    uitleg:
      'De angst van medewerkers dat AI hen overbodig maakt — en de stille drijfveer achter AI-vermijding. Fortune/WalkMe (2026, n=3.750) mat dat ~80% van kenniswerkers AI-tools actief vermijdt of omzeilt, niet omdat de technologie niet werkt, maar uit FOBO. De vertrouwenskloof tussen leidinggevenden en medewerkers over AI is vaak 50+ punten. Technische training zonder FOBO-adressering lost hier niets op.',
    categorie: 'ai-basis',
    zieOok: ['operating-agreement'],
  },
  {
    slug: 'decision-intelligence',
    naam: 'Decision Intelligence',
    uitleg:
      'Discipline (Cassie Kozyrkov) die stelt dat het knelpunt in het AI-tijdperk verschuift van technische uitvoering naar menselijk oordeelsvermogen. Onderscheidt de "genie-kant" (tools, prompts, modellen) van de "wens-kant" (welke beslissing, voor wie, waarom, met welke acceptabele fout). Organisaties die alleen in de genie-kant investeren missen het essentieelste niveau.',
    categorie: 'ai-basis',
    zieOok: ['operating-agreement', 'jagged-frontier'],
  },
  {
    slug: 'centaur-cyborg',
    naam: 'Centaur en cyborg',
    uitleg:
      'Twee empirisch werkende samenwerkingspatronen tussen mens en AI (Mollick/Dell\'Acqua). Centaur: duidelijke taakscheiding — mens doet deel A, AI doet deel B. Cyborg: diepe integratie — continue heen-en-weer interactie, AI verweven in elke stap. Centaur houdt menselijke competentie actiever; cyborg is efficiënter binnen de jagged frontier maar geeft risico op grensblindheid. Beide vereisen dat je de frontier kent.',
    categorie: 'ai-basis',
    zieOok: ['jagged-frontier', 'orchestrator'],
  },
  {
    slug: 'orchestrator',
    naam: 'Orchestrator',
    uitleg:
      'De rol waarin een mens een systeem van AI-agents ontwerpt en bewaakt, in plaats van zelf één taak naast AI uit te voeren. KPMG (2026) onderscheidt vier agent-archetypes — Taskers, Automators, Collaborators en Orchestrators — waarbij de mens naar de orchestrator-laag schuift: bepalen wie wat doet, hoe resultaten worden beoordeeld en wanneer er wordt ingegrepen. Breidt het centaur/cyborg-kader uit voor het agents-tijdperk.',
    categorie: 'ai-basis',
    zieOok: ['agent', 'centaur-cyborg', 'operating-agreement'],
  },
  {
    slug: 'deskilling',
    naam: 'Deskilling',
    uitleg:
      'Het eroderen van menselijke expertise doordat AI taken overneemt en de professional stopt met actief oefenen. Klinisch bewezen in Budzyń et al. (Lancet 2025): ervaren endoscopisten zagen hun adenoom-detectiepercentage in drie maanden dalen van 28% naar 22% op procedures zónder AI. Tegenmaatregel: bewust competentieonderhoud — kritieke taken periodiek zonder AI oefenen, ook als AI ze aankan.',
    categorie: 'ai-basis',
    zieOok: ['jagged-frontier', 'operating-agreement'],
  },

  // ─── Retrieval & kennis ────────────────────────────────────────────
  {
    slug: 'rag',
    naam: 'RAG',
    engels: 'Retrieval-Augmented Generation',
    uitleg:
      'Documenten ophalen uit een kennisbank en meegeven aan het taalmodel, zodat het antwoord geworteld is in echte bronnen in plaats van alleen in wat het model tijdens training heeft geleerd. De standaard-aanpak om AI-systemen toegang te geven tot actuele of organisatie-specifieke informatie.',
    categorie: 'retrieval',
    zieOok: ['chunks', 'embedding', 'reranker'],
  },
  {
    slug: 'chunks',
    naam: 'Chunks',
    uitleg:
      'De stukjes waarin een document wordt opgeknipt voordat het in een kennisbank terechtkomt. Te grote chunks laten het model zwemmen in ruis; te kleine chunks verliezen context. De kwaliteit van chunking heeft vaak meer impact op prestaties dan de keuze van het taalmodel zelf.',
    categorie: 'retrieval',
    zieOok: ['rag', 'embedding'],
  },
  {
    slug: 'embedding',
    naam: 'Embedding',
    uitleg:
      'Een wiskundige representatie van tekst — een reeks getallen — waarmee semantische gelijkenis meetbaar wordt. Twee stukjes tekst die hetzelfde betekenen krijgen wiskundig vergelijkbare embeddings, ook als de exacte woorden verschillen.',
    categorie: 'retrieval',
    zieOok: ['chunks', 'rag'],
  },
  {
    slug: 'reranker',
    naam: 'Reranker',
    uitleg:
      'Een tweede-pass-model dat de eerste lijst opgehaalde documenten herordent op werkelijke relevantie. Waar de eerste ophaalslag vraag en documenten los vergelijkt, leest een reranker beide sámen — wat fijnere relevantiebepaling oplevert.',
    categorie: 'retrieval',
    zieOok: ['rag', 'hybrid-search'],
  },
  {
    slug: 'hybrid-search',
    naam: 'Hybride zoeken',
    engels: 'hybrid search',
    uitleg:
      'Combinatie van semantisch zoeken (op betekenis) en keyword-zoeken (op exacte termen). Voor zakelijke vragen met precieze productnamen, ticket-ID\'s of artikelverwijzingen onmisbaar — pure semantische zoekopdrachten missen exacte matches te vaak.',
    categorie: 'retrieval',
    zieOok: ['rag', 'reranker'],
  },
  {
    slug: 'graphrag',
    naam: 'GraphRAG',
    uitleg:
      'Variant van RAG waarbij de kennisbank niet uit losse documenten bestaat maar uit een kennisnetwerk: entiteiten (klanten, leveranciers, projecten) als knooppunten, relaties tussen die entiteiten als verbindingen. Geschikt voor vragen die meerdere stappen vereisen ("welke klanten werken samen met welke leveranciers?"), maar verhoogt wel de kans op privacy-lekkage van gestructureerde relatie-informatie.',
    categorie: 'retrieval',
    zieOok: ['rag', 'pii'],
  },
  {
    slug: 'top-k',
    naam: 'Top-K',
    uitleg:
      'De K meest gelijkende documenten of fragmenten die een zoeksysteem teruggeeft bij een vraag — typisch K=5, 10 of 20. Lage K geeft minder ruis maar riskeert relevante context missen; hoge K geeft meer dekking maar vraagt vaak een reranker achteraf om de werkelijke toppers bovenaan te zetten.',
    categorie: 'retrieval',
    zieOok: ['rag', 'reranker'],
  },
  {
    slug: 'bm25',
    naam: 'BM25',
    engels: 'Best Matching 25',
    uitleg:
      'Klassiek keyword-matching-algoritme dat documenten scoort op hoe vaak zoektermen erin voorkomen, gewogen naar hoe zeldzaam die termen zijn. Onmisbaar naast semantisch zoeken: voor precieze productcodes, artikelnummers of wetsartikelen mist een puur semantische zoektocht de exacte match te vaak. BM25 vult dat gat.',
    categorie: 'retrieval',
    zieOok: ['hybrid-search', 'rag'],
  },
  {
    slug: 'contextual-retrieval',
    naam: 'Contextual Retrieval',
    uitleg:
      'Anthropic-methode (2024) die elk chunk voor indexering voorziet van een korte contextuele annotatie (50–100 tokens) — document-titel, periode, onderwerp. Daardoor blijft een chunk als "de vennootschap groeide 3%" ook los van zijn document vindbaar als het hoort bij ACME Corp Q2 2023. Reduceert retrieval-fouten met 35% solo, tot 67% in combinatie met BM25 en reranker.',
    categorie: 'retrieval',
    zieOok: ['chunks', 'reranker', 'bm25'],
  },
  {
    slug: 'prompt-caching',
    naam: 'Prompt caching',
    uitleg:
      'Het hergebruiken van al-door-het-model-verwerkte tokens tussen aanroepen, zodat identieke instructies of vaste documenten niet telkens opnieuw betaald hoeven worden. Grote cost- en latency-winst bij gebruikspatronen waar dezelfde context herhaald aan het model wordt gegeven — typisch 80–90% goedkoper op het gecachete deel, mits dat deel lang genoeg is (bij Anthropic minimaal ~1.000 tokens).',
    categorie: 'retrieval',
    zieOok: ['context-window', 'token'],
  },

  // ─── Geheugen & koppeling ─────────────────────────────────────────
  {
    slug: 'werkgeheugen',
    naam: 'Werkgeheugen',
    engels: 'working memory',
    uitleg:
      'De huidige gespreksstatus die op dit moment in het context window van het model zit. Vluchtig — verdwijnt na de sessie. Vergelijkbaar met wat een medewerker op een notitieblokje schrijft tijdens één klantgesprek.',
    categorie: 'geheugen',
    zieOok: ['ervaringsgeheugen', 'kennisgeheugen'],
  },
  {
    slug: 'ervaringsgeheugen',
    naam: 'Ervaringsgeheugen',
    engels: 'episodic memory',
    uitleg:
      'Losse gebeurtenissen en eerdere gesprekken, bewaard in een externe database en doorzoekbaar per gebruiker of dossier. Het archief van klantcontacten: "wat is er eerder besproken, en wanneer?"',
    categorie: 'geheugen',
    zieOok: ['werkgeheugen', 'kennisgeheugen'],
  },
  {
    slug: 'kennisgeheugen',
    naam: 'Kennisgeheugen',
    engels: 'semantic memory',
    uitleg:
      'Patronen en voorkeuren die zijn gedestilleerd uit herhaalde ervaringen. Het langstlevend — hier zit institutioneel geheugen: "deze klant wil altijd per mail worden benaderd, nooit telefonisch."',
    categorie: 'geheugen',
    zieOok: ['werkgeheugen', 'ervaringsgeheugen'],
  },
  {
    slug: 'llm',
    naam: 'LLM',
    engels: 'Large Language Model',
    uitleg:
      'Een groot taalmodel: een AI-model getraind op enorme hoeveelheden tekst om woorden te voorspellen en zo open-ended taken uit te voeren — schrijven, samenvatten, vragen beantwoorden, code genereren, gesprek voeren. In 2026 zijn de bekendste voorbeelden Claude, GPT en Gemini.',
    categorie: 'ai-basis',
    zieOok: ['frontier-model', 'redeneer-model', 'token'],
  },
  {
    slug: 'frontier-model',
    naam: 'Frontier-model',
    uitleg:
      'Het grootste, nieuwste model dat een aanbieder in het publieke domein heeft uitgebracht: duurder, krachtiger en doorgaans beter op de moeilijkste benchmarks dan oudere generaties. In 2026 zijn de bekendste voorbeelden Claude Opus 4.7, OpenAI GPT-5.5 Pro en Google Gemini 3.1 Pro. De keerzijde: hoge kosten, hogere latency en beperkte verklaarbaarheid maken een frontier-model lang niet altijd het juiste gereedschap.',
    categorie: 'ai-basis',
    zieOok: ['llm', 'open-weight-model'],
  },
  {
    slug: 'redeneer-model',
    naam: 'Redeneer-model',
    engels: 'reasoning model',
    uitleg:
      'Een taalmodel dat expliciet rekentijd reserveert om stap-voor-stap door een probleem te denken voordat het antwoordt — herkenbaar aan een hogere latency en duurdere prijs, maar sterker op wiskunde, complexe code-vraagstukken en multi-stap-planning. Voorbeelden in 2026: Claude Opus 4.7 met *extended thinking*, OpenAI o3, GPT-5.5 in thinking-modus.',
    categorie: 'ai-basis',
    zieOok: ['llm', 'frontier-model'],
  },
  {
    slug: 'multimodaal-model',
    naam: 'Multimodaal model',
    uitleg:
      'Een model dat meerdere soorten input tegelijk kan verwerken: tekst, beeld, soms audio of video. Toepassingen: documentbegrip, medische beeldanalyse, formulierverwerking. Geschikt wanneer een tekstuele beschrijving van een visueel ding te veel informatie verliest; voor pure teksttaken is een tekst-model meestal goedkoper.',
    categorie: 'ai-basis',
    zieOok: ['llm', 'embedding-model'],
  },
  {
    slug: 'wereld-model',
    naam: 'Wereld-model',
    engels: 'world model',
    uitleg:
      'Een model dat leert hoe de wereld reageert op acties, in plaats van alleen taal of beeld te interpreteren. Vooral relevant voor robotica, autonome voertuigen en industriële simulatie. Voorbeelden in 2025–2026: Meta V-JEPA 2, Google DeepMind Genie 3, World Labs Marble, NVIDIA Cosmos (Cosmos 3 aangekondigd op GTC maart 2026) en Wayve GAIA-2/LINGO-2.',
    categorie: 'ai-basis',
    zieOok: ['llm', 'multimodaal-model'],
  },
  {
    slug: 'diffusiemodel',
    naam: 'Diffusiemodel',
    uitleg:
      'Een model dat beelden of video genereert door geleidelijk uit "ruis" naar een gewenst eindresultaat te werken. Toepassingen: marketingvisualisaties, prototyping van interfaces, productafbeeldingen, video-content. Voorbeelden: Stable Diffusion, DALL-E, Midjourney (beeld) en Sora, Veo, Runway (video).',
    categorie: 'ai-basis',
    zieOok: ['multimodaal-model', 'llm'],
  },
  {
    slug: 'embedding-model',
    naam: 'Embedding-model',
    uitleg:
      'Een model dat tekst (of beeld, of audio) omzet naar een wiskundige representatie waarmee semantische gelijkenis meetbaar wordt: de zogenaamde [embedding](/begrippen#embedding). Onmisbaar voor RAG, semantisch zoeken, clustering en anomaliedetectie. Significant goedkoper dan generatieve LLMs.',
    categorie: 'ai-basis',
    zieOok: ['embedding', 'rag'],
  },
  {
    slug: 'klassieke-ml',
    naam: 'Klassiek machine learning',
    uitleg:
      'Statistische of regelgebaseerde modellen voor afgebakende, gestructureerde taken: XGBoost, LightGBM, Random Forest, BERT-classifiers en ARIMA voor tijdreeksen. Vaak superieur aan een LLM voor tabellaire data, voorspellingen op historische cijfers, hoog-volume classificatie en gereguleerde omgevingen waar statistisch valideren verplicht is.',
    categorie: 'ai-basis',
    zieOok: ['llm'],
  },
  {
    slug: 'tier',
    naam: 'Tier',
    uitleg:
      'Een prijs- en prestatie-niveau waarop modellen worden ingedeeld in het marktaanbod. In 2026 onderscheidt het veld vijf tiers: frontier (de grootste, duurste modellen voor het zwaarste werk), pro (dagelijks professioneel werk), standaard (gebalanceerd), budget (hoog-volume eenvoudige taken) en lokaal (zelf-gehost voor privacy-kritisch werk). Een tier-strategie betekent: per type taak het juiste niveau kiezen in plaats van overal hetzelfde model gebruiken.',
    categorie: 'ai-basis',
    zieOok: ['frontier-model', 'open-weight-model', 'llm'],
  },
  {
    slug: 'open-weight-model',
    naam: 'Open-weight model',
    uitleg:
      'Een model waarvan de gewichten (de getrainde parameters) publiek beschikbaar zijn, zodat je het zelf kunt draaien op eigen infrastructuur in plaats van alleen via de API van de leverancier. Voorbeelden in 2026: Meta Llama 4, Mistral Large 3, en een opkomende groep Chinese frontier-peers op coding-benchmarks (DeepSeek V4 Pro, Kimi K2.6 van Moonshot AI, GLM-5.1 van Z.ai, MiniMax M2.7). Voordelen: data-soevereiniteit, lagere kosten bij schaal, controle over upgrades. Nadelen: hardware-investering en eigen verantwoordelijkheid voor schaalbaarheid en beveiliging.',
    categorie: 'ai-basis',
    zieOok: ['frontier-model', 'llm'],
  },
  {
    slug: 'tokenizer',
    naam: 'Tokenizer',
    uitleg:
      'De software-laag die ruwe tekst opbreekt in [tokens](/begrippen#token), de rekeneenheden van een taalmodel. Elk model heeft een eigen tokenizer; dezelfde zin kan dus in het ene model 100 tokens kosten en in het andere 135. Daardoor kan een gelijk gebleven prijs-per-token-tarief in de praktijk een onzichtbare kostenstijging betekenen wanneer een leverancier zijn tokenizer vernieuwt.',
    categorie: 'ai-basis',
    zieOok: ['token', 'context-window'],
  },
  {
    slug: 'sdk',
    naam: 'SDK',
    engels: 'Software Development Kit',
    uitleg:
      'Een meegeleverde verzameling code-bouwstenen waarmee een ontwikkelaar een dienst (zoals een AI-model) snel in een eigen toepassing kan inbouwen, zonder zelf alle communicatie met de API te schrijven. Vergelijkbaar met een gereedschapskoffer die past op de schroeven die de leverancier gebruikt: je hoeft niet meer elk stuk maatwerk zelf te smeden.',
    categorie: 'ai-basis',
    zieOok: ['mcp', 'agent'],
  },
  {
    slug: 'function-calling',
    naam: 'Function calling',
    uitleg:
      'Het mechanisme waarmee een taalmodel aangeeft welke externe tool of functie het wil laten uitvoeren, met welke parameters. Het model voert nooit zelf code uit; het retourneert een gestructureerd tool-call-blok dat de toepassing afhandelt. Resultaat gaat terug naar het model, dat verder redeneert. Function calling is de basis voor alle tool-gebruik in moderne agents.',
    categorie: 'ai-basis',
    zieOok: ['agent', 'mcp', 'sdk'],
  },
  {
    slug: 'mcp',
    naam: 'MCP',
    engels: 'Model Context Protocol',
    uitleg:
      'Opkomende standaard (door Anthropic geïntroduceerd in november 2024) om AI-systemen op een uniforme manier te verbinden met externe data en tools. Vervangt maatwerk-integraties per bron. Let op: in 2026 nog geen veilige standaard — vereist expliciete autorisatie per server.',
    categorie: 'geheugen',
    zieOok: ['agent', 'rag'],
  },

  // ─── Kwaliteit & actualiteit ───────────────────────────────────────
  {
    slug: 'context-rot',
    naam: 'Context rot',
    uitleg:
      'Kwaliteitsverlies van een AI-model naarmate de context langer wordt. Empirisch vastgesteld op alle 18 frontier-modellen in Chroma\'s 2025-onderzoek: méér context is niet automatisch beter. Oorzaken: lost-in-the-middle, aandachtsverdunning en afleidende irrelevante content.',
    categorie: 'kwaliteit',
    zieOok: ['lost-in-the-middle', 'context-window', 'degradeert'],
  },
  {
    slug: 'lost-in-the-middle',
    naam: 'Lost-in-the-middle',
    uitleg:
      'Patroon dat taalmodellen informatie aan het begin en einde van hun context beter vinden dan informatie in het midden. Eerst beschreven door Liu et al. (Stanford, TACL 2024); het effect is structureel — geen trainingsfout die een volgende modelversie oplost.',
    categorie: 'kwaliteit',
    zieOok: ['context-rot', 'degradeert'],
  },
  {
    slug: 'stale-context',
    naam: 'Verouderde context',
    engels: 'stale context',
    uitleg:
      'Een kennisbank die niet meer actueel is, terwijl het systeem geen foutmelding geeft maar gewoon een antwoord. Juist die stilte maakt het gevaarlijk: het antwoord ziet er correct uit, maar klopt niet meer.',
    categorie: 'kwaliteit',
    zieOok: ['context-rot', 'freshness-score'],
  },
  {
    slug: 'freshness-score',
    naam: 'Actualiteitsscore',
    engels: 'freshness score',
    uitleg:
      'Samengestelde meting van hoe actueel een kennisbank is, opgebouwd uit vier dimensies: leeftijd van de inhoud, indexering-vertraging, verouderingspercentage en corpusdrift. Een score onder de 85% triggert typisch een waarschuwing, onder 70% wordt het zichtbaar voor eindgebruikers.',
    categorie: 'kwaliteit',
    zieOok: ['stale-context'],
  },
  {
    slug: 'drift',
    naam: 'Drift',
    uitleg:
      'Een stille verandering in het gedrag of de input van een AI-systeem over tijd, zonder dat een foutmelding of duidelijke degradatie het zichtbaar maakt. Een classifier die uit kalibratie raakt omdat de werkelijkheid is verschoven, embeddings die niet meer aansluiten bij de huidige documenten, of een routing-laag die steeds vaker escaleert: het zijn allemaal vormen van drift. Detecteer je niet door alarmen, maar door trends te monitoren: antwoordlengte, escalatie-rate, kwaliteitsmetrieken.',
    categorie: 'kwaliteit',
    zieOok: ['stale-context', 'context-rot', 'degradeert'],
  },
  {
    slug: 'circuit-breaker',
    naam: 'Circuit breaker',
    uitleg:
      'Mechanisme dat een falende afhankelijkheid tijdelijk afschermt om te voorkomen dat een agent blijft hameren op een dienst die toch niet antwoordt. Drie staten: gesloten (alles werkt), open (alle aanvragen falen direct, zonder de dienst te belasten) en half-open (één testaanvraag om te kijken of de dienst weer werkt). Productie-richtlijn: per leverancier een eigen breaker, drempel typisch 50% mislukkingen over 20 aanvragen, oplopende afkoeltijd van 30 seconden tot maximaal 5 minuten.',
    categorie: 'kwaliteit',
    zieOok: ['drift', 'stale-context'],
  },
  {
    slug: 'faithfulness',
    naam: 'Feitelijke grond',
    engels: 'faithfulness',
    uitleg:
      'Mate waarin een AI-antwoord daadwerkelijk gebaseerd is op de aangeleverde bronnen, en niet op verzonnen of extern vastgelegde kennis. Een van de vier standaard RAG-kwaliteitsmetingen (samen met antwoordrelevantie, context-herinnering en context-precisie).',
    categorie: 'kwaliteit',
    zieOok: ['hallucinatie', 'rag'],
  },

  // ─── Privacy & governance ──────────────────────────────────────────
  {
    slug: 'pii',
    naam: 'Persoonsgegevens',
    engels: 'PII — Personally Identifiable Information',
    uitleg:
      'Informatie waarmee een persoon direct of indirect kan worden geïdentificeerd: naam, e-mailadres, BSN, klantnummer, maar ook combinaties zoals postcode + geboortedatum. Onder de AVG (GDPR) aan strikte regels gebonden.',
    categorie: 'privacy',
    zieOok: ['ner', 'pseudonimisering', 'data-lineage'],
  },
  {
    slug: 'ner',
    naam: 'Entiteitsherkenning',
    engels: 'NER — Named Entity Recognition',
    uitleg:
      'Techniek die automatisch namen, plaatsen, organisaties en andere genoemde entiteiten in tekst herkent. Basis voor privacy-filtering in vrije tekst, waar gestructureerde identifiers (zoals BSN) al op andere manieren worden gevangen.',
    categorie: 'privacy',
    zieOok: ['pii', 'pseudonimisering'],
  },
  {
    slug: 'pseudonimisering',
    naam: 'Pseudonimisering',
    uitleg:
      'Persoonsgegevens vervangen door een consistent pseudoniem vóórdat data wordt verwerkt of opgeslagen. "Consistent" betekent: dezelfde BSN krijgt elke keer hetzelfde pseudoniem — zodat verbanden tussen documenten behouden blijven, maar de identiteit niet meer direct zichtbaar is.',
    categorie: 'privacy',
    zieOok: ['pii', 'ner', 'dp-rag'],
  },
  {
    slug: 'data-lineage',
    naam: 'Data-herkomst',
    engels: 'data-lineage',
    uitleg:
      'De traceerbaarheid van een antwoord terug naar het oorspronkelijke brondocument — plus de vector-versie, de ingeststelde datum, en een verwijderingslog. Voor AVG-compliance onmisbaar: zonder deze registratie is het recht op vergetelheid niet afdwingbaar.',
    categorie: 'privacy',
    zieOok: ['pii', 'rag'],
  },
  {
    slug: 'dp-rag',
    naam: 'Differentieel-private RAG',
    engels: 'DP-RAG',
    uitleg:
      'Variant van RAG met formele privacy-garantie via differentiële privacy — een wiskundige methode die de bijdrage van één individu aan een antwoord meetbaar beperkt. Zet privacy-budget alleen in op tokens die echt gevoelige informatie bevatten, en haalt op een redelijk budget zelfs betere antwoorden dan een systeem zónder RAG.',
    categorie: 'privacy',
    zieOok: ['pii', 'rag', 'pseudonimisering'],
  },
  {
    slug: 'cdc',
    naam: 'Event-gedreven bijwerken',
    engels: 'CDC — Change Data Capture',
    uitleg:
      'Databasetechniek die elke wijziging in een bronsysteem als event doorgeeft, zodat een kennisbank of index binnen seconden kan worden bijgewerkt — in plaats van te wachten op een geplande nachtelijke batch.',
    categorie: 'privacy',
    zieOok: ['freshness-score', 'stale-context'],
  },
  {
    slug: 'prompt-injection',
    naam: 'Prompt-injectie',
    engels: 'prompt injection',
    uitleg:
      'Aanval waarbij een aanvaller via tekstuele input — een gebruikersbericht, opgehaald document, webpagina of tool-beschrijving — instructies binnensmokkelt die het AI-model overschrijven. OWASP rangschikt prompt-injectie sinds 2025 als hoogste risico voor LLM-toepassingen (LLM01). De gevaarlijkste variant is indirecte injectie: kwaadaardige instructies komen binnen via tool-resultaten waardoor het model zonder dat de gebruiker iets merkt acties uitvoert die de aanvaller wilde. Verdediging hoort op de executielaag, niet bij het model — een model dat via prompt-injectie kan worden gemanipuleerd, kan ook geen veiligheidsgrens bewaken die afhangt van zijn eigen instructies.',
    categorie: 'privacy',
    zieOok: ['mcp', 'data-lineage'],
  },
];

export function termBySlug(slug: string): Term | undefined {
  return BEGRIPPEN.find((t) => t.slug === slug);
}

export function termenByCategorie(categorie: Categorie): Term[] {
  return BEGRIPPEN.filter((t) => t.categorie === categorie);
}

export const CATEGORIE_VOLGORDE: Categorie[] = [
  'ai-basis',
  'retrieval',
  'geheugen',
  'kwaliteit',
  'privacy',
];
