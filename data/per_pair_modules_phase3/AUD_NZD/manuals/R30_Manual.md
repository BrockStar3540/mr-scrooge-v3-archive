# AUD_NZD — R30 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_0**  (5m ATR <33% stop)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **2,990**  (W=1,894 / L=1,096)  -  WR: **63.3%**

## Session distribution

- ny_close: n=913  W=570/L=343  WR=62.4%
- asia: n=859  W=556/L=303  WR=64.7%
- london: n=339  W=217/L=122  WR=64.0%
- ny_open: n=258  W=164/L=94  WR=63.6%
- off_hours: n=202  W=115/L=87  WR=56.9%
- london_open: n=168  W=111/L=57  WR=66.1%
- asia_late: n=142  W=85/L=57  WR=59.9%
- ny_mid: n=109  W=76/L=33  WR=69.7%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND T1=T1a AND BBP=BBP4`
- Raw: n=180  W=155/L=25  WR=86.1%
- Refine: exclude strategy_id=alpha_breakout_retest_v2 drops 6/25 losers (24%)
- **Final: n=168  W=149/L=19  WR=88.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; upper third  •  AVOID when strategy=alpha_breakout_retest_v2

### W02.  `H20=H20a AND T1=T1a AND ZS=ZS4`
- Raw: n=164  W=143/L=21  WR=87.2%
- Refine: exclude session_bucket=ny_close drops 15/21 losers (71%)
- **Final: n=88  W=82/L=6  WR=93.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; zscore +1 to +2 overbought  •  AVOID when session=ny_close

### W03.  `H20=H20a AND T1=T1a AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=164  W=143/L=21  WR=87.2%
- Refine: exclude session_bucket=ny_close drops 15/21 losers (71%)
- **Final: n=88  W=82/L=6  WR=93.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; upper third; zscore +1 to +2 overbought  •  AVOID when session=ny_close

### W04.  `H20=H20a AND H60=H60a AND T1=T1a AND BBP=BBP4`
- Raw: n=159  W=136/L=23  WR=85.5%
- Refine: exclude strategy_id=alpha_breakout_retest_v2 drops 6/23 losers (26%)
- **Final: n=149  W=132/L=17  WR=88.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; upper third  •  AVOID when strategy=alpha_breakout_retest_v2

### W05.  `H20=H20a AND T1=T1a AND BBP=BBP4 AND direction_exec=long`
- Raw: n=159  W=136/L=23  WR=85.5%
- Refine: exclude strategy_id=alpha_breakout_retest_v2 drops 6/23 losers (26%)
- **Final: n=149  W=132/L=17  WR=88.6%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; upper third  •  AVOID when strategy=alpha_breakout_retest_v2

### W06.  `H60=H60a AND T1=T1a AND RSI=RSI5`
- Raw: n=156  W=136/L=20  WR=87.2%
- Refine: exclude session_bucket=ny_close drops 19/20 losers (95%)
- **Final: n=132  W=131/L=1  WR=99.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when session=ny_close

### W07.  `H60=H60a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=156  W=136/L=20  WR=87.2%
- Refine: exclude session_bucket=ny_close drops 19/20 losers (95%)
- **Final: n=132  W=131/L=1  WR=99.2%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 60-70 strong  •  AVOID when session=ny_close

### W08.  `T1=T1a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=156  W=136/L=20  WR=87.2%
- Refine: exclude session_bucket=ny_close drops 19/20 losers (95%)
- **Final: n=132  W=131/L=1  WR=99.2%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 60-70 strong  •  AVOID when session=ny_close

### W09.  `H60=H60a AND T1=T1a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=156  W=136/L=20  WR=87.2%
- Refine: exclude session_bucket=ny_close drops 19/20 losers (95%)
- **Final: n=132  W=131/L=1  WR=99.2%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when session=ny_close

### W10.  `H20=H20a AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=153  W=132/L=21  WR=86.3%
- Refine: exclude T4=T4a drops 20/21 losers (95%)
- **Final: n=53  W=52/L=1  WR=98.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 50-60 upper neutral; session=asia  •  AVOID when 4h trend WITH trade

### W11.  `H20=H20a AND T4=T4a AND RSI=RSI4 AND session_bucket=ny_close`
- Raw: n=152  W=132/L=20  WR=86.8%
- Refine: exclude ZS=ZS4 drops 18/20 losers (90%)
- **Final: n=57  W=55/L=2  WR=96.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral; session=ny_close  •  AVOID when zscore +1 to +2 overbought

