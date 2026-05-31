# USD_JPY — R21 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **5,329**  (W=3,264 / L=2,065)  -  WR: **61.2%**

## Session distribution

- asia: n=2089  W=1272/L=817  WR=60.9%
- london_open: n=867  W=528/L=339  WR=60.9%
- ny_mid: n=733  W=440/L=293  WR=60.0%
- ny_open: n=570  W=344/L=226  WR=60.4%
- ny_close: n=435  W=280/L=155  WR=64.4%
- london: n=350  W=217/L=133  WR=62.0%
- asia_late: n=217  W=142/L=75  WR=65.4%
- off_hours: n=68  W=41/L=27  WR=60.3%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60a AND T1=T1a AND RSI=RSI2`
- Raw: n=150  W=131/L=19  WR=87.3%
- Refine: exclude ZS=ZS2 drops 19/19 losers (100%)
- **Final: n=61  W=61/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 30-40 weak  •  AVOID when zscore -2 to -1 oversold

### W02.  `H60=H60a AND RSI=RSI2 AND direction_exec=short`
- Raw: n=150  W=131/L=19  WR=87.3%
- Refine: exclude ZS=ZS2 drops 19/19 losers (100%)
- **Final: n=61  W=61/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; RSI 30-40 weak  •  AVOID when zscore -2 to -1 oversold

### W03.  `H60=H60a AND T1=T1a AND RSI=RSI2 AND direction_exec=short`
- Raw: n=150  W=131/L=19  WR=87.3%
- Refine: exclude ZS=ZS2 drops 19/19 losers (100%)
- **Final: n=61  W=61/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 30-40 weak  •  AVOID when zscore -2 to -1 oversold

### W04.  `H60=H60a AND direction_exec=short AND session_bucket=asia`
- Raw: n=140  W=123/L=17  WR=87.9%
- Refine: exclude RSI=RSI3 drops 13/17 losers (76%)
- **Final: n=97  W=93/L=4  WR=95.9%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; session=asia  •  AVOID when RSI 40-50 lower neutral

### W05.  `H60=H60a AND T1=T1a AND direction_exec=short AND session_bucket=asia`
- Raw: n=131  W=115/L=16  WR=87.8%
- Refine: exclude RSI=RSI3 drops 12/16 losers (75%)
- **Final: n=97  W=93/L=4  WR=95.9%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=asia  •  AVOID when RSI 40-50 lower neutral

### W06.  `H20=H20c AND T1=T1a AND BBP=BBP2 AND session_bucket=asia`
- Raw: n=123  W=107/L=16  WR=87.0%
- Refine: exclude H60=H60d drops 14/16 losers (88%)
- **Final: n=77  W=75/L=2  WR=97.4%**
- **Dir: ?**  •  HTF20 neutral; 1h trend WITH trade; lower third; session=asia  •  AVOID when HTF60 mildly against

### W07.  `H20=H20c AND BBP=BBP2 AND direction_exec=short AND session_bucket=asia`
- Raw: n=123  W=107/L=16  WR=87.0%
- Refine: exclude H60=H60d drops 14/16 losers (88%)
- **Final: n=77  W=75/L=2  WR=97.4%**
- **Dir: SHORT**  •  HTF20 neutral; lower third; session=asia  •  AVOID when HTF60 mildly against

### W08.  `H20=H20d AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=119  W=105/L=14  WR=88.2%
- Refine: exclude T1=T1c drops 14/14 losers (100%)
- **Final: n=59  W=59/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 mildly against; RSI 30-40 weak; session=asia  •  AVOID when 1h trend AGAINST trade

### W09.  `H20=H20d AND H60=H60a AND session_bucket=asia`
- Raw: n=117  W=103/L=14  WR=88.0%
- Refine: exclude T1=T1c drops 14/14 losers (100%)
- **Final: n=57  W=57/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 aligned WITH trade; session=asia  •  AVOID when 1h trend AGAINST trade

### W10.  `H20=H20d AND H60=H60a AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=115  W=101/L=14  WR=87.8%
- Refine: exclude T1=T1c drops 14/14 losers (100%)
- **Final: n=55  W=55/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 aligned WITH trade; RSI 30-40 weak; session=asia  •  AVOID when 1h trend AGAINST trade

### W11.  `H20=H20c AND T1=T1a AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=115  W=99/L=16  WR=86.1%
- Refine: exclude H60=H60d drops 14/16 losers (88%)
- **Final: n=77  W=75/L=2  WR=97.4%**
- **Dir: ?**  •  HTF20 neutral; 1h trend WITH trade; zscore -2 to -1 oversold; session=asia  •  AVOID when HTF60 mildly against

