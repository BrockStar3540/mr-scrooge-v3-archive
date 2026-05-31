# AUD_JPY — R31 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **3,342**  (W=2,113 / L=1,229)  -  WR: **63.2%**

## Session distribution

- asia: n=975  W=623/L=352  WR=63.9%
- ny_mid: n=775  W=472/L=303  WR=60.9%
- london_open: n=397  W=259/L=138  WR=65.2%
- london: n=333  W=204/L=129  WR=61.3%
- ny_close: n=314  W=200/L=114  WR=63.7%
- ny_open: n=271  W=186/L=85  WR=68.6%
- asia_late: n=182  W=119/L=63  WR=65.4%
- off_hours: n=95  W=50/L=45  WR=52.6%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60a AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=321  W=284/L=37  WR=88.5%
- Refine: exclude BBP=BBP4 drops 27/37 losers (73%)
- **Final: n=136  W=126/L=10  WR=92.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 60-70 strong; session=asia  •  AVOID when upper third

### W02.  `RSI=RSI5 AND direction_exec=long AND session_bucket=asia`
- Raw: n=321  W=284/L=37  WR=88.5%
- Refine: exclude BBP=BBP4 drops 27/37 losers (73%)
- **Final: n=136  W=126/L=10  WR=92.6%**
- **Dir: LONG**  •  RSI 60-70 strong; session=asia  •  AVOID when upper third

### W03.  `H60=H60a AND RSI=RSI5 AND direction_exec=long AND session_bucket=asia`
- Raw: n=321  W=284/L=37  WR=88.5%
- Refine: exclude BBP=BBP4 drops 27/37 losers (73%)
- **Final: n=136  W=126/L=10  WR=92.6%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 60-70 strong; session=asia  •  AVOID when upper third

### W04.  `T1=T1a AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=319  W=288/L=31  WR=90.3%
- Refine: exclude T4=T4a drops 30/31 losers (97%)
- **Final: n=84  W=83/L=1  WR=98.8%**
- **Dir: ?**  •  1h trend WITH trade; RSI 60-70 strong; session=asia  •  AVOID when 4h trend WITH trade

### W05.  `H60=H60a AND T1=T1a AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=315  W=284/L=31  WR=90.2%
- Refine: exclude BBP=BBP4 drops 25/31 losers (81%)
- **Final: n=132  W=126/L=6  WR=95.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong; session=asia  •  AVOID when upper third

### W06.  `T1=T1a AND RSI=RSI5 AND direction_exec=long AND session_bucket=asia`
- Raw: n=315  W=284/L=31  WR=90.2%
- Refine: exclude BBP=BBP4 drops 25/31 losers (81%)
- **Final: n=132  W=126/L=6  WR=95.5%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 60-70 strong; session=asia  •  AVOID when upper third

### W07.  `H20=H20a AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=313  W=279/L=34  WR=89.1%
- Refine: exclude BBP=BBP4 drops 26/34 losers (76%)
- **Final: n=134  W=126/L=8  WR=94.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 60-70 strong; session=asia  •  AVOID when upper third

### W08.  `H20=H20a AND H60=H60a AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=311  W=277/L=34  WR=89.1%
- Refine: exclude BBP=BBP4 drops 26/34 losers (76%)
- **Final: n=134  W=126/L=8  WR=94.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 60-70 strong; session=asia  •  AVOID when upper third

### W09.  `H20=H20a AND RSI=RSI5 AND direction_exec=long AND session_bucket=asia`
- Raw: n=311  W=277/L=34  WR=89.1%
- Refine: exclude BBP=BBP4 drops 26/34 losers (76%)
- **Final: n=134  W=126/L=8  WR=94.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 60-70 strong; session=asia  •  AVOID when upper third

### W10.  `H20=H20a AND T1=T1a AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=305  W=277/L=28  WR=90.8%
- Refine: exclude BBP=BBP4 drops 24/28 losers (86%)
- **Final: n=130  W=126/L=4  WR=96.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong; session=asia  •  AVOID when upper third

### W11.  `H60=H60a AND T4=T4a AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=237  W=205/L=32  WR=86.5%
- Refine: exclude BBP=BBP4 drops 26/32 losers (81%)
- **Final: n=92  W=86/L=6  WR=93.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 60-70 strong; session=asia  •  AVOID when upper third

