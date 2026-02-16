# Claude Code for Non-Coders — Ironhack Workshop

Workshop materials for teaching non-technical users how to use Claude Code as a personal AI assistant.

## What's Inside

```
.
├── workshop-guide.md          # Full workshop article/guide
├── handout/
│   ├── claude-code-cheatsheet.md    # Cheatsheet (markdown source)
│   └── claude-code-cheatsheet.pdf   # Cheatsheet (print-ready PDF)
├── demos/
│   ├── 01-first-task/         # Create a meeting notes file
│   ├── 02-fetch-and-summarize/# Fetch a URL and summarize it
│   ├── 03-translate-paper/    # Translate a research paper PDF
│   ├── 04-anki-flashcards/    # Generate Anki flashcards
│   ├── 05-create-a-skill/     # Use Claude to create a skill
│   └── 06-context-management/ # Show /cost, /compact in action
├── example-skills/
│   ├── paper-translate/       # PDF translation skill
│   └── anki-card-creator/     # Flashcard generation skill
└── example-commands/
    └── anki-cards.md          # Sample custom command
```

## Workshop Topics

1. **What is Claude Code** — terminal-based AI agent vs. chat interfaces
2. **CLAUDE.md** — persistent memory and configuration
3. **Context Management** — tokens, the desk analogy, session hygiene
4. **Skills & Commands** — reusable automation without code
5. **Live Demos** — paper translation, flashcards, skill creation

## Quick Start

```bash
# Install Claude Code
npm install -g @anthropic-ai/claude-code

# Install the example skills
cp -r example-skills/paper-translate ~/.claude/skills/
cp -r example-skills/anki-card-creator ~/.claude/skills/

# Install the example command
cp example-commands/anki-cards.md ~/.claude/commands/

# Start Claude Code
claude
```

## Resources

- [Claude Code Docs](https://docs.anthropic.com/en/docs/claude-code)
- [Awesome Claude Skills](https://github.com/anthropics/awesome-claude-code)
- [Automata Learning Lab](https://automatalearninglab.thinkific.com)

---

*Ironhack Workshop — Automata Learning Lab*
