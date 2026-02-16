# Claude Code Cheatsheet — Non-Coders Edition

Quick reference for the Ironhack workshop: Claude Code for Non-Coders.

---

## What is Claude Code?

An AI agent that runs **in your terminal**. Unlike AI chats, it executes actions on your machine — creates files, reads documents, runs commands, and chains multi-step tasks.

```bash
claude          # Start Claude Code
```

---

## CLAUDE.md — Persistent Memory

### Global: `~/.claude/CLAUDE.md`

```markdown
# About Me
- My Obsidian vault: ~/Documents/obsidian-vault/
- My Anki database: ~/Library/Application Support/Anki2/
- My automations: ~/automations/

# Preferences
- Use markdown formatting for notes
- Use descriptive filenames with dates
```

### Per-Project: `./CLAUDE.md`

```markdown
# Project: IronHack Workshop
- Output files go in ./output/
- Use Portuguese for student materials
```

**Rule:** Every time you repeat instructions, add them to CLAUDE.md instead.

---

## Context Management — The Golden Rule

**One task, one session, one focus.**

### The Desk Analogy

Your context window (~200K tokens) is like a desk. Everything takes space: your messages, Claude's responses, files read, conversation history. Overload it and things fall off.

### Bad vs Good Prompting

```
BAD:  Read all 200 notes, summarize them, create flashcards,
      then organize by difficulty. (all in one session)

GOOD: Session 1 → Scout filenames
      Session 2 → Read specific files + summarize
      Session 3 → Create flashcards from summary file
```

Connect sessions through **files**, not conversation history.

### Instruction Compression

1. **Front-load in CLAUDE.md** — write preferences once, not every prompt
2. **Use reference files** — `"Follow ./brand-guidelines.md"` instead of pasting rules
3. **Create commands** — `/anki-cards [URL]` replaces a paragraph of instructions
4. **Be specific, not exhaustive** — trust the configuration

---

## Context Commands

| Action | Command |
|--------|---------|
| Check token usage | `/cost` |
| Clear conversation | `/clear` |
| Compact context | `/compact` |
| Start fresh | Exit + `claude` |

---

## Skills & Commands

### Custom Commands (simple)

Save a `.md` file in `~/.claude/commands/`:

```markdown
# /anki-cards
Create Anki flashcards from this content.
Output: CSV with Front, Back, Source fields.
Rules: 10-15 cards, clear questions, include sources.
```

Invoke: `/anki-cards [URL or content]`

### Skills (complex)

```
~/.claude/skills/my-skill/
├── SKILL.md      ← instructions (required)
├── scripts/      ← executable code
├── references/   ← documentation
└── assets/       ← templates, images
```

### Comparison

| | Commands | Skills |
|---|---|---|
| Complexity | Simple prompt | Multi-file workflow |
| Setup | One .md file | Folder + SKILL.md |
| Use case | Quick shortcuts | Deterministic workflows |

---

## Workshop Demo Prompts

**First Task:**
```
Create a markdown file called "meeting-notes.md" with today's date,
sections for Attendees, Agenda, Discussion, Action Items.
```

**Fetch & Summarize:**
```
Fetch https://arxiv.org/abs/2503.10622 and create a summary
note with the key findings.
```

**Translate Paper:**
```
Read ./paper.pdf. Translate to Portuguese with key findings,
methodology, conclusions. Save as paper-summary-pt.md
```

**Anki Flashcards:**
```
Read my notes about prompt engineering. Create 10 Anki
flashcards as a CSV file.
```

**Create a Skill (meta!):**
```
Create a skill that translates PDF papers to Portuguese.
Put it in .claude/skills/translate-paper/
```

---

## Best Practices

1. **Start simple** — build complexity gradually
2. **Build CLAUDE.md iteratively** — add as you discover patterns
3. **One task, one session** — connect through files, not history
4. **Verify outputs** — always fact-check AI-generated content
5. **3x rule** — if you do it 3+ times, make a command or skill
6. **Check community first** — github.com/anthropics/awesome-claude-code

---

## Resources

- **Docs:** docs.anthropic.com/en/docs/claude-code
- **GitHub:** github.com/anthropics/claude-code
- **Community Skills:** github.com/anthropics/awesome-claude-code
- **Skills Deep Dive:** hanchung.dev/claude-skills-deep-dive
- **Course:** automatalearninglab.thinkific.com

---

*Ironhack Workshop — Automata Learning Lab*
