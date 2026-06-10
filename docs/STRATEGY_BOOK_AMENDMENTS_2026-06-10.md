# Strategy Book Amendments — 2026-06-10
Re-verification of the book's core tables against the canonical corpus (`scored_7yr.parquet`, 1,612,711 trades) and the LIVE config (HEAD f9d6499, p_win floor era). Verified by direct recompute, not memory.

## STILL ACCURATE (re-verified digit-for-digit today)
- **Align win-rate ladder**: 42.4 / 46.0 / 47.4 / 49.5 / 51.8 (ladder scoring) and 41.8 / 45.1 / 46.5 / 48.4 / 50.7 (SLTP). Exact match.
- **ADR flat on win rate** (48.8% → 47.0%): amplifier-not-gate framing holds.
- **XGBoost EV veto**: still armed in pip_eater (`data/ml-observer/model.xgb`, "PIP TRICK" veto), EV floor 1.25 unchanged.
- **OOS top-30% ≈ +2.94p**: independently reproduced 2026-06-10 by walk-forward LightGBM calibration (AUC .616, floor .45 → +1.73p avg on 66% kept; top slice ≈ +3p).
- **State-not-strategy (finding 6)**: stands; reinforced by the direction-keyed table (see Amendment 2).

## AMENDMENTS

### 1. Amplifier re-picks (direction-key fix, 2026-06-09/10) — 6 of 21 changed
| strategy | book said | live now |
|---|---|---|
| TF2_pullback_EMA20_short | E50b | **RSI** |
| MR5_williams_extreme_short | ZS3 | **ADR** |
| alpha_breakout_retest_v2 | ADR5 | **RSI** |
| charlie_compression_breakout | RSI6 | **ADR** |
| bravo_failed_momentum | ADR5 | **RSI** |
| echo_box_fade_v2 | ADR5 | **RSI** |
Cause: raw amp factors (RSI/BBP/E50/ZS) invert meaning by direction; the old pooled table averaged the two sides and cancelled ±3–7p. Pooled EV values for these rows are systematically UNDERSTATED. The live playbook is now keyed `pair × strategy × direction × align × amp` (`playbook_ev_pairaware.csv`) — never read EV off the pooled table again.

### 2. Direction asymmetry quantified (new, flag: pending OOS)
Aggregated n-weighted EV across cells at/above floor shows several name-encoded strategies carry their edge on the FLIP side (e.g. TF2_…_short: long +0.5..+1.5 vs short −1.0..−1.5; MR5: long +3.5..+4.7 vs short −3.4..−4.7; RG1_long: short side positive). Interpretation: the trigger (e.g. pullback-to-EMA20) marks a STATE; the state's geometry owns the direction — the name is historical. Matches miner-v2 flip-side opportunity cells. Treat as real-pending-OOS; the per-cell gate already prices it, but roster/naming decisions should not assume the named side is the edge side.

### 3. M(v) — the magnitude claim is STALE under the production exit
Book: "median winner +34p (ADR1) → +69p (ADR5)". Under the live green-exit ladder (`net_ladder`, what all current cells/models train on): mean winner +10.4p (ADR1) → +12.4p (ADR5), p90≈p99≈**18.5p = the ladder's mathematical max** (50%@+12, 25%@+20, 25%@+30). The exit ladder harvests away nearly all volatility amplification. The 34→69 figure was a pre-ladder raw-move metric. Consequence: "ADR drives magnitude" describes the market's OFFER, not current COLLECTION; this is the standing argument for MFE/path-label work (entry models trained on ladder-capped outcomes structurally hide the ADR edge).

### 4. Net-by-align table: cite the population
−0.72 → +1.77 (align 0→4) is the strategy's-OWN-side population. Pooled both-directions corpus: −1.01 → +1.23. Both true; the bot trades own-side so the book's numbers stand for live, but say which population is quoted.

### 5. The production decider is no longer just "EV ≥ +1.25"
As of 2026-06-10 live: EV ≥ 1.25 (direction-keyed playbook + XGB veto) **AND** p_win ≥ 0.45 (LightGBM, corpus-calibrated 06-10) **AND** htf-misalign block (counter-trend align-0) **AND** news blackout (CPI/NFP/FOMC/PPI calendar, −45m/+20m) **AND** dup guard (one position per pair-strategy-direction) **AND** per-pair cap 2, cooldowns, etc.

### 6. Finding 12 (sizing margin-bound) — OUTDATED
At current 1% risk / 12p SL, the RISK cap binds, not margin (live sizing: margin allowed 1.35M units, risk cap cut to 262k). Multi-pair book fits at current risk.

### 7. Pre-2026-06-09 live observations are broken-feed era
Live H20/H60 were frozen/wrong-scale until 2026-06-09 20:23 UTC (htf fix 6964295). All live WR/factor observations before then (incl. finding 11's 28% Monday) are measurements of a configuration that no longer exists. Corpus/offline analyses are unaffected (offline factors were always correct).

### 8. Data-quality flag
`scored_7yr.pnl_pips` is corrupt (values to 1e47). Nothing live reads it. Replaced properly by the corpus-v2 path-label rebuild.

### 9. New artifacts since the book's tables (all 2026-06-10)
- `data/lab_training/v1_candidate/`: honest walk-forward p_win model + isotonic + `calibration_report_2026-06-10.txt`
- `basekey_floor_table.csv` (426 keys: 328 FLOOR / 98 CULL) + `cell_culls.csv` (5,662 validated 2-factor bad cells)
- `miner_v2` map (3,944 cells) + opportunities + floor-band (610k trades @ +0.62p under the 1.25 floor)
- `config/econ_calendar.json` + news_blackout gate (26b32cf), dup guard (f9d6499)
- Updated direction-keyed book table: `strategy_book_2026-06-10_directionkeyed.csv` (this folder / sheet)
