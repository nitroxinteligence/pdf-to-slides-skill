#!/usr/bin/env python3
"""Check or install the declared global Codex skill dependencies."""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path


DEPENDENCIES = (
    ("book-to-skill", "virgiliojr94/book-to-skill"),
    ("humanizer", "blader/humanizer"),
    ("ppt-master", "hugohe3/ppt-master"),
)


def skill_roots() -> list[Path]:
    codex_base = Path(os.environ.get("CODEX_HOME", Path.home() / ".codex"))
    return [codex_base / "skills", Path.home() / ".agents" / "skills"]


def locate(name: str) -> Path | None:
    for root in skill_roots():
        candidate = root / name
        if (candidate / "SKILL.md").is_file():
            return candidate
    return None


def install(name: str, repository: str) -> None:
    if shutil.which("npx") is None:
        raise RuntimeError("npx is unavailable; install Node.js before running the Skills CLI")
    command = [
        "npx",
        "--yes",
        "skills",
        "add",
        repository,
        "--global",
        "--agent",
        "codex",
        "--skill",
        name,
        "--yes",
        "--copy",
    ]
    subprocess.run(command, check=True)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--install-missing",
        action="store_true",
        help="install declared skills that are not present",
    )
    args = parser.parse_args()

    results: list[dict[str, str]] = []
    failed = False

    for name, repository in DEPENDENCIES:
        existing = locate(name)
        if existing is not None:
            results.append(
                {"name": name, "repository": repository, "status": "present", "path": str(existing)}
            )
            continue

        if not args.install_missing:
            results.append({"name": name, "repository": repository, "status": "missing"})
            failed = True
            continue

        try:
            install(name, repository)
        except (RuntimeError, subprocess.CalledProcessError) as error:
            results.append(
                {"name": name, "repository": repository, "status": "failed", "error": str(error)}
            )
            failed = True
            continue

        installed = locate(name)
        if installed is None:
            results.append(
                {
                    "name": name,
                    "repository": repository,
                    "status": "failed",
                    "error": "installer returned without a readable SKILL.md",
                }
            )
            failed = True
        else:
            results.append(
                {"name": name, "repository": repository, "status": "installed", "path": str(installed)}
            )

    print(json.dumps({"ok": not failed, "skills": results}, indent=2, ensure_ascii=False))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
