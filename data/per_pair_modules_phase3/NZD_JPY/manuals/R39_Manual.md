# NZD_JPY — R39 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR3**  (60-90%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **2,771**  (W=1,688 / L=1,083)  -  WR: **60.9%**

## Session distribution

- asia: n=1000  W=587/L=413  WR=58.7%
- ny_mid: n=908  W=556/L=352  WR=61.2%
- london_open: n=450  W=277/L=173  WR=61.6%
- ny_close: n=228  W=143/L=85  WR=62.7%
- off_hours: n=66  W=46/L=20  WR=69.7%
- ny_open: n=62  W=42/L=20  WR=67.7%
- london: n=33  W=22/L=11  WR=66.7%
- asia_late: n=24  W=15/L=9  WR=62.5%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60a AND T1=T1a AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=198  W=171/L=27  WR=86.4%
- Refine: exclude ZS=ZS4 drops 17/27 losers (63%)
- **Final: n=125  W=115/L=10  WR=92.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong; session=ny_mid  •  AVOID when zscore +1 to +2 overbought

### W02.  `H60=H60a AND RSI=RSI5 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=198  W=171/L=27  WR=86.4%
- Refine: exclude ZS=ZS4 drops 17/27 losers (63%)
- **Final: n=125  W=115/L=10  WR=92.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 60-70 strong; session=ny_mid  •  AVOID when zscore +1 to +2 overbought

### W03.  `H60=H60a AND T1=T1a AND BBP=BBP6`
- Raw: n=169  W=146/L=23  WR=86.4%
- Refine: exclude H20=H20b drops 9/23 losers (39%)
- **Final: n=152  W=138/L=14  WR=90.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; deep above upper band  •  AVOID when HTF20 slightly aligned

### W04.  `T1=T1a AND BBP=BBP6 AND direction_exec=long`
- Raw: n=169  W=146/L=23  WR=86.4%
- Refine: exclude H20=H20b drops 9/23 losers (39%)
- **Final: n=152  W=138/L=14  WR=90.8%**
- **Dir: LONG**  •  1h trend WITH trade; deep above upper band  •  AVOID when HTF20 slightly aligned

### W05.  `H60=H60a AND T1=T1a AND BBP=BBP6 AND direction_exec=long`
- Raw: n=169  W=146/L=23  WR=86.4%
- Refine: exclude H20=H20b drops 9/23 losers (39%)
- **Final: n=152  W=138/L=14  WR=90.8%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; deep above upper band  •  AVOID when HTF20 slightly aligned

### W06.  `H60=H60a AND T4=T4a AND BBP=BBP6`
- Raw: n=160  W=139/L=21  WR=86.9%
- Refine: exclude H20=H20b drops 8/21 losers (38%)
- **Final: n=144  W=131/L=13  WR=91.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; deep above upper band  •  AVOID when HTF20 slightly aligned

### W07.  `T4=T4a AND BBP=BBP6 AND direction_exec=long`
- Raw: n=160  W=139/L=21  WR=86.9%
- Refine: exclude H20=H20b drops 8/21 losers (38%)
- **Final: n=144  W=131/L=13  WR=91.0%**
- **Dir: LONG**  •  4h trend WITH trade; deep above upper band  •  AVOID when HTF20 slightly aligned

### W08.  `H60=H60a AND T4=T4a AND BBP=BBP6 AND direction_exec=long`
- Raw: n=160  W=139/L=21  WR=86.9%
- Refine: exclude H20=H20b drops 8/21 losers (38%)
- **Final: n=144  W=131/L=13  WR=91.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend WITH trade; deep above upper band  •  AVOID when HTF20 slightly aligned

### W09.  `T1=T1a AND T4=T4a AND BBP=BBP6`
- Raw: n=156  W=139/L=17  WR=89.1%
- Refine: exclude H20=H20b drops 8/17 losers (47%)
- **Final: n=140  W=131/L=9  WR=93.6%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; deep above upper band  •  AVOID when HTF20 slightly aligned

