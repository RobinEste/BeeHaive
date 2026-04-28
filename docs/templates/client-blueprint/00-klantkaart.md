# Hoofdstuk 0 — Klant- en projectkaart

## 0.1 Waarom dit hoofdstuk

De klant- en projectkaart is de samenvatting op één pagina van wie de klant is, welke waarde-stroom binnen scope ligt, wie de waarde-stroom-eigenaar is, en wat de eerste use case is die binnen die waarde-stroom wordt aangepakt. Dit hoofdstuk is bedoeld om aan iedereen die de blueprint voor het eerst leest binnen vijf minuten een werkbaar beeld te geven van *wat* er gebouwd gaat worden, *voor wie*, en *wat het succescriterium* is. De rest van de blueprint is onderbouwing van wat hier in samengevatte vorm staat.

> *"AI is not the starting point. The business is."*
> — Sam Obeidat, CAIO Newsletter, 2025 [1]

## 0.2 Voorbeeld — Hexant Consulting

| Veld | Waarde |
|------|--------|
| Klant | Hexant Consulting (Nederlands consultancy-bureau, ~120 fte) |
| Sector | Zakelijke dienstverlening (advies en audit) |
| Contractmodel | Outcome-based, vaste prijs per audit + nazorg |
| Waarde-stroom in scope | AI-Readiness Audit, van klant-intake tot eindrapport |
| Type waarde-stroom (unFIX) | Service Value Stream (intern georganiseerd, extern gericht) |
| Waarde-stroom-eigenaar | Hoofd Audit Practice (Hexant) |
| Eindgebruiker van de AI | Senior Auditor (intern) |
| Stakeholder van de uitkomst | CIO van de auditklant (extern) |
| Initiele use case | Audit Scoring Copilot (transcript naar herhaalbare scoring op zeven HLEG-dimensies) |
| AI-ambitie (Gartner-radar) | Inward-facing, Everyday AI (operationele efficiëntie binnen bestaande dienst) |
| EU AI Act-tier (voorlopig) | Tier 4, minimaal risico (interne tooling zonder beslissing-impact op derden) |
| DPIA-status | Voorlopig "niet vereist", herbeoordelen na data-keuze (zie hoofdstuk 4) |
| Doorlooptijd blueprint-fase | 6 weken (intake, mapping, prototype, review, sign-off) |
| Goedkeuringspoort | AI-Comité Hexant + waarde-stroom-eigenaar tekenen samen |

## 0.3 Eén-regel-samenvatting van de oplossing

> Een AI-copilot die ruwe interview-transcripten van een AI-Readiness Audit omzet naar een initiele scoring op de zeven HLEG-dimensies, met inline citatie naar het transcript-fragment, voor menselijke review en bijstelling door de senior auditor; doel is verkorting van de scoring-fase van vier dagen naar één halve dag per audit, bij gelijkblijvende of betere consistentie tussen auditors.

## 0.4 Drie kerncijfers

| Maatstaf | Huidige toestand | Doel binnen één jaar |
|---------|-----------------|---------------------|
| Tijd per audit, scoring-fase | 28-32 uur (vier werkdagen, één auditor) | 4-6 uur (halve werkdag, één auditor) |
| Inter-auditor variatie op identiek transcript | ±2,1 punten op 10-puntsschaal | ≤ ±0,8 punten |
| Aantal audits per jaar bij huidig team | 18 | 30 (66% capaciteits-uitbreiding zonder extra fte's) |

Deze cijfers fungeren als de "noord-ster" voor alle ontwerpkeuzes. Een keuze die deze drie cijfers niet vooruithelpt of zelfs verslechtert komt niet in het ontwerp.

## 0.5 Template — invulblok

> [INVULLEN per nieuwe opdracht]
>
> | Veld | Waarde |
> |------|--------|
> | Klant | ... |
> | Sector | ... |
> | Contractmodel | ... |
> | Waarde-stroom in scope | ... |
> | Type waarde-stroom (unFIX) | Product / Service / Event / Project Value Stream |
> | Waarde-stroom-eigenaar | ... (rol + naam) |
> | Eindgebruiker van de AI | ... |
> | Stakeholder van de uitkomst | ... |
> | Initiele use case | ... (één naam, leesbaar voor niet-technici) |
> | AI-ambitie (Gartner-radar) | inward-facing of outward-facing × Everyday AI of Game-Changing AI |
> | EU AI Act-tier (voorlopig) | Tier 1 / 2 / 3 / 4 |
> | DPIA-status | Niet vereist / Vereist / Herbeoordelen |
> | Doorlooptijd blueprint-fase | ... weken |
> | Goedkeuringspoort | ... (welk gremium tekent) |
>
> **Eén-regel-samenvatting van de oplossing**: ...
>
> **Drie kerncijfers**:
>
> | Maatstaf | Huidige toestand | Doel binnen één jaar |
> |---------|-----------------|---------------------|
> | ... | ... | ... |
> | ... | ... | ... |
> | ... | ... | ... |

## 0.6 Checklist hoofdstuk 0

- [ ] De waarde-stroom in scope is een end-to-end-stroom (trigger naar uitkomst), niet een afdeling of een tool.
- [ ] De waarde-stroom-eigenaar is benoemd en heeft mandaat over de afdelingsgrenzen heen.
- [ ] Eindgebruiker en stakeholder van de uitkomst zijn beide expliciet genoemd, ook als zij niet dezelfde persoon zijn.
- [ ] De drie kerncijfers zijn kwantificeerbaar en gekoppeld aan een bestaand prestatie-meetinstrument.
- [ ] De voorlopige EU AI Act-tier en DPIA-status zijn aangegeven, met de noot dat herbeoordeling in hoofdstuk 4 plaatsvindt.

## 0.7 Status / laatste herziening

- Versie: 1.0
- Laatst bijgewerkt: 2026-04-28
- Wijzigingen sinds vorige versie: eerste vastlegging.

