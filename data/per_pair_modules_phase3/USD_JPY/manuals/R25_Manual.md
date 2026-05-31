# USD_JPY — R25 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_3**  (5m ATR >120%)
- **A1 = A1_2**  (1h ATR 4-8x)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50e**  (EMA50 down >0.5x)
- **ADR = ADR5**  (>110% overshoot)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **4,633**  (W=2,606 / L=2,027)  -  WR: **56.2%**

## Session distribution

- asia: n=1086  W=608/L=478  WR=56.0%
- ny_mid: n=995  W=564/L=431  WR=56.7%
- ny_close: n=901  W=530/L=371  WR=58.8%
- london: n=491  W=250/L=241  WR=50.9%
- london_open: n=464  W=265/L=199  WR=57.1%
- ny_open: n=460  W=257/L=203  WR=55.9%
- asia_late: n=170  W=93/L=77  WR=54.7%
- off_hours: n=66  W=39/L=27  WR=59.1%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60e AND T1=T1a AND RSI=RSI1 AND session_bucket=ny_mid`
- Raw: n=106  W=96/L=10  WR=90.6%
- Refine: exclude H20=H20a drops 8/10 losers (80%)
- **Final: n=72  W=70/L=2  WR=97.2%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; RSI 20-30 oversold; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

### W02.  `H60=H60e AND T4=T4a AND RSI=RSI1 AND session_bucket=ny_mid`
- Raw: n=106  W=96/L=10  WR=90.6%
- Refine: exclude H20=H20a drops 8/10 losers (80%)
- **Final: n=72  W=70/L=2  WR=97.2%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; RSI 20-30 oversold; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

### W03.  `H60=H60e AND RSI=RSI1 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=106  W=96/L=10  WR=90.6%
- Refine: exclude H20=H20a drops 8/10 losers (80%)
- **Final: n=72  W=70/L=2  WR=97.2%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 20-30 oversold; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

### W04.  `T1=T1c AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=93  W=81/L=12  WR=87.1%
- Refine: exclude ZS=ZS3 drops 4/12 losers (33%)
- **Final: n=75  W=67/L=8  WR=89.3%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; session=ny_mid  •  AVOID when zscore -1 to +1 neutral

### W05.  `T1=T1c AND T4=T4a AND RSI=RSI3 AND session_bucket=ny_mid`
- Raw: n=93  W=81/L=12  WR=87.1%
- Refine: exclude ZS=ZS3 drops 4/12 losers (33%)
- **Final: n=75  W=67/L=8  WR=89.3%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 40-50 lower neutral; session=ny_mid  •  AVOID when zscore -1 to +1 neutral

### W06.  `H20=H20a AND T1=T1c AND RSI=RSI3 AND session_bucket=ny_mid`
- Raw: n=77  W=68/L=9  WR=88.3%
- Refine: exclude ZS=ZS2 drops 8/9 losers (89%)
- **Final: n=27  W=26/L=1  WR=96.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 40-50 lower neutral; session=ny_mid  •  AVOID when zscore -2 to -1 oversold

### W07.  `H20=H20a AND H60=H60e AND T4=T4c AND session_bucket=asia`
- Raw: n=77  W=67/L=10  WR=87.0%
- Refine: exclude ZS=ZS3 drops 7/10 losers (70%)
- **Final: n=63  W=60/L=3  WR=95.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 4h trend AGAINST trade; session=asia  •  AVOID when zscore -1 to +1 neutral

### W08.  `H20=H20a AND T4=T4c AND direction_exec=short AND session_bucket=asia`
- Raw: n=77  W=67/L=10  WR=87.0%
- Refine: exclude ZS=ZS3 drops 7/10 losers (70%)
- **Final: n=63  W=60/L=3  WR=95.2%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; session=asia  •  AVOID when zscore -1 to +1 neutral

### W09.  `H20=H20a AND T1=T1a AND T4=T4c AND session_bucket=asia`
- Raw: n=72  W=67/L=5  WR=93.1%
- Refine: exclude RSI=RSI2 drops 4/5 losers (80%)
- **Final: n=45  W=44/L=1  WR=97.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade; session=asia  •  AVOID when RSI 30-40 weak

### W10.  `H60=H60a AND T1=T1c AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=72  W=63/L=9  WR=87.5%
- Refine: exclude ZS=ZS2 drops 8/9 losers (89%)
- **Final: n=30  W=29/L=1  WR=96.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; session=ny_mid  •  AVOID when zscore -2 to -1 oversold

### W11.  `T1=T1c AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=68  W=60/L=8  WR=88.2%
- Refine: exclude ZS=ZS2 drops 8/8 losers (100%)
- **Final: n=26  W=26/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; session=ny_mid  •  AVOID when zscore -2 to -1 oversold

