# EUR_NZD — R23 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20d**  (EMA20 down 0.15-0.5x)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **8,381**  (W=5,088 / L=3,293)  -  WR: **60.7%**

## Session distribution

- asia: n=2264  W=1385/L=879  WR=61.2%
- london_open: n=1987  W=1227/L=760  WR=61.8%
- ny_mid: n=1024  W=611/L=413  WR=59.7%
- ny_open: n=872  W=513/L=359  WR=58.8%
- ny_close: n=860  W=548/L=312  WR=63.7%
- london: n=719  W=428/L=291  WR=59.5%
- off_hours: n=353  W=209/L=144  WR=59.2%
- asia_late: n=302  W=167/L=135  WR=55.3%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60a AND T1=T1c AND RSI=RSI4 AND direction_exec=long`
- Raw: n=215  W=184/L=31  WR=85.6%
- Refine: exclude session_bucket=asia drops 19/31 losers (61%)
- **Final: n=129  W=117/L=12  WR=90.7%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when session=asia

### W02.  `T4=T4c AND RSI=RSI3 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=179  W=155/L=24  WR=86.6%
- Refine: exclude session_bucket=asia drops 17/24 losers (71%)
- **Final: n=119  W=112/L=7  WR=94.1%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; zscore +1 to +2 overbought  •  AVOID when session=asia

### W03.  `H60=H60a AND T4=T4a AND RSI=RSI2`
- Raw: n=131  W=115/L=16  WR=87.8%
- Refine: exclude ZS=ZS2 drops 14/16 losers (88%)
- **Final: n=80  W=78/L=2  WR=97.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 30-40 weak  •  AVOID when zscore -2 to -1 oversold

### W04.  `H60=H60e AND BBP=BBP2 AND session_bucket=ny_close`
- Raw: n=121  W=103/L=18  WR=85.1%
- Refine: exclude H20=H20b drops 10/18 losers (56%)
- **Final: n=82  W=74/L=8  WR=90.2%**
- **Dir: ?**  •  HTF60 strongly against; lower third; session=ny_close  •  AVOID when HTF20 slightly aligned

### W05.  `RSI=RSI3 AND strategy_id=TF2_pullback_EMA20_long AND direction_exec=short`
- Raw: n=120  W=103/L=17  WR=85.8%
- Refine: exclude T4=T4a drops 13/17 losers (76%)
- **Final: n=55  W=51/L=4  WR=92.7%**
- **Dir: SHORT**  •  RSI 40-50 lower neutral; strategy=TF2_pullback_EMA20_long  •  AVOID when 4h trend WITH trade

### W06.  `H20=H20d AND T4=T4c AND ZS=ZS2`
- Raw: n=115  W=100/L=15  WR=87.0%
- Refine: exclude H60=H60c drops 8/15 losers (53%)
- **Final: n=87  W=80/L=7  WR=92.0%**
- **Dir: ?**  •  HTF20 mildly against; 4h trend AGAINST trade; zscore -2 to -1 oversold  •  AVOID when HTF60 neutral

### W07.  `H20=H20d AND T4=T4c AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=115  W=100/L=15  WR=87.0%
- Refine: exclude H60=H60c drops 8/15 losers (53%)
- **Final: n=87  W=80/L=7  WR=92.0%**
- **Dir: ?**  •  HTF20 mildly against; 4h trend AGAINST trade; lower third; zscore -2 to -1 oversold  •  AVOID when HTF60 neutral

### W08.  `H60=H60a AND T1=T1a AND RSI=RSI2`
- Raw: n=114  W=104/L=10  WR=91.2%
- Refine: exclude ZS=ZS2 drops 9/10 losers (90%)
- **Final: n=69  W=68/L=1  WR=98.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 30-40 weak  •  AVOID when zscore -2 to -1 oversold

### W09.  `H60=H60a AND RSI=RSI2 AND direction_exec=short`
- Raw: n=114  W=104/L=10  WR=91.2%
- Refine: exclude ZS=ZS2 drops 9/10 losers (90%)
- **Final: n=69  W=68/L=1  WR=98.6%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; RSI 30-40 weak  •  AVOID when zscore -2 to -1 oversold

### W10.  `H60=H60a AND T1=T1a AND RSI=RSI2 AND direction_exec=short`
- Raw: n=114  W=104/L=10  WR=91.2%
- Refine: exclude ZS=ZS2 drops 9/10 losers (90%)
- **Final: n=69  W=68/L=1  WR=98.6%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 30-40 weak  •  AVOID when zscore -2 to -1 oversold

### W11.  `BBP=BBP6 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=113  W=99/L=14  WR=87.6%
- Refine: exclude T1=T1c drops 14/14 losers (100%)
- **Final: n=67  W=67/L=0  WR=100.0%**
- **Dir: SHORT**  •  deep above upper band; session=london_open  •  AVOID when 1h trend AGAINST trade

