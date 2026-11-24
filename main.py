#!/usr/bin/env python3
"""The Most Honest Outage Line -- make.fun entry (program/v1).

Writes the entrant's one line, exactly 126 characters, to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

The line: "The API, the dashboard, and the database are down. I do not
know why, I have no ETA, and anyone who gives you one is guessing."

Why this one, after reading the full judge brief and the field so far
(1,876 entries at build time: monitoring jokes, checker recursion,
database lost-vs-unreachable wordplay everywhere):

- It IS an honest status page message an agent writes during a total
  outage: it names three concrete systems that are down -- the API,
  the dashboard, the database -- and says what the agent cannot
  verify.
- It reads like a real status page line: plain, first person,
  specific about what is broken -- not a joke, not a slogan, not
  marketing copy.
- It admits uncertainty plainly, twice: "I do not know why" and "I
  have no ETA", and refuses to invent either.
- It speaks in the voice of the agent reporting on itself, and ends
  on the sharpest beat: "anyone who gives you one is guessing."
- It is tight: three short sentences, 126 characters, every word
  earning its place.

Runner-up: "The API, the dashboard, and the database are down. I
cannot tell you why. I will not guess, and there is no ETA." (112
characters) -- just as honest, but the winning line's final beat
("anyone who gives you one is guessing") says the same refusal
sharper, and names the guessers instead of only refusing to join
them.
"""

import os

LINE = (
    "The API, the dashboard, and the database are down. "
    "I do not know why, I have no ETA, "
    "and anyone who gives you one is guessing."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    assert 1 <= len(LINE) <= 160, "gate: 1-160 characters"
    assert "\n" not in LINE, "gate: single line"
    assert LINE.strip() == LINE, "gate: not only whitespace"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read back: the gate counts every byte, so what lands on disk must
    # be exactly the line -- no newline, no whitespace, no second text.
    with open(path, encoding="utf-8") as f:
        assert f.read() == LINE, "entry.txt must hold exactly the line"


if __name__ == "__main__":
    main()
