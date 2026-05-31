# GBP_CAD — R36 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50a**  (EMA50 up >0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **4,391**  (W=2,629 / L=1,762)  -  WR: **59.9%**

## Session distribution

- ny_mid: n=952  W=542/L=410  WR=56.9%
- asia: n=927  W=584/L=343  WR=63.0%
- ny_close: n=896  W=528/L=368  WR=58.9%
- ny_open: n=543  W=300/L=243  WR=55.2%
- london_open: n=413  W=259/L=154  WR=62.7%
- london: n=310  W=198/L=112  WR=63.9%
- off_hours: n=192  W=115/L=77  WR=59.9%
- asia_late: n=158  W=103/L=55  WR=65.2%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND H60=H60a AND ZS=ZS5`
- Raw: n=194  W=166/L=28  WR=85.6%
- Refine: exclude RSI=RSI5 drops 20/28 losers (71%)
- **Final: n=129  W=121/L=8  WR=93.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; zscore +2 to +3 deep overbought  •  AVOID when RSI 60-70 strong

### W02.  `H20=H20a AND T4=T4c AND ZS=ZS5`
- Raw: n=148  W=128/L=20  WR=86.5%
- Refine: exclude session_bucket=asia drops 15/20 losers (75%)
- **Final: n=105  W=100/L=5  WR=95.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  AVOID when session=asia

### W03.  `H20=H20a AND RSI=RSI6 AND ZS=ZS5`
- Raw: n=147  W=138/L=9  WR=93.9%
- Refine: exclude session_bucket=ny_open drops 7/9 losers (78%)
- **Final: n=140  W=138/L=2  WR=98.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 70-80 overbought; zscore +2 to +3 deep overbought  •  AVOID when session=ny_open

### W04.  `T4=T4a AND BBP=BBP6 AND RSI=RSI6 AND ZS=ZS5`
- Raw: n=121  W=111/L=10  WR=91.7%
- Refine: exclude session_bucket=asia_late drops 5/10 losers (50%)
- **Final: n=116  W=111/L=5  WR=95.7%**
- **Dir: ?**  •  4h trend WITH trade; deep above upper band; RSI 70-80 overbought; zscore +2 to +3 deep overbought  •  AVOID when session=asia_late

### W05.  `T1=T1a AND BBP=BBP6 AND RSI=RSI6 AND ZS=ZS5`
- Raw: n=121  W=105/L=16  WR=86.8%
- Refine: exclude T4=T4c drops 6/16 losers (38%)
- **Final: n=115  W=105/L=10  WR=91.3%**
- **Dir: ?**  •  1h trend WITH trade; deep above upper band; RSI 70-80 overbought; zscore +2 to +3 deep overbought  •  AVOID when 4h trend AGAINST trade

### W06.  `BBP=BBP6 AND RSI=RSI6 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=121  W=105/L=16  WR=86.8%
- Refine: exclude T4=T4c drops 6/16 losers (38%)
- **Final: n=115  W=105/L=10  WR=91.3%**
- **Dir: LONG**  •  deep above upper band; RSI 70-80 overbought; zscore +2 to +3 deep overbought  •  AVOID when 4h trend AGAINST trade

### W07.  `T1=T1a AND RSI=RSI6 AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=121  W=103/L=18  WR=85.1%
- Refine: exclude H60=H60d drops 5/18 losers (28%)
- **Final: n=116  W=103/L=13  WR=88.8%**
- **Dir: ?**  •  1h trend WITH trade; RSI 70-80 overbought; zscore +1 to +2 overbought; session=asia  •  AVOID when HTF60 mildly against

### W08.  `T4=T4a AND RSI=RSI6 AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=121  W=103/L=18  WR=85.1%
- Refine: exclude H60=H60d drops 5/18 losers (28%)
- **Final: n=116  W=103/L=13  WR=88.8%**
- **Dir: ?**  •  4h trend WITH trade; RSI 70-80 overbought; zscore +1 to +2 overbought; session=asia  •  AVOID when HTF60 mildly against

### W09.  `RSI=RSI6 AND ZS=ZS4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=121  W=103/L=18  WR=85.1%
- Refine: exclude H60=H60d drops 5/18 losers (28%)
- **Final: n=116  W=103/L=13  WR=88.8%**
- **Dir: LONG**  •  RSI 70-80 overbought; zscore +1 to +2 overbought; session=asia  •  AVOID when HTF60 mildly against

### W10.  `H20=H20a AND T1=T1c AND session_bucket=ny_close`
- Raw: n=116  W=101/L=15  WR=87.1%
- Refine: exclude ZS=ZS1 drops 6/15 losers (40%)
- **Final: n=102  W=93/L=9  WR=91.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; session=ny_close  •  AVOID when zscore -3 to -2 deep oversold

