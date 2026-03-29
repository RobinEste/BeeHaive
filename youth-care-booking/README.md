# Jeugdzorg met Verblijf — Centraal Dataplatform

> "Booking.com voor jeugdzorg met verblijf" — actueel inzicht in beschikbaarheid,
> bezetting en capaciteit van jeugdzorginstellingen.

## Probleem

Gemeenten, regio's en het Rijk hebben geen actueel, gestandaardiseerd overzicht van:
- Waar plek is voor jeugdigen die verblijfszorg nodig hebben
- Hoeveel capaciteit er regionaal en landelijk beschikbaar is
- Hoe bezettingsgraad en wachtlijsten zich ontwikkelen

Aanbieders leveren data in verschillende formaten, op verschillende momenten,
aan verschillende partijen. Dit leidt tot vertraging, fouten en gebrek aan overzicht.

## Oplossing

Een centraal dataplatform waar:

1. **Aanbieders** periodiek (dag/week/maand) gestructureerde data aanleveren
2. **Een third party** de data verwerkt, valideert en anonimiseert
3. **Dashboards** actuele inzichten bieden aan drie doelgroepen:
   - **Gemeenten** — waar is plek voor een jeugdige?
   - **Regio's** — overzicht huisvesting en regionale capaciteit
   - **Centrale overheid** — actuele landelijke cijfers en trends

## Aanpak: Klein Beginnen

```
Fase 1: Eén regio (pilot)
  → 5-10 aanbieders, 1 gemeente, basisset datavelden
  → Validatie van het concept en de data-aanlevering

Fase 2: Regionale uitrol
  → Alle aanbieders in de pilotregio
  → Eerste dashboards voor gemeente en regio

Fase 3: Meerdere regio's
  → Mapping naar GGM (Gemeentelijk Gegevensmodel)
  → Landelijke dashboards

Fase 4: Landelijk
  → Alle regio's, volledige GGM-integratie
  → AI-agent voor datakwaliteit
```

## Kerncomponenten

| Component | Doel |
|-----------|------|
| [Business Glossary](docs/business-glossary/) | Eenduidige definitie van alle begrippen |
| [GGM Mapping](docs/mappings/) | Vertaling van brondata naar Gemeentelijk Gegevensmodel |
| [Procesbeschrijvingen](docs/process-descriptions/) | Hoe aanbieders jeugdzorg met verblijf toepassen |
| [Transcripties](docs/transcripties/) | Verhalen achter de processen |
| [AI Data Quality Agent](src/agents/) | Automatische beoordeling datakwaliteit |
| [Dashboards](src/dashboards/) | Visualisaties per doelgroep |

## Perspectiefprincipe

Alles wordt uitgewerkt vanuit het perspectief van de **klant** (de jeugdige en
het gezin). Elk begrip in de business glossary, elke mapping, elke AI-beoordeling
begint met de vraag: *"Wat betekent dit voor de jeugdige die zorg nodig heeft?"*

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
│   ├── business-glossary/    # Centrale begrippen en definities
│   ├── mappings/             # Brondata → GGM vertalingen
│   ├── process-descriptions/ # Procesbeschrijvingen per aanbieder
│   └── transcripties/        # Verhalen en context bij processen
├── src/
│   ├── api/                  # Data-aanlevering endpoints
│   ├── models/               # Datamodellen (Pydantic)
│   ├── services/             # Verwerking, anonimisering, validatie
│   ├── agents/               # AI agent voor datakwaliteit
│   └── dashboards/           # Dashboard configuraties
├── data/
│   ├── schemas/              # JSON Schema definities
│   └── examples/             # Voorbeelddata per aanbieder
└── config/                   # Configuratie per regio/aanbieder
```
