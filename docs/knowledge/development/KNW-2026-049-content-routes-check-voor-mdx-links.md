# KNW-2026-049: Check route-bestaan vóór inline-links in content-MDX

> **Categorie:** development
> **Datum:** 2026-04-21
> **Sessie-context:** Bij het schrijven van BB_03 werden inline-links naar `/guardrails/<slug>` gelegd. Achteraf bleek de dynamische route `/guardrails/[slug].astro` niet te bestaan — alleen `/framework/[slug].astro` was geïmplementeerd. Alle GR-links liepen op 404. Opgelost door bold+code-notatie in plaats van links.
> **Relevantie:** midden

## Inzicht

Wanneer je inline-links in content-MDX gebruikt die naar andere delen van dezelfde site wijzen, controleer dan **eerst** of de overeenkomstige dynamische route in de pages-laag al bestaat. Een link naar `/guardrails/privacy` is syntactisch geldig, maar levert een stille 404 op als er geen `/guardrails/[slug].astro` bestaat om die slug te resolven. De Astro-compiler signaleert deze fouten niet — ze verschijnen pas op runtime.

## Context

BB_03 werd opgezet met verwijzingen naar de bijbehorende Guardrails. Vanuit de stijlgids was "cross-refs met kernzin + link" de gewenste vorm: `[Privacy](/guardrails/privacy) (GR_03: databescherming als fundament)`. Die links kwamen door de `astro check` heen zonder problemen — MDX ziet ze als gewone markdown-links.

Tijdens de UI-smoketest bleek dat `http://localhost:4322/guardrails/privacy` een HTTP 404 gaf. Het probleem: `frontend/src/pages/` had alleen `framework/[slug].astro` geïmplementeerd, niet `guardrails/[slug].astro`. De Guardrails bestonden als content-collectie (`src/content/guardrails/*.mdx`) maar waren nog niet via een detail-pagina ontsloten — alleen als cards in de `BBGuardrails`-component op de BB-pagina's.

Resolutie: alle `/guardrails/<slug>`-links in BB_03 vervangen door de notatie `**Privacy** (GR_03: databescherming als fundament)` — bold naam + code tussen haakjes met kernzin. Geen dead link, wel herkenbaar als cross-reference.

## Geleerd

### Wat werkte

- **Systematische HTTP-check van alle interne links** tijdens UI-smoketest (curl + 200-OK check op elk pad dat in de MDX voorkomt). Dit vangt dead-links voordat ze in productie belanden.
- **Terugvalnotatie voor cross-refs naar nog-niet-bestaande routes:** `**Name** (CODE: kernzin)` in plaats van een link. Leest vloeiend en signaleert nog steeds de cross-reference aan de lezer.
- **Stijlgids-regel**: "cross-refs krijgen naam + code + kernzin bij eerste voorkomen" werkt ook zonder link — de lezer ziet waarnaar verwezen wordt, ook als de detail-pagina (nog) niet bestaat.

### Wat niet werkte

- **Vertrouwen op `astro check` voor link-validatie**: check valideert typescript en content-schema, niet de interne link-doelen. Dode links slippen er doorheen.
- **Achteraf een guardrails-route bouwen toen de dead-links al waren ontdekt**: dit voelde verleidelijk (één file, 30 regels code, probleem opgelost) maar zou hebben betekend dat we buiten de scope van de BB_03-sessie aan een nieuwe feature begonnen. Terugvalnotatie was het goede antwoord voor die sessie.

### Waarom

Astro's bestandssysteem-routing legt de routes impliciet vast: `/framework/[slug].astro` genereert `/framework/<slug>` voor elke slug in de content-collectie; zonder `/guardrails/[slug].astro` bestaan die routes niet, ook al zijn de onderliggende `.mdx`-bestanden wel aanwezig. Content-collecties en pages zijn **twee aparte lagen** — collectie = data, pages = rendering. Een link veronderstelt dat de rendering bestaat.

Dit probleem schaalt met content-groei: hoe meer MDX-files met interne links je hebt, hoe moeilijker het wordt om met het oog te zien welke links daadwerkelijk resolven. Zonder check-tooling vervalt dit in "broken-links dashboard bij de derde of vierde content-revisie".

## Toepassing

**Preventief (voordat je links plaatst):**

1. **Lijst interne-link-patronen** die je in content gebruikt: `/framework/<slug>`, `/guardrails/<slug>`, `/kennisbank/<id>`, `/begrippen#<slug>`, etc.
2. **Check per patroon of er een pages-bestand voor bestaat**:
   ```bash
   ls frontend/src/pages/guardrails/ 2>/dev/null || echo "GEEN ROUTE — geen guardrails-links in MDX"
   ```
3. **Pas de stijlgids aan** met een "toegestane link-targets"-lijst

**Reactief (opsporen van bestaande dead-links):**

1. **Smoketest-script dat alle interne links extraheert en checkt**:
   ```bash
   # Pseudo — extract [text](/path) uit MDX, curl elke /path lokaal
   grep -rhoE '\(/[a-z][^)]+\)' frontend/src/content/*.mdx | sort -u | while read url; do
     code=$(/usr/bin/curl -s -o /dev/null -w "%{http_code}" "http://localhost:4322${url}")
     [ "$code" != "200" ] && echo "DEAD: $url → $code"
   done
   ```
2. **Fallback-notatie** voor intern verwezen content zonder route: `**Name** (CODE: kernzin)` — leesbaar, geen 404.
3. **Overweeg een Astro-plugin** (bv. `astro-linkinator`) als het content-volume groeit.

**Ontwerpregel voor toekomstige features:**

Wanneer je een content-collectie aanmaakt (`src/content/X/`), maak **tegelijk** of **kort daarna** de bijbehorende `pages/X/[slug].astro` — of leg expliciet vast dat er geen detail-pagina komt zodat auteurs geen links ernaartoe plaatsen. Gesplitste releases (collectie vóór pages) zijn een bron van dead-links.

**Koppeling met andere KNW-entries:**

- KNW-2026-041 (Build-time API fetch met graceful empty-state fallback) — zelfde principe van "check resource-bestaan vóór rendering", andere context
- KNW-2026-038 (Content consistency-pass na narrative-updates) — link-check hoort in die consistency-pass
