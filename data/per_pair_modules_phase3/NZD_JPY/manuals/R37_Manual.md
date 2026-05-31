# NZD_JPY — R37 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **3,238**  (W=2,059 / L=1,179)  -  WR: **63.6%**

## Session distribution

- asia: n=1351  W=842/L=509  WR=62.3%
- london_open: n=435  W=281/L=154  WR=64.6%
- ny_close: n=413  W=274/L=139  WR=66.3%
- ny_mid: n=383  W=232/L=151  WR=60.6%
- ny_open: n=200  W=134/L=66  WR=67.0%
- london: n=184  W=126/L=58  WR=68.5%
- asia_late: n=160  W=95/L=65  WR=59.4%
- off_hours: n=112  W=75/L=37  WR=67.0%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T4=T4a AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=133  W=119/L=14  WR=89.5%
- Refine: exclude ZS=ZS4 drops 12/14 losers (86%)
- **Final: n=75  W=73/L=2  WR=97.3%**
- **Dir: ?**  •  4h trend WITH trade; RSI 60-70 strong; session=london_open  •  AVOID when zscore +1 to +2 overbought

### W02.  `RSI=RSI5 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=133  W=119/L=14  WR=89.5%
- Refine: exclude ZS=ZS4 drops 12/14 losers (86%)
- **Final: n=75  W=73/L=2  WR=97.3%**
- **Dir: LONG**  •  RSI 60-70 strong; session=london_open  •  AVOID when zscore +1 to +2 overbought

### W03.  `T4=T4a AND RSI=RSI5 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=133  W=119/L=14  WR=89.5%
- Refine: exclude ZS=ZS4 drops 12/14 losers (86%)
- **Final: n=75  W=73/L=2  WR=97.3%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 60-70 strong; session=london_open  •  AVOID when zscore +1 to +2 overbought

### W04.  `H60=H60a AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=131  W=119/L=12  WR=90.8%
- Refine: exclude ZS=ZS4 drops 11/12 losers (92%)
- **Final: n=74  W=73/L=1  WR=98.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 60-70 strong; session=london_open  •  AVOID when zscore +1 to +2 overbought

### W05.  `H60=H60a AND T4=T4a AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=131  W=119/L=12  WR=90.8%
- Refine: exclude ZS=ZS4 drops 11/12 losers (92%)
- **Final: n=74  W=73/L=1  WR=98.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 60-70 strong; session=london_open  •  AVOID when zscore +1 to +2 overbought

### W06.  `H60=H60a AND RSI=RSI5 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=131  W=119/L=12  WR=90.8%
- Refine: exclude ZS=ZS4 drops 11/12 losers (92%)
- **Final: n=74  W=73/L=1  WR=98.6%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 60-70 strong; session=london_open  •  AVOID when zscore +1 to +2 overbought

### W07.  `T1=T1a AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=129  W=114/L=15  WR=88.4%
- Refine: exclude ZS=ZS4 drops 12/15 losers (80%)
- **Final: n=72  W=69/L=3  WR=95.8%**
- **Dir: ?**  •  1h trend WITH trade; RSI 60-70 strong; session=london_open  •  AVOID when zscore +1 to +2 overbought

### W08.  `T1=T1a AND T4=T4a AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=127  W=114/L=13  WR=89.8%
- Refine: exclude ZS=ZS4 drops 11/13 losers (85%)
- **Final: n=71  W=69/L=2  WR=97.2%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 60-70 strong; session=london_open  •  AVOID when zscore +1 to +2 overbought

### W09.  `T1=T1a AND RSI=RSI5 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=127  W=114/L=13  WR=89.8%
- Refine: exclude ZS=ZS4 drops 11/13 losers (85%)
- **Final: n=71  W=69/L=2  WR=97.2%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 60-70 strong; session=london_open  •  AVOID when zscore +1 to +2 overbought

### W10.  `H60=H60a AND T1=T1a AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=125  W=114/L=11  WR=91.2%
- Refine: exclude ZS=ZS4 drops 10/11 losers (91%)
- **Final: n=70  W=69/L=1  WR=98.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong; session=london_open  •  AVOID when zscore +1 to +2 overbought

