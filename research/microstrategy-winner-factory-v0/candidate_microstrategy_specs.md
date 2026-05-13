# Candidate Microstrategy Specs v0

These are not old-regime survivors. They are repeated clean-winner entry-state shapes mined from historical chart/corpus data. Each one is a micro-bot candidate: define the entry, define the management, then replay it standalone and try to kill it.

## MS-001 usd_base short overlap_q2 lower_band/low/bbw_mid/echo_expanded

Entry-state synchrony:
- Pair family: `usd_base`
- Direction: `short`
- Time: `overlap` / `overlap_q2`
- BB location: `lower_band`
- RSI state: `low`
- EMA20 distance: `ema_mid`
- Band width: `bbw_mid`
- Echo/range state: `echo_expanded`

Historical behavior:
- Sample: `134` trades
- Clean 2R winners: `66` (`49.3%`), enrichment `2.18x` vs corpus baseline
- Potential 2R reach rate: `52.2%`
- Gave-back-green rate: `11.9%`
- Mean path: MFE `1.45R`, MAE `0.62R`, realized `0.59R`
- Management hypothesis: Hold-for-target candidate; giveback is relatively low for this cell.

Required kill tests before promotion:
- Discovery vs holdout split
- Pair-level concentration inside family
- Standalone raw-M5 replay, not inherited probe replay
- Factor expansion to full 47 raw factors at entry

## MS-002 usd_base long asia_q3 upper_band/mid/bbw_wide/echo_expanded

Entry-state synchrony:
- Pair family: `usd_base`
- Direction: `long`
- Time: `asia` / `asia_q3`
- BB location: `upper_band`
- RSI state: `mid`
- EMA20 distance: `ema_mid`
- Band width: `bbw_wide`
- Echo/range state: `echo_expanded`

Historical behavior:
- Sample: `104` trades
- Clean 2R winners: `52` (`50.0%`), enrichment `2.22x` vs corpus baseline
- Potential 2R reach rate: `51.9%`
- Gave-back-green rate: `19.2%`
- Mean path: MFE `1.43R`, MAE `0.73R`, realized `0.49R`
- Management hypothesis: Balanced target/ratchet candidate; replay variants before naming.

Required kill tests before promotion:
- Discovery vs holdout split
- Pair-level concentration inside family
- Standalone raw-M5 replay, not inherited probe replay
- Factor expansion to full 47 raw factors at entry

## MS-003 usd_base short london_q1 middle/low/bbw_wide/echo_explosive

Entry-state synchrony:
- Pair family: `usd_base`
- Direction: `short`
- Time: `london` / `london_q1`
- BB location: `middle`
- RSI state: `low`
- EMA20 distance: `ema_near`
- Band width: `bbw_wide`
- Echo/range state: `echo_explosive`

Historical behavior:
- Sample: `132` trades
- Clean 2R winners: `64` (`48.5%`), enrichment `2.15x` vs corpus baseline
- Potential 2R reach rate: `51.5%`
- Gave-back-green rate: `21.2%`
- Mean path: MFE `1.64R`, MAE `0.59R`, realized `0.78R`
- Management hypothesis: Entry-shape works but management is suspect; test earlier protection/partial logic.

Required kill tests before promotion:
- Discovery vs holdout split
- Pair-level concentration inside family
- Standalone raw-M5 replay, not inherited probe replay
- Factor expansion to full 47 raw factors at entry

## MS-004 usd_base long london_q1 middle/high/bbw_wide/echo_explosive

Entry-state synchrony:
- Pair family: `usd_base`
- Direction: `long`
- Time: `london` / `london_q1`
- BB location: `middle`
- RSI state: `high`
- EMA20 distance: `ema_near`
- Band width: `bbw_wide`
- Echo/range state: `echo_explosive`

Historical behavior:
- Sample: `114` trades
- Clean 2R winners: `54` (`47.4%`), enrichment `2.10x` vs corpus baseline
- Potential 2R reach rate: `49.1%`
- Gave-back-green rate: `20.2%`
- Mean path: MFE `1.57R`, MAE `0.64R`, realized `0.57R`
- Management hypothesis: Entry-shape works but management is suspect; test earlier protection/partial logic.

