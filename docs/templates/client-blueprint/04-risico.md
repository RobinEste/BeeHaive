# Hoofdstuk 4 — Risico, compliance en ethiek

## 4.1 Waarom dit hoofdstuk

Compliance is geen nazorg-laag boven een afgebouwde architectuur; het is ontwerp-input. Risico-classificatie (EU AI Act-tier), ethische vereisten (HLEG/ALTAI), privacy-impact (DPIA) en technische dreigingen (OWASP LLM Top-10) raken alle hoofdstuk 3 (architectuur) en hoofdstuk 7 (governance). Dit hoofdstuk legt die invloed expliciet vast.

> *"In de overgrote meerderheid van gevallen zal het gebruik van AI een type verwerking betreffen dat waarschijnlijk een hoog risico inhoudt voor de rechten en vrijheden van individuen."*
> — UK ICO, GDPR-guidance op AI [18]

## 4.2 EU AI Act: vier tiers als eerste filter

### Wat hoort hier

De EU AI Act trad in werking op 1 augustus 2024; de meeste regels gelden vanaf 2 augustus 2026 [15]:

- **Tier 1, verboden**: sociale scoring, manipulatieve AI die menselijke vrije wil ondermijnt, realtime gezichtsherkenning in openbare ruimtes, emotieherkenning op de werkvloer.
- **Tier 2, hoog risico**: biometrie, kritieke infrastructuur, onderwijs (toelating, beoordeling, gedragsmonitoring), werkgelegenheid (werving, promotie, prestatiebeoordeling), essentiële diensten (krediet, uitkeringen, noodoproep-dispatching), ordehandhaving, migratie/grens, rechtspraak.
- **Tier 3, beperkt risico**: chatbots, deepfakes — transparantieverplichting naar gebruiker.
- **Tier 4, minimaal risico**: spamfilters, video-game-AI — grotendeels ongereguleerd.

**Acht design-verplichtingen voor Tier 2** [15]:

1. Risicomanagementsysteem gedurende de volledige levenscyclus.
2. Datagovernance (kwaliteit en representativiteit).
3. Technische documentatie voor compliance.
4. Automatische event-logging.
5. Gebruikersinstructies voor deployer-compliance.
6. Human oversight-mogelijkheden.
7. Nauwkeurigheids-, robuustheids- en cybersecurity-standaarden.
8. Kwaliteitsmanagementsysteem.

Tier 2 vraagt deze 8 verplichtingen als ontwerp-gates vóór architectuurfixatie.

### Voorbeeld — Hexant: Tier 4

**Tier 4, minimaal risico.** Argumentatie:

- Geen biometrie, krediet, uitkering, onderwijs, werving, ordehandhaving — Tier 2 valt af.
- Intern gebruik door eigen senior auditors; geen directe interactie tussen AI en de auditklant — Tier 3 niet van toepassing.
- Output gaat altijd langs een senior auditor vóór hij de audit-rapportage in kan; geen automatische beslissingen die rechtsgevolgen hebben voor de auditklant.

**Voorlopig.** Wordt opnieuw getoetst zodra de positionering verschuift naar outward-facing of game-changing (zie hoofdstuk 1).

### Template — invulblok

> [INVULLEN]
>
> **Tier**: 1 / 2 / 3 / 4
> **Argumentatie** (waarom deze tier, waarom de andere drie niet):
> - ...
>
> **Bij Tier 2** — vul alle 8 design-verplichtingen in als ontwerp-gates:
> 1. Risicomanagement: ...
> 2. Datagovernance: ...
> 3. Technische documentatie: ...
> 4. Event-logging: ...
> 5. Gebruikersinstructies: ...
> 6. Human oversight: ...
> 7. Nauwkeurigheid / robuustheid / cybersecurity: ...
> 8. Kwaliteitsmanagement: ...

## 4.3 HLEG en ALTAI: zeven ethische vereisten

### Wat hoort hier

De HLEG Ethics Guidelines for Trustworthy AI [16] benoemen zeven vereisten:

1. Human Agency and Oversight
2. Technical Robustness and Safety
3. Privacy and Data Governance
4. Transparency
5. Diversity, Non-discrimination and Fairness
6. Societal and Environmental Well-being
7. Accountability

