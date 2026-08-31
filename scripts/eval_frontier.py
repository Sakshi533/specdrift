"""Run the benchmark against free-tier API models.

Prereqs: set GEMINI_API_KEY and/or GROQ_API_KEY env vars.
Usage:
    python scripts/eval_frontier.py gemini gemini-2.5-flash
    python scripts/eval_frontier.py groq llama-3.3-70b-versatile
Results land in results/<model>.jsonl; summarize with specdrift.analysis.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from specdrift.adapters import make_adapter
from specdrift.bench import run_benchmark


def main() -> int:
    if len(sys.argv) != 3:
        print(__doc__)
        return 1
    provider, model = sys.argv[1], sys.argv[2]
    root = Path(__file__).resolve().parent.parent
    generate = make_adapter(provider, model)
    run_benchmark(root / "problems", generate, model.replace("/", "_"), root / "results")
    return 0


if __name__ == "__main__":
    sys.exit(main())
