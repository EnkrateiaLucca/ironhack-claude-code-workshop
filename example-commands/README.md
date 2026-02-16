# Example Commands

Custom commands are simple prompt templates saved as `.md` files.

## Installation

Copy any command file to your Claude Code commands directory:

```bash
cp anki-cards.md ~/.claude/commands/
```

Then invoke with `/anki-cards [content or URL]` inside Claude Code.

## Included Commands

| Command | Description |
|---------|-------------|
| `anki-cards.md` | Generate Anki flashcards from any content |

## Commands vs Skills

- **Commands** — Single `.md` file, simple prompt templates, quick shortcuts
- **Skills** — Folder with SKILL.md + scripts/assets, complex workflows

If you do something 3+ times, start with a command. If it gets complex, upgrade to a skill.

---

*Ironhack Workshop — Automata Learning Lab*
