# BeeHaive Frontend — Design Brief voor Artifact Mockups

## Over BeeHaive

BeeHaive is een AI knowledge framework voor professionals. Het platform combineert:
- **7 Building Blocks** (kennisgebieden): Knowledge, Client Blueprint, Dynamic Context, Prompt Design, Tool Integration, Model Engines, Evaluation Loop
- **7 Guardrails** (EU Trustworthy AI): Human Agency, Robustness, Privacy, Fairness, Transparency, Well-being, Accountability
- Een **knowledge graph** met papers, regulations, guidelines en best practices
- **Cursussen en trainingen** (toekomst)
- Een **blog** met AI-inzichten (toekomst)

**Doelgroep:** Nederlandse professionals die AI willen begrijpen en toepassen.
**Merknaam:** BeeHaive = Bee + Hive (bij + bijenkorf) — kennis verzamelen en structureren.

---

## Brandkleuren (uit logo — VERPLICHT, moeten prominent terugkomen)

| Kleur | Hex | RGB | Rol |
|-------|-----|-----|-----|
| **Teal** | `#44C2BA` | 68, 194, 186 | Primaire merkkleur — moet domineren op elke pagina |
| **Light Teal** | `#8BE6DA` | 139, 230, 218 | Grote vlakken, achtergronden, hover states |
| **Gold** | `#E9CA62` | 233, 202, 98 | Warme tegenkleur — koppen, accenten, iconen |
| **Yellow** | `#EEDB43` | 238, 219, 67 | Call-to-action, highlights, actieve elementen |

**Regel:** Deze 4 kleuren zijn NIET subtiele accenten — ze ZIJN het kleurenpalet. Elke sectie moet minimaal 2 van de 4 brandkleuren prominent gebruiken. Aanvulkleuren (achtergrond, tekst) zijn ondersteunend.

---

## Pagina's om te ontwerpen

Maak voor elke design-richting een **homepage mockup** als HTML artifact met:

1. **Hero sectie** — titel, subtitel, CTA knop
2. **Framework overzicht** — de 7 Building Blocks als visueel grid/kaarten
3. **Guardrails sectie** — de 7 Guardrails kort weergegeven
4. **Kennisbank teaser** — 3 voorbeeld knowledge items
5. **Footer** met navigatie

### Voorbeeld content voor de mockup

**Hero:**
- Titel: "AI begrijpen. AI toepassen. AI verantwoord inzetten."
- Subtitel: "BeeHaive is het framework dat AI-kennis structureert in 7 bouwstenen en 7 waarborgen — zodat je niet alleen weet wát AI kan, maar ook hoe je het goed doet."
- CTA: "Ontdek het framework"

**Building Blocks (7):**
1. Knowledge — Menselijke expertise en competentie
2. Client Blueprint — End-to-end beschrijving van een AI-oplossing
3. Dynamic Context — Actuele informatie tijdens uitvoering (RAG, queries)
4. Prompt Design — Ontwerp en verfijning van prompts
5. Tool Integration — Koppeling van externe systemen en API's
6. Model Engines — AI-modellen en runtime-omgevingen
7. Evaluation Loop — Cyclus van meten en verbeteren

**Guardrails (7):**
1. Human Agency — Menselijke controle en oversight
2. Robustness — Technische veerkracht en veiligheid
3. Privacy — Privacy en datagovernance
4. Fairness — Non-discriminatie en inclusie
5. Transparency — Uitlegbaarheid en openheid
6. Well-being — Maatschappelijk welzijn
7. Accountability — Verantwoording en governance

**Kennisbank items (3 voorbeelden):**
- "EU AI Act: A Comprehensive Framework for Trustworthy AI" — regulation
- "RAG-Anything: Multimodal Retrieval-Augmented Generation" — paper
- "Prompt Engineering: From Theory to Practice" — best_practice

---

## Design Richting A: Warm Flowing Network

**Kernidee:** Kennis als stromend netwerk — zachte gradiënten tussen teal en gold, vloeiende verbindingslijnen, grote kleurvlakken. Alsof kennis door het platform stroomt.

