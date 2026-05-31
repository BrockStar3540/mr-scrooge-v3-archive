# USD_CAD — R37 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20d**  (EMA20 down 0.15-0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **2,820**  (W=1,817 / L=1,003)  -  WR: **64.4%**

## Session distribution

- ny_mid: n=558  W=346/L=212  WR=62.0%
- asia: n=549  W=358/L=191  WR=65.2%
- ny_open: n=523  W=344/L=179  WR=65.8%
- ny_close: n=344  W=213/L=131  WR=61.9%
- london_open: n=339  W=219/L=120  WR=64.6%
- london: n=298  W=195/L=103  WR=65.4%
- asia_late: n=135  W=90/L=45  WR=66.7%
- off_hours: n=74  W=52/L=22  WR=70.3%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1a AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=246  W=210/L=36  WR=85.4%
- Refine: exclude H20=H20a drops 33/36 losers (92%)
- **Final: n=80  W=77/L=3  WR=96.2%**
- **Dir: SHORT**  •  1h trend WITH trade; session=ny_open  •  AVOID when HTF20 aligned WITH trade

### W02.  `T1=T1a AND T4=T4a AND session_bucket=ny_open`
- Raw: n=240  W=206/L=34  WR=85.8%
- Refine: exclude H20=H20a drops 33/34 losers (97%)
- **Final: n=74  W=73/L=1  WR=98.6%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; session=ny_open  •  AVOID when HTF20 aligned WITH trade

### W03.  `T1=T1a AND T4=T4a AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=240  W=206/L=34  WR=85.8%
- Refine: exclude H20=H20a drops 33/34 losers (97%)
- **Final: n=74  W=73/L=1  WR=98.6%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend WITH trade; session=ny_open  •  AVOID when HTF20 aligned WITH trade

### W04.  `T4=T4a AND RSI=RSI2 AND session_bucket=ny_open`
- Raw: n=236  W=205/L=31  WR=86.9%
- Refine: exclude H20=H20a drops 30/31 losers (97%)
- **Final: n=74  W=73/L=1  WR=98.6%**
- **Dir: ?**  •  4h trend WITH trade; RSI 30-40 weak; session=ny_open  •  AVOID when HTF20 aligned WITH trade

### W05.  `RSI=RSI2 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=236  W=205/L=31  WR=86.9%
- Refine: exclude H20=H20a drops 30/31 losers (97%)
- **Final: n=74  W=73/L=1  WR=98.6%**
- **Dir: SHORT**  •  RSI 30-40 weak; session=ny_open  •  AVOID when HTF20 aligned WITH trade

### W06.  `T4=T4a AND RSI=RSI2 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=236  W=205/L=31  WR=86.9%
- Refine: exclude H20=H20a drops 30/31 losers (97%)
- **Final: n=74  W=73/L=1  WR=98.6%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 30-40 weak; session=ny_open  •  AVOID when HTF20 aligned WITH trade

### W07.  `T1=T1a AND RSI=RSI2 AND session_bucket=ny_open`
- Raw: n=231  W=198/L=33  WR=85.7%
- Refine: exclude H20=H20a drops 30/33 losers (91%)
- **Final: n=76  W=73/L=3  WR=96.1%**
- **Dir: ?**  •  1h trend WITH trade; RSI 30-40 weak; session=ny_open  •  AVOID when HTF20 aligned WITH trade

### W08.  `T1=T1a AND T4=T4a AND RSI=RSI2 AND session_bucket=ny_open`
- Raw: n=229  W=198/L=31  WR=86.5%
- Refine: exclude H20=H20a drops 30/31 losers (97%)
- **Final: n=74  W=73/L=1  WR=98.6%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 30-40 weak; session=ny_open  •  AVOID when HTF20 aligned WITH trade

### W09.  `T1=T1a AND RSI=RSI2 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=229  W=198/L=31  WR=86.5%
- Refine: exclude H20=H20a drops 30/31 losers (97%)
- **Final: n=74  W=73/L=1  WR=98.6%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 30-40 weak; session=ny_open  •  AVOID when HTF20 aligned WITH trade

### W10.  `H60=H60a AND T4=T4a AND session_bucket=ny_open`
- Raw: n=180  W=158/L=22  WR=87.8%
- Refine: exclude RSI=RSI3 drops 8/22 losers (36%)
- **Final: n=143  W=129/L=14  WR=90.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; session=ny_open  •  AVOID when RSI 40-50 lower neutral

### W11.  `H60=H60a AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=180  W=158/L=22  WR=87.8%
- Refine: exclude RSI=RSI3 drops 8/22 losers (36%)
- **Final: n=143  W=129/L=14  WR=90.2%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; session=ny_open  •  AVOID when RSI 40-50 lower neutral

