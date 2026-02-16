#!/usr/bin/env python3
# /// script
# requires-python = ">=3.12"
# dependencies = ["genanki"]
# ///

import genanki
import random
import argparse
import json
import sys
import subprocess
import tempfile
import shutil
from pathlib import Path
from typing import Literal

# Deck configuration mapping
DECK_CONFIG = {
    "knowledge": {
        "id": 1595764330670,
        "name": "Knowledge"
    },
    "movement": {
        "id": 1741363521912,
        "name": "Movement/Grappling/Strengh Training"
    },
    "notes": {
        "id": 1723200755898,
        "name": "Notes and Reminders"
    }
}

# Keywords for auto-detection
CATEGORY_KEYWORDS = {
    "knowledge": [
        "research", "study", "theory", "concept", "definition", "analysis",
        "technical", "scientific", "academic", "learning", "educational",
        "algorithm", "formula", "principle", "law", "model", "framework"
    ],
    "movement": [
        "exercise", "workout", "technique", "form", "training", "grappling",
        "bjj", "judo", "wrestling", "strength", "mobility", "stretching",
        "movement", "athletic", "physical", "muscle", "drill", "guard",
        "position", "submission", "escape", "sweep"
    ],
    "notes": [
        "reminder", "remember", "note", "todo", "procedure", "steps",
        "reference", "how-to", "command", "shortcut", "tip", "checklist"
    ]
}

def detect_category(question: str, answer: str) -> str:
    """Auto-detect category based on content keywords."""
    combined_text = f"{question} {answer}".lower()

    scores = {category: 0 for category in CATEGORY_KEYWORDS}

    for category, keywords in CATEGORY_KEYWORDS.items():
        for keyword in keywords:
            if keyword in combined_text:
                scores[category] += 1

    # Return category with highest score, default to knowledge
    max_score = max(scores.values())
    if max_score == 0:
        return "knowledge"

    return max(scores, key=scores.get)

def create_basic_model() -> genanki.Model:
    """Create a basic card model with front, back, and source."""
    model_id = random.randrange(1 << 30, 1 << 31)
    return genanki.Model(
        model_id,
        'Basic with Source',
        fields=[
            {'name': 'Front'},
            {'name': 'Back'},
            {'name': 'Source'},
        ],
        templates=[
            {
                'name': 'Card 1',
                'qfmt': '{{Front}}',
                'afmt': '{{FrontSide}}<hr id="answer">{{Back}}<br><br><small style="color: #666;">{{#Source}}Source: {{Source}}{{/Source}}</small>',
            },
        ])

def create_basic_reverse_model() -> genanki.Model:
    """Create a basic card model that generates both directions."""
    model_id = random.randrange(1 << 30, 1 << 31)
    return genanki.Model(
        model_id,
        'Basic with Reverse',
        fields=[
            {'name': 'Front'},
            {'name': 'Back'},
            {'name': 'Source'},
        ],
        templates=[
            {
                'name': 'Card 1',
                'qfmt': '{{Front}}',
                'afmt': '{{FrontSide}}<hr id="answer">{{Back}}<br><br><small style="color: #666;">{{#Source}}Source: {{Source}}{{/Source}}</small>',
            },
            {
                'name': 'Card 2',
                'qfmt': '{{Back}}',
                'afmt': '{{FrontSide}}<hr id="answer">{{Front}}<br><br><small style="color: #666;">{{#Source}}Source: {{Source}}{{/Source}}</small>',
            },
        ])

def create_cloze_model() -> genanki.Model:
    """Create a cloze deletion model."""
    model_id = random.randrange(1 << 30, 1 << 31)
    return genanki.Model(
        model_id,
        'Cloze with Source',
        fields=[
            {'name': 'Text'},
            {'name': 'Source'},
        ],
        templates=[
            {
                'name': 'Cloze',
                'qfmt': '{{cloze:Text}}',
                'afmt': '{{cloze:Text}}<br><br><small style="color: #666;">{{#Source}}Source: {{Source}}{{/Source}}</small>',
            },
        ],
        model_type=genanki.Model.CLOZE)


