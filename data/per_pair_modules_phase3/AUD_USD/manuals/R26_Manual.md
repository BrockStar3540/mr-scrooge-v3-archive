# AUD_USD — R26 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **1,956**  (W=1,243 / L=713)  -  WR: **63.5%**

## Session distribution

- asia: n=950  W=605/L=345  WR=63.7%
- ny_close: n=441  W=278/L=163  WR=63.0%
- london_open: n=187  W=112/L=75  WR=59.9%
- asia_late: n=125  W=91/L=34  WR=72.8%
- off_hours: n=97  W=68/L=29  WR=70.1%
- ny_open: n=96  W=55/L=41  WR=57.3%
- london: n=60  W=34/L=26  WR=56.7%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1a AND T4=T4c AND BBP=BBP2`
- Raw: n=182  W=158/L=24  WR=86.8%
- Refine: exclude session_bucket=london drops 8/24 losers (33%)
- **Final: n=161  W=145/L=16  WR=90.1%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; lower third  •  AVOID when session=london

### W02.  `H60=H60e AND T4=T4c AND BBP=BBP2`
- Raw: n=177  W=153/L=24  WR=86.4%
- Refine: exclude session_bucket=london drops 8/24 losers (33%)
- **Final: n=156  W=140/L=16  WR=89.7%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; lower third  •  AVOID when session=london

### W03.  `T4=T4c AND BBP=BBP2 AND direction_exec=short`
- Raw: n=177  W=153/L=24  WR=86.4%
- Refine: exclude session_bucket=london drops 8/24 losers (33%)
- **Final: n=156  W=140/L=16  WR=89.7%**
- **Dir: SHORT**  •  4h trend AGAINST trade; lower third  •  AVOID when session=london

### W04.  `H60=H60e AND T1=T1a AND T4=T4c AND BBP=BBP2`
- Raw: n=177  W=153/L=24  WR=86.4%
- Refine: exclude session_bucket=london drops 8/24 losers (33%)
- **Final: n=156  W=140/L=16  WR=89.7%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; lower third  •  AVOID when session=london

### W05.  `H60=H60e AND T4=T4c AND BBP=BBP2 AND direction_exec=short`
- Raw: n=177  W=153/L=24  WR=86.4%
- Refine: exclude session_bucket=london drops 8/24 losers (33%)
- **Final: n=156  W=140/L=16  WR=89.7%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend AGAINST trade; lower third  •  AVOID when session=london

### W06.  `T1=T1a AND T4=T4c AND BBP=BBP2 AND direction_exec=short`
- Raw: n=177  W=153/L=24  WR=86.4%
- Refine: exclude session_bucket=london drops 8/24 losers (33%)
- **Final: n=156  W=140/L=16  WR=89.7%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend AGAINST trade; lower third  •  AVOID when session=london

### W07.  `T1=T1a AND T4=T4c AND ZS=ZS2`
- Raw: n=159  W=140/L=19  WR=88.1%
- Refine: exclude session_bucket=london drops 8/19 losers (42%)
- **Final: n=140  W=129/L=11  WR=92.1%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; zscore -2 to -1 oversold  •  AVOID when session=london

### W08.  `T1=T1a AND T4=T4c AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=159  W=140/L=19  WR=88.1%
- Refine: exclude session_bucket=london drops 8/19 losers (42%)
- **Final: n=140  W=129/L=11  WR=92.1%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; lower third; zscore -2 to -1 oversold  •  AVOID when session=london

### W09.  `H60=H60e AND T4=T4c AND ZS=ZS2`
- Raw: n=155  W=136/L=19  WR=87.7%
- Refine: exclude session_bucket=london drops 8/19 losers (42%)
- **Final: n=136  W=125/L=11  WR=91.9%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; zscore -2 to -1 oversold  •  AVOID when session=london

### W10.  `T4=T4c AND ZS=ZS2 AND direction_exec=short`
- Raw: n=155  W=136/L=19  WR=87.7%
- Refine: exclude session_bucket=london drops 8/19 losers (42%)
- **Final: n=136  W=125/L=11  WR=91.9%**
- **Dir: SHORT**  •  4h trend AGAINST trade; zscore -2 to -1 oversold  •  AVOID when session=london

### W11.  `H60=H60e AND T1=T1a AND T4=T4c AND ZS=ZS2`
- Raw: n=155  W=136/L=19  WR=87.7%
- Refine: exclude session_bucket=london drops 8/19 losers (42%)
- **Final: n=136  W=125/L=11  WR=91.9%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; zscore -2 to -1 oversold  •  AVOID when session=london

