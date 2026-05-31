# EUR_CHF — R26 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_0**  (5m ATR <33% stop)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20d**  (EMA20 down 0.15-0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR3**  (60-90%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **630**  (W=412 / L=218)  -  WR: **65.4%**

## Session distribution

- asia: n=215  W=145/L=70  WR=67.4%
- ny_close: n=131  W=87/L=44  WR=66.4%
- ny_mid: n=65  W=47/L=18  WR=72.3%
- ny_open: n=62  W=34/L=28  WR=54.8%
- off_hours: n=59  W=32/L=27  WR=54.2%
- london: n=51  W=34/L=17  WR=66.7%
- london_open: n=33  W=26/L=7  WR=78.8%
- asia_late: n=14  W=7/L=7  WR=50.0%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1c AND ZS=ZS1 AND direction_exec=long`
- Raw: n=101  W=87/L=14  WR=86.1%
- Refine: exclude RSI=RSI3 drops 7/14 losers (50%)
- **Final: n=84  W=77/L=7  WR=91.7%**
- **Dir: LONG**  •  1h trend AGAINST trade; zscore -3 to -2 deep oversold  •  AVOID when RSI 40-50 lower neutral

### W02.  `T1=T1c AND T4=T4c AND ZS=ZS1`
- Raw: n=94  W=81/L=13  WR=86.2%
- Refine: exclude RSI=RSI3 drops 7/13 losers (54%)
- **Final: n=77  W=71/L=6  WR=92.2%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  AVOID when RSI 40-50 lower neutral

### W03.  `T1=T1c AND T4=T4c AND ZS=ZS1 AND direction_exec=long`
- Raw: n=94  W=81/L=13  WR=86.2%
- Refine: exclude RSI=RSI3 drops 7/13 losers (54%)
- **Final: n=77  W=71/L=6  WR=92.2%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  AVOID when RSI 40-50 lower neutral

### W04.  `H60=H60e AND T1=T1c AND ZS=ZS1`
- Raw: n=89  W=77/L=12  WR=86.5%
- Refine: exclude RSI=RSI3 drops 6/12 losers (50%)
- **Final: n=74  W=68/L=6  WR=91.9%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; zscore -3 to -2 deep oversold  •  AVOID when RSI 40-50 lower neutral

### W05.  `H60=H60e AND T1=T1c AND ZS=ZS1 AND direction_exec=long`
- Raw: n=89  W=77/L=12  WR=86.5%
- Refine: exclude RSI=RSI3 drops 6/12 losers (50%)
- **Final: n=74  W=68/L=6  WR=91.9%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend AGAINST trade; zscore -3 to -2 deep oversold  •  AVOID when RSI 40-50 lower neutral

### W06.  `H20=H20e AND T1=T1c AND ZS=ZS1`
- Raw: n=85  W=73/L=12  WR=85.9%
- Refine: exclude RSI=RSI3 drops 6/12 losers (50%)
- **Final: n=76  W=70/L=6  WR=92.1%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; zscore -3 to -2 deep oversold  •  AVOID when RSI 40-50 lower neutral

### W07.  `H20=H20e AND T1=T1c AND ZS=ZS1 AND direction_exec=long`
- Raw: n=85  W=73/L=12  WR=85.9%
- Refine: exclude RSI=RSI3 drops 6/12 losers (50%)
- **Final: n=76  W=70/L=6  WR=92.1%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade; zscore -3 to -2 deep oversold  •  AVOID when RSI 40-50 lower neutral

### W08.  `H60=H60e AND T1=T1c AND T4=T4c AND ZS=ZS1`
- Raw: n=82  W=71/L=11  WR=86.6%
- Refine: exclude RSI=RSI3 drops 6/11 losers (55%)
- **Final: n=67  W=62/L=5  WR=92.5%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  AVOID when RSI 40-50 lower neutral

### W09.  `T1=T1c AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=78  W=73/L=5  WR=93.6%
- Refine: exclude strategy_id=delta_tag_and_go_v2 drops 2/5 losers (40%)
- **Final: n=70  W=67/L=3  WR=95.7%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  AVOID when strategy=delta_tag_and_go_v2

### W10.  `RSI=RSI2 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=78  W=73/L=5  WR=93.6%
- Refine: exclude strategy_id=delta_tag_and_go_v2 drops 2/5 losers (40%)
- **Final: n=70  W=67/L=3  WR=95.7%**
- **Dir: LONG**  •  RSI 30-40 weak; zscore -3 to -2 deep oversold  •  AVOID when strategy=delta_tag_and_go_v2

