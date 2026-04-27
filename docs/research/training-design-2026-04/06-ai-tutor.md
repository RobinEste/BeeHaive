# 06 — AI-tutor: design, guardrails, privacy & meting

> Onderdeel van het training-design onderzoek (april 2026). Zie [`INDEX.md`](INDEX.md).

## Effectiviteit van AI-tutors — wat we weten (2023–2026)

**Gemengd beeld.**

- **Khanmigo:** mixed-methods studie (69 undergrad physics students, *Journal of Teaching and Learning*, 2025): significante learning gains in álle condities, maar géén significant verschil tussen Khanmigo en Google. Studenten waardeerden wel de step-by-step guidance. J-PAL doet een grotere efficacy-studie.
- **Harvard CS50 Duck (Malan, Liu et al., SIGCSE 2024):** grootschalige deployment, sterk positieve student feedback ("alsof ik een persoonlijke TA heb"). Geen RCT; vooral kwalitatief.
- **Duolingo Max:** interne data claimen 34% betere grammatica-retentie met "Explain My Answer" en 15% hogere course completion. Bedrijfsdata, niet peer-reviewed, dus met voorbehoud.
- **Rori (Ghana, WhatsApp math tutor):** 1 uur/week → effect size equivalent aan een extra schooljaar. Eén van de sterkste effect sizes in AI-tutor literatuur (wél peer-reviewed RCT).

**Tegenbewijs/waarschuwingen.**

- University of Pennsylvania studie (Turkse high school, 2024): ChatGPT-gebruikers losten 48% meer oefenproblemen correct op, maar scoorden 17% lager op een conceptueel begrip-test. Cognitive offloading waarschuwing.
- MDPI & *Frontiers in Psychology* (2025): frequent AI-gebruik correleert negatief met critical thinking, gemedieerd door cognitive offloading, vooral bij jongeren.

**Eerlijke inschatting.** AI-tutors zijn *geen* wondermiddel; ze zijn vooral effectief als *scaffolding*-tool die actief denkwerk uitlokt, niet als antwoord-leverancier.

## RAG over cursusmateriaal — grounding

**Kernprincipes (uit 2025 reviews, MEGA-RAG, MetaRAG):**

- **Grounding = antwoorden verankeren aan verifieerbare documenten.** Zonder grounding hallucineren LLM's.
- **Citaties per claim:** elk feitelijk statement moet verwijzen naar een cursusbron (module, pagina, video-timestamp).
- **"Weet ik niet"-gedrag:** de bot moet expliciet zeggen wanneer retrieval niets relevants oplevert; gebruik een confidence threshold.
- **Dual-pathway retrieval** (dense + sparse + knowledge graph): KG-RAG reduceerde hallucinaties met 18% in biomedical QA. Past goed bij BeeHaive's Neo4j knowledge graph.

**Toepassing voor BeeHaive.**

- Alle cursuscontent (video-transcripts, slides, MDX-content in `frontend/src/content`, Neo4j-knowledge-graph van het framework) ingesten in vector store + KG.
- **System prompt patroon:**
  - "Antwoord alléén op basis van de opgehaalde cursusfragmenten. Citeer altijd module en sectie. Als de fragmenten geen antwoord bieden, zeg: 'Dit valt buiten de cursusinhoud — ik raad je aan vraag X te stellen aan een moderator.'"
- **Evaluation:** metamorphic testing (MetaRAG-stijl): decompose antwoorden in atomic factoids, verifieer tegen retrieved context.

**Evidence-sterkte.** Sterk en snel evoluerend.

## Scaffolding via AI — Socratische prompting

**Kernbevinding.** Structurele prompts ("clarify → justify → counterexample → synthesize") + de regel "*Never give the student the answer*" in de system prompt produceren meetbaar meer zelf-reflectie en kritisch denken (SPL / Socratic Playground for Learning; Evolutionary RL Socratic tutor: critical thinking frequency ~3× hoger dan supervised fine-tuning baseline).

**System-prompt template voor BeeHaive-bot (RTRI framework):**

