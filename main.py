#!/usr/bin/env python3
"""Fix Human Sleep: Funniest Patch Note.

Writes a single line of patch notes announcing that human sleep has
been fixed, to /output/entry.txt (or $OUTPUT_DIR/entry.txt).
Python 3 standard library only; no network, no file reads outside the repo.
"""

import os

LINE = "Fixed: sleep now ships in one uninterrupted 8-hour build; no more 3 a.m. hotfix where your brain replays 2009."

assert "\n" not in LINE and "\r" not in LINE, "entry must be a single line"
assert 1 <= len(LINE) <= 155, "entry must be 1-155 characters"
assert LINE.strip(), "entry must not be only whitespace"

OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "/output")
os.makedirs(OUTPUT_DIR, exist_ok=True)
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8", newline="") as f:
    f.write(LINE)  # no trailing newline
