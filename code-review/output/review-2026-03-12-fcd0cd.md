# Code Review — 2026-03-12

## Samenvatting

| Aspect | Waarde |
|--------|--------|
| **Verdict** | approve |
| **Risk Score** | 10/100 (Minimaal) |
| **Bestanden** | 6 gereviewed |
| **Bevindingen** | 2 (gefilterd van 6) |
| **Agents** | python-specialist, security-sentinel, logic-correctness, convention-checker, avg-privacy-guardian |

## Bevindingen

### PYT-001 — PII-redactie fout wordt stil genegeerd (MEDIUM)

**Bestand:** `backend/app/ingestion/pipeline.py:57-63`
**Agent:** python-specialist

De fetcher slaat PII-redactie over als `pii_report.error` truthy is: de ongeredacteerde tekst wordt dan gecached en doorgegeven aan `classify_text`. De pipeline heeft hier geen zicht op. Als de PII-scanner faalt bij een document met e-mailadressen, gaan die naar de Gemini API. De `pii_scan_failed` status bestaat al in het model maar wordt nooit gebruikt.

**Suggestie:** Voeg een `pii_scan_ok` veld toe aan `FetchResult` en laat de pipeline terugkeren met `status='pii_scan_failed'` als de scan is misgelopen.

---

### LOG-001 — Unhandled exceptions in CLI geven raw traceback (MEDIUM)

**Bestand:** `backend/scripts/ingest_item.py:45-47`
**Agent:** logic-correctness

Het `with get_session()` blok heeft geen try/except. Bij Neo4j-verbindingsfouten of een ontbrekende `GEMINI_API_KEY` krijgt de gebruiker een raw Python traceback. De `ValueError('GEMINI_API_KEY not set...')` uit `_get_client()` propageert onafgevangen naar `main()`.

**Suggestie:** try/except rond `get_session` + `ingest` call.

## Gefilterde bevindingen (niet getoond)

- PYT-002 (low): type hint suggestie — uitgesloten als style-only
- CON-001 (low): CHANGELOG entry mist — uitgesloten als documentatie
- LOG-002 (low): theoretische `fallback` status edge case — score te laag
- AVG-001 (medium): Art. 17 wis-mechanisme voor auteurs — aparte feature, niet deze PR
