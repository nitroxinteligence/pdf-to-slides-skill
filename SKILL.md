---
name: pdf-to-slides
description: Transform one or more attached PDFs into a source-grounded, content-dense, visually polished slide deck. Use when the user asks to extract PDFs and create slides, presentations, decks, PowerPoint, or PPTX without shallow summarization.
---

# PDF to Slides

Create a presentation whose claims, examples, numbers, and narrative remain traceable to the supplied PDFs. Treat visual concision and intellectual depth as separate requirements: slides may be clean, but the underlying evidence and speaker notes must stay substantive.

## Bootstrap

Before processing sources, resolve this skill's directory as `SKILL_ROOT`, then run:

```bash
python3 "$SKILL_ROOT/scripts/bootstrap_skills.py" --install-missing
```

The script may install only these declared dependencies when absent:

- `virgiliojr94/book-to-skill` for reusable, chapter-oriented knowledge;
- `blader/humanizer` for the final prose pass;
- `hugohe3/ppt-master` for visual presentation production.

Do not replace an existing installation automatically. Read [references/bootstrap.md](references/bootstrap.md) when installation fails, provenance is unclear, or a dependency needs updating. Report installed, already present, and failed as separate states. A newly installed skill may require a new session before automatic discovery; its files can still be read directly in the current run.

## Intake

Resolve every attached PDF to a local path. If none is accessible, ask the user to attach the files or provide their paths.

Inspect the sources before asking questions. Ask only for decisions the files and prior conversation do not answer and that would materially change the deck, normally:

- audience and desired outcome;
- presentation context and duration or approximate slide count;
- language, tone, and depth;
- brand kit, reference deck, template, or visual direction;
- output format and whether speaker notes are required.

Group related questions and continue any source inspection that does not depend on the answers. Never ask the user to repeat information already present in the conversation or attachments.

## Workflow

1. Read [references/pdf-ingestion.md](references/pdf-ingestion.md) and build the source manifest, faithful Markdown, per-source dossiers, and coverage matrix. Do not design slides yet.
2. Decide whether the material needs long-term reuse. For recurring consultation, use Book-to-Skill in addition to the faithful Markdown. For a one-off deck, Book-to-Skill is optional.
3. Read [references/presentation-workflow.md](references/presentation-workflow.md). Build the cross-source synthesis and slide blueprint before generating the deck.
4. Lock claims, numbers, quotations, and citations. Then apply Humanizer to titles, body copy, and speaker notes. Humanizer may improve prose but must not change facts, source references, rankings, dates, or quantities.
5. Read the installed PPT Master `SKILL.md` and use its workflow for visual production. Preserve the approved brand or template. Create editable slides unless the user explicitly chooses another format.
6. Render and inspect every slide. Fix overflow, clipping, weak contrast, repetitive layouts, unsupported claims, missing source coverage, and leftover placeholders. Re-render changed slides.

## Non-negotiable gates

- Never jump directly from PDF attachments to slide generation.
- Never treat a chapter summary or generated skill as the only source of truth.
- Preserve page anchors in extracted Markdown and use them in the evidence ledger.
- Record extraction failures, unreadable pages, dropped figures, OCR uncertainty, and unsupported formulae explicitly.
- Every substantive slide must map to at least one source and page range, except user-approved framing slides such as cover, agenda, or closing.
- A relevant source unit may be included, moved to speaker notes/background, or omitted with a reason; it may not disappear silently.
- Do not invent facts, quotations, causal claims, or citations to make the story smoother.
- Prefer additional slides or speaker notes over deleting important nuance solely to meet an arbitrary slide count.
- Distinguish a valid PPTX file, a successful render, visual inspection, content coverage, and user approval as separate states.

## Deliverables

Unless the user narrows the scope, finish with:

- the editable presentation;
- rendered previews or a contact sheet;
- a source and extraction manifest;
- a coverage/evidence matrix linking slides to PDFs and pages;
- a short QA report listing extraction limitations and deliberately omitted material.