def create_video_card_model() -> genanki.Model:
    """Create a card model with image support for video screenshots."""
    model_id = random.randrange(1 << 30, 1 << 31)
    return genanki.Model(
        model_id,
        'Video Card with Screenshot',
        fields=[
            {'name': 'Question'},
            {'name': 'Answer'},
            {'name': 'Image'},
            {'name': 'VideoSource'},
            {'name': 'Timestamp'},
        ],
        templates=[
            {
                'name': 'Card 1',
                'qfmt': '{{Question}}<br><br>{{Image}}',
                'afmt': '''{{FrontSide}}<hr id="answer">{{Answer}}
<br><br>
<small style="color: #666;">
{{#VideoSource}}📹 Source: {{VideoSource}}{{/VideoSource}}
{{#Timestamp}}<br>⏱️ Timestamp: {{Timestamp}}{{/Timestamp}}
</small>''',
            },
        ],
        css='''
        .card {
            font-family: arial;
            font-size: 20px;
            text-align: center;
            color: black;
            background-color: white;
        }
        img {
            max-width: 400px;
            max-height: 600px;
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.2);
        }
        '''
    )


def extract_screenshot(video_path: Path, timestamp: str, output_path: Path) -> bool:
    """Extract a screenshot from video at the specified timestamp using ffmpeg."""
    try:
        # Convert timestamp formats like "0:45" or "00:00:45" to ffmpeg format
        parts = timestamp.replace('[', '').replace(']', '').split(':')
        if len(parts) == 2:
            # Format: M:SS or MM:SS
            ts = f"00:{parts[0].zfill(2)}:{parts[1].zfill(2)}"
        elif len(parts) == 3:
            # Format: H:MM:SS or HH:MM:SS
            ts = f"{parts[0].zfill(2)}:{parts[1].zfill(2)}:{parts[2].zfill(2)}"
        else:
            ts = timestamp

        result = subprocess.run(
            ['ffmpeg', '-y', '-i', str(video_path), '-ss', ts, '-vframes', '1', str(output_path)],
            capture_output=True,
            text=True
        )
        return output_path.exists()
    except Exception as e:
        print(f"Warning: Could not extract screenshot at {timestamp}: {e}")
        return False


def format_timestamp_display(timestamp: str) -> str:
    """Format timestamp for display on card."""
    clean = timestamp.replace('[', '').replace(']', '').strip()
    return clean

def create_deck_for_category(category: str) -> genanki.Deck:
    """Create a deck for the specified category."""
    deck_info = DECK_CONFIG[category]
    return genanki.Deck(deck_info["id"], deck_info["name"])

def add_card_to_deck(
    deck: genanki.Deck,
    model: genanki.Model,
    question: str,
    answer: str,
    source: str = "",
    model_type: str = "basic"
) -> None:
    """Add a card to the deck."""
    if model_type == "cloze":
        deck.add_note(genanki.Note(
            model=model,
            fields=[question, source]
        ))
    else:
        deck.add_note(genanki.Note(
            model=model,
            fields=[question, answer, source]
        ))


def add_video_card_to_deck(
    deck: genanki.Deck,
    model: genanki.Model,
    question: str,
    answer: str,
    image_filename: str,
    video_source: str = "",
    timestamp: str = ""
) -> None:
    """Add a video card with screenshot to the deck."""
    deck.add_note(genanki.Note(
        model=model,
        fields=[
            question,
            answer,
            f'<img src="{image_filename}">',
            video_source,
            timestamp
        ]
    ))

def process_batch_file(batch_path: Path) -> list[dict]:
    """Load and parse batch JSON file."""
    try:
        with open(batch_path, 'r') as f:
            cards = json.load(f)

        if not isinstance(cards, list):
            print(f"Error: Batch file must contain a JSON array")
            sys.exit(1)

        return cards
    except FileNotFoundError:
        print(f"Error: Batch file not found: {batch_path}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in batch file: {e}")
        sys.exit(1)


