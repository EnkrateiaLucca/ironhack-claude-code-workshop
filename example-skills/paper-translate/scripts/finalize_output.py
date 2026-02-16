# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "markdown>=3.5.0",
#     "Pillow>=10.0.0",
# ]
# ///
"""
Finalize translated paper output by generating HTML with embedded images
and proper academic paper styling.
"""

import base64
import json
import logging
import re
import sys
from pathlib import Path

try:
    import markdown
except ImportError:
    markdown = None

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
_log = logging.getLogger(__name__)


def image_to_base64(image_path: Path) -> str:
    """Convert an image file to base64 data URI."""
    if not image_path.exists():
        _log.warning(f"Image not found: {image_path}")
        return ""

    suffix = image_path.suffix.lower()
    mime_types = {
        ".png": "image/png",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".gif": "image/gif",
        ".webp": "image/webp",
    }
    mime_type = mime_types.get(suffix, "image/png")

    with image_path.open("rb") as f:
        data = base64.b64encode(f.read()).decode("utf-8")

    return f"data:{mime_type};base64,{data}"


def embed_images_in_markdown(md_content: str, base_dir: Path) -> str:
    """Replace image references with base64 embedded images."""
    # Pattern to match markdown image syntax: ![alt](path)
    pattern = r"!\[([^\]]*)\]\(([^)]+)\)"

    def replace_image(match):
        alt_text = match.group(1)
        image_path = match.group(2)

        # Skip already embedded images (data URIs)
        if image_path.startswith("data:"):
            return match.group(0)

        # Resolve the image path relative to base directory
        full_path = base_dir / image_path
        if not full_path.exists():
            # Try without leading ./
            full_path = base_dir / image_path.lstrip("./")

        if full_path.exists():
            data_uri = image_to_base64(full_path)
            if data_uri:
                return f"![{alt_text}]({data_uri})"

        _log.warning(f"Could not embed image: {image_path}")
        return match.group(0)

    return re.sub(pattern, replace_image, md_content)


