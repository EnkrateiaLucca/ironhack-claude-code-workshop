# Example Skills

Working Claude Code skills you can install and use immediately.

## Installation

Copy any skill folder to your Claude Code skills directory:

```bash
cp -r paper-translate ~/.claude/skills/
cp -r anki-card-creator ~/.claude/skills/
```

After copying, the skill will be automatically available in Claude Code.

---

## Included Skills

### 1. `paper-translate`

Translate research papers from PDF while preserving structure and formatting.

**Use when:** You need to translate a research paper or academic document.

**Features:**
- PDF extraction and processing
- Structure-preserving translation
- Markdown output with key findings, methodology, conclusions

**Example:**
```
Read ./paper.pdf and translate it to Portuguese.
Save the output as paper-summary-pt.md
```

---

### 2. `anki-card-creator`

Generate Anki flashcards from any content.

**Use when:** You want to memorize content using spaced repetition.

**Features:**
- Creates properly formatted cards
- Supports multiple card types
- Includes source attribution
- Auto-adds to Anki database

**Example:**
```
Create 10 Anki flashcards from this article about React hooks.
```

---

## Skill Anatomy

Each skill follows this structure:

```
skill-name/
├── SKILL.md          # Instructions (required)
├── scripts/          # Executable code (optional)
├── references/       # Documentation (optional)
└── assets/           # Templates, images (optional)
```

---

## Resources

- [Claude Code Skills Deep Dive](https://hanchung.dev/claude-skills-deep-dive)
- [Awesome Claude Skills](https://github.com/anthropics/awesome-claude-code)

---

*Ironhack Workshop — Automata Learning Lab*
