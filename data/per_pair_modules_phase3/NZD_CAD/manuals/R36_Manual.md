# NZD_CAD — R36 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_0**  (5m ATR <33% stop)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR3**  (60-90%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **1,162**  (W=747 / L=415)  -  WR: **64.3%**

## Session distribution

- asia: n=502  W=326/L=176  WR=64.9%
- ny_close: n=282  W=183/L=99  WR=64.9%
- london_open: n=89  W=59/L=30  WR=66.3%
- london: n=82  W=46/L=36  WR=56.1%
- off_hours: n=81  W=52/L=29  WR=64.2%
- ny_open: n=70  W=47/L=23  WR=67.1%
- asia_late: n=56  W=34/L=22  WR=60.7%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND RSI=RSI4 AND direction_exec=long`
- Raw: n=227  W=204/L=23  WR=89.9%
- Refine: exclude H60=H60e drops 19/23 losers (83%)
- **Final: n=128  W=124/L=4  WR=96.9%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 50-60 upper neutral  •  AVOID when HTF60 strongly against

### W02.  `H20=H20a AND direction_exec=long AND session_bucket=asia`
- Raw: n=182  W=169/L=13  WR=92.9%
- Refine: exclude RSI=RSI5 drops 7/13 losers (54%)
- **Final: n=154  W=148/L=6  WR=96.1%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; session=asia  •  AVOID when RSI 60-70 strong

### W03.  `H20=H20a AND T4=T4a AND direction_exec=long`
- Raw: n=177  W=158/L=19  WR=89.3%
- Refine: exclude RSI=RSI5 drops 7/19 losers (37%)
- **Final: n=159  W=147/L=12  WR=92.5%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend WITH trade  •  AVOID when RSI 60-70 strong

### W04.  `H20=H20a AND BBP=BBP4 AND direction_exec=long`
- Raw: n=155  W=136/L=19  WR=87.7%
- Refine: exclude RSI=RSI5 drops 11/19 losers (58%)
- **Final: n=132  W=124/L=8  WR=93.9%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; upper third  •  AVOID when RSI 60-70 strong

### W05.  `RSI=RSI4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=155  W=134/L=21  WR=86.5%
- Refine: exclude H60=H60e drops 15/21 losers (71%)
- **Final: n=104  W=98/L=6  WR=94.2%**
- **Dir: LONG**  •  RSI 50-60 upper neutral; session=asia  •  AVOID when HTF60 strongly against

### W06.  `H20=H20a AND ZS=ZS4 AND direction_exec=long`
- Raw: n=147  W=130/L=17  WR=88.4%
- Refine: exclude RSI=RSI5 drops 11/17 losers (65%)
- **Final: n=124  W=118/L=6  WR=95.2%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; zscore +1 to +2 overbought  •  AVOID when RSI 60-70 strong

### W07.  `H20=H20a AND BBP=BBP4 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=147  W=130/L=17  WR=88.4%
- Refine: exclude RSI=RSI5 drops 11/17 losers (65%)
- **Final: n=124  W=118/L=6  WR=95.2%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; upper third; zscore +1 to +2 overbought  •  AVOID when RSI 60-70 strong

### W08.  `H60=H60a AND T4=T4a AND session_bucket=asia`
- Raw: n=140  W=119/L=21  WR=85.0%
- Refine: exclude BBP=BBP4 drops 16/21 losers (76%)
- **Final: n=91  W=86/L=5  WR=94.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; session=asia  •  AVOID when upper third

### W09.  `H20=H20a AND T4=T4a AND session_bucket=asia`
- Raw: n=136  W=126/L=10  WR=92.6%
- Refine: exclude RSI=RSI5 drops 7/10 losers (70%)
- **Final: n=118  W=115/L=3  WR=97.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=asia  •  AVOID when RSI 60-70 strong

### W10.  `H20=H20a AND T1=T1a AND session_bucket=asia`
- Raw: n=134  W=124/L=10  WR=92.5%
- Refine: exclude RSI=RSI5 drops 7/10 losers (70%)
- **Final: n=106  W=103/L=3  WR=97.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=asia  •  AVOID when RSI 60-70 strong

### W11.  `H20=H20a AND T1=T1c AND direction_exec=long`
- Raw: n=134  W=116/L=18  WR=86.6%
- Refine: exclude session_bucket=london_open drops 9/18 losers (50%)
- **Final: n=116  W=107/L=9  WR=92.2%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade  •  AVOID when session=london_open