### W12.  `H20=H20a AND T1=T1c AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=68  W=60/L=8  WR=88.2%
- Refine: exclude ZS=ZS2 drops 8/8 losers (100%)
- **Final: n=26  W=26/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; session=ny_mid  •  AVOID when zscore -2 to -1 oversold

### W13.  `H20=H20a AND T1=T1c AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=68  W=60/L=8  WR=88.2%
- Refine: exclude ZS=ZS2 drops 8/8 losers (100%)
- **Final: n=26  W=26/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; session=ny_mid  •  AVOID when zscore -2 to -1 oversold

### W14.  `H60=H60a AND T1=T1c AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=68  W=60/L=8  WR=88.2%
- Refine: exclude ZS=ZS2 drops 8/8 losers (100%)
- **Final: n=26  W=26/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=ny_mid  •  AVOID when zscore -2 to -1 oversold

### W15.  `T1=T1c AND T4=T4a AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=68  W=60/L=8  WR=88.2%
- Refine: exclude ZS=ZS2 drops 8/8 losers (100%)
- **Final: n=26  W=26/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend WITH trade; session=ny_mid  •  AVOID when zscore -2 to -1 oversold

### W16.  `T1=T1c AND RSI=RSI3 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=68  W=60/L=8  WR=88.2%
- Refine: exclude ZS=ZS2 drops 8/8 losers (100%)
- **Final: n=26  W=26/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 40-50 lower neutral; session=ny_mid  •  AVOID when zscore -2 to -1 oversold

### W17.  `H20=H20a AND T1=T1c AND BBP=BBP4`
- Raw: n=59  W=51/L=8  WR=86.4%
- Refine: exclude T4=T4c drops 6/8 losers (75%)
- **Final: n=40  W=38/L=2  WR=95.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; upper third  •  AVOID when 4h trend AGAINST trade

### W18.  `T1=T1c AND T4=T4a AND BBP=BBP2 AND session_bucket=ny_mid`
- Raw: n=56  W=48/L=8  WR=85.7%
- Refine: exclude H20=H20a drops 8/8 losers (100%)
- **Final: n=12  W=12/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; lower third; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

### W19.  `T1=T1c AND RSI=RSI3 AND ZS=ZS2 AND session_bucket=london_open`
- Raw: n=56  W=48/L=8  WR=85.7%
- Refine: exclude H60=H60e drops 8/8 losers (100%)
- **Final: n=9  W=9/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold; session=london_open  •  AVOID when HTF60 strongly against

### W20.  `RSI=RSI3 AND ZS=ZS2 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=56  W=48/L=8  WR=85.7%
- Refine: exclude H60=H60e drops 8/8 losers (100%)
- **Final: n=9  W=9/L=0  WR=100.0%**
- **Dir: LONG**  •  RSI 40-50 lower neutral; zscore -2 to -1 oversold; session=london_open  •  AVOID when HTF60 strongly against

### W21.  `H20=H20a AND H60=H60a AND T1=T1c AND BBP=BBP4`
- Raw: n=54  W=48/L=6  WR=88.9%
- Refine: exclude RSI=RSI1 drops 3/6 losers (50%)
- **Final: n=49  W=46/L=3  WR=93.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade; upper third  •  AVOID when RSI 20-30 oversold

### W22.  `H20=H20e AND RSI=RSI3 AND ZS=ZS2 AND session_bucket=london_open`
- Raw: n=54  W=46/L=8  WR=85.2%
- Refine: exclude H60=H60e drops 8/8 losers (100%)
- **Final: n=7  W=7/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; RSI 40-50 lower neutral; zscore -2 to -1 oversold; session=london_open  •  AVOID when HTF60 strongly against

### W23.  `H20=H20a AND T4=T4c AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=50  W=44/L=6  WR=88.0%
- Refine: exclude T1=T1c drops 5/6 losers (83%)
- **Final: n=45  W=44/L=1  WR=97.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral; session=asia  •  AVOID when 1h trend AGAINST trade

### W24.  `T4=T4c AND RSI=RSI3 AND direction_exec=short AND session_bucket=asia`
- Raw: n=50  W=44/L=6  WR=88.0%
- Refine: exclude T1=T1c drops 5/6 losers (83%)
- **Final: n=45  W=44/L=1  WR=97.8%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; session=asia  •  AVOID when 1h trend AGAINST trade

