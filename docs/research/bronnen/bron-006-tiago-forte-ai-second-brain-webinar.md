---
id: bron-006
title: "AI Second Brain — Roadmap webinar (PCM cohort kickoff)"
url: "https://youtu.be/yeTn8a5J-Gc"
author: "Tiago Forte (Forte Labs)"
date: "2026-03"
archived: "2026-04-10"
bb_gr:
  - Dynamic Context
  - Prompt Design
  - Knowledge
type: webinar
volledige_tekst: true
ingested: false
---

## Samenvatting

Live webinar (~1u25m) waarin Tiago Forte de roadmap van zijn AI Second Brain cohort pitcht. Kernthese: de bottleneck in kenniswerk is verschoven van tijd/aandacht/intelligentie naar het **verzamelen, cureren en leveren van context** aan AI. Hij introduceert **Personal Context Management (PCM)** als nieuwe discipline en presenteert een stack — **CODE → PARA → Master Prompt → AI Board of Advisors** — als operationele invulling.

Belangrijke punten voor Dynamic Context:

1. **Context rot is een hard technisch feit** — effectief gebruikbare context is ~25–50% van de geadverteerde window (30–50k woorden). Drie failure modes: poisoning, distraction, confusion.
2. **Bundles of context** — je kunt niet "alles dumpen"; je moet het minimum benodigd voor de taak selecteren.
3. **Master prompt + modulaire sub-bundles** — een horizontale altijd-geladen laag (persoonlijke details, rol, doelen, SWOT) plus verticale bundles per domein (health, finance, relatie, project).
4. **Alpha-inventarisatie** — waarde zit in informatie die *niet* in AI's training data zit: lokale kennis, oude documenten, mondelinge overdracht, niet-gedigitaliseerde bronnen.
5. **Auto-update van master prompt** — Tiago doet dit via Claude Code: "update my master prompt based on my latest notes". Middenweg tussen volautomatisch en handmatig: voorstel wijzigingen, flag high-stakes items, rest automatisch.
6. **PARA als organisatie-principe dat zowel mensen als AI begrijpen** — "you need an organizational system that makes sense for both humans and AI."

Daarnaast vijf contrariane stellingen die zijn positionering definiëren: dit is moeilijk (niet easy), notes zijn belangrijker dan ooit (vanwege alpha), agents zijn grotendeels BS (niet klaar voor executie), de echte frontier is intern (zelfkennis, emotieregulatie), en weiger de urgency (decennia, niet maanden).

## Relevante passages

### 1. De nieuwe bottleneck (00:00–04:00)

Tiago vraagt de kijker zich voor te stellen hoe het zou zijn als tijd, aandacht of intelligentie geen beperkingen meer waren. Zijn stelling: **de bottleneck is verschoven** naar het verzamelen, cureren en leveren van context aan AI. Dit is een nieuwe skill — Personal Context Management — die niet intuïtief is en geleerd moet worden.

Hij framed persoonlijke context (notes, expertise, ervaring, relaties, perspectieven) als "a treasure trove of data that no one else has". Dit is volgens hem de enige manier om te ontsnappen aan wat hij de **mediocrity trap** noemt: AI trekt iedereen naar het gemiddelde omdat het getraind is op alles wat er op internet staat.

### 2. Context rot en context window limieten (~04:00–08:00)

Expliciete uitleg van het context window als "working memory" / RAM van een LLM. Tiago stelt dat geadverteerde 1M/2M token windows "lies" zijn — het effectieve bruikbare deel is volgens hem **25–50% van wat geclaimd wordt**, wat neerkomt op 30–50k woorden.

Drie failure modes:
- **Context poisoning** — één fout/inconsistentie raakt obsessief gefixeerd
- **Context distraction** — irrelevante info verzwakt focus
- **Context confusion** — tegenstrijdige info verlamt beslissingen

**Relevant voor BeeHaive:** de 25–50% claim is niet breed onderbouwd in primair onderzoek (zie bron-005 voor nuance), maar de failure modes zelf zijn wél empirisch gedocumenteerd in bron-001 (Anthropic). Gebruik Tiago voor framing, gebruik Anthropic/Liu et al. voor harde onderbouwing.

### 3. CODE → PARA → Master Prompt → AI Advisors (~08:00–12:00)

De stack die Tiago presenteert als fundament voor de AI Second Brain:

1. **CODE** (Capture, Organize, Distill, Express) — pre-AI fundament uit zijn boek *Building a Second Brain*. Skelet van de creative workflow.
2. **PARA** (Projects, Areas, Resources, Archives) — organisatie-principe uit *The PARA Method*. Kritisch quote: *"you need an organizational system that makes sense for both humans and AI."*
3. **Master Prompt** — vervangt de oude "distillation" stap. Platform-agnostisch document met persona, values, workflows, voorkeuren.
4. **AI Board of Advisors** — verticale specialisten per levensdomein met eigen context-bundles.

**Relevant voor BeeHaive Dynamic Context:** PARA is het organiserende principe dat Tiago expliciet koppelt aan menselijke én AI-leesbaarheid. Dit is een directe input voor hoe bundles in een Dynamic Context-systeem gestructureerd kunnen worden.

### 4. Master prompt demo in Claude (~13:00–19:00)

Tiago toont zijn eigen opstelling in Claude desktop:
- Een **Project** in Claude met één file: zijn work master prompt
- Het file gebruikt "1% van project capacity" — expliciet token-budget bewustzijn
- Inhoud: personal details, company info, AI strategy, ICP, products, mission/vision, core values, brand voice, org chart, processes, value chain
- Demo-vraag (via WhisperFlow voice): *"With everything that you know about me, what is the biggest single gap in our product offerings?"*
- Claude antwoordt specifiek: "You have no scalable high-touch offering that doesn't require Tiago's direct involvement" — Tiago bevestigt dat dat klopt

**Relevant voor BeeHaive:** concrete demonstratie dat gecureerde context leidt tot scherpe, bruikbare output die generieke prompts niet kunnen leveren. Validatie van het "context als onderscheidend vermogen" narratief.

### 5. Auto-update van master prompt (~19:00–21:00)

Tiago's workflow voor onderhoud:
> *"Every week or two weeks or three weeks or whenever, I give it access to my notes and I say: based on all of my latest notes across all my current projects, all the areas of responsibility, all the resources, if there's any new ones or any new archives, update my master prompt. And it did that in a few minutes. I went and heated up my coffee, came back, and it was done."*

Later in de Q&A verfijnt hij: volledig automatisch update is riskant (kan incorrecte aannames opnemen), volledig handmatig is te duur. Zijn voorkeur: **"go ahead and propose a set of changes, flag the most high-stakes ones for me so that I can say yes or no, and then once I do, go ahead and do them"**.

### 6. Master prompt is niet statisch; hij breekt snel (Q&A ~37:00)

> *"That's probably the very first thing that will break in your master prompt. It will go outdated within like forty-eight hours. Because that's the pace of modern life."*

**Relevant voor BeeHaive:** staleness is een core concern, niet een edge case. Review-mechanismen horen tot de MVP, niet tot een latere fase.

