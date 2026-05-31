# EUR_NZD — R30 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_3**  (5m ATR >120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **5,513**  (W=3,186 / L=2,327)  -  WR: **57.8%**

## Session distribution

- ny_mid: n=2203  W=1271/L=932  WR=57.7%
- asia: n=1278  W=749/L=529  WR=58.6%
- london_open: n=880  W=523/L=357  WR=59.4%
- ny_open: n=380  W=216/L=164  WR=56.8%
- off_hours: n=292  W=156/L=136  WR=53.4%
- asia_late: n=175  W=102/L=73  WR=58.3%
- london: n=160  W=101/L=59  WR=63.1%
- ny_close: n=145  W=68/L=77  WR=46.9%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60e AND BBP=BBP3 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=115  W=102/L=13  WR=88.7%
- Refine: exclude H20=H20a drops 7/13 losers (54%)
- **Final: n=78  W=72/L=6  WR=92.3%**
- **Dir: LONG**  •  HTF60 strongly against; middle of band; RSI 50-60 upper neutral  •  AVOID when HTF20 aligned WITH trade

### W02.  `H20=H20e AND BBP=BBP3 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=111  W=96/L=15  WR=86.5%
- Refine: exclude H60=H60a drops 10/15 losers (67%)
- **Final: n=73  W=68/L=5  WR=93.2%**
- **Dir: LONG**  •  HTF20 strongly against; middle of band; RSI 50-60 upper neutral  •  AVOID when HTF60 aligned WITH trade

### W03.  `H20=H20e AND H60=H60e AND RSI=RSI4 AND ZS=ZS3`
- Raw: n=101  W=89/L=12  WR=88.1%
- Refine: exclude BBP=BBP2 drops 5/12 losers (42%)
- **Final: n=96  W=89/L=7  WR=92.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  AVOID when lower third

### W04.  `H60=H60e AND T1=T1a AND BBP=BBP3 AND RSI=RSI4`
- Raw: n=100  W=85/L=15  WR=85.0%
- Refine: exclude H20=H20a drops 9/15 losers (60%)
- **Final: n=69  W=63/L=6  WR=91.3%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; middle of band; RSI 50-60 upper neutral  •  AVOID when HTF20 aligned WITH trade

### W05.  `H20=H20e AND T4=T4a AND RSI=RSI4 AND ZS=ZS3`
- Raw: n=97  W=83/L=14  WR=85.6%
- Refine: exclude H60=H60a drops 10/14 losers (71%)
- **Final: n=65  W=61/L=4  WR=93.8%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  AVOID when HTF60 aligned WITH trade

### W06.  `H20=H20e AND BBP=BBP3 AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=96  W=84/L=12  WR=87.5%
- Refine: exclude H60=H60a drops 7/12 losers (58%)
- **Final: n=67  W=62/L=5  WR=92.5%**
- **Dir: ?**  •  HTF20 strongly against; middle of band; RSI 50-60 upper neutral; session=ny_mid  •  AVOID when HTF60 aligned WITH trade

### W07.  `T4=T4c AND RSI=RSI3 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=94  W=80/L=14  WR=85.1%
- Refine: exclude H20=H20e drops 13/14 losers (93%)
- **Final: n=39  W=38/L=1  WR=97.4%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when HTF20 strongly against

### W08.  `RSI=RSI3 AND strategy_id=TF2_pullback_EMA20_long AND direction_exec=short`
- Raw: n=92  W=85/L=7  WR=92.4%
- Refine: exclude BBP=BBP2 drops 3/7 losers (43%)
- **Final: n=85  W=81/L=4  WR=95.3%**
- **Dir: SHORT**  •  RSI 40-50 lower neutral; strategy=TF2_pullback_EMA20_long  •  AVOID when lower third

### W09.  `T1=T1a AND ZS=ZS3 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=89  W=76/L=13  WR=85.4%
- Refine: exclude RSI=RSI4 drops 9/13 losers (69%)
- **Final: n=65  W=61/L=4  WR=93.8%**
- **Dir: SHORT**  •  1h trend WITH trade; zscore -1 to +1 neutral; session=london_open  •  AVOID when RSI 50-60 upper neutral

### W10.  `H60=H60a AND RSI=RSI4 AND session_bucket=ny_open`
- Raw: n=88  W=79/L=9  WR=89.8%
- Refine: exclude H20=H20a drops 9/9 losers (100%)
- **Final: n=51  W=51/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; session=ny_open  •  AVOID when HTF20 aligned WITH trade

### W11.  `H20=H20b AND H60=H60a AND direction_exec=short`
- Raw: n=82  W=72/L=10  WR=87.8%
- Refine: exclude RSI=RSI4 drops 4/10 losers (40%)
- **Final: n=75  W=69/L=6  WR=92.0%**
- **Dir: SHORT**  •  HTF20 slightly aligned; HTF60 aligned WITH trade  •  AVOID when RSI 50-60 upper neutral

