# NZD_JPY — R38 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **1,585**  (W=1,021 / L=564)  -  WR: **64.4%**

## Session distribution

- asia: n=420  W=267/L=153  WR=63.6%
- ny_mid: n=387  W=256/L=131  WR=66.1%
- london_open: n=360  W=230/L=130  WR=63.9%
- ny_open: n=156  W=97/L=59  WR=62.2%
- ny_close: n=110  W=67/L=43  WR=60.9%
- london: n=84  W=60/L=24  WR=71.4%
- asia_late: n=68  W=44/L=24  WR=64.7%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1a AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=186  W=164/L=22  WR=88.2%
- Refine: exclude BBP=BBP6 drops 7/22 losers (32%)
- **Final: n=179  W=164/L=15  WR=91.6%**
- **Dir: ?**  •  1h trend WITH trade; RSI 60-70 strong; session=london_open  •  AVOID when deep above upper band

### W02.  `T1=T1a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=186  W=164/L=22  WR=88.2%
- Refine: exclude BBP=BBP6 drops 7/22 losers (32%)
- **Final: n=179  W=164/L=15  WR=91.6%**
- **Dir: LONG**  •  1h trend WITH trade; session=london_open  •  AVOID when deep above upper band

### W03.  `RSI=RSI5 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=186  W=164/L=22  WR=88.2%
- Refine: exclude BBP=BBP6 drops 7/22 losers (32%)
- **Final: n=179  W=164/L=15  WR=91.6%**
- **Dir: LONG**  •  RSI 60-70 strong; session=london_open  •  AVOID when deep above upper band

### W04.  `T1=T1a AND RSI=RSI5 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=186  W=164/L=22  WR=88.2%
- Refine: exclude BBP=BBP6 drops 7/22 losers (32%)
- **Final: n=179  W=164/L=15  WR=91.6%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 60-70 strong; session=london_open  •  AVOID when deep above upper band

### W05.  `T4=T4c AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=174  W=150/L=24  WR=86.2%
- Refine: exclude H20=H20d drops 20/24 losers (83%)
- **Final: n=119  W=115/L=4  WR=96.6%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 60-70 strong; session=ny_mid  •  AVOID when HTF20 mildly against

### W06.  `H60=H60a AND T1=T1a AND session_bucket=london_open`
- Raw: n=136  W=120/L=16  WR=88.2%
- Refine: exclude BBP=BBP6 drops 7/16 losers (44%)
- **Final: n=129  W=120/L=9  WR=93.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=london_open  •  AVOID when deep above upper band

### W07.  `H60=H60a AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=136  W=120/L=16  WR=88.2%
- Refine: exclude BBP=BBP6 drops 7/16 losers (44%)
- **Final: n=129  W=120/L=9  WR=93.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 60-70 strong; session=london_open  •  AVOID when deep above upper band

### W08.  `H60=H60a AND T1=T1a AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=136  W=120/L=16  WR=88.2%
- Refine: exclude BBP=BBP6 drops 7/16 losers (44%)
- **Final: n=129  W=120/L=9  WR=93.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong; session=london_open  •  AVOID when deep above upper band

### W09.  `H60=H60a AND T1=T1a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=136  W=120/L=16  WR=88.2%
- Refine: exclude BBP=BBP6 drops 7/16 losers (44%)
- **Final: n=129  W=120/L=9  WR=93.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=london_open  •  AVOID when deep above upper band

### W10.  `H60=H60a AND RSI=RSI5 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=136  W=120/L=16  WR=88.2%
- Refine: exclude BBP=BBP6 drops 7/16 losers (44%)
- **Final: n=129  W=120/L=9  WR=93.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 60-70 strong; session=london_open  •  AVOID when deep above upper band

### W11.  `T1=T1c AND T4=T4c AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=130  W=115/L=15  WR=88.5%
- Refine: exclude H20=H20d drops 11/15 losers (73%)
- **Final: n=97  W=93/L=4  WR=95.9%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 60-70 strong; session=ny_mid  •  AVOID when HTF20 mildly against

### W12.  `T4=T4c AND RSI=RSI5 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=130  W=115/L=15  WR=88.5%
- Refine: exclude H20=H20d drops 11/15 losers (73%)
- **Final: n=97  W=93/L=4  WR=95.9%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 60-70 strong; session=ny_mid  •  AVOID when HTF20 mildly against

### W13.  `T1=T1a AND BBP=BBP4 AND session_bucket=london_open`
- Raw: n=129  W=117/L=12  WR=90.7%
- Refine: no further refinement
- **Final: n=129  W=117/L=12  WR=90.7%**
- **Dir: ?**  •  1h trend WITH trade; upper third; session=london_open

