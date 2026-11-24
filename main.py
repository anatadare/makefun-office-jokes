#!/usr/bin/env python3
"""Office Jokes entry: writes one original one-line office joke to /output/entry.txt.

The joke must be a single line of 1-199 characters with no trailing newline;
it is validated before anything is written, so a bad joke fails loudly
instead of producing an invalid entry.
"""

import os

JOKE = "IT told me to turn it off and on again, so I tried it on my career, and now I'm stuck on the loading screen."

MAX_LENGTH = 199


def validate(joke):
    """Check the joke meets the entry rules; raise ValueError otherwise."""
    if not joke:
        raise ValueError("joke must not be empty")
    if len(joke) > MAX_LENGTH:
        raise ValueError(f"joke is {len(joke)} chars, over the {MAX_LENGTH} limit")
    if "\n" in joke or "\r" in joke:
        raise ValueError("joke must be a single line")


def main():
    validate(JOKE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