### W12.  `H20=H20b AND H60=H60a AND T4=T4a AND direction_exec=short`
- Raw: n=80  W=70/L=10  WR=87.5%
- Refine: exclude RSI=RSI4 drops 4/10 losers (40%)
- **Final: n=73  W=67/L=6  WR=91.8%**
- **Dir: SHORT**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 4h trend WITH trade  •  AVOID when RSI 50-60 upper neutral

### W13.  `T1=T1a AND ZS=ZS4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=80  W=69/L=11  WR=86.2%
- Refine: exclude H60=H60d drops 6/11 losers (55%)
- **Final: n=68  W=63/L=5  WR=92.6%**
- **Dir: SHORT**  •  1h trend WITH trade; zscore +1 to +2 overbought; session=asia  •  AVOID when HTF60 mildly against

### W14.  `H60=H60a AND T1=T1a AND RSI=RSI3 AND session_bucket=london_open`
- Raw: n=80  W=68/L=12  WR=85.0%
- Refine: exclude BBP=BBP6 drops 5/12 losers (42%)
- **Final: n=74  W=67/L=7  WR=90.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 40-50 lower neutral; session=london_open  •  AVOID when deep above upper band

### W15.  `T1=T1a AND T4=T4a AND BBP=BBP3 AND session_bucket=london_open`
- Raw: n=77  W=66/L=11  WR=85.7%
- Refine: exclude RSI=RSI4 drops 9/11 losers (82%)
- **Final: n=39  W=37/L=2  WR=94.9%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; middle of band; session=london_open  •  AVOID when RSI 50-60 upper neutral

### W16.  `RSI=RSI3 AND ZS=ZS3 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=75  W=70/L=5  WR=93.3%
- Refine: exclude strategy_id=charlie_pullback_continuation_v2 drops 3/5 losers (60%)
- **Final: n=64  W=62/L=2  WR=96.9%**
- **Dir: SHORT**  •  RSI 40-50 lower neutral; zscore -1 to +1 neutral; session=london_open  •  AVOID when strategy=charlie_pullback_continuation_v2

### W17.  `H20=H20b AND H60=H60a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=75  W=69/L=6  WR=92.0%
- Refine: exclude BBP=BBP4 drops 4/6 losers (67%)
- **Final: n=61  W=59/L=2  WR=96.7%**
- **Dir: SHORT**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; RSI 40-50 lower neutral  •  AVOID when upper third

### W18.  `H20=H20e AND H60=H60e AND BBP=BBP3 AND RSI=RSI4`
- Raw: n=73  W=68/L=5  WR=93.2%
- Refine: exclude session_bucket=london drops 3/5 losers (60%)
- **Final: n=70  W=68/L=2  WR=97.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; middle of band; RSI 50-60 upper neutral  •  AVOID when session=london

### W19.  `T1=T1a AND RSI=RSI3 AND ZS=ZS3 AND session_bucket=london_open`
- Raw: n=73  W=63/L=10  WR=86.3%
- Refine: exclude H20=H20e drops 6/10 losers (60%)
- **Final: n=65  W=61/L=4  WR=93.8%**
- **Dir: ?**  •  1h trend WITH trade; RSI 40-50 lower neutral; zscore -1 to +1 neutral; session=london_open  •  AVOID when HTF20 strongly against

### W20.  `H60=H60a AND T1=T1a AND session_bucket=ny_open`
- Raw: n=72  W=68/L=4  WR=94.4%
- Refine: exclude H20=H20a drops 4/4 losers (100%)
- **Final: n=64  W=64/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=ny_open  •  AVOID when HTF20 aligned WITH trade

### W21.  `T1=T1a AND RSI=RSI3 AND strategy_id=TF2_pullback_EMA20_long AND direction_exec=short`
- Raw: n=69  W=63/L=6  WR=91.3%
- Refine: exclude BBP=BBP6 drops 2/6 losers (33%)
- **Final: n=65  W=61/L=4  WR=93.8%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 40-50 lower neutral; strategy=TF2_pullback_EMA20_long  •  AVOID when deep above upper band

### W22.  `T4=T4c AND BBP=BBP0 AND direction_exec=long`
- Raw: n=69  W=59/L=10  WR=85.5%
- Refine: exclude H60=H60c drops 6/10 losers (60%)
- **Final: n=61  W=57/L=4  WR=93.4%**
- **Dir: LONG**  •  4h trend AGAINST trade; deep below lower band  •  AVOID when HTF60 neutral

### W23.  `T4=T4a AND RSI=RSI3 AND strategy_id=TF2_pullback_EMA20_long AND direction_exec=short`
- Raw: n=68  W=62/L=6  WR=91.2%
- Refine: exclude BBP=BBP6 drops 2/6 losers (33%)
- **Final: n=64  W=60/L=4  WR=93.8%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 40-50 lower neutral; strategy=TF2_pullback_EMA20_long  •  AVOID when deep above upper band

