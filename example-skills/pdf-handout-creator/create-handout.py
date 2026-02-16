#!/usr/bin/env python3
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "reportlab",
# ]
# ///

"""
PDF Handout Creator - Automata Learning Lab Brand System
Generates brand-compliant PDF handouts and cheatsheets
"""

import sys
import json
import subprocess
from pathlib import Path
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, KeepTogether, Frame, PageTemplate
)
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
# TTFont import commented out - not needed for system fonts
# from reportlab.pdfbase.ttfont import TTFont


# ============================================================================
# AUTOMATA LEARNING LAB BRAND SYSTEM
# ============================================================================

class BrandColors:
    """Automata Learning Lab Color System"""
    # Primary Colors
    INK_BLACK = colors.HexColor('#000000')
    WARM_CREAM = colors.HexColor('#F5F3EB')

    # Accent Colors
    CORAL = colors.HexColor('#E86B5A')
    GOLDEN = colors.HexColor('#F5C542')
    SAGE = colors.HexColor('#7CB56B')
    SKY = colors.HexColor('#5B9BD5')

    # Tints & Backgrounds
    CORAL_LIGHT = colors.HexColor('#FBEAE7')
    GOLDEN_LIGHT = colors.HexColor('#FEF8E6')
    SAGE_LIGHT = colors.HexColor('#EEF5EC')
    SKY_LIGHT = colors.HexColor('#E8F1F9')

    # Neutral Grays
    GRAY_100 = colors.HexColor('#F5F4F1')
    GRAY_300 = colors.HexColor('#DDD9D2')
    GRAY_500 = colors.HexColor('#8A847A')
    GRAY_600 = colors.HexColor('#5C5750')
    GRAY_800 = colors.HexColor('#2A2825')

    # White for cards
    WHITE = colors.HexColor('#FFFFFF')


class BrandSpacing:
    """Spacing Scale - space-xs to space-xl"""
    XS = 4
    SM = 8
    MD = 16
    LG = 24
    XL = 40


class BrandFonts:
    """Typography System"""
    # Font families (fallback to system fonts)
    PRIMARY = 'Helvetica'  # Fallback for IBM Plex Sans
    PRIMARY_BOLD = 'Helvetica-Bold'
    MONO = 'Courier'  # Fallback for JetBrains Mono

    # Type Scale (in points)
    DISPLAY = 32
    HEADING_1 = 24
    HEADING_2 = 18
    BODY = 11
    CAPTION = 9


# ============================================================================
# PDF GENERATOR
# ============================================================================