Required kill tests before promotion:
- Discovery vs holdout split
- Pair-level concentration inside family
- Standalone raw-M5 replay, not inherited probe replay
- Factor expansion to full 47 raw factors at entry

## MS-005 usd_base short london_q2 upper_rail/mid/bbw_wide/echo_compressed

Entry-state synchrony:
- Pair family: `usd_base`
- Direction: `short`
- Time: `london` / `london_q2`
- BB location: `upper_rail`
- RSI state: `mid`
- EMA20 distance: `ema_mid`
- Band width: `bbw_wide`
- Echo/range state: `echo_compressed`

Historical behavior:
- Sample: `106` trades
- Clean 2R winners: `50` (`47.2%`), enrichment `2.09x` vs corpus baseline
- Potential 2R reach rate: `49.1%`
- Gave-back-green rate: `18.9%`
- Mean path: MFE `1.46R`, MAE `0.78R`, realized `0.44R`
- Management hypothesis: Balanced target/ratchet candidate; replay variants before naming.

Required kill tests before promotion:
- Discovery vs holdout split
- Pair-level concentration inside family
- Standalone raw-M5 replay, not inherited probe replay
- Factor expansion to full 47 raw factors at entry

## MS-006 usd_base short asia_q2 lower_band/low/bbw_wide/echo_compressed

Entry-state synchrony:
- Pair family: `usd_base`
- Direction: `short`
- Time: `asia` / `asia_q2`
- BB location: `lower_band`
- RSI state: `low`
- EMA20 distance: `ema_mid`
- Band width: `bbw_wide`
- Echo/range state: `echo_compressed`

Historical behavior:
- Sample: `164` trades
- Clean 2R winners: `74` (`45.1%`), enrichment `2.00x` vs corpus baseline
- Potential 2R reach rate: `51.2%`
- Gave-back-green rate: `17.1%`
- Mean path: MFE `1.40R`, MAE `0.70R`, realized `0.47R`
- Management hypothesis: Balanced target/ratchet candidate; replay variants before naming.

Required kill tests before promotion:
- Discovery vs holdout split
- Pair-level concentration inside family
- Standalone raw-M5 replay, not inherited probe replay
- Factor expansion to full 47 raw factors at entry

## MS-007 usd_base short asia_q2 upper_band/low/bbw_wide/echo_explosive

Entry-state synchrony:
- Pair family: `usd_base`
- Direction: `short`
- Time: `asia` / `asia_q2`
- BB location: `upper_band`
- RSI state: `low`
- EMA20 distance: `ema_near`
- Band width: `bbw_wide`
- Echo/range state: `echo_explosive`

Historical behavior:
- Sample: `122` trades
- Clean 2R winners: `56` (`45.9%`), enrichment `2.03x` vs corpus baseline
- Potential 2R reach rate: `50.8%`
- Gave-back-green rate: `24.6%`
- Mean path: MFE `1.58R`, MAE `0.69R`, realized `0.54R`
- Management hypothesis: Entry-shape works but management is suspect; test earlier protection/partial logic.

Required kill tests before promotion:
- Discovery vs holdout split
- Pair-level concentration inside family
- Standalone raw-M5 replay, not inherited probe replay
- Factor expansion to full 47 raw factors at entry

## MS-008 usd_base short asia_q4 upper_band/low/bbw_mid/echo_compressed

Entry-state synchrony:
- Pair family: `usd_base`
- Direction: `short`
- Time: `asia` / `asia_q4`
- BB location: `upper_band`
- RSI state: `low`
- EMA20 distance: `ema_far`
- Band width: `bbw_mid`
- Echo/range state: `echo_compressed`

Historical behavior:
- Sample: `128` trades
- Clean 2R winners: `56` (`43.8%`), enrichment `1.94x` vs corpus baseline
- Potential 2R reach rate: `46.9%`
- Gave-back-green rate: `12.5%`
- Mean path: MFE `1.33R`, MAE `0.84R`, realized `0.37R`
- Management hypothesis: Balanced target/ratchet candidate; replay variants before naming.