### W12.  `H20=H20a AND H60=H60a AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=151  W=130/L=21  WR=86.1%
- Refine: exclude T4=T4a drops 20/21 losers (95%)
- **Final: n=51  W=50/L=1  WR=98.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 50-60 upper neutral; session=asia  •  AVOID when 4h trend WITH trade

### W13.  `H20=H20a AND RSI=RSI4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=151  W=130/L=21  WR=86.1%
- Refine: exclude T4=T4a drops 20/21 losers (95%)
- **Final: n=51  W=50/L=1  WR=98.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 50-60 upper neutral; session=asia  •  AVOID when 4h trend WITH trade

### W14.  `H20=H20a AND H60=H60a AND T1=T1a AND ZS=ZS4`
- Raw: n=144  W=125/L=19  WR=86.8%
- Refine: exclude session_bucket=ny_close drops 13/19 losers (68%)
- **Final: n=84  W=78/L=6  WR=92.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; zscore +1 to +2 overbought  •  AVOID when session=ny_close

### W15.  `H20=H20a AND T1=T1a AND ZS=ZS4 AND direction_exec=long`
- Raw: n=144  W=125/L=19  WR=86.8%
- Refine: exclude session_bucket=ny_close drops 13/19 losers (68%)
- **Final: n=84  W=78/L=6  WR=92.9%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; zscore +1 to +2 overbought  •  AVOID when session=ny_close

### W16.  `H20=H20a AND H60=H60a AND ZS=ZS5`
- Raw: n=140  W=119/L=21  WR=85.0%
- Refine: exclude session_bucket=ny_open drops 4/21 losers (19%)
- **Final: n=134  W=117/L=17  WR=87.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; zscore +2 to +3 deep overbought  •  AVOID when session=ny_open

### W17.  `H20=H20a AND T4=T4c AND RSI=RSI4`
- Raw: n=140  W=119/L=21  WR=85.0%
- Refine: exclude session_bucket=ny_close drops 16/21 losers (76%)
- **Final: n=83  W=78/L=5  WR=94.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when session=ny_close

### W18.  `H20=H20a AND ZS=ZS5 AND direction_exec=long`
- Raw: n=140  W=119/L=21  WR=85.0%
- Refine: exclude session_bucket=ny_open drops 4/21 losers (19%)
- **Final: n=134  W=117/L=17  WR=87.3%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; zscore +2 to +3 deep overbought  •  AVOID when session=ny_open

### W19.  `H20=H20a AND H60=H60a AND ZS=ZS5 AND direction_exec=long`
- Raw: n=140  W=119/L=21  WR=85.0%
- Refine: exclude session_bucket=ny_open drops 4/21 losers (19%)
- **Final: n=134  W=117/L=17  WR=87.3%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; zscore +2 to +3 deep overbought  •  AVOID when session=ny_open

### W20.  `H20=H20a AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=131  W=117/L=14  WR=89.3%
- Refine: exclude strategy_id=CP2_squeeze_momentum_long drops 4/14 losers (29%)
- **Final: n=121  W=111/L=10  WR=91.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when strategy=CP2_squeeze_momentum_long

### W21.  `H20=H20a AND T1=T1a AND T4=T4a AND ZS=ZS4`
- Raw: n=131  W=113/L=18  WR=86.3%
- Refine: exclude RSI=RSI4 drops 16/18 losers (89%)
- **Final: n=44  W=42/L=2  WR=95.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; zscore +1 to +2 overbought  •  AVOID when RSI 50-60 upper neutral

### W22.  `H60=H60a AND T4=T4a AND RSI=RSI5`
- Raw: n=130  W=111/L=19  WR=85.4%
- Refine: exclude session_bucket=ny_close drops 18/19 losers (95%)
- **Final: n=112  W=111/L=1  WR=99.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 60-70 strong  •  AVOID when session=ny_close

### W23.  `T1=T1a AND T4=T4a AND RSI=RSI5`
- Raw: n=130  W=111/L=19  WR=85.4%
- Refine: exclude session_bucket=ny_close drops 18/19 losers (95%)
- **Final: n=112  W=111/L=1  WR=99.1%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 60-70 strong  •  AVOID when session=ny_close

