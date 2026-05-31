# Strategy Encyclopedia

The reference document for all ~25 trading strategies in Mr. Scrooge
V4. Each strategy gets the same template and equal footing. No
strategy is the "main one"; the routing table decides which fires for
which (pair × regime × session) cell.

Companion to [`LIVE_SYSTEM_SPEC.md`](LIVE_SYSTEM_SPEC.md) (what the
system does today) and [`RESEARCH_METHODOLOGY.md`](RESEARCH_METHODOLOGY.md)
(how strategies got measured).

---

## How to use this doc

**If you're picking a strategy to trust** — read the lab numbers and
the limitations. Lab data measures behavior over the Nov 2025 →
May 2026 corpus; live transferability is not guaranteed.

**If you're adding a strategy** — copy the template below, follow the
fields, run it through the lab, and add the entry. The
[lab reproduction guide](LAB_REPRODUCTION_GUIDE.md) covers the steps.

**If you're debugging a live trade** — check the strategy's failure
modes first, then cross-reference the regime + session in
`order-attribution.jsonl` to find the matching cell in the routing
table.

---

## Per-strategy template

Every entry has the same 9 fields:

1. **Name + canonical strategy_id** — the string used in
   `order-attribution.jsonl`, ML observer logs, and routing table.
2. **Family** — one of: reversion / continuation / box / breakout /
   other. Affects which other strategies share its routing-cell space.
3. **Signal philosophy** — one paragraph on what market behavior the
   strategy tries to capture.
4. **Probe code reference** — path to the strategy module + the entry
   conditions in pseudocode.
5. **Stop / TP geometry + management profile** — exit shape.
6. **Lab-measured behavior** — corpus WR, expected pips, pair
   coverage (X/27), regime applicability (X/20), direction asymmetry
   (native vs reversed).
7. **Live behavior** (if applicable) — recent broker-truth slice.
8. **Known limitations / failure modes** — when this strategy is
   known to misfire.
9. **Related strategies** — see-also references.

---

## Taxonomy summary

All ~25 strategies at a glance. Lab numbers are corpus aggregates;
see per-entry detail for breakdowns.

