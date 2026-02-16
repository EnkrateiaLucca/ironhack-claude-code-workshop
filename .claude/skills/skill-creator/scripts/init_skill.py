#!/usr/bin/env python3
"""
Skill Initializer - Creates a new skill from template

Usage:
    init_skill.py <skill-name> --path <path>

Examples:
    init_skill.py my-new-skill --path ~/.claude/skills
    init_skill.py my-api-helper --path .claude/skills
"""

import sys
from pathlib import Path


SKILL_TEMPLATE = """---
name: {skill_name}
description: [TODO: What this skill does and when to use it. Be specific about scenarios, file types, or tasks that trigger it.]
---

# {skill_title}

## Overview

[TODO: 1-2 sentences explaining what this skill enables]

## When to Use

[TODO: Bullet list of trigger scenarios and phrases]

## Workflow

[TODO: Step-by-step instructions. Choose a structure:

**Workflow-Based** — sequential processes (Step 1 → Step 2 → Step 3)
**Task-Based** — different operations (Merge PDFs, Split PDFs, Extract Text)
**Reference/Guidelines** — standards or specs (Colors, Typography, Layout)
**Capabilities-Based** — interrelated features (Feature 1, Feature 2, Feature 3)

Delete this guidance block when done.]

## Examples

[TODO: 2-3 concrete examples showing user request + expected behavior]

## Resources

Delete any resource directories not needed for this skill:

- `scripts/` — Executable code (Python/Bash) for automation
- `references/` — Documentation loaded into context as needed
- `assets/` — Files used in output (templates, images, fonts)
"""

EXAMPLE_SCRIPT = '''#!/usr/bin/env python3
"""
Example helper script for {skill_name}

Replace with actual implementation or delete if not needed.
"""

def main():
    print("Example script for {skill_name}")
    # TODO: Add actual script logic here

if __name__ == "__main__":
    main()
'''

EXAMPLE_REFERENCE = """# Reference Documentation for {skill_title}

Replace with actual reference content or delete if not needed.

Reference docs are ideal for:
- API documentation
- Detailed workflow guides
- Database schemas
- Information too lengthy for SKILL.md
"""

EXAMPLE_ASSET = """# Example Asset Placeholder

Replace with actual asset files (templates, images, fonts) or delete if not needed.

Assets are NOT loaded into context — they are used within Claude's output.
"""


def title_case(name):
    return ' '.join(word.capitalize() for word in name.split('-'))


def init_skill(skill_name, path):
    skill_dir = Path(path).expanduser().resolve() / skill_name

    if skill_dir.exists():
        print(f"Error: Skill directory already exists: {skill_dir}")
        return None

    try:
        skill_dir.mkdir(parents=True, exist_ok=False)
        print(f"Created skill directory: {skill_dir}")
    except Exception as e:
        print(f"Error creating directory: {e}")
        return None

    skill_title = title_case(skill_name)

    # SKILL.md
    (skill_dir / 'SKILL.md').write_text(
        SKILL_TEMPLATE.format(skill_name=skill_name, skill_title=skill_title)
    )
    print("Created SKILL.md")

    # scripts/
    scripts_dir = skill_dir / 'scripts'
    scripts_dir.mkdir()
    script = scripts_dir / 'example.py'
    script.write_text(EXAMPLE_SCRIPT.format(skill_name=skill_name))
    script.chmod(0o755)
    print("Created scripts/example.py")

    # references/
    refs_dir = skill_dir / 'references'
    refs_dir.mkdir()
    (refs_dir / 'reference.md').write_text(
        EXAMPLE_REFERENCE.format(skill_title=skill_title)
    )
    print("Created references/reference.md")

    # assets/
    assets_dir = skill_dir / 'assets'
    assets_dir.mkdir()
    (assets_dir / 'example_asset.txt').write_text(EXAMPLE_ASSET)
    print("Created assets/example_asset.txt")

    print(f"\nSkill '{skill_name}' initialized at {skill_dir}")
    print("\nNext steps:")
    print("1. Edit SKILL.md — complete the TODO items")
    print("2. Delete unused example files in scripts/, references/, assets/")
    print("3. Test with /skill-name")

    return skill_dir


def main():
    if len(sys.argv) < 4 or sys.argv[2] != '--path':
        print("Usage: init_skill.py <skill-name> --path <path>")
        print("\nExamples:")
        print("  init_skill.py my-skill --path ~/.claude/skills")
        print("  init_skill.py my-skill --path .claude/skills")
        sys.exit(1)

    skill_name = sys.argv[1]
    path = sys.argv[3]

    print(f"Initializing skill: {skill_name}")
    print(f"Location: {path}\n")

    result = init_skill(skill_name, path)
    sys.exit(0 if result else 1)


if __name__ == "__main__":
    main()
