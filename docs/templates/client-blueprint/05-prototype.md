# Hoofdstuk 5 — Prototype als gespreksanker

## 5.1 Waarom dit hoofdstuk

Een tekst-blueprint is een abstractie. Een werkend prototype dwingt het juiste gesprek af: stakeholders zien iets concreets en reageren op de werkelijkheid in plaats van op een belofte. Maar een gepolijste UI verleidt tot schijn-zekerheid; klanten gaan geloven dat de oplossing al "bijna af" is, terwijl de businesslogica en data-realiteit nog onaangeroerd zijn. Dit hoofdstuk legt vast hoe het prototype in de blueprint-fase wordt ingezet — als gespreksanker, niet als validatie-eindpunt — welke tool past bij welke vraag, en hoe scope-creep wordt voorkomen.

> *"AI is geen vervanging voor kritisch denken; menselijk oordeel is nog steeds noodzakelijk om gegenereerde inzichten te interpreteren en geïnformeerde productbeslissingen te nemen."*
> — Lenny's Newsletter, *A Guide to AI Prototyping for Product Managers* [25]

## 5.2 Prototype-regels: anker, geen surrogaat

### Wat hoort hier

Drie regels gelden onverkort, ongeacht welke tool wordt gekozen [23, 24, 25]:

1. **Het prototype is een gespreks-instrument, geen oplevering.** Doel: stakeholder-alignment over scope, output-vorm en mens-AI-interactie versnellen, vóór een architectuur- of bouw-commitment.
2. **Het prototype valideert niets zonder evaluatiecriteria.** Een mooie demo zonder vooraf gedefinieerde succescriteria zegt niets over haalbaarheid. De evaluatiecriteria komen uit hoofdstuk 2 (stap 7, Impact Estimation) en hoofdstuk 6 (eval-set).
3. **Het prototype mag het gesprek over doel, data en risico's niet vervangen.** Als het prototype dat gesprek opzij duwt, is het contraproductief en moet het worden ingetrokken.

**Productief gebruik** (uit research):

- Aanname-invalidatie: laat zien wat *niet* werkt, niet alleen wat kan.
- Scope-verkenning: alignment tussen niet-technische stakeholders over functionele grenzen.
- Concrete demo voor goedkeuringspoort, vóór de bouw-commitment.

**Faalmodi:**

- Surrogaat voor gebruikersonderzoek (gepolijste UI = schijn-zekerheid).
- Productiecode-equivalent (klant verwacht release-kwaliteit).
- "Scope lock-in op vroege UI": een vroege demo bevriest beslissingen die nog open hadden moeten staan.

### Voorbeeld — Hexant

Het prototype voor Hexant heeft twee doelen, geen drie:

- **Senior auditors laten zien hoe de copilot de scoring-fase verandert** — verschuiving van "vrije lezing" naar "geleide review met inline citatie". Mens-AI-interactie staat centraal; de eerste vraag is *of senior auditors deze werkstroom acceptabel vinden*, niet of het model goed scoort.
- **AI-Comité en QA-afdeling het concept laten beoordelen** — een werkend voorbeeld voor de goedkeuringspoort, vóór commitment aan een definitieve architectuur (hoofdstuk 3) en iteratieplan (hoofdstuk 6).

Niet-doelen: *pretenderen dat de scoring goed is*. De prototype-output gebruikt synthetische transcripten en het scoring-resultaat wordt expliciet gelabeld als "demonstratie, niet geëvalueerd". Dit voorkomt dat een succesvolle demo de evaluatie-fase opzij duwt.

### Template — invulblok

> [INVULLEN]
>
> **Doel(en) van het prototype** (max 3, expliciet):
> 1. ...
> 2. ...
>
> **Niet-doelen** (wat het prototype expliciet *niet* aantoont):
> - ...
>
> **Wanneer wordt het ingetrokken?** (bijv. zodra goedkeuringspoort gehaald, of zodra eval-set live is):
> ...

