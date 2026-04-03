# Research Protocol — BeeHaive Kennisbank Verrijking

**Versie:** v2.0
**Datum:** 2026-04-03
**Issue:** #29
**Status:** Reviewed — ronde 1 verwerkt

---

## 1. Doel

Per Building Block (7) en Guardrail (7) een actuele, betrouwbare kennisbank opbouwen en wekelijks bijwerken. Drie bronnen:

1. **Bastionclaw** — use-cases uit de praktijk
2. **Natural Intelligence** — artikelen en bronmateriaal
3. **Web research** — recente papers, frameworks, best practices, statistieken

Dit protocol beschrijft het herhaalbare proces voor bron 3 (web research). De cross-project mapping voor bronnen 1 en 2 staat in `docs/CROSS_PROJECT_MAPPING.md`.

### Fasering

Het protocol start **niet** als wekelijks proces terwijl Fase 3 (Frontend Website) nog loopt. De fasering:

| Fase | Trigger | Wat |
|------|---------|-----|
| **Nu (pilot)** | Direct | Eén baseline-run voor 1-2 BB's die al live zijn (bijv. Prompt Design, Knowledge) — om het proces te valideren |
| **Na Fase 3** | #22 en #9 opgeleverd | MVP-variant activeren: maandelijkse cadans, 2 BB/GR per sessie |
| **Na lancering** | BeeHaive.org live met gebruikers | Volledig rotatieschema overwegen op basis van gebruikersfeedback |

### MVP-variant vs. volledig protocol

Dit protocol beschrijft twee varianten. **Start altijd met de MVP-variant.**

| Aspect | MVP-variant | Volledig protocol |
|--------|-------------|-------------------|
| **Stappen** | 3: Search → Select → Synthesize | 8: volledige pipeline |
| **Cadans** | Maandelijks, 2 BB/GR per sessie | Wekelijks, 3-4 BB/GR per sessie |
| **Tijdsinvestering** | ~30 min per sessie | ~60 min per BB/GR |
| **Archivering** | Alleen claims + bronnen in research output | Full-text bronarchief |
| **Wanneer opschalen** | Als MVP onvoldoende diepgang oplevert | Na evaluatie op 4-weken punt |

De MVP-variant volgt dezelfde principes (tiered sources, two-source rule, bronbeperkingen) maar slaat de formele extractie, verificatie en archivering over. Output gaat direct naar de research output per BB/GR.

---

## 2. Principes

Gebaseerd op lessen van Valyu (tiered retrieval), Arun Baby (browsing agents pipeline) en Skywork (research workflow met provenance).

| Principe | Toelichting |
|----------|-------------|
| **Pipeline, geen single call** | Research is een 8-staps proces, niet "zoek en vat samen" |
| **Tiered sources** | Bewust kiezen uit welke bronlaag je zoekt per onderwerp |
| **Two-source rule** | Elke feitelijke claim heeft minstens 2 onafhankelijke bronnen |
| **Structured extraction** | Evidence = claim + exacte quote + URL + confidence |
| **Verification apart** | Verificatie is een eigen stap, niet onderdeel van extractie |
| **Full-text archivering** | Interessante bronnen worden volledig opgeslagen voor toekomstige RAG |
| **Krimpend tijdsvenster** | Eerste run breed (12m), daarna steeds smaller om overlap te voorkomen |
| **Alleen tekst** | Geen YouTube, LinkedIn, X, GitHub, Reddit, Quora — alleen tekstuele bronnen |
| **Budget per onderwerp** | Max 3 query-rondes, max 5-8 bronpagina's per BB/GR per sessie |
| **Provenance altijd** | Elke conclusie is traceerbaar naar de bron |

---

## 2b. AVG-grondslag

Dit protocol verwerkt **persoonsgegevens**: auteursnamen in extractie-schema's, brontemplate en gearchiveerde teksten. Mogelijk ook contactgegevens (e-mail, affiliatie) in gescrapete full-text content.