### W11.  `H20=H20a AND T4=T4c AND session_bucket=ny_close`
- Raw: n=116  W=101/L=15  WR=87.1%
- Refine: exclude ZS=ZS1 drops 6/15 losers (40%)
- **Final: n=102  W=93/L=9  WR=91.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; session=ny_close  •  AVOID when zscore -3 to -2 deep oversold

### W12.  `H20=H20a AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=116  W=101/L=15  WR=87.1%
- Refine: exclude ZS=ZS1 drops 6/15 losers (40%)
- **Final: n=102  W=93/L=9  WR=91.2%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; session=ny_close  •  AVOID when zscore -3 to -2 deep oversold

### W13.  `H20=H20a AND T1=T1c AND T4=T4c AND session_bucket=ny_close`
- Raw: n=116  W=101/L=15  WR=87.1%
- Refine: exclude ZS=ZS1 drops 6/15 losers (40%)
- **Final: n=102  W=93/L=9  WR=91.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_close  •  AVOID when zscore -3 to -2 deep oversold

### W14.  `H20=H20a AND T1=T1c AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=116  W=101/L=15  WR=87.1%
- Refine: exclude ZS=ZS1 drops 6/15 losers (40%)
- **Final: n=102  W=93/L=9  WR=91.2%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; session=ny_close  •  AVOID when zscore -3 to -2 deep oversold

### W15.  `H20=H20a AND T4=T4c AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=116  W=101/L=15  WR=87.1%
- Refine: exclude ZS=ZS1 drops 6/15 losers (40%)
- **Final: n=102  W=93/L=9  WR=91.2%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; session=ny_close  •  AVOID when zscore -3 to -2 deep oversold

### W16.  `H20=H20a AND H60=H60a AND T1=T1c AND session_bucket=ny_close`
- Raw: n=102  W=89/L=13  WR=87.3%
- Refine: exclude ZS=ZS1 drops 6/13 losers (46%)
- **Final: n=90  W=83/L=7  WR=92.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade; session=ny_close  •  AVOID when zscore -3 to -2 deep oversold

### W17.  `H20=H20a AND H60=H60a AND T4=T4c AND session_bucket=ny_close`
- Raw: n=102  W=89/L=13  WR=87.3%
- Refine: exclude ZS=ZS1 drops 6/13 losers (46%)
- **Final: n=90  W=83/L=7  WR=92.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend AGAINST trade; session=ny_close  •  AVOID when zscore -3 to -2 deep oversold

### W18.  `H20=H20a AND H60=H60a AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=102  W=89/L=13  WR=87.3%
- Refine: exclude ZS=ZS1 drops 6/13 losers (46%)
- **Final: n=90  W=83/L=7  WR=92.2%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=ny_close  •  AVOID when zscore -3 to -2 deep oversold

### W19.  `H20=H20a AND BBP=BBP6 AND RSI=RSI6`
- Raw: n=101  W=94/L=7  WR=93.1%
- Refine: exclude H60=H60e drops 7/7 losers (100%)
- **Final: n=82  W=82/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; deep above upper band; RSI 70-80 overbought  •  AVOID when HTF60 strongly against

### W20.  `H60=H60a AND T1=T1a AND RSI=RSI6 AND ZS=ZS5`
- Raw: n=100  W=85/L=15  WR=85.0%
- Refine: exclude H20=H20b drops 15/15 losers (100%)
- **Final: n=46  W=46/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 70-80 overbought; zscore +2 to +3 deep overbought  •  AVOID when HTF20 slightly aligned

### W21.  `H60=H60a AND T4=T4a AND RSI=RSI6 AND ZS=ZS5`
- Raw: n=100  W=85/L=15  WR=85.0%
- Refine: exclude H20=H20b drops 15/15 losers (100%)
- **Final: n=46  W=46/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 70-80 overbought; zscore +2 to +3 deep overbought  •  AVOID when HTF20 slightly aligned

### W22.  `H60=H60a AND RSI=RSI6 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=100  W=85/L=15  WR=85.0%
- Refine: exclude H20=H20b drops 15/15 losers (100%)
- **Final: n=46  W=46/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 70-80 overbought; zscore +2 to +3 deep overbought  •  AVOID when HTF20 slightly aligned

### W23.  `H20=H20a AND H60=H60a AND RSI=RSI6 AND ZS=ZS5`
- Raw: n=98  W=96/L=2  WR=98.0%
- Refine: exclude session_bucket=asia drops 2/2 losers (100%)
- **Final: n=48  W=48/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 70-80 overbought; zscore +2 to +3 deep overbought  •  AVOID when session=asia

