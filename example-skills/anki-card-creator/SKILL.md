---
name: anki-card-creator
description: Create Anki flashcards from content and automatically add them to the appropriate deck (Knowledge, Movement/Grappling, or Notes).
---

# Anki Card Creator Skill

Create Anki flashcards from any content (text, URLs, conversations) and automatically import them into the correct deck based on the content type.

## When to Use This Skill

Use this skill when the user requests:
- Creating Anki cards from information they want to remember
- Converting learning material into flashcards
- Saving important facts, concepts, or reminders to Anki
- Building study decks from articles, videos, or conversations

**Trigger phrases:** "create anki cards", "make flashcards", "add to anki", "remember this in anki", "save to anki", "anki cards for", "flashcard this", "create cards from video", "video flashcards", "cards from transcript"

## Deck Routing Rules

The skill automatically routes cards to the appropriate deck:

| Category | Deck Name | Content Type |
|----------|-----------|--------------|
| **Knowledge** | `Knowledge` | Academic concepts, research findings, technical information, definitions, theories, facts to study |
| **Movement** | `Movement/Grappling/Strengh Training` | Physical exercises, grappling techniques, movement patterns, strength training tips, form cues |
| **Notes** | `Notes and Reminders` | Personal reminders, quick notes, to-do items, procedural steps, personal references |

### Auto-Detection Keywords

**Knowledge indicators:**
- Research, study, theory, concept, definition, analysis
- Technical terms, scientific findings, academic content
- Learning materials, educational content

**Movement indicators:**
- Exercise, workout, technique, form, training, grappling
- BJJ, judo, wrestling, strength, mobility, stretching
- Physical movement, athletic performance

**Notes indicators:**
- Reminder, remember, note, todo, procedure, steps
- Personal reference, quick note, how-to
- Not intended for systematic study

## Script Location

```
~/.claude/skills/anki-card-creator/create-anki-cards.py
```

## Basic Usage

### Create Cards with Auto-Detection

```bash
uv run ~/.claude/skills/anki-card-creator/create-anki-cards.py \
  -q "What is the optimal interval for partial recall?" \
  -a "30-50% of perfect recall interval" \
  -s "Bjork & Bjork (2011)"
```

### Specify Deck Explicitly

```bash
uv run ~/.claude/skills/anki-card-creator/create-anki-cards.py \
  -q "Triangle choke setup from closed guard" \
  -a "Break posture, angle off, pull arm across, kick leg over, squeeze knees" \
  --category movement
```

### Multiple Cards at Once

```bash
uv run ~/.claude/skills/anki-card-creator/create-anki-cards.py \
  --batch cards.json
```

Where `cards.json` contains:
```json
[
  {
    "question": "Question 1?",
    "answer": "Answer 1",
    "source": "Source 1",
    "category": "knowledge"
  },
  {
    "question": "Question 2?",
    "answer": "Answer 2"
  }
]
```

## Command-Line Options

| Option | Description | Default |
|--------|-------------|---------|
| `-q, --question` | Front of card (question or prompt) | - |
| `-a, --answer` | Back of card (answer or explanation) | - |
| `-s, --source` | Source/citation for the information | `""` |
| `-c, --category` | Deck category: `knowledge`, `movement`, or `notes` | Auto-detect |
| `--batch` | Path to JSON file with multiple cards | - |
| `--video-batch` | Path to JSON file with video cards (includes timestamps) | - |
| `--video` | Path to video file for screenshot extraction | - |
| `--deck-name` | Custom deck name (uses `::` for hierarchy) | Auto-generated |
| `--no-import` | Create package but don't auto-import | `False` |
| `--output` | Custom output path for .apkg file | Auto-generated |
| `--model-type` | Card model: `basic`, `cloze`, `basic-reverse`, `video` | `basic` |

## Card Model Types

### Basic (Default)
Simple front/back card with optional source citation.

```
Front: What is X?
Back: X is... [Source: ...]
```

### Basic with Reverse
Creates two cards: question→answer and answer→question.

```bash
--model-type basic-reverse
```

### Cloze Deletion
Use `{{c1::text}}` for cloze deletions.

```bash
-q "The optimal interval for {{c1::partial recall}} is {{c2::30-50%}} of perfect recall" \
--model-type cloze
```

### Video Cards with Screenshots
For creating cards from video content with automatic screenshot extraction.

```bash
uv run ~/.claude/skills/anki-card-creator/create-anki-cards.py \
  --video-batch cards.json \
  --video /path/to/video.mp4 \
  --deck-name "BJJ::Back Attacks::Gordon Ryan"
```

Where `cards.json` contains:
```json
[
  {
    "question": "What is the first step from the back?",
    "answer": "Put a wedge in place with defensive hands",
    "timestamp": "0:03"
  },
  {
    "question": "How do you extract your elbow correctly?",
    "answer": "Drag shoulders FORWARD toward elbow, not back",
    "timestamp": "0:45"
  }
]
```

**Video card features:**
- Automatically extracts screenshots at specified timestamps using ffmpeg
- Embeds the original video file path for reference
- Shows timestamp on the answer side
- Supports timestamps in formats: `0:45`, `1:30`, `00:01:30`

