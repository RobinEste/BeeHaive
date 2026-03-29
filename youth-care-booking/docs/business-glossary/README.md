# Business Glossary — Noordje op weg naar thuis

> Centrale, eenduidige definitie van alle begrippen in het dataplatform.
> Elk begrip wordt beschreven vanuit het perspectief van de jeugdige/het gezin.

## Richtlijnen

1. **Klantperspectief eerst** — Elk begrip begint met wat het betekent voor de jongere
2. **Bronvermelding** — Bij elk begrip staat de herkomst (wet, GGM, aanbieder, etc.)
3. **GGM-referentie** — Waar mogelijk wordt gekoppeld aan het Gemeentelijk Gegevensmodel
4. **Versioning** — Begrippen worden geversioned, wijzigingen worden bijgehouden

---

## Programma en Organisatie

### Thuis voor Noordje (TvN)

| Veld | Waarde |
|------|--------|
| **Definitie** | Bovenregionaal programma in Noord-Holland gericht op de transformatie van gesloten jeugdzorg naar kleinschalige alternatieven |
| **Klantperspectief** | "Het programma dat ervoor zorgt dat ik dicht bij huis kan wonen en niet in een gesloten instelling hoef" |
| **Bron** | Samenwerkingsovereenkomst NH |
| **Gerelateerd** | BORN, BEN NH, Hervormingsagenda Jeugd |

### BORN

| Veld | Waarde |
|------|--------|
| **Definitie** | Bovenregionaal Netwerk van samenwerkende jeugdregio's in Noord-Holland |
| **Klantperspectief** | "De samenwerking tussen gemeenten in mijn provincie die ervoor zorgt dat er overal goede hulp is" |
| **Bron** | Samenwerkingsverband NH |

### BEN NH

| Veld | Waarde |
|------|--------|
| **Definitie** | Bovenregionaal Expertise Netwerk Jeugd Noord-Holland — advies- en ondersteuningsnetwerk voor complexe jeugdhulpvragen |
| **Klantperspectief** | "Het expertteam dat meedenkt als mijn situatie ingewikkeld is" |
| **Bron** | Landelijk: RET (Regionaal Expertise Team) |

### Gecertificeerde Instelling (GI)

| Veld | Waarde |
|------|--------|
| **Definitie** | Organisatie die door de overheid gecertificeerd is om kinderbeschermingsmaatregelen en jeugdreclassering uit te voeren |
| **Klantperspectief** | "De organisatie die betrokken is als de rechter een maatregel heeft opgelegd" |
| **GGM-entiteit** | `GecertificeerdeInstelling` |
| **Bron** | Jeugdwet Art. 3.2 |
| **Synoniemen** | Voogdijinstelling, jeugdbeschermingsorganisatie |

---

## Plaatsingen en Verblijf

### Plaatsing

| Veld | Waarde |
|------|--------|
| **Definitie** | Het toewijzen en huisvesten van een jeugdige bij een zorgaanbieder voor verblijfszorg |
| **Klantperspectief** | "De beslissing waar ik ga wonen voor mijn hulp" |
| **GGM-entiteit** | `Plaatsing` → `JeugdhulpPlaatsing` |
| **Bron** | Jeugdwet |
| **Data-elementen** | type_plaatsing, startdatum, einddatum, aanbieder_id, locatie_id, maatregel |

### Type Plaatsing

| Veld | Waarde |
|------|--------|
| **Definitie** | Classificatie van een plaatsing naar aanleiding en karakter |
| **Klantperspectief** | "Is dit mijn eerste plek, of word ik overgeplaatst?" |
| **Waarden** | Nieuw / Hernieuwd / Overplaatsing / Spoed / Regulier |
| **Bron** | Aanbieders, iJw berichtenverkeer |

### Maatregel

| Veld | Waarde |
|------|--------|
| **Definitie** | Juridische grondslag voor de jeugdhulp |
| **Klantperspectief** | "Op welke basis ben ik hier — vrijwillig of verplicht?" |
| **GGM-entiteit** | `Maatregel` |
| **Bron** | CORV, GI's |
| **Waarden** | Vrijwillig / Beschermingsmaatregel (OTS, voogdij) / Jeugdreclasseringsmaatregel |
| **Data-elementen** | type_maatregel, startdatum, einddatum, verwijzer |

### Gesloten Jeugdhulp (JeugdzorgPlus)

