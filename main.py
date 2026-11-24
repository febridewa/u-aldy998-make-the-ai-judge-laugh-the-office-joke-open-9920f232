#!/usr/bin/env python3
"""Write one one-line joke about office life.

The joke: IT's classic advice (turn it off and on again) backfires on the
advice-giver — the printer files a support ticket about the human. The turn
lands in the last few words, when the machine becomes the complainant.

Deterministic: a fixed string, no randomness, no network, no time.
Writes exactly that one line to /output/entry.txt (created if missing).
"""
import os

OUTPUT_PATH = "/output/entry.txt"

JOKE = (
    "IT told me to turn the jammed printer off and on again; "
    "the printer has now opened a ticket about me."
)


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
