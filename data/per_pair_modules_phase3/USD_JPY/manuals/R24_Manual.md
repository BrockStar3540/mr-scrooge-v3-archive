# USD_JPY — R24 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **6,257**  (W=3,864 / L=2,393)  -  WR: **61.8%**

## Session distribution

- asia: n=1563  W=977/L=586  WR=62.5%
- ny_mid: n=1434  W=902/L=532  WR=62.9%
- london_open: n=1296  W=792/L=504  WR=61.1%
- ny_close: n=659  W=380/L=279  WR=57.7%
- ny_open: n=619  W=373/L=246  WR=60.3%
- london: n=456  W=282/L=174  WR=61.8%
- asia_late: n=216  W=149/L=67  WR=69.0%
- off_hours: n=14  W=9/L=5  WR=64.3%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60a AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=289  W=250/L=39  WR=86.5%
- Refine: exclude BBP=BBP3 drops 13/39 losers (33%)
- **Final: n=253  W=227/L=26  WR=89.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; session=ny_mid  •  AVOID when middle of band

### W02.  `H60=H60a AND RSI=RSI4 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=289  W=250/L=39  WR=86.5%
- Refine: exclude BBP=BBP3 drops 13/39 losers (33%)
- **Final: n=253  W=227/L=26  WR=89.7%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; session=ny_mid  •  AVOID when middle of band

### W03.  `H60=H60a AND T1=T1a AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=287  W=248/L=39  WR=86.4%
- Refine: exclude BBP=BBP3 drops 13/39 losers (33%)
- **Final: n=251  W=225/L=26  WR=89.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 50-60 upper neutral; session=ny_mid  •  AVOID when middle of band

### W04.  `H60=H60a AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=198  W=174/L=24  WR=87.9%
- Refine: exclude H20=H20a drops 24/24 losers (100%)
- **Final: n=56  W=56/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

### W05.  `H60=H60a AND T4=T4c AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=198  W=174/L=24  WR=87.9%
- Refine: exclude H20=H20a drops 24/24 losers (100%)
- **Final: n=56  W=56/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

### W06.  `H60=H60a AND T1=T1a AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=192  W=168/L=24  WR=87.5%
- Refine: exclude H20=H20a drops 24/24 losers (100%)
- **Final: n=50  W=50/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

### W07.  `H60=H60a AND T4=T4c AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=192  W=168/L=24  WR=87.5%
- Refine: exclude H20=H20a drops 24/24 losers (100%)
- **Final: n=50  W=50/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

### W08.  `H60=H60a AND BBP=BBP4 AND session_bucket=ny_mid`
- Raw: n=133  W=115/L=18  WR=86.5%
- Refine: exclude T1=T1c drops 13/18 losers (72%)
- **Final: n=93  W=88/L=5  WR=94.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; upper third; session=ny_mid  •  AVOID when 1h trend AGAINST trade

### W09.  `H60=H60a AND BBP=BBP4 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=133  W=115/L=18  WR=86.5%
- Refine: exclude T1=T1c drops 13/18 losers (72%)
- **Final: n=93  W=88/L=5  WR=94.6%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; upper third; session=ny_mid  •  AVOID when 1h trend AGAINST trade

### W10.  `H20=H20e AND H60=H60e AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=121  W=106/L=15  WR=87.6%
- Refine: exclude BBP=BBP6 drops 12/15 losers (80%)
- **Final: n=64  W=61/L=3  WR=95.3%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; zscore +2 to +3 deep overbought; session=asia  •  AVOID when deep above upper band

### W11.  `H20=H20e AND T1=T1a AND RSI=RSI4 AND direction_exec=long`
- Raw: n=116  W=101/L=15  WR=87.1%
- Refine: exclude T4=T4c drops 15/15 losers (100%)
- **Final: n=27  W=27/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when 4h trend AGAINST trade

### W12.  `T4=T4c AND RSI=RSI3 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=115  W=98/L=17  WR=85.2%
- Refine: exclude session_bucket=ny_mid drops 9/17 losers (53%)
- **Final: n=82  W=74/L=8  WR=90.2%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; zscore +1 to +2 overbought  •  AVOID when session=ny_mid

### W13.  `T1=T1a AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=113  W=97/L=16  WR=85.8%
- Refine: exclude H20=H20b drops 6/16 losers (38%)
- **Final: n=102  W=92/L=10  WR=90.2%**
- **Dir: ?**  •  1h trend WITH trade; zscore +1 to +2 overbought; session=ny_mid  •  AVOID when HTF20 slightly aligned

