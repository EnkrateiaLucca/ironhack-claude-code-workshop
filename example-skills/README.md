# Example Skills

These are production-ready Claude Code skills you can install and use immediately.

## Installation

Copy any skill folder to your Claude Code skills directory:

```bash
# Copy a skill
cp -r remark-slides-skill ~/.claude/skills/

# Or copy all of them
cp -r * ~/.claude/skills/
```

After copying, the skill will be automatically available in Claude Code.

---

## Included Skills

### 1. `remark-slides-skill`

Generate professional HTML presentations using Remark.js.

**Use when:** You need to create a presentation from content or an outline.

**Features:**
- Single-file HTML output
- Brand-aligned styling
- Speaker notes support
- Code syntax highlighting
- Fetches content from URLs automatically

**Example:**
```
Create a 10-slide presentation about machine learning basics
with code examples and speaker notes.
```

---

### 2. `pdf-handout-creator`

Create professional PDF handouts and cheatsheets with brand consistency.

**Use when:** You need a downloadable PDF resource, cheatsheet, or handout.

**Features:**
- Automata Learning Lab brand styling
- IBM Plex Sans / JetBrains Mono fonts
- Color-coded callouts (Info, Success, Caution, Alert)
- Auto-opens generated PDF

**Example:**
```
Create a PDF cheatsheet about Python list comprehensions
with code examples and best practices.
```

---

### 3. `skill-creator`

Meta-skill for creating new Claude Code skills.

**Use when:** You want to create a new skill with proper structure.

**Features:**
- Guides through 6-step creation process
- Generates proper folder structure
- Creates SKILL.md with frontmatter
- Includes packaging scripts

**Example:**
```
/skill-creator I want to create a skill that generates
weekly status reports from my git commits.
```

---

### 4. `anki-card-creator`

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

The `SKILL.md` file contains:
1. YAML frontmatter with `name` and `description`
2. When to use the skill
3. How to execute it
4. References to bundled resources

---

## Creating Your Own Skills

1. Study these examples to understand the pattern
2. Use `/skill-creator` for guided creation
3. Or manually create the folder structure
4. Test thoroughly before sharing

See the `skill-creator` skill for detailed guidance.

---

## Resources

- [Claude Code Skills Deep Dive](https://hanchung.dev/claude-skills-deep-dive)
- [Awesome Claude Skills](https://github.com/anthropics/awesome-claude-code)
- [Anthropic Engineering Blog](https://www.anthropic.com/engineering/skills)

---

*Ironhack Workshop — Automata Learning Lab*