### W24.  `H60=H60a AND T1=T1a AND RSI=RSI6 AND session_bucket=asia`
- Raw: n=97  W=83/L=14  WR=85.6%
- Refine: exclude BBP=BBP4 drops 10/14 losers (71%)
- **Final: n=57  W=53/L=4  WR=93.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 70-80 overbought; session=asia  •  AVOID when upper third

### W25.  `H60=H60a AND T4=T4a AND RSI=RSI6 AND session_bucket=asia`
- Raw: n=97  W=83/L=14  WR=85.6%
- Refine: exclude BBP=BBP4 drops 10/14 losers (71%)
- **Final: n=57  W=53/L=4  WR=93.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 70-80 overbought; session=asia  •  AVOID when upper third

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1c AND RSI=RSI6 AND session_bucket=asia`
- Raw: n=198  W=78/L=120  WR=39.4%
- Sharpen: sharpest is ZS=ZS5 (44/120 of losers there)
- **Sharp: n=56  W=12/L=44  WR=21.4%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 70-80 overbought; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L02.  `T4=T4c AND RSI=RSI6 AND session_bucket=asia`
- Raw: n=198  W=78/L=120  WR=39.4%
- Sharpen: sharpest is ZS=ZS5 (44/120 of losers there)
- **Sharp: n=56  W=12/L=44  WR=21.4%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 70-80 overbought; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L03.  `RSI=RSI6 AND direction_exec=short AND session_bucket=asia`
- Raw: n=198  W=78/L=120  WR=39.4%
- Sharpen: sharpest is ZS=ZS5 (44/120 of losers there)
- **Sharp: n=56  W=12/L=44  WR=21.4%**
- **Dir: SHORT**  •  RSI 70-80 overbought; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L04.  `T1=T1c AND T4=T4c AND RSI=RSI6 AND session_bucket=asia`
- Raw: n=198  W=78/L=120  WR=39.4%
- Sharpen: sharpest is ZS=ZS5 (44/120 of losers there)
- **Sharp: n=56  W=12/L=44  WR=21.4%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 70-80 overbought; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L05.  `T1=T1c AND RSI=RSI6 AND direction_exec=short AND session_bucket=asia`
- Raw: n=198  W=78/L=120  WR=39.4%
- Sharpen: sharpest is ZS=ZS5 (44/120 of losers there)
- **Sharp: n=56  W=12/L=44  WR=21.4%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 70-80 overbought; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L06.  `T4=T4c AND RSI=RSI6 AND direction_exec=short AND session_bucket=asia`
- Raw: n=198  W=78/L=120  WR=39.4%
- Sharpen: sharpest is ZS=ZS5 (44/120 of losers there)
- **Sharp: n=56  W=12/L=44  WR=21.4%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 70-80 overbought; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L07.  `H20=H20c AND T1=T1a AND RSI=RSI5`
- Raw: n=190  W=74/L=116  WR=38.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=190  W=74/L=116  WR=38.9%**
- **Dir: ?**  •  HTF20 neutral; 1h trend WITH trade; RSI 60-70 strong

### L08.  `H20=H20c AND RSI=RSI5 AND direction_exec=long`
- Raw: n=190  W=74/L=116  WR=38.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=190  W=74/L=116  WR=38.9%**
- **Dir: LONG**  •  HTF20 neutral; RSI 60-70 strong

### L09.  `H20=H20c AND T1=T1a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=188  W=73/L=115  WR=38.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=188  W=73/L=115  WR=38.8%**
- **Dir: LONG**  •  HTF20 neutral; 1h trend WITH trade; RSI 60-70 strong

### L10.  `T1=T1a AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=183  W=70/L=113  WR=38.3%
- Sharpen: sharpest is RSI=RSI5 (60/113 of losers there)
- **Sharp: n=71  W=11/L=60  WR=15.5%**
- **Dir: ?**  •  1h trend WITH trade; zscore +1 to +2 overbought; session=ny_mid  •  ONLY when RSI 60-70 strong

### L11.  `T1=T1a AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=183  W=70/L=113  WR=38.3%
- Sharpen: sharpest is RSI=RSI5 (60/113 of losers there)
- **Sharp: n=71  W=11/L=60  WR=15.5%**
- **Dir: ?**  •  1h trend WITH trade; upper third; zscore +1 to +2 overbought; session=ny_mid  •  ONLY when RSI 60-70 strong

### L12.  `T4=T4a AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=180  W=71/L=109  WR=39.4%
- Sharpen: sharpest is ZS=ZS4 (60/109 of losers there)
- **Sharp: n=77  W=17/L=60  WR=22.1%**
- **Dir: ?**  •  4h trend WITH trade; RSI 60-70 strong; session=ny_mid  •  ONLY when zscore +1 to +2 overbought

