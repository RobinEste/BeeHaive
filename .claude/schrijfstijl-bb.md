# Schrijfstijl BeeHaive BB- en GR-pagina's

Werkdocument. Gebaseerd op correcties tijdens het herschrijven van BB_03 Dynamic Context (april 2026). Wordt na elke BB en GR bijgewerkt. Doel: consistente, toegankelijke, zakelijk-precieze teksten voor het `frontend/src/content/building-blocks/*.mdx` en `frontend/src/content/guardrails/*.mdx` die de pagina's op beehaive.org voeden.

---

## Lezer-aanname

Business-professional — consultant, eigenaar, operationeel manager of productowner. Niet een AI-engineer. Kan complexe concepten aan **mits** ze in zakelijke taal worden aangeboden. Wil begrijpen *waarom* iets belangrijk is voor haar organisatie, niet alleen *hoe* het technisch werkt.

De tekst moet functioneren zonder voorkennis van AI-jargon, maar mag wél veeleisend zijn in analytische diepgang.

---

## 1. Vakterm → NL + Engelse term cursief

Elke niet-algemene Engelse term krijgt bij **eerste gebruik** een korte NL-vertaling tussen haakjes, met de Engelse term cursief als die internationaal gangbaar is.

- ✓ `goedkeuringsroutes (*approval chains*: wie moet waarvoor toestemming geven)`
- ✓ `data-herkomst (van brondocument tot antwoord traceerbaar — in het Engels *data-lineage*)`
- ✗ `implementeer een approval chain voor...` (geen uitleg bij eerste gebruik)

**Parafrase-regel.** Als de letterlijke NL-vertaling zélf jargon is, gebruik een concrete parafrase in lopende tekst — niet een jargon-voor-jargon-vervanging:

- ✗ `kennisgraaf` (Nederlands maar academisch; niet-techneut snapt het niet)
- ✓ `kennisnetwerk (entiteiten als knooppunten, relaties tussen entiteiten als verbindingen)`
- ✗ `nabij-getraind op jouw specifieke categorieën`
- ✓ `een bestaand taalmodel dat je extra hebt getraind op jouw specifieke categorieën`
- ✗ `signaal-dichtheid`
- ✓ `méér relevante informatie per token — dat is wat "signaal-dichtheid" betekent`

**Test**: kan een zakelijke lezer na het lezen van de zin zelf de term uitleggen? Zo nee: parafraseer.

**Let op anglicismen in idiomen.** Letterlijk vertaalde Engelse uitdrukkingen lezen als fout Nederlands, ook al zijn alle woorden NL. Herken en vervang door een echt bestaand NL-idioom of een neutrale parafrase:

- ✗ *"alles-en-de-keukenkraan"* (uit *everything and the kitchen sink*)
- ✓ *"alles op een hoop gegooid"*
- ✗ *"aan het einde van de dag"* (uit *at the end of the day*)
- ✓ *"uiteindelijk"*
- ✗ *"de olifant in de kamer"* (uit *elephant in the room*) — wel ingeburgerd maar vermijd voor zakelijke tekst
- ✓ *"het onbesproken probleem"*

**Test**: als je twijfelt of een uitdrukking Nederlands is, zoek hem in Van Dale of bij een Nederlandstalige nieuwsbron. Geen hits? Letterlijke vertaling uit het Engels; herschrijf.

Afkortingen worden pas gebruikt nadat ze zijn uitgeschreven:
- ✓ `Model Context Protocol (MCP: een opkomende standaard om...)` → daarna vrij `MCP`
- ✗ `BB_03` als eigennaam — gebruik `Dynamic Context`, desnoods met `(BB_03)` achter de naam

## 2. Business-termen in Nederlands

Waar afdelings-/rolnamen voorkomen: kies Nederlands tenzij een Engels woord daadwerkelijk breed is ingeburgerd.

| Voorkeur | Vermijd |
|----------|---------|
| Verkoop | Sales |
| Productmanagement | Product |
| Klantenservice | Customer Success |
| Marketing | *(ingeburgerd, mag blijven)* |
| Inkoop | Procurement |
| Juridisch | Legal |

## 3. Voorbeelden uit de business, niet uit code

Als je een concept illustreert met een voorbeeld: kies een scenario dat elke organisatie herkent, niet iets uit een ontwikkelomgeving.

- ✓ "een klantdossier met vier verschillende adressen uit vier verschillende jaren"
- ✓ "oude versies van beleid naast de huidige"
- ✗ "test-fixtures in code-search"
- ✗ "grep-resultaten in een repo"

