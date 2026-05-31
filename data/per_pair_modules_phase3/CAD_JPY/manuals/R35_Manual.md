# CAD_JPY — R35 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **4,325**  (W=2,764 / L=1,561)  -  WR: **63.9%**

## Session distribution

- ny_mid: n=919  W=575/L=344  WR=62.6%
- asia: n=906  W=572/L=334  WR=63.1%
- london_open: n=732  W=491/L=241  WR=67.1%
- ny_close: n=594  W=372/L=222  WR=62.6%
- ny_open: n=531  W=330/L=201  WR=62.1%
- london: n=395  W=257/L=138  WR=65.1%
- asia_late: n=197  W=127/L=70  WR=64.5%
- off_hours: n=51  W=40/L=11  WR=78.4%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60a AND T4=T4a AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=230  W=197/L=33  WR=85.7%
- Refine: exclude session_bucket=ny_mid drops 15/33 losers (45%)
- **Final: n=196  W=178/L=18  WR=90.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; deep above upper band; zscore +2 to +3 deep overbought  •  AVOID when session=ny_mid

### W02.  `T1=T1a AND T4=T4a AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=230  W=197/L=33  WR=85.7%
- Refine: exclude session_bucket=ny_mid drops 15/33 losers (45%)
- **Final: n=196  W=178/L=18  WR=90.8%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; deep above upper band; zscore +2 to +3 deep overbought  •  AVOID when session=ny_mid

### W03.  `T4=T4a AND BBP=BBP6 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=230  W=197/L=33  WR=85.7%
- Refine: exclude session_bucket=ny_mid drops 15/33 losers (45%)
- **Final: n=196  W=178/L=18  WR=90.8%**
- **Dir: LONG**  •  4h trend WITH trade; deep above upper band; zscore +2 to +3 deep overbought  •  AVOID when session=ny_mid

### W04.  `H60=H60a AND RSI=RSI6 AND session_bucket=asia`
- Raw: n=185  W=182/L=3  WR=98.4%
- Refine: exclude ZS=ZS3 drops 2/3 losers (67%)
- **Final: n=179  W=178/L=1  WR=99.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 70-80 overbought; session=asia  •  AVOID when zscore -1 to +1 neutral

### W05.  `T1=T1a AND RSI=RSI6 AND session_bucket=asia`
- Raw: n=185  W=182/L=3  WR=98.4%
- Refine: exclude ZS=ZS3 drops 2/3 losers (67%)
- **Final: n=179  W=178/L=1  WR=99.4%**
- **Dir: ?**  •  1h trend WITH trade; RSI 70-80 overbought; session=asia  •  AVOID when zscore -1 to +1 neutral

### W06.  `T4=T4a AND RSI=RSI6 AND session_bucket=asia`
- Raw: n=185  W=182/L=3  WR=98.4%
- Refine: exclude ZS=ZS3 drops 2/3 losers (67%)
- **Final: n=179  W=178/L=1  WR=99.4%**
- **Dir: ?**  •  4h trend WITH trade; RSI 70-80 overbought; session=asia  •  AVOID when zscore -1 to +1 neutral

### W07.  `RSI=RSI6 AND direction_exec=long AND session_bucket=asia`
- Raw: n=185  W=182/L=3  WR=98.4%
- Refine: exclude ZS=ZS3 drops 2/3 losers (67%)
- **Final: n=179  W=178/L=1  WR=99.4%**
- **Dir: LONG**  •  RSI 70-80 overbought; session=asia  •  AVOID when zscore -1 to +1 neutral

### W08.  `H60=H60a AND T1=T1a AND RSI=RSI6 AND session_bucket=asia`
- Raw: n=185  W=182/L=3  WR=98.4%
- Refine: exclude ZS=ZS3 drops 2/3 losers (67%)
- **Final: n=179  W=178/L=1  WR=99.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 70-80 overbought; session=asia  •  AVOID when zscore -1 to +1 neutral

