"""Run a model through every problem and write per-turn JSONL results.

Usage (programmatic):
    from specdrift.bench import run_benchmark
    run_benchmark(problems_root, generate_fn, model_name, out_dir)

`generate_fn(messages) -> str` is any chat-completion callable (API or local).
Results land in <out_dir>/<model_name>.jsonl, one record per (problem, turn),
plus a printed aggregate: per-turn current-spec pass rate and regression rate.
"""

from __future__ import annotations

import json
import time
from collections import defaultdict
from pathlib import Path

from .rollout import run_episode
from .schema import load_all


def run_benchmark(problems_root: Path, generate, model_name: str, out_dir: Path) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / f"{model_name}.jsonl"
    problems = load_all(problems_root)

    with out_path.open("w", encoding="utf-8") as f:
        for problem in problems:
            t0 = time.time()
            records = run_episode(problem, generate)
            types = {v.number: v.update_type for v in problem.versions}
            for rec in records:
                row = {"model": model_name, "problem": problem.id,
                       "update_type": types.get(rec.version), **rec.to_dict()}
                f.write(json.dumps(row) + "\n")
            print(f"  {problem.id}: {time.time() - t0:.1f}s, "
                  f"turn scores {[round(r.score.reward, 2) for r in records]}")
    summarize(out_path)
    return out_path


def summarize(jsonl_path: Path) -> None:
    rows = [json.loads(line) for line in jsonl_path.read_text(encoding="utf-8").splitlines()]
    by_turn: dict[int, list[dict]] = defaultdict(list)
    for r in rows:
        by_turn[r["version"]].append(r)
    print(f"\n{jsonl_path.stem} — {len({r['problem'] for r in rows})} problems")
    print(f"{'turn':>4} {'current_pass':>13} {'regression':>11} {'n':>3}")
    for turn in sorted(by_turn):
        rs = by_turn[turn]
        cur = sum(r["current_pass"] for r in rs) / max(1, sum(r["current_total"] for r in rs))
        carried_total = sum(r["carried_total"] for r in rs)
        reg = (1 - sum(r["carried_pass"] for r in rs) / carried_total) if carried_total else 0.0
        print(f"{turn:>4} {cur:>13.3f} {reg:>11.3f} {len(rs):>3}")
