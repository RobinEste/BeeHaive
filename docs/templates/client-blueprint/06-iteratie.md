# Hoofdstuk 6 — Iteratieve werkwijze en FDE-principes

## 6.1 Waarom dit hoofdstuk

Het MIT NANDA-rapport en onafhankelijke analyses [5, 6] wijzen consistent op één faalmodus: pilots die technisch werken maar zakelijk geen meetbare verbetering opleveren — vaak omdat de iteratie-cyclus ontbreekt. Een blueprint zonder iteratieplan is een belofte zonder validatieweg. Dit hoofdstuk legt vast hoe het systeem stapsgewijs naar productie wordt gebracht: welke iteraties, met welke succescriteria, met welke evaluatie-set, en welke werkwijze (Forward Deployed Engineering-principes versus klassieke discovery) bij deze opdracht past.

> *"FDEs work with enormous uncertainty, and often what clients describe doesn't match the reality of their data."*
> — Pragmatic Engineer, *What are Forward Deployed Engineers?* [21]

> *"73% van succesvolle implementaties startte bewust klein; 63% fraamde de pilot expliciet als experiment."*
> — Stanford Digital Economy Lab, *Enterprise AI Playbook* (51 cases) [aanvullend]

## 6.2 FDE-principes: wanneer wel, wanneer niet

### Wat hoort hier

Forward Deployed Engineering (Palantir, intern "Delta") is een werkmodel waarin een engineer embedded werkt bij de klant, in plaats van vanaf afstand adviseert. Drie fasen: scoping → validatie → implementatie [21]. Marktbevestiging: FDE-vacatures stegen >800% in 2025 [22]. Tegelijk waarschuwt SVPG (Cagan): klant-specifieke customisaties kunnen de productstrategie ondermijnen [21].

**FDE-principes als werkwijze** (los van het volledige rolmodel):

- *Embedded* — bouwer zit fysiek of doorlopend bij het klantteam, niet in een separate sprint-omgeving.
- *Bouw, geen advies* — opleveringen zijn werkende code, geen rapporten.
- *Snelle, korte iteraties* — dagen tot weken, niet maanden.
- *Onzekerheid als startpunt* — wat klanten beschrijven matcht zelden de werkelijkheid van hun data.

**FDE-principes zijn nuttig wanneer**: klantcontext cruciaal is voor de oplossing, data-realiteit waarschijnlijk afwijkt van wat het projectplan beschrijft, korte feedback-cycli essentieel zijn voor adoptie.

**Klassieke discovery-fase volstaat wanneer**: probleem en data goed afgekaderd zijn, klant beschikt over eigen tech-team, en de oplossing past binnen een bekend referentie-patroon.

**Beperkingen**: FDE-werk is niet schaalbaar als product-capability; rolvervaging tussen FDE, Solutions Architect, Sales Engineer; risico op product-strategie-erosie [21, 22]. Voor de blueprint-fase: FDE als *werkwijze* adopteren, niet automatisch als *rolmodel* invoeren.

### Voorbeeld — Hexant

**Werkwijze**: FDE-principes geadopteerd, klassieke FDE-rol *niet*. Concretisering:

- *Embedded*: BeeHaive-bouwer werkt twee dagen per week op het Hexant-kantoor in iteratie I0-I2; daarna remote met wekelijkse aanwezigheid.
- *Bouw, geen advies*: elke iteratie eindigt met werkende functionaliteit die senior auditors kunnen gebruiken op een klein subset.
- *Korte cycli*: iteraties van twee weken (I0 t/m I3), drie weken voor I4 (productie-rollout).
- *Onzekerheid als startpunt*: aanname dat HLEG-rubric machine-leesbaar is, transcripten geen PII bevatten, en inter-auditor-variatie een single-cause heeft — alle drie expliciet als hypothese, niet als feit.

Klassieke FDE-rol *niet*: er komt geen permanente FDE in dienst van Hexant; het AI-Comité Hexant blijft eindverantwoordelijk en BeeHaive-bouwer fungeert als externe specialist binnen de iteraties.

### Template — invulblok

> [INVULLEN]
>
> **Werkwijze**: FDE-principes geadopteerd / klassieke discovery-fase / hybride — argumentatie:
> ...
>
> **Welke FDE-principes wel** (per principe een korte concretisering):
> - Embedded: ...
> - Bouw, geen advies: ...
> - Korte cycli: ...
> - Onzekerheid als startpunt — drie hypotheses die expliciet open staan:
>   1. ...
>   2. ...
>   3. ...
>
> **Welke FDE-elementen niet** en waarom:
> ...