### W12.  `H60=H60e AND T4=T4c AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=155  W=136/L=19  WR=87.7%
- Refine: exclude session_bucket=london drops 8/19 losers (42%)
- **Final: n=136  W=125/L=11  WR=91.9%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; lower third; zscore -2 to -1 oversold  •  AVOID when session=london

### W13.  `H60=H60e AND T4=T4c AND ZS=ZS2 AND direction_exec=short`
- Raw: n=155  W=136/L=19  WR=87.7%
- Refine: exclude session_bucket=london drops 8/19 losers (42%)
- **Final: n=136  W=125/L=11  WR=91.9%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend AGAINST trade; zscore -2 to -1 oversold  •  AVOID when session=london

### W14.  `T1=T1a AND T4=T4c AND ZS=ZS2 AND direction_exec=short`
- Raw: n=155  W=136/L=19  WR=87.7%
- Refine: exclude session_bucket=london drops 8/19 losers (42%)
- **Final: n=136  W=125/L=11  WR=91.9%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend AGAINST trade; zscore -2 to -1 oversold  •  AVOID when session=london

### W15.  `T4=T4c AND BBP=BBP2 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=155  W=136/L=19  WR=87.7%
- Refine: exclude session_bucket=london drops 8/19 losers (42%)
- **Final: n=136  W=125/L=11  WR=91.9%**
- **Dir: SHORT**  •  4h trend AGAINST trade; lower third; zscore -2 to -1 oversold  •  AVOID when session=london

### W16.  `H60=H60e AND RSI=RSI2 AND session_bucket=ny_close`
- Raw: n=132  W=116/L=16  WR=87.9%
- Refine: exclude H20=H20a drops 12/16 losers (75%)
- **Final: n=78  W=74/L=4  WR=94.9%**
- **Dir: ?**  •  HTF60 strongly against; RSI 30-40 weak; session=ny_close  •  AVOID when HTF20 aligned WITH trade

### W17.  `T1=T1a AND RSI=RSI2 AND session_bucket=ny_close`
- Raw: n=132  W=116/L=16  WR=87.9%
- Refine: exclude H20=H20a drops 12/16 losers (75%)
- **Final: n=78  W=74/L=4  WR=94.9%**
- **Dir: ?**  •  1h trend WITH trade; RSI 30-40 weak; session=ny_close  •  AVOID when HTF20 aligned WITH trade

### W18.  `RSI=RSI2 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=132  W=116/L=16  WR=87.9%
- Refine: exclude H20=H20a drops 12/16 losers (75%)
- **Final: n=78  W=74/L=4  WR=94.9%**
- **Dir: SHORT**  •  RSI 30-40 weak; session=ny_close  •  AVOID when HTF20 aligned WITH trade

### W19.  `H60=H60e AND T1=T1a AND RSI=RSI2 AND session_bucket=ny_close`
- Raw: n=132  W=116/L=16  WR=87.9%
- Refine: exclude H20=H20a drops 12/16 losers (75%)
- **Final: n=78  W=74/L=4  WR=94.9%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; RSI 30-40 weak; session=ny_close  •  AVOID when HTF20 aligned WITH trade

### W20.  `H60=H60e AND RSI=RSI2 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=132  W=116/L=16  WR=87.9%
- Refine: exclude H20=H20a drops 12/16 losers (75%)
- **Final: n=78  W=74/L=4  WR=94.9%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 30-40 weak; session=ny_close  •  AVOID when HTF20 aligned WITH trade

### W21.  `T1=T1a AND RSI=RSI2 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=132  W=116/L=16  WR=87.9%
- Refine: exclude H20=H20a drops 12/16 losers (75%)
- **Final: n=78  W=74/L=4  WR=94.9%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 30-40 weak; session=ny_close  •  AVOID when HTF20 aligned WITH trade

### W22.  `H60=H60e AND T4=T4c AND BBP=BBP2 AND RSI=RSI2`
- Raw: n=120  W=106/L=14  WR=88.3%
- Refine: exclude session_bucket=london drops 8/14 losers (57%)
- **Final: n=112  W=106/L=6  WR=94.6%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; lower third; RSI 30-40 weak  •  AVOID when session=london

### W23.  `T1=T1a AND T4=T4c AND BBP=BBP2 AND RSI=RSI2`
- Raw: n=120  W=106/L=14  WR=88.3%
- Refine: exclude session_bucket=london drops 8/14 losers (57%)
- **Final: n=112  W=106/L=6  WR=94.6%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; lower third; RSI 30-40 weak  •  AVOID when session=london

