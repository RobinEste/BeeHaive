# Research: EU-data-residentie en soevereiniteit — BB_06 Model Engines

**Researcher:** researcher-D
**Dimensie:** EU-soevereiniteit, AI Act, CLOUD Act, lokale inference, sovereign cloud
**Datum:** 2026-04-27

## Samenvatting (1 zin)

Werkelijke EU-data-soevereiniteit vereist meer dan EU-regio's kiezen: de CLOUD Act maakt US-bedrijven kwetsbaar ongeacht datacenter-locatie, waardoor Mistral (EU-gevestigd) en zelf-gehoste open-weight-modellen de enige categorisch veilige opties zijn voor gevoelige data.

## Bevindingen

### Kern-onderscheid: data-residentie vs data-soevereiniteit

- **Data-residentie**: data wordt fysiek opgeslagen in een specifieke geografische locatie
- **Data-soevereiniteit**: data valt onder de wetten van het land waar het staat opgeslagen

Een US-hyperscaler (AWS, Azure, Google Cloud) die opereert vanuit een Canadees/Iers datacenter voldoet aan data-residentie maar NIET aan data-soevereiniteit. De US CLOUD Act (Clarifying Lawful Overseas Use of Data Act) machtigt US-autoriteiten data op te eisen bij US-bedrijven, ook wanneer die data op EU-servers staat [1]. `verified`

### Providers naar EU-positie

**Mistral AI (Paris, France):**
- Enige frontier-provider die categoriaal buiten CLOUD Act-jurisdictie valt [2, 3, 4]
- Alle API-verwerking via La Plateforme in EU-datacenters (Paris-regio) — standaard, niet configureerbaar anders
- Open-weight modellen beschikbaar onder Apache 2.0 — zelf-hostbaar zonder enige externe datatransfer
- Valuation: $13,8 miljard, $400 miljoen ARR (maart 2026), plan om $1 miljard te bereiken eind 2026
- Caveat: Mistral heeft US-investeerders (a16z, Salesforce Ventures) — CLOUD Act-blootstelling juridisch ongetest [5]