De **ALTAI-checklist** [17] vertaalt deze naar een interactieve zelfbeoordeling — bruikbaar als gespreksleidraad. Per vereiste wordt vastgelegd of die op de use-case van toepassing is en, zo ja, hoe het ontwerp eraan voldoet.

### Voorbeeld — Hexant

| Vereiste | Status | Hoe ontwerp eraan voldoet |
|----------|--------|----------------------------|
| 1. Human Agency & Oversight | ✅ | Senior auditor reviewt elke score-suggestie; auditor kan elke score overschrijven met motivatie. |
| 2. Technical Robustness & Safety | ⚠ | Eval-set van inter-auditor-cases nodig; zie hoofdstuk 6. |
| 3. Privacy & Data Governance | ⚠ | Transcripten kunnen PII bevatten (interview-deelnemers); herbeoordeling DPIA in 4.4. |
| 4. Transparency | ✅ | Per score: inline citaties naar transcript-fragmenten; auditor ziet rubric-versie en model-versie. |
| 5. Diversity, Non-discrimination, Fairness | ✅ | Geen persoonsbeoordelingen; rubric is HLEG-gestoeld dus extern gevalideerd. |
| 6. Societal & Environmental Well-being | n.v.t. | — (operationele tool, geen maatschappelijke impact buiten Hexant en hun directe auditklanten). |
| 7. Accountability | ✅ | Senior auditor blijft eindverantwoordelijk voor scoring; logging van alle prompts en outputs. |

**ALTAI-doorloop:** gepland in iteratie I0, gefaciliteerd door AI-Comité Hexant.

### Template — invulblok

> [INVULLEN]
>
> | Vereiste | Status (✅ / ⚠ / n.v.t.) | Hoe ontwerp eraan voldoet (of waarom n.v.t.) |
> |----------|---------------------------|----------------------------------------------|
> | 1. Human Agency & Oversight | ... | ... |
> | 2. Technical Robustness & Safety | ... | ... |
> | 3. Privacy & Data Governance | ... | ... |
> | 4. Transparency | ... | ... |
> | 5. Diversity, Non-discrimination, Fairness | ... | ... |
> | 6. Societal & Environmental Well-being | ... | ... |
> | 7. Accountability | ... | ... |
>
> **ALTAI-doorloop**: wanneer / met wie / status.

## 4.4 DPIA en privacy-by-design

### Wat hoort hier

Voor AI-systemen is een Data Protection Impact Assessment (DPIA) onder de AVG in de meeste gevallen verplicht [18]. Default: ja, tenzij aantoonbaar niet van toepassing. Voor Tier 2-systemen vraagt de EU AI Act bovendien een Fundamental Rights Impact Assessment (FRIA); FRIA en DPIA overlappen maar zijn niet identiek — verschillende scope, toezichthouder en procedurele vereisten [19].

**Privacy-by-design-vragen:**

- Welke persoonsgegevens, voor welk doel, op welke rechtsgrondslag?
- DPIA vereist? (default: ja)
- Data-minimisatie: alleen verwerken wat noodzakelijk is?
- Welke rechten van betrokkenen zijn van toepassing (inzage, bezwaar, uitleg bij geautomatiseerde beslissingen)?
- Verwerkingsregister bijgewerkt?

### Voorbeeld — Hexant: DPIA herbeoordelen

**Status hoofdstuk 0:** voorlopig "niet vereist". **Status na deze pass:** **DPIA vereist** — herbeoordeling.

**Reden:** interview-transcripten bevatten persoonsgegevens van de interview-deelnemers (medewerkers van de auditklant): naam, functie, soms gevoelige meningen over collega's of leiderschap. Hoewel de scoring zelf geen persoonsbeoordeling is, vindt verwerking van persoonsgegevens plaats. Dat verschuift de DPIA-status van "niet vereist" naar "vereist, beperkt scope".

**Privacy-by-design-maatregelen:**

