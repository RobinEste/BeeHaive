# Provenance: Prompt Design 2026

**Datum:** 2026-04-15
**Skill:** /deep-research
**Primair artifact:** `final.md`
**Atom:** `resources/frameworks/prompt-design.md`

## Verificatieoverzicht

- **Totaal bronnen geraadpleegd:** ~40 (R1: 22, R2: 6, R3: 25, R4: 23 — overlap na deduplicatie)
- **Bronnen geaccepteerd (na URL-check):** ~35
- **Bronnen verworpen:** 2 (iBuidl URL kwetsbaar — lage kwaliteit, wel gebruikt als verifieerbare claim-bron; Anthropic claude-s-character: 404)

**Claim-verdeling:**
- `verified`: ~60% — vendordocs en EU AI Act direct gescraped; academische papers via arXiv/ACL
- `inferred`: ~25% — mapping van regelgeving naar prompt-design; generalisaties over model-generaties
- `unverified`: ~15% — iBuidl-statistieken, self-reported benchmark-cijfers van vendors
- `blocked`: 1 (Anthropic claude-s-character: HTTP 404)

## Researcher-rondes

| Ronde | Datum | # Researchers | Dimensies | Nieuwe bronnen |
|-------|-------|---------------|-----------|----------------|
| 1 | 2026-04-15 | 4 | Academisch, Vendor Docs, Industry, Agentic+Guardrails | ~40 |

Geen ronde 2 nodig — alle 8 focusvragen gedekt.

## Verificatie-pass

**Uitkomst:** PASS-WITH-NOTES

**FATAL issues gefixt:** geen

**MAJOR issues in Open Vragen:**
- iBuidl-statistieken onvoldoende peer-reviewed onderbouwd — in final gelabeld als `unverified` (richting `verified`)
- Prompting Inversion gemeten op GPT-5; overdraagbaarheid naar Claude 4.6 / Gemini 3 onbevestigd
- EU AI Act-implicaties zijn `inferred` gebaseerd op wettekst — geen jurisprudentie of EDPB-guidance gevonden

**MINOR issues geaccepteerd:**
- NIST AI 100-1 PDF niet direct gelezen (toegang geblokkeerd); gedekt via secondary sources
- ISO 42001 volledige tekst betaalde standaard; gedekt via implementatiegidsen
- Niet alle ACL/EMNLP 2025 proceedings systematisch gescand

## Geblokkeerde verificaties

- Anthropic claude-s-character (https://www.anthropic.com/research/claude-s-character): HTTP 404 — claim over inherente identiteit niet verifieerbaar via deze URL

## PII-notitie

Geen persoonsgebonden informatie verwerkt. Auteursnamen in bronvermelding zijn publieke academische auteurs.

## Gerelateerde bestanden

- Plan: `plan.md`
- Research files: `research-academisch.md`, `research-vendor-docs.md`, `research-industry.md`, `research-agentic-guardrails.md`
- Draft: (gecombineerd direct in final)
- Final: `final.md`
- Atom: `~/ODIN/resources/frameworks/prompt-design.md`
