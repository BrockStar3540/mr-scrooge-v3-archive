# GBP_CHF — R38 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20d**  (EMA20 down 0.15-0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **1,418**  (W=913 / L=505)  -  WR: **64.4%**

## Session distribution

- asia: n=342  W=235/L=107  WR=68.7%
- london_open: n=237  W=151/L=86  WR=63.7%
- ny_close: n=237  W=150/L=87  WR=63.3%
- ny_mid: n=162  W=97/L=65  WR=59.9%
- ny_open: n=154  W=95/L=59  WR=61.7%
- london: n=129  W=92/L=37  WR=71.3%
- off_hours: n=84  W=48/L=36  WR=57.1%
- asia_late: n=73  W=45/L=28  WR=61.6%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND H60=H60d AND direction_exec=short`
- Raw: n=111  W=95/L=16  WR=85.6%
- Refine: exclude BBP=BBP4 drops 9/16 losers (56%)
- **Final: n=85  W=78/L=7  WR=91.8%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 mildly against  •  AVOID when upper third

### W02.  `H20=H20a AND H60=H60d AND T4=T4a AND direction_exec=short`
- Raw: n=111  W=95/L=16  WR=85.6%
- Refine: exclude BBP=BBP4 drops 9/16 losers (56%)
- **Final: n=85  W=78/L=7  WR=91.8%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 mildly against; 4h trend WITH trade  •  AVOID when upper third

### W03.  `H20=H20a AND H60=H60d AND T1=T1a AND T4=T4a`
- Raw: n=109  W=95/L=14  WR=87.2%
- Refine: exclude BBP=BBP4 drops 9/14 losers (64%)
- **Final: n=83  W=78/L=5  WR=94.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 mildly against; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when upper third

### W04.  `H20=H20a AND H60=H60d AND T1=T1a AND direction_exec=short`
- Raw: n=109  W=95/L=14  WR=87.2%
- Refine: exclude BBP=BBP4 drops 9/14 losers (64%)
- **Final: n=83  W=78/L=5  WR=94.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 mildly against; 1h trend WITH trade  •  AVOID when upper third

### W05.  `H60=H60a AND T1=T1a AND RSI=RSI3`
- Raw: n=87  W=78/L=9  WR=89.7%
- Refine: exclude direction_exec=long drops 5/9 losers (56%)
- **Final: n=65  W=61/L=4  WR=93.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when long

### W06.  `H60=H60d AND T1=T1c AND direction_exec=long`
- Raw: n=87  W=74/L=13  WR=85.1%
- Refine: exclude BBP=BBP2 drops 5/13 losers (38%)
- **Final: n=77  W=69/L=8  WR=89.6%**
- **Dir: LONG**  •  HTF60 mildly against; 1h trend AGAINST trade  •  AVOID when lower third

### W07.  `H60=H60d AND T1=T1c AND T4=T4c`
- Raw: n=79  W=68/L=11  WR=86.1%
- Refine: exclude BBP=BBP2 drops 5/11 losers (45%)
- **Final: n=71  W=65/L=6  WR=91.5%**
- **Dir: ?**  •  HTF60 mildly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  AVOID when lower third

### W08.  `H60=H60d AND T1=T1c AND T4=T4c AND direction_exec=long`
- Raw: n=79  W=68/L=11  WR=86.1%
- Refine: exclude BBP=BBP2 drops 5/11 losers (45%)
- **Final: n=71  W=65/L=6  WR=91.5%**
- **Dir: LONG**  •  HTF60 mildly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  AVOID when lower third

### W09.  `H20=H20b AND H60=H60a AND T1=T1a`
- Raw: n=78  W=67/L=11  WR=85.9%
- Refine: exclude BBP=BBP1 drops 3/11 losers (27%)
- **Final: n=72  W=64/L=8  WR=88.9%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 1h trend WITH trade  •  AVOID when just touched lower band

### W10.  `H60=H60a AND T4=T4a AND RSI=RSI3`
- Raw: n=70  W=61/L=9  WR=87.1%
- Refine: exclude H20=H20d drops 7/9 losers (78%)
- **Final: n=48  W=46/L=2  WR=95.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when HTF20 mildly against

### W11.  `H60=H60a AND T1=T1a AND session_bucket=london_open`
- Raw: n=68  W=60/L=8  WR=88.2%
- Refine: exclude ZS=ZS6 drops 3/8 losers (38%)
- **Final: n=62  W=57/L=5  WR=91.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=london_open  •  AVOID when zscore >+3 extreme

### W12.  `H60=H60a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=67  W=62/L=5  WR=92.5%
- Refine: exclude session_bucket=asia_late drops 2/5 losers (40%)
- **Final: n=65  W=62/L=3  WR=95.4%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral  •  AVOID when session=asia_late

