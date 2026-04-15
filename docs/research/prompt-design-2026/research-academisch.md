# Research: Academisch — Prompt Design 2026

**Researcher:** researcher-1
**Dimensie:** Academisch/foundational — papers, benchmarks, statistieken
**Datum:** 2026-04-15

## Samenvatting (1 zin)
De vier kwantitatieve iBuidl-claims (71%→94% few-shot, +11% XML vs JSON, +34% CoT, >800 tokens instructiedaling) zijn **niet terug te vinden in peer-reviewed of arXiv-literatuur** en moeten als `unverified` worden behandeld; academisch onderzoek bevestigt de algemene richting van sommige claims maar met andere getallen en significante nuances.

---

## Bevindingen

### Statistieken-verificatie (iBuidl-claims)

**Broncheck iBuidl:**
De claims staan letterlijk op `ibuidl.org/blog/prompt-engineering-patterns-2026-20260310` [1], gepubliceerd 10 maart 2026 door "iBuidl Research". De site presenteert geen methodologie, geen testsetomschrijving, geen modelspecificatie, geen vergelijkingsbaseline. De vier getallen verschijnen als marketing-bullets zonder citaties naar primaire bronnen. Na uitgebreid zoeken is geen academische of arXiv-bron gevonden die deze exact-specifieke cijfers ondersteunt.

#### Claim 1: few-shot 71% → 94% betrouwbaarheid (3 voorbeelden)
`unverified`

iBuidl beschrijft dit als "structured output compliance" (JSON-format correctheid), niet als task-accuracy. Wat academisch onderzoek wél zegt:

- **BrittleBench** (Romanou et al., arXiv:2603.13285, Feb 2026) [2]: few-shot prompting verbetert baseline performance substantieel maar vergroot ook brittleness onder prompt-perturbaties — "few-shot prompting leads to higher baseline performance, but more brittleness under perturbations, with up to 12.83% performance degradation." Dit nuanceert de eenvoudige claim.
- **FewMMBench** (Dogan et al., arXiv:2602.21854, Feb 2026) [3]: "instruction-tuned models exhibit strong zero-shot performance but benefit minimally, or even regress, with additional demonstrations or CoT reasoning." Dit tegenspreekt een universeel +23 procentpunt voordeel voor moderne modellen.
- **DOVE** (Habba et al., ACL Findings 2025) [4]: bevestigt wél dat few-shot examples de sensitiviteit voor prompt-variaties verminderen.
- **Fine-tuning vs. Few-shot** (Khoshdel et al., arXiv:2508.04063, Aug 2025) [5]: voor gestructureerde output (JSON) zonder few-shot: F1 ~0.68; met few-shot verbetering aanwezig maar taskspecifiek.

**Conclusie claim 1:** De richting klopt (few-shot verbetert structured output compliance), maar het specifieke bereik 71%→94% is **niet onderbouwd** in peer-reviewed literatuur. Afhankelijk van model en taak varieert het effect sterk.

#### Claim 2: XML +11% t.o.v. JSON op compliance
`unverified`

- **StructEval** (arXiv:2505.20139, 2025) [6]: introduceert een benchmark voor structured output (JSON, XML, YAML, etc.) maar rapporteert geen "XML +11% over JSON" — het benchmark toont juist dat XML een van de moeilijkere formaten is voor sommige taken.
- Medium-analyse door Michael Hannecke (dec 2025) [7]: noemt dat XML de **slechtste token-efficiency** heeft (14% meer tokens dan formatted JSON) en 67.1% LLM comprehension accuracy toont — dit suggereert eerder XML < JSON voor data-interchange, al beveelt Anthropic XML wel aan voor *prompt structure* (niet als output-format).
- Geen arXiv-paper gevonden die "+11% XML compliance over JSON" als algemene claim ondersteunt.

**Conclusie claim 2:** Academisch niet onderbouwd. De practitioner-literatuur wijst eerder op model-afhankelijkheid: Claude prefereert XML voor prompt structuur, GPT prefereert JSON. Een universele +11% is **niet geverifieerd**.

#### Claim 3: CoT +34% op multi-step reasoning
`inferred` (richting klopt, getal niet gecheckt)