### W10.  `H60=H60a AND T1=T1a AND T4=T4a AND BBP=BBP6`
- Raw: n=156  W=139/L=17  WR=89.1%
- Refine: exclude H20=H20b drops 8/17 losers (47%)
- **Final: n=140  W=131/L=9  WR=93.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; deep above upper band  •  AVOID when HTF20 slightly aligned

### W11.  `T1=T1a AND T4=T4a AND BBP=BBP6 AND direction_exec=long`
- Raw: n=156  W=139/L=17  WR=89.1%
- Refine: exclude H20=H20b drops 8/17 losers (47%)
- **Final: n=140  W=131/L=9  WR=93.6%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; deep above upper band  •  AVOID when HTF20 slightly aligned

### W12.  `T1=T1a AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=147  W=126/L=21  WR=85.7%
- Refine: exclude H20=H20a drops 21/21 losers (100%)
- **Final: n=46  W=46/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

### W13.  `H20=H20a AND T1=T1a AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=140  W=122/L=18  WR=87.1%
- Refine: exclude ZS=ZS4 drops 16/18 losers (89%)
- **Final: n=88  W=86/L=2  WR=97.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong; session=ny_mid  •  AVOID when zscore +1 to +2 overbought

### W14.  `H20=H20a AND RSI=RSI5 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=140  W=122/L=18  WR=87.1%
- Refine: exclude ZS=ZS4 drops 16/18 losers (89%)
- **Final: n=88  W=86/L=2  WR=97.7%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 60-70 strong; session=ny_mid  •  AVOID when zscore +1 to +2 overbought

### W15.  `H20=H20a AND H60=H60a AND BBP=BBP6`
- Raw: n=136  W=118/L=18  WR=86.8%
- Refine: exclude ZS=ZS5 drops 18/18 losers (100%)
- **Final: n=34  W=34/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; deep above upper band  •  AVOID when zscore +2 to +3 deep overbought

### W16.  `H20=H20a AND BBP=BBP6 AND direction_exec=long`
- Raw: n=136  W=118/L=18  WR=86.8%
- Refine: exclude ZS=ZS5 drops 18/18 losers (100%)
- **Final: n=34  W=34/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; deep above upper band  •  AVOID when zscore +2 to +3 deep overbought

### W17.  `H20=H20a AND H60=H60a AND BBP=BBP6 AND direction_exec=long`
- Raw: n=136  W=118/L=18  WR=86.8%
- Refine: exclude ZS=ZS5 drops 18/18 losers (100%)
- **Final: n=34  W=34/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; deep above upper band  •  AVOID when zscore +2 to +3 deep overbought

### W18.  `T1=T1a AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=135  W=120/L=15  WR=88.9%
- Refine: exclude RSI=RSI6 drops 10/15 losers (67%)
- **Final: n=97  W=92/L=5  WR=94.8%**
- **Dir: ?**  •  1h trend WITH trade; deep above upper band; zscore +2 to +3 deep overbought  •  AVOID when RSI 70-80 overbought

### W19.  `H20=H20a AND T1=T1a AND BBP=BBP6`
- Raw: n=132  W=118/L=14  WR=89.4%
- Refine: exclude RSI=RSI6 drops 10/14 losers (71%)
- **Final: n=76  W=72/L=4  WR=94.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; deep above upper band  •  AVOID when RSI 70-80 overbought

### W20.  `H20=H20a AND H60=H60a AND T1=T1a AND BBP=BBP6`
- Raw: n=132  W=118/L=14  WR=89.4%
- Refine: exclude RSI=RSI6 drops 10/14 losers (71%)
- **Final: n=76  W=72/L=4  WR=94.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; deep above upper band  •  AVOID when RSI 70-80 overbought