Required kill tests before promotion:
- Discovery vs holdout split
- Pair-level concentration inside family
- Standalone raw-M5 replay, not inherited probe replay
- Factor expansion to full 47 raw factors at entry

## MS-009 usd_base short overlap_q1 middle/low/bbw_wide/echo_explosive

Entry-state synchrony:
- Pair family: `usd_base`
- Direction: `short`
- Time: `overlap` / `overlap_q1`
- BB location: `middle`
- RSI state: `low`
- EMA20 distance: `ema_near`
- Band width: `bbw_wide`
- Echo/range state: `echo_explosive`

Historical behavior:
- Sample: `124` trades
- Clean 2R winners: `54` (`43.5%`), enrichment `1.93x` vs corpus baseline
- Potential 2R reach rate: `46.8%`
- Gave-back-green rate: `18.5%`
- Mean path: MFE `1.56R`, MAE `0.62R`, realized `0.66R`
- Management hypothesis: Balanced target/ratchet candidate; replay variants before naming.

Required kill tests before promotion:
- Discovery vs holdout split
- Pair-level concentration inside family
- Standalone raw-M5 replay, not inherited probe replay
- Factor expansion to full 47 raw factors at entry

## MS-010 gbp_cross short london_q1 lower_band/low/bbw_mid/echo_explosive

Entry-state synchrony:
- Pair family: `gbp_cross`
- Direction: `short`
- Time: `london` / `london_q1`
- BB location: `lower_band`
- RSI state: `low`
- EMA20 distance: `ema_mid`
- Band width: `bbw_mid`
- Echo/range state: `echo_explosive`

Historical behavior:
- Sample: `238` trades
- Clean 2R winners: `98` (`41.2%`), enrichment `1.83x` vs corpus baseline
- Potential 2R reach rate: `47.1%`
- Gave-back-green rate: `12.6%`
- Mean path: MFE `1.40R`, MAE `0.75R`, realized `0.49R`
- Management hypothesis: Hold-for-target candidate; giveback is relatively low for this cell.

Required kill tests before promotion:
- Discovery vs holdout split
- Pair-level concentration inside family
- Standalone raw-M5 replay, not inherited probe replay
- Factor expansion to full 47 raw factors at entry

## MS-011 antipodean_cross short london_q2 lower_band/low/bbw_wide/echo_explosive

Entry-state synchrony:
- Pair family: `antipodean_cross`
- Direction: `short`
- Time: `london` / `london_q2`
- BB location: `lower_band`
- RSI state: `low`
- EMA20 distance: `ema_mid`
- Band width: `bbw_wide`
- Echo/range state: `echo_explosive`

Historical behavior:
- Sample: `130` trades
- Clean 2R winners: `56` (`43.1%`), enrichment `1.91x` vs corpus baseline
- Potential 2R reach rate: `46.2%`
- Gave-back-green rate: `14.6%`
- Mean path: MFE `1.39R`, MAE `0.76R`, realized `0.43R`
- Management hypothesis: Hold-for-target candidate; giveback is relatively low for this cell.

Required kill tests before promotion:
- Discovery vs holdout split
- Pair-level concentration inside family
- Standalone raw-M5 replay, not inherited probe replay
- Factor expansion to full 47 raw factors at entry

## MS-012 eur_cross long overlap_q2 upper_band/high/bbw_wide/echo_mid

Entry-state synchrony:
- Pair family: `eur_cross`
- Direction: `long`
- Time: `overlap` / `overlap_q2`
- BB location: `upper_band`
- RSI state: `high`
- EMA20 distance: `ema_mid`
- Band width: `bbw_wide`
- Echo/range state: `echo_mid`

Historical behavior:
- Sample: `136` trades
- Clean 2R winners: `58` (`42.6%`), enrichment `1.89x` vs corpus baseline
- Potential 2R reach rate: `44.1%`
- Gave-back-green rate: `19.9%`
- Mean path: MFE `1.48R`, MAE `0.67R`, realized `0.53R`
- Management hypothesis: Balanced target/ratchet candidate; replay variants before naming.

