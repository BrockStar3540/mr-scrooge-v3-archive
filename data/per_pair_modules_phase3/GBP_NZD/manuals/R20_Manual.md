# GBP_NZD — R20 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_3**  (5m ATR >120%)
- **A1 = A1_2**  (1h ATR 4-8x)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR3**  (60-90%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **4,863**  (W=2,714 / L=2,149)  -  WR: **55.8%**

## Session distribution

- ny_mid: n=1287  W=697/L=590  WR=54.2%
- asia: n=1126  W=633/L=493  WR=56.2%
- london_open: n=875  W=497/L=378  WR=56.8%
- ny_close: n=638  W=373/L=265  WR=58.5%
- london: n=348  W=201/L=147  WR=57.8%
- ny_open: n=284  W=166/L=118  WR=58.5%
- asia_late: n=187  W=96/L=91  WR=51.3%
- off_hours: n=118  W=51/L=67  WR=43.2%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60a AND T1=T1c AND BBP=BBP1`
- Raw: n=95  W=81/L=14  WR=85.3%
- Refine: exclude H20=H20a drops 13/14 losers (93%)
- **Final: n=61  W=60/L=1  WR=98.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; just touched lower band  •  AVOID when HTF20 aligned WITH trade

### W02.  `H60=H60a AND T1=T1c AND T4=T4a AND BBP=BBP1`
- Raw: n=95  W=81/L=14  WR=85.3%
- Refine: exclude H20=H20a drops 13/14 losers (93%)
- **Final: n=61  W=60/L=1  WR=98.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; just touched lower band  •  AVOID when HTF20 aligned WITH trade

### W03.  `H60=H60a AND T1=T1c AND BBP=BBP1 AND ZS=ZS1`
- Raw: n=95  W=81/L=14  WR=85.3%
- Refine: exclude H20=H20a drops 13/14 losers (93%)
- **Final: n=61  W=60/L=1  WR=98.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; just touched lower band; zscore -3 to -2 deep oversold  •  AVOID when HTF20 aligned WITH trade

### W04.  `H20=H20e AND T1=T1c AND direction_exec=short`
- Raw: n=94  W=81/L=13  WR=86.2%
- Refine: exclude RSI=RSI3 drops 13/13 losers (100%)
- **Final: n=53  W=53/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade  •  AVOID when RSI 40-50 lower neutral

### W05.  `H20=H20e AND H60=H60a AND T1=T1c AND direction_exec=short`
- Raw: n=94  W=81/L=13  WR=86.2%
- Refine: exclude RSI=RSI3 drops 13/13 losers (100%)
- **Final: n=53  W=53/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend AGAINST trade  •  AVOID when RSI 40-50 lower neutral

### W06.  `H60=H60a AND T1=T1c AND RSI=RSI2`
- Raw: n=88  W=77/L=11  WR=87.5%
- Refine: exclude direction_exec=long drops 11/11 losers (100%)
- **Final: n=53  W=53/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 30-40 weak  •  AVOID when long

### W07.  `T1=T1a AND BBP=BBP4 AND direction_exec=long`
- Raw: n=81  W=69/L=12  WR=85.2%
- Refine: exclude ZS=ZS3 drops 8/12 losers (67%)
- **Final: n=59  W=55/L=4  WR=93.2%**
- **Dir: LONG**  •  1h trend WITH trade; upper third  •  AVOID when zscore -1 to +1 neutral

### W08.  `T1=T1a AND T4=T4c AND BBP=BBP4 AND direction_exec=long`
- Raw: n=77  W=66/L=11  WR=85.7%
- Refine: exclude ZS=ZS3 drops 8/11 losers (73%)
- **Final: n=56  W=53/L=3  WR=94.6%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend AGAINST trade; upper third  •  AVOID when zscore -1 to +1 neutral

### W09.  `H20=H20e AND T1=T1a AND BBP=BBP4 AND direction_exec=long`
- Raw: n=74  W=66/L=8  WR=89.2%
- Refine: exclude session_bucket=ny_mid drops 6/8 losers (75%)
- **Final: n=51  W=49/L=2  WR=96.1%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend WITH trade; upper third  •  AVOID when session=ny_mid

### W10.  `H20=H20a AND RSI=RSI3 AND session_bucket=ny_open`
- Raw: n=70  W=63/L=7  WR=90.0%
- Refine: exclude H60=H60c drops 5/7 losers (71%)
- **Final: n=59  W=57/L=2  WR=96.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 40-50 lower neutral; session=ny_open  •  AVOID when HTF60 neutral

### W11.  `H20=H20a AND RSI=RSI3 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=70  W=63/L=7  WR=90.0%
- Refine: exclude H60=H60c drops 5/7 losers (71%)
- **Final: n=59  W=57/L=2  WR=96.6%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 40-50 lower neutral; session=ny_open  •  AVOID when HTF60 neutral

### W12.  `H20=H20e AND RSI=RSI2 AND direction_exec=short`
- Raw: n=69  W=63/L=6  WR=91.3%
- Refine: exclude T1=T1a drops 6/6 losers (100%)
- **Final: n=53  W=53/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 30-40 weak  •  AVOID when 1h trend WITH trade

### W13.  `H20=H20e AND H60=H60e AND T1=T1a AND BBP=BBP4`
- Raw: n=68  W=60/L=8  WR=88.2%
- Refine: exclude ZS=ZS3 drops 5/8 losers (62%)
- **Final: n=56  W=53/L=3  WR=94.6%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend WITH trade; upper third  •  AVOID when zscore -1 to +1 neutral

### W14.  `H60=H60a AND T4=T4a AND BBP=BBP2 AND RSI=RSI2`
- Raw: n=67  W=60/L=7  WR=89.6%
- Refine: exclude strategy_id=bravo_failed_momentum drops 2/7 losers (29%)
- **Final: n=65  W=60/L=5  WR=92.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; lower third; RSI 30-40 weak  •  AVOID when strategy=bravo_failed_momentum

### W15.  `H20=H20e AND T1=T1c AND T4=T4a AND direction_exec=short`
- Raw: n=64  W=58/L=6  WR=90.6%
- Refine: exclude ZS=ZS2 drops 5/6 losers (83%)
- **Final: n=43  W=42/L=1  WR=97.7%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend WITH trade  •  AVOID when zscore -2 to -1 oversold

### W16.  `T1=T1a AND BBP=BBP4 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=62  W=56/L=6  WR=90.3%
- Refine: exclude session_bucket=ny_mid drops 6/6 losers (100%)
- **Final: n=39  W=39/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend WITH trade; upper third; RSI 50-60 upper neutral  •  AVOID when session=ny_mid

### W17.  `H20=H20e AND RSI=RSI2 AND session_bucket=ny_close`
- Raw: n=61  W=52/L=9  WR=85.2%
- Refine: exclude ZS=ZS2 drops 7/9 losers (78%)
- **Final: n=42  W=40/L=2  WR=95.2%**
- **Dir: ?**  •  HTF20 strongly against; RSI 30-40 weak; session=ny_close  •  AVOID when zscore -2 to -1 oversold

### W18.  `T1=T1a AND T4=T4c AND ZS=ZS1 AND session_bucket=london_open`
- Raw: n=60  W=58/L=2  WR=96.7%
- Refine: exclude H60=H60a drops 2/2 losers (100%)
- **Final: n=38  W=38/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold; session=london_open  •  AVOID when HTF60 aligned WITH trade

### W19.  `H20=H20e AND H60=H60a AND RSI=RSI2`
- Raw: n=60  W=57/L=3  WR=95.0%
- Refine: exclude ZS=ZS4 drops 2/3 losers (67%)
- **Final: n=58  W=57/L=1  WR=98.3%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; RSI 30-40 weak  •  AVOID when zscore +1 to +2 overbought

### W20.  `H20=H20e AND T1=T1a AND T4=T4c AND ZS=ZS4`
- Raw: n=60  W=54/L=6  WR=90.0%
- Refine: exclude session_bucket=london_open drops 5/6 losers (83%)
- **Final: n=54  W=53/L=1  WR=98.1%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  AVOID when session=london_open

### W21.  `H20=H20e AND T1=T1c AND RSI=RSI2 AND session_bucket=ny_close`
- Raw: n=60  W=52/L=8  WR=86.7%
- Refine: exclude direction_exec=long drops 8/8 losers (100%)
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 30-40 weak; session=ny_close  •  AVOID when long

### W22.  `T1=T1a AND ZS=ZS4 AND direction_exec=long`
- Raw: n=59  W=55/L=4  WR=93.2%
- Refine: exclude RSI=RSI3 drops 3/4 losers (75%)
- **Final: n=44  W=43/L=1  WR=97.7%**
- **Dir: LONG**  •  1h trend WITH trade; zscore +1 to +2 overbought  •  AVOID when RSI 40-50 lower neutral

### W23.  `H60=H60e AND T1=T1a AND ZS=ZS4 AND direction_exec=long`
- Raw: n=59  W=55/L=4  WR=93.2%
- Refine: exclude RSI=RSI3 drops 3/4 losers (75%)
- **Final: n=44  W=43/L=1  WR=97.7%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend WITH trade; zscore +1 to +2 overbought  •  AVOID when RSI 40-50 lower neutral

### W24.  `T1=T1a AND BBP=BBP4 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=59  W=55/L=4  WR=93.2%
- Refine: exclude RSI=RSI3 drops 3/4 losers (75%)
- **Final: n=44  W=43/L=1  WR=97.7%**
- **Dir: LONG**  •  1h trend WITH trade; upper third; zscore +1 to +2 overbought  •  AVOID when RSI 40-50 lower neutral

### W25.  `H60=H60a AND T4=T4a AND BBP=BBP1 AND RSI=RSI2`
- Raw: n=58  W=58/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=58  W=58/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; just touched lower band; RSI 30-40 weak

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20a AND RSI=RSI4 AND direction_exec=short`
- Raw: n=369  W=144/L=225  WR=39.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=369  W=144/L=225  WR=39.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 50-60 upper neutral

### L02.  `H60=H60a AND RSI=RSI4 AND direction_exec=short`
- Raw: n=334  W=128/L=206  WR=38.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=334  W=128/L=206  WR=38.3%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral

### L03.  `H60=H60a AND T4=T4a AND RSI=RSI4 AND direction_exec=short`
- Raw: n=334  W=128/L=206  WR=38.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=334  W=128/L=206  WR=38.3%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral

### L04.  `H60=H60e AND RSI=RSI2 AND direction_exec=long`
- Raw: n=278  W=87/L=191  WR=31.3%
- Sharpen: sharpest is T4=T4c (114/191 of losers there)
- **Sharp: n=141  W=27/L=114  WR=19.1%**
- **Dir: LONG**  •  HTF60 strongly against; RSI 30-40 weak  •  ONLY when 4h trend AGAINST trade

### L05.  `H20=H20e AND T1=T1c AND direction_exec=long AND session_bucket=london_open`
- Raw: n=264  W=99/L=165  WR=37.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=264  W=99/L=165  WR=37.5%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade; session=london_open

### L06.  `H60=H60e AND T1=T1c AND RSI=RSI2`
- Raw: n=237  W=87/L=150  WR=36.7%
- Sharpen: sharpest is T4=T4c (93/150 of losers there)
- **Sharp: n=120  W=27/L=93  WR=22.5%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 30-40 weak  •  ONLY when 4h trend AGAINST trade

### L07.  `H60=H60e AND T1=T1c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=237  W=87/L=150  WR=36.7%
- Sharpen: sharpest is T4=T4c (93/150 of losers there)
- **Sharp: n=120  W=27/L=93  WR=22.5%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 30-40 weak  •  ONLY when 4h trend AGAINST trade

### L08.  `H20=H20a AND H60=H60a AND T1=T1c`
- Raw: n=235  W=94/L=141  WR=40.0%
- Sharpen: sharpest is ZS=ZS4 (52/141 of losers there)
- **Sharp: n=54  W=2/L=52  WR=3.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade  •  ONLY when zscore +1 to +2 overbought

### L09.  `H20=H20a AND H60=H60a AND T1=T1c AND T4=T4a`
- Raw: n=235  W=94/L=141  WR=40.0%
- Sharpen: sharpest is ZS=ZS4 (52/141 of losers there)
- **Sharp: n=54  W=2/L=52  WR=3.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when zscore +1 to +2 overbought

### L10.  `H20=H20a AND H60=H60a AND T1=T1c AND direction_exec=short`
- Raw: n=235  W=94/L=141  WR=40.0%
- Sharpen: sharpest is ZS=ZS4 (52/141 of losers there)
- **Sharp: n=54  W=2/L=52  WR=3.7%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade  •  ONLY when zscore +1 to +2 overbought

### L11.  `H20=H20e AND H60=H60e AND RSI=RSI2`
- Raw: n=232  W=86/L=146  WR=37.1%
- Sharpen: sharpest is T4=T4c (93/146 of losers there)
- **Sharp: n=120  W=27/L=93  WR=22.5%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 30-40 weak  •  ONLY when 4h trend AGAINST trade

### L12.  `H20=H20e AND H60=H60e AND T1=T1c AND RSI=RSI2`
- Raw: n=232  W=86/L=146  WR=37.1%
- Sharpen: sharpest is T4=T4c (93/146 of losers there)
- **Sharp: n=120  W=27/L=93  WR=22.5%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; RSI 30-40 weak  •  ONLY when 4h trend AGAINST trade

### L13.  `H20=H20e AND H60=H60e AND RSI=RSI2 AND direction_exec=long`
- Raw: n=232  W=86/L=146  WR=37.1%
- Sharpen: sharpest is T4=T4c (93/146 of losers there)
- **Sharp: n=120  W=27/L=93  WR=22.5%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 strongly against; RSI 30-40 weak  •  ONLY when 4h trend AGAINST trade

### L14.  `H20=H20e AND H60=H60e AND T1=T1c AND session_bucket=london_open`
- Raw: n=211  W=80/L=131  WR=37.9%
- Sharpen: sharpest is ZS=ZS1 (41/131 of losers there)
- **Sharp: n=54  W=13/L=41  WR=24.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; session=london_open  •  ONLY when zscore -3 to -2 deep oversold

### L15.  `H20=H20e AND T1=T1c AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=192  W=73/L=119  WR=38.0%
- Sharpen: sharpest is RSI=RSI2 (35/119 of losers there)
- **Sharp: n=40  W=5/L=35  WR=12.5%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_mid  •  ONLY when RSI 30-40 weak

### L16.  `H60=H60e AND T1=T1a AND BBP=BBP2`
- Raw: n=190  W=72/L=118  WR=37.9%
- Sharpen: sharpest is RSI=RSI2 (44/118 of losers there)
- **Sharp: n=46  W=2/L=44  WR=4.3%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; lower third  •  ONLY when RSI 30-40 weak

### L17.  `T4=T4c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=175  W=54/L=121  WR=30.9%
- Sharpen: sharpest is H60=H60e (114/121 of losers there)
- **Sharp: n=141  W=27/L=114  WR=19.1%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when HTF60 strongly against

### L18.  `H60=H60e AND T4=T4c AND RSI=RSI2`
- Raw: n=174  W=45/L=129  WR=25.9%
- Sharpen: sharpest is direction_exec=long (114/129 of losers there)
- **Sharp: n=141  W=27/L=114  WR=19.1%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when long

### L19.  `T4=T4a AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=173  W=64/L=109  WR=37.0%
- Sharpen: sharpest is direction_exec=short (109/109 of losers there)
- **Sharp: n=159  W=50/L=109  WR=31.4%**
- **Dir: ?**  •  4h trend WITH trade; upper third; RSI 50-60 upper neutral  •  ONLY when short

### L20.  `BBP=BBP2 AND RSI=RSI2 AND direction_exec=long`
- Raw: n=172  W=64/L=108  WR=37.2%
- Sharpen: sharpest is H60=H60e (82/108 of losers there)
- **Sharp: n=110  W=28/L=82  WR=25.5%**
- **Dir: LONG**  •  lower third; RSI 30-40 weak  •  ONLY when HTF60 strongly against

### L21.  `BBP=BBP4 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=170  W=50/L=120  WR=29.4%
- Sharpen: sharpest is T1=T1c (47/120 of losers there)
- **Sharp: n=52  W=5/L=47  WR=9.6%**
- **Dir: SHORT**  •  upper third; RSI 50-60 upper neutral  •  ONLY when 1h trend AGAINST trade

### L22.  `H60=H60a AND T4=T4a AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=170  W=64/L=106  WR=37.6%
- Sharpen: sharpest is direction_exec=short (106/106 of losers there)
- **Sharp: n=156  W=50/L=106  WR=32.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; upper third; RSI 50-60 upper neutral  •  ONLY when short

### L23.  `T4=T4a AND BBP=BBP4 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=159  W=50/L=109  WR=31.4%
- Sharpen: sharpest is T1=T1c (47/109 of losers there)
- **Sharp: n=52  W=5/L=47  WR=9.6%**
- **Dir: SHORT**  •  4h trend WITH trade; upper third; RSI 50-60 upper neutral  •  ONLY when 1h trend AGAINST trade

### L24.  `T4=T4a AND BBP=BBP0 AND RSI=RSI3`
- Raw: n=158  W=62/L=96  WR=39.2%
- Sharpen: sharpest is H20=H20d (24/96 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: ?**  •  4h trend WITH trade; deep below lower band; RSI 40-50 lower neutral  •  ONLY when HTF20 mildly against

### L25.  `RSI=RSI2 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=157  W=55/L=102  WR=35.0%
- Sharpen: sharpest is H60=H60e (77/102 of losers there)
- **Sharp: n=104  W=27/L=77  WR=26.0%**
- **Dir: LONG**  •  RSI 30-40 weak; zscore -2 to -1 oversold  •  ONLY when HTF60 strongly against

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | — |
| T1 | — | — |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
