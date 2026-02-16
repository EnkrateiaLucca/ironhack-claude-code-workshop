---
name: meeting-notes-summarizer
description: Transform raw meeting notes into structured summaries with action items, decisions, and follow-up questions. This skill should be used when users need to process unstructured meeting notes into actionable formats.
---

# Meeting Notes Summarizer

Transform raw, unstructured meeting notes into clear, actionable summaries.

## When to Use This Skill

Use this skill when the user:
- Has raw meeting notes that need organizing
- Wants to extract action items from a meeting
- Needs to identify key decisions made
- Wants a structured summary for sharing

**Trigger phrases:** "summarize meeting", "meeting notes", "extract action items", "what did we decide"

## Output Format

The summarizer produces a structured markdown document with four sections:

### 1. Action Items
- Clear tasks with assigned owners
- Due dates when mentioned
- Priority indicators

### 2. Key Decisions
- Decisions reached during the meeting
- Context for each decision
- Who made/approved the decision

### 3. Follow-up Questions
- Unresolved questions
- Items needing clarification
- Topics for next meeting

### 4. Summary Paragraph
- 2-3 sentence overview
- Main topics discussed
- Overall meeting outcome

## How to Execute

1. Read the raw meeting notes provided by the user
2. Identify speakers and their contributions
3. Extract action items (look for "will", "should", "needs to", assignments)
4. Identify decisions (look for "decided", "agreed", "approved", conclusions)
5. Note unresolved questions or "parking lot" items
6. Generate the structured output using `scripts/format-notes.py`

## Script Usage

```bash
python scripts/format-notes.py --input notes.txt --output summary.md
```

The script accepts raw text and outputs formatted markdown.

## Example Input

```
Meeting about Q2 launch - John, Sarah, Mike

John: We need to finalize the landing page by Friday
Sarah: I can handle the copy, but need design assets
Mike: Design will be done by Wednesday
Sarah: What about the mobile version?
John: Let's table that for now, focus on desktop first
Mike: Agreed. I'll send assets to Sarah by EOD Wednesday
John: Great. Sarah, can you have copy ready by Thursday?
Sarah: Yes, I'll send draft for review Thursday morning
```

## Example Output

```markdown
# Meeting Summary: Q2 Launch

## Action Items
- [ ] **Mike:** Send design assets to Sarah (Due: Wednesday EOD)
- [ ] **Sarah:** Complete landing page copy (Due: Thursday AM)
- [ ] **Sarah:** Send copy draft for review (Due: Thursday morning)

## Key Decisions
- **Desktop first approach:** Mobile version tabled for later; focusing on desktop launch
- **Timeline confirmed:** Landing page to be finalized by Friday

## Follow-up Questions
- Mobile version timeline - when to revisit?
- Who reviews Sarah's copy draft?

## Summary
The team aligned on the Q2 landing page timeline with a desktop-first approach. Mike will deliver design assets by Wednesday, enabling Sarah to complete copy by Thursday for Friday's deadline.
```

## Notes

- Preserve speaker attribution when relevant
- Flag any mentioned deadlines prominently
- If no owner is mentioned for a task, note "Owner: TBD"
- Include timestamps if present in original notes
