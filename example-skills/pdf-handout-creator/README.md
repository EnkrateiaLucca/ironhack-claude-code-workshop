# PDF Handout Creator

Create professional, brand-compliant PDF handouts and cheatsheets following Automata Learning Lab design guidelines.

## Features

- **Brand Consistency:** Automatic application of Automata Learning Lab color system, typography, and layout
- **Multiple Layouts:** Support for single/multi-column, cards, callouts, code blocks
- **Color-Coded Callouts:** Info (Sky), Success (Sage), Caution (Golden), Alert (Coral)
- **Professional Typography:** IBM Plex Sans (system fallback), JetBrains Mono for code
- **Sharp Geometric Design:** 0px border radius, 2px black borders, structured spacing
- **Warm Cream Background:** Consistent #F5F3EB canvas with white cards

## Quick Start

### Ask Claude to create a handout:

```
Create a PDF handout about Python list comprehensions with examples
```

Claude will:
1. Structure the content appropriately
2. Generate the JSON configuration
3. Run the script to create the PDF
4. Open it automatically

## Manual Usage

### 1. Create a JSON file with your content:

```json
{
  "title": "Git Commands Cheatsheet",
  "accent_color": "sky",
  "sections": [
    {
      "type": "heading",
      "level": 1,
      "content": "Essential Git Commands"
    },
    {
      "type": "paragraph",
      "content": "A quick reference guide for daily Git operations."
    },
    {
      "type": "callout",
      "callout_type": "info",
      "content": "All commands assume you're in a Git repository directory."
    },
    {
      "type": "heading",
      "level": 2,
      "content": "Basic Commands"
    },
    {
      "type": "code",
      "content": "git status\ngit add .\ngit commit -m \"message\"\ngit push"
    }
  ]
}
```

### 2. Run the script:

```bash
uv run ~/.claude/skills/pdf-handout-creator/create-handout.py content.json
```

### 3. Or pipe JSON directly:

```bash
cat content.json | uv run ~/.claude/skills/pdf-handout-creator/create-handout.py -
```

## Content Structure

### Section Types

#### 1. Heading
```json
{
  "type": "heading",
  "level": 1,  // 1 or 2
  "content": "Section Title"
}
```

#### 2. Paragraph
```json
{
  "type": "paragraph",
  "content": "Body text content",
  "bold": false  // optional
}
```

#### 3. Bullet List
```json
{
  "type": "bullet_list",
  "items": [
    "First item",
    "Second item",
    "Third item"
  ],
  "bold": false  // optional
}
```

#### 4. Numbered List
```json
{
  "type": "numbered_list",
  "items": [
    "First step",
    "Second step",
    "Third step"
  ],
  "bold": false  // optional
}
```

#### 5. Code Block
```json
{
  "type": "code",
  "content": "def hello():\n    print('Hello, World!')"
}
```

#### 6. Callout Box
```json
{
  "type": "callout",
  "callout_type": "info",  // info, success, caution, alert
  "content": "Important information for readers"
}
```

#### 7. Card (White box with border)
```json
{
  "type": "card",
  "elements": [
    ["heading", "Card Title"],
    ["text", "Card content goes here"],
    ["code", "code_example()"]
  ]
}
```

#### 8. Spacer
```json
{
  "type": "spacer",
  "size": "md"  // xs, sm, md, lg, xl
}
```

## Complete Examples

### Example 1: Technical Cheatsheet

```json
{
  "title": "Docker Commands Cheatsheet",
  "accent_color": "sky",
  "filename": "docker-cheatsheet",
  "sections": [
    {
      "type": "callout",
      "callout_type": "info",
      "content": "Quick reference for common Docker operations. Run these commands from your terminal."
    },
    {
      "type": "heading",
      "level": 1,
      "content": "Container Management"
    },
    {
      "type": "paragraph",
      "content": "List all running containers:",
      "bold": true
    },
    {
      "type": "code",
      "content": "docker ps"
    },
    {
      "type": "paragraph",
      "content": "Start a new container:",
      "bold": true
    },
    {
      "type": "code",
      "content": "docker run -d --name myapp nginx:latest"
    },
    {
      "type": "spacer",
      "size": "lg"
    },
    {
      "type": "heading",
      "level": 1,
      "content": "Image Management"
    },
    {
      "type": "bullet_list",
      "items": [
        "docker images - List all images",
        "docker pull ubuntu - Download an image",
        "docker build -t myapp . - Build from Dockerfile"
      ]
    },
    {
      "type": "callout",
      "callout_type": "caution",
      "content": "Always tag your images with version numbers in production environments."
    }
  ]
}
```

### Example 2: Learning Guide

