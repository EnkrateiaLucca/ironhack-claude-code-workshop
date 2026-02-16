# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "docling>=2.0.0",
#     "docling-core>=2.0.0",
#     "Pillow>=10.0.0",
# ]
# ///
"""
Extract PDF content using docling while preserving structure, figures, and tables.
Outputs markdown with image references and saves all images to a separate folder.
"""

import json
import logging
import sys
import time
from pathlib import Path

from docling_core.types.doc import ImageRefMode, PictureItem, TableItem
from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import PdfPipelineOptions
from docling.document_converter import DocumentConverter, PdfFormatOption

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
_log = logging.getLogger(__name__)

IMAGE_RESOLUTION_SCALE = 2.0


def extract_pdf(input_path: Path, output_dir: Path) -> dict:
    """
    Extract PDF content to markdown with images.

    Args:
        input_path: Path to the input PDF file
        output_dir: Directory to save output files

    Returns:
        Dictionary with extraction metadata
    """
    _log.info(f"Processing: {input_path}")

    # Create output directories
    output_dir.mkdir(parents=True, exist_ok=True)
    images_dir = output_dir / "images"
    images_dir.mkdir(exist_ok=True)

    # Configure pipeline for maximum image extraction
    pipeline_options = PdfPipelineOptions()
    pipeline_options.images_scale = IMAGE_RESOLUTION_SCALE
    pipeline_options.generate_page_images = True
    pipeline_options.generate_picture_images = True

    # Initialize converter
    doc_converter = DocumentConverter(
        format_options={
            InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)
        }
    )

    start_time = time.time()

    # Convert the document
    _log.info("Converting PDF with docling...")
    conv_res = doc_converter.convert(input_path)

    doc_filename = conv_res.input.file.stem
    metadata = {
        "source_file": str(input_path),
        "doc_filename": doc_filename,
        "pages": {},
        "tables": [],
        "figures": [],
        "extraction_time": 0,
    }

    # Save page images
    _log.info("Extracting page images...")
    for page_no, page in conv_res.document.pages.items():
        page_image_filename = images_dir / f"page-{page_no}.png"
        if page.image and page.image.pil_image:
            with page_image_filename.open("wb") as fp:
                page.image.pil_image.save(fp, format="PNG")
            metadata["pages"][page_no] = str(page_image_filename.relative_to(output_dir))
            _log.info(f"  Saved page {page_no}")

    # Save images of figures and tables
    _log.info("Extracting figures and tables...")
    table_counter = 0
    picture_counter = 0

    for element, _level in conv_res.document.iterate_items():
        if isinstance(element, TableItem):
            table_counter += 1
            element_image_filename = images_dir / f"table-{table_counter}.png"
            try:
                img = element.get_image(conv_res.document)
                if img:
                    with element_image_filename.open("wb") as fp:
                        img.save(fp, "PNG")
                    metadata["tables"].append({
                        "id": table_counter,
                        "image": str(element_image_filename.relative_to(output_dir)),
                    })
                    _log.info(f"  Saved table {table_counter}")
            except Exception as e:
                _log.warning(f"  Could not extract table {table_counter}: {e}")

        if isinstance(element, PictureItem):
            picture_counter += 1
            element_image_filename = images_dir / f"figure-{picture_counter}.png"
            try:
                img = element.get_image(conv_res.document)
                if img:
                    with element_image_filename.open("wb") as fp:
                        img.save(fp, "PNG")
                    metadata["figures"].append({
                        "id": picture_counter,
                        "image": str(element_image_filename.relative_to(output_dir)),
                    })
                    _log.info(f"  Saved figure {picture_counter}")
            except Exception as e:
                _log.warning(f"  Could not extract figure {picture_counter}: {e}")

    # Save markdown with referenced images (relative paths)
    _log.info("Generating markdown output...")
    md_filename = output_dir / "original.md"
    conv_res.document.save_as_markdown(md_filename, image_mode=ImageRefMode.REFERENCED)

    # Also save HTML version for reference
    html_filename = output_dir / "original.html"
    conv_res.document.save_as_html(html_filename, image_mode=ImageRefMode.REFERENCED)

    # Save embedded version as well (useful for some workflows)
    md_embedded_filename = output_dir / "original_embedded.md"
    conv_res.document.save_as_markdown(md_embedded_filename, image_mode=ImageRefMode.EMBEDDED)

    end_time = time.time() - start_time
    metadata["extraction_time"] = round(end_time, 2)

    # Save metadata
    metadata_file = output_dir / "metadata.json"
    with metadata_file.open("w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2, ensure_ascii=False)

    _log.info(f"Extraction completed in {end_time:.2f} seconds")
    _log.info(f"Output saved to: {output_dir}")
    _log.info(f"  - Pages: {len(metadata['pages'])}")
    _log.info(f"  - Tables: {len(metadata['tables'])}")
    _log.info(f"  - Figures: {len(metadata['figures'])}")

    return metadata


def main():
    if len(sys.argv) < 2:
        print("Usage: uv run extract_pdf.py <pdf-path> [output-dir]")
        print("  pdf-path: Path to the PDF file to extract")
        print("  output-dir: Optional output directory (default: ./paper-translate-output/<filename>)")
        sys.exit(1)

    input_path = Path(sys.argv[1]).resolve()

    if not input_path.exists():
        _log.error(f"File not found: {input_path}")
        sys.exit(1)

    if not input_path.suffix.lower() == ".pdf":
        _log.error(f"Not a PDF file: {input_path}")
        sys.exit(1)

    # Determine output directory
    if len(sys.argv) >= 3:
        output_dir = Path(sys.argv[2]).resolve()
    else:
        output_dir = Path.cwd() / "paper-translate-output" / input_path.stem

    try:
        metadata = extract_pdf(input_path, output_dir)
        print(f"\n{'='*60}")
        print(f"EXTRACTION COMPLETE")
        print(f"{'='*60}")
        print(f"Output directory: {output_dir}")
        print(f"Original markdown: {output_dir / 'original.md'}")
        print(f"\nNext step: Translate the content in 'original.md' and save as 'translated.md'")
    except Exception as e:
        _log.error(f"Extraction failed: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
