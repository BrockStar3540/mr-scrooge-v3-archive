# USD_CAD — R26 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20d**  (EMA20 down 0.15-0.5x)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **2,445**  (W=1,497 / L=948)  -  WR: **61.2%**

## Session distribution

- ny_mid: n=1217  W=731/L=486  WR=60.1%
- ny_close: n=434  W=264/L=170  WR=60.8%
- ny_open: n=367  W=225/L=142  WR=61.3%
- asia: n=210  W=135/L=75  WR=64.3%
- london_open: n=137  W=90/L=47  WR=65.7%
- london: n=74  W=48/L=26  WR=64.9%
- off_hours: n=6  W=4/L=2  WR=66.7%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20e AND H60=H60e AND T1=T1a AND session_bucket=ny_mid`
- Raw: n=119  W=102/L=17  WR=85.7%
- Refine: exclude BBP=BBP3 drops 11/17 losers (65%)
- **Final: n=90  W=84/L=6  WR=93.3%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend WITH trade; session=ny_mid  •  AVOID when middle of band

### W02.  `H20=H20e AND T1=T1a AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=119  W=102/L=17  WR=85.7%
- Refine: exclude BBP=BBP3 drops 11/17 losers (65%)
- **Final: n=90  W=84/L=6  WR=93.3%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend WITH trade; session=ny_mid  •  AVOID when middle of band

### W03.  `H20=H20e AND T1=T1a AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=97  W=85/L=12  WR=87.6%
- Refine: exclude BBP=BBP3 drops 11/12 losers (92%)
- **Final: n=66  W=65/L=1  WR=98.5%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; session=ny_mid  •  AVOID when middle of band

### W04.  `H20=H20e AND T1=T1a AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=92  W=83/L=9  WR=90.2%
- Refine: exclude BBP=BBP3 drops 7/9 losers (78%)
- **Final: n=74  W=72/L=2  WR=97.3%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; RSI 50-60 upper neutral; session=ny_mid  •  AVOID when middle of band

### W05.  `H60=H60e AND T1=T1a AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=89  W=77/L=12  WR=86.5%
- Refine: exclude BBP=BBP3 drops 11/12 losers (92%)
- **Final: n=66  W=65/L=1  WR=98.5%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; session=ny_mid  •  AVOID when middle of band

### W06.  `T1=T1a AND T4=T4c AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=89  W=77/L=12  WR=86.5%
- Refine: exclude BBP=BBP3 drops 11/12 losers (92%)
- **Final: n=66  W=65/L=1  WR=98.5%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend AGAINST trade; session=ny_mid  •  AVOID when middle of band

### W07.  `H20=H20e AND H60=H60e AND T4=T4a`
- Raw: n=79  W=68/L=11  WR=86.1%
- Refine: exclude session_bucket=ny_close drops 5/11 losers (45%)
- **Final: n=61  W=55/L=6  WR=90.2%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend WITH trade  •  AVOID when session=ny_close

### W08.  `H20=H20e AND T4=T4a AND direction_exec=long`
- Raw: n=79  W=68/L=11  WR=86.1%
- Refine: exclude session_bucket=ny_close drops 5/11 losers (45%)
- **Final: n=61  W=55/L=6  WR=90.2%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend WITH trade  •  AVOID when session=ny_close

### W09.  `H20=H20e AND H60=H60e AND T4=T4a AND direction_exec=long`
- Raw: n=79  W=68/L=11  WR=86.1%
- Refine: exclude session_bucket=ny_close drops 5/11 losers (45%)
- **Final: n=61  W=55/L=6  WR=90.2%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 strongly against; 4h trend WITH trade  •  AVOID when session=ny_close

### W10.  `H20=H20b AND H60=H60e AND ZS=ZS2`
- Raw: n=76  W=66/L=10  WR=86.8%
- Refine: exclude session_bucket=ny_mid drops 10/10 losers (100%)
- **Final: n=20  W=20/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 strongly against; zscore -2 to -1 oversold  •  AVOID when session=ny_mid

### W11.  `H20=H20b AND H60=H60e AND T4=T4c AND ZS=ZS2`
- Raw: n=76  W=66/L=10  WR=86.8%
- Refine: exclude session_bucket=ny_mid drops 10/10 losers (100%)
- **Final: n=20  W=20/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 strongly against; 4h trend AGAINST trade; zscore -2 to -1 oversold  •  AVOID when session=ny_mid