| Aspect | Regeling |
|--------|----------|
| **Grondslag** | Art. 6(1)(f) AVG — gerechtvaardigd belang. Zie LIA hieronder en de basis-LIA in `docs/DATA_GLOSSARY.md` |
| **Dataminimalisatie** | PII-scan en redactie vóór archivering (zie §4 Stap 4) |
| **Bewaartermijn** | Max 24 maanden; bronnen die niet naar de knowledge graph zijn doorgesluisd, worden na de termijn verwijderd of geanonimiseerd |
| **Art. 21 bezwaar** | Bij een verwijderverzoek: doorzoek `docs/research/bronnen/` en research outputs op de auteursnaam, redacteer of verwijder. Voeg de naam toe aan `blocked_authors.txt` |
| **Verwerkers** | Exa en Firecrawl ontvangen zoekqueries (geen PII) en retourneren webcontent. PII in retour-content wordt geredacteerd vóór opslag |

### LIA — Bronarchief (Art. 6(4) doelbindingstoets)

Het bronarchief is een **nieuw verwerkingsdoel** naast de bestaande ingestion pipeline. De doelbindingstoets conform Art. 6(4) AVG:

| Onderdeel | Beoordeling |
|-----------|-------------|
| **Belang** | Full-text archivering van publieke bronnen ten behoeve van research-context, vervolgvragen en toekomstige RAG — aanvullend op de kennisverspreiding via de knowledge graph |
| **Noodzaak** | Het bronarchief bewaart volledige teksten die bij de ingestion pipeline worden gereduceerd tot taxonomie-mappings. De volledige tekst is nodig voor contextrijke vervolgvragen en citatie-verificatie |
| **Afweging** | Verenigbaar met het oorspronkelijke doel (kennisverspreiding publieke academische content): dezelfde soort bronnen, dezelfde soort persoonsgegevens (auteursnamen), aanvullende waarborgen (PII-redactie vóór opslag, bewaartermijn 24m, blocked_authors.txt). Het risico voor betrokkenen neemt niet toe t.o.v. de ingestion pipeline |

Verwijs naar `docs/DATA_GLOSSARY.md` voor de basis-LIA en verwerkersregistratie.

---

## 3. Bronlagen per BB/GR

Niet elke BB/GR heeft dezelfde bronmix nodig. Onderstaande tabel geeft de primaire bronlagen aan.

### Building Blocks

| BB | Primaire bronlagen | Toelichting |
|----|--------------------|-------------|
| Knowledge | Web, Proprietary | Veel open content over AI literacy, skills frameworks |
| Client Blueprint | Web, Full-text | Case studies, solution architectures |
| Dynamic Context | Proprietary, Web | RAG papers, technische blogs |
| Prompt Design | Web, Full-text | Snel veranderend veld, veel open content |
| Tool Integration | Web, Full-text | API docs, integratie-tutorials, technische blogs |
| Model Engines | Proprietary, Web | Papers (arXiv), model benchmarks, release notes |
| Evaluation Loop | Proprietary, Web | Papers over evaluatie-methodologie, benchmark datasets |

### Guardrails

| GR | Primaire bronlagen | Toelichting |
|----|--------------------|-------------|
| Human Agency | Web, References | EU AI Act, OECD guidelines, policy docs |
| Robustness | Proprietary, Web | NIST AI RMF, technische papers, red teaming |
| Privacy | References, Proprietary | AVG/GDPR updates, EDPB guidance, privacy engineering |
| Fairness | Proprietary, Web | Fairness papers, bias audits, EU standaarden |
| Transparency | References, Web | AI Act transparantie-eisen, explainability research |
| Well-being | Web, References | Societal impact studies, sustainability, labor market |
| Accountability | References, Proprietary | Governance frameworks, audit standaarden, ISO 42001 |

### Uitgesloten brontypen

De volgende brontypen worden **niet** meegenomen in web research:

| Uitgesloten | Reden |
|-------------|-------|
| YouTube | Video-content, geen tekst; apart verwerkingsproces nodig |
| LinkedIn | Korte posts, moeilijk te crawlen, login-walls |
| X / Twitter | Korte posts, lage informatiedichtheid, moeilijk te verifiëren |
| GitHub | Code repositories, geen kennisartikelen (issues/discussions te ruis-vol) |
| Reddit | Forumcontent, wisselende kwaliteit, moeilijk te verifiëren |
| Quora | Forumcontent, wisselende kwaliteit, SEO-geoptimaliseerd |

**Wel toegestaan:** Blogs, nieuwssites, officiële documentatie, papers (arXiv, PubMed, IEEE), standaarden (NIST, ISO, EU), onderzoeksrapporten, conference proceedings, tech blogs met bronvermelding.

---

