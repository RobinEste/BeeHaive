---
id: bron-005
title: "Personal Context Management — Synthese en toepassing op Dynamic Context"
url: "https://youtu.be/yeTn8a5J-Gc"
author: "Tiago Forte (primaire bron) — synthese door Robin Bertus"
date: "2026-04"
archived: "2026-04-10"
bb_gr:
  - Dynamic Context
type: synthese
volledige_tekst: true
ingested: false
---

## Samenvatting

Tiago Forte introduceert **Personal Context Management (PCM)** als opvolger van Personal Knowledge Management (PKM). Een preciezere lezing is dat PCM een **operationele laag bovenop PKM** is: PKM = voorraadkast, PCM = mise-en-place. De bottleneck is verschoven van "een goede prompt schrijven" naar "de juiste combinatie van instructies, voorbeelden, documenten, tools, historie en state aanleveren" — wat Anthropic, Simon Willison, Tobi Lütke en Andrej Karpathy inmiddels **context engineering** noemen.

Voor BeeHaive's Dynamic Context-ruimte is deze synthese direct relevant: PCM geeft een gebruikerskant-narratief bij wat BeeHaive architectonisch wil oplossen. Het formaliseert waarom dynamische contextselectie geen technische optimalisatie is maar een nieuwe discipline, en welke valkuilen (monolithische master prompts, dogmatische expiry, Context Rot) BeeHaive expliciet moet adresseren.

**Kernpositie:** dynamische context draait om twee fundamenteel verschillende soorten — **persona-context** (traag, altijd geladen, laag volume) en **domein/taak-context** (snel, on-demand, hoog volume). Dat onderscheid ontbreekt in Tiago's eigen "master prompt"-framing en is de belangrijkste correctie in deze synthese.

## Relevante passages

### 1. Context engineering als nieuwe discipline

Context engineering vervangt prompt engineering als dominante term omdat het de volledige werkelijke opgave dekt: niet één slimme instructie, maar een dynamisch samengesteld pakket van (a) system instructions, (b) voorbeelden, (c) relevante documenten, (d) tool-definitions, (e) conversatie-historie en (f) runtime state.

Anthropic (bron-001): context als "critical but finite resource". Definitie: "het cureren en onderhouden van de optimale set tokens tijdens inference".

**Relevantie voor BB/GR Dynamic Context:** dit is de onderliggende theorie voor waarom Dynamic Context een eigen ruimte is naast Prompt Design.

### 2. Context Rot — de empirische grens van grote context windows

Onderzoek (*Lost in the Middle*, Liu et al.) laat zien dat modellen relevante informatie **niet robuust gebruiken** over lange contexten. Performance degradeert vooral wanneer cruciale informatie diep in het midden van de context zit.

**Nuance:** Tiago's specifieke cijfer "slechts 25–50% van het context window is bruikbaar" is **niet onderbouwd** door een primaire bron die het als algemene regel bevestigt. Wat wél onderbouwd is: contextkwaliteit weegt zwaarder dan contextvolume.

De drie geobserveerde failure modes (Anthropic):
- **Context poisoning** — één fout raakt obsessief gefixeerd
- **Context distraction** — irrelevante info verzwakt focus
- **Context confusion** — tegenstrijdige info verlamt beslissingen

**Relevantie voor BeeHaive:** Dynamic Context moet context-budgetten actief beheren, niet maximaliseren. Bundle-grootte is een ontwerpbeslissing, geen toevalligheid.

### 3. Twee fundamenteel verschillende context-soorten

Tiago's "master prompt"-framing vermengt twee dingen die verschillende load-patronen en review-ritmes hebben:

| | Persona-context | Domein/taak-context |
|---|---|---|
| **Inhoud** | waarden, stijl, SWOT, voorkeuren, rol | klantkennis, beleid, dossiers, casussen |
| **Verandering** | traag (kwartalen/jaren) | snel (dagen/weken) |
| **Volume** | laag | potentieel hoog |
| **Relevantie** | bijna altijd | selectief per taak |
| **Load-patroon** | altijd geladen | on-demand bundle |

**Relevantie voor BeeHaive:** deze splitsing moet architectonisch terugkomen. Eén monolithische "user profile" is een anti-patroon. Dynamic Context moet minimaal twee storage/load-paden ondersteunen — een persistent persona-laag en een dynamisch bundle-systeem dat per taak wordt samengesteld.

