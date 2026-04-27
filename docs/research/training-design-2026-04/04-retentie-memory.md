# 04 — Retentie: kennis naar lange-termijn geheugen

> Onderdeel van het training-design onderzoek (april 2026). Zie [`INDEX.md`](INDEX.md).

## Spaced repetition (Ebbinghaus, Cepeda, Anki/Leitner)

**Kernbevinding.** De meta-analyse van Cepeda et al. (839 assessments over 317 experimenten) toont onomstotelijk aan dat gespreide (spaced) studie beter werkt dan gemasseerd (massed). De vuistregel uit Cepeda et al. (2008): het optimale interval tussen herhalingen bedraagt ongeveer **10–20% van de gewenste retentietermijn**. Wil je een concept 6 maanden laten zitten, herhaal het dan na ~3–4 weken. Wil je het 1 jaar laten zitten, dan is een interval van ~5–10% (~3–5 weken) optimaal.

Het Leitner-systeem (1970) en Anki's SM-2 algoritme zijn praktische implementaties: kaarten die correct worden beantwoord verhuizen naar langere intervallen (1d → 3d → 7d → 16d → 35d …); foute kaarten vallen terug naar interval 1. Anki-gebruikers scoren 5–10 punten hoger op examens zoals USMLE Step 1 (correlationeel, niet strikt causaal). Claims dat spaced repetition retentie "met 200%" verhoogt zijn marketing-achtig; de peer-reviewed literatuur spreekt van medium-tot-grote effect sizes.

**Toepassing voor BeeHaive.**

- Bouw per bouwsteen en per guardrail een micro-deck van 8–15 flashcards (definitie, voorbeeld, tegenvoorbeeld, toepassingsvraag).
- Implementeer een Leitner-achtige flow in de cursusbot: dag 1, 3, 7, 16, 35, 90 voor de kern-concepten. De AI-bot kan kaarten semi-automatisch genereren uit cursusnotities met RAG-grounding.
- Communiceer expliciet naar cursisten dat "even elke dag 5 minuten" effectiever is dan een uur per week.

**Evidence-sterkte.** Zeer sterk (meta-analytisch, decennia onderzoek).

## Retrieval practice / testing effect (Roediger & Karpicke)

**Kernbevinding.** Roediger & Karpicke (2006, 2008) lieten zien dat actief terughalen dramatisch beter is dan herlezen. Rowland (2014) vond een medium-to-large effect (g = 0.50) in meta-analyse. Belangrijk: zónder feedback werkt het testing effect alleen als praktijktest-accuracy **>50%** is — anders versterk je fouten. "Testing is leren, niet meten" is de kernboodschap.

**Toepassing voor BeeHaive.**

- Elke module eindigt niet met "samenvatting" maar met 3–5 vrije-ophaalvragen ("Beschrijf in eigen woorden waarom guardrail X de risico's van bouwsteen Y afdekt").
- De cursusbot stelt spontane terugblikvragen: "Je hebt 2 dagen geleden bouwsteen 3 gedaan — kun je zonder terug te kijken de drie kernvragen formuleren die een governance-owner moet stellen?"
- Lage-stakes quizzes wekelijks (geen cijfer), met directe feedback.

**Evidence-sterkte.** Zeer sterk.

## Interleaving vs. blocked practice (Rohrer)

**Kernbevinding.** Rohrer & Taylor (2010): leerlingen die rekenproblemen door elkaar (interleaved) oefenden scoorden na 1 dag 77% vs. 38% voor blocked practice. Het mechanisme: discriminatief contrast — je moet wáárnemen welk concept van toepassing is. **Nuance uit 2025-onderzoek** (MDPI *Behavioral Sciences*): als het doel is een *regel* te leren, is blocked soms beter; voor *herkenning van categorieën op basis van similariteit* is interleaving beter.

**Toepassing voor BeeHaive.**

- Na blok-introductie van bouwstenen 1–7 (blocked), volgt een interleaved oefenblok waarin casussen door elkaar komen: "Welke bouwsteen is hier het meest relevant? Welke guardrail?"
- In de bot: praktijkcasussen uit verschillende sectoren (zorg, overheid, retail) die door elkaar worden aangeboden, niet per sector gegroepeerd.

**Evidence-sterkte.** Sterk voor categorie-discriminatie; gemengd voor regelgebaseerde taken.

## Elaboration