### W09.  `H60=H60a AND T4=T4a AND RSI=RSI6 AND session_bucket=asia`
- Raw: n=185  W=182/L=3  WR=98.4%
- Refine: exclude ZS=ZS3 drops 2/3 losers (67%)
- **Final: n=179  W=178/L=1  WR=99.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 70-80 overbought; session=asia  •  AVOID when zscore -1 to +1 neutral

### W10.  `H60=H60a AND RSI=RSI6 AND direction_exec=long AND session_bucket=asia`
- Raw: n=185  W=182/L=3  WR=98.4%
- Refine: exclude ZS=ZS3 drops 2/3 losers (67%)
- **Final: n=179  W=178/L=1  WR=99.4%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 70-80 overbought; session=asia  •  AVOID when zscore -1 to +1 neutral

### W11.  `T1=T1a AND T4=T4a AND RSI=RSI6 AND session_bucket=asia`
- Raw: n=185  W=182/L=3  WR=98.4%
- Refine: exclude ZS=ZS3 drops 2/3 losers (67%)
- **Final: n=179  W=178/L=1  WR=99.4%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 70-80 overbought; session=asia  •  AVOID when zscore -1 to +1 neutral

### W12.  `T1=T1a AND RSI=RSI6 AND direction_exec=long AND session_bucket=asia`
- Raw: n=185  W=182/L=3  WR=98.4%
- Refine: exclude ZS=ZS3 drops 2/3 losers (67%)
- **Final: n=179  W=178/L=1  WR=99.4%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 70-80 overbought; session=asia  •  AVOID when zscore -1 to +1 neutral

### W13.  `T4=T4a AND RSI=RSI6 AND direction_exec=long AND session_bucket=asia`
- Raw: n=185  W=182/L=3  WR=98.4%
- Refine: exclude ZS=ZS3 drops 2/3 losers (67%)
- **Final: n=179  W=178/L=1  WR=99.4%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 70-80 overbought; session=asia  •  AVOID when zscore -1 to +1 neutral

### W14.  `H60=H60a AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=177  W=164/L=13  WR=92.7%
- Refine: exclude H20=H20c drops 8/13 losers (62%)
- **Final: n=167  W=162/L=5  WR=97.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; zscore +2 to +3 deep overbought; session=asia  •  AVOID when HTF20 neutral

### W15.  `T1=T1a AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=177  W=164/L=13  WR=92.7%
- Refine: exclude H20=H20c drops 8/13 losers (62%)
- **Final: n=167  W=162/L=5  WR=97.0%**
- **Dir: ?**  •  1h trend WITH trade; zscore +2 to +3 deep overbought; session=asia  •  AVOID when HTF20 neutral

### W16.  `ZS=ZS5 AND direction_exec=long AND session_bucket=asia`
- Raw: n=177  W=164/L=13  WR=92.7%
- Refine: exclude H20=H20c drops 8/13 losers (62%)
- **Final: n=167  W=162/L=5  WR=97.0%**
- **Dir: LONG**  •  zscore +2 to +3 deep overbought; session=asia  •  AVOID when HTF20 neutral

### W17.  `H60=H60a AND T1=T1a AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=177  W=164/L=13  WR=92.7%
- Refine: exclude H20=H20c drops 8/13 losers (62%)
- **Final: n=167  W=162/L=5  WR=97.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; zscore +2 to +3 deep overbought; session=asia  •  AVOID when HTF20 neutral

### W18.  `H60=H60a AND ZS=ZS5 AND direction_exec=long AND session_bucket=asia`
- Raw: n=177  W=164/L=13  WR=92.7%
- Refine: exclude H20=H20c drops 8/13 losers (62%)
- **Final: n=167  W=162/L=5  WR=97.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; zscore +2 to +3 deep overbought; session=asia  •  AVOID when HTF20 neutral

### W19.  `T1=T1a AND ZS=ZS5 AND direction_exec=long AND session_bucket=asia`
- Raw: n=177  W=164/L=13  WR=92.7%
- Refine: exclude H20=H20c drops 8/13 losers (62%)
- **Final: n=167  W=162/L=5  WR=97.0%**
- **Dir: LONG**  •  1h trend WITH trade; zscore +2 to +3 deep overbought; session=asia  •  AVOID when HTF20 neutral

