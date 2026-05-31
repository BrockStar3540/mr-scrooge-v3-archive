# USD_CAD — R24 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50a**  (EMA50 up >0.5x)
- **ADR = ADR3**  (60-90%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **1,830**  (W=1,123 / L=707)  -  WR: **61.4%**

## Session distribution

- ny_mid: n=853  W=518/L=335  WR=60.7%
- ny_close: n=375  W=232/L=143  WR=61.9%
- asia: n=221  W=130/L=91  WR=58.8%
- ny_open: n=200  W=126/L=74  WR=63.0%
- london_open: n=70  W=42/L=28  WR=60.0%
- off_hours: n=61  W=41/L=20  WR=67.2%
- asia_late: n=28  W=20/L=8  WR=71.4%
- london: n=22  W=14/L=8  WR=63.6%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60e AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=172  W=148/L=24  WR=86.0%
- Refine: exclude H20=H20e drops 24/24 losers (100%)
- **Final: n=44  W=44/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when HTF20 strongly against

### W02.  `H60=H60e AND T1=T1a AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=169  W=145/L=24  WR=85.8%
- Refine: exclude H20=H20e drops 24/24 losers (100%)
- **Final: n=44  W=44/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when HTF20 strongly against

### W03.  `H60=H60e AND RSI=RSI5 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=169  W=145/L=24  WR=85.8%
- Refine: exclude H20=H20e drops 24/24 losers (100%)
- **Final: n=44  W=44/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 strongly against; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when HTF20 strongly against

### W04.  `H60=H60e AND BBP=BBP5 AND RSI=RSI5`
- Raw: n=136  W=118/L=18  WR=86.8%
- Refine: exclude H20=H20e drops 18/18 losers (100%)
- **Final: n=34  W=34/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; just touched upper band; RSI 60-70 strong  •  AVOID when HTF20 strongly against

### W05.  `H60=H60e AND BBP=BBP5 AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=136  W=118/L=18  WR=86.8%
- Refine: exclude H20=H20e drops 18/18 losers (100%)
- **Final: n=34  W=34/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; just touched upper band; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when HTF20 strongly against

### W06.  `H60=H60e AND T1=T1a AND BBP=BBP5 AND RSI=RSI5`
- Raw: n=133  W=115/L=18  WR=86.5%
- Refine: exclude H20=H20e drops 18/18 losers (100%)
- **Final: n=34  W=34/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; just touched upper band; RSI 60-70 strong  •  AVOID when HTF20 strongly against

### W07.  `H60=H60e AND BBP=BBP5 AND RSI=RSI5 AND direction_exec=long`
- Raw: n=133  W=115/L=18  WR=86.5%
- Refine: exclude H20=H20e drops 18/18 losers (100%)
- **Final: n=34  W=34/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 strongly against; just touched upper band; RSI 60-70 strong  •  AVOID when HTF20 strongly against

### W08.  `H60=H60e AND T4=T4a AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=126  W=109/L=17  WR=86.5%
- Refine: exclude session_bucket=ny_close drops 10/17 losers (59%)
- **Final: n=106  W=99/L=7  WR=93.4%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when session=ny_close

### W09.  `H20=H20a AND T4=T4c AND BBP=BBP4 AND RSI=RSI5`
- Raw: n=101  W=86/L=15  WR=85.1%
- Refine: exclude session_bucket=asia drops 12/15 losers (80%)
- **Final: n=60  W=57/L=3  WR=95.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; upper third; RSI 60-70 strong  •  AVOID when session=asia

### W10.  `H60=H60a AND T4=T4c AND session_bucket=ny_close`
- Raw: n=95  W=81/L=14  WR=85.3%
- Refine: exclude BBP=BBP6 drops 6/14 losers (43%)
- **Final: n=89  W=81/L=8  WR=91.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=ny_close  •  AVOID when deep above upper band

### W11.  `H60=H60a AND T1=T1c AND T4=T4c AND session_bucket=ny_close`
- Raw: n=95  W=81/L=14  WR=85.3%
- Refine: exclude BBP=BBP6 drops 6/14 losers (43%)
- **Final: n=89  W=81/L=8  WR=91.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_close  •  AVOID when deep above upper band

### W12.  `H60=H60a AND T4=T4c AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=95  W=81/L=14  WR=85.3%
- Refine: exclude BBP=BBP6 drops 6/14 losers (43%)
- **Final: n=89  W=81/L=8  WR=91.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=ny_close  •  AVOID when deep above upper band

### W13.  `H60=H60e AND T4=T4a AND BBP=BBP5 AND RSI=RSI5`
- Raw: n=90  W=79/L=11  WR=87.8%
- Refine: exclude H20=H20e drops 11/11 losers (100%)
- **Final: n=34  W=34/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; just touched upper band; RSI 60-70 strong  •  AVOID when HTF20 strongly against

### W14.  `H20=H20a AND T4=T4c AND RSI=RSI5 AND ZS=ZS4`
- Raw: n=88  W=78/L=10  WR=88.6%
- Refine: exclude session_bucket=asia drops 9/10 losers (90%)
- **Final: n=50  W=49/L=1  WR=98.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 60-70 strong; zscore +1 to +2 overbought  •  AVOID when session=asia

### W15.  `H20=H20e AND RSI=RSI5 AND session_bucket=ny_open`
- Raw: n=81  W=74/L=7  WR=91.4%
- Refine: exclude H60=H60e drops 6/7 losers (86%)
- **Final: n=26  W=25/L=1  WR=96.2%**
- **Dir: ?**  •  HTF20 strongly against; RSI 60-70 strong; session=ny_open  •  AVOID when HTF60 strongly against

### W16.  `T1=T1a AND ZS=ZS3 AND session_bucket=ny_mid`
- Raw: n=80  W=68/L=12  WR=85.0%
- Refine: exclude strategy_id=bravo_expansion_continuation drops 6/12 losers (50%)
- **Final: n=59  W=53/L=6  WR=89.8%**
- **Dir: ?**  •  1h trend WITH trade; zscore -1 to +1 neutral; session=ny_mid  •  AVOID when strategy=bravo_expansion_continuation

### W17.  `ZS=ZS3 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=80  W=68/L=12  WR=85.0%
- Refine: exclude strategy_id=bravo_expansion_continuation drops 6/12 losers (50%)
- **Final: n=59  W=53/L=6  WR=89.8%**
- **Dir: LONG**  •  zscore -1 to +1 neutral; session=ny_mid  •  AVOID when strategy=bravo_expansion_continuation

### W18.  `T1=T1a AND ZS=ZS3 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=80  W=68/L=12  WR=85.0%
- Refine: exclude strategy_id=bravo_expansion_continuation drops 6/12 losers (50%)
- **Final: n=59  W=53/L=6  WR=89.8%**
- **Dir: LONG**  •  1h trend WITH trade; zscore -1 to +1 neutral; session=ny_mid  •  AVOID when strategy=bravo_expansion_continuation

### W19.  `H20=H20a AND T1=T1a AND session_bucket=ny_mid`
- Raw: n=79  W=69/L=10  WR=87.3%
- Refine: exclude H60=H60d drops 10/10 losers (100%)
- **Final: n=18  W=18/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=ny_mid  •  AVOID when HTF60 mildly against

### W20.  `H20=H20a AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=79  W=69/L=10  WR=87.3%
- Refine: exclude H60=H60d drops 10/10 losers (100%)
- **Final: n=18  W=18/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; session=ny_mid  •  AVOID when HTF60 mildly against

### W21.  `H20=H20a AND T1=T1a AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=79  W=69/L=10  WR=87.3%
- Refine: exclude H60=H60d drops 10/10 losers (100%)
- **Final: n=18  W=18/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; session=ny_mid  •  AVOID when HTF60 mildly against

### W22.  `H20=H20a AND T1=T1a AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=79  W=69/L=10  WR=87.3%
- Refine: exclude H60=H60d drops 10/10 losers (100%)
- **Final: n=18  W=18/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=ny_mid  •  AVOID when HTF60 mildly against

### W23.  `H20=H20a AND T4=T4a AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=79  W=69/L=10  WR=87.3%
- Refine: exclude H60=H60d drops 10/10 losers (100%)
- **Final: n=18  W=18/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=ny_mid  •  AVOID when HTF60 mildly against

### W24.  `T1=T1a AND ZS=ZS5 AND session_bucket=ny_open`
- Raw: n=74  W=63/L=11  WR=85.1%
- Refine: exclude H20=H20a drops 6/11 losers (55%)
- **Final: n=54  W=49/L=5  WR=90.7%**
- **Dir: ?**  •  1h trend WITH trade; zscore +2 to +3 deep overbought; session=ny_open  •  AVOID when HTF20 aligned WITH trade

### W25.  `T4=T4a AND ZS=ZS5 AND session_bucket=ny_open`
- Raw: n=74  W=63/L=11  WR=85.1%
- Refine: exclude H20=H20a drops 6/11 losers (55%)
- **Final: n=54  W=49/L=5  WR=90.7%**
- **Dir: ?**  •  4h trend WITH trade; zscore +2 to +3 deep overbought; session=ny_open  •  AVOID when HTF20 aligned WITH trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1c AND ZS=ZS5 AND direction_exec=short`
- Raw: n=225  W=90/L=135  WR=40.0%
- Sharpen: sharpest is BBP=BBP6 (45/135 of losers there)
- **Sharp: n=53  W=8/L=45  WR=15.1%**
- **Dir: SHORT**  •  1h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when deep above upper band

### L02.  `T1=T1c AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=199  W=79/L=120  WR=39.7%
- Sharpen: sharpest is H20=H20d (32/120 of losers there)
- **Sharp: n=38  W=6/L=32  WR=15.8%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 60-70 strong; session=ny_mid  •  ONLY when HTF20 mildly against

### L03.  `RSI=RSI5 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=199  W=79/L=120  WR=39.7%
- Sharpen: sharpest is H20=H20d (32/120 of losers there)
- **Sharp: n=38  W=6/L=32  WR=15.8%**
- **Dir: SHORT**  •  RSI 60-70 strong; session=ny_mid  •  ONLY when HTF20 mildly against

### L04.  `T1=T1c AND RSI=RSI5 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=199  W=79/L=120  WR=39.7%
- Sharpen: sharpest is H20=H20d (32/120 of losers there)
- **Sharp: n=38  W=6/L=32  WR=15.8%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 60-70 strong; session=ny_mid  •  ONLY when HTF20 mildly against

### L05.  `H60=H60a AND T1=T1c AND ZS=ZS5`
- Raw: n=192  W=75/L=117  WR=39.1%
- Sharpen: sharpest is BBP=BBP6 (45/117 of losers there)
- **Sharp: n=53  W=8/L=45  WR=15.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when deep above upper band

### L06.  `H60=H60a AND ZS=ZS5 AND direction_exec=short`
- Raw: n=192  W=75/L=117  WR=39.1%
- Sharpen: sharpest is BBP=BBP6 (45/117 of losers there)
- **Sharp: n=53  W=8/L=45  WR=15.1%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; zscore +2 to +3 deep overbought  •  ONLY when deep above upper band

### L07.  `H60=H60a AND T1=T1c AND ZS=ZS5 AND direction_exec=short`
- Raw: n=192  W=75/L=117  WR=39.1%
- Sharpen: sharpest is BBP=BBP6 (45/117 of losers there)
- **Sharp: n=53  W=8/L=45  WR=15.1%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when deep above upper band

### L08.  `H60=H60a AND T1=T1c AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=170  W=65/L=105  WR=38.2%
- Sharpen: sharpest is H20=H20d (27/105 of losers there)
- **Sharp: n=28  W=1/L=27  WR=3.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 60-70 strong; session=ny_mid  •  ONLY when HTF20 mildly against

### L09.  `H60=H60a AND RSI=RSI5 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=170  W=65/L=105  WR=38.2%
- Sharpen: sharpest is H20=H20d (27/105 of losers there)
- **Sharp: n=28  W=1/L=27  WR=3.6%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; RSI 60-70 strong; session=ny_mid  •  ONLY when HTF20 mildly against

### L10.  `T1=T1c AND T4=T4c AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=143  W=52/L=91  WR=36.4%
- Sharpen: sharpest is ZS=ZS5 (22/91 of losers there)
- **Sharp: n=22  W=0/L=22  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 60-70 strong; session=ny_mid  •  ONLY when zscore +2 to +3 deep overbought

### L11.  `T4=T4c AND RSI=RSI5 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=143  W=52/L=91  WR=36.4%
- Sharpen: sharpest is ZS=ZS5 (22/91 of losers there)
- **Sharp: n=22  W=0/L=22  WR=0.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 60-70 strong; session=ny_mid  •  ONLY when zscore +2 to +3 deep overbought

### L12.  `T1=T1c AND T4=T4a AND RSI=RSI5`
- Raw: n=142  W=55/L=87  WR=38.7%
- Sharpen: no sharper sub-pattern
- **Sharp: n=142  W=55/L=87  WR=38.7%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 60-70 strong

### L13.  `T4=T4a AND RSI=RSI5 AND direction_exec=short`
- Raw: n=142  W=55/L=87  WR=38.7%
- Sharpen: no sharper sub-pattern
- **Sharp: n=142  W=55/L=87  WR=38.7%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 60-70 strong

### L14.  `H20=H20a AND T1=T1c AND T4=T4a AND RSI=RSI5`
- Raw: n=142  W=55/L=87  WR=38.7%
- Sharpen: no sharper sub-pattern
- **Sharp: n=142  W=55/L=87  WR=38.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; RSI 60-70 strong

### L15.  `H20=H20a AND T4=T4a AND RSI=RSI5 AND direction_exec=short`
- Raw: n=142  W=55/L=87  WR=38.7%
- Sharpen: no sharper sub-pattern
- **Sharp: n=142  W=55/L=87  WR=38.7%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 60-70 strong

### L16.  `H60=H60a AND T1=T1c AND T4=T4a AND RSI=RSI5`
- Raw: n=142  W=55/L=87  WR=38.7%
- Sharpen: no sharper sub-pattern
- **Sharp: n=142  W=55/L=87  WR=38.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; RSI 60-70 strong

### L17.  `H60=H60a AND T4=T4a AND RSI=RSI5 AND direction_exec=short`
- Raw: n=142  W=55/L=87  WR=38.7%
- Sharpen: no sharper sub-pattern
- **Sharp: n=142  W=55/L=87  WR=38.7%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 60-70 strong

### L18.  `T1=T1c AND T4=T4a AND RSI=RSI5 AND direction_exec=short`
- Raw: n=142  W=55/L=87  WR=38.7%
- Sharpen: no sharper sub-pattern
- **Sharp: n=142  W=55/L=87  WR=38.7%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 60-70 strong

### L19.  `T4=T4a AND RSI=RSI5 AND session_bucket=ny_close`
- Raw: n=134  W=49/L=85  WR=36.6%
- Sharpen: sharpest is H20=H20a (52/85 of losers there)
- **Sharp: n=73  W=21/L=52  WR=28.8%**
- **Dir: ?**  •  4h trend WITH trade; RSI 60-70 strong; session=ny_close  •  ONLY when HTF20 aligned WITH trade

### L20.  `T1=T1c AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=132  W=48/L=84  WR=36.4%
- Sharpen: sharpest is H60=H60a (82/84 of losers there)
- **Sharp: n=115  W=33/L=82  WR=28.7%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  ONLY when HTF60 aligned WITH trade

### L21.  `RSI=RSI5 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=132  W=48/L=84  WR=36.4%
- Sharpen: sharpest is H60=H60a (82/84 of losers there)
- **Sharp: n=115  W=33/L=82  WR=28.7%**
- **Dir: SHORT**  •  RSI 60-70 strong; zscore +2 to +3 deep overbought  •  ONLY when HTF60 aligned WITH trade

### L22.  `T1=T1c AND RSI=RSI5 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=132  W=48/L=84  WR=36.4%
- Sharpen: sharpest is H60=H60a (82/84 of losers there)
- **Sharp: n=115  W=33/L=82  WR=28.7%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  ONLY when HTF60 aligned WITH trade

### L23.  `H60=H60a AND T4=T4c AND ZS=ZS5`
- Raw: n=123  W=49/L=74  WR=39.8%
- Sharpen: sharpest is RSI=RSI5 (61/74 of losers there)
- **Sharp: n=82  W=21/L=61  WR=25.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when RSI 60-70 strong

### L24.  `H60=H60a AND T1=T1c AND T4=T4c AND ZS=ZS5`
- Raw: n=123  W=49/L=74  WR=39.8%
- Sharpen: sharpest is RSI=RSI5 (61/74 of losers there)
- **Sharp: n=82  W=21/L=61  WR=25.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when RSI 60-70 strong

### L25.  `H60=H60a AND T4=T4c AND ZS=ZS5 AND direction_exec=short`
- Raw: n=123  W=49/L=74  WR=39.8%
- Sharpen: sharpest is RSI=RSI5 (61/74 of losers there)
- **Sharp: n=82  W=21/L=61  WR=25.6%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when RSI 60-70 strong

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | H60e(48/38) | H60a(38/48) |
| T1 | T1a(57/42) | T1c(43/58) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(57/42) | short(43/58) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