**Kernbevinding.** Dunlosky et al. (2013) gaf elaboratieve interrogatie en self-explanation een *moderate* utility rating — positief, maar minder robuust dan spacing en retrieval. Elaboratie werkt het best wanneer cursisten nieuwe informatie koppelen aan **eigen werkcontext**.

**Toepassing voor BeeHaive.**

- Elke module bevat de vraag: "Geef een voorbeeld uit je eigen organisatie waar deze bouwsteen/guardrail wel/niet wordt toegepast." De AI-bot kan meedenken en doorvragen.
- "Waarom"-vragen na elk concept: niet "wat is bouwsteen 4" maar "waarom is bouwsteen 4 nodig in een organisatie zonder model governance?"

**Evidence-sterkte.** Matig-sterk.

## Dual coding (kort)

**Kernbevinding.** Combinatie van verbale en visuele representaties verbetert retentie (Paivio, later Mayer's multimedia principles). Dunlosky's review: veelbelovend maar afhankelijk van kwaliteit van visuals. Volledig uitgewerkt in deelbestand 02.

**Toepassing voor BeeHaive.**

- Eén consistente infographic per bouwsteen/guardrail (visueel ankerpunt).
- Framework-diagram waarin alle 7+7 in relatie staan — cursisten zien dit steeds terug.

**Evidence-sterkte.** Matig-sterk.

## Vertaling naar 4–8 weken training + follow-up

**Concrete blueprint voor BeeHaive:**

- **Week 1–4:** één bouwsteen per week (live + self-paced). Elke week: video, lezing, 3 flashcards per concept, 1 live Q&A.
- **Week 5–8:** guardrails geïntroduceerd, interleaved met de bouwstenen.
- **Review-cyclus in de bot:** dag 1 (direct), dag 3, dag 7, dag 21, dag 60, dag 120 per concept.
- **Capstone:** cursisten schrijven een mini-governance-plan voor hun eigen organisatie (elaboration + transfer).

## Bronnen

**Spaced repetition & forgetting curve**

- [Cepeda et al. (2008) Spacing effects in learning — PubMed](https://pubmed.ncbi.nlm.nih.gov/19076480/)
- [Cepeda et al. (2006) Distributed practice meta-analysis — PDF](https://augmentingcognition.com/assets/Cepeda2006.pdf)
- [Using Spacing to Enhance Diverse Forms of Learning (ERIC)](https://files.eric.ed.gov/fulltext/ED536925.pdf)
- [Spaced Repetition — Wikipedia](https://en.wikipedia.org/wiki/Spaced_repetition)
- [Anki SRS Algorithm (Sobczak)](https://juliensobczak.com/inspect/2022/05/30/anki-srs/)
- [Leitner System Guide — e-student](https://e-student.org/leitner-system/)

**Retrieval practice / testing effect**

- [Roediger & Karpicke (2006) The Power of Testing Memory](http://psychnet.wustl.edu/memory/wp-content/uploads/2018/04/Roediger-Karpicke-2006_PPS.pdf)
- [Karpicke & Roediger (2008) Repeated retrieval — PDF](https://learninglab.psych.purdue.edu/downloads/2007/2007_Karpicke_Roediger_JML.pdf)
- [Retrieval-Based Learning: A Decade of Progress (ERIC)](https://files.eric.ed.gov/fulltext/ED599273.pdf)
- [Mike Taylor (2025) The Testing Effect](https://mike-taylor.org/2025/12/01/the-testing-effect-why-retrieval-practice-is-your-most-powerful-learning-tool/)
- [Cross-disciplinary replication — PMC (2024)](https://pmc.ncbi.nlm.nih.gov/articles/PMC12302331/)

**Interleaving**

- [Whether Interleaving or Blocking Is More Effective (MDPI 2025)](https://www.mdpi.com/2076-328X/15/5/662)
- [Rohrer — Interleaved Practice Improves Mathematics Learning (ERIC)](https://files.eric.ed.gov/fulltext/ED557355.pdf)
- [Firth (2021) Systematic review of interleaving — Wiley](https://bera-journals.onlinelibrary.wiley.com/doi/10.1002/rev3.3266)

**Elaboration / Dunlosky**

- [Dunlosky et al. (2013) Improving Students' Learning — PDF](https://www.whz.de/fileadmin/lehre/hochschuldidaktik/docs/dunloskiimprovingstudentlearning.pdf)
- [A Meta-Analysis of Ten Learning Techniques — Frontiers](https://www.frontiersin.org/journals/education/articles/10.3389/feduc.2021.581216/full)
