# Python direct MCP integration

This example connects directly to the altFINS MCP endpoint, lists all available tools, executes direct tool calls, and writes a live tool catalog.

## Prerequisites

- Python 3.10+
- altFINS API key

Create and activate a virtual environment (recommended):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
pip install -r requirements.txt
```

Set your API key in one of these ways:

Option A (recommended for this repo):

```powershell
Copy-Item .env.example .env
```

Then edit `.env` and set:

```text
ALTFINS_API_KEY=YOUR_ALTFINS_API_KEY
```

Option B (current shell only):

```powershell
$env:ALTFINS_API_KEY="YOUR_ALTFINS_API_KEY"
```

Run:

```powershell
.venv/Scripts/python.exe examples/python/altfins_direct_tool_call.py
```

## What it generates

- `feature-runs/00-live-tool-catalog.md` (live, current tool inventory from `list_tools`)
- `feature-runs/00-live-direct-tool-call-output.json` (raw output from direct tool calls)

## Included direct tool calls

1. `technicalAnalysis_getTechnicalAnalysisData` — **paginated**, fetches all pages automatically (page size 50)
2. `ohlc_getLatestData` with symbols `BTC,ETH,SOL`

Optional filter:

```powershell
$env:ALTFINS_TA_SYMBOLS="BTC,ETH,SOL"
```

If `ALTFINS_TA_SYMBOLS` is set, technical analysis is fetched only for those symbols.
Otherwise, all curated entries (~50) are fetched across multiple pages.

## Direct REST API example (no MCP)

Script:

- `examples/python/altfins_direct_api_technical_analysis.py`

This script calls:

- `https://altfins.com/api/v2/public/technical-analysis/data`

Run (all available entries):

```powershell
.venv/Scripts/python.exe examples/python/altfins_direct_api_technical_analysis.py
```

Optional single-symbol filter:

```powershell
$env:ALTFINS_TA_SYMBOLS="ADA"
.venv/Scripts/python.exe examples/python/altfins_direct_api_technical_analysis.py
```

Generated output:

- `feature-runs/00-live-direct-api-technical-analysis.json`

Curl equivalent:

```bash
curl -L "https://altfins.com/api/v2/public/technical-analysis/data" \
	-H "Accept: application/json" \
	-H "X-API-KEY: YOUR_API_KEY"
```

If you receive HTTP 403, your API key may be valid for MCP but not authorized for this direct REST endpoint.

Both the MCP and direct REST scripts paginate automatically (page size 50, stops at last page).

## Symbols list script

Script:

- `examples/python/altfins_symbols_list.py`

This script calls:

- `https://altfins.com/api/v2/public/symbols`

Run:

```powershell
.venv/Scripts/python.exe examples/python/altfins_symbols_list.py
```

Generated output:

- `feature-runs/00-live-symbols-list.json`

Returns the full list of 2000+ supported coin symbols from altFINS.
