"""Sandboxed execution of a candidate solution against a version's test file.

The candidate code is written to solution.py in a temp dir alongside the test
file and a tiny runner, then executed in a subprocess (`python -I`) with a hard
timeout. Tests are plain functions named test_v{origin}_{name}; the origin tag
records which spec version introduced (or last rewrote) the constraint, which
is what lets us separate "satisfies the new spec" from "regressed on an old
constraint".
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path

TEST_NAME_RE = re.compile(r"^test_v(\d+)_")

RUNNER_SOURCE = '''\
import json
import os
import sys
import traceback

# -I (isolated mode) keeps the run dir off sys.path; add it back explicitly.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

results = []
fatal = None
try:
    import tests_mod
except Exception:
    fatal = "test module import failed (likely solution error): " + traceback.format_exc(limit=3)

if fatal is None:
    names = sorted(n for n in dir(tests_mod) if n.startswith("test_") and callable(getattr(tests_mod, n)))
    for name in names:
        try:
            getattr(tests_mod, name)()
            results.append({"test": name, "passed": True, "error": None})
        except Exception:
            results.append({"test": name, "passed": False,
                            "error": traceback.format_exc(limit=2)[-400:]})

print("<<<SPECDRIFT>>>" + json.dumps({"fatal": fatal, "results": results}))
'''


@dataclass
class TestResult:
    name: str
    origin: int  # spec version that introduced/last-rewrote this constraint
    passed: bool
    error: str | None = None


def list_test_names(tests_path: Path) -> list[str]:
    """Statically enumerate test function names (used when execution dies early)."""
    names = []
    for line in tests_path.read_text(encoding="utf-8").splitlines():
        m = re.match(r"def (test_\w+)\s*\(", line)
        if m:
            names.append(m.group(1))
    return names


def _origin(test_name: str) -> int:
    m = TEST_NAME_RE.match(test_name)
    if not m:
        raise ValueError(f"test name {test_name!r} lacks a v<N> origin tag (expected test_v<N>_...)")
    return int(m.group(1))


def run_tests(candidate_code: str, tests_path: Path, timeout: float = 15.0) -> list[TestResult]:
    """Run candidate_code against the given test file; always returns one result per test."""
    all_names = list_test_names(tests_path)

    with tempfile.TemporaryDirectory(prefix="specdrift_") as td:
        tdir = Path(td)
        (tdir / "solution.py").write_text(candidate_code, encoding="utf-8")
        (tdir / "tests_mod.py").write_text(tests_path.read_text(encoding="utf-8"), encoding="utf-8")
        (tdir / "_runner.py").write_text(RUNNER_SOURCE, encoding="utf-8")
        try:
            proc = subprocess.run(
                [sys.executable, "-I", "_runner.py"],
                cwd=tdir, capture_output=True, text=True, timeout=timeout,
            )
            payload = None
            for line in proc.stdout.splitlines():
                if line.startswith("<<<SPECDRIFT>>>"):
                    payload = json.loads(line[len("<<<SPECDRIFT>>>"):])
            if payload is None:
                return [TestResult(n, _origin(n), False, "runner produced no result (crash)") for n in all_names]
            if payload["fatal"]:
                return [TestResult(n, _origin(n), False, payload["fatal"][-400:]) for n in all_names]
            by_name = {r["test"]: r for r in payload["results"]}
            return [
                TestResult(n, _origin(n),
                           by_name.get(n, {}).get("passed", False),
                           by_name.get(n, {}).get("error", "test not collected"))
                for n in all_names
            ]
        except subprocess.TimeoutExpired:
            return [TestResult(n, _origin(n), False, f"timeout after {timeout}s") for n in all_names]
