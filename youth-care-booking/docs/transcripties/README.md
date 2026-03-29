# Transcripties — Verhalen achter de Processen

> Elke procesbeschrijving wordt verrijkt met een transcriptie: het verhaal
> van hoe het proces in de praktijk werkt, verteld door de mensen die het doen.

## Doel

Transcripties dienen drie functies:

1. **Context voor de AI-agent** — De agent gebruikt transcripties om te begrijpen
   *waarom* data er uitziet zoals het eruitziet, en wat afwijkingen kunnen betekenen
2. **Kennisborging** — Impliciete kennis van medewerkers wordt expliciet vastgelegd
3. **Training** — Nieuwe medewerkers begrijpen het proces door de verhalen

## Klantperspectief

Achter elk datapunt zit een verhaal. Een "bezettingsgraad van 95%" betekent
dat er bijna geen plek meer is voor een kind dat hulp nodig heeft. Transcripties
houden die menselijke context vast in een systeem dat met cijfers werkt.

---

## Voorbeeld Transcriptie

### TR-001: Aanlevering bezettingsdata bij Instelling X

**Proces:** Periodieke data-aanlevering (Proces 2)
**Verteld door:** Administratief medewerker
**Datum:** [nog in te vullen]

> "Elke maandagochtend trek ik de cijfers uit ons ECD. Dat is een export naar
> Excel. Dan moet ik handmatig de groepen langslopen omdat het systeem geen
> onderscheid maakt tussen crisis en regulier. Die kolom vul ik zelf in op
> basis van wat ik weet van de teamleiders.
>
> Soms klopt de bezetting niet omdat een kind officieel nog ingeschreven staat
> maar al bij een pleeggezin zit. Dat duurt soms twee weken voordat de
> uitschrijving verwerkt is. Dus mijn cijfers lopen altijd een beetje achter
> op de werkelijkheid.
>
> De wachtlijst is lastig. We hebben eigenlijk geen formele wachtlijst. Als
> iemand belt en wij hebben geen plek, zeggen we 'probeer het volgende week
> nog eens'. Dat staat nergens geregistreerd."

### Gelinkte begrippen

| Begrip (glossary) | Context uit transcriptie |
|-------------------|-------------------------|
| Bezettingsgraad | Loopt achter door vertraagde uitschrijving |
| Wachtlijst | Informeel, niet geregistreerd |
| Type Verblijf | Handmatig onderscheid crisis/regulier |
| Peildatum | Wekelijks, maandagochtend |

### Signalen voor AI-agent

- **Datakwaliteit-risico:** Bezetting kan tot 2 weken vertraagd zijn
- **Ontbrekende data:** Wachtlijst wordt niet bijgehouden
- **Handmatige stap:** Type verblijf wordt handmatig ingevuld → foutgevoelig

---

## Template: Nieuwe Transcriptie

```markdown
### TR-[NNN]: [Titel]

**Proces:** [Link naar procesbeschrijving]
**Verteld door:** [Rol, niet naam]
**Datum:** [Datum interview]

> [Transcriptie in eigen woorden van de geïnterviewde]

### Gelinkte begrippen

| Begrip (glossary) | Context uit transcriptie |
|-------------------|-------------------------|
| ... | ... |

### Signalen voor AI-agent

- **Datakwaliteit-risico:** [...]
- **Ontbrekende data:** [...]
- **Handmatige stap:** [...]
```

## Interviewgids

Bij het afnemen van transcripties, stel deze kernvragen:

1. **Hoe lever je de data aan?** (systeem, format, handmatig)
2. **Hoe vaak?** (frequentie, vaste dag/tijdstip)
3. **Wat gaat er weleens mis?** (fouten, vertragingen, onduidelijkheden)
4. **Wat staat er niet in de data?** (impliciete kennis, informele processen)
5. **Hoe zou je het anders willen?** (verbeterwensen)
