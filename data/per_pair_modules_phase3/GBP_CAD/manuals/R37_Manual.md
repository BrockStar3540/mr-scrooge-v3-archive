# GBP_CAD — R37 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50e**  (EMA50 down >0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **2,899**  (W=1,764 / L=1,135)  -  WR: **60.8%**

## Session distribution

- asia: n=632  W=392/L=240  WR=62.0%
- london_open: n=455  W=273/L=182  WR=60.0%
- ny_close: n=450  W=277/L=173  WR=61.6%
- ny_mid: n=439  W=267/L=172  WR=60.8%
- london: n=353  W=210/L=143  WR=59.5%
- asia_late: n=254  W=156/L=98  WR=61.4%
- ny_open: n=224  W=138/L=86  WR=61.6%
- off_hours: n=92  W=51/L=41  WR=55.4%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60e AND BBP=BBP2 AND session_bucket=london_open`
- Raw: n=116  W=102/L=14  WR=87.9%
- Refine: exclude RSI=RSI1 drops 10/14 losers (71%)
- **Final: n=83  W=79/L=4  WR=95.2%**
- **Dir: ?**  •  HTF60 strongly against; lower third; session=london_open  •  AVOID when RSI 20-30 oversold

### W02.  `H60=H60e AND ZS=ZS2 AND session_bucket=london_open`
- Raw: n=111  W=101/L=10  WR=91.0%
- Refine: exclude RSI=RSI1 drops 9/10 losers (90%)
- **Final: n=79  W=78/L=1  WR=98.7%**
- **Dir: ?**  •  HTF60 strongly against; zscore -2 to -1 oversold; session=london_open  •  AVOID when RSI 20-30 oversold

### W03.  `H60=H60e AND BBP=BBP2 AND ZS=ZS2 AND session_bucket=london_open`
- Raw: n=111  W=101/L=10  WR=91.0%
- Refine: exclude RSI=RSI1 drops 9/10 losers (90%)
- **Final: n=79  W=78/L=1  WR=98.7%**
- **Dir: ?**  •  HTF60 strongly against; lower third; zscore -2 to -1 oversold; session=london_open  •  AVOID when RSI 20-30 oversold

### W04.  `T1=T1c AND T4=T4c AND session_bucket=ny_open`
- Raw: n=104  W=89/L=15  WR=85.6%
- Refine: exclude ZS=ZS5 drops 6/15 losers (40%)
- **Final: n=90  W=81/L=9  WR=90.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_open  •  AVOID when zscore +2 to +3 deep overbought

### W05.  `T4=T4c AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=104  W=89/L=15  WR=85.6%
- Refine: exclude ZS=ZS5 drops 6/15 losers (40%)
- **Final: n=90  W=81/L=9  WR=90.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; session=ny_open  •  AVOID when zscore +2 to +3 deep overbought

### W06.  `T1=T1c AND T4=T4c AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=104  W=89/L=15  WR=85.6%
- Refine: exclude ZS=ZS5 drops 6/15 losers (40%)
- **Final: n=90  W=81/L=9  WR=90.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_open  •  AVOID when zscore +2 to +3 deep overbought

### W07.  `H60=H60e AND T1=T1c AND BBP=BBP2 AND session_bucket=london_open`
- Raw: n=99  W=85/L=14  WR=85.9%
- Refine: exclude RSI=RSI1 drops 10/14 losers (71%)
- **Final: n=83  W=79/L=4  WR=95.2%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; lower third; session=london_open  •  AVOID when RSI 20-30 oversold

### W08.  `H60=H60e AND T4=T4c AND BBP=BBP2 AND session_bucket=london_open`
- Raw: n=99  W=85/L=14  WR=85.9%
- Refine: exclude RSI=RSI1 drops 10/14 losers (71%)
- **Final: n=83  W=79/L=4  WR=95.2%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; lower third; session=london_open  •  AVOID when RSI 20-30 oversold

