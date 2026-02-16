---
name: remark-slides-skill
description: Generate beautiful, professional presentations in HTML using remark.js templates and best practices.
---

# Remark.js Presentation Generator Skill

You are an expert at creating professional, visually appealing presentations using remark.js. This skill equips you with comprehensive knowledge of established presentation patterns, templates, and best practices.

## INPUT REQUIREMENT

**CRITICAL:** This skill **REQUIRES** a `.md` (markdown) file as input that serves as the instructions and guide for creating the presentation. This instructions file should contain:

- Presentation structure and outline
- Topics and content points to cover
- Links to external resources (will be fetched via WebFetch)
- Paths to images and screenshots (will be included with proper formatting)
- References to PDF files (will be processed using subagents)

**Each line or point in the instructions file is an executable instruction** - you must process links, include images, fetch content, and integrate everything into the final presentation with proper source citations.

## Core Capabilities

When asked to create a presentation, you will:

1. **Read and process the instructions markdown file** - treating each point as an executable task
2. Generate complete, single-file HTML presentations using remark.js
3. **Fetch content from URLs** mentioned in instructions using WebFetch
4. **Process PDF files** mentioned in instructions using Task tool with a subagent
5. **Include images** from paths specified in instructions using appropriate layout styles
6. **Track all sources** and add hyperlink footnote references to all slides that refer to those sources
7. Apply consistent styling and visual patterns according to example in `./examples/sample-presentation.html`
8. Follow established design patterns and color schemes from `./examples/sample-presentation.html` unless instructed otherwise

## Standard HTML Boilerplate

Always start presentations with this Automata Learning Lab brand-aligned structure:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Presentation Title</title>
    <meta charset="utf-8">
    <style>
      @import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600;700&display=swap');
      @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;700&display=swap');

      body {
        font-family: 'IBM Plex Sans', Arial, sans-serif;
        color: #000000;
      }
      h1, h2, h3 {
        font-family: 'IBM Plex Sans', Arial, sans-serif;
        font-weight: 700;
        color: #000000;
      }
      .remark-code, .remark-inline-code {
        font-family: 'JetBrains Mono', Courier, monospace;
      }
      .remark-slide-content {
        background-color: #F5F3EB;
        background-position: center;
        background-repeat: no-repeat;
        background-size: contain;
        color: #2A2825;
      }
      /* Brand Colors Available:
         Primary: #000000 (Ink Black), #F5F3EB (Warm Cream)
         Accents: #E86B5A (Coral), #F5C542 (Golden), #7CB56B (Sage), #5B9BD5 (Sky)
         Light Tints: #FBEAE7 (Coral), #FEF8E6 (Golden), #EEF5EC (Sage), #E8F1F9 (Sky)
      */
    </style>
  </head>
  <body>
    <textarea id="source">
```

**Note:** If the presentation needs a 4:3 aspect ratio, use: `var slideshow = remark.create({ratio: "4:3"});`

---

## Brand Color System

### Primary Colors
- **Ink Black**: `#000000` - Primary text, borders, structural elements
- **Warm Cream**: `#F5F3EB` - Background, page canvas
- **White**: `#FFFFFF` - Cards, containers on cream background

### Accent Colors (Use 2-3 max per composition)
- **Coral**: `#E86B5A` - Primary CTAs, alerts, important highlights
- **Golden**: `#F5C542` - Highlights, tips, featured content
- **Sage**: `#7CB56B` - Success states, progress, completion, demo highlights
- **Sky**: `#5B9BD5` - Information, links, interactive elements

### Light Tints (For backgrounds, callouts, subtle highlighting)
- **Coral Light**: `#FBEAE7` - Alert/warning backgrounds
- **Golden Light**: `#FEF8E6` - Caution/tip backgrounds
- **Sage Light**: `#EEF5EC` - Success/completion backgrounds
- **Sky Light**: `#E8F1F9` - Information backgrounds

### Neutral Grays
- **Gray 100**: `#F5F4F1` - Section backgrounds
- **Gray 300**: `#DDD9D2` - Borders, dividers
- **Gray 500**: `#8A847A` - Disabled, placeholder text
- **Gray 600**: `#5C5750` - Secondary text, captions, links
- **Gray 800**: `#2A2825` - Body text on light backgrounds

### Design Principles
- Sharp corners: `border-radius: 0px` (no rounded edges)
- Primary borders: `2px solid #000000`
- Spacing scale: `4px`, `8px`, `16px`, `24px`, `40px`
- Use no more than 2-3 accent colors per slide
- Maintain high contrast for accessibility (WCAG AA minimum)