### W25.  `H20=H20a AND T1=T1c AND ZS=ZS4`
- Raw: n=48  W=42/L=6  WR=87.5%
- Refine: exclude RSI=RSI1 drops 3/6 losers (50%)
- **Final: n=43  W=40/L=3  WR=93.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; zscore +1 to +2 overbought  •  AVOID when RSI 20-30 oversold

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1c AND T4=T4c AND RSI=RSI1`
- Raw: n=538  W=210/L=328  WR=39.0%
- Sharpen: sharpest is ZS=ZS1 (111/328 of losers there)
- **Sharp: n=150  W=39/L=111  WR=26.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when zscore -3 to -2 deep oversold

### L02.  `T4=T4c AND RSI=RSI1 AND direction_exec=long`
- Raw: n=538  W=210/L=328  WR=39.0%
- Sharpen: sharpest is ZS=ZS1 (111/328 of losers there)
- **Sharp: n=150  W=39/L=111  WR=26.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when zscore -3 to -2 deep oversold

### L03.  `T1=T1c AND T4=T4c AND RSI=RSI1 AND direction_exec=long`
- Raw: n=538  W=210/L=328  WR=39.0%
- Sharpen: sharpest is ZS=ZS1 (111/328 of losers there)
- **Sharp: n=150  W=39/L=111  WR=26.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when zscore -3 to -2 deep oversold

### L04.  `H20=H20e AND direction_exec=long AND session_bucket=asia`
- Raw: n=417  W=163/L=254  WR=39.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=417  W=163/L=254  WR=39.1%**
- **Dir: LONG**  •  HTF20 strongly against; session=asia

### L05.  `H20=H20e AND T1=T1c AND session_bucket=asia`
- Raw: n=335  W=117/L=218  WR=34.9%
- Sharpen: sharpest is BBP=BBP2 (126/218 of losers there)
- **Sharp: n=172  W=46/L=126  WR=26.7%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; session=asia  •  ONLY when lower third

### L06.  `H20=H20e AND T1=T1c AND direction_exec=long AND session_bucket=asia`
- Raw: n=335  W=117/L=218  WR=34.9%
- Sharpen: sharpest is BBP=BBP2 (126/218 of losers there)
- **Sharp: n=172  W=46/L=126  WR=26.7%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade; session=asia  •  ONLY when lower third

### L07.  `T1=T1c AND T4=T4c AND session_bucket=asia`
- Raw: n=307  W=122/L=185  WR=39.7%
- Sharpen: no sharper sub-pattern
- **Sharp: n=307  W=122/L=185  WR=39.7%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=asia

### L08.  `H20=H20e AND T1=T1c AND T4=T4c AND session_bucket=asia`
- Raw: n=277  W=108/L=169  WR=39.0%
- Sharpen: sharpest is BBP=BBP2 (93/169 of losers there)
- **Sharp: n=135  W=42/L=93  WR=31.1%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; session=asia  •  ONLY when lower third

### L09.  `H20=H20e AND BBP=BBP2 AND RSI=RSI2 AND direction_exec=long`
- Raw: n=276  W=106/L=170  WR=38.4%
- Sharpen: sharpest is session_bucket=asia (101/170 of losers there)
- **Sharp: n=138  W=37/L=101  WR=26.8%**
- **Dir: LONG**  •  HTF20 strongly against; lower third; RSI 30-40 weak  •  ONLY when session=asia

### L10.  `T4=T4c AND BBP=BBP1 AND ZS=ZS1`
- Raw: n=269  W=102/L=167  WR=37.9%
- Sharpen: sharpest is RSI=RSI1 (72/167 of losers there)
- **Sharp: n=90  W=18/L=72  WR=20.0%**
- **Dir: ?**  •  4h trend AGAINST trade; just touched lower band; zscore -3 to -2 deep oversold  •  ONLY when RSI 20-30 oversold

### L11.  `H20=H20e AND RSI=RSI2 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=260  W=102/L=158  WR=39.2%
- Sharpen: sharpest is session_bucket=asia (99/158 of losers there)
- **Sharp: n=136  W=37/L=99  WR=27.2%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 30-40 weak; zscore -2 to -1 oversold  •  ONLY when session=asia

### L12.  `T1=T1c AND BBP=BBP2 AND session_bucket=asia`
- Raw: n=258  W=98/L=160  WR=38.0%
- Sharpen: sharpest is H20=H20e (126/160 of losers there)
- **Sharp: n=172  W=46/L=126  WR=26.7%**
- **Dir: ?**  •  1h trend AGAINST trade; lower third; session=asia  •  ONLY when HTF20 strongly against

### L13.  `H20=H20e AND T1=T1c AND BBP=BBP2 AND RSI=RSI2`
- Raw: n=253  W=100/L=153  WR=39.5%
- Sharpen: sharpest is session_bucket=asia (101/153 of losers there)
- **Sharp: n=138  W=37/L=101  WR=26.8%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; lower third; RSI 30-40 weak  •  ONLY when session=asia