### W13.  `H20=H20b AND H60=H60a AND T4=T4a`
- Raw: n=66  W=58/L=8  WR=87.9%
- Refine: exclude BBP=BBP1 drops 3/8 losers (38%)
- **Final: n=60  W=55/L=5  WR=91.7%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 4h trend WITH trade  •  AVOID when just touched lower band

### W14.  `H20=H20b AND H60=H60a AND direction_exec=short`
- Raw: n=66  W=58/L=8  WR=87.9%
- Refine: exclude BBP=BBP1 drops 3/8 losers (38%)
- **Final: n=60  W=55/L=5  WR=91.7%**
- **Dir: SHORT**  •  HTF20 slightly aligned; HTF60 aligned WITH trade  •  AVOID when just touched lower band

### W15.  `H20=H20b AND H60=H60a AND T1=T1a AND T4=T4a`
- Raw: n=66  W=58/L=8  WR=87.9%
- Refine: exclude BBP=BBP1 drops 3/8 losers (38%)
- **Final: n=60  W=55/L=5  WR=91.7%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when just touched lower band

### W16.  `H20=H20b AND H60=H60a AND T1=T1a AND direction_exec=short`
- Raw: n=66  W=58/L=8  WR=87.9%
- Refine: exclude BBP=BBP1 drops 3/8 losers (38%)
- **Final: n=60  W=55/L=5  WR=91.7%**
- **Dir: SHORT**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 1h trend WITH trade  •  AVOID when just touched lower band

### W17.  `H20=H20b AND H60=H60a AND T4=T4a AND direction_exec=short`
- Raw: n=66  W=58/L=8  WR=87.9%
- Refine: exclude BBP=BBP1 drops 3/8 losers (38%)
- **Final: n=60  W=55/L=5  WR=91.7%**
- **Dir: SHORT**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 4h trend WITH trade  •  AVOID when just touched lower band

### W18.  `H60=H60a AND T1=T1a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=65  W=61/L=4  WR=93.8%
- Refine: exclude session_bucket=asia_late drops 2/4 losers (50%)
- **Final: n=63  W=61/L=2  WR=96.8%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when session=asia_late

### W19.  `H60=H60d AND T1=T1a AND RSI=RSI2`
- Raw: n=61  W=52/L=9  WR=85.2%
- Refine: exclude session_bucket=london drops 4/9 losers (44%)
- **Final: n=55  W=50/L=5  WR=90.9%**
- **Dir: ?**  •  HTF60 mildly against; 1h trend WITH trade; RSI 30-40 weak  •  AVOID when session=london

### W20.  `H60=H60d AND T4=T4a AND RSI=RSI2`
- Raw: n=61  W=52/L=9  WR=85.2%
- Refine: exclude session_bucket=london drops 4/9 losers (44%)
- **Final: n=55  W=50/L=5  WR=90.9%**
- **Dir: ?**  •  HTF60 mildly against; 4h trend WITH trade; RSI 30-40 weak  •  AVOID when session=london

### W21.  `H60=H60d AND RSI=RSI2 AND direction_exec=short`
- Raw: n=61  W=52/L=9  WR=85.2%
- Refine: exclude session_bucket=london drops 4/9 losers (44%)
- **Final: n=55  W=50/L=5  WR=90.9%**
- **Dir: SHORT**  •  HTF60 mildly against; RSI 30-40 weak  •  AVOID when session=london

### W22.  `H60=H60d AND T1=T1a AND T4=T4a AND RSI=RSI2`
- Raw: n=61  W=52/L=9  WR=85.2%
- Refine: exclude session_bucket=london drops 4/9 losers (44%)
- **Final: n=55  W=50/L=5  WR=90.9%**
- **Dir: ?**  •  HTF60 mildly against; 1h trend WITH trade; 4h trend WITH trade; RSI 30-40 weak  •  AVOID when session=london

### W23.  `H60=H60d AND T1=T1a AND RSI=RSI2 AND direction_exec=short`
- Raw: n=61  W=52/L=9  WR=85.2%
- Refine: exclude session_bucket=london drops 4/9 losers (44%)
- **Final: n=55  W=50/L=5  WR=90.9%**
- **Dir: SHORT**  •  HTF60 mildly against; 1h trend WITH trade; RSI 30-40 weak  •  AVOID when session=london