### 4. Alpha als AI-asset

"Alpha" = informatie die **niet** in de training data van LLMs zit. Concreet: lokale kennis, oraal overgedragen wijsheid, oude niet-gedigitaliseerde documenten, verborgen kennis in de hoofden van mensen, private datasets, besluitredeneringen die nooit zijn opgeschreven.

Persoonlijke notities worden hierdoor juist **waardevoller**, niet minder. Ethan Mollick adviseert expliciet om AI context te geven via documenten en persoonlijke achtergrond, en voegt toe dat hij dat vaak handmatig doet om redactiecontrole te houden.

**Relevantie voor BeeHaive:** BeeHaive's Dynamic Context is geen archief maar een **activeringsmechanisme voor alpha**. De waardepropositie is niet "alle kennis vindbaar" maar "jouw unieke kennis ingezet in AI-interacties". Dit verschuift het narratief van opslag naar operationele activering.

### 5. Review-ritmes in plaats van harde expiry

Tiago's "zes-maanden-venster" (alles ouder dan zes maanden is vrijwel nutteloos) is **niet onderbouwd** door primaire bronnen. OpenAI's memory-documentatie noemt recentheid en frequentie als factoren zonder harde halfwaardetijd. Anthropic waarschuwt wel dat aannames en harnesses verouderen als modellen verbeteren.

Praktisch: werk met **review-ritmes per bundle** (2 weken / 1 maand / 1 kwartaal / 1 jaar), gekoppeld aan een mechanisme dat stale bundles proactief oppakt.

**Relevantie voor BeeHaive:** bundles krijgen een `review_cadence` veld, geen `expires_at`. Dynamic Context beheert achterstallig onderhoud proactief, niet door automatische expiratie.

### 6. PKM versus PCM

- **PKM** gaat over kennis **vastleggen en terugvinden** — de voorraadkast
- **PCM** gaat over kennis **selecteren en activeren** voor een concrete AI-taak — de mise-en-place

Niet: PKM eruit, PCM erin. Maar: PCM is de operationele laag die PKM ontsluit voor AI-samenwerking.

