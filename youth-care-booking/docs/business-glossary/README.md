# Business Glossary — Jeugdzorg met Verblijf

> Centrale, eenduidige definitie van alle begrippen in het dataplatform.
> Elk begrip wordt beschreven vanuit het perspectief van de jeugdige/het gezin.

## Richtlijnen

1. **Klantperspectief eerst** — Elk begrip begint met wat het betekent voor de jeugdige
2. **Bronvermelding** — Bij elk begrip staat de herkomst (wet, GGM, aanbieder, etc.)
3. **GGM-referentie** — Waar mogelijk wordt gekoppeld aan het Gemeentelijk Gegevensmodel
4. **Versioning** — Begrippen worden geversioned, wijzigingen worden bijgehouden

## Begrippen

### Verblijf

| Veld | Waarde |
|------|--------|
| **Definitie** | Een plek waar een jeugdige tijdelijk of langdurig woont in het kader van jeugdhulp |
| **Klantperspectief** | "De plek waar ik woon zolang ik extra hulp nodig heb" |
| **GGM-entiteit** | `Verblijf` → `JeugdhulpVerblijf` |
| **Bron** | Jeugdwet Art. 1.1 |
| **Synoniemen** | Residentieel verblijf, plaatsing, opname |
| **Data-elementen** | startdatum, einddatum, type_verblijf, instelling_id |

### Beschikbare Plek

| Veld | Waarde |
|------|--------|
| **Definitie** | Een niet-bezette verblijfsplek bij een aanbieder die direct of op korte termijn inzetbaar is |
| **Klantperspectief** | "Hier kan ik terecht als ik een plek nodig heb" |
| **GGM-entiteit** | Nog te mappen |
| **Bron** | Operationeel (aanbieders) |
| **Synoniemen** | Vrije plek, capaciteit, bed |
| **Data-elementen** | aanbieder_id, locatie_id, type_plek, beschikbaar_vanaf, leeftijdsgroep |

### Bezettingsgraad

| Veld | Waarde |
|------|--------|
| **Definitie** | Percentage van de totale capaciteit dat op een peildatum bezet is |
| **Klantperspectief** | "Hoe vol zit deze instelling — is er ruimte voor mij?" |
| **GGM-entiteit** | Nog te mappen |
| **Bron** | Berekend uit aanlevering |
| **Formule** | `(bezette_plekken / totale_capaciteit) × 100` |
| **Data-elementen** | peildatum, bezette_plekken, totale_capaciteit, percentage |

### Aanbieder

| Veld | Waarde |
|------|--------|
| **Definitie** | Organisatie die jeugdhulp met verblijf levert |
| **Klantperspectief** | "De organisatie die voor mij zorgt" |
| **GGM-entiteit** | `Aanbieder` → `Jeugdhulpaanbieder` |
| **Bron** | Jeugdwet, AGB-register |
| **Data-elementen** | agb_code, naam, kvk_nummer, regio, type_zorg[] |

### Wachtlijst

| Veld | Waarde |
|------|--------|
| **Definitie** | Lijst van jeugdigen die wachten op een verblijfsplek bij een specifieke aanbieder of in een regio |
| **Klantperspectief** | "Hoelang moet ik wachten voordat er plek is?" |
| **GGM-entiteit** | Nog te mappen |
| **Bron** | Operationeel (aanbieders) |
| **Data-elementen** | aantal_wachtenden, gemiddelde_wachttijd_dagen, urgentieniveau |

### Zorgprofiel

| Veld | Waarde |
|------|--------|
| **Definitie** | Beschrijving van het type zorg dat een jeugdige nodig heeft, gebruikt voor matching met beschikbare plekken |
| **Klantperspectief** | "Wat voor soort hulp heb ik nodig en wie kan dat bieden?" |
| **GGM-entiteit** | Nog te mappen |
| **Bron** | Verwijzing / indicatie |
| **Data-elementen** | zorgzwaarte, doelgroep, specialisatie[], leeftijdscategorie |

### Peildatum

| Veld | Waarde |
|------|--------|
| **Definitie** | De datum waarop de aangeleverde gegevens betrekking hebben |
| **Klantperspectief** | "De datum waarop deze informatie klopt" |
| **GGM-entiteit** | Standaard attribuut |
| **Bron** | Aanlevering |
| **Data-elementen** | datum, frequentie (dag/week/maand) |

### Regio

| Veld | Waarde |
|------|--------|
| **Definitie** | Samenwerkingsverband van gemeenten voor de inkoop en organisatie van jeugdhulp |
| **Klantperspectief** | "Het gebied waarin voor mij gezocht wordt naar een passende plek" |
| **GGM-entiteit** | `Regio` → `Jeugdhulpregio` |
| **Bron** | VNG Jeugdhulpregio-indeling |
| **Data-elementen** | regio_code, naam, gemeenten[], contactpersoon |

---

## Toevoegen van nieuwe begrippen

Gebruik het volgende template:

```markdown
### [Begrip]

| Veld | Waarde |
|------|--------|
| **Definitie** | [Formele definitie] |
| **Klantperspectief** | "[Wat betekent dit voor de jeugdige?]" |
| **GGM-entiteit** | [GGM mapping of 'Nog te mappen'] |
| **Bron** | [Wet, standaard, operationeel] |
| **Synoniemen** | [Alternatieve termen] |
| **Data-elementen** | [Relevante datavelden] |
```
