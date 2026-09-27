# Optional PDF companions

Create companion PDFs only when the brief requests them or when they materially improve review, delivery, or learner use. Define each artifact's purpose before choosing its format.

## Possible companions

- deck preview or contact sheet for rapid review;
- learner workbook with prompts, worksheets, and space to respond;
- diagnostic instrument with scoring and interpretation guidance;
- presenter guide with narration, timing, facilitation cues, and sources;
- print or distribution copy of the deck.

Keep an editable source for any artifact expected to change. A PDF is a delivery format, not the editable source.

## Output profiles

Choose the profile that matches use:

- `display`: screen-oriented dimensions, RGB color, accessible contrast, and links when useful;
- `print`: appropriate page size, margins, image resolution, and restrained ink coverage;
- `fillable`: usable form fields, logical tab order, clear labels, and enough space for realistic answers.

Do not call a PDF fillable because it visually resembles a form. Enter representative responses, save, reopen, edit, clear, and verify every field. Confirm that scoring or calculated fields work if included.

For an interactive form, inspect both the canonical AcroForm field tree and the page widgets after saving. Verify field names, stored values, appearances, and page placement agree. A rendered answer alone does not prove the saved field value is correct.

## Production and QA

- Preserve source attribution, image credits, and asset license records in the editable source or evidence manifest.
- Use an available PDF authoring workflow with a maintained editable source. For programmatic generation, tools such as ReportLab can build the file; Poppler rendering and a PDF parser can verify it. Text extraction does not replace visual inspection.
- Render and inspect every page. Check cropping, overflow, contrast, image quality, pagination, links, form fields, and blank or duplicated pages.
- Verify Unicode and accented characters in headings, body text, filenames, bookmarks, and form fields. Normalize combining characters or embed a font that supports them when a render shows missing-glyph boxes.
- When exporting a PDF from a PPTX, export from the current final PPTX and confirm slide count, order, content, notes policy, dimensions, fonts, and visual parity. Re-export after any PPTX change that affects the PDF.
- Report editable-source validation, PDF generation, rendered-page inspection, fillable-form validation, and export parity as separate states.