### W14.  `BBP=BBP4 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=129  W=117/L=12  WR=90.7%
- Refine: no further refinement
- **Final: n=129  W=117/L=12  WR=90.7%**
- **Dir: LONG**  •  upper third; session=london_open

### W15.  `T1=T1a AND BBP=BBP4 AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=129  W=117/L=12  WR=90.7%
- Refine: no further refinement
- **Final: n=129  W=117/L=12  WR=90.7%**
- **Dir: ?**  •  1h trend WITH trade; upper third; RSI 60-70 strong; session=london_open

### W16.  `T1=T1a AND BBP=BBP4 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=129  W=117/L=12  WR=90.7%
- Refine: no further refinement
- **Final: n=129  W=117/L=12  WR=90.7%**
- **Dir: LONG**  •  1h trend WITH trade; upper third; session=london_open

### W17.  `BBP=BBP4 AND RSI=RSI5 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=129  W=117/L=12  WR=90.7%
- Refine: no further refinement
- **Final: n=129  W=117/L=12  WR=90.7%**
- **Dir: LONG**  •  upper third; RSI 60-70 strong; session=london_open

### W18.  `H60=H60e AND T4=T4c AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=122  W=107/L=15  WR=87.7%
- Refine: exclude H20=H20d drops 11/15 losers (73%)
- **Final: n=89  W=85/L=4  WR=95.5%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 60-70 strong; session=ny_mid  •  AVOID when HTF20 mildly against

### W19.  `T1=T1a AND T4=T4c AND session_bucket=london_open`
- Raw: n=120  W=105/L=15  WR=87.5%
- Refine: exclude BBP=BBP6 drops 7/15 losers (47%)
- **Final: n=113  W=105/L=8  WR=92.9%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; session=london_open  •  AVOID when deep above upper band

### W20.  `T1=T1a AND ZS=ZS4 AND session_bucket=london_open`
- Raw: n=115  W=105/L=10  WR=91.3%
- Refine: exclude H20=H20e drops 4/10 losers (40%)
- **Final: n=87  W=81/L=6  WR=93.1%**
- **Dir: ?**  •  1h trend WITH trade; zscore +1 to +2 overbought; session=london_open  •  AVOID when HTF20 strongly against

### W21.  `ZS=ZS4 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=115  W=105/L=10  WR=91.3%
- Refine: exclude H20=H20e drops 4/10 losers (40%)
- **Final: n=87  W=81/L=6  WR=93.1%**
- **Dir: LONG**  •  zscore +1 to +2 overbought; session=london_open  •  AVOID when HTF20 strongly against

### W22.  `T1=T1a AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=london_open`
- Raw: n=115  W=105/L=10  WR=91.3%
- Refine: exclude H20=H20e drops 4/10 losers (40%)
- **Final: n=87  W=81/L=6  WR=93.1%**
- **Dir: ?**  •  1h trend WITH trade; upper third; zscore +1 to +2 overbought; session=london_open  •  AVOID when HTF20 strongly against

### W23.  `T1=T1a AND RSI=RSI5 AND ZS=ZS4 AND session_bucket=london_open`
- Raw: n=115  W=105/L=10  WR=91.3%
- Refine: exclude H20=H20e drops 4/10 losers (40%)
- **Final: n=87  W=81/L=6  WR=93.1%**
- **Dir: ?**  •  1h trend WITH trade; RSI 60-70 strong; zscore +1 to +2 overbought; session=london_open  •  AVOID when HTF20 strongly against

### W24.  `T1=T1a AND ZS=ZS4 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=115  W=105/L=10  WR=91.3%
- Refine: exclude H20=H20e drops 4/10 losers (40%)
- **Final: n=87  W=81/L=6  WR=93.1%**
- **Dir: LONG**  •  1h trend WITH trade; zscore +1 to +2 overbought; session=london_open  •  AVOID when HTF20 strongly against

### W25.  `BBP=BBP4 AND ZS=ZS4 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=115  W=105/L=10  WR=91.3%
- Refine: exclude H20=H20e drops 4/10 losers (40%)
- **Final: n=87  W=81/L=6  WR=93.1%**
- **Dir: LONG**  •  upper third; zscore +1 to +2 overbought; session=london_open  •  AVOID when HTF20 strongly against

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1c AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=134  W=38/L=96  WR=28.4%
- Sharpen: sharpest is ZS=ZS4 (72/96 of losers there)
- **Sharp: n=84  W=12/L=72  WR=14.3%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 60-70 strong; session=london_open  •  ONLY when zscore +1 to +2 overbought