### W20.  `T4=T4a AND BBP=BBP6 AND RSI=RSI6`
- Raw: n=171  W=155/L=16  WR=90.6%
- Refine: exclude session_bucket=ny_close drops 6/16 losers (38%)
- **Final: n=165  W=155/L=10  WR=93.9%**
- **Dir: ?**  •  4h trend WITH trade; deep above upper band; RSI 70-80 overbought  •  AVOID when session=ny_close

### W21.  `H20=H20a AND T4=T4a AND session_bucket=london`
- Raw: n=171  W=147/L=24  WR=86.0%
- Refine: exclude ZS=ZS3 drops 7/24 losers (29%)
- **Final: n=153  W=136/L=17  WR=88.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=london  •  AVOID when zscore -1 to +1 neutral

### W22.  `H60=H60a AND BBP=BBP6 AND RSI=RSI6`
- Raw: n=168  W=153/L=15  WR=91.1%
- Refine: exclude session_bucket=ny_close drops 6/15 losers (40%)
- **Final: n=162  W=153/L=9  WR=94.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; deep above upper band; RSI 70-80 overbought  •  AVOID when session=ny_close

### W23.  `T1=T1a AND BBP=BBP6 AND RSI=RSI6`
- Raw: n=168  W=153/L=15  WR=91.1%
- Refine: exclude session_bucket=ny_close drops 6/15 losers (40%)
- **Final: n=162  W=153/L=9  WR=94.4%**
- **Dir: ?**  •  1h trend WITH trade; deep above upper band; RSI 70-80 overbought  •  AVOID when session=ny_close

### W24.  `BBP=BBP6 AND RSI=RSI6 AND direction_exec=long`
- Raw: n=168  W=153/L=15  WR=91.1%
- Refine: exclude session_bucket=ny_close drops 6/15 losers (40%)
- **Final: n=162  W=153/L=9  WR=94.4%**
- **Dir: LONG**  •  deep above upper band; RSI 70-80 overbought  •  AVOID when session=ny_close

### W25.  `H60=H60a AND T1=T1a AND BBP=BBP6 AND RSI=RSI6`
- Raw: n=168  W=153/L=15  WR=91.1%
- Refine: exclude session_bucket=ny_close drops 6/15 losers (40%)
- **Final: n=162  W=153/L=9  WR=94.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; deep above upper band; RSI 70-80 overbought  •  AVOID when session=ny_close

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND T4=T4c AND RSI=RSI6 AND ZS=ZS5`
- Raw: n=193  W=74/L=119  WR=38.3%
- Sharpen: sharpest is session_bucket=asia (39/119 of losers there)
- **Sharp: n=39  W=0/L=39  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 70-80 overbought; zscore +2 to +3 deep overbought  •  ONLY when session=asia

### L02.  `T1=T1c AND T4=T4c AND RSI=RSI6 AND ZS=ZS5`
- Raw: n=193  W=74/L=119  WR=38.3%
- Sharpen: sharpest is session_bucket=asia (39/119 of losers there)
- **Sharp: n=39  W=0/L=39  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 70-80 overbought; zscore +2 to +3 deep overbought  •  ONLY when session=asia

### L03.  `T4=T4c AND RSI=RSI6 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=193  W=74/L=119  WR=38.3%
- Sharpen: sharpest is session_bucket=asia (39/119 of losers there)
- **Sharp: n=39  W=0/L=39  WR=0.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 70-80 overbought; zscore +2 to +3 deep overbought  •  ONLY when session=asia

### L04.  `T4=T4c AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=128  W=51/L=77  WR=39.8%
- Sharpen: sharpest is RSI=RSI6 (39/77 of losers there)
- **Sharp: n=39  W=0/L=39  WR=0.0%**
- **Dir: ?**  •  4h trend AGAINST trade; zscore +2 to +3 deep overbought; session=asia  •  ONLY when RSI 70-80 overbought

