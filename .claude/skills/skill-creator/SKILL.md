---
name: skill-creator
description: Create new Claude Code skills with proper structure, frontmatter, and best practices. Use when the user wants to create a new skill, scaffold a skill directory, or update an existing skill's SKILL.md. Trigger phrases include "create a skill", "new skill", "make a skill", "scaffold a skill".
disable-model-invocation: true
argument-hint: <skill-name> [--path <location>]
---

# Skill Creator

Create well-structured Claude Code skills following the official documentation and best practices.

## When to Use

- Creating a new skill from scratch
- Scaffolding a skill directory with proper structure
- Updating or improving an existing SKILL.md
- Converting a workflow or set of instructions into a reusable skill

## Skill Creation Workflow

### Step 1: Gather Requirements

Before creating anything, understand what the skill should do by asking:

1. What does the skill do? (core purpose in 1-2 sentences)
2. What triggers it? (user phrases, scenarios, file types)
3. Should it be user-invocable, model-invocable, or both?
4. Does it need bundled resources (scripts, references, assets)?
5. Should it run inline or in a forked subagent (`context: fork`)?

Keep questions focused — ask 2-3 at a time, not all at once.

### Step 2: Determine Skill Location

| Location | Path | Scope |
|----------|------|-------|
| Personal | `~/.claude/skills/<name>/SKILL.md` | All projects |
| Project | `.claude/skills/<name>/SKILL.md` | This project only |

Default to **personal** (`~/.claude/skills/`) unless the user specifies otherwise or the skill is project-specific.

### Step 3: Initialize the Skill

Run the bundled init script to scaffold the directory:

```bash
python .claude/skills/skill-creator/scripts/init_skill.py <skill-name> --path <parent-directory>
```

Examples:
```bash
# Personal skill (available everywhere)
python .claude/skills/skill-creator/scripts/init_skill.py my-skill --path ~/.claude/skills

# Project skill (this repo only)
python .claude/skills/skill-creator/scripts/init_skill.py my-skill --path .claude/skills
```

The script creates:
```
<skill-name>/
├── SKILL.md          # Template with TODO placeholders
├── scripts/          # Executable code (Python/Bash)
│   └── example.py
├── references/       # Docs loaded into context as needed
│   └── api_reference.md
└── assets/           # Files used in output (templates, images)
    └── example_asset.txt
```

### Step 4: Write the SKILL.md

#### Frontmatter (YAML between `---` markers)

All fields are optional except `description` (recommended):

| Field | Purpose | Example |
|-------|---------|---------|
| `name` | Slash command name (kebab-case, max 64 chars) | `my-skill` |
| `description` | When to use this skill (Claude reads this) | `Generate API docs from code` |
| `argument-hint` | Autocomplete hint | `[filename] [format]` |
| `disable-model-invocation` | Only user can trigger (`/name`) | `true` |
| `user-invocable` | Hide from `/` menu (background knowledge) | `false` |
| `allowed-tools` | Restrict tool access | `Read, Grep, Glob` |
| `context` | Run in isolated subagent | `fork` |
| `agent` | Subagent type (requires `context: fork`) | `Explore` |
| `model` | Override model | `sonnet` |

#### Body Content Rules

1. **Write in imperative/verb-first form**: "Extract the data" not "You should extract the data"
2. **Keep SKILL.md under 500 lines** — move detailed content to `references/`
3. **Reference bundled resources** with paths so Claude knows they exist
4. **Use `$ARGUMENTS`** for user input: `$ARGUMENTS` (all), `$0` `$1` (positional)
5. **Use `!`command`` syntax** to inject dynamic context (runs before Claude sees content)

#### Recommended Sections

```markdown
# Skill Title

## Overview
1-2 sentences on what this enables.

## When to Use
- Bullet list of trigger scenarios
- Trigger phrases: "create X", "generate Y"

## Workflow / Instructions
Step-by-step numbered instructions.
Reference scripts: `~/.claude/skills/<name>/scripts/tool.py`

## Examples
2-3 concrete usage examples showing user request + expected behavior.

## Resources (if applicable)
- `scripts/` — what each script does
- `references/` — what reference docs contain
- `assets/` — what templates/files are available
```

### Step 5: Clean Up Scaffolding

Delete any example files and directories not needed for the skill. The init script creates placeholder files in `scripts/`, `references/`, and `assets/` — most skills won't need all three.

### Step 6: Verify the Skill

After creating the skill, verify by:
1. Checking the SKILL.md has no remaining TODO placeholders
2. Confirming the `description` is specific enough for Claude to know when to activate
3. Testing with `/skill-name` to ensure it loads correctly
4. If the skill has `disable-model-invocation: false` (default), verify Claude triggers it for matching requests

## Key Design Principles

### Progressive Disclosure
- **Metadata** (~100 words): Always in context — name + description
- **SKILL.md body** (<5k words): Loads when skill triggers
- **Bundled resources** (unlimited): Loaded only as needed by Claude

### Invocation Control Matrix

| Setting | User invokes | Claude invokes | Use case |
|---------|-------------|---------------|----------|
| Default | Yes | Yes | Most skills |
| `disable-model-invocation: true` | Yes | No | Deploy, commit, send messages |
| `user-invocable: false` | No | Yes | Background knowledge, context |

### When to Use `context: fork`
- The skill performs a self-contained task (research, analysis, generation)
- The skill doesn't need conversation history
- Running in isolation prevents context pollution

### When to Bundle Scripts
- The same code gets rewritten repeatedly
- Deterministic reliability is needed
- Token efficiency matters (scripts execute without loading into context)

## Common Patterns

### Task Skill (user-triggered action)
```yaml
---
name: deploy
description: Deploy the application to production
disable-model-invocation: true
context: fork
---
```

### Reference Skill (background knowledge)
```yaml
---
name: api-conventions
description: API design patterns for this codebase
user-invocable: false
---
```

### Research Skill (forked exploration)
```yaml
---
name: deep-research
description: Research a topic thoroughly
context: fork
agent: Explore
---
```

### Dynamic Context Skill (injects live data)
```yaml
---
name: pr-summary
description: Summarize a pull request
context: fork
allowed-tools: Bash(gh *)
---
PR diff: !`gh pr diff`
Changed files: !`gh pr diff --name-only`
```
