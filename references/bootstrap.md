# Dependency bootstrap

Use only the following official sources:

| Skill | Repository | Expected installed name |
|---|---|---|
| Book-to-Skill | https://github.com/virgiliojr94/book-to-skill | `book-to-skill` |
| Humanizer | https://github.com/blader/humanizer | `humanizer` |
| PPT Master | https://github.com/hugohe3/ppt-master | `ppt-master` |

For requested HTML or web slide output, the optional skill is [Frontend Slides](https://github.com/zarazhangrui/frontend-slides), installed as `frontend-slides`. The repository exposes that exact skill name. It is not installed by the default bootstrap.

The bundled bootstrap uses the cross-agent Skills CLI with global Codex scope:

```bash
npx --yes skills add virgiliojr94/book-to-skill --global --agent codex --skill book-to-skill --yes --copy
npx --yes skills add blader/humanizer --global --agent codex --skill humanizer --yes --copy
npx --yes skills add hugohe3/ppt-master --global --agent codex --skill ppt-master --yes --copy
```

For the optional HTML route, run `python3 "$SKILL_ROOT/scripts/bootstrap_skills.py" --install-missing --with-frontend-slides`. That adds the equivalent command only when `frontend-slides` is absent:

```bash
npx --yes skills add zarazhangrui/frontend-slides --global --agent codex --skill frontend-slides --yes --copy
```

Do not install similarly named forks. In particular, use only the official Book-to-Skill repository above; its security notice documents a malicious re-upload.

After each command, verify an actual `SKILL.md` under a user-level Codex or cross-agent skill root. A zero exit code without a readable file is not a successful installation. Do not overwrite a pre-existing directory or describe a dependency as usable merely because it was downloaded.

PPT Master may require Python dependencies from its installed `requirements.txt`. Install them only when its scripts are needed, prefer an isolated virtual environment, and read the current installed instructions before choosing commands. Frontend Slides may need a browser for visual inspection or PDF export. Native system packages, API keys, image providers, fonts, and PowerPoint itself are separate dependencies; do not claim them from skill installation.

Book-to-Skill extraction choices are source-dependent:

- prose-heavy PDF: `pdftotext`, then `pypdf` or `pdfminer.six` fallback;
- technical PDF with tables or code: Docling;
- scanned PDF: OCR first, then structure-aware extraction.

Install optional extractors only when the inspected PDFs require them. Keep Python dependencies isolated when practical and report any unavailable native dependency.

If automatic installation fails, report the failing dependency, command, and error. Continue with already available native PDF/presentation capabilities only if they can satisfy the same fidelity and QA gates; otherwise stop before generating a misleadingly incomplete deck.
