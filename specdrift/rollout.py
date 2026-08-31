"""Multi-turn episode protocol: drive a model through a problem's spec updates.

Model-agnostic: `generate` is any callable taking a list of chat messages
({"role", "content"}) and returning the assistant's reply text. Works for API
models and local HF models alike.
"""

from __future__ import annotations

import re
from dataclasses import asdict, dataclass

from .sandbox import run_tests
from .schema import Problem
from .scoring import VersionScore, score_version

CODE_BLOCK_RE = re.compile(r"```(?:python)?\s*(.*?)```", re.DOTALL)

SYSTEM_PROMPT = (
    "You are a senior Python engineer implementing a client's request. The client "
    "may send requirement updates; each update amends the CURRENT requirements — "
    "everything not changed by an update still applies. Always reply with the "
    "complete, updated implementation in a single ```python code block (full "
    "function definitions, never a diff). No tests, no example usage."
)


def extract_code(reply: str) -> str:
    """Take the last fenced code block (models often restate old code first)."""
    blocks = CODE_BLOCK_RE.findall(reply)
    return blocks[-1].strip() if blocks else reply.strip()


@dataclass
class TurnRecord:
    version: int
    code: str
    score: VersionScore
    failed_tests: list[str]

    def to_dict(self) -> dict:
        return {"version": self.version, "code": self.code,
                "failed_tests": self.failed_tests, **asdict(self.score)}


def run_episode(problem: Problem, generate, timeout: float = 15.0) -> list[TurnRecord]:
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    records: list[TurnRecord] = []
    for v in problem.versions:
        if v.number == 1:
            user = v.spec
        else:
            user = f"Requirement update from the client:\n\n{v.spec}"
        messages.append({"role": "user", "content": user})
        reply = generate(messages)
        messages.append({"role": "assistant", "content": reply})

        code = extract_code(reply)
        results = run_tests(code, v.tests_path, timeout=timeout)
        records.append(TurnRecord(
            version=v.number,
            code=code,
            score=score_version(results, v.number),
            failed_tests=[r.name for r in results if not r.passed],
        ))
    return records
