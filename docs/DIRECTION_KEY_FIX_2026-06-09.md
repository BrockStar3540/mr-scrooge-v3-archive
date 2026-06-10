# Direction-key fix + amp re-pick — 2026-06-09

## The bug (months-long signal loss)
The pip_eater Play Book EV gate pooled **long + short** into one cell. The amp
factors are RAW (RSI/BBP/E50 **invert** by direction — a long wants high RSI, a
short wants low RSI), so pooling **cancelled a ±3–7p signal**. Example:
`alpha_pullback EUR align4 RSI5` = **long +4.51 / short −1.89**, but the pooled
cell read ~+2.76 — so a long passed and a short that should've been blocked also
passed (and vice-versa).

## Root cause
The **2026-06-07 playbook migration** replaced the old `pip_meal`/`matrix_meal`
lookups (which WERE keyed `(pair, strategy, direction, session)`) with
`playbook_ev_pairaware.csv` and **dropped the direction key**.

## Full direction audit — 9/10 layers were already correct
| Layer | Direction-aware before fix? |
|---|---|
| Factor engine — align cluster (H20/H60/T1/T4) | YES (normalized to candidate dir) |
| Factor engine — amp factors (RSI/BBP/ADR/…) | RAW (correct **iff** consumer keys on dir) |
| LightGBM v0 gate scorer | YES (`direction_exec` is a feature) |
| ml-observer model.xgb | YES (`direction_exec` in feature_order) |
| per_pair_modules regime layer | YES (key = `pair\|strategy\|direction\|…`) |
| optimized_matrix.csv (research) | YES (has `direction` column) |
| old pip_meal/matrix_meal lookups | YES (now deleted) |
| corpus / scans / order-attribution | YES |
| **playbook_ev_pairaware.csv + pip_eater EV gate** | **NO ← the one regression** |

## The fix (commit 9cc79b1)
- **Playbook regenerated split by direction** (4,230 rows). Faithful: 1581/1581
  cells reproduce the old pooled EV as the n-weighted long/short average.
- **Gate** (`pip_eater_gate.py`): load `groupby([pair,strategy,direction])`;
  lookup `(pair, strategy, direction)`. The gate already computed the candidate's
  direction (`_normalize_direction(candidate.direction)`) — it just wasn't using
  it for the EV key. Loads 224 keys (28 strat × 4 pair × 2 dir).

## Amp re-pick (direction-aware OOS keep-EV bake-off)
With direction now keyed, several strategies' RAW amps were no longer cancelled,
so the best amp changed. 5 changes validated (>0.10p OOS keep-EV margin):
- MR5_williams_extreme_short: ZS → **ADR** (3.64 → 4.43)
- TF2_pullback_EMA20_short: E50 → **RSI** (0.97 → 1.76)
- alpha_breakout_retest_v2: ADR → **RSI** (0.76 → 1.21)
- bravo_failed_momentum: ADR → **RSI** (0.80 → 0.94)
- echo_box_fade_v2: ADR → **RSI** (0.73 → 0.85)
charlie stayed ADR (RSI doesn't win it on keep-EV; the earlier charlie→ADR ship
was correct). ADR-amp strategies unchanged (ADR is direction-invariant).

## Status
Both live (playbook + gate restarted, 0 errors). Backups: `*.bak_pre_direction`,
`*.bak_*_direction_key`, `*.bak_pre_amp_repick`. The whole stack — factor engine,
gate, playbook, both ML models, per-pair modules, every matrix — is now
direction-consistent.