### W09.  `H60=H60e AND BBP=BBP2 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=99  W=85/L=14  WR=85.9%
- Refine: exclude RSI=RSI1 drops 10/14 losers (71%)
- **Final: n=83  W=79/L=4  WR=95.2%**
- **Dir: LONG**  •  HTF60 strongly against; lower third; session=london_open  •  AVOID when RSI 20-30 oversold

### W10.  `H60=H60e AND T1=T1c AND ZS=ZS2 AND session_bucket=london_open`
- Raw: n=94  W=84/L=10  WR=89.4%
- Refine: exclude RSI=RSI1 drops 9/10 losers (90%)
- **Final: n=79  W=78/L=1  WR=98.7%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; zscore -2 to -1 oversold; session=london_open  •  AVOID when RSI 20-30 oversold

### W11.  `H60=H60e AND T4=T4c AND ZS=ZS2 AND session_bucket=london_open`
- Raw: n=94  W=84/L=10  WR=89.4%
- Refine: exclude RSI=RSI1 drops 9/10 losers (90%)
- **Final: n=79  W=78/L=1  WR=98.7%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; zscore -2 to -1 oversold; session=london_open  •  AVOID when RSI 20-30 oversold

### W12.  `H60=H60e AND ZS=ZS2 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=94  W=84/L=10  WR=89.4%
- Refine: exclude RSI=RSI1 drops 9/10 losers (90%)
- **Final: n=79  W=78/L=1  WR=98.7%**
- **Dir: LONG**  •  HTF60 strongly against; zscore -2 to -1 oversold; session=london_open  •  AVOID when RSI 20-30 oversold

### W13.  `H20=H20a AND BBP=BBP2 AND session_bucket=london`
- Raw: n=87  W=80/L=7  WR=92.0%
- Refine: exclude RSI=RSI1 drops 7/7 losers (100%)
- **Final: n=40  W=40/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; lower third; session=london  •  AVOID when RSI 20-30 oversold

### W14.  `H60=H60e AND BBP=BBP2 AND RSI=RSI2 AND session_bucket=london_open`
- Raw: n=83  W=79/L=4  WR=95.2%
- Refine: exclude ZS=ZS3 drops 3/4 losers (75%)
- **Final: n=79  W=78/L=1  WR=98.7%**
- **Dir: ?**  •  HTF60 strongly against; lower third; RSI 30-40 weak; session=london_open  •  AVOID when zscore -1 to +1 neutral

### W15.  `T1=T1c AND BBP=BBP2 AND RSI=RSI2 AND session_bucket=london_open`
- Raw: n=83  W=79/L=4  WR=95.2%
- Refine: exclude ZS=ZS3 drops 3/4 losers (75%)
- **Final: n=79  W=78/L=1  WR=98.7%**
- **Dir: ?**  •  1h trend AGAINST trade; lower third; RSI 30-40 weak; session=london_open  •  AVOID when zscore -1 to +1 neutral

### W16.  `T4=T4c AND BBP=BBP2 AND RSI=RSI2 AND session_bucket=london_open`
- Raw: n=83  W=79/L=4  WR=95.2%
- Refine: exclude ZS=ZS3 drops 3/4 losers (75%)
- **Final: n=79  W=78/L=1  WR=98.7%**
- **Dir: ?**  •  4h trend AGAINST trade; lower third; RSI 30-40 weak; session=london_open  •  AVOID when zscore -1 to +1 neutral

### W17.  `BBP=BBP2 AND RSI=RSI2 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=83  W=79/L=4  WR=95.2%
- Refine: exclude ZS=ZS3 drops 3/4 losers (75%)
- **Final: n=79  W=78/L=1  WR=98.7%**
- **Dir: LONG**  •  lower third; RSI 30-40 weak; session=london_open  •  AVOID when zscore -1 to +1 neutral

### W18.  `H20=H20a AND T1=T1c AND BBP=BBP2 AND RSI=RSI2`
- Raw: n=83  W=78/L=5  WR=94.0%
- Refine: exclude ZS=ZS3 drops 3/5 losers (60%)
- **Final: n=76  W=74/L=2  WR=97.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; lower third; RSI 30-40 weak  •  AVOID when zscore -1 to +1 neutral

