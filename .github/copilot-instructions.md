# Project Guidelines

## Scope
This repository is a documentation-first workspace for altFINS MCP usage.

- Primary docs: `README.md`
- Python direct MCP example: `examples/python/altfins_direct_tool_call.py`
- Python example setup: `examples/python/README.md`
- Capability run outputs: `feature-runs/`

## Build and Test
There is no formal build or test suite yet.

Use these commands for validation work:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
.venv/Scripts/python.exe examples/python/altfins_direct_tool_call.py
```

If a virtual environment is used, prefer the repo venv interpreter:

```powershell
.venv/Scripts/python.exe examples/python/altfins_direct_tool_call.py
```

## Architecture
- `README.md` is the main entrypoint and should stay aligned with current MCP capabilities.
- `examples/python/altfins_direct_tool_call.py` is the source of truth for live capability discovery via `list_tools`.
- `feature-runs/00-live-tool-catalog.md` and `feature-runs/00-live-direct-tool-call-output.json` are generated artifacts from the Python script.
- `feature-runs/01-*.md` through `feature-runs/12-*.md` are human-readable capability execution records.

## Conventions
- Keep documentation practical and executable: every feature description should include a concrete prompt or command.
- Prefer linking existing docs over duplicating content:
  - setup and feature map in `README.md`
  - script-specific steps in `examples/python/README.md`
- Do not hardcode secrets in code or docs. Use environment variables (`ALTFINS_API_KEY`) and keep `.env` ignored.
- When updating capabilities, prefer live discovery (`list_tools`) over static lists.

## Pitfalls and Environment Notes
- The direct MCP script reads `ALTFINS_API_KEY` from either shell environment variables or `.env`.
- Tool availability can vary by server version/account permissions; treat static lists as snapshots.
- Generated files under `feature-runs/00-*` should be regenerated after capability changes.
