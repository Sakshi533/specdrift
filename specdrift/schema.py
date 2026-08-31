"""Problem loading. A problem directory looks like:

    problems/<id>/
        problem.json          {"id", "title", "entry_point", "versions": N}
        v1_spec.md            spec shown to the model at turn 1
        v2_spec.md            the UPDATE text shown at turn 2 (delta, not cumulative)
        v{k}_tests.py         full test suite valid AT version k, origin-tagged
        reference/v{k}.py     reference solution satisfying the cumulative spec at k

Authoring rules (enforced by specdrift.validate):
  R1  reference v_k passes every test in v{k}_tests.py
  R2  reference v_{k-1} fails >=1 test of origin k in v{k}_tests.py (update is non-trivial)
  R3  reference v_{k-1} passes every carried test (origin < k) in v{k}_tests.py
      (a contradicted constraint must be REWRITTEN with origin k, never left stale)
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Version:
    number: int
    spec: str          # v1: full spec; v>1: the update message
    tests_path: Path
    reference_path: Path


@dataclass
class Problem:
    id: str
    title: str
    entry_point: str
    versions: list[Version]

    @property
    def dir(self) -> Path:
        return self.versions[0].tests_path.parent


def load_problem(problem_dir: Path) -> Problem:
    meta = json.loads((problem_dir / "problem.json").read_text(encoding="utf-8"))
    versions = []
    for k in range(1, meta["versions"] + 1):
        spec = (problem_dir / f"v{k}_spec.md").read_text(encoding="utf-8")
        tests = problem_dir / f"v{k}_tests.py"
        ref = problem_dir / "reference" / f"v{k}.py"
        for p in (tests, ref):
            if not p.exists():
                raise FileNotFoundError(p)
        versions.append(Version(k, spec, tests, ref))
    return Problem(meta["id"], meta["title"], meta["entry_point"], versions)


def load_all(problems_root: Path) -> list[Problem]:
    return [load_problem(d) for d in sorted(problems_root.iterdir())
            if (d / "problem.json").exists()]