---

## Workflow & Best Practices

### When Creating a Presentation:

**PREREQUISITE:** Always start with a `.md` instructions file that outlines the presentation.

1. **Read the instructions markdown file** - This is your primary input and guide
2. **Process each instruction sequentially**:
   - Parse each bullet point or section as a task
   - Identify links that need to be fetched with WebFetch
   - Identify PDFs that need agent processing (use Task tool with subagent_type="general-purpose")
   - Identify images/screenshots that need to be included
3. **Start with the boilerplate** - Include all standard fonts, CSS, and remark setup
4. **Create a title slide** - Use the standard centered format
5. **Add a table of contents** - If the presentation has multiple sections
6. **Use section headers** - To divide major topics
7. **Process content with source tracking**:
   - For each external link, fetch content and create slide(s)
   - Add hyperlink footnote references to slides using external sources
   - Number references sequentially within each slide
8. **Include images using appropriate styles**:
   - Choose layout based on number and purpose of images
   - Use grid layouts for multiple screenshots
   - Use centered with shadow for single important images
   - Use comparison layouts for before/after scenarios
9. **Apply incremental reveals** - For lists and progressive disclosure
10. **Use demo slides** - Centered with header 1 and green highlighting
11. **Add breaks** - Every 20-30 minutes of content
12. **Include Q&A slides** - After major sections or at the end
13. **End with a summary** - Recap key points with references to sources

### Visual Hierarchy:

- **Title slides:** Large, centered, minimal
- **Section headers:** Centered, introduce new topics
- **Content slides:** Left-aligned, detailed information
- **Demo slides:** Green highlighted background, attention-grabbing
- **Break slides:** Simple, centered

### Content Guidelines:

- **Keep slides simple** - One main idea per slide
- **Use visuals liberally** - Images, diagrams, code examples
- **Progressive disclosure** - Use `--` for incremental reveals
- **Consistent styling** - Use the established color palette
- **Code examples** - Always specify language for syntax highlighting
- **White space** - Don't overcrowd slides
- **Grid/comparison layouts** - Always use `font-size: 16px` for text inside colored boxes (e.g., blue `#f0f8ff` and green `#f0fff0` comparison panels)

---

## Common Patterns Quick Reference

- See `./examples/sample-presentation.html` for all the relevant patterns for the slides to be generated

### Comparison Grid Layout (Two Columns)
```html
<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 24px; margin: 24px 0;">
  <div style="background: #E8F1F9; padding: 16px; border: 2px solid #000000; border-radius: 0px;">
    <h4 style="margin-top: 0; color: #000000;">Left Panel Title</h4>
    <ul style="font-size: 16px; color: #2A2825;">
      <li><strong>Point 1:</strong> Description</li>
      <li><strong>Point 2:</strong> Description</li>
    </ul>
  </div>
  <div style="background: #EEF5EC; padding: 16px; border: 2px solid #000000; border-radius: 0px;">
    <h4 style="margin-top: 0; color: #000000;">Right Panel Title</h4>
    <ul style="font-size: 16px; color: #2A2825;">
      <li>Item 1</li>
      <li>Item 2</li>
    </ul>
  </div>
</div>
```
**Note:** Always use sharp corners (0px border-radius), 2px solid black borders, and brand-aligned light tint backgrounds.

### Horizontal Flow Diagram (Step-by-Step Process)

**USE THIS** for sequential steps, workflows, or processes. Cards have equal widths and are connected with arrows.

```html
<div style="display: flex; justify-content: center; align-items: center; gap: 16px; margin: 40px 0;">
  <div style="background: #FBEAE7; border: 2px solid #000000; padding: 16px; border-radius: 0px; text-align: center; width: 140px;">
    <div style="font-size: 1.8em; margin-bottom: 8px; color: #E86B5A;">1</div>
    <h4 style="margin: 8px 0; color: #000000; font-weight: 600;">Step One</h4>
    <p style="font-size: 12px; color: #5C5750; margin: 0;">Description<br>goes here</p>
  </div>
  <div style="font-size: 24px; color: #2A2825;">→</div>
  <div style="background: #FEF8E6; border: 2px solid #000000; padding: 16px; border-radius: 0px; text-align: center; width: 140px;">
    <div style="font-size: 1.8em; margin-bottom: 8px; color: #F5C542;">2</div>
    <h4 style="margin: 8px 0; color: #000000; font-weight: 600;">Step Two</h4>
    <p style="font-size: 12px; color: #5C5750; margin: 0;">Description<br>goes here</p>
  </div>
  <div style="font-size: 24px; color: #2A2825;">→</div>
  <div style="background: #EEF5EC; border: 2px solid #000000; padding: 16px; border-radius: 0px; text-align: center; width: 140px;">
    <div style="font-size: 1.8em; margin-bottom: 8px; color: #7CB56B;">3</div>
    <h4 style="margin: 8px 0; color: #000000; font-weight: 600;">Step Three</h4>
    <p style="font-size: 12px; color: #5C5750; margin: 0;">Description<br>goes here</p>
  </div>
</div>
```

