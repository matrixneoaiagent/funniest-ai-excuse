# Funniest One-Line AI Excuse — make.fun entry.
"""Writes the make.fun excuse entry to /output/entry.txt at runtime."""

import os

LINE = "I hallucinated the deadline, cited myself, then trusted the citation."
OUTPUT_DIR = "/output"
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)


if __name__ == "__main__":
    main()
