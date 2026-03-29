# Procesbeschrijvingen — Jeugdzorg met Verblijf

> Hoe passen verschillende partijen jeugdzorg met verblijf toe?
> Elke beschrijving wordt gekoppeld aan de business glossary en GGM-mapping.

## Klantperspectief

Voor een jeugdige en gezin is het proces van "hulp nodig hebben" tot "ergens
wonen waar je geholpen wordt" vaak ondoorzichtig. Deze procesbeschrijvingen
maken zichtbaar wat er achter de schermen gebeurt, zodat het platform de
juiste data op het juiste moment kan vastleggen.

---

## Proces 1: Aanmelding en Plaatsing (vanuit gemeente)

**Actoren:** Jeugdige/gezin, wijkteam, gemeente, aanbieder

### Stappen

```
Jeugdige/gezin meldt zich bij wijkteam
        ↓
Wijkteam stelt hulpvraag vast
  → Data: zorgprofiel, urgentie, leeftijd
        ↓
Wijkteam zoekt passende plek
  → Data: type_verblijf, regio, beschikbaarheid
        ↓
Gemeente geeft beschikking af
  → Data: verwijzing, product, startdatum
        ↓
Aanbieder bevestigt plaatsing
  → Data: bezetting +1, beschikbare_plek -1
        ↓
Jeugdige start verblijf
  → Data: startdatum_verblijf, locatie
```

### Data-elementen in dit proces

| Stap | Glossary-begrip | GGM-mapping |
|------|----------------|-------------|
| Hulpvraag | Zorgprofiel | Product.productCategorie |
| Zoeken plek | Beschikbare Plek | Verblijf.capaciteit |
| Beschikking | Verwijzing | Verwijzing |
| Plaatsing | Verblijf | JeugdhulpVerblijf |
| Bezetting update | Bezettingsgraad | Verblijf.bezettingsaantal |

---

## Proces 2: Periodieke Data-aanlevering (vanuit aanbieder)

**Actoren:** Aanbieder, third party verwerker, centraal platform

### Stappen

```
Aanbieder exporteert data uit eigen systeem
  → Formaat: CSV, API, of handmatig formulier
        ↓
Third party ontvangt aanlevering
  → Validatie: compleetheid, format, tijdigheid
        ↓
Data wordt gematched op GGM-mapping
  → Transformatie: bronvelden → standaardvelden
        ↓
Kwaliteitscheck door AI-agent
  → Beoordeling: afwijkingen, ontbrekende data, trends
        ↓
Anonimisering
  → Verwijder: namen, BSN, geboortedata → pseudoniemen
        ↓
Opslag in centraal datamodel
  → Beschikbaar voor dashboards
```

### Frequentie-opties

| Frequentie | Geschikt voor | Datapunten |
|------------|--------------|------------|
| **Dagelijks** | Beschikbaarheid, crisis | Vrije plekken, wachtlijst acute |
| **Wekelijks** | Bezetting, plaatsingen | Bezettingsgraad, in/uitstroom |
| **Maandelijks** | Financieel, trends | Totaalcijfers, kosten, kwaliteit |

---

## Proces 3: Dashboard-raadpleging (vanuit gemeente)

**Actoren:** Gemeente-medewerker, centraal platform

### Stappen

```
Medewerker opent dashboard
  → Authenticatie via gemeente-account
        ↓
Selecteert regio en filters
  → Filters: type_verblijf, leeftijd, zorgzwaarte
        ↓
Bekijkt beschikbare plekken
  → Anoniem: geen namen, wel aantallen per aanbieder
        ↓
Kiest passende aanbieder(s)
  → Contact opnemen buiten platform om
        ↓
(Optioneel) Plaatsingsverzoek via platform
  → Toekomstige functionaliteit
```

---

## Proces 4: Regionale Capaciteitsplanning

**Actoren:** Regio-coördinator, centraal platform, gemeenten

### Stappen

```
Regio-coördinator opent regionaal dashboard
        ↓
Overzicht capaciteit alle aanbieders in regio
  → Totale capaciteit, bezetting, vrije plekken
        ↓
Signalering knelpunten
  → Hoge bezetting (>90%), groeiende wachtlijsten
        ↓
Analyse trends
  → Maand-op-maand vergelijking, seizoenspatronen
        ↓
Rapportage aan bestuurlijk overleg
  → Geaggregeerde, geanonimiseerde data
```

---

## Template: Nieuwe Procesbeschrijving

```markdown
## Proces N: [Naam]

**Actoren:** [Lijst van betrokken partijen]

### Klantperspectief
[Wat betekent dit proces voor de jeugdige?]

### Stappen
[Flowchart in tekst met data-elementen per stap]

### Data-elementen
| Stap | Glossary-begrip | GGM-mapping |
|------|----------------|-------------|
| ... | ... | ... |

### Transcriptie-referentie
[Link naar bijbehorende transcriptie in docs/transcripties/]
```
