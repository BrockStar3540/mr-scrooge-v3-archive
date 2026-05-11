# 2003. V3 Scoring System — WR-Lift Hybrid with Pair Layer

**Status:** Accepted (live on V1 and V2 from 2026-04-15); foundation for V3 ML observer per-strategy filter
**Date:** 2026-04-15 (commit `c5b5cc3`)
**Version scope:** V2 (deployed simultaneously to V1 and V2)
**Backfilled:** 2026-05-11

## Context

By mid-April 2026, the original V1/V2 scoring formula was demonstrably weak:
- Separation between winners and losers: **+0.5 pts** (essentially noise)
- Never profitable at any threshold

A formal experiment was run: ten scoring formulas tested simultaneously on a 50-trade raw OANDA dataset (30 train / 20 test, chronological split).

The methodology (preserved in `SCORING_V3.md`):
- Data source: raw OANDA `/trades` API + raw D/H1/M5 candles at each trade's entry time
- 35-column feature table computed from raw candles, fully transparent (`pull_raw_data.py` logs every API call and calculation)
- Methods M1 through M10 evaluated by separation (winner score minus loser score) and out-of-sample P&L

Result summary (visible in `SCORING_V3.md` table):

| Method | Separation | Best P&L |
|---|---|---|
| M1 — Proportional gap | +46.2 | +$268 |
| M2 — WR-weighted | +51.0 | +$237 |
| M3 — Binary vote | +30.0 | +$236 |
| M6 — Top-5 factors max weight | +61.7 | +$198 |
| **Selected — WR-Lift Hybrid + Pair Layer** | **+82.9 train / +75.1 test** | **+$189 train / +$144 test** |

The selected formula achieved **100% WR at threshold ≥5 on the 20-trade OOS test set** (9W/0L; 8/8 losers blocked).

## Decision

Adopt the WR-Lift Hybrid with Pair Layer as the live scoring formula for V1 and V2 (and as the foundation for V3 work to follow).

The formula has two layers:
1. **Layer 0 — Hard blocks** (automatic reject): e.g. RSI 45-55 (no directional conviction, 29-50% WR in neutral zone)
2. **WR-lift scoring** with per-pair adjustments

(Full formula in `SCORING_V3.md` in `BrockStar3540/mr-scrooge`. Cross-referenced because the math is large and the implementation lives in V3 — see ADR 3001 cross-references.)

## Alternatives considered

- **Stay with old formula** — rejected; +0.5 separation is noise.
- **M6 (best separation)** — considered. Slightly higher train separation but lower P&L; selected was more robust on test.
- **Ensemble of multiple methods** — rejected for V2; reintroduced conceptually in V3's "ML observer + deterministic probe library" combo.

## Consequences

**Enabled:**
- 100% WR at threshold ≥5 on OOS → a credible filter that doesn't bleed.
- Per-pair adjustment layer recognizes that EUR/USD and GBP/JPY have different factor distributions.
- Foundation for the V3 per-strategy ML edge work (`dbb_trend` AUC 0.774 at p≥0.5) — same per-strategy mental model.

**Closed:**
- Single global-weight scoring (V1's original approach). The pair-aware formula is a partial step toward what V3 makes explicit per-regime (ADR 3001).

**Costs:**
- 100% WR on 9 trades is a *very small* sample. The formula was deployed knowing this. Subsequent live performance was mixed; led to the May 2026 reframing (regime-aware in ADR 3001).

## Survival into V3

The V3 ML observer (`scrooge_v3/advisors/ml_observer/`) maintains the per-pair adjustment layer and extends it to per-strategy (dbb_trend AUC 0.774 found 2026-04-28).

ADR 3001 supersedes this scoring system as the *primary* decision axis. V3 keeps WR-lift hybrid as a satellite filter, not the primary gate.

## Cross-references

- `SCORING_V3.md` in `BrockStar3540/mr-scrooge`
- Commit `c5b5cc3` — V3 scoring system go-live
- ADR `3001-regime-aware-not-global-score.md` — what came after this
- ML per-strategy edge: memory note (2026-04-28)