## 5.3 Vijf prototype-tools: sterktes en faalmodi

### Wat hoort hier

Vijf tools domineren het 2026-landschap voor prototype-driven blueprinting [23, 24, 25]. Elk heeft een sterkte en een faalmodus die in de blueprint-context expliciet moet worden afgewogen.

| Tool | Sterk als blueprint-vehikel | Faalmodus in blueprint-context |
|------|------------------------------|----|
| **Google Stitch** (Google I/O 2025) | Live ideation, multi-richting UX-verkenning, voice canvas in meetings | Geen backend → misleidend voor processen met complexe businesslogica; nog Google Labs-status (maart 2026) → onzeker voor enterprise-klanten |
| **v0 by Vercel** | Productie-kwaliteit React/Tailwind-componenten (shadcn/ui); developer-team alignment | Alleen React/Next.js; componenten ≠ applicaties; technisch publiek noodzakelijk |
| **Lovable** | Full-stack: idee naar deployed app (TypeScript + Supabase + auth + hosting); non-technische stakeholders zien werkende flow | Vendor lock-in; klanten overschatten gereedheid ("dit is toch de productie-versie?"); design-kwaliteit secundair |
| **Bolt.new** | Snelste output; live demo in meeting; browser — nul lokale setup | Token-kosten onvoorspelbaar bij iteratie; eerste output is ruw; verwachtingsmanagement vereist |
| **Claude Artifacts / Claude Design** | Snelle interactieve component of PoC, deelbaar in 10 minuten; sterk voor één-component verkenning | Geen persistente state buiten artefact-scope; beperkt tot één artefact; Claude Design nog research-preview |

**Keuze-leidraad** (samengevat):

- Niet-technische stakeholders, full-flow demo, korte tijd → **Lovable**.
- Eén UI-richting verkennen met designer of business-lead → **Stitch**.
- Eén interactieve component voor klant-feedback → **Claude Artifacts**.
- React-team dat productie-componenten direct in de codebase wil → **v0**.
- Eerste, snelste, browser-only demo (vluchtige variant van Lovable) → **Bolt.new**.

**Kritische waarschuwing**: alle vijf produceren oppervlakkig gepolijste UI's die strategische vragen (gebruikersonderzoek, businesslogica-validatie, A/B-testopzet) niet beantwoorden [24]. Het prototype is altijd een kortere versie van het echte gesprek, nooit een vervanging.

### Voorbeeld — Hexant: Lovable voor de flow, Claude Artifacts voor één component

**Lovable** voor de werkstroom-demo van de Audit Scoring Copilot. Argumentatie:

- Twee primaire doelgroepen (senior auditors, AI-Comité) zijn niet-technisch — full-stack demo zonder code zien werken is meer overtuigend dan een wireframe.
- De interactie (transcript-input → voorgestelde score per HLEG-dimensie → auditor accepteert/past aan) is de kern van het gesprek — Lovable kan dit binnen één werkdag werkend tonen.
- Vendor lock-in van Lovable is hier acceptabel: het prototype wordt ingetrokken zodra de goedkeuringspoort gehaald is en het echte iteratieplan (hoofdstuk 6) start.

**Claude Artifacts** voor één geïsoleerde verkenning: hoe ziet "score-suggestie met inline citaties" eruit op één HLEG-dimensie. Wordt gedeeld in een sessie met QA-afdeling en twee senior auditors, vóór de Lovable-demo.

**Niet gekozen**:

- Stitch — Hexant-stakeholders willen werkende flow, geen UX-verkenning op zichzelf.
- v0 — Hexant heeft geen React-team, en de demo moet bedrijfstaal spreken, niet developer-jargon.
- Bolt.new — overlap met Lovable; Lovable is rijker voor non-technische demo.

### Template — invulblok