### 7. Gefaseerde didactiek — zelfkritiek op vorige aanpak (~21:00–25:00)

Tiago's expliciete reflectie: *"there was a big mistake that I made... I imagined the ideal system... and then I said, let me teach this ultimate system to everyone. The problem with that approach is that the fully mature system is not how you start."*

Rectificatie: dezelfde system drie keer bouwen in drie weken:
- **Week 1 — Foundational** — MVP master prompt. Genoeg voor 60–70% van alle interacties. Ook voor gevorderden nuttig als fallback.
- **Week 2 — Intermediate** — opbreken in modulaire bundles per domein. *"Imagine your master prompt as a whole collection of different documents. And you only load up the ones that you need when you need them."*
- **Week 3 — Advanced** — long-term memory, sub-agents, integraties, harnesses.

**Relevant voor BeeHaive:** MVP-first denken valideert een gefaseerde Dynamic Context roadmap. De "modulaire bundles" uit week 2 zijn precies wat een BeeHaive-achtig product moet ondersteunen.

### 8. Privacy als calculated trade-off (Q&A ~33:00)

> *"It's nuanced. The single answers that you get these days are very black and white. Give AI everything, no problem, YOLO — and the other extreme is no, AI is inherently evil. Pretty sure there's some middle ground there... it's a trade-off like everything."*

Hij benoemt dat privacy implicaties heeft voor tool-keuze, permissies, en wat je überhaupt aan een tool geeft. Directe parafrase van een deelnemer: "security in the AI era is a calculated risk".

### 9. Work vs. persoonlijk scheiden (Q&A ~38:00)

Tiago's eigen aanpak: **aparte master prompts** voor werk en persoonlijk, **in hetzelfde Claude-account**. Dat geeft "always a little bit of bleeding in and out". Hij introduceert de term **context stack**:

> *"Imagine a pyramid where there's different layers of context. The ones that are more foundational influence all of your AI interactions... but then there's higher levels where it starts to become something that you can turn on or off."*

**Relevant voor BeeHaive:** dit is een directe voorloper van de persona/domein-splitsing uit bron-005. Foundational laag = altijd geladen; higher layers = on-demand.

### 10. Vijf contrariane stellingen (~42:00–52:00)

1. **Dit is moeilijk** — "every day I see AI influencer after AI influencer just either say or imply that it's easy... it's not". Tiago claimt dat werken met AI juist *meer* cognitieve energie kost vanwege architectuurbeslissingen.

2. **Note-taking is belangrijker dan ooit** — introductie van **alpha** als concept uit investing: informatie die anderen niet hebben. Voor kenniswerk = informatie die niet in AI's training data zit. Concrete voorbeelden: lokale geschiedenis, oude niet-gedigitaliseerde boeken, info in hoofden van mensen, video/audio dat nog niet geïngest is.

3. **Agents zijn grotendeels BS** — harde stelling: *"they're so not ready... the online hype cycle is putting far too much attention on automation and execution."* Concreet voorbeeld: AI verwijderde per ongeluk een meeting met 30 genodigden tijdens een simpele calendar check. Zijn positie: focus op **judgment, decisions, research, synthesis** — "the realm of pure information where it doesn't have to interact with anyone or anything outside of your computer."

4. **De echte frontier is intern** — *"I really think the true frontier is inside our minds and bodies."* Zelfbewustzijn, emotieregulatie, nervous system-regulatie bepalen volgens hem of AI over tijd een positieve of negatieve kracht wordt.

5. **Weiger de urgency** — *"I've been alive long enough that I have seen multiple technology waves, and this is what they always say... this is going to take decades. It's going to play out for the rest of our lives."* Tiago weigert apocalyptisch denken en fear-based urgency.

### 11. Zes-maanden-venster voor AI-relevantie (~55:00)

> *"I went through months or even years of notes and notion docs and experiments. There was like a six-month window. Only things about six months old were relevant. Everything that was more than six months older was zero relevance, zero usage."*

**Relevant voor BeeHaive:** dit cijfer is niet hard onderbouwd (zie bron-005 voor nuance), maar illustreert dat Tiago zelf **review-intervallen** als core discipline ziet. Voor een product betekent dit: staleness-tracking is geen luxe-feature.

### 12. Alpha-scan in de praktijk (Q&A ~1:09:00)

Tiago's voorbeeld van lokale geschiedenis in zijn Mexicaanse woonplaats:
> *"It has a really rich history that goes back almost 500 years, and none of it is digital. You can't find it online. I've tried asking every AI platform... At first I was annoyed. But as I thought about it, I'm like, this is an incredible opportunity."*

Hij gebruikt AI om oude Spaanse documenten te vertalen, bouwt een blogpost rond 500 jaar lokale geschiedenis, gebruikt het voor community building via een non-profit. ROI is niet financieel maar **connectie, nieuwsgierigheid, conversatie**.

Andere alpha-voorbeelden die hij noemt: conversaties met vrienden, jeugdherinneringen, oude home videos, ervaringen die nooit zijn opgeschreven.

### 13. Health en finance als hoogste persoonlijke ROI (~1:12:00)

Volgens Tiago zijn de twee grootste wins uit zijn eigen AI Board of Advisors:

**Health advisor** — cross-references tussen supplementen, voeding, workouts. Concreet voorbeeld: "you're taking that supplement, but you're also having that protein after your workouts. This ingredient and that protein are counteracting, making it so you can't absorb that supplement."

**Financial advisor** — als alternatief voor dure financial advisors die een percentage van assets onder management nemen. Tiago claimt dat hij misconcepties over retirement accounts, 529 accounts en risicodefinities heeft gecorrigeerd via AI. Concreet impact: "significantly changed how we save, how we invest, how we give, how we donate."

**Waarom master prompt tekortschiet voor deze domeinen:**
> *"Your master prompt is very horizontal — across every AI interaction. But if you have a certain domain of your work or life, like health, like finances... one vertical slice — your master prompt won't have anywhere near enough context."*

**Relevant voor BeeHaive:** dit is de directe motivering voor verticale bundles. De horizontale master prompt is de basis, maar echte waarde ontstaat pas bij diepe verticale bundles per domein.

### 14. We worden allemaal middle managers van AI (~1:19:00)

> *"Middle management is going away? Maybe so, but we're all going to become middle managers now. We're all middle managers of our own team of AI agents. And as any manager will tell you, people go through an incredible transformation to become managers — to lead, to delegate, to coach, to guide, to see things from different perspectives."*

Opmerkelijk: Tiago noemt dit expliciet als "golden age voor ADHD en neurodivergente mensen" — multitasking tussen meerdere cloud code sessies wordt een kernvaardigheid in plaats van een beperking.

## Kernquotes

> "There's a new bottleneck in modern productivity. It's no longer your time. It's collecting, curating and providing context, which is really just information, to increasingly powerful generations of artificial intelligence tools. Which is a skill. It's not obvious how to do this. It's a discipline that we're calling PCM, personal context management." — Tiago Forte (~01:30)