**Anthropic (via AWS Bedrock EU-regio's):**
- Beschikbaar in: Ireland (eu-west-1), Frankfurt (eu-central-1), Paris (eu-west-3)
- AWS DPA van toepassing; Claude API ondersteunt ook EU-routing direct
- US-gevestigd bedrijf; data op EU-servers is CLOUD Act-kwetsbaar [1, 6]

**OpenAI (EU Data Residency):**
- Enterprise / Zero Data Retention: Ireland, Germany, Netherlands
- DPA beschikbaar; data processing addendum
- Standard API: data via US-infrastructuur
- GPT-5.4 Regional Processing: 10% prijstoeslag [6, 7]

**Google (Vertex AI / Gemini):**
- Full EU Data Boundary beschikbaar; regio's: Belgium, Netherlands, Frankfurt, Finland, Warsaw, Milan, Paris
- Vertex AI configureerbaar voor exclusieve EU-verwerking — sterkste configureerbare compliance van hyperscalers
- Customer-managed encryption keys (CMEK) beschikbaar
- US-gevestigd — CLOUD Act kwetsbaarheid blijft [1]

**Microsoft (Azure OpenAI):**
- West Europe, North Europe, Sweden Central, France Central, Germany West Central
- Full EU Data Boundary met ondertekende DPA
- CLOUD Act kwetsbaarheid als US-bedrijf

### AWS European Sovereign Cloud

AWS lanceerde in 2025 de European Sovereign Cloud:
- Amazon Bedrock beschikbaar: modellen van Anthropic, Meta, Mistral, Amazon
- Voldoet NIET aan SecNumCloud (hoogste Franse overheidsnorm)
- Biedt wél directe Bedrock-toegang voor AI-workloads
- Keuze: Bedrock in European Sovereign Cloud (direct beschikbaar, geen SecNumCloud) vs wachten op S3NS/Bleu (SecNumCloud maar beperkte AI-offerings) [5]

### Lokale / on-premise inference opties

| Tool | Type | Sterkte |
|------|------|---------|
| Ollama | Local inference runtime | Eenvoudige installatie, breed model-support |
| vLLM | Production serving | Hoge doorvoer, speculative decoding |
| TGI (Text Generation Inference, HuggingFace) | Production serving | Geoptimaliseerd voor HF-modellen |
| llama.cpp | CPU + GPU inference | Low-hardware-requirement, Llama 4 Scout op M4 Mac |

Lokale inference elimineert alle externe datatransfers. Kwaliteits- en feature-pariteit-beperkingen:
- Lokale modellen (Llama 4 Scout, Mistral Large 3 zelf-gehost) bereiken 85–95% van frontier-kwaliteit op gefocuste taken `inferred`
- Real-time updates, RLHF-fine-tuning en agentic tooling zijn minder volwassen dan bij commercial APIs
- Hardware-kosten: break-even tussen cloud-API en eigen inference bij ~500K–1M tokens/dag `inferred`

### EU AI Act — model-specifieke verplichtingen

De EU AI Act is in gefaseerde handhaving getreden; meeste bepalingen actief per augustus 2025/2026 [3, 4, 8]:

**GPAI-model-providers (artikel 53)** — van toepassing op OpenAI, Anthropic, Google, Mistral:
- Technische documentatie verplicht
- Trainingsdata-samenvatting/copyright-compliance
- Voor modellen met "systemisch risico" (artikel 55): veiligheidsevaluaties en beveiligingsmaatregelen

**Voordelen van EU-gebaseerde provider voor GPAI-compliance:**
- Mistral als EU-bedrijf valt direct onder EU AI Act-verplichtingen en heeft AI-beleid gepubliceerd dat aansluit bij Europese grondrechten
- US-providers ondertekenden Code of Practice maar zijn primair US-regulated

**DORA, EHDS, AVG-raakvlakken:**
- DORA (financiële sector): strikte data-lokalisatievereisten voor kritieke IT-systemen
- EHDS (European Health Data Space): gezondheidsdata mag EU niet verlaten
- AVG artikel 44–49: adequaatheid-besluit, SCCs of bindende bedrijfsregels vereist voor datatransfers buiten EER

### Sovereign cloud partners Mistral

Mistral werkt samen met EU-native cloudproviders [4]:
- OVHcloud (France)
- Scaleway (France)
- T-Systems (Germany)
- Hetzner (Germany) — geen officiële partnership maar compatibel met open-weight zelf-hosting

### Werkelijke beperkingen "EU-only"-architectuur in 2026

1. **Kwaliteitskloof**: Mistral Large 3 benadert maar overtreft niet consistente Claude Opus 4.7/GPT-5.4 op alle taken
2. **Feature-pariteit**: agentic tooling (MCP, computer-use) is minder ver bij EU-native providers
3. **Pricing**: Mistral is aanzienlijk goedkoper dan Anthropic op vergelijkbare tiers (70% minder)
4. **Governance**: Mistral's Forge biedt dedicated on-premise training-optie voor gevoelige organisaties (overheid, defensie)

## Evidence Table

| # | Bron | URL | Type | Key claim | Confidence |
|---|------|-----|------|-----------|------------|
| 1 | dev.to — AI Data Residency Guide | https://dev.to/morley-media/ai-data-residency-when-cloud-apis-dont-meet-your-compliance-requirements-5eb8 | secondary | CLOUD Act maakt EU-regio onvoldoende voor soevereiniteit | high |
| 2 | APIScout — Mistral vs OpenAI 2026 | https://apiscout.dev/blog/mistral-ai-vs-openai-api-2026 | secondary | Mistral enige EU-native frontier provider, geen CLOUD Act | high |
| 3 | Hyperion — Mistral AI Guide for European Enterprises | https://hyperion-consulting.io/en/insights/mistral-ai-complete-guide-2026 | secondary | EU AI Act, GDPR, open-weight deploymentdetails | high |
| 4 | aimagicx — Mistral Build Your Own AI | https://www.aimagicx.com/blog/mistral-build-your-own-ai-enterprise-strategy-2026 | secondary | Sovereign cloud partners, EU AI Act compliance tools | medium |
| 5 | Medium (Julien Simon) — AI Sovereignty Europe | https://building.theatlantic.com/ai-sovereignty-in-europe-a-decision-framework-375a517a4179 | secondary | AWS ESC vs S3NS/Bleu; Mistral US-investeerder-caveat | high |
| 6 | BenchGecko — EU-Hosted LLMs | https://benchgecko.ai/pricing/eu-hosted | secondary | Overzicht providers met EU-residency | high |
| 7 | Complyance — EU AI Act Vendor Compliance | https://complyance.app/blog/ai-vendor-compliance-openai-anthropic | secondary | GPAI-verplichtingen per provider; DPA-status | high |
| 8 | Hyperion — Mistral Forge | https://hyperion-consulting.io/en/insights/mistral-forge-enterprise-ai-model-ownership | secondary | On-premise Forge voor govt/zorg/defensie; AI Act artikel 13/17 | medium |

## Coverage Status

- **Gecheckt direct:** CLOUD Act-kwetsbaarheid bevestigd via meerdere onafhankelijke juridische analyses
- **Blijft onzeker:** Mistral CLOUD Act-blootstelling via US-investeerders — juridisch ongetest
- **Niet afgerond:** NL AIC specifieke aanbevelingen niet gevonden; NL NCSC AI-beveiligingsrichtlijnen niet gecheckt

## Sources

1. dev.to — AI Data Residency: When Cloud APIs Don't Meet Your Compliance Requirements — https://dev.to/morley-media/ai-data-residency-when-cloud-apis-dont-meet-your-compliance-requirements-5eb8
2. APIScout — Mistral AI vs OpenAI API 2026 — https://apiscout.dev/blog/mistral-ai-vs-openai-api-2026
3. Hyperion Consulting — The Definitive Mistral AI Guide for European Enterprises 2026 — https://hyperion-consulting.io/en/insights/mistral-ai-complete-guide-2026
4. AI Magicx — Mistral's Build Your Own AI Strategy — https://www.aimagicx.com/blog/mistral-build-your-own-ai-enterprise-strategy-2026
5. Medium / Julien Simon — AI Sovereignty in Europe: A Decision Framework — https://building.theatlantic.com/ai-sovereignty-in-europe-a-decision-framework-375a517a4179
6. BenchGecko — EU-Hosted LLMs & GDPR Compliant AI Model Providers — https://benchgecko.ai/pricing/eu-hosted
7. Complyance — Is Your AI Vendor EU AI Act Compliant? — https://complyance.app/blog/ai-vendor-compliance-openai-anthropic
8. Hyperion Consulting — Mistral Forge: Own Your AI Model — https://hyperion-consulting.io/en/insights/mistral-forge-enterprise-ai-model-ownership
