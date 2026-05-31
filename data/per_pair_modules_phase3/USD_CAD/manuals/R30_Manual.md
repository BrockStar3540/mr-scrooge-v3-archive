# USD_CAD — R30 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **2,214**  (W=1,440 / L=774)  -  WR: **65.0%**

## Session distribution

- asia: n=893  W=589/L=304  WR=66.0%
- ny_close: n=635  W=403/L=232  WR=63.5%
- off_hours: n=259  W=168/L=91  WR=64.9%
- london_open: n=173  W=110/L=63  WR=63.6%
- ny_open: n=110  W=74/L=36  WR=67.3%
- asia_late: n=105  W=70/L=35  WR=66.7%
- london: n=31  W=22/L=9  WR=71.0%
- ny_mid: n=8  W=4/L=4  WR=50.0%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1a AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=198  W=172/L=26  WR=86.9%
- Refine: exclude BBP=BBP5 drops 10/26 losers (38%)
- **Final: n=183  W=167/L=16  WR=91.3%**
- **Dir: LONG**  •  1h trend WITH trade; session=ny_close  •  AVOID when just touched upper band

### W02.  `T1=T1c AND ZS=ZS5 AND direction_exec=short`
- Raw: n=179  W=155/L=24  WR=86.6%
- Refine: exclude session_bucket=asia drops 17/24 losers (71%)
- **Final: n=90  W=83/L=7  WR=92.2%**
- **Dir: SHORT**  •  1h trend AGAINST trade; zscore +2 to +3 deep overbought  •  AVOID when session=asia

### W03.  `H60=H60e AND T1=T1a AND session_bucket=ny_close`
- Raw: n=176  W=154/L=22  WR=87.5%
- Refine: exclude BBP=BBP5 drops 10/22 losers (45%)
- **Final: n=161  W=149/L=12  WR=92.5%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; session=ny_close  •  AVOID when just touched upper band

### W04.  `H60=H60e AND T1=T1a AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=176  W=154/L=22  WR=87.5%
- Refine: exclude BBP=BBP5 drops 10/22 losers (45%)
- **Final: n=161  W=149/L=12  WR=92.5%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend WITH trade; session=ny_close  •  AVOID when just touched upper band

### W05.  `H20=H20b AND RSI=RSI3 AND direction_exec=long`
- Raw: n=160  W=140/L=20  WR=87.5%
- Refine: exclude BBP=BBP4 drops 11/20 losers (55%)
- **Final: n=137  W=128/L=9  WR=93.4%**
- **Dir: LONG**  •  HTF20 slightly aligned; RSI 40-50 lower neutral  •  AVOID when upper third

### W06.  `H20=H20e AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=160  W=136/L=24  WR=85.0%
- Refine: exclude T4=T4c drops 22/24 losers (92%)
- **Final: n=42  W=40/L=2  WR=95.2%**
- **Dir: ?**  •  HTF20 strongly against; upper third; RSI 50-60 upper neutral  •  AVOID when 4h trend AGAINST trade

### W07.  `T1=T1a AND RSI=RSI4 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=159  W=136/L=23  WR=85.5%
- Refine: exclude BBP=BBP5 drops 10/23 losers (43%)
- **Final: n=144  W=131/L=13  WR=91.0%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 50-60 upper neutral; session=ny_close  •  AVOID when just touched upper band

### W08.  `H20=H20e AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=157  W=134/L=23  WR=85.4%
- Refine: exclude T4=T4c drops 21/23 losers (91%)
- **Final: n=42  W=40/L=2  WR=95.2%**
- **Dir: ?**  •  HTF20 strongly against; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when 4h trend AGAINST trade

### W09.  `H20=H20e AND BBP=BBP4 AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=157  W=134/L=23  WR=85.4%
- Refine: exclude T4=T4c drops 21/23 losers (91%)
- **Final: n=42  W=40/L=2  WR=95.2%**
- **Dir: ?**  •  HTF20 strongly against; upper third; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when 4h trend AGAINST trade

### W10.  `H60=H60a AND T1=T1c AND ZS=ZS5`
- Raw: n=155  W=135/L=20  WR=87.1%
- Refine: exclude H20=H20a drops 14/20 losers (70%)
- **Final: n=85  W=79/L=6  WR=92.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; zscore +2 to +3 deep overbought  •  AVOID when HTF20 aligned WITH trade

### W11.  `H60=H60a AND T1=T1c AND ZS=ZS5 AND direction_exec=short`
- Raw: n=155  W=135/L=20  WR=87.1%
- Refine: exclude H20=H20a drops 14/20 losers (70%)
- **Final: n=85  W=79/L=6  WR=92.9%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; zscore +2 to +3 deep overbought  •  AVOID when HTF20 aligned WITH trade

