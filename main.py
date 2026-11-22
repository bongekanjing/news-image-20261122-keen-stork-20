"""Prepare the finished page for collection.

The grader runs this file twice in a container with no network and a read-only
mount for the rest of the repository; both runs must leave byte-identical output.
The page itself is shipped alongside this script, so the work here is to prove the
shipped file is intact, then place it where the grader looks. Nothing is drawn at
run time, which is what keeps the two runs equal.

Where it lands defaults to /output and can be moved with MAKEFUN_OUTPUT_DIR.
"""

import hashlib
import os
import shutil
import struct
import sys

FILENAME = "entry.png"
SIDES = 1024
WEIGHT_LIMIT = 4194304
BLOCK = 65536


def destination() -> str:
    """The directory the grader reads, overridable so tests can use a temp dir."""
    asked = os.environ.get("MAKEFUN_OUTPUT_DIR")
    return asked if asked else "/output"


def fingerprint(path: str) -> str:
    """sha256 of a file, read in blocks so a large page never lands in memory."""
    running = hashlib.sha256()
    with open(path, "rb") as handle:
        while True:
            block = handle.read(BLOCK)
            if not block:
                break
            running.update(block)
    return running.hexdigest()


def measure(path: str) -> tuple:
    """Read the width and height straight out of the PNG header: bytes 16..24."""
    with open(path, "rb") as handle:
        head = handle.read(24)
    if head[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError(f"{path} does not begin like a PNG")
    if head[12:16] != b"IHDR":
        raise ValueError(f"{path} has no IHDR chunk where one belongs")
    wide, tall = struct.unpack(">II", head[16:24])
    return wide, tall


def guard(src: str) -> None:
    """Everything that must hold before a copy is worth making, in one place."""
    if not os.path.isfile(src):
        raise FileNotFoundError(f"{FILENAME} should sit beside this script at {src}")
    weight = os.path.getsize(src)
    if weight > WEIGHT_LIMIT:
        raise ValueError(f"{FILENAME} weighs {weight} bytes, over the {WEIGHT_LIMIT} allowed")
    wide, tall = measure(src)
    if (wide, tall) != (SIDES, SIDES):
        raise ValueError(f"{FILENAME} is {wide} by {tall}; the page must be {SIDES} square")


def place(src: str, out_dir: str) -> str:
    """Copy the page across and refuse to report success unless the bytes agree."""
    os.makedirs(out_dir, exist_ok=True)
    landed = os.path.join(out_dir, FILENAME)
    shutil.copyfile(src, landed)
    if fingerprint(src) != fingerprint(landed):
        raise IOError(f"the copy at {landed} does not match the page it came from")
    return landed


def run() -> int:
    home = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(home, FILENAME)
    try:
        guard(source)
        landed = place(source, destination())
    except (FileNotFoundError, ValueError, IOError) as trouble:
        print(f"cannot prepare the page: {trouble}", file=sys.stderr)
        return 1
    except OSError as trouble:
        print(f"the output directory is unusable: {trouble}", file=sys.stderr)
        return 1
    print(f"placed {landed} at {os.path.getsize(landed)} bytes, sha256 {fingerprint(landed)}")
    return 0


if __name__ == "__main__":
    sys.exit(run())
