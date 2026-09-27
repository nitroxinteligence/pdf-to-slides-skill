# Visual design and review

Use this reference when creating a deck or revising an existing one. A valid file and a clean render do not establish good visual communication. Make design decisions from the audience, content, display conditions, and approved identity.

## Audit before redesign

Render the existing deck, if supplied, and inspect every slide twice: at full presentation size and in a contact sheet. Read any supplied brand manual in full, including rules for asset use and forbidden approximations. Inventory slide dimensions, typefaces, masters or layouts, diagrams, images, notes, and source claims.

For each slide, record:

| Field | Question |
|---|---|
| Claim | What should a viewer understand after this slide? |
| Reading path | Where does the eye start, and what comes next? |
| Evidence | Does the visual actually demonstrate the claim? |
| Geometry | Are margins, axes, spacing, scale, and alignment intentional? |
| Legibility | Can essential text and marks be read at intended distance? |
| Pedagogy | Does the design disclose an answer before the learner should decide? |
| Brand | Is identity faithful and subordinate to the message? |
| Fix | What specific change solves the observed problem? |

Keep a before/after log, including what was retained. A subjective adjective such as "premium" is not a diagnosis. Name the measurable or observable defect: tiny label, weak contrast, unequal choices, broken alignment, ambiguous connector, decorative image, or a logo competing with a title.

If the visual direction is still unresolved, use a few representative previews that exercise different slide functions, such as cover, dense diagram, and case. Choosing a preview approves a direction, not the legibility and composition of every final slide. If the user already supplied an approved brand system, preserve it and avoid an unnecessary style contest.

## Compose the message

- Give each slide one dominant assertion, question, comparison, or action. Use a title that communicates the point when a neutral topic heading would make the viewer wait for the speaker.
- Choose the visual form that exposes the relationship: comparison for alternatives, timeline for dependencies, process for sequence, map for a stable model, and evidence or example for a claim. Avoid repeating cards merely because they are easy to generate.
- Keep a canonical diagram for a named model. When demonstrating the model on a case, reuse its topology, labels, and reading direction so the audience recognizes the application without learning a new graphic language.
- If learners must choose, predict, or diagnose before the explanation, give plausible alternatives equal visual weight. Reveal the recommended path only after the pause or vote. Do not point an unexplained arrow or accent color toward an answer.
- Use images when they clarify a situation, create a relevant setting, or provide evidence. Empty space can be useful. Do not fill it with decorative photographs or oversized shapes that weaken the reading path.

Assertion-evidence research and practical slide guidance can inform these choices: [Garner and Alley](https://writing.engr.psu.edu/ae_comprehension.pdf), [Naegle](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1009554), and [Microsoft presentation tips](https://support.microsoft.com/en-us/powerpoint/tips-for-creating-and-delivering-an-effective-presentation). Apply them to the task rather than treating one layout as universally superior.

## Build a visual system

- Set the stage ratio and a small set of shared alignment axes. Use a modular spacing scale and stable outer margins; adapt the grid to the slide content instead of forcing every slide into the same card pattern. [IBM Carbon 2x Grid](https://carbondesignsystem.com/elements/2x-grid/overview/) is a useful reference for consistent spacing, not a required slide template.
- Establish title, body, annotation, citation, and folio roles. Essential content must stay readable at the actual delivery size. [Microsoft](https://support.microsoft.com/en-us/powerpoint/tips-for-creating-and-delivering-an-effective-presentation) advises avoiding sizes below 18 pt for projected slides; test the real room, screen, and audience when available. Small labels cannot carry an otherwise missing idea.
- Assign color by function, such as structure, evidence, action, status, or warning. [Material Design color roles](https://m3.material.io/styles/color/roles) illustrate a semantic approach; use the project's own approved palette. Do not use accent colors as a blanket way to make text look branded. Test actual foreground/background pairs after final export.
- Make diagram states legible in grayscale or without hue by adding labels, positions, shapes, fills, or patterns. A color accent may reinforce state but must not be its only signal.
- Let the logo or official signature act as a consistent endorsement. Use the supplied asset and its prescribed clear space. Do not redraw a protected symbol, guess a handle, or let a masthead compete with the slide title.
- Vary composition according to narrative function while keeping type, grid, palette, and navigation stable. Contact sheets reveal accidental monotony and abrupt style changes.

## Contrast and accessibility

For screen output, use [WCAG 2.2 text contrast](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) as a measurable baseline: 4.5:1 for ordinary text and 3:1 for large text. Aim for at least 3:1 on essential non-text graphic elements and controls per [non-text contrast](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html). The ratios are thresholds for the specified pair; do not round a failing value up. Logo text has a standards exception, but nearby informational text does not inherit it.

Those web ratios are a useful slide design target, not proof that a PPTX conforms to WCAG. Also inspect thin strokes, transparency, text on photos, projector conditions, and whether the presentation app preserves colors. Check the final rendered pair rather than trusting color tokens alone.

For accessibility, provide meaningful alternative text for informative images, a logical reading order, distinct slide titles, and complete notes when requested. Verify native PowerPoint accessibility with its checker and a real screen reader when formal compliance is required. An OOXML inspection, text extract, or HTML audit alone cannot prove that experience.

## Asset and rights ledger

Record each photo, generated image, icon, illustration, logo, and font with origin, source URL or local path, rights or license, intended use, and modifications. A generated output may be usable commercially under its provider's terms without being exclusive or free of third-party rights. A brand manual permits only the uses it actually states. A font named in CSS or PPTX is different from redistributing the font file or embedding a subset in a PDF. Verify the export's actual font rather than inferring it from the source declaration.

## Final visual pass

Inspect every rendered slide at full size and every slide in a contact sheet. Check title and body hierarchy, baseline alignment, gutters, cropping, small labels, connectors, chart values, logo scale, contrast, slide-to-slide rhythm, and narrative order. Revisit the exact slides changed in the last edit. Report which formats and pages were visually inspected and which were only checked structurally.
