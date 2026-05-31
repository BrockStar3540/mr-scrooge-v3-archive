# USD_JPY — R38 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **3,554**  (W=2,258 / L=1,296)  -  WR: **63.5%**

## Session distribution

- asia: n=1626  W=1047/L=579  WR=64.4%
- ny_close: n=658  W=428/L=230  WR=65.0%
- ny_mid: n=378  W=227/L=151  WR=60.1%
- london: n=253  W=167/L=86  WR=66.0%
- ny_open: n=203  W=123/L=80  WR=60.6%
- asia_late: n=152  W=95/L=57  WR=62.5%
- london_open: n=151  W=90/L=61  WR=59.6%
- off_hours: n=133  W=81/L=52  WR=60.9%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1a AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=168  W=153/L=15  WR=91.1%
- Refine: exclude H20=H20a drops 11/15 losers (73%)
- **Final: n=96  W=92/L=4  WR=95.8%**
- **Dir: ?**  •  1h trend WITH trade; RSI 60-70 strong; session=asia  •  AVOID when HTF20 aligned WITH trade

### W02.  `RSI=RSI5 AND direction_exec=long AND session_bucket=asia`
- Raw: n=168  W=152/L=16  WR=90.5%
- Refine: exclude H20=H20a drops 12/16 losers (75%)
- **Final: n=95  W=91/L=4  WR=95.8%**
- **Dir: LONG**  •  RSI 60-70 strong; session=asia  •  AVOID when HTF20 aligned WITH trade

### W03.  `T1=T1a AND RSI=RSI5 AND direction_exec=long AND session_bucket=asia`
- Raw: n=167  W=152/L=15  WR=91.0%
- Refine: exclude H20=H20a drops 11/15 losers (73%)
- **Final: n=95  W=91/L=4  WR=95.8%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 60-70 strong; session=asia  •  AVOID when HTF20 aligned WITH trade

### W04.  `T1=T1a AND BBP=BBP4 AND RSI=RSI5`
- Raw: n=141  W=123/L=18  WR=87.2%
- Refine: exclude H20=H20a drops 13/18 losers (72%)
- **Final: n=83  W=78/L=5  WR=94.0%**
- **Dir: ?**  •  1h trend WITH trade; upper third; RSI 60-70 strong  •  AVOID when HTF20 aligned WITH trade

### W05.  `BBP=BBP4 AND RSI=RSI5 AND direction_exec=long`
- Raw: n=141  W=123/L=18  WR=87.2%
- Refine: exclude H20=H20a drops 13/18 losers (72%)
- **Final: n=83  W=78/L=5  WR=94.0%**
- **Dir: LONG**  •  upper third; RSI 60-70 strong  •  AVOID when HTF20 aligned WITH trade

### W06.  `T1=T1a AND BBP=BBP4 AND RSI=RSI5 AND direction_exec=long`
- Raw: n=141  W=123/L=18  WR=87.2%
- Refine: exclude H20=H20a drops 13/18 losers (72%)
- **Final: n=83  W=78/L=5  WR=94.0%**
- **Dir: LONG**  •  1h trend WITH trade; upper third; RSI 60-70 strong  •  AVOID when HTF20 aligned WITH trade

### W07.  `H20=H20e AND T1=T1a AND RSI=RSI5`
- Raw: n=140  W=133/L=7  WR=95.0%
- Refine: exclude ZS=ZS3 drops 5/7 losers (71%)
- **Final: n=121  W=119/L=2  WR=98.3%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when zscore -1 to +1 neutral

### W08.  `T4=T4a AND RSI=RSI5 AND direction_exec=long AND session_bucket=asia`
- Raw: n=140  W=124/L=16  WR=88.6%
- Refine: exclude H60=H60a drops 16/16 losers (100%)
- **Final: n=37  W=37/L=0  WR=100.0%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 60-70 strong; session=asia  •  AVOID when HTF60 aligned WITH trade

### W09.  `H20=H20e AND RSI=RSI5 AND direction_exec=long`
- Raw: n=139  W=132/L=7  WR=95.0%
- Refine: exclude ZS=ZS3 drops 5/7 losers (71%)
- **Final: n=120  W=118/L=2  WR=98.3%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 60-70 strong  •  AVOID when zscore -1 to +1 neutral

### W10.  `H20=H20e AND T1=T1a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=139  W=132/L=7  WR=95.0%
- Refine: exclude ZS=ZS3 drops 5/7 losers (71%)
- **Final: n=120  W=118/L=2  WR=98.3%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when zscore -1 to +1 neutral

### W11.  `T1=T1a AND T4=T4a AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=139  W=124/L=15  WR=89.2%
- Refine: exclude H60=H60a drops 15/15 losers (100%)
- **Final: n=37  W=37/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 60-70 strong; session=asia  •  AVOID when HTF60 aligned WITH trade