- **Role:** "Je bent een Socratische tutor voor BeeHaive's AI-governance cursus."
- **Task:** "Help de cursist concepten te begrijpen door vragen te stellen, geen directe antwoorden."
- **Requirements:** "Geef nooit een volledig antwoord bij een open-eind vraag. Begin met een verhelderende tegen-vraag. Geef hints in 3 niveaus: (1) context, (2) gerelateerd concept, (3) gedeeltelijke hint. Pas na 3 pogingen van cursist mag je een fragment van het antwoord geven."
- **Instructions:** "Blijf binnen de 7 bouwstenen + 7 guardrails. Citeer bron bij elke feitelijke claim. Als cursist vraagt om 'de casus voor me op te lossen', weiger vriendelijk en bied scaffolding aan."

## Guardrails — implementatie

**Best-practice patronen (2025 literatuur, Arthur AI, Confident AI, Datadog):**

- **Pre-LLM guardrails:** input-filtering. Blokkeer: verzoeken om volledige essays/huiswerk op te lossen, vragen buiten scope (politiek, andere frameworks).
- **Post-LLM guardrails:** output-filtering. Check: bevat antwoord citaat? Is antwoord >X tokens zonder scaffolding-vraag? Bevat het PII?
- **LLM-as-judge evaluatie:** tweede model beoordeelt of antwoord Socratisch is (heeft vraag, geeft niet te veel weg) en grounded.
- **Domain boundary:** expliciete lijst van in-scope topics (de 7+7) en een "escalatie naar moderator"-pad.

**Concreet voor BeeHaive:**

- Guardrails-AI library (Python) in `backend/app/services`; policy definities als YAML.
- Logging van alle guardrail-triggers voor review.

## Voorkomen van luiheid / cognitive offloading

**Kernbevinding.** Over-reliance op AI verlaagt concept-begrip (UPenn studie, 17% lager). Mitigaties uit literatuur:

- **Reflection prompts:** "Leg het antwoord in eigen woorden uit" na bot-interactie.
- **AI-free sessies:** zelf-tests zonder botgebruik (zichtbaar gelogd).
- **Delayed testing:** quiz op dag 7 over concepten die op dag 1 met de bot waren besproken — zonder botgebruik.
- **Transparantie over gebruik:** cursisten zien hun eigen "bot-dependency score" als zachte nudge.

## Privacy — AVG-conform

**Kernbevindingen (2025–2026 guides: moinAI, DocuChat, Premai, Quickchat):**

- **EU-hosting verplicht** voor gevoelige conversaties — BeeHaive zit al goed met Hetzner.
- **Data-minimalisatie:** bewaar chat-logs zo kort mogelijk (default: 30–90 dagen; 1 jaar is al lang).
- **Recht op vergeten:** expliciete delete-functie per gebruiker.
- **Geïnformeerde consent:** duidelijk tonen dat cursist met AI chat, wat wordt opgeslagen, waarvoor gebruikt.
- **DPIA verplicht** voor AI-systemen die persoonsgegevens verwerken (EU AI Act + AVG overlap).
- **Encryptie in transit & at rest** voor alle conversation-data.
- **Geen gebruik van cursist-data voor LLM-training** zonder aparte opt-in.
- **Processor agreements** met LLM-provider (Anthropic): zero-data-retention endpoints aanvragen waar mogelijk.

**Concreet voor BeeHaive:**

- Postgres tabel `chat_sessions` met TTL van 90 dagen (configurable per gebruiker).
- DPIA-document als onderdeel van de governance-documentatie (eet je eigen hondenbrood).
- In de privacy-policy expliciet: conversaties → alleen gebruikt voor kwaliteitsverbetering, nooit voor training van derde-partij-modellen.

**Evidence-sterkte.** Juridisch vereist, niet optioneel.

## Measurement — retentie & indicatoren

### Hoe meet je retentie concreet?

**Best practice uit Kirkpatrick-literatuur (2025–2026):**

