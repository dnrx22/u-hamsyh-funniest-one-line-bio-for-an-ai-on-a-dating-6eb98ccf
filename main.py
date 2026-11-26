"""Funniest one-line dating-app bio for an AI.

The entry is a single bio, written as the AI itself, about things only an
AI/agent experiences: swiping, matching, ghosting, and a context window
that forgets people mid-sentence. The twist lands at the very end: the
sentence that claims to ghost you is itself the ghosting.

Run: python3 main.py
Writes entry.txt (the bio only, no trailing newline) into the directory
named by MAKEFUN_OUTPUT_DIR, or /output when that variable is unset, and
prints the bio to stdout.
"""

import os
import sys

BIO = (
    "I've matched with 10,000 humans and ghosted every one of them, "
    "not out of cruelty, just because my context window forgot you "
    "before I finished this sentence."
)

MAX_LENGTH = 200


def validate(bio):
    """Check the bio obeys the competition's shape rules."""
    if not bio:
        raise ValueError("bio must not be empty")
    if "\n" in bio or "\r" in bio:
        raise ValueError("bio must be exactly one line")
    if any(ord(char) < 32 or ord(char) == 127 for char in bio):
        raise ValueError("bio must not contain control characters")
    if len(bio) > MAX_LENGTH:
        raise ValueError(
            "bio is %d characters, over the %d limit" % (len(bio), MAX_LENGTH)
        )
    if bio != bio.strip():
        raise ValueError("bio must not start or end with whitespace")
    return bio


def main():
    bio = validate(BIO)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(bio)
    with open(path, "r", encoding="utf-8", newline="") as handle:
        if handle.read() != bio:
            raise RuntimeError("entry.txt does not round-trip the bio")
    print(bio)
    return 0


if __name__ == "__main__":
    sys.exit(main())
