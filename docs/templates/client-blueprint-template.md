# Client Blueprint — Template en Voorbeeld

**Gebaseerd op:** BeeHaive BB_02 Client Blueprint (`frontend/src/content/building-blocks/client-blueprint.mdx`)
**Onderbouwing:** `docs/research/client-blueprint-2026/final.md` en vier deel-research-bestanden
**Versie:** 1.0 — 2026-04-28
**Status:** Template + uitgewerkt voorbeeld voor de fictieve klant *Hexant Consulting*

---

## Leeswijzer

Dit document is twee dingen tegelijk:

1. **Een ingevuld voorbeeld** dat aan een klant laat zien hoe een Client Blueprint eruitziet als hij is opgeleverd. Het voorbeeld gebruikt overal de fictieve klant *Hexant Consulting* (een Nederlands consultancy-bureau dat AI-Readiness Audits levert), zodat de klant kan zien hoe de structuur op een concreet geval landt.
2. **Een herbruikbare template** waarin elk hoofdstuk een placeholder-blok bevat (gemarkeerd met `> [INVULLEN: ...]`) dat per nieuwe opdracht wordt overschreven met klant-specifieke inhoud.

Per hoofdstuk wordt eerst kort uitgelegd *waarom* dat hoofdstuk in de blueprint hoort (de "wat staat hier en waarom"), gevolgd door een quote die de noodzaak onderschrijft, vervolgens het uitgewerkte voorbeeld voor Hexant, daarna het invul-blok, een checklist, en de relevante literatuur.

Drie leesregels:

- **Lineair lezen voor een eerste indruk; selectief lezen na overdracht.** Hoofdstuk 0 (klant- en projectkaart) en Bijlage A (eindchecklist) volstaan voor een snelle review; de tussenliggende hoofdstukken zijn de onderbouwing.
- **De blueprint is een levend document.** Elk hoofdstuk bevat een `Status / laatste herziening`-veld zodat zichtbaar blijft welke onderdelen sinds de bouw zijn bijgewerkt.
- **Bij twijfel: het gesprek is belangrijker dan het document.** De blueprint dwingt het juiste gesprek af; hij vervangt dat gesprek niet.

---

## Bronnen-conventie

- Verwijzingen tussen blokhaken `[NN]` corresponderen met de literatuurlijst in Bijlage B.
- Citaten staan in *cursief* met bronvermelding direct erachter.
- Verwijzingen naar de zes andere BeeHaive-bouwstenen (BB_01, BB_03 t/m BB_07) verwijzen naar `frontend/src/content/building-blocks/*.mdx`.

---

## Inhoudsopgave

| Hoofdstuk | Titel | Hoort bij BB-sectie |
|-----------|-------|---------------------|
| 0 | Klant- en projectkaart | (alle) |
| 1 | Strategische verankering en waarde-stroom | "Toegevoegde waarde voor de klant is hét uitgangspunt" |
| 2 | Use-case-discovery in zeven stappen | "De zeven stappen van use-case-discovery" |
| 3 | Architectuur en technische ontwerpkeuzes | "Architectuur: wanneer kies je een workflow, wanneer een agent?" |
| 4 | Risico, compliance en ethiek | "Risico's als ontwerp-input, niet achteraf bepaald" |
| 5 | Prototype als gespreksanker | "Het prototype als basis voor klantreview" |
| 6 | Iteratieve werkwijze en FDE-principes | "Iteratief bouwen: FDE-principes en hun grenzen" |
| 7 | Governance, goedkeuring en Nederlandse context | "Governance, goedkeuring en de Nederlandse context" |
| 8 | Cross-bouwsteen-overzicht | "In de praktijk" (cross-cutting) |
| A | Eindchecklist (goedkeuringspoort) | (samenvatting) |
| B | Literatuur en bronvermeldingen | (samenvatting) |

---

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

# Hoofdstuk 1 — Strategische verankering en waarde-stroom

## 1.1 Waarom dit hoofdstuk

De grootste fout bij het bouwen van AI-oplossingen is starten met de techniek. Een Client Blueprint die meteen begint met "we kiezen Claude Sonnet 4.6 met een vector-database" zonder dat de bovenliggende vraag (welke beslissing of werkstap willen we beter maken, in welke waarde-stroom?) is beantwoord, levert vrijwel zeker een van de patronen op die het MIT NANDA-rapport (augustus 2025) signaleert: een pilot die technisch werkt maar zakelijk geen meetbare verbetering oplevert [5]. Dit hoofdstuk verankert de blueprint in de waarde-stroom van de klant en in de bewuste keuze welke ambitie de klant heeft.

Dit hoofdstuk beantwoordt drie vragen, in deze volgorde:

1. Welke AI-ambitie heeft de klant? (Gartner Opportunity Radar)
2. Welke waarde-stroom wordt geraakt, en wat is haar trigger, faseringen en uitkomst?
3. Wie is de eigenaar van die waarde-stroom, en welke knelpunten zijn meetbaar?

> *"AI is not the starting point. The business is."*
> — Sam Obeidat, CAIO Newsletter, 2025 [1]

