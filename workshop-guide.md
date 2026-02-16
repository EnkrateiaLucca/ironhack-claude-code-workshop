# Claude Code for Non-Coders: Your First AI Personal Assistant

This is it!!! Your first real taste of an **AI agent that lives on your machine**. You're here to learn how Claude Code can make you insanely productive — even if you've never written a line of code.

*— But wait, isn't Claude Code a coding tool?*

Yes. And no. Claude Code is marketed as a coding agent, but it's really a **general-purpose AI assistant** that happens to live in your terminal. It can read your files, create documents, organize your notes, build presentations, and automate workflows — all through natural language.

And y'all like "termiwhaaaat?". Yes, the terminal. That black screen with text that hackers use in movies. Except now **you're** the hacker.

Think of it this way: Claude Code is like having a brilliant intern sitting next to you, except this intern can read 200 pages in seconds, never forgets your preferences, and works at the speed of thought.

Claude Code brings in:

- **The right mental model** for working with AI agents — you stop thinking of AI as "a chatbot" and start thinking of it as "a colleague that executes"
- **Transferable skills** — prompt engineering, context management, workflow design — these apply to every AI tool you'll ever use, not just Claude Code

Sit back, relax, and enjoy your lesson!

---

# Prerequisites

Before we begin, make sure you have:

