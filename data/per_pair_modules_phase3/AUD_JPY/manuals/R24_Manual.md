# AUD_JPY — R24 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50a**  (EMA50 up >0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **5,202**  (W=3,196 / L=2,006)  -  WR: **61.4%**

## Session distribution

- asia: n=1620  W=975/L=645  WR=60.2%
- ny_mid: n=1509  W=941/L=568  WR=62.4%
- london_open: n=799  W=471/L=328  WR=58.9%
- ny_close: n=512  W=322/L=190  WR=62.9%
- ny_open: n=286  W=185/L=101  WR=64.7%
- asia_late: n=186  W=111/L=75  WR=59.7%
- london: n=185  W=120/L=65  WR=64.9%
- off_hours: n=105  W=71/L=34  WR=67.6%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60a AND T4=T4a AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=365  W=311/L=54  WR=85.2%
- Refine: exclude ZS=ZS4 drops 39/54 losers (72%)
- **Final: n=181  W=166/L=15  WR=91.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 70-80 overbought; session=ny_mid  •  AVOID when zscore +1 to +2 overbought

### W02.  `T1=T1a AND T4=T4a AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=365  W=311/L=54  WR=85.2%
- Refine: exclude ZS=ZS4 drops 39/54 losers (72%)
- **Final: n=181  W=166/L=15  WR=91.7%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 70-80 overbought; session=ny_mid  •  AVOID when zscore +1 to +2 overbought

### W03.  `T4=T4a AND RSI=RSI6 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=365  W=311/L=54  WR=85.2%
- Refine: exclude ZS=ZS4 drops 39/54 losers (72%)
- **Final: n=181  W=166/L=15  WR=91.7%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 70-80 overbought; session=ny_mid  •  AVOID when zscore +1 to +2 overbought

### W04.  `H20=H20a AND RSI=RSI6 AND session_bucket=asia`
- Raw: n=348  W=299/L=49  WR=85.9%
- Refine: no further refinement
- **Final: n=348  W=299/L=49  WR=85.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 70-80 overbought; session=asia

### W05.  `H20=H20a AND H60=H60a AND RSI=RSI6 AND session_bucket=asia`
- Raw: n=339  W=292/L=47  WR=86.1%
- Refine: no further refinement
- **Final: n=339  W=292/L=47  WR=86.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 70-80 overbought; session=asia

### W06.  `H20=H20a AND T1=T1a AND RSI=RSI6 AND session_bucket=asia`
- Raw: n=339  W=292/L=47  WR=86.1%
- Refine: no further refinement
- **Final: n=339  W=292/L=47  WR=86.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 70-80 overbought; session=asia

### W07.  `H20=H20a AND T4=T4a AND RSI=RSI6 AND session_bucket=asia`
- Raw: n=339  W=292/L=47  WR=86.1%
- Refine: no further refinement
- **Final: n=339  W=292/L=47  WR=86.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 70-80 overbought; session=asia

### W08.  `H20=H20a AND RSI=RSI6 AND direction_exec=long AND session_bucket=asia`
- Raw: n=339  W=292/L=47  WR=86.1%
- Refine: no further refinement
- **Final: n=339  W=292/L=47  WR=86.1%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 70-80 overbought; session=asia

### W09.  `H20=H20a AND H60=H60a AND RSI=RSI6 AND ZS=ZS5`
- Raw: n=223  W=190/L=33  WR=85.2%
- Refine: exclude session_bucket=london drops 12/33 losers (36%)
- **Final: n=209  W=188/L=21  WR=90.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 70-80 overbought; zscore +2 to +3 deep overbought  •  AVOID when session=london

### W10.  `H20=H20a AND T1=T1a AND RSI=RSI6 AND ZS=ZS5`
- Raw: n=223  W=190/L=33  WR=85.2%
- Refine: exclude session_bucket=london drops 12/33 losers (36%)
- **Final: n=209  W=188/L=21  WR=90.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 70-80 overbought; zscore +2 to +3 deep overbought  •  AVOID when session=london

### W11.  `H20=H20a AND RSI=RSI6 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=223  W=190/L=33  WR=85.2%
- Refine: exclude session_bucket=london drops 12/33 losers (36%)
- **Final: n=209  W=188/L=21  WR=90.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 70-80 overbought; zscore +2 to +3 deep overbought  •  AVOID when session=london

