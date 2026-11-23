# Agents — 1C MCP Lib (onec-mcp-lib)

- **Scope:** personal
- **Registry ID:** `1c-mcp-lib`
- **Path:** `E:/Projects/personal/1c-mcp-lib`
- **Hub:** [dev-hub-personal](https://github.com/dorynkov/dev-hub-personal)

## Role

Shared Python library for sibling MCP servers (`1c-mcp-bsl`, `ssl`, `templates`, `docs`, `code-checker`, `data`).

## Read first

1. `pyproject.toml` — package name `onec-mcp-lib`
2. `src/` — `@tool_safe`, logging, diagnostics helpers

## Rules

- Breaking API changes require bump in all dependent MCP repos
- Not a standalone MCP server — no Docker compose here

## Personal infra (AdminTools)

Sibling repo (**not** kit): VPS, secrets, deploy — [personal-infra](https://github.com/dorynkov/dev-hub-personal/blob/main/docs/methodology/personal-infra.md).

- Path: `E:/Projects/personal/admin-tools` · override: `ADMINTOOLS_ROOT`
- Catalog: [admin-tools/AGENTS.md](https://github.com/dorynkov/admin-tools/blob/main/AGENTS.md)
