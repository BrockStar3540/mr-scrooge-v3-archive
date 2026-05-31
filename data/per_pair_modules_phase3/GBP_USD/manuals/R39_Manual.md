# GBP_USD — R39 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50a**  (EMA50 up >0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **2,410**  (W=1,523 / L=887)  -  WR: **63.2%**

## Session distribution

- asia: n=1151  W=734/L=417  WR=63.8%
- ny_close: n=487  W=302/L=185  WR=62.0%
- off_hours: n=237  W=156/L=81  WR=65.8%
- ny_open: n=150  W=100/L=50  WR=66.7%
- london_open: n=137  W=82/L=55  WR=59.9%
- asia_late: n=95  W=61/L=34  WR=64.2%
- ny_mid: n=80  W=50/L=30  WR=62.5%
- london: n=73  W=38/L=35  WR=52.1%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND H60=H60a AND RSI=RSI6`
- Raw: n=221  W=188/L=33  WR=85.1%
- Refine: exclude strategy_id=charlie_compression_breakout drops 7/33 losers (21%)
- **Final: n=204  W=178/L=26  WR=87.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 70-80 overbought  •  AVOID when strategy=charlie_compression_breakout

### W02.  `H20=H20a AND H60=H60a AND T1=T1a AND RSI=RSI6`
- Raw: n=193  W=166/L=27  WR=86.0%
- Refine: exclude ZS=ZS4 drops 19/27 losers (70%)
- **Final: n=92  W=84/L=8  WR=91.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; RSI 70-80 overbought  •  AVOID when zscore +1 to +2 overbought

### W03.  `H20=H20a AND H60=H60a AND RSI=RSI6 AND direction_exec=long`
- Raw: n=193  W=166/L=27  WR=86.0%
- Refine: exclude ZS=ZS4 drops 19/27 losers (70%)
- **Final: n=92  W=84/L=8  WR=91.3%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 70-80 overbought  •  AVOID when zscore +1 to +2 overbought

### W04.  `H20=H20a AND H60=H60a AND T4=T4a AND RSI=RSI6`
- Raw: n=181  W=156/L=25  WR=86.2%
- Refine: exclude ZS=ZS4 drops 19/25 losers (76%)
- **Final: n=86  W=80/L=6  WR=93.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade; RSI 70-80 overbought  •  AVOID when zscore +1 to +2 overbought

### W05.  `H20=H20a AND BBP=BBP4 AND RSI=RSI6`
- Raw: n=175  W=149/L=26  WR=85.1%
- Refine: exclude session_bucket=asia drops 18/26 losers (69%)
- **Final: n=84  W=76/L=8  WR=90.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; upper third; RSI 70-80 overbought  •  AVOID when session=asia

### W06.  `H20=H20a AND T1=T1a AND BBP=BBP4 AND RSI=RSI6`
- Raw: n=174  W=148/L=26  WR=85.1%
- Refine: exclude session_bucket=asia drops 18/26 losers (69%)
- **Final: n=83  W=75/L=8  WR=90.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; upper third; RSI 70-80 overbought  •  AVOID when session=asia

### W07.  `H20=H20a AND BBP=BBP4 AND RSI=RSI6 AND direction_exec=long`
- Raw: n=174  W=148/L=26  WR=85.1%
- Refine: exclude session_bucket=asia drops 18/26 losers (69%)
- **Final: n=83  W=75/L=8  WR=90.4%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; upper third; RSI 70-80 overbought  •  AVOID when session=asia

### W08.  `T1=T1a AND T4=T4a AND BBP=BBP6`
- Raw: n=155  W=133/L=22  WR=85.8%
- Refine: exclude session_bucket=london drops 6/22 losers (27%)
- **Final: n=149  W=133/L=16  WR=89.3%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; deep above upper band  •  AVOID when session=london

### W09.  `T4=T4a AND BBP=BBP6 AND direction_exec=long`
- Raw: n=155  W=133/L=22  WR=85.8%
- Refine: exclude session_bucket=london drops 6/22 losers (27%)
- **Final: n=149  W=133/L=16  WR=89.3%**
- **Dir: LONG**  •  4h trend WITH trade; deep above upper band  •  AVOID when session=london

### W10.  `T1=T1a AND T4=T4a AND BBP=BBP6 AND direction_exec=long`
- Raw: n=155  W=133/L=22  WR=85.8%
- Refine: exclude session_bucket=london drops 6/22 losers (27%)
- **Final: n=149  W=133/L=16  WR=89.3%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; deep above upper band  •  AVOID when session=london

### W11.  `H20=H20a AND H60=H60a AND RSI=RSI6 AND session_bucket=asia`
- Raw: n=119  W=105/L=14  WR=88.2%
- Refine: exclude BBP=BBP4 drops 11/14 losers (79%)
- **Final: n=50  W=47/L=3  WR=94.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 70-80 overbought; session=asia  •  AVOID when upper third

### W12.  `H60=H60a AND T1=T1a AND RSI=RSI6 AND session_bucket=asia`
- Raw: n=113  W=97/L=16  WR=85.8%
- Refine: no further refinement
- **Final: n=113  W=97/L=16  WR=85.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 70-80 overbought; session=asia

### W13.  `H60=H60a AND T4=T4a AND RSI=RSI6 AND session_bucket=asia`
- Raw: n=113  W=97/L=16  WR=85.8%
- Refine: no further refinement
- **Final: n=113  W=97/L=16  WR=85.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 70-80 overbought; session=asia

### W14.  `H60=H60a AND RSI=RSI6 AND direction_exec=long AND session_bucket=asia`
- Raw: n=113  W=97/L=16  WR=85.8%
- Refine: no further refinement
- **Final: n=113  W=97/L=16  WR=85.8%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 70-80 overbought; session=asia

### W15.  `H20=H20a AND RSI=RSI6 AND ZS=ZS5`
- Raw: n=96  W=82/L=14  WR=85.4%
- Refine: exclude session_bucket=london drops 6/14 losers (43%)
- **Final: n=90  W=82/L=8  WR=91.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 70-80 overbought; zscore +2 to +3 deep overbought  •  AVOID when session=london

### W16.  `T1=T1a AND BBP=BBP6 AND session_bucket=asia`
- Raw: n=86  W=75/L=11  WR=87.2%
- Refine: exclude RSI=RSI4 drops 5/11 losers (45%)
- **Final: n=72  W=66/L=6  WR=91.7%**
- **Dir: ?**  •  1h trend WITH trade; deep above upper band; session=asia  •  AVOID when RSI 50-60 upper neutral

### W17.  `T4=T4a AND BBP=BBP6 AND session_bucket=asia`
- Raw: n=86  W=75/L=11  WR=87.2%
- Refine: exclude RSI=RSI4 drops 5/11 losers (45%)
- **Final: n=72  W=66/L=6  WR=91.7%**
- **Dir: ?**  •  4h trend WITH trade; deep above upper band; session=asia  •  AVOID when RSI 50-60 upper neutral

### W18.  `BBP=BBP6 AND direction_exec=long AND session_bucket=asia`
- Raw: n=86  W=75/L=11  WR=87.2%
- Refine: exclude RSI=RSI4 drops 5/11 losers (45%)
- **Final: n=72  W=66/L=6  WR=91.7%**
- **Dir: LONG**  •  deep above upper band; session=asia  •  AVOID when RSI 50-60 upper neutral

### W19.  `T1=T1a AND T4=T4a AND BBP=BBP6 AND session_bucket=asia`
- Raw: n=86  W=75/L=11  WR=87.2%
- Refine: exclude RSI=RSI4 drops 5/11 losers (45%)
- **Final: n=72  W=66/L=6  WR=91.7%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; deep above upper band; session=asia  •  AVOID when RSI 50-60 upper neutral

### W20.  `T1=T1a AND BBP=BBP6 AND direction_exec=long AND session_bucket=asia`
- Raw: n=86  W=75/L=11  WR=87.2%
- Refine: exclude RSI=RSI4 drops 5/11 losers (45%)
- **Final: n=72  W=66/L=6  WR=91.7%**
- **Dir: LONG**  •  1h trend WITH trade; deep above upper band; session=asia  •  AVOID when RSI 50-60 upper neutral

### W21.  `T4=T4a AND BBP=BBP6 AND direction_exec=long AND session_bucket=asia`
- Raw: n=86  W=75/L=11  WR=87.2%
- Refine: exclude RSI=RSI4 drops 5/11 losers (45%)
- **Final: n=72  W=66/L=6  WR=91.7%**
- **Dir: LONG**  •  4h trend WITH trade; deep above upper band; session=asia  •  AVOID when RSI 50-60 upper neutral

### W22.  `T4=T4a AND BBP=BBP6 AND RSI=RSI5`
- Raw: n=85  W=73/L=12  WR=85.9%
- Refine: exclude session_bucket=ny_close drops 7/12 losers (58%)
- **Final: n=73  W=68/L=5  WR=93.2%**
- **Dir: ?**  •  4h trend WITH trade; deep above upper band; RSI 60-70 strong  •  AVOID when session=ny_close

### W23.  `H20=H20e AND T4=T4c AND RSI=RSI5 AND session_bucket=ny_close`
- Raw: n=77  W=67/L=10  WR=87.0%
- Refine: exclude H60=H60e drops 8/10 losers (80%)
- **Final: n=34  W=32/L=2  WR=94.1%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 60-70 strong; session=ny_close  •  AVOID when HTF60 strongly against

### W24.  `H60=H60d AND T1=T1a AND BBP=BBP4`
- Raw: n=73  W=65/L=8  WR=89.0%
- Refine: exclude RSI=RSI5 drops 6/8 losers (75%)
- **Final: n=40  W=38/L=2  WR=95.0%**
- **Dir: ?**  •  HTF60 mildly against; 1h trend WITH trade; upper third  •  AVOID when RSI 60-70 strong

### W25.  `H60=H60d AND T1=T1a AND ZS=ZS4`
- Raw: n=73  W=65/L=8  WR=89.0%
- Refine: exclude RSI=RSI5 drops 6/8 losers (75%)
- **Final: n=40  W=38/L=2  WR=95.0%**
- **Dir: ?**  •  HTF60 mildly against; 1h trend WITH trade; zscore +1 to +2 overbought  •  AVOID when RSI 60-70 strong

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1c AND RSI=RSI6 AND direction_exec=short`
- Raw: n=318  W=125/L=193  WR=39.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=318  W=125/L=193  WR=39.3%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 70-80 overbought

