# KNW-2026-036: Disjoint dimensies voorkomen dubbel werk bij parallelle researchers

> **Categorie:** development
> **Datum:** 2026-04-15
> **Sessie-context:** Deep research naar Prompt Design 2026 als input voor BB_04 website-uitbreiding. Vier researchers parallel gedispatcht via de `/deep-research` skill.
> **Relevantie:** hoog

## Inzicht

Wanneer je meerdere parallelle researchers dispatcht voor één onderzoek, is de grootste efficiëntie-winst het expliciet afbakenen van elkaars scope. Elke researcher krijgt niet alleen een eigen dimensie ("academisch", "vendor-docs"), maar ook expliciete **taakgrenzen** — "geen vendor-docs (dat is R2), geen academische papers (dat is R1)". Zonder deze uitsluitingen werken researchers overlappend en leveren ze dezelfde bronnen dubbel.

## Context

Deep research naar de actuele stand van Prompt Design moest 8 focusvragen dekken over 18 maanden aan ontwikkelingen. Vier researchers parallel: **R1 academisch** (arXiv/ACL), **R2 vendor docs** (Anthropic/OpenAI/Google), **R3 industry/practitioners** (engineering blogs), **R4 agentic + guardrails** (EU AI Act, OWASP). Elke brief bevatte zowel positieve scope ("wat jij dekt") als expliciete uitsluitingen ("wat jij NIET dekt — dat is Rx").

Resultaat: ~40 unieke bronnen over 4 onderzoeksfiles, minimale overlap, één ronde was voldoende voor alle 8 vragen.

## Geleerd

### Wat werkte
- Expliciete "Taakgrenzen:" sectie in elke researcher-brief met verwijzing naar andere researchers ("dat is R2")
- Dimensies gekozen op **brontype/perspectief** (academisch vs. vendor vs. practitioner vs. governance), niet op onderwerp-onderdelen. Elk onderwerp werd zo vanuit vier invalshoeken belicht.
- Elk onderwerp met één bron leverde zwakke onderbouwing; twee+ bronnen uit verschillende dimensies leverde triangulation

### Wat niet werkte
- Initial neiging om dimensies op onderwerp te splitsen (bijv. "evolutie" vs. "technieken") — zou de "Prompting Inversion"-paper zowel bij evolutie als bij technieken laten landen. Vermeden door brontype-splitsing te kiezen.

### Waarom
LLM-researchers neigen naar overlap als ze niet expliciet begrensd worden — ze willen "compleet" zijn en pakken alles wat raakt aan hun onderwerp. Door de complementaire scope (R1 pakt X niet want R2 doet dat) krijgt elke researcher vertrouwen dat gaten elders worden ingevuld.

## Toepassing

Bij elke `/deep-research` of `/parallel-agents` dispatch:

1. **Kies dimensies op perspectief/brontype**, niet op onderwerp-onderdelen. Het onderwerp blijft ongedeeld; de lens verschilt per researcher.
2. **Schrijf voor elke researcher een "Taakgrenzen"-sectie** die expliciet vernoemt wat anderen doen ("geen X want dat is R2").
3. **Reserveer één dimensie voor de cross-cutting concerns** (governance, ethiek, compliance) — die raken anders te breed aan alle andere dimensies.
4. **Eén ronde is vaak genoeg** als de dimensies disjoint zijn. Plan toch altijd voor de mogelijkheid van een tweede ronde voor gaten.
