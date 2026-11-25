#!/usr/bin/env python3
"""The Tired Dark Lord: A 100-Word Villain Monologue.

Writes one monologue (exactly 100 words, 595 characters) to /output/entry.txt.
Pure stdlib, deterministic, no network. The output path may be overridden
with the ENTRY_OUTPUT environment variable for local testing only.
"""

import os

MONOLOGUE = (
    "Listen, boy. I am Vey Marrow, Lord of the Hollow Toll. "
    "I drowned King Aldous's fleet here, and counted every soul since"
    "\u2014nine hundred years\u2014still stamping them, because my wraiths "
    "keep botching names. Your sword is pretty\u2014put it down. "
    "Tonight I loose my mire-wyrms on Dawnland\u2014at least, that was the "
    "plan, except they sent a form. Triplicate. "
    "River tolls at midnight, ledger settles at dawn, and somewhere... "
    "where was I? Ah, the wyrms. Sit, boy. "
    "Drink this tea\u2014cold, like everything here\u2014and tell me of your town. "
    "Now run along, hero. Come back Thursday. "
    "The wyrms keep office hours, same as me."
)


def main() -> None:
    words = MONOLOGUE.split()
    assert len(words) == 100, f"expected 100 words, got {len(words)}"
    assert 1 <= len(MONOLOGUE) <= 600, (
        f"expected 1-600 chars, got {len(MONOLOGUE)}"
    )
    out = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(MONOLOGUE)


if __name__ == "__main__":
    main()