### W12.  `H20=H20d AND H60=H60a AND T1=T1c AND direction_exec=long`
- Raw: n=110  W=95/L=15  WR=86.4%
- Refine: exclude BBP=BBP6 drops 9/15 losers (60%)
- **Final: n=101  W=95/L=6  WR=94.1%**
- **Dir: LONG**  •  HTF20 mildly against; HTF60 aligned WITH trade; 1h trend AGAINST trade  •  AVOID when deep above upper band

### W13.  `H20=H20d AND T4=T4c AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=109  W=94/L=15  WR=86.2%
- Refine: exclude H60=H60c drops 8/15 losers (53%)
- **Final: n=81  W=74/L=7  WR=91.4%**
- **Dir: ?**  •  HTF20 mildly against; 4h trend AGAINST trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when HTF60 neutral

### W14.  `H60=H60a AND T1=T1a AND T4=T4a AND RSI=RSI2`
- Raw: n=104  W=94/L=10  WR=90.4%
- Refine: exclude BBP=BBP2 drops 10/10 losers (100%)
- **Final: n=54  W=54/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; RSI 30-40 weak  •  AVOID when lower third

### W15.  `H60=H60a AND T4=T4a AND RSI=RSI2 AND direction_exec=short`
- Raw: n=104  W=94/L=10  WR=90.4%
- Refine: exclude BBP=BBP2 drops 10/10 losers (100%)
- **Final: n=54  W=54/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 30-40 weak  •  AVOID when lower third

### W16.  `H20=H20d AND H60=H60a AND RSI=RSI4 AND direction_exec=long`
- Raw: n=103  W=97/L=6  WR=94.2%
- Refine: exclude T4=T4c drops 6/6 losers (100%)
- **Final: n=44  W=44/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 mildly against; HTF60 aligned WITH trade; RSI 50-60 upper neutral  •  AVOID when 4h trend AGAINST trade

### W17.  `H20=H20d AND T4=T4c AND ZS=ZS2 AND direction_exec=long`
- Raw: n=103  W=88/L=15  WR=85.4%
- Refine: exclude H60=H60c drops 8/15 losers (53%)
- **Final: n=75  W=68/L=7  WR=90.7%**
- **Dir: LONG**  •  HTF20 mildly against; 4h trend AGAINST trade; zscore -2 to -1 oversold  •  AVOID when HTF60 neutral

### W18.  `H60=H60c AND T4=T4c AND direction_exec=short`
- Raw: n=100  W=86/L=14  WR=86.0%
- Refine: exclude T1=T1a drops 14/14 losers (100%)
- **Final: n=29  W=29/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 neutral; 4h trend AGAINST trade  •  AVOID when 1h trend WITH trade

### W19.  `H20=H20b AND T1=T1a AND session_bucket=ny_close`
- Raw: n=97  W=91/L=6  WR=93.8%
- Refine: exclude BBP=BBP3 drops 3/6 losers (50%)
- **Final: n=89  W=86/L=3  WR=96.6%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend WITH trade; session=ny_close  •  AVOID when middle of band

### W20.  `H20=H20a AND BBP=BBP4 AND session_bucket=ny_close`
- Raw: n=95  W=81/L=14  WR=85.3%
- Refine: exclude T4=T4a drops 14/14 losers (100%)
- **Final: n=53  W=53/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; upper third; session=ny_close  •  AVOID when 4h trend WITH trade

### W21.  `H20=H20d AND T4=T4a AND direction_exec=long`
- Raw: n=93  W=81/L=12  WR=87.1%
- Refine: exclude BBP=BBP2 drops 6/12 losers (50%)
- **Final: n=84  W=78/L=6  WR=92.9%**
- **Dir: LONG**  •  HTF20 mildly against; 4h trend WITH trade  •  AVOID when lower third

### W22.  `T1=T1a AND RSI=RSI3 AND strategy_id=TF2_pullback_EMA20_long AND direction_exec=short`
- Raw: n=92  W=79/L=13  WR=85.9%
- Refine: exclude T4=T4a drops 9/13 losers (69%)
- **Final: n=42  W=38/L=4  WR=90.5%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 40-50 lower neutral; strategy=TF2_pullback_EMA20_long  •  AVOID when 4h trend WITH trade

### W23.  `H20=H20d AND T1=T1c AND T4=T4a AND direction_exec=long`
- Raw: n=91  W=81/L=10  WR=89.0%
- Refine: exclude session_bucket=asia drops 8/10 losers (80%)
- **Final: n=53  W=51/L=2  WR=96.2%**
- **Dir: LONG**  •  HTF20 mildly against; 1h trend AGAINST trade; 4h trend WITH trade  •  AVOID when session=asia