> "Your AI can only make use of what you give it. Your personal curated context — your notes, your knowledge, your expertise, your experience, your memories, your points of view, your perspectives, your relationships, your network — all the stuff that makes you you. Is now not just this little weird productivity habit. It's a treasure trove." — (~02:30)

> "Everything with AI pulls you towards the average. The way that it thinks, the way that it writes, the way that it works through problems, it's constantly sort of homogenizing your thinking. Because it's trained on the entire internet, everyone else's ideas and opinions. You can't stand out. You can't really have a competitive advantage if you allow yourself to be pulled into that average level of quality, that mediocrity." — (~03:30)

> "You cannot just dump everything in. I wish you could. You have to selectively curate. The right — I think of them as bundles of context. The minimum amount of context that you need to accomplish the task at hand." — (~07:30)

> "You need an organizational system that makes sense for both humans and AI. You can have AI create a completely custom, bespoke organizational system that perfectly fits how it thinks. But if it doesn't fit how you think, then you've created a system that you can't actually make use of." — (~10:00)

> "Think of a master prompt as your personal operating manual for AI — for all AI. It's a completely cross-platform, platform agnostic way of working with AI. It's not limited to any one platform." — (~12:30)

> "Every week or two weeks, I give it access to my notes and I say: based on all my latest notes across all my current projects, all the areas of responsibility, all the resources, update my master prompt. I went and heated up my coffee, came back, and it was done." — (~19:30)

> "Alpha is a kind of information that other people don't have. That same idea is coming to all knowledge work. There are pieces of information that are not known to AI — information that is only in certain places at certain times, in certain people's heads, in old books that have not been digitized, in formats that are harder for AI to ingest. If you can find them and capture them in your notes, you have a disproportionate advantage." — (~44:00)

> "Agents are largely a bunch of BS. They're so not ready. What AI can do, what it's more than ready to do, is judgment — or rather helping you with your judgment. It's decision-making, making better decisions. It's researching, synthesizing research, finding the gaps in research. The realm of pure information where it doesn't have to interact with anyone or anything outside of your computer, which is where it starts to go wrong." — (~46:00)

> "I really think the true frontier is inside our minds and bodies. It's not about the tools. It's not about the features. It's not about the technology. Over the long term, this is what's going to determine if AI is a force for good in your life, or if it's a negative force." — (~48:30)

> "Your master prompt is very horizontal. But if you have a certain domain of your work or life — like health, like finances — one vertical slice, your master prompt won't have anywhere near enough context. For those vertical slices, you have to go really deep on just that slice." — (~1:15:30)

> "We're all going to become middle managers now. We're all middle managers of our own team of AI agents. People go through an incredible transformation to become managers — to lead, to delegate, to coach, to guide, to see things from different perspectives." — (~1:19:30)

## Koppelingen met andere bronnen

- **bron-001** (Anthropic — Effective context engineering) — levert de harde technische onderbouwing voor wat Tiago intuïtief beschrijft. Failure modes (context rot, poisoning, distraction, confusion) overlappen. Anthropic's "critical but finite resource" = Tiago's "you can't just dump everything in".
- **bron-005** (PCM synthese) — integreert deze webinar met nuance vanuit Anthropic, Liu et al., Mollick en anderen. Corrigeert Tiago's onderbouwde claims (25–50% window, zes-maanden-venster) en voegt de persona/domein-splitsing toe die Tiago impliciet benoemt via de "context stack"-metafoor (~38:00).

## Open vragen uit deze bron

Expliciet onbeantwoord gelaten door Tiago tijdens de webinar (veel verwezen naar latere cohort-sessies):

1. **Privacy-architectuur** — welke data hoort in welke laag van de context stack? Hoe scheid je work/personal zonder dubbele accounts? Tiago noemt alleen zijn eigen aanpak (twee master prompts, één account) zonder principiële richtlijnen.
2. **Auto-update betrouwbaarheid** — hoe detecteer je dat een auto-update incorrect is? Tiago beschrijft "flag high-stakes" maar niet hoe "high-stakes" gedefinieerd wordt.
3. **Alpha-identificatie als proces** — Tiago geeft voorbeelden maar geen systematische methode. Hoe bouw je een herhaalbaar proces om alpha te detecteren in je dagelijkse leven?
4. **Context stack als primitive** — de pyramide-metafoor blijft schets. Welke lagen zijn er precies? Hoe beslis je waar iets thuishoort?
5. **Skills vs master prompt** — Tiago noemt in de Q&A dat skills delen van je master prompt vervangen ("you'll notice some stuff shouldn't be there. It should be skills"). Maar wanneer is iets een skill vs. een bundle vs. een master prompt-entry?

## Volledige originele tekst

**Speaker 1 (00:00)**
So as I said, I want you to have a roadmap, a high-level roadmap, of what the AI second brain system, the system that we talk about, looks like. And how, if, assuming you want to learn alongside us what that might look like, how it works. All right? I don't have that many slides. I think I have like 25 or 26. There's going to be plenty of time for us to interact. That's kind of one of the main benefits of this format. In the cohort itself, we do breakout rooms, we do coaching, we do a lot of different things. In today's call, just because it's so large, it will be mostly questions that we will interact with via the chat. So I'll have two separate times for you to ask questions in the chat. You can put questions anytime and we'll do our best to answer them, but I will specifically turn to questions in the middle after about 45 minutes or so and then at the end for the last 15 to 20 or 30 minutes. Okay? So save your hardest questions for me.

But first, let's get on the same page. So a few kind of observations and perspectives here. To kind of set the stage, set the context. I really believe that there's a new bottleneck in modern productivity. There's a new constraint. It's no longer your time. So just think of first line, think about this for a sec. Think about your career. Think about your life. Your life experiences. And just imagine for a sec, even not even to do with AI, just set AI aside. Can you even imagine what it means to have your time, the time you have available, not be a bottleneck? Just try to imagine. Imagine if you had infinite time. If time was not a factor, time was not a limitation. It's almost as if you could pause time for as long as you needed and spend as much time as was needed on whatever you wanted to create or learn or experience, anywhere you wanted to travel, anyone you wanted to meet. It's like really an imagination challenge here.

Imagine what it would be like to have your attention not be a bottleneck. Your attention, your ability to focus, your attention span, your ability to pay attention to things that are hard or complicated or boring. What would you do with that mind of yours, with that creativity, if attention was not a bottleneck? And then intelligence. What if your intelligence even was not a bottleneck on what you could create, achieve, experience, the impact you could have. Not your natural talents that you were born with, your IQ, your EQ, even, all those natural traits. What if those were just not a limitation anymore?

And imagine, or just consider that the bottleneck has moved. The bottleneck has moved to collecting, curating and providing context, which is really just information, to increasingly powerful generations of artificial intelligence tools. Which is a skill. It's not obvious how to do this. It's a skill. It's a discipline that we're calling PCM, personal context management. A brand new skill in the world that if you can master, you can get around this bottleneck.

