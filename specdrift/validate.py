"""Self-check every problem against the authoring rules (see schema.py docstring).

Usage: python -m specdrift.validate [problems_root]
Exit code 0 iff every rule holds for every problem.
"""

from __future__ import annotations

import sys
from pathlib import Path

from .sandbox import run_tests
from .schema import load_all
from .scoring import score_version


def validate_problem(problem) -> list[str]:
    errors: list[str] = []
    refs = {v.number: v.reference_path.read_text(encoding="utf-8") for v in problem.versions}

    for v in problem.versions:
        results = run_tests(refs[v.number], v.tests_path)
        score_version(results, v.number)  # raises on origin > version tags
        failed = [r for r in results if not r.passed]
        if failed:  # R1
            errors.append(f"[R1] {problem.id} v{v.number}: reference fails "
                          f"{[f'{r.name}: {(r.error or chr(63))[:120]}' for r in failed]}")

        if v.number >= 2:
            prev = run_tests(refs[v.number - 1], v.tests_path)
            new_broken = [r for r in prev if r.origin == v.number and not r.passed]
            carried_broken = [r for r in prev if r.origin < v.number and not r.passed]
            if not new_broken:  # R2
                errors.append(f"[R2] {problem.id} v{v.number}: update is a no-op — "
                              f"reference v{v.number - 1} already passes all origin-v{v.number} tests")
            if carried_broken:  # R3
                errors.append(f"[R3] {problem.id} v{v.number}: stale carried tests (contradicted "
                              f"constraints must be rewritten with new origin): "
                              f"{[r.name for r in carried_broken]}")
    return errors


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent / "problems"
    problems = load_all(root)
    if not problems:
        print(f"no problems found under {root}")
        return 1
    all_errors = []
    for p in problems:
        errs = validate_problem(p)
        n_tests = {v.number: len(run_tests(p.versions[0].reference_path.read_text(encoding='utf-8'), v.tests_path))
                   for v in p.versions}  # counts only; cheap enough at pilot scale
        status = "OK " if not errs else "FAIL"
        print(f"{status} {p.id}: {len(p.versions)} versions, tests/version {list(n_tests.values())}")
        all_errors += errs
    for e in all_errors:
        print(" ", e)
    print(f"\n{len(problems)} problems, {len(all_errors)} rule violations")
    return 0 if not all_errors else 1


if __name__ == "__main__":
    sys.exit(main())
