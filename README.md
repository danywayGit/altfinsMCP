# altFINS MCP Server - Capabilities and Setup

This repository contains a ready-to-use local MCP configuration for the altFINS server, plus examples of what each capability does.

## What this MCP server gives you

The altFINS MCP server provides tools for:

- Crypto calendar events (upcoming token, exchange, and ecosystem events)
- Crypto news (sources and recent messages)
- Market screener data (snapshot metrics, filters, and available data types)
- Technical analysis data (indicator-driven views)
- Historical analytics (time-series indicator history)
- OHLC price history and latest candles

It can also expose additional tools depending on your server version (for example portfolio-related tools). The most reliable way to stay current is to query the live MCP server with `list_tools`.

## Live tool discovery (Python direct MCP)

To keep your feature list updated automatically, use the Python direct integration in this repo:

- `examples/python/altfins_direct_tool_call.py`
- `examples/python/README.md`

This script:

1. Connects directly to `https://mcp.altfins.com/mcp` with `X-Api-Key`.
2. Calls `list_tools` and exports current tools to `feature-runs/00-live-tool-catalog.md`.
3. Runs direct calls including:
	- `technicalAnalysis_getTechnicalAnalysisData` for all symbols by default (curated trade setups / analyst views)
	- `ohlc_getLatestData`
4. Saves raw direct-call output to `feature-runs/00-live-direct-tool-call-output.json`.

Optional symbol filter for technical analysis:

```powershell
$env:ALTFINS_TA_SYMBOLS="BTC,ETH,SOL"
```

Install Python dependencies for this script:

```powershell
pip install -r requirements.txt
```

Option A (shell variable in current terminal):

```powershell
$env:ALTFINS_API_KEY="YOUR_ALTFINS_API_KEY"
.venv/Scripts/python.exe examples/python/altfins_direct_tool_call.py
```

Option B (recommended, local `.env` file):

```powershell
Copy-Item .env.example .env
```

Then set `ALTFINS_API_KEY` in `.env`.

The live discovered tool inventory is generated in:

- `feature-runs/00-live-tool-catalog.md`

Use that generated file as the source of truth instead of a hardcoded list in this README.

## Tool capability map (with one example each)

Below is one practical example per capability/tool.

### 1) Analytics types discovery

- Tool: `mcp_altfins-mcp-s_analytics_getAnalyticsTypes`
- What it does: lists all valid analytics type identifiers you can query historically.
- Example request:

```text
Show all analytics types available from altFINS so I can pick one for historical analysis.
```

### 2) Latest analytics history for all symbols

- Tool: `mcp_altfins-mcp-s_analytics_getAllLatestHistoryData`
- What it does: fetches the latest available datapoint for a selected analytics metric across many symbols.
- Example request:

```text
Get the latest RSI14 history datapoint across all tracked symbols.
```

### 3) Historical analytics for one symbol

- Tool: `mcp_altfins-mcp-s_analytics_getHistoryData`
- What it does: returns time-series values for one analytics type and symbol.
- Example request:

```text
Get SMA50 historical values for BTCUSDT over the last 90 days.
```

### 4) OHLC history

- Tool: `mcp_altfins-mcp-s_ohlc_getHistoryData`
- What it does: returns historical OHLC candles for a symbol and timeframe.
- Example request:

```text
Get daily OHLC history for ETHUSDT for the last 6 months.
```

### 5) Latest OHLC candle(s)

- Tool: `mcp_altfins-mcp-s_ohlc_getLatestData`
- What it does: returns the most recent OHLC candle(s) for a symbol/timeframe.
- Example request:

```text
Get the latest 1h OHLC candle for SOLUSDT.
```

### 6) Crypto calendar events

- Tool: `mcp_altfins-mcp-s_getCryptoCalendarEvents`
- What it does: fetches scheduled crypto events.
- Example request:

```text
Show crypto calendar events coming in the next 7 days.
```

### 7) News sources