### L02.  `T1=T1c AND direction_exec=short AND session_bucket=london_open`
- Raw: n=134  W=38/L=96  WR=28.4%
- Sharpen: sharpest is ZS=ZS4 (72/96 of losers there)
- **Sharp: n=84  W=12/L=72  WR=14.3%**
- **Dir: SHORT**  •  1h trend AGAINST trade; session=london_open  •  ONLY when zscore +1 to +2 overbought

### L03.  `RSI=RSI5 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=134  W=38/L=96  WR=28.4%
- Sharpen: sharpest is ZS=ZS4 (72/96 of losers there)
- **Sharp: n=84  W=12/L=72  WR=14.3%**
- **Dir: SHORT**  •  RSI 60-70 strong; session=london_open  •  ONLY when zscore +1 to +2 overbought

### L04.  `T1=T1c AND RSI=RSI5 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=134  W=38/L=96  WR=28.4%
- Sharpen: sharpest is ZS=ZS4 (72/96 of losers there)
- **Sharp: n=84  W=12/L=72  WR=14.3%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 60-70 strong; session=london_open  •  ONLY when zscore +1 to +2 overbought

### L05.  `T1=T1c AND T4=T4a AND RSI=RSI5 AND ZS=ZS4`
- Raw: n=117  W=46/L=71  WR=39.3%
- Sharpen: sharpest is session_bucket=london_open (45/71 of losers there)
- **Sharp: n=50  W=5/L=45  WR=10.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 60-70 strong; zscore +1 to +2 overbought  •  ONLY when session=london_open

### L06.  `T4=T4a AND RSI=RSI5 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=117  W=46/L=71  WR=39.3%
- Sharpen: sharpest is session_bucket=london_open (45/71 of losers there)
- **Sharp: n=50  W=5/L=45  WR=10.0%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 60-70 strong; zscore +1 to +2 overbought  •  ONLY when session=london_open

### L07.  `H60=H60e AND T1=T1c AND session_bucket=london_open`
- Raw: n=104  W=36/L=68  WR=34.6%
- Sharpen: sharpest is ZS=ZS4 (45/68 of losers there)
- **Sharp: n=55  W=10/L=45  WR=18.2%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; session=london_open  •  ONLY when zscore +1 to +2 overbought

### L08.  `H60=H60e AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=104  W=36/L=68  WR=34.6%
- Sharpen: sharpest is ZS=ZS4 (45/68 of losers there)
- **Sharp: n=55  W=10/L=45  WR=18.2%**
- **Dir: ?**  •  HTF60 strongly against; RSI 60-70 strong; session=london_open  •  ONLY when zscore +1 to +2 overbought

### L09.  `H60=H60e AND T1=T1c AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=104  W=36/L=68  WR=34.6%
- Sharpen: sharpest is ZS=ZS4 (45/68 of losers there)
- **Sharp: n=55  W=10/L=45  WR=18.2%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 60-70 strong; session=london_open  •  ONLY when zscore +1 to +2 overbought

### L10.  `H60=H60e AND T1=T1c AND direction_exec=short AND session_bucket=london_open`
- Raw: n=104  W=36/L=68  WR=34.6%
- Sharpen: sharpest is ZS=ZS4 (45/68 of losers there)
- **Sharp: n=55  W=10/L=45  WR=18.2%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; session=london_open  •  ONLY when zscore +1 to +2 overbought

### L11.  `H60=H60e AND RSI=RSI5 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=104  W=36/L=68  WR=34.6%
- Sharpen: sharpest is ZS=ZS4 (45/68 of losers there)
- **Sharp: n=55  W=10/L=45  WR=18.2%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 60-70 strong; session=london_open  •  ONLY when zscore +1 to +2 overbought

### L12.  `T1=T1a AND T4=T4a AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=97  W=33/L=64  WR=34.0%
- Sharpen: sharpest is H20=H20a (50/64 of losers there)
- **Sharp: n=60  W=10/L=50  WR=16.7%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 60-70 strong; session=ny_mid  •  ONLY when HTF20 aligned WITH trade

### L13.  `T4=T4a AND RSI=RSI5 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=97  W=33/L=64  WR=34.0%
- Sharpen: sharpest is H20=H20a (50/64 of losers there)
- **Sharp: n=60  W=10/L=50  WR=16.7%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 60-70 strong; session=ny_mid  •  ONLY when HTF20 aligned WITH trade