### W12.  `H60=H60a AND BBP=BBP4 AND RSI=RSI6 AND session_bucket=asia`
- Raw: n=194  W=167/L=27  WR=86.1%
- Refine: no further refinement
- **Final: n=194  W=167/L=27  WR=86.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; upper third; RSI 70-80 overbought; session=asia

### W13.  `T1=T1a AND BBP=BBP4 AND RSI=RSI6 AND session_bucket=asia`
- Raw: n=194  W=167/L=27  WR=86.1%
- Refine: no further refinement
- **Final: n=194  W=167/L=27  WR=86.1%**
- **Dir: ?**  •  1h trend WITH trade; upper third; RSI 70-80 overbought; session=asia

### W14.  `T4=T4a AND BBP=BBP4 AND RSI=RSI6 AND session_bucket=asia`
- Raw: n=194  W=167/L=27  WR=86.1%
- Refine: no further refinement
- **Final: n=194  W=167/L=27  WR=86.1%**
- **Dir: ?**  •  4h trend WITH trade; upper third; RSI 70-80 overbought; session=asia

### W15.  `BBP=BBP4 AND RSI=RSI6 AND direction_exec=long AND session_bucket=asia`
- Raw: n=194  W=167/L=27  WR=86.1%
- Refine: no further refinement
- **Final: n=194  W=167/L=27  WR=86.1%**
- **Dir: LONG**  •  upper third; RSI 70-80 overbought; session=asia

### W16.  `H20=H20a AND BBP=BBP4 AND RSI=RSI6 AND session_bucket=asia`
- Raw: n=193  W=167/L=26  WR=86.5%
- Refine: no further refinement
- **Final: n=193  W=167/L=26  WR=86.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; upper third; RSI 70-80 overbought; session=asia

### W17.  `H60=H60a AND RSI=RSI6 AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=180  W=155/L=25  WR=86.1%
- Refine: no further refinement
- **Final: n=180  W=155/L=25  WR=86.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 70-80 overbought; zscore +1 to +2 overbought; session=asia

### W18.  `T1=T1a AND RSI=RSI6 AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=180  W=155/L=25  WR=86.1%
- Refine: no further refinement
- **Final: n=180  W=155/L=25  WR=86.1%**
- **Dir: ?**  •  1h trend WITH trade; RSI 70-80 overbought; zscore +1 to +2 overbought; session=asia

### W19.  `T4=T4a AND RSI=RSI6 AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=180  W=155/L=25  WR=86.1%
- Refine: no further refinement
- **Final: n=180  W=155/L=25  WR=86.1%**
- **Dir: ?**  •  4h trend WITH trade; RSI 70-80 overbought; zscore +1 to +2 overbought; session=asia

### W20.  `RSI=RSI6 AND ZS=ZS4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=180  W=155/L=25  WR=86.1%
- Refine: no further refinement
- **Final: n=180  W=155/L=25  WR=86.1%**
- **Dir: LONG**  •  RSI 70-80 overbought; zscore +1 to +2 overbought; session=asia

### W21.  `H20=H20a AND RSI=RSI6 AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=179  W=155/L=24  WR=86.6%
- Refine: no further refinement
- **Final: n=179  W=155/L=24  WR=86.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 70-80 overbought; zscore +1 to +2 overbought; session=asia

### W22.  `H20=H20a AND T4=T4a AND BBP=BBP4 AND RSI=RSI7`
- Raw: n=160  W=136/L=24  WR=85.0%
- Refine: exclude session_bucket=london_open drops 14/24 losers (58%)
- **Final: n=117  W=107/L=10  WR=91.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; upper third; RSI>80 extreme overbought  •  AVOID when session=london_open

### W23.  `H20=H20a AND T4=T4a AND RSI=RSI7 AND ZS=ZS4`
- Raw: n=149  W=127/L=22  WR=85.2%
- Refine: exclude session_bucket=london_open drops 14/22 losers (64%)
- **Final: n=106  W=98/L=8  WR=92.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI>80 extreme overbought; zscore +1 to +2 overbought  •  AVOID when session=london_open

