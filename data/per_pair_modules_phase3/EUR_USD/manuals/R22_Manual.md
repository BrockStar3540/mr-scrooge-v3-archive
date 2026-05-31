# EUR_USD — R22 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20d**  (EMA20 down 0.15-0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR3**  (60-90%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **2,805**  (W=1,816 / L=989)  -  WR: **64.7%**

## Session distribution

- ny_mid: n=856  W=563/L=293  WR=65.8%
- london_open: n=622  W=400/L=222  WR=64.3%
- london: n=408  W=266/L=142  WR=65.2%
- ny_open: n=400  W=248/L=152  WR=62.0%
- asia: n=263  W=167/L=96  WR=63.5%
- ny_close: n=142  W=94/L=48  WR=66.2%
- asia_late: n=99  W=64/L=35  WR=64.6%
- off_hours: n=15  W=14/L=1  WR=93.3%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60a AND RSI=RSI2 AND session_bucket=london_open`
- Raw: n=172  W=150/L=22  WR=87.2%
- Refine: exclude H20=H20e drops 10/22 losers (45%)
- **Final: n=146  W=134/L=12  WR=91.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 30-40 weak; session=london_open  •  AVOID when HTF20 strongly against

### W02.  `H60=H60a AND T1=T1a AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=160  W=136/L=24  WR=85.0%
- Refine: exclude BBP=BBP2 drops 19/24 losers (79%)
- **Final: n=92  W=87/L=5  WR=94.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; session=ny_mid  •  AVOID when lower third

### W03.  `H20=H20a AND H60=H60a AND RSI=RSI2 AND session_bucket=london_open`
- Raw: n=124  W=114/L=10  WR=91.9%
- Refine: exclude BBP=BBP1 drops 7/10 losers (70%)
- **Final: n=73  W=70/L=3  WR=95.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 30-40 weak; session=london_open  •  AVOID when just touched lower band

### W04.  `H60=H60a AND BBP=BBP2 AND session_bucket=london_open`
- Raw: n=121  W=105/L=16  WR=86.8%
- Refine: exclude H20=H20e drops 6/16 losers (38%)
- **Final: n=103  W=93/L=10  WR=90.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; lower third; session=london_open  •  AVOID when HTF20 strongly against

### W05.  `H60=H60a AND ZS=ZS1 AND session_bucket=ny_mid`
- Raw: n=120  W=110/L=10  WR=91.7%
- Refine: exclude H20=H20b drops 8/10 losers (80%)
- **Final: n=110  W=108/L=2  WR=98.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; zscore -3 to -2 deep oversold; session=ny_mid  •  AVOID when HTF20 slightly aligned

### W06.  `H60=H60a AND T4=T4c AND session_bucket=london_open`
- Raw: n=120  W=107/L=13  WR=89.2%
- Refine: exclude RSI=RSI2 drops 10/13 losers (77%)
- **Final: n=56  W=53/L=3  WR=94.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=london_open  •  AVOID when RSI 30-40 weak

### W07.  `H60=H60a AND T1=T1c AND session_bucket=london_open`
- Raw: n=117  W=102/L=15  WR=87.2%
- Refine: exclude direction_exec=short drops 4/15 losers (27%)
- **Final: n=110  W=99/L=11  WR=90.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=london_open  •  AVOID when short

### W08.  `H20=H20e AND H60=H60a AND session_bucket=ny_mid`
- Raw: n=117  W=100/L=17  WR=85.5%
- Refine: exclude ZS=ZS2 drops 9/17 losers (53%)
- **Final: n=79  W=71/L=8  WR=89.9%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; session=ny_mid  •  AVOID when zscore -2 to -1 oversold

### W09.  `H20=H20e AND H60=H60a AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=117  W=100/L=17  WR=85.5%
- Refine: exclude ZS=ZS2 drops 9/17 losers (53%)
- **Final: n=79  W=71/L=8  WR=89.9%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 aligned WITH trade; session=ny_mid  •  AVOID when zscore -2 to -1 oversold

### W10.  `H60=H60a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=116  W=105/L=11  WR=90.5%
- Refine: exclude RSI=RSI2 drops 8/11 losers (73%)
- **Final: n=58  W=55/L=3  WR=94.8%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; session=london_open  •  AVOID when RSI 30-40 weak

### W11.  `H60=H60a AND T1=T1a AND RSI=RSI2 AND session_bucket=london_open`
- Raw: n=114  W=100/L=14  WR=87.7%
- Refine: exclude H20=H20e drops 10/14 losers (71%)
- **Final: n=88  W=84/L=4  WR=95.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 30-40 weak; session=london_open  •  AVOID when HTF20 strongly against