## 4. Standaard-definities (herbruikbaar op alle pagina's)

Bij eerste voorkomen op een pagina: één tussen-haakjes-zin of korte parenthese. Hieronder de canonieke formuleringen — copy-paste, dan blijven we over de site consistent.

| Term | Standaarddefinitie |
|------|---------------------|
| context window | de hoeveelheid tekst die een model in één keer kan verwerken |
| tokens | stukjes tekst van grofweg 3–4 letters; 1M tokens ≈ 750.000 woorden |
| agent | AI-systeem dat zelfstandig acties uitvoert |
| RAG | Retrieval-Augmented Generation — documenten ophalen uit een kennisbank en meegeven aan het model |
| MCP | Model Context Protocol — opkomende standaard om AI-systemen met externe data en tools te verbinden |
| data-lineage | data-herkomst: van brondocument tot antwoord traceerbaar |
| degradeert | in kwaliteit achteruitgaat |
| chunks | stukjes waarin een document wordt opgeknipt voor het ophalen uit de kennisbank |
| embedding | wiskundige representatie van tekst die semantische gelijkenis meetbaar maakt |
| embedding-model | taalmodel dat tekst omzet naar een reeks getallen zodat een computer kan uitrekenen hoe sterk twee stukken tekst op elkaar lijken |
| reranker | tweede-pass-model dat opgehaalde documenten herordent op relevantie — leest vraag en document sámen |
| retrieval | het ophalen van relevante documenten of fragmenten uit een kennisbank voor het model |
| prompt | de instructie die je aan een AI-model geeft |
| system prompt | de overkoepelende instructie die het gedrag van een AI over álle gesprekken heen stuurt |
| few-shot | 2–5 diverse voorbeelden in de prompt zodat het model zich kalibreert op gedrag dat moeilijk in regels te vangen is |
| hallucinatie | het verzinnen van feiten door een model die plausibel klinken maar niet kloppen |
| top-K | de K meest gelijkende documenten die een zoeksysteem teruggeeft — typisch 5, 10 of 20 |
| BM25 | klassiek keyword-matching-algoritme — vindt exacte termen die semantisch zoeken mist |
| prompt caching | al-door-het-model-verwerkte tokens hergebruiken tussen aanroepen, voor kosten- en latency-winst |
| contextual retrieval | Anthropic-methode: korte contextuele annotatie vóór indexering per chunk plakken |
| jagged frontier | onvoorspelbare, taakafhankelijke grens tussen wat AI goed kan en waar het subtiel faalt |
| operating agreement | schriftelijke afspraak per AI-proces: wie beslist, waar zit human-in-the-loop, wat is "klaar" |
| FOBO | Fear of Becoming Obsolete — de stille drijfveer achter AI-vermijding door medewerkers |
| decision intelligence | Kozyrkov's kader: knelpunt verschuift van uitvoering ("genie-kant") naar probleem-formulering ("wens-kant") |
| centaur / cyborg | twee mens-AI-samenwerkingspatronen: centaur = duidelijke taakscheiding, cyborg = diepe integratie |
| orchestrator | rol waarin een mens een systeem van AI-agents ontwerpt in plaats van zelf naast AI te werken |
| deskilling | het eroderen van menselijke expertise doordat AI taken overneemt en de professional stopt met oefenen |

*(Deze tabel groeit na elke BB/GR die we afronden.)*

## 5. Eerst concreet, dan abstract

Elk getal krijgt óók een menselijke eenheid:
- ✓ `50–200 tokens (ongeveer 40–150 woorden)`
- ✓ `32K tokens (ruim 20.000 woorden — de omvang van een kort rapport)`

Elke metafoor wordt eerst uitgelegd en daarna pas bondig gebruikt:
- ✓ "hoe meer tekst je het model voert, hoe minder aandacht elke zin afzonderlijk krijgt"
- ✗ "het signaal wordt niet luider — de ruisvloer stijgt" (zonder voorafgaande uitleg)

## 6. Claims eerlijk contextualiseren

- Noem **het jaar** van onderzoek/benchmark bij eerste vermelding
- Zeg expliciet of cijfers verouderen: *"de cijfers zijn meer dan een jaar oud en gelden voor 2024-2025-modelversies; moderne modellen presteren doorgaans beter op hetzelfde type taken, maar de richting is consistent"*
- **Richting > absolute waarden** — claim liever een richting die stand houdt dan een specifiek percentage dat achterhaald raakt
- Geen cijfer zonder bron; geen bron zonder jaartal