class HandoutGenerator:
    """Generate brand-compliant PDF handouts"""

    def __init__(self, output_dir=None):
        self.output_dir = Path(output_dir or "/Users/greatmaster/Desktop/automated")
        self.output_dir.mkdir(parents=True, exist_ok=True)

        # Page setup
        self.page_width, self.page_height = letter
        self.margin = BrandSpacing.XL
        self.content_width = self.page_width - (2 * self.margin)

        # Story elements
        self.story = []

        # Styles
        self.styles = self._create_styles()

    def _create_styles(self):
        """Create paragraph styles following brand typography"""
        styles = {}

        # Display style (32pt Bold)
        styles['Display'] = ParagraphStyle(
            'Display',
            fontName=BrandFonts.PRIMARY_BOLD,
            fontSize=BrandFonts.DISPLAY,
            textColor=BrandColors.INK_BLACK,
            leading=BrandFonts.DISPLAY * 1.2,
            spaceAfter=BrandSpacing.LG,
            alignment=TA_CENTER
        )

        # Heading 1 (24pt Bold)
        styles['Heading1'] = ParagraphStyle(
            'Heading1',
            fontName=BrandFonts.PRIMARY_BOLD,
            fontSize=BrandFonts.HEADING_1,
            textColor=BrandColors.INK_BLACK,
            leading=BrandFonts.HEADING_1 * 1.3,
            spaceAfter=BrandSpacing.MD,
            spaceBefore=BrandSpacing.LG
        )

        # Heading 2 (18pt Semibold)
        styles['Heading2'] = ParagraphStyle(
            'Heading2',
            fontName=BrandFonts.PRIMARY_BOLD,
            fontSize=BrandFonts.HEADING_2,
            textColor=BrandColors.INK_BLACK,
            leading=BrandFonts.HEADING_2 * 1.4,
            spaceAfter=BrandSpacing.SM,
            spaceBefore=BrandSpacing.MD
        )

        # Body text (11pt Regular)
        styles['Body'] = ParagraphStyle(
            'Body',
            fontName=BrandFonts.PRIMARY,
            fontSize=BrandFonts.BODY,
            textColor=BrandColors.GRAY_800,
            leading=BrandFonts.BODY * 1.6,
            spaceAfter=BrandSpacing.SM
        )

        # Body bold for emphasis
        styles['BodyBold'] = ParagraphStyle(
            'BodyBold',
            fontName=BrandFonts.PRIMARY_BOLD,
            fontSize=BrandFonts.BODY,
            textColor=BrandColors.INK_BLACK,
            leading=BrandFonts.BODY * 1.6,
            spaceAfter=BrandSpacing.SM
        )

        # Monospace for code/technical content
        styles['Mono'] = ParagraphStyle(
            'Mono',
            fontName=BrandFonts.MONO,
            fontSize=BrandFonts.BODY - 1,
            textColor=BrandColors.GRAY_800,
            leading=(BrandFonts.BODY - 1) * 1.5,
            spaceAfter=BrandSpacing.SM,
            leftIndent=BrandSpacing.MD,
            backColor=BrandColors.GRAY_100
        )

        # Caption/Label (9pt Medium)
        styles['Caption'] = ParagraphStyle(
            'Caption',
            fontName=BrandFonts.PRIMARY,
            fontSize=BrandFonts.CAPTION,
            textColor=BrandColors.GRAY_600,
            leading=BrandFonts.CAPTION * 1.4,
            spaceAfter=BrandSpacing.XS
        )

        return styles

    def add_title(self, title, accent_color=None):
        """Add main title with optional accent underline"""
        # Add title
        self.story.append(Spacer(1, BrandSpacing.SM))
        self.story.append(Paragraph(title, self.styles['Display']))

        # Optional accent underline
        if accent_color:
            accent = getattr(BrandColors, accent_color.upper(), BrandColors.CORAL)
            underline_width = self.content_width * 0.3
            underline_data = [['']]
            underline_table = Table(underline_data, colWidths=[underline_width])
            underline_table.setStyle(TableStyle([
                ('LINEABOVE', (0, 0), (-1, -1), 4, accent),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ]))
            self.story.append(underline_table)

        self.story.append(Spacer(1, BrandSpacing.MD))

    def add_heading(self, text, level=1):
        """Add section heading"""
        style = 'Heading1' if level == 1 else 'Heading2'
        self.story.append(Paragraph(text, self.styles[style]))

    def add_paragraph(self, text, bold=False):
        """Add body paragraph"""
        style = 'BodyBold' if bold else 'Body'
        self.story.append(Paragraph(text, self.styles[style]))

    def add_code_block(self, code):
        """Add code/technical content block"""
        # Escape HTML characters
        code = code.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        lines = code.split('\n')

        for line in lines:
            self.story.append(Paragraph(line or ' ', self.styles['Mono']))

    def add_callout(self, text, callout_type='info'):
        """
        Add colored callout box
        Types: info (sky), success (sage), caution (golden), alert (coral)
        """
        # Map callout types to colors
        callout_colors = {
            'info': (BrandColors.SKY_LIGHT, BrandColors.SKY, 'INFORMATION'),
            'success': (BrandColors.SAGE_LIGHT, BrandColors.SAGE, 'SUCCESS'),
            'caution': (BrandColors.GOLDEN_LIGHT, BrandColors.GOLDEN, 'CAUTION'),
            'alert': (BrandColors.CORAL_LIGHT, BrandColors.CORAL, 'ALERT')
        }

        bg_color, border_color, label = callout_colors.get(
            callout_type.lower(),
            callout_colors['info']
        )

        # Create callout content
        label_para = Paragraph(
            f"<b>{label}</b>",
            self.styles['Caption']
        )
        text_para = Paragraph(text, self.styles['Body'])

        # Create table for callout box
        data = [[label_para], [text_para]]
        table = Table(data, colWidths=[self.content_width - (BrandSpacing.MD * 2)])
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), bg_color),
            ('LEFTPADDING', (0, 0), (-1, -1), BrandSpacing.MD),
            ('RIGHTPADDING', (0, 0), (-1, -1), BrandSpacing.MD),
            ('TOPPADDING', (0, 0), (-1, -1), BrandSpacing.SM),
            ('BOTTOMPADDING', (0, 0), (-1, -1), BrandSpacing.SM),
            ('LINEABOVE', (0, 0), (-1, 0), 4, border_color),  # 4px accent border
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ]))

        self.story.append(table)
        self.story.append(Spacer(1, BrandSpacing.MD))

    def add_card(self, content_elements):
        """
        Add white card with 2px black border
        content_elements: list of (type, content) tuples
        """
        card_story = []

        for elem_type, elem_content in content_elements:
            if elem_type == 'heading':
                card_story.append(Paragraph(elem_content, self.styles['Heading2']))
            elif elem_type == 'text':
                card_story.append(Paragraph(elem_content, self.styles['Body']))
            elif elem_type == 'code':
                self.add_code_block(elem_content)

            card_story.append(Spacer(1, BrandSpacing.SM))

        # Create card table
        data = [[card_story]]
        table = Table(data, colWidths=[self.content_width - (BrandSpacing.MD * 2)])
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), BrandColors.WHITE),
            ('BOX', (0, 0), (-1, -1), 2, BrandColors.INK_BLACK),  # 2px border
            ('LEFTPADDING', (0, 0), (-1, -1), BrandSpacing.MD),
            ('RIGHTPADDING', (0, 0), (-1, -1), BrandSpacing.MD),
            ('TOPPADDING', (0, 0), (-1, -1), BrandSpacing.MD),
            ('BOTTOMPADDING', (0, 0), (-1, -1), BrandSpacing.MD),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ]))

        self.story.append(table)
        self.story.append(Spacer(1, BrandSpacing.MD))

    def add_bullet_list(self, items, bold=False):
        """Add bulleted list"""
        style = 'BodyBold' if bold else 'Body'
        for item in items:
            bullet_text = f"• {item}"
            para = Paragraph(bullet_text, self.styles[style])
            self.story.append(para)
        self.story.append(Spacer(1, BrandSpacing.SM))

    def add_numbered_list(self, items, bold=False):
        """Add numbered list"""
        style = 'BodyBold' if bold else 'Body'
        for i, item in enumerate(items, 1):
            numbered_text = f"{i}. {item}"
            para = Paragraph(numbered_text, self.styles[style])
            self.story.append(para)
        self.story.append(Spacer(1, BrandSpacing.SM))

    def add_spacer(self, size='md'):
        """Add vertical space"""
        size_map = {
            'xs': BrandSpacing.XS,
            'sm': BrandSpacing.SM,
            'md': BrandSpacing.MD,
            'lg': BrandSpacing.LG,
            'xl': BrandSpacing.XL
        }
        self.story.append(Spacer(1, size_map.get(size, BrandSpacing.MD)))

    def generate(self, filename, title="Handout"):
        """Generate the PDF file"""
        # Create full output path
        timestamp = datetime.now().strftime("%Y%m%d")
        safe_title = "".join(c for c in title if c.isalnum() or c in (' ', '-', '_')).strip()
        safe_title = safe_title.replace(' ', '-').lower()[:50]
        filename = f"handout-{safe_title}-{timestamp}.pdf"
        output_path = self.output_dir / filename

        # Create PDF document
        doc = SimpleDocTemplate(
            str(output_path),
            pagesize=letter,
            leftMargin=self.margin,
            rightMargin=self.margin,
            topMargin=self.margin,
            bottomMargin=self.margin,
        )

        # Custom page template with cream background
        def draw_background(canvas, doc):
            """Draw warm cream background on every page"""
            canvas.saveState()
            canvas.setFillColor(BrandColors.WARM_CREAM)
            canvas.rect(0, 0, self.page_width, self.page_height, fill=1, stroke=0)
            canvas.restoreState()

        # Build PDF
        doc.build(self.story, onFirstPage=draw_background, onLaterPages=draw_background)

        print(f"✓ PDF created: {output_path}")
        return output_path


