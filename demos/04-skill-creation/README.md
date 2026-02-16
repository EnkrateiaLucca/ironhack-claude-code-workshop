# Demo 4: Creating Skills with Claude (Meta-Demo)

**Duration:** ~5 minutes

## What This Demo Shows

- How skills are structured
- Using Claude to create new skills
- The skill creation workflow
- Extensibility of Claude Code

## Live Demo Prompt

Use the prompt in `prompt.txt` — copy and paste it into Claude Code.

## Expected Behavior

1. Claude creates a new folder: `meeting-notes-summarizer/`
2. Generates `SKILL.md` with proper frontmatter and instructions
3. Creates `scripts/format-notes.py` for output formatting
4. Optionally creates `references/` for templates

## Folder Structure Created

```
meeting-notes-summarizer/
├── SKILL.md
│   ├── name: meeting-notes-summarizer
│   ├── description: Summarize meeting notes...
│   ├── When to use
│   ├── Output format
│   └── Script reference
├── scripts/
│   └── format-notes.py
└── references/
    └── output-template.md
```

## Fallback

If the live demo fails:
1. Show the `skill-creator` skill in `example-skills/skill-creator/`
2. Walk through its `SKILL.md` file
3. Explain the 6-step skill creation process

## Talking Points

- **Skills prepare Claude** — they don't solve problems directly, they equip Claude with knowledge
- **Progressive disclosure** — metadata always loaded, SKILL.md loaded on trigger, resources loaded as needed
- **Bundled resources**:
  - `scripts/` — executable code for deterministic tasks
  - `references/` — documentation loaded into context
  - `assets/` — files used in output (templates, images)

## The Meta Moment

Point out: "We just used Claude to create a workflow that Claude will use. This is how you extend Claude Code's capabilities."

## Bonus: Using skill-creator

For more complex skills:
```
/skill-creator I want to create a skill that generates
weekly status reports from my git commits and calendar events
```

This invokes the `skill-creator` skill which guides through:
1. Understanding with concrete examples
2. Planning reusable contents
3. Initializing structure
4. Editing SKILL.md
5. Packaging for distribution
