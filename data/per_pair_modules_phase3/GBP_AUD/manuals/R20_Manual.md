# GBP_AUD — R20 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_3**  (5m ATR >120%)
- **A1 = A1_2**  (1h ATR 4-8x)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50e**  (EMA50 down >0.5x)
- **ADR = ADR3**  (60-90%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **3,823**  (W=2,154 / L=1,669)  -  WR: **56.3%**

## Session distribution

- asia: n=1086  W=648/L=438  WR=59.7%
- ny_mid: n=892  W=460/L=432  WR=51.6%
- ny_open: n=481  W=278/L=203  WR=57.8%
- ny_close: n=461  W=260/L=201  WR=56.4%
- london_open: n=428  W=230/L=198  WR=53.7%
- london: n=251  W=151/L=100  WR=60.2%
- off_hours: n=118  W=72/L=46  WR=61.0%
- asia_late: n=106  W=55/L=51  WR=51.9%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20e AND H60=H60e AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=61  W=54/L=7  WR=88.5%
- Refine: exclude BBP=BBP5 drops 4/7 losers (57%)
- **Final: n=54  W=51/L=3  WR=94.4%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 40-50 lower neutral; session=asia  •  AVOID when just touched upper band

### W02.  `H20=H20e AND RSI=RSI3 AND direction_exec=long AND session_bucket=asia`
- Raw: n=61  W=54/L=7  WR=88.5%
- Refine: exclude BBP=BBP5 drops 4/7 losers (57%)
- **Final: n=54  W=51/L=3  WR=94.4%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 40-50 lower neutral; session=asia  •  AVOID when just touched upper band

### W03.  `H20=H20a AND RSI=RSI2 AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=60  W=51/L=9  WR=85.0%
- Refine: exclude H60=H60e drops 7/9 losers (78%)
- **Final: n=38  W=36/L=2  WR=94.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 30-40 weak; zscore -2 to -1 oversold; session=asia  •  AVOID when HTF60 strongly against

### W04.  `H20=H20e AND H60=H60e AND BBP=BBP1 AND session_bucket=ny_mid`
- Raw: n=57  W=50/L=7  WR=87.7%
- Refine: exclude RSI=RSI1 drops 7/7 losers (100%)
- **Final: n=27  W=27/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; just touched lower band; session=ny_mid  •  AVOID when RSI 20-30 oversold

### W05.  `H20=H20e AND T1=T1c AND BBP=BBP1 AND session_bucket=ny_mid`
- Raw: n=57  W=50/L=7  WR=87.7%
- Refine: exclude RSI=RSI1 drops 7/7 losers (100%)
- **Final: n=27  W=27/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; just touched lower band; session=ny_mid  •  AVOID when RSI 20-30 oversold

### W06.  `H20=H20e AND T4=T4c AND BBP=BBP1 AND session_bucket=ny_mid`
- Raw: n=57  W=50/L=7  WR=87.7%
- Refine: exclude RSI=RSI1 drops 7/7 losers (100%)
- **Final: n=27  W=27/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; just touched lower band; session=ny_mid  •  AVOID when RSI 20-30 oversold

### W07.  `H20=H20e AND BBP=BBP1 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=57  W=50/L=7  WR=87.7%
- Refine: exclude RSI=RSI1 drops 7/7 losers (100%)
- **Final: n=27  W=27/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 strongly against; just touched lower band; session=ny_mid  •  AVOID when RSI 20-30 oversold

### W08.  `H60=H60e AND BBP=BBP4 AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=57  W=49/L=8  WR=86.0%
- Refine: exclude strategy_id=bravo_expansion_continuation drops 2/8 losers (25%)
- **Final: n=53  W=47/L=6  WR=88.7%**
- **Dir: ?**  •  HTF60 strongly against; upper third; RSI 40-50 lower neutral; session=asia  •  AVOID when strategy=bravo_expansion_continuation

### W09.  `T1=T1c AND BBP=BBP4 AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=57  W=49/L=8  WR=86.0%
- Refine: exclude strategy_id=bravo_expansion_continuation drops 2/8 losers (25%)
- **Final: n=53  W=47/L=6  WR=88.7%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; RSI 40-50 lower neutral; session=asia  •  AVOID when strategy=bravo_expansion_continuation

### W10.  `T4=T4c AND BBP=BBP4 AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=57  W=49/L=8  WR=86.0%
- Refine: exclude strategy_id=bravo_expansion_continuation drops 2/8 losers (25%)
- **Final: n=53  W=47/L=6  WR=88.7%**
- **Dir: ?**  •  4h trend AGAINST trade; upper third; RSI 40-50 lower neutral; session=asia  •  AVOID when strategy=bravo_expansion_continuation

### W11.  `BBP=BBP4 AND RSI=RSI3 AND direction_exec=long AND session_bucket=asia`
- Raw: n=57  W=49/L=8  WR=86.0%
- Refine: exclude strategy_id=bravo_expansion_continuation drops 2/8 losers (25%)
- **Final: n=53  W=47/L=6  WR=88.7%**
- **Dir: LONG**  •  upper third; RSI 40-50 lower neutral; session=asia  •  AVOID when strategy=bravo_expansion_continuation

### W12.  `H20=H20e AND T1=T1a AND T4=T4a AND BBP=BBP3`
- Raw: n=55  W=47/L=8  WR=85.5%
- Refine: exclude strategy_id=bravo_expansion_continuation drops 3/8 losers (38%)
- **Final: n=51  W=46/L=5  WR=90.2%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend WITH trade; middle of band  •  AVOID when strategy=bravo_expansion_continuation

### W13.  `H60=H60e AND RSI=RSI3 AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=52  W=46/L=6  WR=88.5%
- Refine: exclude strategy_id=bravo_expansion_continuation drops 2/6 losers (33%)
- **Final: n=48  W=44/L=4  WR=91.7%**
- **Dir: ?**  •  HTF60 strongly against; RSI 40-50 lower neutral; zscore +1 to +2 overbought; session=asia  •  AVOID when strategy=bravo_expansion_continuation

### W14.  `T1=T1c AND RSI=RSI3 AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=52  W=46/L=6  WR=88.5%
- Refine: exclude strategy_id=bravo_expansion_continuation drops 2/6 losers (33%)
- **Final: n=48  W=44/L=4  WR=91.7%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 40-50 lower neutral; zscore +1 to +2 overbought; session=asia  •  AVOID when strategy=bravo_expansion_continuation

### W15.  `T4=T4c AND RSI=RSI3 AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=52  W=46/L=6  WR=88.5%
- Refine: exclude strategy_id=bravo_expansion_continuation drops 2/6 losers (33%)
- **Final: n=48  W=44/L=4  WR=91.7%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; zscore +1 to +2 overbought; session=asia  •  AVOID when strategy=bravo_expansion_continuation

### W16.  `RSI=RSI3 AND ZS=ZS4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=52  W=46/L=6  WR=88.5%
- Refine: exclude strategy_id=bravo_expansion_continuation drops 2/6 losers (33%)
- **Final: n=48  W=44/L=4  WR=91.7%**
- **Dir: LONG**  •  RSI 40-50 lower neutral; zscore +1 to +2 overbought; session=asia  •  AVOID when strategy=bravo_expansion_continuation

### W17.  `H60=H60a AND T4=T4a AND BBP=BBP6`
- Raw: n=48  W=41/L=7  WR=85.4%
- Refine: exclude RSI=RSI3 drops 7/7 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; deep above upper band  •  AVOID when RSI 40-50 lower neutral

### W18.  `T1=T1a AND T4=T4a AND BBP=BBP6`
- Raw: n=48  W=41/L=7  WR=85.4%
- Refine: exclude RSI=RSI3 drops 7/7 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; deep above upper band  •  AVOID when RSI 40-50 lower neutral

### W19.  `T4=T4a AND BBP=BBP6 AND direction_exec=short`
- Raw: n=48  W=41/L=7  WR=85.4%
- Refine: exclude RSI=RSI3 drops 7/7 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: SHORT**  •  4h trend WITH trade; deep above upper band  •  AVOID when RSI 40-50 lower neutral

### W20.  `H60=H60a AND T1=T1a AND T4=T4a AND BBP=BBP6`
- Raw: n=48  W=41/L=7  WR=85.4%
- Refine: exclude RSI=RSI3 drops 7/7 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; deep above upper band  •  AVOID when RSI 40-50 lower neutral

### W21.  `H60=H60a AND T4=T4a AND BBP=BBP6 AND direction_exec=short`
- Raw: n=48  W=41/L=7  WR=85.4%
- Refine: exclude RSI=RSI3 drops 7/7 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend WITH trade; deep above upper band  •  AVOID when RSI 40-50 lower neutral

### W22.  `T1=T1a AND T4=T4a AND BBP=BBP6 AND direction_exec=short`
- Raw: n=48  W=41/L=7  WR=85.4%
- Refine: exclude RSI=RSI3 drops 7/7 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend WITH trade; deep above upper band  •  AVOID when RSI 40-50 lower neutral

### W23.  `T1=T1a AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=46  W=43/L=3  WR=93.5%
- Refine: exclude T4=T4a drops 3/3 losers (100%)
- **Final: n=35  W=35/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; zscore +1 to +2 overbought; session=ny_mid  •  AVOID when 4h trend WITH trade

### W24.  `T1=T1a AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=46  W=43/L=3  WR=93.5%
- Refine: exclude T4=T4a drops 3/3 losers (100%)
- **Final: n=35  W=35/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; upper third; zscore +1 to +2 overbought; session=ny_mid  •  AVOID when 4h trend WITH trade

### W25.  `H20=H20d AND T4=T4a AND ZS=ZS3`
- Raw: n=46  W=40/L=6  WR=87.0%
- Refine: exclude session_bucket=ny_close drops 2/6 losers (33%)
- **Final: n=44  W=40/L=4  WR=90.9%**
- **Dir: ?**  •  HTF20 mildly against; 4h trend WITH trade; zscore -1 to +1 neutral  •  AVOID when session=ny_close

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND T1=T1c AND BBP=BBP0`
- Raw: n=190  W=70/L=120  WR=36.8%
- Sharpen: sharpest is session_bucket=ny_open (28/120 of losers there)
- **Sharp: n=28  W=0/L=28  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; deep below lower band  •  ONLY when session=ny_open

### L02.  `T1=T1c AND BBP=BBP0 AND direction_exec=long`
- Raw: n=190  W=70/L=120  WR=36.8%
- Sharpen: sharpest is session_bucket=ny_open (28/120 of losers there)
- **Sharp: n=28  W=0/L=28  WR=0.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; deep below lower band  •  ONLY when session=ny_open

### L03.  `H60=H60e AND T1=T1c AND BBP=BBP0 AND direction_exec=long`
- Raw: n=190  W=70/L=120  WR=36.8%
- Sharpen: sharpest is session_bucket=ny_open (28/120 of losers there)
- **Sharp: n=28  W=0/L=28  WR=0.0%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend AGAINST trade; deep below lower band  •  ONLY when session=ny_open

### L04.  `T4=T4c AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=189  W=66/L=123  WR=34.9%
- Sharpen: sharpest is RSI=RSI1 (48/123 of losers there)
- **Sharp: n=54  W=6/L=48  WR=11.1%**
- **Dir: ?**  •  4h trend AGAINST trade; deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when RSI 20-30 oversold

### L05.  `H60=H60e AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=189  W=71/L=118  WR=37.6%
- Sharpen: sharpest is RSI=RSI1 (48/118 of losers there)
- **Sharp: n=54  W=6/L=48  WR=11.1%**
- **Dir: ?**  •  HTF60 strongly against; deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when RSI 20-30 oversold

### L06.  `BBP=BBP0 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=189  W=71/L=118  WR=37.6%
- Sharpen: sharpest is RSI=RSI1 (48/118 of losers there)
- **Sharp: n=54  W=6/L=48  WR=11.1%**
- **Dir: LONG**  •  deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when RSI 20-30 oversold

### L07.  `H60=H60e AND BBP=BBP0 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=189  W=71/L=118  WR=37.6%
- Sharpen: sharpest is RSI=RSI1 (48/118 of losers there)
- **Sharp: n=54  W=6/L=48  WR=11.1%**
- **Dir: LONG**  •  HTF60 strongly against; deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when RSI 20-30 oversold

### L08.  `H60=H60e AND T4=T4c AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=184  W=66/L=118  WR=35.9%
- Sharpen: sharpest is RSI=RSI1 (48/118 of losers there)
- **Sharp: n=54  W=6/L=48  WR=11.1%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when RSI 20-30 oversold

### L09.  `T4=T4c AND BBP=BBP0 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=184  W=66/L=118  WR=35.9%
- Sharpen: sharpest is RSI=RSI1 (48/118 of losers there)
- **Sharp: n=54  W=6/L=48  WR=11.1%**
- **Dir: LONG**  •  4h trend AGAINST trade; deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when RSI 20-30 oversold

### L10.  `T1=T1c AND T4=T4c AND BBP=BBP0`
- Raw: n=183  W=65/L=118  WR=35.5%
- Sharpen: sharpest is session_bucket=ny_open (28/118 of losers there)
- **Sharp: n=28  W=0/L=28  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; deep below lower band  •  ONLY when session=ny_open

### L11.  `T1=T1c AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=182  W=62/L=120  WR=34.1%
- Sharpen: sharpest is RSI=RSI1 (48/120 of losers there)
- **Sharp: n=54  W=6/L=48  WR=11.1%**
- **Dir: ?**  •  1h trend AGAINST trade; deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when RSI 20-30 oversold

### L12.  `H60=H60e AND T1=T1c AND T4=T4c AND BBP=BBP0`
- Raw: n=177  W=65/L=112  WR=36.7%
- Sharpen: sharpest is session_bucket=ny_open (28/112 of losers there)
- **Sharp: n=28  W=0/L=28  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; deep below lower band  •  ONLY when session=ny_open

### L13.  `T1=T1c AND T4=T4c AND BBP=BBP0 AND direction_exec=long`
- Raw: n=177  W=65/L=112  WR=36.7%
- Sharpen: sharpest is session_bucket=ny_open (28/112 of losers there)
- **Sharp: n=28  W=0/L=28  WR=0.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; deep below lower band  •  ONLY when session=ny_open

### L14.  `H60=H60e AND T1=T1c AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=166  W=55/L=111  WR=33.1%
- Sharpen: sharpest is RSI=RSI1 (48/111 of losers there)
- **Sharp: n=54  W=6/L=48  WR=11.1%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when RSI 20-30 oversold

### L15.  `T1=T1c AND BBP=BBP0 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=166  W=55/L=111  WR=33.1%
- Sharpen: sharpest is RSI=RSI1 (48/111 of losers there)
- **Sharp: n=54  W=6/L=48  WR=11.1%**
- **Dir: LONG**  •  1h trend AGAINST trade; deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when RSI 20-30 oversold

### L16.  `T1=T1c AND T4=T4c AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=161  W=50/L=111  WR=31.1%
- Sharpen: sharpest is RSI=RSI1 (48/111 of losers there)
- **Sharp: n=54  W=6/L=48  WR=11.1%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when RSI 20-30 oversold

### L17.  `H20=H20e AND H60=H60e AND RSI=RSI2 AND ZS=ZS2`
- Raw: n=154  W=61/L=93  WR=39.6%
- Sharpen: sharpest is session_bucket=asia (29/93 of losers there)
- **Sharp: n=33  W=4/L=29  WR=12.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 30-40 weak; zscore -2 to -1 oversold  •  ONLY when session=asia

### L18.  `H20=H20e AND T1=T1c AND RSI=RSI2 AND ZS=ZS2`
- Raw: n=154  W=61/L=93  WR=39.6%
- Sharpen: sharpest is session_bucket=asia (29/93 of losers there)
- **Sharp: n=33  W=4/L=29  WR=12.1%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 30-40 weak; zscore -2 to -1 oversold  •  ONLY when session=asia

### L19.  `H20=H20e AND T4=T4c AND RSI=RSI2 AND ZS=ZS2`
- Raw: n=154  W=61/L=93  WR=39.6%
- Sharpen: sharpest is session_bucket=asia (29/93 of losers there)
- **Sharp: n=33  W=4/L=29  WR=12.1%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 30-40 weak; zscore -2 to -1 oversold  •  ONLY when session=asia

### L20.  `H20=H20e AND RSI=RSI2 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=154  W=61/L=93  WR=39.6%
- Sharpen: sharpest is session_bucket=asia (29/93 of losers there)
- **Sharp: n=33  W=4/L=29  WR=12.1%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 30-40 weak; zscore -2 to -1 oversold  •  ONLY when session=asia

### L21.  `H20=H20b AND H60=H60e AND T1=T1c`
- Raw: n=133  W=53/L=80  WR=39.8%
- Sharpen: sharpest is ZS=ZS3 (24/80 of losers there)
- **Sharp: n=30  W=6/L=24  WR=20.0%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 strongly against; 1h trend AGAINST trade  •  ONLY when zscore -1 to +1 neutral

### L22.  `H20=H20b AND H60=H60e AND direction_exec=long`
- Raw: n=133  W=53/L=80  WR=39.8%
- Sharpen: sharpest is ZS=ZS3 (24/80 of losers there)
- **Sharp: n=30  W=6/L=24  WR=20.0%**
- **Dir: LONG**  •  HTF20 slightly aligned; HTF60 strongly against  •  ONLY when zscore -1 to +1 neutral

### L23.  `H20=H20b AND T1=T1c AND direction_exec=long`
- Raw: n=133  W=53/L=80  WR=39.8%
- Sharpen: sharpest is ZS=ZS3 (24/80 of losers there)
- **Sharp: n=30  W=6/L=24  WR=20.0%**
- **Dir: LONG**  •  HTF20 slightly aligned; 1h trend AGAINST trade  •  ONLY when zscore -1 to +1 neutral

### L24.  `H20=H20b AND H60=H60e AND T1=T1c AND direction_exec=long`
- Raw: n=133  W=53/L=80  WR=39.8%
- Sharpen: sharpest is ZS=ZS3 (24/80 of losers there)
- **Sharp: n=30  W=6/L=24  WR=20.0%**
- **Dir: LONG**  •  HTF20 slightly aligned; HTF60 strongly against; 1h trend AGAINST trade  •  ONLY when zscore -1 to +1 neutral

### L25.  `H60=H60e AND RSI=RSI1 AND ZS=ZS1`
- Raw: n=131  W=48/L=83  WR=36.6%
- Sharpen: sharpest is BBP=BBP0 (48/83 of losers there)
- **Sharp: n=54  W=6/L=48  WR=11.1%**
- **Dir: ?**  •  HTF60 strongly against; RSI 20-30 oversold; zscore -3 to -2 deep oversold  •  ONLY when deep below lower band

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | H60a(53/48) | H60e(47/52) |
| T1 | T1a(55/45) | T1c(45/55) |
| T4 | T4a(54/47) | T4c(46/53) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(53/48) | long(47/52) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