- *Doel:* uitsluitend HLEG-scoring ondersteunen; geen secundair gebruik (geen training, geen analyses op transcripten over audits heen).
- *Rechtsgrondslag:* gerechtvaardigd belang (auditkwaliteit) i.c.m. expliciete informatie aan interview-deelnemers vooraf.
- *Data-minimisatie:* transcripten worden per audit geïsoleerd opgeslagen; vector-store-tenancy per audit; verwijdering 90 dagen na audit-afsluiting (bewaartermijn-overeenkomst Hexant).
- *Rechten betrokkenen:* informatieverstrekking via standaard-interview-briefing; inzage- en bezwaarrechten via Hexant's privacy-officer.

**Wijziging op hoofdstuk 0:** de DPIA-status in de klantkaart wordt bijgewerkt naar *Vereist (beperkt scope)*.

### Template — invulblok

> [INVULLEN]
>
> **Persoonsgegevens verwerkt?** ja / nee — welke categorieën:
> **Doel**: ...
> **Rechtsgrondslag**: ...
> **DPIA-status na deze pass**: niet vereist / vereist (beperkt scope) / vereist (volledige) / herbeoordelen
> **Data-minimisatie-maatregelen**:
> - ...
> **Rechten betrokkenen**:
> - ...
> **Verwerkingsregister bijgewerkt?** ja / nee — datum:
>
> **Wijziging op hoofdstuk 0** (klantkaart, DPIA-status): ...

## 4.5 OWASP LLM Top-10 (2025)

### Wat hoort hier

OWASP publiceerde de Top-10 voor LLM Applications 2025 op 17 november 2024 [20]. Per dreiging wordt vastgelegd of die hier speelt en welke mitigatie in het ontwerp zit:

1. **LLM01 — Prompt Injection**
2. **LLM02 — Sensitive Information Disclosure**
3. **LLM03 — Supply Chain**
4. **LLM04 — Data and Model Poisoning**
5. **LLM05 — Improper Output Handling**
6. **LLM06 — Excessive Agency**
7. **LLM07 — System Prompt Leakage**
8. **LLM08 — Vector and Embedding Weaknesses**
9. **LLM09 — Misinformation**
10. **LLM10 — Unbounded Consumption**

Voor agentic systemen: ook OWASP Agentic AI Top-10 (late 2025) raadplegen.

### Voorbeeld — Hexant

| Dreiging | Speelt hier? | Mitigatie in ontwerp |
|----------|--------------|----------------------|
| LLM01 Prompt Injection | Ja, transcripten zijn user-input | Extractie-stap met strikte JSON-schema; system-prompt afgeschermd; geen vrije tool-aanroepen vanuit transcript-content. |
| LLM02 Sensitive Information Disclosure | Ja, PII in transcripten | Tenant-scoped retrieval per audit; geen output naar systemen buiten Hexant; bewaartermijn 90 dagen. |
| LLM03 Supply Chain | Ja, LLM-keuze raakt dit | AI BOM in hoofdstuk 7; alleen leveranciers met ISO 27001 of SOC 2 Type II. |
| LLM04 Data/Model Poisoning | Beperkt | RAG-corpus is intern beheerd; geen externe trainings-input. |
| LLM05 Improper Output Handling | Ja | Deterministische post-checks (rubric-conformiteit, evidence-aantallen, score-range). |
| LLM06 Excessive Agency | Beperkt — geen agent | MCP-servers read-only; geen schrijfrechten, geen e-mail. |
| LLM07 System Prompt Leakage | Ja | System-prompt versioneerd in repo; niet weergegeven aan eindgebruiker; getest tegen prompt-leakage. |
| LLM08 Vector/Embedding | Ja | Vector-index achter dezelfde authenticatie als overige systemen; geen open endpoints. |
| LLM09 Misinformation | Ja | Bron-attributie verplicht in elke output; senior auditor ziet welke transcript-fragmenten gebruikt zijn. |
| LLM10 Unbounded Consumption | Ja | Token-budget per audit; rate-limiting op MCP-servers. |

**Agentic OWASP**: niet van toepassing (geen agent in v1).

### Template — invulblok

> [INVULLEN]
>
> | Dreiging | Speelt hier? | Mitigatie in ontwerp |
> |----------|--------------|----------------------|
> | LLM01 Prompt Injection | ja / beperkt / nee | ... |
> | LLM02 Sensitive Information Disclosure | ... | ... |
> | LLM03 Supply Chain | ... | ... |
> | LLM04 Data/Model Poisoning | ... | ... |
> | LLM05 Improper Output Handling | ... | ... |
> | LLM06 Excessive Agency | ... | ... |
> | LLM07 System Prompt Leakage | ... | ... |
> | LLM08 Vector/Embedding | ... | ... |
> | LLM09 Misinformation | ... | ... |
> | LLM10 Unbounded Consumption | ... | ... |
>
> **Agentic OWASP** van toepassing? ja/nee — bij ja: ...