## 6.3 Iteratieplan: I0 tot productie

### Wat hoort hier

Een iteratieplan met genummerde iteraties (I0, I1, I2, ...) waar elke iteratie heeft: doelstelling, scope, succescriteria, evaluatie-aanpak, beslisparagraaf (doorgaan / aanpassen / stoppen). Twee disciplines die hier zichtbaar blijven:

- **Pilot-als-experiment frame'n** — Stanford [aanvullend]: 63% van succesvolle implementaties fraamt expliciet als experiment, niet als product. Dit beschermt tegen scope lock-in en sunk-cost-fallacy.
- **Eval-set centraal** — succescriteria zijn meetbaar tegen een eval-set die vóór de bouw is samengesteld, niet ad hoc tijdens de demo.

### Voorbeeld — Hexant: vijf iteraties

| Iteratie | Doel | Scope | Succescriterium | Beslismoment |
|---------|------|-------|-----------------|--------------|
| **I0** (2 weken) | Eval-set + intake | 12 historische audits gedigitaliseerd; HLEG-rubric in JSON; 50 inter-auditor scoring-cases als evaluatie-set | Eval-set bestaat; baseline-meting van inter-auditor-variatie ±2,1 bevestigd | Doorgaan zodra eval-set 50+ cases bevat |
| **I1** (2 weken) | Extractie-werkstroom | LLM-call die uitspraken classificeert naar HLEG-dimensie + sterkte (sterk-bewijs/zwak-bewijs/signaal); inline citatie | Op eval-set: precisie classificatie ≥ 0,80, recall ≥ 0,75 | Bij ≥0,75: door naar I2; <0,75: rubric-uniformeren / extractie-prompt herzien |
| **I2** (2 weken) | Scoring-werkstroom | Per-dimensie aggregatie + score-voorstel met top-3 evidence-fragmenten | Inter-AI-auditor variatie op eval-set ≤ ±1,0; senior auditors accepteren ≥ 60% scoring-voorstellen ongewijzigd | Bij ≥60% en ≤±1,0: door naar I3 |
| **I3** (2 weken) | Validatie-laag + UI | Deterministische post-checks (rubric-conformiteit, evidence-aantallen); auditor-UI | Op één live audit: senior-auditor-tijd in scoring-fase ≤ 12u (tussen baseline 28u en doel 4-6u) | Doorgaan naar I4 zodra senior auditor de werkwijze accepteert |
| **I4** (3 weken) | Rollout op 3 audits | Drie parallelle audits met verschillende auditors; meting tegen eval-set; feedback-cyclus | Inter-auditor-variatie ≤ ±0,8 (doel hoofdstuk 0); scoring-tijd 4-6u/audit; geen kritieke incidenten | Goedkeuringspoort: AI-Comité + waarde-stroom-eigenaar tekenen |

**Aanname-invalidatie**: in I0 wordt de drie-hypothese-lijst (zie 6.2) actief getoetst. Als HLEG-rubric niet machine-leesbaar te krijgen is in I0, schuift I1 op of wijzigt scope. Stoppen is een legitieme uitkomst.

**Wat I0 niet doet**: pretenderen dat de eval-set "compleet" is. Eval-sets groeien tijdens iteraties; I0 levert de minimaal werkbare versie.

### Template — invulblok

> [INVULLEN]
>
> | Iteratie | Doel | Scope | Succescriterium (kwantitatief) | Beslismoment |
> |---------|------|-------|--------------------------------|--------------|
> | I0 | ... | ... | ... | ... |
> | I1 | ... | ... | ... | ... |
> | I2 | ... | ... | ... | ... |
> | I3 | ... | ... | ... | ... |
> | I4 | ... | ... | ... | ... |
>
> **Drie expliciete hypotheses** (uit 6.2) en hoe iteratie I0 ze toetst:
> 1. ...
> 2. ...
> 3. ...
>
> **Stoppen als uitkomst**: bij welke meting wordt het project gestopt of gepivot? ...

## 6.4 Eval-set: het kompas van de iteratie

### Wat hoort hier

Een eval-set is geen test-suite. Het is een verzameling realistische voorbeelden die representatief zijn voor de productie-werkelijkheid, met een gewenste uitkomst per voorbeeld. Per iteratie wordt het systeem tegen de eval-set gemeten; vooruitgang is meetbaar of de iteratie heeft geen vooruitgang opgeleverd.