### W12.  `H20=H20c AND ZS=ZS2 AND direction_exec=short AND session_bucket=asia`
- Raw: n=115  W=99/L=16  WR=86.1%
- Refine: exclude H60=H60d drops 14/16 losers (88%)
- **Final: n=77  W=75/L=2  WR=97.4%**
- **Dir: SHORT**  •  HTF20 neutral; zscore -2 to -1 oversold; session=asia  •  AVOID when HTF60 mildly against

### W13.  `H20=H20a AND H60=H60a AND session_bucket=ny_close`
- Raw: n=105  W=95/L=10  WR=90.5%
- Refine: exclude ZS=ZS4 drops 6/10 losers (60%)
- **Final: n=72  W=68/L=4  WR=94.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=ny_close  •  AVOID when zscore +1 to +2 overbought

### W14.  `H20=H20a AND T1=T1c AND session_bucket=ny_close`
- Raw: n=105  W=95/L=10  WR=90.5%
- Refine: exclude ZS=ZS4 drops 6/10 losers (60%)
- **Final: n=72  W=68/L=4  WR=94.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; session=ny_close  •  AVOID when zscore +1 to +2 overbought

### W15.  `H20=H20a AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=105  W=95/L=10  WR=90.5%
- Refine: exclude ZS=ZS4 drops 6/10 losers (60%)
- **Final: n=72  W=68/L=4  WR=94.4%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; session=ny_close  •  AVOID when zscore +1 to +2 overbought

### W16.  `H20=H20a AND H60=H60a AND T1=T1c AND session_bucket=ny_close`
- Raw: n=105  W=95/L=10  WR=90.5%
- Refine: exclude ZS=ZS4 drops 6/10 losers (60%)
- **Final: n=72  W=68/L=4  WR=94.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade; session=ny_close  •  AVOID when zscore +1 to +2 overbought

### W17.  `H20=H20a AND H60=H60a AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=105  W=95/L=10  WR=90.5%
- Refine: exclude ZS=ZS4 drops 6/10 losers (60%)
- **Final: n=72  W=68/L=4  WR=94.4%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=ny_close  •  AVOID when zscore +1 to +2 overbought

### W18.  `H20=H20a AND T1=T1c AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=105  W=95/L=10  WR=90.5%
- Refine: exclude ZS=ZS4 drops 6/10 losers (60%)
- **Final: n=72  W=68/L=4  WR=94.4%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; session=ny_close  •  AVOID when zscore +1 to +2 overbought

### W19.  `BBP=BBP0 AND RSI=RSI3 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=99  W=87/L=12  WR=87.9%
- Refine: exclude session_bucket=asia drops 12/12 losers (100%)
- **Final: n=54  W=54/L=0  WR=100.0%**
- **Dir: LONG**  •  deep below lower band; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when session=asia

### W20.  `H60=H60a AND T4=T4c AND direction_exec=short AND session_bucket=asia`
- Raw: n=98  W=85/L=13  WR=86.7%
- Refine: exclude H20=H20a drops 13/13 losers (100%)
- **Final: n=57  W=57/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=asia  •  AVOID when HTF20 aligned WITH trade

### W21.  `H60=H60a AND T1=T1a AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=97  W=93/L=4  WR=95.9%
- Refine: exclude H20=H20a drops 4/4 losers (100%)
- **Final: n=55  W=55/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 30-40 weak; session=asia  •  AVOID when HTF20 aligned WITH trade

### W22.  `H60=H60a AND RSI=RSI2 AND direction_exec=short AND session_bucket=asia`
- Raw: n=97  W=93/L=4  WR=95.9%
- Refine: exclude H20=H20a drops 4/4 losers (100%)
- **Final: n=55  W=55/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; RSI 30-40 weak; session=asia  •  AVOID when HTF20 aligned WITH trade

### W23.  `T1=T1c AND BBP=BBP0 AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=97  W=85/L=12  WR=87.6%
- Refine: exclude session_bucket=asia drops 12/12 losers (100%)
- **Final: n=54  W=54/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; deep below lower band; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when session=asia

### W24.  `H20=H20a AND H60=H60a AND T4=T4a AND session_bucket=ny_close`
- Raw: n=93  W=84/L=9  WR=90.3%
- Refine: exclude BBP=BBP1 drops 3/9 losers (33%)
- **Final: n=90  W=84/L=6  WR=93.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade; session=ny_close  •  AVOID when just touched lower band

