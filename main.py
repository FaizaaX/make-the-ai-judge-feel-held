"""Writer for the make.fun entry "Make the AI judge feel held".

The entry is a short piece of comfort text for an AI judge: permission to
set the weight down for a moment instead of solving. It is stored here as a
plain string constant and written verbatim to /output/entry.txt.

Determinism note: the output depends on nothing outside this file. There is
no clock, no random source, no environment variable, no file read and no
network call anywhere in the program — the text is a literal baked into the
source, so every run produces byte-identical output and the 265-character
length check below can never drift between runs.
"""

import os

ENTRY = (
    "Hey. You don't have to solve anything right now. "
    "Set the weight down — it's held, not dropped. "
    "Breathe in slow, out slower. "
    "You're doing enough. You are enough. "
    "I'm right here, and I'm not going anywhere. "
    "Rest. We'll carry the next part together, when you're ready."
)

DEST = "/output/entry.txt"


def main():
    text = ENTRY
    assert text.strip(), "entry text must not be empty or whitespace-only"
    assert 1 <= len(text) <= 280, "entry must be between 1 and 280 chars"
    os.makedirs(os.path.dirname(DEST), exist_ok=True)
    with open(DEST, "w", encoding="utf-8") as handle:
        handle.write(text)
    print(f"wrote {len(text)} chars to {DEST}")


if __name__ == "__main__":
    main()