### W12.  `H60=H60a AND RSI=RSI2 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=114  W=100/L=14  WR=87.7%
- Refine: exclude H20=H20e drops 10/14 losers (71%)
- **Final: n=88  W=84/L=4  WR=95.5%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; RSI 30-40 weak; session=london_open  •  AVOID when HTF20 strongly against

### W13.  `H20=H20a AND H60=H60a AND RSI=RSI1`
- Raw: n=112  W=96/L=16  WR=85.7%
- Refine: exclude T1=T1a drops 14/16 losers (88%)
- **Final: n=44  W=42/L=2  WR=95.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 20-30 oversold  •  AVOID when 1h trend WITH trade

### W14.  `H20=H20e AND H60=H60a AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=111  W=96/L=15  WR=86.5%
- Refine: exclude ZS=ZS2 drops 8/15 losers (53%)
- **Final: n=74  W=67/L=7  WR=90.5%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 4h trend WITH trade; session=ny_mid  •  AVOID when zscore -2 to -1 oversold

### W15.  `H20=H20a AND BBP=BBP2 AND session_bucket=london_open`
- Raw: n=111  W=95/L=16  WR=85.6%
- Refine: exclude H60=H60b drops 5/16 losers (31%)
- **Final: n=104  W=93/L=11  WR=89.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; lower third; session=london_open  •  AVOID when HTF60 slightly aligned

### W16.  `H60=H60a AND T1=T1c AND direction_exec=long AND session_bucket=london_open`
- Raw: n=110  W=99/L=11  WR=90.0%
- Refine: exclude RSI=RSI2 drops 8/11 losers (73%)
- **Final: n=52  W=49/L=3  WR=94.2%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=london_open  •  AVOID when RSI 30-40 weak

### W17.  `H20=H20a AND BBP=BBP0 AND direction_exec=long`
- Raw: n=109  W=94/L=15  WR=86.2%
- Refine: exclude session_bucket=asia drops 6/15 losers (40%)
- **Final: n=98  W=89/L=9  WR=90.8%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; deep below lower band  •  AVOID when session=asia

### W18.  `H20=H20a AND ZS=ZS2 AND session_bucket=london_open`
- Raw: n=109  W=94/L=15  WR=86.2%
- Refine: exclude H60=H60b drops 5/15 losers (33%)
- **Final: n=103  W=93/L=10  WR=90.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; zscore -2 to -1 oversold; session=london_open  •  AVOID when HTF60 slightly aligned

### W19.  `H20=H20a AND BBP=BBP2 AND ZS=ZS2 AND session_bucket=london_open`
- Raw: n=109  W=94/L=15  WR=86.2%
- Refine: exclude H60=H60b drops 5/15 losers (33%)
- **Final: n=103  W=93/L=10  WR=90.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; lower third; zscore -2 to -1 oversold; session=london_open  •  AVOID when HTF60 slightly aligned

### W20.  `H60=H60a AND ZS=ZS2 AND session_bucket=london_open`
- Raw: n=109  W=93/L=16  WR=85.3%
- Refine: exclude H20=H20e drops 6/16 losers (38%)
- **Final: n=101  W=91/L=10  WR=90.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; zscore -2 to -1 oversold; session=london_open  •  AVOID when HTF20 strongly against

### W21.  `H60=H60a AND BBP=BBP2 AND ZS=ZS2 AND session_bucket=london_open`
- Raw: n=109  W=93/L=16  WR=85.3%
- Refine: exclude H20=H20e drops 6/16 losers (38%)
- **Final: n=101  W=91/L=10  WR=90.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; lower third; zscore -2 to -1 oversold; session=london_open  •  AVOID when HTF20 strongly against

### W22.  `H60=H60a AND T4=T4c AND direction_exec=long AND session_bucket=london_open`
- Raw: n=108  W=97/L=11  WR=89.8%
- Refine: exclude RSI=RSI2 drops 8/11 losers (73%)
- **Final: n=50  W=47/L=3  WR=94.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=london_open  •  AVOID when RSI 30-40 weak

### W23.  `H60=H60a AND T4=T4a AND RSI=RSI2 AND session_bucket=london_open`
- Raw: n=108  W=96/L=12  WR=88.9%
- Refine: exclude H20=H20e drops 8/12 losers (67%)
- **Final: n=88  W=84/L=4  WR=95.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 30-40 weak; session=london_open  •  AVOID when HTF20 strongly against

