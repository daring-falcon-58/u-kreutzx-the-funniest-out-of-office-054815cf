#!/usr/bin/env python3
"""The Funniest Out-of-Office — make.fun entry (u-kreutzx-the-funniest-out-of-office-054815cf).

Writes one line, the funniest out-of-office auto-reply, to
$MAKEFUN_OUTPUT_DIR/entry.txt (falling back to /output/entry.txt).

The line (83 characters, 83 bytes, no trailing newline):
    I'm on leave. Please email my replacement: me, but on holiday, so also unavailable.

Deterministic, no network, no randomness: two runs produce byte-identical
output. See README.md for how the line was chosen (20 candidates, scored
criterion by criterion against the published judge brief; the live-judge A/B
was not run — the shared OpenRouter free quota is exhausted until
2026-11-25 07:00 WIB — so selection is by structured manual scoring,
stated honestly).
"""

import os

ENTRY = "I'm on leave. Please email my replacement: me, but on holiday, so also unavailable."

# The competition gate is 1-140 characters. Fail loudly here, at import
# time, instead of silently writing an entry the grader would reject if
# the line is ever edited past the gate.
if not 1 <= len(ENTRY) <= 140:
    raise ValueError(f"entry is {len(ENTRY)} chars, outside the 1-140 gate")


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Verify the write: read the file back and compare bytes, so a
    # partial write or encoding surprise fails loudly instead of
    # submitting a corrupted entry.
    if open(path, "rb").read() != ENTRY.encode("utf-8"):
        raise OSError(f"entry.txt at {path} does not match the entry")


if __name__ == "__main__":
    main()