## 4. Research pipeline (8 stappen)

### Stap 1: Plan

Voordat je gaat zoeken, definieer per BB/GR:

- **Focus-vragen** (max 3): Wat wil je specifiek weten?
- **Tijdsvenster**: krimpend per run (zie schema hieronder)
- **Inclusiecriteria**: taal (EN/NL), brontype, minimale kwaliteit
- **Uitsluitingen**: marketing content, verouderde versies, niet-peer-reviewed opinies, uitgesloten brontypen (§3)

#### Krimpend tijdsvenster

De AI-wereld verandert snel. Om bij de eerste run een brede basis te leggen en daarna gericht bij te werken, krimpt het tijdsvenster per run:

| Run | Tijdsvenster | Toelichting |
|-----|-------------|-------------|
| 1e (baseline) | Laatste 12 maanden | Brede basis leggen |
| 2e | Laatste 6 maanden | Verdieping, nieuwe ontwikkelingen |
| 3e | Laatste 3 maanden | Recente updates |
| 4e+ | Laatste maand | Wekelijkse bijhouding |

**Overlap-check:** Voordat je een run start, controleer de `docs/research/INDEX.md` op de laatst onderzochte datum per BB/GR. Als het tijdsvenster overlapt met de vorige run, verklein het venster zodat alleen de nieuwe periode wordt gedekt. Voorbeeld: vorige run onderzocht t/m 2026-03-15, huidige run begint bij 2026-03-15.

Voorbeeld voor *Prompt Design* (1e run):
```
Focus-vragen:
1. Welke nieuwe prompt engineering technieken zijn sinds 2025 mainstream geworden?
2. Zijn er nieuwe benchmarks of evaluatieframeworks voor prompt kwaliteit?
3. Hoe verandert prompt design met de opkomst van agentic workflows?

Tijdsvenster: 2025-04 — 2026-04 (baseline run)
Inclusie: peer-reviewed papers, officiële docs, gevestigde tech blogs
Uitsluiting: listicles, SEO-content, tutorials zonder bronvermelding
```

### Stap 2: Search

Genereer **3-5 gerichte queries** per focus-vraag, vanuit verschillende invalshoeken:

| Query-type | Voorbeeld |
|------------|-----------|
| Definitie | "prompt engineering techniques 2026 survey" |
| Officieel | "prompt design best practices site:anthropic.com OR site:openai.com" |
| Academisch | "prompt optimization evaluation framework arxiv 2025" |
| Vergelijking | "chain-of-thought vs tree-of-thought performance comparison" |
| Recency | "prompt engineering agentic AI 2026" |

**Toolkeuze:** Zie §8 voor volledige tooling-tabel. Kort:
- `firecrawl_search` met `-site:` operatoren voor domeinfiltering (primair)
- `exa_web_search` met freshness filter voor semantische verkenning
- Resultaten altijd filteren op uitgesloten brontypen (§3) vóór selectie

### Stap 3: Select

Beoordeel elke gevonden bron op kwaliteit voordat je de volledige content ophaalt.

**Harde filters (automatisch):**
- Verwijder uitgesloten brontypen (§3): YouTube, LinkedIn, X, GitHub, Reddit, Quora
- Verwijder content farms, SEO-spam, marketing zonder bronvermelding
- Verwijder bronnen ouder dan het gedefinieerde tijdsvenster (krimpend per run)
- Verwijder duplicaten (zelfde content op meerdere sites)

**Zachte scoring:**

| Criterium | Score |
|-----------|-------|
| Officieel document / primaire bron | +3 |
| Peer-reviewed paper of gevestigd onderzoeksinstituut | +3 |
| Gevestigde tech blog met bronvermelding | +2 |
| Bevat publicatiedatum en auteur | +1 |
| Onbekend domein zonder referenties | -2 |
| Content farm / zware ads | -3 |

**Selecteer top 5-8 bronnen** per BB/GR op basis van score.

**Early exit (low-yield check):** Als na filtering minder dan 2 bronnen overblijven die de scoring-drempel halen, stop de pipeline voor dit onderwerp. Dit bespaart 30+ minuten op een run die toch geen bruikbare output oplevert. Noteer in INDEX.md:
- Status: `low-yield`
- Reden: bijv. "1 bron gevonden, onvoldoende voor two-source rule"
- Actie: verschuif naar de volgende cyclus. Als 3 opeenvolgende runs low-yield zijn, verlaag de cadans voor dit onderwerp naar kwartaal.

