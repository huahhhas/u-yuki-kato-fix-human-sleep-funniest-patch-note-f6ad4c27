#!/usr/bin/env python3
"""Fix Human Sleep: Funniest Patch Note.

Writes a single line of patch notes announcing that human sleep has
been fixed, to /output/entry.txt (or $OUTPUT_DIR/entry.txt).
Python 3 standard library only; no network, no file reads outside the repo.
"""

import os

LINE = "Fixed: sleep now ships in one uninterrupted 8-hour build; no more 3 a.m. hotfix where your brain replays 2009."

# Gate validation: the sealed scorer requires UTF-8 text of 1-160
# characters, not only whitespace, with no trailing newline.
assert "\n" not in LINE and "\r" not in LINE, "entry must be a single line"
assert 1 <= len(LINE) <= 160, "entry must be 1-160 characters"
assert LINE.strip(), "entry must not be only whitespace"
assert LINE == LINE.strip(), "entry must not start or end with whitespace"
LINE.encode("utf-8")  # raises if the line is not valid UTF-8 text

def main():
    """Write the validated patch-note line to entry.txt, byte-exact.

    The file is written in binary mode from the UTF-8 encoding of LINE,
    so no newline translation or trailing newline can ever sneak in.
    """
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "wb") as f:
        f.write(LINE.encode("utf-8"))


if __name__ == "__main__":
    main()
