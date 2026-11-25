#!/usr/bin/env python3
"""Have You Tried Turning It Off? -- make.fun entry.

Writes one funny line, under 200 characters, that a hopeless tech support
agent says to a desperate customer, to /output/entry.txt.

Deterministic, stdlib-only, no network, no input files: the line is a
constant baked into this file, so every run produces byte-identical output.
"""

import os

LINE = (
    "Have you tried turning it off and on again? "
    "It's fixed every device I've owned "
    "\u2014 just never any of my life choices."
)


def main() -> None:
    if not 1 <= len(LINE) <= 199:
        raise ValueError(f"line must be 1-199 characters, got {len(LINE)}")
    if not LINE.strip():
        raise ValueError("line must not be only whitespace")
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("line must be exactly one line, no line breaks")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
