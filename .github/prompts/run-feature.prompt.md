---
name: run-feature
description: "Run an altFINS MCP capability example and update the matching feature-runs file with prompt, invocation, and output evidence."
argument-hint: "Feature/tool name and optional parameters, e.g. technicalAnalysis_getTechnicalAnalysisData symbol=BTC"
agent: agent
---
Run the requested altFINS MCP feature and update documentation evidence in this repository.

## Inputs
- Requested feature/tool: ${input:argument}

## Required workflow
1. Map the feature to the existing file under `feature-runs/`.
2. Execute the MCP tool with realistic parameters matching the README example intent.
3. Record:
   - Prompt used
   - Tool invocation used
   - Output received
4. If output is large, include a concise excerpt and explicitly note it is truncated.
5. Ensure naming and style stay consistent with existing `feature-runs/01-*.md` to `feature-runs/11-*.md` files.
6. If a new feature is discovered, create the next numbered `feature-runs/*.md` file and add a link in `README.md`.

## Constraints
- Do not include secrets.
- Use `ALTFINS_API_KEY` only as an environment variable reference.
- Keep prose short and evidence-oriented.
