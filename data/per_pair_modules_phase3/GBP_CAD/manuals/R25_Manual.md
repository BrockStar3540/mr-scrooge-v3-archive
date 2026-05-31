# GBP_CAD — R25 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **3,935**  (W=2,521 / L=1,414)  -  WR: **64.1%**

## Session distribution

- london_open: n=1231  W=791/L=440  WR=64.3%
- asia: n=890  W=559/L=331  WR=62.8%
- london: n=721  W=466/L=255  WR=64.6%
- ny_open: n=463  W=297/L=166  WR=64.1%
- asia_late: n=459  W=283/L=176  WR=61.7%
- ny_mid: n=122  W=88/L=34  WR=72.1%
- off_hours: n=37  W=28/L=9  WR=75.7%
- ny_close: n=12  W=9/L=3  WR=75.0%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1c AND RSI=RSI4 AND direction_exec=long`
- Raw: n=399  W=347/L=52  WR=87.0%
- Refine: exclude H20=H20c drops 17/52 losers (33%)
- **Final: n=331  W=296/L=35  WR=89.4%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when HTF20 neutral

### W02.  `T4=T4c AND direction_exec=long AND session_bucket=london_open`
- Raw: n=351  W=302/L=49  WR=86.0%
- Refine: exclude RSI=RSI5 drops 28/49 losers (57%)
- **Final: n=251  W=230/L=21  WR=91.6%**
- **Dir: LONG**  •  4h trend AGAINST trade; session=london_open  •  AVOID when RSI 60-70 strong

### W03.  `T1=T1a AND T4=T4c AND direction_exec=long AND session_bucket=london_open`
- Raw: n=236  W=201/L=35  WR=85.2%
- Refine: exclude RSI=RSI5 drops 28/35 losers (80%)
- **Final: n=136  W=129/L=7  WR=94.9%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend AGAINST trade; session=london_open  •  AVOID when RSI 60-70 strong

### W04.  `H60=H60e AND T1=T1c AND RSI=RSI4 AND direction_exec=long`
- Raw: n=216  W=196/L=20  WR=90.7%
- Refine: exclude session_bucket=asia drops 15/20 losers (75%)
- **Final: n=109  W=104/L=5  WR=95.4%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when session=asia

### W05.  `T1=T1c AND T4=T4c AND RSI=RSI4 AND direction_exec=long`
- Raw: n=209  W=181/L=28  WR=86.6%
- Refine: exclude session_bucket=london drops 9/28 losers (32%)
- **Final: n=195  W=176/L=19  WR=90.3%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when session=london

### W06.  `H60=H60c AND T1=T1c AND direction_exec=long`
- Raw: n=207  W=185/L=22  WR=89.4%
- Refine: exclude RSI=RSI2 drops 11/22 losers (50%)
- **Final: n=196  W=185/L=11  WR=94.4%**
- **Dir: LONG**  •  HTF60 neutral; 1h trend AGAINST trade  •  AVOID when RSI 30-40 weak

### W07.  `H60=H60a AND T1=T1c AND BBP=BBP2`
- Raw: n=206  W=191/L=15  WR=92.7%
- Refine: exclude T4=T4c drops 14/15 losers (93%)
- **Final: n=68  W=67/L=1  WR=98.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; lower third  •  AVOID when 4h trend AGAINST trade

### W08.  `T1=T1c AND T4=T4a AND RSI=RSI4 AND direction_exec=long`
- Raw: n=190  W=166/L=24  WR=87.4%
- Refine: exclude session_bucket=asia drops 15/24 losers (62%)
- **Final: n=138  W=129/L=9  WR=93.5%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when session=asia

### W09.  `H60=H60a AND T1=T1c AND ZS=ZS2`
- Raw: n=185  W=171/L=14  WR=92.4%
- Refine: exclude T4=T4c drops 14/14 losers (100%)
- **Final: n=61  W=61/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; zscore -2 to -1 oversold  •  AVOID when 4h trend AGAINST trade

### W10.  `H60=H60a AND T1=T1c AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=185  W=171/L=14  WR=92.4%
- Refine: exclude T4=T4c drops 14/14 losers (100%)
- **Final: n=61  W=61/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; lower third; zscore -2 to -1 oversold  •  AVOID when 4h trend AGAINST trade

### W11.  `H60=H60a AND T1=T1c AND BBP=BBP2 AND direction_exec=short`
- Raw: n=174  W=159/L=15  WR=91.4%
- Refine: exclude T4=T4c drops 14/15 losers (93%)
- **Final: n=64  W=63/L=1  WR=98.4%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; lower third  •  AVOID when 4h trend AGAINST trade

