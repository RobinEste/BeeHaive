# Databronnen — Noordje op weg naar thuis

> Overzicht van alle databronnen die nodig zijn voor het dataplatform,
> inclusief eigenaar, toegang, inhoud en relevantie per informatiebehoefte.

## Klantperspectief

Al deze databronnen bevatten samen het antwoord op de vraag: "Waar kan ik
terecht, hoe snel, en krijg ik de juiste hulp?" Geen enkele bron geeft het
complete plaatje — pas door ze samen te brengen ontstaat een overzicht.

---

## Overzicht

| # | Databron | Eigenaar | Inhoud (relevant) | Prio subdoel | Toegang | Status |
|---|---------|---------|-------------------|-------------|---------|--------|
| 1 | iJw berichtenverkeer | VNG / Ketenbureau i-Sociaal Domein | Toewijzingen, start/stop zorg, productcodes, declaraties | 1a, 3 | Via gemeente/aanbieder | Te onderzoeken |
| 2 | iWmo berichtenverkeer | VNG / Ketenbureau i-Sociaal Domein | Wmo-gerelateerde trajecten (context) | 4, 5 | Via gemeente | Te onderzoeken |
| 3 | Aanbieders (operationeel) | Zorgaanbieders | Bezetting, capaciteit, beschikbaarheid, wachtlijsten, kenmerken locaties | 1a, 1b | Directe aanlevering | Te onderzoeken |
| 4 | CORV | Min. J&V | Maatregelen, machtigingen gesloten jeugdhulp, justitieel berichtenverkeer | 1a, 2 | Via CORV-koppeling | Te onderzoeken |
| 5 | CBS microdata | CBS | Landelijke cijfers jeugdzorg, demografisch, sociaal-economisch | 1a, 2 | CBS Remote Access (overeenkomst) | Te onderzoeken |
| 6 | DUO | Min. OCW | Thuiszitters, schoolverzuim, leerlingenregistratie | 2 | Via DUO / CBS | Te onderzoeken |
| 7 | Gemeenten | Gemeenten NH | Verwijzingen, beschikkingen, BRP-data (woonplaats) | 1a, 5 | Via gemeente | Pilot: Haarlemmermeer |
| 8 | GI's | Gecertificeerde Instellingen | Maatregelen, caseload, verwijzingen | 1a, 2 | Via GI | Te onderzoeken |
| 9 | J&V / DJI | Min. J&V | Forensisch profiel, JJI-plaatsingen | 2 | Via J&V | Te onderzoeken |

---

## Detailbeschrijving per Databron

### 1. iJw Berichtenverkeer

| Veld | Waarde |
|------|--------|
| **Eigenaar** | VNG / Ketenbureau i-Sociaal Domein |
| **Beschrijving** | Gestandaardiseerd berichtenverkeer tussen gemeenten en jeugdhulpaanbieders |
| **Relevante berichten** | 301 (Toewijzing), 305 (Start zorg), 307 (Stop zorg), 315 (Declaratie) |
| **Datavelden** | Productcode, aanbieder, startdatum, einddatum, volume, gemeente, BSN (versleuteld) |
| **Informatiewaarde** | Type zorg, duur, aanbieder, in/uitstroom, plaatsingen, verwijzer |
| **Frequentie** | Per bericht (near real-time in theorie) |
| **Toegang** | Via gemeenten (als verwerkingsverantwoordelijke) of Ketenbureau |
| **Juridisch** | AVG: gemeente is verwerkingsverantwoordelijke |
| **Aandachtspunten** | Kwaliteit verschilt per gemeente; niet alle berichten worden correct verstuurd |

### 2. Aanbieders (Operationele data)

| Veld | Waarde |
|------|--------|
| **Eigenaar** | Individuele zorgaanbieders |
| **Beschrijving** | Operationele gegevens uit ECD-systemen (Elektronisch Cliënt Dossier) |
| **Datavelden** | Bezetting, capaciteit, beschikbaarheid, wachtlijst, locatiekenmerken, doelgroep |
| **Informatiewaarde** | Actuele beschikbaarheid, voorzieningen-overzicht |
| **Frequentie** | Af te spreken: dag/week/maand |
| **Toegang** | Directe aanlevering (CSV, API, formulier) |
| **Aandachtspunten** | Formaten verschillen per aanbieder; handmatige stappen; wachtlijst vaak informeel (zie transcripties) |