## 7. Stijl-tic: actief voor oorzaak, passief voor systeem-gevolg

Vermijd menselijke intenties toeschrijven aan AI-systemen in gevolg-zinnen. Dat leest alsof de agent iets "wil" of "beslist" — terwijl je het over een systeem-effect hebt.

- ✗ *"Een autonome agent die een verkeerde definitie hanteert, keurt korting goed op basis van verkeerde criteria, escaleert tickets naar verkeerde teams..."*
- ✓ *"Een verkeerde definitie kan leiden tot kortingen die goed worden gekeurd op basis van niet-correcte criteria, klantvragen die bij verkeerde teams terecht komen..."*

De passieve vorm benadrukt dat het probleem het **ontwerp** is, niet het "gedrag" van het systeem.

## 8. Interpunctie in NL

**Na vetgedrukt kopje hoort `:`, geen `—`.** Dit is het belangrijkste verschil met Engels schrijven en het meest-voorkomende foutpatroon:

- ✗ `**Systeeminstructies & rol-definities** — wie is de agent...`
- ✓ `**Systeeminstructies & rol-definities**: wie is de agent...`

Geldt voor bullets, tabelkoppen in proza, en alinea-openers. Test: als de zin begint met een vetgedrukt *onderwerp* gevolgd door zijn *definitie*, dan `:`.

**`;` boven `—` voor zin-koppel.** Em-dashes zijn voor zijsprongen, niet voor "en-nog-iets":

- ✗ *"komt te laat — de schade is al aangericht"*
- ✓ *"komt te laat; de schade is al aangericht"*
- ✗ *"het patroon blijft — het is een structurele eigenschap"*
- ✓ *"het patroon blijft: het is een structurele eigenschap"* (hier is `:` want tweede helft expliciteert de eerste)

**Em-dash: alleen als dubbele dash rond een tussenzin.** Een enkele em-dash in een zin is bijna altijd fout in NL. De regel is streng:

- ✓ *"Chroma's onderzoek testte **18 frontier-modellen** — inclusief GPT-4.1, Claude Opus 4, Gemini 2.5 Pro — en vond dat elk model degradeert."* (dubbele em-dash rondom tussenzin)
- ✗ *"een verouderde kennisbank geeft een antwoord — structureel correct, zelfverzekerd van toon..."* (losse em-dash)
- ✓ *"een verouderde kennisbank geeft een antwoord; structureel correct, zelfverzekerd van toon..."* (met `;`)
- ✗ *"definitie — en zonder die definitie..."* (losse em-dash)
- ✓ *"definitie. En zonder die definitie..."* of *"definitie, en zonder die definitie..."*

**Check**: zoek in je diff op ` — ` (met spaties). Elke hit moet óf een openings-em-dash óf een sluitings-em-dash van een tussenzin zijn. Als er maar één losse em-dash staat in een zin, herformuleer: `;`, `.`, `,`, of de zin opbreken.

**Blinde vlek: je eigen concept-voorstellen.** Em-dashes zijn in Engelstalige training diep ingebakken; ze sluipen terug in voorstellen die je zelf aanbiedt *terwijl je de regel uitlegt*. Voor je een concept-zin, herschreven alinea of Quick Start-voorstel presenteert: scan je eigen tekst op ` — ` en vervang eerst. Als een reviewer jouw voorstel nog moet corrigeren op iets wat je zelf als regel hebt geformuleerd, ondermijnt dat de regel.

**Komma-voegwoordje tussen gelijkwaardige zinsdelen**: *"slechte antwoorden, kortingen die goed worden gekeurd..."* → `;` als het tweede deel een andere gedachtelijn is: *"slechte antwoorden; kortingen die ..."*.

**Aanhalingstekens** liggend NL-stijl ("zo") of typografisch ("zó"), niet rechtop in body-tekst.

**NL-grammatica**: geen bepalers verzwijgen zoals in EN. *"Simpel splitsen elke 512 tokens"* → *"Simpel splitsen **van** elke 512 tokens"*.

## 9. Opsommingen: labels met uitleg, niet alleen labels

Als een opsomming technische termen bevat die betekenisdragend zijn: geef per bullet een korte uitleg.