### W11.  `H20=H20a AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=105  W=93/L=12  WR=88.6%
- Refine: exclude ZS=ZS4 drops 11/12 losers (92%)
- **Final: n=52  W=51/L=1  WR=98.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 60-70 strong; session=london_open  •  AVOID when zscore +1 to +2 overbought

### W12.  `H20=H20a AND H60=H60a AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=105  W=93/L=12  WR=88.6%
- Refine: exclude ZS=ZS4 drops 11/12 losers (92%)
- **Final: n=52  W=51/L=1  WR=98.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 60-70 strong; session=london_open  •  AVOID when zscore +1 to +2 overbought

### W13.  `H20=H20a AND T4=T4a AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=105  W=93/L=12  WR=88.6%
- Refine: exclude ZS=ZS4 drops 11/12 losers (92%)
- **Final: n=52  W=51/L=1  WR=98.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 60-70 strong; session=london_open  •  AVOID when zscore +1 to +2 overbought

### W14.  `H20=H20a AND RSI=RSI5 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=105  W=93/L=12  WR=88.6%
- Refine: exclude ZS=ZS4 drops 11/12 losers (92%)
- **Final: n=52  W=51/L=1  WR=98.1%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 60-70 strong; session=london_open  •  AVOID when zscore +1 to +2 overbought

### W15.  `T4=T4a AND direction_exec=long AND session_bucket=london`
- Raw: n=100  W=85/L=15  WR=85.0%
- Refine: exclude RSI=RSI4 drops 12/15 losers (80%)
- **Final: n=59  W=56/L=3  WR=94.9%**
- **Dir: LONG**  •  4h trend WITH trade; session=london  •  AVOID when RSI 50-60 upper neutral

### W16.  `H20=H20a AND T1=T1a AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=99  W=88/L=11  WR=88.9%
- Refine: exclude ZS=ZS4 drops 10/11 losers (91%)
- **Final: n=48  W=47/L=1  WR=97.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong; session=london_open  •  AVOID when zscore +1 to +2 overbought

### W17.  `T1=T1a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=95  W=82/L=13  WR=86.3%
- Refine: exclude ZS=ZS3 drops 6/13 losers (46%)
- **Final: n=86  W=79/L=7  WR=91.9%**
- **Dir: LONG**  •  1h trend WITH trade; session=ny_open  •  AVOID when zscore -1 to +1 neutral

### W18.  `T1=T1a AND T4=T4a AND session_bucket=ny_open`
- Raw: n=93  W=82/L=11  WR=88.2%
- Refine: exclude ZS=ZS3 drops 5/11 losers (45%)
- **Final: n=85  W=79/L=6  WR=92.9%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; session=ny_open  •  AVOID when zscore -1 to +1 neutral

### W19.  `T1=T1a AND T4=T4a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=93  W=82/L=11  WR=88.2%
- Refine: exclude ZS=ZS3 drops 5/11 losers (45%)
- **Final: n=85  W=79/L=6  WR=92.9%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; session=ny_open  •  AVOID when zscore -1 to +1 neutral

### W20.  `T1=T1c AND T4=T4a AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=92  W=79/L=13  WR=85.9%
- Refine: exclude H20=H20e drops 7/13 losers (54%)
- **Final: n=70  W=64/L=6  WR=91.4%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 50-60 upper neutral; session=asia  •  AVOID when HTF20 strongly against

### W21.  `H60=H60a AND T1=T1a AND session_bucket=ny_open`
- Raw: n=89  W=79/L=10  WR=88.8%
- Refine: exclude RSI=RSI4 drops 7/10 losers (70%)
- **Final: n=55  W=52/L=3  WR=94.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=ny_open  •  AVOID when RSI 50-60 upper neutral

### W22.  `H60=H60a AND T1=T1a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=89  W=79/L=10  WR=88.8%
- Refine: exclude RSI=RSI4 drops 7/10 losers (70%)
- **Final: n=55  W=52/L=3  WR=94.5%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=ny_open  •  AVOID when RSI 50-60 upper neutral

### W23.  `H60=H60a AND T1=T1a AND T4=T4a AND session_bucket=ny_open`
- Raw: n=87  W=79/L=8  WR=90.8%
- Refine: exclude H20=H20c drops 3/8 losers (38%)
- **Final: n=83  W=78/L=5  WR=94.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; session=ny_open  •  AVOID when HTF20 neutral

