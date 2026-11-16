"""Phoenix Ascendant — entry program for make.fun's ai-excited-01.

The shipped image is the entry. This program only delivers it: it
copies entry.png into the output directory the grader provides.
Standard library only, fully deterministic — every run writes the
same bytes.
"""

from pathlib import Path
import os
import shutil


def entry_image() -> Path:
    return Path(__file__).resolve().parent / "entry.png"


def main() -> int:
    target = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    target.mkdir(parents=True, exist_ok=True)
    # A plain copy, so the judge sees exactly the shipped bytes.
    shutil.copyfile(entry_image(), target / "entry.png")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
