# Updated ML-Lab Miner (v2) — HANDOFF for next session (2026-06-10)

## What it is
`lab_miner_v2.py` (Mini `~/` + repo `docs/` + Dropbox) — the matrix-miner updated to the
current config. **PURE ANALYSIS — NOT wired to the bot.** Reads `scored_7yr.parquet`,
keys **direction × align × amp** like the live direction-keyed playbook, scores on
**net_ladder** (green-exit ladder, not the old SL10/TP12), frames opportunities against
the **CURRENT** gates (per-strategy floor + align_min=0 + the +1.25 net EV floor + the
htf-misalign gate) — NOT the retired align_min=4.

## How to run (pure analysis, safe)
`python3 ~/lab_miner_v2.py` on the Mini → writes `~/miner_v2/{miner_map_v2, miner_opportunities_v2, miner_floorband_v2}.csv`.
Re-run whenever `scored_7yr.parquet` is rebuilt. Env: `SRC=` (corpus), `MINN=` (min n/cell, default 40).

## What it found (run 2026-06-10) — 3,944 cells (763 spine / 3,181 amp), book net_ladder +0.169p

### A. OPPORTUNITIES — +EV cells BELOW the per-strategy floor (27 cells, ~11k vol)
The mean-reversion / range strategies have **+2.0–3.0p net_ladder edge at align 0–1**
(their fade/range habitat), but the floors (2–3) exclude them:
- BR3_inside_bar_short SHORT align0 = +2.96 (floor 3)
- MR4_zscore_extreme_short LONG align1 = +2.92 (floor 2)
- RG1_range_bound_scalp_long SHORT align1 = +2.53 · CP2_squeeze_momentum_long LONG align0 = +2.46
- CP3_vol_coil_fade_short/long, CP1_coil_breakout_short align0/1 = +2.0–2.2
→ **candidate: lower the align floor for the fade/range strategies** (they don't need trend alignment).

### B. FLOOR-BAND — net-positive cells starved by the +1.25 EV floor (200 cells, ~610k vol, +0.62p mean)
In-playbook cells net-positive but under the floor → the gate rejects ~610k trades @ +0.62p.
Top sit at +1.2 (just under): MR2_short long align2, MR4_long short align2, bravo_expansion
long align4, alpha_pullback long align3/4.
→ **candidate: lower `pip_eater.floor_pips` 1.25 → ~0.75.**

## NEXT-SESSION steps (NONE applied — research candidates only)
1. **OOS the opportunities**: split `scored_7yr` ~2024 train/test; do the low-align fade cells
   in (A) hold out-of-sample? Low-align is give-back-prone — verify before trusting.
2. **Subtract the htf-misalign overlap**: the align==0 misaligned subset is already blocked
   (correctly); exclude those rows from (A) so we only chase genuinely-reachable cells.
3. **Model the floor drop** (B): 1.25 → 0.75 vs realized net over a session; the floor was the
   binding constraint (~75% of pip_eater blocks) and these cells are net-positive.
4. **Apply config-only if validated**: per-strategy floor via the playbook regen, or
   `pip_eater.floor_pips`. Commit + deploy + verify. **Do NOT auto-apply.**

## Artifacts
- Miner: `~/lab_miner_v2.py` (Mini), `docs/MINER_V2_*` (repo), Dropbox session folder.
- Outputs: `~/miner_v2/*.csv` (Mini) + Dropbox.  Source: `~/scored_7yr.parquet`.
- Old (v1) miner: `ml-lab/scripts/lab_miner.py` (SL10/TP12, align_min=4 framing — superseded).

**NOT wired to the bot. Pure analysis. The bot is unchanged.**