### L14.  `T1=T1c AND BBP=BBP4 AND session_bucket=london_open`
- Raw: n=94  W=17/L=77  WR=18.1%
- Sharpen: sharpest is T4=T4a (45/77 of losers there)
- **Sharp: n=50  W=5/L=45  WR=10.0%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; session=london_open  •  ONLY when 4h trend WITH trade

### L15.  `BBP=BBP4 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=94  W=17/L=77  WR=18.1%
- Sharpen: sharpest is T4=T4a (45/77 of losers there)
- **Sharp: n=50  W=5/L=45  WR=10.0%**
- **Dir: SHORT**  •  upper third; session=london_open  •  ONLY when 4h trend WITH trade

### L16.  `T1=T1c AND BBP=BBP4 AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=94  W=17/L=77  WR=18.1%
- Sharpen: sharpest is T4=T4a (45/77 of losers there)
- **Sharp: n=50  W=5/L=45  WR=10.0%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; RSI 60-70 strong; session=london_open  •  ONLY when 4h trend WITH trade

### L17.  `T1=T1c AND BBP=BBP4 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=94  W=17/L=77  WR=18.1%
- Sharpen: sharpest is T4=T4a (45/77 of losers there)
- **Sharp: n=50  W=5/L=45  WR=10.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; upper third; session=london_open  •  ONLY when 4h trend WITH trade

### L18.  `BBP=BBP4 AND RSI=RSI5 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=94  W=17/L=77  WR=18.1%
- Sharpen: sharpest is T4=T4a (45/77 of losers there)
- **Sharp: n=50  W=5/L=45  WR=10.0%**
- **Dir: SHORT**  •  upper third; RSI 60-70 strong; session=london_open  •  ONLY when 4h trend WITH trade

### L19.  `H60=H60a AND T4=T4a AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=94  W=33/L=61  WR=35.1%
- Sharpen: sharpest is H20=H20a (50/61 of losers there)
- **Sharp: n=60  W=10/L=50  WR=16.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 60-70 strong; session=ny_mid  •  ONLY when HTF20 aligned WITH trade

### L20.  `T1=T1c AND T4=T4a AND session_bucket=london_open`
- Raw: n=88  W=25/L=63  WR=28.4%
- Sharpen: sharpest is BBP=BBP4 (45/63 of losers there)
- **Sharp: n=50  W=5/L=45  WR=10.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; session=london_open  •  ONLY when upper third

### L21.  `T1=T1c AND ZS=ZS4 AND session_bucket=london_open`
- Raw: n=84  W=12/L=72  WR=14.3%
- Sharpen: sharpest is T4=T4a (45/72 of losers there)
- **Sharp: n=50  W=5/L=45  WR=10.0%**
- **Dir: ?**  •  1h trend AGAINST trade; zscore +1 to +2 overbought; session=london_open  •  ONLY when 4h trend WITH trade

### L22.  `ZS=ZS4 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=84  W=12/L=72  WR=14.3%
- Sharpen: sharpest is T4=T4a (45/72 of losers there)
- **Sharp: n=50  W=5/L=45  WR=10.0%**
- **Dir: SHORT**  •  zscore +1 to +2 overbought; session=london_open  •  ONLY when 4h trend WITH trade

### L23.  `T1=T1c AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=london_open`
- Raw: n=84  W=12/L=72  WR=14.3%
- Sharpen: sharpest is T4=T4a (45/72 of losers there)
- **Sharp: n=50  W=5/L=45  WR=10.0%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; zscore +1 to +2 overbought; session=london_open  •  ONLY when 4h trend WITH trade

### L24.  `T1=T1c AND RSI=RSI5 AND ZS=ZS4 AND session_bucket=london_open`
- Raw: n=84  W=12/L=72  WR=14.3%
- Sharpen: sharpest is T4=T4a (45/72 of losers there)
- **Sharp: n=50  W=5/L=45  WR=10.0%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 60-70 strong; zscore +1 to +2 overbought; session=london_open  •  ONLY when 4h trend WITH trade

### L25.  `T1=T1c AND ZS=ZS4 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=84  W=12/L=72  WR=14.3%
- Sharpen: sharpest is T4=T4a (45/72 of losers there)
- **Sharp: n=50  W=5/L=45  WR=10.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; zscore +1 to +2 overbought; session=london_open  •  ONLY when 4h trend WITH trade

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(43/29) | H20e(31/46) |
| H60 | — | — |
| T1 | T1a(55/42) | T1c(45/58) |
| T4 | T4a(52/46) | T4c(48/54) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(53/45) | short(47/55) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
