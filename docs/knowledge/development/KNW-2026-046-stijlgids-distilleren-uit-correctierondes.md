# KNW-2026-046: Stijlgids distilleren uit correctierondes, niet vooraf

> **Categorie:** development
> **Datum:** 2026-04-21
> **Sessie-context:** BB_03 Dynamic Context-pagina schrijven — ~10 opeenvolgende correctierondes van de gebruiker op taalgebruik, terminologie en structuur. Na afloop werd de impliciete schrijflijn gecodificeerd in `.claude/schrijfstijl-bb.md` (14 paragrafen + review-checklist).
> **Relevantie:** hoog

## Inzicht

Een bruikbare stijlgids schrijf je niet vooraf op basis van principes — je oogst hem uit echte correctierondes op één pilot-pagina. Pas wanneer een gebruiker 8–12 keer heeft gecorrigeerd op dezelfde soort dingen ontstaan de **gevalideerde** patronen die generaliseren. Eerder is het abstracte goede bedoelingen zonder traction.

## Context

BB_03 werd als eerste volledig uitgewerkte BB-pagina gekozen als baseline. Tijdens de inhoudelijke review gaf de gebruiker steeds **korte, specifieke** correcties: "Sales → Verkoop", "token uitleggen", "em-dash weg", "test-fixtures in code-search kan dat niet ook zakelijk?", "context window ook uitleggen", etc. Elke correctie was klein; gecumuleerd vormden ze een scherp profiel van de lezer-aanname, terminologie-discipline en interpunctievoorkeur.

Pas na ~10 rondes vroeg de gebruiker zelf: *"laten we een lijn uit de correcties halen die we op de rest kunnen loslaten."* Op dát moment was de gids schrijfbaar: we hadden genoeg concrete voorbeelden om de regels te onderbouwen, en we wisten welke regels gevalideerd waren (vs. welke we vermoedden).

## Geleerd

### Wat werkte

- **Correcties eerst verzamelen, dan pas generaliseren.** Elke correctie apart oplossen zonder te proberen meteen een meta-regel te vinden. Pattern-matching komt vanzelf zodra er voldoende datapunten zijn.
- **De pilot-pagina als baseline in de gids vermelden** (log-tabel achteraan: "BB_03 — 322 regels — baseline voor deze gids"). Dat maakt herleidbaar waar de regel vandaan komt.
- **Voorbeelden uit de echte correcties** (niet verzonnen). *"✗ Sales / ✓ Verkoop"* is overtuigender dan een abstract principe over NL-terminologie, omdat elke lezer de eerdere correctie in de tekst herkent.
- **Review-checklist als afsluiter**: van 14 paragrafen naar 14 concrete vragen om per toekomstige pagina af te lopen.

### Wat niet werkte

- **Eerdere poging om vooraf een schrijfstijlgids op te stellen**: die bestond in vage vorm in de eerste drafts (zaken als "zakelijk maar toegankelijk") maar was te abstract om correcties te voorkomen. De gebruiker moest alsnog 10 rondes specifieke dingen aanstippen.
- **Correcties "oplossen met een meta-regel" tijdens de eerste 2–3 rondes**: te vroeg generaliseren leidt tot regels die niet houdbaar blijken of waar je later op terugkomt.

### Waarom

Schrijfstijl is expertisekennis die grotendeels impliciet is — de auteur/eigenaar weet "het klopt niet" of "dat is te technisch" zonder vooraf het volledige regelkader op papier te hebben. Dat kader **kristalliseert** pas in de daadwerkelijke redactiefase. Proberen het vooraf expliciet te maken is een vorm van premature optimization: je specifieert regels zonder empirische dekking.

Na 8–12 correctierondes bestaan genoeg voorbeelden om:
- De regel te **onderbouwen** met meerdere datapunten (niet één anekdote)
- De regel te **contrasteren** (wanneer wel, wanneer niet)
- De regel **concreet** te maken met werkelijke voor/na-paren

## Toepassing

**Wanneer toepassen:**

- Een nieuwe content-serie (bouwstenen, guardrails, trainings-modules, wiki-artikelen) waar consistente stijl over 5+ pagina's wenselijk is.
- Wanneer je meerdere auteurs of AI-assistenten op dezelfde tekst-serie wilt laten werken.
- Voor whitepapers, trainingsmateriaal of klant-deliverables met herhalende structuur.

**Concrete workflow:**

1. **Kies één pilot-pagina** (de rijkste, meest eisende — niet de eenvoudigste)
2. **Laat correcties komen zonder meta-regels te formuleren** in ronde 1–3
3. **Registreer de correcties** (expliciet in notities of via toolcall-patroon)
4. **Na ~8–12 correcties**: distilleer met de gebruiker een gezamenlijke stijllijn. Groepeer correcties naar patronen. Formuleer regels met voorbeelden.
5. **Leg vast** op een plek die voor alle volgende schrijfsessies beschikbaar is (`.claude/` in project-root voor Claude Code, `docs/style.md` voor teams).
6. **Voeg een log-tabel toe** zodat elke nieuwe pagina in de serie tegen de gids kan worden afgevinkt — en de gids zelf kan worden bijgewerkt bij nieuwe patronen.

**Contra-indicatie:** wanneer de content-serie in totaal 1–2 pagina's blijft, is de overhead van een formele gids hoger dan de opbrengst. Dan blijft ad-hoc redactie beter.

**Koppeling met andere KNW-entries:**

- KNW-2026-030 (Iteratieve content-review als ontwerpproces) — dit inzicht specificeert dát iteratie werkt; het nieuwe inzicht specificeert *wanneer* je er een gids uit moet distilleren.
- KNW-2026-038 (Content consistency-pass na narrative-updates) — de gids helpt die consistency-pass gestructureerder te maken.
