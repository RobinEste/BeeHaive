---
id: bron-007
title: "Lost in the Middle: How Language Models Use Long Contexts"
url: "https://aclanthology.org/2024.tacl-1.9/"
author: "Nelson F. Liu, Kevin Lin, John Hewitt, Ashwin Paranjape, Michele Bevilacqua, Fabio Petroni, Percy Liang"
date: "2024-01"
archived: "2026-04-10"
bb_gr:
  - Dynamic Context
  - Model Engines
type: paper
volledige_tekst: false
ingested: false
---

## Samenvatting

Peer-reviewed paper gepubliceerd in *Transactions of the Association for Computational Linguistics* (TACL, vol. 12, pp. 157–173, 2024) — oorspronkelijk op arXiv in juli 2023. Deze studie is de eerste systematische empirische onderbouwing van wat later populair bekend werd als **"context rot"**: taalmodellen gebruiken informatie in lange contexten **niet uniform**, en verliezen prestaties wanneer relevante informatie in het **midden** van de context staat.

**Kernbevinding — de U-curve:** performance is het hoogst wanneer relevante informatie aan het **begin** of **einde** van de context staat, en zakt significant wanneer modellen die informatie in het midden moeten gebruiken. Dit geldt zelfs voor modellen die expliciet ontworpen zijn voor lange contexten.

De auteurs testen dit op twee taken:
1. **Multi-document question answering** — het model krijgt meerdere documenten en moet de vraag beantwoorden met informatie uit één specifiek document. De positie van dat document wordt systematisch gevarieerd.
2. **Key-value retrieval** — een gecontroleerde synthetic test waarbij het model een waarde moet ophalen gegeven een key uit een lijst van key-value paren. De positie van het target-paar wordt gevarieerd.

**Implicatie voor context engineering:** context window grootte is niet hetzelfde als bruikbare context. Een model met een 100k+ token window kan feitelijk informatie in het middengebied missen, ook al past alles technisch gezien "erin". Dit valideert het principe dat **kwaliteit en positie** van context belangrijker zijn dan volume — precies het principe dat BeeHaive's Dynamic Context ruimte moet operationaliseren.

**Relevantie voor BeeHaive:** dit is de **primaire wetenschappelijke onderbouwing** onder alles wat bron-001 (Anthropic), bron-005 (PCM synthese) en bron-006 (Tiago Forte) beweren over context rot. Waar Tiago het cijfer "25–50% bruikbaar context window" noemt zonder bron, en Anthropic het als "critical but finite resource" framet, is deze paper de peer-reviewed studie die het effect **empirisch gemeten** heeft. Voor BeeHaive's positioning als serieus product in de Dynamic Context ruimte is deze bron onmisbaar als wetenschappelijke anchor.

## Relevante passages

### 1. De onderzoeksvraag

Het paper opent met de observatie dat moderne taalmodellen steeds grotere context windows adverteren, maar dat er relatief weinig bekend is over **hoe goed** ze die lange contexten daadwerkelijk gebruiken. De auteurs stellen een simpele vraag: als je een model veel informatie geeft, gebruikt het die informatie dan uniform? Of zijn er positionele effecten?

**Relevant voor BeeHaive:** dit is precies de vraag die elk Dynamic Context systeem moet beantwoorden voordat het bundle-grootte en bundle-volgorde kan ontwerpen. Zonder deze empirie wordt bundle-ontwerp giswerk.

### 2. De twee experimenten

**Multi-document QA:** de auteurs construeren een test waarbij een model een vraag moet beantwoorden op basis van meerdere documenten die tegelijkertijd in de context staan. Slechts één van die documenten bevat het daadwerkelijke antwoord ("het gouden document"). De positie van het gouden document binnen de lijst wordt systematisch gevarieerd — begin, midden, einde — terwijl de totale context-lengte constant blijft.

**Key-value retrieval:** een gecontroleerder experiment waarbij het model een lijst van JSON-achtige key-value paren krijgt en één specifieke waarde moet ophalen gegeven de bijbehorende key. Dit isoleert het positie-effect van eventuele semantische complexiteit die in QA-taken zit.