### W24.  `H20=H20a AND BBP=BBP5 AND RSI=RSI6`
- Raw: n=137  W=118/L=19  WR=86.1%
- Refine: exclude session_bucket=london drops 9/19 losers (47%)
- **Final: n=126  W=116/L=10  WR=92.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; just touched upper band; RSI 70-80 overbought  •  AVOID when session=london

### W25.  `H20=H20a AND BBP=BBP5 AND RSI=RSI6 AND ZS=ZS5`
- Raw: n=137  W=118/L=19  WR=86.1%
- Refine: exclude session_bucket=london drops 9/19 losers (47%)
- **Final: n=126  W=116/L=10  WR=92.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; just touched upper band; RSI 70-80 overbought; zscore +2 to +3 deep overbought  •  AVOID when session=london

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND H60=H60e AND RSI=RSI6`
- Raw: n=849  W=335/L=514  WR=39.5%
- Sharpen: sharpest is session_bucket=asia (213/514 of losers there)
- **Sharp: n=294  W=81/L=213  WR=27.6%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 70-80 overbought  •  ONLY when session=asia

### L02.  `H20=H20e AND T1=T1c AND RSI=RSI6`
- Raw: n=849  W=335/L=514  WR=39.5%
- Sharpen: sharpest is session_bucket=asia (213/514 of losers there)
- **Sharp: n=294  W=81/L=213  WR=27.6%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when session=asia

### L03.  `H20=H20e AND RSI=RSI6 AND direction_exec=short`
- Raw: n=849  W=335/L=514  WR=39.5%
- Sharpen: sharpest is session_bucket=asia (213/514 of losers there)
- **Sharp: n=294  W=81/L=213  WR=27.6%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 70-80 overbought  •  ONLY when session=asia

### L04.  `H20=H20e AND H60=H60e AND T1=T1c AND RSI=RSI6`
- Raw: n=849  W=335/L=514  WR=39.5%
- Sharpen: sharpest is session_bucket=asia (213/514 of losers there)
- **Sharp: n=294  W=81/L=213  WR=27.6%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when session=asia

### L05.  `H20=H20e AND H60=H60e AND RSI=RSI6 AND direction_exec=short`
- Raw: n=849  W=335/L=514  WR=39.5%
- Sharpen: sharpest is session_bucket=asia (213/514 of losers there)
- **Sharp: n=294  W=81/L=213  WR=27.6%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; RSI 70-80 overbought  •  ONLY when session=asia

### L06.  `H20=H20e AND T1=T1c AND RSI=RSI6 AND direction_exec=short`
- Raw: n=849  W=335/L=514  WR=39.5%
- Sharpen: sharpest is session_bucket=asia (213/514 of losers there)
- **Sharp: n=294  W=81/L=213  WR=27.6%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when session=asia

### L07.  `H20=H20e AND T4=T4c AND RSI=RSI6`
- Raw: n=790  W=314/L=476  WR=39.7%
- Sharpen: sharpest is session_bucket=asia (213/476 of losers there)
- **Sharp: n=294  W=81/L=213  WR=27.6%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when session=asia

### L08.  `H20=H20e AND H60=H60e AND T4=T4c AND RSI=RSI6`
- Raw: n=790  W=314/L=476  WR=39.7%
- Sharpen: sharpest is session_bucket=asia (213/476 of losers there)
- **Sharp: n=294  W=81/L=213  WR=27.6%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when session=asia

### L09.  `H20=H20e AND T1=T1c AND T4=T4c AND RSI=RSI6`
- Raw: n=790  W=314/L=476  WR=39.7%
- Sharpen: sharpest is session_bucket=asia (213/476 of losers there)
- **Sharp: n=294  W=81/L=213  WR=27.6%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when session=asia

### L10.  `H20=H20e AND T4=T4c AND RSI=RSI6 AND direction_exec=short`
- Raw: n=790  W=314/L=476  WR=39.7%
- Sharpen: sharpest is session_bucket=asia (213/476 of losers there)
- **Sharp: n=294  W=81/L=213  WR=27.6%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when session=asia

### L11.  `H60=H60e AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=310  W=114/L=196  WR=36.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=310  W=114/L=196  WR=36.8%**
- **Dir: ?**  •  HTF60 strongly against; RSI 70-80 overbought; session=ny_mid

