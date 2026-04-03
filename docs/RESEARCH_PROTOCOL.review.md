# Plan Review Log — RESEARCH_PROTOCOL

## Metadata
- **Plan:** docs/RESEARCH_PROTOCOL.md
- **Rondes:** 2
- **Datum ronde 1:** 2026-04-03
- **Datum ronde 2:** 2026-04-03
- **Eindstatus:** Goedgekeurd — klaar voor pilot-run

## Ronde 1

| # | Agent | Classificatie | Aandachtspunt | Beslissing |
|---|-------|---------------|---------------|------------|
| 1 | PM | must_address | Wekelijks research-proces start terwijl Fase 3 onaf is | Verwerkt: fasering + pilot-modus toegevoegd |
| 2 | CCR | must_address | Protocol is disproportioneel voor huidige schaal | Verwerkt: MVP-variant + maandelijkse cadans |
| 3 | CCR | must_address | Geen bewijs dat huidige content verouderd is | Bewust niet: content is aantoonbaar verouderd (bijv. Prompt Design: "Rol vastleggen" → "betekenis vastleggen") |
| 4 | SECADV+AVGADV | must_address | Bronarchief omzeilt sanitisatie- en PII-pipeline | Verwerkt: sanitisatie + PII-scan + blocked_authors check toegevoegd aan Stap 4 |
| 5 | AVGADV | must_address | Verwerkingsgrondslag en betrokkenenrechten niet geadresseerd | Verwerkt: §2b AVG-grondslag sectie toegevoegd |
| 6 | PM+CCR | must_address | Geen meetbare successcriteria | Verwerkt: successcriteria + stopcriteria + evaluatiemoment in §7 |
| 7 | FEAS | must_address | Exa crawling zonder maxCharacters limiet | Verwerkt: 50000 chars limiet + twee-staps fetch voor lange papers |
| 8 | ARCH+PM+FEAS | should_consider | Bronarchief dupliceert data ingestion pipeline | Verwerkt: staging-rol + triage naar knowledge graph beschreven |
| 9 | ARCH | should_consider | Full-text in git blaast repo op | Bewust niet: data bewaren is gewenst, 180MB acceptabel met opschoning |
| 10 | PM | should_consider | Faalscenario ontbreekt | Verwerkt: early exit na Stap 3 bij <2 bronnen |
| 11 | PM | should_consider | Capaciteitsaanname ontbreekt | Verwerkt: capaciteitsbudget tabel in §7 |
| 12 | AVGADV | should_consider | Geen bewaartermijn voor bronarchief | Verwerkt: 24 maanden + jaarlijkse opschoning |
| 13 | AVGADV | should_consider | Claim 'geen gebruikersdata' onvoldoende | Verwerkt: PII-erkenning in §2b |

### Beslissingen
- **Fasering toegevoegd:** protocol start als pilot (1-2 BB's), schaalt op naar MVP (maandelijks) na Fase 3, volledig schema pas na lancering
- **MVP-variant gedefinieerd:** 3 stappen i.p.v. 8, maandelijks i.p.v. wekelijks, ~30 min i.p.v. ~60 min
- **AVG-grondslag:** nieuw §2b met verwijzing naar DATA_GLOSSARY LIA, bewaartermijn 24m, Art. 21 procedure
- **Content is verouderd:** Robin bevestigt dat bijv. Prompt Design verouderde concepten bevat (rol vs. betekenis)

### Pre-flight synthese
3 van 6 agents beoordeelden negatief (PM: timing, SECADV: sanitisatie, CCR: proportionaliteit). Na verwerking zijn de kernbezwaren geadresseerd door fasering, MVP-variant en sanitisatiestap.

## Ronde 2

| # | Agent | Classificatie | Aandachtspunt | Beslissing |
|---|-------|---------------|---------------|------------|
| 1 | ARCH+SEC+FEAS+AVG | should_consider | PII-scan is LLM-instructie, niet fail-closed gate | Doorgeschoven: overwegen `make pii-check` CLI-command bij implementatie |
| 2 | CCR+PM | should_consider | MVP-variant niet als zelfstandig uitvoerbaar blok | Bewust niet: Robin kiest direct voor 8-staps test |
| 3 | FEAS | should_consider | Toolkeuze-tabel §8 inconsistent met maxCharacters-fix | Verwerkt: tabel bijgewerkt |
| 4 | FEAS | should_consider | Geen bootstrap-stap voor docs/research/ | Verwerkt: mappenstructuur + INDEX.md aangemaakt |
| 5 | AVGADV | should_consider | LIA dekt research-archiveringsdoel niet | Verwerkt: mini-LIA Art. 6(4) doelbindingstoets in §2b |
| 6 | AVGADV | should_consider | Exa/Firecrawl ontbreken in verwerkersregistratie | Doorgeschoven: bij DATA_GLOSSARY update |
| 7 | CCR | nice_to_have | Rotatieschema mist prioritering verandersnelheid | Bewust niet: eerst pilot, cadans evalueren daarna |
| 8 | PM | nice_to_have | Successcriterium '2 updates' niet gekalibreerd | Bewust niet: pilot dient als kalibratie |

### Beslissingen
- Robin kiest ervoor de volledige 8-staps pipeline direct te testen (niet MVP)
- PII-afdwingbaarheid via CLI-command wordt overwogen bij implementatie
- Verwerkersregistratie update naar DATA_GLOSSARY doorgeschoven

### Pre-flight synthese
4 van 6 agents positief (was 1/6 in ronde 1). Geen must-address items. Kernbezwaren uit ronde 1 adequaat verwerkt.

### Conclusie
Plan goedgekeurd. Geen openstaande must-address items. 2 punten doorgeschoven naar implementatie (PII CLI-command, verwerkersregistratie). Protocol klaar voor pilot-run.