### W12.  `H20=H20b AND H60=H60e AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=76  W=66/L=10  WR=86.8%
- Refine: exclude session_bucket=ny_mid drops 10/10 losers (100%)
- **Final: n=20  W=20/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 strongly against; lower third; zscore -2 to -1 oversold  •  AVOID when session=ny_mid

### W13.  `H20=H20b AND H60=H60e AND ZS=ZS2 AND direction_exec=long`
- Raw: n=76  W=66/L=10  WR=86.8%
- Refine: exclude session_bucket=ny_mid drops 10/10 losers (100%)
- **Final: n=20  W=20/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 slightly aligned; HTF60 strongly against; zscore -2 to -1 oversold  •  AVOID when session=ny_mid

### W14.  `H20=H20e AND BBP=BBP4 AND session_bucket=ny_mid`
- Raw: n=74  W=63/L=11  WR=85.1%
- Refine: exclude T4=T4a drops 7/11 losers (64%)
- **Final: n=62  W=58/L=4  WR=93.5%**
- **Dir: ?**  •  HTF20 strongly against; upper third; session=ny_mid  •  AVOID when 4h trend WITH trade

### W15.  `T4=T4c AND RSI=RSI2 AND session_bucket=ny_mid`
- Raw: n=65  W=61/L=4  WR=93.8%
- Refine: exclude BBP=BBP3 drops 3/4 losers (75%)
- **Final: n=51  W=50/L=1  WR=98.0%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 30-40 weak; session=ny_mid  •  AVOID when middle of band

### W16.  `H20=H20e AND H60=H60e AND BBP=BBP4 AND session_bucket=ny_mid`
- Raw: n=65  W=59/L=6  WR=90.8%
- Refine: exclude strategy_id=bravo_failed_momentum drops 2/6 losers (33%)
- **Final: n=61  W=57/L=4  WR=93.4%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; upper third; session=ny_mid  •  AVOID when strategy=bravo_failed_momentum

### W17.  `H20=H20e AND BBP=BBP4 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=65  W=59/L=6  WR=90.8%
- Refine: exclude strategy_id=bravo_failed_momentum drops 2/6 losers (33%)
- **Final: n=61  W=57/L=4  WR=93.4%**
- **Dir: LONG**  •  HTF20 strongly against; upper third; session=ny_mid  •  AVOID when strategy=bravo_failed_momentum

### W18.  `H20=H20d AND T1=T1a AND ZS=ZS5`
- Raw: n=65  W=58/L=7  WR=89.2%
- Refine: exclude H60=H60e drops 7/7 losers (100%)
- **Final: n=34  W=34/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when HTF60 strongly against

### W19.  `T1=T1c AND T4=T4a AND RSI=RSI3 AND ZS=ZS3`
- Raw: n=65  W=58/L=7  WR=89.2%
- Refine: exclude session_bucket=ny_mid drops 5/7 losers (71%)
- **Final: n=34  W=32/L=2  WR=94.1%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 40-50 lower neutral; zscore -1 to +1 neutral  •  AVOID when session=ny_mid

### W20.  `T1=T1a AND BBP=BBP4 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=65  W=57/L=8  WR=87.7%
- Refine: exclude T4=T4a drops 8/8 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend WITH trade; upper third; session=ny_mid  •  AVOID when 4h trend WITH trade

### W21.  `H20=H20e AND T4=T4c AND BBP=BBP4 AND session_bucket=ny_mid`
- Raw: n=62  W=58/L=4  WR=93.5%
- Refine: exclude T1=T1c drops 4/4 losers (100%)
- **Final: n=34  W=34/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; upper third; session=ny_mid  •  AVOID when 1h trend AGAINST trade

### W22.  `H20=H20e AND H60=H60e AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=61  W=55/L=6  WR=90.2%
- Refine: exclude BBP=BBP5 drops 3/6 losers (50%)
- **Final: n=56  W=53/L=3  WR=94.6%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend WITH trade; session=ny_mid  •  AVOID when just touched upper band

### W23.  `H20=H20e AND T4=T4a AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=61  W=55/L=6  WR=90.2%
- Refine: exclude BBP=BBP5 drops 3/6 losers (50%)
- **Final: n=56  W=53/L=3  WR=94.6%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend WITH trade; session=ny_mid  •  AVOID when just touched upper band

### W24.  `H60=H60e AND BBP=BBP4 AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=58  W=53/L=5  WR=91.4%
- Refine: exclude T1=T1c drops 3/5 losers (60%)
- **Final: n=53  W=51/L=2  WR=96.2%**
- **Dir: ?**  •  HTF60 strongly against; upper third; RSI 50-60 upper neutral; session=ny_mid  •  AVOID when 1h trend AGAINST trade