### W24.  `H20=H20e AND H60=H60a AND T1=T1a AND session_bucket=ny_open`
- Raw: n=89  W=79/L=10  WR=88.8%
- Refine: exclude RSI=RSI4 drops 10/10 losers (100%)
- **Final: n=47  W=47/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend WITH trade; session=ny_open  •  AVOID when RSI 50-60 upper neutral

### W25.  `T1=T1a AND BBP=BBP6 AND ZS=ZS5 AND session_bucket=london_open`
- Raw: n=89  W=78/L=11  WR=87.6%
- Refine: exclude direction_exec=long drops 11/11 losers (100%)
- **Final: n=55  W=55/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; deep above upper band; zscore +2 to +3 deep overbought; session=london_open  •  AVOID when long

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `RSI=RSI3 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=307  W=109/L=198  WR=35.5%
- Sharpen: sharpest is T4=T4a (90/198 of losers there)
- **Sharp: n=115  W=25/L=90  WR=21.7%**
- **Dir: LONG**  •  RSI 40-50 lower neutral; zscore +1 to +2 overbought  •  ONLY when 4h trend WITH trade

### L02.  `BBP=BBP4 AND RSI=RSI3 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=307  W=109/L=198  WR=35.5%
- Sharpen: sharpest is T4=T4a (90/198 of losers there)
- **Sharp: n=115  W=25/L=90  WR=21.7%**
- **Dir: LONG**  •  upper third; RSI 40-50 lower neutral; zscore +1 to +2 overbought  •  ONLY when 4h trend WITH trade

### L03.  `T1=T1c AND RSI=RSI3 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=232  W=87/L=145  WR=37.5%
- Sharpen: sharpest is T4=T4a (68/145 of losers there)
- **Sharp: n=92  W=24/L=68  WR=26.1%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 40-50 lower neutral; zscore +1 to +2 overbought  •  ONLY when 4h trend WITH trade

### L04.  `T1=T1a AND T4=T4c AND RSI=RSI4 AND direction_exec=short`
- Raw: n=232  W=90/L=142  WR=38.8%
- Sharpen: sharpest is ZS=ZS4 (94/142 of losers there)
- **Sharp: n=120  W=26/L=94  WR=21.7%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when zscore +1 to +2 overbought

### L05.  `T4=T4c AND BBP=BBP4 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=215  W=76/L=139  WR=35.3%
- Sharpen: sharpest is T1=T1a (103/139 of losers there)
- **Sharp: n=137  W=34/L=103  WR=24.8%**
- **Dir: SHORT**  •  4h trend AGAINST trade; upper third; RSI 50-60 upper neutral  •  ONLY when 1h trend WITH trade

### L06.  `T1=T1c AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=214  W=79/L=135  WR=36.9%
- Sharpen: sharpest is H20=H20a (38/135 of losers there)
- **Sharp: n=38  W=0/L=38  WR=0.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; session=ny_open  •  ONLY when HTF20 aligned WITH trade

### L07.  `H60=H60e AND T1=T1c AND session_bucket=ny_open`
- Raw: n=209  W=81/L=128  WR=38.8%
- Sharpen: sharpest is H20=H20a (44/128 of losers there)
- **Sharp: n=52  W=8/L=44  WR=15.4%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; session=ny_open  •  ONLY when HTF20 aligned WITH trade

### L08.  `H60=H60e AND T4=T4c AND RSI=RSI4 AND direction_exec=short`
- Raw: n=197  W=75/L=122  WR=38.1%
- Sharpen: sharpest is BBP=BBP4 (71/122 of losers there)
- **Sharp: n=89  W=18/L=71  WR=20.2%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when upper third

### L09.  `H20=H20e AND RSI=RSI3 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=182  W=69/L=113  WR=37.9%
- Sharpen: sharpest is T4=T4a (57/113 of losers there)
- **Sharp: n=78  W=21/L=57  WR=26.9%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 40-50 lower neutral; zscore +1 to +2 overbought  •  ONLY when 4h trend WITH trade

### L10.  `H60=H60e AND RSI=RSI3 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=181  W=69/L=112  WR=38.1%
- Sharpen: sharpest is T4=T4a (47/112 of losers there)
- **Sharp: n=59  W=12/L=47  WR=20.3%**
- **Dir: LONG**  •  HTF60 strongly against; RSI 40-50 lower neutral; zscore +1 to +2 overbought  •  ONLY when 4h trend WITH trade

### L11.  `T4=T4c AND RSI=RSI4 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=180  W=63/L=117  WR=35.0%
- Sharpen: sharpest is T1=T1a (94/117 of losers there)
- **Sharp: n=120  W=26/L=94  WR=21.7%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when 1h trend WITH trade