### W12.  `H20=H20a AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=132  W=119/L=13  WR=90.2%
- Refine: exclude direction_exec=short drops 7/13 losers (54%)
- **Final: n=125  W=119/L=6  WR=95.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; upper third; RSI 50-60 upper neutral  •  AVOID when short

### W13.  `H60=H60a AND T4=T4a AND direction_exec=long`
- Raw: n=130  W=115/L=15  WR=88.5%
- Refine: exclude RSI=RSI5 drops 12/15 losers (80%)
- **Final: n=109  W=106/L=3  WR=97.2%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend WITH trade  •  AVOID when RSI 60-70 strong

### W14.  `H20=H20a AND T1=T1a AND RSI=RSI4 AND direction_exec=long`
- Raw: n=127  W=115/L=12  WR=90.6%
- Refine: exclude H60=H60e drops 10/12 losers (83%)
- **Final: n=87  W=85/L=2  WR=97.7%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when HTF60 strongly against

### W15.  `BBP=BBP4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=127  W=109/L=18  WR=85.8%
- Refine: exclude T4=T4a drops 13/18 losers (72%)
- **Final: n=63  W=58/L=5  WR=92.1%**
- **Dir: LONG**  •  upper third; session=asia  •  AVOID when 4h trend WITH trade

### W16.  `H20=H20a AND T4=T4a AND RSI=RSI4 AND direction_exec=long`
- Raw: n=126  W=114/L=12  WR=90.5%
- Refine: exclude H60=H60e drops 8/12 losers (67%)
- **Final: n=92  W=88/L=4  WR=95.7%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when HTF60 strongly against

### W17.  `H20=H20a AND BBP=BBP4 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=125  W=119/L=6  WR=95.2%
- Refine: exclude session_bucket=london_open drops 3/6 losers (50%)
- **Final: n=115  W=112/L=3  WR=97.4%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; upper third; RSI 50-60 upper neutral  •  AVOID when session=london_open

### W18.  `ZS=ZS4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=122  W=105/L=17  WR=86.1%
- Refine: exclude T1=T1a drops 15/17 losers (88%)
- **Final: n=46  W=44/L=2  WR=95.7%**
- **Dir: LONG**  •  zscore +1 to +2 overbought; session=asia  •  AVOID when 1h trend WITH trade

### W19.  `BBP=BBP4 AND ZS=ZS4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=122  W=105/L=17  WR=86.1%
- Refine: exclude T1=T1a drops 15/17 losers (88%)
- **Final: n=46  W=44/L=2  WR=95.7%**
- **Dir: LONG**  •  upper third; zscore +1 to +2 overbought; session=asia  •  AVOID when 1h trend WITH trade

### W20.  `H20=H20a AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=121  W=113/L=8  WR=93.4%
- Refine: exclude direction_exec=short drops 3/8 losers (38%)
- **Final: n=118  W=113/L=5  WR=95.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when short

### W21.  `H20=H20a AND BBP=BBP4 AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=121  W=113/L=8  WR=93.4%
- Refine: exclude direction_exec=short drops 3/8 losers (38%)
- **Final: n=118  W=113/L=5  WR=95.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; upper third; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when short

### W22.  `H20=H20a AND RSI=RSI4 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=118  W=113/L=5  WR=95.8%
- Refine: exclude session_bucket=off_hours drops 2/5 losers (40%)
- **Final: n=114  W=111/L=3  WR=97.4%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when session=off_hours

### W23.  `H20=H20a AND T1=T1a AND T4=T4a AND direction_exec=long`
- Raw: n=118  W=106/L=12  WR=89.8%
- Refine: exclude RSI=RSI5 drops 7/12 losers (58%)
- **Final: n=100  W=95/L=5  WR=95.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when RSI 60-70 strong

### W24.  `H20=H20a AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=115  W=114/L=1  WR=99.1%
- Refine: no further refinement
- **Final: n=115  W=114/L=1  WR=99.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 50-60 upper neutral; session=asia

