# USD_CHF — R22 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **3,455**  (W=2,235 / L=1,220)  -  WR: **64.7%**

## Session distribution

- london_open: n=971  W=628/L=343  WR=64.7%
- ny_mid: n=603  W=393/L=210  WR=65.2%
- ny_open: n=569  W=369/L=200  WR=64.9%
- asia: n=458  W=291/L=167  WR=63.5%
- london: n=381  W=253/L=128  WR=66.4%
- ny_close: n=323  W=207/L=116  WR=64.1%
- off_hours: n=85  W=50/L=35  WR=58.8%
- asia_late: n=65  W=44/L=21  WR=67.7%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `RSI=RSI4 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=291  W=252/L=39  WR=86.6%
- Refine: exclude BBP=BBP6 drops 18/39 losers (46%)
- **Final: n=204  W=183/L=21  WR=89.7%**
- **Dir: LONG**  •  RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when deep above upper band

### W02.  `BBP=BBP5 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=234  W=203/L=31  WR=86.8%
- Refine: exclude RSI=RSI3 drops 10/31 losers (32%)
- **Final: n=204  W=183/L=21  WR=89.7%**
- **Dir: LONG**  •  just touched upper band; zscore +2 to +3 deep overbought  •  AVOID when RSI 40-50 lower neutral

### W03.  `T1=T1a AND RSI=RSI4 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=221  W=195/L=26  WR=88.2%
- Refine: exclude strategy_id=BR5_opening_range_breakout_long drops 8/26 losers (31%)
- **Final: n=189  W=171/L=18  WR=90.5%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when strategy=BR5_opening_range_breakout_long

### W04.  `BBP=BBP5 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=204  W=183/L=21  WR=89.7%
- Refine: exclude session_bucket=london_open drops 14/21 losers (67%)
- **Final: n=109  W=102/L=7  WR=93.6%**
- **Dir: LONG**  •  just touched upper band; RSI 50-60 upper neutral  •  AVOID when session=london_open

### W05.  `BBP=BBP5 AND RSI=RSI4 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=204  W=183/L=21  WR=89.7%
- Refine: exclude session_bucket=london_open drops 14/21 losers (67%)
- **Final: n=109  W=102/L=7  WR=93.6%**
- **Dir: LONG**  •  just touched upper band; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when session=london_open

### W06.  `T4=T4a AND RSI=RSI4 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=167  W=143/L=24  WR=85.6%
- Refine: exclude H20=H20e drops 17/24 losers (71%)
- **Final: n=117  W=110/L=7  WR=94.0%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when HTF20 strongly against

### W07.  `H60=H60e AND T4=T4a AND session_bucket=ny_open`
- Raw: n=165  W=142/L=23  WR=86.1%
- Refine: exclude RSI=RSI3 drops 18/23 losers (78%)
- **Final: n=81  W=76/L=5  WR=93.8%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; session=ny_open  •  AVOID when RSI 40-50 lower neutral

### W08.  `T1=T1a AND RSI=RSI4 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=149  W=128/L=21  WR=85.9%
- Refine: exclude BBP=BBP4 drops 15/21 losers (71%)
- **Final: n=79  W=73/L=6  WR=92.4%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 50-60 upper neutral; session=ny_mid  •  AVOID when upper third

### W09.  `T1=T1a AND BBP=BBP5 AND direction_exec=long`
- Raw: n=148  W=131/L=17  WR=88.5%
- Refine: exclude RSI=RSI3 drops 4/17 losers (24%)
- **Final: n=144  W=131/L=13  WR=91.0%**
- **Dir: LONG**  •  1h trend WITH trade; just touched upper band  •  AVOID when RSI 40-50 lower neutral

### W10.  `T1=T1a AND BBP=BBP5 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=148  W=131/L=17  WR=88.5%
- Refine: exclude RSI=RSI3 drops 4/17 losers (24%)
- **Final: n=144  W=131/L=13  WR=91.0%**
- **Dir: LONG**  •  1h trend WITH trade; just touched upper band; zscore +2 to +3 deep overbought  •  AVOID when RSI 40-50 lower neutral

### W11.  `T1=T1a AND BBP=BBP5 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=144  W=131/L=13  WR=91.0%
- Refine: exclude H20=H20a drops 5/13 losers (38%)
- **Final: n=122  W=114/L=8  WR=93.4%**
- **Dir: LONG**  •  1h trend WITH trade; just touched upper band; RSI 50-60 upper neutral  •  AVOID when HTF20 aligned WITH trade