### W24.  `T4=T4c AND BBP=BBP2 AND RSI=RSI2 AND direction_exec=short`
- Raw: n=120  W=106/L=14  WR=88.3%
- Refine: exclude session_bucket=london drops 8/14 losers (57%)
- **Final: n=112  W=106/L=6  WR=94.6%**
- **Dir: SHORT**  •  4h trend AGAINST trade; lower third; RSI 30-40 weak  •  AVOID when session=london

### W25.  `H60=H60e AND T4=T4c AND RSI=RSI2 AND ZS=ZS2`
- Raw: n=113  W=99/L=14  WR=87.6%
- Refine: exclude session_bucket=london drops 8/14 losers (57%)
- **Final: n=105  W=99/L=6  WR=94.3%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 30-40 weak; zscore -2 to -1 oversold  •  AVOID when session=london

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1c AND T4=T4a AND BBP=BBP2`
- Raw: n=159  W=61/L=98  WR=38.4%
- Sharpen: no sharper sub-pattern
- **Sharp: n=159  W=61/L=98  WR=38.4%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; lower third

### L02.  `H60=H60a AND T4=T4a AND BBP=BBP2`
- Raw: n=155  W=61/L=94  WR=39.4%
- Sharpen: no sharper sub-pattern
- **Sharp: n=155  W=61/L=94  WR=39.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; lower third

### L03.  `T4=T4a AND BBP=BBP2 AND direction_exec=long`
- Raw: n=155  W=61/L=94  WR=39.4%
- Sharpen: no sharper sub-pattern
- **Sharp: n=155  W=61/L=94  WR=39.4%**
- **Dir: LONG**  •  4h trend WITH trade; lower third

### L04.  `H60=H60a AND T1=T1c AND T4=T4a AND BBP=BBP2`
- Raw: n=155  W=61/L=94  WR=39.4%
- Sharpen: no sharper sub-pattern
- **Sharp: n=155  W=61/L=94  WR=39.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; lower third

### L05.  `H60=H60a AND T4=T4a AND BBP=BBP2 AND direction_exec=long`
- Raw: n=155  W=61/L=94  WR=39.4%
- Sharpen: no sharper sub-pattern
- **Sharp: n=155  W=61/L=94  WR=39.4%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend WITH trade; lower third

### L06.  `T1=T1c AND T4=T4a AND BBP=BBP2 AND direction_exec=long`
- Raw: n=155  W=61/L=94  WR=39.4%
- Sharpen: no sharper sub-pattern
- **Sharp: n=155  W=61/L=94  WR=39.4%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend WITH trade; lower third

### L07.  `T1=T1c AND T4=T4a AND ZS=ZS2`
- Raw: n=138  W=54/L=84  WR=39.1%
- Sharpen: sharpest is H20=H20b (22/84 of losers there)
- **Sharp: n=27  W=5/L=22  WR=18.5%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; zscore -2 to -1 oversold  •  ONLY when HTF20 slightly aligned

### L08.  `T1=T1c AND T4=T4a AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=138  W=54/L=84  WR=39.1%
- Sharpen: sharpest is H20=H20b (22/84 of losers there)
- **Sharp: n=27  W=5/L=22  WR=18.5%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; lower third; zscore -2 to -1 oversold  •  ONLY when HTF20 slightly aligned

### L09.  `H60=H60a AND T4=T4a AND ZS=ZS2`
- Raw: n=135  W=54/L=81  WR=40.0%
- Sharpen: sharpest is H20=H20b (22/81 of losers there)
- **Sharp: n=27  W=5/L=22  WR=18.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; zscore -2 to -1 oversold  •  ONLY when HTF20 slightly aligned

### L10.  `T4=T4a AND ZS=ZS2 AND direction_exec=long`
- Raw: n=135  W=54/L=81  WR=40.0%
- Sharpen: sharpest is H20=H20b (22/81 of losers there)
- **Sharp: n=27  W=5/L=22  WR=18.5%**
- **Dir: LONG**  •  4h trend WITH trade; zscore -2 to -1 oversold  •  ONLY when HTF20 slightly aligned

### L11.  `H60=H60a AND T1=T1c AND T4=T4a AND ZS=ZS2`
- Raw: n=135  W=54/L=81  WR=40.0%
- Sharpen: sharpest is H20=H20b (22/81 of losers there)
- **Sharp: n=27  W=5/L=22  WR=18.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; zscore -2 to -1 oversold  •  ONLY when HTF20 slightly aligned

### L12.  `H60=H60a AND T4=T4a AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=135  W=54/L=81  WR=40.0%
- Sharpen: sharpest is H20=H20b (22/81 of losers there)
- **Sharp: n=27  W=5/L=22  WR=18.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; lower third; zscore -2 to -1 oversold  •  ONLY when HTF20 slightly aligned