| Veld | Waarde |
|------|--------|
| **Definitie** | Verblijf in een gesloten accommodatie op basis van een machtiging van de kinderrechter, voor jeugdigen die zich anders onttrekken aan de noodzakelijke hulp |
| **Klantperspectief** | "Een plek waar de deur op slot zit — het doel is dat dit niet meer nodig is" |
| **GGM-entiteit** | `GeslotenJeugdhulp` |
| **Bron** | Jeugdwet Hoofdstuk 6 |
| **Synoniemen** | JeugdzorgPlus, gesloten plaatsing, JJI (deels) |
| **Data-elementen** | machtiging_datum, machtiging_duur, locatie_id |

### Kleinschalige Woonvorm

| Veld | Waarde |
|------|--------|
| **Definitie** | Alternatief voor grootschalige (gesloten) jeugdhulpaccommodaties; een woonvorm met een beperkt aantal plekken in een huiselijke setting |
| **Klantperspectief** | "Een kleiner huis waar ik meer persoonlijke aandacht krijg" |
| **Bron** | Hervormingsagenda Jeugd, TvN |
| **Synoniemen** | Kleinschalige voorziening, woongroep |
| **Data-elementen** | capaciteit (typisch 4-8), type, locatie |

### Verblijf

| Veld | Waarde |
|------|--------|
| **Definitie** | Een plek waar een jeugdige tijdelijk of langdurig woont in het kader van jeugdhulp |
| **Klantperspectief** | "De plek waar ik woon zolang ik extra hulp nodig heb" |
| **GGM-entiteit** | `Verblijf` → `JeugdhulpVerblijf` |
| **Bron** | Jeugdwet Art. 1.1 |
| **Synoniemen** | Residentieel verblijf, opname |
| **Data-elementen** | startdatum, einddatum, type_verblijf, instelling_id, duur |

### Type Verblijf

| Veld | Waarde |
|------|--------|
| **Definitie** | Classificatie van de verblijfsvorm |
| **Klantperspectief** | "Wat voor soort plek is dit?" |
| **Waarden** | Pleegzorg (PLG) / Gezinshuis (GZH) / Residentieel (RES) / Gesloten (GJJ) / Crisisopvang (CRS) / Kamertraining (KTW) |
| **Bron** | iJw productcodes |

---

## Capaciteit en Beschikbaarheid

### Beschikbare Plek

| Veld | Waarde |
|------|--------|
| **Definitie** | Een niet-bezette verblijfsplek bij een aanbieder die direct of op korte termijn inzetbaar is |
| **Klantperspectief** | "Hier kan ik terecht als ik een plek nodig heb" |
| **GGM-entiteit** | Nog te mappen |
| **Bron** | Operationeel (aanbieders) |
| **Data-elementen** | aanbieder_id, locatie_id, type_plek, beschikbaar_vanaf, leeftijdsgroep |

### Bezettingsgraad

| Veld | Waarde |
|------|--------|
| **Definitie** | Percentage van de totale capaciteit dat op een peildatum bezet is |
| **Klantperspectief** | "Hoe vol zit deze instelling — is er ruimte voor mij?" |
| **Formule** | `(bezette_plekken / totale_capaciteit) × 100` |
| **Data-elementen** | peildatum, bezette_plekken, totale_capaciteit, percentage |

### Instroom / Uitstroom

| Veld | Waarde |
|------|--------|
| **Definitie** | Aantal jeugdigen dat in een periode start (instroom) of stopt (uitstroom) met verblijf |
| **Klantperspectief** | "Hoeveel jongeren komen en gaan — wordt er plek vrij?" |
| **Bron** | iJw berichtenverkeer, aanbieders |
| **Data-elementen** | instroom_aantal, uitstroom_aantal, periode, type_verblijf |

### Wachtlijst

| Veld | Waarde |
|------|--------|
| **Definitie** | Lijst van jeugdigen die wachten op een verblijfsplek |
| **Klantperspectief** | "Hoelang moet ik wachten voordat er plek is?" |
| **Bron** | Operationeel (aanbieders) |
| **Let op** | Uit transcripties blijkt dat wachtlijsten vaak informeel en onvolledig zijn |
| **Data-elementen** | aantal_wachtenden, gemiddelde_wachttijd_dagen, urgentieniveau |

---

## Verwijzing en Traject

### Verwijzer

| Veld | Waarde |
|------|--------|
| **Definitie** | Persoon of instantie die een jeugdige verwijst naar jeugdhulp met verblijf |
| **Klantperspectief** | "Wie heeft besloten dat ik hier hulp krijg?" |
| **GGM-entiteit** | `Verwijzing.verwijzer` |
| **Bron** | iJw, CORV |
| **Waarden** | Huisarts / Wijkteam / GI / Kinderrechter / Jeugdreclassering |