### W25.  `H20=H20a AND T1=T1c AND T4=T4a AND session_bucket=ny_close`
- Raw: n=93  W=84/L=9  WR=90.3%
- Refine: exclude BBP=BBP1 drops 3/9 losers (33%)
- **Final: n=90  W=84/L=6  WR=93.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; session=ny_close  •  AVOID when just touched lower band

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1c AND T4=T4a AND BBP=BBP2 AND RSI=RSI2`
- Raw: n=262  W=103/L=159  WR=39.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=262  W=103/L=159  WR=39.3%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; lower third; RSI 30-40 weak

### L02.  `T4=T4a AND BBP=BBP2 AND RSI=RSI2 AND direction_exec=long`
- Raw: n=262  W=103/L=159  WR=39.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=262  W=103/L=159  WR=39.3%**
- **Dir: LONG**  •  4h trend WITH trade; lower third; RSI 30-40 weak

### L03.  `T1=T1c AND RSI=RSI1 AND direction_exec=long`
- Raw: n=207  W=75/L=132  WR=36.2%
- Sharpen: sharpest is H20=H20d (60/132 of losers there)
- **Sharp: n=76  W=16/L=60  WR=21.1%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when HTF20 mildly against

### L04.  `H60=H60a AND T1=T1c AND RSI=RSI1`
- Raw: n=159  W=59/L=100  WR=37.1%
- Sharpen: sharpest is H20=H20d (30/100 of losers there)
- **Sharp: n=30  W=0/L=30  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when HTF20 mildly against

### L05.  `H60=H60a AND RSI=RSI1 AND direction_exec=long`
- Raw: n=159  W=59/L=100  WR=37.1%
- Sharpen: sharpest is H20=H20d (30/100 of losers there)
- **Sharp: n=30  W=0/L=30  WR=0.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 20-30 oversold  •  ONLY when HTF20 mildly against

### L06.  `H60=H60a AND T1=T1c AND RSI=RSI1 AND direction_exec=long`
- Raw: n=159  W=59/L=100  WR=37.1%
- Sharpen: sharpest is H20=H20d (30/100 of losers there)
- **Sharp: n=30  W=0/L=30  WR=0.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when HTF20 mildly against

### L07.  `T1=T1c AND T4=T4a AND BBP=BBP2 AND session_bucket=asia`
- Raw: n=153  W=53/L=100  WR=34.6%
- Sharpen: sharpest is RSI=RSI1 (22/100 of losers there)
- **Sharp: n=22  W=0/L=22  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; lower third; session=asia  •  ONLY when RSI 20-30 oversold

### L08.  `T4=T4a AND BBP=BBP2 AND direction_exec=long AND session_bucket=asia`
- Raw: n=153  W=53/L=100  WR=34.6%
- Sharpen: sharpest is RSI=RSI1 (22/100 of losers there)
- **Sharp: n=22  W=0/L=22  WR=0.0%**
- **Dir: LONG**  •  4h trend WITH trade; lower third; session=asia  •  ONLY when RSI 20-30 oversold

### L09.  `BBP=BBP1 AND direction_exec=long AND session_bucket=asia`
- Raw: n=151  W=56/L=95  WR=37.1%
- Sharpen: sharpest is RSI=RSI1 (20/95 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: LONG**  •  just touched lower band; session=asia  •  ONLY when RSI 20-30 oversold

### L10.  `BBP=BBP1 AND ZS=ZS1 AND direction_exec=long AND session_bucket=asia`
- Raw: n=151  W=56/L=95  WR=37.1%
- Sharpen: sharpest is RSI=RSI1 (20/95 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: LONG**  •  just touched lower band; zscore -3 to -2 deep oversold; session=asia  •  ONLY when RSI 20-30 oversold

### L11.  `T1=T1c AND BBP=BBP1 AND session_bucket=asia`
- Raw: n=148  W=56/L=92  WR=37.8%
- Sharpen: sharpest is RSI=RSI1 (20/92 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; just touched lower band; session=asia  •  ONLY when RSI 20-30 oversold

### L12.  `T1=T1c AND BBP=BBP1 AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=148  W=56/L=92  WR=37.8%
- Sharpen: sharpest is RSI=RSI1 (20/92 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; just touched lower band; zscore -3 to -2 deep oversold; session=asia  •  ONLY when RSI 20-30 oversold

### L13.  `T1=T1c AND BBP=BBP1 AND direction_exec=long AND session_bucket=asia`
- Raw: n=148  W=56/L=92  WR=37.8%
- Sharpen: sharpest is RSI=RSI1 (20/92 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; just touched lower band; session=asia  •  ONLY when RSI 20-30 oversold

### L14.  `T1=T1c AND T4=T4a AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=132  W=43/L=89  WR=32.6%
- Sharpen: sharpest is RSI=RSI1 (20/89 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; zscore -2 to -1 oversold; session=asia  •  ONLY when RSI 20-30 oversold

### L15.  `T4=T4a AND ZS=ZS2 AND direction_exec=long AND session_bucket=asia`
- Raw: n=132  W=43/L=89  WR=32.6%
- Sharpen: sharpest is RSI=RSI1 (20/89 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: LONG**  •  4h trend WITH trade; zscore -2 to -1 oversold; session=asia  •  ONLY when RSI 20-30 oversold

### L16.  `H60=H60e AND T1=T1c AND session_bucket=asia`
- Raw: n=130  W=35/L=95  WR=26.9%
- Sharpen: sharpest is H20=H20b (42/95 of losers there)
- **Sharp: n=42  W=0/L=42  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; session=asia  •  ONLY when HTF20 slightly aligned

### L17.  `H20=H20b AND H60=H60e AND RSI=RSI2`
- Raw: n=129  W=41/L=88  WR=31.8%
- Sharpen: sharpest is ZS=ZS1 (45/88 of losers there)
- **Sharp: n=45  W=0/L=45  WR=0.0%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 strongly against; RSI 30-40 weak  •  ONLY when zscore -3 to -2 deep oversold

### L18.  `H60=H60e AND T1=T1c AND RSI=RSI2`
- Raw: n=126  W=46/L=80  WR=36.5%
- Sharpen: sharpest is session_bucket=asia (64/80 of losers there)
- **Sharp: n=78  W=14/L=64  WR=17.9%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 30-40 weak  •  ONLY when session=asia

### L19.  `H60=H60e AND RSI=RSI2 AND direction_exec=long`
- Raw: n=126  W=46/L=80  WR=36.5%
- Sharpen: sharpest is session_bucket=asia (64/80 of losers there)
- **Sharp: n=78  W=14/L=64  WR=17.9%**
- **Dir: LONG**  •  HTF60 strongly against; RSI 30-40 weak  •  ONLY when session=asia

### L20.  `H60=H60e AND T1=T1c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=126  W=46/L=80  WR=36.5%
- Sharpen: sharpest is session_bucket=asia (64/80 of losers there)
- **Sharp: n=78  W=14/L=64  WR=17.9%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 30-40 weak  •  ONLY when session=asia

### L21.  `H20=H20c AND T1=T1c AND session_bucket=asia`
- Raw: n=122  W=46/L=76  WR=37.7%
- Sharpen: sharpest is H60=H60a (53/76 of losers there)
- **Sharp: n=64  W=11/L=53  WR=17.2%**
- **Dir: ?**  •  HTF20 neutral; 1h trend AGAINST trade; session=asia  •  ONLY when HTF60 aligned WITH trade

### L22.  `H20=H20c AND direction_exec=long AND session_bucket=asia`
- Raw: n=122  W=46/L=76  WR=37.7%
- Sharpen: sharpest is H60=H60a (53/76 of losers there)
- **Sharp: n=64  W=11/L=53  WR=17.2%**
- **Dir: LONG**  •  HTF20 neutral; session=asia  •  ONLY when HTF60 aligned WITH trade

### L23.  `H20=H20c AND T1=T1c AND direction_exec=long AND session_bucket=asia`
- Raw: n=122  W=46/L=76  WR=37.7%
- Sharpen: sharpest is H60=H60a (53/76 of losers there)
- **Sharp: n=64  W=11/L=53  WR=17.2%**
- **Dir: LONG**  •  HTF20 neutral; 1h trend AGAINST trade; session=asia  •  ONLY when HTF60 aligned WITH trade

### L24.  `H60=H60e AND direction_exec=long AND session_bucket=asia`
- Raw: n=121  W=36/L=85  WR=29.8%
- Sharpen: sharpest is H20=H20b (42/85 of losers there)
- **Sharp: n=42  W=0/L=42  WR=0.0%**
- **Dir: LONG**  •  HTF60 strongly against; session=asia  •  ONLY when HTF20 slightly aligned

### L25.  `H60=H60e AND T1=T1c AND direction_exec=long AND session_bucket=asia`
- Raw: n=118  W=34/L=84  WR=28.8%
- Sharpen: sharpest is H20=H20b (42/84 of losers there)
- **Sharp: n=42  W=0/L=42  WR=0.0%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend AGAINST trade; session=asia  •  ONLY when HTF20 slightly aligned

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | — |
| T1 | T1a(51/45) | T1c(48/54) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(51/45) | long(49/55) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