### L02.  `T1=T1c AND T4=T4c AND RSI=RSI6`
- Raw: n=304  W=121/L=183  WR=39.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=304  W=121/L=183  WR=39.8%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 70-80 overbought

### L03.  `T4=T4c AND RSI=RSI6 AND direction_exec=short`
- Raw: n=304  W=121/L=183  WR=39.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=304  W=121/L=183  WR=39.8%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 70-80 overbought

### L04.  `T1=T1c AND T4=T4c AND RSI=RSI6 AND direction_exec=short`
- Raw: n=304  W=121/L=183  WR=39.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=304  W=121/L=183  WR=39.8%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 70-80 overbought

### L05.  `H20=H20e AND T1=T1c AND RSI=RSI6`
- Raw: n=243  W=85/L=158  WR=35.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=243  W=85/L=158  WR=35.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 70-80 overbought

### L06.  `H20=H20e AND RSI=RSI6 AND direction_exec=short`
- Raw: n=243  W=85/L=158  WR=35.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=243  W=85/L=158  WR=35.0%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 70-80 overbought

### L07.  `H20=H20e AND T1=T1c AND RSI=RSI6 AND direction_exec=short`
- Raw: n=243  W=85/L=158  WR=35.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=243  W=85/L=158  WR=35.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 70-80 overbought