- **Wei et al. 2022** (arXiv:2201.11903) [8]: het founding CoT-paper. Op GSM8K: standaard prompting 18%, CoT prompting 57% — dat is +39 percentpunten voor PaLM 540B. Op andere benchmarks: +31.3 pp (Date), diverse getallen per taak. Een "gemiddeld +34%" is niet als enkel getal in dit paper.
- **Hi-CoT** (arXiv:2604.00130, Apr 2026) [9]: "average accuracy improvement of 6.2% (up to 61.4%)" over standaard CoT door hierarchische CoT — het absolute verbetering t.o.v. zero-shot is groter.
- **Robustness study** (Lunardi et al., arXiv:2509.04013, Sep 2025) [10]: "average improvement in accuracy over the zero-shot setting was typically below 3%, with the exception of specific models" — op paraphrase-robuste benchmarks.
- **MME-CoT** (ICML 2025) [11]: CoT verbetert reasoning-heavy taken maar **verslechtert** perception-heavy taken ("overthinking behavior").

**Conclusie claim 3:** CoT verbetert multi-step reasoning aantoonbaar en substantieel, maar "+34%" is een model- en taakspecifieke waarde. Sommige papers tonen grotere winst (GSM8K: +39pp), andere veel kleinere (benchmark-robuste settings: <3%). Het getal is **inferred** als representatief voor specifieke reasoning benchmarks uit 2022-2024, maar niet als universele 2026-claim.

#### Claim 4: System prompt adherentie daalt bij >800 tokens
`inferred` (richting klopt, 800-tokens grens niet bewezen)

- **IFScale** (Jaroslawicz et al., arXiv:2507.11538, Jul 2025) [12]: meet instructie-opvolgingsnauwkeurigheid bij toenemende *instructiedichtheid* (10–500 instructies). Beste frontier-modellen behalen slechts 68% accuracy bij 500 instructies. Drie degradatiepatronen: threshold decay, linear decay, exponential decay. Dit gaat over instructie-aantallen, niet direct over systeem-prompt-woordlengte.
- **LIFBench** (Wu et al., arXiv:2411.07037, Nov 2024 / v3 Jul 2025) [13]: evalueert instruction-following in long-context scenarios (tot 128k tokens). Significante performance-daling naarmate context langer wordt — dit bevestigt de richting.
- **VerIFY** (Robinette et al., EACL Findings 2026) [14]: "longer contexts also pose challenges to system instruction adherence" — bevestigt nadrukkelijk het principe, zonder 800-tokens grens te noemen.
- **System Prompt Robustness** (arXiv:2502.12197, Feb 2025) [15]: guardrail-compliance daalt bij complexere/langere system prompts; reasoning models presteren beter.

**Conclusie claim 4:** De richting is academisch goed onderbouwd — langere prompts leiden tot adherentie-degradatie. Maar de specifieke "800 tokens" grens is een iBuidl-interne bevinding zonder peer-review ondersteuning.

---

### Evolutie van het veld (Q5, Q6)

#### Q5: Prompt engineering → intent/betekenis-articulatie

Geen peer-reviewed paper gevonden die letterlijk stelt "prompt engineering evolueert van LLM-management naar intent-articulatie." Wél een cluster van practitioner-artikelen:

- "Prompt Engineering is Dead. Intent Engineering is the Real Game" (Feroz, Medium, Feb 2026) [16] — niet academisch.
- LoopJar: "Context Engineering: The Skill That Replaced Prompt Engineering in 2026" — niet academisch.

Academisch meest relevant:
- **"You Don't Need Prompt Engineering Anymore: The Prompting Inversion"** (Khan, arXiv:2510.22251, Oct 2025) [17]: Introduceert "Sculpting" als constrained CoT. Kernbevinding: **Prompting Inversion** — constraints die mid-tier modellen (gpt-4o) helpen worden **schadelijk** voor geavanceerde modellen (gpt-5, 94.00% vs 96.36%). "Optimal prompting strategies must co-evolve with model capabilities, suggesting simpler prompts for more capable models." Dit is de academische tegenhanger van de intent/betekenis-claim: naarmate modellen capabeler worden, verschuift de waarde van complexe rolzetting naar intentie-articulatie.

- **The Prompt Report** (Schulhoff et al., arXiv:2406.06608, Jun 2024 / v6 Feb 2025) [18]: grootste systematische survey — 58 LLM prompting-technieken, 33 vocabulaire-termen. Geeft geen evolutie-claim maar legt de taxonomische basis voor het veld.