| Strategy | Family | Routed live | Lab WR | Lab pair coverage | Status |
|---|---|---|---|---|---|
| [box_master_theory](#box_master_theory) | box | ✓ | 81% | 27/27 | Current — V1 lineage, now equal footing |
| [dbb_trend](#dbb_trend) | continuation | ✓ | 77% | 27/27 | Current — V3 family workhorse |
| [direct](#direct) | other | ✓ (fallback) | 82% | 27/27 | Current — fallback admission path |
| [reversal](#reversal) | reversion | registered (rarely routes) | n/a | **0/27 in matrix** | **Coverage gap** — see entry |
| [trend](#trend) | continuation | sidelined | 80% | 27/27 | Legacy V3 family — V4 deletion candidate (see entry) |
| [trend_aligned_breakout](#trend_aligned_breakout) | breakout | conditional | 72% | 20/27 | HTF-confluence breakout, narrow coverage |
| [canonical_lien_dbb](#canonical_lien_dbb) | continuation | ✓ | 78% | 25/27 | Current — DBB derivative |
| [canonical_darvas](#canonical_darvas) | box | conditional | **n/a** | **0/27 in matrix** | **Coverage gap** — see entry |
| [trend_pullback](#trend_pullback) | continuation | ✓ (promoted 2026-05-27) | 81% | 27/27 | Current |
| [chaikin_macd_atr](#chaikin_macd_atr) | continuation | ✓ (promoted 2026-05-27) | 81% | 27/27 | Current |
| [compression_expansion](#compression_expansion) | breakout | ✓ (promoted 2026-05-27) | 80% | 27/27 | Current |
| [compression_reversion](#compression_reversion) | reversion | ✓ (promoted 2026-05-27, **regime-mismatched**) | tiny n | n/a | Entry pending Phase 3 |
| [ifvg](#ifvg) | other (inverse FVG) | ✓ (promoted 2026-05-27) | 81% | 27/27 | Current |
| [session_breakout](#session_breakout) | breakout | ✓ (promoted 2026-05-27) | 80% | **8/27** | Current — narrow pair coverage |
| BR2_vcb (long + short) | breakout | sidelined | ~62% lab | 27/27 | Phase 3 lab winner, **promotion pending** |
| BR3_inside_bar | breakout | sidelined | 63% lab / loser | 27/27 | Phase 3 lab loser — drop candidate |
| BR5_opening_range_breakout (long + short) | breakout | sidelined | ~61% lab | 27/27 | Phase 3 lab winner, promotion pending |
| CP1_coil_breakout (long + short) | breakout | sidelined | ~62% lab | 27/27 | Phase 3 lab winner, promotion pending |
| CP2_squeeze_momentum_long | breakout | sidelined | ~62% lab | 27/27 | Phase 3 lab winner, promotion pending |
| CP3_vol_coil_fade (long + short) | reversion | sidelined | wrong-direction | 26-27/27 | Run reversed, promotion pending |
| MR2_bb_reversion_short | reversion | sidelined | wrong-direction | 27/27 | Run reversed, promotion pending |
| MR4_zscore_extreme (long + short) | reversion | sidelined | wrong-direction | 23-27/27 | Run reversed, promotion pending |
| MR5_williams_extreme (long + short) | reversion | sidelined | wrong-direction | 27/27 + narrow timing | Cautious promotion candidate |
| RG1_range_bound_scalp (long + short) | reversion | sidelined | wrong-direction | 27/27 | Run reversed, promotion pending |
| TF2_pullback_EMA20 (long + short) | other (pullback) | sidelined | wrong-direction | 27/27 | Run reversed, promotion pending |

**Coverage note:** "Lab WR" for current-routed strategies = corpus-mining
weighted aggregate from matrix. "Lab WR" for Phase 3 sidelined variants =
sweep-aggregate at default exit config. Lab numbers tied up in Phase 3
sweep completion (ETA Sun late / Mon AM 2026-05-31 / 06-01); entries
fill in as data lands.

---

## Glossary

- **Family** — the strategy's behavioral category. Determines routing-cell
  sharing (e.g., two continuation strategies compete for the same cells).
- **Routed live** — whether the strategy is admitted by the live MatrixRouter
  via the current `routing_table.parquet`. Some strategies are registered
  but not currently routed (`trend`, `reversal` currently).
- **Lab WR** — win rate over the 6mo corpus, weighted by trade count.
- **Pair coverage** — for how many of the 27 pairs the strategy generates
  enough trades to mine meaningful rules (>5 trades typically).
- **Regime applicability** — out of 20 KMeans regimes per pair, how many
  the strategy generates trades in.
- **Native / reversed** — Phase 3 lab tests each probe in both directions
  (the probe's coded direction, and its inverse). Direction asymmetry
  shows whether the probe is correctly directioned for the corpus regime.

---

# Strategy entries

---

## box_master_theory

**Family:** box (single-member family — only `box_master_theory` and
`canonical_darvas` qualify as box-shape strategies; everything else
is continuation/reversion/breakout flavored)

**Signal philosophy.** The original Mr. Scrooge V1 doctrine
([`MASTER_THEORY_v1-box-reversal-origin-2025.md`](archive/MASTER_THEORY_v1-box-reversal-origin-2025.md)
in the archive — the foundational document that defined the bot
through April 2026). The premise: each trading day forms a high-low
"box" (PDH / PDL). Liquidity sweeps at the box edges, followed by a
3-5-candle "sucker move" and a pitchfork-shaped entry pattern, signal
a reversal opportunity back toward the opposite box edge.

In V4, this is one of ~25 strategies and gets evaluated by the same
admission pipeline as everything else. The historical "this is THE
strategy" framing is preserved in `MASTER_THEORY_v1-box-reversal-origin-2025.md`;
operationally, `box_master_theory` is just an entry in the registry.

**Probe code reference.** `src/scrooge/strategies/box_master_theory.py`

Pseudocode:
```
candidate = box_master_theory.evaluate(symbol, features):
  if no PDH/PDL detected for symbol today:
    return None
  if not at_box_edge(features, proximity=0.25%):
    return None
  if not sucker_move_present(features, lookback=5, min_count=3):
    return None
  if not pitchfork_pattern(features.candles[-3:]):
    return None
  if not bb_exhaustion(features):
    return None
  direction = away_from_box_edge(features)
  return Candidate(symbol, direction, entry, stop, target)
```

**Stop / TP geometry + management profile.**
- Stop: signal candle extreme + buffer (typically 7p)
- TP1: 50% to mid-box (harvest)
- TP2: opposite box edge
- Management: `trend_runner` (`early_hold_r=0.6, min_sl_step_pips=4.0`)
  for trend-aligned firings; default for reversion-firings.

**Lab-measured behavior (6mo corpus, matrix-mined):**

| Direction | n_optimized | weighted WR | weighted exp_pips | weighted lift_pips |
|---|---|---|---|---|
| long | 7,114 | 81.2% | 6.37 | 3.84 |
| short | 6,444 | 80.7% | 6.62 | 4.17 |

- 27/27 pair coverage
- 184 long cells + 180 short cells in the matrix
- Direction-symmetric — works both ways (consistent with reversal
  thesis — boxes form in any direction)

**Live behavior.** Routed live since V3 launch (2026-04-15). Per the
2026-05-30 27-day broker-truth audit: low live volume relative to
other live strategies (most fires happened pre-routing-table promotion).

**Known limitations / failure modes.**
- Box detection requires clean PDH/PDL geometry; range-bound days
  with multiple equal highs/lows confuse the detector
- Counter-trend bet by construction; bleeds in strong directional days
  unless the HTF gate ([ADR 3015](decisions/3015-htf-trend-filter-observe-to-hard.md))
  catches the directional alignment failure
- "Sucker move" detection has historically had high false-positive
  rate on choppy markets — the 3-5 candle window is permissive

**Related strategies.**
- `canonical_darvas` — different box construction (rolling N-day high)
- `reversal` — same reversion philosophy at non-box levels
- `compression_reversion` — same reversion intent at compressed-volatility moments

---

## dbb_trend

**Family:** continuation (the V3 family workhorse for trend-aligned
trades; routes into TREND_UP/DOWN, BREAKOUT_UP/DOWN, STRETCH_DOWN
historical BB states though those state mappings are subsumed by the
matrix router now).

**Signal philosophy.** Double Bollinger Band trend continuation. The
DBB strategy identifies two pattern types: **breakouts** (price closes
beyond the outer band signaling trend acceleration) and **pullbacks**
(price retraces to the inner band in an established trend, then
resumes). The strategy emits long candidates in uptrending DBB states
and short candidates in downtrending DBB states.

**Probe code reference.** `src/scrooge/strategies/dbb_trend.py`

Pseudocode:
```
candidate = dbb_trend.evaluate(symbol, features):
  bb_state = classifier.bb_state(features)  # TREND_UP/DOWN/BREAKOUT_UP/DOWN/STRETCH_DOWN

  if bb_state in {BREAKOUT_UP, BREAKOUT_DOWN}:
    mode = "BREAKOUT"
    direction = "long" if bb_state == BREAKOUT_UP else "short"
  elif bb_state in {TREND_UP, TREND_DOWN}:
    mode = "PULLBACK"
    direction = "long" if bb_state == TREND_UP else "short"
  elif bb_state == STRETCH_DOWN:
    mode = "BREAKOUT" ; direction = "short"
  else:
    return None

  return Candidate(symbol, direction, entry, stop, target)
```

**Stop / TP geometry + management profile.**
- Stop: structural (last swing low for longs / high for shorts)
- TP: variable based on mode (BREAKOUT goes for runners; PULLBACK
  takes 2R then trails)
- Management: `trend_runner` (`early_hold_r=0.6, min_sl_step_pips=4.0`)

**Lab-measured behavior (6mo corpus, matrix-mined):**

| Direction | n_optimized | weighted WR | weighted exp_pips | weighted lift_pips |
|---|---|---|---|---|
| long | 3,296 | 78.2% | 5.90 | 3.11 |
| short | 3,629 | 76.4% | 5.71 | 3.39 |

- 27/27 pair coverage
- 102 long cells + 113 short cells in the matrix
- Direction-symmetric within ~2pp

**Live behavior (27d broker-truth slice ending 2026-05-29):**
- 31 trades, 19% WR, sum −$6,659 (mean −$215/trade)
- Sub-variants firing: `DBB1_buy_zone_long` (0/6 W), `DBB2_buy_zone_confirmed_long`
  (0/7), `DBB3_buy_zone_sustained_long` (1/12), `DBB1_sell_zone_short` (1/5)
- The long-bias sub-variants (`*_buy_zone_long`) lost catastrophically in
  the bearish-friendly regime that dominated this 27d window
- The short-bias sub-variant `DBB3_sell_zone_sustained_short` was
  positive (6/13 W, +$269)

**Known limitations / failure modes.**
- Strongly regime-dependent: catastrophic when the prevailing trend
  reverses against the BB state's bias (the $5,350 streak diagnosed
  2026-05-04 was a `dbb_trend` family failure mode of this type)
- HTF gate (ADR 3015) is the structural fix — blocks counter-HTF
  direction admissions
- Sub-variant `_buy_zone_long` distribution showed 1/25 wins (4% WR)
  in the post-promotion window — under per-strategy audit

**Related strategies.**
- `canonical_lien_dbb` — DBB-derived simpler variant
- `trend_pullback` — non-DBB version of the pullback pattern
- `compression_expansion` — different breakout shape

---

## direct

**Family:** other (the fallback admission path — when no other
strategy emits a candidate but the matrix has WIN rules for the
current state, `direct` emits a generic candidate that the rules
themselves admit).

**Signal philosophy.** A backstop. Where strategies like
`box_master_theory` or `dbb_trend` only fire on specific patterns,
`direct` fires on any state where the matrix-mined rules say "this
combination of signature buckets has high WR." The strategy is
intentionally permissive at emission; the routing table + LightGBM gate
do the actual selection.

**Probe code reference.** `src/scrooge/strategies/direct.py`

Pseudocode:
```
candidate = direct.evaluate(symbol, features):
  for direction in ['long', 'short']:
    if matrix_router.has_admitted_cell(symbol, features, direction):
      return Candidate(symbol, direction, entry_at_market, stop, target)
  return None
```

**Stop / TP geometry + management profile.**
- Stop: ATR-based (default 1.5 × ATR_5m)
- TP: matrix-mined cell's mean R_optimized × ATR_5m
- Management: `default` (`early_hold_r=0.5, min_sl_step_pips=3.0`)

**Lab-measured behavior (6mo corpus, matrix-mined):**

| Direction | n_optimized | weighted WR | weighted exp_pips | weighted lift_pips |
|---|---|---|---|---|
| long | 5,990 | 83.2% | 7.05 | 4.47 |
| short | 5,943 | 81.6% | 6.80 | 4.45 |

- 27/27 pair coverage
- 173 long cells + 176 short cells in the matrix
- **Highest weighted WR in the matrix** (83% long / 82% short) —
  unsurprising since `direct` admissions are filtered to the
  highest-WR cells by construction

**Live behavior (27d broker-truth slice ending 2026-05-29):**
- 73 trades, 30% WR, sum −$13,052 (mean −$179/trade)
- Highest-volume strategy in the live broker truth window
- Net negative despite the highest lab WR — consistent with the bearish
  regime favoring shorts (the lab WR aggregates across regimes that
  weren't all present in the 27d live window)

**Known limitations / failure modes.**
- "Highest-volume + lowest realized WR" is the classic signature of a
  permissive emitter caught in a regime mismatch — the cells the matrix
  admitted aren't the cells the live regime is producing
- Reliance on matrix WIN rules means `direct` only fires when LightGBM
  ALSO admits; the failure mode is when LightGBM scores high (0.75+)
  but the realized regime isn't the historical regime that produced
  the WIN rule

**Related strategies.**
- All routed strategies share cells with `direct` — when a more
  specific strategy emits, it takes priority in scoring

---

## reversal

**Family:** reversion

**Signal philosophy.** The V3 family for sweep-reversal trades at
non-box levels — Bollinger Band extremes, RSI extremes, generic
liquidity-sweep-and-reject patterns. EXTREME and REJECTION mode
sub-variants. Conceptually the broader version of `box_master_theory`'s
reversal logic, applied to any level that produces a sweep + rejection.

**⚠️ Coverage gap.** As of 2026-05-30, `reversal` family **has no
entries in the lab matrix or per-pair modules.** The strategy is
registered in `bootstrap.py` and would be routed if the routing table
had cells for it, but the matrix was mined on a corpus that didn't
include `reversal`-family trades.

This is a known gap, queued for fix in [Task #41](https://github.com/BrockStar3540/mr-scrooge-v3/issues/41)
(Phase 3 module rebuild). Until then, `reversal` candidates that emit
are essentially abstained on by the live router (no admitted cells).

**Probe code reference.** `src/scrooge/strategies/reversal.py`

Pseudocode (abbreviated):
```
candidate = reversal.evaluate(symbol, features):
  mode = detect_mode(features)  # EXTREME or REJECTION
  if mode is None: return None
  direction = opposite_of_extreme(features)
  return Candidate(symbol, direction, entry, stop, target)
```

**Stop / TP geometry + management profile.**
- Stop: signal-candle extreme + buffer
- TP: variable based on mode
- Management: `reversal_core` (`early_hold_r=0.5, min_sl_step_pips=3.0`)

**Lab-measured behavior.** **n/a — strategy not in lab corpus.**

**Live behavior (27d broker-truth slice).** **0 trades.** The strategy
was registered but never routed during the 27d window (no admitted
cells in the routing table for `reversal`).

**Known limitations / failure modes.**
- The current "structural coverage gap" is itself the most important
  limitation. Until the strategy is in the matrix, we have no
  data-mined edge measurement for it
- Historically (V1/V2 era) reversal trades had ~75% WR on the
  documented NORMAL-regime cohort, but this is from the legacy
  hand-tuned doctrine, not the V4-era lab corpus
- Once added to the lab corpus + matrix in [Task #41], the encyclopedia
  entry will be updated with measured behavior

**Related strategies.**
- `box_master_theory` — reversal at PDH/PDL levels specifically
- `compression_reversion` — reversal at compressed-volatility moments
- `ifvg` — reversal into Fair Value Gap fills

---

## canonical_lien_dbb

**Family:** continuation (DBB-derived; simpler variant of `dbb_trend`
focused on the structural-stop side of the entry rather than the
breakout/pullback mode distinction).

**Signal philosophy.** A leaner DBB strategy. Where `dbb_trend`
branches on breakout vs pullback modes, `canonical_lien_dbb` uses a
single entry condition: price tags an outer Bollinger band and
the prior swing-low/high provides the structural stop (the "lien"
the trade is filed against). Routes shorter pullback geometries than
the breakout-flavored `dbb_trend`.

**Probe code reference.** `src/scrooge/strategies/canonical_lien_dbb.py`

**Entry conditions — long (all must hold):**
- Prior 3 bars (excluding current) had a high above the upper Bollinger band (`upper_a`, 2σ) — i.e., the 2σ band was tagged or broken
- Current `bb_position` is in `(0.5, 1.0)` — price has pulled back from upper extreme but holds above the midline
- Current bar is a **bullish bar** (continuation candle)
- `RSI14 < 68` — not overbought

**Entry conditions — short (mirror):**
- Prior 3 bars had a low below the lower Bollinger band (`lower_a`, 2σ)
- `bb_position` in `(0.0, 0.5)` — pulled back from lower extreme, still below midline
- Current bar is **bearish**
- `RSI14 > 32` — not oversold

**Stop / TP geometry + management profile.**
- Stop: prior swing low (long) / high (short) + small buffer
- TP: variable; matrix-cell driven
- Management: `default` (`early_hold_r=0.5, min_sl_step_pips=3.0`)

**Lab-measured behavior (6mo corpus, matrix-mined):**

| Direction | n_optimized | weighted WR | weighted exp_pips | weighted lift_pips |
|---|---|---|---|---|
| long | 4,177 | 79.7% | 6.16 | 3.41 |
| short | 4,197 | 76.4% | 5.60 | 3.42 |

- **25/27 pair coverage** (two pairs missing — likely thin lab data)
- 123 long + 125 short cells in the matrix
- Direction-symmetric — slight long-side advantage on exp_pips

**Known limitations / failure modes.**
- 2 pairs without matrix data — admission for those pairs will be
  abstained until next module rebuild (Task #41) fills coverage
- Same regime sensitivity as `dbb_trend` — counter-trend bets on
  strong directional days bleed unless HTF gate catches misalignment

**Related strategies.**
- `dbb_trend` — same DBB family, different entry-mode logic
- `trend_pullback` — non-DBB pullback equivalent

---

## canonical_darvas

**Family:** box (Darvas-style rolling-N-day box construction)

**⚠️ Coverage gap.** No matrix data, no factor_lift_table data as of
2026-05-30. Strategy is registered in `bootstrap.py` but absent from
the lab corpus mining. Same gap pattern as `reversal` — queued for
Task #41 (Phase 3 module rebuild).

**Signal philosophy.** Nicolas Darvas's box theory adapted for forex.
Rolling N-day highs / lows form a "box" the price action stays inside
until a breakout. Long when price closes above the box top; short on
box-bottom breakdown. Differs from `box_master_theory` in that the
box construction is rolling-N (not previous-day-only) and the trade
direction is breakout (not reversal).

**Probe code reference.** `src/scrooge/strategies/canonical_darvas.py`

**Entry conditions (all must hold):**
- 40+ M5 bars available; ATR(14) + EMA50 features present
- A Darvas box exists for the configured `hold` window (e.g., 7-bar, 12-bar)
  - Long: box `top` = local high; box `bottom` = matching low established later
  - Short: mirror (box bottom established first)
- Box is fresh: `(current_bar_idx − box_set_idx) ≤ max_stale_bars`
- Box height ≥ `max(min_box_pips × pip, min_box_atr × ATR14)` — meaningful range, not micro-noise
- Trend filter (if enabled per variant): long requires `close > EMA50`, short requires `close < EMA50`
- **Breakout trigger:**
  - Long: `current_close > box_top + (entry_buffer_atr × ATR14)` AND `prev_close ≤ box_top + buffer` (just-now break)
  - Short: mirror with box_bottom
- `risk_reward ≥ min_rr` (typically 1.2)

**Stop / TP geometry + management profile.**
- Stop: opposite edge of the box
- TP: box-height projection beyond the breakout
- Management: `default`

**Lab-measured behavior.** **n/a — strategy not in lab corpus.**

**Live behavior.** Routed conditionally when matrix has no cells.
Effectively dormant in current live deployment.

**Known limitations / failure modes.**
- Coverage gap is the primary limitation; cannot make confident
  admission decisions without lab-mined factor lift
- Like `box_master_theory`, sensitive to noisy box geometry on
  range-bound days

**Related strategies.**
- `box_master_theory` — different box construction (PDH/PDL)
- `compression_expansion` — different breakout shape (vol-coil)

---

## chaikin_macd_atr

**Family:** continuation (momentum-confluence trend-follow)

**Signal philosophy.** Triple-confluence trend continuation. The
strategy fires when Chaikin Money Flow (volume-weighted accumulation/
distribution) AND MACD histogram AND ATR-normalized momentum all
align in the same direction. Conceptually the "everything points the
same way" version of trend-follow — sacrifices entry frequency for
confluence-driven WR.

**Probe code reference.** `src/scrooge/strategies/chaikin_macd_atr.py`

**Entry conditions (all must hold):**
- 27+ M5 bars (MACD's binding requirement); plus volume column present
- **Chaikin Money Flow bias (CMF):** computed over `cmf_window` (default 20)
  - Long requires `CMF > 0` (accumulation)
  - Short requires `CMF < 0` (distribution)
  - `CMF == 0` → no signal
- **MACD trigger (12/26/9):** cross of MACD line over signal line
  - Long requires bullish cross: `(MACD − Signal)` flipped from `≤ 0` to `> 0` on the current bar
  - Short requires bearish cross: flipped from `≥ 0` to `< 0`
- Signal alignment: long needs `CMF > 0 AND bullish_cross`; short needs `CMF < 0 AND bearish_cross`
- ATR(14) computable and positive (used for stop/TP geometry)

**Stop / TP geometry + management profile.**
- Stop: ATR-based (1.5 × ATR_5m typical)
- TP: matrix-cell driven, 2R typical
- Management: `default`

**Lab-measured behavior (6mo corpus, matrix-mined):**

| Direction | n_optimized | weighted WR | weighted exp_pips | weighted lift_pips |
|---|---|---|---|---|
| long | 5,578 | 81.3% | 6.53 | 3.99 |
| short | 5,310 | 79.9% | 6.43 | 4.08 |

- 27/27 pair coverage
- 168 long + 166 short cells in the matrix
- Direction-symmetric, high WR — confluence requirement filters cleanly

**Live behavior.** Promoted to live 2026-05-27 (ADR 3016). Limited
live trade volume in the first days post-promotion; per-strategy
audit pending Phase 3 module rebuild.

**Known limitations / failure modes.**
- Confluence requirement = low fire rate; misses trends that only
  one of the three signals catches
- Chaikin Money Flow on OANDA is approximate (no true order-book
  depth) — relies on tick-volume proxy

**Related strategies.**
- `trend_pullback` — looser confluence (no volume requirement)
- `dbb_trend` — DBB-based trend version

---

## compression_expansion

**Family:** breakout (volatility-compression → expansion shape)

**Signal philosophy.** Bollinger Band width compressing below
historical norm signals stored energy; subsequent expansion is the
release. Fires LONG on upward expansion from compression, SHORT on
downward expansion. The "squeeze + release" classic, refined with
ATR-relative thresholds for compression detection.

**Probe code reference.** `src/scrooge/strategies/compression_expansion.py`

**Entry conditions (all must hold):**
- Sufficient bars for `bb_period + compression_window` (default 20 + ~20)
- **Compression detection** — per bar in the rolling window, compute composite compression score:
  - `score = mean(1 − percentile_rank(bb_width), 1 − percentile_rank(ATR_proxy), 1 − percentile_rank(bar_range))` — higher = more compressed
  - Require ≥ **60%** of the prior `compression_lookback` bars (excluding current) to score ≥ `compression_percentile` threshold
- **Expansion trigger:** current bar's range ≥ `expansion_mult × median(prior expansion_lookback ranges)` (typical mult ≈ 1.5)
- **Directional alignment:**
  - Long requires `cur_close > cur_open AND cur_close > prev_close` (bullish body + above prior close)
  - Short requires mirror
- Compression envelope (high/low of compressed bars) is well-defined (height > 0)

**Stop / TP geometry + management profile.**
- Stop: BB midline (target-side stop — gives room for the expansion)
- TP: opposite Bollinger band on the expansion side
- Management: `trend_runner` (the expansion can run; let it)

**Lab-measured behavior (6mo corpus, matrix-mined):**

| Direction | n_optimized | weighted WR | weighted exp_pips | weighted lift_pips |
|---|---|---|---|---|
| long | 4,916 | 81.4% | 6.33 | 3.76 |
| short | 5,124 | 79.2% | 6.12 | 3.78 |

- 27/27 pair coverage
- 152 long + 156 short cells in the matrix
- Direction-symmetric

**Live behavior.** Promoted to live 2026-05-27 (ADR 3016). Sub-variant
naming (CE_*) appears in attribution logs.

**Known limitations / failure modes.**
- Compression detection is threshold-sensitive; choppy markets with
  brief compressions produce false signals
- BE config A/B sweep deferred to v1.14c per ADR 3016 — current BE
  geometry may not be optimal for this strategy

**Related strategies.**
- `CP1_coil_breakout` (Phase 3 sidelined) — same family, different
  thresholds
- `CP2_squeeze_momentum_long` (Phase 3 sidelined) — adds momentum
  filter
- `compression_reversion` — same compression detector, opposite
  direction (mean-revert thesis)

---

## trend_pullback

**Family:** continuation (intraday trend + pullback to mean)

**Signal philosophy.** Identify an established intraday trend (slope
of EMA + ADX threshold) and wait for a shallow pullback to a
designated mean (EMA20 or fib retracement). Fire continuation
in the trend's direction on resumption signal. The "buy the dip
in an uptrend" textbook trade, formalized.

**Probe code reference.** `src/scrooge/strategies/trend_pullback.py`

**Entry conditions (all must hold):**
- M5 + Daily candles available; M5 needs `swing_lookback + 2` bars
- **HTF bias from daily closes:** `bias_delta_pips = (d_now − d_then) / pip` over `bias_lookback_d` days; require `|bias_delta_pips| ≥ bias_min_pips` (flat = no trade)
- Direction set by bias sign (long if positive, short if negative)
- **Retest level** chosen as the nearest of:
  - H1 EMA20 (from `ctx.features['ema'].values['ema20']` or computed from H1 closes)
  - Recent swing extreme (`min` of last N M5 lows for long, `max` of N highs for short)
  - M5 EMA20 (fallback)
- `|current_close − retest_level| / pip ≤ retest_tolerance_pips` — price IS at the retest level
- **Rejection-candle trigger:**
  - Long: `lower_wick / bar_range > wick_frac_min` AND bullish body (`close > open`)
  - Short: `upper_wick / bar_range > wick_frac_min` AND bearish body
- `reward / risk ≥ min_rr` (typical 1.5+)

**Entry conditions (all must hold):**
- `bb_state ∈ {STRETCH_UP, STRETCH_DOWN}` — the BB classifier sees the band stretched (precondition; class is filtered out otherwise)
- 22+ M5 bars available
- **Direction:** `STRETCH_UP → LONG`, `STRETCH_DOWN → SHORT`
- **Proximity to SMA20:**
  - `proximity_pct = |close − SMA20| / SMA20 ≤ sma_proximity_pct` (default 0.0015) — OR
  - `proximity_atr = |close − SMA20| / ATR_5m ≤ 0.3`
- **Bounce confirmation:**
  - Long: `close > open` (bullish body) AND `close ≤ SMA20 × (1 + max_pct × 2)` (not extended)
  - Short: mirror
- **2-candle confirmation:** prior bar also passes the same proximity + body-alignment checks
- **Spread sanity:** if session range half-box is known, `spread / range_half ≤ 0.30`

**Stop / TP geometry + management profile.**
- Stop: prior swing extreme (last pullback low/high)
- TP: prior trend leg height projection
- Management: `default`

**Lab-measured behavior (6mo corpus, matrix-mined):**

| Direction | n_optimized | weighted WR | weighted exp_pips | weighted lift_pips |
|---|---|---|---|---|
| long | 5,125 | 81.3% | 6.27 | 3.74 |
| short | 5,289 | 80.8% | 6.42 | 3.96 |

- 27/27 pair coverage
- 156 long + 165 short cells in the matrix
- Direction-symmetric — slight short-side edge in pips

**Live behavior.** Promoted to live 2026-05-27 (ADR 3016). Sub-variant
`ITP_pullback_long` appears in broker truth — small sample (n=2, both
losses in the 27d window).

**Known limitations / failure modes.**
- Pullback definition is loose; can fire on noise that retraces to
  EMA20 without being a real countertrend wave
- The TF2_pullback_EMA20 Phase 3 finding (wrong-direction in this
  corpus regime) is a cousin pattern — worth cross-referencing once
  Phase 3 numbers land for `trend_pullback` specifically

**Related strategies.**
- `TF2_pullback_EMA20_long/short` (Phase 3) — same shape, different probe
- `dbb_trend` PULLBACK mode — DBB-version
- `chaikin_macd_atr` — confluence-version

---

## ifvg

**Family:** other (Inverse Fair Value Gap — ICT concept)

**Signal philosophy.** A Fair Value Gap (FVG) is a 3-candle pattern
where candle[1].high < candle[3].low (bullish gap) or candle[1].low >
candle[3].high (bearish gap). The "inverse" version trades into the
unfilled gap — long into bullish gaps expecting return-to-mean,
short into bearish gaps. ICT lineage; this is the strategy that the
broader ICT-derived strategy spec (HTF_PO3_SMT) was hoping to add as
a more sophisticated framework eventually.

**Probe code reference.** `src/scrooge/strategies/ifvg.py`

**Entry conditions (all must hold) — 4-pass detection logic:**

**Pass 1 — Detect Fair Value Gaps** in the lookback window (default 40 bars):
- Bullish FVG at bar `i`: `high[i−2] < low[i]` AND `gap = low[i] − high[i−2] ≥ min_gap_pips × pip`
- Bearish FVG at bar `i`: `low[i−2] > high[i]` AND gap meets minimum

**Pass 2 — Flip FVG → IFVG** when invalidated:
- A bullish FVG becomes a **short IFVG** when a later bar's close prints below the gap's lower edge
- A bearish FVG becomes a **long IFVG** when a later bar's close prints above the gap's upper edge
- The inverting bar is the "inversion candle"

**Pass 3 — Filter to still-active IFVGs:**
- A short IFVG dies if a later close prints above its upper edge (re-violation)
- A long IFVG dies if a later close prints below its lower edge
- Only zones that survived re-violation are admissible

**Pass 4 — Recent retest:**
- A bar in the last `retest_bars` window has touched a still-active zone (i.e., its `[low, high]` intersects the zone)
- Most recently inverted zone is preferred (freshest signal)

Direction comes from the active zone's IFVG direction (the flipped side of the original gap).

**Stop / TP geometry + management profile.**
- Stop: opposite side of the gap
- TP: mean of the gap (filling) + extension to next swing
- Management: `default`

**Lab-measured behavior (6mo corpus, matrix-mined):**

| Direction | n_optimized | weighted WR | weighted exp_pips | weighted lift_pips |
|---|---|---|---|---|
| long | 5,866 | 81.4% | 6.54 | 4.08 |
| short | 5,808 | 80.2% | 6.66 | 4.45 |

- 27/27 pair coverage
- 169 long + 167 short cells in the matrix
- Direction-symmetric

**Live behavior.** Promoted to live 2026-05-27 (ADR 3016). Sub-variants
`IFVG_v1_long`, `IFVG_v1_short` appear in broker truth. Small live
sample so far; IFVG_v1_short showed 0/2 W in the post-promotion
window, IFVG_v1_long 1/1 W.

**Known limitations / failure modes.**
- FVG detection requires reliable candle data — broker-side gap
  artifacts (e.g., weekend gaps) can produce false signals
- "Mean reversion into gap" thesis is regime-dependent; in strong
  directional regimes the gap continues to be ignored rather than
  filled

**Related strategies.**
- The HTF_PO3_SMT_Strategy_Spec (Phase 4 backlog candidate) would
  build on IFVG by adding the broader Power-of-Three context

---

## session_breakout

**Family:** breakout (session-anchored opening range)

**Signal philosophy.** Each trading session (Tokyo, London, NY) opens
with an opening range. After ~30 minutes, the high and low of that
opening range become breakout levels. Fire LONG on close above the
range, SHORT on close below. Session-anchored timing is the key
ingredient.

**Probe code reference.** `src/scrooge/strategies/session_breakout.py`

**Entry conditions (all must hold):**
- Current `session_bucket` ∈ `_ELIGIBLE_SESSIONS` (Tokyo open / London open / NY open — configurable)
- Opening Range (OR) is COMPLETE: `now ≥ or_end` (default ~30min into session)
- Still inside entry window: `now ≤ sess_end`
- `≥ min_or_bars` bars in the OR window + ≥ 2 post-OR bars
- OR `high = max(or_window_highs)`, `low = min(or_window_lows)`, range > 0
- **Direction trigger** (one-sided break + retest):

  **LONG:**
  - `max(post_OR_highs) > OR_high` AND `min(post_OR_lows) ≥ OR_low` (clean upward break)
  - Either: current bar low touched OR_high (±retest buffer) AND current close > OR_low — direct retest
  - OR: recent pullback in last 4 post-OR bars touched OR_high AND current close > OR_high — pullback-and-reclaim

  **SHORT (mirror):**
  - Clean downward break + retest of OR_low (or pullback-and-reclaim below)

**Stop / TP geometry + management profile.**
- Stop: opposite side of opening range
- TP: 1× or 2× opening-range height projection
- Management: `default`

**Lab-measured behavior (6mo corpus, matrix-mined):**

| Direction | n_optimized | weighted WR | weighted exp_pips | weighted lift_pips |
|---|---|---|---|---|
| long | 782 | 82.2% | 6.54 | 4.02 |
| short | 774 | 77.4% | 5.43 | 3.36 |

- **8/27 pair coverage** (much lower than other promoted strategies)
- 25 long + 25 short cells in the matrix
- Long-direction advantage (~5pp WR + better exp_pips and lift)

**Live behavior.** Promoted to live 2026-05-27 (ADR 3016). Limited
fire rate by design — only 8 pair-coverage means it's silent for ~70%
of the pair universe.

**Known limitations / failure modes.**
- Low pair coverage (8/27) — most pairs don't have meaningful
  session-anchored breakout edge in the lab data
- Session boundary definitions assume canonical Tokyo/London/NY hours;
  daylight savings shifts and broker session quirks can confuse the
  opening-range computation
- Asymmetric direction edge (long > short) suggests the lab regime
  favored upward breakouts; may invert in other regimes

**Related strategies.**
- `BR5_opening_range_breakout` (Phase 3 sidelined) — same shape,
  different threshold defaults; Phase 3 lab showed it as a strong
  variant (~$4.5M PnL, 6/27 pair concentration warning)
- `compression_expansion` — different breakout trigger (BB squeeze)

---

## trend

**Family:** continuation (legacy V3 trend strategy — sidelined)

**Signal philosophy.** The V3-era "trend" strategy: identify a
prevailing trend via EMA/ADX, enter on confirmation. Predates the
DBB-specific variants. Effectively superseded by `dbb_trend`,
`canonical_lien_dbb`, and `trend_pullback` — those are sharper-edged
versions of the same idea.

**Sidelined status.** Registered in `bootstrap.py` but explicitly
sidelined in routing — the routing table doesn't admit `trend` cells.
The strategy code is preserved for backward compatibility and as a
fallback if all newer trend variants are disabled simultaneously.

**Probe code reference.** `src/scrooge/strategies/trend.py`

**Stop / TP geometry + management profile.**
- Stop: ATR-based (default)
- TP: 2R typical
- Management: `trend_runner`

**Lab-measured behavior (6mo corpus, matrix-mined):**

| Direction | n_optimized | weighted WR | weighted exp_pips | weighted lift_pips |
|---|---|---|---|---|
| long | 5,250 | 80.2% | 6.24 | 3.87 |
| short | 5,332 | 79.3% | 6.42 | 3.93 |

- 27/27 pair coverage in matrix (was mined when strategy was active)
- 162 long + 164 short cells

**Live behavior.** Zero live trades since sidelined. Lab data only.

**Known limitations / failure modes.**
- Superseded — its admission space is fully covered by sharper-edged
  successors
- At V4 cutover (Task #57 code archaeology), `trend` is a deletion
  candidate. Decision deferred until Phase 3 confirms the newer
  trend variants are robust enough to fully replace it

**Related strategies.**
- All other continuation-family strategies are direct successors

---

## trend_aligned_breakout

**Family:** breakout (HTF-trend-aligned breakout)

**Signal philosophy.** Breakout trade with explicit HTF (1H/4H)
trend-alignment requirement. Fires LONG only when both M5 breakout
condition AND HTF1 trend is up AND HTF4 trend is up (or aligned-with).
The HTF-aligned subset of breakouts — sacrifices fire rate for
WR + directional confidence.

**Probe code reference.** `src/scrooge/strategies/trend_aligned_breakout.py`

**Entry conditions (rules NOT in scrooge_v3/strategies/*.py):**

`trend_aligned_breakout` is **not a standalone strategy module** in the
codebase — it's a matrix-mined category surfaced via the
`optimized_matrix_by_session.csv` `strategy` column. Cells in this
category are admitted via the routing table when a breakout-flavored
candidate happens to fire AND its 14-bucket signature falls into a
historically-validated HTF-aligned cell.

In other words: the "trigger rules" here are **emergent** from the
combination of (any breakout probe firing) + (HTF-alignment cell match
in the routing table). The 20/27 pair coverage + 60-cell short-side
asymmetry noted in this entry come from matrix mining, not from
explicit probe code.

To make this a first-class strategy in V4, a `trend_aligned_breakout.py`
probe module would need to be authored that pre-checks the HTF
alignment internally rather than relying on the routing table to catch
it post-hoc.

**Stop / TP geometry + management profile.**
- Stop: structural breakout-base
- TP: variable
- Management: `default`

**Lab-measured behavior (6mo corpus, matrix-mined):**

| Direction | n_optimized | weighted WR | weighted exp_pips | weighted lift_pips |
|---|---|---|---|---|
| long | 931 | 72.4% | 5.92 | 3.25 |
| short | 1,871 | 72.5% | 5.96 | 3.49 |

- **20/27 pair coverage** (7 pairs missing — likely thin breakout-aligned data)
- 30 long + **60 short** cells (2× short-side cells — bearish-regime
  artifact in the corpus)
- Direction-symmetric WR despite the cell-count asymmetry
- Lower WR than the matrix average (~80%) — confluence requirements
  produce a tighter cohort but at lower per-cell quality

**Live behavior.** Routed conditionally where cells exist. Limited
fire rate by design.

**Known limitations / failure modes.**
- Asymmetric cell count (60 short vs 30 long) reflects the bearish
  corpus regime — short-direction had more confluence-aligned setups
  during the lab window. Will likely rebalance in different regimes
- 7-pair coverage gap means it's silent on some major pairs
- The "confluence sacrifice" trade-off (fewer fires for higher
  directional confidence) means it underperforms volume-greedy
  variants like `BR2_vcb` in raw PnL

**Related strategies.**
- `compression_expansion`, `session_breakout` — different breakout triggers
- `chaikin_macd_atr` — different confluence framework
- The HTF gate ([ADR 3015](decisions/3015-htf-trend-filter-observe-to-hard.md))
  applies a similar filter at the system level — `trend_aligned_breakout`
  is the strategy-internal version of that filter


---

---

# probes_v2 family entries (10 NATO-phonetic probes)

These probes live in `src/scrooge/strategies/probes_v2.py` (ported from
the Oanda-Bot-Trainer playbook). All default DISABLED; enable per-probe
via `config.strategies.probes_v2.<name>.enabled = true`. Regime gating
is handled by the router based on the `family` mapping below — the
probe itself does not gate on regime.

**None of these are in the current matrix.** They enter via Task #41
module rebuild after Phase 3.

---

## alpha_pullback_v2

**Family routing:** dbb_trend (continuation pullback)

**Direction:** auto — `long` if `close > EMA20`, `short` if `close < EMA20`

**Entry conditions (all must hold):**
- `|close − EMA20| ≤ 0.3 × ATR_pips` — price within 0.3 ATR of EMA20 (the pullback proximity)
- Current bar is the resumption shape:
  - For long: bullish bar AND `close − low ≥ 0.5 × bar_range` (closed in upper half)
  - For short: bearish bar AND `high − close ≥ 0.5 × bar_range` (closed in lower half)
- `30 < RSI14 < 70` — not in extreme zones (avoid fading exhaustion at extremes)

**Stop / TP geometry:**
- Stop: `min(last 5 lows)` for long / `max(last 5 highs)` for short
- TP: 2.0 R (per probe registry `target: 2.0`)

**Live behavior.** Default DISABLED. Phase 3 lab data available (in sweep results).

**Related.** `charlie_pullback_continuation_v2` — same family, tighter pullback (3-bar declining lows required)

---

## alpha_breakout_retest_v2

**Family routing:** direct (breakout retest)

**Direction:** auto — `long` if `close > EMA20`, `short` if `close < EMA20`

**Entry conditions (all must hold):**
- Prior 12-bar window (bars −16 to −4) defines `broken_level`:
  - For long: `broken_level = max(prior_window_highs)`, AND `max(last 4 highs) > broken_level` (level was broken)
  - For short: `broken_level = min(prior_window_lows)`, AND `min(last 4 lows) < broken_level`
- Retest proximity: `|close − broken_level| ≤ 0.2 × ATR_pips`
- Current bar direction matches: bullish for long, bearish for short

**Stop / TP geometry:**
- Stop: `broken_level` (the level we retested)
- TP: 1.5 R

**Live behavior.** Default DISABLED.

---

## alpha_extended_fade_v2

**Family routing:** reversal (extension fade)

**Direction:** auto — `short` if `RSI ≥ 65 AND close > EMA20`, `long` if `RSI ≤ 35 AND close < EMA20`

**Entry conditions:**
- RSI in extreme zone (above 65 or below 35) AND price on aligned side of EMA20
- Current bar wick confirms exhaustion:
  - For short: upper wick ≥ body length
  - For long: lower wick ≥ body length

**Stop / TP geometry:**
- Stop: `max(last 5 highs)` for short / `min(last 5 lows)` for long
- TP: 2.0 R

**Live behavior.** Default DISABLED. **Family is `reversal`** — same reversion family that the wrong-direction Phase 3 finding hit; verify direction-asymmetry before promotion.

---

## bravo_failed_momentum

**Family routing:** reversal (failed-momentum fade)

**Direction:** auto — opposite of prior bar's direction (fading the momentum failure)

**Entry conditions (all must hold):**
- Prior bar's range ≥ 1.5 × mean(20-bar ranges) — prior bar was a strong momentum push
- Current close is INSIDE prior bar's range (`prev_low < cur_close < prev_high`) — momentum failed to follow through
- Current bar direction is OPPOSITE prior bar's direction (the fade)

**Stop / TP geometry:**
- Stop: `prev_low` for long-fade / `prev_high` for short-fade
- TP: 2.0 R

**Live behavior.** Default DISABLED.

---

## bravo_expansion_continuation

**Family routing:** dbb_trend (range expansion)

**Direction:** auto — `long` if bullish bar, `short` if bearish bar

**Entry conditions (all must hold):**
- Current bar range ≥ 1.3 × mean(20-bar ranges) — current bar is a strong expansion
- Close is in the trade direction's third of the bar:
  - For long: `close − low ≥ 0.67 × bar_range` (closed in top third)
  - For short: `high − close ≥ 0.67 × bar_range` (closed in bottom third)

**Stop / TP geometry:**
- Stop: current bar's `low` (long) or `high` (short)
- TP: 2.0 R

**Live behavior.** Default DISABLED.

---

## charlie_pullback_continuation_v2

**Family routing:** dbb_trend (continuation, tighter than alpha_pullback)

**Direction:** auto — `long` if `close > EMA20`, `short` if `close < EMA20`

**Entry conditions (all must hold):**
- 3-bar declining-lows pattern (long) or rising-highs (short):
  - For long: `m5_low[-2] < m5_low[-3] < m5_low[-4]` (three lower lows)
  - For short: `m5_high[-2] > m5_high[-3] > m5_high[-4]`
- Current bar reverses the pullback: `close > m5_close[-2]` (long) or `<` (short)
- `|close − EMA20| ≤ 0.5 × ATR_pips`
- `35 < RSI14 < 65` (mid-zone)

**Stop / TP geometry:**
- Stop: `min(last 5 lows)` (long) / `max(last 5 highs)` (short)
- TP: 2.0 R

**Live behavior.** Default DISABLED. **🚨 Phase 3 outlier — $297M PnL on
86k trades.** Same compound-growth signature as TF2_pullback_EMA20_long.
Forensic needed (200 EMA filter test, same as TF2) before any promotion
decision — verify it's real edge in regime-aligned direction, not artifact.

---

## charlie_compression_breakout

**Family routing:** direct (compression breakout)

**Direction:** auto — long on upward break + bullish bar, short on downward break + bearish bar

**Entry conditions (all must hold):**
- Volatility compression: `mean(last 6 TRs) < 0.85 × mean(prior 19 TRs)` — last 6 bars meaningfully tighter than baseline
- Current bar breaks the prior-6-bar range:
  - For long: `current_high > max(prior 6 highs)` AND current bar is bullish
  - For short: `current_low < min(prior 6 lows)` AND current bar is bearish

**Stop / TP geometry:**
- Stop: opposite side of prior 6-bar range (long stops at `min(prior 6 lows)`, short at `max(prior 6 highs)`)
- TP: 1.5 R

**Live behavior.** Default DISABLED. Phase 3 sweep: n=62k, pnl=$1.7M.

---

## delta_tag_and_go_v2

**Family routing:** direct (tag-and-go continuation)

**Direction:** auto — long on prior-bar break above 12-bar high, short on break below 12-bar low

**Entry conditions (all must hold):**
- Prior bar broke the 12-bar window range (bars −14 to −2):
  - For long: `prev_high > max(window_highs)` AND `prev_close > max(window_highs)`
  - For short: `prev_low < min(window_lows)` AND `prev_close < min(window_lows)`
- Current bar continues in break direction (bullish for long, bearish for short)

**Stop / TP geometry:**
- Stop: 12-bar window boundary (the level that was broken)
- TP: 1.5 R

**Live behavior.** Default DISABLED. Phase 3 sweep: n=86k, pnl=$2M.

---

## echo_box_fade_v2

**Family routing:** reversal (rail fade)

**Direction:** auto — `long` if `bb_position ≤ 0.03`, `short` if `bb_position ≥ 0.87`

**Entry conditions (all must hold):**
- Price at Bollinger extreme (using `bb_position` feature)
- Wick exhaustion confirms:
  - For long: lower wick ≥ body length
  - For short: upper wick ≥ body length

**Stop / TP geometry:**
- Stop: `min(last 3 lows)` (long) / `max(last 3 highs)` (short)
- TP: 2.0 R

**Live behavior.** Default DISABLED. Phase 3 sweep status: pending (variant 33 or 34 of 34).

---

## echo_failed_breakout_v2

**Family routing:** reversal (failed-break fade)

**Direction:** auto — based on which BB was pierced + closed-back-inside

**Entry conditions (all must hold):**
- Prior bar pierced a Bollinger band by ≥ 1.0 × ATR_pips but closed BACK inside:
  - For long: `prev_low < bb_lower AND prev_close > bb_lower AND (bb_lower − prev_low) ≥ 1.0 × ATR_pips`
  - For short: mirror with `bb_upper`
- Current bar continues the fade direction (bullish for long-fade, bearish for short-fade)

**Stop / TP geometry:**
- Stop: prior bar's extreme (`prev_low` for long, `prev_high` for short)
- TP: 2.0 R
- Extra payload: `pierce_size_atr_x` (how far past BB the prior bar went, in ATR units)

**Live behavior.** Default DISABLED. Phase 3 sweep status: pending (variant 33 or 34 of 34).

---

# Missed textbook_scalper variants

These 2 entries from `src/scrooge/strategies/textbook_scalper.py` were
missed in the prior taxonomy. Added now for completeness.

---

## TF4_sar_long

**Family routing:** direct (Parabolic SAR trend-follow, long-only)

**Direction:** long-only (no short variant defined)

**Entry conditions (all must hold):**
- Parabolic SAR(0.02, 0.2) computed over last 12 M5 bars indicates uptrend (`bull = True`)
- `close > SAR` AND `close > EMA20` (price aligned with both)
- `54 ≤ RSI14 ≤ 76` (momentum present but not exhausted)
- ADX14 ≥ 17 if available (trend strength)
- `close_pos ≥ 0.55` if available (closed in upper half of bar)
- `bars_since_SAR_flip ≤ 8` (fresh trend, not stale)
- `close > max(prior 5 highs)` (breakout confirmation)

**Stop / TP geometry:**
- Stop: structural reference (per `_build_candidate_multi`)
- TP: 1.5 R (per probe registry)

**Live behavior.** Default DISABLED. Phase 3 sweep complete — check
per_variant_TF4_sar_long.csv for results.

---

## RG2_range_support_bounce_long

**Family routing:** reversal (PDL support bounce, long-only)

**Direction:** long-only

**Entry conditions (all must hold):**
- `bb_state ∈ {REJECTION_LONG, EXTREME_DOWN}` (BB classifier confirms reversal context)
- PDH and PDL both available
- `pdl < current_price < pdh` (inside the daily box)
- `current_close ≤ pdl + 0.25% × box_range` (very close to PDL, the proximity tolerance)
- Prior bar shows hammer/pin shape:
  - `lower_wick ≥ 1.5 × body` (long lower wick — rejection from PDL)
  - `lower_wick > upper_wick` (asymmetric in long direction)
- `current_close > prior_high` (resumption confirmation)

**Stop / TP geometry:**
- Stop: per `_build_candidate_multi` defaults
- TP: per probe registry

**⚠️ Phase 3 sweep: 0 trades.** Either the conditions never aligned in the
6mo corpus (very strict — requires REJECTION_LONG or EXTREME_DOWN BB state
AND PDL proximity AND prior-bar pin AND resumption all simultaneously) or
the probe code has a bug. Verify before encyclopedia promotion / live
enabling.


---

---

# textbook_scalper family entries (20 variants)

These probes live in `src/scrooge/strategies/textbook_scalper.py` —
parametric scalping probes derived from common technical-analysis
patterns. All default DISABLED via `config.strategies.textbook_scalper.*`.
Phase 3 sweep tested all 22 variants (including TF4_sar_long + RG2_range_support_bounce_long
documented above) — Phase 3 numbers fill in the "Lab-measured behavior" once Task #41
module rebuild lands.

---

## TF2_pullback_EMA20_long

**Family routing:** direct (trend-follow pullback to EMA20, long-only)

**Entry conditions (all must hold):**
- `close > EMA20` (price above EMA20 — long side of trend)
- `(close − EMA20) / pip ≤ 0.4 × ATR_pips` (within 0.4 ATR of EMA20 — pullback proximity)
- `40 ≤ RSI14 ≤ 65` (moderate, not extreme)
- Current bar is **bullish** (resumption signal)

**Stop / TP geometry:**
- Stop: `min(last 5 lows)`
- TP: 1.5 R

**Notable behavior.** Phase 3 sweep: 80,061 trades, 61% raw WR (cross-calibrated
against TraderDale 48% raw / 60% +VWAP article and TradePro 60-63% YouTube setup).
Forensic 2026-05-30 confirmed real edge — the lab's $126M compound-growth PnL is
$50k seed × 6mo compounding at ~70% WR (not artifact). **Wrong-direction probe** in
the bearish 6mo corpus regime: reversed direction (short same signals) wins
70-74% WR with +3-4pp lift from 200 EMA filter. Reframed correctly as
"trade in direction of regime trend," not as "flip the probe."

---

## TF2_pullback_EMA20_short

**Family routing:** direct (mirror of TF2_long)

**Entry conditions (all must hold):**
- `close < EMA20`
- `(EMA20 − close) / pip ≤ 0.4 × ATR_pips`
- `40 ≤ RSI14 ≤ 65` (same mid-range)
- Current bar is **bearish**

**Stop / TP geometry:** stop at `max(last 5 highs)`, TP 1.5 R.

---

## BR2_vcb_long

**Family routing:** direct (Volume Compression Breakout, long)

**Entry conditions (all must hold):**
- `bb_position ≥ 0.80` (price pushing into upper half — expansion phase)
- `50 ≤ RSI14 ≤ 78` (momentum present, not extreme)
- `close > max(prior 5 closes)` (breakout bar — close above prior 5-bar high close)
- Current bar is **bullish**

**Stop / TP geometry:** stop at `min(last 5 lows)`, TP 1.5 R.

**Phase 3:** $4.9M PnL, ~62% WR, 27/27 pair coverage. Strong winner.

---

## BR2_vcb_short

**Family routing:** direct (mirror of BR2_long)

**Entry conditions:** `bb_position ≤ 0.20`, `22 ≤ RSI14 ≤ 50`, `close < min(prior 5 closes)`, bearish bar.

**Stop / TP geometry:** stop at `max(last 5 highs)`, TP 1.5 R.

**Phase 3:** ~62% WR, 27/27 pair coverage.

---

## BR3_inside_bar_long

**Family routing:** direct (3-bar inside-bar breakout, long)

**Entry conditions (all must hold):**
- 3-bar inside-bar pattern: `inside_hi ≤ mother_hi AND inside_lo ≥ mother_lo` (bar −2 is contained inside bar −3)
- `close > mother_hi` (current closes above the inside-bar mother's high)
- `close > EMA20` (trend filter)
- `RSI14 ≥ 52` (momentum)
- Current bar is **bullish**

**Stop / TP geometry:** stop at `min(mother_lo, inside_lo)`, TP 1.5 R.

**Phase 3:** Net-negative variant — flagged as drop candidate. Inside-bar break
+ trend filter combo didn't show edge in the 6mo corpus.

---

## BR3_inside_bar_short

**Family routing:** direct (mirror of BR3_long)

**Entry conditions:** same inside-bar pattern, but `close < mother_lo`, `close < EMA20`, `RSI14 ≤ 48`, bearish bar.

**Stop / TP geometry:** stop at `max(mother_hi, inside_hi)`, TP 1.5 R.

**Phase 3:** Net-negative. Drop candidate alongside BR3_long.

---

## BR5_opening_range_breakout_long

**Family routing:** direct (20-bar high break, long)

**Entry conditions (all must hold):**
- `high > max(prior 20 highs, excluding current + previous)` — true breakout above the rolling 20-bar window
- Current bar is **bullish**
- `RSI14 ≥ 50` (above neutral)

**Stop / TP geometry:** stop at `min(last 5 lows)`, TP 1.5 R.

**Phase 3:** Strong winner alongside BR2_vcb_short, ~$4.5M PnL.

---

## BR5_opening_range_breakout_short

**Family routing:** direct (mirror)

**Entry conditions:** `low < min(prior 20 lows excl current+prev)`, bearish bar, `RSI14 ≤ 50`.

**Stop / TP geometry:** stop at `max(last 5 highs)`, TP 1.5 R.

---

## CP1_coil_breakout_long

**Family routing:** direct (coil breakout, long)

**Entry conditions (all must hold):**
- `BB_compress` (if present) `≤ 0.95` — compressed BB state
- Coil window: 5-bar `coil_hi = max(prior 5 highs)`, `coil_lo = min(prior 5 lows)`
- Coil range in ATR units: `(coil_hi − coil_lo) / (ATR_pips × pip) ≤ 1.25` (tight coil, not just any range)
- `close > coil_hi` (breakout above coil)
- `close > EMA20` (trend filter)
- `RSI14 ≥ 53` (momentum)
- Current bar is **bullish**

**Stop / TP geometry:** stop at `coil_lo`, TP 1.5 R.

**Phase 3:** Top winner — $7.3M PnL, 67% pair breadth (18/27 positive).

---

## CP1_coil_breakout_short

**Family routing:** direct (mirror)

**Entry conditions:** `BB_compress ≤ 0.95`, coil range tight, `close < coil_lo`, `close < EMA20`, `RSI14 ≤ 47`, bearish bar.

**Stop / TP geometry:** stop at `coil_hi`, TP 1.5 R.

---

## CP2_squeeze_momentum_long

**Family routing:** direct (squeeze-then-momentum continuation, long-only)

**Entry conditions (all must hold):**
- `BB_compress ≤ 0.92` (real squeeze, tighter than CP1's 0.95)
- `ADX14 ≥ 18` if available (broader tape carrying)
- `close_pos ≥ 0.58` if available (closed in upper portion of bar)
- 8-bar coil range in pips ≤ `max(ATR_pips × 1.05, 6.0)` — meaningfully tight
- `close > coil_hi` (break above)
- `close > EMA20` (trend filter)
- `56 ≤ RSI14 ≤ 78` (momentum, not exhausted)
- **3-bar expanding closes:** `close > close[-2] AND close[-2] > close[-3]` (not a one-bar poke)
- Current bar is **bullish**

**Stop / TP geometry:** stop at `coil_lo`, TP 1.5 R.

**Phase 3:** Strong winner — $3.8M PnL, ~62% WR, 16/27 pair breadth.

---

## CP3_vol_coil_fade_long

**Family routing:** reversal (fade the extension at lower band after compression)

**Entry conditions (all must hold):**
- `bb_position ≤ 0.12` (extreme lower band tag — oversold spike)
- `RSI14 ≤ 35` (oversold confirmation)
- `close > close[-2]` (current closes higher than previous — turn-off-lows)
- Current bar is **bullish** (reversal confirmation)

**Stop / TP geometry:** stop at `min(last 3 lows)`, TP 2.0 R.

**Notable.** **Wrong-direction probe** in 6mo corpus (Phase 3 finding):
reversed (= short same signals) wins 24-26/27 pairs. The fade thesis is
correct as a setup detector but the regime continued the extension rather
than reverting in this window.

---

## CP3_vol_coil_fade_short

**Family routing:** reversal (mirror)

**Entry conditions:** `bb_position ≥ 0.88`, `RSI14 ≥ 65`, `close < close[-2]`, bearish bar.

**Stop / TP geometry:** stop at `max(last 3 highs)`, TP 2.0 R.

**Notable.** Same wrong-direction pattern as CP3_long.

---

## MR2_bb_reversion_short

**Family routing:** reversal (Bollinger mean-reversion, short-only)

**Entry conditions (all must hold):**
- `z_score ≥ 1.2` if available (statistical stretch — fallback to `bb_position ≥ 0.82`)
- `bb_position ≥ 0.78` (upper rail)
- `RSI14 ≥ 58`
- `BB_compress ≤ 1.15` if available (not in extreme expansion)
- `close < close[-2]` (turn-off-highs)
- Current bar is **bearish**

**Stop / TP geometry:** stop at `max(last 4 highs)`, TP 2.0 R.

**Notable.** **Wrong-direction probe** (Phase 3): reversed (long) wins
22-27/27 pairs. Bearish corpus continued the upper-band push rather than
reverting.

---

## MR4_zscore_extreme_long

**Family routing:** reversal (z-score extreme reversion, long)

**Entry conditions (all must hold):**
- `z_score ≤ −1.8` (statistical stretch downward)
- `bb_position ≤ 0.12` (lower band)
- `RSI14 ≤ 36`
- `close > close[-2]` (turn-off-lows)
- Current bar is **bullish**

**Stop / TP geometry:** stop at `min(last 4 lows)`, TP 2.0 R.

**Notable.** **Wrong-direction probe** in 6mo corpus.

---

## MR4_zscore_extreme_short

**Family routing:** reversal (mirror)

**Entry conditions:** `z_score ≥ 1.8`, `bb_position ≥ 0.88`, `RSI14 ≥ 64`, `close < close[-2]`, bearish bar.

**Stop / TP geometry:** stop at `max(last 4 highs)`, TP 2.0 R.

**Notable.** Phase 3 weakest wrong-direction case — only 21/27 pairs prefer
reversed (vs 23-27/27 for the others in the family). 5 dissenting pairs
suggest the z-score-extreme thesis is closer to neutral than the BB-position
or Williams %R variants.

---

## MR5_williams_extreme_long

**Family routing:** reversal (Williams %R extreme — RSI14 proxy)

**Entry conditions (all must hold):**
- `RSI14 ≤ 22` (extreme low — Williams %R equivalent)
- `close > close[-2]` (turn-off-lows)
- Current bar is **bullish**

**Stop / TP geometry:** stop at `min(last 3 lows)`, TP 2.0 R.

**Notable.** **Wrong-direction probe** in 6mo corpus (100% week-by-week
agreement, 26/26 weeks). Lowest-volume variant in the textbook_scalper
family — only ~2,875 trades over 6mo per direction. Temporally
narrow firing (only 25/26 weeks active vs 26/26 for most other variants),
flagged as the riskiest promotion target in the family.

---

## MR5_williams_extreme_short

**Family routing:** reversal (mirror)

**Entry conditions:** `RSI14 ≥ 78`, `close < close[-2]`, bearish bar.

**Stop / TP geometry:** stop at `max(last 3 highs)`, TP 2.0 R.

**Notable.** Same temporal-narrow + wrong-direction pattern as MR5_long.

---

## RG1_range_bound_scalp_long

**Family routing:** reversal (rail fade in range/compression regime)

**Entry conditions (all must hold):**
- `bb_position ≤ 0.22` (near lower rail)
- `20 ≤ RSI14 ≤ 38` (mild oversold zone — NOT extreme; that's MR5's territory)
- Current bar is **bullish**

**Stop / TP geometry:** stop at `min(last 3 lows)`, TP 1.5 R.

**Notable.** **Wrong-direction probe** in 6mo corpus — Phase 3 lab:
27/27 pairs prefer reversed, 25/26 weeks consistent. Tighter probe
conditions than MR5/MR4 (RSI 20-38 vs RSI ≤22 for MR5) — more frequent
firing (~19k trades over 6mo).

---

## RG1_range_bound_scalp_short

**Family routing:** reversal (mirror)

**Entry conditions:** `bb_position ≥ 0.78`, `62 ≤ RSI14 ≤ 80`, bearish bar.

**Stop / TP geometry:** stop at `max(last 3 highs)`, TP 1.5 R.

**Notable.** Same wrong-direction pattern as RG1_long. The Phase 3 forensic
on EUR_USD showed native takes a short at 1.15434, stopped at 1.15534
(−$2,166); reversed-trade (long same setup) hit TPs for $801-$1,299. Same
probe, same moment, opposite outcomes — direction is the question, not the
setup detection.

---

# Pending entries (Phase 3 module rebuild needed)

The following strategy entries are queued for fill-in once the Phase 3
sweep (Task #40) completes and the module rebuild (Task #41) lands.
Each follows the same 9-field template. Phase 3 produces per-variant
lab metrics; the rebuild produces routing-table cells per (pair ×
regime × strategy × direction); together they fill the encyclopedia's
"Lab-measured behavior" + "Live behavior" sections.

Pending V3-promoted families (only `compression_reversion` left from this group):
- ~~`canonical_lien_dbb`~~ — **entry written** (matrix data, 25/27 pairs)
- ~~`canonical_darvas`~~ — **entry written** (coverage gap noted)
- ~~`trend_pullback`~~ — **entry written** (matrix data, 27/27 pairs)
- ~~`chaikin_macd_atr`~~ — **entry written** (matrix data, 27/27 pairs)
- ~~`compression_expansion`~~ — **entry written** (matrix data, 27/27 pairs)
- `compression_reversion` — regime-mismatched, very low n; entry pending Phase 3 confirmation
- ~~`ifvg`~~ — **entry written** (matrix data, 27/27 pairs)
- ~~`session_breakout`~~ — **entry written** (matrix data, 8/27 pairs — narrow coverage)

**Pending probes_v2 family** (10 NATO-phonetic probes from `src/scrooge/strategies/probes_v2.py`,
all default-DISABLED — fan in one at a time per Phase 3 evidence). **None of these are in the
matrix yet** — they enter for the first time via Task #41 module rebuild after Phase 3.

| Probe | Live family | Description | Phase 3 sweep |
|---|---|---|---|
| [`alpha_pullback_v2`](#alpha_pullback_v2) | dbb_trend | continuation pullback | ✓ + entry written |
| [`alpha_breakout_retest_v2`](#alpha_breakout_retest_v2) | direct | breakout retest | ✓ + entry written |
| [`alpha_extended_fade_v2`](#alpha_extended_fade_v2) | reversal | extension fade | ✓ + entry written |
| [`bravo_failed_momentum`](#bravo_failed_momentum) | reversal | failed-momentum fade | ✓ + entry written |
| [`bravo_expansion_continuation`](#bravo_expansion_continuation) | dbb_trend | range expansion | ✓ + entry written |
| [`charlie_pullback_continuation_v2`](#charlie_pullback_continuation_v2) | dbb_trend | continuation (**$297M Phase 3 compounder** — needs forensic) | ✓ + entry written |
| [`charlie_compression_breakout`](#charlie_compression_breakout) | direct | compression breakout | ✓ + entry written |
| [`delta_tag_and_go_v2`](#delta_tag_and_go_v2) | direct | tag-and-go continuation | ✓ + entry written |
| [`echo_box_fade_v2`](#echo_box_fade_v2) | reversal | rail fade | pending Phase 3 + entry written |
| [`echo_failed_breakout_v2`](#echo_failed_breakout_v2) | reversal | failed-break fade | pending Phase 3 + entry written |

**textbook_scalper family — all 22 entries WRITTEN** (with trigger rules
extracted from probe source). Still pending Phase 3 lab numbers + matrix
mining (Task #41) to fill the "Lab-measured behavior" sections per variant.

The only V4-pending entry is `compression_reversion` (data-thin even
in current matrix; needs Phase 3 confirmation of whether the regime
shift made it tradable).

**Notable Phase 3 findings already known** (each gets its own entry
when filled):

- **Wrong-direction family pattern.** All 5 reversion-flavored families
  (MR2, MR4, MR5, RG1, CP3) showed strongly negative native-direction
  PnL and strongly positive reversed-direction PnL across 23-27/27
  pairs. The pattern was 100% week-by-week consistent for MR5 (26/26
  weeks). Reframed as "trade in the direction of the regime trend"
  rather than "flip the probe" — the HTF gate ([ADR 3015](decisions/3015-htf-trend-filter-observe-to-hard.md))
  is the durable expression.
- **TF2_pullback_EMA20** appeared as a large outlier ($1,578/trade ×
  80k trades × 27/27 positive pairs) — forensic confirmed real edge
  (compound growth on $50k seed equity, not artifact), but the
  "native direction" is structurally wrong-direction in the bearish
  corpus regime. Calibrated against external sources (TraderDale
  article, TradePro YouTube video) — both reported 60-63% WR for
  trend-filtered EMA20 pullback; our 61% raw is consistent.
- **BR3_inside_bar** was the only Phase 3 variant with net-negative
  aggregate PnL across the corpus. Drop candidate.

---

## Cross-references

- [`LIVE_SYSTEM_SPEC.md`](LIVE_SYSTEM_SPEC.md) — what the routing table
  currently admits and how the admission stack works
- [`ARCHITECTURE_DIAGRAM.md`](ARCHITECTURE_DIAGRAM.md) — visual map of
  the scan-to-execution flow including strategy emission
- [`RESEARCH_METHODOLOGY.md`](RESEARCH_METHODOLOGY.md) — how lab numbers
  in this doc were computed
- [`decisions/`](decisions/) — ADRs covering individual promotion +
  retirement decisions per strategy
- [`history/`](history/) — chronological story of which strategies
  came / went / changed family over V1 → V4
- [`archive/MASTER_THEORY_v1-box-reversal-origin-2025.md`](archive/MASTER_THEORY_v1-box-reversal-origin-2025.md)
  — the foundational V1 doctrine that originally defined
  `box_master_theory` (preserved as historical context)