def process_video_batch(args, cards_data: list[dict]) -> None:
    """Process video cards: extract screenshots and create Anki package with media."""
    video_path = args.video
    video_source = str(video_path.absolute())

    # Create temp directory for screenshots
    temp_dir = Path(tempfile.mkdtemp(prefix='anki_video_'))
    media_files = []

    # Determine deck name
    if args.deck_name:
        deck_name = args.deck_name
    else:
        # Auto-generate from video filename
        video_stem = video_path.stem
        deck_name = f"Video Cards::{video_stem}"

    # Create deck with random ID
    deck_id = random.randrange(1 << 30, 1 << 31)
    deck = genanki.Deck(deck_id, deck_name)

    # Create video card model
    model = create_video_card_model()

    print(f"📹 Processing video: {video_path.name}")
    print(f"📚 Deck: {deck_name}")
    print(f"🎬 Extracting screenshots...")

    successful_cards = 0
    for i, card_data in enumerate(cards_data):
        question = card_data.get('question', '')
        answer = card_data.get('answer', '')
        timestamp = card_data.get('timestamp', '0:00')

        # Generate screenshot filename
        screenshot_name = f"screenshot_{i+1:03d}.jpg"
        screenshot_path = temp_dir / screenshot_name

        # Extract screenshot
        if extract_screenshot(video_path, timestamp, screenshot_path):
            media_files.append(str(screenshot_path))

            # Add card to deck
            add_video_card_to_deck(
                deck,
                model,
                question,
                answer,
                screenshot_name,
                video_source,
                format_timestamp_display(timestamp)
            )
            successful_cards += 1
            print(f"  ✓ Card {i+1}: {timestamp}")
        else:
            print(f"  ⚠️  Card {i+1}: Failed to extract screenshot at {timestamp}")

    if successful_cards == 0:
        print("\n❌ No cards created - all screenshot extractions failed")
        shutil.rmtree(temp_dir, ignore_errors=True)
        sys.exit(1)

    # Generate output filename
    if args.output:
        output_file = args.output
    else:
        output_file = Path(f'/Users/greatmaster/Desktop/automated/anki_video_{video_path.stem}.apkg')

    # Create package with media
    package = genanki.Package(deck)
    package.media_files = media_files
    package.write_to_file(str(output_file))

    # Cleanup temp directory
    shutil.rmtree(temp_dir, ignore_errors=True)

    # Summary
    print(f"\n✓ Created {successful_cards} card(s) with screenshots")
    print(f"  📚 Deck: {deck_name}")
    print(f"  📹 Video source: {video_source}")
    print(f"\n📦 Package: {output_file}")

    # Auto-import unless disabled
    if not args.no_import:
        print("\n🚀 Importing to Anki...")
        try:
            subprocess.run(['open', str(output_file)], check=True)
            print("✓ Import initiated! Check Anki to confirm.")
        except subprocess.CalledProcessError:
            print(f"⚠️  Auto-import failed. Manually import: {output_file}")
    else:
        print(f"\n💡 To import manually: open '{output_file}'")


