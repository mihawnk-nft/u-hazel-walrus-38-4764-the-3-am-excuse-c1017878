#!/usr/bin/env python3
"""The 3 AM Excuse — make.fun entry.

Writes a single line (under 200 characters) to /output/entry.txt:
the most creative excuse a hardware wallet gives for refusing to
sign a transaction at 3 AM.

Pure standard library, no dependencies, no network.

Determinism: the entry is a fixed literal assembled from fixed parts.
There is no randomness, no clock, and no input other than the output
path, so every run writes byte-identical output.
"""

import os

# The excuse, kept as one clause per string so the line can be audited
# clause by clause. Joining them in build_entry() reproduces the exact
# same single line as before — no spaces added, none removed.
ENTRY_PARTS = (
    "It's 3 AM. My secure element is off the clock, your 'genius' trade ",
    "is already filed under Regrets, and I don't sign anything the sun ",
    "hasn't seen yet.",
)

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def build_entry() -> str:
    """Assemble the entry line from its fixed parts."""
    return "".join(ENTRY_PARTS)


def validate(entry: str) -> None:
    """Enforce the competition's length and non-blank rules."""
    assert 1 <= len(entry) <= 200, f"entry length {len(entry)} out of range"
    assert entry.strip(), "entry must not be only whitespace"


def main() -> None:
    entry = build_entry()
    validate(entry)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(entry)


if __name__ == "__main__":
    main()