### W12.  `T4=T4a AND BBP=BBP4 AND direction_exec=long`
- Raw: n=170  W=149/L=21  WR=87.6%
- Refine: exclude H20=H20a drops 13/21 losers (62%)
- **Final: n=119  W=111/L=8  WR=93.3%**
- **Dir: LONG**  •  4h trend WITH trade; upper third  •  AVOID when HTF20 aligned WITH trade

### W13.  `T4=T4c AND ZS=ZS1 AND direction_exec=long`
- Raw: n=170  W=149/L=21  WR=87.6%
- Refine: exclude session_bucket=asia drops 13/21 losers (62%)
- **Final: n=137  W=129/L=8  WR=94.2%**
- **Dir: LONG**  •  4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  AVOID when session=asia

### W14.  `T1=T1c AND BBP=BBP4 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=163  W=141/L=22  WR=86.5%
- Refine: exclude H20=H20c drops 9/22 losers (41%)
- **Final: n=131  W=118/L=13  WR=90.1%**
- **Dir: LONG**  •  1h trend AGAINST trade; upper third; RSI 50-60 upper neutral  •  AVOID when HTF20 neutral

### W15.  `H60=H60a AND T1=T1c AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=159  W=146/L=13  WR=91.8%
- Refine: exclude H20=H20c drops 9/13 losers (69%)
- **Final: n=94  W=90/L=4  WR=95.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; lower third; RSI 40-50 lower neutral  •  AVOID when HTF20 neutral

### W16.  `H60=H60a AND T1=T1c AND ZS=ZS2 AND direction_exec=short`
- Raw: n=159  W=145/L=14  WR=91.2%
- Refine: exclude T4=T4c drops 14/14 losers (100%)
- **Final: n=57  W=57/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; zscore -2 to -1 oversold  •  AVOID when 4h trend AGAINST trade

### W17.  `T1=T1c AND BBP=BBP2 AND session_bucket=london`
- Raw: n=159  W=141/L=18  WR=88.7%
- Refine: exclude H60=H60b drops 7/18 losers (39%)
- **Final: n=136  W=125/L=11  WR=91.9%**
- **Dir: ?**  •  1h trend AGAINST trade; lower third; session=london  •  AVOID when HTF60 slightly aligned

### W18.  `T1=T1c AND ZS=ZS2 AND session_bucket=london`
- Raw: n=153  W=137/L=16  WR=89.5%
- Refine: exclude H60=H60b drops 7/16 losers (44%)
- **Final: n=130  W=121/L=9  WR=93.1%**
- **Dir: ?**  •  1h trend AGAINST trade; zscore -2 to -1 oversold; session=london  •  AVOID when HTF60 slightly aligned

### W19.  `T1=T1c AND BBP=BBP2 AND ZS=ZS2 AND session_bucket=london`
- Raw: n=153  W=137/L=16  WR=89.5%
- Refine: exclude H60=H60b drops 7/16 losers (44%)
- **Final: n=130  W=121/L=9  WR=93.1%**
- **Dir: ?**  •  1h trend AGAINST trade; lower third; zscore -2 to -1 oversold; session=london  •  AVOID when HTF60 slightly aligned

### W20.  `T1=T1c AND RSI=RSI4 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=153  W=135/L=18  WR=88.2%
- Refine: exclude H20=H20c drops 8/18 losers (44%)
- **Final: n=122  W=112/L=10  WR=91.8%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when HTF20 neutral

### W21.  `T4=T4c AND RSI=RSI4 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=152  W=146/L=6  WR=96.1%
- Refine: exclude ZS=ZS5 drops 6/6 losers (100%)
- **Final: n=105  W=105/L=0  WR=100.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 50-60 upper neutral; session=london_open  •  AVOID when zscore +2 to +3 deep overbought

### W22.  `T4=T4a AND ZS=ZS4 AND direction_exec=long`
- Raw: n=152  W=135/L=17  WR=88.8%
- Refine: exclude H20=H20a drops 11/17 losers (65%)
- **Final: n=109  W=103/L=6  WR=94.5%**
- **Dir: LONG**  •  4h trend WITH trade; zscore +1 to +2 overbought  •  AVOID when HTF20 aligned WITH trade

### W23.  `T4=T4a AND BBP=BBP4 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=152  W=135/L=17  WR=88.8%
- Refine: exclude H20=H20a drops 11/17 losers (65%)
- **Final: n=109  W=103/L=6  WR=94.5%**
- **Dir: LONG**  •  4h trend WITH trade; upper third; zscore +1 to +2 overbought  •  AVOID when HTF20 aligned WITH trade