### W24.  `H60=H60a AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=87  W=77/L=10  WR=88.5%
- Refine: exclude H20=H20a drops 10/10 losers (100%)
- **Final: n=44  W=44/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 60-70 strong; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

### W25.  `T1=T1a AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=87  W=77/L=10  WR=88.5%
- Refine: exclude H20=H20a drops 10/10 losers (100%)
- **Final: n=44  W=44/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; RSI 60-70 strong; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20d AND T1=T1c AND T4=T4c`
- Raw: n=97  W=38/L=59  WR=39.2%
- Sharpen: sharpest is session_bucket=ny_mid (30/59 of losers there)
- **Sharp: n=30  W=0/L=30  WR=0.0%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when session=ny_mid

### L02.  `H20=H20d AND H60=H60e AND T1=T1c AND T4=T4c`
- Raw: n=97  W=38/L=59  WR=39.2%
- Sharpen: sharpest is session_bucket=ny_mid (30/59 of losers there)
- **Sharp: n=30  W=0/L=30  WR=0.0%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when session=ny_mid

### L03.  `H20=H20d AND T1=T1c AND T4=T4c AND direction_exec=short`
- Raw: n=97  W=38/L=59  WR=39.2%
- Sharpen: sharpest is session_bucket=ny_mid (30/59 of losers there)
- **Sharp: n=30  W=0/L=30  WR=0.0%**
- **Dir: SHORT**  •  HTF20 mildly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when session=ny_mid

### L04.  `T1=T1c AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=93  W=35/L=58  WR=37.6%
- Sharpen: sharpest is ZS=ZS5 (25/58 of losers there)
- **Sharp: n=29  W=4/L=25  WR=13.8%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 60-70 strong; session=london_open  •  ONLY when zscore +2 to +3 deep overbought

### L05.  `H60=H60a AND T4=T4a AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=90  W=35/L=55  WR=38.9%
- Sharpen: sharpest is ZS=ZS4 (28/55 of losers there)
- **Sharp: n=28  W=0/L=28  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral; session=ny_mid  •  ONLY when zscore +1 to +2 overbought

### L06.  `T1=T1a AND T4=T4a AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=90  W=35/L=55  WR=38.9%
- Sharpen: sharpest is ZS=ZS4 (28/55 of losers there)
- **Sharp: n=28  W=0/L=28  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral; session=ny_mid  •  ONLY when zscore +1 to +2 overbought

### L07.  `T4=T4a AND RSI=RSI4 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=90  W=35/L=55  WR=38.9%
- Sharpen: sharpest is ZS=ZS4 (28/55 of losers there)
- **Sharp: n=28  W=0/L=28  WR=0.0%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 50-60 upper neutral; session=ny_mid  •  ONLY when zscore +1 to +2 overbought

### L08.  `T4=T4c AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=89  W=30/L=59  WR=33.7%
- Sharpen: sharpest is ZS=ZS5 (26/59 of losers there)
- **Sharp: n=26  W=0/L=26  WR=0.0%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 60-70 strong; session=london_open  •  ONLY when zscore +2 to +3 deep overbought

### L09.  `RSI=RSI5 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=89  W=30/L=59  WR=33.7%
- Sharpen: sharpest is ZS=ZS5 (26/59 of losers there)
- **Sharp: n=26  W=0/L=26  WR=0.0%**
- **Dir: SHORT**  •  RSI 60-70 strong; session=london_open  •  ONLY when zscore +2 to +3 deep overbought

### L10.  `T4=T4c AND RSI=RSI5 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=89  W=30/L=59  WR=33.7%
- Sharpen: sharpest is ZS=ZS5 (26/59 of losers there)
- **Sharp: n=26  W=0/L=26  WR=0.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 60-70 strong; session=london_open  •  ONLY when zscore +2 to +3 deep overbought

### L11.  `H60=H60e AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=87  W=28/L=59  WR=32.2%
- Sharpen: sharpest is ZS=ZS5 (26/59 of losers there)
- **Sharp: n=26  W=0/L=26  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; RSI 60-70 strong; session=london_open  •  ONLY when zscore +2 to +3 deep overbought

### L12.  `H60=H60e AND T4=T4c AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=87  W=28/L=59  WR=32.2%
- Sharpen: sharpest is ZS=ZS5 (26/59 of losers there)
- **Sharp: n=26  W=0/L=26  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 60-70 strong; session=london_open  •  ONLY when zscore +2 to +3 deep overbought