**Relevant voor BeeHaive:** de twee taken dekken samen zowel natuurlijke taal (multi-document QA) als gestructureerde retrieval (key-value). Beide patronen komen voor in real-world Dynamic Context toepassingen: bundles kunnen prose-context zijn (klant-context) of gestructureerde context (voorkeuren, instellingen).

### 3. De U-curve

De hoofdbevinding van het paper is een duidelijke **U-vormige performance curve**: modellen presteren het best wanneer het doel-document aan het begin of het einde van de context staat, en significant slechter wanneer het in het midden staat. Dit effect is robuust — het verschijnt in meerdere modellen, meerdere context-lengtes, en beide experimentele taken.

Dit patroon is vergelijkbaar met twee bekende cognitieve effecten uit de psychologie:
- **Primacy effect** — mensen herinneren het begin van een lijst beter
- **Recency effect** — mensen herinneren het einde van een lijst beter
- **Serial position effect** — de combinatie van beide geeft een U-curve

Dat taalmodellen dit patroon overnemen is niet verbazingwekkend (ze zijn getraind op menselijke tekst), maar het is wel een probleem voor hoe we aannemen dat ze lange contexten gebruiken.

**Relevant voor BeeHaive:** dit heeft directe ontwerpimplicaties voor Dynamic Context:
- Kritieke informatie moet **bewust** aan begin of einde geplaatst worden, niet willekeurig in het midden
- Bundle-ordering is een ontwerpvariabele, geen cosmetisch detail
- "Groot" context window betekent niet "gelijk benut" context window
- Samenvattingen of key-takeaways horen aan de randen, niet in het midden

### 4. Extended-context modellen lossen het niet op

Een bijzonder belangrijke bevinding: modellen die **expliciet** ontworpen zijn voor langere contexten (bijvoorbeeld 32k tokens in plaats van 4k) vertonen **hetzelfde U-curve patroon**. Ze hebben dus wel een technisch groter window, maar het middengedeelte ervan is nog steeds een "dode zone" in gebruik.

**Relevantie voor BeeHaive:** dit weerlegt de aanname "koop gewoon een groter model met groter window". Het probleem is architectureel/representationeel, niet enkel een kwestie van token-capaciteit. Dynamic Context moet als core principe aannemen dat **alle context windows onderhevig zijn aan positionele effecten**, ongeacht grootte.

### 5. Nieuwe evaluatie-protocollen

Het paper sluit af met het voorstel dat het veld nieuwe evaluatie-protocollen nodig heeft om long-context modellen te beoordelen. Een model dat technisch 100k tokens aankan maar informatie in het middengebied mist, faalt op een manier die standaard-benchmarks niet detecteren.

**Relevant voor BeeHaive:** als Dynamic Context claims wil maken over "we gebruiken je context effectief", dan is er een evaluatie-protocol nodig dat positionele effecten test. Dit is potentieel een **meetbare differentiator** voor het product.

## Kernquotes

> "While recent language models have the ability to take long contexts as input, relatively little is known about how well they use longer context." — Abstract

> "We analyze the performance of language models on two tasks that require identifying relevant information in their input contexts: multi-document question answering and key-value retrieval." — Abstract

> "We find that performance can degrade significantly when changing the position of relevant information, indicating that current language models do not robustly make use of information in long input contexts." — Abstract

> "In particular, we observe that performance is often highest when relevant information occurs at the beginning or end of the input context, and significantly degrades when models must access relevant information in the middle of long contexts, even for explicitly long-context models." — Abstract

> "Our analysis provides a better understanding of how language models use their input context and provides new evaluation protocols for future long-context language models." — Abstract

## Koppelingen met andere bronnen

- **bron-001 (Anthropic — Effective context engineering)** — Anthropic noemt "context rot" expliciet als onderzoeksbevinding ("research on needle-in-a-haystack benchmarking uncovered context rot"). Liu et al. is een van de canonieke papers die deze observatie empirisch onderbouwt. Bron-001 beschrijft de operationele implicaties; bron-007 geeft de wetenschappelijke basis.
- **bron-005 (PCM synthese)** — In de passage over Context Rot (sectie 2) wordt Liu et al. expliciet aangeroepen als onderbouwing van "modellen gebruiken informatie niet robuust over lange contexten". Bron-007 maakt die claim nu traceerbaar naar primaire wetenschap in plaats van parafrase.
- **bron-006 (Tiago Forte webinar)** — Tiago noemt "a paper" tijdens zijn context rot uitleg (~04:00–08:00) zonder expliciete citatie. Dit paper is vrijwel zeker wat hij bedoelt (of een opvolger die ernaar verwijst). Tiago's cijfer "25–50% bruikbaar context window" is **niet** rechtstreeks in Liu et al. te vinden — die specifieke getallen zijn Tiago's interpretatie/extrapolatie. Liu et al. toont het **patroon**, niet een exact percentage. Dat is een belangrijk onderscheid dat BeeHaive moet bewaren in z'n communicatie: het fenomeen is onderbouwd, het exacte percentage niet.