### W24.  `T1=T1c AND RSI=RSI4 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=152  W=131/L=21  WR=86.2%
- Refine: exclude BBP=BBP6 drops 16/21 losers (76%)
- **Final: n=64  W=59/L=5  WR=92.2%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when deep above upper band

### W25.  `T1=T1c AND T4=T4c AND session_bucket=asia_late`
- Raw: n=151  W=129/L=22  WR=85.4%
- Refine: exclude ZS=ZS2 drops 9/22 losers (41%)
- **Final: n=127  W=114/L=13  WR=89.8%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=asia_late  •  AVOID when zscore -2 to -1 oversold

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1a AND T4=T4a AND RSI=RSI4`
- Raw: n=380  W=144/L=236  WR=37.9%
- Sharpen: sharpest is ZS=ZS5 (85/236 of losers there)
- **Sharp: n=103  W=18/L=85  WR=17.5%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when zscore +2 to +3 deep overbought

### L02.  `T1=T1a AND RSI=RSI4 AND direction_exec=short`
- Raw: n=324  W=104/L=220  WR=32.1%
- Sharpen: sharpest is ZS=ZS5 (89/220 of losers there)
- **Sharp: n=107  W=18/L=89  WR=16.8%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when zscore +2 to +3 deep overbought

### L03.  `T1=T1a AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=250  W=95/L=155  WR=38.0%
- Sharpen: sharpest is direction_exec=short (89/155 of losers there)
- **Sharp: n=107  W=18/L=89  WR=16.8%**
- **Dir: ?**  •  1h trend WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when short

### L04.  `H20=H20e AND T1=T1a AND direction_exec=short`
- Raw: n=236  W=91/L=145  WR=38.6%
- Sharpen: sharpest is RSI=RSI4 (88/145 of losers there)
- **Sharp: n=111  W=23/L=88  WR=20.7%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend WITH trade  •  ONLY when RSI 50-60 upper neutral

### L05.  `H20=H20e AND T1=T1a AND T4=T4a`
- Raw: n=196  W=72/L=124  WR=36.7%
- Sharpen: sharpest is ZS=ZS5 (40/124 of losers there)
- **Sharp: n=42  W=2/L=40  WR=4.8%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when zscore +2 to +3 deep overbought

### L06.  `H60=H60a AND T1=T1a AND RSI=RSI4 AND direction_exec=short`
- Raw: n=168  W=47/L=121  WR=28.0%
- Sharpen: sharpest is BBP=BBP5 (33/121 of losers there)
- **Sharp: n=35  W=2/L=33  WR=5.7%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when just touched upper band

### L07.  `T1=T1a AND T4=T4a AND RSI=RSI4 AND direction_exec=short`
- Raw: n=163  W=48/L=115  WR=29.4%
- Sharpen: sharpest is H60=H60c (35/115 of losers there)
- **Sharp: n=37  W=2/L=35  WR=5.4%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when HTF60 neutral

### L08.  `T1=T1a AND T4=T4c AND RSI=RSI4 AND direction_exec=short`
- Raw: n=161  W=56/L=105  WR=34.8%
- Sharpen: sharpest is ZS=ZS5 (40/105 of losers there)
- **Sharp: n=47  W=7/L=40  WR=14.9%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when zscore +2 to +3 deep overbought

### L09.  `H60=H60c AND T1=T1a AND direction_exec=short`
- Raw: n=160  W=52/L=108  WR=32.5%
- Sharpen: sharpest is RSI=RSI4 (64/108 of losers there)
- **Sharp: n=72  W=8/L=64  WR=11.1%**
- **Dir: SHORT**  •  HTF60 neutral; 1h trend WITH trade  •  ONLY when RSI 50-60 upper neutral

### L10.  `T1=T1a AND T4=T4a AND RSI=RSI4 AND session_bucket=london_open`
- Raw: n=157  W=58/L=99  WR=36.9%
- Sharpen: sharpest is ZS=ZS5 (44/99 of losers there)
- **Sharp: n=56  W=12/L=44  WR=21.4%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral; session=london_open  •  ONLY when zscore +2 to +3 deep overbought

### L11.  `T1=T1a AND ZS=ZS5 AND direction_exec=short`
- Raw: n=151  W=48/L=103  WR=31.8%
- Sharpen: sharpest is RSI=RSI4 (89/103 of losers there)
- **Sharp: n=107  W=18/L=89  WR=16.8%**
- **Dir: SHORT**  •  1h trend WITH trade; zscore +2 to +3 deep overbought  •  ONLY when RSI 50-60 upper neutral

