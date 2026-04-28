# Hoofdstuk 2 — Use-case-discovery in zeven stappen

## 2.1 Waarom dit hoofdstuk

Hoofdstuk 1 verankert de blueprint in een waarde-stroom en wijst de fase aan waar AI hoort. Dit hoofdstuk gaat één niveau dieper: binnen die fase wordt de eerste use-case gedestilleerd via Sam Obeidat's discovery-flow van zeven stappen, gevolgd door een geschiktheidstoets in drie filters. Het doel is niet "een use-case kiezen", maar bewijzen dat de gekozen use-case zowel waardevol als haalbaar is — vóór een architectuurkeuze valt in hoofdstuk 3.

> *"Most AI projects don't fail because the technology is weak — they fail because the business model is missing."*
> — Sam Obeidat (CAIO Newsletter, 2025) [aanvullend, zie bijlage B]

> *"The purpose is important, and the purpose comes from people."*
> — Cassie Kozyrkov (Acceldata-interview, 2025) [2]

## 2.2 Sam Obeidat's zeven stappen

### Wat hoort hier

Sam Obeidat publiceerde "How to Identify an AI Use Case in 7 Steps" (CAIO Newsletter, gevalideerd met World AI Council, geüpdatet dec. 2025). Het is op dit moment de meest complete, gepubliceerde en praktijkgevalideerde aanpak om van waarde-stroom naar AI-use-case te komen. Vandaar dat BB_02 en deze template hem als ruggengraat hanteren. De zeven stappen zijn cumulatief: elke stap bouwt op de vorige.

1. **Map de waarde-stroom** — trigger → fasen → uitkomst, met stakeholders, één-noord-ster-KPI en betrokken afdelingen. Grotendeels al gedaan in hoofdstuk 1; hier wordt de map gebruikt als vertrekpunt.
2. **Diagnose via TRACE** — binnen de waarde-stroom kies je één werkstroom en pas je TRACE toe: **T**rigger (wat start de werkstroom?), **R**oute (welke handen, systemen en stappen volgen?), **A**nnotate (waar wordt informatie toegevoegd of vertaald?), **C**heck (waar zijn controles, goedkeuringen, validaties?), **E**scalate (waar gaat het naar een hogere autoriteit?). Bij elke stap kwantificeer je de frictie. Een Obeidat-principe dat hard staat: *"Never optimize a step that shouldn't exist."*
3. **Scherpe probleemformulering** — *Probleem = huidige toestand + pijn + gekwantificeerde impact + wie wordt geraakt*. Vergelijk: "Cashflow-zicht is slecht" (vaag, geen AI-aangrijpingspunt) versus "Cashflow-consolidatie kost 4-6 uur per project, leunt op vijf spreadsheets en biedt geen forecast, waardoor management op verouderde cijfers beslist" (concreet, gekwantificeerd, eindgebruiker geïdentificeerd).
4. **Waarde-propositie langs zes AI-Value-Objectives** — *Speed/Time*, *Cost*, *Revenue*, *Quality*, *Robustness*, *Impact*. De waarde-propositie noemt expliciet welke objectieven worden gediend en welke trade-offs worden geaccepteerd.
5. **AI Solution Canvas** — vijf niet-technische velden die de basis leggen voor het klantgesprek: *Main Inputs* (welke informatie kijkt de AI?), *Main Job of AI* (wat moet de AI met die input doen?), *How Humans Use It* (dashboard / alerts / copilot / achtergrond-automatisering?), *AI Role Name* (leesbare titel — bv. "AI Klant-Adviseur"), *AI Solution Summary* (één à twee zinnen).
6. **Feasibility Check Canvas** — twee vragen die meestal bepalen of het haalbaar is: *hebben we de data?* en *hebben we de tech-readiness?* Uitkomst: *ready now*, *needs prep work*, of *not feasible yet*. Voorkomt de faalmodus waarin een mooi ontwerp bij de bouw vastloopt op afwezige data.
7. **Impact Estimation Canvas** — een korte tabel met vier rijen: tijd, kosten, kwaliteit/risico, beslissingsimpact. Per rij huidige toestand versus verwachte verbetering. Geen volledig ROI-model, wel een richtinggevend beeld dat een directie kan beoordelen.

