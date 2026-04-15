# KNW-2026-037: Native `<details>` + progressive enhancement voor anchor-link auto-open

> **Categorie:** development
> **Datum:** 2026-04-15
> **Sessie-context:** BBDisclosure component voor BB detail-pagina's in BeeHaive. User klikt teaser-link naar andere disclosure, scrollt wel maar de details blijft dicht.
> **Relevantie:** hoog

## Inzicht

Native HTML `<details>/<summary>` is zero-JS, toegankelijk en past bij een zuinige UX — maar heeft één UX-gat: een anchor-link naar `#section-x` scrollt wél naar de `<details>`, maar opent hem niet. Content blijft verborgen voor de gebruiker die erheen klikte. Een klein script (≈15 regels) dat op `hashchange` en page load de matching details auto-opent, herstelt de UX zonder de native voordelen te verliezen. Verwerk ook hashes die een heading **binnen** een `<details>` raken, via `element.closest('details')`.

## Context

Op de Prompt Design pagina staan vijf `<BBDisclosure>`-secties, default dicht. In één disclosure staat een teaser: "Dit is een eigen ontwerpdiscipline geworden — zie de sectie [Agentic prompt design: flow engineering](#agentic-prompt-design-flow-engineering) hieronder voor de diepte." Klikken scrollt netjes, maar de target-disclosure blijft gesloten — gebruiker staat voor een dichte `<summary>` zonder context.

De fix: script in de `BBDisclosure.astro` component dat bij `hashchange` (en eenmalig op load) de hash checkt en de matching `<details>` opent.

```javascript
function openFromHash() {
  const hash = window.location.hash.slice(1);
  if (!hash) return;
  const target = document.getElementById(hash);
  if (!target) return;
  const details = target instanceof HTMLDetailsElement
    ? target
    : target.closest('details');
  if (details instanceof HTMLDetailsElement && !details.open) {
    details.open = true;
    target.scrollIntoView({ behavior: 'smooth', block: 'start' });
  }
}
openFromHash();
window.addEventListener('hashchange', openFromHash);
```

## Geleerd

### Wat werkte
- Native `<details>` als basis houden — accessibility, keyboard-nav, screenreader-support kosten niks
- Script alleen voor de UX-fix, niet voor het basisgedrag
- `closest('details')` voor het geval de hash een heading BINNEN een disclosure raakt (H3 met slug-id)
- Astro `<script>` wordt per component dedupliceerd — één script volstaat ook al zijn er meerdere disclosures op de pagina

### Wat niet werkte
- Alternatief "alle disclosures default open" — verliest de samenvatting/overzicht-UX
- Alternatief ":target` CSS pseudo-class" — werkt niet voor details (zou `details[id]:target { open: true }` moeten zijn en dat is geen bestaande CSS)

### Waarom
Progressive enhancement principe: native werkt zonder JS, JS voegt comfort toe bij specifieke gaten. De browser-spec definieert `<details>` auto-open expliciet NIET bij anchor-navigation (zie [html.spec.whatwg.org](https://html.spec.whatwg.org/multipage/interactive-elements.html#the-details-element)). Implementatie is dus aan de site.

## Toepassing

Voor elke UI met collapsible content + deep-links:

1. **Start met native `<details>/<summary>`** — niet een React/JS-accordion component
2. **Als deep-links ondersteund moeten worden**: voeg een hashchange-listener toe
3. **Vergeet de `.closest('details')` check niet** — headings binnen een disclosure moeten ook hun parent openen
4. **Scroll na open, niet vóór** — zonder open staat scrollIntoView op een onzichtbaar element

De listener hoort bij het component waarin `<details>` leeft — niet globaal — zodat elke disclosure-component zelf-contained is.
