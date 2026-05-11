# Historical archive — V1/V2 institutional memory

This directory mirrors the V1/V2 era institutional memory layer from the Obsidian vault on EC2 (`/data/obsidian-vault/wiki/systems/scrooge-*`). The intent is durability: the **EC2 vault is the live navigation system**, this git directory is the **backup of record**.

## Layered storage model

| Layer | Role | Authoritative? |
|---|---|---|
| EC2 (`~/mr-scrooge-v3/` + live bot state + Obsidian vault) | Truth — the live system, the operator HUD | YES |
| GitHub `mr-scrooge-v3` repo | Backup of code + decision records + this history archive | No (mirror) |
| Obsidian vault (`/data/obsidian-vault/`) | Navigation, cross-linking, working notes | Vault is authoritative for navigation; files mirror to git on a snapshot basis |

If a file diverges between vault and this directory: the vault is newer.
This directory is re-mirrored on demand, not auto-synced.

## Files

| File | Scope |
|---|---|
| `evolution-timeline.md` | V1 → V2 → V3 chronological narrative (~Feb 2026 → Apr 2026) |
| `bug-catalog.md` | B-001 through B-074, organized by era. Box-drawing family (B-068 to B-074) added 2026-05-11. |
| `dead-ends-graveyard.md` | Rejected proposals, reverted experiments, applied fixes that may have been wrong — reconsider candidates |
| `backtest-sampling-proposal.md` | How to slice the v2 corpus output by era / regime / config. Priorities 1-7 (6-7 added 2026-05-11). |
| `box-bugs-and-validation-targets.md` | 7 box-drawing bugs forensic + 3 validation-target winning days for any backtest. |
| `v1-exec-summary-feb-2026.md` | Verbatim Feb 26 2026 doctrine document (recovered from Desktop trash) |

## Source files in the Claude-sessions archive

Several entries in `bug-catalog.md`, `dead-ends-graveyard.md`, and `box-bugs-and-validation-targets.md` cite a Claude-sessions index that points at private Dropbox files (`/Users/brock-mini-mac/Dropbox/LLM Sessions/Claude Sessions/trading - Mr Scrooge/`). The index itself is **vault-only** (`scrooge-claude-sessions-index.md`) — not mirrored here — because the underlying files are private operator-only material. Quotes extracted into ADRs and the catalog are sufficient context for a future reader who only has this repo.

## Vault wikilinks

Files use `[[scrooge-other-note]]` Obsidian wikilink format for cross-references. These render as plain text in git but are functional in the vault. Don't try to "fix" them by removing brackets — they're machine-readable for the vault layer.

## ADR cross-references

ADRs in `../decisions/` (1001-3001) have "Conversation evidence" sections appended (2026-05-11) for ADRs 1005, 1006, 1008, 1010 — verbatim quotes from the corresponding Claude sessions.