- ✗ *"Drie disciplines: bundle-engineering, chunk-precisie en context-isolatie blijven blijvende ontwerpdisciplines"*
- ✓ per bullet:
  - **bundle-engineering** — bewust samenstellen welke stukjes context je op welk moment aan het model aanbiedt
  - **chunk-precisie** — documenten zó opknippen dat elk stukje zelfstandig betekenisvol is
  - **context-isolatie** — subvragen in aparte context-sessies afhandelen zodat hun zoek- en verwerpfase de hoofdcontext niet vervuilt

## 10. Cross-refs: naam + code + kernzin

Wanneer je voor het eerst naar een andere BB of GR verwijst:

- ✓ *"Robustness-guardrail (GR_02: betrouwbaarheid onder alle omstandigheden)"*
- ✓ *"Evaluation Loop (BB_06 — meten, analyseren, verbeteren, opnieuw meten)"*
- ✗ *"GR_02"* (zegt de lezer niets)
- ✗ *"Robustness (GR_02)"* (naam + code zonder kernzin)

Bij vervolgverwijzingen op dezelfde pagina: alleen naam, geen code meer.

## 11. Slotzinnen: concreet, geen galm

Een sectie-afsluitende zin moet **iets nieuws zeggen** of een beeld achterlaten, niet de stelling herhalen in abstracte taal.

- ✗ *"context rot is een systemische, stille faalmodus die robuuste AI-systemen expliciet moeten ontwerpen"*
- ✓ *"context rot geeft geen foutmelding, het geeft een plausibel maar verkeerd antwoord. Juist daarom moet een robuust AI-systeem vooraf ontworpen zijn om deze stille faalmodus op te vangen — monitoren kan niet wat niet zichtbaar faalt."*

Test: als je de slotzin weghaalt, mist de lezer iets? Zo nee: weghalen of herschrijven.

## 12. Consistente terminologie binnen één pagina

Kies één term en houd die vast:
- ✓ `context window` (overal hetzelfde)
- ✗ `context window` / `model window` / `window` door elkaar

De bewoording in frontmatter (`checklist`, `quickStart`, `evidence`) moet **dezelfde termen** gebruiken als de body. Als je in de body "staleness-drempels" zegt, niet in de checklist "verouderdheidsgrens".

## 13. Tabellen vs. bullets

Tabellen zijn slecht leesbaar op mobiel zodra ze tekst bevatten. Richtlijn:

- **Tabel alleen voor** numerieke vergelijking over max 3 kolommen, met kleine tabelkoppen (één of twee woorden per kop)
- **Bullets voor** inhoudelijke uitleg per categorie — ook als een tabel "logisch" lijkt
- Als een tabelcel méér dan 8–10 woorden nodig heeft: het moet bullets worden

Voorbeeld — ✗ als tabel:

| Documenttype | Chunk-grootte | Overlap tussen chunks |
|--------------|---------------|------------------------|
| Algemene tekst | 256–512 tokens (ca. 180–350 woorden) | 20–30% |

Voorbeeld — ✓ als bullets:

- **Algemene tekst** (blogs, rapporten): 256–512 tokens per chunk (ca. 180–350 woorden), met 20–30% overlap.

## 14. Koppen: gewone-woorden-toets

Een sectie-kop moet begrijpelijk zijn zonder de sectie zelf te lezen. Vermijd samenstellingen met `-architectuur`, `-engine`, `-tijdperk`, `-pijplijn` en andere abstracties.

- ✗ *"Retrieval-architecturen — van simpele RAG naar context engines"*
- ✓ *"Documenten ophalen: van simpel zoeken naar een intelligente zoekmachine"*
- ✗ *"Context rot — waarom grotere windows geen oplossing zijn"*
- ✓ *"Context rot: waarom meer informatie het probleem niet oplost"*

Test: kan een zakelijke lezer na het lezen van alleen de kop vertellen waar de sectie over gaat? Zo nee: herschrijf.

## 15. Glossary-links maken inline-uitleg vaak overbodig

Sinds hover-tooltips op `/begrippen#slug`-links werken, toont de tooltip automatisch de volledige uitleg van de term. Inline parenthese na de link is dan duplicaat.

- ✗ `[MCP](/begrippen#mcp) — het Model Context Protocol`  (tooltip zegt dit al)
- ✓ `[MCP](/begrippen#mcp)`  (zin blijft leesbaar zonder parenthese)
- ✓ `het [MCP](/begrippen#mcp) — het Model Context Protocol` (behouden alléén als de zin anders onleesbaar wordt voor wie niet hovert)

Regel: **als de term in glossary staat, link plaatsen en parenthese weglaten** — tenzij de vloeiendheid van de zin echt lijdt onder de bondigheid.

