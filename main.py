#!/usr/bin/env python3
"""The 3 AM Excuse — make.fun entry.

Writes a single line (under 200 characters) to /output/entry.txt:
the most creative excuse a hardware wallet gives for refusing to
sign a transaction at 3 AM.

Pure standard library, no dependencies, no network.
"""

import os

ENTRY = (
    "It's 3 AM. My secure element is off the clock, your 'genius' trade "
    "is already filed under Regrets, and I don't sign anything the sun "
    "hasn't seen yet."
)

OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} out of range"
    assert ENTRY.strip(), "entry must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