- A laptop with a terminal (macOS Terminal, Windows PowerShell/WSL, or Linux)
- Claude Code installed → [installation guide](https://docs.anthropic.com/en/docs/claude-code)
- A valid Anthropic API key or Claude Pro/Max subscription
- (Optional) An [Obsidian](https://obsidian.md/) vault or any markdown notes folder
- (Optional) [Anki](https://apps.ankiweb.net/) installed for the flashcard exercises

---

# What is Claude Code?

Claude Code is an AI assistant that runs **inside your terminal**. Unlike ChatGPT or Claude.ai (which give you text in a browser window), Claude Code can actually **do things on your machine** — create files, read your documents, run commands, organize folders, and chain complex multi-step tasks together.

You start it by typing one word:

```bash
claude
```

From there, you just talk to it:

```
"Read this PDF and summarize the key points into a markdown file"
"Create a folder structure for my new project"
"Find all notes in my vault about machine learning and summarize them"
```

Claude Code asks for your permission before executing actions. You always stay in control. (Unless you go full YOLO mode — we'll get to that later)

### Why Claude Code instead of a regular AI chat?

The key difference is **agency**. A chat gives you text. Claude Code gives you **action**.

| Regular AI Chat | Claude Code |
|---|---|
| Generates text in a browser | Executes actions on your machine |
| You copy-paste the output | Claude saves the file directly |
| One response at a time | Chains multiple steps automatically |
| Forgets everything between sessions | Remembers your preferences (CLAUDE.md) |

It reads your files, creates new ones, runs scripts, and chains multiple steps together. It turns conversation into execution.

### Quick Command Recap

| **Action** | **Command** |
| --- | --- |
| **Start Claude Code** | `claude` |
| **Start in a specific folder** | `cd ~/my-folder && claude` |
| **Check Claude Code version** | `claude --version` |

---

# CLAUDE.md — Teaching Claude About *You*

One of Claude Code's most powerful features is the **CLAUDE.md** file. Think of it as Claude's **persistent memory** — a place where you store instructions that Claude should always remember, no matter what you're working on.

### Global CLAUDE.md

Create a file at `~/.claude/CLAUDE.md` (the global config). This applies **every time** you open Claude Code, regardless of which folder you're in.

Here's a real example:

```markdown
# About Me
- My name is Lucas
- I'm an AI Engineer based in Lisbon
- I teach courses on AI agents and prompt engineering

# My File System
- My Obsidian vault: ~/Documents/obsidian-vault/
- My Anki database: ~/Library/Application Support/Anki2/
- My automations folder: ~/automations/

# Preferences
- Always write in clear, concise language
- Use markdown formatting for notes
- When creating files, use descriptive filenames with dates
```

Now, whenever you say *"save this note to my vault"*, Claude already knows where your vault is. No need to repeat yourself. Ever.

### Project-Specific CLAUDE.md

You can also create a `CLAUDE.md` in any folder. These **local configs** extend or override the global settings. This is perfect for project-specific instructions:

```markdown
# Project: IronHack Workshop
- All output files go in ./output/
- Use Portuguese for any student-facing materials
- Brand colors: #FF6B35 (orange), #1A1A2E (dark blue)
```

**The takeaway:** CLAUDE.md is how you train Claude about your personal ecosystem. The more you invest in it, the less you repeat yourself and the smarter Claude becomes about *your* world.

---

# Quick Example: Your First Task

All right, let's get our hands dirty.

Open Claude Code in any folder and try this:

```
Create a markdown file called "meeting-notes.md" with today's date
as the title, sections for Attendees, Agenda, Discussion, and
Action Items. Save it in the current folder.
```

Claude will:
1. Generate the file with proper structure
2. Ask for your permission to create it
3. Save it exactly where you told it to

That's it. You just used an AI agent to create a structured document in seconds. Now imagine scaling that to hundreds of notes, research reports, and presentations.

Try another one:

```
Fetch the contents of this URL: https://arxiv.org/abs/2503.10622
and create a summary note with the key findings.
```

Claude Code will fetch the content, process it, and create the file — all while asking for your permission before taking actions.

---

# Managing Context — The Most Important Concept

This is the section that will **make or break** your experience with Claude Code (and honestly, with any AI tool). **Context management** is what separates someone who gets mediocre results from someone who gets incredible ones.

Even experienced developers get this wrong. So pay attention — this is your superpower.

## What Are Tokens and the Context Window?

Every AI model works with **tokens** — small chunks of text (roughly 3/4 of a word). When you chat with Claude Code, **everything** takes up tokens:

- Your messages → tokens
- Claude's responses → tokens
- Files Claude reads → tokens
- The CLAUDE.md file → tokens
- Previous conversation history → tokens

All of this lives inside a **context window** — think of it as Claude's short-term working memory. Claude has a large context window (around 200K tokens), but it's **not infinite**. Once the window fills up, older information starts getting pushed out, and Claude's performance degrades.

### The Desk Analogy

Imagine your desk. You can spread out papers, books, and notes — but the desk has a fixed size. If you pile too much on it, things fall off the edges, and you can't find what you need anymore.

That's the context window. And **you** are responsible for what goes on that desk.

```
┌─────────────────────────────────────────────┐
│           CONTEXT WINDOW (~200K tokens)       │
│                                               │
│  ┌──────────┐ ┌──────────┐ ┌──────────────┐ │
│  │ CLAUDE.md│ │ Your     │ │ Claude's     │ │
│  │ config   │ │ messages │ │ responses    │ │
│  └──────────┘ └──────────┘ └──────────────┘ │
│  ┌──────────┐ ┌──────────┐                   │
│  │ Files    │ │ Convo    │  ← stuff falls   │
│  │ read     │ │ history  │    off here!     │
│  └──────────┘ └──────────┘                   │
└─────────────────────────────────────────────┘
```

### Why This Matters for You

Every task you give Claude Code has a **context cost**. When you say *"read all the files in my vault"*, Claude is loading potentially thousands of tokens into its working memory. If you then ask it to also write a report, create flashcards, AND organize your calendar — all in the same session — you're stacking context on top of context.

The result? Claude starts "forgetting" things from earlier in the conversation. Its responses get less precise. It might hallucinate or contradict earlier statements.

### Context Management Commands

| **Action** | **Command** |
| --- | --- |
| **Check context usage** | `/cost` |
| **Clear conversation** | `/clear` |
| **Compact context** | `/compact` |
| **Start fresh session** | Exit and run `claude` again |

## How to Think About Context When Instructing an Agent

Here's the key mental model: **every instruction you give has a context footprint**. Your job is to be intentional about what goes into Claude's working memory.

Think of each task as a **weight** you're placing on the desk. Some tasks are light (a quick question), some are heavy (reading 50 files). You need to plan your desk space.

### Bad: Context-Wasteful Prompting

```
Read all 200 notes in my vault, then find the ones about machine
learning, then summarize them, then create flashcards from the
summaries, then organize the flashcards by difficulty.
```

This is asking Claude to hold everything in memory at once. By the time it gets to creating flashcards, it's already forgotten details from the first notes it read. It's like asking someone to hold 200 papers in their hands while also writing a report. Things *will* fall.

### Good: Context-Aware Prompting

Break it into focused sessions:

**Session 1: Scout**
```
Search my vault for notes related to machine learning.
List just the filenames and a one-line summary of each.
```

**Session 2: Process**
```
Read these 5 specific notes: [list from session 1].
Create a summary document and save it as ml-summary.md.
```

**Session 3: Create**
```
Based on the file ml-summary.md, create 10 Anki flashcards.
```

Each session gets a fresh, focused context. The **output of one session becomes the clean input for the next**. Files are the bridge between sessions — not conversation history.

## Compressing Instructions Through Smart Prompting

One of the most powerful techniques is **instruction compression** — getting more done with fewer tokens. This is what separates a good AI user from a great one.

### 1. Front-Load Context in CLAUDE.md

Instead of explaining your preferences every time, put them in CLAUDE.md **once**:

```markdown
# Note Format
- Always use H2 headers for sections
- Include a "Source" field at the bottom
- Use ISO dates (YYYY-MM-DD)
- Tags go at the top in YAML frontmatter
```

Now instead of a 50-word instruction, you just say: *"Create a note about transformers."* Claude already knows your format. You just saved 40+ tokens.

### 2. Use Reference Files Instead of Inline Instructions

Instead of pasting a long style guide into your prompt:

```
Read the file ./brand-guidelines.md and follow those rules
when creating the PDF handout.
```

The file is loaded once. Much more efficient than repeating rules in every single prompt.

### 3. Create Commands for Repeated Patterns

If you find yourself writing the same type of instruction over and over, compress it into a **custom command**:

```
/anki-cards https://some-article-url.com
```

One line replaces a paragraph of instructions. We'll cover how to build these soon.

### 4. Be Specific, Not Exhaustive

```
# Bad — Wasteful (47 tokens)
"I want you to create a note. The note should be in markdown.
It should have a title. The title should be descriptive.
It should have sections. The sections should be..."

# Good — Compressed (12 tokens)
"Create a markdown note following my vault format about [topic]."
```

Claude already knows your format from CLAUDE.md. **Trust the configuration.**

## The Golden Rule of Context

**One task, one session, one focus.**

If you're doing research → fresh session for research.
If you're creating flashcards → fresh session for flashcards.
If you're organizing notes → fresh session for organizing.

Connect them through **files**, not through conversation history. This is the single most important thing you'll learn today.

---

# Skills, Workflows & Examples

Now let's get to the fun stuff.

## What Are Skills?

Claude Skills are **reusable instruction packages** — organized folders of instructions, scripts, and resources that Claude can load dynamically. Think of them as **recipes** that Claude follows to produce consistent, high-quality results.

Unlike regular prompts, skills work through **prompt expansion**: when you invoke a skill, Claude loads a markdown file (SKILL.md), expands it into detailed instructions, and uses those to guide its work. Skills prepare Claude to solve a problem rather than solving it directly.

### Anatomy of a Skill

```
my-skill/
├── SKILL.md          ← the "recipe" (main instructions)
├── scripts/          ← executable scripts, if needed
├── references/       ← example outputs, documentation
└── assets/           ← templates, images, supporting files
```

The SKILL.md file tells Claude:
- **What** the skill does
- **When** to use it
- **How** to execute it
- **What format** to use for output
- **Which tools** to employ

### Example: Anki Card Creator Skill

```markdown
# Anki Card Creator Skill

## Purpose
Create Anki flashcards from content and save to the Anki database.

## When to Use
- When the user asks to create flashcards
- When reviewing notes that should be memorized

## Output Format
CSV format with fields: Front, Back, Source

## Execution
Run the bundled Python script: scripts/createankicards.py

## Database Location
/Users/user/Library/Application Support/Anki2/User 1/collection.anki2
```

## What Are Custom Commands?

Commands are simpler than skills — they're **prompt templates** that you invoke with `/command-name`. Think of them as keyboard shortcuts for your most common instructions.

You save them as `.md` files in `.claude/commands/`:

```markdown
# /anki-cards

Create Anki flashcards from this content.

Output format: CSV with Front, Back, Source fields.

Rules:
- Create 10-15 cards
- Use clear, concise questions
- Include source URLs or file paths
- Save to: ~/Desktop/anki_import.csv
```

Now you just type `/anki-cards [URL or content]` and it works. Every single time.

### Skills vs. Commands

| | **Commands** | **Skills** |
|---|---|---|
| **Complexity** | Simple prompt templates | Multi-file workflows with scripts |
| **Use case** | Quick, repeatable tasks | Sophisticated, deterministic workflows |
| **Setup** | One markdown file | Folder with SKILL.md + assets |
| **Example** | `/anki-cards` | Research report generator with citations |

---

# Live Demo: Translate a Paper

Let's see Claude Code in action with a real-world task. We'll take a research paper (PDF) and ask Claude to translate and summarize it.

```
Read the PDF file ./paper.pdf. Create a translated summary
in Portuguese with the key findings, methodology, and conclusions.
Save it as ./paper-summary-pt.md
```

Claude will:
1. Read the PDF content
2. Extract the key sections
3. Translate to Portuguese
4. Structure it as a clean markdown document
5. Save the file

This is the kind of task that would take a human 30-60 minutes. Claude does it in under a minute. And you didn't write a single line of code.

---

# Meta: Using Claude to Create Skills (The Skill Creator)

Here's where it gets meta (and magical): **you can ask Claude Code to create skills for itself**.

```
Create a skill that takes a PDF research paper, extracts the key
findings, translates them to Portuguese, and saves the output as
a structured markdown file. Put the skill in .claude/skills/translate-paper/
```

Claude will:
1. Create the skill folder structure
2. Write the SKILL.md with detailed instructions
3. Create any helper scripts if needed
4. Install it so you can use it immediately

You just created a reusable automation without writing any code. Next time, you just invoke the skill instead of explaining the whole workflow again.

That's the meta-level magic: **the agent builds its own tools**.

---

# Anki Flashcard Skills — Study, Learn, Memorize

One of the most brilliant use cases: turning **any** content into spaced-repetition flashcards.

### From Notes to Flashcards

```
Read my notes about prompt engineering in my vault.
Create 10 Anki flashcards and save them as a CSV file
I can import into Anki.
```

### From Web Articles to Flashcards

Using a custom command:

```
/anki-cards https://some-great-article.com/about-ai-agents
```

Claude fetches the article, extracts the key concepts, generates well-structured Q&A flashcards, and saves them ready for import.

### From Research Papers to Flashcards

```
Read ./paper.pdf and create flashcards focusing on the
methodology and key findings. Include page references.
```

**Important caveat:** Creating flashcards automatically is convenient, but for deep learning, you should still read the source material and engage with it critically. Claude Code accelerates the process — it doesn't replace the thinking.

---

# Skills Unlock Automation for Non-Devs

This is the paradigm shift. Traditionally, automation required programming — Python scripts, cron jobs, API configurations. With Claude Code skills:

- **No code required** — skills are written in markdown (plain English instructions)
- **No setup overhead** — Claude handles file operations, API calls, and data processing
- **No maintenance burden** — update the SKILL.md file and the workflow updates

| **Traditional Automation** | **Claude Code Skills** |
|---|---|
| Write a Python script | Write a paragraph in English |
| Debug the code | Refine the instructions |
| Install dependencies | Claude handles it |
| Set up a scheduler | Invoke the skill when needed |
| Maintain the codebase | Update the SKILL.md |

This is like the difference between learning to cook from scratch vs. having a chef who follows your recipe. You still design the meal — you just don't have to chop the onions anymore.

---

# The Compound Effect — No Technical Ability Required

Let's zoom out and see the full picture of what we covered:

1. **Claude Code** → An AI agent on your machine
2. **CLAUDE.md** → Persistent memory and preferences
3. **Context management** → Smart, focused prompting
4. **Skills & commands** → Reusable automation packages
5. **Real workflows** → Translation, flashcards, research

Each of these individually is useful. Together, they **compound** into something much bigger.

**The compound effect is real.** Every skill you create saves you time *every single time you use it*. Build 10 skills, and you've automated 10 recurring workflows. Build 50, and you've essentially created a **personal operating system** powered by AI — and you never wrote a line of code.

The workflows we covered barely scratch the surface:

- Note-taking systems become dynamic knowledge graphs
- Flashcard creation goes from tedious to instant
- Research becomes verifiable with deep-linked citations
- Content creation maintains brand consistency
- Workflows crystallize into reusable skills

---

# Claude Code: Your First Taste of a True General Personal Assistant

Claude Code is not just a tool. It's a **cognitive layer** between you and your work:

- **You do the thinking**: reading, reflecting, deciding what's important
- **Claude handles the operations**: creating files, organizing, connecting, formatting
- **You verify and iterate**: checking outputs, refining workflows

It's not about AI replacing thought — it's about **removing friction** from knowledge work so you can focus on the high-value cognitive tasks: understanding, synthesizing, and creating.

The future of productivity isn't about learning to code. It's about learning to **instruct, configure, and orchestrate** AI agents. And that's exactly what you just did today.

---

# Full Command Reference

| **Action** | **Command** |
| --- | --- |
| **Start Claude Code** | `claude` |
| **Check context/cost** | `/cost` |
| **Clear conversation** | `/clear` |
| **Compact context** | `/compact` |
| **Run a custom command** | `/command-name` |
| **Check version** | `claude --version` |
| **Start fresh session** | Exit + `claude` |

---

# Resources

- [Claude Code Official Docs](https://docs.anthropic.com/en/docs/claude-code)
- [Anthropic: Building Effective Agents](https://www.anthropic.com/research/building-effective-agents)
- [Automata Learning Lab — Claude Code Course](https://automatalearninglab.thinkific.com)
- [Anki — Spaced Repetition Flashcards](https://apps.ankiweb.net/)
- [Obsidian — Markdown Note-Taking](https://obsidian.md/)
- [Awesome Claude Skills](https://github.com/anthropics/awesome-claude-code) — Community-curated collection

---

*In under 60 minutes*, you learned how to set up and configure an AI agent, manage its context like a pro, and create reusable automations — all without writing a single line of code.

The skills you develop today — prompt engineering, context management, workflow design — will serve you well as these tools continue to evolve. This is what being "AI-native" looks like.

Now go build your first skill.

---

*Ironhack Workshop — Automata Learning Lab*
