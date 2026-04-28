# Bijlage A — Eindchecklist (goedkeuringspoort)

## A.1 Waarom deze bijlage

Deze bijlage bundelt de checklists uit hoofdstukken 0-8 in één overzicht voor de goedkeuringspoort (zie 7.5). Bedoeld voor de twee handtekenende rollen — AI-Comité (collectief) en waarde-stroom-eigenaar (individueel) — om in één pagina te kunnen toetsen of de blueprint compleet en consistent is. De bijlage is geen vervanging van de hoofdstuk-checklists; hij is een convergentie-instrument.

**Gebruik**: per regel afvinken; bij "n.v.t." een korte motivatie noteren in de marge of in een begeleidende notitie. Niet-afvinken = niet door de poort.

## A.2 Hoofdstuk 0 — Klant- en projectkaart

- [ ] Waarde-stroom in scope is end-to-end (trigger naar uitkomst), niet een afdeling of tool.
- [ ] Waarde-stroom-eigenaar benoemd, met afdelings-overschrijdend mandaat.
- [ ] Eindgebruiker en stakeholder van de uitkomst beide expliciet benoemd.
- [ ] Drie kerncijfers kwantificeerbaar en gekoppeld aan bestaand prestatie-meetinstrument.
- [ ] EU AI Act-tier en DPIA-status voorlopig aangegeven, met noot over herbeoordeling in hoofdstuk 4.

## A.3 Hoofdstuk 1 — Strategische verankering en waarde-stroom

- [ ] AI-ambitie expliciet gepositioneerd op Gartner Opportunity Radar (twee assen).
- [ ] Drie consequenties van die positionering benoemd (risico-bereidheid, EU AI Act-tier, tijdslijn).
- [ ] Waarde-stroom-definitie gekozen (Obeidat / Appelo-unFIX) met argumentatie.
- [ ] Waarde-stroom als één-regel-map vastgelegd.
- [ ] Eén-noord-ster-KPI benoemd, kwantificeerbaar, gekoppeld aan bestaande meting.
- [ ] Alle betrokken afdelingen genoemd, ook indirecte.
- [ ] Vastgesteld in welke fase AI-interventie hoort, op basis van meting (geen aanname).
- [ ] Toets uitgevoerd of waarde-stroom-lens primair of secundair is.

## A.4 Hoofdstuk 2 — Use-case-discovery in zeven stappen

- [ ] Stap 1: waarde-stroom-map uit hoofdstuk 1 als vertrekpunt.
- [ ] Stap 2: TRACE-diagnose op één werkstroom; frictie kwantitatief per stap.
- [ ] Stap 2: *"Never optimize a step that shouldn't exist"*-toets uitgevoerd.
- [ ] Stap 3: probleem geformuleerd als huidige toestand + pijn + gekwantificeerde impact + wie.
- [ ] Stap 4: primaire AI-Value-Objective(s) gekozen, met trade-offs benoemd.
- [ ] Stap 5: AI Solution Canvas (5 velden) volledig.
- [ ] Stap 6: Feasibility Check (data-status én tech-status met *ready / needs prep / not feasible*).
- [ ] Stap 7: Impact Estimation Canvas op vier dimensies.
- [ ] AI-BMC overwogen; wel/niet ingevuld met motivatie.
- [ ] Drie filters: alle drie afzonderlijk doorlopen; AI-3P-score numeriek.
- [ ] Bij AI-3P < 60: actieplan eerst, geen bouw.
- [ ] Niet-AI-knelpunten uit dezelfde waarde-stroom expliciet "niet in scope".

## A.5 Hoofdstuk 3 — Architectuur en technische ontwerpkeuzes

- [ ] Workflow- of agent-keuze expliciet, met argumentatie.
- [ ] Gekozen patroon herleidbaar naar Anthropic's vijf.
- [ ] Multi-agent: niet gekozen, tenzij alle drie criteria getoetst en 15×-tokenkost expliciet aanvaard.
- [ ] Architectuurlaag (RAG / fine-tuning / agents) onderbouwd; niet-gekozen lagen expliciet vermeld.
- [ ] Tools-tabel (MCP) met protocol, rechten, doel per integratie.
- [ ] Begin-simpel-regel zichtbaar gevolgd: bewijs voor elke complexiteits-stap.
- [ ] Drie kerneigenschappen (eenvoud, transparantie, tool-interface) zijn ontwerp-input.

## A.6 Hoofdstuk 4 — Risico, compliance en ethiek