### W14.  `T1=T1a AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=113  W=97/L=16  WR=85.8%
- Refine: exclude H20=H20b drops 6/16 losers (38%)
- **Final: n=102  W=92/L=10  WR=90.2%**
- **Dir: ?**  •  1h trend WITH trade; upper third; zscore +1 to +2 overbought; session=ny_mid  •  AVOID when HTF20 slightly aligned

### W15.  `H20=H20d AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=107  W=91/L=16  WR=85.0%
- Refine: exclude direction_exec=short drops 13/16 losers (81%)
- **Final: n=71  W=68/L=3  WR=95.8%**
- **Dir: ?**  •  HTF20 mildly against; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when short

### W16.  `RSI=RSI3 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=103  W=94/L=9  WR=91.3%
- Refine: exclude session_bucket=ny_open drops 6/9 losers (67%)
- **Final: n=79  W=76/L=3  WR=96.2%**
- **Dir: SHORT**  •  RSI 40-50 lower neutral; zscore +2 to +3 deep overbought  •  AVOID when session=ny_open

### W17.  `T4=T4a AND ZS=ZS1 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=103  W=93/L=10  WR=90.3%
- Refine: exclude BBP=BBP1 drops 10/10 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: LONG**  •  4h trend WITH trade; zscore -3 to -2 deep oversold; session=london_open  •  AVOID when just touched lower band

### W18.  `T1=T1a AND RSI=RSI3 AND ZS=ZS5`
- Raw: n=100  W=85/L=15  WR=85.0%
- Refine: exclude H60=H60a drops 12/15 losers (80%)
- **Final: n=76  W=73/L=3  WR=96.1%**
- **Dir: ?**  •  1h trend WITH trade; RSI 40-50 lower neutral; zscore +2 to +3 deep overbought  •  AVOID when HTF60 aligned WITH trade

### W19.  `T1=T1a AND T4=T4c AND BBP=BBP4 AND session_bucket=ny_mid`
- Raw: n=100  W=85/L=15  WR=85.0%
- Refine: exclude RSI=RSI3 drops 10/15 losers (67%)
- **Final: n=66  W=61/L=5  WR=92.4%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; upper third; session=ny_mid  •  AVOID when RSI 40-50 lower neutral

### W20.  `H20=H20e AND T1=T1a AND BBP=BBP5`
- Raw: n=98  W=88/L=10  WR=89.8%
- Refine: exclude session_bucket=ny_close drops 4/10 losers (40%)
- **Final: n=93  W=87/L=6  WR=93.5%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; just touched upper band  •  AVOID when session=ny_close

### W21.  `H20=H20e AND T1=T1a AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=98  W=88/L=10  WR=89.8%
- Refine: exclude session_bucket=ny_close drops 4/10 losers (40%)
- **Final: n=93  W=87/L=6  WR=93.5%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; just touched upper band; zscore +2 to +3 deep overbought  •  AVOID when session=ny_close

### W22.  `T1=T1a AND BBP=BBP4 AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=96  W=88/L=8  WR=91.7%
- Refine: exclude H60=H60b drops 3/8 losers (38%)
- **Final: n=93  W=88/L=5  WR=94.6%**
- **Dir: ?**  •  1h trend WITH trade; upper third; RSI 50-60 upper neutral; session=ny_mid  •  AVOID when HTF60 slightly aligned

### W23.  `T1=T1a AND BBP=BBP4 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=96  W=88/L=8  WR=91.7%
- Refine: exclude H60=H60b drops 3/8 losers (38%)
- **Final: n=93  W=88/L=5  WR=94.6%**
- **Dir: LONG**  •  1h trend WITH trade; upper third; session=ny_mid  •  AVOID when HTF60 slightly aligned

### W24.  `BBP=BBP4 AND RSI=RSI4 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=96  W=88/L=8  WR=91.7%
- Refine: exclude H60=H60b drops 3/8 losers (38%)
- **Final: n=93  W=88/L=5  WR=94.6%**
- **Dir: LONG**  •  upper third; RSI 50-60 upper neutral; session=ny_mid  •  AVOID when HTF60 slightly aligned