### W12.  `T4=T4a AND RSI=RSI5 AND direction_exec=long AND session_bucket=asia`
- Raw: n=237  W=205/L=32  WR=86.5%
- Refine: exclude BBP=BBP4 drops 26/32 losers (81%)
- **Final: n=92  W=86/L=6  WR=93.5%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 60-70 strong; session=asia  •  AVOID when upper third

### W13.  `T1=T1a AND T4=T4a AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=235  W=205/L=30  WR=87.2%
- Refine: exclude BBP=BBP4 drops 24/30 losers (80%)
- **Final: n=92  W=86/L=6  WR=93.5%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 60-70 strong; session=asia  •  AVOID when upper third

### W14.  `H20=H20a AND T4=T4a AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=227  W=198/L=29  WR=87.2%
- Refine: exclude BBP=BBP4 drops 25/29 losers (86%)
- **Final: n=90  W=86/L=4  WR=95.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 60-70 strong; session=asia  •  AVOID when upper third

### W15.  `H20=H20a AND T4=T4c AND RSI=RSI5`
- Raw: n=224  W=198/L=26  WR=88.4%
- Refine: exclude session_bucket=ny_mid drops 11/26 losers (42%)
- **Final: n=172  W=157/L=15  WR=91.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when session=ny_mid

### W16.  `T1=T1a AND T4=T4c AND RSI=RSI5`
- Raw: n=218  W=195/L=23  WR=89.4%
- Refine: exclude session_bucket=london drops 10/23 losers (43%)
- **Final: n=176  W=163/L=13  WR=92.6%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when session=london

### W17.  `H60=H60a AND T4=T4c AND RSI=RSI5`
- Raw: n=218  W=191/L=27  WR=87.6%
- Refine: exclude session_bucket=london drops 10/27 losers (37%)
- **Final: n=176  W=159/L=17  WR=90.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when session=london

### W18.  `T4=T4c AND RSI=RSI5 AND direction_exec=long`
- Raw: n=218  W=191/L=27  WR=87.6%
- Refine: exclude session_bucket=london drops 10/27 losers (37%)
- **Final: n=176  W=159/L=17  WR=90.3%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when session=london

### W19.  `H60=H60a AND T4=T4c AND RSI=RSI5 AND direction_exec=long`
- Raw: n=218  W=191/L=27  WR=87.6%
- Refine: exclude session_bucket=london drops 10/27 losers (37%)
- **Final: n=176  W=159/L=17  WR=90.3%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when session=london

### W20.  `H20=H20a AND H60=H60a AND T4=T4c AND RSI=RSI5`
- Raw: n=217  W=191/L=26  WR=88.0%
- Refine: exclude session_bucket=london drops 10/26 losers (38%)
- **Final: n=175  W=159/L=16  WR=90.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when session=london

### W21.  `H20=H20a AND T4=T4c AND RSI=RSI5 AND direction_exec=long`
- Raw: n=217  W=191/L=26  WR=88.0%
- Refine: exclude session_bucket=london drops 10/26 losers (38%)
- **Final: n=175  W=159/L=16  WR=90.9%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when session=london

### W22.  `H60=H60a AND T1=T1a AND T4=T4c AND RSI=RSI5`
- Raw: n=214  W=191/L=23  WR=89.3%
- Refine: exclude session_bucket=london drops 10/23 losers (43%)
- **Final: n=172  W=159/L=13  WR=92.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when session=london

### W23.  `T1=T1a AND T4=T4c AND RSI=RSI5 AND direction_exec=long`
- Raw: n=214  W=191/L=23  WR=89.3%
- Refine: exclude session_bucket=london drops 10/23 losers (43%)
- **Final: n=172  W=159/L=13  WR=92.4%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when session=london

### W24.  `H20=H20a AND T1=T1a AND T4=T4c AND RSI=RSI5`
- Raw: n=213  W=191/L=22  WR=89.7%
- Refine: exclude session_bucket=london drops 10/22 losers (45%)
- **Final: n=171  W=159/L=12  WR=93.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when session=london