### W24.  `H60=H60d AND T4=T4a AND RSI=RSI2 AND direction_exec=short`
- Raw: n=61  W=52/L=9  WR=85.2%
- Refine: exclude session_bucket=london drops 4/9 losers (44%)
- **Final: n=55  W=50/L=5  WR=90.9%**
- **Dir: SHORT**  •  HTF60 mildly against; 4h trend WITH trade; RSI 30-40 weak  •  AVOID when session=london

### W25.  `H20=H20a AND H60=H60d AND T1=T1a AND RSI=RSI2`
- Raw: n=58  W=52/L=6  WR=89.7%
- Refine: exclude session_bucket=london drops 4/6 losers (67%)
- **Final: n=52  W=50/L=2  WR=96.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 mildly against; 1h trend WITH trade; RSI 30-40 weak  •  AVOID when session=london

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20a AND H60=H60e AND T1=T1c`
- Raw: n=83  W=32/L=51  WR=38.6%
- Sharpen: sharpest is session_bucket=ny_mid (11/51 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend AGAINST trade  •  ONLY when session=ny_mid

### L02.  `H20=H20a AND H60=H60e AND T1=T1c AND direction_exec=long`
- Raw: n=83  W=32/L=51  WR=38.6%
- Sharpen: sharpest is session_bucket=ny_mid (11/51 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend AGAINST trade  •  ONLY when session=ny_mid

### L03.  `H20=H20e AND H60=H60b AND T4=T4c`
- Raw: n=80  W=31/L=49  WR=38.8%
- Sharpen: sharpest is BBP=BBP2 (18/49 of losers there)
- **Sharp: n=20  W=2/L=18  WR=10.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 slightly aligned; 4h trend AGAINST trade  •  ONLY when lower third

### L04.  `H20=H20e AND H60=H60b AND T1=T1c`
- Raw: n=76  W=29/L=47  WR=38.2%
- Sharpen: sharpest is BBP=BBP2 (17/47 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 slightly aligned; 1h trend AGAINST trade  •  ONLY when lower third

### L05.  `H20=H20e AND H60=H60b AND direction_exec=long`
- Raw: n=70  W=25/L=45  WR=35.7%
- Sharpen: sharpest is BBP=BBP2 (17/45 of losers there)
- **Sharp: n=19  W=2/L=17  WR=10.5%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 slightly aligned  •  ONLY when lower third

### L06.  `H20=H20e AND H60=H60b AND T4=T4c AND direction_exec=long`
- Raw: n=70  W=25/L=45  WR=35.7%
- Sharpen: sharpest is BBP=BBP2 (17/45 of losers there)
- **Sharp: n=19  W=2/L=17  WR=10.5%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 slightly aligned; 4h trend AGAINST trade  •  ONLY when lower third

### L07.  `H20=H20e AND H60=H60b AND T1=T1c AND T4=T4c`
- Raw: n=68  W=23/L=45  WR=33.8%
- Sharpen: sharpest is BBP=BBP2 (17/45 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 slightly aligned; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when lower third

### L08.  `H20=H20e AND H60=H60b AND T1=T1c AND direction_exec=long`
- Raw: n=68  W=23/L=45  WR=33.8%
- Sharpen: sharpest is BBP=BBP2 (17/45 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 slightly aligned; 1h trend AGAINST trade  •  ONLY when lower third

### L09.  `T1=T1c AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=68  W=25/L=43  WR=36.8%
- Sharpen: sharpest is RSI=RSI2 (39/43 of losers there)
- **Sharp: n=49  W=10/L=39  WR=20.4%**
- **Dir: LONG**  •  1h trend AGAINST trade; session=ny_mid  •  ONLY when RSI 30-40 weak