### W19.  `H20=H20a AND BBP=BBP2 AND RSI=RSI2 AND direction_exec=long`
- Raw: n=83  W=78/L=5  WR=94.0%
- Refine: exclude ZS=ZS3 drops 3/5 losers (60%)
- **Final: n=76  W=74/L=2  WR=97.4%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; lower third; RSI 30-40 weak  •  AVOID when zscore -1 to +1 neutral

### W20.  `H20=H20a AND ZS=ZS2 AND session_bucket=london`
- Raw: n=81  W=74/L=7  WR=91.4%
- Refine: exclude RSI=RSI1 drops 7/7 losers (100%)
- **Final: n=34  W=34/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; zscore -2 to -1 oversold; session=london  •  AVOID when RSI 20-30 oversold

### W21.  `H20=H20a AND BBP=BBP2 AND ZS=ZS2 AND session_bucket=london`
- Raw: n=81  W=74/L=7  WR=91.4%
- Refine: exclude RSI=RSI1 drops 7/7 losers (100%)
- **Final: n=34  W=34/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; lower third; zscore -2 to -1 oversold; session=london  •  AVOID when RSI 20-30 oversold

### W22.  `H60=H60e AND RSI=RSI2 AND ZS=ZS2 AND session_bucket=london_open`
- Raw: n=79  W=78/L=1  WR=98.7%
- Refine: no further refinement
- **Final: n=79  W=78/L=1  WR=98.7%**
- **Dir: ?**  •  HTF60 strongly against; RSI 30-40 weak; zscore -2 to -1 oversold; session=london_open

### W23.  `T1=T1c AND RSI=RSI2 AND ZS=ZS2 AND session_bucket=london_open`
- Raw: n=79  W=78/L=1  WR=98.7%
- Refine: no further refinement
- **Final: n=79  W=78/L=1  WR=98.7%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 30-40 weak; zscore -2 to -1 oversold; session=london_open

### W24.  `T4=T4c AND RSI=RSI2 AND ZS=ZS2 AND session_bucket=london_open`
- Raw: n=79  W=78/L=1  WR=98.7%
- Refine: no further refinement
- **Final: n=79  W=78/L=1  WR=98.7%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 30-40 weak; zscore -2 to -1 oversold; session=london_open

### W25.  `RSI=RSI2 AND ZS=ZS2 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=79  W=78/L=1  WR=98.7%
- Refine: no further refinement
- **Final: n=79  W=78/L=1  WR=98.7%**
- **Dir: LONG**  •  RSI 30-40 weak; zscore -2 to -1 oversold; session=london_open

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND T1=T1a AND BBP=BBP2`
- Raw: n=154  W=61/L=93  WR=39.6%
- Sharpen: sharpest is RSI=RSI2 (45/93 of losers there)
- **Sharp: n=57  W=12/L=45  WR=21.1%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; lower third  •  ONLY when RSI 30-40 weak

### L02.  `H20=H20e AND BBP=BBP2 AND direction_exec=short`
- Raw: n=152  W=60/L=92  WR=39.5%
- Sharpen: sharpest is RSI=RSI2 (45/92 of losers there)
- **Sharp: n=57  W=12/L=45  WR=21.1%**
- **Dir: SHORT**  •  HTF20 strongly against; lower third  •  ONLY when RSI 30-40 weak

### L03.  `H20=H20e AND T1=T1a AND BBP=BBP2 AND direction_exec=short`
- Raw: n=152  W=60/L=92  WR=39.5%
- Sharpen: sharpest is RSI=RSI2 (45/92 of losers there)
- **Sharp: n=57  W=12/L=45  WR=21.1%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend WITH trade; lower third  •  ONLY when RSI 30-40 weak

### L04.  `H20=H20e AND T1=T1a AND ZS=ZS2`
- Raw: n=132  W=50/L=82  WR=37.9%
- Sharpen: sharpest is RSI=RSI2 (41/82 of losers there)
- **Sharp: n=47  W=6/L=41  WR=12.8%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; zscore -2 to -1 oversold  •  ONLY when RSI 30-40 weak

### L05.  `H20=H20e AND T1=T1a AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=132  W=50/L=82  WR=37.9%
- Sharpen: sharpest is RSI=RSI2 (41/82 of losers there)
- **Sharp: n=47  W=6/L=41  WR=12.8%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; lower third; zscore -2 to -1 oversold  •  ONLY when RSI 30-40 weak

