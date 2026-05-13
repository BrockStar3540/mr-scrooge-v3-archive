# MS-001 + MS-002 Raw-M5 Replay — Verdict

Generated: 2026-05-13T05:45:31.208658+00:00

## TL;DR

**MS-001 strict-bin spec: KILL.** Zero raw-M5 candidates with strict bins.
**MS-001 loosened (BBW expanded): below deployment threshold.** 48 candidates total,
36% clean_2R discovery, holdout n=3 (statistically meaningless), BE@0.5R destroys it.
**MS-002 strict-bin spec: KILL.** Zero raw-M5 candidates.

**Methodological problem identified:** the winner-factory's bins describe
CORPUS PROBE-FIRED moments, not raw-chart conditions. Strict bin conjunctions don't
naturally occur on raw M5 bars at meaningful frequency.

## Why the bins don't fire on raw M5

MS-001 spec requires simultaneous:
- bb_position in [0.10, 0.35)  — price in lower band region
- |ema20_dist_pct| in [10, 30) — price 10-30 bps from EMA20
- bbw_a_bps in [5, 15)         — band width 5-15 bps
- echo_range_ratio in [1.0, 1.4) — current range 100-140% of recent avg

These are internally tight constraints on raw chart data. EMA20 distance of 10-30 bps
requires bands wider than 5-15 bps for bb_position to be inside the lower band at the
same time. The corpus has 82 EUR_USD rows matching the strict bins across 7 years
because each was a **probe-fired moment** — the probe triggers selected for specific
price-action setups that happened to satisfy this bin conjunction.

On raw M5 (every 5-minute bar regardless of probe), the conjunction never co-occurs.

## EUR_USD overlap_q2 raw distributions (vs corpus)

| Indicator | My raw-M5 median | Corpus EUR_USD 2024 median |
|---|---|---|
| bb_position | 0.51 | 0.52 (matches) |
| rsi | 50.1 | 49.9 (matches) |
| bbw_a_bps | **18.7** | **10.5** |
| ema20_dist_pct | 0.1 | 23.2 |
| echo_range_ratio | 1.03 | 0.88 |

Raw M5 has higher BBW and lower EMA distance than the corpus's probe-fired subset.
The corpus subset bias toward narrower BBW + higher EMA distance is because probes
typically fire when price has stretched far from a moving average BUT the volatility
regime is compressed (specific setup signature).

## MS-001 loosened (BBW [5, 30]) results

Total raw-M5 candidates across 8 usd_base pairs over 7 years: **48**

| Variant | era | n | mean R | win % | clean 2R % | exit profile |
|---|---|---|---|---|---|---|
| V0_TP2R_no_BE | discovery | 45 | +0.27 | 42% | **36%** | natural TP/SL |
| V0_TP2R_no_BE | holdout | 3 | 0.00 | 33% | 33% | n too small |
| V1_TP1.5R_no_BE | discovery | 45 | +0.17 | 47% | 16% | tighter target |
| V2_TP2R_BE_0.5R | discovery | 45 | -0.22 | 0% | 0% | **78% BE_stop** |
| V3_TP2R_BE_1.0R | discovery | 45 | -0.11 | 13% | 13% | 49% BE_stop |

**V0 discovery: 36% clean_2R rate is below MS-001's promotion threshold (47.1% per validation table).**
**Holdout n=3 is statistically meaningless.**
**BE variants destroy the rule** (78% of trades hit BE stop before reaching TP) — confirming the V3-era forensic finding that direction-asymmetric BE is too aggressive in production.

## MS-002 raw-M5: zero candidates

Spec: usd_base / long / asia_q3 / upper_band / RSI mid / EMA mid / BBW wide / echo expanded.
Zero raw-M5 candidates across all 8 pairs and 7 years. Same structural issue as MS-001 strict.

## The systemic finding

The winner factory operated on **corpus probe-fired rows** — sim trades that fired
because V2 probes triggered. Those rows have bin distributions biased by probe-trigger
conjunction (probes select for tight-volatility, far-from-mean setups). When we mine for
repeated winner shapes in this pre-filtered set, the bin combinations we find describe
the probe-fire conjunction, not natural chart conditions.

**The promoted microstrategy specs (MS-001 through MS-025) are NOT directly reproducible**
**as raw-chart entry rules.** They're descriptions of probe-fired conditions that
happened to win, not deployable bot rules.

## Recommended path forward (per Brock's principle: no probe filter)

**Option A (preferred): Re-run the winner factory on RAW M5 candidate generation.**
Instead of mining corpus probe-fired rows, generate candidates directly from raw M5:
- Define a generic candidate-fire rule that's RAW-chart only (e.g., 'M5 close crosses back inside lower BB band after touching')
- Forward-walk each candidate
- Bin the winners by entry-state, find repeated shapes
- This produces microbot specs that ARE reproducible on raw chart

Estimated cost: same compute as the original factory (~30 min) plus the candidate-
fire-rule design. Could be done in a fresh research session.

**Option B (less ambitious): Re-spec MS-001 through MS-025 with explicit price-action triggers.**
Each spec needs:
- bins (context filter)
- AND a trigger event (e.g., 'first M5 close inside band after wick touch')
Then test trigger-conditional bin matching.

**Option C (rejected): Loosen the existing bins.**
Loosened MS-001 generates 48 trades over 7 years with 36% clean_2R. That's below the
deployment bar (47.1% claimed) and frequency is too low to be operationally meaningful.

## What this validates

- Brock's directive ('don't use probe filters as the final answer') was the right rule.
- The winner-factory work is methodologically incomplete — the bins identified WIN-
  conditional shapes WITHIN the probe-fired space, but didn't validate that those
  shapes are observable IN raw-chart space.
- The Codex-generated 'PROMOTE_TO_RAW_M5_REPLAY' verdicts were premature — they passed
  the discovery/holdout statistical bar on corpus rows but didn't confirm the entries
  are reproducible.

## What this DOESN'T mean

- The trade-film ledger work is still valid (uses actual broker trades + manual + AI-curated)
- The factor lineage / era-split methodology is still valid
- The direction-asymmetric finding (longs run, shorts give back) is still valid as a research finding
- The V3 box-formation review is still valid (live V3 is fine)

## What's next

Honest options for Brock to choose:

1. **Re-run winner factory on raw-M5 candidate generation (Option A above)** — methodologically correct, ~1-2 sessions of work.
2. **Re-spec MS-XXX with triggers (Option B)** — case-by-case, slower but uses existing winner-shape research.
3. **Skip down the MS-list trying loose-bin variants** — likely to find more marginal-edge candidates without breakthrough.
4. **Accept the negative result and shift research focus** — back to trade-film ledger forensics or other unexplored areas.

## Verdict on MS-001 specifically

**STATUS: KILL.** Strict bins unfireable on raw M5; loosened version below deployment threshold.
Re-investigate with Option A or B before re-attempting.

## Verdict on MS-002 specifically

**STATUS: KILL.** Strict bins unfireable on raw M5 (same structural issue).

## Higher-level finding

This run validates the **'sim ≠ live'** principle one more time. The winner factory's
136 promoted cells were probe-fired-conjunction artifacts, not deployable rules. The
methodology to fix this is clear (Option A); it just needs to be run.