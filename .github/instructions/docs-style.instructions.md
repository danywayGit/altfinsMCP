---
name: Docs Style
description: "Use when writing or updating README files, feature-runs markdown files, or setup documentation. Covers concise structure, evidence-first examples, and link-don't-duplicate rules for this altFINS MCP repo."
applyTo: "**/*.md"
---
# Documentation Style Rules

- Keep documentation practical and executable.
- Prefer concrete prompts and commands over abstract descriptions.
- For capability docs, include:
  - prompt used
  - tool invocation
  - output received (full when short, excerpt when large)
- Link existing docs instead of duplicating setup steps.

## Required Patterns In This Repo

- Main entrypoint stays in `README.md`.
- Script usage details stay in `examples/python/README.md`.
- Feature evidence stays in `feature-runs/*.md`.
- Live generated artifacts stay as:
  - `feature-runs/00-live-tool-catalog.md`
  - `feature-runs/00-live-direct-tool-call-output.json`

## Security

- Never include real API keys in docs.
- Use `ALTFINS_API_KEY` environment variable examples.
- Keep references aligned with `.gitignore` behavior for `.env`.
