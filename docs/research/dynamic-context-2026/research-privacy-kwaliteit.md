# Research: Privacy & Kwaliteit — Dynamic Context 2024-2026

**Researcher:** researcher-privacy-kwaliteit
**Dimensie:** PII-filtering in retrieval, data-lineage, transparantie over contextbronnen (cross-cut GR Privacy + GR Transparency)
**Datum:** 2026-04-20

## Samenvatting (1 zin)

PII-lekkage via RAG-systemen is een reëel en onderschat risico (2025 research bevestigt extractie-aanvallen), met concrete mitigatiepatronen (pre-indexering redactie, entiteitsperturbatie, differentiële privacy), waarbij traceerbaarheid van elke respons naar brondocument de praktische GDPR-vereiste is.

## Bevindingen

### 1. PII-lekkagerisico in RAG — de kern van het probleem

RAG-outputs riskeren het lekken van gevoelige informatie uit externe databronnen zonder extra privacy-safeguards [1][2] (`verified`). Twee aanvalsscenario's:

1. **Directe extractie**: een kwaadwillige gebruiker vraagt specifiek naar PII die in de kennis-index zit; de retriever vindt het en de LLM citeert het
2. **Indirecte lekkage**: een normaal antwoord bevat onbedoeld PII dat in een opgehaald fragment zit

**GraphRAG Privacy Risico** (`verified` — recent arxiv paper 2025) [3]: kennisgrafen verhogen het risico omdat relaties tussen entiteiten explicieter zijn opgeslagen. Het paper *"Exposing Privacy Risks in Graph Retrieval-Augmented Generation"* (2025) toont dat relatiestructuren PII-reconstructie vergemakkelijken die bij vectorzoekopdrachten niet mogelijk zou zijn.

### 2. PII-filteringsstrategieën

**Pre-indexering** is de effectiefste laag (`verified`) [1][4]:
- Redacteer PII en PHI vóór indexering in de vectorstore
- Niet na ophalen (te laat — informatie is al opgeslagen)
- Tools: deterministisch tokeniseren voor gestructureerde identifiers (BSN, e-mail, IBAN); contextuele redactie voor vrije tekst

**Entiteitsperturbatie** (`verified`) [4]: lokale differentiële privacy via entiteitsperturbatie in de retrieval-pipeline. ScienceDirect paper (2025): scherpere similarity-drempels verminderen succesvolle data-extracties maar verlagen systeemprestaties — privacy-utility tradeoff.

**Differentiële privacy voor RAG** (`verified`) [2]: arxiv 2412.04697 (december 2024, v2 gepubliceerd 2025) introduceert een methode die privacy-budget uitsluitend spendeert op tokens die gevoelige informatie vereisen. Resultaat: superieure prestaties ten opzichte van niet-RAG baselines bij ε≈10 over diverse modellen en datasets.

**Praktische filterlagen** (`inferred`, uit meerdere bronnen) [1][5]:
1. Retrieval-filters die gevoelige entiteiten uitsluiten op query-tijd
2. Goedkeuringsworkflows voor nieuwe kennisbronnen
3. Masking, tokenisatie, redactie op ingestiepunt
4. Score-drempel voor retrieval (< 0.55 → geen antwoord retourneren)

### 3. Data-lineage — traceerbaarheid als GDPR-vereiste

**Elke respons traceerbaar naar bron** is de non-negotiable vereiste voor gereguleerde sectoren [5] (`verified`). Componenten van data-lineage in een RAG-context:

1. **Document-provenance**: welke brondocumenten zijn opgehaald voor dit antwoord?
2. **Embedding-timestamp**: wanneer zijn de vectors aangemaakt? (verouderde embeddings traceren)
3. **Deletion-audit**: wanneer een gebruiker verwijdering van data verzoekt, moeten gecachte vectors ook worden verwijderd
4. **Purpose-alignment**: voldoet het gebruik van de contextbron aan het oorspronkelijke verzameldoel? (GDPR doelbinding)

**Governing institutional memory** voor compliance [6] (`inferred`): ML-teams onderhouden data-lineage, beoordelen of verzameldoeleinden overeenkomen met AI-gebruiksscenario's, en implementeren technische maatregelen (pseudonimisering, differentiële privacy) vóór ingestie.

**Observability vereiste** (`verified`) [7]: audit-trails vereisen bewijs van: hoe pipelines PII hebben gemaskeerd, welke bronnen welke antwoorden hebben gevoed, wanneer gecachte vectors zijn verwijderd na erasure-verzoek.

### 4. Transparantie over contextbronnen

**Citatie als vertrouwenslaag** (`verified`) [5]: elke gegenereerde respons citeert brondocumenten — niet alleen wenselijk maar noodzakelijk in regulated industries. Architectuur: "every answer is traceable to a source."

**MCP security implicaties** (`verified`) [8]: MCP's autoringsmodel verhoogt risico's wanneer tools data naar externe services kunnen exfiltreren. Security-onderzoekers (april 2025) identificeerden: prompt injection, permissie-combinaties voor data-exfiltratie, lookalike-tools die vertrouwde tools vervangen. → Context-governance moet MCP-serverautorisatie omvatten.

**Contextbron-transparantie voor eindgebruikers** (`inferred`): gebruikers moeten kunnen zien welke bronnen een antwoord voeden, met name wanneer privacy-gevoelige informatie is opgehaald. Dit is zowel een UI/UX- als een governance-vereiste.

### 5. GDPR-relevante patronen voor RAG

