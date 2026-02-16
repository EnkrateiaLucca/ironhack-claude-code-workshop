# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///

"""
Meeting Notes Formatter

Formats raw meeting notes into structured markdown output.
This script is called by the meeting-notes-summarizer skill.

Usage:
    uv run format-notes.py --input notes.txt --output summary.md
    uv run format-notes.py --input notes.txt  # prints to stdout
"""

import argparse
import re
from dataclasses import dataclass
from typing import Optional


@dataclass
class MeetingSummary:
    """Structured meeting summary."""
    title: str
    action_items: list[dict]
    decisions: list[dict]
    follow_ups: list[str]
    summary: str


def extract_action_items(text: str) -> list[dict]:
    """Extract action items from meeting text.

    Looks for patterns like:
    - "X will do Y"
    - "X to do Y"
    - "X needs to Y"
    - "Action: X"
    """
    action_items = []

    # Pattern: Person will/should/needs to do something
    patterns = [
        r'(\w+):\s*.*?(?:will|should|needs? to|has to)\s+(.+?)(?:\.|$)',
        r'(\w+)\s+(?:will|should|needs? to)\s+(.+?)(?:\.|$)',
        r'\*\*(\w+)\*\*.*?(?:will|should|needs? to)\s+(.+?)(?:\.|$)',
    ]

    for pattern in patterns:
        matches = re.findall(pattern, text, re.IGNORECASE | re.MULTILINE)
        for owner, task in matches:
            action_items.append({
                'owner': owner.strip(),
                'task': task.strip(),
                'due': extract_due_date(task)
            })

    return action_items


def extract_due_date(text: str) -> Optional[str]:
    """Extract due date from text if present."""
    patterns = [
        r'by\s+(monday|tuesday|wednesday|thursday|friday|saturday|sunday)',
        r'by\s+(eod|end of day|tomorrow|next week)',
        r'due:?\s*(\w+)',
        r'by\s+(\d{1,2}/\d{1,2})',
    ]

    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            return match.group(1)

    return None


def extract_decisions(text: str) -> list[dict]:
    """Extract decisions from meeting text.

    Looks for patterns like:
    - "decided to"
    - "agreed that"
    - "approved"
    - "confirmed"
    """
    decisions = []

    patterns = [
        r'(?:we\s+)?(?:decided|agreed|approved|confirmed)\s+(?:to\s+|that\s+)?(.+?)(?:\.|$)',
        r'decision:\s*(.+?)(?:\.|$)',
    ]

    for pattern in patterns:
        matches = re.findall(pattern, text, re.IGNORECASE | re.MULTILINE)
        for decision in matches:
            decisions.append({
                'decision': decision.strip(),
                'context': ''
            })

    return decisions


def extract_follow_ups(text: str) -> list[str]:
    """Extract follow-up questions and unresolved items."""
    follow_ups = []

    # Questions that weren't answered
    questions = re.findall(r'[^.!]*\?', text)
    follow_ups.extend([q.strip() for q in questions if len(q.strip()) > 10])

    # "Table for later" items
    tabled = re.findall(r'(?:table|park|defer|later)[^.]*', text, re.IGNORECASE)
    follow_ups.extend([t.strip() for t in tabled])

    return list(set(follow_ups))[:5]  # Dedupe and limit


def generate_summary(text: str, action_items: list, decisions: list) -> str:
    """Generate a brief summary paragraph."""
    num_actions = len(action_items)
    num_decisions = len(decisions)

    summary_parts = []

    if num_decisions > 0:
        summary_parts.append(f"The team made {num_decisions} key decision(s)")

    if num_actions > 0:
        owners = list(set(item['owner'] for item in action_items))
        summary_parts.append(f"{num_actions} action item(s) were assigned to {', '.join(owners[:3])}")

    return ". ".join(summary_parts) + "." if summary_parts else "Meeting notes processed."


def format_output(summary: MeetingSummary) -> str:
    """Format the summary as markdown."""
    output = []

    output.append(f"# Meeting Summary: {summary.title}\n")

    # Action Items
    output.append("## Action Items\n")
    if summary.action_items:
        for item in summary.action_items:
            due = f" (Due: {item['due']})" if item['due'] else ""
            output.append(f"- [ ] **{item['owner']}:** {item['task']}{due}")
    else:
        output.append("- No action items identified")
    output.append("")

    # Decisions
    output.append("## Key Decisions\n")
    if summary.decisions:
        for item in summary.decisions:
            output.append(f"- {item['decision']}")
    else:
        output.append("- No formal decisions recorded")
    output.append("")

    # Follow-ups
    output.append("## Follow-up Questions\n")
    if summary.follow_ups:
        for item in summary.follow_ups:
            output.append(f"- {item}")
    else:
        output.append("- No follow-up items identified")
    output.append("")

    # Summary
    output.append("## Summary\n")
    output.append(summary.summary)

    return "\n".join(output)


def process_notes(text: str, title: str = "Meeting") -> str:
    """Main processing function."""
    action_items = extract_action_items(text)
    decisions = extract_decisions(text)
    follow_ups = extract_follow_ups(text)
    summary_text = generate_summary(text, action_items, decisions)

    summary = MeetingSummary(
        title=title,
        action_items=action_items,
        decisions=decisions,
        follow_ups=follow_ups,
        summary=summary_text
    )

    return format_output(summary)


def main():
    parser = argparse.ArgumentParser(description='Format meeting notes into structured summary')
    parser.add_argument('--input', '-i', help='Input file with raw meeting notes')
    parser.add_argument('--output', '-o', help='Output file for formatted summary')
    parser.add_argument('--title', '-t', default='Meeting', help='Meeting title')

    args = parser.parse_args()

    # Read input
    if args.input:
        with open(args.input, 'r') as f:
            text = f.read()
    else:
        import sys
        text = sys.stdin.read()

    # Process
    result = process_notes(text, args.title)

    # Output
    if args.output:
        with open(args.output, 'w') as f:
            f.write(result)
        print(f"Summary written to {args.output}")
    else:
        print(result)


if __name__ == '__main__':
    main()