### W24.  `T4=T4a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=130  W=111/L=19  WR=85.4%
- Refine: exclude session_bucket=ny_close drops 18/19 losers (95%)
- **Final: n=112  W=111/L=1  WR=99.1%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 60-70 strong  •  AVOID when session=ny_close

### W25.  `H60=H60a AND T1=T1a AND T4=T4a AND RSI=RSI5`
- Raw: n=130  W=111/L=19  WR=85.4%
- Refine: exclude session_bucket=ny_close drops 18/19 losers (95%)
- **Final: n=112  W=111/L=1  WR=99.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; RSI 60-70 strong  •  AVOID when session=ny_close

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND T4=T4c AND ZS=ZS4`
- Raw: n=219  W=84/L=135  WR=38.4%
- Sharpen: no sharper sub-pattern
- **Sharp: n=219  W=84/L=135  WR=38.4%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; zscore +1 to +2 overbought

### L02.  `T4=T4c AND ZS=ZS4 AND direction_exec=short`
- Raw: n=219  W=84/L=135  WR=38.4%
- Sharpen: no sharper sub-pattern
- **Sharp: n=219  W=84/L=135  WR=38.4%**
- **Dir: SHORT**  •  4h trend AGAINST trade; zscore +1 to +2 overbought

### L03.  `H60=H60e AND T4=T4c AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=219  W=84/L=135  WR=38.4%
- Sharpen: no sharper sub-pattern
- **Sharp: n=219  W=84/L=135  WR=38.4%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; upper third; zscore +1 to +2 overbought

### L04.  `H60=H60e AND T4=T4c AND ZS=ZS4 AND direction_exec=short`
- Raw: n=219  W=84/L=135  WR=38.4%
- Sharpen: no sharper sub-pattern
- **Sharp: n=219  W=84/L=135  WR=38.4%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend AGAINST trade; zscore +1 to +2 overbought

### L05.  `T4=T4c AND BBP=BBP4 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=219  W=84/L=135  WR=38.4%
- Sharpen: no sharper sub-pattern
- **Sharp: n=219  W=84/L=135  WR=38.4%**
- **Dir: SHORT**  •  4h trend AGAINST trade; upper third; zscore +1 to +2 overbought

