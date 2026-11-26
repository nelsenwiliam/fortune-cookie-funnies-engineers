"""Fortune Cookie Funnies for Engineers.

Writes a single-line engineering fortune to entry.txt.
Pure standard library only.
"""

import os

FORTUNE = "Your future self will read this code at 3 a.m. and forgive you. Leave a comment."


def resolve_output_dir():
    """Return the first writable output directory, in grader order."""
    candidates = []
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        candidates.append(env_dir)
    candidates.append("/output")
    candidates.append("out")
    for candidate in candidates:
        try:
            os.makedirs(candidate, exist_ok=True)
            probe = os.path.join(candidate, ".write_probe")
            with open(probe, "w", encoding="utf-8") as handle:
                handle.write("")
            os.remove(probe)
            return candidate
        except OSError:
            continue
    raise OSError("no writable output directory found")


def main():
    output_dir = resolve_output_dir()
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(FORTUNE)
    with open(path, encoding="utf-8") as handle:
        written = handle.read()
    assert written == FORTUNE and len(written) == 80, "fortune mismatch"


if __name__ == "__main__":
    main()