### W12.  `H60=H60e AND T1=T1a AND RSI=RSI4 AND session_bucket=ny_close`
- Raw: n=150  W=128/L=22  WR=85.3%
- Refine: exclude BBP=BBP5 drops 10/22 losers (45%)
- **Final: n=135  W=123/L=12  WR=91.1%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; RSI 50-60 upper neutral; session=ny_close  •  AVOID when just touched upper band

### W13.  `T1=T1c AND RSI=RSI4 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=136  W=117/L=19  WR=86.0%
- Refine: exclude session_bucket=asia drops 17/19 losers (89%)
- **Final: n=71  W=69/L=2  WR=97.2%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when session=asia

### W14.  `H20=H20c AND H60=H60a AND T1=T1a`
- Raw: n=134  W=114/L=20  WR=85.1%
- Refine: exclude BBP=BBP2 drops 14/20 losers (70%)
- **Final: n=82  W=76/L=6  WR=92.7%**
- **Dir: ?**  •  HTF20 neutral; HTF60 aligned WITH trade; 1h trend WITH trade  •  AVOID when lower third

### W15.  `H20=H20c AND T1=T1a AND direction_exec=short`
- Raw: n=134  W=114/L=20  WR=85.1%
- Refine: exclude BBP=BBP2 drops 14/20 losers (70%)
- **Final: n=82  W=76/L=6  WR=92.7%**
- **Dir: SHORT**  •  HTF20 neutral; 1h trend WITH trade  •  AVOID when lower third

### W16.  `H20=H20c AND H60=H60a AND T1=T1a AND direction_exec=short`
- Raw: n=134  W=114/L=20  WR=85.1%
- Refine: exclude BBP=BBP2 drops 14/20 losers (70%)
- **Final: n=82  W=76/L=6  WR=92.7%**
- **Dir: SHORT**  •  HTF20 neutral; HTF60 aligned WITH trade; 1h trend WITH trade  •  AVOID when lower third

### W17.  `H20=H20c AND T1=T1a AND RSI=RSI3`
- Raw: n=130  W=111/L=19  WR=85.4%
- Refine: exclude BBP=BBP2 drops 14/19 losers (74%)
- **Final: n=71  W=66/L=5  WR=93.0%**
- **Dir: ?**  •  HTF20 neutral; 1h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when lower third

### W18.  `T1=T1a AND BBP=BBP4 AND session_bucket=ny_close`
- Raw: n=129  W=117/L=12  WR=90.7%
- Refine: exclude H60=H60c drops 4/12 losers (33%)
- **Final: n=124  W=116/L=8  WR=93.5%**
- **Dir: ?**  •  1h trend WITH trade; upper third; session=ny_close  •  AVOID when HTF60 neutral

### W19.  `H60=H60a AND T1=T1c AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=126  W=111/L=15  WR=88.1%
- Refine: exclude session_bucket=asia drops 13/15 losers (87%)
- **Final: n=65  W=63/L=2  WR=96.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when session=asia

### W20.  `H20=H20b AND T4=T4a AND RSI=RSI3`
- Raw: n=125  W=113/L=12  WR=90.4%
- Refine: exclude BBP=BBP4 drops 7/12 losers (58%)
- **Final: n=108  W=103/L=5  WR=95.4%**
- **Dir: ?**  •  HTF20 slightly aligned; 4h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when upper third

### W21.  `H20=H20b AND T4=T4a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=125  W=113/L=12  WR=90.4%
- Refine: exclude BBP=BBP4 drops 7/12 losers (58%)
- **Final: n=108  W=103/L=5  WR=95.4%**
- **Dir: LONG**  •  HTF20 slightly aligned; 4h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when upper third

### W22.  `H60=H60a AND T1=T1a AND session_bucket=asia`
- Raw: n=122  W=110/L=12  WR=90.2%
- Refine: exclude T4=T4c drops 10/12 losers (83%)
- **Final: n=62  W=60/L=2  WR=96.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=asia  •  AVOID when 4h trend AGAINST trade

### W23.  `H60=H60a AND T1=T1a AND direction_exec=short AND session_bucket=asia`
- Raw: n=122  W=110/L=12  WR=90.2%
- Refine: exclude T4=T4c drops 10/12 losers (83%)
- **Final: n=62  W=60/L=2  WR=96.8%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=asia  •  AVOID when 4h trend AGAINST trade

### W24.  `T1=T1c AND BBP=BBP5 AND RSI=RSI4`
- Raw: n=121  W=104/L=17  WR=86.0%
- Refine: exclude H60=H60e drops 8/17 losers (47%)
- **Final: n=96  W=87/L=9  WR=90.6%**
- **Dir: ?**  •  1h trend AGAINST trade; just touched upper band; RSI 50-60 upper neutral  •  AVOID when HTF60 strongly against

