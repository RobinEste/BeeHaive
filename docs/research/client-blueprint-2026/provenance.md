# Provenance: BB_02 Client Blueprint — Actuele Patronen voor AI-oplossingen (2024-2026)

**Datum:** 2026-04-26
**Skill:** /deep-research
**Primair artifact:** `final.md`

## Bronverantwoording

| # | Bron | URL | Claim | Status |
|---|------|-----|-------|--------|
| 1 | Kozyrkov — AI-First Leadership (INFORMS) | https://pubsonline.informs.org/do/10.1287/LYTX.2025.02.02n/full/ | Decision-first framework, drie evaluatiecriteria | inferred |
| 2 | Acceldata — Kozyrkov on AI Leadership | https://www.acceldata.io/blog/cassie-kozyrkov-on-what-it-really-means-to-be-ai-first-key-takeaways-for-enterprise-leaders | "Purpose comes from people", AI-first definitie | inferred |
| 3 | Inference by Sequoia — Software 3.0 | https://inferencebysequoia.substack.com/p/andrej-karpathys-software-30-and | Karpathy Software 3.0 keynote YC 19 jun 2025 | inferred |
| 4 | Medium (Pouladian) — Software 3.0 | https://medium.com/@ben_pouladian/andrej-karpathy-on-software-3-0-software-in-the-age-of-ai-b25533da93b6 | LLM als OS-metafoor | inferred |
| 5 | Fortune — MIT 95% rapport | https://fortune.com/2025/08/18/mit-report-95-percent-generative-ai-pilots-at-companies-failing-cfo/ | MIT NANDA rapport aug 2025, methodologie | verified |
| 6 | Marketing AI Institute — MIT-kritiek | https://www.marketingaiinstitute.com/blog/mit-study-ai-pilots | Methodologische beperkingen 95%-claim | verified |
| 7 | Microsoft AI Decision Framework | https://github.com/microsoft/Microsoft-AI-Decision-Framework | Kwantificeerbaarheidscriterium | unverified |
| 8 | Towards Data Science — AI-3P | https://towardsdatascience.com/the-ai-3p-assessment-framework/ | People-Process-Product scoringsmodel | verified |
| 9 | Anthropic — Building Effective Agents | https://www.anthropic.com/research/building-effective-agents | 5 patronen, begin-simpel-regel, tool design | verified |
| 10 | Anthropic Engineering — Multi-agent system | https://www.anthropic.com/engineering/multi-agent-research-system | 90.2% verbetering, 15x token-gebruik | verified |
| 11 | Anthropic — MCP introductie | https://www.anthropic.com/news/model-context-protocol | MCP architectuur, 25 nov 2024, adoptie | verified |
| 12 | EU AI Act — High-Level Summary | https://artificialintelligenceact.eu/high-level-summary/ | Vier risico-tiers, Tier 2 design-verplichtingen | verified |
| 13 | HLEG Ethics Guidelines | https://digital-strategy.ec.europa.eu/en/library/ethics-guidelines-trustworthy-ai | HLEG 7 vereisten | verified |
| 14 | ALTAI checklist | https://altai.insight-centre.org/ | HLEG zelfbeoordelingschecklist bestaat | verified |
| 15 | ICO GDPR AI guidance | https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/artificial-intelligence/guidance-on-ai-and-data-protection/what-are-the-accountability-and-governance-implications-of-ai/ | DPIA-verplichting voor AI | verified |
| 16 | TechGDPR — AI Act/GDPR samenloop | https://techgdpr.com/blog/data-protection-digest-03112025-new-ai-act-and-gdpr-study-personal-data-stored-on-blockchain/ | FRIA vs DPIA overlap | verified |
| 17 | OWASP LLM Top-10 2025 | https://genai.owasp.org/llm-top-10/ | Volledige LLM Top-10 2025 | verified |
| 18 | Pragmatic Engineer — FDE | https://newsletter.pragmaticengineer.com/p/forward-deployed-engineers | FDE origine, drie fasen, beperkingen | verified |
| 19 | SSO Network — FDE guide | https://www.ssonetwork.com/intelligent-automation/columns/forward-deployed-engineers-guide | 800% vacature-stijging, Salesforce 1000 FDEs | verified |
| 20 | NxCode — Vibe Design Tools 2026 | https://www.nxcode.io/resources/news/vibe-design-tools-compared-stitch-v0-lovable-2026 | Tool-vergelijking, sterktes/faalmodi | verified |
| 21 | Lenny's Newsletter — AI Prototyping | https://www.lennysnewsletter.com/p/a-guide-to-ai-prototyping-for-product | Wanneer productief, kritische kanttekening | verified |
| 22 | WorkOS — Enterprise AI Agent Playbook | https://workos.com/blog/enterprise-ai-agent-playbook-what-anthropic-and-openai-reveal-about-building-production-ready-systems | Drie-signalen framework voor agent-geschiktheid | verified |
| 23 | Stanford Enterprise AI Playbook PDF | https://digitaleconomy.stanford.edu/app/uploads/2026/03/EnterpriseAIPlaybook_PereiraGraylinBrynjolfsson.pdf | 73% klein gestart, 63% pilot-als-experiment | inferred (PDF niet tekstueel leesbaar) |

