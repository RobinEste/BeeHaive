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
      'Variant van RAG waarbij de kennisbank niet uit losse documenten bestaat maar uit een kennisgraaf: entiteiten als knooppunten, relaties als verbindingen. Geschikt voor vragen die meerdere stappen vereisen ("welke klanten werken samen met welke leveranciers?"), maar verhoogt wel de kans op privacy-lekkage van gestructureerde relatie-informatie.',
    categorie: 'retrieval',
    zieOok: ['rag', 'pii'],
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
