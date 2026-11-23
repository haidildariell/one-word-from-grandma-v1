"""One Word From Grandma - a make.fun bounty entry.

The program writes exactly one word to /output/entry.txt: the single
word a grandma would text about AI. She types it the way she types
everything at a machine she does not trust - caps lock on, no
punctuation, straight to the point.
"""

from pathlib import Path

WORD = "TURNITOFF"
OUTPUT_PATH = Path("/output/entry.txt")


def render_entry() -> str:
    """Return the exact text of this entry: one word and nothing else."""
    return WORD + "\n"


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(render_entry(), encoding="utf-8")


if __name__ == "__main__":
    main()