### L08.  `H20=H20e AND T4=T4c AND RSI=RSI6`
- Raw: n=229  W=81/L=148  WR=35.4%
- Sharpen: no sharper sub-pattern
- **Sharp: n=229  W=81/L=148  WR=35.4%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 70-80 overbought

### L09.  `H20=H20e AND T1=T1c AND T4=T4c AND RSI=RSI6`
- Raw: n=229  W=81/L=148  WR=35.4%
- Sharpen: no sharper sub-pattern
- **Sharp: n=229  W=81/L=148  WR=35.4%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 70-80 overbought

### L10.  `H20=H20e AND T4=T4c AND RSI=RSI6 AND direction_exec=short`
- Raw: n=229  W=81/L=148  WR=35.4%
- Sharpen: no sharper sub-pattern
- **Sharp: n=229  W=81/L=148  WR=35.4%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 70-80 overbought

### L11.  `T1=T1c AND BBP=BBP4 AND RSI=RSI6`
- Raw: n=171  W=57/L=114  WR=33.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=171  W=57/L=114  WR=33.3%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; RSI 70-80 overbought

### L12.  `BBP=BBP4 AND RSI=RSI6 AND direction_exec=short`
- Raw: n=171  W=57/L=114  WR=33.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=171  W=57/L=114  WR=33.3%**
- **Dir: SHORT**  •  upper third; RSI 70-80 overbought

