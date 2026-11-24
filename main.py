#!/usr/bin/env python3
"""Seventeen Syllables of Debugging.

Writes one haiku about debugging (5-7-5, seventeen syllables) to
/output/entry.txt. The haiku:

    one red error glows
    cursor blinks at three a.m.
    the fix was one space

Syllables, line by line: one(1) red(1) er-ror(2) glows(1) = 5;
cur-sor(2) blinks(1) at(1) three(1) a-m(2) = 7;
the(1) fix(1) was(1) one(1) space(1) = 5. Seventeen in all.
"""

import os

HAIKU = (
    "one red error glows\n"
    "cursor blinks at three a.m.\n"
    "the fix was one space"
)

# Syllable counts for every word in the haiku, checked by hand.
SYLLABLES = {
    "one": 1, "red": 1, "error": 2, "glows": 1,
    "cursor": 2, "blinks": 1, "at": 1, "three": 1, "a.m.": 2,
    "the": 1, "fix": 1, "was": 1, "space": 1,
}


def validate(text: str) -> None:
    """Mirror the bounty gate: 3 lines, 5-7-5 syllables, 1-200 chars."""
    lines = text.split("\n")
    assert len(lines) == 3, f"expected 3 lines, got {len(lines)}"
    for line, want in zip(lines, (5, 7, 5)):
        got = sum(SYLLABLES[word] for word in line.split())
        assert got == want, f"{line!r} has {got} syllables, want {want}"
    assert 1 <= len(text) <= 200, f"{len(text)} chars, want 1-200"
    assert text.strip(), "entry must not be only whitespace"


def main() -> None:
    validate(HAIKU)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(HAIKU)


if __name__ == "__main__":
    main()
