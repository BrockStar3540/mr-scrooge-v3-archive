# USD_CHF — R28 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **1,212**  (W=775 / L=437)  -  WR: **63.9%**

## Session distribution

- ny_mid: n=292  W=189/L=103  WR=64.7%
- london_open: n=289  W=201/L=88  WR=69.6%
- asia: n=221  W=122/L=99  WR=55.2%
- ny_close: n=170  W=116/L=54  WR=68.2%
- london: n=87  W=54/L=33  WR=62.1%
- ny_open: n=77  W=50/L=27  WR=64.9%
- off_hours: n=41  W=21/L=20  WR=51.2%
- asia_late: n=35  W=22/L=13  WR=62.9%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1c AND T4=T4c AND session_bucket=ny_close`
- Raw: n=68  W=58/L=10  WR=85.3%
- Refine: exclude ZS=ZS3 drops 5/10 losers (50%)
- **Final: n=59  W=54/L=5  WR=91.5%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_close  •  AVOID when zscore -1 to +1 neutral

### W02.  `T1=T1c AND T4=T4c AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=68  W=58/L=10  WR=85.3%
- Refine: exclude ZS=ZS3 drops 5/10 losers (50%)
- **Final: n=59  W=54/L=5  WR=91.5%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_close  •  AVOID when zscore -1 to +1 neutral

### W03.  `H20=H20a AND T1=T1a AND RSI=RSI1`
- Raw: n=66  W=59/L=7  WR=89.4%
- Refine: exclude session_bucket=ny_close drops 6/7 losers (86%)
- **Final: n=50  W=49/L=1  WR=98.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 20-30 oversold  •  AVOID when session=ny_close

### W04.  `H20=H20a AND T4=T4a AND RSI=RSI1`
- Raw: n=66  W=59/L=7  WR=89.4%
- Refine: exclude session_bucket=ny_close drops 6/7 losers (86%)
- **Final: n=50  W=49/L=1  WR=98.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 20-30 oversold  •  AVOID when session=ny_close

### W05.  `H20=H20a AND RSI=RSI1 AND direction_exec=short`
- Raw: n=66  W=59/L=7  WR=89.4%
- Refine: exclude session_bucket=ny_close drops 6/7 losers (86%)
- **Final: n=50  W=49/L=1  WR=98.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 20-30 oversold  •  AVOID when session=ny_close

### W06.  `H20=H20a AND T1=T1a AND T4=T4a AND RSI=RSI1`
- Raw: n=66  W=59/L=7  WR=89.4%
- Refine: exclude session_bucket=ny_close drops 6/7 losers (86%)
- **Final: n=50  W=49/L=1  WR=98.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; RSI 20-30 oversold  •  AVOID when session=ny_close

### W07.  `H20=H20a AND T1=T1a AND RSI=RSI1 AND direction_exec=short`
- Raw: n=66  W=59/L=7  WR=89.4%
- Refine: exclude session_bucket=ny_close drops 6/7 losers (86%)
- **Final: n=50  W=49/L=1  WR=98.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 20-30 oversold  •  AVOID when session=ny_close

### W08.  `H20=H20a AND T4=T4a AND RSI=RSI1 AND direction_exec=short`
- Raw: n=66  W=59/L=7  WR=89.4%
- Refine: exclude session_bucket=ny_close drops 6/7 losers (86%)
- **Final: n=50  W=49/L=1  WR=98.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 20-30 oversold  •  AVOID when session=ny_close

### W09.  `H60=H60e AND BBP=BBP2 AND RSI=RSI2`
- Raw: n=62  W=54/L=8  WR=87.1%
- Refine: exclude H20=H20b drops 5/8 losers (62%)
- **Final: n=57  W=54/L=3  WR=94.7%**
- **Dir: ?**  •  HTF60 strongly against; lower third; RSI 30-40 weak  •  AVOID when HTF20 slightly aligned

### W10.  `H60=H60e AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=58  W=51/L=7  WR=87.9%
- Refine: exclude ZS=ZS3 drops 4/7 losers (57%)
- **Final: n=52  W=49/L=3  WR=94.2%**
- **Dir: LONG**  •  HTF60 strongly against; session=ny_close  •  AVOID when zscore -1 to +1 neutral

### W11.  `H60=H60e AND RSI=RSI2 AND ZS=ZS2`
- Raw: n=57  W=50/L=7  WR=87.7%
- Refine: exclude H20=H20b drops 5/7 losers (71%)
- **Final: n=52  W=50/L=2  WR=96.2%**
- **Dir: ?**  •  HTF60 strongly against; RSI 30-40 weak; zscore -2 to -1 oversold  •  AVOID when HTF20 slightly aligned