### W25.  `T1=T1a AND BBP=BBP4 AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=187  W=162/L=25  WR=86.6%
- Refine: exclude T4=T4a drops 24/25 losers (96%)
- **Final: n=44  W=43/L=1  WR=97.7%**
- **Dir: ?**  •  1h trend WITH trade; upper third; RSI 60-70 strong; session=asia  •  AVOID when 4h trend WITH trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=242  W=81/L=161  WR=33.5%
- Sharpen: sharpest is ZS=ZS5 (67/161 of losers there)
- **Sharp: n=73  W=6/L=67  WR=8.2%**
- **Dir: ?**  •  HTF60 strongly against; RSI 60-70 strong; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L02.  `RSI=RSI5 AND direction_exec=short AND session_bucket=asia`
- Raw: n=242  W=81/L=161  WR=33.5%
- Sharpen: sharpest is ZS=ZS5 (67/161 of losers there)
- **Sharp: n=73  W=6/L=67  WR=8.2%**
- **Dir: SHORT**  •  RSI 60-70 strong; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L03.  `H60=H60e AND RSI=RSI5 AND direction_exec=short AND session_bucket=asia`
- Raw: n=242  W=81/L=161  WR=33.5%
- Sharpen: sharpest is ZS=ZS5 (67/161 of losers there)
- **Sharp: n=73  W=6/L=67  WR=8.2%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 60-70 strong; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L04.  `H60=H60e AND T4=T4a AND direction_exec=short`
- Raw: n=242  W=91/L=151  WR=37.6%
- Sharpen: sharpest is RSI=RSI5 (118/151 of losers there)
- **Sharp: n=156  W=38/L=118  WR=24.4%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend WITH trade  •  ONLY when RSI 60-70 strong

### L05.  `H20=H20e AND H60=H60e AND T4=T4a`
- Raw: n=238  W=87/L=151  WR=36.6%
- Sharpen: sharpest is RSI=RSI5 (118/151 of losers there)
- **Sharp: n=154  W=36/L=118  WR=23.4%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend WITH trade  •  ONLY when RSI 60-70 strong

### L06.  `H20=H20e AND T4=T4a AND direction_exec=short`
- Raw: n=238  W=87/L=151  WR=36.6%
- Sharpen: sharpest is RSI=RSI5 (118/151 of losers there)
- **Sharp: n=154  W=36/L=118  WR=23.4%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend WITH trade  •  ONLY when RSI 60-70 strong

### L07.  `H20=H20e AND H60=H60e AND T4=T4a AND direction_exec=short`
- Raw: n=238  W=87/L=151  WR=36.6%
- Sharpen: sharpest is RSI=RSI5 (118/151 of losers there)
- **Sharp: n=154  W=36/L=118  WR=23.4%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; 4h trend WITH trade  •  ONLY when RSI 60-70 strong