def generate_html(md_content: str, title: str = "Translated Paper") -> str:
    """Generate styled HTML from markdown content."""
    # Convert markdown to HTML
    if markdown:
        html_body = markdown.markdown(
            md_content,
            extensions=["tables", "fenced_code", "toc"]
        )
    else:
        # Basic fallback if markdown package not available
        html_body = f"<pre>{md_content}</pre>"

    html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        :root {{
            --primary-color: #2c3e50;
            --text-color: #333;
            --bg-color: #fafafa;
            --paper-bg: #fff;
            --border-color: #e0e0e0;
            --code-bg: #f5f5f5;
        }}

        * {{
            box-sizing: border-box;
        }}

        body {{
            font-family: 'Times New Roman', Times, Georgia, serif;
            font-size: 12pt;
            line-height: 1.6;
            color: var(--text-color);
            background-color: var(--bg-color);
            margin: 0;
            padding: 20px;
        }}

        .paper {{
            max-width: 8.5in;
            margin: 0 auto;
            background: var(--paper-bg);
            padding: 1in;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}

        h1 {{
            font-size: 18pt;
            text-align: center;
            margin-bottom: 0.5em;
            color: var(--primary-color);
        }}

        h2 {{
            font-size: 14pt;
            margin-top: 1.5em;
            margin-bottom: 0.5em;
            color: var(--primary-color);
            border-bottom: 1px solid var(--border-color);
            padding-bottom: 0.3em;
        }}

        h3 {{
            font-size: 12pt;
            margin-top: 1.2em;
            margin-bottom: 0.4em;
            color: var(--primary-color);
        }}

        h4, h5, h6 {{
            font-size: 11pt;
            margin-top: 1em;
            margin-bottom: 0.3em;
        }}

        p {{
            margin: 0.8em 0;
            text-align: justify;
        }}

        img {{
            max-width: 100%;
            height: auto;
            display: block;
            margin: 1em auto;
            border: 1px solid var(--border-color);
        }}

        figure {{
            margin: 1.5em 0;
            text-align: center;
        }}

        figcaption {{
            font-size: 10pt;
            color: #666;
            margin-top: 0.5em;
            font-style: italic;
        }}

        table {{
            border-collapse: collapse;
            width: 100%;
            margin: 1em 0;
            font-size: 10pt;
        }}

        th, td {{
            border: 1px solid var(--border-color);
            padding: 8px 12px;
            text-align: left;
        }}

        th {{
            background-color: #f0f0f0;
            font-weight: bold;
        }}

        tr:nth-child(even) {{
            background-color: #f9f9f9;
        }}

        code {{
            font-family: 'Courier New', Courier, monospace;
            font-size: 10pt;
            background-color: var(--code-bg);
            padding: 2px 6px;
            border-radius: 3px;
        }}

        pre {{
            background-color: var(--code-bg);
            padding: 1em;
            overflow-x: auto;
            border-radius: 5px;
            border: 1px solid var(--border-color);
        }}

        pre code {{
            padding: 0;
            background: none;
        }}

        blockquote {{
            margin: 1em 0;
            padding: 0.5em 1em;
            border-left: 4px solid var(--primary-color);
            background-color: #f9f9f9;
            font-style: italic;
        }}

        ul, ol {{
            margin: 0.8em 0;
            padding-left: 2em;
        }}

        li {{
            margin: 0.3em 0;
        }}

        a {{
            color: #0066cc;
            text-decoration: none;
        }}

        a:hover {{
            text-decoration: underline;
        }}

        .abstract {{
            margin: 1.5em 2em;
            padding: 1em;
            background-color: #f9f9f9;
            border-left: 3px solid var(--primary-color);
            font-style: italic;
        }}

        .references {{
            font-size: 10pt;
        }}

        hr {{
            border: none;
            border-top: 1px solid var(--border-color);
            margin: 2em 0;
        }}

        @media print {{
            body {{
                background: none;
                padding: 0;
            }}
            .paper {{
                box-shadow: none;
                padding: 0;
            }}
        }}

        @media (max-width: 768px) {{
            body {{
                padding: 10px;
            }}
            .paper {{
                padding: 0.5in;
            }}
        }}
    </style>
</head>
<body>
    <article class="paper">
        {html_body}
    </article>
</body>
</html>"""

    return html_template


def finalize_output(output_dir: Path) -> None:
    """Generate final HTML and standalone markdown outputs."""
    translated_md = output_dir / "translated.md"

    if not translated_md.exists():
        _log.error(f"Translated markdown not found: {translated_md}")
        _log.error("Please translate 'original.md' and save as 'translated.md' first.")
        sys.exit(1)

    # Read translated content
    md_content = translated_md.read_text(encoding="utf-8")

    # Load metadata for title
    metadata_file = output_dir / "metadata.json"
    if metadata_file.exists():
        with metadata_file.open("r", encoding="utf-8") as f:
            metadata = json.load(f)
        title = f"Translated: {metadata.get('doc_filename', 'Paper')}"
    else:
        title = "Translated Paper"

    # Generate standalone markdown with embedded images
    _log.info("Creating standalone markdown with embedded images...")
    embedded_md = embed_images_in_markdown(md_content, output_dir)
    standalone_md_file = output_dir / "translated_standalone.md"
    standalone_md_file.write_text(embedded_md, encoding="utf-8")
    _log.info(f"Saved: {standalone_md_file}")

    # Generate HTML output
    _log.info("Generating HTML output...")
    html_content = generate_html(embedded_md, title)
    html_file = output_dir / "translated.html"
    html_file.write_text(html_content, encoding="utf-8")
    _log.info(f"Saved: {html_file}")

    print(f"\n{'='*60}")
    print("FINALIZATION COMPLETE")
    print(f"{'='*60}")
    print(f"HTML output: {html_file}")
    print(f"Standalone MD: {standalone_md_file}")
    print(f"\nOpen the HTML file in a browser to view the translated paper.")


def main():
    if len(sys.argv) < 2:
        print("Usage: uv run finalize_output.py <output-dir>")
        print("  output-dir: Directory containing translated.md")
        sys.exit(1)

    output_dir = Path(sys.argv[1]).resolve()

    if not output_dir.exists():
        _log.error(f"Directory not found: {output_dir}")
        sys.exit(1)

    finalize_output(output_dir)


if __name__ == "__main__":
    main()
