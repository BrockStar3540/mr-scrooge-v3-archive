# AUD_CAD — R39 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50a**  (EMA50 up >0.5x)
- **ADR = ADR3**  (60-90%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **1,769**  (W=1,099 / L=670)  -  WR: **62.1%**

## Session distribution

- asia: n=544  W=340/L=204  WR=62.5%
- london: n=264  W=166/L=98  WR=62.9%
- ny_open: n=259  W=165/L=94  WR=63.7%
- ny_mid: n=214  W=133/L=81  WR=62.1%
- ny_close: n=192  W=122/L=70  WR=63.5%
- london_open: n=165  W=89/L=76  WR=53.9%
- asia_late: n=103  W=66/L=37  WR=64.1%
- off_hours: n=28  W=18/L=10  WR=64.3%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60a AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=94  W=84/L=10  WR=89.4%
- Refine: exclude RSI=RSI7 drops 4/10 losers (40%)
- **Final: n=86  W=80/L=6  WR=93.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; deep above upper band; zscore +2 to +3 deep overbought  •  AVOID when RSI>80 extreme overbought

### W02.  `T1=T1a AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=94  W=84/L=10  WR=89.4%
- Refine: exclude RSI=RSI7 drops 4/10 losers (40%)
- **Final: n=86  W=80/L=6  WR=93.0%**
- **Dir: ?**  •  1h trend WITH trade; deep above upper band; zscore +2 to +3 deep overbought  •  AVOID when RSI>80 extreme overbought

### W03.  `T4=T4a AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=94  W=84/L=10  WR=89.4%
- Refine: exclude RSI=RSI7 drops 4/10 losers (40%)
- **Final: n=86  W=80/L=6  WR=93.0%**
- **Dir: ?**  •  4h trend WITH trade; deep above upper band; zscore +2 to +3 deep overbought  •  AVOID when RSI>80 extreme overbought

### W04.  `BBP=BBP6 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=94  W=84/L=10  WR=89.4%
- Refine: exclude RSI=RSI7 drops 4/10 losers (40%)
- **Final: n=86  W=80/L=6  WR=93.0%**
- **Dir: LONG**  •  deep above upper band; zscore +2 to +3 deep overbought  •  AVOID when RSI>80 extreme overbought

### W05.  `H60=H60a AND T1=T1a AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=94  W=84/L=10  WR=89.4%
- Refine: exclude RSI=RSI7 drops 4/10 losers (40%)
- **Final: n=86  W=80/L=6  WR=93.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; deep above upper band; zscore +2 to +3 deep overbought  •  AVOID when RSI>80 extreme overbought

### W06.  `H60=H60a AND T4=T4a AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=94  W=84/L=10  WR=89.4%
- Refine: exclude RSI=RSI7 drops 4/10 losers (40%)
- **Final: n=86  W=80/L=6  WR=93.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; deep above upper band; zscore +2 to +3 deep overbought  •  AVOID when RSI>80 extreme overbought

### W07.  `H60=H60a AND BBP=BBP6 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=94  W=84/L=10  WR=89.4%
- Refine: exclude RSI=RSI7 drops 4/10 losers (40%)
- **Final: n=86  W=80/L=6  WR=93.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; deep above upper band; zscore +2 to +3 deep overbought  •  AVOID when RSI>80 extreme overbought

### W08.  `T1=T1a AND T4=T4a AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=94  W=84/L=10  WR=89.4%
- Refine: exclude RSI=RSI7 drops 4/10 losers (40%)
- **Final: n=86  W=80/L=6  WR=93.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; deep above upper band; zscore +2 to +3 deep overbought  •  AVOID when RSI>80 extreme overbought

### W09.  `T1=T1a AND BBP=BBP6 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=94  W=84/L=10  WR=89.4%
- Refine: exclude RSI=RSI7 drops 4/10 losers (40%)
- **Final: n=86  W=80/L=6  WR=93.0%**
- **Dir: LONG**  •  1h trend WITH trade; deep above upper band; zscore +2 to +3 deep overbought  •  AVOID when RSI>80 extreme overbought

### W10.  `T4=T4a AND BBP=BBP6 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=94  W=84/L=10  WR=89.4%
- Refine: exclude RSI=RSI7 drops 4/10 losers (40%)
- **Final: n=86  W=80/L=6  WR=93.0%**
- **Dir: LONG**  •  4h trend WITH trade; deep above upper band; zscore +2 to +3 deep overbought  •  AVOID when RSI>80 extreme overbought

### W11.  `H60=H60a AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=89  W=77/L=12  WR=86.5%
- Refine: no further refinement
- **Final: n=89  W=77/L=12  WR=86.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; zscore +2 to +3 deep overbought; session=asia

### W12.  `T1=T1a AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=89  W=77/L=12  WR=86.5%
- Refine: no further refinement
- **Final: n=89  W=77/L=12  WR=86.5%**
- **Dir: ?**  •  1h trend WITH trade; zscore +2 to +3 deep overbought; session=asia

### W13.  `T4=T4a AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=89  W=77/L=12  WR=86.5%
- Refine: no further refinement
- **Final: n=89  W=77/L=12  WR=86.5%**
- **Dir: ?**  •  4h trend WITH trade; zscore +2 to +3 deep overbought; session=asia

### W14.  `ZS=ZS5 AND direction_exec=long AND session_bucket=asia`
- Raw: n=89  W=77/L=12  WR=86.5%
- Refine: no further refinement
- **Final: n=89  W=77/L=12  WR=86.5%**
- **Dir: LONG**  •  zscore +2 to +3 deep overbought; session=asia

### W15.  `H60=H60a AND T1=T1a AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=89  W=77/L=12  WR=86.5%
- Refine: no further refinement
- **Final: n=89  W=77/L=12  WR=86.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; zscore +2 to +3 deep overbought; session=asia

### W16.  `H60=H60a AND T4=T4a AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=89  W=77/L=12  WR=86.5%
- Refine: no further refinement
- **Final: n=89  W=77/L=12  WR=86.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; zscore +2 to +3 deep overbought; session=asia

### W17.  `H60=H60a AND ZS=ZS5 AND direction_exec=long AND session_bucket=asia`
- Raw: n=89  W=77/L=12  WR=86.5%
- Refine: no further refinement
- **Final: n=89  W=77/L=12  WR=86.5%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; zscore +2 to +3 deep overbought; session=asia

### W18.  `T1=T1a AND T4=T4a AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=89  W=77/L=12  WR=86.5%
- Refine: no further refinement
- **Final: n=89  W=77/L=12  WR=86.5%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; zscore +2 to +3 deep overbought; session=asia

### W19.  `T1=T1a AND ZS=ZS5 AND direction_exec=long AND session_bucket=asia`
- Raw: n=89  W=77/L=12  WR=86.5%
- Refine: no further refinement
- **Final: n=89  W=77/L=12  WR=86.5%**
- **Dir: LONG**  •  1h trend WITH trade; zscore +2 to +3 deep overbought; session=asia

### W20.  `T4=T4a AND ZS=ZS5 AND direction_exec=long AND session_bucket=asia`
- Raw: n=89  W=77/L=12  WR=86.5%
- Refine: no further refinement
- **Final: n=89  W=77/L=12  WR=86.5%**
- **Dir: LONG**  •  4h trend WITH trade; zscore +2 to +3 deep overbought; session=asia

### W21.  `T4=T4a AND RSI=RSI5 AND session_bucket=ny_open`
- Raw: n=84  W=76/L=8  WR=90.5%
- Refine: exclude BBP=BBP4 drops 8/8 losers (100%)
- **Final: n=49  W=49/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend WITH trade; RSI 60-70 strong; session=ny_open  •  AVOID when upper third

### W22.  `H60=H60e AND T1=T1c AND RSI=RSI4`
- Raw: n=80  W=73/L=7  WR=91.2%
- Refine: exclude H20=H20d drops 7/7 losers (100%)
- **Final: n=31  W=31/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when HTF20 mildly against

### W23.  `H60=H60e AND RSI=RSI4 AND direction_exec=short`
- Raw: n=80  W=73/L=7  WR=91.2%
- Refine: exclude H20=H20d drops 7/7 losers (100%)
- **Final: n=31  W=31/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 50-60 upper neutral  •  AVOID when HTF20 mildly against

### W24.  `T1=T1c AND RSI=RSI4 AND direction_exec=short`
- Raw: n=80  W=73/L=7  WR=91.2%
- Refine: exclude H20=H20d drops 7/7 losers (100%)
- **Final: n=31  W=31/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when HTF20 mildly against

### W25.  `H60=H60e AND T1=T1c AND RSI=RSI4 AND direction_exec=short`
- Raw: n=80  W=73/L=7  WR=91.2%
- Refine: exclude H20=H20d drops 7/7 losers (100%)
- **Final: n=31  W=31/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when HTF20 mildly against

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND T1=T1c AND ZS=ZS5`
- Raw: n=238  W=91/L=147  WR=38.2%
- Sharpen: no sharper sub-pattern
- **Sharp: n=238  W=91/L=147  WR=38.2%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; zscore +2 to +3 deep overbought

### L02.  `H60=H60e AND ZS=ZS5 AND direction_exec=short`
- Raw: n=238  W=91/L=147  WR=38.2%
- Sharpen: no sharper sub-pattern
- **Sharp: n=238  W=91/L=147  WR=38.2%**
- **Dir: SHORT**  •  HTF60 strongly against; zscore +2 to +3 deep overbought

### L03.  `T1=T1c AND ZS=ZS5 AND direction_exec=short`
- Raw: n=238  W=91/L=147  WR=38.2%
- Sharpen: no sharper sub-pattern
- **Sharp: n=238  W=91/L=147  WR=38.2%**
- **Dir: SHORT**  •  1h trend AGAINST trade; zscore +2 to +3 deep overbought

### L04.  `H60=H60e AND T1=T1c AND ZS=ZS5 AND direction_exec=short`
- Raw: n=238  W=91/L=147  WR=38.2%
- Sharpen: no sharper sub-pattern
- **Sharp: n=238  W=91/L=147  WR=38.2%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; zscore +2 to +3 deep overbought

### L05.  `H60=H60e AND T4=T4c AND ZS=ZS5`
- Raw: n=206  W=79/L=127  WR=38.3%
- Sharpen: sharpest is RSI=RSI6 (67/127 of losers there)
- **Sharp: n=95  W=28/L=67  WR=29.5%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when RSI 70-80 overbought

### L06.  `T1=T1c AND T4=T4c AND ZS=ZS5`
- Raw: n=206  W=79/L=127  WR=38.3%
- Sharpen: sharpest is RSI=RSI6 (67/127 of losers there)
- **Sharp: n=95  W=28/L=67  WR=29.5%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when RSI 70-80 overbought

### L07.  `T4=T4c AND ZS=ZS5 AND direction_exec=short`
- Raw: n=206  W=79/L=127  WR=38.3%
- Sharpen: sharpest is RSI=RSI6 (67/127 of losers there)
- **Sharp: n=95  W=28/L=67  WR=29.5%**
- **Dir: SHORT**  •  4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when RSI 70-80 overbought

### L08.  `H60=H60e AND T1=T1c AND T4=T4c AND ZS=ZS5`
- Raw: n=206  W=79/L=127  WR=38.3%
- Sharpen: sharpest is RSI=RSI6 (67/127 of losers there)
- **Sharp: n=95  W=28/L=67  WR=29.5%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when RSI 70-80 overbought

### L09.  `H60=H60e AND T4=T4c AND ZS=ZS5 AND direction_exec=short`
- Raw: n=206  W=79/L=127  WR=38.3%
- Sharpen: sharpest is RSI=RSI6 (67/127 of losers there)
- **Sharp: n=95  W=28/L=67  WR=29.5%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when RSI 70-80 overbought

### L10.  `T1=T1c AND T4=T4c AND ZS=ZS5 AND direction_exec=short`
- Raw: n=206  W=79/L=127  WR=38.3%
- Sharpen: sharpest is RSI=RSI6 (67/127 of losers there)
- **Sharp: n=95  W=28/L=67  WR=29.5%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when RSI 70-80 overbought

### L11.  `H60=H60e AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=129  W=49/L=80  WR=38.0%
- Sharpen: sharpest is H20=H20d (56/80 of losers there)
- **Sharp: n=75  W=19/L=56  WR=25.3%**
- **Dir: ?**  •  HTF60 strongly against; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  ONLY when HTF20 mildly against

### L12.  `T1=T1c AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=129  W=49/L=80  WR=38.0%
- Sharpen: sharpest is H20=H20d (56/80 of losers there)
- **Sharp: n=75  W=19/L=56  WR=25.3%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  ONLY when HTF20 mildly against

### L13.  `RSI=RSI5 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=129  W=49/L=80  WR=38.0%
- Sharpen: sharpest is H20=H20d (56/80 of losers there)
- **Sharp: n=75  W=19/L=56  WR=25.3%**
- **Dir: SHORT**  •  RSI 60-70 strong; zscore +2 to +3 deep overbought  •  ONLY when HTF20 mildly against

### L14.  `H60=H60e AND T1=T1c AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=129  W=49/L=80  WR=38.0%
- Sharpen: sharpest is H20=H20d (56/80 of losers there)
- **Sharp: n=75  W=19/L=56  WR=25.3%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  ONLY when HTF20 mildly against

### L15.  `H60=H60e AND RSI=RSI5 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=129  W=49/L=80  WR=38.0%
- Sharpen: sharpest is H20=H20d (56/80 of losers there)
- **Sharp: n=75  W=19/L=56  WR=25.3%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  ONLY when HTF20 mildly against

### L16.  `T1=T1c AND RSI=RSI5 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=129  W=49/L=80  WR=38.0%
- Sharpen: sharpest is H20=H20d (56/80 of losers there)
- **Sharp: n=75  W=19/L=56  WR=25.3%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  ONLY when HTF20 mildly against

### L17.  `H20=H20e AND T4=T4c AND ZS=ZS5`
- Raw: n=98  W=38/L=60  WR=38.8%
- Sharpen: sharpest is RSI=RSI6 (51/60 of losers there)
- **Sharp: n=57  W=6/L=51  WR=10.5%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when RSI 70-80 overbought

### L18.  `H20=H20e AND H60=H60e AND T4=T4c AND ZS=ZS5`
- Raw: n=98  W=38/L=60  WR=38.8%
- Sharpen: sharpest is RSI=RSI6 (51/60 of losers there)
- **Sharp: n=57  W=6/L=51  WR=10.5%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when RSI 70-80 overbought

### L19.  `H20=H20e AND T1=T1c AND T4=T4c AND ZS=ZS5`
- Raw: n=98  W=38/L=60  WR=38.8%
- Sharpen: sharpest is RSI=RSI6 (51/60 of losers there)
- **Sharp: n=57  W=6/L=51  WR=10.5%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when RSI 70-80 overbought

### L20.  `H20=H20e AND T4=T4c AND ZS=ZS5 AND direction_exec=short`
- Raw: n=98  W=38/L=60  WR=38.8%
- Sharpen: sharpest is RSI=RSI6 (51/60 of losers there)
- **Sharp: n=57  W=6/L=51  WR=10.5%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when RSI 70-80 overbought

### L21.  `H60=H60e AND T4=T4c AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=97  W=37/L=60  WR=38.1%
- Sharpen: sharpest is session_bucket=asia (31/60 of losers there)
- **Sharp: n=38  W=7/L=31  WR=18.4%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  ONLY when session=asia

### L22.  `T1=T1c AND T4=T4c AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=97  W=37/L=60  WR=38.1%
- Sharpen: sharpest is session_bucket=asia (31/60 of losers there)
- **Sharp: n=38  W=7/L=31  WR=18.4%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  ONLY when session=asia

### L23.  `T4=T4c AND RSI=RSI5 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=97  W=37/L=60  WR=38.1%
- Sharpen: sharpest is session_bucket=asia (31/60 of losers there)
- **Sharp: n=38  W=7/L=31  WR=18.4%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  ONLY when session=asia

### L24.  `H60=H60e AND RSI=RSI6 AND ZS=ZS5`
- Raw: n=95  W=28/L=67  WR=29.5%
- Sharpen: sharpest is H20=H20e (51/67 of losers there)
- **Sharp: n=57  W=6/L=51  WR=10.5%**
- **Dir: ?**  •  HTF60 strongly against; RSI 70-80 overbought; zscore +2 to +3 deep overbought  •  ONLY when HTF20 strongly against

### L25.  `T1=T1c AND RSI=RSI6 AND ZS=ZS5`
- Raw: n=95  W=28/L=67  WR=29.5%
- Sharpen: sharpest is H20=H20e (51/67 of losers there)
- **Sharp: n=57  W=6/L=51  WR=10.5%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 70-80 overbought; zscore +2 to +3 deep overbought  •  ONLY when HTF20 strongly against

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | H60a(50/42) | H60e(50/58) |
| T1 | T1a(50/42) | T1c(50/58) |
| T4 | T4a(51/44) | T4c(49/56) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(50/42) | short(50/58) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