### W12.  `H60=H60a AND T1=T1a AND session_bucket=ny_mid`
- Raw: n=142  W=127/L=15  WR=89.4%
- Refine: exclude ZS=ZS2 drops 13/15 losers (87%)
- **Final: n=101  W=99/L=2  WR=98.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=ny_mid  •  AVOID when zscore -2 to -1 oversold

### W13.  `H60=H60e AND RSI=RSI4 AND session_bucket=ny_open`
- Raw: n=142  W=122/L=20  WR=85.9%
- Refine: exclude T4=T4c drops 15/20 losers (75%)
- **Final: n=81  W=76/L=5  WR=93.8%**
- **Dir: ?**  •  HTF60 strongly against; RSI 50-60 upper neutral; session=ny_open  •  AVOID when 4h trend AGAINST trade

### W14.  `T4=T4a AND BBP=BBP5 AND direction_exec=long`
- Raw: n=134  W=116/L=18  WR=86.6%
- Refine: exclude H20=H20e drops 12/18 losers (67%)
- **Final: n=84  W=78/L=6  WR=92.9%**
- **Dir: LONG**  •  4h trend WITH trade; just touched upper band  •  AVOID when HTF20 strongly against

### W15.  `T4=T4a AND BBP=BBP5 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=134  W=116/L=18  WR=86.6%
- Refine: exclude H20=H20e drops 12/18 losers (67%)
- **Final: n=84  W=78/L=6  WR=92.9%**
- **Dir: LONG**  •  4h trend WITH trade; just touched upper band; zscore +2 to +3 deep overbought  •  AVOID when HTF20 strongly against

### W16.  `T1=T1a AND T4=T4a AND ZS=ZS5 AND direction_exec=long`
- Raw: n=129  W=113/L=16  WR=87.6%
- Refine: exclude H20=H20e drops 15/16 losers (94%)
- **Final: n=81  W=80/L=1  WR=98.8%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when HTF20 strongly against

### W17.  `H60=H60a AND T1=T1a AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=125  W=119/L=6  WR=95.2%
- Refine: exclude ZS=ZS2 drops 4/6 losers (67%)
- **Final: n=101  W=99/L=2  WR=98.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade; session=ny_mid  •  AVOID when zscore -2 to -1 oversold

### W18.  `T4=T4c AND RSI=RSI4 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=124  W=109/L=15  WR=87.9%
- Refine: exclude H20=H20a drops 8/15 losers (53%)
- **Final: n=100  W=93/L=7  WR=93.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when HTF20 aligned WITH trade

### W19.  `RSI=RSI4 AND ZS=ZS5 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=124  W=106/L=18  WR=85.5%
- Refine: exclude H20=H20e drops 12/18 losers (67%)
- **Final: n=74  W=68/L=6  WR=91.9%**
- **Dir: LONG**  •  RSI 50-60 upper neutral; zscore +2 to +3 deep overbought; session=london_open  •  AVOID when HTF20 strongly against

### W20.  `H20=H20e AND BBP=BBP5 AND direction_exec=long`
- Raw: n=123  W=105/L=18  WR=85.4%
- Refine: exclude T4=T4a drops 12/18 losers (67%)
- **Final: n=73  W=67/L=6  WR=91.8%**
- **Dir: LONG**  •  HTF20 strongly against; just touched upper band  •  AVOID when 4h trend WITH trade

### W21.  `H20=H20e AND BBP=BBP5 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=123  W=105/L=18  WR=85.4%
- Refine: exclude T4=T4a drops 12/18 losers (67%)
- **Final: n=73  W=67/L=6  WR=91.8%**
- **Dir: LONG**  •  HTF20 strongly against; just touched upper band; zscore +2 to +3 deep overbought  •  AVOID when 4h trend WITH trade

### W22.  `H20=H20e AND RSI=RSI4 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=123  W=105/L=18  WR=85.4%
- Refine: exclude H60=H60d drops 7/18 losers (39%)
- **Final: n=107  W=96/L=11  WR=89.7%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 50-60 upper neutral; session=ny_mid  •  AVOID when HTF60 mildly against

### W23.  `T4=T4a AND direction_exec=long AND session_bucket=london`
- Raw: n=120  W=102/L=18  WR=85.0%
- Refine: exclude H60=H60e drops 10/18 losers (56%)
- **Final: n=93  W=85/L=8  WR=91.4%**
- **Dir: LONG**  •  4h trend WITH trade; session=london  •  AVOID when HTF60 strongly against

### W24.  `H20=H20a AND T4=T4a AND session_bucket=london`
- Raw: n=119  W=102/L=17  WR=85.7%
- Refine: exclude T1=T1c drops 17/17 losers (100%)
- **Final: n=39  W=39/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=london  •  AVOID when 1h trend AGAINST trade