**Daarna (optioneel)**: AI Business Model Canvas (AI-BMC, Obeidat 2025) — elf-bloks executive-validatie vóór architectuur-commitment: Value Proposition, Data, Capabilities, Team, Key Metrics, Systems & Platforms, Stakeholders, End Users, Key Dependencies, Estimated Cost, Business Outcome.

### Voorbeeld — Hexant: van AI-Readiness Audit naar Audit Scoring Copilot

**Stap 1 — Map de waarde-stroom.** Reeds in hoofdstuk 1 vastgelegd: AI-Readiness Audit, zes fasen, KPI-noord-ster doorlooptijd 7,2 → 5,0 weken. AI-interventie hoort in fase 4 (scoring en triangulatie).

**Stap 2 — Diagnose via TRACE op werkstroom *scoring*:**

- **Trigger:** alle interviews afgerond, transcripten beschikbaar, peer-review-team klaar.
- **Route:** senior auditor leest transcripten (~25 stuks à 30 min) → identificeert evidence per HLEG-dimensie → kent voorlopige score (0-10) toe per dimensie → triangulatie met documentatie (fase 2) en peer-review.
- **Annotate:** per uitspraak in een transcript wordt geclassificeerd op HLEG-dimensie en sterkte (sterk-bewijs / zwak-bewijs / signaal).
- **Check:** peer review op consistentie tussen scoring-onderbouwingen.
- **Escalate:** bij dimensie-score onder 4 of bij conflicterende evidence: tweede senior auditor toetst.

Frictie-meting: ~28 uur in *Route* (lezen + classificeren + scoren) en ~4 uur in *Check*. *Annotate* gebeurt impliciet en is precies waar inter-auditor-variatie ontstaat. Stap-die-niet-zou-bestaan-toets: handmatig opnieuw lezen van een transcript bij elke nieuwe scoring-iteratie is een symptoom van ontbrekende structurering, niet van inherente complexiteit.

**Stap 3 — Scherpe probleemformulering.** *Het scoren van interview-transcripten op de zeven HLEG-dimensies kost een senior auditor gemiddeld 28-32 uur per audit, leunt op impliciete classificatie van uitspraken zonder gestructureerde tussenlaag, en levert een inter-auditor-variatie van ±2,1 punten op een 10-puntsschaal — waardoor de auditkwaliteit afhangt van wélke senior auditor de scoring uitvoert, en het maximum van 18 audits per jaar bij het huidige team niet is op te schalen.*

**Stap 4 — Waarde-propositie langs zes AI-Value-Objectives.**

- *Speed/Time:* primair — scoring-fase van 28-32u naar 4-6u.
- *Quality:* primair — inter-auditor-variatie van ±2,1 naar ≤±0,8 door gestructureerde evidence-extractie.
- *Robustness:* secundair — minder afhankelijkheid van individu-bias.
- *Cost:* secundair — capaciteits-uitbreiding 18 → 30 audits/jaar zonder extra fte's.
- *Revenue / Impact:* niet primair — outward-facing-positie volgt pas later.

Trade-off geaccepteerd: gestructureerde evidence-extractie verandert iets in de werkwijze van de auditor (van "vrije lezing" naar "geleide review"). Aanvaard mits de auditor altijd kan terugzien waar elke score-suggestie vandaan komt.

**Stap 5 — AI Solution Canvas.**