### W12.  `H60=H60a AND T4=T4a AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=180  W=158/L=22  WR=87.8%
- Refine: exclude RSI=RSI3 drops 8/22 losers (36%)
- **Final: n=143  W=129/L=14  WR=90.2%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend WITH trade; session=ny_open  •  AVOID when RSI 40-50 lower neutral

### W13.  `H60=H60a AND T1=T1a AND session_bucket=ny_open`
- Raw: n=154  W=137/L=17  WR=89.0%
- Refine: exclude H20=H20a drops 16/17 losers (94%)
- **Final: n=48  W=47/L=1  WR=97.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=ny_open  •  AVOID when HTF20 aligned WITH trade

### W14.  `H60=H60a AND T1=T1a AND T4=T4a AND session_bucket=ny_open`
- Raw: n=154  W=137/L=17  WR=89.0%
- Refine: exclude H20=H20a drops 16/17 losers (94%)
- **Final: n=48  W=47/L=1  WR=97.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; session=ny_open  •  AVOID when HTF20 aligned WITH trade

### W15.  `H60=H60a AND T1=T1a AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=154  W=137/L=17  WR=89.0%
- Refine: exclude H20=H20a drops 16/17 losers (94%)
- **Final: n=48  W=47/L=1  WR=97.9%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=ny_open  •  AVOID when HTF20 aligned WITH trade

### W16.  `T4=T4a AND direction_exec=short AND session_bucket=london`
- Raw: n=145  W=135/L=10  WR=93.1%
- Refine: exclude RSI=RSI3 drops 8/10 losers (80%)
- **Final: n=98  W=96/L=2  WR=98.0%**
- **Dir: SHORT**  •  4h trend WITH trade; session=london  •  AVOID when RSI 40-50 lower neutral

### W17.  `H60=H60a AND T1=T1a AND RSI=RSI2 AND session_bucket=ny_open`
- Raw: n=143  W=129/L=14  WR=90.2%
- Refine: exclude H20=H20a drops 13/14 losers (93%)
- **Final: n=48  W=47/L=1  WR=97.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 30-40 weak; session=ny_open  •  AVOID when HTF20 aligned WITH trade

### W18.  `H60=H60a AND T4=T4a AND RSI=RSI2 AND session_bucket=ny_open`
- Raw: n=143  W=129/L=14  WR=90.2%
- Refine: exclude H20=H20a drops 13/14 losers (93%)
- **Final: n=48  W=47/L=1  WR=97.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 30-40 weak; session=ny_open  •  AVOID when HTF20 aligned WITH trade

### W19.  `H60=H60a AND RSI=RSI2 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=143  W=129/L=14  WR=90.2%
- Refine: exclude H20=H20a drops 13/14 losers (93%)
- **Final: n=48  W=47/L=1  WR=97.9%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; RSI 30-40 weak; session=ny_open  •  AVOID when HTF20 aligned WITH trade

### W20.  `T1=T1a AND direction_exec=short AND session_bucket=london`
- Raw: n=136  W=124/L=12  WR=91.2%
- Refine: exclude ZS=ZS3 drops 8/12 losers (67%)
- **Final: n=110  W=106/L=4  WR=96.4%**
- **Dir: SHORT**  •  1h trend WITH trade; session=london  •  AVOID when zscore -1 to +1 neutral

### W21.  `H20=H20a AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=135  W=120/L=15  WR=88.9%
- Refine: exclude H60=H60e drops 13/15 losers (87%)
- **Final: n=55  W=53/L=2  WR=96.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 30-40 weak; session=asia  •  AVOID when HTF60 strongly against

### W22.  `T1=T1a AND T4=T4a AND session_bucket=london`
- Raw: n=122  W=112/L=10  WR=91.8%
- Refine: exclude RSI=RSI3 drops 8/10 losers (80%)
- **Final: n=94  W=92/L=2  WR=97.9%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; session=london  •  AVOID when RSI 40-50 lower neutral

### W23.  `BBP=BBP2 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=122  W=104/L=18  WR=85.2%
- Refine: exclude H20=H20a drops 14/18 losers (78%)
- **Final: n=66  W=62/L=4  WR=93.9%**
- **Dir: SHORT**  •  lower third; session=ny_open  •  AVOID when HTF20 aligned WITH trade

### W24.  `T4=T4a AND BBP=BBP2 AND session_bucket=ny_open`
- Raw: n=120  W=103/L=17  WR=85.8%
- Refine: exclude H20=H20a drops 15/17 losers (88%)
- **Final: n=62  W=60/L=2  WR=96.8%**
- **Dir: ?**  •  4h trend WITH trade; lower third; session=ny_open  •  AVOID when HTF20 aligned WITH trade