### W25.  `T1=T1c AND BBP=BBP5 AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=121  W=104/L=17  WR=86.0%
- Refine: exclude H60=H60e drops 8/17 losers (47%)
- **Final: n=96  W=87/L=9  WR=90.6%**
- **Dir: ?**  •  1h trend AGAINST trade; just touched upper band; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when HTF60 strongly against

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60a AND T1=T1c AND ZS=ZS4`
- Raw: n=188  W=73/L=115  WR=38.8%
- Sharpen: sharpest is H20=H20a (79/115 of losers there)
- **Sharp: n=108  W=29/L=79  WR=26.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; zscore +1 to +2 overbought  •  ONLY when HTF20 aligned WITH trade

### L02.  `H60=H60a AND T1=T1c AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=188  W=73/L=115  WR=38.8%
- Sharpen: sharpest is H20=H20a (79/115 of losers there)
- **Sharp: n=108  W=29/L=79  WR=26.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; upper third; zscore +1 to +2 overbought  •  ONLY when HTF20 aligned WITH trade

### L03.  `H60=H60a AND T1=T1c AND ZS=ZS4 AND direction_exec=short`
- Raw: n=188  W=73/L=115  WR=38.8%
- Sharpen: sharpest is H20=H20a (79/115 of losers there)
- **Sharp: n=108  W=29/L=79  WR=26.9%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; zscore +1 to +2 overbought  •  ONLY when HTF20 aligned WITH trade

### L04.  `H60=H60a AND T1=T1c AND T4=T4a AND BBP=BBP4`
- Raw: n=173  W=69/L=104  WR=39.9%
- Sharpen: sharpest is H20=H20a (68/104 of losers there)
- **Sharp: n=85  W=17/L=68  WR=20.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; upper third  •  ONLY when HTF20 aligned WITH trade

### L05.  `T1=T1c AND T4=T4a AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=166  W=66/L=100  WR=39.8%
- Sharpen: sharpest is H20=H20a (59/100 of losers there)
- **Sharp: n=76  W=17/L=59  WR=22.4%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; upper third; RSI 50-60 upper neutral  •  ONLY when HTF20 aligned WITH trade

### L06.  `H60=H60a AND T1=T1c AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=165  W=65/L=100  WR=39.4%
- Sharpen: sharpest is H20=H20a (70/100 of losers there)
- **Sharp: n=97  W=27/L=70  WR=27.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when HTF20 aligned WITH trade

### L07.  `T1=T1c AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=160  W=64/L=96  WR=40.0%
- Sharpen: sharpest is BBP=BBP4 (54/96 of losers there)
- **Sharp: n=71  W=17/L=54  WR=23.9%**
- **Dir: SHORT**  •  1h trend AGAINST trade; session=ny_close  •  ONLY when upper third

### L08.  `H60=H60a AND T1=T1c AND T4=T4a AND ZS=ZS4`
- Raw: n=154  W=58/L=96  WR=37.7%
- Sharpen: sharpest is H20=H20a (67/96 of losers there)
- **Sharp: n=84  W=17/L=67  WR=20.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; zscore +1 to +2 overbought  •  ONLY when HTF20 aligned WITH trade

### L09.  `T1=T1c AND T4=T4a AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=153  W=59/L=94  WR=38.6%
- Sharpen: sharpest is H20=H20a (58/94 of losers there)
- **Sharp: n=75  W=17/L=58  WR=22.7%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when HTF20 aligned WITH trade

### L10.  `H20=H20a AND H60=H60a AND T4=T4a AND RSI=RSI4`
- Raw: n=147  W=56/L=91  WR=38.1%
- Sharpen: sharpest is BBP=BBP4 (59/91 of losers there)
- **Sharp: n=74  W=15/L=59  WR=20.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when upper third

### L11.  `H20=H20a AND T1=T1c AND BBP=BBP4`
- Raw: n=141  W=52/L=89  WR=36.9%
- Sharpen: sharpest is H60=H60a (80/89 of losers there)
- **Sharp: n=109  W=29/L=80  WR=26.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; upper third  •  ONLY when HTF60 aligned WITH trade

### L12.  `H60=H60a AND T1=T1c AND session_bucket=ny_close`
- Raw: n=139  W=55/L=84  WR=39.6%
- Sharpen: sharpest is BBP=BBP4 (49/84 of losers there)
- **Sharp: n=64  W=15/L=49  WR=23.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=ny_close  •  ONLY when upper third