### L08.  `H20=H20e AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=237  W=75/L=162  WR=31.6%
- Sharpen: sharpest is ZS=ZS5 (67/162 of losers there)
- **Sharp: n=73  W=6/L=67  WR=8.2%**
- **Dir: ?**  •  HTF20 strongly against; RSI 60-70 strong; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L09.  `H20=H20e AND H60=H60e AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=235  W=74/L=161  WR=31.5%
- Sharpen: sharpest is ZS=ZS5 (67/161 of losers there)
- **Sharp: n=73  W=6/L=67  WR=8.2%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 60-70 strong; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L10.  `H20=H20e AND RSI=RSI5 AND direction_exec=short AND session_bucket=asia`
- Raw: n=235  W=74/L=161  WR=31.5%
- Sharpen: sharpest is ZS=ZS5 (67/161 of losers there)
- **Sharp: n=73  W=6/L=67  WR=8.2%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 60-70 strong; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L11.  `H60=H60e AND T1=T1c AND T4=T4a`
- Raw: n=231  W=81/L=150  WR=35.1%
- Sharpen: sharpest is RSI=RSI5 (117/150 of losers there)
- **Sharp: n=145  W=28/L=117  WR=19.3%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when RSI 60-70 strong

### L12.  `T1=T1c AND T4=T4a AND direction_exec=short`
- Raw: n=231  W=81/L=150  WR=35.1%
- Sharpen: sharpest is RSI=RSI5 (117/150 of losers there)
- **Sharp: n=145  W=28/L=117  WR=19.3%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when RSI 60-70 strong

### L13.  `H60=H60e AND T1=T1c AND T4=T4a AND direction_exec=short`
- Raw: n=231  W=81/L=150  WR=35.1%
- Sharpen: sharpest is RSI=RSI5 (117/150 of losers there)
- **Sharp: n=145  W=28/L=117  WR=19.3%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when RSI 60-70 strong

### L14.  `T1=T1c AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=229  W=67/L=162  WR=29.3%
- Sharpen: sharpest is ZS=ZS5 (67/162 of losers there)
- **Sharp: n=73  W=6/L=67  WR=8.2%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 60-70 strong; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L15.  `H60=H60e AND T1=T1c AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=227  W=67/L=160  WR=29.5%
- Sharpen: sharpest is ZS=ZS5 (67/160 of losers there)
- **Sharp: n=73  W=6/L=67  WR=8.2%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 60-70 strong; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L16.  `T1=T1c AND RSI=RSI5 AND direction_exec=short AND session_bucket=asia`
- Raw: n=227  W=67/L=160  WR=29.5%
- Sharpen: sharpest is ZS=ZS5 (67/160 of losers there)
- **Sharp: n=73  W=6/L=67  WR=8.2%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 60-70 strong; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L17.  `H20=H20e AND T1=T1c AND T4=T4a`
- Raw: n=227  W=77/L=150  WR=33.9%
- Sharpen: sharpest is RSI=RSI5 (117/150 of losers there)
- **Sharp: n=143  W=26/L=117  WR=18.2%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when RSI 60-70 strong

### L18.  `H20=H20e AND H60=H60e AND T1=T1c AND T4=T4a`
- Raw: n=227  W=77/L=150  WR=33.9%
- Sharpen: sharpest is RSI=RSI5 (117/150 of losers there)
- **Sharp: n=143  W=26/L=117  WR=18.2%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when RSI 60-70 strong

### L19.  `H20=H20e AND T1=T1c AND T4=T4a AND direction_exec=short`
- Raw: n=227  W=77/L=150  WR=33.9%
- Sharpen: sharpest is RSI=RSI5 (117/150 of losers there)
- **Sharp: n=143  W=26/L=117  WR=18.2%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when RSI 60-70 strong

### L20.  `H20=H20e AND T1=T1c AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=220  W=60/L=160  WR=27.3%
- Sharpen: sharpest is ZS=ZS5 (67/160 of losers there)
- **Sharp: n=73  W=6/L=67  WR=8.2%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 60-70 strong; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L21.  `H60=H60e AND T4=T4c AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=175  W=68/L=107  WR=38.9%
- Sharpen: sharpest is ZS=ZS5 (47/107 of losers there)
- **Sharp: n=53  W=6/L=47  WR=11.3%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 60-70 strong; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L22.  `T4=T4c AND RSI=RSI5 AND direction_exec=short AND session_bucket=asia`
- Raw: n=175  W=68/L=107  WR=38.9%
- Sharpen: sharpest is ZS=ZS5 (47/107 of losers there)
- **Sharp: n=53  W=6/L=47  WR=11.3%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 60-70 strong; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L23.  `T1=T1c AND T4=T4c AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=171  W=64/L=107  WR=37.4%
- Sharpen: sharpest is ZS=ZS5 (47/107 of losers there)
- **Sharp: n=53  W=6/L=47  WR=11.3%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 60-70 strong; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L24.  `H20=H20e AND T4=T4c AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=168  W=61/L=107  WR=36.3%
- Sharpen: sharpest is ZS=ZS5 (47/107 of losers there)
- **Sharp: n=53  W=6/L=47  WR=11.3%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 60-70 strong; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L25.  `H20=H20e AND T4=T4a AND RSI=RSI5`
- Raw: n=161  W=37/L=124  WR=23.0%
- Sharpen: sharpest is ZS=ZS5 (33/124 of losers there)
- **Sharp: n=33  W=0/L=33  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when zscore +2 to +3 deep overbought

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(54/36) | H20e(38/58) |
| H60 | H60a(58/40) | H60e(42/60) |
| T1 | T1a(59/39) | T1c(41/61) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(58/40) | short(42/60) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