### W25.  `H20=H20d AND T1=T1a AND BBP=BBP6`
- Raw: n=57  W=50/L=7  WR=87.7%
- Refine: exclude H60=H60e drops 7/7 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend WITH trade; deep above upper band  •  AVOID when HTF60 strongly against

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1c AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=230  W=88/L=142  WR=38.3%
- Sharpen: sharpest is BBP=BBP6 (53/142 of losers there)
- **Sharp: n=66  W=13/L=53  WR=19.7%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; session=ny_mid  •  ONLY when deep above upper band

### L02.  `T1=T1c AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=200  W=75/L=125  WR=37.5%
- Sharpen: sharpest is BBP=BBP6 (42/125 of losers there)
- **Sharp: n=49  W=7/L=42  WR=14.3%**
- **Dir: SHORT**  •  1h trend AGAINST trade; session=ny_mid  •  ONLY when deep above upper band

### L03.  `T1=T1c AND RSI=RSI4 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=167  W=61/L=106  WR=36.5%
- Sharpen: sharpest is ZS=ZS5 (50/106 of losers there)
- **Sharp: n=61  W=11/L=50  WR=18.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; session=ny_mid  •  ONLY when zscore +2 to +3 deep overbought

### L04.  `H60=H60a AND T1=T1c AND session_bucket=ny_mid`
- Raw: n=166  W=57/L=109  WR=34.3%
- Sharpen: sharpest is BBP=BBP6 (42/109 of losers there)
- **Sharp: n=49  W=7/L=42  WR=14.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=ny_mid  •  ONLY when deep above upper band

### L05.  `H60=H60a AND T1=T1c AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=166  W=57/L=109  WR=34.3%
- Sharpen: sharpest is BBP=BBP6 (42/109 of losers there)
- **Sharp: n=49  W=7/L=42  WR=14.3%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=ny_mid  •  ONLY when deep above upper band

### L06.  `H60=H60a AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=157  W=56/L=101  WR=35.7%
- Sharpen: sharpest is ZS=ZS5 (59/101 of losers there)
- **Sharp: n=73  W=14/L=59  WR=19.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; session=ny_mid  •  ONLY when zscore +2 to +3 deep overbought

### L07.  `H60=H60a AND RSI=RSI4 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=157  W=56/L=101  WR=35.7%
- Sharpen: sharpest is ZS=ZS5 (59/101 of losers there)
- **Sharp: n=73  W=14/L=59  WR=19.2%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; session=ny_mid  •  ONLY when zscore +2 to +3 deep overbought

### L08.  `H60=H60a AND T1=T1c AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=133  W=43/L=90  WR=32.3%
- Sharpen: sharpest is BBP=BBP6 (42/90 of losers there)
- **Sharp: n=49  W=7/L=42  WR=14.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 50-60 upper neutral; session=ny_mid  •  ONLY when deep above upper band

### L09.  `H20=H20b AND T1=T1c AND RSI=RSI4`
- Raw: n=115  W=33/L=82  WR=28.7%
- Sharpen: sharpest is H60=H60a (39/82 of losers there)
- **Sharp: n=47  W=8/L=39  WR=17.0%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when HTF60 aligned WITH trade

### L10.  `T1=T1c AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=102  W=36/L=66  WR=35.3%
- Sharpen: sharpest is H20=H20b (36/66 of losers there)
- **Sharp: n=43  W=7/L=36  WR=16.3%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when HTF20 slightly aligned

### L11.  `H20=H20e AND T4=T4c AND RSI=RSI3`
- Raw: n=102  W=38/L=64  WR=37.3%
- Sharpen: sharpest is BBP=BBP3 (30/64 of losers there)
- **Sharp: n=40  W=10/L=30  WR=25.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when middle of band

### L12.  `H20=H20e AND H60=H60e AND T4=T4c AND RSI=RSI3`
- Raw: n=102  W=38/L=64  WR=37.3%
- Sharpen: sharpest is BBP=BBP3 (30/64 of losers there)
- **Sharp: n=40  W=10/L=30  WR=25.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when middle of band

### L13.  `H20=H20e AND T4=T4c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=102  W=38/L=64  WR=37.3%
- Sharpen: sharpest is BBP=BBP3 (30/64 of losers there)
- **Sharp: n=40  W=10/L=30  WR=25.0%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when middle of band

