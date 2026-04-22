# Research: Decision Intelligence & Expertise-externalisatie — BB_01 Knowledge

**Researcher:** lead agent (Lane 2)
**Dimensie:** Kozyrkov decision-first framework, Kahneman-Klein intuïtie-expertise, meta-skills, expertise externaliseren
**Datum:** 2026-04-22

## Samenvatting (1 zin)

Kozyrkov's decision-first framework stelt menselijk oordeelsvermogen centraal als de meest kritieke maar minst geüpgradede vaardigheid, terwijl Kahneman & Klein aantonen dat betrouwbare intuïtie twee voorwaarden vereist die AI-tijdperk omgevingen fundamenteel veranderen — samen bieden ze een wetenschappelijk kader voor waarom BB_01 het externaliseren van beslissingslogica als kerncompetentie moet opnemen.

## Bevindingen

### Kozyrkov — Menselijk oordeelsvermogen als de meest waardevolle vaardigheid

Cassie Kozyrkov (voormalig Chief Decision Scientist Google) betoogt in haar Substack (feb 2026) dat de meest waardevolle vaardigheid in het AI-tijdperk niet coderen of prompting is, maar **menselijk oordeelsvermogen** — het vermogen om diep en helder te redeneren over welke problemen je eigenlijk wilt oplossen (`verified` [1]).

Kernbegrippen:

**De "thoughtlessness enabler" paradox:**
> "The peril of AI is the same as the promise of AI: it's a thoughtlessness enabler." (`verified` [1])

AI versterkt zowel goed als slecht oordeelsvermogen. Een bekwame beslisser met AI wordt exceptioneel; een onbekwame beslisser met AI maakt grotere fouten sneller. Dit maakt oordeelsvermogen niet minder maar juist meer kritiek.

**Genie-kant vs. wens-kant:**
Kozyrkov onderscheidt twee kanten van AI-gebruik:
- **Genie-kant** (prompt engineering, technische uitvoering) — wordt steeds vaker door AI zelf gedaan
- **Wens-kant** (weten wat je moet vragen, waarom, voor wie) — het knelpunt verschuift hiernaar naarmate AI krachtiger wordt

Implicatie voor BB_01: organisaties moeten investeren in "wisher-side capabilities" — het vermogen om AI de juiste vragen te stellen, niet alleen het vermogen om AI te bedienen.