### L13.  `H60=H60a AND T1=T1c AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=139  W=55/L=84  WR=39.6%
- Sharpen: sharpest is BBP=BBP4 (49/84 of losers there)
- **Sharp: n=64  W=15/L=49  WR=23.4%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=ny_close  •  ONLY when upper third

### L14.  `T4=T4a AND RSI=RSI4 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=136  W=52/L=84  WR=38.2%
- Sharpen: sharpest is ZS=ZS3 (23/84 of losers there)
- **Sharp: n=28  W=5/L=23  WR=17.9%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 50-60 upper neutral; session=ny_close  •  ONLY when zscore -1 to +1 neutral

### L15.  `H20=H20a AND H60=H60a AND BBP=BBP4`
- Raw: n=134  W=49/L=85  WR=36.6%
- Sharpen: sharpest is T1=T1c (80/85 of losers there)
- **Sharp: n=109  W=29/L=80  WR=26.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; upper third  •  ONLY when 1h trend AGAINST trade

### L16.  `H20=H20a AND H60=H60a AND BBP=BBP4 AND direction_exec=short`
- Raw: n=134  W=49/L=85  WR=36.6%
- Sharpen: sharpest is T1=T1c (80/85 of losers there)
- **Sharp: n=109  W=29/L=80  WR=26.6%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; upper third  •  ONLY when 1h trend AGAINST trade

### L17.  `H20=H20a AND T1=T1c AND ZS=ZS4`
- Raw: n=134  W=52/L=82  WR=38.8%
- Sharpen: sharpest is H60=H60a (79/82 of losers there)
- **Sharp: n=108  W=29/L=79  WR=26.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; zscore +1 to +2 overbought  •  ONLY when HTF60 aligned WITH trade

### L18.  `H20=H20a AND T1=T1c AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=134  W=52/L=82  WR=38.8%
- Sharpen: sharpest is H60=H60a (79/82 of losers there)
- **Sharp: n=108  W=29/L=79  WR=26.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; upper third; zscore +1 to +2 overbought  •  ONLY when HTF60 aligned WITH trade

### L19.  `H20=H20a AND T1=T1c AND BBP=BBP4 AND direction_exec=short`
- Raw: n=129  W=49/L=80  WR=38.0%
- Sharpen: sharpest is H60=H60a (80/80 of losers there)
- **Sharp: n=109  W=29/L=80  WR=26.6%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; upper third  •  ONLY when HTF60 aligned WITH trade

### L20.  `H20=H20a AND T1=T1c AND ZS=ZS4 AND direction_exec=short`
- Raw: n=128  W=49/L=79  WR=38.3%
- Sharpen: sharpest is H60=H60a (79/79 of losers there)
- **Sharp: n=108  W=29/L=79  WR=26.9%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; zscore +1 to +2 overbought  •  ONLY when HTF60 aligned WITH trade

### L21.  `T1=T1c AND RSI=RSI4 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=128  W=50/L=78  WR=39.1%
- Sharpen: sharpest is BBP=BBP4 (52/78 of losers there)
- **Sharp: n=69  W=17/L=52  WR=24.6%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; session=ny_close  •  ONLY when upper third

### L22.  `H20=H20a AND H60=H60a AND ZS=ZS4`
- Raw: n=125  W=41/L=84  WR=32.8%
- Sharpen: sharpest is T4=T4a (70/84 of losers there)
- **Sharp: n=89  W=19/L=70  WR=21.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; zscore +1 to +2 overbought  •  ONLY when 4h trend WITH trade

### L23.  `H20=H20a AND H60=H60a AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=125  W=41/L=84  WR=32.8%
- Sharpen: sharpest is T4=T4a (70/84 of losers there)
- **Sharp: n=89  W=19/L=70  WR=21.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; upper third; zscore +1 to +2 overbought  •  ONLY when 4h trend WITH trade

### L24.  `H20=H20a AND H60=H60a AND ZS=ZS4 AND direction_exec=short`
- Raw: n=125  W=41/L=84  WR=32.8%
- Sharpen: sharpest is T4=T4a (70/84 of losers there)
- **Sharp: n=89  W=19/L=70  WR=21.3%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; zscore +1 to +2 overbought  •  ONLY when 4h trend WITH trade

### L25.  `H20=H20a AND T4=T4a AND BBP=BBP4`
- Raw: n=125  W=45/L=80  WR=36.0%
- Sharpen: sharpest is RSI=RSI4 (64/80 of losers there)
- **Sharp: n=81  W=17/L=64  WR=21.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; upper third  •  ONLY when RSI 50-60 upper neutral

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20b(19/12) | H20d(13/20), H20a(20/25) |
| H60 | H60b(11/4) | H60d(5/11) |
| T1 | T1a(56/42) | T1c(44/58) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