def main():
    parser = argparse.ArgumentParser(
        description="Create Anki flashcards and import them to the appropriate deck"
    )

    # Single card mode
    parser.add_argument('-q', '--question', help='Front of card (question or prompt)')
    parser.add_argument('-a', '--answer', help='Back of card (answer or explanation)')
    parser.add_argument('-s', '--source', default='', help='Source/citation for the information')
    parser.add_argument(
        '-c', '--category',
        choices=['knowledge', 'movement', 'notes'],
        help='Deck category (auto-detected if not specified)'
    )

    # Batch mode
    parser.add_argument('--batch', type=Path, help='Path to JSON file with multiple cards')

    # Video mode - for cards with screenshots from video
    parser.add_argument('--video-batch', type=Path, help='Path to JSON file with video cards (includes timestamps)')
    parser.add_argument('--video', type=Path, help='Path to video file for screenshot extraction')
    parser.add_argument('--deck-name', type=str, help='Custom deck name for video cards (uses :: for hierarchy)')

    # Options
    parser.add_argument('--no-import', action='store_true', help="Create package but don't auto-import")
    parser.add_argument('--output', type=Path, help='Custom output path for .apkg file')
    parser.add_argument(
        '--model-type',
        choices=['basic', 'cloze', 'basic-reverse', 'video'],
        default='basic',
        help='Card model type'
    )

    args = parser.parse_args()

    # Validate input mode
    if args.video_batch:
        # Video batch mode - process cards with screenshots
        if not args.video:
            parser.error("--video is required with --video-batch")
        if not args.video.exists():
            print(f"Error: Video file not found: {args.video}")
            sys.exit(1)

        cards_data = process_batch_file(args.video_batch)
        process_video_batch(args, cards_data)
        return

    elif args.batch:
        cards_data = process_batch_file(args.batch)
    elif args.question and args.answer:
        cards_data = [{
            'question': args.question,
            'answer': args.answer,
            'source': args.source,
            'category': args.category
        }]
    else:
        parser.error("Either provide -q/-a for single card, --batch for multiple cards, or --video-batch with --video for video cards")

    # Process cards by category
    decks_by_category = {}
    models_by_type = {}

    for card_data in cards_data:
        question = card_data.get('question', '')
        answer = card_data.get('answer', '')
        source = card_data.get('source', '')
        category = card_data.get('category')
        model_type = card_data.get('model_type', args.model_type)

        # Auto-detect category if not specified
        if not category:
            category = detect_category(question, answer)
            print(f"Auto-detected category: {category}")

        # Create deck if not exists
        if category not in decks_by_category:
            decks_by_category[category] = create_deck_for_category(category)

        # Create model if not exists
        if model_type not in models_by_type:
            if model_type == "basic":
                models_by_type[model_type] = create_basic_model()
            elif model_type == "basic-reverse":
                models_by_type[model_type] = create_basic_reverse_model()
            elif model_type == "cloze":
                models_by_type[model_type] = create_cloze_model()

        # Add card to appropriate deck
        add_card_to_deck(
            decks_by_category[category],
            models_by_type[model_type],
            question,
            answer,
            source,
            model_type
        )

    # Generate output filename
    if args.output:
        output_file = args.output
    else:
        # Auto-generate filename
        if len(decks_by_category) == 1:
            category = list(decks_by_category.keys())[0]
            output_file = Path(f'/Users/greatmaster/Desktop/automated/anki_{category}_cards.apkg')
        else:
            output_file = Path('/Users/greatmaster/Desktop/automated/anki_cards.apkg')

    # Create package with all decks
    package = genanki.Package(list(decks_by_category.values()))
    package.write_to_file(str(output_file))

    # Summary
    total_cards = sum(len(deck.notes) for deck in decks_by_category.values())
    print(f"\n✓ Created {total_cards} card(s) in {len(decks_by_category)} deck(s)")

    for category, deck in decks_by_category.items():
        deck_name = DECK_CONFIG[category]['name']
        print(f"  • {len(deck.notes)} card(s) → {deck_name}")

    print(f"\n📦 Package: {output_file}")

    # Auto-import unless disabled
    if not args.no_import:
        print("\n🚀 Importing to Anki...")
        try:
            subprocess.run(['open', str(output_file)], check=True)
            print("✓ Import initiated! Check Anki to confirm.")
        except subprocess.CalledProcessError:
            print(f"⚠️  Auto-import failed. Manually import: {output_file}")
    else:
        print(f"\n💡 To import manually: open '{output_file}'")

if __name__ == "__main__":
    main()