### W11.  `T1=T1c AND RSI=RSI2 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=78  W=73/L=5  WR=93.6%
- Refine: exclude strategy_id=delta_tag_and_go_v2 drops 2/5 losers (40%)
- **Final: n=70  W=67/L=3  WR=95.7%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  AVOID when strategy=delta_tag_and_go_v2

### W12.  `H20=H20e AND T1=T1c AND T4=T4c AND ZS=ZS1`
- Raw: n=78  W=67/L=11  WR=85.9%
- Refine: exclude RSI=RSI3 drops 6/11 losers (55%)
- **Final: n=69  W=64/L=5  WR=92.8%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  AVOID when RSI 40-50 lower neutral

### W13.  `T4=T4c AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=76  W=67/L=9  WR=88.2%
- Refine: exclude H60=H60a drops 5/9 losers (56%)
- **Final: n=71  W=67/L=4  WR=94.4%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  AVOID when HTF60 aligned WITH trade

### W14.  `H60=H60e AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=75  W=67/L=8  WR=89.3%
- Refine: exclude ZS=ZS4 drops 3/8 losers (38%)
- **Final: n=67  W=62/L=5  WR=92.5%**
- **Dir: ?**  •  HTF60 strongly against; RSI 30-40 weak; session=asia  •  AVOID when zscore +1 to +2 overbought

### W15.  `T1=T1c AND T4=T4c AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=71  W=67/L=4  WR=94.4%
- Refine: exclude strategy_id=delta_tag_and_go_v2 drops 2/4 losers (50%)
- **Final: n=64  W=62/L=2  WR=96.9%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  AVOID when strategy=delta_tag_and_go_v2

### W16.  `T4=T4c AND RSI=RSI2 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=71  W=67/L=4  WR=94.4%
- Refine: exclude strategy_id=delta_tag_and_go_v2 drops 2/4 losers (50%)
- **Final: n=64  W=62/L=2  WR=96.9%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  AVOID when strategy=delta_tag_and_go_v2

### W17.  `H20=H20e AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=70  W=66/L=4  WR=94.3%
- Refine: exclude session_bucket=ny_close drops 2/4 losers (50%)
- **Final: n=50  W=48/L=2  WR=96.0%**
- **Dir: ?**  •  HTF20 strongly against; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  AVOID when session=ny_close

### W18.  `H20=H20e AND T1=T1c AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=70  W=66/L=4  WR=94.3%
- Refine: exclude session_bucket=ny_close drops 2/4 losers (50%)
- **Final: n=50  W=48/L=2  WR=96.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  AVOID when session=ny_close

### W19.  `H20=H20e AND RSI=RSI2 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=70  W=66/L=4  WR=94.3%
- Refine: exclude session_bucket=ny_close drops 2/4 losers (50%)
- **Final: n=50  W=48/L=2  WR=96.0%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  AVOID when session=ny_close

### W20.  `H60=H60e AND T1=T1c AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=70  W=63/L=7  WR=90.0%
- Refine: exclude ZS=ZS4 drops 3/7 losers (43%)
- **Final: n=66  W=62/L=4  WR=93.9%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 30-40 weak; session=asia  •  AVOID when zscore +1 to +2 overbought

### W21.  `H60=H60e AND T4=T4c AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=70  W=63/L=7  WR=90.0%
- Refine: exclude ZS=ZS4 drops 3/7 losers (43%)
- **Final: n=66  W=62/L=4  WR=93.9%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 30-40 weak; session=asia  •  AVOID when zscore +1 to +2 overbought

### W22.  `H60=H60e AND RSI=RSI2 AND direction_exec=long AND session_bucket=asia`
- Raw: n=70  W=63/L=7  WR=90.0%
- Refine: exclude ZS=ZS4 drops 3/7 losers (43%)
- **Final: n=66  W=62/L=4  WR=93.9%**
- **Dir: LONG**  •  HTF60 strongly against; RSI 30-40 weak; session=asia  •  AVOID when zscore +1 to +2 overbought

### W23.  `H60=H60e AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=68  W=64/L=4  WR=94.1%
- Refine: exclude session_bucket=ny_close drops 2/4 losers (50%)
- **Final: n=54  W=52/L=2  WR=96.3%**
- **Dir: ?**  •  HTF60 strongly against; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  AVOID when session=ny_close

### W24.  `H60=H60e AND T1=T1c AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=68  W=64/L=4  WR=94.1%
- Refine: exclude session_bucket=ny_close drops 2/4 losers (50%)
- **Final: n=54  W=52/L=2  WR=96.3%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  AVOID when session=ny_close

