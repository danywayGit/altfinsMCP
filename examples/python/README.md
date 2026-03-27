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

1. `technicalAnalysis_getTechnicalAnalysisData` with symbol `BTC`
2. `ohlc_getLatestData` with symbols `BTC,ETH,SOL`