### L12.  `T1=T1c AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=310  W=114/L=196  WR=36.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=310  W=114/L=196  WR=36.8%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 70-80 overbought; session=ny_mid

### L13.  `RSI=RSI6 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=310  W=114/L=196  WR=36.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=310  W=114/L=196  WR=36.8%**
- **Dir: SHORT**  •  RSI 70-80 overbought; session=ny_mid

### L14.  `H60=H60e AND T1=T1c AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=310  W=114/L=196  WR=36.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=310  W=114/L=196  WR=36.8%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 70-80 overbought; session=ny_mid

### L15.  `H60=H60e AND RSI=RSI6 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=310  W=114/L=196  WR=36.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=310  W=114/L=196  WR=36.8%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 70-80 overbought; session=ny_mid

### L16.  `T1=T1c AND RSI=RSI6 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=310  W=114/L=196  WR=36.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=310  W=114/L=196  WR=36.8%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 70-80 overbought; session=ny_mid

### L17.  `T4=T4c AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=309  W=117/L=192  WR=37.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=309  W=117/L=192  WR=37.9%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 70-80 overbought; session=ny_mid

### L18.  `H20=H20e AND RSI=RSI6 AND session_bucket=asia`
- Raw: n=303  W=84/L=219  WR=27.7%
- Sharpen: sharpest is ZS=ZS5 (61/219 of losers there)
- **Sharp: n=71  W=10/L=61  WR=14.1%**
- **Dir: ?**  •  HTF20 strongly against; RSI 70-80 overbought; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L19.  `H60=H60e AND RSI=RSI6 AND session_bucket=asia`
- Raw: n=303  W=88/L=215  WR=29.0%
- Sharpen: sharpest is ZS=ZS5 (61/215 of losers there)
- **Sharp: n=71  W=10/L=61  WR=14.1%**
- **Dir: ?**  •  HTF60 strongly against; RSI 70-80 overbought; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L20.  `T1=T1c AND RSI=RSI6 AND session_bucket=asia`
- Raw: n=303  W=88/L=215  WR=29.0%
- Sharpen: sharpest is ZS=ZS5 (61/215 of losers there)
- **Sharp: n=71  W=10/L=61  WR=14.1%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 70-80 overbought; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L21.  `T4=T4c AND RSI=RSI6 AND session_bucket=asia`
- Raw: n=303  W=88/L=215  WR=29.0%
- Sharpen: sharpest is ZS=ZS5 (61/215 of losers there)
- **Sharp: n=71  W=10/L=61  WR=14.1%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 70-80 overbought; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L22.  `RSI=RSI6 AND direction_exec=short AND session_bucket=asia`
- Raw: n=303  W=88/L=215  WR=29.0%
- Sharpen: sharpest is ZS=ZS5 (61/215 of losers there)
- **Sharp: n=71  W=10/L=61  WR=14.1%**
- **Dir: SHORT**  •  RSI 70-80 overbought; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L23.  `H60=H60e AND T1=T1c AND RSI=RSI6 AND session_bucket=asia`
- Raw: n=303  W=88/L=215  WR=29.0%
- Sharpen: sharpest is ZS=ZS5 (61/215 of losers there)
- **Sharp: n=71  W=10/L=61  WR=14.1%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 70-80 overbought; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L24.  `H60=H60e AND T4=T4c AND RSI=RSI6 AND session_bucket=asia`
- Raw: n=303  W=88/L=215  WR=29.0%
- Sharpen: sharpest is ZS=ZS5 (61/215 of losers there)
- **Sharp: n=71  W=10/L=61  WR=14.1%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 70-80 overbought; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L25.  `H60=H60e AND RSI=RSI6 AND direction_exec=short AND session_bucket=asia`
- Raw: n=303  W=88/L=215  WR=29.0%
- Sharpen: sharpest is ZS=ZS5 (61/215 of losers there)
- **Sharp: n=71  W=10/L=61  WR=14.1%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 70-80 overbought; session=asia  •  ONLY when zscore +2 to +3 deep overbought

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(56/41) | H20e(42/57) |
| H60 | H60a(59/40) | H60e(41/60) |
| T1 | T1a(60/39) | T1c(40/61) |
| T4 | T4a(58/41) | T4c(42/59) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(59/40) | short(41/60) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