### L05.  `H60=H60e AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=123  W=33/L=90  WR=26.8%
- Sharpen: sharpest is BBP=BBP6 (56/90 of losers there)
- **Sharp: n=60  W=4/L=56  WR=6.7%**
- **Dir: ?**  •  HTF60 strongly against; zscore +2 to +3 deep overbought; session=asia  •  ONLY when deep above upper band

### L06.  `T1=T1c AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=123  W=33/L=90  WR=26.8%
- Sharpen: sharpest is BBP=BBP6 (56/90 of losers there)
- **Sharp: n=60  W=4/L=56  WR=6.7%**
- **Dir: ?**  •  1h trend AGAINST trade; zscore +2 to +3 deep overbought; session=asia  •  ONLY when deep above upper band

### L07.  `ZS=ZS5 AND direction_exec=short AND session_bucket=asia`
- Raw: n=123  W=33/L=90  WR=26.8%
- Sharpen: sharpest is BBP=BBP6 (56/90 of losers there)
- **Sharp: n=60  W=4/L=56  WR=6.7%**
- **Dir: SHORT**  •  zscore +2 to +3 deep overbought; session=asia  •  ONLY when deep above upper band

### L08.  `H60=H60e AND T1=T1c AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=123  W=33/L=90  WR=26.8%
- Sharpen: sharpest is BBP=BBP6 (56/90 of losers there)
- **Sharp: n=60  W=4/L=56  WR=6.7%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; zscore +2 to +3 deep overbought; session=asia  •  ONLY when deep above upper band

### L09.  `H60=H60e AND ZS=ZS5 AND direction_exec=short AND session_bucket=asia`
- Raw: n=123  W=33/L=90  WR=26.8%
- Sharpen: sharpest is BBP=BBP6 (56/90 of losers there)
- **Sharp: n=60  W=4/L=56  WR=6.7%**
- **Dir: SHORT**  •  HTF60 strongly against; zscore +2 to +3 deep overbought; session=asia  •  ONLY when deep above upper band

### L10.  `T1=T1c AND ZS=ZS5 AND direction_exec=short AND session_bucket=asia`
- Raw: n=123  W=33/L=90  WR=26.8%
- Sharpen: sharpest is BBP=BBP6 (56/90 of losers there)
- **Sharp: n=60  W=4/L=56  WR=6.7%**
- **Dir: SHORT**  •  1h trend AGAINST trade; zscore +2 to +3 deep overbought; session=asia  •  ONLY when deep above upper band

### L11.  `H60=H60e AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=115  W=43/L=72  WR=37.4%
- Sharpen: sharpest is H20=H20a (35/72 of losers there)
- **Sharp: n=45  W=10/L=35  WR=22.2%**
- **Dir: ?**  •  HTF60 strongly against; RSI 70-80 overbought; session=ny_mid  •  ONLY when HTF20 aligned WITH trade

### L12.  `T1=T1c AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=115  W=43/L=72  WR=37.4%
- Sharpen: sharpest is H20=H20a (35/72 of losers there)
- **Sharp: n=45  W=10/L=35  WR=22.2%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 70-80 overbought; session=ny_mid  •  ONLY when HTF20 aligned WITH trade

### L13.  `T4=T4c AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=115  W=43/L=72  WR=37.4%
- Sharpen: sharpest is H20=H20a (35/72 of losers there)
- **Sharp: n=45  W=10/L=35  WR=22.2%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 70-80 overbought; session=ny_mid  •  ONLY when HTF20 aligned WITH trade

### L14.  `RSI=RSI6 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=115  W=43/L=72  WR=37.4%
- Sharpen: sharpest is H20=H20a (35/72 of losers there)
- **Sharp: n=45  W=10/L=35  WR=22.2%**
- **Dir: SHORT**  •  RSI 70-80 overbought; session=ny_mid  •  ONLY when HTF20 aligned WITH trade