- [ ] EU AI Act-tier expliciet bepaald met argumentatie.
- [ ] Bij Tier 2: alle 8 design-verplichtingen ingevuld als ontwerp-gates.
- [ ] Alle 7 HLEG-vereisten doorlopen, "n.v.t." onderbouwd.
- [ ] DPIA-trigger getoetst; expliciete uitkomst (vereist / niet vereist + reden).
- [ ] Privacy-officer heeft privacy-paragraaf gezien en geaccordeerd.
- [ ] OWASP LLM Top-10: per dreiging mitigatie of "speelt niet".
- [ ] Agentic OWASP overwogen indien agent in scope.
- [ ] Guardrails-by-design vertaald naar concrete maatregelen.
- [ ] Hoofdstuk 3 heroverwogen na risk-pass; wijzigingen vermeld.
- [ ] Hoofdstuk 0 bijgewerkt indien tier of DPIA-status verschoof.

## A.7 Hoofdstuk 5 — Prototype als gespreksanker

- [ ] Doel(en) van het prototype expliciet en in aantal beperkt.
- [ ] Niet-doelen expliciet — wat valt buiten scope van de demo.
- [ ] Eén tool gekozen, met argumentatie en niet-gekozen-alternatieven.
- [ ] Demo-script: vraag-vooraf, happy path, één getoonde faalmodus, vraag-na.
- [ ] Het prototype kent een einddatum (intrekking na goedkeuringspoort of I0-start).
- [ ] Geen scope-creep van prototype naar productie-codebase.

## A.8 Hoofdstuk 6 — Iteratieve werkwijze en FDE-principes

- [ ] Werkwijze gekozen (FDE-principes / klassieke discovery / hybride) met argumentatie.
- [ ] Drie expliciete hypotheses geformuleerd; in I0 getoetst.
- [ ] Iteraties I0 t/m In benoemd, met doel + scope + kwantitatief criterium + beslismoment.
- [ ] "Stoppen als uitkomst" is legitiem in minstens één iteratie.
- [ ] Eval-set bestaat in I0; samenstelling, eigenaarschap, versionering vastgelegd.
- [ ] Eval-set representatief — geen happy-path-only, geen ontwikkelaars-only.
- [ ] Doorlooptijd iteraties consistent met hoofdstuk 0 en hoofdstuk 7.
- [ ] Pilot expliciet als experiment gefaamd, niet als product.

## A.9 Hoofdstuk 7 — Governance, goedkeuring en Nederlandse context

- [ ] AI-Comité samenstelling vastgelegd; alle zes minimale rollen vertegenwoordigd.
- [ ] Vergader-cadans en accordering-mandaat expliciet.
- [ ] AI BOM-template gedefinieerd.
- [ ] AI BOM van eerste leverancier opgevraagd.
- [ ] NL AIC-toets uitgevoerd; bij van toepassing: werkgroep / richtlijn benoemd.
- [ ] PACE-aanpak overwogen; concretisering bij van toepassing.
- [ ] Goedkeuringspoort-criteria meetbaar en kwantitatief.
- [ ] Pad bij niet halen van een criterium expliciet.
- [ ] Twee handtekeningen-eis gehandhaafd (AI-Comité collectief + waarde-stroom-eigenaar).

## A.10 Hoofdstuk 8 — Cross-bouwsteen-overzicht

- [ ] Per BB (01, 03-07) is concreet benoemd welke input vanuit BB_02 doorwerkt.
- [ ] Per BB is een eigenaar benoemd; geen lege "TBD"-velden.
- [ ] Cross-cutting overzicht-tabel volledig ingevuld.
- [ ] Inconsistenties tussen hoofdstukken weggewerkt.
- [ ] Cross-cutting checks (uit 3, 4, 6, 7) zijn niet in conflict met cross-bouwsteen-overzicht.

## A.11 Goedkeurings-handtekening

> | Rol | Naam | Datum | Handtekening |
> |-----|------|-------|--------------|
> | AI-Comité (collectief, namens) | ... | ... | ... |
> | Waarde-stroom-eigenaar (individueel) | ... | ... | ... |
>
> **Bij niet-doorgang van de poort**:
> - Welke regels niet afgevinkt: ...
> - Vervolg-pad (volgende iteratie / pauzeren / stoppen): ...
> - Hervatting-criteria: ...

## A.12 Status / laatste herziening

- Versie: 1.0
- Laatst bijgewerkt: 2026-04-28
- Wijzigingen sinds vorige versie: eerste vastlegging.