## 16. Cross-sectie consistentie

Elke pragmatische aanbeveling moet stand houden tegen de beperkingen die elders op de pagina staan. Check bij elke sectie: *"weerleg ik hier iets wat ik eerder heb beweerd?"*

- ✗ Sectie A: *"context rot zorgt dat nauwkeurigheid instort bij 32K tokens"*. Sectie B: *"voor 200K-tokens kennisbanken: stop het gewoon in de prompt"*.
- ✓ Sectie A onveranderd. Sectie B: *"voor kleine kennisbanken met simpele vragen: stop in prompt. Voor vragen waarbij het model moet redeneren: loopt alsnog tegen context rot aan (zie sectie hierboven)"*.

Een pagina mag spanning tonen tussen ideeën — maar moet de spanning dan expliciet benoemen.

## 17. Structuur per BB-pagina

Verplichte volgorde die we met BB_03 hebben vastgesteld:

1. **Frontmatter** — `code`, `name`, `tagline`, `icon`, `order`, `quote` + `quoteAuthor`, `checklist` (8–10 items), `quickStart` (3 items), `auditExample`, `evidence` (3–5 items)
2. **`## Wat is {BB}?`** — 2–3 alinea's kern-definitie + relatie tot nabijgelegen BB (bij BB_03: relatie tot Prompt Design)
3. **6–7 `<BBDisclosure>` secties** — uitklapbaar, elk een volledige deelverhaalstructuur:
   - De evolutie / waarom dit nu belangrijk is
   - Het mechanisme / de empirische basis
   - De toolbox / hoe je het aanpakt
   - Een stille faalmodus / tegenkracht
   - Cross-bouwsteen of cross-guardrail-integratie
   - "In de praktijk" — pragmatische principes + koppelingen
4. **Interne links** door de tekst heen naar andere `/framework/{slug}` pagina's (BB's). GR's nog niet als URL (geen `/guardrails/[slug]` route); gebruik `**Name** (GR_0X: kernzin)` in-line.

## 18. Frontmatter-discipline

- `checklist` — vraagvorm, concreet, meetbaar ("Zijn chunks contextueel verrijkt vóór indexering?")
- `quickStart` — **drie stappen op drie niveaus**: strategisch (bedrijfs-/directie-beslissing), tactisch (eigenaarschap, beleid, organisatie), operationeel (concrete technische handeling). Elke stap beschrijft de eerste logische stap op dát niveau, zodat iedere rol — directie, domain-owner, developer — direct iets heeft om mee te starten. Elke stap begint met een werkwoord en eindigt met een concrete actie.
- `evidence` — wat lever je op als bewijs dat de BB goed draait
- `auditExample` — authentiek eigen voorbeeld (AI-Readiness Audit of vergelijkbaar), niet een generiek scenario

**Voorbeeld** (uit BB_03 Dynamic Context):

1. **Strategisch**: *"Bepaal welke kennisbronnen überhaupt in de context-laag mogen. Beslis per bron of hij erin hoort, hoe vaak hij actueel moet zijn, en welk privacy-regime geldt..."*
2. **Tactisch**: *"Wijs per bron een inhoudelijke eigenaar en een houdbaarheidsgrens aan..."*
3. **Operationeel**: *"Begin bij chunking en contextuele annotatie, niet bij model-keuze..."*

De drie niveaus dekken samen de rol-laag waar de BB organisatorisch impact heeft. Geen van de drie mag ontbreken; als je er maar één of twee kunt formuleren, begrijp je zelf de BB nog niet volledig. De niveaus-labels (`Strategisch:`, `Tactisch:`, `Operationeel:`) horen in de tekst van de Quick Start zelf, niet alleen impliciet.

---

## Review-checklist vóór publicatie

Voor elke nieuwe BB- of GR-pagina, doorloop deze vragen:

