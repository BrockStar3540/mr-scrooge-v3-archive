# EUR_GBP Trading Module

Self-contained per-pair research module built from 6 months of lab trades.

## Layout
- `trade_serials.csv` — every lab trade with its 14-bucket serial + regime + session + W/L
- `regime_centroids.csv` — the 20 KMeans regimes (defined by 7 regime factors)
- `regime_session_grid.csv` — performance per (regime, session) cell
- `regime_session_wl_grid.csv` — W/L breakdown per cell
- `manuals/R??_Manual.md` — readable per-regime manual with refined WIN + LOSE rules
- `manuals/master_rules.csv` — every refined rule, indexed by regime
- `manuals/regime_summary.csv` — headline stats per regime
- `manuals/cross_regime_factors.csv` — bucket prevalence W vs L

## Self-contained
- `lib/factor_buckets.py` — local copy, no external imports
- `lib/build_pair_module.py` — the builder script (this folder is reproducible)

To rebuild from source:
    python3 lib/build_pair_module.py EUR_GBP

Built: 2026-05-31 15:07:44 UTC
Trades: 18,595  WR: 65.0%  Regimes: 20
Rules: 979 refined