- *Main Inputs:* interview-transcripten (~25 per audit, ~6 uur opname elk), HLEG-rubric (Hexant-eigen, geënt op HLEG 7), eerdere audit-rapporten (Knowledge Management).
- *Main Job of AI:* uitspraken classificeren naar HLEG-dimensie + sterkte; voorlopige dimensie-score voorstellen met inline citatie naar transcript-fragmenten.
- *How Humans Use It:* in-app copilot voor de senior auditor; per dimensie ziet de auditor voorgestelde score + onderbouwende fragmenten; auditor accepteert, past aan, of overschrijft.
- *AI Role Name:* "Audit Scoring Copilot".
- *AI Solution Summary:* "Een AI-copilot die ruwe interview-transcripten van een AI-Readiness Audit omzet naar een initiele scoring op de zeven HLEG-dimensies, met inline citatie naar het transcript-fragment, voor menselijke review en bijstelling door de senior auditor."

**Stap 6 — Feasibility Check Canvas.**

- *Data:* transcripten (Whisper-output uit Zoom — ~12 audits aan historisch materiaal, gestructureerd) — *ready*. HLEG-rubric (Hexant-eigen Excel, niet machine-leesbaar) — *needs prep work* (uniformeren naar JSON, geschatte 2 weken in iteratie I1). Historische scoring-rapporten (~12) — *ready* maar omvang beperkt voor evaluatie. Status totaal: **needs prep work**.
- *Tech:* PostgreSQL/pgvector zelf-gehost — beschikbaar; LLM-keuze met EU-residency open (zie hoofdstuk 3 en 6); IT-team capaciteit gereserveerd. Status: **ready** met bouw.

**Stap 7 — Impact Estimation Canvas.**

| Dimensie | Huidige toestand | Verwachte verbetering |
|----------|------------------|-----------------------|
| Tijd | 28-32u senior auditor per audit, scoring-fase | 4-6u per audit, scoring-fase |
| Kosten | ~€4.000 senior-auditor-uren per audit aan scoring | ~€800/audit + LLM-kosten ~€20/audit |
| Kwaliteit/risico | Inter-auditor-variatie ±2,1 op 10-puntsschaal | ≤±0,8; expliciete evidence-trail per score |
| Beslissingsimpact | Capaciteit max 18 audits/jaar | Capaciteit 30 audits/jaar bij ongewijzigde teamomvang |

**AI-BMC (optioneel).** Voor Hexant niet ingevuld in deze blueprint-fase: het AI-Comité tekent op de zeven stappen + de drie filters (zie 2.3); de bredere business-model-impact (inward-facing, geen propositie-wijziging) is in hoofdstuk 1 al adequaat afgekaart.

### Template — invulblok

> [INVULLEN per nieuwe opdracht]
>
> **Stap 1 — Map de waarde-stroom**: verwijs naar hoofdstuk 1, geef de gekozen fase aan waar AI hoort.
>
> **Stap 2 — Diagnose via TRACE op werkstroom *...*:**
> - Trigger: ...
> - Route: ...
> - Annotate: ...
> - Check: ...
> - Escalate: ...
> - Frictie kwantitatief per stap: ...
> - "Step that shouldn't exist"-toets: ...
>
> **Stap 3 — Scherpe probleemformulering**: huidige toestand + pijn + gekwantificeerde impact + wie wordt geraakt.
>
> **Stap 4 — Waarde-propositie langs zes AI-Value-Objectives**: primair / secundair / niet, met trade-offs.
>
> **Stap 5 — AI Solution Canvas**: Main Inputs, Main Job of AI, How Humans Use It, AI Role Name, AI Solution Summary.
>
> **Stap 6 — Feasibility Check Canvas**: data-status (ready / needs prep / not feasible) + tech-status, met onderbouwing.
>
> **Stap 7 — Impact Estimation Canvas**: tabel met vier rijen (tijd, kosten, kwaliteit/risico, beslissingsimpact); per rij huidig vs. verwacht.
>
> **AI-BMC (optioneel)**: ingevuld? ja/nee, met motivatie.

