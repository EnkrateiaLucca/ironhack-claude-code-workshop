# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Workshop materials for an **Ironhack workshop** teaching non-technical users how to use Claude Code as a personal AI assistant. This is educational content, not a software project — there are no build steps, tests, or dependencies.

**Audience:** Non-coders. All materials should be written in clear, accessible language. Avoid jargon unless it's being explicitly taught.

## Repository Structure

- `workshop-guide.md` — The full workshop article/guide (primary content)
- `handout/` — Print-ready cheatsheet (markdown source + PDF)
- `demos/01-06/` — Six sequential demo modules, each with a `README.md` (instructions) and `prompt.txt` (the exact prompt to run)
- `example-skills/` — Two complete Claude Code skills (paper-translate, anki-card-creator) used as teaching examples
- `example-commands/` — Sample custom command (`anki-cards.md`)
- `paper-translate-output/` — Sample output from the paper-translate skill demo

## Workshop Flow

The six demos follow a progression: basic file creation → web fetching → PDF translation → flashcard generation → skill creation (meta) → context management. When adding or modifying demos, maintain this beginner-to-advanced arc.

## Content Conventions

- Demo prompts in `prompt.txt` files should be copy-pasteable into Claude Code as-is
- The workshop teaches five core concepts: Claude Code basics, CLAUDE.md, context management, skills/commands, and live workflows
- The "desk analogy" for context windows is a central teaching metaphor — keep it consistent
- Example skills should be self-contained and installable by copying to `~/.claude/skills/`

## Key Files to Edit Together

When updating workshop content, these files share overlapping material and should stay in sync:
- `workshop-guide.md` (full guide) ↔ `handout/claude-code-cheatsheet.md` (condensed version)
- `demos/*/README.md` (demo instructions) ↔ `demos/*/prompt.txt` (the actual prompts)
- `example-skills/*/SKILL.md` ↔ references in `workshop-guide.md` and demo READMEs