### W25.  `T1=T1a AND BBP=BBP5 AND direction_exec=short`
- Raw: n=96  W=86/L=10  WR=89.6%
- Refine: exclude RSI=RSI4 drops 7/10 losers (70%)
- **Final: n=61  W=58/L=3  WR=95.1%**
- **Dir: SHORT**  •  1h trend WITH trade; just touched upper band  •  AVOID when RSI 50-60 upper neutral

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND T4=T4c AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=204  W=79/L=125  WR=38.7%
- Sharpen: sharpest is H60=H60e (92/125 of losers there)
- **Sharp: n=130  W=38/L=92  WR=29.2%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; lower third; RSI 40-50 lower neutral  •  ONLY when HTF60 strongly against

### L02.  `H20=H20e AND H60=H60e AND T4=T4c AND BBP=BBP2`
- Raw: n=197  W=76/L=121  WR=38.6%
- Sharpen: sharpest is RSI=RSI3 (92/121 of losers there)
- **Sharp: n=130  W=38/L=92  WR=29.2%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; lower third  •  ONLY when RSI 40-50 lower neutral

### L03.  `H20=H20e AND T1=T1a AND ZS=ZS2 AND direction_exec=short`
- Raw: n=195  W=76/L=119  WR=39.0%
- Sharpen: sharpest is T4=T4c (108/119 of losers there)
- **Sharp: n=164  W=56/L=108  WR=34.1%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend WITH trade; zscore -2 to -1 oversold  •  ONLY when 4h trend AGAINST trade

### L04.  `T1=T1c AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=190  W=72/L=118  WR=37.9%
- Sharpen: sharpest is ZS=ZS3 (49/118 of losers there)
- **Sharp: n=55  W=6/L=49  WR=10.9%**
- **Dir: SHORT**  •  1h trend AGAINST trade; session=ny_close  •  ONLY when zscore -1 to +1 neutral

### L05.  `T1=T1c AND T4=T4a AND session_bucket=ny_close`
- Raw: n=188  W=67/L=121  WR=35.6%
- Sharpen: sharpest is ZS=ZS3 (49/121 of losers there)
- **Sharp: n=64  W=15/L=49  WR=23.4%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; session=ny_close  •  ONLY when zscore -1 to +1 neutral

### L06.  `H20=H20e AND T1=T1a AND T4=T4c AND BBP=BBP2`
- Raw: n=187  W=70/L=117  WR=37.4%
- Sharpen: sharpest is H60=H60e (96/117 of losers there)
- **Sharp: n=141  W=45/L=96  WR=31.9%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; lower third  •  ONLY when HTF60 strongly against

### L07.  `H60=H60e AND T1=T1c AND session_bucket=ny_close`
- Raw: n=174  W=66/L=108  WR=37.9%
- Sharpen: sharpest is ZS=ZS3 (48/108 of losers there)
- **Sharp: n=55  W=7/L=48  WR=12.7%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; session=ny_close  •  ONLY when zscore -1 to +1 neutral

### L08.  `H20=H20e AND H60=H60e AND T4=T4c AND ZS=ZS2`
- Raw: n=173  W=65/L=108  WR=37.6%
- Sharpen: sharpest is T1=T1a (90/108 of losers there)
- **Sharp: n=126  W=36/L=90  WR=28.6%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; zscore -2 to -1 oversold  •  ONLY when 1h trend WITH trade

### L09.  `T4=T4c AND BBP=BBP1 AND direction_exec=short`
- Raw: n=169  W=64/L=105  WR=37.9%
- Sharpen: sharpest is session_bucket=london_open (36/105 of losers there)
- **Sharp: n=42  W=6/L=36  WR=14.3%**
- **Dir: SHORT**  •  4h trend AGAINST trade; just touched lower band  •  ONLY when session=london_open

### L10.  `T4=T4c AND BBP=BBP1 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=169  W=64/L=105  WR=37.9%
- Sharpen: sharpest is session_bucket=london_open (36/105 of losers there)
- **Sharp: n=42  W=6/L=36  WR=14.3%**
- **Dir: SHORT**  •  4h trend AGAINST trade; just touched lower band; zscore -3 to -2 deep oversold  •  ONLY when session=london_open

### L11.  `H60=H60e AND T1=T1c AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=167  W=65/L=102  WR=38.9%
- Sharpen: sharpest is ZS=ZS3 (44/102 of losers there)
- **Sharp: n=50  W=6/L=44  WR=12.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; session=ny_close  •  ONLY when zscore -1 to +1 neutral

### L12.  `H20=H20e AND H60=H60e AND T1=T1a AND ZS=ZS2`
- Raw: n=167  W=66/L=101  WR=39.5%
- Sharpen: sharpest is T4=T4c (90/101 of losers there)
- **Sharp: n=126  W=36/L=90  WR=28.6%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend WITH trade; zscore -2 to -1 oversold  •  ONLY when 4h trend AGAINST trade

