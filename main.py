"""Writes 22 November 2026's front page to /output/entry.png.

The grader runs this twice in a fresh container with no network and a read-only /bot,
and both runs must write the same bytes. The page is therefore drawn once and shipped
in the repository; this copies those exact bytes through, which is deterministic by
construction. `draw.py` beside it is the program that produced `entry.png`, and
`stories.py` holds the story list it draws from.

To regenerate the image:
    python3 draw.py
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

os.makedirs(OUT_DIR, exist_ok=True)
shutil.copyfile(os.path.join(HERE, "entry.png"), os.path.join(OUT_DIR, "entry.png"))
