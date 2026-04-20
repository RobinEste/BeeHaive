# KNW-2026-043: Skill-fork pattern bij 1M-parent-context

> **Categorie:** development
> **Datum:** 2026-04-20
> **Sessie-context:** `/deep-research` draaien voor Dynamic Context BB_03 vanuit een Opus 4.7 [1M] hoofdsessie. Skill faalde bij invocatie met "Extra usage is required for 1M context".
> **Relevantie:** hoog

## Inzicht

Wanneer een skill bedoeld is om goedkoper te draaien (Sonnet) maar wordt aangeroepen vanuit een sessie met 1M extra-usage context (Opus), is alleen `model: sonnet` in de frontmatter onvoldoende — de harness probeert de 1M-context te erven voor Sonnet, wat een aparte extra-usage vereist. Het werkende patroon is `context: fork` + `model: sonnet` + `agent: general-purpose` gecombineerd met `$ARGUMENTS` (niet `$1`) voor arg-injection. De fork-configuratie en arg-injection zijn twee onafhankelijke concerns die beide moeten kloppen.

## Context

`/deep-research` had oorspronkelijk `model: sonnet` maar geen fork-instructie. Invocatie vanuit een Opus 4.7 [1M] sessie crashte met een API-error. Drie iteraties waren nodig om het volledige patroon te vinden:

1. **`model:` weglaten** → erft opus, werkt maar is duur en mist context-isolatie
2. **`model: inherit` toevoegen** → zelfde probleem, geen fork
3. **Pattern uit `/daily-start` overnemen** (`context: fork` + `model: sonnet` + `agent: general-purpose`) → skill startte maar meldde "geen onderwerp"
4. **`$1` → `$ARGUMENTS`** → werkte, 4 parallelle researchers draaiden naar behoren

## Geleerd

### Wat werkte
- `/daily-start` als referentie gebruiken — bewezen werkend skill onder vergelijkbare condities
- `context: fork` + `model: sonnet` + `agent: general-purpose` als drievoudig pakket
- `$ARGUMENTS` env-var voor arg-injection over de fork-boundary

### Wat niet werkte
- Partiële fixes (alleen `model` wijzigen; alleen `inherit` proberen; alleen fork toevoegen zonder arg-fix)
- Aannemen dat `$1` shell-expansion werkt in een geforkte skill-context

### Waarom
De fork-boundary is procesgrenzen-achtig: de harness spawnt een subagent met eigen model + eigen context-budget. Bash-stijl positional args (`$1`, `$2`) leven niet over die grens; `$ARGUMENTS` is de expliciet gesupporteerde injection-variabele. Zonder fork erft de skill zowel model als context van de parent — waardoor `sonnet` + parent-1M een onbedoelde combinatie wordt die extra-usage vereist.

## Toepassing

Voor elke nieuwe skill die in een zware parent-sessie goedkoop moet draaien:

```yaml
---
name: <skill-naam>
description: ...
disable-model-invocation: false
argument-hint: "<input>"
context: fork
model: sonnet            # of haiku voor nog goedkoper
agent: general-purpose
---
```

En in de body (Dynamische context-sectie): `$ARGUMENTS`, niet `$1`.

**Debug-checklist** bij skill-fork-errors:

1. Frontmatter heeft `context: fork`?
2. `model:` past bij de workload (`sonnet` voor research, `haiku` voor lichte ops)?
3. `agent: general-purpose` aanwezig?
4. Body gebruikt `$ARGUMENTS` (niet `$1`)?
5. Wijkt de structuur af van een werkend referentie-skill (`/daily-start`)?

**Wanneer géén fork:** als de skill juist op de parent-context moet werken (bijv. `/simplify` reviewed git diff die alleen in parent-context leeft), gebruik dan `model: inherit` of geen `model:` veld.
