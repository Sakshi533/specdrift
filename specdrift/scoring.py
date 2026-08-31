"""Scoring: split a version's test results into current-spec vs carried constraints."""

from __future__ import annotations

from dataclasses import dataclass

from .sandbox import TestResult


@dataclass
class VersionScore:
    version: int
    current_pass: int
    current_total: int
    carried_pass: int
    carried_total: int

    @property
    def current_rate(self) -> float:
        return self.current_pass / self.current_total if self.current_total else 1.0

    @property
    def regression_rate(self) -> float:
        """Fraction of still-valid earlier constraints now broken."""
        return 1.0 - (self.carried_pass / self.carried_total) if self.carried_total else 0.0

    @property
    def reward(self) -> float:
        """Scalar reward for RL: weight the new spec, penalize regressions."""
        return 0.6 * self.current_rate + 0.4 * (1.0 - self.regression_rate)


def score_version(results: list[TestResult], version: int) -> VersionScore:
    current = [r for r in results if r.origin == version]
    carried = [r for r in results if r.origin < version]
    stray = [r for r in results if r.origin > version]
    if stray:
        raise ValueError(f"tests tagged with origin > current version {version}: {[r.name for r in stray]}")
    return VersionScore(
        version=version,
        current_pass=sum(r.passed for r in current),
        current_total=len(current),
        carried_pass=sum(r.passed for r in carried),
        carried_total=len(carried),
    )