### W25.  `H60=H60e AND RSI=RSI2 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=68  W=64/L=4  WR=94.1%
- Refine: exclude session_bucket=ny_close drops 2/4 losers (50%)
- **Final: n=54  W=52/L=2  WR=96.3%**
- **Dir: LONG**  •  HTF60 strongly against; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  AVOID when session=ny_close

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1a AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=33  W=10/L=23  WR=30.3%
- Sharpen: sharpest is T4=T4c (5/23 of losers there)
- **Sharp: n=5  W=0/L=5  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when 4h trend AGAINST trade

### L02.  `RSI=RSI2 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=33  W=10/L=23  WR=30.3%
- Sharpen: sharpest is T4=T4c (5/23 of losers there)
- **Sharp: n=5  W=0/L=5  WR=0.0%**
- **Dir: SHORT**  •  RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when 4h trend AGAINST trade

### L03.  `T1=T1a AND RSI=RSI2 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=33  W=10/L=23  WR=30.3%
- Sharpen: sharpest is T4=T4c (5/23 of losers there)
- **Sharp: n=5  W=0/L=5  WR=0.0%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when 4h trend AGAINST trade

### L04.  `H20=H20a AND RSI=RSI2 AND session_bucket=ny_close`
- Raw: n=33  W=11/L=22  WR=33.3%
- Sharpen: sharpest is H60=H60c (8/22 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 30-40 weak; session=ny_close  •  ONLY when HTF60 neutral

### L05.  `T1=T1a AND RSI=RSI2 AND session_bucket=ny_close`
- Raw: n=33  W=11/L=22  WR=33.3%
- Sharpen: sharpest is H60=H60c (8/22 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; RSI 30-40 weak; session=ny_close  •  ONLY when HTF60 neutral

### L06.  `T4=T4a AND RSI=RSI2 AND session_bucket=ny_close`
- Raw: n=33  W=11/L=22  WR=33.3%
- Sharpen: sharpest is H60=H60c (8/22 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: ?**  •  4h trend WITH trade; RSI 30-40 weak; session=ny_close  •  ONLY when HTF60 neutral

### L07.  `RSI=RSI2 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=33  W=11/L=22  WR=33.3%
- Sharpen: sharpest is H60=H60c (8/22 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: SHORT**  •  RSI 30-40 weak; session=ny_close  •  ONLY when HTF60 neutral

### L08.  `H20=H20a AND T1=T1a AND RSI=RSI2 AND session_bucket=ny_close`
- Raw: n=33  W=11/L=22  WR=33.3%
- Sharpen: sharpest is H60=H60c (8/22 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 30-40 weak; session=ny_close  •  ONLY when HTF60 neutral

### L09.  `H20=H20a AND T4=T4a AND RSI=RSI2 AND session_bucket=ny_close`
- Raw: n=33  W=11/L=22  WR=33.3%
- Sharpen: sharpest is H60=H60c (8/22 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 30-40 weak; session=ny_close  •  ONLY when HTF60 neutral

### L10.  `H20=H20a AND RSI=RSI2 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=33  W=11/L=22  WR=33.3%
- Sharpen: sharpest is H60=H60c (8/22 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 30-40 weak; session=ny_close  •  ONLY when HTF60 neutral

### L11.  `T1=T1a AND T4=T4a AND RSI=RSI2 AND session_bucket=ny_close`
- Raw: n=33  W=11/L=22  WR=33.3%
- Sharpen: sharpest is H60=H60c (8/22 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 30-40 weak; session=ny_close  •  ONLY when HTF60 neutral

### L12.  `T1=T1a AND RSI=RSI2 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=33  W=11/L=22  WR=33.3%
- Sharpen: sharpest is H60=H60c (8/22 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 30-40 weak; session=ny_close  •  ONLY when HTF60 neutral

### L13.  `T4=T4a AND RSI=RSI2 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=33  W=11/L=22  WR=33.3%
- Sharpen: sharpest is H60=H60c (8/22 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 30-40 weak; session=ny_close  •  ONLY when HTF60 neutral

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20e(41/31), H20d(20/14) | H20a(25/34), H20b(13/19) |
| H60 | H60e(45/35) | H60a(32/39) |
| T1 | T1c(64/40) | T1a(36/60) |
| T4 | T4c(57/50) | T4a(43/50) |
| BBP | BBP1(17/11) | — |
| RSI | — | — |
| ZS | ZS1(28/19) | — |
| strategy_id | — | — |
| direction_exec | long(63/42) | short(37/58) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