### W25.  `T4=T4a AND BBP=BBP2 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=118  W=102/L=16  WR=86.4%
- Refine: exclude H20=H20a drops 14/16 losers (88%)
- **Final: n=62  W=60/L=2  WR=96.8%**
- **Dir: SHORT**  •  4h trend WITH trade; lower third; session=ny_open  •  AVOID when HTF20 aligned WITH trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T4=T4c AND RSI=RSI2 AND session_bucket=ny_open`
- Raw: n=177  W=70/L=107  WR=39.5%
- Sharpen: sharpest is H20=H20d (27/107 of losers there)
- **Sharp: n=27  W=0/L=27  WR=0.0%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 30-40 weak; session=ny_open  •  ONLY when HTF20 mildly against

### L02.  `RSI=RSI2 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=177  W=70/L=107  WR=39.5%
- Sharpen: sharpest is H20=H20d (27/107 of losers there)
- **Sharp: n=27  W=0/L=27  WR=0.0%**
- **Dir: LONG**  •  RSI 30-40 weak; session=ny_open  •  ONLY when HTF20 mildly against

### L03.  `T4=T4c AND RSI=RSI2 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=177  W=70/L=107  WR=39.5%
- Sharpen: sharpest is H20=H20d (27/107 of losers there)
- **Sharp: n=27  W=0/L=27  WR=0.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 30-40 weak; session=ny_open  •  ONLY when HTF20 mildly against

### L04.  `T1=T1c AND T4=T4c AND RSI=RSI2 AND session_bucket=ny_open`
- Raw: n=175  W=70/L=105  WR=40.0%
- Sharpen: sharpest is H20=H20d (27/105 of losers there)
- **Sharp: n=27  W=0/L=27  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 30-40 weak; session=ny_open  •  ONLY when HTF20 mildly against

### L05.  `T1=T1c AND RSI=RSI2 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=175  W=70/L=105  WR=40.0%
- Sharpen: sharpest is H20=H20d (27/105 of losers there)
- **Sharp: n=27  W=0/L=27  WR=0.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 30-40 weak; session=ny_open  •  ONLY when HTF20 mildly against

### L06.  `T4=T4c AND ZS=ZS4 AND direction_exec=long`
- Raw: n=150  W=60/L=90  WR=40.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=150  W=60/L=90  WR=40.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; zscore +1 to +2 overbought

### L07.  `T4=T4c AND BBP=BBP4 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=150  W=60/L=90  WR=40.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=150  W=60/L=90  WR=40.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; upper third; zscore +1 to +2 overbought

### L08.  `T4=T4c AND direction_exec=long AND session_bucket=london`
- Raw: n=116  W=37/L=79  WR=31.9%
- Sharpen: sharpest is RSI=RSI2 (47/79 of losers there)
- **Sharp: n=58  W=11/L=47  WR=19.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; session=london  •  ONLY when RSI 30-40 weak

### L09.  `H20=H20e AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=108  W=41/L=67  WR=38.0%
- Sharpen: sharpest is T4=T4a (43/67 of losers there)
- **Sharp: n=61  W=18/L=43  WR=29.5%**
- **Dir: ?**  •  HTF20 strongly against; RSI 30-40 weak; session=asia  •  ONLY when 4h trend WITH trade

