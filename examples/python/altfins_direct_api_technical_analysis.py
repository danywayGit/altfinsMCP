import json
import os
from pathlib import Path

import httpx
from dotenv import load_dotenv

API_URL = "https://altfins.com/api/v2/public/technical-analysis/data"


def _build_error_detail(response: httpx.Response) -> str:
    try:
        data = response.json()
    except ValueError:
        text = (response.text or "").strip()
        return text[:300] if text else "No response body"

    if isinstance(data, dict):
        message = data.get("message") or data.get("error") or "Unknown error"
        uid = data.get("exceptionUID")
        request_uri = data.get("request")
        parts = [str(message)]
        if uid:
            parts.append(f"exceptionUID={uid}")
        if request_uri:
            parts.append(f"request={request_uri}")
        return " | ".join(parts)

    return str(data)[:300]


def main() -> None:
    load_dotenv()

    api_key = os.getenv("ALTFINS_API_KEY")
    if not api_key:
        raise RuntimeError("Set ALTFINS_API_KEY in environment or .env before running.")

    # Keep env naming aligned with MCP script; allow legacy fallback.
    symbol = os.getenv("ALTFINS_TA_SYMBOLS", "").strip() or os.getenv(
        "ALTFINS_TA_SYMBOL", ""
    ).strip()

    header_variants = [
        {"Accept": "application/json", "X-API-KEY": api_key},
        {"Accept": "application/json", "X-Api-Key": api_key},
    ]

    page_size = 50
    all_entries: list = []
    page = 0

    with httpx.Client(timeout=60.0, follow_redirects=True) as client:
        while True:
            page_params = {"page": page, "size": page_size}
            if symbol:
                page_params["symbol"] = symbol

            response = None
            payload = None
            for headers in header_variants:
                current = client.get(API_URL, headers=headers, params=page_params)
                if current.status_code < 400:
                    response = current
                    payload = response.json()
                    break
                response = current

            if payload is None:
                if response is not None and response.status_code == 403:
                    raise RuntimeError(
                        "Direct API call returned 403 Forbidden. "
                        f"Details: {_build_error_detail(response)}. "
                        "Your key may be valid for MCP but not authorized for this direct REST endpoint."
                    )
                if response is not None and response.status_code == 401:
                    raise RuntimeError(
                        "Direct API call returned 401 Unauthorized. "
                        f"Details: {_build_error_detail(response)}. "
                        "Check ALTFINS_API_KEY value and expected auth header format."
                    )
                if response is not None:
                    response.raise_for_status()
                raise RuntimeError("No response received from technical analysis endpoint.")

            # Handle paginated envelope or flat list
            if isinstance(payload, dict) and "content" in payload:
                all_entries.extend(payload["content"])
                is_last = payload.get("last", True)
            elif isinstance(payload, list):
                all_entries.extend(payload)
                is_last = True
            else:
                all_entries.append(payload)
                is_last = True

            page += 1
            if is_last:
                break

    output_path = Path("feature-runs") / "00-live-direct-api-technical-analysis.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(all_entries, indent=2), encoding="utf-8")

    print(f"Fetched {len(all_entries)} technical analysis entries across {page} page(s)")
    print(f"Wrote output to: {output_path}")


if __name__ == "__main__":
    main()
