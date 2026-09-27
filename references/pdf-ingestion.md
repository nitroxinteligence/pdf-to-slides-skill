# PDF ingestion and knowledge capture

The output of this phase is evidence, not slides.

## 1. Inventory

For every source, record:

- stable source ID, path or URL, file type, byte size, and checksum when local;
- page count or section structure, title, author, language, and actual access level when available;
- text-heavy, technical/layout-heavy, or scanned/image-only;
- presence of tables, figures, charts, formulas, columns, footnotes, and appendices;
- extraction method selected and why;
- rights or license restrictions relevant to the intended use.

Compare hashes to identify exact duplicates. Mark close derivatives or overlapping editions so repeated content is not counted as independent support. Identify cover-only images, snippets, inaccessible files, and secondary reporting explicitly. Do not infer an unread book from its cover or a full course from a public sales page.

Use an isolated work directory. Keep the original PDFs unchanged.

## 2. Faithful extraction

Extract each PDF separately before merging sources. Preserve heading hierarchy and insert explicit page anchors such as:

```markdown
<!-- source: pdf-01 | page: 17 -->
```

Retain meaningful lists, tables, captions, quotations, examples, references, and footnotes. Export important figures to assets and link them from the Markdown with their source page. For multi-column layouts, confirm reading order visually. For scanned pages, record OCR use and uncertainty.

For supporting DOCX files, keep heading or section anchors and inspect embedded figures. For web pages, save the exact URL, access date, and what was publicly visible. For photos of covers, record only visible bibliographic evidence. Distinguish all of these from full-document reading.

Do not silently normalize away repeated headers if they carry section meaning. Do not infer text hidden inside diagrams; inspect or transcribe it explicitly when relevant.

## 3. Extraction validation

Compare extraction against the rendered pages. At minimum check:

- every page is extracted or explicitly marked failed/blank;
- first, middle, and last portions of each document;
- pages containing dense tables, diagrams, formulas, or unusual layouts;
- chapter boundaries and table of contents;
- suspiciously short pages and abrupt text breaks;
- numeric values, units, dates, and names used later in the deck.

Check the latest source when a claim, statistic, regulation, product detail, or external benchmark may have changed. Record whether a video or audiobook was actually viewed or heard in full, sampled, or assessed only from metadata. A third-party upload does not establish a license to reuse it.

If a search or platform connector reaches a quota or access limit, record that limit and continue with directly accessible primary sources when possible. Do not treat a search snippet, inaccessible page, or metadata record as a full reading of the source.

Create a source manifest with page-level status and limitations. Do not mark extraction complete when unreadable or unavailable pages remain unreported.

## 4. Per-source dossier

For each substantive source, produce a detailed dossier containing:

- hierarchy of sections and arguments;
- theses, claims, and supporting evidence;
- definitions and named frameworks;
- data, statistics, dates, and comparisons;
- examples, case studies, stories, and analogies;
- methods, processes, decision rules, and anti-patterns;
- important quotations within copyright-safe limits;
- visual assets worth reusing or recreating;
- caveats, counterarguments, and conclusions;
- slide-worthy material with source/page references.

For a commercial deliverable, note reuse limits and create original explanation, cases, diagrams, and learner exercises. Attribution alone does not override a noncommercial or no-derivatives license. Short citations must remain within applicable rights.

This is not a short summary. Preserve enough detail for another agent to reconstruct the reasoning without rereading every page.

## 5. Coverage matrix

Split the source into meaningful content units. Give each unit one disposition:

- `slide`: represented explicitly in one or more slides;
- `notes`: retained in speaker notes or appendix/background material;
- `omit`: intentionally excluded, with a concrete reason;
- `pending`: not yet resolved.

Track source ID, page or section range, topic, evidence, priority, disposition, destination slide or companion PDF page, and reuse constraint. The matrix must contain no `pending` items before final delivery.

## 6. Book-to-Skill

Use Book-to-Skill when the user wants a persistent knowledge asset or expects repeated questions about the documents. Generate it from the faithful extraction and retain the extraction beside it.

Book-to-Skill is a navigation and synthesis layer. Its compact chapter files, glossary, patterns, and cheatsheet do not replace the full Markdown or the original PDF when checking exact facts, figures, quotations, or nuance.