### 3. CORV

| Veld | Waarde |
|------|--------|
| **Eigenaar** | Ministerie van Justitie en Veiligheid |
| **Beschrijving** | Routeervoorziening voor justitieel berichtenverkeer jeugdketen |
| **Datavelden** | Type maatregel, machtigingen gesloten jeugdhulp, verzoeken, beschikkingen |
| **Informatiewaarde** | Maatregel per plaatsing, aantal gesloten machtigingen |
| **Frequentie** | Per bericht |
| **Toegang** | Via CORV-koppeling (gemeente moet aangesloten zijn) |
| **Juridisch** | Strenge autorisatie; alleen bevoegde partijen |

### 4. CBS Microdata

| Veld | Waarde |
|------|--------|
| **Eigenaar** | Centraal Bureau voor de Statistiek |
| **Beschrijving** | Niet-openbare gedetailleerde data over jeugdzorggebruik, demografisch en sociaal-economisch |
| **Relevante bestanden** | Jeugdzorggebruik, huishoudsamenstelling, inkomen, onderwijs |
| **Informatiewaarde** | Landelijke vergelijking, trends, voorspellende factoren |
| **Frequentie** | Jaarlijks (vertraging ~1 jaar) |
| **Toegang** | CBS Remote Access Environment, vereist goedgekeurd onderzoeksvoorstel |
| **Juridisch** | CBS-wet; output moet voldoen aan onthullingsregels |

### 5. DUO

| Veld | Waarde |
|------|--------|
| **Eigenaar** | Dienst Uitvoering Onderwijs / Min. OCW |
| **Beschrijving** | Leerlingenregistratie, schoolverzuim, thuiszitters |
| **Datavelden** | Inschrijvingen, verzuimmeldingen, thuiszitters |
| **Informatiewaarde** | Voorspellende factor: thuiszitters hebben verhoogd risico op plaatsing |
| **Frequentie** | Schooljaar-basis |
| **Toegang** | Via CBS microdata of direct bij DUO (convenant nodig) |

### 6. Gemeenten

| Veld | Waarde |
|------|--------|
| **Eigenaar** | Individuele gemeenten |
| **Beschrijving** | Verwijzingen, beschikkingen, BRP-gegevens |
| **Datavelden** | Verwijzingen, woonplaats jeugdige, beschikking, wijkteam-informatie |
| **Informatiewaarde** | Verwijzer, woonplaats (afstand tot plaatsing), lokale context |
| **Frequentie** | Per beschikking/verwijzing |
| **Toegang** | Via gemeentelijk applicatielandschap |
| **Pilot** | Gemeente Haarlemmermeer als eerste |

---

## Verwerkersovereenkomsten

Per databron moet een verwerkersovereenkomst (VO) of andere juridische grondslag
worden geregeld. Dit is onderdeel van de DPIA.

| Databron | Type overeenkomst | Verantwoordelijke | Deadline |
|---------|-------------------|-------------------|----------|
| iJw | VO met gemeente(n) | Pilotgemeente + projectgroep | Jan-Mrt 2025 |
| Aanbieders | VO per aanbieder | Projectgroep | Jan-Mrt 2025 |
| CORV | Autorisatiebesluit | J&V + gemeente | Jan-Mrt 2025 |
| CBS | Microdata-overeenkomst | Onderzoeksinstelling | Jan-Mrt 2025 |
| DUO | Convenant | Via CBS of direct | Fase 3 |
| Gemeenten | Intern (pilot) | Haarlemmermeer | Jan 2025 |

---

## Datakwaliteit per Bron

| Databron | Verwachte kwaliteit | Bekende risico's |
|---------|--------------------|--------------------|
| iJw | Gemiddeld | Niet alle berichten correct; verschilt per gemeente |
| Aanbieders | Wisselend | Handmatige stappen; formaatverschillen; wachtlijst informeel |
| CORV | Hoog | Beperkte toegankelijkheid |
| CBS | Hoog | Vertraging ~1 jaar; aggregatieniveau |
| DUO | Hoog | Beperkt tot onderwijsdomein |
| Gemeenten | Wisselend | Applicatielandschap verschilt sterk |
