"""One Word From Grandma - a make.fun bounty entry.

Grandma never types a whole command at a machine she does not trust.
She hunts and pecks it out a few letters at a time, caps lock stuck
on, until the pieces add up to the only thing she has to say to AI.
This program builds her message the same way: fragment by fragment.
"""

from pathlib import Path

# Her message, in the chunks she pecked out, in order.
FRAGMENTS = ("TURN", "IT", "OFF")


def assemble_word() -> str:
    """Join the fragments into the single word this entry submits."""
    return "".join(FRAGMENTS)


def entry_path() -> Path:
    """Resolve the file this entry is written to."""
    return Path("/output") / "entry.txt"


def emit(text: str, target: Path) -> None:
    """Deliver text to target, creating its folder when needed."""
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8")


def main() -> None:
    emit(assemble_word() + "\n", entry_path())


if __name__ == "__main__":
    main()