### L10.  `H20=H20e AND T1=T1c AND ZS=ZS2`
- Raw: n=68  W=27/L=41  WR=39.7%
- Sharpen: sharpest is H60=H60b (15/41 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; zscore -2 to -1 oversold  •  ONLY when HTF60 slightly aligned

### L11.  `H60=H60c AND T1=T1c AND T4=T4c`
- Raw: n=68  W=27/L=41  WR=39.7%
- Sharpen: sharpest is session_bucket=off_hours (15/41 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: ?**  •  HTF60 neutral; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when session=off_hours

### L12.  `H20=H20e AND T1=T1c AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=68  W=27/L=41  WR=39.7%
- Sharpen: sharpest is H60=H60b (15/41 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; lower third; zscore -2 to -1 oversold  •  ONLY when HTF60 slightly aligned

### L13.  `H60=H60c AND T1=T1c AND T4=T4c AND direction_exec=long`
- Raw: n=68  W=27/L=41  WR=39.7%
- Sharpen: sharpest is session_bucket=off_hours (15/41 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: LONG**  •  HTF60 neutral; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when session=off_hours

### L14.  `T1=T1c AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=62  W=20/L=42  WR=32.3%
- Sharpen: sharpest is RSI=RSI2 (38/42 of losers there)
- **Sharp: n=48  W=10/L=38  WR=20.8%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_mid  •  ONLY when RSI 30-40 weak

### L15.  `T4=T4c AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=62  W=20/L=42  WR=32.3%
- Sharpen: sharpest is RSI=RSI2 (38/42 of losers there)
- **Sharp: n=48  W=10/L=38  WR=20.8%**
- **Dir: LONG**  •  4h trend AGAINST trade; session=ny_mid  •  ONLY when RSI 30-40 weak

### L16.  `T1=T1c AND T4=T4c AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=62  W=20/L=42  WR=32.3%
- Sharpen: sharpest is RSI=RSI2 (38/42 of losers there)
- **Sharp: n=48  W=10/L=38  WR=20.8%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_mid  •  ONLY when RSI 30-40 weak

### L17.  `H60=H60c AND T1=T1c AND RSI=RSI2`
- Raw: n=60  W=22/L=38  WR=36.7%
- Sharpen: sharpest is session_bucket=off_hours (15/38 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: ?**  •  HTF60 neutral; 1h trend AGAINST trade; RSI 30-40 weak  •  ONLY when session=off_hours

### L18.  `H60=H60c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=60  W=22/L=38  WR=36.7%
- Sharpen: sharpest is session_bucket=off_hours (15/38 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: LONG**  •  HTF60 neutral; RSI 30-40 weak  •  ONLY when session=off_hours

### L19.  `H60=H60c AND T1=T1c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=60  W=22/L=38  WR=36.7%
- Sharpen: sharpest is session_bucket=off_hours (15/38 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: LONG**  •  HTF60 neutral; 1h trend AGAINST trade; RSI 30-40 weak  •  ONLY when session=off_hours

### L20.  `H20=H20e AND T1=T1c AND T4=T4c AND BBP=BBP2`
- Raw: n=59  W=23/L=36  WR=39.0%
- Sharpen: sharpest is H60=H60b (17/36 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; lower third  •  ONLY when HTF60 slightly aligned

### L21.  `T4=T4c AND RSI=RSI2 AND session_bucket=ny_mid`
- Raw: n=56  W=18/L=38  WR=32.1%
- Sharpen: sharpest is T1=T1c (38/38 of losers there)
- **Sharp: n=48  W=10/L=38  WR=20.8%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 30-40 weak; session=ny_mid  •  ONLY when 1h trend AGAINST trade

### L22.  `H20=H20e AND H60=H60c AND T1=T1c AND T4=T4c`
- Raw: n=56  W=21/L=35  WR=37.5%
- Sharpen: sharpest is RSI=RSI2 (24/35 of losers there)
- **Sharp: n=28  W=4/L=24  WR=14.3%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 neutral; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when RSI 30-40 weak

### L23.  `H60=H60e AND T1=T1c AND BBP=BBP2 AND RSI=RSI2`
- Raw: n=56  W=21/L=35  WR=37.5%
- Sharpen: sharpest is H20=H20d (9/35 of losers there)
- **Sharp: n=11  W=2/L=9  WR=18.2%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; lower third; RSI 30-40 weak  •  ONLY when HTF20 mildly against

### L24.  `H60=H60e AND BBP=BBP2 AND RSI=RSI2 AND direction_exec=long`
- Raw: n=56  W=21/L=35  WR=37.5%
- Sharpen: sharpest is H20=H20d (9/35 of losers there)
- **Sharp: n=11  W=2/L=9  WR=18.2%**
- **Dir: LONG**  •  HTF60 strongly against; lower third; RSI 30-40 weak  •  ONLY when HTF20 mildly against

### L25.  `H20=H20e AND T1=T1c AND BBP=BBP2 AND RSI=RSI2`
- Raw: n=56  W=22/L=34  WR=39.3%
- Sharpen: sharpest is H60=H60b (13/34 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; lower third; RSI 30-40 weak  •  ONLY when HTF60 slightly aligned

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | H60a(40/21), H60d(19/8) | H60e(19/37), H60b(8/16) |
| T1 | T1a(58/43) | T1c(42/57) |
| T4 | T4a(55/45) | T4c(45/55) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(56/45) | long(44/55) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
