/**
 * Shared section ID constants for BB detail pages.
 * Used by both BBTableOfContents and the individual section components.
 */
export const BB_SECTIONS = {
  WAT_IS_HET: { id: 'wat-is-het', label: 'Wat is het?' },
  CHECKLIST: { id: 'checklist', label: 'Checklist' },
  QUICK_START: { id: 'quick-start', label: 'Quick Start' },
  VOORBEELD: { id: 'voorbeeld', label: 'Voorbeeld' },
  RESEARCH: { id: 'research', label: 'Research' },
  GUARDRAILS: { id: 'guardrails', label: 'Guardrails' },
  CONTACT: { id: 'contact', label: 'Aan de slag' },
} as const;

export const BB_SECTION_LIST = Object.values(BB_SECTIONS);