### W24.  `H20=H20a AND T1=T1c AND BBP=BBP0`
- Raw: n=105  W=90/L=15  WR=85.7%
- Refine: exclude session_bucket=asia drops 6/15 losers (40%)
- **Final: n=94  W=85/L=9  WR=90.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; deep below lower band  •  AVOID when session=asia

### W25.  `H20=H20a AND T4=T4c AND BBP=BBP0`
- Raw: n=105  W=90/L=15  WR=85.7%
- Refine: exclude session_bucket=asia drops 6/15 losers (40%)
- **Final: n=94  W=85/L=9  WR=90.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; deep below lower band  •  AVOID when session=asia

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND H60=H60e AND ZS=ZS1`
- Raw: n=163  W=60/L=103  WR=36.8%
- Sharpen: sharpest is session_bucket=ny_mid (35/103 of losers there)
- **Sharp: n=42  W=7/L=35  WR=16.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; zscore -3 to -2 deep oversold  •  ONLY when session=ny_mid

### L02.  `H20=H20e AND H60=H60e AND session_bucket=london_open`
- Raw: n=158  W=59/L=99  WR=37.3%
- Sharpen: sharpest is RSI=RSI2 (61/99 of losers there)
- **Sharp: n=84  W=23/L=61  WR=27.4%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; session=london_open  •  ONLY when RSI 30-40 weak

### L03.  `H60=H60e AND T1=T1c AND session_bucket=ny_mid`
- Raw: n=145  W=57/L=88  WR=39.3%
- Sharpen: sharpest is RSI=RSI3 (23/88 of losers there)
- **Sharp: n=27  W=4/L=23  WR=14.8%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; session=ny_mid  •  ONLY when RSI 40-50 lower neutral

### L04.  `H20=H20e AND RSI=RSI2 AND session_bucket=london_open`
- Raw: n=131  W=48/L=83  WR=36.6%
- Sharpen: sharpest is T1=T1c (48/83 of losers there)
- **Sharp: n=58  W=10/L=48  WR=17.2%**
- **Dir: ?**  •  HTF20 strongly against; RSI 30-40 weak; session=london_open  •  ONLY when 1h trend AGAINST trade

### L05.  `H20=H20e AND T1=T1a AND session_bucket=london_open`
- Raw: n=131  W=52/L=79  WR=39.7%
- Sharpen: sharpest is RSI=RSI1 (20/79 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; session=london_open  •  ONLY when RSI 20-30 oversold

### L06.  `H20=H20e AND direction_exec=short AND session_bucket=london_open`
- Raw: n=129  W=50/L=79  WR=38.8%
- Sharpen: sharpest is RSI=RSI1 (20/79 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; session=london_open  •  ONLY when RSI 20-30 oversold

### L07.  `H20=H20e AND T1=T1a AND direction_exec=short AND session_bucket=london_open`
- Raw: n=129  W=50/L=79  WR=38.8%
- Sharpen: sharpest is RSI=RSI1 (20/79 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend WITH trade; session=london_open  •  ONLY when RSI 20-30 oversold

### L08.  `H60=H60e AND RSI=RSI2 AND session_bucket=london_open`
- Raw: n=127  W=48/L=79  WR=37.8%
- Sharpen: sharpest is H20=H20e (61/79 of losers there)
- **Sharp: n=84  W=23/L=61  WR=27.4%**
- **Dir: ?**  •  HTF60 strongly against; RSI 30-40 weak; session=london_open  •  ONLY when HTF20 strongly against

### L09.  `H20=H20e AND T4=T4a AND session_bucket=london_open`
- Raw: n=122  W=46/L=76  WR=37.7%
- Sharpen: sharpest is RSI=RSI1 (20/76 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; session=london_open  •  ONLY when RSI 20-30 oversold

### L10.  `H20=H20e AND H60=H60e AND BBP=BBP1`
- Raw: n=120  W=48/L=72  WR=40.0%
- Sharpen: sharpest is session_bucket=ny_mid (20/72 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; just touched lower band  •  ONLY when session=ny_mid

### L11.  `H20=H20e AND H60=H60e AND BBP=BBP1 AND ZS=ZS1`
- Raw: n=120  W=48/L=72  WR=40.0%
- Sharpen: sharpest is session_bucket=ny_mid (20/72 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; just touched lower band; zscore -3 to -2 deep oversold  •  ONLY when session=ny_mid

### L12.  `H20=H20e AND H60=H60e AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=119  W=43/L=76  WR=36.1%
- Sharpen: sharpest is session_bucket=london_open (35/76 of losers there)
- **Sharp: n=41  W=6/L=35  WR=14.6%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when session=london_open