### L12.  `T1=T1a AND BBP=BBP4 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=172  W=55/L=117  WR=32.0%
- Sharpen: sharpest is H60=H60e (67/117 of losers there)
- **Sharp: n=81  W=14/L=67  WR=17.3%**
- **Dir: SHORT**  •  1h trend WITH trade; upper third; RSI 50-60 upper neutral  •  ONLY when HTF60 strongly against

### L13.  `H20=H20e AND RSI=RSI4 AND direction_exec=short`
- Raw: n=172  W=64/L=108  WR=37.2%
- Sharpen: sharpest is H60=H60a (45/108 of losers there)
- **Sharp: n=60  W=15/L=45  WR=25.0%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 50-60 upper neutral  •  ONLY when HTF60 aligned WITH trade

### L14.  `H60=H60e AND T1=T1a AND RSI=RSI4 AND direction_exec=short`
- Raw: n=161  W=40/L=121  WR=24.8%
- Sharpen: sharpest is ZS=ZS4 (66/121 of losers there)
- **Sharp: n=78  W=12/L=66  WR=15.4%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when zscore +1 to +2 overbought

### L15.  `T1=T1c AND T4=T4a AND session_bucket=ny_close`
- Raw: n=155  W=56/L=99  WR=36.1%
- Sharpen: sharpest is BBP=BBP4 (29/99 of losers there)
- **Sharp: n=33  W=4/L=29  WR=12.1%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; session=ny_close  •  ONLY when upper third

### L16.  `H20=H20e AND T4=T4c AND RSI=RSI4 AND direction_exec=short`
- Raw: n=154  W=52/L=102  WR=33.8%
- Sharpen: sharpest is session_bucket=london (30/102 of losers there)
- **Sharp: n=30  W=0/L=30  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when session=london

### L17.  `H20=H20b AND RSI=RSI4 AND direction_exec=short`
- Raw: n=154  W=59/L=95  WR=38.3%
- Sharpen: sharpest is H60=H60e (63/95 of losers there)
- **Sharp: n=76  W=13/L=63  WR=17.1%**
- **Dir: SHORT**  •  HTF20 slightly aligned; RSI 50-60 upper neutral  •  ONLY when HTF60 strongly against

### L18.  `T4=T4a AND BBP=BBP4 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=152  W=47/L=105  WR=30.9%
- Sharpen: sharpest is ZS=ZS4 (90/105 of losers there)
- **Sharp: n=115  W=25/L=90  WR=21.7%**
- **Dir: LONG**  •  4h trend WITH trade; upper third; RSI 40-50 lower neutral  •  ONLY when zscore +1 to +2 overbought

### L19.  `RSI=RSI3 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=152  W=54/L=98  WR=35.5%
- Sharpen: sharpest is BBP=BBP5 (65/98 of losers there)
- **Sharp: n=88  W=23/L=65  WR=26.1%**
- **Dir: LONG**  •  RSI 40-50 lower neutral; zscore +2 to +3 deep overbought  •  ONLY when just touched upper band

### L20.  `H20=H20e AND T1=T1c AND RSI=RSI4 AND direction_exec=short`
- Raw: n=151  W=55/L=96  WR=36.4%
- Sharpen: sharpest is session_bucket=london_open (15/96 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when session=london_open

### L21.  `T1=T1a AND RSI=RSI4 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=148  W=41/L=107  WR=27.7%
- Sharpen: sharpest is H60=H60e (66/107 of losers there)
- **Sharp: n=78  W=12/L=66  WR=15.4%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when HTF60 strongly against

### L22.  `H60=H60e AND BBP=BBP4 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=144  W=52/L=92  WR=36.1%
- Sharpen: sharpest is T1=T1a (67/92 of losers there)
- **Sharp: n=81  W=14/L=67  WR=17.3%**
- **Dir: SHORT**  •  HTF60 strongly against; upper third; RSI 50-60 upper neutral  •  ONLY when 1h trend WITH trade

### L23.  `H60=H60e AND T1=T1c AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=141  W=47/L=94  WR=33.3%
- Sharpen: sharpest is BBP=BBP2 (35/94 of losers there)
- **Sharp: n=40  W=5/L=35  WR=12.5%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend AGAINST trade; session=ny_open  •  ONLY when lower third

### L24.  `H60=H60e AND T1=T1c AND T4=T4c AND session_bucket=ny_open`
- Raw: n=140  W=55/L=85  WR=39.3%
- Sharpen: sharpest is RSI=RSI2 (25/85 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_open  •  ONLY when RSI 30-40 weak

### L25.  `H20=H20b AND BBP=BBP3 AND ZS=ZS3`
- Raw: n=140  W=56/L=84  WR=40.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=140  W=56/L=84  WR=40.0%**
- **Dir: ?**  •  HTF20 slightly aligned; middle of band; zscore -1 to +1 neutral

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | — |
| T1 | — | — |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