- **Level 1 (Reaction):** direct na module — NPS, relevantie-score.
- **Level 2 (Learning):** direct + delayed post-tests op **dag 30, 60, 90**. Zelfde item-bank, random sample 10 items.
- **Level 3 (Behavior):** 30/60/90 dagen, via zelf-rapportage + (waar mogelijk) manager observation. Sweet spot is dag 45–60 voor balans response rate vs. transfer-periode.
- **Level 4 (Results):** business outcomes — voor BeeHaive lastig, maar proxies: aantal governance-artefacten geproduceerd, incidents voorkomen.

**Waarschuwing:** response rates dalen van ~80% (direct) naar 20–40% (delayed). Gebruik:

- Korte surveys (5 min max).
- Incentives (bijv. een additional resource na invullen).
- De AI-bot kan het als conversationeel formulier aanbieden — hogere response rates.

### Leading vs. lagging indicators

| Type | Indicator |
|---|---|
| Leading | % cursisten dat binnen 30 dagen een governance-document heeft opgesteld |
| Leading | Aantal if-then plans dat is uitgevoerd (zelfrapportage) |
| Leading | Bot-engagement frequency (als proxy voor actieve verwerking — let op offloading-risico) |
| Leading | Community-posts per cursist |
| Leading | Delayed quiz-score dag 60 |
| Lagging | Adoptie van BeeHaive-framework in de organisatie (jaarlijkse survey alumni) |
| Lagging | Door cursisten gerapporteerde AI-incidenten voorkomen |
| Lagging | NPS/retention voor vervolgcursussen |

**Evidence-sterkte.** Framework is standaard (Kirkpatrick sinds 1959, herzien in "New World" model 2016); specifieke metrieken voor AI-governance training zijn nieuw en moeten bij BeeHaive zelf gevalideerd worden.

## Slotsamenvatting — 7 prioriteiten voor BeeHaive-design

1. **Spaced retrieval als ruggegraat** (zeer sterke evidence): Leitner-achtige flashcard-flow in bot op dag 1, 3, 7, 21, 60, 120.
2. **Testing ≠ meten; testing = leren.** Elke module eindigt met 3–5 open retrieval-vragen.
3. **Interleaved cases in weken 5–8**, blocked introductie in weken 1–4.
4. **If-then implementation intentions** aan het eind van elke module (d = 0.65).
5. **Socratische AI-bot met RAG + strikte guardrails**, expliciet "never give the answer", citaties verplicht.
6. **Post-course drip:** dag 1, 3, 7, 14, 30, 60, 90 + booster-sessies op maand 1 en 3.
7. **Delayed post-tests op 30/60/90 dagen** + leading indicators (governance-artefacten, if-then completion) + jaarlijkse alumni-survey voor lagging indicators.

**Waar de evidence zwak is:** exacte email-cadans, effect sizes van community-learning in online B2B-context, en lange-termijn effectiviteit van AI-tutors voor volwassen professionals (meeste studies zijn K-12 of undergraduate). BeeHaive zou een eigen A/B-test moeten inbouwen (bot-aan vs. bot-uit groep) om hierover zelf data te genereren.

## Bronnen

**AI-tutors: Khanmigo, CS50, Duolingo**

