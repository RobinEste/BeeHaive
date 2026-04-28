# Client Blueprint — Template en Voorbeeld

**Gebaseerd op:** BeeHaive BB_02 Client Blueprint (`frontend/src/content/building-blocks/client-blueprint.mdx`)
**Onderbouwing:** `docs/research/client-blueprint-2026/final.md` en vier deel-research-bestanden
**Versie:** 1.0 — 2026-04-28
**Status:** Template + uitgewerkt voorbeeld voor de fictieve klant *Hexant Consulting*

---

## Leeswijzer

Dit document is twee dingen tegelijk:

1. **Een ingevuld voorbeeld** dat aan een klant laat zien hoe een Client Blueprint eruitziet als hij is opgeleverd. Het voorbeeld gebruikt overal de fictieve klant *Hexant Consulting* (een Nederlands consultancy-bureau dat AI-Readiness Audits levert), zodat de klant kan zien hoe de structuur op een concreet geval landt.
2. **Een herbruikbare template** waarin elk hoofdstuk een placeholder-blok bevat (gemarkeerd met `> [INVULLEN: ...]`) dat per nieuwe opdracht wordt overschreven met klant-specifieke inhoud.

Per hoofdstuk wordt eerst kort uitgelegd *waarom* dat hoofdstuk in de blueprint hoort (de "wat staat hier en waarom"), gevolgd door een quote die de noodzaak onderschrijft, vervolgens het uitgewerkte voorbeeld voor Hexant, daarna het invul-blok, een checklist, en de relevante literatuur.

Drie leesregels:

- **Lineair lezen voor een eerste indruk; selectief lezen na overdracht.** Hoofdstuk 0 (klant- en projectkaart) en Bijlage A (eindchecklist) volstaan voor een snelle review; de tussenliggende hoofdstukken zijn de onderbouwing.
- **De blueprint is een levend document.** Elk hoofdstuk bevat een `Status / laatste herziening`-veld zodat zichtbaar blijft welke onderdelen sinds de bouw zijn bijgewerkt.
- **Bij twijfel: het gesprek is belangrijker dan het document.** De blueprint dwingt het juiste gesprek af; hij vervangt dat gesprek niet.

---

## Bronnen-conventie

- Verwijzingen tussen blokhaken `[NN]` corresponderen met de literatuurlijst in Bijlage B.
- Citaten staan in *cursief* met bronvermelding direct erachter.
- Verwijzingen naar de zes andere BeeHaive-bouwstenen (BB_01, BB_03 t/m BB_07) verwijzen naar `frontend/src/content/building-blocks/*.mdx`.

---

## Inhoudsopgave

Elke hoofdstuk staat in een eigen bestand in deze map. De volgorde is bewust: hoofdstuk 0 en Bijlage A volstaan voor een snelle review, de tussenliggende hoofdstukken zijn de onderbouwing.

| # | Bestand | Titel | Hoort bij BB-sectie |
|---|---------|-------|---------------------|
| 0 | [`00-klantkaart.md`](./00-klantkaart.md) | Klant- en projectkaart | (alle) |
| 1 | [`01-waarde-stroom.md`](./01-waarde-stroom.md) | Strategische verankering en waarde-stroom | "Toegevoegde waarde voor de klant is hét uitgangspunt" |
| 2 | [`02-discovery.md`](./02-discovery.md) | Use-case-discovery in zeven stappen | "De zeven stappen van use-case-discovery" |
| 3 | [`03-architectuur.md`](./03-architectuur.md) | Architectuur en technische ontwerpkeuzes | "Architectuur: wanneer kies je een workflow, wanneer een agent?" |
| 4 | [`04-risico.md`](./04-risico.md) | Risico, compliance en ethiek | "Risico's als ontwerp-input, niet achteraf bepaald" |
| 5 | [`05-prototype.md`](./05-prototype.md) | Prototype als gespreksanker | "Het prototype als basis voor klantreview" |
| 6 | [`06-iteratie.md`](./06-iteratie.md) | Iteratieve werkwijze en FDE-principes | "Iteratief bouwen: FDE-principes en hun grenzen" |
| 7 | [`07-governance.md`](./07-governance.md) | Governance, goedkeuring en Nederlandse context | "Governance, goedkeuring en de Nederlandse context" |
| 8 | [`08-cross-bouwsteen.md`](./08-cross-bouwsteen.md) | Cross-bouwsteen-overzicht | "In de praktijk" (cross-cutting) |
| A | [`bijlage-a-eindchecklist.md`](./bijlage-a-eindchecklist.md) | Eindchecklist (goedkeuringspoort) | (samenvatting) |
| B | [`bijlage-b-literatuur.md`](./bijlage-b-literatuur.md) | Literatuur en bronvermeldingen | (samenvatting) |

---