### L13.  `H60=H60a AND T4=T4a AND ZS=ZS2 AND direction_exec=long`
- Raw: n=135  W=54/L=81  WR=40.0%
- Sharpen: sharpest is H20=H20b (22/81 of losers there)
- **Sharp: n=27  W=5/L=22  WR=18.5%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend WITH trade; zscore -2 to -1 oversold  •  ONLY when HTF20 slightly aligned

### L14.  `T1=T1c AND T4=T4a AND ZS=ZS2 AND direction_exec=long`
- Raw: n=135  W=54/L=81  WR=40.0%
- Sharpen: sharpest is H20=H20b (22/81 of losers there)
- **Sharp: n=27  W=5/L=22  WR=18.5%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend WITH trade; zscore -2 to -1 oversold  •  ONLY when HTF20 slightly aligned

### L15.  `T4=T4a AND BBP=BBP2 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=135  W=54/L=81  WR=40.0%
- Sharpen: sharpest is H20=H20b (22/81 of losers there)
- **Sharp: n=27  W=5/L=22  WR=18.5%**
- **Dir: LONG**  •  4h trend WITH trade; lower third; zscore -2 to -1 oversold  •  ONLY when HTF20 slightly aligned

### L16.  `H60=H60a AND T4=T4a AND BBP=BBP2 AND RSI=RSI2`
- Raw: n=107  W=40/L=67  WR=37.4%
- Sharpen: sharpest is session_bucket=asia_late (14/67 of losers there)
- **Sharp: n=16  W=2/L=14  WR=12.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; lower third; RSI 30-40 weak  •  ONLY when session=asia_late

### L17.  `T1=T1c AND T4=T4a AND BBP=BBP2 AND RSI=RSI2`
- Raw: n=107  W=40/L=67  WR=37.4%
- Sharpen: sharpest is session_bucket=asia_late (14/67 of losers there)
- **Sharp: n=16  W=2/L=14  WR=12.5%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; lower third; RSI 30-40 weak  •  ONLY when session=asia_late

### L18.  `T4=T4a AND BBP=BBP2 AND RSI=RSI2 AND direction_exec=long`
- Raw: n=107  W=40/L=67  WR=37.4%
- Sharpen: sharpest is session_bucket=asia_late (14/67 of losers there)
- **Sharp: n=16  W=2/L=14  WR=12.5%**
- **Dir: LONG**  •  4h trend WITH trade; lower third; RSI 30-40 weak  •  ONLY when session=asia_late

### L19.  `H60=H60a AND RSI=RSI2 AND session_bucket=ny_close`
- Raw: n=101  W=26/L=75  WR=25.7%
- Sharpen: sharpest is H20=H20d (19/75 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 30-40 weak; session=ny_close  •  ONLY when HTF20 mildly against

### L20.  `T1=T1c AND RSI=RSI2 AND session_bucket=ny_close`
- Raw: n=101  W=26/L=75  WR=25.7%
- Sharpen: sharpest is H20=H20d (19/75 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 30-40 weak; session=ny_close  •  ONLY when HTF20 mildly against

### L21.  `RSI=RSI2 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=101  W=26/L=75  WR=25.7%
- Sharpen: sharpest is H20=H20d (19/75 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: LONG**  •  RSI 30-40 weak; session=ny_close  •  ONLY when HTF20 mildly against

### L22.  `H60=H60a AND T1=T1c AND RSI=RSI2 AND session_bucket=ny_close`
- Raw: n=101  W=26/L=75  WR=25.7%
- Sharpen: sharpest is H20=H20d (19/75 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 30-40 weak; session=ny_close  •  ONLY when HTF20 mildly against

### L23.  `H60=H60a AND RSI=RSI2 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=101  W=26/L=75  WR=25.7%
- Sharpen: sharpest is H20=H20d (19/75 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 30-40 weak; session=ny_close  •  ONLY when HTF20 mildly against

### L24.  `T1=T1c AND RSI=RSI2 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=101  W=26/L=75  WR=25.7%
- Sharpen: sharpest is H20=H20d (19/75 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 30-40 weak; session=ny_close  •  ONLY when HTF20 mildly against

### L25.  `H60=H60a AND T4=T4a AND RSI=RSI2 AND ZS=ZS2`
- Raw: n=100  W=40/L=60  WR=40.0%
- Sharpen: sharpest is session_bucket=asia_late (14/60 of losers there)
- **Sharp: n=16  W=2/L=14  WR=12.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 30-40 weak; zscore -2 to -1 oversold  •  ONLY when session=asia_late

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | H60e(55/41) | H60a(45/59) |
| T1 | T1a(58/40) | T1c(42/60) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(55/41) | long(45/59) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
