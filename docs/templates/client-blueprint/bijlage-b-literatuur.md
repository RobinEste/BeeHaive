# Bijlage B — Literatuur en bronvermeldingen

## B.1 Waarom deze bijlage

De hoofdstukken 0-8 verwijzen via `[NN]` naar bronnen die in deze bijlage worden opgesomd. Deze bijlage geeft per bron: titel, auteur(s), publicatie-organisatie, jaar, URL en — waar relevant — de verificatiestatus uit het onderliggende researchdossier (`docs/research/client-blueprint-2026/final.md`).

**Verificatiestatus** komt overeen met de markering in het researchdossier:

- `verified` — directe bronfetch uitgevoerd, primaire claim bevestigd.
- `inferred` — bron secundair geciteerd of indirecte bevestiging; gebruik met voorzichtigheid.
- `unverified` — bron is bekend maar niet primair gefetcht.

## B.2 Hoofdbronnen [1] — [26]

### Use Case-selectie en probleem-framing

**[1]** Kozyrkov, C. *AI-First Leadership: Rethinking Decision-making in the Age of AI*. INFORMS Analytics Magazine, 2025. <https://pubsonline.informs.org/do/10.1287/LYTX.2025.02.02n/full/> — `verified`. Decision-first framework, drie evaluatiecriteria.

**[2]** Kozyrkov, C. (Acceldata-interview). *Cassie Kozyrkov on What AI Really Means for Enterprise Leaders*. Acceldata, 2025. <https://www.acceldata.io/blog/cassie-kozyrkov-on-what-it-really-means-to-be-ai-first-key-takeaways-for-enterprise-leaders> — `verified`. Kerncitaat: *"The purpose is important, and the purpose comes from people."*

**[3]** Karpathy, A. (besproken door Inference by Sequoia). *Karpathy's Software 3.0 and the New AI Stack*. Substack, 19 juni 2025. <https://inferencebysequoia.substack.com/p/andrej-karpathys-software-30-and> — `verified`. Software 3.0 keynote, YC AI Startup School.

**[4]** Pouladian, B. *Andrej Karpathy on Software 3.0: Software in the Age of AI*. Medium, 2025. <https://medium.com/@ben_pouladian/andrej-karpathy-on-software-3-0-software-in-the-age-of-ai-b25533da93b6> — `inferred`. LLM-als-OS-metafoor.

**[5]** Fortune. *MIT report: 95% of generative AI pilots at companies are failing*. Augustus 2025. <https://fortune.com/2025/08/18/mit-report-95-percent-generative-ai-pilots-at-companies-failing-cfo/> — `inferred` voor het exacte getal. MIT NANDA-rapport, methodologie.

**[6]** Marketing AI Institute (Roetzer, P.). *That Viral MIT Study Claiming 95% of AI Pilots Fail? Don't Believe the Hype*. 2025. <https://www.marketingaiinstitute.com/blog/mit-study-ai-pilots> — `verified`. Methodologische kritiek op MIT NANDA.

**[7]** Microsoft. *Microsoft AI Decision Framework*. GitHub. <https://github.com/microsoft/Microsoft-AI-Decision-Framework> — `verified`. Kwantificeerbaarheidscriterium, governance-focus.

**[8]** Tosic, M. *Introducing the AI-3P Assessment Framework*. Towards Data Science, 24 september 2025. <https://towardsdatascience.com/the-ai-3p-assessment-framework/> — `verified`. People-Process-Product-scoringsmodel (40/35/25, schaal 0-100).

### Architectuurpatronen

**[9]** Anthropic. *Building Effective Agents* (research). <https://www.anthropic.com/research/building-effective-agents> — `verified`. Vijf workflow-patronen, drie kerneigenschappen, "begin simpel"-regel. Kerncitaat: *"Start with a simple prompt chain optimized with retrieval and examples before adding complexity."*

**[10]** Anthropic Resources. *Building Effective AI Agents: Architecture Patterns and Implementation Frameworks*. <https://resources.anthropic.com/building-effective-agents> — `verified`. Uitgebreide architectuurhandleiding.

**[11]** Anthropic Engineering. *How We Built Our Multi-Agent Research System*. <https://www.anthropic.com/engineering/multi-agent-research-system> — `verified`. 90,2% prestatieverbetering, 15× tokens, multi-agent-criteria.

**[12]** Anthropic. *Introducing the Model Context Protocol* (25 november 2024). <https://www.anthropic.com/news/model-context-protocol> — `verified`. MCP-architectuur, adoptie, beveiligingsrisico's april 2025.