### Stap 4: Fetch + Archiveer

Haal de volledige content op van geselecteerde bronnen en archiveer interessante bronnen.

**Ophalen:**
- Gebruik `mcp__exa__crawling_exa` voor meerdere URLs tegelijk
- Standaard `maxCharacters: 50000` — ook voor bronnen die gearchiveerd worden
- Voor snelle screening: `maxCharacters: 5000` is voldoende
- **Lange bronnen (arXiv, standaarden, >50K tekens):** twee-staps fetch:
  1. Eerst metadata + abstract ophalen (`maxCharacters: 5000`)
  2. Beoordeel of volledige tekst nodig is → zo ja, haal relevante secties op in delen
  3. Combineer de delen in het bronarchief met `[...]` markering bij weggelaten secties

**Sanitisatie (verplicht vóór archivering):**
- Strip raw HTML, script-tags en potentieel gevaarlijke markdown-constructies
- Voer PII-scan uit: redacteer e-mailadressen, telefoonnummers en andere contactgegevens
- Check auteursnamen tegen `blocked_authors.txt` — bij match: redacteer naam
- Pas dezelfde redactielogica toe als de bestaande ingestion pipeline (`backend/app/ingestion/pii.py`)

**Archivering (naar NI-patroon):**

Het bronarchief is een **staging area** voor research-context. Het dient als:
- **Eigen database** — bij vervolgvragen direct doorzoekbaar zonder opnieuw te fetchen
- **RAG-basis** — toekomstige vector search over volledige teksten
- **Provenance** — elke claim is traceerbaar naar de originele tekst

Bronnen die **permanent** in de knowledge graph moeten (frameworks, standaarden, referentiepapers), gaan daarnaast via `make ingest-item` naar Neo4j + LightRAG. Het archief wordt periodiek opgeschoond (zie §2b bewaartermijn).

```
docs/research/bronnen/
  bron-001.md    # Eerste bron
  bron-002.md    # Tweede bron
  ...
```

Template per bron:

```markdown
---
id: bron-NNN
title: "Titel van het artikel"
url: "https://..."
author: "Naam auteur"
date: "2026-01-15"
archived: "2026-04-03"
bb_gr: ["Prompt Design", "Evaluation Loop"]
type: "paper|blog|report|standard|documentation"
volledige_tekst: true
---

## Samenvatting

[2-3 zinnen over de kern van het artikel]

## Relevante passages

[Passages die relevant zijn voor de gelinkte BB/GRs, met sectieverwijzing]

## Kernquotes

> "Exacte quote 1" — sectie/pagina
> "Exacte quote 2" — sectie/pagina

## Volledige originele tekst

[Volledige tekst zoals opgehaald, in markdown]
```

**Criteria voor archivering:**
- Bron scoort ≥ +2 in de selectie-scoring (Stap 3)
- Bevat statistieken, frameworks of best practices die we willen citeren
- Is een primaire bron of peer-reviewed paper
- Niet archiveren: nieuwsartikelen met alleen secondaire informatie, korte blogposts zonder onderbouwing

**Triage naar knowledge graph:**
- Bron met score ≥ +3 EN type `paper|standard|documentation` → ook via `make ingest-item` toevoegen aan Neo4j + LightRAG
- Voeg aan de frontmatter `ingested: true` toe met de Neo4j `source_url` als koppeling

**Bewaartermijn:** Max 24 maanden (conform §2b). Bronnen die na de termijn niet zijn doorgesluisd naar de knowledge graph, worden verwijderd of geanonimiseerd. Jaarlijkse opschoningsronde.

### Stap 5: Clean

Wordt automatisch afgehandeld door de crawling tools (markdown output, boilerplate verwijderd). Bij handmatige verwerking: verwijder navigatie, ads, cookie-banners, footers.

### Stap 6: Extract

Per bron, extraheer gestructureerde evidence. **Niet samenvatten, maar evidence vastleggen.**

Schema per extractie:

```yaml
- claim: "Korte feitelijke bewering"
  quote: "Exacte quote uit de bron (1-3 zinnen)"
  url: "https://..."
  author: "Naam auteur"
  date: "2026-01-15"
  confidence: 0.85  # 0.0-1.0
  bb_gr: ["Prompt Design"]  # welke BB/GR raakt dit
  type: "statistic|best-practice|framework|tool|trend|regulation"
```