### L14.  `H20=H20e AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=248  W=97/L=151  WR=39.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=248  W=97/L=151  WR=39.1%**
- **Dir: ?**  •  HTF20 strongly against; RSI 30-40 weak; session=asia

### L15.  `T1=T1c AND BBP=BBP2 AND direction_exec=long AND session_bucket=asia`
- Raw: n=248  W=98/L=150  WR=39.5%
- Sharpen: sharpest is H20=H20e (126/150 of losers there)
- **Sharp: n=172  W=46/L=126  WR=26.7%**
- **Dir: LONG**  •  1h trend AGAINST trade; lower third; session=asia  •  ONLY when HTF20 strongly against

### L16.  `H60=H60a AND T4=T4c AND RSI=RSI1`
- Raw: n=242  W=89/L=153  WR=36.8%
- Sharpen: sharpest is session_bucket=ny_mid (73/153 of losers there)
- **Sharp: n=87  W=14/L=73  WR=16.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when session=ny_mid

### L17.  `T1=T1c AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=242  W=89/L=153  WR=36.8%
- Sharpen: sharpest is H20=H20e (122/153 of losers there)
- **Sharp: n=167  W=45/L=122  WR=26.9%**
- **Dir: ?**  •  1h trend AGAINST trade; zscore -2 to -1 oversold; session=asia  •  ONLY when HTF20 strongly against

### L18.  `T1=T1c AND BBP=BBP2 AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=242  W=89/L=153  WR=36.8%
- Sharpen: sharpest is H20=H20e (122/153 of losers there)
- **Sharp: n=167  W=45/L=122  WR=26.9%**
- **Dir: ?**  •  1h trend AGAINST trade; lower third; zscore -2 to -1 oversold; session=asia  •  ONLY when HTF20 strongly against

### L19.  `T1=T1c AND ZS=ZS2 AND direction_exec=long AND session_bucket=asia`
- Raw: n=233  W=89/L=144  WR=38.2%
- Sharpen: sharpest is H20=H20e (122/144 of losers there)
- **Sharp: n=167  W=45/L=122  WR=26.9%**
- **Dir: LONG**  •  1h trend AGAINST trade; zscore -2 to -1 oversold; session=asia  •  ONLY when HTF20 strongly against

### L20.  `T1=T1c AND RSI=RSI1 AND session_bucket=ny_mid`
- Raw: n=225  W=83/L=142  WR=36.9%
- Sharpen: sharpest is H60=H60a (73/142 of losers there)
- **Sharp: n=87  W=14/L=73  WR=16.1%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 20-30 oversold; session=ny_mid  •  ONLY when HTF60 aligned WITH trade

### L21.  `T4=T4c AND RSI=RSI1 AND session_bucket=ny_mid`
- Raw: n=225  W=83/L=142  WR=36.9%
- Sharpen: sharpest is H60=H60a (73/142 of losers there)
- **Sharp: n=87  W=14/L=73  WR=16.1%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 20-30 oversold; session=ny_mid  •  ONLY when HTF60 aligned WITH trade

### L22.  `RSI=RSI1 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=225  W=83/L=142  WR=36.9%
- Sharpen: sharpest is H60=H60a (73/142 of losers there)
- **Sharp: n=87  W=14/L=73  WR=16.1%**
- **Dir: LONG**  •  RSI 20-30 oversold; session=ny_mid  •  ONLY when HTF60 aligned WITH trade

### L23.  `T1=T1c AND T4=T4c AND RSI=RSI1 AND session_bucket=ny_mid`
- Raw: n=225  W=83/L=142  WR=36.9%
- Sharpen: sharpest is H60=H60a (73/142 of losers there)
- **Sharp: n=87  W=14/L=73  WR=16.1%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 20-30 oversold; session=ny_mid  •  ONLY when HTF60 aligned WITH trade

### L24.  `T1=T1c AND RSI=RSI1 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=225  W=83/L=142  WR=36.9%
- Sharpen: sharpest is H60=H60a (73/142 of losers there)
- **Sharp: n=87  W=14/L=73  WR=16.1%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 20-30 oversold; session=ny_mid  •  ONLY when HTF60 aligned WITH trade

### L25.  `T4=T4c AND RSI=RSI1 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=225  W=83/L=142  WR=36.9%
- Sharpen: sharpest is H60=H60a (73/142 of losers there)
- **Sharp: n=87  W=14/L=73  WR=16.1%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 20-30 oversold; session=ny_mid  •  ONLY when HTF60 aligned WITH trade

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(46/35) | H20e(36/48) |
| H60 | — | — |
| T1 | T1a(54/45) | T1c(46/55) |
| T4 | T4a(55/43) | T4c(45/57) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(57/42) | long(43/58) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
