"""Chat adapters for free-tier providers. Each returns a `generate(messages) -> str`.

Keys come from env vars (never hardcode): GEMINI_API_KEY, GROQ_API_KEY.
Both endpoints are OpenAI-chat-compatible, so one implementation serves both.
Uses urllib only — no SDK dependencies. Includes basic retry for free-tier 429s.
"""

from __future__ import annotations

import json
import os
import time
import urllib.error
import urllib.request

PROVIDERS = {
    "gemini": {
        "url": "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions",
        "key_env": "GEMINI_API_KEY",
    },
    "groq": {
        "url": "https://api.groq.com/openai/v1/chat/completions",
        "key_env": "GROQ_API_KEY",
    },
}


def make_adapter(provider: str, model: str, temperature: float = 0.0,
                 max_tokens: int = 1500, max_retries: int = 5):
    cfg = PROVIDERS[provider]
    key = os.environ.get(cfg["key_env"])
    if not key:
        raise RuntimeError(f"set {cfg['key_env']} first")

    def generate(messages: list[dict]) -> str:
        body = json.dumps({
            "model": model,
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens,
        }).encode("utf-8")
        req = urllib.request.Request(
            cfg["url"], data=body,
            headers={"Content-Type": "application/json", "Authorization": f"Bearer {key}",
                     "User-Agent": "specdrift-bench/0.1"},  # Groq's CDN blocks urllib's default UA
        )
        for attempt in range(max_retries):
            try:
                with urllib.request.urlopen(req, timeout=120) as resp:
                    data = json.loads(resp.read().decode("utf-8"))
                return data["choices"][0]["message"]["content"]
            except urllib.error.HTTPError as e:
                if e.code in (429, 500, 503) and attempt < max_retries - 1:
                    time.sleep(min(60, 5 * 2 ** attempt))  # free tiers rate-limit hard
                    continue
                raise
        raise RuntimeError("unreachable")

    return generate
