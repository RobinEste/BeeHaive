/**
 * Shared icon definitions for Building Blocks.
 * Used by both BuildingBlocksGrid and BB detail pages.
 */

export interface BBIcon {
  type: 'png' | 'svg';
  /** For png: the image path. For svg: the inner SVG markup. */
  src: string;
}

export const bbIcons: Record<string, BBIcon> = {
  knowledge: {
    type: 'png',
    src: '/icons/bb-knowledge.png',
  },
  'client-blueprint': {
    type: 'svg',
    src: '<rect x="4" y="2" width="12" height="16" rx="1.5" stroke="currentColor" stroke-width="1.4" fill="none"/><line x1="7" y1="6" x2="13" y2="6" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><line x1="7" y1="9" x2="13" y2="9" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/><line x1="7" y1="12" x2="11" y2="12" stroke="currentColor" stroke-width="1.1" stroke-linecap="round"/>',
  },
  'dynamic-context': {
    type: 'svg',
    src: '<circle cx="8.5" cy="8.5" r="5" stroke="currentColor" stroke-width="1.5" fill="none"/><line x1="12" y1="12" x2="17" y2="17" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/><path d="M8 6l-1 3h2.5L8 12" stroke="currentColor" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round"/>',
  },
  'prompt-design': {
    type: 'svg',
    src: '<rect x="2" y="2" width="16" height="16" rx="1.5" stroke="currentColor" stroke-width="1.4" fill="none"/><line x1="2" y1="7" x2="18" y2="7" stroke="currentColor" stroke-width="1.2"/><line x1="10" y1="7" x2="10" y2="18" stroke="currentColor" stroke-width="1.1"/><line x1="4.5" y1="10" x2="8" y2="10" stroke="currentColor" stroke-width="0.9" stroke-linecap="round"/><line x1="4.5" y1="13" x2="8" y2="13" stroke="currentColor" stroke-width="0.9" stroke-linecap="round"/><line x1="12" y1="10" x2="16" y2="10" stroke="currentColor" stroke-width="0.9" stroke-linecap="round"/><line x1="12" y1="13" x2="16" y2="13" stroke="currentColor" stroke-width="0.9" stroke-linecap="round"/>',
  },
  'tool-integration': {
    type: 'png',
    src: '/icons/bb-tool-integration.png',
  },
  'model-engines': {
    type: 'png',
    src: '/icons/bb-model-engines.png',
  },
  'evaluation-loop': {
    type: 'svg',
    src: '<circle cx="10" cy="10" r="7" stroke="currentColor" stroke-width="1.4" fill="none"/><circle cx="10" cy="10" r="4" stroke="currentColor" stroke-width="1.3" fill="none"/><circle cx="10" cy="10" r="1.5" fill="currentColor"/><line x1="14" y1="6" x2="16" y2="4" stroke="currentColor" stroke-width="1.2" stroke-linecap="round"/><line x1="14" y1="4" x2="17" y2="4" stroke="currentColor" stroke-width="1.2" stroke-linecap="round"/><line x1="17" y1="4" x2="17" y2="7" stroke="currentColor" stroke-width="1.2" stroke-linecap="round"/>',
  },
};