## 2.3 De drie filters: is dit überhaupt een AI-probleem?

### Wat hoort hier

Voordat de uitkomst van de zeven stappen doorgaat naar architectuur (hoofdstuk 3), passeert de use-case drie filters. Eén "ja" volstaat niet; de filters zijn cumulatief.

**Filter 1 — De drie-signalen-toets** (Anthropic, via WorkOS) [26]:

- Complexe besluitvorming die contextueel varieert?
- Regelonderhoud dat developer-tijd vereist bij elke wijziging?
- Ongestructureerde data (natural language, documenten, conversaties)?

Tenminste één "ja" is een noodzakelijke voorwaarde — niet voldoende. Als geen van de drie speelt: het is geen AI-probleem maar waarschijnlijk een dashboard- of rule-engine-probleem.

**Filter 2 — Geschiktheidscriteria** [7]:

- AI is geschikt wanneer: het probleem te complex is voor deterministische regels, output beschrijfbaar maar niet specificeerbaar is, voldoende representatieve data beschikbaar is, een zekere foutmarge acceptabel is, en het doel kwantificeerbaar is.
- AI is *niet* geschikt wanneer: een BI-dashboard of regelautomatisering volstaat, data ontbreekt, foutmarge nul moet zijn zonder oversight, of het doel niet kwantificeerbaar is.

**Filter 3 — AI-3P-score** (Marina Tosic) [8]:

- Gewogen score: People (40%) × Process (35%) × Product (25%), schaal 0-100.
- 80-100: bouwen kan starten; 60-79: piloot met guardrails; 0-59: risico's eerst aanpakken.

### Voorbeeld — Hexant

**Filter 1 — drie-signalen-toets:** ja op alle drie. Scoring is contextueel-variërend (dezelfde uitspraak betekent iets anders bij verschillende organisatie-grootte); HLEG-rubric-onderhoud kost senior-auditor-tijd bij elke release; transcripten zijn ongestructureerd. ✅

**Filter 2 — geschiktheidscriteria:** complex voor regels (te veel context), output beschrijfbaar (HLEG-dimensie + score + evidence), data aanwezig (12 historische audits), foutmarge acceptabel met human-in-the-loop, doel kwantificeerbaar (variatie ±2,1 → ≤±0,8). ✅

**Filter 3 — AI-3P-score (geschat na intake-gesprek):**

- People (40%) — score 80: senior auditors staan ervoor open; AI-Comité Hexant is ervaren met AI-tooling; QA-team aanvankelijk skeptisch maar betrokken.
- Process (35%) — score 70: bestaande peer-review-stap maakt human-in-the-loop natuurlijk; HLEG-rubric is geformaliseerd; inter-auditor-variatie is structureel gemeten (positief signaal voor evaluatie-cultuur).
- Product (25%) — score 75: data en tooling beschikbaar; afhankelijkheid van LLM-residency en transcript-OCR-kwaliteit (audio → tekst).

Gewogen: 0,40 × 80 + 0,35 × 70 + 0,25 × 75 = **75,25** → **piloot met guardrails**. Geen "bouwen kan starten"-score, dus pilot expliciet als experiment frame'n (hoofdstuk 6).

### Template — invulblok

> [INVULLEN]
>
> **Filter 1 — drie-signalen-toets**:
> - Contextueel variërend? ja / nee — onderbouwing: ...
> - Regelonderhoud kost developer-tijd? ja / nee — onderbouwing: ...
> - Ongestructureerde data? ja / nee — onderbouwing: ...
>
> **Filter 2 — geschiktheidscriteria** (vink af, met onderbouwing per criterium):
> - [ ] Te complex voor regels: ...
> - [ ] Output beschrijfbaar maar niet specificeerbaar: ...
> - [ ] Data beschikbaar en representatief: ...
> - [ ] Foutmarge acceptabel met oversight: ...
> - [ ] Doel kwantificeerbaar: ...
>
> **Filter 3 — AI-3P-score**:
> - People-score (0-100): ...
> - Process-score (0-100): ...
> - Product-score (0-100): ...
> - Gewogen score: 0,40 × People + 0,35 × Process + 0,25 × Product = ...
> - Advies: bouwen kan starten / piloot met guardrails / risico's eerst aanpakken.