### L14.  `H60=H60a AND T4=T4c AND RSI=RSI4`
- Raw: n=96  W=38/L=58  WR=39.6%
- Sharpen: sharpest is H20=H20b (37/58 of losers there)
- **Sharp: n=45  W=8/L=37  WR=17.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when HTF20 slightly aligned

### L15.  `T1=T1c AND BBP=BBP6 AND RSI=RSI4`
- Raw: n=90  W=32/L=58  WR=35.6%
- Sharpen: sharpest is session_bucket=ny_mid (53/58 of losers there)
- **Sharp: n=66  W=13/L=53  WR=19.7%**
- **Dir: ?**  •  1h trend AGAINST trade; deep above upper band; RSI 50-60 upper neutral  •  ONLY when session=ny_mid

### L16.  `T1=T1c AND T4=T4a AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=90  W=33/L=57  WR=36.7%
- Sharpen: sharpest is session_bucket=ny_mid (30/57 of losers there)
- **Sharp: n=36  W=6/L=30  WR=16.7%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; upper third; RSI 50-60 upper neutral  •  ONLY when session=ny_mid

### L17.  `T1=T1c AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=90  W=35/L=55  WR=38.9%
- Sharpen: sharpest is session_bucket=ny_mid (50/55 of losers there)
- **Sharp: n=63  W=13/L=50  WR=20.6%**
- **Dir: ?**  •  1h trend AGAINST trade; deep above upper band; zscore +2 to +3 deep overbought  •  ONLY when session=ny_mid

### L18.  `H20=H20b AND H60=H60a AND direction_exec=short`
- Raw: n=89  W=28/L=61  WR=31.5%
- Sharpen: sharpest is T1=T1c (39/61 of losers there)
- **Sharp: n=47  W=8/L=39  WR=17.0%**
- **Dir: SHORT**  •  HTF20 slightly aligned; HTF60 aligned WITH trade  •  ONLY when 1h trend AGAINST trade

### L19.  `H60=H60a AND T1=T1c AND T4=T4c AND RSI=RSI4`
- Raw: n=88  W=34/L=54  WR=38.6%
- Sharpen: sharpest is H20=H20b (37/54 of losers there)
- **Sharp: n=45  W=8/L=37  WR=17.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when HTF20 slightly aligned

### L20.  `H60=H60a AND T4=T4c AND RSI=RSI4 AND direction_exec=short`
- Raw: n=88  W=34/L=54  WR=38.6%
- Sharpen: sharpest is H20=H20b (37/54 of losers there)
- **Sharp: n=45  W=8/L=37  WR=17.8%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when HTF20 slightly aligned

### L21.  `H60=H60a AND T4=T4c AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=88  W=34/L=54  WR=38.6%
- Sharpen: sharpest is H20=H20b (37/54 of losers there)
- **Sharp: n=45  W=8/L=37  WR=17.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral; session=ny_mid  •  ONLY when HTF20 slightly aligned

### L22.  `H60=H60a AND ZS=ZS5 AND session_bucket=ny_mid`
- Raw: n=87  W=28/L=59  WR=32.2%
- Sharpen: sharpest is RSI=RSI4 (59/59 of losers there)
- **Sharp: n=73  W=14/L=59  WR=19.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; zscore +2 to +3 deep overbought; session=ny_mid  •  ONLY when RSI 50-60 upper neutral

### L23.  `H60=H60a AND ZS=ZS5 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=87  W=28/L=59  WR=32.2%
- Sharpen: sharpest is RSI=RSI4 (59/59 of losers there)
- **Sharp: n=73  W=14/L=59  WR=19.2%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; zscore +2 to +3 deep overbought; session=ny_mid  •  ONLY when RSI 50-60 upper neutral

### L24.  `H20=H20a AND H60=H60a AND T1=T1c AND session_bucket=ny_mid`
- Raw: n=86  W=25/L=61  WR=29.1%
- Sharpen: sharpest is RSI=RSI4 (48/61 of losers there)
- **Sharp: n=59  W=11/L=48  WR=18.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade; session=ny_mid  •  ONLY when RSI 50-60 upper neutral

### L25.  `H20=H20a AND T1=T1c AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=86  W=25/L=61  WR=29.1%
- Sharpen: sharpest is RSI=RSI4 (48/61 of losers there)
- **Sharp: n=59  W=11/L=48  WR=18.6%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; session=ny_mid  •  ONLY when RSI 50-60 upper neutral

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | H60e(42/33) | H60a(35/44) |
| T1 | — | — |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(52/46) | short(48/54) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
