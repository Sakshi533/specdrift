"""Package the repo (specdrift/ + problems/) as a Kaggle dataset the training
kernel can mount. Run locally: python kaggle_train/push_dataset.py
First run creates the dataset; later runs push new versions."""

import json
import shutil
import tempfile
from pathlib import Path

from kaggle.api.kaggle_api_extended import KaggleApi

REPO = Path(__file__).resolve().parent.parent
DATASET_ID = "sakshigoswami335/specdrift-repo"


def main():
    api = KaggleApi()
    api.authenticate()
    with tempfile.TemporaryDirectory() as td:
        staging = Path(td) / "specdrift-repo"
        staging.mkdir()
        for sub in ("specdrift", "problems"):
            shutil.copytree(REPO / sub, staging / sub,
                            ignore=shutil.ignore_patterns("__pycache__"))
        (staging / "dataset-metadata.json").write_text(json.dumps({
            "title": "specdrift-repo",
            "id": DATASET_ID,
            "licenses": [{"name": "CC0-1.0"}],
        }))
        try:
            print(api.dataset_create_version(str(staging), version_notes="update", quiet=True))
        except Exception as e:
            print(f"create_version failed ({e}); trying first-time create")
            print(api.dataset_create_new(str(staging), public=False, quiet=True))


if __name__ == "__main__":
    main()
