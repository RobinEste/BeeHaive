# Hoofdstuk 7 — Governance, goedkeuring en Nederlandse context

## 7.1 Waarom dit hoofdstuk

Een blueprint zonder eigenaar is een document op een schap. Governance regelt drie zaken: wie draagt de verantwoordelijkheid, hoe wordt vendor-leverancierschap getoetst, en hoe wordt het ontwerp geborgd binnen de Nederlandse en Europese context. Dit hoofdstuk legt vast: het AI-Comité (of Center of Excellence), de AI Bill of Materials voor leveranciers, de aansluiting bij de Nederlandse AI Coalitie en het PACE-platform, en de criteria voor de goedkeuringspoort.

> *"Ethics is not a compliance checkbox; it is a proactive design principle."*
> — NL AIC / PACE-platform, *Participative And Constructive Ethics* [aanvullend]

## 7.2 Het AI-Comité: wie zit erin, wat tekent het

### Wat hoort hier

Een AI-Comité (synoniem: AI Center of Excellence, AI-stuurgroep) is het gremium dat ontwerpkeuzes over AI-systemen accordeert en eindverantwoordelijk is voor compliance binnen de organisatie. Het is geen technisch comité; het is een multidisciplinair gremium met expertise uit techniek, juridisch, infosec en de inhoudelijke business-portefeuille [convergence-Gemini]. Concrete voorbeelden: JLL, Workday.

**Minimale samenstelling:**

- Voorzitter — Head of AI of bestuurslid met portefeuille AI/digitalisering.
- Tech-vertegenwoordiger — leidinggevende engineering of architectuur.
- Juridisch — privacy/compliance-officer (DPO of equivalent).
- Infosec — CISO of security-lead.
- Business-portefeuille — de waarde-stroom-eigenaar uit hoofdstuk 0/1.
- Gebruikers-vertegenwoordiging — minstens één eindgebruiker of zijn lijn-manager.

**Wat het comité accordeert** (minimaal):

1. EU AI Act-tier en HLEG-positionering uit hoofdstuk 4.
2. Architectuurkeuze uit hoofdstuk 3.
3. Iteratieplan en eval-set uit hoofdstuk 6.
4. AI BOM van leveranciers (zie 7.3).
5. Sign-off voor productie.

### Voorbeeld — Hexant

**AI-Comité Hexant** (bestaat sinds maart 2025; vergadert 2-wekelijks):

- Voorzitter: Hoofd Audit Practice (tevens waarde-stroom-eigenaar).
- Tech: Hoofd IT Hexant.
- Juridisch: privacy-officer Hexant (extern ingehuurd, 0,2 fte).
- Infosec: senior auditor met CISA-certificering, intern.
- Business: de senior auditors uit de Audit Practice (twee personen, roterend).
- Gebruikers: drie senior auditors, één junior auditor.

**Wat het comité tekent voor Audit Scoring Copilot:**

- Tier-classificatie (Tier 4) uit hoofdstuk 4.
- DPIA-status (vereist, beperkt scope) na de herbeoordeling in 4.4.
- Iteratieplan I0-I4 uit hoofdstuk 6, inclusief eval-set v1.0.
- AI BOM van LLM-leverancier (zie 7.3).
- Eindgoedkeuring na I4.

### Template — invulblok

> [INVULLEN]
>
> | Rol | Persoon / functie | Mandaat |
> |-----|-------------------|---------|
> | Voorzitter | ... | ... |
> | Tech | ... | ... |
> | Juridisch | ... | ... |
> | Infosec | ... | ... |
> | Business / waarde-stroom-eigenaar | ... | ... |
> | Gebruikers-vertegenwoordiging | ... | ... |
>
> **Vergader-cadans**: ... (wekelijks / 2-wekelijks / maandelijks).
>
> **Wat het comité tekent**:
> 1. ...
> 2. ...

## 7.3 AI Bill of Materials: vendor-governance

### Wat hoort hier

Een AI Bill of Materials (AI BOM) is voor AI-systemen wat een Software Bill of Materials voor software is: een gedocumenteerde lijst van alle onderdelen — modellen, datasets, fine-tunes, tooling, third-party libraries — met herkomst, versie en compliance-evidence. AI BOMs worden door het AI-Comité geëist van leveranciers vóórdat hun product in productie kan [convergence-Gemini].

**Minimale velden in een AI BOM:**

- Modelnaam, -versie, -leverancier.
- Trainingsdata-categorieën (geen ruwe data; categorieën als "internet web crawl", "publieke datasets", "klant-data").
- Fine-tunes (intern of extern); herkomst trainingsdata fine-tune.
- Hosting-locatie en data-residency.
- Compliance-certificeringen (ISO 27001, SOC 2 Type II, AVG-DPA).
- Bekende beperkingen of risico's.
- Update-cadans en deprecation-beleid.