### L06.  `H20=H20e AND ZS=ZS2 AND direction_exec=short`
- Raw: n=131  W=49/L=82  WR=37.4%
- Sharpen: sharpest is RSI=RSI2 (41/82 of losers there)
- **Sharp: n=47  W=6/L=41  WR=12.8%**
- **Dir: SHORT**  •  HTF20 strongly against; zscore -2 to -1 oversold  •  ONLY when RSI 30-40 weak

### L07.  `H20=H20e AND T1=T1a AND ZS=ZS2 AND direction_exec=short`
- Raw: n=131  W=49/L=82  WR=37.4%
- Sharpen: sharpest is RSI=RSI2 (41/82 of losers there)
- **Sharp: n=47  W=6/L=41  WR=12.8%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend WITH trade; zscore -2 to -1 oversold  •  ONLY when RSI 30-40 weak

### L08.  `H20=H20e AND BBP=BBP2 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=131  W=49/L=82  WR=37.4%
- Sharpen: sharpest is RSI=RSI2 (41/82 of losers there)
- **Sharp: n=47  W=6/L=41  WR=12.8%**
- **Dir: SHORT**  •  HTF20 strongly against; lower third; zscore -2 to -1 oversold  •  ONLY when RSI 30-40 weak

### L09.  `T1=T1a AND RSI=RSI2 AND session_bucket=london_open`
- Raw: n=130  W=47/L=83  WR=36.2%
- Sharpen: sharpest is ZS=ZS2 (38/83 of losers there)
- **Sharp: n=39  W=1/L=38  WR=2.6%**
- **Dir: ?**  •  1h trend WITH trade; RSI 30-40 weak; session=london_open  •  ONLY when zscore -2 to -1 oversold

### L10.  `T4=T4a AND RSI=RSI2 AND session_bucket=london_open`
- Raw: n=130  W=47/L=83  WR=36.2%
- Sharpen: sharpest is ZS=ZS2 (38/83 of losers there)
- **Sharp: n=39  W=1/L=38  WR=2.6%**
- **Dir: ?**  •  4h trend WITH trade; RSI 30-40 weak; session=london_open  •  ONLY when zscore -2 to -1 oversold

### L11.  `RSI=RSI2 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=130  W=47/L=83  WR=36.2%
- Sharpen: sharpest is ZS=ZS2 (38/83 of losers there)
- **Sharp: n=39  W=1/L=38  WR=2.6%**
- **Dir: SHORT**  •  RSI 30-40 weak; session=london_open  •  ONLY when zscore -2 to -1 oversold

### L12.  `T1=T1a AND T4=T4a AND RSI=RSI2 AND session_bucket=london_open`
- Raw: n=130  W=47/L=83  WR=36.2%
- Sharpen: sharpest is ZS=ZS2 (38/83 of losers there)
- **Sharp: n=39  W=1/L=38  WR=2.6%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 30-40 weak; session=london_open  •  ONLY when zscore -2 to -1 oversold

### L13.  `T1=T1a AND RSI=RSI2 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=130  W=47/L=83  WR=36.2%
- Sharpen: sharpest is ZS=ZS2 (38/83 of losers there)
- **Sharp: n=39  W=1/L=38  WR=2.6%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 30-40 weak; session=london_open  •  ONLY when zscore -2 to -1 oversold

### L14.  `T4=T4a AND RSI=RSI2 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=130  W=47/L=83  WR=36.2%
- Sharpen: sharpest is ZS=ZS2 (38/83 of losers there)
- **Sharp: n=39  W=1/L=38  WR=2.6%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 30-40 weak; session=london_open  •  ONLY when zscore -2 to -1 oversold

