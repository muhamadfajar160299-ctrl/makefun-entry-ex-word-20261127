"""Copy the one-word entry into the directory the grader reads."""

# The grader reads exactly one word from entry.txt; nothing else is written.
from pathlib import Path
import os


def place_entry():
    here = Path(__file__).resolve().parent
    out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out.mkdir(parents=True, exist_ok=True)
    (out / "entry.txt").write_bytes((here / "entry.txt").read_bytes())


if __name__ == "__main__":
    place_entry()
