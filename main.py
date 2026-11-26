#!/usr/bin/env python3
"""Fortune Cookie Funnies for Engineers.

Writes one fortune-cookie message for a software engineer to
/output/entry.txt — a single line of at most 120 characters.

Pure standard library only; no third-party packages, no network,
no files outside this repository.
"""

import os

FORTUNE = (
    "Your future self will read this code at 3 a.m. "
    "and forgive you. Leave a comment."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(FORTUNE)


if __name__ == "__main__":
    main()