## Workflow for Claude

When a user wants to create Anki cards:

### 1. Analyze Content Type

Determine the category automatically by analyzing the content:
- Does it contain research, technical concepts, or study material? → **knowledge**
- Does it involve physical movement, exercise, or martial arts? → **movement**
- Is it a reminder, procedure, or quick reference? → **notes**

### 2. Extract Key Information

From the content, identify:
- **Questions/Prompts**: What should trigger recall?
- **Answers**: What information should be remembered?
- **Sources**: Where did this come from? (if applicable)

### 3. Format Cards Appropriately

**For research/concepts (Knowledge):**
- Focus on understanding, not just facts
- Include context in questions
- Add sources for credibility
- Consider creating multiple cards for complex concepts

**For techniques (Movement):**
- Break complex movements into steps
- Include key cues and common mistakes
- Reference coaching points or instructors

**For reminders (Notes):**
- Keep concise and actionable
- Focus on recall of specific information
- No need for extensive sources

### 4. Create and Import

Run the script with appropriate parameters, and it will:
1. Generate properly formatted Anki cards
2. Create an `.apkg` package file
3. Automatically import into Anki (opens the file)
4. Cards appear in the correct deck

## Example Workflows

### Example 1: Research Findings

```
User: "I want to remember that research shows partial recall benefits long-term retention"

Actions:
1. Detect category: knowledge (research finding)
2. Format as Q&A:
   Q: "Why is partial recall beneficial for long-term learning?"
   A: "Effortful retrieval produces better long-term retention than easy retrieval. This 'desirable difficulty' strengthens memory more than effortless recall."
   Source: "Pyc & Rawson (2009)"
3. Run: uv run ~/.claude/skills/anki-card-creator/create-anki-cards.py \
   -q "Why is partial recall beneficial for long-term learning?" \
   -a "Effortful retrieval produces better long-term retention..." \
   -s "Pyc & Rawson (2009)"
4. Confirm: "✓ Card created and imported to Knowledge deck"
```

### Example 2: BJJ Technique

```
User: "Add an anki card for triangle choke details from closed guard"

Actions:
1. Detect category: movement (grappling technique)
2. Format with key steps:
   Q: "What are the key steps for triangle choke from closed guard?"
   A: "1. Break opponent's posture\n2. Angle off 45°\n3. Pull arm across centerline\n4. Kick leg over shoulder\n5. Lock ankle behind knee\n6. Squeeze knees together\n7. Pull head down"
3. Run: uv run ~/.claude/skills/anki-card-creator/create-anki-cards.py \
   -q "What are the key steps for triangle choke from closed guard?" \
   -a "1. Break opponent's posture..." \
   --category movement
4. Confirm: "✓ Card created and imported to Movement/Grappling/Strength Training deck"
```

### Example 3: Personal Reminder

```
User: "Remember that my transcription command has a --process flag for readable output"

Actions:
1. Detect category: notes (personal reference/reminder)
2. Format as Q&A:
   Q: "What flag makes transcription output readable?"
   A: "Use --process flag: transcribe file.mp4 --process"
3. Run: uv run ~/.claude/skills/anki-card-creator/create-anki-cards.py \
   -q "What flag makes transcription output readable?" \
   -a "Use --process flag: transcribe file.mp4 --process" \
   --category notes
4. Confirm: "✓ Card created and imported to Notes and Reminders deck"
```

### Example 4: Batch Creation from Article

```
User: "Create anki cards from this article about Python decorators: [URL]"

Actions:
1. Use WebFetch to get article content
2. Extract 5-8 key concepts
3. Detect category: knowledge (technical learning)
4. Create batch JSON with all cards
5. Run: uv run ~/.claude/skills/anki-card-creator/create-anki-cards.py --batch cards.json
6. Confirm: "✓ Created 7 cards and imported to Knowledge deck"
```

### Example 5: Video-Based Cards with Screenshots (BJJ/Movement)

```
User: "Create anki cards from this video transcript with screenshots"
       [Provides: video.mp4 and transcript.txt]

Actions:
1. Read transcript to identify key techniques and timestamps
2. For each key concept, identify:
   - Question: What technique/concept to test
   - Answer: The explanation/steps
   - Timestamp: When this appears in video (e.g., "0:45")
3. Create video-batch JSON file:
   [
     {"question": "What's the first step?", "answer": "...", "timestamp": "0:03"},
     {"question": "Common mistake?", "answer": "...", "timestamp": "0:45"}
   ]
4. Run: uv run ~/.claude/skills/anki-card-creator/create-anki-cards.py \
     --video-batch cards.json \
     --video /path/to/video.mp4 \
     --deck-name "BJJ::Technique::Instructor Name"
5. Confirm: "✓ Created 6 cards with screenshots in BJJ::Technique::Instructor Name"
```

**Important for video cards:**
- Each card includes a screenshot extracted at the timestamp
- The video file path is embedded for reference (can rewatch source)
- Timestamps are displayed on the answer side
- Perfect for technique breakdowns, tutorials, and instructional content

## Card Quality Guidelines

### Good Question/Answer Pairs

