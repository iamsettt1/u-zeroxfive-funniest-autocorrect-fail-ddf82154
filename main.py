#!/usr/bin/env python3
"""Funniest Autocorrect Fail — make.fun entry.

Writes a single line that reads as a hilarious autocorrect fail to
/output/entry.txt. The line is a fixed, hand-written text: a job
candidate excitedly texting her mom, autocorrect swapping "traits"
for "tits" mid-sentence, then frantically correcting herself.
"""

import os

ENTRY = (
    "Mom, my interview went great! The manager said I have excellent "
    "tits \u2014 I MEAN TRAITS. TRAITS. I'm never texting you again."
)

# The gate requires 1-199 characters of non-whitespace UTF-8 text.
assert 1 <= len(ENTRY) <= 199 and ENTRY.strip(), "entry out of gate bounds"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    # Write the line exactly, with no trailing newline, so the file
    # content is byte-for-byte the one-line entry the judge sees.
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