### Voorbeeld — Hexant: AI BOM voor LLM-leverancier

| Veld | Waarde (voorbeeld voor selectie LLM-leverancier) |
|------|--------------------------------------------------|
| Modelnaam / versie | (ingevuld na selectie hoofdstuk 6 BB_06) |
| Leverancier | (ingevuld) |
| Trainingsdata-categorieën | (ingevuld via leverancier-disclosure) |
| Fine-tunes | Geen (Hexant gebruikt baseline-model met RAG) |
| Hosting-locatie | EU (eis) |
| Data-residency-garantie | EU/EEA, schriftelijk in DPA |
| Compliance-certificeringen | Minimaal ISO 27001 of SOC 2 Type II + AVG-DPA |
| Bekende beperkingen | Gedocumenteerd door leverancier |
| Update-cadans | Modelversie wordt vastgelegd; major upgrade triggert hertest tegen eval-set |
| Deprecation-beleid | Minimaal 6 maanden vooraankondiging vereist |

**Eis aan elke leverancier**: AI BOM aanleveren bij contract-ondertekening; bijwerken bij elke major model-upgrade.

### Template — invulblok

> [INVULLEN]
>
> | Veld | Waarde |
> |------|--------|
> | Modelnaam / versie | ... |
> | Leverancier | ... |
> | Trainingsdata-categorieën | ... |
> | Fine-tunes | ... |
> | Hosting-locatie | ... |
> | Data-residency-garantie | ... |
> | Compliance-certificeringen | ... |
> | Bekende beperkingen | ... |
> | Update-cadans | ... |
> | Deprecation-beleid | ... |
>
> **Eis aan elke nieuwe leverancier**: ...

## 7.4 Nederlandse context: NL AIC en PACE

### Wat hoort hier

Voor Nederlandse organisaties zijn twee gremia richtinggevend, naast EU AI Act en HLEG [convergence-Gemini]:

- **Nederlandse AI Coalitie (NL AIC)** — publiek-private samenwerking met werkgroepen waaronder Data Delen. De interoperabiliteits-richtlijnen voor data spaces zijn relevant voor organisaties die data tussen partijen willen uitwisselen voor AI-doeleinden.
- **PACE-platform** — *Participative And Constructive Ethics*. Beschouwt ethiek als proactief ontwerpprincipe in plaats van compliance-vink achteraf. Methodisch onderscheidend: stakeholder-betrokkenheid in het ontwerp-proces, niet alleen in de toetsing.

**Wat dit betekent voor de blueprint-fase:**

- Wanneer data-uitwisseling tussen partijen aan de orde is: NL AIC-interoperabiliteits-richtlijnen overwegen vóór een eigen format te kiezen.
- Wanneer de oplossing maatschappelijke implicaties heeft of breder wordt uitgerold: PACE-aanpak (participatief, constructief) toepassen — niet alleen ALTAI-checklist invullen, maar stakeholders actief betrekken in het ontwerp-gesprek.
- Voor outward-facing of game-changing AI-positie (Gartner-radar in 1.2): NL AIC en PACE expliciet overwegen.

### Voorbeeld — Hexant

**NL AIC**: niet primair van toepassing — geen data-uitwisseling tussen Hexant en derden anders dan de auditklant zelf, en die uitwisseling is contractueel bilateraal geregeld. Wel relevant voor toekomstige outward-facing-positionering (zie 1.2).

**PACE**: gedeeltelijk geadopteerd. Concretisering:

- Senior auditors zijn betrokken vanaf I0 (ontwerp van eval-set), niet pas in I4 (rollout). Dit is participatief in PACE-zin.
- Een interview-deelnemers-perspectief is toegevoegd via de privacy-officer in 4.4 — DPIA-status werd herzien op basis van wat interview-deelnemers zouden ervaren, niet alleen op basis van wat technisch verplicht is.
- Een formele PACE-sessie is gepland tussen I2 en I3, met deelname van Hexant's klant-vertegenwoordigers (twee CIO's van eerder geauditeerde organisaties), om te toetsen of de copilot-werkwijze acceptabel is voor de auditklant-relatie.

### Template — invulblok

> [INVULLEN]
>
> **NL AIC van toepassing?** ja / nee — argumentatie:
> ...
>
> **Bij ja**: welke werkgroep (Data Delen, anders), en welke richtlijn raakt deze blueprint:
> ...
>
> **PACE-aanpak overwogen?** ja / nee — argumentatie:
> ...
>
> **Bij ja**: hoe is participatieve betrokkenheid verankerd in het iteratieplan (verwijs naar hoofdstuk 6):
> ...