> *"The purpose is important, and the purpose comes from people."*
> — Cassie Kozyrkov (Acceldata-interview, 2025) [2]

## 1.2 De AI-ambitie van de klant

### Wat hoort hier

Voordat de eerste use case in detail wordt uitgewerkt, wordt de overkoepelende AI-ambitie expliciet gemaakt. Dit gebeurt langs twee Gartner-assen [25]: van *intern-gericht* (productiviteit en operationele efficiëntie binnen de eigen organisatie) naar *extern-gericht* (klant- of marktimpact), en van *alledaags* (Everyday AI: bestaande processen versnellen) naar *baanbrekend* (Game-Changing AI: processen herdenken). De positie op deze radar dicteert direct welke risicokaders worden geactiveerd: een outward-facing, game-changing toepassing introduceert exponentieel meer ethische, juridische en reputatie-risico's dan een inward-facing tool die interne documenten doorzoekbaar maakt.

### Voorbeeld — Hexant

Hexant positioneert het Audit Scoring Copilot-initiatief expliciet als **inward-facing × Everyday AI**. Reden: het initiatief versnelt een bestaand auditproces zonder dat het de aard van de dienst verandert; de eindrapportage en de relatie met de auditklant blijven inhoudelijk hetzelfde. Hexant kiest bewust *niet* voor een game-changing positionering ("AI-driven Audits as a Service") in deze fase, omdat zij eerst intern willen valideren dat de scoring-kwaliteit gehandhaafd blijft voordat zij de propositie naar buiten herzien.

Consequenties van deze keuze:

- **Risico-bereidheid**: laag. Een fout in de copilot mag de auditkwaliteit niet verlagen; de senior auditor blijft eindverantwoordelijk en reviewt elk scoring-voorstel.
- **EU AI Act-tier (voorlopig)**: Tier 4 (minimaal risico), want geen beslissing-impact op derden, geen automatisch effect op de auditklant.
- **Tijdslijn**: zes maanden tot productie-klaar, in plaats van twee jaar.

### Template — invulblok

> [INVULLEN]
>
> **AI-ambitie (Gartner Opportunity Radar)**:
> - Inward-facing of outward-facing? Argumentatie: ...
> - Everyday AI of Game-Changing AI? Argumentatie: ...
>
> **Drie consequenties van deze positionering**:
> 1. Risico-bereidheid: ...
> 2. EU AI Act-tier (voorlopig): ...
> 3. Tijdslijn tot productie-klaar: ...

## 1.3 De waarde-stroom in detail

### Wat hoort hier

Een **waarde-stroom** (*value stream*) is de end-to-end-journey die een trigger transformeert in een uitkomst voor een stakeholder; niet een afdeling, niet een tool, maar een volledige flow van waarde [1]. In dit hoofdstuk wordt de waarde-stroom in scope expliciet beschreven: trigger, fasen, uitkomst, betrokken afdelingen, één-noord-ster-KPI. Dit is de input voor alle volgende hoofdstukken.

Twee gangbare definities zijn beide bruikbaar; de blueprint maakt expliciet welke wordt gehanteerd:

- **Sam Obeidat (breed)**: trigger naar uitkomst voor een stakeholder; geschikt voor operationele en governance-stromen [1].
- **Jurgen Appelo, unFIX (nauwer)**: *"the set of actions needed to discover or deliver on a job-to-be-done / value proposition from a signal to an experience"* [verwijzing in BB-pagina]. Geschikt als de stroom expliciet een job-to-be-done en een gebruiker-ervaring heeft.

unFIX onderscheidt vier waarde-stroom-typen: Product, Service, Event en Project Value Stream. Voor de meeste consultancy- en interne-procesblueprints is een Service Value Stream de juiste classificatie.

### Voorbeeld — Hexant: de AI-Readiness Audit

**Definitie gehanteerd**: Obeidat's brede framing (de auditklant ontvangt het eindrapport, maar de stroom is operationeel-procesmatig en niet productgedreven).

**Type (unFIX)**: Service Value Stream, intern georganiseerd, extern gericht.

**Trigger**: getekend opdrachtformulier "AI-Readiness Audit" door auditklant.

**Uitkomst**: getekend eindrapport met scoring op zeven HLEG-dimensies, vrijgegeven aan auditklant en hun directie.

**Faseringen (één-regel-map)**:

```
Trigger: opdracht getekend
   → Fase 1: kick-off en stakeholder-mapping (1 week)
   → Fase 2: documentatie-review (1 week)
   → Fase 3: interviews afnemen (2 weken, 60 interviews)
   → Fase 4: scoring en triangulatie (1 week)
   → Fase 5: rapportage en review (1 week)
   → Fase 6: presentatie aan klant-directie (0,5 week)
Uitkomst: getekend eindrapport
```

**Eén-noord-ster-KPI**: doorlooptijd opdracht-getekend tot eindrapport-vrijgegeven. Huidig: gemiddeld 7,2 weken. Doel: 5,0 weken.

**Betrokken afdelingen**: Audit Practice (eigenaar), Knowledge Management (templates en bibliotheek), Quality Assurance (peer review), Sales (klantintake), IT (data-infrastructuur).