```json
{
  "title": "5 Principles of Clean Code",
  "accent_color": "sage",
  "sections": [
    {
      "type": "paragraph",
      "content": "Writing clean, maintainable code is essential for long-term project success."
    },
    {
      "type": "heading",
      "level": 1,
      "content": "1. Use Meaningful Names"
    },
    {
      "type": "paragraph",
      "content": "Choose descriptive variable and function names that reveal intent."
    },
    {
      "type": "code",
      "content": "// Bad\nconst d = 86400;\n\n// Good\nconst SECONDS_PER_DAY = 86400;"
    },
    {
      "type": "heading",
      "level": 1,
      "content": "2. Keep Functions Small"
    },
    {
      "type": "paragraph",
      "content": "Functions should do one thing and do it well."
    },
    {
      "type": "callout",
      "callout_type": "success",
      "content": "Aim for functions that fit on one screen without scrolling."
    },
    {
      "type": "heading",
      "level": 1,
      "content": "3. Follow DRY Principle"
    },
    {
      "type": "paragraph",
      "content": "Don't Repeat Yourself - extract common logic into reusable functions."
    },
    {
      "type": "heading",
      "level": 1,
      "content": "4. Write Self-Documenting Code"
    },
    {
      "type": "paragraph",
      "content": "Code should be readable without extensive comments."
    },
    {
      "type": "heading",
      "level": 1,
      "content": "5. Handle Errors Gracefully"
    },
    {
      "type": "paragraph",
      "content": "Always validate inputs and handle edge cases."
    },
    {
      "type": "callout",
      "callout_type": "alert",
      "content": "Never ignore errors silently - log them or surface them to users."
    }
  ]
}
```

### Example 3: Social Media Companion

```json
{
  "title": "API Design Best Practices",
  "accent_color": "coral",
  "sections": [
    {
      "type": "paragraph",
      "content": "Essential principles for designing RESTful APIs that developers love."
    },
    {
      "type": "card",
      "elements": [
        ["heading", "Use Consistent Naming"],
        ["text", "Stick to plural nouns for collections and singular for items."],
        ["code", "GET /api/users\nGET /api/users/123"]
      ]
    },
    {
      "type": "card",
      "elements": [
        ["heading", "Version Your API"],
        ["text", "Include version in URL or headers to support changes without breaking clients."],
        ["code", "GET /api/v1/users\nGET /api/v2/users"]
      ]
    },
    {
      "type": "card",
      "elements": [
        ["heading", "Return Proper Status Codes"],
        ["text", "Use HTTP status codes correctly: 200 (OK), 201 (Created), 400 (Bad Request), 404 (Not Found), 500 (Server Error)"]
      ]
    },
    {
      "type": "callout",
      "callout_type": "info",
      "content": "Download the full API design guide at automatalearninglab.com"
    }
  ]
}
```

## Brand System Details

### Colors Applied

- **Background:** Warm Cream (#F5F3EB)
- **Text:** Ink Black (#000000), Gray 800 (#2A2825)
- **Borders:** 2px solid black
- **Accents:** Coral, Golden, Sage, Sky

### Typography Scale

- **Display:** 32pt Bold (titles)
- **Heading 1:** 24pt Bold (major sections)
- **Heading 2:** 18pt Semibold (subsections)
- **Body:** 11pt Regular (content)
- **Code:** 10pt Monospace (technical content)

### Spacing System

- **XS:** 4px (tight inline spacing)
- **SM:** 8px (default element spacing)
- **MD:** 16px (card padding, gaps)
- **LG:** 24px (section spacing)
- **XL:** 40px (page margins)

### Callout Types

| Type | Color | Use Case |
|------|-------|----------|
| **info** | Sky Blue | General information, tips |
| **success** | Sage Green | Confirmations, positive notes |
| **caution** | Golden Yellow | Warnings, considerations |
| **alert** | Coral | Errors, critical warnings |

## Output

### File Location
Generated PDFs are saved to: `/Users/greatmaster/Desktop/automated/`

### File Naming
Pattern: `handout-{title-slug}-{YYYYMMDD}.pdf`

Example: `handout-git-commands-20260109.pdf`

### Page Specifications
- Size: US Letter (8.5" x 11")
- Margins: 40px all sides
- Background: Warm Cream (#F5F3EB)
- Border Radius: 0px (sharp corners)

## Dependencies

- Python 3.12+
- reportlab (installed via uv)
- uv package manager

## Troubleshooting

### Fonts not rendering correctly
The script uses system fallback fonts (Helvetica, Courier). For best results:
- Install IBM Plex Sans
- Install JetBrains Mono

### PDF not opening automatically
Check that `open` command works:
```bash
open test.pdf
```

### Color issues
Ensure RGB color mode is supported by your PDF viewer.

## Integration with Claude

When using this skill through Claude:

1. Describe your content requirements
2. Claude will structure the content
3. Claude generates the JSON
4. Script creates the PDF
5. File opens automatically

Example prompt:
```
Create a cheatsheet for Python f-strings with 5 examples and tips
```

Claude handles everything end-to-end!

## Contributing

To extend the skill:
1. Add new section types to `parse_content()`
2. Create new styles in `_create_styles()`
3. Follow brand guidelines strictly
4. Test with various content types

## License

Part of Automata Learning Lab content creation toolkit.

## Version

1.0.0 - Initial release with full brand system implementation