# ============================================================================
# CONTENT PARSER
# ============================================================================

def parse_content(content_data):
    """Parse content JSON and generate PDF"""

    generator = HandoutGenerator()

    # Add title
    title = content_data.get('title', 'Handout')
    accent = content_data.get('accent_color', 'coral')
    generator.add_title(title, accent)

    # Process sections
    sections = content_data.get('sections', [])

    for section in sections:
        section_type = section.get('type', 'text')

        if section_type == 'heading':
            level = section.get('level', 1)
            generator.add_heading(section['content'], level)

        elif section_type == 'paragraph':
            bold = section.get('bold', False)
            generator.add_paragraph(section['content'], bold)

        elif section_type == 'bullet_list':
            bold = section.get('bold', False)
            generator.add_bullet_list(section['items'], bold)

        elif section_type == 'numbered_list':
            bold = section.get('bold', False)
            generator.add_numbered_list(section['items'], bold)

        elif section_type == 'code':
            generator.add_code_block(section['content'])

        elif section_type == 'callout':
            callout_type = section.get('callout_type', 'info')
            generator.add_callout(section['content'], callout_type)

        elif section_type == 'card':
            elements = section.get('elements', [])
            generator.add_card(elements)

        elif section_type == 'spacer':
            size = section.get('size', 'md')
            generator.add_spacer(size)

    # Generate PDF
    output_path = generator.generate(
        filename=content_data.get('filename', 'handout.pdf'),
        title=title
    )

    return output_path


# ============================================================================
# MAIN
# ============================================================================

def main():
    """Main entry point"""
    if len(sys.argv) < 2:
        print("Usage: create-handout.py <content.json>")
        print("\nOr pipe JSON content:")
        print("echo '{...}' | create-handout.py -")
        sys.exit(1)

    # Read content
    if sys.argv[1] == '-':
        content_json = sys.stdin.read()
    else:
        with open(sys.argv[1], 'r') as f:
            content_json = f.read()

    # Parse and generate
    try:
        content_data = json.loads(content_json)
        output_path = parse_content(content_data)

        # Open PDF
        subprocess.run(['open', str(output_path)])

        print(f"\n✓ Handout created successfully!")
        print(f"  Location: {output_path}")

    except json.JSONDecodeError as e:
        print(f"✗ Invalid JSON: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"✗ Error generating PDF: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