**De vraag op waarde-stroom-niveau**: in welke fase verliest de stroom de meeste tijd, en is dat waar AI-interventie hoort?

Antwoord uit de meting (eerste twee weken van de blueprint-fase): fase 4 (scoring en triangulatie) is de grootste consumeerder van senior-auditor-tijd, met de hoogste inter-auditor-variatie. Fasen 1, 5 en 6 zijn relatie- en oordeel-werk waar AI-interventie waarschijnlijk meer schaadt dan helpt; fase 3 (interviews) is mens-werk waar AI hoogstens kan ondersteunen bij voorbereiding (samenvatting van eerdere documentatie). De AI-interventie hoort in fase 4.

### Template — invulblok

> [INVULLEN]
>
> **Definitie gehanteerd**: Obeidat (breed) of Appelo/unFIX (gebruiker-gecentreerd). Argumentatie: ...
>
> **Type (unFIX)**: Product / Service / Event / Project Value Stream
>
> **Trigger**: ...
>
> **Uitkomst**: ...
>
> **Faseringen (één-regel-map)**:
> ```
> Trigger: ...
>    → Fase 1: ... (... weken)
>    → Fase 2: ... (... weken)
>    → ...
> Uitkomst: ...
> ```
>
> **Eén-noord-ster-KPI**: ... (huidig: ...; doel: ...)
>
> **Betrokken afdelingen**: ...
>
> **In welke fase verliest de stroom de meeste tijd of kwaliteit, en hoort daar de AI-interventie?**
> Antwoord met onderbouwing uit meting (geen aanname): ...

## 1.4 Wanneer is een waarde-stroom *niet* de juiste lens?

Niet elke AI-toepassing past in één waarde-stroom. Een bedrijfsbrede zoek-assistent over alle interne kennis is *horizontaal* en raakt meerdere waarde-stromen tegelijk; een blueprint die zo'n toepassing in één waarde-stroom wil persen voelt geforceerd. Voor horizontale toepassingen werkt de waarde-stroom-lens als *secundair* kader: welke waarde-stromen gaan deze assistent het zwaarst gebruiken, en welke kwaliteitseisen volgen daaruit?

**Toets voor Hexant**: het Audit Scoring Copilot-initiatief is geen horizontale toepassing; de waarde-stroom-lens is hier primair en passend.

**Template — invulvraag**: is dit een waarde-stroom-toepassing (lens primair) of een horizontale toepassing (lens secundair)? Argumentatie: ...

## 1.5 Cross-cutting check: silo's

Een knelpunt in de waarde-stroom zit zelden netjes binnen één afdeling. AI ontworpen *voor één afdeling* automatiseert silo-werk; AI ontworpen *voor een waarde-stroom* pakt de overdrachten en wachttijden tussen afdelingen aan, waar de meeste doorlooptijd verloren gaat.

**Voorbeeld — Hexant**: scoring (fase 4) raakt formeel alleen de Audit Practice. Maar de inputs ervoor komen uit fase 2 (Knowledge Management levert de auditstandaard) en fase 3 (interviewers zijn vaak junior auditors uit een andere sub-practice). De copilot moet dus toegang hebben tot zowel de auditstandaard-bibliotheek (KM) als de transcript-archief (Audit Practice). Eigenaarschap van de copilot ligt bij de Audit Practice, maar de QA-afdeling tekent mee op de scoring-validatie-procedure.

## 1.6 Checklist hoofdstuk 1

- [ ] AI-ambitie expliciet gepositioneerd op de Gartner Opportunity Radar (twee assen, met argumentatie).
- [ ] Drie consequenties van die positionering benoemd (risico-bereidheid, EU AI Act-tier, tijdslijn).
- [ ] Waarde-stroom-definitie gekozen (Obeidat of Appelo/unFIX) met argumentatie.
- [ ] Waarde-stroom als één-regel-map vastgelegd (trigger → fasen → uitkomst).
- [ ] Eén-noord-ster-KPI benoemd, kwantificeerbaar en gekoppeld aan bestaande meting.
- [ ] Alle betrokken afdelingen genoemd, ook degene die alleen indirect raken.
- [ ] Vastgesteld in welke fase de AI-interventie hoort, op basis van meting (geen aanname).
- [ ] Toets uitgevoerd of de waarde-stroom-lens primair of secundair is.

## 1.7 Literatuur (kerncitaten dit hoofdstuk)

- Sam Obeidat, *AI is not the starting point*, CAIO Newsletter, 2025 [1].
- Cassie Kozyrkov (Acceldata-interview), *Decision-first leadership* [2].
- Jurgen Appelo, *unFIX value stream definition* [verwijzing in BB-pagina].
- Gartner, *AI Opportunity Radar* [25].
- MIT NANDA, *The GenAI Divide: State of AI in Business 2025* [5], met methodologische kanttekeningen van het Marketing AI Institute [6].

## 1.8 Status / laatste herziening

- Versie: 1.0
- Laatst bijgewerkt: 2026-04-28
- Wijzigingen sinds vorige versie: eerste vastlegging.

<!-- HIER_VERDER -->