**Types evidence:**
- `statistic` — getal, percentage, benchmark score
- `best-practice` — aanbevolen werkwijze met onderbouwing
- `framework` — gestructureerd model of methodologie
- `tool` — specifieke tool, library of platform
- `trend` — opkomende ontwikkeling of verschuiving
- `regulation` — wet, standaard, richtlijn

### Stap 7: Verify

Verificatie is een **aparte stap**, niet onderdeel van extractie.

**Checks:**

1. **Quote-ondersteunt-claim**: Onderbouwt de exacte quote daadwerkelijk de claim?
   - Ja → behouden
   - Vaag → confidence verlagen
   - Nee → verwijderen

2. **Two-source rule**: Heeft de claim minstens 2 onafhankelijke bronnen?
   - Ja → confidence ≥ 0.8
   - Eén primaire bron (officieel doc) → confidence ≥ 0.7
   - Eén secundaire bron → confidence ≤ 0.6, markeer als "needs verification"

3. **Freshness check**: Is de informatie nog actueel?
   - Bron < 6 maanden → OK
   - Bron 6-12 maanden → check of er nieuwere info is
   - Bron > 12 maanden → alleen behouden als het een standaard/referentie betreft

4. **Consistentie**: Spreken bronnen elkaar tegen?
   - Ja → beide perspectieven vastleggen, niet middelen
   - Onzekerheid expliciet benoemen

### Stap 8: Synthesize

Per BB/GR een gestructureerd overzicht samenstellen:

```markdown
## [BB/GR naam] — Research Update [datum]

### Samenvatting
[2-3 zinnen: wat is er veranderd/nieuw sinds de vorige update?]

### Belangrijkste bevindingen
1. [Claim] — [Bron 1], [Bron 2]
2. [Claim] — [Bron 1], [Bron 2]

### Statistieken & benchmarks
| Metric | Waarde | Bron | Datum |
|--------|--------|------|-------|

### Aanbevelingen voor content-update
- [ ] Beschrijving bijwerken: [wat en waarom]
- [ ] Nieuwe best practice toevoegen: [welke]
- [ ] Statistiek vervangen: [oude → nieuwe]

### Open vragen
- [Wat kon niet geverifieerd worden?]

### Bronnen
1. [Auteur (jaar). Titel. URL]
2. ...

### Metadata
- Queries uitgevoerd: [N]
- Bronnen geraadpleegd: [N]
- Bronnen geselecteerd: [N]
- AI-assisted: ja (Claude Code + Exa/Firecrawl)
```

---

## 5. Output & opslag

### Mappenstructuur

```
docs/research/
  INDEX.md                           # Status per BB/GR (zie hieronder)
  YYYY-MM-DD-{bb|gr}-{slug}.md      # Research output per sessie
  bronnen/                           # Full-text bronarchief
    bron-001.md                      # Gearchiveerde bron (template zie §4.4)
    bron-002.md
    ...
```

### Research output per sessie

Bestandsnaam: `YYYY-MM-DD-{bb|gr}-{slug}.md`
Voorbeeld: `2026-04-03-bb-prompt-design.md`

### Bronarchief

Alle gearchiveerde bronnen staan in `docs/research/bronnen/`. Nummering is doorlopend (bron-001, bron-002, ...) ongeacht BB/GR. De koppeling naar BB/GR zit in de frontmatter (`bb_gr` veld).

Het bronarchief dient als:
1. **Eigen database** — bij vervolgvragen direct doorzoekbaar zonder opnieuw te fetchen
2. **RAG-basis** — toekomstige vector search over volledige teksten
3. **Provenance** — elke claim is traceerbaar naar de originele tekst

### Index

`docs/research/INDEX.md` houdt de status per BB/GR bij:

| BB/GR | Laatst onderzocht | Run # | Tijdsvenster | Bronnen | Open acties |
|-------|-------------------|-------|-------------|---------|-------------|
| Prompt Design | 2026-04-03 | 1 (baseline) | 2025-04 — 2026-04 | 5 | 2 |
| ... | | | | | |

---

## 6. Processchema

### MVP-cadans (maandelijks, 2 BB/GR per sessie)

