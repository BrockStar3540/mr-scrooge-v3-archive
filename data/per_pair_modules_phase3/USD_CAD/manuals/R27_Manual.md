# USD_CAD — R27 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50e**  (EMA50 down >0.5x)
- **ADR = ADR3**  (60-90%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **2,710**  (W=1,667 / L=1,043)  -  WR: **61.5%**

## Session distribution

- asia: n=918  W=581/L=337  WR=63.3%
- ny_close: n=626  W=380/L=246  WR=60.7%
- ny_mid: n=506  W=311/L=195  WR=61.5%
- london_open: n=220  W=136/L=84  WR=61.8%
- off_hours: n=172  W=95/L=77  WR=55.2%
- ny_open: n=118  W=70/L=48  WR=59.3%
- london: n=104  W=68/L=36  WR=65.4%
- asia_late: n=46  W=26/L=20  WR=56.5%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND T1=T1a AND BBP=BBP2 AND session_bucket=asia`
- Raw: n=112  W=98/L=14  WR=87.5%
- Refine: no further refinement
- **Final: n=112  W=98/L=14  WR=87.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; lower third; session=asia

### W02.  `H20=H20a AND T4=T4a AND BBP=BBP2 AND session_bucket=asia`
- Raw: n=112  W=98/L=14  WR=87.5%
- Refine: no further refinement
- **Final: n=112  W=98/L=14  WR=87.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; lower third; session=asia

### W03.  `H20=H20a AND BBP=BBP2 AND direction_exec=short AND session_bucket=asia`
- Raw: n=112  W=98/L=14  WR=87.5%
- Refine: no further refinement
- **Final: n=112  W=98/L=14  WR=87.5%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; lower third; session=asia

### W04.  `H20=H20a AND H60=H60a AND BBP=BBP2 AND session_bucket=asia`
- Raw: n=106  W=93/L=13  WR=87.7%
- Refine: no further refinement
- **Final: n=106  W=93/L=13  WR=87.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; lower third; session=asia

### W05.  `H20=H20a AND T1=T1a AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=106  W=93/L=13  WR=87.7%
- Refine: no further refinement
- **Final: n=106  W=93/L=13  WR=87.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; zscore -2 to -1 oversold; session=asia

### W06.  `H20=H20a AND T4=T4a AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=106  W=93/L=13  WR=87.7%
- Refine: no further refinement
- **Final: n=106  W=93/L=13  WR=87.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; zscore -2 to -1 oversold; session=asia

### W07.  `H20=H20a AND ZS=ZS2 AND direction_exec=short AND session_bucket=asia`
- Raw: n=106  W=93/L=13  WR=87.7%
- Refine: no further refinement
- **Final: n=106  W=93/L=13  WR=87.7%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; zscore -2 to -1 oversold; session=asia

### W08.  `H20=H20a AND H60=H60a AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=100  W=88/L=12  WR=88.0%
- Refine: no further refinement
- **Final: n=100  W=88/L=12  WR=88.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; zscore -2 to -1 oversold; session=asia

### W09.  `H20=H20a AND BBP=BBP2 AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=99  W=87/L=12  WR=87.9%
- Refine: no further refinement
- **Final: n=99  W=87/L=12  WR=87.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; lower third; RSI 30-40 weak; session=asia

### W10.  `H20=H20a AND RSI=RSI2 AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=97  W=86/L=11  WR=88.7%
- Refine: no further refinement
- **Final: n=97  W=86/L=11  WR=88.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 30-40 weak; zscore -2 to -1 oversold; session=asia

### W11.  `H20=H20a AND RSI=RSI1 AND session_bucket=ny_mid`
- Raw: n=87  W=74/L=13  WR=85.1%
- Refine: no further refinement
- **Final: n=87  W=74/L=13  WR=85.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 20-30 oversold; session=ny_mid

### W12.  `H60=H60a AND RSI=RSI1 AND session_bucket=ny_mid`
- Raw: n=87  W=74/L=13  WR=85.1%
- Refine: no further refinement
- **Final: n=87  W=74/L=13  WR=85.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 20-30 oversold; session=ny_mid

### W13.  `H60=H60a AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=87  W=74/L=13  WR=85.1%
- Refine: exclude BBP=BBP0 drops 7/13 losers (54%)
- **Final: n=60  W=54/L=6  WR=90.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; zscore -3 to -2 deep oversold; session=asia  •  AVOID when deep below lower band

### W14.  `T1=T1a AND RSI=RSI1 AND session_bucket=ny_mid`
- Raw: n=87  W=74/L=13  WR=85.1%
- Refine: no further refinement
- **Final: n=87  W=74/L=13  WR=85.1%**
- **Dir: ?**  •  1h trend WITH trade; RSI 20-30 oversold; session=ny_mid

### W15.  `T4=T4a AND RSI=RSI1 AND session_bucket=ny_mid`
- Raw: n=87  W=74/L=13  WR=85.1%
- Refine: no further refinement
- **Final: n=87  W=74/L=13  WR=85.1%**
- **Dir: ?**  •  4h trend WITH trade; RSI 20-30 oversold; session=ny_mid

### W16.  `RSI=RSI1 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=87  W=74/L=13  WR=85.1%
- Refine: no further refinement
- **Final: n=87  W=74/L=13  WR=85.1%**
- **Dir: SHORT**  •  RSI 20-30 oversold; session=ny_mid

### W17.  `H20=H20a AND H60=H60a AND RSI=RSI1 AND session_bucket=ny_mid`
- Raw: n=87  W=74/L=13  WR=85.1%
- Refine: no further refinement
- **Final: n=87  W=74/L=13  WR=85.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 20-30 oversold; session=ny_mid

### W18.  `H20=H20a AND T1=T1a AND RSI=RSI1 AND session_bucket=ny_mid`
- Raw: n=87  W=74/L=13  WR=85.1%
- Refine: no further refinement
- **Final: n=87  W=74/L=13  WR=85.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 20-30 oversold; session=ny_mid

### W19.  `H20=H20a AND T4=T4a AND RSI=RSI1 AND session_bucket=ny_mid`
- Raw: n=87  W=74/L=13  WR=85.1%
- Refine: no further refinement
- **Final: n=87  W=74/L=13  WR=85.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 20-30 oversold; session=ny_mid

### W20.  `H20=H20a AND RSI=RSI1 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=87  W=74/L=13  WR=85.1%
- Refine: no further refinement
- **Final: n=87  W=74/L=13  WR=85.1%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 20-30 oversold; session=ny_mid

### W21.  `H60=H60a AND T1=T1a AND RSI=RSI1 AND session_bucket=ny_mid`
- Raw: n=87  W=74/L=13  WR=85.1%
- Refine: no further refinement
- **Final: n=87  W=74/L=13  WR=85.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 20-30 oversold; session=ny_mid

### W22.  `H60=H60a AND T1=T1a AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=87  W=74/L=13  WR=85.1%
- Refine: exclude BBP=BBP0 drops 7/13 losers (54%)
- **Final: n=60  W=54/L=6  WR=90.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; zscore -3 to -2 deep oversold; session=asia  •  AVOID when deep below lower band

### W23.  `H60=H60a AND T4=T4a AND RSI=RSI1 AND session_bucket=ny_mid`
- Raw: n=87  W=74/L=13  WR=85.1%
- Refine: no further refinement
- **Final: n=87  W=74/L=13  WR=85.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 20-30 oversold; session=ny_mid

### W24.  `H60=H60a AND T4=T4a AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=87  W=74/L=13  WR=85.1%
- Refine: exclude BBP=BBP0 drops 7/13 losers (54%)
- **Final: n=60  W=54/L=6  WR=90.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; zscore -3 to -2 deep oversold; session=asia  •  AVOID when deep below lower band

### W25.  `H60=H60a AND RSI=RSI1 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=87  W=74/L=13  WR=85.1%
- Refine: no further refinement
- **Final: n=87  W=74/L=13  WR=85.1%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; RSI 20-30 oversold; session=ny_mid

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=246  W=92/L=154  WR=37.4%
- Sharpen: no sharper sub-pattern
- **Sharp: n=246  W=92/L=154  WR=37.4%**
- **Dir: ?**  •  HTF60 strongly against; RSI 30-40 weak; session=asia

### L02.  `T1=T1c AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=245  W=94/L=151  WR=38.4%
- Sharpen: no sharper sub-pattern
- **Sharp: n=245  W=94/L=151  WR=38.4%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 30-40 weak; session=asia

### L03.  `T4=T4c AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=245  W=94/L=151  WR=38.4%
- Sharpen: no sharper sub-pattern
- **Sharp: n=245  W=94/L=151  WR=38.4%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 30-40 weak; session=asia

### L04.  `RSI=RSI2 AND direction_exec=long AND session_bucket=asia`
- Raw: n=245  W=94/L=151  WR=38.4%
- Sharpen: no sharper sub-pattern
- **Sharp: n=245  W=94/L=151  WR=38.4%**
- **Dir: LONG**  •  RSI 30-40 weak; session=asia

### L05.  `T1=T1c AND T4=T4c AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=245  W=94/L=151  WR=38.4%
- Sharpen: no sharper sub-pattern
- **Sharp: n=245  W=94/L=151  WR=38.4%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 30-40 weak; session=asia

### L06.  `T1=T1c AND RSI=RSI2 AND direction_exec=long AND session_bucket=asia`
- Raw: n=245  W=94/L=151  WR=38.4%
- Sharpen: no sharper sub-pattern
- **Sharp: n=245  W=94/L=151  WR=38.4%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 30-40 weak; session=asia

### L07.  `T4=T4c AND RSI=RSI2 AND direction_exec=long AND session_bucket=asia`
- Raw: n=245  W=94/L=151  WR=38.4%
- Sharpen: no sharper sub-pattern
- **Sharp: n=245  W=94/L=151  WR=38.4%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 30-40 weak; session=asia

### L08.  `H20=H20e AND T1=T1c AND session_bucket=asia`
- Raw: n=237  W=94/L=143  WR=39.7%
- Sharpen: sharpest is ZS=ZS2 (60/143 of losers there)
- **Sharp: n=81  W=21/L=60  WR=25.9%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; session=asia  •  ONLY when zscore -2 to -1 oversold

### L09.  `H20=H20e AND T4=T4c AND session_bucket=asia`
- Raw: n=237  W=94/L=143  WR=39.7%
- Sharpen: sharpest is ZS=ZS2 (60/143 of losers there)
- **Sharp: n=81  W=21/L=60  WR=25.9%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; session=asia  •  ONLY when zscore -2 to -1 oversold

### L10.  `H20=H20e AND direction_exec=long AND session_bucket=asia`
- Raw: n=237  W=94/L=143  WR=39.7%
- Sharpen: sharpest is ZS=ZS2 (60/143 of losers there)
- **Sharp: n=81  W=21/L=60  WR=25.9%**
- **Dir: LONG**  •  HTF20 strongly against; session=asia  •  ONLY when zscore -2 to -1 oversold

### L11.  `H20=H20e AND T1=T1c AND T4=T4c AND session_bucket=asia`
- Raw: n=237  W=94/L=143  WR=39.7%
- Sharpen: sharpest is ZS=ZS2 (60/143 of losers there)
- **Sharp: n=81  W=21/L=60  WR=25.9%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; session=asia  •  ONLY when zscore -2 to -1 oversold

### L12.  `H20=H20e AND T1=T1c AND direction_exec=long AND session_bucket=asia`
- Raw: n=237  W=94/L=143  WR=39.7%
- Sharpen: sharpest is ZS=ZS2 (60/143 of losers there)
- **Sharp: n=81  W=21/L=60  WR=25.9%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade; session=asia  •  ONLY when zscore -2 to -1 oversold

### L13.  `H20=H20e AND T4=T4c AND direction_exec=long AND session_bucket=asia`
- Raw: n=237  W=94/L=143  WR=39.7%
- Sharpen: sharpest is ZS=ZS2 (60/143 of losers there)
- **Sharp: n=81  W=21/L=60  WR=25.9%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend AGAINST trade; session=asia  •  ONLY when zscore -2 to -1 oversold

### L14.  `H60=H60e AND T1=T1c AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=233  W=86/L=147  WR=36.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=233  W=86/L=147  WR=36.9%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 30-40 weak; session=asia

### L15.  `H60=H60e AND T4=T4c AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=233  W=86/L=147  WR=36.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=233  W=86/L=147  WR=36.9%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 30-40 weak; session=asia

### L16.  `H60=H60e AND RSI=RSI2 AND direction_exec=long AND session_bucket=asia`
- Raw: n=233  W=86/L=147  WR=36.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=233  W=86/L=147  WR=36.9%**
- **Dir: LONG**  •  HTF60 strongly against; RSI 30-40 weak; session=asia

### L17.  `H20=H20e AND H60=H60e AND session_bucket=asia`
- Raw: n=204  W=80/L=124  WR=39.2%
- Sharpen: sharpest is ZS=ZS2 (51/124 of losers there)
- **Sharp: n=68  W=17/L=51  WR=25.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; session=asia  •  ONLY when zscore -2 to -1 oversold

### L18.  `H20=H20e AND H60=H60e AND T1=T1c AND session_bucket=asia`
- Raw: n=204  W=80/L=124  WR=39.2%
- Sharpen: sharpest is ZS=ZS2 (51/124 of losers there)
- **Sharp: n=68  W=17/L=51  WR=25.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; session=asia  •  ONLY when zscore -2 to -1 oversold

### L19.  `H20=H20e AND H60=H60e AND T4=T4c AND session_bucket=asia`
- Raw: n=204  W=80/L=124  WR=39.2%
- Sharpen: sharpest is ZS=ZS2 (51/124 of losers there)
- **Sharp: n=68  W=17/L=51  WR=25.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; session=asia  •  ONLY when zscore -2 to -1 oversold

### L20.  `H20=H20e AND H60=H60e AND direction_exec=long AND session_bucket=asia`
- Raw: n=204  W=80/L=124  WR=39.2%
- Sharpen: sharpest is ZS=ZS2 (51/124 of losers there)
- **Sharp: n=68  W=17/L=51  WR=25.0%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 strongly against; session=asia  •  ONLY when zscore -2 to -1 oversold

### L21.  `H20=H20e AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=173  W=61/L=112  WR=35.3%
- Sharpen: sharpest is BBP=BBP2 (48/112 of losers there)
- **Sharp: n=63  W=15/L=48  WR=23.8%**
- **Dir: ?**  •  HTF20 strongly against; RSI 30-40 weak; session=asia  •  ONLY when lower third

### L22.  `H20=H20e AND T1=T1c AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=173  W=61/L=112  WR=35.3%
- Sharpen: sharpest is BBP=BBP2 (48/112 of losers there)
- **Sharp: n=63  W=15/L=48  WR=23.8%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 30-40 weak; session=asia  •  ONLY when lower third

### L23.  `H20=H20e AND T4=T4c AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=173  W=61/L=112  WR=35.3%
- Sharpen: sharpest is BBP=BBP2 (48/112 of losers there)
- **Sharp: n=63  W=15/L=48  WR=23.8%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 30-40 weak; session=asia  •  ONLY when lower third

### L24.  `H20=H20e AND RSI=RSI2 AND direction_exec=long AND session_bucket=asia`
- Raw: n=173  W=61/L=112  WR=35.3%
- Sharpen: sharpest is BBP=BBP2 (48/112 of losers there)
- **Sharp: n=63  W=15/L=48  WR=23.8%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 30-40 weak; session=asia  •  ONLY when lower third

### L25.  `H20=H20e AND H60=H60e AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=171  W=59/L=112  WR=34.5%
- Sharpen: sharpest is BBP=BBP2 (48/112 of losers there)
- **Sharp: n=63  W=15/L=48  WR=23.8%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 30-40 weak; session=asia  •  ONLY when lower third

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(46/32) | H20e(30/46) |
| H60 | H60a(53/37) | H60e(36/51) |
| T1 | T1a(60/42) | T1c(40/58) |
| T4 | T4a(59/42) | T4c(41/58) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(60/42) | long(40/58) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
