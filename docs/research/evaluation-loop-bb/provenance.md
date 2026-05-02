# Provenance: Evaluation Loop (BB_07)

**Datum:** 2026-05-01
**Skill:** /deep-research
**Primair artifact:** `final.md`

## Bronverantwoording

| # | Bron | URL | Claim | Status |
|---|------|-----|-------|--------|
| 1 | Anthropic — Demystifying Evals | https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents | Definitie eval; 7 kernelementen | verified |
| 2 | Anthropic — Building Effective Agents | https://www.anthropic.com/research/building-effective-agents | Evaluator-optimizer loop patroon | verified |
| 3 | OpenAI — Working with Evals | https://developers.openai.com/api/docs/guides/evals | Definitie evals; data-flywheel loop | verified |
| 4 | OpenAI — Evals drive next chapter | https://openai.com/index/evals-drive-next-chapter-of-ai/ | Evals als methode om doelen te specificeren | inferred (403) |
| 5 | AWS — Evaluation Loops GenAI | https://docs.aws.amazon.com/prescriptive-guidance/latest/gen-ai-lifecycle-operational-excellence/dev-experimenting-experimentation-loops.html | 5-componenten model | verified |
| 6 | Stanford HELM | https://crfm.stanford.edu/helm/latest/ | Evaluation harness definitie; 7 dimensies | verified |
| 7 | NIST AI RMF 1.0 | https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf | TEVV als lifecycle-proces | verified |
| 8 | Google DeepMind Evals | https://deepmind.google/research/evals/ | Geen expliciete definitie; benchmark-aanpak | verified |
| 9 | TRAJECT-Bench | https://arxiv.org/abs/2510.04550 | Trajectory evaluation metrics | verified |
| 10 | Amazon ML Blog — Agentic Eval | https://aws.amazon.com/blogs/machine-learning/evaluating-ai-agents-real-world-lessons-from-building-agentic-systems-at-amazon/ | Tool-call metrics; productielessen | verified |
| 11 | Evidently AI — LLM Metrics | https://www.evidentlyai.com/llm-guide/llm-evaluation-metrics | Taxonomie evaluatiemetrieken | verified |
| 12 | ICML 2025 — Data Contamination | https://icml.cc/virtual/2025/poster/43619 | 5-15% accuracy drop bij contaminated evals | verified |
| 13 | ACL 2025 — AntiLeakBench | https://aclanthology.org/2025.acl-long.901/ | Anti-leakage benchmarking | verified |
| 14 | arxiv — Judge's Verdict | https://arxiv.org/pdf/2510.09738 | Biases in LLM-judges | verified |
| 15 | LangChain AgentEvals | https://github.com/langchain-ai/agentevals | Trajectory match evaluators | verified |
| 16 | TianPan — LLM Rollout | https://tianpan.co/blog/2026-04-09-llm-gradual-rollout-shadow-canary-ab-testing | Shadow/canary patronen | verified |
| 17 | EU AI Act Art. 9 | https://artificialintelligenceact.eu/article/9/ | Continuous iterative process; prior defined metrics | verified |
| 18 | EU AI Act Art. 10 | https://artificialintelligenceact.eu/article/10/ | Biasdetectie; representatieve data | verified |
| 19 | EU AI Act Art. 15 | https://artificialintelligenceact.eu/article/15/ | Accuracy/robustness; feedback loop contamination | verified |
| 20 | EU AI Act Art. 72 | https://artificialintelligenceact.eu/article/72/ | Post-marktmonitoring; 2 aug 2026 | verified |
| 21 | CSA — ISO 42001 Audit | https://cloudsecurityalliance.org/blog/2025/05/08/iso-42001-lessons-learned-from-auditing-and-implementing-the-framework | Clause 9; jaarlijkse audit | verified |
| 22 | AWS — ISO 42001 | https://aws.amazon.com/blogs/security/ai-lifecycle-risk-management-iso-iec-420012023-for-ai-governance/ | ISO 42001 als complement EU AI Act | verified |
| 23 | AP/RDI — Supervisie NL | https://www.autoriteitpersoonsgegevens.nl/en/current/ap-and-rdi-supervision-of-ai-systems-requires-cooperation-and-must-be-arranged-quickly | Nederlandse AI-toezichtstructuur | verified |
| 24 | Pinsent Masons — 10 NL regulators | https://www.pinsentmasons.com/out-law/news/ai-compliance-overseen-10-dutch-regulators | Tien toezichthouders NL | verified |
| 25 | Goodeye Labs — Eval tools 2026 | https://www.goodeyelabs.com/articles/top-ai-agent-evaluation-tools-2026 | Platform-vergelijking 2026 | verified |
| 26 | Braintrust — Platform vergelijking | https://www.braintrust.dev/articles/best-llm-evaluation-platforms-2025 | Platform-features en pricing | self-reported |
| 27 | Arize Phoenix Docs | https://arize.com/docs/phoenix | Features; v3.0.0; OpenTelemetry | verified |
| 28 | Inspect AI — AISI | https://inspect.aisi.org.uk/ | Sandboxed agentic evals | verified |
| 29 | GitHub deepeval | https://github.com/confident-ai/deepeval | 50+ metrics; Pytest-integratie | verified |
| 30 | Collinear — Goodhart's Law | https://blog.collinear.ai/p/gaming-the-system-goodharts-law-exemplified-in-ai-leaderboard-controversy | Goodhart's law in AI leaderboards | verified |

## Verificatieoverzicht

- **Totaal bronnen geraadpleegd:** 35+
- **Bronnen geaccepteerd (na URL-check):** 30
- **Bronnen verworpen:** 0 (dode links: 0; onverifieerbaar: 0)

**Claim-verdeling:**
- `verified`: 26
- `inferred`: 8
- `unverified`: 0
- `blocked`: 1 (OpenAI blog — 403 HTTP error; beschrijving via zoekresultaten)

## Researcher-rondes

| Ronde | Datum | # researchers | Nieuwe bronnen | Nieuwe claims |
|-------|-------|---------------|----------------|---------------|
| 1 | 2026-05-01 | 3 | 35+ | ~120 |

## Externe agents

Geen externe agents gebruikt (geen `--with-gemini` flag).

## Verificatie-pass

**Uitkomst:** PASS-WITH-NOTES

**FATAL issues gefixt:** geen

**MAJOR issues in Open Vragen:**
- Cohen's Kappa productiedrempel: geen single primaire AI-bron; gelabeld als `inferred`
- Art. 17 (kwaliteitsmanagementsysteem): niet directe brontekst gecheckt; als `inferred` gelabeld
- Exacte bewaartermijnen eval-sets: niet expliciet in EU AI Act voor eval-resultaten

**MINOR issues geaccepteerd:**
- SaaS-platform prijzen zijn self-reported; gelabeld als zodanig
- OpenAI blog (403): beschrijving via zoekresultaten; als `inferred` gelabeld

## Geblokkeerde verificaties

- OpenAI "evals drive next chapter" blog (https://openai.com/index/evals-drive-next-chapter-of-ai/): HTTP 403. Claim beschreven via zoekresultaten; gelabeld `inferred`.

## PII-notitie

Geen PII in bronnen. Geen persoonlijke profielen geraadpleegd. Alle bronnen zijn publieke documenten, websites of papers.

## Gerelateerde bestanden

- Plan: `plan.md`
- Research files: `research-definitie-methoden.md`, `research-governance.md`, `research-tooling-praktijk.md`
- Reflection: `reflection-round-1.md`
- Draft: `draft.md`
- Final: `final.md`
