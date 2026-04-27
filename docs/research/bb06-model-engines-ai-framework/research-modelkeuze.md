# Research: Modeltype-keuze als ontwerpvraag — BB_06 Model Engines

**Researcher:** researcher-A
**Dimensie:** Modeltype-keuze heuristieken, LLM vs klassiek ML, besliskaders
**Datum:** 2026-04-27

## Samenvatting (1 zin)

Het grootste anti-patroon in enterprise AI is het inzetten van frontier-LLMs voor taken waarbij klassiek ML, regels of kleinere specialistische modellen goedkoper, sneller en beter verklaarbaar zijn.

## Bevindingen

### De vier beslisfactoren

Vier factoren domineren iedere modelkeuze [1, 2]:
1. **Taakcomplexiteit** — open-ended of gesloten/gedetermineerd?
2. **Kosten** — wat is de tolerabele prijs per aanroep?
3. **Latency** — realtime (<200 ms) of asynchroon (seconden/minuten)?
4. **Privacy / data-residentie** — wat mag de data verlaten?

Alle bronnen zijn het erover eens: benchmarks (MMLU, HumanEval) correleren zwak met real-world bedrijfsprestaties. Het enige zinvolle kwaliteitstest is een private evaluatie op 50–200 eigen representatieve voorbeelden [1, 3]. `verified`

### LLM vs klassiek ML vs regels — beslismatrix

| Dimensie | Regels | Klassiek ML | LLM |
|----------|--------|-------------|-----|
| Kosten per aanvraag | Nagenoeg nul | $0,001–$0,01 | $0,01–$0,50+ |
| Setup-tijd | Dagen–weken | Weken–maanden | Uren–dagen |
| Nauwkeurigheid op afgebakende taken | Perfect (als regels kloppen) | Hoog (met data) | Goed–hoog |
| Omgaan met ambiguïteit | Nee | Beperkt | Ja |
| Verklaarbaar/auditeerbaar | Uitstekend | Laag–gemiddeld | Zeer moeilijk |
| Latency | Sub-milliseconde | 10–100 ms | 200 ms–5 s |
| Databehoefte | Geen (domeinkennis) | 1.000–100.000+ gelabelde voorbeelden | Nul tot weinig |

Bron: [4] `verified`

### Wanneer klassiek ML superieur is

Klassieke modellen (XGBoost, LightGBM, BERT-classifiers) zijn superieur bij [3, 4, 5]:
- **Tabellaire gestructureerde data** — churn-voorspelling, fraude, voorraadbeheer, kredietscores
- **Tijdreeksen** — productieforecast, energieverbruik, sensordata
- **Hoge-volume classificatie** — content-moderatie, transactie-labeling
- **Gereguleerde omgevingen** — financieel, zorg: klassieke modellen zijn statistisch valideerbaar en auditeerbaar

XGBoost/LightGBM blijven in 2026 dominant voor tabellaire productietaken. Vervanging door LLM is in de meeste gevallen duurder, trager en minder verklaarbaar [4, 5]. `verified`

### Wanneer LLM het juiste gereedschap is

LLMs winnen wanneer [1, 4]:
- De taak open-ended is (vrije tekst, vertaling, redenering)
- Er onvoldoende gelabelde trainingsdata is voor een klassiek model
- De input sterk varieert (edge cases, lange staarten)
- Snelle time-to-market vereist is (uren vs weken fine-tuning)

### Diagnostische vragen: "Is dit een LLM-probleem?"

Gebruik deze vragen als filter [4, 5]:
1. Is de uitvoer een gestructureerd getal of label? → overweeg klassiek ML of regels
2. Heb ik 1.000+ gelabelde voorbeelden? → klassiek ML is kandidaat
3. Moet het resultaat statistisch verklaarbaar zijn voor een auditor? → klassiek ML of regels
4. Is latency <100 ms een harde grens? → klassiek ML of gespecialiseerd model
5. Gaat het om tabellaire, historische data? → XGBoost/LightGBM eerst proberen

### SLM (Small Language Models) als tussencategorie

SLMs (<10 miljard parameters) presteren bij gefocuste taken soms beter dan grote LLMs, werken sneller en goedkoper, en passen op edge-hardware [6]. Ze zijn het juiste gereedschap voor goed gedefinieerde, herhalende taken (classificatie, vertaling in een eng domein, samenvatting van vaste typen documenten). `inferred` uit meerdere bronnen

### Aanbevolen workflow (validatie door meerdere bronnen)

1. Begin met prompt engineering op een generalistisch model
2. Voeg RAG toe als kenniscontext ontbreekt
3. Gebruik fine-tuning alleen als laatste stap — vereist ≥1.000 kwaliteitsvoorbeelden en een meetbaar evaluatie-criterium
4. Fine-tuning zonder evaluatiepijplijn is "schieten in het donker" [3]

## Evidence Table

| # | Bron | URL | Type | Key claim | Confidence |
|---|------|-----|------|-----------|------------|
| 1 | LLM Gateway — Choosing Right LLM 2026 | https://llmgateway.io/blog/how-to-choose-the-right-llm | secondary | 4 beslisfactoren: taak, kosten, latency, context | high |
| 2 | NovaKit — Decision Framework 2026 | https://www.novakit.ai/blog/choosing-right-ai-model | secondary | Task-first selectie; één model voor alles is budget-lek | high |
| 3 | core.cz — Enterprise AI Model Selection | https://core.cz/en/blog/2026/ai-model-selection-enterprise-2026/ | secondary | Evaluatiepijplijn >200 voorbeelden; fine-tuning als laatste stap | high |
| 4 | IdeaPlan — LLM vs Traditional ML vs Rules | https://www.ideaplan.io/compare/llm-vs-traditional-ml-vs-rules | secondary | Vergelijkingstabel met kosten, latency, data | high |
| 5 | phptrends — Practical AI Decision Guide | https://phptrends.com/choosing-the-right-approach-to-artificial-intelligence-a-practical-decision-guide/ | secondary | Klassiek ML voor gestructureerde voorspellingen; beter auditeerbaar | high |
| 6 | Longbridge — LLM vs SLM vs FM | https://longbridge.com/en/news/273584759 | secondary | SLM als specialist-laag; FM voor autonome multi-step taken | medium |

## Coverage Status

- **Gecheckt direct:** alle 6 bronnen gelezen via Exa search met uitgebreide highlights
- **Blijft onzeker:** harde empirische vergelijking XGBoost vs LLM op dezelfde enterprise dataset (niet gevonden in 2026-bronnen)
- **Niet afgerond:** geen primaire benchmarkpaper voor SLM vs LLM op NL-talige enterprise-taken

## Sources

1. LLM Gateway — How to Choose the Right LLM for Your Use Case in 2026 — https://llmgateway.io/blog/how-to-choose-the-right-llm
2. NovaKit — Choosing the Right AI Model: A Decision Framework for 2026 — https://www.novakit.ai/blog/choosing-right-ai-model
3. core.cz — How to Choose the Right AI Model for Enterprise Deployment in 2026 — https://core.cz/en/blog/2026/ai-model-selection-enterprise-2026/
4. IdeaPlan — LLM vs Traditional ML vs Rules: When to Use Each — https://www.ideaplan.io/compare/llm-vs-traditional-ml-vs-rules
5. phptrends — Choosing the Right Approach to AI: A Practical Decision Guide — https://phptrends.com/choosing-the-right-approach-to-artificial-intelligence-a-practical-decision-guide/
6. Longbridge — LLM vs. SLM vs. FM: Choosing the Right AI Model — https://longbridge.com/en/news/273584759