Required kill tests before promotion:
- Discovery vs holdout split
- Pair-level concentration inside family
- Standalone raw-M5 replay, not inherited probe replay
- Factor expansion to full 47 raw factors at entry

## MS-013 antipodean_cross short asia_q1 lower_band/low/bbw_wide/echo_mid

Entry-state synchrony:
- Pair family: `antipodean_cross`
- Direction: `short`
- Time: `asia` / `asia_q1`
- BB location: `lower_band`
- RSI state: `low`
- EMA20 distance: `ema_mid`
- Band width: `bbw_wide`
- Echo/range state: `echo_mid`

Historical behavior:
- Sample: `178` trades
- Clean 2R winners: `74` (`41.6%`), enrichment `1.84x` vs corpus baseline
- Potential 2R reach rate: `46.1%`
- Gave-back-green rate: `9.6%`
- Mean path: MFE `1.29R`, MAE `0.69R`, realized `0.36R`
- Management hypothesis: Balanced target/ratchet candidate; replay variants before naming.

Required kill tests before promotion:
- Discovery vs holdout split
- Pair-level concentration inside family
- Standalone raw-M5 replay, not inherited probe replay
- Factor expansion to full 47 raw factors at entry

## MS-014 usd_base long asia_q2 lower_band/high/bbw_wide/echo_explosive

Entry-state synchrony:
- Pair family: `usd_base`
- Direction: `long`
- Time: `asia` / `asia_q2`
- BB location: `lower_band`
- RSI state: `high`
- EMA20 distance: `ema_near`
- Band width: `bbw_wide`
- Echo/range state: `echo_explosive`

Historical behavior:
- Sample: `126` trades
- Clean 2R winners: `54` (`42.9%`), enrichment `1.90x` vs corpus baseline
- Potential 2R reach rate: `47.6%`
- Gave-back-green rate: `13.5%`
- Mean path: MFE `1.48R`, MAE `0.65R`, realized `0.51R`
- Management hypothesis: Hold-for-target candidate; giveback is relatively low for this cell.

Required kill tests before promotion:
- Discovery vs holdout split
- Pair-level concentration inside family
- Standalone raw-M5 replay, not inherited probe replay
- Factor expansion to full 47 raw factors at entry

## MS-015 usd_base short london_q2 lower_rail/low/bbw_wide/echo_expanded

Entry-state synchrony:
- Pair family: `usd_base`
- Direction: `short`
- Time: `london` / `london_q2`
- BB location: `lower_rail`
- RSI state: `low`
- EMA20 distance: `ema_mid`
- Band width: `bbw_wide`
- Echo/range state: `echo_expanded`

Historical behavior:
- Sample: `180` trades
- Clean 2R winners: `74` (`41.1%`), enrichment `1.82x` vs corpus baseline
- Potential 2R reach rate: `48.9%`
- Gave-back-green rate: `18.9%`
- Mean path: MFE `1.47R`, MAE `0.80R`, realized `0.49R`
- Management hypothesis: Balanced target/ratchet candidate; replay variants before naming.

Required kill tests before promotion:
- Discovery vs holdout split
- Pair-level concentration inside family
- Standalone raw-M5 replay, not inherited probe replay
- Factor expansion to full 47 raw factors at entry

## MS-016 antipodean_cross long london_q1 lower_band/high/bbw_wide/echo_explosive

Entry-state synchrony:
- Pair family: `antipodean_cross`
- Direction: `long`
- Time: `london` / `london_q1`
- BB location: `lower_band`
- RSI state: `high`
- EMA20 distance: `ema_near`
- Band width: `bbw_wide`
- Echo/range state: `echo_explosive`

Historical behavior:
- Sample: `102` trades
- Clean 2R winners: `44` (`43.1%`), enrichment `1.91x` vs corpus baseline
- Potential 2R reach rate: `45.1%`
- Gave-back-green rate: `26.5%`
- Mean path: MFE `1.55R`, MAE `0.64R`, realized `0.55R`
- Management hypothesis: Entry-shape works but management is suspect; test earlier protection/partial logic.

Required kill tests before promotion:
- Discovery vs holdout split
- Pair-level concentration inside family
- Standalone raw-M5 replay, not inherited probe replay
- Factor expansion to full 47 raw factors at entry