## 4.6 Guardrails-by-design

### Wat hoort hier

Verdediging in de diepte: input-filtering, gedragsconstrainering (rol-instructies, taakbeperking), output-validatie met deterministische code, privilege-scheiding (least privilege voor agents en tools), monitoring en logging. Geen afterthought; ontwerpparameter dat hoofdstuk 3 (architectuur) kan terugraken.

### Voorbeeld — Hexant

- *Input:* schema-validatie op extractie-output; transcripten doorlopen een PII-flag-stap (markering, geen verwijdering — auditor ziet de markering).
- *Gedrag:* system-prompt staat alleen evidence-classificatie en scoring-voorstel toe; expliciet *geen* aanbevelingen aan de auditklant, geen oordelen over personen.
- *Output:* deterministische post-checks (zie 4.5); bij gefaalde validatie wordt scoring-suggestie geblokkeerd en de auditor scoort handmatig.
- *Privilege-scheiding:* MCP-servers read-only; geen tools die buiten de tenant kunnen.
- *Logging:* alle prompts, retrievals en outputs vastgelegd inclusief gebruiker-ID; bewaartermijn 12 maanden voor audit-trail.

### Template — invulblok

> [INVULLEN]
>
> - **Input-filtering**: ...
> - **Gedragsconstrainering**: ...
> - **Output-validatie**: ...
> - **Privilege-scheiding**: ...
> - **Monitoring & logging**: ...
> - **Bewaartermijn logs**: ...

## 4.7 Cross-cutting check: hoofdstuk 4 ↔ hoofdstuk 3

Na deze risico-pass wordt hoofdstuk 3 heroverwogen. Wijzigingen op de architectuur — tenant-scoping, extra validatie-stap, residency-eis op modelkeuze — staan hier en worden naar 3 teruggekoppeld.

**Voor Hexant**: één aanpassing op hoofdstuk 3 — *vector-index per audit-tenant* werd in 3.3 al geanticipeerd, maar wordt hier hard ontwerp-vereist gemaakt vanwege LLM02. Geen andere wijzigingen.

## 4.8 Checklist hoofdstuk 4

- [ ] EU AI Act-tier expliciet bepaald met argumentatie.
- [ ] Bij Tier 2: alle 8 design-verplichtingen afzonderlijk ingevuld als ontwerp-gates.
- [ ] Alle 7 HLEG-vereisten doorlopen — "n.v.t." mag, mits onderbouwd.
- [ ] DPIA-trigger getoetst; expliciete uitkomst (vereist / niet vereist + reden).
- [ ] Data Protection Officer / privacy-officer heeft de privacy-paragraaf gezien en geaccordeerd.
- [ ] OWASP LLM Top-10: per dreiging "speelt hier" of "speelt niet", en bij "speelt" een mitigatie.
- [ ] Agentic OWASP overwogen indien agent in scope.
- [ ] Guardrails-by-design vertaald naar concrete maatregelen — niet als principe.
- [ ] Hoofdstuk 3 heroverwogen na deze risk-pass; wijzigingen vermeld.
- [ ] Hoofdstuk 0 (klantkaart) bijgewerkt indien tier of DPIA-status verschoof.

## 4.9 Literatuur (kerncitaten dit hoofdstuk)

- EU AI Act, *High-Level Summary* [15].
- European Commission, *Ethics Guidelines for Trustworthy AI (HLEG)* [16].
- ALTAI, *Assessment List for Trustworthy AI* [17].
- UK ICO, *Accountability and governance implications of AI* [18].
- TechGDPR, *Data protection digest: AI Act and GDPR study* [19].
- OWASP, *Top 10 for LLM Applications 2025* [20].

## 4.10 Status / laatste herziening

- Versie: 1.0
- Laatst bijgewerkt: 2026-04-28
- Wijzigingen sinds vorige versie: eerste vastlegging.