### Voorgeschiedenis (Stapeling)

| Veld | Waarde |
|------|--------|
| **Definitie** | Overzicht van eerdere jeugdhulptrajecten die een jongere heeft doorlopen |
| **Klantperspectief** | "Ik heb al op veel plekken gewoond — zien ze dat ook?" |
| **Bron** | iJw historisch, aanbieders |
| **Data-elementen** | trajecten[], aanbieders[], periodes[], type_zorg[] |
| **Let op** | Hoge stapeling is indicator voor complexe problematiek |

### Zorgprofiel

| Veld | Waarde |
|------|--------|
| **Definitie** | Beschrijving van het type zorg dat een jeugdige nodig heeft |
| **Klantperspectief** | "Wat voor soort hulp heb ik nodig en wie kan dat bieden?" |
| **Bron** | Verwijzing / indicatie |
| **Data-elementen** | zorgzwaarte, doelgroep, specialisatie[], leeftijdscategorie |

---

## Databronnen

### iJw (iJeugdwet) Berichtenverkeer

| Veld | Waarde |
|------|--------|
| **Definitie** | Gestandaardiseerd digitaal berichtenverkeer tussen gemeenten en jeugdhulpaanbieders over toewijzingen, start/stop zorg en declaraties |
| **Klantperspectief** | "De digitale berichten die ervoor zorgen dat mijn hulp geregeld en betaald wordt" |
| **Bron** | VNG/Ketenbureau i-Sociaal Domein |
| **Bevat** | Toewijzingen, start/stop berichten, declaraties, productcodes |

### CORV

| Veld | Waarde |
|------|--------|
| **Definitie** | Collectieve Opdracht Routeervoorziening — digitale voorziening voor berichtenverkeer in de justitiële jeugdketen |
| **Klantperspectief** | "Het systeem dat informatie deelt als de rechter of reclassering betrokken is" |
| **Bron** | Justitie en Veiligheid |
| **Bevat** | Maatregelen, verzoeken machtiging gesloten jeugdhulp |

### CBS Microdata

| Veld | Waarde |
|------|--------|
| **Definitie** | Niet-openbare gedetailleerde databestanden van het Centraal Bureau voor de Statistiek |
| **Klantperspectief** | "Landelijke cijfers die laten zien hoe het gaat met jeugdzorg in heel Nederland" |
| **Bron** | CBS |
| **Toegang** | Via CBS Remote Access, vereist overeenkomst |

---

## Organisatie en Geografie

### Aanbieder

| Veld | Waarde |
|------|--------|
| **Definitie** | Organisatie die jeugdhulp met verblijf levert |
| **Klantperspectief** | "De organisatie die voor mij zorgt" |
| **GGM-entiteit** | `Aanbieder` → `Jeugdhulpaanbieder` |
| **Bron** | Jeugdwet, AGB-register |
| **Data-elementen** | agb_code, naam, kvk_nummer, regio, type_zorg[] |

### Regio (Jeugdhulpregio)

| Veld | Waarde |
|------|--------|
| **Definitie** | Samenwerkingsverband van gemeenten voor de inkoop en organisatie van jeugdhulp |
| **Klantperspectief** | "Het gebied waarin voor mij gezocht wordt naar een passende plek" |
| **GGM-entiteit** | `Regio` → `Jeugdhulpregio` |
| **Bron** | VNG Jeugdhulpregio-indeling |
| **Data-elementen** | regio_code, naam, gemeenten[], contactpersoon |

### Peildatum

| Veld | Waarde |
|------|--------|
| **Definitie** | De datum waarop de aangeleverde gegevens betrekking hebben |
| **Klantperspectief** | "De datum waarop deze informatie klopt" |
| **Data-elementen** | datum, frequentie (dag/week/maand) |

---

## Toevoegen van nieuwe begrippen

Gebruik het volgende template:

```markdown
### [Begrip]

| Veld | Waarde |
|------|--------|
| **Definitie** | [Formele definitie] |
| **Klantperspectief** | "[Wat betekent dit voor de jongere?]" |
| **GGM-entiteit** | [GGM mapping of 'Nog te mappen'] |
| **Bron** | [Wet, standaard, operationeel] |
| **Synoniemen** | [Alternatieve termen] |
| **Data-elementen** | [Relevante datavelden] |
```
