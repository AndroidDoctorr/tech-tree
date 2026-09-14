"""Repair the invented 4+-asterisk 'extra bold' tier in the journal markdown.

Markdown has no emphasis level above **bold**. A run of four asterisks parses as
bold-opening-inside-bold, so ****x**** renders with stray literal asterisks instead
of stronger emphasis. This collapses every run of 4+ down to a real bold marker and
then drops an orphan trailing marker on any line whose ** no longer pair up.

Default is a dry run; pass --apply to rewrite.
"""

import argparse
import pathlib
import re

RUN = re.compile(r"\*{4,}")
MARKER = re.compile(r"\*\*")

# Live + recent material only. The deep archive under obsolete/ and the pre-split
# inventory are frozen and use older conventions, so they are left alone.
SCOPE = [
    "now.md",
    "bees.md",
    "inventory.md",
    "hazards.md",
    "player-calendar.md",
    "building-code-1.md",
    "museum.md",
    "rules.md",
    "advancements.md",
    "journal/index.md",
]
SCOPE_GLOBS = [
    "journal/days/year-009/**/*.md",
    "journal/weeks/*.md",
    "journal/retcons/*.md",
    ".cursor/rules/*.mdc",
]


def odd_lines(text):
    return sum(1 for line in text.splitlines() if len(MARKER.findall(line)) % 2)


def repair(text):
    out = []
    for line in RUN.sub("**", text).splitlines():
        if len(MARKER.findall(line)) % 2:
            # An unpaired marker left over from a bold that wrapped a whole table
            # cell and never closed. Drop the last one; it is the one with no partner.
            head, _, tail = line.rpartition("**")
            line = head + tail
        out.append(line)
    return "\n".join(out) + ("\n" if text.endswith("\n") else "")


def targets(root):
    seen = []
    for rel in SCOPE:
        p = root / rel
        if p.is_file():
            seen.append(p)
    for pattern in SCOPE_GLOBS:
        seen.extend(sorted(root.glob(pattern)))
    return seen


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--root", default=".")
    args = ap.parse_args()

    root = pathlib.Path(args.root).resolve()
    runs = touched = before = after = 0

    for path in targets(root):
        original = path.read_text(encoding="utf-8")
        fixed = repair(original)
        if fixed == original:
            continue
        touched += 1
        runs += len(RUN.findall(original))
        before += odd_lines(original)
        after += odd_lines(fixed)
        if args.apply:
            path.write_text(fixed, encoding="utf-8", newline="\n")

    verb = "rewrote" if args.apply else "would rewrite"
    print(f"{verb} {touched} files, collapsing {runs} runs")
    print(f"lines with unpaired **: {before} before -> {after} after")


if __name__ == "__main__":
    main()
