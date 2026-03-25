import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const buildingBlocks = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/building-blocks' }),
  schema: z.object({
    code: z.string(),           // BB_01, BB_02, etc.
    name: z.string(),           // Knowledge, Client Blueprint, etc.
    tagline: z.string(),        // One-line summary
    icon: z.string(),           // Emoji or icon reference
    order: z.number(),          // Sort order (1-7)
    quote: z.string().optional(), // Hero quote
    checklist: z.array(z.string()),
    quickStart: z.array(z.string()).optional(),
    tools: z.array(z.object({
      name: z.string(),
      description: z.string(),
      url: z.string().optional(),
    })).optional(),
    auditExample: z.object({
      title: z.string(),
      description: z.string(),
    }).optional(),
  }),
});

const guardrails = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/guardrails' }),
  schema: z.object({
    code: z.string(),           // GR_01, GR_02, etc.
    name: z.string(),           // Human Agency, Robustness, etc.
    euTerm: z.string(),         // Official EU term
    tagline: z.string(),        // One-line summary
    icon: z.string(),           // Emoji or icon reference
    order: z.number(),          // Sort order (1-7)
    checklist: z.array(z.string()),
    operationalFocus: z.array(z.string()),
    legislation: z.array(z.object({
      name: z.string(),
      relevance: z.string(),
    })).optional(),
    auditExample: z.object({
      title: z.string(),
      description: z.string(),
    }).optional(),
  }),
});

export const collections = { 'building-blocks': buildingBlocks, guardrails };