So thinking about you as the human in all this, don't want to forget about that part. Consider that your AI, all your different AI tools can only use, they can only make use of what you give it. What you give it, your personal curated context, your notes, your knowledge, your expertise, your experience, your memories, your points of view, your perspectives, your relationships, your network, all the stuff that makes you you. Is now not just this little weird productivity habit you have. It's a treasure trove. It's just an incredibly valuable treasure trove of data that no one else has. No one else can access, no one else can compile, no one else can generate. That context, I believe, is the only way that you escape the disruptive changes that are coming, that you escape competition, that you create a real competitive advantage that doesn't get eliminated with the next AI release.

I call it the mediocrity trap. Everything with AI you may have noticed kind of pulls you towards the average. The way that AI thinks, the way that it writes, the way that it works through problems, it's constantly sort of homogenizing your thinking. And that's because it's trained on the entire internet, everyone else's ideas and opinions and everything they've ever said. You can't stand out. You can't really have a competitive advantage if you allow yourself to be pulled into that average level of quality, that mediocrity.

I published a video a few months ago, maybe someone on the team could drop that in the chat, which was exploring some research that has been done on something called context rot. Okay, so imagine — actually before I go there, there's something called a context window. Okay, we're gonna start at the very very beginning. I'm not gonna assume that you know anything about how these AI platforms, which are known as LLMs, large language models work.

So your context window, the AI's context window, is how much information it can work with. You can think of it almost like its working memory or its RAM. So you can give an LLM 10,000 words or tokens, 50,000, 100,000, but at a certain point it quits. At a certain point there's an error. I'm sure you've come across this. "You have exceeded the context window." So without getting too technical here, what you really need to understand is context windows have limits. They are not infinite. Not even close. Even with the latest AI models that say, oh, a million token context window, two million context window — those are lies. As this paper really proves and explains, the effective context window, how much you can actually give to these AI platforms, is really only maybe 25 to 50% of what they claim. That comes out to something around 30 to 50,000 words.

Okay, so even if they say a million words, two million, five million words — if you exceed around 30 to 50,000 words or in AI speak tokens, you start having these negative impacts, which is what this paper documents. You start having context poisoning. Context poisoning is one little error, one little mistake, it poisons the whole interaction with AI. It's like it gets fixated, obsessed with this one error, and it can't let it go. I'm sure you've experienced this. Or context distraction. If there's too much in the context that you give the AI that is not relevant to the task at hand, it gets distracted, just like humans. It gets fragmented. It's paying attention to the wrong things. It's getting distracted, just very much like humans do. And then there's context confusion. These are all kind of failure modes that the research has documented. Context confusion is when there's things that conflict. What is the AI supposed to do if you have two pieces of information that are either inconsistent or directly contradictory or incompatible, which I guarantee you will happen the more context that you try to give it?

So setting aside all this new terminology and these numbers — that little warning sign down there at the bottom right is what I want you to take away from this. **You cannot just dump everything in.** I wish you could. I wish you could just say, here, here's my hard drives, my computer, my cloud drives, here's all my logins, just access it all, make sense of it all, organize it all. You really cannot. You have to selectively curate the right — I think of them as bundles of context. **The minimum amount of context that you need to accomplish the task at hand.** And that might seem like just a random technical detail, but it's huge. It's so important because it means that all the stuff that we had to do and that we learned pre-AI — how to organize, how to curate, how to select, how to take notes, how to structure — all those things are still important. They're even more important because you have to do them to take advantage of AI's power.

So zooming out for a second, what is this AI second brain? It's the same as it always was. Going back with my work over 10 years now — and really if you look at the history of what we call PKM, that's personal knowledge management, it goes back decades to the early years of the 20th century. It's a system designed to amplify you. It's a system that lives outside your head, outside your body, that is designed to amplify you. To unlock your creative potential and ultimately at the grandest scale to unlock your ability to lead a thriving generative life. So we're using generative AI to lead a generative life.

And this graphic on the right is kind of the 50,000 foot view of how we're gonna do this. It's been amazing to me. It's been so surprising that all the techniques and the skills that came pre-AI not only are still relevant, they're more important than ever. So at the bottom there we have CODE. That is the core method that I talked about in my book, *Building a Second Brain*. Okay, so that really is centering your creative process, your productive process, getting information in — which is the C, capture — organizing it, that's the O — distilling it — and then expressing it. That has to be the foundation. Ultimately you're trying to put something out there — to publish something, communicate something, launch something, sell something. There's an expression at the end.

To do that, we build this new layer on top, which is PARA, which is a way to organize your entire digital life. That was explained in my book, *The PARA Method*. Because you need certain kinds of information to express whatever you're trying to express. You have Projects, that's the P. You have Areas of responsibility, both at work and in your personal life, that's the A. You have a wide variety of Resources, that's the R, and you have Archives, that's the second A. Okay. So those two methodologies, CODE and PARA, at this point are very well distributed. In fact we'll send you some links. There are the books themselves, but if you don't want to read a book there's YouTube videos, there's the podcast, there's many blog posts. In whatever format you like to learn, there is a way for you to learn those two methodologies.

But we're adding a new one. We're adding this new layer that is building on, it is extending those pre-AI capabilities, but with this new generation of technology that we call AI.

All right. So let's zoom in a bit. How does this AI-powered second brain work? So I always like to think of it like a system, like almost a mechanical system. Like if this was a manufacturing line or a water treatment plant — how do the actual bits of information flow from one place to another and how does that add value to my life?

So the four main parts that we're going to talk about in the program that we're teaching — and this is also going to find its way into everything else that we do — is in four parts. So the first one, as ever, as always, is **capture**. You need a way to capture information. That's where it all starts. Capture notes, capture ideas, capture insights, highlights from your reading. Now there's new ways to do that with AI. You can have an AI note taker now, you can do voice transcription, there's a lot of really powerful AI capture tools, but you still need to think about it. There's still some decisions to be made. How do I want to capture information? What is the way of capturing that fits me?

Once you've captured it, as before, this part also hasn't changed, is you want to **organize it**. And that's where PARA comes in. And the key thing with PARA that I'll point out here: **you need an organizational system that makes sense for both humans and AI.** This is the key point. You can have AI create a completely custom, bespoke organizational system that perfectly fits how it thinks. But if it doesn't fit how you think, then you've just created a system that you can't actually make use of. PARA not only is really well proven and well-validated, it's simple enough and it's straightforward enough that AIs can understand it perfectly, and so can humans. That's the key criteria.

Now this is where it changes. Instead of going to distillation, which was quite a manual, labor-intensive process, the information in PARA that you've organized now flows into what we call a **master prompt**. I'm going to say a lot more about that in just a minute. But it's basically that curated context that you provide to AI that I was mentioning before. Then that master prompt (or those master prompts plural) flow into and inform what I think of as a set of **AI advisors**, like an AI board of advisors. Imagine if you had a coach and a business consultant and a strategic analyst and then also a relationship coach and a health coach. All the people that if you had unlimited money you would hire to help you, you can now have with AI. But it requires some design.