**Voorbereiding (5 min)**
1. Check INDEX.md: welke BB/GR is aan de beurt?
2. Sync Bastionclaw use-cases en check NI repo (als er nieuwe zijn)

**Research (20-30 min per BB/GR)**
3. Voer de pipeline uit (MVP: 3 stappen, volledig: 8 stappen)
4. Leg resultaten vast in `docs/research/`

**Verwerking (10-15 min)**
5. Update `CROSS_PROJECT_MAPPING.md` als er nieuwe koppelingen zijn
6. Verwerk content-updates direct in `frontend/src/content/`

### Rotatieschema (maandelijks)

Per maand 2 sessies van elk 2 BB/GR. In 4 maanden zijn alle 14 onderwerpen behandeld. Snel veranderende onderwerpen kunnen vaker aan de beurt komen.

| Maand | Sessie 1 | Sessie 2 |
|-------|----------|----------|
| 1 | Prompt Design, Model Engines | Knowledge, Dynamic Context |
| 2 | Tool Integration, Evaluation Loop | Client Blueprint, Privacy |
| 3 | Human Agency, Robustness | Transparency, Fairness |
| 4 | Well-being, Accountability | Herhaalsessie snel-veranderende BB/GRs |

### Opschaling naar wekelijks (optioneel, na lancering)

Activeer het volledige 4-weken rotatieschema alleen als:
- BeeHaive.org live is met actieve gebruikers
- De MVP-cadans onvoldoende diepgang oplevert (evaluatie na 4 maanden)
- Het capaciteitsbudget (§7) dit toelaat

---

## 7. Kwaliteitscriteria & successcriteria

### Per research output

- [ ] Minimaal 3 bronnen per BB/GR
- [ ] Two-source rule nageleefd voor alle feitelijke claims
- [ ] Alle claims hebben een exacte quote als onderbouwing
- [ ] Freshness: geen bronnen ouder dan 12 maanden (tenzij standaard/referentie)
- [ ] Bronnen gelogd met URL, auteur, datum
- [ ] AI-disclosure aanwezig in metadata

### Per content-update

- [ ] Wijziging is traceerbaar naar research output
- [ ] Oude statistieken/claims zijn vervangen, niet alleen aangevuld
- [ ] Cross-check met Bastionclaw use-cases en NI-artikelen

### Successcriteria protocol

| Criterium | Meting |
|-----------|--------|
| **Per run** | Minimaal 2 actionable content-updates per BB/GR-sessie |
| **Stopcriterium** | Als 3 opeenvolgende runs voor dezelfde BB/GR geen nieuwe inzichten opleveren → pauzeer die BB/GR, verlaag cadans naar kwartaal |
| **Evaluatiemoment** | Na de eerste volledige cyclus (4 weken): beoordeel of de cadans, diepgang en tijdsinvestering passend zijn. Pas het schema aan op basis van werkelijke resultaten |
| **Actualiteitsdrempel** | Een BB/GR is actueel als: (1) geen claim ouder dan 12m zonder standaard-status, (2) geen statistiek met nieuwere versie beschikbaar, (3) geen relevante regulering gemist. Haalt een BB/GR alle drie → sla die ronde over |

### Capaciteitsbudget

| Fase | Tijdsinvestering | Wie |
|------|-----------------|-----|
| **Pilot (nu)** | 1-2 uur eenmalig voor 1-2 BB's | Robin + Claude Code |
| **MVP (na Fase 3)** | ~2 uur per maand (2 sessies × ~1 uur) | Robin + Claude Code |
| **Volledig (na lancering)** | ~4-6 uur per maand | Evalueren of dit past |

Prioriteit: development-werk gaat altijd voor research. Bij tijdsdruk: sla de research-ronde over en hervat de volgende maand. Gemiste rondes verschuiven de cyclus, er worden geen BB/GRs overgeslagen.

---

## 8. Tooling

### Huidige tools (beschikbaar in Claude Code)

| Tool | Sterkte | Gebruik voor | Bronbeperking |
|------|---------|-------------|---------------|
| `mcp__exa__web_search_exa` | Semantische search, freshness filter, relevantie-ranking | Brede verkenning: "ontdek wat er is" over een BB/GR | `excludeDomains` ondersteunt niet — handmatig filteren |
| `mcp__exa__crawling_exa` | Batch full-text ophalen, subpage crawling | Full-text archivering van geselecteerde bronnen | Haalt elke URL op — bronbeperking in Search-stap |
| `mcp__firecrawl__firecrawl_search` | Web search met inline content, operatoren (`site:`, `-site:`) | Gerichte search met domeinfilters | `-site:reddit.com -site:linkedin.com` etc. |
| `mcp__firecrawl__firecrawl_extract` | Structured JSON extractie uit URLs | Specifieke velden uit bekende pagina's (statistieken, tabellen) | N.v.t. — werkt op bekende URLs |