### W25.  `T1=T1a AND BBP=BBP0 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=118  W=102/L=16  WR=86.4%
- Refine: exclude session_bucket=asia drops 8/16 losers (50%)
- **Final: n=106  W=98/L=8  WR=92.5%**
- **Dir: SHORT**  •  1h trend WITH trade; deep below lower band; RSI 40-50 lower neutral  •  AVOID when session=asia

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `BBP=BBP5 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=151  W=50/L=101  WR=33.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=151  W=50/L=101  WR=33.1%**
- **Dir: SHORT**  •  just touched upper band; zscore +2 to +3 deep overbought

### L02.  `BBP=BBP5 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=132  W=42/L=90  WR=31.8%
- Sharpen: sharpest is T4=T4a (47/90 of losers there)
- **Sharp: n=61  W=14/L=47  WR=23.0%**
- **Dir: SHORT**  •  just touched upper band; RSI 50-60 upper neutral  •  ONLY when 4h trend WITH trade

### L03.  `BBP=BBP5 AND RSI=RSI4 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=132  W=42/L=90  WR=31.8%
- Sharpen: sharpest is T4=T4a (47/90 of losers there)
- **Sharp: n=61  W=14/L=47  WR=23.0%**
- **Dir: SHORT**  •  just touched upper band; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when 4h trend WITH trade

### L04.  `RSI=RSI3 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=116  W=43/L=73  WR=37.1%
- Sharpen: sharpest is T4=T4a (40/73 of losers there)
- **Sharp: n=53  W=13/L=40  WR=24.5%**
- **Dir: LONG**  •  RSI 40-50 lower neutral; session=ny_mid  •  ONLY when 4h trend WITH trade

### L05.  `H60=H60e AND T1=T1c AND session_bucket=ny_mid`
- Raw: n=102  W=32/L=70  WR=31.4%
- Sharpen: sharpest is T4=T4a (67/70 of losers there)
- **Sharp: n=91  W=24/L=67  WR=26.4%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; session=ny_mid  •  ONLY when 4h trend WITH trade

### L06.  `ZS=ZS5 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=101  W=40/L=61  WR=39.6%
- Sharpen: sharpest is RSI=RSI4 (56/61 of losers there)
- **Sharp: n=81  W=25/L=56  WR=30.9%**
- **Dir: SHORT**  •  zscore +2 to +3 deep overbought; session=london_open  •  ONLY when RSI 50-60 upper neutral

### L07.  `H60=H60a AND T4=T4c AND session_bucket=ny_open`
- Raw: n=96  W=34/L=62  WR=35.4%
- Sharpen: sharpest is T1=T1c (39/62 of losers there)
- **Sharp: n=52  W=13/L=39  WR=25.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=ny_open  •  ONLY when 1h trend AGAINST trade

### L08.  `T1=T1c AND T4=T4c AND session_bucket=ny_open`
- Raw: n=96  W=38/L=58  WR=39.6%
- Sharpen: sharpest is H60=H60a (39/58 of losers there)
- **Sharp: n=52  W=13/L=39  WR=25.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_open  •  ONLY when HTF60 aligned WITH trade

### L09.  `T1=T1c AND BBP=BBP5 AND direction_exec=short`
- Raw: n=94  W=33/L=61  WR=35.1%
- Sharpen: sharpest is RSI=RSI4 (61/61 of losers there)
- **Sharp: n=88  W=27/L=61  WR=30.7%**
- **Dir: SHORT**  •  1h trend AGAINST trade; just touched upper band  •  ONLY when RSI 50-60 upper neutral

### L10.  `T1=T1c AND BBP=BBP5 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=94  W=33/L=61  WR=35.1%
- Sharpen: sharpest is RSI=RSI4 (61/61 of losers there)
- **Sharp: n=88  W=27/L=61  WR=30.7%**
- **Dir: SHORT**  •  1h trend AGAINST trade; just touched upper band; zscore +2 to +3 deep overbought  •  ONLY when RSI 50-60 upper neutral

