# Demo 2: PDF Handouts with Brand Guidelines

**Duration:** ~5 minutes

## What This Demo Shows

- Creating professional PDFs with Claude Code
- Using brand guidelines for consistent styling
- The `pdf-handout-creator` skill in action

## Live Demo Prompt

Use the prompt in `prompt.txt` — copy and paste it into Claude Code.

Alternatively, use the skill directly:
```
/pdf-handout-creator Create a cheatsheet about "5 Essential Git Commands"
```

## Expected Behavior

1. Claude loads the `pdf-handout-creator` skill
2. Structures the content into sections
3. Applies brand styling (Warm Cream background, IBM Plex Sans fonts, 2px black borders)
4. Generates PDF using the bundled Python script
5. Opens the PDF automatically

## Fallback

If the live demo fails, open `expected-output/git-commands-cheatsheet.pdf`

## Talking Points

- **Brand consistency** — same visual identity across all materials
- **Skill = reusable workflow** — bundled script + instructions + brand reference
- **Output location** — files go to `~/Desktop/automated/` by default

## Brand System to Highlight

| Element | Value |
|---------|-------|
| Background | Warm Cream (#F5F3EB) |
| Text | Ink Black (#000000) |
| Accents | Coral, Golden, Sage, Sky |
| Borders | 2px solid black, sharp corners |
| Fonts | IBM Plex Sans, JetBrains Mono |