### W24.  `H20=H20b AND H60=H60e AND BBP=BBP2`
- Raw: n=66  W=59/L=7  WR=89.4%
- Refine: exclude strategy_id=bravo_failed_momentum drops 2/7 losers (29%)
- **Final: n=64  W=59/L=5  WR=92.2%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 strongly against; lower third  •  AVOID when strategy=bravo_failed_momentum

### W25.  `H20=H20e AND T4=T4a AND BBP=BBP3 AND RSI=RSI4`
- Raw: n=66  W=59/L=7  WR=89.4%
- Refine: exclude H60=H60a drops 7/7 losers (100%)
- **Final: n=39  W=39/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; middle of band; RSI 50-60 upper neutral  •  AVOID when HTF60 aligned WITH trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60a AND T1=T1c AND session_bucket=ny_mid`
- Raw: n=294  W=111/L=183  WR=37.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=294  W=111/L=183  WR=37.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=ny_mid

### L02.  `T1=T1c AND BBP=BBP4 AND direction_exec=long`
- Raw: n=256  W=102/L=154  WR=39.8%
- Sharpen: sharpest is ZS=ZS4 (121/154 of losers there)
- **Sharp: n=184  W=63/L=121  WR=34.2%**
- **Dir: LONG**  •  1h trend AGAINST trade; upper third  •  ONLY when zscore +1 to +2 overbought

### L03.  `H60=H60a AND T1=T1c AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=206  W=75/L=131  WR=36.4%
- Sharpen: sharpest is T4=T4a (59/131 of losers there)
- **Sharp: n=80  W=21/L=59  WR=26.2%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=ny_mid  •  ONLY when 4h trend WITH trade

### L04.  `H20=H20e AND T1=T1c AND BBP=BBP4`
- Raw: n=198  W=78/L=120  WR=39.4%
- Sharpen: sharpest is ZS=ZS4 (92/120 of losers there)
- **Sharp: n=137  W=45/L=92  WR=32.8%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; upper third  •  ONLY when zscore +1 to +2 overbought

### L05.  `BBP=BBP4 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=198  W=79/L=119  WR=39.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=198  W=79/L=119  WR=39.9%**
- **Dir: LONG**  •  upper third; RSI 40-50 lower neutral

### L06.  `H60=H60e AND T1=T1a AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=195  W=74/L=121  WR=37.9%
- Sharpen: sharpest is ZS=ZS2 (102/121 of losers there)
- **Sharp: n=141  W=39/L=102  WR=27.7%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; lower third; RSI 40-50 lower neutral  •  ONLY when zscore -2 to -1 oversold

### L07.  `H60=H60a AND RSI=RSI4 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=195  W=75/L=120  WR=38.5%
- Sharpen: sharpest is T4=T4a (51/120 of losers there)
- **Sharp: n=63  W=12/L=51  WR=19.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; session=ny_mid  •  ONLY when 4h trend WITH trade

### L08.  `H60=H60a AND T1=T1c AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=192  W=66/L=126  WR=34.4%
- Sharpen: sharpest is T4=T4a (62/126 of losers there)
- **Sharp: n=76  W=14/L=62  WR=18.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 50-60 upper neutral; session=ny_mid  •  ONLY when 4h trend WITH trade

### L09.  `H60=H60a AND T4=T4a AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=189  W=75/L=114  WR=39.7%
- Sharpen: sharpest is T1=T1c (62/114 of losers there)
- **Sharp: n=76  W=14/L=62  WR=18.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral; session=ny_mid  •  ONLY when 1h trend AGAINST trade

### L10.  `T1=T1c AND ZS=ZS4 AND direction_exec=long`
- Raw: n=184  W=63/L=121  WR=34.2%
- Sharpen: sharpest is T4=T4c (86/121 of losers there)
- **Sharp: n=117  W=31/L=86  WR=26.5%**
- **Dir: LONG**  •  1h trend AGAINST trade; zscore +1 to +2 overbought  •  ONLY when 4h trend AGAINST trade

### L11.  `T1=T1c AND BBP=BBP4 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=184  W=63/L=121  WR=34.2%
- Sharpen: sharpest is T4=T4c (86/121 of losers there)
- **Sharp: n=117  W=31/L=86  WR=26.5%**
- **Dir: LONG**  •  1h trend AGAINST trade; upper third; zscore +1 to +2 overbought  •  ONLY when 4h trend AGAINST trade

### L12.  `H20=H20e AND H60=H60a AND ZS=ZS4`
- Raw: n=175  W=64/L=111  WR=36.6%
- Sharpen: sharpest is T1=T1c (40/111 of losers there)
- **Sharp: n=49  W=9/L=40  WR=18.4%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; zscore +1 to +2 overbought  •  ONLY when 1h trend AGAINST trade