**[13]** Orq.ai. *RAG Architecture Explained: A Comprehensive Guide [2026]*. <https://orq.ai/blog/rag-architecture> — `verified`. Drie architectuurlagen, hybride patronen.

**[14]** Techment. *RAG vs Fine-Tuning vs AI Agents: Choosing the Right LLM Strategy*. <https://www.techment.com/blogs/rag-vs-fine-tuning-vs-ai-agents-llm-strategy/> — `verified`. Drie-lagenmodel, beslismatrix.

### Risk-based design

**[15]** EU AI Act. *High-Level Summary*. artificialintelligenceact.eu. <https://artificialintelligenceact.eu/high-level-summary/> — `verified`. Vier risico-tiers, Tier 2 design-verplichtingen.

**[16]** European Commission. *Ethics Guidelines for Trustworthy AI* (HLEG). <https://digital-strategy.ec.europa.eu/en/library/ethics-guidelines-trustworthy-ai> — `verified`. HLEG zeven vereisten.

**[17]** ALTAI. *Assessment List for Trustworthy AI* (interactieve tool). <https://altai.insight-centre.org/> — `verified`. HLEG-zelfbeoordelingschecklist.

**[18]** UK ICO. *Accountability and Governance Implications of AI* (GDPR-guidance). <https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/artificial-intelligence/guidance-on-ai-and-data-protection/what-are-the-accountability-and-governance-implications-of-ai/> — `verified`. DPIA-verplichting voor AI-systemen.

**[19]** TechGDPR. *Data protection digest: AI Act and GDPR study* (november 2025). <https://techgdpr.com/blog/data-protection-digest-03112025-new-ai-act-and-gdpr-study-personal-data-stored-on-blockchain/> — `verified`. FRIA versus DPIA-overlap.

**[20]** OWASP. *Top 10 for LLM Applications 2025* (gepubliceerd 17 november 2024). <https://genai.owasp.org/llm-top-10/> — `verified`. Volledige LLM Top-10 2025.

### FDE, iteratie, prototype, playbook

**[21]** Pragmatic Engineer. *What are Forward Deployed Engineers, and why are they so in demand?* <https://newsletter.pragmaticengineer.com/p/forward-deployed-engineers> — `verified`. Palantir "Delta", drie fasen, SVPG-vermelding. Kerncitaat: *"FDEs work with enormous uncertainty, and often what clients describe doesn't match the reality of their data."*

**[22]** SSO Network. *Forward Deployed Engineers: Turning AI Promise into Progress*. <https://www.ssonetwork.com/intelligent-automation/columns/forward-deployed-engineers-guide> — `verified`. 800% vacature-stijging, Salesforce 1.000 FDEs.

**[23]** NxCode. *Vibe Design Tools 2026: Stitch vs v0 vs Lovable vs Bolt Compared*. <https://www.nxcode.io/resources/news/vibe-design-tools-compared-stitch-v0-lovable-2026> — `verified`. Tool-vergelijking met sterktes en faalmodi.

**[24]** NxCode. *Google Stitch vs v0 vs Lovable 2026*. <https://www.nxcode.io/resources/news/google-stitch-vs-v0-vs-lovable-ai-app-builder-2026> — `verified`. Strategisch inzetbaarheidsoverzicht.

**[25]** Lenny's Newsletter. *A Guide to AI Prototyping for Product Managers*. <https://www.lennysnewsletter.com/p/a-guide-to-ai-prototyping-for-product> — `verified`. Wanneer productief, tool-keuze, kritische kanttekening. Kerncitaat: *"AI is not a substitute for critical thinking; human judgment is still necessary to interpret generated insights and make informed product decisions."*

**[26]** WorkOS. *Enterprise AI Agent Playbook: What Anthropic and OpenAI Reveal*. <https://workos.com/blog/enterprise-ai-agent-playbook-what-anthropic-and-openai-reveal-about-building-production-ready-systems> — `verified`. Drie-signalen-framework, vijf composable patronen.

## B.3 Aanvullende bronnen (uit convergence-pass)

De volgende bronnen zijn geadopteerd uit de convergence-pass (`convergence-gemini.md`) en lossen het MAJOR open punt op uit `final.md` (geen kant-en-klaar gepubliceerd discovery-playbook):

**Obeidat, S.** *How to Identify an AI Use Case in 7 Steps*. CAIO Newsletter, geüpdatet december 2025. *Bron-131* in convergence-pass. — De ruggengraat van hoofdstuk 2 (TRACE-diagnose, AI-Value-Objectives, AI Solution Canvas, Feasibility Check, Impact Estimation). Gevalideerd met World AI Council members.