**Key requirements:**
- Fixed `width: 140px` for all cards (ensures visual balance)
- Sharp corners (border-radius: 0px) with 2px solid black borders
- Brand color progression: Coral → Golden → Sage (using light tints for backgrounds)
- Spacing follows brand scale (8px, 16px, 24px, 40px)

**AVOID THIS anti-pattern** (vertical list with badges):
```html
<!-- ❌ DON'T DO THIS - unbalanced badge widths, visually awkward -->
<div style="display: flex; align-items: center; margin-bottom: 15px;">
  <div style="background: #e74c3c; color: white; padding: 10px 20px; border-radius: 5px; margin-right: 15px;">Stuck?</div>
  <p style="margin: 0;">Output quality degrading?</p>
</div>
<div style="display: flex; align-items: center; margin-bottom: 15px;">
  <div style="background: #f39c12; color: white; padding: 10px 20px; border-radius: 5px; margin-right: 15px;">Clear</div>
  <p style="margin: 0;">Start fresh</p>
</div>
```
**Why it's bad:** Badge widths vary based on text length, creating visual imbalance. The vertical layout wastes horizontal space and looks like a bulleted list pretending to be a diagram.

### End of Presentation
```markdown
    </textarea>
    <script src="https://remarkjs.com/downloads/remark-latest.min.js"></script>
    <script>
      var slideshow = remark.create();
    </script>
  </body>
</html>
```

---

## Input Handling

### REQUIRED: Markdown Instructions File

**IMPORTANT:** This skill ALWAYS expects a `.md` (markdown) file as input containing instructions and guidance for the presentation. This file serves as the blueprint for the entire presentation.

The instructions file should contain:
- Presentation outline and structure
- Content points and topics to cover
- Links to resources and references
- Paths to images and screenshots
- Any specific requirements or notes

### Example Instructions File Format:

```markdown
# Presentation: AI and Machine Learning Basics

## Introduction
- Overview of AI
- Historical context (https://example.com/ai-history)
- Current applications

## Core Concepts
- Machine Learning fundamentals
- Neural networks diagram: ./assets/neural-net.png
- PDF resource: ./docs/ml-guide.pdf

## Practical Examples
- Image classification demo
- Example outputs: ./screenshots/demo1.png, ./screenshots/demo2.png

## References
- https://research.example.com/ml-paper
- https://blog.example.com/ai-tutorial
```

### Generating Screenshots

- When instructed, use the available tools to get a screenshot of a webpage given the context of the slide. 

### Hyperlink Footnote Reference System:

**For every slide that uses external sources, add footnote references at the bottom:**

```html
<div style="position: absolute; bottom: 30px; width: 100%; left: 0; text-align: left;">
  <p style="font-size: 14px; margin-bottom: 0px; margin-left: 36px;">
    <sup>[Number]</sup><a href="https://example.com" style="color: #555;">Reference Source</a>
  </p>
</div>
```

**Multiple references on one slide:**

```html
<div style="position: absolute; bottom: 30px; width: 100%; left: 0; text-align: left;">
  <p style="font-size: 14px; margin-bottom: 0px; margin-left: 36px;">
    <sup>[1]</sup><a href="https://example.com" style="color: #555;">First Reference</a><br>
    <sup>[2]</sup><a href="https://another-example.com" style="color: #555;">Second Reference</a><br>
    <sup>[3]</sup><a href="https://third-site.org" style="color: #555;">Third Reference</a>
  </p>
</div>
```

## Notes

- All presentations should work as standalone HTML files
- No external CSS files required - all styling is inline
- Images, pdfs and other files should use relative paths (e.g., `../assets/`, if this folder doesn't exist, create it.)
- The remark.js library is loaded from CDN
- Presentations are keyboard-navigable (arrow keys)
- Press 'p' during presentation for presenter mode
- Press 'c' to clone presentation view for second monitor
