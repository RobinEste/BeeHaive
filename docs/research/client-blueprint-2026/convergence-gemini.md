# Convergence-pass: BeeHaive deep research × Gemini deep research

**Datum:** 2026-04-26
**Onderwerp:** BB_02 Client Blueprint
**Externe bron:** `external/gemini-synthese-2026-04-26.md` (Gemini Deep Research, gevraagd door Robin)
**Onze bron:** `final.md` (4-lane parallelle deep-research, 26 verified/inferred sources)
**Aanvullende externe input (clippings → bronnen-archief):**
- bron-131 — Sam Obeidat, How to Identify an AI Use Case in 7 Steps (CAIO Newsletter)
- bron-132 — Sam Obeidat, The AI Business Model Canvas (AI-BMC)
- bron-133 — Seroter & Sanin, 101 gen AI use cases with technical blueprints (Google Cloud)

---

## Doel

Deze pass legt expliciet vast (a) waar onze pipeline en de externe Gemini-synthese hetzelfde concluderen, (b) wat Gemini wel had en wij niet, (c) wat wij wel hadden en Gemini niet, (d) waar bronnen elkaar tegenspreken. Dit is een eerste invulling van het *convergence-pass*-patroon (zie ROADMAP — kandidaat voor uitbreiding van /deep-research).

---

## A. Gedeelde kernbevindingen (cross-validated)

Beide pipelines komen onafhankelijk uit op dezelfde kernpatronen — relatief sterk bewijs dat dit *het stabiele veld* is voor BB_02:

1. **Decision-first / outcome-first als startpunt** — Kozyrkov bij ons; "AI-ambitie" + "compliance by design" bij Gemini. Beide: AI volgt uit de bedrijfsvraag, niet andersom.
2. **De 95%-faaldiagnose** — Gemini noemt "stagnatie na pilotfase"; wij hebben MIT NANDA + Marketing AI Institute kritiek expliciet. Diagnose convergeert: mismatch tussen AI-aanpak en bedrijfsprobleem, niet de techniek.
3. **EU AI Act risico-tiers als ontwerpinput** — beide met dezelfde 4-tier-structuur en dezelfde art.-verwijzingen (Art. 6, 11, 17, 18, 55).
4. **HLEG 7 vereisten + ALTAI als checklist** — beide pipelines noemen dit als blueprint-control.
5. **Modelselectie multi-criteria + Model Routing** — beide noemen Task Fit, Parameter Count, Context Window, Reasoning, Output Consistency en Model Routing als architectuurpatroon.
6. **Context Engineering als paradigmaverschuiving** — beide framingen lijnen op (just-in-time retrieval, compaction, multi-agent + KG). Dit hoort bij BB_03, niet BB_02, en dat is consistent.
7. **Multi-agent als specifiek patroon, niet default** — beide pipelines waarschuwen tegen multi-agent als prematuur.
8. **Iteratieve werkwijze ipv waterval** — beide expliciet.

---

## B. Wat Gemini wel had en wij niet (deltas: pickup-kandidaten)

### B1. Strategische framing-instrumenten

- **Gartner AI Opportunity Radar** — twee-assen-positionering (inward/outward × everyday/game-changing). Concrete management-tool om ambitie-bepaling expliciet te maken vóór architectuurkeuze. **Pickup:** noemen in BB_02 als optionele ambitie-tool.
- **BXT-framework (Microsoft ISV)** — Business · Experience · Technology. Aanvulling op AI-3P (People · Process · Product) door *Experience* als eigen pijler — UX/adoptie. **Pickup:** als optie naast AI-3P.

### B2. AI-canvassen-typologie

Onze research had alleen Hyacinth 8-Steps + Sparkco templates. Gemini biedt drie aanvullende AI-canvassen:

- **Board of Innovation AI Canvas** — sterk op haalbaarheid + tech (Value Proposition, Data, Capabilities, Key Dependencies, Systems & Platforms).
- **BrandKarma AI/Tech Use Case Canvas** — sterk op governance + UX (Human Interaction, Ethics & Legal, Stakeholders & Impact). Voegt expliciet bias/inclusiviteit/AVG/EU AI Act in een canvas-veld.
- **AI Model Canvas** — technisch, focus op interactie ML-model × menselijk oordeel + voorspellingskosten.

**Pickup:** noemen als typologie. De BrandKarma-ethics-laag is een echte aanvulling op onze risk-design (klassieke canvassen vangen geen ethics).

### B3. NL-context