### L15.  `H60=H60e AND T1=T1c AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=115  W=43/L=72  WR=37.4%
- Sharpen: sharpest is H20=H20a (35/72 of losers there)
- **Sharp: n=45  W=10/L=35  WR=22.2%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 70-80 overbought; session=ny_mid  •  ONLY when HTF20 aligned WITH trade

### L16.  `H60=H60e AND T4=T4c AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=115  W=43/L=72  WR=37.4%
- Sharpen: sharpest is H20=H20a (35/72 of losers there)
- **Sharp: n=45  W=10/L=35  WR=22.2%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 70-80 overbought; session=ny_mid  •  ONLY when HTF20 aligned WITH trade

### L17.  `H60=H60e AND RSI=RSI6 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=115  W=43/L=72  WR=37.4%
- Sharpen: sharpest is H20=H20a (35/72 of losers there)
- **Sharp: n=45  W=10/L=35  WR=22.2%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 70-80 overbought; session=ny_mid  •  ONLY when HTF20 aligned WITH trade

### L18.  `T1=T1c AND T4=T4c AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=115  W=43/L=72  WR=37.4%
- Sharpen: sharpest is H20=H20a (35/72 of losers there)
- **Sharp: n=45  W=10/L=35  WR=22.2%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 70-80 overbought; session=ny_mid  •  ONLY when HTF20 aligned WITH trade

### L19.  `T1=T1c AND RSI=RSI6 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=115  W=43/L=72  WR=37.4%
- Sharpen: sharpest is H20=H20a (35/72 of losers there)
- **Sharp: n=45  W=10/L=35  WR=22.2%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 70-80 overbought; session=ny_mid  •  ONLY when HTF20 aligned WITH trade

### L20.  `T4=T4c AND RSI=RSI6 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=115  W=43/L=72  WR=37.4%
- Sharpen: sharpest is H20=H20a (35/72 of losers there)
- **Sharp: n=45  W=10/L=35  WR=22.2%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 70-80 overbought; session=ny_mid  •  ONLY when HTF20 aligned WITH trade

### L21.  `H60=H60e AND T4=T4c AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=110  W=33/L=77  WR=30.0%
- Sharpen: sharpest is RSI=RSI6 (39/77 of losers there)
- **Sharp: n=39  W=0/L=39  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; zscore +2 to +3 deep overbought; session=asia  •  ONLY when RSI 70-80 overbought

### L22.  `T1=T1c AND T4=T4c AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=110  W=33/L=77  WR=30.0%
- Sharpen: sharpest is RSI=RSI6 (39/77 of losers there)
- **Sharp: n=39  W=0/L=39  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought; session=asia  •  ONLY when RSI 70-80 overbought

### L23.  `T4=T4c AND ZS=ZS5 AND direction_exec=short AND session_bucket=asia`
- Raw: n=110  W=33/L=77  WR=30.0%
- Sharpen: sharpest is RSI=RSI6 (39/77 of losers there)
- **Sharp: n=39  W=0/L=39  WR=0.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; zscore +2 to +3 deep overbought; session=asia  •  ONLY when RSI 70-80 overbought

### L24.  `H20=H20e AND RSI=RSI5 AND session_bucket=london`
- Raw: n=110  W=42/L=68  WR=38.2%
- Sharpen: sharpest is H60=H60e (46/68 of losers there)
- **Sharp: n=58  W=12/L=46  WR=20.7%**
- **Dir: ?**  •  HTF20 strongly against; RSI 60-70 strong; session=london  •  ONLY when HTF60 strongly against

### L25.  `T4=T4c AND BBP=BBP4 AND session_bucket=ny_open`
- Raw: n=109  W=42/L=67  WR=38.5%
- Sharpen: sharpest is H20=H20d (14/67 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  4h trend AGAINST trade; upper third; session=ny_open  •  ONLY when HTF20 mildly against

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(47/41) | H20e(41/46) |
| H60 | H60a(57/42) | H60e(42/57) |
| T1 | T1a(57/43) | T1c(43/57) |
| T4 | T4a(56/45) | T4c(44/55) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(57/43) | short(43/57) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