## 2.4 Wat we expliciet *niet* doen

### Wat hoort hier

Discovery is even belangrijk in wat het uitsluit. Knelpunten of werkstromen die *binnen* de gekozen waarde-stroom liggen maar geen AI-probleem zijn, krijgen hier expliciet een "niet in scope"-stempel met reden. Dit voorkomt scope-creep tijdens de bouw.

### Voorbeeld — Hexant

| Werkstroom in waarde-stroom | Waarom niet AI-waardig in deze blueprint |
|------------------------------|------------------------------------------|
| Fase 1: kick-off en stakeholder-mapping | Mens-werk (relatie-opbouw); AI maakt dit niet beter, mogelijk slechter |
| Fase 3: interviews afnemen | Idem; AI-ondersteuning bij voorbereiding kan in een toekomstige fase, niet nu |
| Fase 5: rapportage opstellen | Sjablonen + scoring-output uit fase 4 zijn afdoende; geen AI nodig |
| Fase 6: presentatie aan klant-directie | Mens-werk; out-of-scope |

### Template — invulblok

> [INVULLEN]
>
> | Werkstroom / knelpunt | Waarom niet AI-waardig |
> |------------------------|------------------------|
> | ... | ... |

## 2.5 Checklist hoofdstuk 2

- [ ] Stap 1 — waarde-stroom-map (hoofdstuk 1) is vertrekpunt.
- [ ] Stap 2 — TRACE-diagnose toegepast op één werkstroom; frictie kwantitatief per stap.
- [ ] Stap 2 — *"Never optimize a step that shouldn't exist"*-toets uitgevoerd.
- [ ] Stap 3 — probleem geformuleerd als huidige toestand + pijn + gekwantificeerde impact + wie.
- [ ] Stap 4 — primaire AI-Value-Objective(s) gekozen, met trade-offs benoemd.
- [ ] Stap 5 — AI Solution Canvas (5 velden) volledig.
- [ ] Stap 6 — Feasibility Check: data-status én tech-status met *ready / needs prep / not feasible*.
- [ ] Stap 7 — Impact Estimation Canvas op vier dimensies (tijd, kosten, kwaliteit/risico, beslissingsimpact).
- [ ] AI-BMC overwogen — wel/niet ingevuld, met motivatie.
- [ ] Drie filters: alle drie afzonderlijk doorlopen; AI-3P-score numeriek berekend.
- [ ] Bij AI-3P < 60: actieplan eerst, geen bouw.
- [ ] Niet-AI-knelpunten uit dezelfde waarde-stroom expliciet "niet in scope" gemarkeerd.

## 2.6 Literatuur (kerncitaten dit hoofdstuk)

- Sam Obeidat, *How to Identify an AI Use Case in 7 Steps*, CAIO Newsletter, geüpdatet dec. 2025 (`bron-131` in convergence-pass; aanvullend, zie bijlage B).
- Sam Obeidat, *The AI Business Model Canvas*, 2025 (aanvullend).
- Cassie Kozyrkov (Acceldata-interview) [2].
- Microsoft, *AI Decision Framework* [7].
- Marina Tosic, *AI-3P Assessment Framework*, Towards Data Science [8].
- WorkOS, *Enterprise AI Agent Playbook* (drie-signalen-framework) [26].

## 2.7 Status / laatste herziening

- Versie: 1.0
- Laatst bijgewerkt: 2026-04-28
- Wijzigingen sinds vorige versie: eerste vastlegging.
