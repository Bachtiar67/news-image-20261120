#!/usr/bin/env python3
"""Entrypoint: write the 20 November 2026 news summary image.

Copies the pre-rendered PNG asset (assets/entry.png) byte-for-byte to
$MAKEFUN_OUTPUT_DIR/entry.png (default /output). Standard library only,
no network, deterministic: both runs write identical bytes.
"""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "assets", "entry.png")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    with open(SRC, "rb") as fh:
        head = fh.read(8)
        ihdr = fh.read(25)
    if head != b"\x89PNG\r\n\x1a\n":
        sys.exit("assets/entry.png is not a PNG file")
    if len(ihdr) < 25 or ihdr[4:8] != b"IHDR":
        sys.exit("assets/entry.png has no IHDR chunk")
    width = int.from_bytes(ihdr[8:12], "big")
    height = int.from_bytes(ihdr[12:16], "big")
    if width > 1024 or height > 1024:
        sys.exit("assets/entry.png exceeds 1024x1024")
    if os.path.getsize(SRC) > 1048576:
        sys.exit("assets/entry.png exceeds 1 MiB")
    shutil.copyfile(SRC, dst)
    if os.path.getsize(dst) != os.path.getsize(SRC):
        sys.exit("copied file size mismatch")
    print("wrote", dst, os.path.getsize(dst), "bytes")


if __name__ == "__main__":
    main()