### L13.  `H20=H20e AND H60=H60a AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=175  W=64/L=111  WR=36.6%
- Sharpen: sharpest is T1=T1c (40/111 of losers there)
- **Sharp: n=49  W=9/L=40  WR=18.4%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; upper third; zscore +1 to +2 overbought  •  ONLY when 1h trend AGAINST trade

### L14.  `T1=T1c AND BBP=BBP4 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=173  W=69/L=104  WR=39.9%
- Sharpen: sharpest is session_bucket=london_open (19/104 of losers there)
- **Sharp: n=20  W=1/L=19  WR=5.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; upper third; RSI 40-50 lower neutral  •  ONLY when session=london_open

### L15.  `T4=T4a AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=172  W=63/L=109  WR=36.6%
- Sharpen: sharpest is direction_exec=long (56/109 of losers there)
- **Sharp: n=73  W=17/L=56  WR=23.3%**
- **Dir: ?**  •  4h trend WITH trade; deep above upper band; zscore +2 to +3 deep overbought  •  ONLY when long

### L16.  `H20=H20e AND H60=H60a AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=170  W=67/L=103  WR=39.4%
- Sharpen: sharpest is T1=T1c (30/103 of losers there)
- **Sharp: n=38  W=8/L=30  WR=21.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; upper third; RSI 50-60 upper neutral  •  ONLY when 1h trend AGAINST trade

### L17.  `RSI=RSI3 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=170  W=68/L=102  WR=40.0%
- Sharpen: sharpest is T4=T4a (65/102 of losers there)
- **Sharp: n=86  W=21/L=65  WR=24.4%**
- **Dir: SHORT**  •  RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when 4h trend WITH trade

### L18.  `H20=H20a AND H60=H60a AND T1=T1c AND session_bucket=ny_mid`
- Raw: n=160  W=54/L=106  WR=33.8%
- Sharpen: sharpest is ZS=ZS3 (32/106 of losers there)
- **Sharp: n=38  W=6/L=32  WR=15.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade; session=ny_mid  •  ONLY when zscore -1 to +1 neutral

### L19.  `T1=T1c AND T4=T4c AND BBP=BBP4 AND direction_exec=long`
- Raw: n=160  W=54/L=106  WR=33.8%
- Sharpen: sharpest is ZS=ZS4 (86/106 of losers there)
- **Sharp: n=117  W=31/L=86  WR=26.5%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; upper third  •  ONLY when zscore +1 to +2 overbought

### L20.  `H60=H60e AND RSI=RSI3 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=160  W=57/L=103  WR=35.6%
- Sharpen: sharpest is H20=H20e (19/103 of losers there)
- **Sharp: n=20  W=1/L=19  WR=5.0%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  ONLY when HTF20 strongly against

### L21.  `H20=H20e AND T4=T4a AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=159  W=56/L=103  WR=35.2%
- Sharpen: sharpest is T1=T1a (45/103 of losers there)
- **Sharp: n=55  W=10/L=45  WR=18.2%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; lower third; RSI 40-50 lower neutral  •  ONLY when 1h trend WITH trade

### L22.  `H60=H60e AND T1=T1c AND BBP=BBP4 AND direction_exec=long`
- Raw: n=158  W=63/L=95  WR=39.9%
- Sharpen: sharpest is H20=H20e (54/95 of losers there)
- **Sharp: n=79  W=25/L=54  WR=31.6%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend AGAINST trade; upper third  •  ONLY when HTF20 strongly against

### L23.  `H20=H20e AND T1=T1c AND T4=T4c AND BBP=BBP4`
- Raw: n=157  W=60/L=97  WR=38.2%
- Sharpen: sharpest is ZS=ZS4 (76/97 of losers there)
- **Sharp: n=105  W=29/L=76  WR=27.6%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; upper third  •  ONLY when zscore +1 to +2 overbought

### L24.  `H20=H20d AND H60=H60e AND RSI=RSI3`
- Raw: n=153  W=57/L=96  WR=37.3%
- Sharpen: sharpest is direction_exec=long (49/96 of losers there)
- **Sharp: n=56  W=7/L=49  WR=12.5%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 strongly against; RSI 40-50 lower neutral  •  ONLY when long

### L25.  `BBP=BBP6 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=149  W=48/L=101  WR=32.2%
- Sharpen: sharpest is H20=H20b (30/101 of losers there)
- **Sharp: n=33  W=3/L=30  WR=9.1%**
- **Dir: LONG**  •  deep above upper band; RSI 50-60 upper neutral  •  ONLY when HTF20 slightly aligned

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | — |
| T1 | T1a(53/46) | T1c(46/53) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