**Relevantie voor BeeHaive:** Dynamic Context bouwt voort op bestaande knowledge-bases (notes, wiki's, dossiers). De ruimte vervangt geen PKM, het activeert PKM per taak.

### 7. Autonomie is overschat; oordeel en synthese zijn onderschat

Tiago stelt dat "agents grotendeels BS zijn" — AI's werkelijke sterkte zit in judgment, decisions, research en synthesis, niet in autonome executie. Dit is **te absoluut** (Anthropic laat zien dat multi-agent systemen nuttig zijn voor parallelle research), maar als correctie op hype en als prioritering voor persoonlijk gebruik is het verstandig: eerst oordeel en synthese, pas daarna meer autonomie.

**Relevantie voor BeeHaive:** Dynamic Context dient primair judgment en synthese, niet autonome executie. Deze positionering helpt bij feature-scoping.

## Kernquotes

> "Personal Context Management — the new bottleneck isn't intelligence, time, or attention. It's curating and delivering the right context to AI." — Tiago Forte, *AI Second Brain*

> "Context represents a critical yet finite resource. LLMs, like humans, lose focus when handling excessive information... context functions as a finite resource with diminishing returns." — Anthropic (bron-001)

> "When relevant information is placed in the middle of long contexts, models struggle to use it robustly. Performance is often best when relevant information appears at the beginning or end." — Liu et al., *Lost in the Middle*

> "Your notes are no longer just for you. They're training material for your daily AI collaboration." — parafrase van Tiago Forte's positionering van persoonlijke notities

> "PKM is de voorraadkast. PCM is de mise-en-place." — synthese-framing (deze bron)

## Open vragen

Uit de synthese, direct toepasbaar op BeeHaive's Dynamic Context ontwerpbeslissingen:

- Hoe meet BeeHaive effectieve contextbelasting per interactie zonder handmatig tokens te tellen?
- Welke bundle-granulariteit werkt in de praktijk — per klant, per domein, per rol, of een combinatie?
- Hoe onderscheidt Dynamic Context zich operationeel van bestaande PKM-tools (Obsidian, Notion, Evernote)?
- Wat is de juiste review-cadans voordat het review-mechanisme zelf een bron van achterstallig onderhoud wordt?
- Hoe borgt BeeHaive privacy bij bundles met PII (bijv. health/finance advisors) als modellen remote draaien?
- Hoe verhoudt persona-context zich tot user profile-systemen die al in veel apps bestaan?

## Toepassing op BB/GR Dynamic Context

Deze synthese levert zes concrete ontwerpprincipes voor BeeHaive's Dynamic Context ruimte:

1. **Splits persona en domein** — twee verschillende storage/load-paden, niet één master prompt
2. **Taakgerichte bundles** — minimum benodigd voor de taak, niet maximum beschikbaar
3. **Review-ritmes per bundle** — cadans op basis van veranderfrequentie, geen harde expiry
4. **Alpha-georiënteerd** — Dynamic Context is een activeringsmechanisme voor unieke kennis, geen archief
5. **Cross-platform bundles** — markdown/JSON, geen lock-in in een specifiek notitie-tool
6. **Privacy-bewuste load** — PII-bundles krijgen expliciete pre-load prompts en model-routering per privacy-klasse

## Referenties

Deze synthese integreert de volgende bronnen:

| Bron | Status in BeeHaive |
|---|---|
| Tiago Forte — *AI Second Brain* (YouTube serie) | Primaire bron voor PCM-concept — nog niet apart gearchiveerd |
| Anthropic — *Effective context engineering* | Al gearchiveerd als **bron-001** |
| Simon Willison — blogposts over context engineering vs prompt engineering | Nog niet gearchiveerd |
| Liu et al. — *Lost in the Middle* (arXiv 2307.03172) | Nog niet gearchiveerd |
| Ethan Mollick — *Co-Intelligence* + *One Useful Thing* | Nog niet gearchiveerd |
| OpenAI — ChatGPT memory documentatie | Nog niet gearchiveerd |
| Andrej Karpathy — publieke uitspraken over context als kernfactor | Nog niet gearchiveerd |
| Tobi Lütke (Shopify) — context engineering als cruciale skill | Nog niet gearchiveerd |

**Follow-up:** voor volledige BeeHaive-ingest is het aan te raden om minimaal Liu et al., Simon Willison (1-2 kernposts) en een directe Tiago Forte transcriptie als aparte bronnen toe te voegen. Deze synthese is het integrerende verhaal; de afzonderlijke bronnen leveren de empirische onderbouwing.

## Volledige originele tekst

> Dit is een synthese-bron, geen archief van één externe publicatie. De "volledige tekst" is deze synthese zelf (zie secties hierboven). Voor de primaire Tiago Forte uitspraken: zie de YouTube-serie in de frontmatter `url`. Voor de Anthropic onderbouwing: zie bron-001 in deze map.

### Aanleiding en methode

Deze synthese is opgebouwd op 2026-04-10 vanuit een analyse van Tiago Forte's *AI Second Brain* video-serie, aangevuld met cross-referentie naar Anthropic's context engineering publicatie, *Lost in the Middle*-onderzoek, en recente uitspraken van Ethan Mollick, Simon Willison, Tobi Lütke en Andrej Karpathy. De synthese is gemaakt voor twee doeleinden: (1) onderbouwing van een persoonlijk contextplatform binnen het claude-code-framework (PLAN-2026-021), en (2) input voor BeeHaive's Dynamic Context ruimte.

### Waarom dit relevant is voor BeeHaive

BeeHaive positioneert Dynamic Context als een van de bouwstenen van effectief AI-gebruik. De PCM-literatuur geeft daar een gebruikerskant-narratief bij dat tot nu toe ontbrak in de theoretische onderbouwing:

- **Voor productpositionering:** PCM geeft taal waarmee Dynamic Context zich laat uitleggen aan niet-technische gebruikers ("mise-en-place voor AI"). Dit is krachtiger dan "dynamische context injection".
- **Voor architectuur:** de splitsing persona/domein is een harde ontwerpconstraint. Een systeem dat alleen één master prompt ondersteunt, mist de helft van het probleem.
- **Voor roadmap:** review-ritmes zijn een feature, geen ops-taak. Dynamic Context heeft ingebouwde staleness-tracking nodig.
- **Voor concurrentiepositie:** alpha-georiënteerde activering onderscheidt BeeHaive van archief-tools (Notion, Evernote) en van memory-systemen van platform-vendors (OpenAI memory, Claude projects).

### Kernverschuiving die BeeHaive moet omarmen

De dominante framing van "AI helpen door betere prompts" is achterhaald. De werkelijke vraag is: **welke configuratie van context genereert het gewenste modelgedrag?**

Dat antwoord verandert per taak, per gebruiker, per moment. Statische "user profiles" of "system prompts" zijn daarvoor inadequaat. Dynamische bundle-selectie — samengesteld uit een altijd-geladen persona-kern plus taakspecifieke context-bundles — is het operationele antwoord.

### Wat dit betekent voor Dynamic Context MVP

Op basis van deze synthese zijn dit de minimumvereisten voor een eerste werkende versie van Dynamic Context binnen BeeHaive:

1. **Persona-storage** — persistente, gebruiker-specifieke kernidentiteit (waarden, stijl, rol, voorkeuren) die altijd in context wordt geladen. Beperkt in omvang (<500 woorden), handmatig te vullen, met versiegeschiedenis.

2. **Bundle-catalogus** — modulaire context-pakketten per domein/klant/rol, elk met eigen frontmatter (type, review_cadence, privacy_class, load_trigger).

3. **On-demand load-mechanisme** — expliciete API of UI om bundles te activeren per sessie, met token-budget preview voordat context wordt geïnjecteerd.

4. **Staleness-tracking** — proactieve detectie van bundles die hun review-cadans hebben overschreden, met workflow om bij te werken of te archiveren.

5. **Privacy-classificatie** — elke bundle krijgt een `privacy_class` (public / internal / pii) die model-routering en export-gedrag stuurt.

6. **Platform-agnostische storage** — bundles zijn markdown of JSON, leesbaar buiten BeeHaive, geen lock-in.

### Wat BeeHaive expliciet NIET moet overnemen uit Tiago's framing

- **De somatisch/emotieregulatie-laag** — past niet in een software-tool. Hoort in persoonlijke praktijk.
- **Cohort-didactiek (week 1/2/3 drie keer herbouwen)** — niet schaalbaar als SaaS-ervaring.
- **"Agents zijn BS"** — te absoluut; BeeHaive's roadmap mag best executie-agents bevatten voor narrow-scope taken.
- **Dogmatische expiry** — review-ritmes werken beter dan harde verval-datums.
- **Monolithische master prompt** — anti-patroon; persona + bundles is de juiste decompositie.

### Verbinding met andere BB/GR-ruimtes

Dynamic Context raakt direct aan:

- **Prompt Design** — persona-kern is een soort "standing system prompt"; de grens is vloeiend
- **Model Engines** — privacy-classificatie stuurt model-selectie (Tier 1 vs Tier 2, local vs remote)
- **Privacy** — PII-bundles vereisen expliciete handling die over beide ruimtes heen loopt
- **Evaluation Loop** — staleness-tracking en bundle-effectiviteit zijn meetbare metrics
- **Knowledge** — PKM blijft de voorraadkast; Dynamic Context is de mise-en-place erbovenop

### Open onderzoekslijnen

Voor een diepere ingest zijn dit de prioritaire vervolgstappen:

1. **Liu et al. — *Lost in the Middle*** archiveren als bron-006. Dit levert de harde empirische onderbouwing van Context Rot.
2. **Simon Willison context engineering posts** (1–2 kernposts) archiveren als bron-007. Levert de terminologie-onderbouwing.
3. **Tiago Forte directe transcriptie** (uit YouTube) archiveren als bron-008. Primaire quotes die nu alleen geparafraseerd zijn.
4. **Ethan Mollick hoofdstuk over persoonlijke AI-context** uit *Co-Intelligence* — als die bestaat — als bron-009. Levert het "persoonlijke notities als asset" narratief met naamsbekendheid.
5. **Interview met bestaande Obsidian/Notion power-users** die al handmatig PCM doen — als bron-010. Levert praktijkvalidatie van de persona/domein-splitsing.