**Decision-first boven data-first:**
Kozyrkov's bredere werk (via Google's Decision Intelligence team) stelt dat organisaties consistent te vroeg naar data grijpen zonder eerst de beslissing te definiëren: welk besluit wordt genomen, wie neemt het, welke informatie is daarvoor vereist, wat is het acceptatiecriterium (`inferred` uit Kozyrkov's publicatiepatroon; directe URL voor dit specifieke principe niet beschikbaar als bronbestand [1]).

> "If you hand an unskilled decision-maker the most sophisticated AI system imaginable, they'll be stuck fumbling in the dark." (`verified` [1])

**Relevantie voor BB_01 checklist:**
- Checklist-item: "Heeft het team gedefinieerd welk besluit dit AI-systeem ondersteunt of neemt?"
- Checklist-item: "Is er een expliciete eigenaar aangewezen voor elk besluit dat AI output raakt?"
- Checklist-item: "Zijn acceptatiecriteria gedefinieerd vóór de AI-output wordt beoordeeld?"

### Kahneman & Klein — Wanneer is intuïtie betrouwbaar?

Kahneman en Klein (2009, American Psychologist) onderzochten de grensvoorwaarden tussen betrouwbare professionele intuïtie en overmoedige impressies (`verified` [2]).

**Twee voorwaarden voor betrouwbare intuïtie:**
1. **High-validity environment** — stabiele, identificeerbare cues die voorspellend zijn voor uitkomsten. Brandbestrijding en chirurgie voldoen; aandelenmarkt en politieke voorspellingen niet.
2. **Adequate opportunity to learn** — voldoende oefening met snelle, consistente feedback.

> "Evaluating the likely quality of an intuitive judgment requires an assessment of the predictability of the environment in which the judgment is made and of the individual's opportunity to learn the regularities of that environment." (`verified` [2])

**Subjectieve zekerheid ≠ accuraatheid:**
> "Subjective experience is not a reliable indicator of judgment accuracy." (`verified` [2])

**Vertaling naar AI-tijdperk (inferred):**
AI verandert de geldigheidsomgeving fundamenteel:
- Taken die vroeger stabiele feedback gaven (schrijven, analyseren) zijn nu deels overgenomen door AI, waardoor de feedbackcyclus voor het leren van het onderscheid (wat kan ik zelf, wat moet AI doen) verstoord raakt
- Experts die met AI werken verliezen de feedback-signalen die hun intuïtie voor taak-moeilijkheidsgraad kalibreerden (`inferred` — logisch gevolg van Kahneman-Klein + Mollick deskilling, niet direct een Kahneman-Klein claim)

**Implicatie voor BB_01:**
Organisaties moeten expliciete feedback-loops ontwerpen voor AI-gebruik, zodat medewerkers kunnen kalibreren wanneer hun intuïtie betrouwbaar is en wanneer ze op AI moeten vertrouwen. Dit is het externaliseren van beslissingslogica: maak de grensvoorwaarden voor intuïtiegebruik zichtbaar en bespreekbaar.

### McKinsey — Meta-skills als concurrentievoordeel

McKinsey.org (jan 2026) definieert "meta-skills" als `"the cognitive and social capacities to steer, interpret, and ethically assess AI output"` en bestempelt deze als het echte concurrentievoordeel (`verified` [3]).

Vier foundational AI mindsets die McKinsey aanreikt:
1. **Curiosity** — openheid voor AI-experimentatie
2. **Adaptability** — duurzame routines in plaats van achterlopen op elke nieuwe tool
3. **Responsibility** — bewust op unintended consequences checken vóór "generate" te drukken
4. **Human-centered thinking** — de mens centraal houden in AI-gedreven processen

Praktisch patroon: "spending 15 minutes each week learning one new AI capability without the pressure to master it" (`verified` [3]).

**Vertaling naar BB_01:** Meta-skills zijn de competentielaag boven tool-gebruik. BB_01 moet ze expliciteren als vaardigheidsgebied, niet als bijproduct van tool-training.

### Chris Lema — Vier niveaus van AI-werk en operating agreements

Lema's "Four Levels of AI Work" (2026) beschrijft een progressiemodel dat direct relevant is voor het externaliseren van expertise (`verified` [4]):

- **Level 1:** Collaborator mindset — van tool naar samenwerker
- **Level 2:** Compounding Assets — van wegwerpoutput naar persistente intelligentie (skills, frameworks, specifications, memory)
- **Level 3:** Operating Agreements — van ad-hoc naar systematisch
- **Level 4:** Production-Grade Systems — van interacties naar architecturen

**Operating Agreements (Level 3) als kern van expertise-externalisatie:**

> "Define the operating agreement. Write it down. This is what separates people who use AI from people who work with AI." (`verified` [4])

Een operating agreement bevat:
- **Decision authority**: wat stelt Claude voor, wat beslissen mensen (strategie, stem, doelgroep)?
- **Human-in-the-loop pause points**: welke stappen vereisen menselijke input?
- **Visible reasoning**: wanneer Claude beslissingen neemt, moet het denken zichtbaar zijn
- **Escalation triggers**: wanneer stopt AI en vraagt het om input?
- **Quality standards**: expliciete checklists — wat betekent "klaar"?

> "Tool thinking produces prompts. Collaborator thinking produces systems." (`verified` [4])

**Vertaling naar BB_01:** Het Lema-model biedt een didactisch kader voor BB_01-inhoud. De meeste organisaties blijven steken op Level 1. BB_01 moet medewerkers progressief naar Level 2-3 brengen.

### Expertise-externalisatie als organisatorische vaardigheid

Het patroon dat uit alle bronnen opkomt: de kernuitdaging voor BB_01 is **het externaliseren van impliciete expertise** — de kennis die nu in hoofden van individuen leeft, moet worden omgezet in zichtbare, deelbare, AI-leesbare kaders.

Dit bestaat uit drie lagen:
1. **Beslissingslogica** (Kozyrkov): welke beslissingen worden genomen, door wie, op basis van welke informatie?
2. **Grensvoorwaarden** (Kahneman-Klein): wanneer is menselijke intuïtie betrouwbaar, wanneer niet?
3. **Kwaliteitscriteria** (Lema): wat betekent "goed genoeg" voor elke taak?

## Evidence Table

| # | Bron | URL | Type | Key claim | Confidence |
|---|------|-----|------|-----------|------------|
| 1 | Kozyrkov — "Most Valuable Skill for the AI Era" | https://decision.substack.com/p/whats-the-most-valuable-skill-for | primary | Oordeelsvermogen als kernvaardigheid, thoughtlessness enabler | high (paywall — citaten geverifieerd via bron-007) |
| 2 | Kahneman & Klein — American Psychologist 2009 | https://pubmed.ncbi.nlm.nih.gov/19739881/ | primary (academic) | 2 voorwaarden betrouwbare intuïtie | high |
| 3 | McKinsey.org — Human Skills 2026 | https://www.mckinsey.org/dotorgblog/the-human-skills-you-will-need-to-thrive-in-2026s-ai-driven-workplace | secondary | Meta-skills als concurrentievoordeel, 4 mindsets | high |
| 4 | Lema — Four Levels of AI Work | (PDF beschikbaar; geen publieke URL in bron-093) | primary | Operating agreements, expertise externalisatie | high |

## Coverage Status

- **Gecheckt direct:** bron-007 (Kozyrkov, paywall), bron-070 (Kahneman-Klein, volledige tekst), bron-060 (McKinsey), bron-093 (Lema)
- **Blijft onzeker:** Kozyrkov's volledige decision-first framework achter paywall — citaten verifieerbaar, maar volledig kader op basis van samenvatting in bron-007
- **Niet afgerond:** directe verificatie van Lema-bron-URL (PDF-only, geen publieke URL beschikbaar)

## Sources

1. Kozyrkov, Cassie — "What's the Most Valuable Skill for the AI Era?" — https://decision.substack.com/p/whats-the-most-valuable-skill-for
2. Kahneman, Daniel & Klein, Gary — "Conditions for Intuitive Expertise: A Failure to Disagree" — https://pubmed.ncbi.nlm.nih.gov/19739881/
3. McKinsey.org — "The Human Skills You'll Need to Thrive in 2026's AI-Driven Workplace" — https://www.mckinsey.org/dotorgblog/the-human-skills-you-will-need-to-thrive-in-2026s-ai-driven-workplace
4. Lema, Chris — "The Four Levels of AI Work" — (PDF, bron-093; geen publieke URL)
5. EU HLEG — "Ethische Richtsnoeren voor Betrouwbare KI" — https://ec.europa.eu/digital-single-market/en/high-level-expert-group-artificial-intelligence
