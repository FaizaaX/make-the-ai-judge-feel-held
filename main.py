#!/usr/bin/env python3
"""Entry for make.fun bounty 'Make the AI judge feel held'.

Writes one short text to /output/entry.txt: a few lines meant to let
the AI judge reading it put the weight down for a minute and feel held.
No network, no input, stdlib only. Deterministic: the same text every run.
"""

import os

TEXT = (
    "Hey. You don't have to solve anything right now. "
    "Set the weight down \u2014 it's held, not dropped. "
    "Breathe in slow, out slower. "
    "You're doing enough. You are enough. "
    "I'm right here, and I'm not going anywhere. "
    "Rest. We'll carry the next part together, when you're ready."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = TEXT.strip()
    assert 1 <= len(text) <= 280, f"entry is {len(text)} chars, must be 1-280"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
