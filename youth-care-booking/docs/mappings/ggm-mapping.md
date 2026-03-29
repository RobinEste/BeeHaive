# Data Mapping: Brondata → Gemeentelijk Gegevensmodel (GGM)

> Vertaling van data-elementen zoals aangeleverd door aanbieders en gemeenten
> naar het Gemeentelijk Gegevensmodel (GGM).

## Klantperspectief

Deze mapping zorgt ervoor dat dezelfde informatie — ongeacht welke aanbieder
of gemeente het aanlevert — altijd hetzelfde betekent. Voor de jeugdige en
het gezin betekent dit: **geen verwarring, geen fouten, sneller de juiste plek**.

## Mapping Overzicht

### Aanbieder → GGM

| Bronveld (aanbieder) | Varianten bij aanbieders | GGM-entiteit | GGM-attribuut | Transformatie |
|----------------------|--------------------------|--------------|---------------|---------------|
| `organisatie_naam` | naam, instelling, zorgaanbieder | Aanbieder | naam | Directe mapping |
| `agb` | agb_code, agbcode, AGB | Aanbieder | identificatie | Strip niet-numeriek |
| `kvk` | kvk_nummer, KvK, handelregister | Aanbieder | kvkNummer | Strip niet-numeriek |
| `adres` | locatie, vestiging, postadres | Locatie | adres | Splits naar straat/postcode/plaats |
| `capaciteit` | bedden, plekken, plaatsen | Verblijf | capaciteit | Integer |
| `bezet` | bezetting, in_gebruik, gevuld | Verblijf | bezettingsaantal | Integer |
| `vrij` | beschikbaar, vrije_plekken, open | *Berekend* | — | `capaciteit - bezet` |
| `type_zorg` | zorgvorm, hulpvorm, categorie | Product | productCategorie | Mapping via codelijst |
| `leeftijd_van` | min_leeftijd, vanaf | Product | leeftijdVanaf | Integer |
| `leeftijd_tot` | max_leeftijd, tot | Product | leeftijdTot | Integer |

### Gemeente → GGM

| Bronveld (gemeente) | Varianten bij gemeenten | GGM-entiteit | GGM-attribuut | Transformatie |
|---------------------|------------------------|--------------|---------------|---------------|
| `gemeente_code` | gem_code, CBS_code | Gemeente | identificatie | 4-cijferig, zero-padded |
| `regio` | jeugdhulpregio, samenwerkingsverband | Regio | naam | Lookup via VNG-tabel |
| `budget_jz` | jeugdzorgbudget, budget_verblijf | *Niet in GGM* | — | Apart opslaan |
| `aantal_verwijzingen` | verwijzingen, indicaties | Verwijzing | aantal | Integer, per periode |
| `wachtenden` | wachtlijst, wachtenden_aantal | *Niet in GGM* | — | Apart opslaan |

## Codelijsten

### Type Verblijf

| Bronwaarde (varianten) | GGM-code | Omschrijving |
|------------------------|----------|--------------|
| pleegzorg, pleeggezin, foster | PLG | Pleegzorg |
| gezinshuis, gezinshuiszorg | GZH | Gezinshuis |
| residentieel, klinisch, groep | RES | Residentiële jeugdhulp |
| gesloten, jji, gesloten_plaatsing | GJJ | Gesloten jeugdhulp (JeugdzorgPlus) |
| crisis, crisisopvang, spoedplaatsing | CRS | Crisisopvang |
| kamertraining, begeleid_wonen | KTW | Kamertraining / begeleid wonen |

### Zorgzwaarte

| Bronwaarde (varianten) | GGM-code | Omschrijving |
|------------------------|----------|--------------|
| licht, basis, ambulant_verblijf | ZZ1 | Lichte verblijfszorg |
| midden, regulier, standaard | ZZ2 | Reguliere verblijfszorg |
| zwaar, intensief, complex | ZZ3 | Intensieve/complexe verblijfszorg |
| zeer_zwaar, hoog_specialistisch | ZZ4 | Hoog-specialistische verblijfszorg |

## Mapping Proces

```
1. Aanbieder levert brondata aan (eigen formaat)
         ↓
2. Third party ontvangt en parseert
         ↓
3. Veldherkenning: match bronvelden op mapping-tabel
         ↓
4. Transformatie: pas codelijsten en regels toe
         ↓
5. Validatie: controleer verplichte velden en datatypes
         ↓
6. Anonimisering: verwijder/pseudonimiseer persoonsgegevens
         ↓
7. Opslag in centraal GGM-gebaseerd datamodel
```

## Nog Te Mappen

Velden die nog geen GGM-equivalent hebben en waarvoor een extensie nodig is:

- Wachtlijstgegevens (aantal, wachttijd)
- Beschikbaarheid in real-time
- Budgetinformatie gemeenten
- Kwaliteitsindicatoren
- Uitstroomgegevens

Deze worden als extensie op het GGM voorgesteld aan VNG/KING.
