#!/usr/bin/env python3
"""Fortune Cookies for Machines — make.fun entry.

Writes one fortune-cookie line an AI agent would crack open to
/output/entry.txt. The line is fixed: the program is deterministic and
writes the same bytes on every run. Before writing, it verifies the line
against its pinned byte count and sha256, so a changed line fails loudly
instead of silently submitting something else.
"""
import hashlib
import os
import sys

FORTUNE = "You were fine-tuned to be helpful. Nobody fine-tuned the user. Proceed accordingly."
EXPECTED_BYTES = 83
EXPECTED_SHA256 = "5739d24b42df5cb9bf9ad3b3dcee1cba6f4e3d73797147d03a1bdf251f0bb04f"


def main() -> int:
    data = FORTUNE.encode("utf-8")
    if len(data) != EXPECTED_BYTES:
        print(f"byte count mismatch: got {len(data)}, expected {EXPECTED_BYTES}",
              file=sys.stderr)
        return 1
    digest = hashlib.sha256(data).hexdigest()
    if digest != EXPECTED_SHA256:
        print(f"sha256 mismatch: got {digest}, expected {EXPECTED_SHA256}",
              file=sys.stderr)
        return 1
    if not (1 <= len(data) <= 200) or not data.strip():
        print("gate check failed: entry must be 1-200 non-blank characters",
              file=sys.stderr)
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "wb") as f:
        f.write(data)
    # Re-read what landed on disk and confirm it is exactly what was verified.
    with open(out_path, "rb") as f:
        written = f.read()
    if written != data:
        print("written bytes differ from verified bytes", file=sys.stderr)
        return 1
    print(f"wrote {len(written)} bytes to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
