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

Afkortingen worden pas gebruikt nadat ze zijn uitgeschreven:
- ✓ `Model Context Protocol (MCP — een opkomende standaard om...)` → daarna vrij `MCP`
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
| chunks | stukjes waarin een document wordt opgeknipt voor retrieval |
| embedding | wiskundige representatie van tekst die semantische gelijkenis meetbaar maakt |
| reranker | tweede-pass-model dat opgehaalde documenten herordent op relevantie |
| prompt | de instructie die je aan een AI-model geeft |
| hallucinatie | het verzinnen van feiten door een model die plausibel klinken maar niet kloppen |

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

- **Em-dashes spaarzaam** — gebruik in NL komma's voor bijzin, em-dash alleen voor zijsprong/nadruk
- ✗ *"definitie — en zonder die definitie..."*
- ✓ *"definitie en wanneer er geen definitie bekend is..."*
- ✗ *"ontwerpdisciplines — ongeacht hoe groot..."*
- ✓ *"ontwerpdisciplines, ongeacht hoe groot..."*
- Aanhalingstekens liggend NL-stijl ("zo") of typografisch ("zó") — niet rechtop ("zo") in body-tekst

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

## 13. Structuur per BB-pagina

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

## 14. Frontmatter-discipline

- `checklist` — vraagvorm, concreet, meetbaar ("Zijn chunks contextueel verrijkt vóór indexering?")
- `quickStart` — 3 stappen, elk begint met een werkwoord, eindigt met een concrete actie
- `evidence` — wat lever je op als bewijs dat de BB goed draait
- `auditExample` — authentiek eigen voorbeeld (AI-Readiness Audit of vergelijkbaar), niet een generiek scenario

---

## Review-checklist vóór publicatie

Voor elke nieuwe BB- of GR-pagina, doorloop deze vragen:

- [ ] Elke vakterm bij eerste gebruik uitgelegd (tabel §4 gebruikt waar mogelijk)?
- [ ] Business-termen NL (Verkoop/Productmanagement/Klantenservice, niet Sales/Product/Customer Success)?
- [ ] Alle voorbeelden herkenbaar voor niet-techneut?
- [ ] Elk getal voorzien van menselijke eenheid?
- [ ] Metaforen eerst uitgelegd, dan bondig?
- [ ] Benchmarks van jaartal voorzien en met richting-claim?
- [ ] Gevolg-zinnen passief (niet anthropomorfisch)?
- [ ] Em-dashes terughoudend; komma's voor bijzin?
- [ ] Opsommingen met uitleg per bullet, niet alleen labels?
- [ ] Cross-refs: naam + code + kernzin bij eerste vermelding?
- [ ] Slotzin van elke disclosure toegevoegde waarde?
- [ ] Consistente terminologie (context window niet model window)?
- [ ] Frontmatter-bewoording lijnt met body?
- [ ] `astro check` → 0 errors?
- [ ] Dev-server render gecheckt op: alle disclosures openen, alle tools-cards zichtbaar, alle links werken?

---

## Log: welke pagina's zijn hiermee geschreven/herschreven

| Datum | Pagina | Status |
|-------|--------|--------|
| 2026-04-21 | BB_03 Dynamic Context | Volledig — baseline voor deze gids (322 regels, 7 disclosures, alle secties nu volgens gids §1-14) |

Na elke afgeronde BB/GR: entry toevoegen + zo nodig gids bijwerken met nieuwe patronen die we ontdekten.

---

## Tot-slot

**Wanneer een skill maken?** Wanneer deze gids 6-7 BB's en 6-7 GR's ondersteund heeft en we op patronen uitkomen die automatiseerbaar zijn (lint-achtige checks, glossarium-enforcement, stijl-validatie per diff). Tot dan: dit document is de werkwijze.
