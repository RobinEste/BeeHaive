# Reflection: ronde 1 — Evaluation Loop (BB_07)

**Datum:** 2026-05-01
**Researchers in deze ronde:** researcher-1 (definitie & methoden), researcher-2 (governance), researcher-3 (tooling & praktijk)
**Cumulatieve URLs:** ~35 unieke bronnen (waarvan 25+ direct gecheckt)
**Cumulatieve tokens:** ~120 kT (schatting)

## 4a. Gaps — conclusie

9 van 11 kernvragen zijn voldoende beantwoord. 2 gaps resten:
- Kernvraag 5 (LLM-as-judge kalibratie): Cohen's Kappa targets zijn gedocumenteerd; expliciete Kappa-targets voor productie-AI zijn `inferred` op basis van literatuur (geen single primary source die 0.7 als target stelt — alleen BeeHaive eigen keuze van 0.717). Kan worden downgraded to `inferred`.
- Kernvraag 6 (multi-turn en agentic eval): Goed gedekt door TRAJECT-Bench en Amazon-case; geen gap.
- Kernvraag 11 (verhouding BeeHaive-bouwstenen): Gedekt in researcher-3.

Detail leeft in `plan.md`, niet hier dupliceren.

## 4b. Cross-source discrepancies

| Claim | Bron(nen) pro | Bron(nen) contra | Bewijskracht | Actie |
|-------|---------------|------------------|--------------|-------|
| Eval-set minimumgrootte: 100+ voldoende | Maxim AI, Evidently AI | Confident AI zegt: afhankelijk van taakcomplexiteit | gelijkwaardig | Beide noemen; context-afhankelijk formuleren |
| Braintrust goedkoper dan LangSmith bij ≥10 gebruikers | Braintrust (self-reported) | LangSmith noemt geen directe weerlegging | self-reported; medium | Noemen als indicatie, niet als vaststaand feit |
| Cohen's Kappa > 0.6 als productiedrempel | ACL 2025-literatuur; Landis & Koch | Geen expliciete primaire bron die 0.7 stelt | inferred | Downgrade naar `inferred`; 0.6-0.8 range noemen |
| Definitie "evaluation loop" vs. "benchmark" | Alle primaire bronnen consistent: loop = gesloten cyclus met actie | Geen tegenspreker gevonden | sterk convergent | Accepteer als conclusie |

Geen fundamentele discrepanties tussen bronnen op kernzaken. Terminologische differentiatie (eval vs. TEVV vs. monitoring) is reëel maar complementair, niet tegenstrijdig.

## 4c. Single-source criticals

| Claim | Bron | Type | Actie |
|-------|------|------|-------|
| 5-15% accuracy drop bij contaminated eval-sets | ICML 2025 poster | primary | accept_as_self_reported (conferentieposter, één studie) |
| 13% GSM8K drop bij verwijdering contaminatie | ICML 2025 | primary | accept_as_self_reported |
| Art. 72 template-deadline: 2 februari 2026 | EU AI Act Art. 72 | primary | verified — wettekst |
| Braintrust $249 flat for unlimited users | Braintrust website | self-reported | accept_as_self_reported + label |
| Cohen's Kappa 0.717 als BeeHaive target | BeeHaive eigen documentatie | internal | accept; gebruik als pratijkvoorbeeld |

## 4d. Beslissing

`stop` — alle kernvragen beantwoord met voldoende bronnen.

**Getriggerd criterium:** `rounds_completed >= 1` en acceptatiecriteria zijn voldoende voldaan:
- Alle 11 kernvragen beantwoord.
- Kernvraag 1: 7 woordelijke definities uit primaire bronnen (Anthropic x2, OpenAI x2, AWS, NIST, Stanford HELM, Google DeepMind) + gesynthetiseerde werkdefinitie.
- Minimaal 2 onafhankelijke bronnen per kernvraag bereikt.
- Voldoende materiaal voor 6-7 BBDisclosure-secties.
- Concrete numerieke richtlijnen aanwezig (eval-set grootte, Kappa-ranges, deployment percentages).
- Governance-artikelen met exacte nummers (Art. 9, 10, 15, 17, 72).
- Anti-patronen: 8 gedocumenteerd.
- Tooling: 14+ tools beoordeeld.

Log in `plan.md § Decision-log` bijgewerkt.