### L06.  `H20=H20e AND T4=T4c AND ZS=ZS4`
- Raw: n=163  W=64/L=99  WR=39.3%
- Sharpen: sharpest is session_bucket=ny_open (18/99 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  ONLY when session=ny_open

### L07.  `H20=H20e AND T4=T4c AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=163  W=64/L=99  WR=39.3%
- Sharpen: sharpest is session_bucket=ny_open (18/99 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; upper third; zscore +1 to +2 overbought  •  ONLY when session=ny_open

### L08.  `H20=H20e AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=156  W=61/L=95  WR=39.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=156  W=61/L=95  WR=39.1%**
- **Dir: ?**  •  HTF20 strongly against; upper third; RSI 50-60 upper neutral

### L09.  `H60=H60e AND T1=T1c AND T4=T4c AND BBP=BBP4`
- Raw: n=150  W=57/L=93  WR=38.0%
- Sharpen: sharpest is H20=H20c (26/93 of losers there)
- **Sharp: n=29  W=3/L=26  WR=10.3%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; upper third  •  ONLY when HTF20 neutral

### L10.  `T1=T1c AND T4=T4c AND BBP=BBP4 AND direction_exec=short`
- Raw: n=150  W=57/L=93  WR=38.0%
- Sharpen: sharpest is H20=H20c (26/93 of losers there)
- **Sharp: n=29  W=3/L=26  WR=10.3%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; upper third  •  ONLY when HTF20 neutral

### L11.  `H20=H20e AND H60=H60e AND T4=T4c AND ZS=ZS4`
- Raw: n=145  W=55/L=90  WR=37.9%
- Sharpen: sharpest is session_bucket=ny_open (17/90 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  ONLY when session=ny_open

### L12.  `H20=H20e AND T4=T4c AND ZS=ZS4 AND direction_exec=short`
- Raw: n=145  W=55/L=90  WR=37.9%
- Sharpen: sharpest is session_bucket=ny_open (17/90 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  ONLY when session=ny_open

### L13.  `H20=H20e AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=145  W=58/L=87  WR=40.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=145  W=58/L=87  WR=40.0%**
- **Dir: ?**  •  HTF20 strongly against; RSI 50-60 upper neutral; zscore +1 to +2 overbought

### L14.  `H20=H20e AND BBP=BBP4 AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=145  W=58/L=87  WR=40.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=145  W=58/L=87  WR=40.0%**
- **Dir: ?**  •  HTF20 strongly against; upper third; RSI 50-60 upper neutral; zscore +1 to +2 overbought

### L15.  `H20=H20e AND RSI=RSI4 AND session_bucket=ny_close`
- Raw: n=141  W=53/L=88  WR=37.6%
- Sharpen: sharpest is ZS=ZS5 (30/88 of losers there)
- **Sharp: n=36  W=6/L=30  WR=16.7%**
- **Dir: ?**  •  HTF20 strongly against; RSI 50-60 upper neutral; session=ny_close  •  ONLY when zscore +2 to +3 deep overbought

### L16.  `H60=H60e AND T1=T1c AND RSI=RSI5`
- Raw: n=137  W=45/L=92  WR=32.8%
- Sharpen: sharpest is H20=H20c (28/92 of losers there)
- **Sharp: n=31  W=3/L=28  WR=9.7%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when HTF20 neutral

### L17.  `H60=H60e AND RSI=RSI5 AND direction_exec=short`
- Raw: n=137  W=45/L=92  WR=32.8%
- Sharpen: sharpest is H20=H20c (28/92 of losers there)
- **Sharp: n=31  W=3/L=28  WR=9.7%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 60-70 strong  •  ONLY when HTF20 neutral

### L18.  `T1=T1c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=137  W=45/L=92  WR=32.8%
- Sharpen: sharpest is H20=H20c (28/92 of losers there)
- **Sharp: n=31  W=3/L=28  WR=9.7%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when HTF20 neutral

### L19.  `H60=H60e AND T1=T1c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=137  W=45/L=92  WR=32.8%
- Sharpen: sharpest is H20=H20c (28/92 of losers there)
- **Sharp: n=31  W=3/L=28  WR=9.7%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when HTF20 neutral

### L20.  `H60=H60e AND T1=T1c AND T4=T4c AND ZS=ZS4`
- Raw: n=135  W=49/L=86  WR=36.3%
- Sharpen: sharpest is H20=H20c (25/86 of losers there)
- **Sharp: n=28  W=3/L=25  WR=10.7%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  ONLY when HTF20 neutral

### L21.  `T1=T1c AND T4=T4c AND ZS=ZS4 AND direction_exec=short`
- Raw: n=135  W=49/L=86  WR=36.3%
- Sharpen: sharpest is H20=H20c (25/86 of losers there)
- **Sharp: n=28  W=3/L=25  WR=10.7%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  ONLY when HTF20 neutral

### L22.  `H20=H20e AND H60=H60e AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=135  W=51/L=84  WR=37.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=135  W=51/L=84  WR=37.8%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; upper third; RSI 50-60 upper neutral

### L23.  `H20=H20e AND BBP=BBP4 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=135  W=51/L=84  WR=37.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=135  W=51/L=84  WR=37.8%**
- **Dir: SHORT**  •  HTF20 strongly against; upper third; RSI 50-60 upper neutral

### L24.  `H20=H20c AND H60=H60e AND T1=T1c`
- Raw: n=133  W=51/L=82  WR=38.3%
- Sharpen: sharpest is T4=T4c (45/82 of losers there)
- **Sharp: n=52  W=7/L=45  WR=13.5%**
- **Dir: ?**  •  HTF20 neutral; HTF60 strongly against; 1h trend AGAINST trade  •  ONLY when 4h trend AGAINST trade

### L25.  `H20=H20c AND T1=T1c AND direction_exec=short`
- Raw: n=133  W=51/L=82  WR=38.3%
- Sharpen: sharpest is T4=T4c (45/82 of losers there)
- **Sharp: n=52  W=7/L=45  WR=13.5%**
- **Dir: SHORT**  •  HTF20 neutral; 1h trend AGAINST trade  •  ONLY when 4h trend AGAINST trade

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(38/26) | H20e(26/38) |
| H60 | H60a(57/45) | H60e(43/55) |
| T1 | T1a(52/46) | T1c(48/54) |
| T4 | T4a(56/44) | T4c(43/55) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(57/45) | short(43/55) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