- **Sahoo et al. survey** (arXiv:2402.07927, Feb 2024 / v2 Mar 2025) [19]: surveys prompt engineering per applicatiegebied. Beschrijft CoT, few-shot etc. als fundamentele technieken.

#### Q6: Ontwikkeling 2024–2026 — welke technieken promoveren/achterhaald?

**Gepromoveerd:**
- **Reasoning-first CoT / structured CoT**: Hi-CoT [9] (+6.2% accuracy, -13.9% tokens), CoT-Valve (ACL 2025) [20] — CoT-lengte comprimeerbaar zonder kwaliteitsverlies.
- **Self-initiated CoT** (MSLR, arXiv:2511.07979, Nov 2025) [21]: door modellen zelf gegenereerde CoT overtreft menselijk-ontworpen CoT.
- **Constrained/structured output via schema-enforcement**: verschuiving van "hope the model follows the prompt" naar native schema-enforcement (OpenAI Structured Outputs mid-2024, Anthropic tool use).
- **Dynamic few-shot retrieval** (i.p.v. statische examples): erkend als superieur in productieomgevingen [Sola Fide, 2026].

**Genuanceerd/uitgedaagd:**
- **Standaard CoT bij instruction-tuned modellen**: FewMMBench [3] toont dat instruction-tuned modellen minimaal profiteren van CoT.
- **Complexe prompt engineering bij frontier models**: "Prompting Inversion" [17] — constraints werken averechts bij gpt-5.
- **Static few-shot**: afhankelijk van de context nu minder effectief dan dynamic retrieval of fine-tuning.
- **Benchmark-gebaseerde evaluatie overall**: BrittleBench [2], DOVE [4], RELIABLEEVAL (ACL EMNLP 2025) [22] tonen aan dat absolute accuracyscores sterk dalen bij paraphrase-variaties — claims over "+X%" moeten altijd met evaluatie-setup worden gespecificeerd.

**Emergente richting (2025–2026):**
Context engineering als opvolger van prompt engineering: verschuiving van "hoe formuleer ik de instructie?" naar "welke informatie geef ik het model?" — breed erkend in de practitioner-literatuur, nog niet als formeel academisch construct gedefinieerd.

---

## Evidence Table