### W25.  `H20=H20a AND RSI=RSI4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=115  W=114/L=1  WR=99.1%
- Refine: no further refinement
- **Final: n=115  W=114/L=1  WR=99.1%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 50-60 upper neutral; session=asia

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND RSI=RSI4 AND direction_exec=short`
- Raw: n=162  W=57/L=105  WR=35.2%
- Sharpen: sharpest is session_bucket=asia (64/105 of losers there)
- **Sharp: n=75  W=11/L=64  WR=14.7%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 50-60 upper neutral  •  ONLY when session=asia

### L02.  `H20=H20e AND T4=T4c AND direction_exec=short`
- Raw: n=135  W=45/L=90  WR=33.3%
- Sharpen: sharpest is RSI=RSI3 (23/90 of losers there)
- **Sharp: n=26  W=3/L=23  WR=11.5%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade  •  ONLY when RSI 40-50 lower neutral

### L03.  `H20=H20e AND T1=T1c AND direction_exec=short`
- Raw: n=130  W=48/L=82  WR=36.9%
- Sharpen: sharpest is session_bucket=asia (56/82 of losers there)
- **Sharp: n=77  W=21/L=56  WR=27.3%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade  •  ONLY when session=asia

### L04.  `H20=H20e AND direction_exec=short AND session_bucket=asia`
- Raw: n=129  W=35/L=94  WR=27.1%
- Sharpen: sharpest is RSI=RSI4 (64/94 of losers there)
- **Sharp: n=75  W=11/L=64  WR=14.7%**
- **Dir: SHORT**  •  HTF20 strongly against; session=asia  •  ONLY when RSI 50-60 upper neutral

### L05.  `T1=T1c AND T4=T4c AND direction_exec=short`
- Raw: n=123  W=46/L=77  WR=37.4%
- Sharpen: sharpest is H20=H20e (53/77 of losers there)
- **Sharp: n=74  W=21/L=53  WR=28.4%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when HTF20 strongly against

### L06.  `RSI=RSI4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=117  W=42/L=75  WR=35.9%
- Sharpen: sharpest is H20=H20e (64/75 of losers there)
- **Sharp: n=75  W=11/L=64  WR=14.7%**
- **Dir: SHORT**  •  RSI 50-60 upper neutral; session=asia  •  ONLY when HTF20 strongly against

### L07.  `H20=H20e AND BBP=BBP4 AND direction_exec=short`
- Raw: n=105  W=37/L=68  WR=35.2%
- Sharpen: sharpest is RSI=RSI4 (55/68 of losers there)
- **Sharp: n=70  W=15/L=55  WR=21.4%**
- **Dir: SHORT**  •  HTF20 strongly against; upper third  •  ONLY when RSI 50-60 upper neutral

### L08.  `H20=H20e AND ZS=ZS4 AND direction_exec=short`
- Raw: n=98  W=33/L=65  WR=33.7%
- Sharpen: sharpest is RSI=RSI4 (53/65 of losers there)
- **Sharp: n=65  W=12/L=53  WR=18.5%**
- **Dir: SHORT**  •  HTF20 strongly against; zscore +1 to +2 overbought  •  ONLY when RSI 50-60 upper neutral

### L09.  `H20=H20e AND BBP=BBP4 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=98  W=33/L=65  WR=33.7%
- Sharpen: sharpest is RSI=RSI4 (53/65 of losers there)
- **Sharp: n=65  W=12/L=53  WR=18.5%**
- **Dir: SHORT**  •  HTF20 strongly against; upper third; zscore +1 to +2 overbought  •  ONLY when RSI 50-60 upper neutral

### L10.  `H20=H20e AND T4=T4c AND session_bucket=asia`
- Raw: n=96  W=26/L=70  WR=27.1%
- Sharpen: sharpest is H60=H60a (25/70 of losers there)
- **Sharp: n=27  W=2/L=25  WR=7.4%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; session=asia  •  ONLY when HTF60 aligned WITH trade

