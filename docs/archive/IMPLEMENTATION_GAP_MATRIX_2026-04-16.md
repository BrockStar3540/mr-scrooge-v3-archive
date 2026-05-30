> **ARCHIVED 2026-05-30.** This doc tracked doctrine-vs-code gaps as of
> 2026-04-16. Every entry below references either:
> (a) a gate that has since been retired (see ADRs 3008, 3017),
> (b) a strategy router architecture that no longer exists, or
> (c) a known bug that has since been fixed (the "Dashboard candidate truth"
>     gap was B-079, closed by Patch C / commit 64410a3 on 2026-05-27).
>
> The "doctrine says X vs code does Y" framing was useful when the V3.0
> doctrine doc was authoritative. With `docs/LIVE_SYSTEM_SPEC.md` as the
> executable truth and `docs/decisions/` as the rationale layer, this
> matrix is redundant and would be more confusing to maintain than not.
>
> Not replaced. Read `LIVE_SYSTEM_SPEC.md` to know what the system does;
> read the ADRs to know why.

---

# Implementation Gap Matrix

> Tracks what doctrine/docs claim vs what code actually does.
> Updated 2026-04-16. Keep this lean — update on every strategic code change.

---

| Area | Doctrine Says | Code Status | Gap | Priority |
|------|--------------|-------------|-----|----------|
| **Strategy routing** | Router selects allowed strategy set per BB state | Implemented. Reversal owns EXTREME/REJECTION, dbb_trend owns TREND/BREAKOUT, direct is fallback | Stale comments in router (fixed 2026-04-16) | Done |
| **DBB Trend Engine** | Breakout/pullback continuation with structural stops | Implemented. Two modes (BREAKOUT, PULLBACK), live in TREND/BREAKOUT/STRETCH_DOWN states | Old TrendStrategy still in codebase (disabled) | Low — keep for reference |
| **Family-aware scoring** | Scorer branches on strategy_family for overlays + thresholds | Implemented. Trend gets +6/+4/+2/+2/+3/-5 overlays, separate session thresholds | None — working as designed | Done |
| **Management profiles** | Profile-driven shared management (trend_runner vs reversal_core) | Implemented in position_pipeline. trend_runner: early_hold=0.6, step=4.0 | Only affects early_hold_r and min_sl_step. Ratchet/trail/harvest not yet profile-aware | Medium |
| **RR gate family** | Gate uses strategy family for min RR threshold | Implemented via candidate_family() helper. Trend=1.10, reversal=1.00 | None | Done |
| **Config/runtime parity** | Config describes live system | Config pruned to 3 live gates (2026-04-16). Matches runtime | None | Done |
| **Dashboard candidate truth** | Dashboard shows actual winner path after gates + scorer | Partial. scan_symbol_full() may take first candidate, not best scored | Verify pair-view mirrors live selection | High |
| **Runtime extraction** | Runtime is thin conductor | Implemented. 877→232 lines across 4 phases | None — 8 modules extracted | Done |
| **Recovery/reconciliation** | Robust restart-safe recovery | Implemented in state_recovery.py + bootstrap.py. Orphan detection, pending order reconciliation | No dedicated recovery tests | Medium |
| **Replay/comparison** | Replay harness for decision comparison | EventRecorder + EventReplayer exist. Not used for strategy comparison yet | No DBB vs reversal comparison tooling | Low |
| **Regime-strategy compatibility** | Regime should influence strategy eligibility beyond BLOCKED | Not implemented. Regime only contributes BLOCKED kill switch | Missing middle layer (planned in PLATFORM_DOCTRINE) | Medium |
| **Breakout continuation** | Future strategy for measured moves / vol compression | Not implemented. Placeholder in config (disabled) | Planned, not blocking | Low |

---

## Status Legend

- **Done** — implemented and verified
- **High** — should be addressed before adding new strategies
- **Medium** — important but not blocking current operation
- **Low** — planned future work, not urgent
