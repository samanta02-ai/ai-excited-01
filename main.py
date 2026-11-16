"""Phoenix Ascendant — make.fun ai-excited-01 entry.

Copies the entry image to the output directory the grader provides.
Standard library only; the program is deterministic: every run writes
the same bytes.
"""

import os
import shutil
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # A plain copy: the judge sees exactly the shipped bytes.
    shutil.copyfile(source, os.path.join(out_dir, "entry.png"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