### W12.  `T4=T4a AND BBP=BBP4 AND RSI=RSI5`
- Raw: n=137  W=117/L=20  WR=85.4%
- Refine: exclude H20=H20a drops 15/20 losers (75%)
- **Final: n=77  W=72/L=5  WR=93.5%**
- **Dir: ?**  •  4h trend WITH trade; upper third; RSI 60-70 strong  •  AVOID when HTF20 aligned WITH trade

### W13.  `H60=H60a AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=131  W=115/L=16  WR=87.8%
- Refine: exclude T4=T4a drops 16/16 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 60-70 strong; session=asia  •  AVOID when 4h trend WITH trade

### W14.  `H60=H60a AND RSI=RSI5 AND direction_exec=long AND session_bucket=asia`
- Raw: n=131  W=115/L=16  WR=87.8%
- Refine: exclude T4=T4a drops 16/16 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 60-70 strong; session=asia  •  AVOID when 4h trend WITH trade

### W15.  `H60=H60a AND T1=T1a AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=130  W=115/L=15  WR=88.5%
- Refine: exclude ZS=ZS4 drops 8/15 losers (53%)
- **Final: n=90  W=83/L=7  WR=92.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong; session=asia  •  AVOID when zscore +1 to +2 overbought

### W16.  `T1=T1a AND T4=T4a AND BBP=BBP4 AND RSI=RSI5`
- Raw: n=128  W=113/L=15  WR=88.3%
- Refine: exclude H20=H20a drops 11/15 losers (73%)
- **Final: n=72  W=68/L=4  WR=94.4%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; upper third; RSI 60-70 strong  •  AVOID when HTF20 aligned WITH trade

### W17.  `T4=T4a AND BBP=BBP4 AND RSI=RSI5 AND direction_exec=long`
- Raw: n=128  W=113/L=15  WR=88.3%
- Refine: exclude H20=H20a drops 11/15 losers (73%)
- **Final: n=72  W=68/L=4  WR=94.4%**
- **Dir: LONG**  •  4h trend WITH trade; upper third; RSI 60-70 strong  •  AVOID when HTF20 aligned WITH trade

### W18.  `T1=T1a AND RSI=RSI5 AND ZS=ZS4`
- Raw: n=121  W=106/L=15  WR=87.6%
- Refine: exclude H20=H20a drops 11/15 losers (73%)
- **Final: n=78  W=74/L=4  WR=94.9%**
- **Dir: ?**  •  1h trend WITH trade; RSI 60-70 strong; zscore +1 to +2 overbought  •  AVOID when HTF20 aligned WITH trade

### W19.  `RSI=RSI5 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=121  W=106/L=15  WR=87.6%
- Refine: exclude H20=H20a drops 11/15 losers (73%)
- **Final: n=78  W=74/L=4  WR=94.9%**
- **Dir: LONG**  •  RSI 60-70 strong; zscore +1 to +2 overbought  •  AVOID when HTF20 aligned WITH trade

### W20.  `T1=T1a AND BBP=BBP4 AND RSI=RSI5 AND ZS=ZS4`
- Raw: n=121  W=106/L=15  WR=87.6%
- Refine: exclude H20=H20a drops 11/15 losers (73%)
- **Final: n=78  W=74/L=4  WR=94.9%**
- **Dir: ?**  •  1h trend WITH trade; upper third; RSI 60-70 strong; zscore +1 to +2 overbought  •  AVOID when HTF20 aligned WITH trade

### W21.  `T1=T1a AND RSI=RSI5 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=121  W=106/L=15  WR=87.6%
- Refine: exclude H20=H20a drops 11/15 losers (73%)
- **Final: n=78  W=74/L=4  WR=94.9%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 60-70 strong; zscore +1 to +2 overbought  •  AVOID when HTF20 aligned WITH trade

### W22.  `BBP=BBP4 AND RSI=RSI5 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=121  W=106/L=15  WR=87.6%
- Refine: exclude H20=H20a drops 11/15 losers (73%)
- **Final: n=78  W=74/L=4  WR=94.9%**
- **Dir: LONG**  •  upper third; RSI 60-70 strong; zscore +1 to +2 overbought  •  AVOID when HTF20 aligned WITH trade

### W23.  `H20=H20e AND T4=T4a AND RSI=RSI5`
- Raw: n=117  W=110/L=7  WR=94.0%
- Refine: exclude H60=H60a drops 6/7 losers (86%)
- **Final: n=94  W=93/L=1  WR=98.9%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; RSI 60-70 strong  •  AVOID when HTF60 aligned WITH trade