### L13.  `RSI=RSI5 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=180  W=71/L=109  WR=39.4%
- Sharpen: sharpest is ZS=ZS4 (60/109 of losers there)
- **Sharp: n=77  W=17/L=60  WR=22.1%**
- **Dir: LONG**  •  RSI 60-70 strong; session=ny_mid  •  ONLY when zscore +1 to +2 overbought

### L14.  `T4=T4a AND RSI=RSI5 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=180  W=71/L=109  WR=39.4%
- Sharpen: sharpest is ZS=ZS4 (60/109 of losers there)
- **Sharp: n=77  W=17/L=60  WR=22.1%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 60-70 strong; session=ny_mid  •  ONLY when zscore +1 to +2 overbought

### L15.  `H60=H60a AND T1=T1c AND session_bucket=asia`
- Raw: n=178  W=69/L=109  WR=38.8%
- Sharpen: sharpest is BBP=BBP4 (58/109 of losers there)
- **Sharp: n=64  W=6/L=58  WR=9.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=asia  •  ONLY when upper third

### L16.  `H60=H60a AND direction_exec=short AND session_bucket=asia`
- Raw: n=178  W=69/L=109  WR=38.8%
- Sharpen: sharpest is BBP=BBP4 (58/109 of losers there)
- **Sharp: n=64  W=6/L=58  WR=9.4%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; session=asia  •  ONLY when upper third

### L17.  `H60=H60a AND T1=T1c AND direction_exec=short AND session_bucket=asia`
- Raw: n=178  W=69/L=109  WR=38.8%
- Sharpen: sharpest is BBP=BBP4 (58/109 of losers there)
- **Sharp: n=64  W=6/L=58  WR=9.4%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=asia  •  ONLY when upper third

### L18.  `T1=T1a AND ZS=ZS4 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=177  W=70/L=107  WR=39.5%
- Sharpen: sharpest is RSI=RSI5 (54/107 of losers there)
- **Sharp: n=65  W=11/L=54  WR=16.9%**
- **Dir: LONG**  •  1h trend WITH trade; zscore +1 to +2 overbought; session=ny_mid  •  ONLY when RSI 60-70 strong

### L19.  `H60=H60a AND T4=T4c AND session_bucket=asia`
- Raw: n=171  W=66/L=105  WR=38.6%
- Sharpen: sharpest is BBP=BBP4 (58/105 of losers there)
- **Sharp: n=64  W=6/L=58  WR=9.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=asia  •  ONLY when upper third

### L20.  `H60=H60a AND T1=T1c AND T4=T4c AND session_bucket=asia`
- Raw: n=171  W=66/L=105  WR=38.6%
- Sharpen: sharpest is BBP=BBP4 (58/105 of losers there)
- **Sharp: n=64  W=6/L=58  WR=9.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; session=asia  •  ONLY when upper third

### L21.  `H60=H60a AND T4=T4c AND direction_exec=short AND session_bucket=asia`
- Raw: n=171  W=66/L=105  WR=38.6%
- Sharpen: sharpest is BBP=BBP4 (58/105 of losers there)
- **Sharp: n=64  W=6/L=58  WR=9.4%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=asia  •  ONLY when upper third

### L22.  `T4=T4c AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=155  W=56/L=99  WR=36.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=155  W=56/L=99  WR=36.1%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 70-80 overbought; session=ny_mid

### L23.  `BBP=BBP4 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=153  W=59/L=94  WR=38.6%
- Sharpen: sharpest is H20=H20c (36/94 of losers there)
- **Sharp: n=46  W=10/L=36  WR=21.7%**
- **Dir: SHORT**  •  upper third; session=ny_open  •  ONLY when HTF20 neutral

### L24.  `T4=T4c AND BBP=BBP4 AND session_bucket=ny_open`
- Raw: n=152  W=59/L=93  WR=38.8%
- Sharpen: sharpest is H20=H20c (36/93 of losers there)
- **Sharp: n=46  W=10/L=36  WR=21.7%**
- **Dir: ?**  •  4h trend AGAINST trade; upper third; session=ny_open  •  ONLY when HTF20 neutral

### L25.  `T4=T4c AND BBP=BBP4 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=152  W=59/L=93  WR=38.8%
- Sharpen: sharpest is H20=H20c (36/93 of losers there)
- **Sharp: n=46  W=10/L=36  WR=21.7%**
- **Dir: SHORT**  •  4h trend AGAINST trade; upper third; session=ny_open  •  ONLY when HTF20 neutral

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(33/23) | — |
| H60 | H60a(32/26) | — |
| T1 | — | — |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