### Domeinfilters toepassen

Om de uitgesloten brontypen (§3) te handhaven, gebruik bij elke search:

**Firecrawl** (via query-operatoren):
```
query + " -site:youtube.com -site:linkedin.com -site:twitter.com -site:x.com -site:github.com -site:reddit.com -site:quora.com"
```

**Exa** (geen native exclude-domeinen — handmatig filteren):
Na zoekresultaten: verwijder resultaten met URLs die matchen op uitgesloten domeinen voordat je naar Stap 3 (Select) gaat.

### Toolkeuze per stap

| Pipeline-stap | Primaire tool | Alternatief |
|--------------|---------------|-------------|
| **Search (web)** | `firecrawl_search` (domeinfilters) | `exa_web_search` (semantisch) |
| **Search (academisch)** | `exa_web_search` (query: "site:arxiv.org OR site:scholar.google.com") | `firecrawl_search` met `site:` operators |
| **Search (standaarden)** | `firecrawl_search` met `site:nist.gov OR site:iso.org OR site:eur-lex.europa.eu` | — |
| **Fetch (full-text)** | `exa_crawling` (batch, maxCharacters: 50000) | `firecrawl_extract` (structured) |
| **Extract (structured)** | `firecrawl_extract` (JSON schema) | Handmatig uit crawl-output |

### Valyu (toekomstige integratie)

Valyu biedt een unified API die web + academisch + proprietary combineert — relevant voor onze use case:

| Valyu feature | Ons voordeel | Status |
|--------------|-------------|--------|
| **Search API** (`searchType: "all"/"web"/"proprietary"`) | Eén call voor web + arXiv + PubMed | Nog niet geïntegreerd |
| **Proprietary sources** (`valyu/valyu-arxiv`, `valyu/valyu-pubmed`) | Directe full-text access tot papers zonder scraping | MCP server beschikbaar |
| **Date filtering** (`startDate`, `endDate`) | Past perfect bij krimpend tijdsvenster | — |
| **Domain exclusion** (`excludeSources: ["reddit.com", ...]`) | Native bronbeperking | — |
| **Contents API** | Full-text + AI-summary in één call | — |
| **DeepResearch** | Autonome research agent met citaties | — |
| **Pricing** | $0.003/result (web), $0.01+/result (proprietary) | $10 gratis credits bij aanmelding |

**Aanbeveling:** Valyu MCP server installeren voor de academische bronlagen (arXiv, PubMed). Dit vervangt de huidige workaround van `site:arxiv.org` queries en geeft directe full-text access met DOI, citaties en auteursinformatie.

```bash
# Valyu MCP server installatie (toekomstig)
git clone https://github.com/ValyuNetwork/valyu-mcp.git
cd valyu-mcp && python -m venv .venv && pip install -r requirements.txt
# Config toevoegen aan .claude/settings.json
```

### BeeHaive ingestion pipeline

Voor bronnen die permanent in de knowledge graph moeten:
- `make ingest-item URL=<url>` — verwerkt via fetcher → PII scan → Gemini classificatie → Neo4j + LightRAG
- Hergebruikt de bestaande taxonomie-mapping naar BB/GR
- Complementair aan het bronarchief: archief = research context, pipeline = knowledge graph

---

## 9. Referenties

- Valyu Search API — tiered data retrieval voor AI agents, unified web + proprietary + academic search (valyu.ai)
- Valyu JS SDK — search, contents en DeepResearch API (github.com/valyuAI/valyu-js)
- Valyu MCP Server — MCP integratie voor Claude Code (github.com/ValyuNetwork/valyu-mcp)
- Arun Baby — "Web Browsing Agents" pipeline architectuur, 8-staps model (arunbaby.com)
- Skywork — "AI Research Workflow Ultimate Guide" met provenance en research notebook (skywork.ai)
- Natural Intelligence bronarchief — template en patroon voor full-text archivering (zusterproject)