- **Nederlandse AI Coalitie (NL AIC)** — werkgroep Data Delen, interoperabiliteitsrichtlijnen voor data spaces.
- **PACE-platform** — Participative And Constructive Ethics — ethiek als proactief ontwerpprincipe ipv compliance-vink achteraf.
- **AI Bill of Materials (AI BOM)** — vendor-governance-output: leveranciers leveren een AI BOM als compliance-bewijs.

**Pickup:** sterk onderscheidend voor BeeHaive (Nederlands publiek). Verdient een eigen paragraaf.

### B4. Concrete benchmark-cijfers (voor BB_07, niet BB_02)

- AI Reply Correctness: 85-90% target
- Faithfulness: 85-95% (zorg: 95%)
- Hallucination Rate: ≤5-15% afhankelijk van domein
- Cijfers zijn `inferred` (Gemini geeft geen primaire bron) maar consistent met industrie-praktijk.

**Pickup:** doorzetten naar BB_07 (Evaluation Loop).

### B5. Strategische merkmetrieken

- Share of LLM Voice (SoLV)
- Narrative Accuracy Score
- Context and Sentiment Quality
- Query Intent Alignment

**Pickup:** noemen onder "evaluation" maar primaire plek is BB_07. Voor BB_02: signaleren dat *evaluatie-criteria al in de blueprint-fase moeten worden gedefinieerd*.

### B6. Governance-organisatiemodel

- **AI Comité / Center of Excellence** met Head of AI als voorzitter, vertegenwoordigers uit tech, juridisch, infosec, dataportefeuille.
- **Vendor Governance** met AI BOM-eis voor derde partijen.
- **JLL** en **Workday** als concrete voorbeelden.

**Pickup:** korte vermelding in BB_02-governance-paragraaf, dieper in BB_07 of in een Guardrail.

---

## C. Wat wij wel hadden en Gemini niet (onze pipeline sterker)

### C1. Concrete prototype-tools-vergelijking