> [INVULLEN]
>
> **Hoofd-tool** (één): Stitch / v0 / Lovable / Bolt.new / Claude Artifacts — argumentatie:
> ...
>
> **Aanvullend** (optioneel, één): ... — argumentatie:
> ...
>
> **Niet gekozen** (per niet-gekozen tool, één regel waarom niet):
> - Stitch: ...
> - v0: ...
> - Lovable: ...
> - Bolt.new: ...
> - Claude Artifacts: ...

## 5.4 Wat een goed prototype-script bevat

### Wat hoort hier

Het prototype zelf is niet voldoende; de demo-context bepaalt of het zijn rol als gespreksanker waarmaakt. Een minimaal demo-script:

1. **Vraag-vooraf**: één concrete vraag die beantwoord moet worden door deze demo. Geen vraag = geen gesprek.
2. **Toon de happy path**: één pad door het systeem dat de kern-interactie laat zien.
3. **Toon één faalmodus**: één scenario waar het systeem expliciet fout gaat (en de mens corrigeert). Voorkomt schijn-zekerheid.
4. **Vraag-na**: één concrete beslissing die uit deze demo voortkomt — geen vage "wat denken jullie?"

### Voorbeeld — Hexant

- *Vraag-vooraf:* "Vinden senior auditors de geleide-review-werkwijze acceptabel, of voelt het als deskilling?"
- *Happy path:* twee transcript-fragmenten → drie HLEG-dimensies krijgen een score met onderliggende citatie → auditor accepteert.
- *Faalmodus:* een transcript-uitspraak die ironisch bedoeld was wordt verkeerd geclassificeerd; de auditor moet handmatig overschrijven; het systeem laat zien *waarom* het de uitspraak op die manier las.
- *Vraag-na:* "Mag iteratie I1 starten met deze werkstroom als uitgangspunt, of moet de interactie eerst herontworpen worden?"

### Template — invulblok

> [INVULLEN]
>
> **Vraag-vooraf**: ...
> **Happy path** (één scenario): ...
> **Eén faalmodus** (expliciet getoond): ...
> **Vraag-na** (concrete beslissing): ...

## 5.5 Cross-cutting check: hoofdstuk 5 ↔ hoofdstuk 6

Het prototype is geen iteratie. Iteratie I0 (hoofdstuk 6) start zodra het prototype zijn werk heeft gedaan en de goedkeuringspoort is gehaald. Verwarring tussen prototype en I0 leidt tot scope-creep ("we breiden de Lovable-app gewoon uit naar productie"); houd ze gescheiden.

**Voor Hexant**: het Lovable-prototype wordt na de goedkeuringspoort *gearchiveerd* en niet doorontwikkeld. Iteratie I0 (intake en eval-set-bouw) begint daarna in de eigen architectuur (hoofdstuk 3) — geen Lovable-codebase als basis.

## 5.6 Checklist hoofdstuk 5

- [ ] Doel(en) van het prototype zijn expliciet en in aantal beperkt.
- [ ] Niet-doelen zijn expliciet — wat valt buiten scope van deze demo.
- [ ] Eén tool gekozen, met argumentatie en niet-gekozen-alternatieven.
- [ ] Demo-script bevat vraag-vooraf, happy path, één getoonde faalmodus, vraag-na.
- [ ] Het prototype kent een einddatum (intrekking na goedkeuringspoort of na I0-start).
- [ ] Geen scope-creep van prototype naar productie-codebase.

## 5.7 Literatuur (kerncitaten dit hoofdstuk)

- NxCode, *Vibe Design Tools 2026: Stitch vs v0 vs Lovable vs Bolt Compared* [23].
- NxCode, *Google Stitch vs v0 vs Lovable 2026* [24].
- Lenny's Newsletter, *A Guide to AI Prototyping for Product Managers* [25].

## 5.8 Status / laatste herziening

- Versie: 1.0
- Laatst bijgewerkt: 2026-04-28
- Wijzigingen sinds vorige versie: eerste vastlegging.
