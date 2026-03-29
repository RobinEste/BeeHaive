# Noordje op weg naar thuis — Dataplatform

> Inzicht in plaatsingen, beschikbaarheid en capaciteit van jeugdzorg met verblijf
> in Noord-Holland. Van pilot Haarlemmermeer naar landelijke uitrol.

## Context

Het kabinet werkt aan de **Hervormingsagenda Jeugd** met als doel de afbouw van
gesloten jeugdzorg (JeugdzorgPlus) en de opbouw van kleinschalige alternatieven.
Doelstelling: **nul gesloten plaatsingen in 2030**.

In Noord-Holland werken partijen samen onder het programma **"Thuis voor Noordje" (TvN)**:
- **BORN** — Bovenregionaal Netwerk van samenwerkende jeugdregio's in NH
- **BEN NH** — Bovenregionaal Expertise Netwerk Jeugd Noord-Holland
- **Gemeente Amsterdam** — coördinerende gemeente voor de SPUK-regeling

De middelen komen uit de regeling *'Specifieke uitkering transformatie gesloten
jeugdhulp'* en worden ingezet voor:
1. Afbouw gesloten jeugdhulp (sluiting/gedeeltelijke sluiting)
2. Ombouw naar kleinschalige gesloten jeugdhulp
3. Ontwikkeling alternatieven voor gesloten jeugdhulp

## Probleem

Om de transformatie te monitoren en bij te sturen ontbreekt **betrouwbare,
geïntegreerde data**. Data zit verspreid over gemeenten, aanbieders, CBS,
berichtenverkeer (iJw/iWmo), CORV en DUO. Formaten, definities en frequenties
verschillen. Er is geen 0-situatie vastgesteld.

## Oplossing

Een centraal dataplatform (dashboard) dat data uit verschillende bronnen
samenbrengt op lokaal, regionaal en nationaal niveau.

### Te monitoren hoofddoel

> Jeugdigen niet meer gesloten plaatsen, niet meer buiten de provinciegrens,
> maar zo dicht mogelijk bij thuis en bij school.

### Informatiebehoefte (drie prioriteiten)

| Prio | Domein | Kernvragen |
|------|--------|------------|
| **1** | Overzicht plaatsingen | Aanmeldingen, type maatregel, type plaatsing, zorgverlener, locatie, beschikbaarheid, in/uitstroom, duur, verwijzer, woonplaats |
| **2** | Voorspellende factoren | Voorgeschiedenis, thuiszitters, justitiecontact, vechtscheidingen |
| **3** | Effectiviteit behandeling | Stapeling trajecten, duur, zorgverlener |

Zie [docs/informatiebehoefte/](docs/informatiebehoefte/) voor de volledige uitwerking.

## Aanpak: Klein Beginnen

```
Fase 1: Pilot Haarlemmermeer (Q1-Q2 2025)
  → Eerste gemeente, basisset datavelden
  → 0-situatie vaststellen
  → DPIA + verwerkersovereenkomsten

Fase 2: Noord-Holland (Q3-Q4 2025)
  → Alle NH-gemeenten aanhaken
  → Dashboards voor gemeente, regio, TvN

Fase 3: Landelijk (2026+)
  → Afstemming met landelijk ondersteuningsteam
  → Uitrol naar andere bovenregionale samenwerkingsverbanden
```

## Resultaten

| Resultaat | Deadline |
|-----------|----------|
| 0-situatie | Jan 2025 |
| Analyse informatiebehoefte | Jan 2025 |
| Analyse beschikbare databronnen | Jan-Feb 2025 |
| Verwerkersovereenkomsten + CBS microdata | Jan-Mrt 2025 |
| Datawarehouse (architectuur, ETL, kwaliteit, beveiliging) | Apr 2025 |
| Data governance | Apr 2025 |
| Data-analyse | Apr 2025 |
| Metadata register | Mei 2025 |
| Dashboard + releasenotes | Mei 2025 |
| Handleiding | Mei 2025 |
| Publicatie in community | Mei-Jun 2025 |

## Doelstellingen

1. Antwoord geven op de informatiebehoefte van TvN en het project "Afbouw JeugdzorgPlus 2024-2028"
2. Resultaat **herbruikbaar** maken voor alle andere bovenregionale samenwerkingsverbanden
3. Community iWMO en iJW versterken en uitbreiden

## Kerncomponenten

| Component | Doel |
|-----------|------|
| [Informatiebehoefte](docs/informatiebehoefte/) | Uitwerking per subdoel en prioriteit |
| [Business Glossary](docs/business-glossary/) | Eenduidige definitie van alle begrippen |
| [Databronnen](docs/databronnen/) | Overzicht CBS, iJw/iWmo, CORV, DUO, aanbieders, gemeenten |
| [GGM Mapping](docs/mappings/) | Vertaling van brondata naar Gemeentelijk Gegevensmodel |
| [Procesbeschrijvingen](docs/process-descriptions/) | Hoe partijen jeugdzorg met verblijf toepassen |
| [Transcripties](docs/transcripties/) | Verhalen achter de processen |
| [AI Data Quality Agent](src/agents/) | Automatische beoordeling datakwaliteit |
| [Dashboards](src/dashboards/) | Visualisaties per doelgroep |

## Perspectiefprincipe

Alles wordt uitgewerkt vanuit het perspectief van de **jeugdige en het gezin**.
Elk begrip in de business glossary, elke mapping, elke AI-beoordeling begint
met de vraag: *"Wat betekent dit voor de jongere die zorg nodig heeft?"*

## Betrokkenen

| Naam | Organisatie |
|------|------------|
| Chantal van Liefland | Projectgroep |
| Bente Bontefaas | Projectgroep |
| Arjen Roek | Projectgroep |
| Jan-Luuk de Groot | Projectgroep |
| Joost Broumels | Projectgroep |
| Robin Bertus | Projectgroep |

**Betrokken partijen:** Gemeenten, zorgaanbieders, onderwijs, gecertificeerde
instellingen (GI's), BEN/RET, Ketenbureau, CBS, DUO, J&V/DJI, VNG.

## Tech Stack

| Component | Technologie |
|-----------|------------|
| API | Python FastAPI |
| Database | PostgreSQL |
| Dashboards | Apache Superset / Metabase |
| Data validatie | Great Expectations / Pydantic |
| AI Agent | Claude API |
| Anonimisering | ARX / custom pipeline |
| Hosting | Hetzner (EU, AVG-compliant) |

## Projectstructuur

```
youth-care-booking/
├── README.md
├── docs/
│   ├── informatiebehoefte/   # Uitwerking per subdoel en prioriteit
│   ├── databronnen/          # Overzicht en analyse per databron
│   ├── business-glossary/    # Centrale begrippen en definities
│   ├── mappings/             # Brondata → GGM vertalingen
│   ├── process-descriptions/ # Procesbeschrijvingen per partij
│   └── transcripties/        # Verhalen en context bij processen
├── src/
│   ├── api/                  # Data-aanlevering endpoints
│   ├── models/               # Datamodellen (Pydantic)
│   ├── services/             # Verwerking, anonimisering, validatie
│   ├── agents/               # AI agent voor datakwaliteit
│   └── dashboards/           # Dashboard configuraties
├── data/
│   ├── schemas/              # JSON Schema definities
│   └── examples/             # Voorbeelddata per bron
└── config/                   # Configuratie per regio/gemeente
```