### W21.  `H20=H20a AND T1=T1a AND BBP=BBP6 AND direction_exec=long`
- Raw: n=132  W=118/L=14  WR=89.4%
- Refine: exclude RSI=RSI6 drops 10/14 losers (71%)
- **Final: n=76  W=72/L=4  WR=94.7%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; deep above upper band  •  AVOID when RSI 70-80 overbought

### W22.  `H20=H20a AND H60=H60a AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=132  W=114/L=18  WR=86.4%
- Refine: exclude session_bucket=london_open drops 14/18 losers (78%)
- **Final: n=98  W=94/L=4  WR=95.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when session=london_open

### W23.  `H20=H20a AND T1=T1a AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=132  W=114/L=18  WR=86.4%
- Refine: exclude session_bucket=london_open drops 14/18 losers (78%)
- **Final: n=98  W=94/L=4  WR=95.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when session=london_open

### W24.  `H20=H20a AND RSI=RSI5 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=132  W=114/L=18  WR=86.4%
- Refine: exclude session_bucket=london_open drops 14/18 losers (78%)
- **Final: n=98  W=94/L=4  WR=95.9%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when session=london_open

### W25.  `H60=H60a AND T4=T4a AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=127  W=109/L=18  WR=85.8%
- Refine: exclude H20=H20b drops 9/18 losers (50%)
- **Final: n=104  W=95/L=9  WR=91.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 60-70 strong; session=ny_mid  •  AVOID when HTF20 slightly aligned

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=486  W=190/L=296  WR=39.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=486  W=190/L=296  WR=39.1%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 60-70 strong

### L02.  `H60=H60e AND T1=T1c AND RSI=RSI5`
- Raw: n=440  W=163/L=277  WR=37.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=440  W=163/L=277  WR=37.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 60-70 strong

### L03.  `H60=H60e AND RSI=RSI5 AND direction_exec=short`
- Raw: n=440  W=163/L=277  WR=37.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=440  W=163/L=277  WR=37.0%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 60-70 strong

### L04.  `H60=H60e AND T1=T1c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=440  W=163/L=277  WR=37.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=440  W=163/L=277  WR=37.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 60-70 strong

### L05.  `T1=T1c AND T4=T4c AND RSI=RSI5`
- Raw: n=380  W=139/L=241  WR=36.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=380  W=139/L=241  WR=36.6%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 60-70 strong

### L06.  `T4=T4c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=380  W=139/L=241  WR=36.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=380  W=139/L=241  WR=36.6%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 60-70 strong

### L07.  `T1=T1c AND T4=T4c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=380  W=139/L=241  WR=36.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=380  W=139/L=241  WR=36.6%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 60-70 strong

### L08.  `H60=H60e AND T4=T4c AND RSI=RSI5`
- Raw: n=334  W=112/L=222  WR=33.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=334  W=112/L=222  WR=33.5%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 60-70 strong

### L09.  `H60=H60e AND T1=T1c AND T4=T4c AND RSI=RSI5`
- Raw: n=334  W=112/L=222  WR=33.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=334  W=112/L=222  WR=33.5%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 60-70 strong

### L10.  `H60=H60e AND T4=T4c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=334  W=112/L=222  WR=33.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=334  W=112/L=222  WR=33.5%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 60-70 strong

### L11.  `H20=H20e AND H60=H60e AND RSI=RSI5`
- Raw: n=312  W=122/L=190  WR=39.1%
- Sharpen: sharpest is T4=T4c (150/190 of losers there)
- **Sharp: n=228  W=78/L=150  WR=34.2%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 60-70 strong  •  ONLY when 4h trend AGAINST trade

### L12.  `H20=H20e AND T1=T1c AND RSI=RSI5`
- Raw: n=297  W=110/L=187  WR=37.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=297  W=110/L=187  WR=37.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 60-70 strong

### L13.  `H20=H20e AND RSI=RSI5 AND direction_exec=short`
- Raw: n=297  W=110/L=187  WR=37.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=297  W=110/L=187  WR=37.0%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 60-70 strong

### L14.  `H20=H20e AND T1=T1c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=297  W=110/L=187  WR=37.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=297  W=110/L=187  WR=37.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 60-70 strong