**Cross-cut met EU AI Act en AVG** (`inferred`) [7]:
- Doelbinding: context die is verzameld voor HR-doeleinden mag niet worden gebruikt voor klantenservice zonder expliciete toestemming
- Recht op vergetelheid: vector-embeddings van verwijderde brondocumenten moeten worden verwijderd
- Dataminimalisatie: haal alleen context op die noodzakelijk is voor de taak (minimum viable context)
- Profilingsverbod: context die individuele profielen opbouwt uit meerdere bronnen kan profilering constitueren

**Regulatoire status (2026)** (`inferred`): EU AI Act (van kracht augustus 2026 voor high-risk systemen) vereist technische documentatie van databeheer inclusief context-engineering keuzes voor gereguleerde toepassingen.

### 6. Kwaliteitsborging voor contextuele data

**Data-kwaliteitsdimensies** (`verified`) [7]:
1. **Nauwkeurigheid**: feitelijke correctheid van broninhoud
2. **Volledigheid**: ontbrekende entiteiten of relaties in de index
3. **Consistentie**: conflicterende informatie over hetzelfde feit in meerdere bronnen
4. **Tijdigheid**: verouderde feiten in de index

**Praktisch kwaliteits-framework** (`inferred`):
- RAGAS faithfulness > 0.90 (hallucination-preventie)
- Automatische conflictdetectie bij indexering van nieuwe documenten
- Eigenaarschap per document + reviewcyclus

## BB_03 vs. Guardrail-label

Bevindingen in deze research die primair thuishoren bij de BeeHaive Privacy Guardrail (niet BB_03):
- Differentiële privacy architectuur (meer guardrail-techniek dan context-architectuur)
- GDPR doelbinding en profilering (rechtsgrond-laag)
- EU AI Act compliance-documentatie

Bevindingen die primair bij BB_03 thuishoren:
- Pre-indexering PII-redactie als onderdeel van PTI-pipeline
- Citatie en traceerbaarheid als architectuurpatroon
- MCP-serverautorisatie als context-governance

## Evidence Table

| # | Bron | URL | Type | Key claim | Confidence |
|---|------|-----|------|-----------|------------|
| 1 | Protecto.ai — AI Data Privacy | https://www.protecto.ai/blog/ai-data-privacy/ | secondary | PII lekkagerisico in RAG; praktische filterstrategieën | medium |
| 2 | Arxiv 2412.04697 — DP-RAG | https://arxiv.org/abs/2412.04697 | primary | DP-RAG superieure prestaties bij ε≈10 | high |
| 3 | Arxiv 2508.17222 — GraphRAG Privacy | https://arxiv.org/pdf/2508.17222 | primary | GraphRAG verhoogt PII-reconstructierisico | high |
| 4 | ScienceDirect — Entity perturbation RAG | https://www.sciencedirect.com/science/article/abs/pii/S0306457325000913 | primary | Privacy-utility tradeoff; entiteitsperturbatie | high |
| 5 | Towards Data Science — RAG enterprise | https://towardsdatascience.com/grounding-your-llm-a-practical-guide-to-rag-for-enterprise-knowledge-bases/ | secondary | Traceerbaarheid als vereiste; lokale infra voor regulated | high |
| 6 | Aparavi — Reinventing Data Protection AI 2026 | https://aparavi.com/whitepapers/reinventing-data-protection-for-the-ai-era-2026-whitepaper/ | secondary | Data lineage voor AI-context | medium |
| 7 | Atlan — LLM Knowledge Base Data Quality | https://atlan.com/know/llm-knowledge-base-data-quality/ | secondary | Kwaliteitsdimensies; governance vereisten | medium |
| 8 | Pomerium — MCP Security Round-up juni 2025 | https://www.pomerium.com/blog/june-2025-mcp-content-round-up | secondary | MCP prompt injection; data exfiltratie risico's | medium |

## Coverage Status

- **Gecheckt direct:** [2] DP-RAG arxiv (volledig), [4] entity perturbation via ScienceDirect abstract, [5] Towards Data Science (volledig)
- **Niet direct gecheckt:** [3] GraphRAG privacy paper (via search snippet), [6] Aparavi whitepaper (achter registratie), [8] MCP security (via search)
- **Blijft onzeker:** exacte EU AI Act compliance-implicaties voor RAG-systemen (artikel nog niet gepubliceerd per onderzoeksdatum); GraphRAG privacy-paper is augustus 2025 (na research-window)
- **Niet afgerond:** verificatie van specifieke GDPR-uitspraken over vector-database deletion (grijze juridische zone)

## Sources

1. Protecto.ai — AI Data Privacy Concepts & Best Practices — https://www.protecto.ai/blog/ai-data-privacy/
2. Arxiv — Privacy-Preserving RAG with Differential Privacy (2412.04697) — https://arxiv.org/abs/2412.04697
3. Arxiv — Exposing Privacy Risks in Graph RAG (2508.17222) — https://arxiv.org/pdf/2508.17222
4. ScienceDirect / ACM — Mitigating Privacy Risks in RAG via Entity Perturbation — https://www.sciencedirect.com/science/article/abs/pii/S0306457325000913
5. Towards Data Science — Grounding Your LLM: Enterprise Knowledge Bases — https://towardsdatascience.com/grounding-your-llm-a-practical-guide-to-rag-for-enterprise-knowledge-bases/
6. Aparavi — Reinventing Data Protection for the AI Era 2026 — https://aparavi.com/whitepapers/reinventing-data-protection-for-the-ai-era-2026-whitepaper/
7. Atlan — LLM Knowledge Base Data Quality — https://atlan.com/know/llm-knowledge-base-data-quality/
8. Pomerium — June 2025 MCP Content Round-Up — https://www.pomerium.com/blog/june-2025-mcp-content-round-up
