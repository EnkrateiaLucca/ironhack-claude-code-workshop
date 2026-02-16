# Claude Code Cheatsheet

Quick reference guide for Claude Code — Anthropic's terminal-based AI agent.

---

## Installation

```bash
# Via npm (requires Node.js 18+)
npm install -g @anthropic-ai/claude-code

# Via Homebrew
brew install claude-code

# Launch
claude
```

**Requirements:** Node.js 18+, Anthropic API key

---

## Essential Commands

| Command | Description |
|---------|-------------|
| `/help` | Show all available commands |
| `/clear` | Clear conversation context |
| `/context` | Show context window usage |
| `/compact` | Summarize conversation to reduce tokens |
| `/settings` | Open settings menu |
| `/doctor` | Diagnose configuration issues |
| `/skills` | List available skills |
| `/commands` | List custom commands |

---

## Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Ctrl+C` | Cancel current operation |
| `Ctrl+D` | Exit Claude Code |
| `Tab` | Autocomplete file paths |
| `Up/Down` | Navigate command history |
| `Ctrl+R` | Search command history |

---

## CLAUDE.md Configuration

### Global Config (`~/.claude/CLAUDE.md`)

```markdown
# My Claude Configuration

- My notes are at: ~/obsidian-vault/
- Automation scripts go in: ~/Desktop/automated/
- Use uv for Python scripts with inline metadata
- Ask before deleting multiple files
```

### Project Config (`./CLAUDE.md`)

```markdown
# Project: My App

## Tech Stack
- React + TypeScript
- Tailwind CSS

## Rules
- Use functional components
- Run tests before committing
```

---

## Skills vs Commands

| Feature | Commands | Skills |
|---------|----------|--------|
| Location | `~/.claude/commands/` | `~/.claude/skills/` |
| Format | Single `.md` file | Folder with resources |
| Complexity | Simple prompts | Complex workflows |
| Invoke | `/command-name` | Auto-detected or `/skill-name` |

---

## Skill Folder Structure

```
my-skill/
├── SKILL.md          # Required: Instructions
├── scripts/          # Optional: Python/Bash
├── references/       # Optional: Docs
└── assets/           # Optional: Templates
```

### SKILL.md Template

```yaml
---
name: my-skill
description: What this skill does
---

# My Skill

## When to Use
Use when the user asks to...

## How to Execute
1. Step one
2. Step two
3. Run scripts/process.py
```

---

## Top Productivity Prompts

### Generate Spreadsheet
```
Create a CSV with [columns] containing
[number] rows of [type of data].
Save as [filename].csv
```

### Create PDF Handout
```
Create a PDF cheatsheet about [topic].
Make it scannable with clear sections.
```

### Generate Presentation
```
Create a [N]-slide Remark.js presentation
about [topic] with speaker notes.
```

### Research with Citations
```
Create a research report about [topic]
using these sources: [URLs]
Include text fragment links for verification.
```

### Summarize Notes
```
Review my notes in [folder] and create
a summary with backlinks to sources.
```

---

## MCP Servers

Model Context Protocol enables external tool access.

### Google Calendar Setup
1. Create Google Cloud project
2. Enable Calendar API
3. Create OAuth credentials
4. Configure in Claude settings

### Common MCP Operations
```
Show my calendar for this week
Schedule a meeting tomorrow at 2pm
Find an open slot for a 30-min call
```

---

## Best Practices

1. **Build CLAUDE.md gradually** — Add instructions as you discover patterns

2. **Use skills for repeated tasks** — If you do it 3+ times, make a skill

3. **Verify AI outputs** — Use citations for fact-checking

4. **Multiple instances** — Keep different tasks in separate sessions

5. **Check community first** — Don't reinvent existing skills

6. **Context management** — Use `/compact` when context gets large

---

## Resources

- **Docs:** docs.anthropic.com/claude-code
- **GitHub:** github.com/anthropics/claude-code
- **Skills:** github.com/anthropics/awesome-claude-code
- **Remark.js:** remarkjs.com
- **Deep Dive:** hanchung.dev/claude-skills-deep-dive

---

## Quick Start Workflow

```
1. Install: npm install -g @anthropic-ai/claude-code
2. Launch: claude
3. Try: "Create a simple todo list as a CSV file"
4. Explore: /help
5. Configure: Create ~/.claude/CLAUDE.md
6. Extend: Install skills from awesome-claude-code
```

---

*Ironhack Workshop — Automata Learning Lab*