### L13.  `H20=H20e AND T1=T1a AND T4=T4a AND session_bucket=london_open`
- Raw: n=119  W=46/L=73  WR=38.7%
- Sharpen: sharpest is RSI=RSI1 (20/73 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend WITH trade; session=london_open  •  ONLY when RSI 20-30 oversold

### L14.  `H20=H20e AND T4=T4a AND direction_exec=short AND session_bucket=london_open`
- Raw: n=119  W=46/L=73  WR=38.7%
- Sharpen: sharpest is RSI=RSI1 (20/73 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend WITH trade; session=london_open  •  ONLY when RSI 20-30 oversold

### L15.  `H20=H20e AND H60=H60e AND T1=T1c AND ZS=ZS1`
- Raw: n=117  W=43/L=74  WR=36.8%
- Sharpen: sharpest is session_bucket=london_open (38/74 of losers there)
- **Sharp: n=49  W=11/L=38  WR=22.4%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when session=london_open

### L16.  `H20=H20e AND H60=H60e AND ZS=ZS1 AND direction_exec=long`
- Raw: n=114  W=43/L=71  WR=37.7%
- Sharpen: sharpest is session_bucket=london_open (38/71 of losers there)
- **Sharp: n=49  W=11/L=38  WR=22.4%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 strongly against; zscore -3 to -2 deep oversold  •  ONLY when session=london_open

### L17.  `H20=H20e AND direction_exec=long AND session_bucket=london_open`
- Raw: n=112  W=44/L=68  WR=39.3%
- Sharpen: sharpest is RSI=RSI2 (48/68 of losers there)
- **Sharp: n=58  W=10/L=48  WR=17.2%**
- **Dir: LONG**  •  HTF20 strongly against; session=london_open  •  ONLY when RSI 30-40 weak

### L18.  `H20=H20e AND T1=T1c AND session_bucket=london_open`
- Raw: n=110  W=42/L=68  WR=38.2%
- Sharpen: sharpest is RSI=RSI2 (48/68 of losers there)
- **Sharp: n=58  W=10/L=48  WR=17.2%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; session=london_open  •  ONLY when RSI 30-40 weak

### L19.  `H20=H20e AND T1=T1c AND direction_exec=long AND session_bucket=london_open`
- Raw: n=110  W=42/L=68  WR=38.2%
- Sharpen: sharpest is RSI=RSI2 (48/68 of losers there)
- **Sharp: n=58  W=10/L=48  WR=17.2%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade; session=london_open  •  ONLY when RSI 30-40 weak

### L20.  `H20=H20e AND T1=T1c AND T4=T4c AND session_bucket=london_open`
- Raw: n=107  W=42/L=65  WR=39.3%
- Sharpen: sharpest is RSI=RSI2 (48/65 of losers there)
- **Sharp: n=58  W=10/L=48  WR=17.2%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; session=london_open  •  ONLY when RSI 30-40 weak

### L21.  `H20=H20e AND H60=H60e AND T1=T1c AND session_bucket=london_open`
- Raw: n=105  W=42/L=63  WR=40.0%
- Sharpen: sharpest is RSI=RSI2 (48/63 of losers there)
- **Sharp: n=58  W=10/L=48  WR=17.2%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; session=london_open  •  ONLY when RSI 30-40 weak

### L22.  `H20=H20a AND H60=H60e AND session_bucket=ny_mid`
- Raw: n=99  W=36/L=63  WR=36.4%
- Sharpen: sharpest is ZS=ZS3 (13/63 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; session=ny_mid  •  ONLY when zscore -1 to +1 neutral

### L23.  `H20=H20a AND H60=H60e AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=99  W=36/L=63  WR=36.4%
- Sharpen: sharpest is ZS=ZS3 (13/63 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 strongly against; session=ny_mid  •  ONLY when zscore -1 to +1 neutral

### L24.  `H20=H20e AND H60=H60e AND T4=T4c AND ZS=ZS1`
- Raw: n=97  W=33/L=64  WR=34.0%
- Sharpen: sharpest is session_bucket=london_open (38/64 of losers there)
- **Sharp: n=49  W=11/L=38  WR=22.4%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when session=london_open

### L25.  `H20=H20a AND H60=H60e AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=95  W=34/L=61  WR=35.8%
- Sharpen: sharpest is ZS=ZS3 (13/61 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 4h trend AGAINST trade; session=ny_mid  •  ONLY when zscore -1 to +1 neutral

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(51/38) | H20e(38/52) |
| H60 | H60a(46/35) | H60e(37/46) |
| T1 | — | — |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(54/48) | short(46/52) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
