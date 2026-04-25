# KNW-2026-056: Disclosure-isolatie — elke collapsable sectie moet zelfdragend zijn

> **Categorie:** design
> **Datum:** 2026-04-25
> **Sessie-context:** BB_01 Knowledge tweede lees-review — termen als FOBO en jagged frontier waren in de eerste disclosure uitgelegd, maar in latere disclosures ("In de praktijk") opnieuw zonder context gebruikt
> **Relevantie:** hoog

## Inzicht

Bij UI-patronen waarin secties default-collapsed zijn (`<details>`/BBDisclosure, accordion, tabs), is het normale leesgedrag NIET top-down maar landing-in-een-sectie via search, deep-link of inhoudsopgave. Daarom moet elke disclosure zelfdragend zijn: termen die in een eerdere disclosure zijn uitgelegd, moeten bij hergebruik in een latere disclosure opnieuw kort worden geïntroduceerd (inline-uitleg + glossary-link), niet één keer-en-klaar op de hele pagina.

## Context

In BB_01 Knowledge waren termen als "FOBO" en "jagged frontier" zorgvuldig geïntroduceerd in de eerste disclosure waar ze voorkwamen, met inline-uitleg en glossary-link. In de "In de praktijk"-disclosure verderop op dezelfde pagina werden ze opnieuw gebruikt zonder context — alleen als string. Robin flagde beide:

- *"Kun je FOBO ook neerzetten als begrip. In Zijn mensen en organisaties klaar voor AI staat het uitgelegd, maar in In de praktijk niet."*
- *"De jagged frontier van AI is niet stabiel staat in dit stuk ook op zichzelf: nog toelichten."*

Dit is geen incident: `<details>` default-closed UI maakt elke disclosure een mogelijke landingsplek. Search highlights, anchor-links, inhoudsopgave-clicks en ctrl-F binnen de pagina openen typisch één disclosure. De lezer ziet niet wat in andere disclosures staat tenzij hij die ook openvouwt.

## Geleerd

### Wat werkte
- Op de eerste mention in elke afzonderlijke disclosure: glossary-link (`[**FOBO**](/begrippen#fobo)`) + korte inline-expansie ("FOBO — *Fear of Becoming Obsolete*, de angst dat AI je overbodig maakt — is hier de stille drijfveer").
- Korte expansie volstaat — geen volledige uitleg, gewoon één bijzin die de term tastbaar maakt voor wie hier binnenvalt.
- Glossary-link verwijst naar de volledige uitleg voor wie meer wil; inline-expansie volstaat voor wie alleen door wil lezen.

### Wat niet werkte
- Eén keer uitleggen op de hele pagina, in de aanname dat de lezer de pagina top-down leest.
- Vertrouwen op cross-section memory ("we hebben dit eerder uitgelegd, dus hoeft niet meer").
- Een term puur als string gebruiken (FOBO, jagged frontier) zonder de aanname expliciet te maken dat de lezer hem kent.

### Waarom
Default-collapsed UI verandert het leescontract: elke disclosure is een mini-pagina, niet een paragraaf in een lineair document. De lezer kan via deep-link naar een sectie binnenkomen, of de pagina scannend doorlopen en alleen de disclosures openvouwen die relevant lijken. Dat is een UX-feature (snelheid, scanbaarheid), maar het breekt de aanname van schrijfregels die gebouwd zijn voor lineaire teksten ("eenmaal uitgelegd, dan bekend").

## Toepassing

Bij content in collapsable UI-componenten (BBDisclosure, accordion, `<details>`, tab-panes):

1. **Behandel elke disclosure als een mini-pagina** met eigen reading context. Schrijfregels die voor één pagina gelden ("introduceer term op eerste mention") gelden binnen elke disclosure.
2. **Bij eerste mention van een gespecialiseerde term in een disclosure**: inline-expansie + glossary-link. Bij vervolgmentions binnen dezelfde disclosure: alleen de term.
3. **Korte expansie volstaat**: één bijzin met `[**term**](/begrippen#slug) — *Engelse vorm*, kerndefinitie —` is genoeg. Geen herhaling van de volledige uitleg.
4. **Bouw deze regel in als review-stap** bij content-checks: scan de tweede en latere disclosures op terms die alleen in disclosure-1 zijn uitgelegd.
5. **Voor cross-disclosure consistency**: een glossary-pagina (met stable URL als `/begrippen#fobo`) is essentieel. Zonder die single source of truth wordt elke inline-expansie een potentieel divergentiepunt.
