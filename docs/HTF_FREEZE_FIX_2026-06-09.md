# HTF (H20/H60) freeze fix — 2026-06-09

## Symptom
`H20` and `H60` factor buckets were stuck at `H20e`/`H60e` for ~months —
**100% `e` across 2327 live candidates** (both directions, all 4 pairs). Since
`align_score = count{H20∈(a,b), H60∈(a,b), T1==a, T4==a}`, the alignment the
gate filters on was effectively dead, and the same frozen buckets fed the
pip_eater cell lookup, the exit-brain signature (`exit_sig`), and the LightGBM
`p_win`. Four consumers, one broken input.

## Root cause
`features/matrix_features.py` computed `htf_pct_20/60` as a **1H [0..1]
range-position** via `_pct_position` — `(close − lo)/(hi − lo)` over N 1H bars.
But `factor_buckets._htf_align_score` (and the entire lab corpus the
matrix/model were trained on) expect a **signed DAILY N-day return**
(`htf_pct_20 = (Dclose_now − Dclose_20d_ago)/Dclose_20d_ago`). Reference impl:
`research/replay_lab/backtesting_py/strategy_wrappers.py` (`htf="D"`, lookbacks
`5/20/60/120` days). Feeding a [0..1] value into the ±0.005-scale, sign-based
bucketizer floors every candidate to the extreme bucket → frozen `e`.

The daily candles were **already in the snapshot** (`snapshot.candles["D"]`,
fetched by `scan_coordinator`) — the feature just used the wrong timeframe and
formula.

## Fix
- `matrix_features.compute`: derive `htf_pct_20/60` from `snapshot.candles["D"]`
  as 20-day / 60-day signed close returns; `htf_bias = sign`. Matches the
  corpus/`factor_buckets` contract exactly.
- `scan_coordinator`: fetch **130** daily candles (was default 50; the 60-day
  window needs > 60 bars).

## Validation
- Offline: recomputed H20/H60 for 16 live trades using the daily-return formula
  → **12/12 exact match** to the clean replay buckets.
- Post-deploy: live `align` now spans **0–4** (align=4 requires H20∈{a,b},
  impossible when frozen at `e`); zero `htf_pct` degraded markers.

## Deploy
`systemctl --user restart mr-scrooge-v3.service` (loads edited local source).
Backups: `*.bak_20260609_202019_htf_daily_fix` alongside each patched file.

## Note for downstream
`align_min` is still `0` in live config. Now that align is *correct*, raising it
(or wiring an `align × ADR` bucket filter — see the 8yr-validated factor-bucket
analysis) is the next lever. The LightGBM `p_win` feed should also widen from its
previously-compressed 0.5–0.7 range as corrected factors flow through.
