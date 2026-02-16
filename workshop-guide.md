# Claude Code for Productivity

**Ironhack Workshop | 45 Minutes**

> Beyond coding: Using Claude Code as your AI-powered productivity assistant for spreadsheets, PDFs, presentations, and custom workflows.

---

## Workshop Overview

| Duration | Audience | Prerequisites |
|----------|----------|---------------|
| 45 min | Developers, technical learners | Terminal basics, curiosity |

**What you'll learn:**
- How Claude Code works as a terminal-based AI agent
- Creating spreadsheets, PDFs, and presentations with natural language
- Building reusable skills and commands
- Practical workflows for knowledge work

**What you'll take home:**
- Example skills ready to use
- Cheatsheet PDF
- Demo prompts to try yourself

---

## Table of Contents

1. [Quick Claude Code Overview](#section-1-quick-claude-code-overview) (5 min)
2. [Productivity Tasks Demo](#section-2-productivity-tasks-demo) (15 min)
3. [Claude Code Skills Deep Dive](#section-3-claude-code-skills-deep-dive) (15 min)
4. [Practical Workflows & Wrap-up](#section-4-practical-workflows--wrap-up) (10 min)

---

# Section 1: Quick Claude Code Overview

**Time: 5 minutes**

## What is Claude Code?

Claude Code is Anthropic's **agentic coding tool** that lives in your terminal. Unlike chat interfaces, it can actually **do things** on your machine:

- Read and write files
- Execute commands
- Browse the web
- Manage your calendar (via MCP)
- Create documents, spreadsheets, presentations

[Screenshot: Claude Code terminal interface showing a conversation]

> **Key Insight:** Claude Code is marketed as a coding assistant, but it's really a **general-purpose AI agent** that happens to be exceptionally good at coding.

## Installation

```bash
# Install via npm (requires Node.js)
npm install -g @anthropic-ai/claude-code

# Or via Homebrew
brew install claude-code

# Launch in any folder
claude
```

After installation, simply type `claude` in your terminal to start a session.

## The CLAUDE.md Configuration System

One of Claude Code's most powerful features is the **CLAUDE.md configuration file** — Claude's persistent memory.

### Global Configuration (`~/.claude/CLAUDE.md`)

Instructions that apply **every time** you run Claude Code:

```markdown
# My Claude Configuration

- My Obsidian vault is located at: ~/obsidian-vault/
- My Anki deck is stored here: ~/Library/Application Support/Anki2/User 1/
- My automation scripts go in: ~/Desktop/automated/
- When creating calendar events, use .ics files
```

[Screenshot: Example CLAUDE.md file in VS Code]

### Project-Level Configuration

Create a `CLAUDE.md` in any project folder for **project-specific instructions**:

```markdown
# Project: E-commerce App

## Tech Stack
- React + TypeScript
- Tailwind CSS
- Supabase backend

## Coding Standards
- Use functional components
- Prefer named exports
- Run tests before committing
```

> **Pro Tip:** Build your CLAUDE.md gradually. Every time you find yourself repeating instructions to Claude, add them to the file.

## Quick Demo: Your First Claude Code Task

```
Create a simple CSV file with 5 famous programming languages,
their creation year, and creator name.
```

Claude will:
1. Generate the data
2. Ask permission to create the file
3. Save it to your current directory

---

# Section 2: Productivity Tasks Demo

**Time: 15 minutes**

Let's see Claude Code handle real productivity tasks — no coding required.

---

## Demo 1: Spreadsheet Generation

**The prompt:**

```
Create a CSV file with sample sales data for Q1 2025.
Include columns: Date, Product, Quantity, Revenue, Region.
Generate 20 rows of realistic sample data.
Save it as sales-q1-2025.csv
```

[Screenshot: Claude Code creating the CSV file]

**What Claude does:**
- Generates realistic, varied data
- Formats dates properly
- Calculates plausible revenue based on quantity
- Creates the file with proper CSV formatting

> **Beyond basic:** Try asking Claude to create Excel files with multiple sheets, formulas, and formatting using the `openpyxl` library.

### Variations to try:

```
Create a budget spreadsheet with monthly expenses,
automatic totals, and highlight cells over $500.
```

```
Convert this JSON data to a formatted Excel file
with a summary sheet and charts.
```

---

## Demo 2: PDF Handouts with Brand Guidelines

Now let's create professional PDF documents that follow brand guidelines.

**The setup:** I have a brand guidelines PDF that defines my visual identity — colors, fonts, spacing, borders.

**The prompt:**

```
Create a PDF cheatsheet about "5 Essential Git Commands"
Use my brand guidelines document for styling.
Make it clean, scannable, and ready to share on social media.
```

[Screenshot: Generated PDF handout with brand styling]

### How It Works

Claude Code can reference your brand guidelines document and apply:

| Element | Brand Standard |
|---------|----------------|
| Background | Warm Cream (#F5F3EB) |
| Text | Ink Black (#000000) |
| Accents | Coral, Golden, Sage, Sky |
| Borders | 2px solid black, sharp corners |
| Fonts | IBM Plex Sans, JetBrains Mono |

> **Key Feature:** The `pdf-handout-creator` skill bundles a Python script that generates PDFs following these exact standards — every time.

### Live Demo

Using the `/pdf-handout-creator` skill:

```
/pdf-handout-creator Create a cheatsheet about Claude Code
keyboard shortcuts and essential commands
```

[Screenshot: PDF being generated and opened]

---

## Demo 3: Presentation Slides with Remark.js

For presentations, I use **Remark.js** — an open-source framework that creates HTML-based slides from markdown.

**Why Remark.js?**
- Single HTML file (no dependencies)
- Markdown-based (easy to write)
- Customizable with CSS
- Works in any browser
- Exports to PDF

**The prompt:**

```
Create a 10-slide Remark.js presentation about
"Getting Started with Claude Code" including:
- Title slide
- What is Claude Code
- Installation
- CLAUDE.md configuration
- 3 practical examples
- Best practices
- Resources

Include speaker notes and code examples.
```

[Screenshot: Remark.js slides in browser]

### How the Skill Works

The `remark-slides-skill` accepts a markdown instructions file:

```markdown
# Presentation: Getting Started with Claude Code

## Introduction
- What is Claude Code?
- Why use it for productivity?

## Installation
- npm install command
- Screenshot: ./assets/terminal-install.png

## Configuration
- CLAUDE.md system
- Reference: https://docs.anthropic.com/claude-code

## Examples
- PDF resource: ./docs/examples.pdf
```

Each line becomes an executable instruction — URLs are fetched, images are included, PDFs are processed.

[Screenshot: Sample presentation open in browser]

> **Pro Tip:** Press `p` during presentation for presenter mode with notes. Press `c` to clone the view for a second monitor.

---

# Section 3: Claude Code Skills Deep Dive

**Time: 15 minutes**

Now let's understand **how** these productivity workflows work — and how to create your own.

---

## What Are Skills?

Skills are **modular packages** that extend Claude's capabilities with:

1. **Specialized workflows** — Multi-step procedures for specific tasks
2. **Tool integrations** — Instructions for working with file formats or APIs
3. **Domain expertise** — Company-specific knowledge, schemas, business logic
4. **Bundled resources** — Scripts, references, and assets

> **Key Concept:** Skills work through **prompt expansion**. When you invoke a skill, Claude loads a markdown file (SKILL.md) that modifies how it processes your request.

As [Lee Hanchung's deep dive](https://hanchung.dev/claude-skills-deep-dive) explains:

> "Skills prepare Claude to solve a problem rather than solving it directly."

---

## Anatomy of a Skill

Every skill lives in `~/.claude/skills/` and follows this structure:

```
my-skill/
├── SKILL.md          # Required: Main instructions
├── scripts/          # Optional: Executable code
│   └── process.py
├── references/       # Optional: Documentation
│   └── api-docs.md
└── assets/           # Optional: Templates, images
    └── template.html
```

[Screenshot: Skill folder structure in Finder/VS Code]

### The SKILL.md File

This is the brain of every skill. It tells Claude:

- **What** the skill does
- **When** to use it
- **How** to execute it
- **Where** to find resources

```yaml
---
name: pdf-handout-creator
description: Create brand-aligned PDF handouts following
  Automata Learning Lab design guidelines.
---

# PDF Handout Creator Skill

## When to Use This Skill
Use this skill when the user requests:
- Creating a PDF handout or cheatsheet
- Generating a downloadable resource
- Making a quick reference guide

## How to Execute
1. Parse the user's content request
2. Structure into sections
3. Run scripts/create-handout.py
4. Open the generated PDF

## Brand Guidelines Applied
- Background: Warm Cream (#F5F3EB)
- Text: Ink Black (#000000)
- Borders: 2px solid black, sharp corners
...
```

---

## Skills vs. Commands

Claude Code offers two ways to create reusable workflows:

| Feature | Commands | Skills |
|---------|----------|--------|
| Location | `~/.claude/commands/` | `~/.claude/skills/` |
| Format | Single `.md` file | Folder with resources |
| Complexity | Simple prompts | Complex workflows |
| Resources | None | Scripts, assets, references |
| Use case | Quick shortcuts | Sophisticated workflows |

### Example Command (`~/.claude/commands/anki-cards.md`)

```markdown
Create Anki flashcards from this content.

Output format: CSV with Front, Back, Source fields.

Rules:
- Create 10-15 cards
- Use clear, concise questions
- Include source URLs
- Save to: ~/Desktop/anki_import.csv
```

Invoke with: `/anki-cards [content or URL]`

### Example Skill

The `pdf-handout-creator` skill includes:
- SKILL.md with detailed instructions
- `create-handout.py` script for PDF generation
- Brand guidelines reference
- Output file naming conventions

---

## Meta-Demo: Creating Skills with Claude

Here's where it gets meta — we'll use Claude Code to create a new skill.

**The prompt:**

```
Create a Claude Code skill called "meeting-notes-summarizer"
that takes raw meeting notes and outputs:
1. Action items with owners
2. Key decisions made
3. Follow-up questions
4. Summary paragraph

Include a Python script that formats the output as markdown.
```

[Screenshot: Claude creating the skill folder structure]

### What Claude Creates

```
meeting-notes-summarizer/
├── SKILL.md
│   ├── name: meeting-notes-summarizer
│   ├── description: ...
│   ├── When to use
│   ├── Output format
│   └── Script reference
├── scripts/
│   └── format-notes.py
└── references/
    └── output-template.md
```

### The Skill Creator Skill

For more complex skills, use the `skill-creator` skill:

```
/skill-creator I want to create a skill that generates
weekly status reports from my git commits and calendar events
```

This meta-skill guides you through:
1. Understanding the skill with concrete examples
2. Planning reusable contents
3. Initializing the skill structure
4. Editing SKILL.md
5. Packaging for distribution

> **Mind-bending:** You're using a skill to create skills. This is Claude Code's extensibility model in action.

---

## Sharing Skills

Skills can be shared as zip files:

```bash
# Package a skill for distribution
scripts/package_skill.py path/to/my-skill

# Creates: my-skill.zip
```

Recipients extract to `~/.claude/skills/` and immediately have access.

Check out [awesome-claude-skills](https://github.com/anthropics/awesome-claude-code) for community-created skills.

---

# Section 4: Practical Workflows & Wrap-up

**Time: 10 minutes**

Let's connect everything into practical workflows you can use daily.

---

## Workflow 1: The Single Note System

Inspired by [Andrej Karpathy's workflow](https://twitter.com/karpathy/status/1850943658283823104):

1. **Capture** everything in one `note.md` file
2. **Review** daily with Claude's help
3. **Extract** important items into permanent notes, flashcards, projects

```
Review my note.md file and:
1. Identify any action items I should tackle today
2. Find ideas worth converting to permanent notes
3. Suggest any redundant or outdated entries to remove
```

Claude acts as a **cognitive layer** — you do the thinking, Claude handles the organizing.

---

## Workflow 2: Research with Verifiable Citations

Combat AI hallucinations with deep-linked citations:

```
Create a research report about "best practices for React
performance optimization" using these sources:
- https://react.dev/learn/render-and-commit
- https://kentcdodds.com/blog/usememo-and-usecallback

For each claim, include a text fragment link that
jumps directly to the supporting passage.
```

The output includes links like:
```
https://react.dev/learn#:~:text=React%20only%20changes
```

When clicked, the browser scrolls to and highlights that exact text.

---

## Workflow 3: Content Creation Pipeline

From research to polished output:

```
1. Read my notes on [topic] from Obsidian
2. Create an outline for a blog post
3. Generate a presentation using remark-slides-skill
4. Create a PDF handout using pdf-handout-creator
5. Draft 3 LinkedIn post variations
```

All outputs maintain **brand consistency** because the skills reference the same guidelines.

---

## Best Practices Recap

| Practice | Why |
|----------|-----|
| Start simple | Build complexity gradually |
| Build CLAUDE.md iteratively | Add instructions as you discover patterns |
| Verify AI outputs | Use deep-linked citations |
| Create skills for repeated tasks | If you do it 3+ times, make a skill |
| Use multiple Claude instances | Keeps context clean |
| Check community skills first | Don't reinvent the wheel |

---

## Resources

### Official Documentation
- [Claude Code Documentation](https://docs.anthropic.com/en/docs/claude-code)
- [Claude Code GitHub](https://github.com/anthropics/claude-code)
- [Building Effective Agents](https://docs.anthropic.com/en/docs/agents)

### Deep Dives
- [Claude Agent Skills Deep Dive](https://hanchung.dev/claude-skills-deep-dive) — Lee Hanchung
- [Equipping Agents with Skills](https://www.anthropic.com/engineering/skills) — Anthropic Engineering

### Tools & Community
- [Remark.js](https://remarkjs.com) — Markdown presentations
- [Awesome Claude Skills](https://github.com/anthropics/awesome-claude-code) — Community skills
- [Anki](https://apps.ankiweb.net) — Spaced repetition flashcards

### Learn More
- [Introduction to Claude Code Course](https://automatalearninglab.thinkific.com) — Automata Learning Lab
- [Lucas's Newsletter](https://automata-learning-lab.kit.com) — Weekly AI insights

---

## Q&A

**Common questions:**

**Q: Is Claude Code free?**
A: Claude Code requires an Anthropic API key with usage-based pricing. There's also a Pro plan option.

**Q: Can I use it offline?**
A: No, it requires an internet connection to communicate with Claude's API.

**Q: What about sensitive data?**
A: Claude Code runs locally but sends prompts to Anthropic's API. Review their privacy policy for sensitive use cases.

**Q: How is this different from ChatGPT?**
A: Claude Code can execute actions on your machine — create files, run commands, manage your system. Chat interfaces are limited to conversation.

---

## Thank You!

**Take home:**
- `example-skills/` — Working skills to install
- `handout/claude-code-cheatsheet.pdf` — Quick reference
- `demos/` — All prompts from today

**Connect:**
- Workshop repo: [GitHub link]
- Questions: [Contact info]

---

## Appendix: Demo Prompts Reference

### Demo 1: Spreadsheet
```
Create a CSV file with sample sales data for Q1 2025.
Include columns: Date, Product, Quantity, Revenue, Region.
Generate 20 rows of realistic sample data.
Save it as sales-q1-2025.csv
```

### Demo 2: PDF Handout
```
Create a PDF cheatsheet about "5 Essential Git Commands"
Use my brand guidelines document for styling.
Make it clean, scannable, and ready to share on social media.
```

### Demo 3: Remark.js Slides
```
Create a 10-slide Remark.js presentation about
"Getting Started with Claude Code" including:
- Title slide
- What is Claude Code
- Installation
- CLAUDE.md configuration
- 3 practical examples
- Best practices
- Resources

Include speaker notes and code examples.
```

### Demo 4: Skill Creation
```
Create a Claude Code skill called "meeting-notes-summarizer"
that takes raw meeting notes and outputs:
1. Action items with owners
2. Key decisions made
3. Follow-up questions
4. Summary paragraph

Include a Python script that formats the output as markdown.
```

---

*Workshop created for Ironhack by Lucas — Automata Learning Lab*