### L12.  `H20=H20e AND H60=H60a AND T1=T1a`
- Raw: n=150  W=54/L=96  WR=36.0%
- Sharpen: sharpest is RSI=RSI4 (60/96 of losers there)
- **Sharp: n=75  W=15/L=60  WR=20.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend WITH trade  •  ONLY when RSI 50-60 upper neutral

### L13.  `H20=H20e AND H60=H60a AND T1=T1a AND direction_exec=short`
- Raw: n=150  W=54/L=96  WR=36.0%
- Sharpen: sharpest is RSI=RSI4 (60/96 of losers there)
- **Sharp: n=75  W=15/L=60  WR=20.0%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend WITH trade  •  ONLY when RSI 50-60 upper neutral

### L14.  `H60=H60e AND T1=T1a AND BBP=BBP2`
- Raw: n=147  W=41/L=106  WR=27.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=147  W=41/L=106  WR=27.9%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; lower third

### L15.  `T4=T4a AND RSI=RSI4 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=146  W=57/L=89  WR=39.0%
- Sharpen: sharpest is T1=T1a (49/89 of losers there)
- **Sharp: n=60  W=11/L=49  WR=18.3%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when 1h trend WITH trade

### L16.  `T1=T1a AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=140  W=54/L=86  WR=38.6%
- Sharpen: sharpest is T4=T4a (45/86 of losers there)
- **Sharp: n=60  W=15/L=45  WR=25.0%**
- **Dir: ?**  •  1h trend WITH trade; just touched upper band; zscore +2 to +3 deep overbought  •  ONLY when 4h trend WITH trade

### L17.  `H60=H60e AND T1=T1a AND ZS=ZS2`
- Raw: n=137  W=40/L=97  WR=29.2%
- Sharpen: no sharper sub-pattern
- **Sharp: n=137  W=40/L=97  WR=29.2%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; zscore -2 to -1 oversold

### L18.  `H60=H60e AND T1=T1a AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=137  W=40/L=97  WR=29.2%
- Sharpen: no sharper sub-pattern
- **Sharp: n=137  W=40/L=97  WR=29.2%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; lower third; zscore -2 to -1 oversold

### L19.  `T1=T1a AND T4=T4a AND BBP=BBP2 AND direction_exec=long`
- Raw: n=137  W=52/L=85  WR=38.0%
- Sharpen: sharpest is H60=H60e (58/85 of losers there)
- **Sharp: n=84  W=26/L=58  WR=31.0%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; lower third  •  ONLY when HTF60 strongly against

### L20.  `H60=H60a AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=136  W=52/L=84  WR=38.2%
- Sharpen: sharpest is T1=T1a (51/84 of losers there)
- **Sharp: n=64  W=13/L=51  WR=20.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when 1h trend WITH trade

### L21.  `H20=H20e AND T1=T1a AND ZS=ZS5`
- Raw: n=135  W=52/L=83  WR=38.5%
- Sharpen: sharpest is T4=T4a (40/83 of losers there)
- **Sharp: n=42  W=2/L=40  WR=4.8%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; zscore +2 to +3 deep overbought  •  ONLY when 4h trend WITH trade

### L22.  `H60=H60c AND T1=T1a AND RSI=RSI4`
- Raw: n=134  W=43/L=91  WR=32.1%
- Sharpen: sharpest is direction_exec=short (64/91 of losers there)
- **Sharp: n=72  W=8/L=64  WR=11.1%**
- **Dir: ?**  •  HTF60 neutral; 1h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when short

### L23.  `T1=T1a AND T4=T4a AND ZS=ZS5`
- Raw: n=133  W=38/L=95  WR=28.6%
- Sharpen: sharpest is RSI=RSI4 (85/95 of losers there)
- **Sharp: n=103  W=18/L=85  WR=17.5%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  ONLY when RSI 50-60 upper neutral

### L24.  `T1=T1a AND ZS=ZS5 AND session_bucket=london_open`
- Raw: n=133  W=53/L=80  WR=39.8%
- Sharpen: sharpest is T4=T4a (49/80 of losers there)
- **Sharp: n=65  W=16/L=49  WR=24.6%**
- **Dir: ?**  •  1h trend WITH trade; zscore +2 to +3 deep overbought; session=london_open  •  ONLY when 4h trend WITH trade

### L25.  `H20=H20e AND T1=T1a AND T4=T4a AND direction_exec=short`
- Raw: n=132  W=48/L=84  WR=36.4%
- Sharpen: sharpest is RSI=RSI4 (44/84 of losers there)
- **Sharp: n=52  W=8/L=44  WR=15.4%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when RSI 50-60 upper neutral

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | — |
| T1 | T1c(57/41) | T1a(43/59) |
| T4 | T4c(55/43) | T4a(45/57) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