## 7.5 Goedkeuringspoort: criteria voor sign-off

### Wat hoort hier

De goedkeuringspoort is het moment waarop de blueprint de bouw-fase verlaat en de productie-fase ingaat. Sign-off vereist concrete, getoetste criteria — geen procedurele "comité akkoord". Vereisten:

- Alle hoofdstuk-checklists (0-8 + bijlage A) afgevinkt of expliciet "n.v.t."-onderbouwd.
- Eval-set-resultaat van laatste iteratie ≥ succescriterium hoofdstuk 6.
- DPIA en (bij Tier 2) FRIA afgerond en geaccordeerd door privacy-officer.
- AI BOM van alle leveranciers ontvangen en geaccordeerd.
- Iteratieplan-rapportage (welke hypotheses bevestigd/verworpen, welke aanpassingen gemaakt).
- Twee handtekeningen: AI-Comité (collectief) + waarde-stroom-eigenaar (individueel).

### Voorbeeld — Hexant

**Goedkeuringspoort einde I4**:

- Eval-set: inter-auditor-variatie ≤ ±0,8 op 50 cases (doel hoofdstuk 0).
- Live-meting drie audits in I4: scoring-tijd 4-6u/audit (doel hoofdstuk 0).
- DPIA-rapport ondertekend door privacy-officer.
- AI BOM van LLM-leverancier ontvangen.
- Iteratie-rapportage: drie hypotheses uit 6.2 zijn óf bevestigd, óf verworpen-met-aanpassing.
- Handtekening AI-Comité Hexant + Hoofd Audit Practice.

**Bij niet halen van één criterium**: geen go-live; iteratie I5 plannen of project pauseren met expliciete hervatting-criteria.

### Template — invulblok

> [INVULLEN]
>
> **Goedkeuringspoort-criteria**:
> 1. Eval-set-resultaat: ... (cijfer + criterium)
> 2. Live-meting: ... (cijfer + criterium)
> 3. DPIA-status: ... (afgerond door wie)
> 4. AI BOM ontvangen van: ... (lijst leveranciers)
> 5. Iteratie-rapportage: hypotheses bevestigd / verworpen / aangepast
> 6. Tekenende rollen: ... (AI-Comité + waarde-stroom-eigenaar)
>
> **Bij niet halen van een criterium**: vervolg-pad (I+1 / pauzeren / stoppen):
> ...

## 7.6 Cross-cutting check: hoofdstuk 7 ↔ hoofdstukken 4 en 6

- **Hoofdstuk 4**: het AI-Comité accordeert de tier-classificatie en de DPIA-status; deze sign-offs lopen via 7.2 en 7.5, niet via 4 zelf.
- **Hoofdstuk 6**: de goedkeuringspoort einde I4 is dezelfde gate als 7.5; geen dubbele governance-stap.
- **Hoofdstuk 0**: de "goedkeuringspoort" in de klantkaart verwijst naar 7.5; consistent.

## 7.7 Checklist hoofdstuk 7

- [ ] AI-Comité samenstelling vastgelegd; alle zes minimale rollen vertegenwoordigd.
- [ ] Vergader-cadans en accordering-mandaat expliciet.
- [ ] AI BOM-template gedefinieerd met minimaal vereiste velden.
- [ ] AI BOM van eerste leverancier opgevraagd en getoetst (of bij intake gevraagd).
- [ ] NL AIC-toets uitgevoerd; bij van toepassing: relevante werkgroep / richtlijn benoemd.
- [ ] PACE-aanpak overwogen en concretisering gemaakt waar van toepassing.
- [ ] Goedkeuringspoort-criteria zijn meetbaar en kwantitatief, niet procedureel.
- [ ] Pad bij niet halen van een criterium expliciet — geen vage "comité besluit".
- [ ] Twee handtekeningen-eis gehandhaafd (AI-Comité collectief + waarde-stroom-eigenaar individueel).

## 7.8 Literatuur (kerncitaten dit hoofdstuk)

- NL AIC + PACE-platform (zie bijlage B, aanvullende bronnen).
- Sam Obeidat, *AI Business Model Canvas* — aansluiting bij governance-niveau (zie bijlage B).
- HLEG, *Ethics Guidelines for Trustworthy AI* [16].
- Convergence-pass intern (gedeelde bevindingen Claude-pipeline × Gemini Deep Research).

## 7.9 Status / laatste herziening

- Versie: 1.0
- Laatst bijgewerkt: 2026-04-28
- Wijzigingen sinds vorige versie: eerste vastlegging.
