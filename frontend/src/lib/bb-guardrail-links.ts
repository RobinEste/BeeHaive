/**
 * Static mapping of Building Blocks to their most relevant Guardrails.
 * Interim solution until the Neo4j knowledge graph API provides dynamic links (Fase B).
 */

export type GuardrailCode = 'GR_01' | 'GR_02' | 'GR_03' | 'GR_04' | 'GR_05' | 'GR_06' | 'GR_07';

export interface GuardrailLink {
  code: GuardrailCode;
  name: string;
  slug: string;
  tagline: string;
  /** Why this guardrail is relevant to this building block */
  relevance: string;
}

const guardrails: Record<GuardrailCode, Omit<GuardrailLink, 'relevance'>> = {
  GR_01: { code: 'GR_01', name: 'Human Agency', slug: 'human-agency', tagline: 'De mens houdt controle — AI ondersteunt, maar beslist niet.' },
  GR_02: { code: 'GR_02', name: 'Robustness', slug: 'robustness', tagline: 'Betrouwbaar gedrag onder alle omstandigheden.' },
  GR_03: { code: 'GR_03', name: 'Privacy', slug: 'privacy', tagline: 'Data bescherming als fundament, niet als bijzaak.' },
  GR_04: { code: 'GR_04', name: 'Fairness', slug: 'fairness', tagline: 'Gelijke behandeling, geen systematische benadeling.' },
  GR_05: { code: 'GR_05', name: 'Transparency', slug: 'transparency', tagline: 'Helder hoe AI werkt, wat het doet, en waarom.' },
  GR_06: { code: 'GR_06', name: 'Well-being', slug: 'well-being', tagline: 'AI die bijdraagt aan maatschappelijk welzijn.' },
  GR_07: { code: 'GR_07', name: 'Accountability', slug: 'accountability', tagline: 'Duidelijk wie verantwoordelijk is — en hoe daarop wordt toegezien.' },
};

function link(code: GuardrailCode, relevance: string): GuardrailLink {
  return { ...guardrails[code], relevance };
}

export const bbGuardrailLinks: Record<string, GuardrailLink[]> = {
  knowledge: [
    link('GR_01', 'Kennis is de basis voor menselijk toezicht — zonder begrip geen controle.'),
    link('GR_05', 'Wie de materie begrijpt, kan uitleggen hoe en waarom AI wordt ingezet.'),
    link('GR_07', 'Verantwoording vereist dat de juiste mensen de juiste kennis hebben.'),
  ],
  'client-blueprint': [
    link('GR_01', 'Een goed ontwerp borgt dat mensen de regie houden over het AI-systeem.'),
    link('GR_05', 'De blueprint documenteert hoe het systeem werkt — transparantie by design.'),
    link('GR_07', 'Rollen, verantwoordelijkheden en escalatiepaden worden in de blueprint vastgelegd.'),
  ],
  'dynamic-context': [
    link('GR_03', 'PII in RAG lekt stilzwijgend: pre-indexering redactie, DP-RAG en data-lineage zijn privacy-architectuurvereisten, niet optionele filters.'),
    link('GR_02', 'Context rot en stale context zijn stille faalmodi — alle frontier-modellen degraderen bij groeiende context, en verouderde kennisbanken geven geen error maar een plausibel fout antwoord.'),
    link('GR_05', 'Document-provenance, embedding-timestamp en confidence-fallback in de retrieval-laag zijn voorwaarden voor betekenisvolle bronverwijzingen bij AI-antwoorden.'),
    link('GR_07', 'Elk bron-document heeft een `owner` voor recertificatie bij staleness; retrieval-audit trails maken incident-analyse mogelijk en tonen AVG-doelbinding aan.'),
  ],
  'prompt-design': [
    link('GR_05', 'Een prompt bepaalt wat het model doet en hoe. In productie moet die instructie navolgbaar en uitlegbaar zijn, zodat gebruikers de output kunnen interpreteren.'),
    link('GR_01', 'De prompt bepaalt of gebruikers de output kunnen corrigeren, het systeem kunnen stoppen of kunnen escaleren naar een mens. Zonder expliciete stopcondities en escalatie-paden is menselijke controle een illusie.'),
    link('GR_07', 'Een production prompt is geen losse tekststring in de code — het is een document waarvoor iemand verantwoordelijk is. Versioning, review-trails en expliciet eigenaarschap zijn voorwaarden voor verantwoording.'),
  ],
  'tool-integration': [
    link('GR_02', 'Externe koppelingen zijn kwetsbaar — robuuste error handling is cruciaal.'),
    link('GR_03', 'Data die via tools stroomt moet beschermd worden in transit en opslag.'),
    link('GR_07', 'Elke tool-actie moet traceerbaar zijn voor auditdoeleinden.'),
  ],
  'model-engines': [
    link('GR_02', 'Modelkeuze bepaalt betrouwbaarheid — test op edge cases en hallucinations.'),
    link('GR_04', 'Modellen bevatten inherente biases — evalueer en mitigeer systematisch.'),
    link('GR_05', 'Documenteer welk model wordt gebruikt, waarom, en wat de beperkingen zijn.'),
  ],
  'evaluation-loop': [
    link('GR_07', 'Meten is verantwoorden — evaluatie maakt prestaties toetsbaar.'),
    link('GR_04', 'Continue evaluatie detecteert bias die bij lancering niet zichtbaar was.'),
    link('GR_06', 'Meet niet alleen technische metrics maar ook maatschappelijke impact.'),
  ],
};
