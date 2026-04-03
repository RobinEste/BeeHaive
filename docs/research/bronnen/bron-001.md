---
id: bron-001
title: "Effective context engineering for AI agents"
url: "https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents"
author: "Anthropic Applied AI team (Prithvi Rajasekaran, Ethan Dixon, Carly Ryan, Jeremy Hadfield)"
date: "2025-09-29"
archived: "2026-04-03"
bb_gr: ["Prompt Design", "Dynamic Context", "Model Engines"]
type: "blog"
volledige_tekst: true
ingested: false
---

## Samenvatting

Anthropic beschrijft context engineering als de opvolger van prompt engineering: niet alleen de prompt optimaliseren, maar de volledige context-state (system prompts, tools, MCP, data, message history) beheren als eindige resource met afnemend rendement. Sleuteltechnieken: compaction, structured note-taking, sub-agent architecturen.

## Relevante passages

**Definitie context engineering vs prompt engineering:**
Context engineering is het cureren en onderhouden van de optimale set tokens tijdens LLM-inference, inclusief alle informatie buiten de prompts zelf.

**System prompt altitude:**
De "juiste hoogte" is de balans tussen te prescriptief (fragiel) en te vaag (onvoorspelbaar).

**Agentic search:**
Just-in-time context retrieval via lightweight identifiers (file paths, queries, links) in plaats van alle data vooraf laden.

**Lange-horizon taken:**
Drie strategieën: compaction (samenvatten + herinitiëren), structured note-taking (persistente geheugen), sub-agent architecturen (geïsoleerde context per taak).

## Kernquotes

> "Building with language models is becoming less about finding the right words and phrases for your prompts, and more about answering the broader question of 'what configuration of context is most likely to generate our model's desired behavior?'" — Context engineering definitie

> "The optimal altitude strikes a balance: specific enough to guide behavior effectively, yet flexible enough to provide the model with strong heuristics to guide behavior." — System prompt design

> "Context, therefore, must be treated as a finite resource with diminishing marginal returns." — Waarom context engineering essentieel is

> "Do the simplest thing that works" — Advies voor teams die agents bouwen

## Volledige originele tekst

[Zie volledige tekst in crawl-output — te lang voor archivering, relevante secties hierboven opgenomen]