- [ ] Elke vakterm bij eerste gebruik uitgelegd (tabel §4 gebruikt waar mogelijk)?
- [ ] **Geen vertaalde termen die zelf uitleg vergen** (kennisgraaf, nabij-getraind, etc.) → parafrase (§1)
- [ ] Business-termen NL (Verkoop/Productmanagement/Klantenservice, niet Sales/Product/Customer Success)?
- [ ] Alle voorbeelden herkenbaar voor niet-techneut?
- [ ] Elk getal voorzien van menselijke eenheid?
- [ ] Metaforen eerst uitgelegd, dan bondig?
- [ ] Benchmarks van jaartal voorzien en met richting-claim?
- [ ] Gevolg-zinnen passief (niet anthropomorfisch)?
- [ ] **Na vetgedrukt kopje `:`, geen `—`** (§8) — grootste foutpatroon, veroorzaakte 76 correcties in BB_03
- [ ] **`;` boven `—` als zin-koppel** (§8)
- [ ] Em-dashes terughoudend; komma's voor bijzin?
- [ ] Opsommingen met uitleg per bullet, niet alleen labels?
- [ ] **Geen tabellen met meer dan 8-10 woorden per cel → bullets** (§13)
- [ ] **Koppen in gewone-woorden-toets** — vermijd `-architectuur`, `-engine`, `-pijplijn` in kop (§14)
- [ ] **Inline-parenthese weggelaten als glossary-link tooltip al de uitleg biedt** (§15)
- [ ] **Cross-sectie consistentie** — elk advies houdt stand tegen eerder genoemde beperkingen (§16)
- [ ] Cross-refs: naam + code + kernzin bij eerste vermelding?
- [ ] Slotzin van elke disclosure toegevoegde waarde?
- [ ] Consistente terminologie (context window niet model window)?
- [ ] **Quick Start beschrijft eerste logische stap op drie niveaus** — strategisch (directie/product-lead), tactisch (domain-owner/ops), operationeel (developer). Labels expliciet in de tekst (§18).
- [ ] Frontmatter-bewoording lijnt met body?
- [ ] `astro check` → 0 errors?
- [ ] Dev-server render gecheckt op: alle disclosures openen, alle tools-cards zichtbaar, alle links werken, **hover-tooltips tonen definities op glossary-links**?

---

## Log: welke pagina's zijn hiermee geschreven/herschreven

| Datum | Pagina | Status |
|-------|--------|--------|
| 2026-04-21 | BB_03 Dynamic Context | Volledig — baseline voor deze gids (322 regels, 7 disclosures, alle secties nu volgens gids §1-14) |
| 2026-04-22 | BB_01 Knowledge | Volledig — 391 regels, 7 disclosures, checklist + frontmatter + 12 KnowledgeItems + 5 tools |
| 2026-04-22 | BB_03 her-pass | Lees-review door Robin: 76× `**x** —` → `:`, 10+ em-dash → `;`, 12 jargon-termen uitgelegd of geparafraseerd, tabel → bullets (§13), koppen in gewone-woorden-toets (§14), hover-tooltip-redundantie opgeruimd (§15), 200k-cachen-claim cross-sectie gealigneerd (§16). Gids §1, §4, §8 aangescherpt; §13-§16 nieuw toegevoegd. |
| 2026-04-22 | BB_03 her-pass 2 | Enkele em-dash-regel verscherpt (§8: alleen dubbel rond tussenzin), anglicisme-regel toegevoegd (§1), Privacy-sectie top-down gerestructureerd (strategisch/tactisch/operationeel), pseudonimiseren-vs-anonimiseren nuance toegevoegd (AVG overweging 26), Quick Start omgebouwd naar drie-niveau-stap (§18 aangescherpt). |
| 2026-04-26 | BB_02 Client Blueprint | Volledig — 409 regels, 7 BBDisclosures + slot-disclosure, value-stream-georiënteerde structuur (Obeidat 7-stappen, unFIX value streams van Appelo, FDE Pragmatic Engineer + SVPG-tegen, prototype-tools NxCode/Lenny, EU AI Act + HLEG/ALTAI + DPIA + OWASP, NL AIC + PACE + AI BOM). Convergence-pass tegen Gemini Deep Research uitgevoerd; drie clippings gearchiveerd als bron-131/132/133. Eerste 14 em-dashes-fouten in eerste concept handmatig gerepareerd; aanleiding tot bouw van /bb-write skill als forcing function (zie `~/ODIN/projecten/BeeHaive/.claude/skills/bb-write/SKILL.md`) en CLAUDE.md-aanvulling met top-3 hard rules. |

Na elke afgeronde BB/GR: entry toevoegen + zo nodig gids bijwerken met nieuwe patronen die we ontdekten.

---

## Tot-slot

**Wanneer een skill maken?** Wanneer deze gids 6-7 BB's en 6-7 GR's ondersteund heeft en we op patronen uitkomen die automatiseerbaar zijn (lint-achtige checks, glossarium-enforcement, stijl-validatie per diff). Tot dan: dit document is de werkwijze.