## Verificatieoverzicht

- **Totaal bronnen geraadpleegd:** 26 (inclusief aanvullende bronnen)
- **Bronnen geaccepteerd (na URL-check):** 23
- **Bronnen verworpen** (dode link, onverifiëerbaar): 0
- **Bronnen geblokkeerd** (403-fout, PDF niet leesbaar): 3

**Claim-verdeling:**
- `verified`: 16
- `inferred`: 6
- `unverified`: 1
- `blocked`: 0

## Researcher-rondes

| Ronde | Datum | # researchers | Nieuwe bronnen | Nieuwe claims |
|-------|-------|---------------|----------------|---------------|
| 1 | 2026-04-26 | 4 (lanes parallel) | 26 | ~40 kritieke claims |
| Verificatie | 2026-04-26 | lead agent | 0 nieuw | OWASP nummering gecorrigeerd |

## Verificatie-pass

**Uitkomst:** PASS-WITH-NOTES

**FATAL issues gefixt:** OWASP LLM nummering was incorrect in draft (verkeerde nummers voor System Prompt Leakage en Vector/Embedding); gecorrigeerd in final.md na directe fetch van OWASP LLM Top-10 pagina. Correct: LLM07 = System Prompt Leakage, LLM08 = Vector and Embedding Weaknesses.

**MAJOR issues in Open Vragen:**
- Geen enkelvoudige gepubliceerde playbook-template gevonden — 10 blueprint-elementen zijn synthese uit meerdere bronnen
- Stanford Enterprise AI Playbook PDF niet tekstueel leesbaar — bevindingen `inferred`

**MINOR issues geaccepteerd:**
- Kozyrkov-criteria geciteerd via secondaire bronnen (geen directe fetch van primaire keynote)
- Karpathy Software 3.0 via secondaire analyses (originele keynote transcript niet beschikbaar als webpagina)
- SVPG-kritiek via Pragmatic Engineer-citaten (SVPG directe pagina gaf 403)
- OWASP Agentic AI Top-10 (late 2025) vermeld maar directe URL niet geverifieerd

## Geblokkeerde verificaties

- **SVPG FDE-kritiek:** SVPG-website gaf 403-fout. Positie consistent beschreven via Pragmatic Engineer-citaten maar niet direct geverifieerd.
- **Stanford Enterprise AI Playbook:** PDF was image-gebaseerd, niet tekstueel leesbaar. Bevindingen via zoekresultaat-samenvatting beschikbaar.
- **IBM MCP-architectuurpatronen:** developer.ibm.com gaf 403-fout. MCP-architectuur gedekt via Anthropic primaire bron.

## PII-notitie

Geen persoonsgebonden data verwerkt in dit onderzoek. Cassie Kozyrkov en Andrej Karpathy worden bij naam genoemd in hun publieke professionele rol als gepubliceerde auteurs/sprekers. Marina Tosic (AI-3P framework) wordt bij naam genoemd als gepubliceerde auteur. Geen anonimisering noodzakelijk.

## Gerelateerde bestanden

- Plan: `plan.md`
- Research files: `research-usecase-framing.md`, `research-architectuur.md`, `research-risk-design.md`, `research-fde-iteratie.md`
- Draft: `draft.md`
- Final: `final.md`