| # | Bron | URL | Type | Key claim | Confidence |
|---|------|-----|------|-----------|-----------|
| 1 | iBuidl Research (2026-03-10) | https://ibuidl.org/blog/prompt-engineering-patterns-2026-20260310 | Blog/non-peer-reviewed | Alle 4 kwantitatieve claims | Laag — geen methodologie |
| 2 | Romanou et al., BrittleBench, arXiv:2603.13285 (Feb 2026) | https://arxiv.org/pdf/2603.13285 | arXiv preprint | Few-shot vergroot brittleness +12.83% onder perturbaties | Hoog |
| 3 | Dogan et al., FewMMBench, arXiv:2602.21854 (Feb 2026) | https://arxiv.org/abs/2602.21854 | arXiv preprint | Instruction-tuned modellen profiteren minimaal van few-shot/CoT | Hoog |
| 4 | Habba et al., DOVE, ACL Findings 2025 | https://aclanthology.org/2025.findings-acl.611/ | ACL peer-reviewed | Few-shot reduces sensitivity to prompt variations | Hoog |
| 5 | Khoshdel et al., arXiv:2508.04063 (Aug 2025) | https://arxiv.org/pdf/2508.04063 | arXiv | Few-shot vs fine-tuning voor structured output (JSON); F1 0.68 → 0.73 | Middel |
| 6 | StructEval, arXiv:2505.20139 (2025) | https://arxiv.org/html/2505.20139 | arXiv | Benchmark voor structured output (JSON/XML/YAML); geen XML-voordeel gevonden | Hoog |
| 7 | Hannecke, Medium (Dec 2025) | https://medium.com/@michael.hannecke/beyond-json-picking-the-right-format | Practitioner blog | XML 14% meer tokens, 67.1% LLM comprehension; JSON preferred for output | Middel |
| 8 | Wei et al., Chain-of-Thought, arXiv:2201.11903 (2022) | https://arxiv.org/pdf/2201.11903v4 | arXiv/NeurIPS | CoT +31–39 pp op GSM8K; emergent bij schaalgrootte | Hoog (founding paper) |
| 9 | Hi-CoT, arXiv:2604.00130 (Apr 2026) | https://www.arxiv.org/pdf/2604.00130 | arXiv preprint | Hi-CoT +6.2% accuracy gemiddeld, -13.9% tokens vs. standaard CoT | Hoog |
| 10 | Lunardi et al., arXiv:2509.04013 (Sep 2025) | https://arxiv.org/html/2509.04013v1 | arXiv | CoT verbetering gemiddeld <3% op paraphrase-robuste benchmarks | Hoog |
| 11 | MME-CoT, ICML 2025 | https://icml.cc/virtual/2025/poster/44904 | ICML peer-reviewed | CoT verslechtert performance op perception-heavy taken | Hoog |
| 12 | IFScale, arXiv:2507.11538 (Jul 2025) | https://arxiv.org/pdf/2507.11538 | arXiv | Instruction-following daalt naar 68% bij 500 instructies; 3 degradatiepatronen | Hoog |
| 13 | LIFBench, arXiv:2411.07037 (Nov 2024) | https://arxiv.org/abs/2411.07037 | arXiv/ACL | Performance daalt bij toenemende context-lengte | Hoog |
| 14 | Robinette et al., VerIFY, EACL Findings 2026 | https://aclanthology.org/2026.findings-eacl.254/ | EACL peer-reviewed | Longer contexts challenge system instruction adherence | Hoog |
| 15 | ArXiv:2502.12197 (Feb 2025) | https://arxiv.org/pdf/2502.12197 | arXiv | System prompt robustness daalt; reasoning models beter | Hoog |
| 16 | Feroz, Medium (Feb 2026) | https://office.qz.com/prompt-engineering-is-dead-intent-engineering | Blog | Evolutie PE → intent engineering | Laag (practitioner only) |
| 17 | Khan, "Prompting Inversion", arXiv:2510.22251 (Oct 2025) | https://arxiv.org/abs/2510.22251 | arXiv | Complexe prompts werken averechts bij frontier models (gpt-5); simpler is better | Hoog |
| 18 | Schulhoff et al., The Prompt Report, arXiv:2406.06608 (v6 Feb 2025) | https://arxiv.org/abs/2406.06608 | arXiv | 58 prompting-technieken; meest complete taxonomie | Hoog |
| 19 | Sahoo et al., arXiv:2402.07927 (v2 Mar 2025) | https://arxiv.org/abs/2402.07927 | arXiv | Survey prompt engineering per applicatiegebied | Hoog |
| 20 | CoT-Valve, ACL 2025 | https://aclanthology.org/2025.acl-long.300.pdf | ACL peer-reviewed | CoT-lengte comprimeerbaar; 95.07% → 94.92% bij 741→225 tokens | Hoog |
| 21 | MSLR, arXiv:2511.07979 (Nov 2025) | https://arxiv.org/abs/2511.07979 | arXiv | Self-initiated CoT overtreft menselijk-ontworpen CoT | Hoog |
| 22 | RELIABLEEVAL, ACL EMNLP Findings 2025 | https://aclanthology.org/2025.findings-emnlp.594.pdf | EMNLP peer-reviewed | Benchmark-evaluaties overschatten performance; few-shot gevoelig voor example-volgorde | Hoog |

---

## Coverage Status

**Gecheckt direct:**
- arXiv.org: few-shot prompting benchmarks 2024–2026
- arXiv.org: CoT benchmarks en surveys 2024–2026
- ACL/EMNLP Anthology 2025 (findings)
- ICML 2025 (MME-CoT)
- EACL Findings 2026 (VerIFY)
- iBuidl.org bronpagina: geverifieerd gelezen
- Structured output / XML vs JSON: arXiv + practitioner literatuur
- System prompt adherentie: IFScale, LIFBench, VerIFY, arXiv:2502.12197
- Prompt engineering evolutie/paradigmaverschuiving: arXiv:2510.22251, The Prompt Report, Sahoo et al.

**Blijft onzeker:**
- Precieze herkomst van de "800 tokens" grens — mogelijk interne iBuidl-test, niet publiek geverifieerbaar
- De "71%→94%" baseline: welk model, welke taak, welke evaluatieprotocol — niet gerapporteerd
- Of "+11% XML over JSON" ergens gepubliceerd is buiten iBuidl — niet gevonden

**Niet afgerond:**
- Geen exhaustieve search op alle EMNLP 2025 proceedings gedaan (te groot)
- ACL 2025 main proceedings slechts steekproefsgewijs gecheckt

---

## Sources