### L13.  `T1=T1c AND BBP=BBP4 AND RSI=RSI6 AND direction_exec=short`
- Raw: n=171  W=57/L=114  WR=33.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=171  W=57/L=114  WR=33.3%**
- **Dir: SHORT**  •  1h trend AGAINST trade; upper third; RSI 70-80 overbought

### L14.  `T4=T4c AND BBP=BBP4 AND RSI=RSI6`
- Raw: n=170  W=61/L=109  WR=35.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=170  W=61/L=109  WR=35.9%**
- **Dir: ?**  •  4h trend AGAINST trade; upper third; RSI 70-80 overbought

### L15.  `T1=T1c AND T4=T4c AND BBP=BBP4 AND RSI=RSI6`
- Raw: n=164  W=55/L=109  WR=33.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=164  W=55/L=109  WR=33.5%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; upper third; RSI 70-80 overbought

### L16.  `T4=T4c AND BBP=BBP4 AND RSI=RSI6 AND direction_exec=short`
- Raw: n=164  W=55/L=109  WR=33.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=164  W=55/L=109  WR=33.5%**
- **Dir: SHORT**  •  4h trend AGAINST trade; upper third; RSI 70-80 overbought

### L17.  `H20=H20e AND H60=H60e AND RSI=RSI6`
- Raw: n=163  W=51/L=112  WR=31.3%
- Sharpen: sharpest is ZS=ZS5 (36/112 of losers there)
- **Sharp: n=39  W=3/L=36  WR=7.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 70-80 overbought  •  ONLY when zscore +2 to +3 deep overbought

### L18.  `T1=T1c AND RSI=RSI6 AND ZS=ZS4`
- Raw: n=160  W=56/L=104  WR=35.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=160  W=56/L=104  WR=35.0%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 70-80 overbought; zscore +1 to +2 overbought

### L19.  `RSI=RSI6 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=160  W=56/L=104  WR=35.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=160  W=56/L=104  WR=35.0%**
- **Dir: SHORT**  •  RSI 70-80 overbought; zscore +1 to +2 overbought

### L20.  `T1=T1c AND BBP=BBP4 AND RSI=RSI6 AND ZS=ZS4`
- Raw: n=160  W=56/L=104  WR=35.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=160  W=56/L=104  WR=35.0%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; RSI 70-80 overbought; zscore +1 to +2 overbought

### L21.  `T1=T1c AND RSI=RSI6 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=160  W=56/L=104  WR=35.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=160  W=56/L=104  WR=35.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 70-80 overbought; zscore +1 to +2 overbought

### L22.  `BBP=BBP4 AND RSI=RSI6 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=160  W=56/L=104  WR=35.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=160  W=56/L=104  WR=35.0%**
- **Dir: SHORT**  •  upper third; RSI 70-80 overbought; zscore +1 to +2 overbought

### L23.  `T4=T4c AND RSI=RSI6 AND ZS=ZS4`
- Raw: n=159  W=60/L=99  WR=37.7%
- Sharpen: no sharper sub-pattern
- **Sharp: n=159  W=60/L=99  WR=37.7%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 70-80 overbought; zscore +1 to +2 overbought

### L24.  `T4=T4c AND BBP=BBP4 AND RSI=RSI6 AND ZS=ZS4`
- Raw: n=159  W=60/L=99  WR=37.7%
- Sharpen: no sharper sub-pattern
- **Sharp: n=159  W=60/L=99  WR=37.7%**
- **Dir: ?**  •  4h trend AGAINST trade; upper third; RSI 70-80 overbought; zscore +1 to +2 overbought

### L25.  `H60=H60e AND T1=T1c AND RSI=RSI6`
- Raw: n=157  W=60/L=97  WR=38.2%
- Sharpen: sharpest is H20=H20e (93/97 of losers there)
- **Sharp: n=139  W=46/L=93  WR=33.1%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when HTF20 strongly against

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(51/42) | H20e(40/48) |
| H60 | — | H60e(36/42) |
| T1 | T1a(58/43) | T1c(42/57) |
| T4 | T4a(57/44) | T4c(43/56) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(58/44) | short(42/56) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