All right. So I want to say a little bit more about the master prompt because this is really the core thing. **What is a master prompt? You can think of a master prompt as your personal operating manual for AI, for all AI.** All the different — you probably have half a dozen or a dozen different AI tools you work with. So this is a completely cross-platform, platform agnostic way of working with AI. It's not limited to any one platform.

Imagine a document — like any document. A .txt, a markdown, a Word document, a Google Doc — just a single long document that has some of these little bubbles. As I read each of these, imagine your interactions, whether it's with Claude or Gemini or ChatGPT or Notebook LM or Perplexity or whatever it is. Imagine if that AI knew:

- Your basic personal details — who you are, your name, age, where you live, who's in your family
- Your basic professional info — job, title, role, team, who you report to, who reports to you
- Your income sources — for money-related questions. Wouldn't it be useful if it knew how much money you make, your investments, your risk tolerance, your savings?
- Your core values — not company values, you as an individual
- Your vision, your mission, your intentions for AI usage
- Your communication preferences — how you like to communicate and collaborate
- Your working style, tool preferences, workflows, rules, boundaries
- Your goals and intentions (twice, because they're so important)
- Your personal SWOT — strengths, weaknesses, opportunities, threats
- Your skills, what quality looks like to you

I know this might seem like a lot. When I talk to people, even people who are very deep in AI, who have very sophisticated systems, I'd say 99% of the time when I ask them if they have this kind of information provided to their AI tool of choice, the answer is no. I kind of can't believe that after all this time, we still largely don't do this.

All right, let me show you. This is my Claude. This is the desktop app for Mac. What you're looking at — let's make this very simple. I'm clicking over here on the left where it says Projects. A project is simply a little self-contained, almost think of it like a folder, that is kind of self-contained. Everything that happens within that little container is limited to that container. So I have one for the book I'm writing, for the upcoming cohort, for the company as a whole, for my writing, for a different program that we run — each little self-contained box.

So the one I want to go into is "Tiago's Work Master Prompt". I have a different one for my personal life because I don't want them to bleed over into each other. But if I click into that — this is the project interface. The main thing I want you to notice is this little box over here that says Files. This is that curated context that I was talking about. They're also known as project files. There's only one file. You can have any number of things. You can see this one document is only using 1% of my project capacity, so that's good to know. I could add lots of other things. But if you click on this, you'll see my work master prompt.

All right, so you have basic personal details about me, where I live, company information, our AI strategy, our ideal customer profile, our core products that we offer, the company mission, the company vision, the core values of the company, the business strengths. A lot of this is very business oriented, but I have something similar with my personal master prompt. I have the weaknesses of the business, examples of our brand voice, the org chart, some of our internal processes, our strategic and operational process architecture, our core value chain, how we serve customers, etc.

With that master prompt as context, I can ask it something like: *"With everything that you know about me, what is the biggest single gap in our product offerings and what would you propose in order to address it?"* (The reason I could speak that, by the way, is I use an app called WhisperFlow, which allows me to just hold down a key on my keyboard and speak. That's one of the capture tools that we'll show you how to use.)

And notice if you look along the top here, there's three modes that you can use Claude in: Chat, Co-work, and Code. I'm using Chat. So this is the most basic, the most beginner level, the most elementary version of Claude. If you want more power or you need more capabilities, you can use the others.

Okay, interesting. So it has a strong opinion. Notice that there's no way for it to have a strong opinion or for its strong opinion to be of any use to me if it doesn't have a tremendous amount of context. Think how much context you need to answer this question. You've got to be able to holistically see the entire business plus my role in that business. And here's the gap that it sees: *"You have no scalable high-touch offering that doesn't require Tiago's direct involvement."* And that's exactly right. It's so true. And then it makes a proposal. Notice that it knows my product ladder, how people ascend through our ecosystem. It knows that I am highly involved in pretty much all of them, especially the high-touch ones. It knows that this is capitalizing on our three biggest strengths. It knows that we previously tried to move into B2B offerings and it didn't work. And it even knows why. And then it has follow-up questions. And they're not just general vague ones. They're really specific. For example, "what's your wife up to?" The fact that it knows I'm married, knows her name, knows what she's up to, knows that she's not currently involved in the business.

This isn't a long response. This isn't one of those mega thousand-word things that I have to pour through. It's just a very succinct and very targeted observation, the way that a coach would do, pointing out what's missing in my work currently.

Notice that this was updated today. I updated it this morning. And the way that I updated that — I'm not going to get into this now — but every once in a while, every week or two weeks or three weeks or whenever, I give it access to my notes and I say: *"Based on all of my latest notes across all my current projects, all the areas of responsibility, all the resources, if there's any new ones or any new archives, update my master prompt."* And it did that in a few minutes. I think I told it to do that, I went and heated up my coffee, came back, and it was done. Do you guys understand what is going on here? This is so insane. I can just take notes in my casual freeform kind of messy way and then once a week or every two weeks say, "hey, Claude Code, update my master prompt." And that's just the most basic level. That's just kind of the beginner or what we call the foundational level of what this looks like.

All right. I don't know about you, but my mind is still blown by this. Okay, I can sense those questions. I can feel the tidal wave of doubts and worries and follow-ups, and I want to get to those.

So how do I recommend you go about creating this thing called a master prompt? I have a very strong opinion on this. And this really speaks to what — I think I've done so much reflection on the decade that we were teaching Building a Second Brain, the previous ecosystem, the previous method. We taught it in so many different formats in so many different ways. And just reflecting on all that experience, I think there was a big mistake that I made. There was a variety of mistakes, but this was the biggest one: I sort of imagined the ideal system. What is the ultimate way this looks? Which for me took years and many iterations, many versions. And then I said, "let me teach this ultimate system to everyone." And that had some benefits. It was impressive, it was inspiring, kind of got you excited. But I think the problem with that approach is that **the fully mature system, as cool as it is, is not how you start.** That can't be how you start. That's the worst way to start. That's trying to swallow something that you're not ready for. It's trying to build something that is on version 15 when you really need to start with version one.

So in this cohort, in this program, I'm going to try to rectify that mistake. And the way we're going to do that is **we're going to build the same system three times.**

**Week one** we're going to spend at the foundational level, just creating the basic master prompt. The version that I really believe is the MVP — the minimum viable product, minimum viable prompt. Like what every single professional, no matter what you do, needs to have. We're going to do that in week one. So if you just do week one and then you get busy or you drop off or that's enough for you, great. You've got the 80/20 of what I have to offer. And the other thing that's important: even for those of you who are more advanced, if you think about it, most of your AI interactions still reside at kind of a basic level. You don't need to fire up the most advanced system. You don't need to fire up Claude Code for probably 50, 60, 70% of your AI interactions. So even for advanced users, you want almost a fallback — something that is small, simple, minimal and streamlined that you can fall back to for those simple everyday interactions. And that's the foundational level.

Then we're going to do it again. We're going to rebuild the system in **week two** at an intermediate level. Because what you're going to find is for many tasks, that foundational level is not enough. And I actually want you to run into those barriers yourself. I want you to have the experience of what it's like having a more basic master prompt and then running up against the limits of it, the places where it doesn't work. There's so many. So then you feel the need — like viscerally, like in your gut — you feel the need for what we're going to do at the intermediate level. Which is basically to **break apart your master prompt into little modular bundles.**

I know that sounds complicated, but it just means: imagine your master prompt as a whole collection of different documents. And **you only load up the ones that you need when you need them.** So imagine you have a master prompt just for one project. If you're working on that project, you only load up that master prompt and nothing else. You have a master prompt for your finances. You have a master prompt for your relationship. You have one for your health. You have one for your vacations. For each little part of your life and your work, you have almost like a little specialized master prompt so that you avoid overloading and confusing it with too much random context.

Then in **week three**, we're going to do it again. Because the intermediate level also has limitations. The important point here is it is only at the advanced level that we're going to layer in all the stuff. The crazy complicated impressive sophisticated stuff that makes up 90% of what you see on social media: long-term memory where the AI can build and keep track of its own memory, agents and sub-agents, integrations with other platforms, advanced harnesses. I really strongly believe should only come at the advanced level when you have the previous, more foundational levels in place.

All right. I think I'm going to pause here.

**Speaker 2 (32:45)**
Yeah, for sure. Definitely seeing a theme around privacy and security when it comes to the master prompt. This is a question that popped up a lot. So how do you think about that? Like giving more sort of sensitive personal data to the LLM or putting it into your master prompt?

**Speaker 1 (33:04)**
This is a whole conversation. We're going to have — not an entire live session, but a big chunk of one towards the end, I believe, about this, because it's very nuanced. Don't think there's a single — the single answers that you get these days are very black and white. They're very all or nothing. "Give AI everything, it's no problem, YOLO." And the other extreme is "no, AI is inherently evil, it's stealing all your data." Pretty sure there's some middle ground there. And it has implications. It has implications for which tools you use in the first place, for how you use those tools, for what you provide to those tools, for the permissions you give at different levels. This is a world. We will talk about it for sure, but it's nuanced. If I had to say one answer, it's just a trade-off like everything. It's a trade-off between getting the power and the leverage of AI without getting the risk and the pitfalls and the dangers.

**Speaker 2 (34:16)**
Yeah, I like how Mohammed just put it in the chat — "security in the AI era is a calculated risk."

**Speaker 1 (34:23)**
Yeah. Like everything. Getting in your car, driving down the freeway is probably one of the biggest risks you take. They're all calculated, they're mitigated, they're counterbalanced.

**Speaker 2 (34:47)**
Should we get to some questions from the Q&A?

**Speaker 1 (34:52)**
Yeah, would you mind surfacing those for me? The chat is pretty crazy right now.

**Speaker 2 (35:00)**
Let's pick this one from Julie. "I'm building my second brain in Notion and Claude. I bought the Notion Power template. Personally working with Claude — do you have Claude skills you're building or endorsing? How will the cohort maybe cover skills?"

**Speaker 1 (35:20)**
Yes, we will talk about skills. That's one of those intermediate to advanced things. So what you're going to notice is that when you build your foundational master prompt, you're going to put stuff in there that later on I'm going to have you look through — or have your AI look through — and you're going to notice some of the stuff you're putting in your master prompt shouldn't be there. It should be skills. If it's something like "in this case do that" or "in these situations apply this lens" — those things that are sort of triggered. You can create something that's called a hook. This is advanced, but you can create a hook or a skill. It's almost like what was originally just this single monolithic master prompt is now being pulled apart into different specialized purpose-built tools. But I want you to start with the master prompt. Just get it all in one place because AI can do a lot of that for you. It can tell you what things should be and where they go and what format they should be in. Skills are one of the advanced things we're going to look at.

One of the criteria that I have is just what's mature. I'm only going to teach you things that are mature, that are proven. Because there's this wild crazy frontier right now. Like OpenCloud for example — we're not going to do anything related to OpenCloud because it is a circus. It is a wild west. I have poured so many hours with zero return on that thing. It's not ready. Maybe later it'll be ready. But we're sticking just to Claude Code, which has been out for more than a year now. That is mature. And then we'll revisit what's ready to look at in the fall.

**Speaker 2 (37:01)**
Let's go to a comment from Andy, who is asking from YouTube about your experience on letting Claude update the master prompt on its own and how it might understand your intentions, update itself. How are you making sure that the updates are actually happening? Would you like, read the whole thing again?

**Speaker 1 (37:24)**
Yes, that's probably the very first thing that will break in your master prompt. **It will go outdated within like 48 hours.** Because that's the pace of modern life. That's how fast things move. And then we're going to have a conversation because there's different approaches to this. This is one of our guiding principles, in fact. There's never just one right way. I wish there was. I wish I could just tell you the best way. But even something as simple as updating your master prompt, there's a spectrum — from more automatic ways. You could really say "just go ahead and update it. I don't even need to know about it. Just do that every hour." But then there's the risk trade-off. It could put something in there that is not correct or is not accurate. And then on the other end of the spectrum is full human updating, which again has certain advantages and disadvantages. I tend to be in the middle, which is: **go ahead and propose a set of changes, flag the most high-stakes ones for me so that I can say yes or no or provide input. And then once I do, go ahead and do them.**

**Speaker 2 (38:32)**
Similar question from Elise and Megan regarding work versus personal. Would you recommend different Claude accounts for each? Do you put them together? How do you think about the separation?

**Speaker 1 (38:48)**
Again, this is going to be my stock answer for everything: this is a conversation. I think you need some sort of separation. So we're going to look at something which is the **context stack**. Imagine a pyramid where there's different layers of context. The ones that are more foundational influence all of your AI interactions. So just think: what is so inherent to you and universal to everything that you do that you want it to influence every single AI interaction that you have? There's actually not that many things. But then there's higher levels where it starts to become something that you can turn on or off. I typically choose to separate it at the level of the master prompt. I have a master prompt for work and a different one for personal. And that's a pretty clean separation. But then I have both of those in the same Claude account, which is tied to my work email. So there's always a little bit of bleeding in and out or some overlap.

Okay, I think I'm going to keep going. So that was a little bit in the weeds. I kind of like to zoom in and out, always keep in mind the big picture and not get lost. And so I want to zoom out because — it's sort of like one of the questions that I would love for you to answer out of this call is whether we're the right people for you to learn from. I don't assume by any means that I am the right person, that our team is the right person for everyone. You really want to find the teacher or the community or the method or the philosophy that fits you and that you're going to be able to have confidence in.

So to help you do that, I want to give you — I think there's five of them — my five most contrarian opinions. They're contrarian in the sense that they're the most different from everything that I see online. Everything I see on X, on Instagram, on LinkedIn, on Substack. To the extent that you either agree with these contrarian opinions or are willing to entertain them, willing to consider them, then I'm probably the right teacher for you.

**Contrarian opinion #1: This stuff is hard.** This is like maybe the most contrarian thing. Every day I see AI influencer after AI influencer just either say or imply that it's easy, it's seamless, it takes seconds, you could do this if you're brain dead, it takes no effort. And then every time I take what they're telling me and I go and just try it, virtually all the time I find in my experience (and I'm fairly competent), it just requires so much more complexity than they say. So much more subtlety is involved in the decisions. There's so much more setup than they set the expectations for. And there's so much more maintenance. So I just want to be very honest with this: this isn't this magic button that you press and life becomes easy or your work becomes easy. It's hard work. And in a weird way, AI takes more cognitive effort. It really burns through your energy to work with AI. Because you're making these architectural decisions that have a lot of downstream implications. So I'm never going to pretend or say that this is easy.

**Contrarian opinion #2: Note-taking is more valuable than ever.** I see a lot of commentary out there that "oh you never need to take notes, just have your AI note taker do everything for you and just dump everything on all your drives and all your places." No. Note-taking is more valuable than ever. It still requires human discernment and human judgment to pick out the signal and the noise. What of all this stuff matters? What is the important factor, the important priority? What's the point of view that I'm taking?

At the same time, the value and the purpose of note-taking is shifting. So there's this idea from finance, from investing, called **alpha**. Alpha is a kind of information that other people don't have. If you were a Wall Street investor, maybe you travel out to Minnesota and you find out that there's a pest that is eating the cornfields, and you have alpha. You have this unique piece of information that is not out there in the public, and you can use that alpha to invest, to make decisions that give you a better return.

That same idea is coming to all knowledge work. **There are pieces of information that are not known to AI.** Information that is only in certain places at certain times, that is in certain people's heads, that is in old books that have not been digitized, that is in certain formats such as video and audio that are harder for the AI to ingest. There's hundreds of little pockets of information, of alpha, that if you can find them and capture them in your notes, you now actually have a disproportionate advantage over everyone else who is only using what the AI already knows and what it already has in its training data. So we are not leaving note-taking behind.

**Contrarian opinion #3: Agents are largely a bunch of BS.** They're so not ready. I've done so many tests and so many experiments. And I think basically that the online hype cycle is putting far too much attention on automation and execution. Those are the buzzwords right now. "AI to automate your life. AI to execute for you. To do your to-do list for you." And I think that's just so misguided. It's not true. They actually have tons of bugs. They constantly fail. They're constantly making mistakes. And in a way, it's not even the right place to focus because the simplest bits of execution AI cannot do.

The other day I asked it to just look at my calendar. Like the simplest thing: "hey, go and look at my calendar and tell me what I'm doing tomorrow." Well, it immediately deleted a very important meeting that had 30 people invited to it. And then it caught it and said, "oh, sorry, I deleted that meeting. Let me undo it." And it said "I undid it" — and it didn't. Execution is not the right place for AI to focus.

What AI can do, what it's more than ready to do, is **judgment** — or rather, helping you with your judgment. It's decision-making, making better decisions. It's researching, synthesizing research, finding the gaps in research. That's the realm of pure information. The realm of pure information where it doesn't have to interact with anyone or anything outside of your computer, which is where it starts to go wrong. So we are not going to be talking about any kind of agent. We are talking about a **cognitive exoskeleton** — AI as an enhancement and as an amplifier to you, the human.

**Contrarian opinion #4: The true frontier is inside our minds and bodies.** We talk about the frontier of AI. I really think the true frontier is inside our minds and bodies. And we're going to have a series of guest instructors that are all related to this. This is it. It's not about the tools. It's not about the features. It's not about the technology. It's about: do you have self-awareness? Do you know yourself? Do you know how your mind works? Do you have emotional fluidity? Do you have the ability to shift between emotions? The ability to regulate yourself? The ability to rest and recover? Over the long term — maybe not on the order of weeks and months, but on the order of months and years — this is what's going to determine if AI is a force for good in your life, or if it's a negative force.

**Contrarian opinion #5: Refuse the urgency.** This might be the most controversial. I just think it's so misguided — all this apocalyptic thinking, "you have three months, six months, a year, 18 months to make all the money you can before our world is over and you join the permanent underclass." I've been alive long enough that I have seen multiple technology waves, and this is what they always say. Every single new technology wave, they say it's all over and you have to do A, B, and C right now. I think typically when they do that, it's to get you to do something — to panic, give in to fear, buy something, do something, buy into an idea. And I just won't do it. This is going to take decades. It's going to play out for the rest of our lives. When we are on our deathbed, they're still going to be arguing about AI's impact on society. People will still have jobs. We'll still send our kids to school. We'll still read books. I'm not giving in to the panic and the hype. We are being more thoughtful and more present in the face of what AI is doing rather than less.

---

*(Transcriptie hieronder gaat verder met de programma-pitch voor het cohort, Q&A over community, health/finance-voorbeelden en slotopmerkingen. Voor de oorspronkelijke pitch/sales-context is de tekst integraal opgenomen tot en met het einde van het webinar. Inhoudelijk relevante passages voor Dynamic Context zijn hierboven al uitgelicht. De cohort-sales sectie is minder relevant voor BeeHaive's research-doeleinden maar wordt bewaard voor completeness.)*

Let me transition now from talking in broad strokes about my point of view, my method, my principles — to the program that we're launching. This is the concrete thing that you can do starting today, if you have decided you want to keep learning with me and keep learning with us.

It's the first time that we're teaching a live cohort. At least we did one focused on businesses last year, but this is the first time we're doing one for individuals, for professionals, in three years. It's taken three years of research and thinking, and we've done many experiments, many trial and error things. And this is what we've come up with as really the new direction of our entire company and my work. It's an intensive live three-week program. For three weeks, we are going to meet three times a week. I will be there every minute of it personally to lead you through everything. And what you're going to walk away with is a working AI second brain at some level of capability — foundational, intermediate, or advanced. What that is, is a personalized, organized, context-rich digital exoskeleton. And what it's going to do is make every single conversation and collaboration not just something that anyone else in the world would get from working with AI, but something that's informed by your expertise, your context, and your goals.

**Compression** is the first principle: the assumption is that you don't have time. Or at least not as much time as you want or need to explore the frontier of AI. Takes our entire team spending most of our time — hundreds, thousands of hours of research and experimentation, compressed into three weeks. That's the main value proposition.

Everything we do in this cohort is **community-centric**. This is a learning community, a community of practice. I would say from our past years of doing cohorts that at least 50% of what you learn and a lot of the most impactful things come not from me, but from the other participants.

Everything we do is **platform agnostic**. All the demonstrations will be on Claude because that's the one I know best. But everything we're building — the master prompt, the little context bundles, the AI board of advisors — this is like a life principle for me: I don't do anything that is limited to one platform. So everything we're creating is completely platform agnostic. You take it with you.

And I'm really **not interested in replacing humans**. Even if humans can be replaced, that's just not my preference. I like humans. I value humans, and my time and attention and effort is going to augmenting them — making them smarter, faster, wiser, more embodied, more connected to their intuition, more creative with better judgment. We are really focused on augmentation, not automation.

---

**Q&A second half (hoofdpunten):**

**On emotional regulation (~1:00:50):**
> "A few weeks ago I did a week-long course with Joe Hudson in Sonoma in California. The big breakthrough, the big takeaway was around fear. I would not have said that I was afraid of AI. I would have said I was excited, optimistic and positive. But through this process I realized that I had so much fear at multiple levels. Fear on the personal level — what's going to happen to me, my work, my career, my income. Fear on the family level — what are my kids' futures going to be like? What is the right way to parent? What do my relationships look like? At the level of the team, the business, the business model, the industry, all the way to the fate of the world and the future of civilization. There's no way that all those levels of fear are not really powerfully shaping the way you think and the decisions you make. And so the important thing is not to deny that, it's to bring it into the light. To feel through it. Because each one of those kinds of fear are telling you something. They have a message. They have a signal that you need to hear."

**On CODE and PARA as prerequisites (~1:03:18):**
> "The first thing you will see when you sign up is a little cloud course. We're really not assuming any knowledge. It's probably helpful if you've opened ChatGPT once or twice. The first thing you will see in the curriculum is a pretty six-module beginner's introduction to Claude. The other thing is we have so much existing content — just watch the PARA video, that's 10 minutes and you can get most of what you need to know. My principle here is I want the floor to be very low. My parents are going to be there. They're the ultimate judge of whether we've made it easy to understand. But then I want to make the ceiling very high."

**On time commitment (~1:17:15):**
> "If time is a constraint — because if time is not a constraint, if you can afford to spend one or two hours a day to kind of tread water. That's just maintenance. It really does take maintenance. Don't let anyone convince you that no maintenance is required. And then I think you would need at least another one or two hours to do anything new. To learn anything new, try anything new, adopt anything new. So like three to four hours a day is what it really takes. If you have three to four hours a day, go for it. But if you don't, then allow us to compress."

**On the six-month window (~1:17:50):**
> "I went through months or even years of notes and Notion docs and experiments. There was like a six-month window. Only things about six months old were relevant. Everything that was more than six months older was zero relevance, zero usage — was actually the wrong thing to pay attention to. So I kind of think in AI right now there's a moving six-month window of relevance."

**On alpha-finding (~1:08:37):**
> "Such a great one. We're going to talk about this. We have a whole session dedicated to note-taking and capture. Because it's subtle. I'll give you one random example. I'm really getting into local history. This is the last thing I ever thought I would be interested in. We live in this Mexican town right now, smallish — hundred thousand people. I'm noticing that it has a really rich history that goes back almost 500 years, and none of it is digital. You can't find it online. I've tried asking every AI platform. They're all like, 'we know nothing about this town.' And at first I was annoyed. But as I thought about it, I'm like, oh my God, this is an incredible opportunity. I'm now kind of like Indiana Jones. I'm going to the local library and taking out old books and literally blowing the dust off them. And it's like I get to go on this little adventure of finding these rare physical printed documents and reading through them, in some cases in old Spanish, using AI to translate the old Spanish into English. I'm working on a blog post where I'm going to talk about the 500-year history of this town."

**On health and finance advisors (~1:12:07):**
> "I tend to use work-related examples because the return on investment is so clear. But the impacts have been just as big in my personal life. I have actually found them more useful in my personal life. Because in my personal life, I don't have as good of advice. I can't justify the consulting and the coaching in my personal life."

On **health**:
> "I've just started basically assembling all the context I can find about my health, providing it to my AI health coach. I have learned more about my own personal health in the past couple of months than I ever have before. Its ability to cross-reference — 'oh, you're taking that supplement, but you're also having that protein after your workouts. Well, this ingredient and that protein, which I shared with it, is counteracting and making it so you can't absorb that supplement.' Or 'you're trying to get more protein in your diet, but you're eating too much steak. That's too much red meat, which is increasing your cholesterol, which I know you're trying to keep an eye on. So substitute 50% of that red meat intake with fish and chicken.' You would need a team of not even doctors — because doctors aren't good at nutrition — you would need a team of nutritionists around the table going through your health documents which are in a dozen different formats. I talk to it almost every day. And now I'm doing the same for my family."

On **finances**:
> "We've worked with a financial advisor before, but do you know what financial advisors charge? They charge a percentage of fees under management. If you work with a financial advisor over 5, 10, 20 years, you're paying them a sizable percentage of all the money you make from your investing. It's absurd. Even the advisors that you can pay by the hour are expensive. So I've given it our financial context. There are all these mistaken assumptions I was making about my finances. There were some things I just flat out did not understand about how retirement accounts work, how 529 education accounts work. I had certain ideas of what risk even means that were completely misguided. We've significantly changed how we save, how we invest, how we give, how we donate based on our work with our AI financial advisor."

**Why the master prompt alone is not enough:**
> "This is another example of where the master prompt fails. Your master prompt is very horizontal — across every AI interaction. But if you have a certain domain of your work or life, like health, like finances — at work it might be looking at your HR policies or your insurance needs or your marketing strategy — one vertical slice. Your master prompt won't have anywhere near enough context. How could it? For those vertical slices, you have to go really deep on just that slice. Where is the context that you'll need? Often you've got to go spelunking. You've got to go log into random platforms, download things, convert them from one format to — we're going to talk all about this — convert them into a format that is AI friendly, such as Markdown. You have to do a dedicated curation effort to get that context in one place because it tends to either not exist at all or not exist in digital form or not exist in a digital form that AI can make use of."

**On ADHD and middle management (~1:19:30):**
> "AI is ushering in a golden age for people with ADHD and people who are neurodivergent. Because finally, multitasking — such as between multiple Claude Code sessions that are all happening at the same time or multiple agents that are all working — that's now going to become one of the most valuable skills. And it is a skill. It's the skill of middle management. Those of you who are middle managers and have eight direct reports — people talk about 'oh, middle management is going away, that's going to be the first people to lose their jobs.' Maybe so, but we're all going to become middle managers now. We're all middle managers of our own team of AI agents. And as any manager will tell you, people go through an incredible transformation to become managers — to lead, to delegate, to coach, to guide, to see things from different perspectives and let go of your perspective to take on someone else's. It's like a whole skill set that we kind of need to learn now. People with ADHD tend to thrive in that environment."

**On capture for people mid-reading Building a Second Brain (~1:21:10):**
> "Capture continues to be important, as important as ever. But the way it happens and what it's focused on needs to change. It needs to become more about finding whatever is not in AI's training data or what AI cannot find through a web search. It's as simple as that."

**Closing thought (~1:23:00):**
> "When I think about the scale of years and decades — think about what is most important if this is something that is going to unfold over many years and even decades. I think the single most important thing for you to decide now is: who are you going to learn with? Any single book or video or course is going to pass away within a matter of months. Any method, any technique, any set of principles — they're all being revolutionized on a monthly basis. What will persist, I think, what's going to stand the test of time, is your community. The people, the other human bodies that you decide you want to influence and be influenced by. So if there's one decision that I would make today, really it's — thoughtfully consider who do you want to learn with. Don't make the feed on Twitter your community. Don't make the feed of endless hype that community. Choose a real community."