### L11.  `H20=H20e AND T1=T1c AND session_bucket=asia`
- Raw: n=94  W=25/L=69  WR=26.6%
- Sharpen: sharpest is H60=H60b (18/69 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; session=asia  •  ONLY when HTF60 slightly aligned

### L12.  `H60=H60e AND T4=T4c AND direction_exec=short`
- Raw: n=94  W=35/L=59  WR=37.2%
- Sharpen: sharpest is RSI=RSI4 (45/59 of losers there)
- **Sharp: n=57  W=12/L=45  WR=21.1%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend AGAINST trade  •  ONLY when RSI 50-60 upper neutral

### L13.  `H20=H20e AND T4=T4c AND RSI=RSI4 AND direction_exec=short`
- Raw: n=91  W=29/L=62  WR=31.9%
- Sharpen: sharpest is T1=T1c (37/62 of losers there)
- **Sharp: n=44  W=7/L=37  WR=15.9%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when 1h trend AGAINST trade

### L14.  `H20=H20e AND T1=T1a AND RSI=RSI4`
- Raw: n=89  W=34/L=55  WR=38.2%
- Sharpen: sharpest is session_bucket=asia (30/55 of losers there)
- **Sharp: n=34  W=4/L=30  WR=11.8%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when session=asia

### L15.  `H20=H20e AND T4=T4c AND direction_exec=short AND session_bucket=asia`
- Raw: n=85  W=24/L=61  WR=28.2%
- Sharpen: sharpest is RSI=RSI4 (37/61 of losers there)
- **Sharp: n=45  W=8/L=37  WR=17.8%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade; session=asia  •  ONLY when RSI 50-60 upper neutral

### L16.  `H20=H20e AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=85  W=29/L=56  WR=34.1%
- Sharpen: sharpest is session_bucket=asia (35/56 of losers there)
- **Sharp: n=39  W=4/L=35  WR=10.3%**
- **Dir: ?**  •  HTF20 strongly against; upper third; RSI 50-60 upper neutral  •  ONLY when session=asia

### L17.  `H20=H20e AND T1=T1c AND RSI=RSI4 AND direction_exec=short`
- Raw: n=82  W=25/L=57  WR=30.5%
- Sharpen: sharpest is T4=T4c (37/57 of losers there)
- **Sharp: n=44  W=7/L=37  WR=15.9%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when 4h trend AGAINST trade

### L18.  `H20=H20e AND T1=T1a AND RSI=RSI4 AND direction_exec=short`
- Raw: n=80  W=32/L=48  WR=40.0%
- Sharpen: sharpest is session_bucket=asia (30/48 of losers there)
- **Sharp: n=34  W=4/L=30  WR=11.8%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when session=asia

### L19.  `T1=T1c AND T4=T4c AND direction_exec=short AND session_bucket=asia`
- Raw: n=78  W=31/L=47  WR=39.7%
- Sharpen: sharpest is RSI=RSI3 (11/47 of losers there)
- **Sharp: n=12  W=1/L=11  WR=8.3%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=asia  •  ONLY when RSI 40-50 lower neutral

### L20.  `H20=H20e AND T1=T1c AND direction_exec=short AND session_bucket=asia`
- Raw: n=77  W=21/L=56  WR=27.3%
- Sharpen: sharpest is H60=H60b (18/56 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; session=asia  •  ONLY when HTF60 slightly aligned

### L21.  `H20=H20e AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=75  W=11/L=64  WR=14.7%
- Sharpen: sharpest is H60=H60b (12/64 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; RSI 50-60 upper neutral; session=asia  •  ONLY when HTF60 slightly aligned

### L22.  `H20=H20e AND RSI=RSI4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=75  W=11/L=64  WR=14.7%
- Sharpen: sharpest is H60=H60b (12/64 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 50-60 upper neutral; session=asia  •  ONLY when HTF60 slightly aligned

### L23.  `H20=H20e AND T1=T1c AND T4=T4c AND direction_exec=short`
- Raw: n=74  W=21/L=53  WR=28.4%
- Sharpen: sharpest is RSI=RSI4 (37/53 of losers there)
- **Sharp: n=44  W=7/L=37  WR=15.9%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when RSI 50-60 upper neutral

### L24.  `H20=H20e AND H60=H60e AND session_bucket=asia`
- Raw: n=73  W=24/L=49  WR=32.9%
- Sharpen: sharpest is RSI=RSI3 (17/49 of losers there)
- **Sharp: n=19  W=2/L=17  WR=10.5%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; session=asia  •  ONLY when RSI 40-50 lower neutral

### L25.  `BBP=BBP4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=73  W=24/L=49  WR=32.9%
- Sharpen: sharpest is RSI=RSI4 (38/49 of losers there)
- **Sharp: n=47  W=9/L=38  WR=19.1%**
- **Dir: SHORT**  •  upper third; session=asia  •  ONLY when RSI 50-60 upper neutral

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(44/22) | H20e(24/46) |
| H60 | H60a(44/38) | — |
| T1 | T1a(56/47) | T1c(44/53) |
| T4 | T4a(54/43) | T4c(46/57) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(60/41) | short(40/59) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
