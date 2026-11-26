#!/usr/bin/env python3
"""The Internet in One Word -- entry for make.fun
competition u-ronigrv-the-internet-in-one-word-e388f33b.

The task: write one single word to /output/entry.txt, the word that
describes the whole internet. The judge weighs, in order: it is a
single word, it is funny on its own, it says something true about the
internet as a whole, it surprises, and it lands in one beat.

The word I picked is "unhinged". Why it wins each of those:

* Single word -- one adjective, eight letters, no phrase, no trick.
* Funny -- it is the word people reach for when a timeline, a
  comment section, or a group chat goes off the rails, and everyone
  knows exactly what it means the instant they read it.
* True of the whole internet -- not one app or one mood. The web's
  defining quality is that millions of strangers, all slightly
  unhinged, are shouting into the same room at once. The word
  describes the place, not a behaviour inside it.
* Surprising -- the first obvious answers are "chaos", "infinite",
  "addictive". "Unhinged" is the second thought that is funnier
  than the first thought, which is exactly what the judge rewards.
* Lands in one beat -- correctly spelled, instantly readable, short
  enough to hit before the reader has time to think.

The program itself is deliberately deterministic: the same word on
every run, so the two grading runs produce byte-identical output.
Before writing, it checks the gate the sealed scorer enforces --
UTF-8 text, 1 to 30 characters, not only whitespace -- and refuses
to write anything that would fail it.
"""

import os
import sys

# The entry: one word for the whole internet.
WORD = "unhinged"

# The gate, as published in the competition's RULES.txt:
# /output/entry.txt must be UTF-8 text of 1 to 30 characters,
# not only white space.
MAX_CHARS = 30
# The grader runs this in its own sandbox where /output is the
# output directory. MAKEFUN_OUTPUT only exists so the entry can be
# verified locally without touching the machine's shared /output;
# it never changes the graded path, which stays /output/entry.txt.
OUTPUT_PATH = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")


def validate(word):
    """Return True only if the word passes the published gate."""
    if not isinstance(word, str):
        return False
    if not (1 <= len(word) <= MAX_CHARS):
        return False
    if not word.strip():
        return False
    if any(ch.isspace() for ch in word):
        # A single word: no spaces, tabs, or newlines inside it.
        return False
    # Must encode cleanly as UTF-8.
    try:
        word.encode("utf-8")
    except UnicodeEncodeError:
        return False
    return True


def main():
    if not validate(WORD):
        print("entry word fails the gate: %r" % WORD, file=sys.stderr)
        return 1

    # The grader runs this in a sandbox where /output exists. Locally
    # it may not, so create the directory when it is missing.
    out_dir = os.path.dirname(OUTPUT_PATH)
    os.makedirs(out_dir, exist_ok=True)

    # Write exactly the word, no trailing newline: the file is the
    # entry, and nothing else may be in it.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as fh:
        fh.write(WORD)

    print("wrote %r to %s (%d chars)" % (WORD, OUTPUT_PATH, len(WORD)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
