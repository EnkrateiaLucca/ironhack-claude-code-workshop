---
name: pdf-handout-creator
description: Create brand-aligned PDF handouts and cheatsheets following Automata Learning Lab design guidelines. Generates professional educational materials with proper typography, color system, and layout structure.
---

# PDF Handout Creator Skill

Generate professional PDF handouts, cheatsheets, and educational materials that strictly follow the Automata Learning Lab brand guidelines. Perfect for creating social media companion PDFs, quick reference guides, and learning resources.

## When to Use This Skill

Use this skill when the user requests:
- Creating a PDF handout or cheatsheet
- Generating a downloadable resource for social media
- Making a quick reference guide or summary document
- Creating educational materials with brand consistency
- Building visual learning aids with proper design

**Trigger phrases:** "create pdf handout", "make a cheatsheet", "generate pdf", "create handout", "make downloadable guide", "pdf resource", "cheatsheet for"

## Brand Guidelines Applied

This skill automatically applies the Automata Learning Lab brand system:

### Color System
- **Background:** Warm Cream (#F5F3EB) for page canvas
- **Text:** Ink Black (#000000) for primary content
- **Accents:** Coral, Golden, Sage, Sky for callouts and highlights
- **Borders:** 2px solid black (sharp corners, no radius)

### Typography
- **Headings:** IBM Plex Sans Bold (24-32pt)
- **Body:** IBM Plex Sans Regular (10-12pt)
- **Technical:** JetBrains Mono for code/labels
- **Line Height:** 1.5-1.6 for readability

### Layout Structure
- Sharp geometric design (0px border radius)
- Clear visual hierarchy
- Structured spacing (8px, 16px, 24px, 40px)
- White cards on cream background
- 2px black borders for containment

### Components
- **Callouts:** Color-coded boxes (Info=Sky, Success=Sage, Caution=Golden, Alert=Coral)
- **Cards:** White background with 2px black border
- **Sections:** Clear hierarchy with accent color accents
- **Headers:** Bold typography with optional accent underlines

## Script Location

```
~/.claude/skills/pdf-handout-creator/create-handout.py
```

## Usage

The skill accepts content in various formats:

### 1. Simple Text Content
```
Create a PDF handout about Python list comprehensions
```

### 2. Structured Content with Sections
```
Create a cheatsheet with:
- Title: Git Commands Cheatsheet
- Sections:
  - Basic Commands
  - Branching
  - Remote Operations
```

### 3. From Existing Content
```
Create a PDF handout from this article: [URL or pasted content]
```

### 4. Custom Layout
```
Make a 2-column cheatsheet about API endpoints with code examples
```

## Output Location

Generated PDFs are saved to:
- `/Users/greatmaster/Desktop/automated/` (default automation folder)
- Automatically opened after generation

## Examples

### Example 1: Quick Reference
```
Create a PDF handout: "5 Key Principles of Prompt Engineering"
```

Generates a single-page PDF with:
- Bold heading in brand typography
- 5 numbered sections with clear hierarchy
- Sage green callout boxes for tips
- Proper spacing and margins

### Example 2: Technical Cheatsheet
```
Make a cheatsheet for Docker commands with code examples
```

Generates a structured PDF with:
- Title section with accent border
- Commands in monospace (JetBrains Mono)
- Categorized sections
- Sky blue info callouts for explanations

### Example 3: Social Media Resource
```
Create a downloadable PDF guide from this thread about async Python
```

Generates a polished handout with:
- Professional layout following brand guidelines
- Clear sections with visual hierarchy
- Accent colors for emphasis
- Ready for social media sharing

## File Naming

Generated files follow the pattern:
- `handout-{slugified-title}-{timestamp}.pdf`
- Example: `handout-git-commands-20260109.pdf`

## Dependencies

The script uses:
- `reportlab` for PDF generation
- `uv` package manager for inline dependencies
- Brand guidelines reference document

## Technical Notes

- PDFs are US Letter size (8.5" x 11")
- 40px margins on all sides (space-xl)
- RGB color mode for digital display
- Embedded fonts for consistent rendering
- No rounded corners (sharp geometric design)
- 2px borders throughout

## Error Handling

- Missing content: Prompts for input
- Invalid formatting: Falls back to clean defaults
- Font unavailable: Uses system fallbacks (Arial, Courier)
- Long content: Auto-paginates with consistent headers

## Customization Options

When creating a handout, you can specify:
- **Title:** Main heading for the document
- **Accent Color:** Choose from Coral, Golden, Sage, or Sky
- **Layout:** Single column (default) or two-column
- **Callouts:** Add information/success/caution/alert boxes
- **Code Blocks:** Technical content in monospace
- **Sections:** Organize with clear hierarchy

## Quality Standards

All generated PDFs ensure:
- ✓ WCAG AA color contrast compliance
- ✓ Clear visual hierarchy
- ✓ Consistent brand identity
- ✓ Professional typography
- ✓ Proper spacing and alignment
- ✓ Sharp, geometric design
- ✓ Maximum 2-3 accent colors per document

## Workflow Integration

After generation:
1. PDF opens automatically for review
2. File saved to automations folder
3. Ready for upload/sharing
4. Maintains brand consistency across all materials
