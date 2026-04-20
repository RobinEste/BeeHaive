# KNW-2026-044: Vault-migratie van gedeelde resources vereist dependency-audit

> **Categorie:** development
> **Datum:** 2026-04-20
> **Sessie-context:** Ontdekt dat NI-scripts + CLAUDE.md + `/research-ni` skill-Stap 5 nog naar lokale `resources/bronnen/` wezen, 6 weken na commit `c4216ed` die het archief naar vault-level verplaatste.
> **Relevantie:** midden

## Inzicht

Wanneer een gedeelde resource (bronnen-archief, templates, scripts) van project-level naar vault-level wordt gemigreerd, laat een commit die alleen de move doet een trail van dead references achter: scripts die naar lege directories wijzen, skill-instructies met stale paden, CLAUDE.md-documentatie die verdwenen flows beschrijft. Deze failures zijn stilzwijgend — niets crasht, maar nieuwe runs schrijven naar de verkeerde lokatie. De migratie-commit moet daarom zowel de move als de dependent-updates bevatten.

## Context

In de NI-repo was in commit `c4216ed` (2026-03) het bronnenarchief verplaatst naar `~/ODIN/resources/bronnen/ai/`. In deze sessie (6 weken later) bleek:

- `NI/scripts/scrape-bron.sh` en `check-bronnen.sh` wezen nog naar `$PROJECT_ROOT/resources/bronnen` (inmiddels lege dir)
- `NI/CLAUDE.md` documenteerde de oude flow (scripts, template-path, batch-invocatie)
- `NI/.claude/skills/research-ni/SKILL.md` Stap 5 instrueerde de LLM om nieuwe bronnen in de lokale lege dir te schrijven

Elke `/research-ni`-run sinds de migratie zou nieuwe bronnen hebben gesplitst tussen vault en lokale project-dir. Geen enkele fout, alleen inconsistentie.

## Geleerd

### Wat werkte
- Drie-stappen cleanup: scripts verwijderen, CLAUDE.md updaten, skill-Stap delegeren naar `/bron-archiveren`
- Grep-audit op oude pad (`grep -r "resources/bronnen"`) vond alle referenties
- Scripts porten naar een canonieke plek (framework-skill `scripts/`) voorkomt herhaling

### Wat niet werkte
- Aanname dat een migratie-commit alleen de move-hoeft-te-doen: de dependency-trail blijft
- Vertrouwen op "as-needed" fixes: scripts faalden silent, dus niemand wist dat ze stuk waren tot we actief zochten

### Waarom
Migraties focussen cognitief op "bestanden verplaatsen" — dat is het fysieke werk. Het mentale model van "wat kijkt nu naar die bestanden" is secundair en makkelijk over te slaan. Scripts en skill-instructies gebruiken vaak relatieve paden (`$PROJECT_ROOT/...`) die niet direct grep-baar zijn op de destination-path, dus routine-search vindt ze niet.

## Toepassing

Bij elke migratie van een gedeelde resource (vault-move, cross-project consolidatie, refactor naar shared package):

### Pre-migratie dependency-audit

```bash
# Zoek referenties naar het oude pad
grep -rE '<oude-pad>|\$PROJECT_ROOT.*<oude-dirname>' \
  --include='*.sh' --include='*.md' --include='*.py' --include='*.ts' \
  ~/ODIN
```

Let op: expand ook naar `CLAUDE.md`, `README.md`, `.claude/skills/*/SKILL.md`, en project-specifieke configs.

### Commit-scope

Eén commit = move + update-dependents. Niet "migrate in PR 1, cleanup in PR 2" — de tussenperiode zijn silent failures.

### Post-migratie smoketest

Run de belangrijkste skills/scripts tegen de nieuwe lokatie. Als een skill een `/research-ni` Stap 5-achtige sectie heeft die paden hardcodeert, test die expliciet.

### Migration-checklist

Voeg dit toe als sectie in `CLAUDE.md` of als PR-template:

- [ ] Scripts die op oude pad wijzen (inclusief relatieve paden via `$PROJECT_ROOT`)
- [ ] Skill-instructies/SKILL.md met oude paden
- [ ] CLAUDE.md secties die de oude flow beschrijven
- [ ] README of onboarding-docs
- [ ] Open PRs/branches die oude pad gebruiken (merge-conflict opvangen)
- [ ] Smoketest op minstens één skill/script tegen nieuwe lokatie