## MS-017 antipodean_cross short london_q4 upper_rail/high/bbw_wide/echo_compressed

Entry-state synchrony:
- Pair family: `antipodean_cross`
- Direction: `short`
- Time: `london` / `london_q4`
- BB location: `upper_rail`
- RSI state: `high`
- EMA20 distance: `ema_mid`
- Band width: `bbw_wide`
- Echo/range state: `echo_compressed`

Historical behavior:
- Sample: `114` trades
- Clean 2R winners: `48` (`42.1%`), enrichment `1.87x` vs corpus baseline
- Potential 2R reach rate: `45.6%`
- Gave-back-green rate: `8.8%`
- Mean path: MFE `1.33R`, MAE `0.77R`, realized `0.43R`
- Management hypothesis: Balanced target/ratchet candidate; replay variants before naming.

Required kill tests before promotion:
- Discovery vs holdout split
- Pair-level concentration inside family
- Standalone raw-M5 replay, not inherited probe replay
- Factor expansion to full 47 raw factors at entry

## MS-018 antipodean_cross short asia_q1 upper_band/low/bbw_mid/echo_compressed

Entry-state synchrony:
- Pair family: `antipodean_cross`
- Direction: `short`
- Time: `asia` / `asia_q1`
- BB location: `upper_band`
- RSI state: `low`
- EMA20 distance: `ema_far`
- Band width: `bbw_mid`
- Echo/range state: `echo_compressed`

Historical behavior:
- Sample: `174` trades
- Clean 2R winners: `70` (`40.2%`), enrichment `1.78x` vs corpus baseline
- Potential 2R reach rate: `46.0%`
- Gave-back-green rate: `16.1%`
- Mean path: MFE `1.30R`, MAE `0.79R`, realized `0.30R`
- Management hypothesis: Balanced target/ratchet candidate; replay variants before naming.

Required kill tests before promotion:
- Discovery vs holdout split
- Pair-level concentration inside family
- Standalone raw-M5 replay, not inherited probe replay
- Factor expansion to full 47 raw factors at entry

## MS-019 antipodean_cross long london_q1 upper_band/high/bbw_wide/echo_explosive

Entry-state synchrony:
- Pair family: `antipodean_cross`
- Direction: `long`
- Time: `london` / `london_q1`
- BB location: `upper_band`
- RSI state: `high`
- EMA20 distance: `ema_mid`
- Band width: `bbw_wide`
- Echo/range state: `echo_explosive`

Historical behavior:
- Sample: `262` trades
- Clean 2R winners: `102` (`38.9%`), enrichment `1.73x` vs corpus baseline
- Potential 2R reach rate: `45.8%`
- Gave-back-green rate: `13.7%`
- Mean path: MFE `1.42R`, MAE `0.71R`, realized `0.52R`
- Management hypothesis: Hold-for-target candidate; giveback is relatively low for this cell.

Required kill tests before promotion:
- Discovery vs holdout split
- Pair-level concentration inside family
- Standalone raw-M5 replay, not inherited probe replay
- Factor expansion to full 47 raw factors at entry

## MS-020 eur_cross long london_q1 middle/high/bbw_mid/echo_expanded

Entry-state synchrony:
- Pair family: `eur_cross`
- Direction: `long`
- Time: `london` / `london_q1`
- BB location: `middle`
- RSI state: `high`
- EMA20 distance: `ema_mid`
- Band width: `bbw_mid`
- Echo/range state: `echo_expanded`

Historical behavior:
- Sample: `186` trades
- Clean 2R winners: `74` (`39.8%`), enrichment `1.76x` vs corpus baseline
- Potential 2R reach rate: `41.9%`
- Gave-back-green rate: `21.0%`
- Mean path: MFE `1.33R`, MAE `0.74R`, realized `0.30R`
- Management hypothesis: Entry-shape works but management is suspect; test earlier protection/partial logic.

Required kill tests before promotion:
- Discovery vs holdout split
- Pair-level concentration inside family
- Standalone raw-M5 replay, not inherited probe replay
- Factor expansion to full 47 raw factors at entry

