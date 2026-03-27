---
name: altfins-capability-refresh
description: 'Refresh altFINS MCP capabilities by running live tool discovery, regenerating 00-live artifacts, and syncing README links and capability notes. Use for capability updates, tool list drift checks, and release-day documentation refresh.'
argument-hint: 'Optional focus: full-refresh, live-catalog-only, or specific tool name'
user-invocable: true
---

# altFINS Capability Refresh

## When to use

- MCP tool set changed or may have changed.
- `README.md` capability section appears stale.
- Need regenerated evidence artifacts under `feature-runs/00-*`.

## Procedure

1. Validate environment prerequisites.
   - Confirm dependencies are installed from `requirements.txt`.
   - Confirm `ALTFINS_API_KEY` is set in the current terminal session.
2. Run live discovery script:
   - `.venv/Scripts/python.exe examples/python/altfins_direct_tool_call.py`
3. Verify generated artifacts exist and are current:
   - `feature-runs/00-live-tool-catalog.md`
   - `feature-runs/00-live-direct-tool-call-output.json`
4. Compare live discovered tools against README capability statements.
5. Update docs with link-first strategy:
   - Keep setup details centralized in `README.md` and `examples/python/README.md`.
   - Add or revise per-feature files only when needed.
6. Summarize changes and highlight newly discovered tools.

## Repository rules

- Do not commit secrets or raw API keys.
- Treat static tool lists as snapshots; live discovery is source of truth.
- Keep feature evidence files practical (prompt, invocation, output).