### L10.  `H60=H60e AND T1=T1c AND RSI=RSI2 AND session_bucket=ny_open`
- Raw: n=105  W=38/L=67  WR=36.2%
- Sharpen: sharpest is BBP=BBP0 (20/67 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 30-40 weak; session=ny_open  •  ONLY when deep below lower band

### L11.  `H60=H60e AND T4=T4c AND RSI=RSI2 AND session_bucket=ny_open`
- Raw: n=105  W=38/L=67  WR=36.2%
- Sharpen: sharpest is BBP=BBP0 (20/67 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 30-40 weak; session=ny_open  •  ONLY when deep below lower band

### L12.  `H60=H60e AND RSI=RSI2 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=105  W=38/L=67  WR=36.2%
- Sharpen: sharpest is BBP=BBP0 (20/67 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: LONG**  •  HTF60 strongly against; RSI 30-40 weak; session=ny_open  •  ONLY when deep below lower band

### L13.  `T1=T1c AND direction_exec=long AND session_bucket=london`
- Raw: n=103  W=36/L=67  WR=35.0%
- Sharpen: sharpest is RSI=RSI2 (52/67 of losers there)
- **Sharp: n=66  W=14/L=52  WR=21.2%**
- **Dir: LONG**  •  1h trend AGAINST trade; session=london  •  ONLY when RSI 30-40 weak

### L14.  `T1=T1c AND T4=T4c AND session_bucket=london`
- Raw: n=96  W=35/L=61  WR=36.5%
- Sharpen: sharpest is RSI=RSI2 (46/61 of losers there)
- **Sharp: n=57  W=11/L=46  WR=19.3%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=london  •  ONLY when RSI 30-40 weak

### L15.  `T1=T1c AND T4=T4c AND direction_exec=long AND session_bucket=london`
- Raw: n=94  W=33/L=61  WR=35.1%
- Sharpen: sharpest is RSI=RSI2 (46/61 of losers there)
- **Sharp: n=57  W=11/L=46  WR=19.3%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=london  •  ONLY when RSI 30-40 weak

### L16.  `H20=H20e AND BBP=BBP4 AND RSI=RSI3`
- Raw: n=93  W=37/L=56  WR=39.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=93  W=37/L=56  WR=39.8%**
- **Dir: ?**  •  HTF20 strongly against; upper third; RSI 40-50 lower neutral

### L17.  `H20=H20e AND ZS=ZS4 AND direction_exec=long`
- Raw: n=86  W=31/L=55  WR=36.0%
- Sharpen: sharpest is H60=H60e (22/55 of losers there)
- **Sharp: n=27  W=5/L=22  WR=18.5%**
- **Dir: LONG**  •  HTF20 strongly against; zscore +1 to +2 overbought  •  ONLY when HTF60 strongly against

### L18.  `H20=H20e AND BBP=BBP4 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=86  W=31/L=55  WR=36.0%
- Sharpen: sharpest is H60=H60e (22/55 of losers there)
- **Sharp: n=27  W=5/L=22  WR=18.5%**
- **Dir: LONG**  •  HTF20 strongly against; upper third; zscore +1 to +2 overbought  •  ONLY when HTF60 strongly against

### L19.  `H20=H20e AND T4=T4c AND ZS=ZS4`
- Raw: n=86  W=32/L=54  WR=37.2%
- Sharpen: sharpest is H60=H60e (21/54 of losers there)
- **Sharp: n=25  W=4/L=21  WR=16.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  ONLY when HTF60 strongly against

### L20.  `H20=H20e AND T4=T4c AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=86  W=32/L=54  WR=37.2%
- Sharpen: sharpest is H60=H60e (21/54 of losers there)
- **Sharp: n=25  W=4/L=21  WR=16.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; upper third; zscore +1 to +2 overbought  •  ONLY when HTF60 strongly against

### L21.  `H20=H20e AND T4=T4a AND session_bucket=asia`
- Raw: n=83  W=28/L=55  WR=33.7%
- Sharpen: sharpest is ZS=ZS1 (22/55 of losers there)
- **Sharp: n=26  W=4/L=22  WR=15.4%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; session=asia  •  ONLY when zscore -3 to -2 deep oversold

### L22.  `H20=H20e AND T1=T1c AND BBP=BBP4`
- Raw: n=81  W=29/L=52  WR=35.8%
- Sharpen: sharpest is H60=H60e (24/52 of losers there)
- **Sharp: n=31  W=7/L=24  WR=22.6%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; upper third  •  ONLY when HTF60 strongly against

### L23.  `H20=H20e AND T1=T1c AND BBP=BBP4 AND direction_exec=long`
- Raw: n=81  W=29/L=52  WR=35.8%
- Sharpen: sharpest is H60=H60e (24/52 of losers there)
- **Sharp: n=31  W=7/L=24  WR=22.6%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade; upper third  •  ONLY when HTF60 strongly against

### L24.  `T1=T1a AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=81  W=30/L=51  WR=37.0%
- Sharpen: sharpest is T4=T4a (35/51 of losers there)
- **Sharp: n=48  W=13/L=35  WR=27.1%**
- **Dir: ?**  •  1h trend WITH trade; lower third; RSI 40-50 lower neutral  •  ONLY when 4h trend WITH trade

### L25.  `H20=H20e AND T4=T4c AND ZS=ZS4 AND direction_exec=long`
- Raw: n=80  W=29/L=51  WR=36.2%
- Sharpen: sharpest is H60=H60e (21/51 of losers there)
- **Sharp: n=25  W=4/L=21  WR=16.0%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  ONLY when HTF60 strongly against

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(38/31) | H20e(33/38) |
| H60 | H60a(41/33) | H60e(37/44) |
| T1 | T1a(53/45) | T1c(47/55) |
| T4 | T4a(55/43) | T4c(45/57) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(55/43) | long(45/57) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
