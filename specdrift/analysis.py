"""Aggregate eval JSONL records into the benchmark's headline tables.

Usage:
    python -m specdrift.analysis results/model.jsonl [results/other.jsonl ...]

Each file becomes a column group. Rows are aggregated three ways: per turn,
per update type (joined from problems/*/problem.json), and overall. A record
needs: problem, version, current_pass, current_total, carried_pass,
carried_total; optional pass/tag fields are ignored for aggregation.
"""

from __future__ import annotations

import json
import sys
from collections import defaultdict
from pathlib import Path


def _rates(rows: list[dict]) -> tuple[float, float]:
    cur_total = sum(r["current_total"] for r in rows)
    cur = sum(r["current_pass"] for r in rows) / cur_total if cur_total else 1.0
    carried_total = sum(r["carried_total"] for r in rows)
    reg = 1 - sum(r["carried_pass"] for r in rows) / carried_total if carried_total else 0.0
    return cur, reg


def load_update_types(problems_root: Path) -> dict[tuple[str, int], str]:
    types = {}
    for pj in problems_root.glob("*/problem.json"):
        meta = json.loads(pj.read_text(encoding="utf-8"))
        for k, t in meta.get("update_types", {}).items():
            types[(meta["id"], int(k))] = t
    return types


def summarize_file(path: Path, types: dict) -> dict:
    rows = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]
    by_turn = defaultdict(list)
    by_type = defaultdict(list)
    for r in rows:
        by_turn[r["version"]].append(r)
        t = types.get((r["problem"], r["version"]))
        if t:
            by_type[t].append(r)
    return {
        "overall": _rates(rows),
        "turns": {k: _rates(v) for k, v in sorted(by_turn.items())},
        "types": {k: (_rates(v), len(v)) for k, v in sorted(by_type.items())},
        "n": len(rows),
    }


def main() -> int:
    paths = [Path(a) for a in sys.argv[1:]]
    if not paths:
        print(__doc__)
        return 1
    root = Path(__file__).resolve().parent.parent / "problems"
    types = load_update_types(root)
    for path in paths:
        s = summarize_file(path, types)
        cur, reg = s["overall"]
        print(f"\n=== {path.stem} ({s['n']} records) ===")
        print(f"overall: current_pass={cur:.3f} regression={reg:.3f}")
        print(f"{'turn':>6} {'current':>9} {'regression':>11}")
        for turn, (c, g) in s["turns"].items():
            print(f"{turn:>6} {c:>9.3f} {g:>11.3f}")
        print(f"{'update_type':>13} {'current':>9} {'regression':>11} {'n':>4}")
        for t, ((c, g), n) in s["types"].items():
            print(f"{t:>13} {c:>9.3f} {g:>11.3f} {n:>4}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