### W12.  `H60=H60e AND BBP=BBP2 AND RSI=RSI2 AND ZS=ZS2`
- Raw: n=57  W=50/L=7  WR=87.7%
- Refine: exclude H20=H20b drops 5/7 losers (71%)
- **Final: n=52  W=50/L=2  WR=96.2%**
- **Dir: ?**  •  HTF60 strongly against; lower third; RSI 30-40 weak; zscore -2 to -1 oversold  •  AVOID when HTF20 slightly aligned

### W13.  `T1=T1a AND T4=T4c AND session_bucket=london_open`
- Raw: n=57  W=49/L=8  WR=86.0%
- Refine: exclude BBP=BBP1 drops 5/8 losers (62%)
- **Final: n=51  W=48/L=3  WR=94.1%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; session=london_open  •  AVOID when just touched lower band

### W14.  `H60=H60e AND T1=T1c AND session_bucket=ny_close`
- Raw: n=56  W=50/L=6  WR=89.3%
- Refine: exclude ZS=ZS3 drops 4/6 losers (67%)
- **Final: n=50  W=48/L=2  WR=96.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; session=ny_close  •  AVOID when zscore -1 to +1 neutral

### W15.  `H60=H60e AND T1=T1c AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=56  W=50/L=6  WR=89.3%
- Refine: exclude ZS=ZS3 drops 4/6 losers (67%)
- **Final: n=50  W=48/L=2  WR=96.0%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend AGAINST trade; session=ny_close  •  AVOID when zscore -1 to +1 neutral

### W16.  `H20=H20d AND T4=T4a AND RSI=RSI2`
- Raw: n=55  W=49/L=6  WR=89.1%
- Refine: exclude BBP=BBP3 drops 5/6 losers (83%)
- **Final: n=45  W=44/L=1  WR=97.8%**
- **Dir: ?**  •  HTF20 mildly against; 4h trend WITH trade; RSI 30-40 weak  •  AVOID when middle of band

### W17.  `H60=H60e AND T4=T4c AND session_bucket=ny_close`
- Raw: n=54  W=47/L=7  WR=87.0%
- Refine: exclude ZS=ZS3 drops 4/7 losers (57%)
- **Final: n=48  W=45/L=3  WR=93.8%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; session=ny_close  •  AVOID when zscore -1 to +1 neutral

### W18.  `T1=T1c AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=54  W=47/L=7  WR=87.0%
- Refine: exclude H60=H60b drops 6/7 losers (86%)
- **Final: n=48  W=47/L=1  WR=97.9%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 30-40 weak; session=asia  •  AVOID when HTF60 slightly aligned

### W19.  `RSI=RSI2 AND direction_exec=long AND session_bucket=asia`
- Raw: n=54  W=47/L=7  WR=87.0%
- Refine: exclude H60=H60b drops 6/7 losers (86%)
- **Final: n=48  W=47/L=1  WR=97.9%**
- **Dir: LONG**  •  RSI 30-40 weak; session=asia  •  AVOID when HTF60 slightly aligned

### W20.  `H60=H60e AND T4=T4c AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=54  W=47/L=7  WR=87.0%
- Refine: exclude ZS=ZS3 drops 4/7 losers (57%)
- **Final: n=48  W=45/L=3  WR=93.8%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend AGAINST trade; session=ny_close  •  AVOID when zscore -1 to +1 neutral

### W21.  `T1=T1c AND RSI=RSI2 AND direction_exec=long AND session_bucket=asia`
- Raw: n=54  W=47/L=7  WR=87.0%
- Refine: exclude H60=H60b drops 6/7 losers (86%)
- **Final: n=48  W=47/L=1  WR=97.9%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 30-40 weak; session=asia  •  AVOID when HTF60 slightly aligned

### W22.  `H60=H60e AND T1=T1c AND BBP=BBP2 AND RSI=RSI2`
- Raw: n=54  W=46/L=8  WR=85.2%
- Refine: exclude H20=H20b drops 5/8 losers (62%)
- **Final: n=49  W=46/L=3  WR=93.9%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; lower third; RSI 30-40 weak  •  AVOID when HTF20 slightly aligned

### W23.  `H60=H60e AND BBP=BBP2 AND RSI=RSI2 AND direction_exec=long`
- Raw: n=54  W=46/L=8  WR=85.2%
- Refine: exclude H20=H20b drops 5/8 losers (62%)
- **Final: n=49  W=46/L=3  WR=93.9%**
- **Dir: LONG**  •  HTF60 strongly against; lower third; RSI 30-40 weak  •  AVOID when HTF20 slightly aligned