### L13.  `H60=H60e AND RSI=RSI5 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=87  W=28/L=59  WR=32.2%
- Sharpen: sharpest is ZS=ZS5 (26/59 of losers there)
- **Sharp: n=26  W=0/L=26  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 60-70 strong; session=london_open  •  ONLY when zscore +2 to +3 deep overbought

### L14.  `T1=T1c AND T4=T4c AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=87  W=30/L=57  WR=34.5%
- Sharpen: sharpest is ZS=ZS5 (25/57 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 60-70 strong; session=london_open  •  ONLY when zscore +2 to +3 deep overbought

### L15.  `T1=T1c AND RSI=RSI5 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=87  W=30/L=57  WR=34.5%
- Sharpen: sharpest is ZS=ZS5 (25/57 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 60-70 strong; session=london_open  •  ONLY when zscore +2 to +3 deep overbought

### L16.  `H60=H60e AND T1=T1c AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=85  W=28/L=57  WR=32.9%
- Sharpen: sharpest is ZS=ZS5 (25/57 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 60-70 strong; session=london_open  •  ONLY when zscore +2 to +3 deep overbought

### L17.  `H60=H60e AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=62  W=12/L=50  WR=19.4%
- Sharpen: sharpest is H20=H20d (30/50 of losers there)
- **Sharp: n=30  W=0/L=30  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; RSI 60-70 strong; session=ny_mid  •  ONLY when HTF20 mildly against

### L18.  `T1=T1c AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=62  W=12/L=50  WR=19.4%
- Sharpen: sharpest is H20=H20d (30/50 of losers there)
- **Sharp: n=30  W=0/L=30  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 60-70 strong; session=ny_mid  •  ONLY when HTF20 mildly against

### L19.  `T4=T4c AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=62  W=12/L=50  WR=19.4%
- Sharpen: sharpest is H20=H20d (30/50 of losers there)
- **Sharp: n=30  W=0/L=30  WR=0.0%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 60-70 strong; session=ny_mid  •  ONLY when HTF20 mildly against

### L20.  `RSI=RSI5 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=62  W=12/L=50  WR=19.4%
- Sharpen: sharpest is H20=H20d (30/50 of losers there)
- **Sharp: n=30  W=0/L=30  WR=0.0%**
- **Dir: SHORT**  •  RSI 60-70 strong; session=ny_mid  •  ONLY when HTF20 mildly against

### L21.  `H60=H60e AND T1=T1c AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=62  W=12/L=50  WR=19.4%
- Sharpen: sharpest is H20=H20d (30/50 of losers there)
- **Sharp: n=30  W=0/L=30  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 60-70 strong; session=ny_mid  •  ONLY when HTF20 mildly against

### L22.  `H60=H60e AND T4=T4c AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=62  W=12/L=50  WR=19.4%
- Sharpen: sharpest is H20=H20d (30/50 of losers there)
- **Sharp: n=30  W=0/L=30  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 60-70 strong; session=ny_mid  •  ONLY when HTF20 mildly against

### L23.  `H60=H60e AND RSI=RSI5 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=62  W=12/L=50  WR=19.4%
- Sharpen: sharpest is H20=H20d (30/50 of losers there)
- **Sharp: n=30  W=0/L=30  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 60-70 strong; session=ny_mid  •  ONLY when HTF20 mildly against

### L24.  `T1=T1c AND T4=T4c AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=62  W=12/L=50  WR=19.4%
- Sharpen: sharpest is H20=H20d (30/50 of losers there)
- **Sharp: n=30  W=0/L=30  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 60-70 strong; session=ny_mid  •  ONLY when HTF20 mildly against

### L25.  `T1=T1c AND RSI=RSI5 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=62  W=12/L=50  WR=19.4%
- Sharpen: sharpest is H20=H20d (30/50 of losers there)
- **Sharp: n=30  W=0/L=30  WR=0.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 60-70 strong; session=ny_mid  •  ONLY when HTF20 mildly against

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | H60a(50/42) | H60e(45/52) |
| T1 | T1a(51/46) | T1c(49/54) |
| T4 | T4a(54/46) | T4c(46/54) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(52/46) | short(48/54) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