- Tool: `mcp_altfins-mcp-s_news_getCryptoNewsSources`
- What it does: lists supported news sources.
- Example request:

```text
List all available crypto news sources in altFINS.
```

### 8) News messages

- Tool: `mcp_altfins-mcp-s_news_getCryptoNewsMessages`
- What it does: returns recent crypto news messages.
- Example request:

```text
Get the latest 20 crypto news messages from all sources.
```

### 9) Screener data types

- Tool: `mcp_altfins-mcp-s_screener_getAltfinsScreenerDataTypes`
- What it does: lists available screener fields/columns you can query.
- Example request:

```text
Show all altFINS screener data types and their meanings.
```

### 10) Screener data

- Tool: `mcp_altfins-mcp-s_screener_getAltfinsScreenerData`
- What it does: returns screener results for selected filters/columns.
- Example request:

```text
Get screener data for top coins with bullish trend and volume above average.
```

### 11) Technical analysis data

- Tool: `mcp_altfins-mcp-s_technicalAnalysis_getTechnicalAnalysisData`
- What it does: returns curated trade setups and professional analyst views.
- Example request:

```text
Get technical analysis data for ADAUSDT on the 4h timeframe.
```

### 12) User portfolio

- Tool: `getUserPortfolio`
- What it does: returns the authenticated user's connected portfolio.
- Example request:

```text
Get my connected user portfolio from altFINS.
```

## Per-feature run files

Each capability execution (prompt + output) is saved in one file:

- [feature-runs/01-analytics-types.md](feature-runs/01-analytics-types.md)
- [feature-runs/02-latest-analytics.md](feature-runs/02-latest-analytics.md)
- [feature-runs/03-historical-analytics.md](feature-runs/03-historical-analytics.md)
- [feature-runs/04-ohlc-history.md](feature-runs/04-ohlc-history.md)
- [feature-runs/05-latest-ohlc.md](feature-runs/05-latest-ohlc.md)
- [feature-runs/06-calendar-events.md](feature-runs/06-calendar-events.md)
- [feature-runs/07-news-sources.md](feature-runs/07-news-sources.md)
- [feature-runs/08-news-messages.md](feature-runs/08-news-messages.md)
- [feature-runs/09-screener-data-types.md](feature-runs/09-screener-data-types.md)
- [feature-runs/10-screener-data.md](feature-runs/10-screener-data.md)
- [feature-runs/11-technical-analysis.md](feature-runs/11-technical-analysis.md)
- [feature-runs/12-user-portfolio.md](feature-runs/12-user-portfolio.md)

Live generated files from direct MCP discovery/calls:

- [feature-runs/00-live-tool-catalog.md](feature-runs/00-live-tool-catalog.md) (generated after running Python script)
- [feature-runs/00-live-direct-tool-call-output.json](feature-runs/00-live-direct-tool-call-output.json) (generated after running Python script)

## Local MCP configuration saved in this repo

This repo stores a working altFINS MCP config template at:

- `keep/altfins-mcp.json`

Copy it into your VS Code User MCP config (for example `%APPDATA%\Code\User\mcp.json`) and adapt as needed.

## Quick setup

1. Create a virtual environment (recommended):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Create your environment file from template:

```powershell
Copy-Item .env.example .env
```

4. Set your API key in `.env`:

```text
ALTFINS_API_KEY=your_real_api_key_here
```

5. Run live discovery:

```powershell
.venv/Scripts/python.exe examples/python/altfins_direct_tool_call.py
```

6. Open this folder in VS Code and ensure MCP support is enabled.

7. Reload the window (`Developer: Reload Window`) if the MCP server is not picked up immediately.

8. In Copilot Chat (agent mode), try one of the example prompts from this README.

## Notes

- If your altFINS MCP server config format changes, update `keep/altfins-mcp.json` and your VS Code User MCP config accordingly.
- Keep secrets in `.env` (or your OS secret store), not in committed files.