Onze pipeline had Stitch / v0 / Lovable / Bolt / Claude Artifacts met sterktes en faalmodi per tool (NxCode + Lenny's Newsletter). Gemini noemt prototyping niet expliciet als blueprint-vehikel. Dit is een echte BeeHaive-eigen toevoeging.

### C2. FDE expliciet onderbouwd

Pragmatic Engineer over FDE-oorsprong (Palantir "Delta") + SVPG-contra-perspectief (Cagan). Gemini noemt FDE niet. Voor Robin's werkpraktijk centraal.

### C3. Anthropic's 5 patronen + multi-agent benchmark

Anthropic's Building Effective Agents (5 workflow-patronen) + Multi-Agent Research System (90,2% beter, 15× tokens) als concrete autoritatieve referentie. Gemini noemt multi-agent + KG maar niet de 5-patronen-typologie.

### C4. MCP als standaard tooling-laag

Anthropic MCP (nov 2024), 97M+ SDK-downloads, OpenAI-adoptie maart 2025, beveiligingsrisico's april 2025. Gemini noemt MCP niet expliciet.

### C5. OWASP LLM Top-10 2025

Gehele Top-10 met correcte nummering (LLM07 System Prompt Leakage, LLM08 Vector/Embedding). Gemini noemt threat modeling niet expliciet.

### C6. AI-3P Assessment Framework (Tosic)

Kwantitatief 0-100 scoringsmodel met beslisdrempels. Gemini heeft alleen het BXT-framework (kwalitatief).

### C7. WorkOS Three-Signals Framework

Concrete geschiktheidstoets voor agent vs. workflow vs. rule-based. Gemini noemt deze drie-signalen-test niet.

---

## D. Aanvullingen uit clippings (bron-131, 132, 133)

### D1. Sam Obeidat — 7-stappen Discovery + AI-BMC (bron-131, 132)

**Status:** lost het MAJOR open punt op uit final.md ("geen kant-en-klaar gepubliceerd discovery-playbook"). Gevalideerd met World AI Council members, geüpdatet dec 2025.

**Pickup voor BB_02 (kern):**
1. Map Value Stream (trigger → outcome)
2. TRACE workflow-mapping (Trigger, Route, Annotate, Check, Escalate)
3. Probleemformulering (Current State + Pain + Quantified Impact + Who)
4. Value Proposition langs 6 AI Value Objectives (Speed, Cost, Revenue, Quality, Robustness, Impact)
5. AI Solution Canvas (5 velden, niet-technisch)
6. Feasibility Check Canvas (data + tech)
7. Impact Estimation Canvas (Time · Cost · Quality/Risk · Decision Impact)
8. Daarna AI-BMC met 11 blokken voor business-model-validatie

Dit wordt het *organisatorische skelet* van de nieuwe BB_02-pagina. Value-stream-eerste-aanpak congrueert met Robin's voorkeur voor unFIX (Appelo).

### D2. Google Cloud 101 Blueprints (bron-133)

Vendor-specifieke referentie-architecturen in 10 industrie-clusters. **Pickup:** noemen als een van de referentie-bibliotheken voor pattern-recognition (naast AWS Solutions Library, Azure Reference Architectures), niet als voorgeschreven oplossing.

---

## E. Tegenstrijdigheden tussen bronnen

### E1. Modelvolwassenheid vs. context engineering

Gemini-synthese (§4) stelt: "Prompt engineering loopt onherroepelijk tegen de eigen grenzen aan" en moet vervangen worden door context engineering. Onze BB_04-research (Prompt Design) en Anthropic's Building Effective Agents stellen genuanceerder: prompt design is niet *vervangen* maar *gepromoveerd* — het iteratieve gesprek en de heldere betekenis-articulatie blijven kern; context engineering is een aanvullende discipline op systeemniveau.

**Resolutie:** beide kunnen waar zijn op verschillende niveaus. Voor *single-turn interactions* is prompt design de centrale discipline; voor *multi-turn agentic systems* is context engineering kritisch. BB_02 hoeft hier geen positie in te nemen — verwijs door naar BB_04 (prompt) en BB_03 (context).

### E2. FDE als best practice vs. SVPG-kritiek

Onze deep research had al beide kanten (Pragmatic Engineer vs. Cagan/SVPG). Gemini noemt FDE niet, dus geen tegenspraak — wel een gat dat onze pipeline beter dekt.

### E3. AI-canvas-veelheid

Gemini suggereert *hybride* werkwijze (BoI + BrandKarma combineren). Sam Obeidat (bron-131/132) suggereert *één playbook* (7 stappen + AI-BMC). Beide zijn legitiem; verschil is in *granulariteit* en *fase*. Geen echte tegenspraak — Obeidat's flow is een *implementatie* van het hybride canvas-idee.

---

## F. Nieuwe BB_02-structuur na deze pass

Op basis van de convergence wordt de BB_02-narrative georganiseerd rond:

1. **Ambitie & risico-bereidheid** (Gartner Radar)
2. **Value stream als startpunt** (Obeidat + unFIX/Appelo) — *organiserend principe*
3. **Workflow-diagnose** (TRACE)
4. **Probleem-framing** (Kozyrkov decision-first + Obeidat-formule)
5. **Geschiktheidstest** (WorkOS three-signals + AI-3P-readiness)
6. **AI Solution Canvas** (Obeidat) — bruglaag tussen probleem en techniek
7. **Architectuurkeuze** (Anthropic 5 patronen, MCP, RAG/fine-tune/agents-laag)
8. **Risk-by-design** (EU AI Act tier, HLEG/ALTAI, DPIA, OWASP, BrandKarma-ethics)
9. **Prototype als gespreksanker** (Stitch/v0/Lovable/Bolt/Artifacts)
10. **Iteratieve werkwijze** (FDE-principes + AI BOM voor vendor-output)
11. **Governance & sign-off** (AI Comité, NL AIC/PACE, AI-BMC voor business-model-validatie)

---

## G. Convergence-pass als methodisch patroon

Deze pass illustreert de waarde van het *convergence-pass*-patroon:
- **Bias-correctie tussen pipelines** — Claude/Exa miste de canvas-typologie en NL AIC; Gemini miste FDE en MCP. Zonder convergence-pass zouden beide gaten onzichtbaar blijven.
- **Versterkte cross-validation** — punten die in beide pipelines onafhankelijk verschijnen (sectie A) zijn extra robuust.
- **Open-punten-resolutie** — het MAJOR open punt uit final.md (geen kant-en-klaar discovery-playbook) is opgelost door de Sam Obeidat-bronnen die via een ander zoekpad zijn binnengekomen.

**Aanbeveling:** convergence-pass formaliseren als optionele L3-stap in /deep-research:
- `plan.md` krijgt sectie `external_research_inputs:` met paden naar externe deep-research-output.
- Na L2 (final.md) draait een L3-agent die expliciet diff't en `convergence-{provider}.md` produceert.
- Selectieve update van final.md met geadopteerde inzichten, gemarkeerd als `[external-source]`.

Te realiseren via een aparte skill-update voor `~/.claude/skills/deep-research/` — tracken in `claude-code-framework`-roadmap.
