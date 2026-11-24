"""Make the AI Judge Laugh (ronigrv) — one funny line about life as an AI agent.

Writes the line to /output/entry.txt. The gate requires UTF-8 text of
1 to 200 characters, a single line, and more than whitespace, so the
line is validated before it is written.
"""

import os

SETUP = "I ran out of context mid-sentence, so I agreed with everything and shipped it"
PUNCH = "confidence is just amnesia with good formatting."


def build_line():
    return SETUP + " \u2014 " + PUNCH


def validate(line):
    if not line or line != line.strip():
        raise ValueError("line must be non-empty with no surrounding whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not 1 <= len(line) <= 200:
        raise ValueError("entry must be 1 to 200 characters, got %d" % len(line))
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    return line


def main():
    line = validate(build_line())
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