**Minimum-vereisten**:

- Voorbeelden zijn representatief voor de productie-distributie (geen alleen "schone" gevallen).
- Per voorbeeld een duidelijke gewenste uitkomst, vastgesteld door domein-experts.
- Eval-set bevat moeilijke gevallen, niet alleen happy-path.
- Eval-set is versie-gecontroleerd; veranderingen worden gemotiveerd.

**Anti-patroon**: een eval-set die uitsluitend door ontwikkelaars is samengesteld, of die alleen meet wat het systeem makkelijk kan. Dit creëert schijn-vooruitgang.

### Voorbeeld — Hexant

**Eval-set: 50 inter-auditor scoring-cases**.

Samenstelling:

- 12 historische audits, elk met 7 HLEG-dimensies = 84 dimensie-scoringen door senior auditor A en 84 door senior auditor B (12 audits × 7 dimensies × 2 auditors).
- Daarvan zijn 50 cases geselecteerd waar A en B substantieel verschillen (≥1,5 punten op 10-puntsschaal). Dit is de inter-auditor-variatie waarover de copilot aantoonbaar moet helpen.
- Elke case bevat: transcript-fragmenten die A en B gebruikten, scoring + motivatie van A, scoring + motivatie van B, en een consensus-score van een derde senior auditor (na review).

**Wie stelt op**: AI-Comité Hexant + twee senior auditors, in I0. Niet door BeeHaive-bouwer alleen.

**Versionering**: eval-set v1.0 in I0; eval-set v1.1 zodra in I2 blijkt dat één HLEG-dimensie systematisch slechter scoort — dan wordt de set uitgebreid met 10 extra cases voor die dimensie.

### Template — invulblok

> [INVULLEN]
>
> **Eval-set: ...** (naam, omvang).
>
> **Samenstelling** (waar komen de cases vandaan, wie levert de gewenste uitkomst):
> ...
>
> **Wie stelt op** (rollen, niet alleen ontwikkelaars):
> ...
>
> **Hoe wordt representativiteit geborgd** (anti-patroon-beleid):
> ...
>
> **Versionering**: ...

## 6.5 Cross-cutting check: hoofdstuk 6 ↔ hoofdstukken 0, 4 en 7

- **Hoofdstuk 0 (klantkaart)**: doorlooptijd blueprint-fase moet realistisch matchen met I0-I4. Voor Hexant: 6 weken blueprint-fase + 11 weken iteraties = 17 weken tot productie. Klopt met "6 maanden tot productie-klaar" (1.2).
- **Hoofdstuk 4 (risico)**: privacy-by-design-maatregelen en OWASP-mitigaties hebben elk een iteratie waarin ze geverifieerd worden. Bijvoorbeeld: tenant-scoping (LLM02) wordt in I3 expliciet getest met een "kruis-tenant"-scenario.
- **Hoofdstuk 7 (governance)**: de goedkeuringspoort aan het einde van I4 is gelijk aan de poort in 7.5 — niet twee aparte gates.

## 6.6 Checklist hoofdstuk 6

- [ ] Werkwijze gekozen (FDE-principes / klassieke discovery / hybride) met argumentatie.
- [ ] Drie expliciete hypotheses geformuleerd die in I0 worden getoetst.
- [ ] Iteraties I0 t/m In benoemd, met doel + scope + kwantitatief succescriterium + beslismoment.
- [ ] "Stoppen als uitkomst" is een legitiem beslispad in minstens één iteratie.
- [ ] Eval-set is bestaat in I0; samenstelling, eigenaarschap, en versionering vastgelegd.
- [ ] Eval-set representatief — niet alleen happy-path, niet alleen door ontwikkelaars opgesteld.
- [ ] Doorlooptijd iteraties consistent met hoofdstuk 0 (klantkaart) en hoofdstuk 7 (governance).
- [ ] Pilot expliciet als experiment gefaamd, niet als product.

## 6.7 Literatuur (kerncitaten dit hoofdstuk)

- Pragmatic Engineer, *What are Forward Deployed Engineers?* [21].
- SSO Network, *Forward Deployed Engineers Guide* [22].
- Stanford Digital Economy Lab, *Enterprise AI Playbook (51 cases)* [aanvullend, zie bijlage B].
- WorkOS, *Enterprise AI Agent Playbook* [26].

## 6.8 Status / laatste herziening

- Versie: 1.0
- Laatst bijgewerkt: 2026-04-28
- Wijzigingen sinds vorige versie: eerste vastlegging.