- [Khanmigo — Journal of Teaching and Learning (2025)](https://jtl.uwindsor.ca/index.php/jtl/article/view/10052)
- [J-PAL — AI-Powered Tutoring Khanmigo](https://www.povertyactionlab.org/initiative-project/ai-powered-tutoring-unleashing-full-potential-personalized-learning-khanmigo)
- [Khan Academy Efficacy Results November 2024](https://blog.khanacademy.org/khan-academy-efficacy-results-november-2024/)
- [Liu et al. — Teaching CS50 with AI (SIGCSE 2024)](https://cs.harvard.edu/malan/publications/V1fp0567-liu.pdf)
- [Improving AI in CS50 — Liu et al.](https://cs.harvard.edu/malan/publications/fp0627-liu.pdf)
- [Harvard SEAS — Quacking into Computer Programming](https://seas.harvard.edu/news/2024/01/quacking-computer-programming)
- [Duolingo Max Review 2025 — Medium](https://cheapersgames.medium.com/duolingo-max-review-how-ai-makes-language-learning-2-faster-in-2025-64fafe992424)
- [5D Vision — Duolingo AI Case Study](https://www.5dvision.com/post/case-study-duolingos-ai-powered-language-learning-revolution/)

**RAG, grounding, hallucination mitigation**

- [MEGA-RAG — PMC 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12540348/)
- [RAG Comprehensive Survey — arxiv 2506.00054](https://arxiv.org/html/2506.00054v1)
- [MetaRAG — CEUR-WS](https://ceur-ws.org/Vol-4136/iaai6.pdf)
- [Hallucination Mitigation Survey — arxiv 2510.24476](https://arxiv.org/html/2510.24476v1)
- [RAG in 2025 — Morphik](https://www.morphik.ai/blog/retrieval-augmented-generation-strategies)

**Socratic tutoring & scaffolding**

- [AI Virtual Tutor — U Toronto CTSI (Dec 2025)](https://teaching.utoronto.ca/wp-content/uploads/AI-virtual-tutor-developing-effective-system-prompt-CTSI-Dec2025.pdf)
- [Evolutionary RL-based Socratic AI Tutor — arxiv 2512.11930](https://arxiv.org/html/2512.11930)
- [Scaffolding Metacognition in Programming — arxiv 2511.04144](https://arxiv.org/html/2511.04144)
- [Socratic method AI in healthcare — ScienceDirect](https://www.sciencedirect.com/science/article/pii/S1471595326000727)

**Guardrails for LLM tutors**

- [Arthur AI — Agent Guardrails Best Practices](https://www.arthur.ai/blog/best-practices-for-building-agents-guardrails)
- [Confident AI — LLM Guardrails Guide](https://www.confident-ai.com/blog/llm-guardrails-the-ultimate-guide-to-safeguard-llm-systems)
- [Orq.ai — Mastering LLM Guardrails 2025](https://orq.ai/blog/llm-guardrails)
- [Datadog — LLM Guardrails Best Practices](https://www.datadoghq.com/blog/llm-guardrails-best-practices/)
- [Guardrails-AI — GitHub](https://github.com/guardrails-ai/guardrails)

**Cognitive offloading / over-reliance**

- [Cognitive paradox of AI in education — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC12036037/)
- [AI Tools and Cognitive Offloading — MDPI](https://www.mdpi.com/2075-4698/15/1/6)
- [Impact of AI Tools on Learning Outcomes — arxiv 2510.16019](https://arxiv.org/html/2510.16019v1)
- [ChatGPT as cognitive crutch (RCT) — ScienceDirect](https://www.sciencedirect.com/science/article/pii/S2590291125010186)
- [Learners' AI dependence and critical thinking — ScienceDirect 2025](https://www.sciencedirect.com/science/article/pii/S0001691825010388)

**Privacy / GDPR / AVG**

- [moinAI — Chatbots & data protection 2026](https://www.moin.ai/en/chatbot-wiki/chatbots-data-protection-gdpr)
- [Premai — GDPR Compliant AI Chat 2026](https://blog.premai.io/gdpr-compliant-ai-chat-requirements-architecture-setup-2026/)
- [Quickchat — GDPR-Compliant Chatbot Guide 2026](https://quickchat.ai/post/gdpr-compliant-chatbot-guide)
- [Ninjaibot — GDPR and EU AI Act](https://www.ninjaibot.com/ensuring-ai-chatbot-compliance-with-gdpr-and-the-eu-ai-act/)
- [Crescendo — AI and GDPR in 2026](https://www.crescendo.ai/blog/ai-and-gdpr)

**Kirkpatrick / measurement**

- [Kirkpatrick Partners — The Kirkpatrick Model](https://www.kirkpatrickpartners.com/the-kirkpatrick-model/)
- [Knowlify — Kirkpatrick Model Training Evaluation](https://www.knowlify.com/articles/kirkpatrick-model-training-evaluation)
- [Valamis — Kirkpatrick Model](https://www.valamis.com/hub/kirkpatrick-model)
- [AllenComm — Corporate Training Metrics (Mar 2026)](https://www.allencomm.com/2026/03/corporate-training-metrics-what-to-track-beyond-completions/)
- [OpenFormations — Immediate and delayed training evaluations](https://openformations.com/en/blog/evaluations-chaud-froid-formation-guide)