### L15.  `H20=H20e AND H60=H60e AND T1=T1c AND RSI=RSI5`
- Raw: n=284  W=105/L=179  WR=37.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=284  W=105/L=179  WR=37.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; RSI 60-70 strong

### L16.  `H20=H20e AND H60=H60e AND RSI=RSI5 AND direction_exec=short`
- Raw: n=284  W=105/L=179  WR=37.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=284  W=105/L=179  WR=37.0%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; RSI 60-70 strong

### L17.  `H60=H60e AND BBP=BBP4 AND RSI=RSI5`
- Raw: n=251  W=100/L=151  WR=39.8%
- Sharpen: sharpest is session_bucket=london_open (35/151 of losers there)
- **Sharp: n=42  W=7/L=35  WR=16.7%**
- **Dir: ?**  •  HTF60 strongly against; upper third; RSI 60-70 strong  •  ONLY when session=london_open

### L18.  `H20=H20e AND T4=T4c AND RSI=RSI5`
- Raw: n=241  W=83/L=158  WR=34.4%
- Sharpen: no sharper sub-pattern
- **Sharp: n=241  W=83/L=158  WR=34.4%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 60-70 strong

### L19.  `H20=H20e AND T1=T1c AND T4=T4c AND RSI=RSI5`
- Raw: n=241  W=83/L=158  WR=34.4%
- Sharpen: no sharper sub-pattern
- **Sharp: n=241  W=83/L=158  WR=34.4%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 60-70 strong

### L20.  `H20=H20e AND T4=T4c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=241  W=83/L=158  WR=34.4%
- Sharpen: no sharper sub-pattern
- **Sharp: n=241  W=83/L=158  WR=34.4%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 60-70 strong

### L21.  `H20=H20e AND H60=H60e AND T4=T4c AND RSI=RSI5`
- Raw: n=228  W=78/L=150  WR=34.2%
- Sharpen: no sharper sub-pattern
- **Sharp: n=228  W=78/L=150  WR=34.2%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; RSI 60-70 strong

### L22.  `H60=H60e AND T1=T1c AND BBP=BBP4 AND RSI=RSI5`
- Raw: n=223  W=83/L=140  WR=37.2%
- Sharpen: sharpest is session_bucket=london_open (35/140 of losers there)
- **Sharp: n=42  W=7/L=35  WR=16.7%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; upper third; RSI 60-70 strong  •  ONLY when session=london_open

### L23.  `H60=H60e AND BBP=BBP4 AND RSI=RSI5 AND direction_exec=short`
- Raw: n=223  W=83/L=140  WR=37.2%
- Sharpen: sharpest is session_bucket=london_open (35/140 of losers there)
- **Sharp: n=42  W=7/L=35  WR=16.7%**
- **Dir: SHORT**  •  HTF60 strongly against; upper third; RSI 60-70 strong  •  ONLY when session=london_open

### L24.  `H60=H60e AND T1=T1c AND RSI=RSI5 AND ZS=ZS4`
- Raw: n=214  W=83/L=131  WR=38.8%
- Sharpen: sharpest is session_bucket=london_open (31/131 of losers there)
- **Sharp: n=38  W=7/L=31  WR=18.4%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 60-70 strong; zscore +1 to +2 overbought  •  ONLY when session=london_open

### L25.  `H60=H60e AND RSI=RSI5 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=214  W=83/L=131  WR=38.8%
- Sharpen: sharpest is session_bucket=london_open (31/131 of losers there)
- **Sharp: n=38  W=7/L=31  WR=18.4%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 60-70 strong; zscore +1 to +2 overbought  •  ONLY when session=london_open

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(47/41) | H20e(38/47) |
| H60 | H60a(55/40) | H60e(40/54) |
| T1 | T1a(61/40) | T1c(39/60) |
| T4 | T4a(54/47) | T4c(46/53) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(57/43) | short(43/57) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
