# Anki Card Creator Skill

Automatically create Anki flashcards and route them to the appropriate deck based on content type.

## Quick Start

```bash
# Single card (auto-detected category)
uv run ~/.claude/skills/anki-card-creator/create-anki-cards.py \
  -q "What is X?" \
  -a "X is..." \
  -s "Source"

# Specify category explicitly
uv run ~/.claude/skills/anki-card-creator/create-anki-cards.py \
  -q "How to perform technique?" \
  -a "Step 1, Step 2, Step 3..." \
  --category movement

# Batch mode
uv run ~/.claude/skills/anki-card-creator/create-anki-cards.py \
  --batch cards.json
```

## Deck Routing

| Category | Deck Name | Auto-detected for |
|----------|-----------|-------------------|
| `knowledge` | Knowledge | Research, technical concepts, study material |
| `movement` | Movement/Grappling/Strengh Training | Physical techniques, exercises, training |
| `notes` | Notes and Reminders | Personal reminders, procedures, quick references |

## Batch JSON Format

```json
[
  {
    "question": "Front of card",
    "answer": "Back of card",
    "source": "Optional source",
    "category": "knowledge"
  }
]
```

## Usage from Claude

When a user asks to create Anki cards, Claude will:

1. Analyze the content to determine the category
2. Format the information as Q&A pairs
3. Run this script to create and import the cards
4. Confirm which deck the cards were added to

## Files

- `skill.md` - Complete documentation for Claude
- `create-anki-cards.py` - Main implementation script
- `example-batch.json` - Example batch file with 3 cards
- `README.md` - This file

## Requirements

- Python 3.12+
- `genanki` package (auto-installed via uv)
- Anki installed on macOS

## Testing

The skill has been tested with:
- ✓ Single card creation with auto-detection
- ✓ Explicit category selection
- ✓ Batch mode with multiple decks
- ✓ Auto-import to Anki
- ✓ All three deck types (knowledge, movement, notes)
