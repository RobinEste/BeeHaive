# KNW-2026-041: Build-time API fetch met graceful empty-state fallback

> **Categorie:** development
> **Datum:** 2026-04-17
> **Sessie-context:** Astro static site haalt Research + Tools per BB uit FastAPI/Neo4j bij `astro build`
> **Relevantie:** hoog

## Inzicht

Bij build-time fetching naar een eigen backend API: laat de fetch-helper **nooit throwen** maar altijd een lege-collectie teruggeven bij netwerkfouten of non-200 responses. Combineer dat met componenten die zichzelf conditioneel renderen (`{items.length > 0 && …}`). Dan blijft `astro build` groen ook als de backend even plat ligt, en verschijnt de betreffende sectie simpelweg niet — in plaats van een CI-failure of een half-gerenderde pagina.

## Context

Astro's `getStaticPaths` haalt bij elke build KnowledgeItems en Tools uit de Neo4j-API. Als de backend niet draait (lokaal: Docker uit, CI: API-container niet gestart), zou een naïeve implementatie elke BB-pagina laten falen. Maar voor een content-gerichte site is *missende sectie* een acceptabele graceful degradation — de kernpagina (hero, checklist, MDX-body) is de source-of-truth en hangt niet van de API af.

## Geleerd

### Wat werkte

```typescript
async function apiGet<T>(path: string): Promise<T | null> {
  try {
    const res = await fetch(`${API_BASE}${path}`);
    if (!res.ok) {
      console.warn(`[api] ${path} returned ${res.status}`);
      return null;
    }
    return (await res.json()) as T;
  } catch (err) {
    console.warn(`[api] ${path} failed: ${message}`);
    return null;
  }
}

export async function fetchBBItems(bbName: string): Promise<KnowledgeItem[]> {
  const items = await apiGet<KnowledgeItem[]>(`/api/building-blocks/${encoded}/items`);
  return items ?? [];   // nooit null — altijd []
}
```

Component-kant:
```astro
{topItems.length > 0 && (
  <section class="bb-research">…</section>
)}
```

Resultaat: backend down → warning in build-log, geen exceptions, sectie onzichtbaar, build groen.

### Wat niet werkte

- **Throwen bij fetch-fout**: breekt de build, ook als alleen een kleine dynamische sectie mist. Overreactie voor content-sites.
- **Fallback op hardcoded default data**: verbergt de fout (geen visueel verschil tussen "API down" en "API gevuld met oude data"), en je moet fallback-data synchroon houden met het echte schema.
- **Fallback op lege array zonder console.warn**: silent failures in CI — niemand merkt dat de API down was.

### Waarom

De scheidslijn ligt bij *wat is wezenlijk voor de pagina*. Als een sectie **aanvullend** is (Research, Tools, Guardrails als dynamische extensies van een statische BB-pagina), dan is "niet tonen" een nette graceful degradation. Als een pagina *alleen* dynamische content heeft (bv. een item-detail-pagina uit de API), moet je falen luider — anders krijg je 404's of lege pagina's.

## Toepassing

- **Astro + externe API** (of Next.js SSG, Gatsby, etc.): default pattern voor niet-kritieke secties. `apiGet → null` + component conditional render.
- **Wél laten falen** wanneer de pagina zelf bestaat bij gratie van de API (dynamic routes die items uit de graph halen als primaire bron). Daar is null een echte fout.
- **Altijd `console.warn`**: zichtbaar in build-logs zonder de build te breken. Geen silent failures.
- **Test met backend uit**: run `npm run build` minimaal één keer met API offline om te verifiëren dat de graceful path écht werkt — anders is het papier-tijger-code.
