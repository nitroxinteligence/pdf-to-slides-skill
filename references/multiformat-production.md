# Editable deck, web slides, and PDF parity

Read this when a request combines PPTX, HTML, and PDF, or when export fidelity matters. Choose one content specification for slide order, wording, notes, sources, asset IDs, and design tokens. Renderers may differ, but a late copy or timing change must reach every requested format. Keep scripts modular enough that content, visual components, export, and QA can be revised independently.

## Select production routes

- For an editable PowerPoint, follow the installed PPT Master skill and create native text, shapes, tables, charts, layouts, and notes. Use raster media only where it serves the design, such as a photograph or an official logo asset. A slide-sized screenshot inside a PPTX is not an editable slide.
- For an HTML presentation, follow the installed Frontend Slides skill. HTML can help explore visual directions, but it does not itself prove PowerPoint editability. Translate the selected design into native PPTX objects when both formats are required.
- If the user supplied an approved deck or template, inspect its actual content and master before replacing it. Preserve approved identity and content unless the request authorizes redesign. Prefer a traceable revision over a visually similar reconstruction when the original file is available.
- When an editable PPTX and its PDF preview are both requested, export that PDF from the final PPTX. For an HTML-only request, a browser PDF may be appropriate, but label its source. Do not pass off an HTML print as the export of a different PPTX.

If HTML is not requested, do not build it simply to demonstrate frontend techniques. If a requested HTML deck must be portable as one file, inline required local assets and avoid network-only fonts, scripts, and images. Keep a separate asset ledger even when bytes are embedded.

## PPTX structure and editability

Check the package with an OOXML-aware library or ZIP inspection. Confirm slide and notes counts, slide dimensions, layouts or masters, relationships, media inventory, and absence of broken or external links. Inspect representative slide object trees to distinguish native shapes and text from slide-sized pictures. Verify that the planned speaker notes contain the promised objective, narration, transition, timing, and source information.

Use the actual approved logo asset if it can be extracted faithfully and its use is permitted. Do not rebuild a trademark from rough geometric copies. Place recurring identity in a master or layout when feasible and confirm its visible scale after export.

## HTML interaction and accessibility

Use a stable stage ratio, then scale the stage to the viewport without changing its internal geometry. Inspect the deck at the intended presentation resolution and at smaller viewports. For a portable HTML file, verify there are no unresolved relative asset URLs or required network requests. If an image is inlined as a data URI, decode it and compare its hash with the source asset when practical.

Keyboard, pointer, and touch navigation must not steal input from buttons, forms, or editable text. Closed notes should leave the focus order, such as through `hidden` and `inert`; reopening notes should expose usable controls and focus. Give controls names and visible focus, announce slide changes when appropriate, keep DOM reading order aligned with visual order, and respect `prefers-reduced-motion`. Test the actual browser behavior. Code inspection alone does not establish usability or screen-reader compatibility.

## PDF export and fonts

Export after the last PPTX edit. Confirm page count, aspect ratio, slide order, selectable text where expected, and visible charts, images, and branding. Render every PDF page and compare against the deck's intended design. Inspect the actual font families embedded in the PDF, for example with `pdffonts`, and distinguish them from families merely declared in the PPTX. An office exporter can substitute fonts even when the source font is installed; record that substitution and inspect the result. Check font licensing and embedding rights separately from the rights to slide content.

Re-exporting the same final PPTX with the same exporter and comparing equal-sized raster pages is a useful reproducibility check. Zero pixel differences prove those two exports match under that renderer. They do not prove that Microsoft PowerPoint, Keynote, a browser version, or a projector will render identically. Compare HTML and PPTX by content, diagram grammar, hierarchy, and visible layout; record any intentional differences.

## Small, deterministic QA set

Select only checks that answer a concrete risk:

1. Structural: PPTX package integrity, slide and notes counts, expected editability, broken relationships, HTML syntax, PDF page count.
2. Content: titles, numbers, sources, slide order, speaker notes, script word count, pauses, and calculated speaking rate. Exclude written pause instructions from spoken-word counts.
3. Visual: every slide in the final PPTX-derived PDF, every HTML slide when present, and every requested companion PDF page. Inspect full size and a contact sheet.
4. Accessibility: contrast pairs, color-independent states, alt text, reading order, focus and keyboard behavior, and native presentation-app checks when available.
5. Delivery: open or extract the final ZIP, verify expected files and byte hashes, and remove obsolete duplicate renders from the package.

Report exact coverage: inventoried, structurally checked, rendered, visually inspected, and untested. A successful build is not a visual review. A matching PDF export is not a rehearsal, user approval, or formal accessibility certification.