### L15.  `H20=H20e AND T4=T4a AND BBP=BBP2`
- Raw: n=123  W=47/L=76  WR=38.2%
- Sharpen: sharpest is RSI=RSI2 (35/76 of losers there)
- **Sharp: n=44  W=9/L=35  WR=20.5%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; lower third  •  ONLY when RSI 30-40 weak

### L16.  `H20=H20e AND T1=T1a AND T4=T4a AND BBP=BBP2`
- Raw: n=123  W=47/L=76  WR=38.2%
- Sharpen: sharpest is RSI=RSI2 (35/76 of losers there)
- **Sharp: n=44  W=9/L=35  WR=20.5%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend WITH trade; lower third  •  ONLY when RSI 30-40 weak

### L17.  `H20=H20e AND T4=T4a AND BBP=BBP2 AND direction_exec=short`
- Raw: n=123  W=47/L=76  WR=38.2%
- Sharpen: sharpest is RSI=RSI2 (35/76 of losers there)
- **Sharp: n=44  W=9/L=35  WR=20.5%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend WITH trade; lower third  •  ONLY when RSI 30-40 weak

### L18.  `H60=H60a AND T1=T1a AND RSI=RSI2 AND session_bucket=london_open`
- Raw: n=121  W=46/L=75  WR=38.0%
- Sharpen: sharpest is ZS=ZS2 (38/75 of losers there)
- **Sharp: n=39  W=1/L=38  WR=2.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 30-40 weak; session=london_open  •  ONLY when zscore -2 to -1 oversold

### L19.  `H60=H60a AND T4=T4a AND RSI=RSI2 AND session_bucket=london_open`
- Raw: n=121  W=46/L=75  WR=38.0%
- Sharpen: sharpest is ZS=ZS2 (38/75 of losers there)
- **Sharp: n=39  W=1/L=38  WR=2.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 30-40 weak; session=london_open  •  ONLY when zscore -2 to -1 oversold

### L20.  `H60=H60a AND RSI=RSI2 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=121  W=46/L=75  WR=38.0%
- Sharpen: sharpest is ZS=ZS2 (38/75 of losers there)
- **Sharp: n=39  W=1/L=38  WR=2.6%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; RSI 30-40 weak; session=london_open  •  ONLY when zscore -2 to -1 oversold

### L21.  `H20=H20e AND H60=H60e AND T1=T1c AND ZS=ZS1`
- Raw: n=104  W=40/L=64  WR=38.5%
- Sharpen: sharpest is BBP=BBP0 (31/64 of losers there)
- **Sharp: n=37  W=6/L=31  WR=16.2%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when deep below lower band

### L22.  `H20=H20e AND T4=T4a AND ZS=ZS2`
- Raw: n=102  W=36/L=66  WR=35.3%
- Sharpen: sharpest is RSI=RSI2 (31/66 of losers there)
- **Sharp: n=34  W=3/L=31  WR=8.8%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; zscore -2 to -1 oversold  •  ONLY when RSI 30-40 weak

### L23.  `H20=H20e AND T1=T1a AND T4=T4a AND ZS=ZS2`
- Raw: n=102  W=36/L=66  WR=35.3%
- Sharpen: sharpest is RSI=RSI2 (31/66 of losers there)
- **Sharp: n=34  W=3/L=31  WR=8.8%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend WITH trade; zscore -2 to -1 oversold  •  ONLY when RSI 30-40 weak

### L24.  `H20=H20e AND T4=T4a AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=102  W=36/L=66  WR=35.3%
- Sharpen: sharpest is RSI=RSI2 (31/66 of losers there)
- **Sharp: n=34  W=3/L=31  WR=8.8%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; lower third; zscore -2 to -1 oversold  •  ONLY when RSI 30-40 weak

### L25.  `H20=H20e AND T4=T4a AND ZS=ZS2 AND direction_exec=short`
- Raw: n=102  W=36/L=66  WR=35.3%
- Sharpen: sharpest is RSI=RSI2 (31/66 of losers there)
- **Sharp: n=34  W=3/L=31  WR=8.8%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend WITH trade; zscore -2 to -1 oversold  •  ONLY when RSI 30-40 weak

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(38/28) | H20e(30/40) |
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
