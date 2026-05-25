# Replay Lab — Known Calibration Issues (as of 2026-05-25)

Scaffold is **complete and runs end-to-end**. Pipeline confirmed: data fetch
→ context build → strategy emit (851/1900 bars → 851 candidates) → routing
→ Backtest.run() → results CSV.

But routing rejects all candidates because two replay-time classifier issues
need fixing before the first real result comes out.

## Issue 1: regime53 stuck at "unknown"

**Symptom:** every bar emits with `technical_regime_53 = "unknown"`.

**Root cause:** `TechnicalRegime53Calculator.compute()` requires both M5
candles AND daily candles (`snapshot.candles["D"]`) with a minimum bar
count. The 30-day window fetches ~22 daily bars; classifier needs more,
or the lookback inside the calc is too aggressive.

**Fix options:**
- Extend the date range to 90+ days so daily bars exceed any internal floor
- Or pre-compute regime53 codes against a much longer daily history and
  cache, then inject as classification rather than re-compute per bar
- Or instantiate `TechnicalRegime53Calculator` with relaxed min-bar config

## Issue 2: session_bucket stuck at "ny_close"

**Symptom:** every bar emits with `session_bucket = "ny_close"` regardless
of bar timestamp.

**Root cause:** `SessionBucketClassifier` likely uses wall-clock `now()`
instead of the bar's `snapshot.timestamp`. In replay we need bar-time.

**Fix options:**
- Pass bar timestamp explicitly into the classifier (some classifiers
  accept a `clock` arg — see `OandaClock` vs `FixedClock` in core/clock.py)
- Or wrap the classifier to compute hour-of-day from `snap.timestamp.hour`
  directly in `context_factory.build_context`

## Issue 3: ATR daily/EMA hourly insufficient bars

Less critical because the gates that block on these are already configured
to fail-OPEN in replay, but loudly warns. Same fix as #1: extend lookback
or relax min-bar config.

## What WORKS

- OANDA candle fetcher with 10-day M5 chunking + retry
- Cache layer at `research/replay_lab/cache/`
- `SymbolContext` builder calling all 7 features + 7 classifiers per bar
- All 6 canonical_lien_dbb variants emitting candidates correctly
  (851 emits in 1900 bars, ~45% emission rate — feels right)
- Routing table loads (888 rows, 137 leaves)
- backtesting.py Backtest runs to completion, writes summary CSV
- Direction-comparison runner sweeps native vs reversed
- Entry-mode + management-ablation runners scaffolded
- Regression suite scaffolded with 4 benchmark cases

## What needs ~half a day in a fresh session

1. Fix regime53 + session_bucket replay-time classification (issues 1+2 above)
2. Once those return real values, verify routing matches succeed
3. Run direction comparison, expect non-zero trade counts both sides
4. Run entry-mode + management-ablation
5. Wire box_master_theory family wrapper (currently only canonical_lien_dbb)
6. Run regression suite, save baseline
