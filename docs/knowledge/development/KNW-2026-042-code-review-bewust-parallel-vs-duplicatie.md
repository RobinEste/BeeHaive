# KNW-2026-042: Code-review agent-bevindingen — bewust parallel ≠ duplicatie

> **Categorie:** development
> **Datum:** 2026-04-17
> **Sessie-context:** `/simplify` pass met drie review-agents flagt dat BBTools/BBResearch/BBGuardrails "duplicatie" is en roept om shared abstraction
> **Relevantie:** hoog

## Inzicht

Code-review agents herkennen structurele gelijkheid als duplicatie en stellen voor om te abstraheren. Maar *bewust parallelle structuur* (waarin elke variant z'n eigen axis verandert — kleur, layout, metadata-shape) is géén duplicatie die weggerefactord moet worden. Laat reviews de vraag stellen, maar check zelf of de geëxtrahireerde abstractie echt iets oplevert of alleen moeilijk te navigeren parameter-sprawl creëert.

## Context

Tijdens twee opeenvolgende `/simplify` passes flagden review-agents consistent dat BBResearch, BBTools en BBGuardrails "duplicatie" hadden (allemaal zelfde `bb-section` class, eyebrow/title/intro, accent-bar, card-layout). Voorgestelde fix: shared `<BBCard>` of `<BBListSection>`. Maar bij nauwkeurige inspectie: elk component heeft een andere grid-shape (verticaal list vs 2-col grid), andere meta-chip (source-type vs category vs guardrail-code), andere accent-kleur (gold vs teal), andere CTA (truncation + external link vs altijd link vs geen link).

## Geleerd

### Wat werkte

- **Diff leggen op axes van variatie, niet op oppervlakte-gelijkheid.** Voor elk "duplicatie"-flag: schrijf expliciet op welke dimensies de varianten verschillen. Als dat er 5+ zijn en elke variant gebruikt een andere subset, is een shared abstractie parameter-sprawl.
- **Parallelle structuur is een feature**. Een lezer die BBResearch begrijpt, herkent BBTools instantly — de naming, class-convention en file-shape zijn bewust identiek. Dat is leesbaarheid.
- **Regel van drie**: pas abstraheren nadat je een derde variant hebt gezien én het helder is dat die derde dezelfde axes heeft. Bij `/simplify` flag notice, maar wacht op de vierde variant voordat je breekt.

### Wat niet werkte

- **Agent-advies klakkeloos volgen**: in de eerste `/simplify` pass was ik bijna begonnen met een `<BBCard>` basis-component. Pas toen ik de varianten expliciet ging vergelijken, werd duidelijk dat de "shared" basis zo dun zou zijn dat elke variant toch eigen CSS-overrides nodig had.
- **"Het kan DRY'er"** is geen voldoende rechtvaardiging. DRY is een middel, niet een doel. Als de "duplicatie" drie keer **dezelfde structurele idioom** is dat makkelijk te lezen is, is dat beter dan één abstractie met veel parameters.

### Waarom

Code-review agents zijn patroon-matchers; ze zien structurele overlap (eyebrow + h2 + intro + list + CTA) en triggeren op een abstraheer-regel. Ze hebben minder zicht op *waarom* de varianten bestaan — dat is redactioneel/visueel onderscheid waar de agent geen oordeel over heeft. De eindbeslissing blijft bij de programmeur die de semantiek kent.

## Toepassing

- **Bij elke `/simplify` finding over "duplicatie"**: voer de diff-op-axes check uit. 3+ assen met verschillende waarden = parallel, laat staan. 1–2 assen = waarschijnlijk echte duplicatie, abstraheer.
- **In commit-messages**: noem expliciet "bewust parallel, volgt BBGuardrails-patroon" als je een nieuwe variant toevoegt. Dan begrijpt de volgende reviewer (of jezelf over drie maanden) dat de overlap intentioneel is.
- **Agent-feedback serieus nemen maar niet blind**: de agent ziet iets; de vraag is of het écht een probleem is. Antwoord met een zinnetje waarom-wel-of-niet, dan groeit je intuïtie mee.
- **Geldt voor ALLE review-tooling**: ESLint's `no-duplicate-code`, SonarQube's CPD, Claude/GPT review-agents. Allemaal structurele matchers, allemaal blind voor redactionele parallellen.