### L11.  `H60=H60e AND T1=T1c AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=91  W=24/L=67  WR=26.4%
- Sharpen: sharpest is BBP=BBP0 (21/67 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade; session=ny_mid  •  ONLY when deep below lower band

### L12.  `T4=T4c AND BBP=BBP0 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=90  W=34/L=56  WR=37.8%
- Sharpen: sharpest is ZS=ZS0 (21/56 of losers there)
- **Sharp: n=25  W=4/L=21  WR=16.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; deep below lower band; RSI 40-50 lower neutral  •  ONLY when zscore <-3 extreme

### L13.  `T4=T4a AND RSI=RSI4 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=90  W=34/L=56  WR=37.8%
- Sharpen: sharpest is BBP=BBP5 (47/56 of losers there)
- **Sharp: n=61  W=14/L=47  WR=23.0%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when just touched upper band

### L14.  `T1=T1c AND BBP=BBP0 AND direction_exec=long`
- Raw: n=90  W=36/L=54  WR=40.0%
- Sharpen: sharpest is H60=H60e (30/54 of losers there)
- **Sharp: n=37  W=7/L=30  WR=18.9%**
- **Dir: LONG**  •  1h trend AGAINST trade; deep below lower band  •  ONLY when HTF60 strongly against

### L15.  `H60=H60b AND T4=T4a AND direction_exec=long`
- Raw: n=89  W=34/L=55  WR=38.2%
- Sharpen: sharpest is RSI=RSI3 (30/55 of losers there)
- **Sharp: n=35  W=5/L=30  WR=14.3%**
- **Dir: LONG**  •  HTF60 slightly aligned; 4h trend WITH trade  •  ONLY when RSI 40-50 lower neutral

### L16.  `T1=T1c AND BBP=BBP5 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=88  W=27/L=61  WR=30.7%
- Sharpen: sharpest is H20=H20a (38/61 of losers there)
- **Sharp: n=49  W=11/L=38  WR=22.4%**
- **Dir: SHORT**  •  1h trend AGAINST trade; just touched upper band; RSI 50-60 upper neutral  •  ONLY when HTF20 aligned WITH trade

### L17.  `H20=H20a AND H60=H60e AND session_bucket=ny_mid`
- Raw: n=88  W=28/L=60  WR=31.8%
- Sharpen: sharpest is T4=T4c (18/60 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; session=ny_mid  •  ONLY when 4h trend AGAINST trade

### L18.  `T1=T1c AND RSI=RSI3 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=87  W=28/L=59  WR=32.2%
- Sharpen: sharpest is T4=T4a (37/59 of losers there)
- **Sharp: n=49  W=12/L=37  WR=24.5%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 40-50 lower neutral; session=ny_mid  •  ONLY when 4h trend WITH trade

### L19.  `H20=H20e AND ZS=ZS4 AND session_bucket=london_open`
- Raw: n=86  W=34/L=52  WR=39.5%
- Sharpen: sharpest is H60=H60a (25/52 of losers there)
- **Sharp: n=33  W=8/L=25  WR=24.2%**
- **Dir: ?**  •  HTF20 strongly against; zscore +1 to +2 overbought; session=london_open  •  ONLY when HTF60 aligned WITH trade

### L20.  `H20=H20e AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=london_open`
- Raw: n=86  W=34/L=52  WR=39.5%
- Sharpen: sharpest is H60=H60a (25/52 of losers there)
- **Sharp: n=33  W=8/L=25  WR=24.2%**
- **Dir: ?**  •  HTF20 strongly against; upper third; zscore +1 to +2 overbought; session=london_open  •  ONLY when HTF60 aligned WITH trade

### L21.  `T1=T1c AND T4=T4c AND ZS=ZS5 AND direction_exec=short`
- Raw: n=86  W=34/L=52  WR=39.5%
- Sharpen: sharpest is session_bucket=london_open (24/52 of losers there)
- **Sharp: n=29  W=5/L=24  WR=17.2%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when session=london_open

### L22.  `T1=T1a AND RSI=RSI4 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=85  W=33/L=52  WR=38.8%
- Sharpen: sharpest is T4=T4a (29/52 of losers there)
- **Sharp: n=35  W=6/L=29  WR=17.1%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 50-60 upper neutral; session=london_open  •  ONLY when 4h trend WITH trade

### L23.  `H60=H60e AND T1=T1c AND T4=T4c AND RSI=RSI3`
- Raw: n=85  W=34/L=51  WR=40.0%
- Sharpen: sharpest is session_bucket=asia (15/51 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when session=asia

### L24.  `T4=T4c AND BBP=BBP5 AND direction_exec=short`
- Raw: n=83  W=30/L=53  WR=36.1%
- Sharpen: sharpest is session_bucket=ny_mid (12/53 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; just touched upper band  •  ONLY when session=ny_mid

### L25.  `T4=T4c AND BBP=BBP5 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=83  W=30/L=53  WR=36.1%
- Sharpen: sharpest is session_bucket=ny_mid (12/53 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; just touched upper band; zscore +2 to +3 deep overbought  •  ONLY when session=ny_mid

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | — |
| T1 | T1a(54/47) | T1c(46/53) |
| T4 | T4a(52/47) | T4c(48/53) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(54/47) | short(46/53) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
