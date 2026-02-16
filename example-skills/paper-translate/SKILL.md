---
name: paper-translate
description: Translate academic papers from PDF while preserving structure, figures, tables, and formatting. Use when translating research papers, academic documents, or technical PDFs to another language.
argument-hint: <pdf-path> [target-language]
allowed-tools: Bash(python *), Bash(uv *), Read, Write, Edit
---

# Paper Translation Skill

Translate academic papers from PDF format while preserving the original document structure, figures, tables, and formatting as accurately as possible.

## Workflow Overview

1. **Extract**: Use docling to extract PDF content preserving structure
2. **Translate**: Translate text content while preserving markdown structure and image references
3. **Output**: Generate translated markdown with embedded images

## Step 1: Extract PDF Content

Run the extraction script to convert the PDF to structured markdown with images:

```bash
uv run ~/.claude/skills/paper-translate/scripts/extract_pdf.py "$0"
```

This creates an output directory with:
- `original.md` - Extracted markdown with structure preserved
- `images/` - Extracted figures, tables, and page images
- `metadata.json` - Document metadata and structure info

## Step 2: Translate the Content

After extraction, you must translate the content yourself by:

1. Read the extracted `original.md` file
2. Translate ALL text content to the target language (default: English, or use `$1` if specified)
3. **CRITICAL**: Preserve the exact markdown structure:
   - Keep all `![image](...)` references unchanged
   - Keep all heading levels (`#`, `##`, etc.)
   - Keep all table formatting (`|...|...|`)
   - Keep all code blocks and formatting markers
   - Only translate the actual text content

### Translation Guidelines

- Translate section headings while keeping hierarchy
- Translate figure/table captions
- Translate all body text paragraphs
- Translate table cell contents
- Keep mathematical notation, formulas, and equations intact
- Keep author names, affiliations, and references as-is (transliterate if needed)
- Maintain academic tone and technical terminology accuracy

## Step 3: Save Translated Output

Save the translated content to `translated.md` in the same output directory.

Then run the finalization script to create the final HTML output with embedded images:

```bash
uv run ~/.claude/skills/paper-translate/scripts/finalize_output.py "<output-dir>"
```

This generates:
- `translated.html` - Final HTML with embedded images and proper styling
- `translated_standalone.md` - Markdown with base64 embedded images

## Output Location

All output files are saved to: `./paper-translate-output/<pdf-filename>/`

## Example Usage

```
/paper-translate ./research-paper.pdf
/paper-translate ./russian-paper.pdf English
/paper-translate ./german-study.pdf Spanish
```

## Dependencies

The scripts require these Python packages (handled by uv inline metadata):
- docling
- docling-core
- Pillow

## Notes

- Complex mathematical formulas may need manual verification
- Some figure text embedded in images cannot be translated
- Tables with merged cells may have formatting variations
- Right-to-left languages may need additional formatting adjustments