**Kleurtoepassing (brandkleuren dominant):**
- Hero achtergrond: groot teal-naar-light-teal gradiënt (#44C2BA → #8BE6DA) — de hele hero is kleur
- Building blocks: kaarten met gold (#E9CA62) borders en teal iconen
- CTA knoppen: yellow (#EEDB43) met donkere tekst
- Secties wisselen af: teal-achtige secties ↔ warme gold-tinted secties
- Tekst op kleurvlakken: wit (#FFFFFF)
- Tekst op lichte achtergronden: #1A2E2D (donker teal-zwart)
- Lichte secties: #F0FFFE (teal-tinted wit, NIET neutraal grijs)

**Typografie (Google Fonts):**
- Headings: **Syne** (700, 800) — bold geometric met karakter, voelt energiek en modern
- Body: **Figtree** (400, 500) — organisch, warm, uitstekende leesbaarheid

**Layout-concept:**
- Hero: vol-breedte teal gradiënt met grote witte tekst, golvende onderkant (CSS clip-path)
- Building blocks: 2×4 grid (laatste cel = CTA) met zachte kaarten, lichte schaduw, gold accent-lijn bovenaan
- Guardrails: horizontale scroll/ribbon met teal tags op goudgele achtergrondstrip
- Kennisbank: 3 kaarten met light teal achtergrond, teal hover-glow

**Visuele signatuur:** Zachte, golvende sectiescheidingen (wave dividers) in teal/gold — elke sectie stroomt in de volgende. Geen harde lijnen.

**Sfeer:** Vloeiend, warm, verbonden

**VERMIJD:** Hexagons, honingraatpatronen, rechte lijnen als decoratie, neutrale grijstinten als hoofdkleur.

---

## Design Richting B: Bold Contrast Editorial

**Kernidee:** Grote kleurvlakken ontmoeten strakke typografie. Teal en gold als gelijkwaardige, dominante kleuren in een high-contrast layout. Denk aan een architectuurmagazine, niet aan een tech-blog.

**Kleurtoepassing (brandkleuren dominant):**
- Navigatie: teal (#44C2BA) balk met witte tekst
- Hero: split-screen — linkerkant teal (#44C2BA) vlak met witte tekst, rechterkant gold (#E9CA62) vlak met donkere tekst
- Building blocks achtergrond: light teal (#8BE6DA) als groot vlak
- Guardrails achtergrond: gold (#E9CA62) als groot vlak
- CTA: yellow (#EEDB43) knoppen
- Tekst op kleur: wit of #0F1F1E (afhankelijk van contrast)
- Witte secties: smalle accent-banen in teal of gold langs de rand

**Typografie (Google Fonts):**
- Headings: **Young Serif** (400) — elegante, onverwachte serif met warmte, valt op zonder te schreeuwen
- Body: **Onest** (400, 500) — fris, onderscheidend van standaard sans, subtiel rond

**Layout-concept:**
- Hero: asymmetrische split (60/40) met twee grote kleurvlakken, tekst links, abstracte vorm rechts
- Building blocks: 7 rijen in een gestaggerde layout — afwisselend links/rechts uitgelijnd, nummer groot in gold
- Guardrails: op een groot goudgeel vlak, 7 items als boldige lijst met teal nummering
- Kennisbank: kaarten met dikke teal linkerborder, hover verschuift kaart naar rechts

**Visuele signatuur:** Grote, onbehaaglijk boldige kleurvlakken die botsen en overlappen — teal en gold claimen elk hun ruimte op de pagina. Geen zachte overgangen.

**Sfeer:** Bold, autoritair, eigenzinnig

**VERMIJD:** Witruimte als dominant element, subtiele accenten, zachte schaduwen, alles wat "veilig" voelt.

---

## Design Richting C: Luminous Dark

**Kernidee:** Donker canvas waar teal en gold als lichtbronnen fungeren. De brandkleuren gloeien tegen een diepe achtergrond — alsof kennis oplicht in het donker.

**Kleurtoepassing (brandkleuren dominant):**
- Achtergrond: #0C1E1D (diep donker teal, NIET neutraal zwart)
- Secundair vlak: #122C2A
- Teal (#44C2BA): navigatie-items, links, kaartborders, grote decoratieve cirkels op achtergrond
- Light teal (#8BE6DA): hover states, geselecteerde items, subtiele glows (box-shadow: 0 0 30px #8BE6DA40)
- Gold (#E9CA62): headings, nummering, accent-elementen — gold op donker is luxe
- Yellow (#EEDB43): CTA knoppen, badges, actieve states
- Tekst: #E0F2F1 (licht teal-wit)

**Typografie (Google Fonts):**
- Headings: **Bricolage Grotesque** (600, 700) — karaktervol, speels maar serieus, opvallend in elke maat
- Body: **Instrument Sans** (400, 500) — verfijnd, elegant, uitstekend leesbaar op donker

**Layout-concept:**
- Hero: donkere achtergrond met grote gold heading, teal gradiënt-orb als decoratief element (CSS radial-gradient), CTA in yellow
- Building blocks: 7 kaarten met glassmorphism (backdrop-filter: blur, semi-transparante teal border), gold nummering
- Guardrails: verticale timeline met gloeiende teal dots en gold labels
- Kennisbank: kaarten met teal linkerborder die gloeien bij hover

**Visuele signatuur:** Gloeiende teal en gold orbs/gradiënten op de donkere achtergrond — decoratieve radial-gradients die suggereren dat kennis licht uitstraalt. Niet neon, maar lumineus.

**Sfeer:** Diep, lumineus, premium

**VERMIJD:** Neutraal zwart (#000), neon-effecten, matrix/hacker-esthetiek, te veel glow (subtiel > overdreven).

---

## Instructie voor artifact-generatie

Maak per design-richting (A, B, C) een volledig werkende HTML homepage als artifact.

### Verplichte regels:
1. **Brandkleuren (#44C2BA, #8BE6DA, #E9CA62, #EEDB43) moeten samen minstens 60% van het zichtbare kleuroppervlak innemen.** Ze zijn niet "accenten" — ze ZIJN het ontwerp.
2. **Google Fonts** laden via `<link>` in de `<head>` — gebruik exact de fonts uit de richting.
3. **Inline CSS** in een `<style>` blok (geen externe stylesheets).
4. **Responsive design** — moet er goed uitzien op desktop (1200px+) én mobiel (375px).
5. **Werkende hover-effecten** en minstens één CSS-animatie.
6. **Echte content** uit de "Pagina's om te ontwerpen" sectie — geen lorem ipsum.
7. **Volg de "VERMIJD" regel** per richting strikt op.
8. De hele pagina moet scrollbaar zijn met alle 5 secties (hero, building blocks, guardrails, kennisbank, footer).

### Kwaliteitscheck:
- Als je de pagina in zwart-wit bekijkt en de layout niet interessant is → het ontwerp leunt te veel op kleur
- Als je de kleur wegdenkt en alleen tekst overhoudt → de typografie moet op zichzelf staan
- Als minder dan de helft van het scherm brandkleur toont → je gebruikt de kleuren niet genoeg
