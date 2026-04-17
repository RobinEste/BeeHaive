/**
 * BeeHaive backend API client.
 *
 * Fetchers return [] on any failure so the build stays green when the
 * backend is unreachable — consumers decide whether to render or hide.
 */

const API_BASE = import.meta.env.PUBLIC_API_URL ?? 'http://localhost:8000';

export interface KnowledgeItem {
  title: string;
  content: string;
  summary_nl: string | null;
  source_url: string | null;
  source_type: string | null;
  is_current: boolean | null;
  curation_score: number;
}

export interface BuildingBlock {
  name: string;
  description: string;
  checklist: string[];
}

export interface Guardrail {
  name: string;
  eu_term: string;
  description: string;
  checklist: string[];
}

export type ToolCategory = 'open_source' | 'framework' | 'enterprise' | 'saas';

export interface Tool {
  slug: string;
  name: string;
  category: ToolCategory;
  url: string;
  description: string;
  display_order: number;
}

async function apiGet<T>(path: string): Promise<T | null> {
  try {
    const res = await fetch(`${API_BASE}${path}`);
    if (!res.ok) {
      console.warn(`[api] ${path} returned ${res.status}`);
      return null;
    }
    return (await res.json()) as T;
  } catch (err) {
    const message = err instanceof Error ? err.message : String(err);
    console.warn(`[api] ${path} failed: ${message}`);
    return null;
  }
}

/**
 * Fetch KnowledgeItems linked to a BuildingBlock.
 * `bbName` must match the Neo4j `BuildingBlock.name` (e.g. "Knowledge",
 * "Client Blueprint") — the same value as the MDX `name` frontmatter.
 */
export async function fetchBBItems(bbName: string): Promise<KnowledgeItem[]> {
  const encoded = encodeURIComponent(bbName);
  const items = await apiGet<KnowledgeItem[]>(`/api/building-blocks/${encoded}/items`);
  return items ?? [];
}

export async function fetchBBTools(bbName: string): Promise<Tool[]> {
  const encoded = encodeURIComponent(bbName);
  const tools = await apiGet<Tool[]>(`/api/building-blocks/${encoded}/tools`);
  return tools ?? [];
}