### W24.  `H60=H60a AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=52  W=49/L=3  WR=94.2%
- Refine: exclude T1=T1c drops 2/3 losers (67%)
- **Final: n=50  W=49/L=1  WR=98.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; session=ny_mid  •  AVOID when 1h trend AGAINST trade

### W25.  `H60=H60e AND T1=T1c AND T4=T4c AND session_bucket=ny_close`
- Raw: n=52  W=46/L=6  WR=88.5%
- Refine: exclude ZS=ZS3 drops 4/6 losers (67%)
- **Final: n=46  W=44/L=2  WR=95.7%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_close  •  AVOID when zscore -1 to +1 neutral

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T4=T4c AND RSI=RSI2 AND session_bucket=ny_mid`
- Raw: n=63  W=25/L=38  WR=39.7%
- Sharpen: sharpest is BBP=BBP2 (8/38 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 30-40 weak; session=ny_mid  •  ONLY when lower third

### L02.  `T1=T1c AND T4=T4c AND RSI=RSI2 AND session_bucket=ny_mid`
- Raw: n=61  W=24/L=37  WR=39.3%
- Sharpen: sharpest is BBP=BBP1 (8/37 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 30-40 weak; session=ny_mid  •  ONLY when just touched lower band

### L03.  `T4=T4c AND RSI=RSI2 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=61  W=24/L=37  WR=39.3%
- Sharpen: sharpest is BBP=BBP1 (8/37 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 30-40 weak; session=ny_mid  •  ONLY when just touched lower band

### L04.  `H60=H60e AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=55  W=20/L=35  WR=36.4%
- Sharpen: sharpest is session_bucket=asia (22/35 of losers there)
- **Sharp: n=26  W=4/L=22  WR=15.4%**
- **Dir: ?**  •  HTF60 strongly against; lower third; RSI 40-50 lower neutral  •  ONLY when session=asia

### L05.  `T4=T4c AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=54  W=21/L=33  WR=38.9%
- Sharpen: sharpest is H60=H60e (23/33 of losers there)
- **Sharp: n=31  W=8/L=23  WR=25.8%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  ONLY when HTF60 strongly against

### L06.  `RSI=RSI3 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=54  W=21/L=33  WR=38.9%
- Sharpen: sharpest is H60=H60e (23/33 of losers there)
- **Sharp: n=31  W=8/L=23  WR=25.8%**
- **Dir: LONG**  •  RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  ONLY when HTF60 strongly against

### L07.  `T4=T4c AND BBP=BBP2 AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=54  W=21/L=33  WR=38.9%
- Sharpen: sharpest is H60=H60e (23/33 of losers there)
- **Sharp: n=31  W=8/L=23  WR=25.8%**
- **Dir: ?**  •  4h trend AGAINST trade; lower third; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  ONLY when HTF60 strongly against

### L08.  `T4=T4c AND RSI=RSI3 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=54  W=21/L=33  WR=38.9%
- Sharpen: sharpest is H60=H60e (23/33 of losers there)
- **Sharp: n=31  W=8/L=23  WR=25.8%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  ONLY when HTF60 strongly against

### L09.  `BBP=BBP2 AND RSI=RSI3 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=54  W=21/L=33  WR=38.9%
- Sharpen: sharpest is H60=H60e (23/33 of losers there)
- **Sharp: n=31  W=8/L=23  WR=25.8%**
- **Dir: LONG**  •  lower third; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  ONLY when HTF60 strongly against

### L10.  `T1=T1a AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=48  W=19/L=29  WR=39.6%
- Sharpen: sharpest is RSI=RSI2 (13/29 of losers there)
- **Sharp: n=14  W=1/L=13  WR=7.1%**
- **Dir: ?**  •  1h trend WITH trade; zscore -2 to -1 oversold; session=asia  •  ONLY when RSI 30-40 weak

### L11.  `T1=T1a AND BBP=BBP2 AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=48  W=19/L=29  WR=39.6%
- Sharpen: sharpest is RSI=RSI2 (13/29 of losers there)
- **Sharp: n=14  W=1/L=13  WR=7.1%**
- **Dir: ?**  •  1h trend WITH trade; lower third; zscore -2 to -1 oversold; session=asia  •  ONLY when RSI 30-40 weak

### L12.  `H60=H60e AND T4=T4c AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=45  W=14/L=31  WR=31.1%
- Sharpen: sharpest is session_bucket=asia (18/31 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; lower third; RSI 40-50 lower neutral  •  ONLY when session=asia

### L13.  `H60=H60e AND BBP=BBP2 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=45  W=14/L=31  WR=31.1%
- Sharpen: sharpest is session_bucket=asia (18/31 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: LONG**  •  HTF60 strongly against; lower third; RSI 40-50 lower neutral  •  ONLY when session=asia

### L14.  `H20=H20e AND H60=H60e AND T4=T4c AND session_bucket=asia`
- Raw: n=45  W=18/L=27  WR=40.0%
- Sharpen: sharpest is RSI=RSI3 (24/27 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; session=asia  •  ONLY when RSI 40-50 lower neutral

### L15.  `H20=H20e AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=44  W=15/L=29  WR=34.1%
- Sharpen: sharpest is session_bucket=asia (18/29 of losers there)
- **Sharp: n=20  W=2/L=18  WR=10.0%**
- **Dir: ?**  •  HTF20 strongly against; lower third; RSI 40-50 lower neutral  •  ONLY when session=asia

### L16.  `H20=H20c AND H60=H60a AND T1=T1a`
- Raw: n=41  W=13/L=28  WR=31.7%
- Sharpen: sharpest is RSI=RSI4 (9/28 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: ?**  •  HTF20 neutral; HTF60 aligned WITH trade; 1h trend WITH trade  •  ONLY when RSI 50-60 upper neutral

### L17.  `H20=H20c AND H60=H60a AND T4=T4a`
- Raw: n=41  W=13/L=28  WR=31.7%
- Sharpen: sharpest is RSI=RSI4 (9/28 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: ?**  •  HTF20 neutral; HTF60 aligned WITH trade; 4h trend WITH trade  •  ONLY when RSI 50-60 upper neutral

### L18.  `H20=H20c AND H60=H60a AND direction_exec=short`
- Raw: n=41  W=13/L=28  WR=31.7%
- Sharpen: sharpest is RSI=RSI4 (9/28 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: SHORT**  •  HTF20 neutral; HTF60 aligned WITH trade  •  ONLY when RSI 50-60 upper neutral

### L19.  `H20=H20c AND T1=T1a AND T4=T4a`
- Raw: n=41  W=13/L=28  WR=31.7%
- Sharpen: sharpest is RSI=RSI4 (9/28 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: ?**  •  HTF20 neutral; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when RSI 50-60 upper neutral

### L20.  `H20=H20c AND T1=T1a AND direction_exec=short`
- Raw: n=41  W=13/L=28  WR=31.7%
- Sharpen: sharpest is RSI=RSI4 (9/28 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: SHORT**  •  HTF20 neutral; 1h trend WITH trade  •  ONLY when RSI 50-60 upper neutral

### L21.  `H20=H20c AND T4=T4a AND direction_exec=short`
- Raw: n=41  W=13/L=28  WR=31.7%
- Sharpen: sharpest is RSI=RSI4 (9/28 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: SHORT**  •  HTF20 neutral; 4h trend WITH trade  •  ONLY when RSI 50-60 upper neutral

### L22.  `H20=H20c AND H60=H60a AND T1=T1a AND T4=T4a`
- Raw: n=41  W=13/L=28  WR=31.7%
- Sharpen: sharpest is RSI=RSI4 (9/28 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: ?**  •  HTF20 neutral; HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when RSI 50-60 upper neutral

### L23.  `H20=H20c AND H60=H60a AND T1=T1a AND direction_exec=short`
- Raw: n=41  W=13/L=28  WR=31.7%
- Sharpen: sharpest is RSI=RSI4 (9/28 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: SHORT**  •  HTF20 neutral; HTF60 aligned WITH trade; 1h trend WITH trade  •  ONLY when RSI 50-60 upper neutral

### L24.  `H20=H20c AND H60=H60a AND T4=T4a AND direction_exec=short`
- Raw: n=41  W=13/L=28  WR=31.7%
- Sharpen: sharpest is RSI=RSI4 (9/28 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: SHORT**  •  HTF20 neutral; HTF60 aligned WITH trade; 4h trend WITH trade  •  ONLY when RSI 50-60 upper neutral

### L25.  `H20=H20c AND T1=T1a AND T4=T4a AND direction_exec=short`
- Raw: n=41  W=13/L=28  WR=31.7%
- Sharpen: sharpest is RSI=RSI4 (9/28 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: SHORT**  •  HTF20 neutral; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when RSI 50-60 upper neutral

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(33/27) | H20e(26/33) |
| H60 | H60e(38/31) | — |
| T1 | — | — |
| T4 | T4a(54/49) | T4c(46/51) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | london_open(26/20) | asia(16/23) |

*Read: `bucket(winner%/loser%)`.*
