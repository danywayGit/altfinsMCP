"""Fetch the full list of supported symbols from altFINS public API."""

import json
import os
from pathlib import Path

import httpx
from dotenv import load_dotenv

SYMBOLS_URL = "https://altfins.com/api/v2/public/symbols"


def main() -> None:
    load_dotenv()

    api_key = os.getenv("ALTFINS_API_KEY")
    if not api_key:
        raise RuntimeError("Set ALTFINS_API_KEY in environment or .env before running.")

    headers = {"Accept": "application/json", "X-API-KEY": api_key}

    with httpx.Client(timeout=60.0, follow_redirects=True) as client:
        response = client.get(SYMBOLS_URL, headers=headers)
        response.raise_for_status()
        payload = response.json()

    output_path = Path("feature-runs") / "00-live-symbols-list.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")

    if isinstance(payload, list):
        print(f"Fetched {len(payload)} symbols")
        sample = [s if isinstance(s, str) else s.get("symbol", s) for s in payload[:10]]
        print(f"Sample: {', '.join(str(s) for s in sample)}")
    else:
        print("Fetched symbols response (non-list format)")

    print(f"Wrote output to: {output_path}")


if __name__ == "__main__":
    main()