1. iBuidl Research. "Prompt Engineering Patterns That Actually Work in 2026." ibuidl.org, 2026-03-10. https://ibuidl.org/blog/prompt-engineering-patterns-2026-20260310
2. Romanou, A. et al. "Brittlebench: Quantifying LLM robustness via prompt sensitivity." arXiv:2603.13285, Feb 2026. https://arxiv.org/pdf/2603.13285
3. Dogan, M. et al. "FewMMBench: A Benchmark for Multimodal Few-Shot Learning." arXiv:2602.21854, Feb 2026. https://arxiv.org/abs/2602.21854
4. Habba, E. et al. "DOVE: A Large-Scale Multi-Dimensional Predictions Dataset Towards Meaningful LLM Evaluation." ACL Findings 2025. https://aclanthology.org/2025.findings-acl.611/
5. Khoshdel et al. "Fine-tuning for Better Few Shot Prompting." arXiv:2508.04063, Aug 2025. https://arxiv.org/pdf/2508.04063
6. StructEval. "Benchmarking LLMs' Capabilities to Generate Structural Outputs." arXiv:2505.20139, 2025. https://arxiv.org/html/2505.20139
7. Hannecke, M. "Beyond JSON: Picking the Right Format for LLM Pipelines." Medium, Dec 2025. https://medium.com/@michael.hannecke/beyond-json-picking-the-right-format-for-llm-pipelines-b65f15f77f7d
8. Wei, J. et al. "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models." arXiv:2201.11903, 2022 (NeurIPS). https://arxiv.org/pdf/2201.11903v4
9. Hi-CoT team. "Hi-CoT: Hierarchical Chain-of-Thought Prompting." arXiv:2604.00130, Apr 2026. https://www.arxiv.org/pdf/2604.00130
10. Lunardi, R. et al. "On Robustness and Reliability of Benchmark-Based Evaluation of LLMs." arXiv:2509.04013, Sep 2025. https://arxiv.org/html/2509.04013v1
11. Jiang, D. et al. "MME-CoT: Benchmarking Chain-of-Thought in Large Multimodal Models." ICML 2025. https://icml.cc/virtual/2025/poster/44904
12. Jaroslawicz, D. et al. "IFScale: How Many Instructions Can LLMs Follow at Once?" arXiv:2507.11538, Jul 2025. https://arxiv.org/pdf/2507.11538
13. Wu, X. et al. "LIFBench: Evaluating the Instruction Following Performance and Stability of LLMs in Long-Context Scenarios." arXiv:2411.07037, Nov 2024 / v3 Jul 2025. https://arxiv.org/abs/2411.07037
14. Robinette, P.K. et al. "We Are What We Repeatedly Do: Improving Long Context Instruction Following." EACL Findings 2026. https://aclanthology.org/2026.findings-eacl.254/
15. Anon. "A Closer Look at System Prompt Robustness." arXiv:2502.12197, Feb 2025. https://arxiv.org/pdf/2502.12197
16. Feroz, F. "Prompt Engineering is Dead. Intent Engineering is the Real Game." Medium, Feb 2026. https://office.qz.com/prompt-engineering-is-dead-intent-engineering-is-the-real-game-89ed83cdf3a4
17. Khan, I. "You Don't Need Prompt Engineering Anymore: The Prompting Inversion." arXiv:2510.22251, Oct 2025. https://arxiv.org/abs/2510.22251
18. Schulhoff, S. et al. "The Prompt Report: A Systematic Survey of Prompt Engineering Techniques." arXiv:2406.06608 (v6 Feb 2025). https://arxiv.org/abs/2406.06608
19. Sahoo, P. et al. "A Systematic Survey of Prompt Engineering in Large Language Models: Techniques and Applications." arXiv:2402.07927 (v2 Mar 2025). https://arxiv.org/abs/2402.07927
20. Yin, M. et al. "CoT-Valve: Length-Compressible Chain-of-Thought Tuning." ACL 2025. https://aclanthology.org/2025.acl-long.300.pdf
21. Yu, W. et al. "Benchmarking Multi-Step Legal Reasoning and Analyzing Chain-of-Thought Effects in LLMs." arXiv:2511.07979, Nov 2025. https://arxiv.org/abs/2511.07979
22. RELIABLEEVAL team. "RELIABLEEVAL: A Recipe for Stochastic LLM Evaluation." EMNLP Findings 2025. https://aclanthology.org/2025.findings-emnlp.594.pdf
