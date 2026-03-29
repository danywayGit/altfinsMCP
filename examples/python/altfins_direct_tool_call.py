import asyncio
import json
import os
from datetime import datetime, timezone
from pathlib import Path

from dotenv import load_dotenv
from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client

ALTFINS_MCP_URL = "https://mcp.altfins.com/mcp"


def _extract_text_blocks(result) -> list[str]:
    blocks = []
    for item in getattr(result, "content", []) or []:
        text = getattr(item, "text", None)
        if text:
            blocks.append(text)
    return blocks


def _parse_blocks(blocks: list[str]) -> list[object]:
    parsed: list[object] = []
    for block in blocks:
        try:
            parsed.append(json.loads(block))
        except (json.JSONDecodeError, TypeError):
            parsed.append(block)
    return parsed


def _write_live_tool_catalog(tools, output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Live altFINS MCP Tool Catalog",
        "",
        f"Generated at: {datetime.now(timezone.utc).isoformat()}",
        "",
        "| Tool | Description |",
        "|---|---|",
    ]

    for tool in sorted(tools.tools, key=lambda t: t.name):
        description = (tool.description or "").replace("\n", " ").replace("|", "\\|")
        lines.append(f"|{tool.name}|{description}|")

    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


async def main() -> None:
    # Allow local .env usage while still supporting shell environment variables.
    load_dotenv()
    api_key = os.getenv("ALTFINS_API_KEY")
    if not api_key:
        raise RuntimeError("Set ALTFINS_API_KEY environment variable before running.")

    # Optional override (comma-separated symbols, e.g. BTC,ETH).
    ta_symbols = os.getenv("ALTFINS_TA_SYMBOLS", "").strip()

    headers = {"X-Api-Key": api_key}

    async with streamablehttp_client(ALTFINS_MCP_URL, headers=headers) as (
        read_stream,
        write_stream,
        _,
    ):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()

            tools = await session.list_tools()
            print("Available tools:")
            for tool in sorted(tools.tools, key=lambda t: t.name):
                description = (tool.description or "")
                short_description = description[:90] + ("..." if len(description) > 90 else "")
                print(f"  - {tool.name}: {short_description}")

            # --- Technical Analysis: paginate through all results ---
            ta_base_args: dict = {"size": 50, "sortField": "updatedDate", "sortDirection": "DESC"}
            if ta_symbols:
                ta_base_args["symbol"] = ta_symbols

            all_ta_entries: list = []
            page = 0
            while True:
                ta_args = {**ta_base_args, "page": page}
                technical_result = await session.call_tool(
                    "technicalAnalysis_getTechnicalAnalysisData",
                    arguments=ta_args,
                )
                blocks = _extract_text_blocks(technical_result)
                parsed = _parse_blocks(blocks)
                # Flatten: each parsed item may be a list of entries or a single entry
                for item in parsed:
                    if isinstance(item, list):
                        all_ta_entries.extend(item)
                    elif isinstance(item, dict):
                        all_ta_entries.append(item)
                # Stop if we got fewer items than page size (last page)
                page_count = sum(len(i) if isinstance(i, list) else 1 for i in parsed)
                page += 1
                if page_count < ta_base_args["size"]:
                    break

            if ta_symbols:
                print(f"\nCurated technical analysis for symbol: {ta_symbols}")
            else:
                print(f"\nCurated technical analysis for all available symbols:")
            print(f"  Total entries fetched: {len(all_ta_entries)} (across {page} page(s))")
            symbols_found = [e.get("symbol", "?") for e in all_ta_entries if isinstance(e, dict)]
            if symbols_found:
                print(f"  Symbols: {', '.join(symbols_found)}")

            ohlc_result = await session.call_tool(
                "ohlc_getLatestData",
                arguments={"symbols": "BTC,ETH,SOL", "timeInterval": "DAILY"},
            )
            print("\nLatest OHLCV for BTC, ETH, SOL:")
            for block in _extract_text_blocks(ohlc_result):
                print(block)

            raw_result = {
                "technicalAnalysis_getTechnicalAnalysisData": all_ta_entries,
                "technicalAnalysis_request": ta_base_args,
                "technicalAnalysis_pages_fetched": page,
                "technicalAnalysis_total_entries": len(all_ta_entries),
                "ohlc_getLatestData": _parse_blocks(_extract_text_blocks(ohlc_result)),
            }
            output_json = Path("feature-runs") / "00-live-direct-tool-call-output.json"
            output_json.parent.mkdir(parents=True, exist_ok=True)
            output_json.write_text(json.dumps(raw_result, indent=2), encoding="utf-8")

            catalog_path = Path("feature-runs") / "00-live-tool-catalog.md"
            _write_live_tool_catalog(tools, catalog_path)
            print(f"\nWrote live tool catalog to: {catalog_path}")
            print(f"Wrote direct call output to: {output_json}")


if __name__ == "__main__":
    asyncio.run(main())