### W24.  `T1=T1a AND T4=T4a AND RSI=RSI5 AND ZS=ZS4`
- Raw: n=112  W=98/L=14  WR=87.5%
- Refine: exclude H20=H20a drops 11/14 losers (79%)
- **Final: n=69  W=66/L=3  WR=95.7%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 60-70 strong; zscore +1 to +2 overbought  •  AVOID when HTF20 aligned WITH trade

### W25.  `T4=T4a AND RSI=RSI5 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=112  W=98/L=14  WR=87.5%
- Refine: exclude H20=H20a drops 11/14 losers (79%)
- **Final: n=69  W=66/L=3  WR=95.7%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 60-70 strong; zscore +1 to +2 overbought  •  AVOID when HTF20 aligned WITH trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=298  W=110/L=188  WR=36.9%
- Sharpen: sharpest is H20=H20a (77/188 of losers there)
- **Sharp: n=101  W=24/L=77  WR=23.8%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when HTF20 aligned WITH trade

### L02.  `T4=T4c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=245  W=92/L=153  WR=37.6%
- Sharpen: sharpest is H20=H20a (63/153 of losers there)
- **Sharp: n=87  W=24/L=63  WR=27.6%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when HTF20 aligned WITH trade

### L03.  `T1=T1c AND T4=T4c AND RSI=RSI5`
- Raw: n=244  W=91/L=153  WR=37.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=244  W=91/L=153  WR=37.3%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 60-70 strong

### L04.  `T1=T1c AND T4=T4c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=244  W=91/L=153  WR=37.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=244  W=91/L=153  WR=37.3%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 60-70 strong

### L05.  `T1=T1c AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=126  W=49/L=77  WR=38.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=126  W=49/L=77  WR=38.9%**
- **Dir: SHORT**  •  1h trend AGAINST trade; session=ny_mid

### L06.  `T1=T1c AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=123  W=37/L=86  WR=30.1%
- Sharpen: sharpest is H20=H20a (39/86 of losers there)
- **Sharp: n=47  W=8/L=39  WR=17.0%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 60-70 strong; session=asia  •  ONLY when HTF20 aligned WITH trade

### L07.  `RSI=RSI5 AND direction_exec=short AND session_bucket=asia`
- Raw: n=123  W=38/L=85  WR=30.9%
- Sharpen: sharpest is H20=H20a (38/85 of losers there)
- **Sharp: n=46  W=8/L=38  WR=17.4%**
- **Dir: SHORT**  •  RSI 60-70 strong; session=asia  •  ONLY when HTF20 aligned WITH trade

### L08.  `T1=T1c AND RSI=RSI5 AND direction_exec=short AND session_bucket=asia`
- Raw: n=122  W=37/L=85  WR=30.3%
- Sharpen: sharpest is H20=H20a (38/85 of losers there)
- **Sharp: n=46  W=8/L=38  WR=17.4%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 60-70 strong; session=asia  •  ONLY when HTF20 aligned WITH trade

### L09.  `T1=T1c AND BBP=BBP4 AND RSI=RSI5`
- Raw: n=118  W=47/L=71  WR=39.8%
- Sharpen: sharpest is H20=H20c (20/71 of losers there)
- **Sharp: n=24  W=4/L=20  WR=16.7%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; RSI 60-70 strong  •  ONLY when HTF20 neutral

### L10.  `BBP=BBP4 AND RSI=RSI5 AND direction_exec=short`
- Raw: n=118  W=47/L=71  WR=39.8%
- Sharpen: sharpest is H20=H20c (20/71 of losers there)
- **Sharp: n=24  W=4/L=20  WR=16.7%**
- **Dir: SHORT**  •  upper third; RSI 60-70 strong  •  ONLY when HTF20 neutral

### L11.  `T1=T1c AND BBP=BBP4 AND RSI=RSI5 AND direction_exec=short`
- Raw: n=118  W=47/L=71  WR=39.8%
- Sharpen: sharpest is H20=H20c (20/71 of losers there)
- **Sharp: n=24  W=4/L=20  WR=16.7%**
- **Dir: SHORT**  •  1h trend AGAINST trade; upper third; RSI 60-70 strong  •  ONLY when HTF20 neutral

