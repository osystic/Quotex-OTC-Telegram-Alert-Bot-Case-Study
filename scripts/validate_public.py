#!/usr/bin/env python3
"""Fail closed on unexpected public-file types and common accidental secret forms."""
from pathlib import Path
import json
import re
import sys

root = Path(__file__).resolve().parents[1]
allowed = {
    ".github/workflows/public-hygiene.yml", ".osystic/repository.yml",
    "README.md", "case-study.md", "SECURITY.md", "NOTICE.md", ".gitignore",
    "public-showcase-manifest.json",
    "docs/architecture.md", "docs/verification.md", "docs/completion.md",
    "scripts/validate_public.py",
}
found = {str(p.relative_to(root)) for p in root.rglob("*") if p.is_file() and ".git" not in p.parts}
unexpected = found - allowed
missing = allowed - found
assert not unexpected, f"Unexpected public artifacts: {sorted(unexpected)}"
assert not missing, f"Missing case-study artifacts: {sorted(missing)}"
meta = json.loads((root / "public-showcase-manifest.json").read_text())
assert meta["publisher"] == "OSYSTIC" and meta["project_completion_status"] == "completed"
assert meta["source_code_included"] is False and meta["client_identity_included"] is False
for file in found:
    if file == "scripts/validate_public.py":
        continue
    content = (root / file).read_text()
    for regex in [
        r"(?i)gh[pousr]_[A-Za-z0-9_]{30,}",
        r"(?i)AKIA[0-9A-Z]{16}",
        r"-----BEGIN [^-]*PRIVATE KEY-----",
        r"\b\d{8,10}:[A-Za-z0-9_-]{35,}\b",
    ]:
        if re.search(regex, content):
            raise AssertionError(f"Potential secret in {file}")
print(f"PASS public case-study hygiene: {len(found)} approved files, completed metadata, no identified credential patterns.")