## Open vragen uit deze bron

1. **Is de U-curve modelafhankelijk?** — De paper test meerdere modellen, maar het is een momentopname uit 2023. Modellen zijn sindsdien aanzienlijk verbeterd. Is de U-curve zwakker of sterker geworden in 2024–2026 frontier-modellen? BeeHaive zou dit kunnen valideren via eigen metingen op Claude Sonnet 4.6 / Opus 4.6 / GPT-5.
2. **Geldt het effect ook voor niet-retrieval taken?** — De twee taken (QA, key-value) zijn beide retrieval. Wat gebeurt er bij synthese-taken, reasoning-taken of creative taken? Geldt de U-curve daar ook, of heeft dan positie minder invloed?
3. **Werkt re-ordering als mitigatie?** — Als je kritieke informatie expliciet aan begin en einde zet (met herhaling/samenvatting), compenseer je de U-curve dan volledig? Gedeeltelijk? Dit is een direct actionable BeeHaive onderzoekslijn.
4. **Zijn er context-budgetten per positie?** — Als begin en einde "hoogwaardige" posities zijn en midden "laagwaardig", kun je dan een bundle ontwerpen met een **positioneel gewogen budget** in plaats van een flat token-telling?

## Volledige originele tekst

**Let op:** deze bron archiveert **alleen de abstract en metadata** van de paper. De volledige tekst is een peer-reviewed academisch artikel (TACL 2024, 17 pagina's) en is open-access beschikbaar via de ACL Anthology en arXiv:

- **ACL Anthology (open access, HTML + PDF):** https://aclanthology.org/2024.tacl-1.9/
- **arXiv preprint (v3, november 2023):** https://arxiv.org/abs/2307.03172
- **DOI:** 10.1162/tacl_a_00638

### Citatie (BibTeX-stijl)

```
Liu, N. F., Lin, K., Hewitt, J., Paranjape, A., Bevilacqua, M.,
Petroni, F., & Liang, P. (2024).
Lost in the Middle: How Language Models Use Long Contexts.
Transactions of the Association for Computational Linguistics, 12, 157–173.
https://doi.org/10.1162/tacl_a_00638
```

### Volledige abstract (verbatim)

> While recent language models have the ability to take long contexts as input, relatively little is known about how well they use longer context. We analyze the performance of language models on two tasks that require identifying relevant information in their input contexts: multi-document question answering and key-value retrieval. We find that performance can degrade significantly when changing the position of relevant information, indicating that current language models do not robustly make use of information in long input contexts. In particular, we observe that performance is often highest when relevant information occurs at the beginning or end of the input context, and significantly degrades when models must access relevant information in the middle of long contexts, even for explicitly long-context models. Our analysis provides a better understanding of how language models use their input context and provides new evaluation protocols for future long-context language models.

### Archivering status

- `volledige_tekst: false` — alleen abstract gearchiveerd, niet de volledige paper
- **Reden:** academische PDFs zijn onpraktisch om inline in een markdown-bron te archiveren; de primaire bronnen (ACL Anthology, arXiv) zijn open-access en stabiel
- **Vervolgactie indien nodig:** de volledige PDF kan lokaal opgeslagen worden in `docs/research/bronnen/pdfs/liu-2024-lost-in-the-middle.pdf` zonder deze markdown-bron te vervuilen. Dit is aan te bevelen als BeeHaive eigen meting wil doen tegen het experimentele protocol van het paper
- **Inhoudsvolledigheid:** voor Dynamic Context design-beslissingen zijn de abstract, kernbevindingen en implicaties voldoende. Voor herproductie van experimenten is de volledige paper nodig