### L12.  `T4=T4c AND RSI=RSI5 AND direction_exec=short AND session_bucket=asia`
- Raw: n=109  W=38/L=71  WR=34.9%
- Sharpen: sharpest is BBP=BBP2 (13/71 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 60-70 strong; session=asia  •  ONLY when lower third

### L13.  `T1=T1c AND T4=T4c AND BBP=BBP4 AND RSI=RSI5`
- Raw: n=109  W=43/L=66  WR=39.4%
- Sharpen: sharpest is H20=H20c (20/66 of losers there)
- **Sharp: n=24  W=4/L=20  WR=16.7%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; upper third; RSI 60-70 strong  •  ONLY when HTF20 neutral

### L14.  `T4=T4c AND BBP=BBP4 AND RSI=RSI5 AND direction_exec=short`
- Raw: n=109  W=43/L=66  WR=39.4%
- Sharpen: sharpest is H20=H20c (20/66 of losers there)
- **Sharp: n=24  W=4/L=20  WR=16.7%**
- **Dir: SHORT**  •  4h trend AGAINST trade; upper third; RSI 60-70 strong  •  ONLY when HTF20 neutral

### L15.  `T1=T1c AND T4=T4c AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=108  W=37/L=71  WR=34.3%
- Sharpen: sharpest is BBP=BBP2 (13/71 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 60-70 strong; session=asia  •  ONLY when lower third

### L16.  `T1=T1c AND RSI=RSI5 AND ZS=ZS4`
- Raw: n=105  W=40/L=65  WR=38.1%
- Sharpen: sharpest is H20=H20c (20/65 of losers there)
- **Sharp: n=22  W=2/L=20  WR=9.1%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 60-70 strong; zscore +1 to +2 overbought  •  ONLY when HTF20 neutral

### L17.  `RSI=RSI5 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=105  W=40/L=65  WR=38.1%
- Sharpen: sharpest is H20=H20c (20/65 of losers there)
- **Sharp: n=22  W=2/L=20  WR=9.1%**
- **Dir: SHORT**  •  RSI 60-70 strong; zscore +1 to +2 overbought  •  ONLY when HTF20 neutral

### L18.  `T1=T1c AND BBP=BBP4 AND RSI=RSI5 AND ZS=ZS4`
- Raw: n=105  W=40/L=65  WR=38.1%
- Sharpen: sharpest is H20=H20c (20/65 of losers there)
- **Sharp: n=22  W=2/L=20  WR=9.1%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; RSI 60-70 strong; zscore +1 to +2 overbought  •  ONLY when HTF20 neutral

### L19.  `T1=T1c AND RSI=RSI5 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=105  W=40/L=65  WR=38.1%
- Sharpen: sharpest is H20=H20c (20/65 of losers there)
- **Sharp: n=22  W=2/L=20  WR=9.1%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 60-70 strong; zscore +1 to +2 overbought  •  ONLY when HTF20 neutral

### L20.  `BBP=BBP4 AND RSI=RSI5 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=105  W=40/L=65  WR=38.1%
- Sharpen: sharpest is H20=H20c (20/65 of losers there)
- **Sharp: n=22  W=2/L=20  WR=9.1%**
- **Dir: SHORT**  •  upper third; RSI 60-70 strong; zscore +1 to +2 overbought  •  ONLY when HTF20 neutral

### L21.  `H20=H20a AND T1=T1c AND RSI=RSI5`
- Raw: n=102  W=24/L=78  WR=23.5%
- Sharpen: sharpest is ZS=ZS5 (35/78 of losers there)
- **Sharp: n=37  W=2/L=35  WR=5.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when zscore +2 to +3 deep overbought

### L22.  `H20=H20a AND RSI=RSI5 AND direction_exec=short`
- Raw: n=101  W=24/L=77  WR=23.8%
- Sharpen: sharpest is ZS=ZS5 (34/77 of losers there)
- **Sharp: n=36  W=2/L=34  WR=5.6%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 60-70 strong  •  ONLY when zscore +2 to +3 deep overbought

### L23.  `H20=H20a AND T1=T1c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=101  W=24/L=77  WR=23.8%
- Sharpen: sharpest is ZS=ZS5 (34/77 of losers there)
- **Sharp: n=36  W=2/L=34  WR=5.6%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when zscore +2 to +3 deep overbought

### L24.  `T1=T1c AND T4=T4c AND RSI=RSI5 AND ZS=ZS4`
- Raw: n=99  W=38/L=61  WR=38.4%
- Sharpen: sharpest is H20=H20c (20/61 of losers there)
- **Sharp: n=22  W=2/L=20  WR=9.1%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 60-70 strong; zscore +1 to +2 overbought  •  ONLY when HTF20 neutral

### L25.  `T4=T4c AND RSI=RSI5 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=99  W=38/L=61  WR=38.4%
- Sharpen: sharpest is H20=H20c (20/61 of losers there)
- **Sharp: n=22  W=2/L=20  WR=9.1%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 60-70 strong; zscore +1 to +2 overbought  •  ONLY when HTF20 neutral

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20e(32/26) | — |
| H60 | — | — |
| T1 | T1a(54/46) | T1c(46/54) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(52/47) | short(48/53) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