**Obeidat, S.** *The AI Business Model Canvas (AI-BMC)*. 2025. *Bron-132* in convergence-pass. — Elf-bloks executive-validatie als optionele afsluiting van de zeven discovery-stappen. Gebruikt als optie in 2.2 en als governance-aanvulling in 7.

**Obeidat, S.** *AI is not the starting point*. CAIO Newsletter, 2025. — Geciteerd in hoofdstuk 1.1 als opening-quote. Decision-first / waarde-stroom-eerste-aanpak.

**Appelo, J.** *unFIX value stream definition* (BB-pagina-verwijzing). — Vier waarde-stroom-typen (Product, Service, Event, Project Value Stream). Gebruikt in hoofdstukken 0 en 1.

**Gartner.** *AI Opportunity Radar* (twee assen: inward/outward × everyday/game-changing). — Strategische ambitie-positionering in hoofdstuk 1.2.

**Stanford Digital Economy Lab** (Pereira, Graylin, Brynjolfsson). *Enterprise AI Playbook: Lessons from 51 Successful Deployments*. 2026. <https://digitaleconomy.stanford.edu/app/uploads/2026/03/EnterpriseAIPlaybook_PereiraGraylinBrynjolfsson.pdf> — `inferred` (PDF niet tekstueel leesbaar via fetch). 73% bewust klein gestart, 63% pilot-als-experiment. Aanbevolen als secundaire onderbouwing in hoofdstuk 6.

**Getmaxim.ai.** *The Complete AI Guardrails Implementation Guide for 2026*. <https://www.getmaxim.ai/articles/the-complete-ai-guardrails-implementation-guide-for-2026/> — Aanvullend voor hoofdstuk 4.6 (guardrails-by-design).

**Nederlandse AI Coalitie (NL AIC)** — werkgroep Data Delen, interoperabiliteits-richtlijnen voor data spaces. — Genoemd in hoofdstuk 7.4.

**PACE-platform** — *Participative And Constructive Ethics*. — Genoemd in hoofdstuk 7.4 als ethiek-als-ontwerpprincipe (versus ethiek-als-compliance-vink).

**Seroter, R. & Sanin, V.** *101 gen AI use cases with technical blueprints*. Google Cloud, 2025. *Bron-133* in convergence-pass. — Optioneel als referentie-bibliotheek voor pattern-recognition; niet voorgeschreven.

## B.4 Methodische status

De bronnenset is opgebouwd via een vier-laans deep-research (zie `docs/research/client-blueprint-2026/`):

- `research-usecase-framing.md` — bronnen [1] tot en met [8].
- `research-architectuur.md` — bronnen [9] tot en met [14].
- `research-risk-design.md` — bronnen [15] tot en met [20].
- `research-fde-iteratie.md` — bronnen [21] tot en met [26].

Een convergence-pass tegen een externe Gemini Deep Research (`convergence-gemini.md`) heeft de bronnenset uitgebreid met de Obeidat-flow, NL AIC, PACE en de Stanford Enterprise AI Playbook. Open punten uit de eindpass:

- *MAJOR* — eerder ontbrekend kant-en-klaar discovery-playbook is opgelost via de Obeidat-bronnen.
- *MAJOR* — Stanford Enterprise AI Playbook PDF is niet tekstueel gefetcht; bevindingen staan op `inferred`.
- *MINOR* — OWASP Agentic AI Top-10 (late 2025) bestaat als vermelding maar de directe URL is niet primair geverifieerd.
- *MINOR* — SVPG-kritiek op FDE is geciteerd via Pragmatic Engineer; directe SVPG-pagina gaf 403.

De blueprint behandelt deze open punten conservatief: claims op `inferred` of `unverified` worden in de tekst voorzichtig gepositioneerd ("richtinggevend, niet betrouwbaar als hard cijfer").

## B.5 Aanwijzing voor herziening

Bij een nieuwe blueprint-versie:

- Verifieer de URLs (link-rot is het grootste risico).
- Werk de verificatiestatus bij waar nieuwe primaire bronnen beschikbaar komen.
- Toets of de tier-classificaties (EU AI Act, [15]) en de DPIA-context ([18, 19]) niet zijn gewijzigd door nieuwe wetgeving of jurisprudentie.
- Bij AI BOM-eisen (hoofdstuk 7.3): toets of de ISO 27001 / SOC 2 Type II-status van leveranciers nog actueel is.

## B.6 Status / laatste herziening

- Versie: 1.0
- Laatst bijgewerkt: 2026-04-28
- Wijzigingen sinds vorige versie: eerste vastlegging.
