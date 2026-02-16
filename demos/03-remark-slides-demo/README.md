# Demo 3: Presentation Slides with Remark.js

**Duration:** ~5 minutes

## What This Demo Shows

- Creating HTML-based presentations from markdown
- The `remark-slides-skill` workflow
- Single-file presentations that work anywhere

## Live Demo Prompt

Use the prompt in `prompt.txt` — copy and paste it into Claude Code.

## Expected Behavior

1. Claude loads the `remark-slides-skill`
2. Structures the presentation content
3. Generates a single HTML file with embedded CSS and remark.js
4. Applies brand styling (Warm Cream background, IBM Plex fonts)
5. Opens in default browser

## Fallback

If the live demo fails, open `expected-output/claude-code-intro.html` in a browser.

## Talking Points

- **Single HTML file** — no dependencies, works offline, easy to share
- **Markdown-based** — slides are written in markdown within the HTML
- **Presenter mode** — press `p` for notes, press `c` for clone view
- **Export to PDF** — print from browser

## Remark.js Features to Highlight

```markdown
---           # Slide separator
--            # Incremental reveal
.center[]     # Center content
.left-column  # Two-column layout
???           # Speaker notes (hidden)
```

## Show the Sample

The `remark-slides-skill` includes a working example:
```
~/.claude/skills/remark-slides-skill/examples/sample-presentation.html
```

Open this in browser to show what a finished presentation looks like.