**Clear and Specific:**
```
✓ "What is the optimal interval reduction for partial recall in spaced repetition?"
✗ "What about partial recall?"
```

**Self-Contained:**
```
✓ "In the Two-Component Model, what does 'Storage Strength' represent?"
✗ "What does Storage Strength mean?" (missing context)
```

**Testable:**
```
✓ "What are the 3 key principles of effective spaced repetition?"
✗ "Tell me about spaced repetition" (too broad)
```

### Answer Formatting

- **Use HTML for formatting**: `<b>bold</b>`, `<i>italic</i>`, `<br>` for line breaks
- **Use lists**: `<ul><li>Item 1</li><li>Item 2</li></ul>`
- **Keep concise**: Focus on key information, not lengthy explanations
- **Include mnemonics**: When helpful for memory

## Auto-Import Behavior

By default, the script:
1. Creates the `.apkg` file in `/Users/greatmaster/Desktop/automated/`
2. Automatically runs `open <file>.apkg` to import into Anki
3. Returns success message with deck location

If Anki is not running, the system will launch it and import the cards.

## Error Handling

**If deck doesn't exist:**
- Script will note the issue
- Create cards in Default deck
- Advise user to move them manually or check deck names

**If category is ambiguous:**
- Default to `knowledge` deck
- Log the decision
- User can re-run with explicit `--category` flag

**If Anki import fails:**
- Provide path to generated `.apkg` file
- Instruct user to import manually via Anki UI
- File is preserved for manual import

## Tips for Success

1. **Be specific with questions** - The more specific, the better the retrieval practice
2. **One concept per card** - Don't combine multiple ideas
3. **Use sources** - Especially for knowledge cards, citations add credibility
4. **Break down complex movements** - Multiple simple cards > one complex card
5. **Test directionality** - For some cards, use `--model-type basic-reverse`

## Integration with Learning Workflow

This skill works best when integrated into your learning process:

1. **After reading/watching content** - Immediately create cards for key concepts
2. **During conversations** - When you learn something valuable, add it to Anki
3. **After training** - Document techniques and cues while they're fresh
4. **Regular review** - Use Anki's spaced repetition to retain information

## Deck IDs (for reference)

The script uses these deck IDs from your Anki database:
- Knowledge: `1595764330670`
- Movement/Grappling/Strength Training: `1741363521912`
- Notes and Reminders: `1723200755898`

## Video Card Creation - Complete Workflow

When user provides a video file and transcript for flashcard creation:

### Prerequisites
- Video file (.mp4, .mov, etc.)
- Transcript file (with or without timestamps)
- ffmpeg installed (required for screenshot extraction)

### Step-by-Step Process

1. **Read the transcript** to understand the content
2. **Identify key concepts** - what should become flashcards?
   - For BJJ/movement: technique steps, key details, common mistakes
   - For lectures: main concepts, definitions, important points
3. **Determine timestamps** for each card
   - If transcript has timestamps, use them directly
   - If not, estimate based on video duration and content flow
4. **Create the JSON batch file** with this structure:
```json
[
  {
    "question": "Clear, testable question about the concept",
    "answer": "Concise answer with key details",
    "timestamp": "M:SS"
  }
]
```
5. **Run the script**:
```bash
uv run ~/.claude/skills/anki-card-creator/create-anki-cards.py \
  --video-batch /path/to/cards.json \
  --video /path/to/video.mp4 \
  --deck-name "Category::Topic::Source"
```

### Video Card JSON Schema

```json
{
  "question": "string (required) - The front of the card",
  "answer": "string (required) - The back of the card",
  "timestamp": "string (required) - Format: 'M:SS' or 'H:MM:SS'"
}
```

### Output

Each card will include:
- **Front**: Question + screenshot from video at timestamp
- **Back**: Answer + video source path + timestamp reference

### Fallback Behavior

If Anki import fails or there are issues:
1. The .apkg file is saved to `/Users/greatmaster/Desktop/automated/`
2. Create a .txt backup with all cards and screenshot paths
3. Screenshots can be manually attached if needed

### Example Video Batch File

`gordon_ryan_rnc.json`:
```json
[
  {
    "question": "When finishing from the back, what is the FIRST step?",
    "answer": "<b>Put a wedge in place</b> with opponent having defensive hands in.",
    "timestamp": "0:03"
  },
  {
    "question": "What's the COMMON MISTAKE when extracting your elbow for RNC?",
    "answer": "<b>Pulling elbow BACK</b> disconnects ear-to-ear contact.",
    "timestamp": "0:45"
  },
  {
    "question": "What's the CORRECT way to extract your elbow? (Gordon Ryan)",
    "answer": "<b>Build elbow up, drag shoulders FORWARD</b> toward elbow, palm behind head.",
    "timestamp": "1:05"
  }
]
```

Run with:
```bash
uv run ~/.claude/skills/anki-card-creator/create-anki-cards.py \
  --video-batch gordon_ryan_rnc.json \
  --video ~/Downloads/gordon_ryan_tutorial.mp4 \
  --deck-name "BJJ::Back Attacks::Gordon Ryan RNC"
```
