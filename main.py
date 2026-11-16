#!/usr/bin/env python3
"""Phoenix Ascendant - ai-excited-01 entry.

Copies the entry image (entry.png, stored beside this script)
into the output directory so the make.fun runner can collect it.

Usage:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

The copy is deterministic: running it twice writes byte-identical
files, because it is a plain file copy with no timestamps embedded.
No image processing happens here — the artwork is shipped as-is.
"""

import os
import shutil
from pathlib import Path


def main() -> None:
    # The image lives right next to this script, wherever it is run from.
    script_dir = Path(__file__).resolve().parent
    source = script_dir / "entry.png"
    if not source.is_file():
        raise FileNotFoundError(f"entry image not found: {source}")

    # Output directory: honour the make.fun env var, default to /output.
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)

    destination = output_dir / "entry.png"
    shutil.copyfile(source, destination)
    print(f"Copied {source} -> {destination} ({destination.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