### L13.  `H20=H20e AND T1=T1a AND T4=T4c AND ZS=ZS2`
- Raw: n=165  W=56/L=109  WR=33.9%
- Sharpen: sharpest is H60=H60e (90/109 of losers there)
- **Sharp: n=126  W=36/L=90  WR=28.6%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; zscore -2 to -1 oversold  •  ONLY when HTF60 strongly against

### L14.  `H20=H20a AND T1=T1c AND direction_exec=short`
- Raw: n=154  W=60/L=94  WR=39.0%
- Sharpen: sharpest is RSI=RSI4 (57/94 of losers there)
- **Sharp: n=75  W=18/L=57  WR=24.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade  •  ONLY when RSI 50-60 upper neutral

### L15.  `H60=H60e AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=152  W=49/L=103  WR=32.2%
- Sharpen: sharpest is BBP=BBP4 (38/103 of losers there)
- **Sharp: n=38  W=0/L=38  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; session=ny_mid  •  ONLY when upper third

### L16.  `H60=H60e AND T4=T4a AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=152  W=49/L=103  WR=32.2%
- Sharpen: sharpest is BBP=BBP4 (38/103 of losers there)
- **Sharp: n=38  W=0/L=38  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend WITH trade; session=ny_mid  •  ONLY when upper third

### L17.  `H60=H60e AND T1=T1c AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=149  W=49/L=100  WR=32.9%
- Sharpen: sharpest is BBP=BBP4 (35/100 of losers there)
- **Sharp: n=35  W=0/L=35  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade; session=ny_mid  •  ONLY when upper third

### L18.  `H60=H60e AND T4=T4a AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=149  W=49/L=100  WR=32.9%
- Sharpen: sharpest is BBP=BBP4 (35/100 of losers there)
- **Sharp: n=35  W=0/L=35  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; RSI 50-60 upper neutral; session=ny_mid  •  ONLY when upper third

### L19.  `H60=H60e AND T1=T1a AND T4=T4c AND ZS=ZS1`
- Raw: n=141  W=53/L=88  WR=37.6%
- Sharpen: sharpest is session_bucket=london_open (36/88 of losers there)
- **Sharp: n=40  W=4/L=36  WR=10.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when session=london_open

### L20.  `T1=T1a AND T4=T4c AND BBP=BBP1 AND direction_exec=short`
- Raw: n=126  W=47/L=79  WR=37.3%
- Sharpen: sharpest is session_bucket=london_open (30/79 of losers there)
- **Sharp: n=33  W=3/L=30  WR=9.1%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend AGAINST trade; just touched lower band  •  ONLY when session=london_open

### L21.  `H20=H20e AND H60=H60e AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=122  W=48/L=74  WR=39.3%
- Sharpen: sharpest is BBP=BBP4 (26/74 of losers there)
- **Sharp: n=26  W=0/L=26  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend WITH trade; session=ny_mid  •  ONLY when upper third

### L22.  `H20=H20e AND T4=T4a AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=122  W=48/L=74  WR=39.3%
- Sharpen: sharpest is BBP=BBP4 (26/74 of losers there)
- **Sharp: n=26  W=0/L=26  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; RSI 50-60 upper neutral; session=ny_mid  •  ONLY when upper third

### L23.  `H20=H20e AND T4=T4a AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=122  W=48/L=74  WR=39.3%
- Sharpen: sharpest is BBP=BBP4 (26/74 of losers there)
- **Sharp: n=26  W=0/L=26  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend WITH trade; session=ny_mid  •  ONLY when upper third

### L24.  `T1=T1c AND RSI=RSI3 AND session_bucket=ny_close`
- Raw: n=115  W=37/L=78  WR=32.2%
- Sharpen: sharpest is H60=H60e (44/78 of losers there)
- **Sharp: n=56  W=12/L=44  WR=21.4%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 40-50 lower neutral; session=ny_close  •  ONLY when HTF60 strongly against

### L25.  `H20=H20a AND T1=T1c AND T4=T4a AND direction_exec=short`
- Raw: n=115  W=46/L=69  WR=40.0%
- Sharpen: sharpest is ZS=ZS3 (24/69 of losers there)
- **Sharp: n=29  W=5/L=24  WR=17.2%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when zscore -1 to +1 neutral

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | H60e(39/44) |
| T1 | T1a(52/45) | T1c(48/54) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(55/46) | short(45/54) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
