# GBP_AUD — R36 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_3**  (5m ATR >120%)
- **A1 = A1_2**  (1h ATR 4-8x)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **3,417**  (W=1,945 / L=1,472)  -  WR: **56.9%**

## Session distribution

- asia: n=1012  W=585/L=427  WR=57.8%
- ny_mid: n=828  W=483/L=345  WR=58.3%
- london_open: n=487  W=284/L=203  WR=58.3%
- ny_open: n=477  W=267/L=210  WR=56.0%
- ny_close: n=306  W=160/L=146  WR=52.3%
- london: n=172  W=96/L=76  WR=55.8%
- off_hours: n=126  W=68/L=58  WR=54.0%
- asia_late: n=9  W=2/L=7  WR=22.2%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T4=T4a AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=139  W=119/L=20  WR=85.6%
- Refine: exclude H20=H20e drops 14/20 losers (70%)
- **Final: n=75  W=69/L=6  WR=92.0%**
- **Dir: ?**  •  4h trend WITH trade; deep below lower band; zscore -3 to -2 deep oversold  •  AVOID when HTF20 strongly against

### W02.  `H20=H20a AND T4=T4a AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=75  W=69/L=6  WR=92.0%
- Refine: exclude T1=T1a drops 4/6 losers (67%)
- **Final: n=55  W=53/L=2  WR=96.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; deep below lower band; zscore -3 to -2 deep oversold  •  AVOID when 1h trend WITH trade

### W03.  `H60=H60e AND T1=T1a AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=69  W=64/L=5  WR=92.8%
- Refine: exclude BBP=BBP2 drops 5/5 losers (100%)
- **Final: n=64  W=64/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; RSI 50-60 upper neutral; session=ny_mid  •  AVOID when lower third

### W04.  `T1=T1a AND RSI=RSI4 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=69  W=64/L=5  WR=92.8%
- Refine: exclude BBP=BBP2 drops 5/5 losers (100%)
- **Final: n=64  W=64/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 50-60 upper neutral; session=ny_mid  •  AVOID when lower third

### W05.  `H20=H20a AND T1=T1c AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=62  W=53/L=9  WR=85.5%
- Refine: exclude T4=T4c drops 7/9 losers (78%)
- **Final: n=55  W=53/L=2  WR=96.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; deep below lower band; zscore -3 to -2 deep oversold  •  AVOID when 4h trend AGAINST trade

### W06.  `H20=H20a AND T1=T1a AND T4=T4a AND ZS=ZS1`
- Raw: n=59  W=53/L=6  WR=89.8%
- Refine: exclude RSI=RSI3 drops 6/6 losers (100%)
- **Final: n=37  W=37/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  AVOID when RSI 40-50 lower neutral

### W07.  `H20=H20a AND T4=T4c AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=57  W=51/L=6  WR=89.5%
- Refine: exclude T1=T1a drops 6/6 losers (100%)
- **Final: n=31  W=31/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when 1h trend WITH trade

### W08.  `H60=H60e AND ZS=ZS5 AND session_bucket=ny_mid`
- Raw: n=56  W=52/L=4  WR=92.9%
- Refine: exclude RSI=RSI3 drops 3/4 losers (75%)
- **Final: n=53  W=52/L=1  WR=98.1%**
- **Dir: ?**  •  HTF60 strongly against; zscore +2 to +3 deep overbought; session=ny_mid  •  AVOID when RSI 40-50 lower neutral

### W09.  `T1=T1a AND ZS=ZS5 AND session_bucket=ny_mid`
- Raw: n=56  W=52/L=4  WR=92.9%
- Refine: exclude RSI=RSI3 drops 3/4 losers (75%)
- **Final: n=53  W=52/L=1  WR=98.1%**
- **Dir: ?**  •  1h trend WITH trade; zscore +2 to +3 deep overbought; session=ny_mid  •  AVOID when RSI 40-50 lower neutral

### W10.  `T4=T4c AND ZS=ZS5 AND session_bucket=ny_mid`
- Raw: n=56  W=52/L=4  WR=92.9%
- Refine: exclude RSI=RSI3 drops 3/4 losers (75%)
- **Final: n=53  W=52/L=1  WR=98.1%**
- **Dir: ?**  •  4h trend AGAINST trade; zscore +2 to +3 deep overbought; session=ny_mid  •  AVOID when RSI 40-50 lower neutral

### W11.  `ZS=ZS5 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=56  W=52/L=4  WR=92.9%
- Refine: exclude RSI=RSI3 drops 3/4 losers (75%)
- **Final: n=53  W=52/L=1  WR=98.1%**
- **Dir: LONG**  •  zscore +2 to +3 deep overbought; session=ny_mid  •  AVOID when RSI 40-50 lower neutral

### W12.  `H60=H60e AND T1=T1a AND ZS=ZS5 AND session_bucket=ny_mid`
- Raw: n=56  W=52/L=4  WR=92.9%
- Refine: exclude RSI=RSI3 drops 3/4 losers (75%)
- **Final: n=53  W=52/L=1  WR=98.1%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; zscore +2 to +3 deep overbought; session=ny_mid  •  AVOID when RSI 40-50 lower neutral

### W13.  `H60=H60e AND T4=T4c AND ZS=ZS5 AND session_bucket=ny_mid`
- Raw: n=56  W=52/L=4  WR=92.9%
- Refine: exclude RSI=RSI3 drops 3/4 losers (75%)
- **Final: n=53  W=52/L=1  WR=98.1%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; zscore +2 to +3 deep overbought; session=ny_mid  •  AVOID when RSI 40-50 lower neutral

### W14.  `H60=H60e AND ZS=ZS5 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=56  W=52/L=4  WR=92.9%
- Refine: exclude RSI=RSI3 drops 3/4 losers (75%)
- **Final: n=53  W=52/L=1  WR=98.1%**
- **Dir: LONG**  •  HTF60 strongly against; zscore +2 to +3 deep overbought; session=ny_mid  •  AVOID when RSI 40-50 lower neutral

### W15.  `T1=T1a AND T4=T4c AND ZS=ZS5 AND session_bucket=ny_mid`
- Raw: n=56  W=52/L=4  WR=92.9%
- Refine: exclude RSI=RSI3 drops 3/4 losers (75%)
- **Final: n=53  W=52/L=1  WR=98.1%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought; session=ny_mid  •  AVOID when RSI 40-50 lower neutral

### W16.  `T1=T1a AND ZS=ZS5 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=56  W=52/L=4  WR=92.9%
- Refine: exclude RSI=RSI3 drops 3/4 losers (75%)
- **Final: n=53  W=52/L=1  WR=98.1%**
- **Dir: LONG**  •  1h trend WITH trade; zscore +2 to +3 deep overbought; session=ny_mid  •  AVOID when RSI 40-50 lower neutral

### W17.  `T4=T4c AND ZS=ZS5 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=56  W=52/L=4  WR=92.9%
- Refine: exclude RSI=RSI3 drops 3/4 losers (75%)
- **Final: n=53  W=52/L=1  WR=98.1%**
- **Dir: LONG**  •  4h trend AGAINST trade; zscore +2 to +3 deep overbought; session=ny_mid  •  AVOID when RSI 40-50 lower neutral

### W18.  `H20=H20e AND H60=H60e AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=51  W=51/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=51  W=51/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 50-60 upper neutral; session=ny_mid

### W19.  `H20=H20e AND RSI=RSI4 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=51  W=51/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=51  W=51/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 50-60 upper neutral; session=ny_mid

### W20.  `H20=H20a AND T1=T1c AND T4=T4c AND ZS=ZS5`
- Raw: n=51  W=47/L=4  WR=92.2%
- Refine: exclude RSI=RSI3 drops 4/4 losers (100%)
- **Final: n=31  W=31/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  AVOID when RSI 40-50 lower neutral

### W21.  `T4=T4a AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=47  W=42/L=5  WR=89.4%
- Refine: exclude session_bucket=asia drops 5/5 losers (100%)
- **Final: n=34  W=34/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend WITH trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  AVOID when session=asia

### W22.  `H20=H20a AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=46  W=42/L=4  WR=91.3%
- Refine: exclude T4=T4c drops 4/4 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  AVOID when 4h trend AGAINST trade

### W23.  `H60=H60a AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=46  W=42/L=4  WR=91.3%
- Refine: exclude T4=T4c drops 4/4 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  AVOID when 4h trend AGAINST trade

### W24.  `T1=T1a AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=46  W=42/L=4  WR=91.3%
- Refine: exclude T4=T4c drops 4/4 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  AVOID when 4h trend AGAINST trade

### W25.  `RSI=RSI2 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=46  W=42/L=4  WR=91.3%
- Refine: exclude T4=T4c drops 4/4 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: SHORT**  •  RSI 30-40 weak; zscore -3 to -2 deep oversold  •  AVOID when 4h trend AGAINST trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1a AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=167  W=60/L=107  WR=35.9%
- Sharpen: sharpest is T4=T4c (88/107 of losers there)
- **Sharp: n=118  W=30/L=88  WR=25.4%**
- **Dir: ?**  •  1h trend WITH trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when 4h trend AGAINST trade

### L02.  `T4=T4c AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=162  W=61/L=101  WR=37.7%
- Sharpen: sharpest is T1=T1a (88/101 of losers there)
- **Sharp: n=118  W=30/L=88  WR=25.4%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when 1h trend WITH trade

### L03.  `T4=T4a AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=154  W=51/L=103  WR=33.1%
- Sharpen: sharpest is session_bucket=ny_mid (22/103 of losers there)
- **Sharp: n=22  W=0/L=22  WR=0.0%**
- **Dir: ?**  •  4h trend WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when session=ny_mid

### L04.  `T1=T1a AND T4=T4c AND ZS=ZS1`
- Raw: n=144  W=48/L=96  WR=33.3%
- Sharpen: sharpest is RSI=RSI3 (88/96 of losers there)
- **Sharp: n=118  W=30/L=88  WR=25.4%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when RSI 40-50 lower neutral

### L05.  `H20=H20e AND T4=T4c AND session_bucket=ny_open`
- Raw: n=136  W=54/L=82  WR=39.7%
- Sharpen: sharpest is T1=T1a (38/82 of losers there)
- **Sharp: n=50  W=12/L=38  WR=24.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; session=ny_open  •  ONLY when 1h trend WITH trade

### L06.  `T1=T1c AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=120  W=47/L=73  WR=39.2%
- Sharpen: sharpest is H60=H60a (47/73 of losers there)
- **Sharp: n=52  W=5/L=47  WR=9.6%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; session=ny_mid  •  ONLY when HTF60 aligned WITH trade

### L07.  `T1=T1c AND T4=T4a AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=119  W=39/L=80  WR=32.8%
- Sharpen: sharpest is session_bucket=ny_mid (22/80 of losers there)
- **Sharp: n=22  W=0/L=22  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when session=ny_mid

### L08.  `H20=H20a AND T4=T4a AND ZS=ZS5`
- Raw: n=119  W=44/L=75  WR=37.0%
- Sharpen: sharpest is H60=H60e (29/75 of losers there)
- **Sharp: n=31  W=2/L=29  WR=6.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  ONLY when HTF60 strongly against

### L09.  `H60=H60e AND T4=T4a AND RSI=RSI3 AND session_bucket=ny_mid`
- Raw: n=119  W=46/L=73  WR=38.7%
- Sharpen: sharpest is H20=H20a (46/73 of losers there)
- **Sharp: n=60  W=14/L=46  WR=23.3%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; RSI 40-50 lower neutral; session=ny_mid  •  ONLY when HTF20 aligned WITH trade

### L10.  `T4=T4a AND RSI=RSI3 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=119  W=46/L=73  WR=38.7%
- Sharpen: sharpest is H20=H20a (46/73 of losers there)
- **Sharp: n=60  W=14/L=46  WR=23.3%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 40-50 lower neutral; session=ny_mid  •  ONLY when HTF20 aligned WITH trade

### L11.  `T1=T1a AND T4=T4c AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=118  W=30/L=88  WR=25.4%
- Sharpen: no sharper sub-pattern
- **Sharp: n=118  W=30/L=88  WR=25.4%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold

### L12.  `T1=T1a AND T4=T4c AND BBP=BBP0`
- Raw: n=118  W=47/L=71  WR=39.8%
- Sharpen: sharpest is ZS=ZS1 (64/71 of losers there)
- **Sharp: n=83  W=19/L=64  WR=22.9%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; deep below lower band  •  ONLY when zscore -3 to -2 deep oversold

### L13.  `H20=H20a AND T1=T1c AND T4=T4a AND ZS=ZS5`
- Raw: n=115  W=43/L=72  WR=37.4%
- Sharpen: sharpest is H60=H60e (29/72 of losers there)
- **Sharp: n=31  W=2/L=29  WR=6.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  ONLY when HTF60 strongly against

### L14.  `H60=H60e AND T4=T4a AND ZS=ZS5`
- Raw: n=112  W=33/L=79  WR=29.5%
- Sharpen: sharpest is H20=H20a (29/79 of losers there)
- **Sharp: n=31  W=2/L=29  WR=6.5%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  ONLY when HTF20 aligned WITH trade

### L15.  `T4=T4a AND ZS=ZS5 AND direction_exec=long`
- Raw: n=112  W=33/L=79  WR=29.5%
- Sharpen: sharpest is H20=H20a (29/79 of losers there)
- **Sharp: n=31  W=2/L=29  WR=6.5%**
- **Dir: LONG**  •  4h trend WITH trade; zscore +2 to +3 deep overbought  •  ONLY when HTF20 aligned WITH trade

### L16.  `H60=H60e AND T4=T4a AND ZS=ZS5 AND direction_exec=long`
- Raw: n=112  W=33/L=79  WR=29.5%
- Sharpen: sharpest is H20=H20a (29/79 of losers there)
- **Sharp: n=31  W=2/L=29  WR=6.5%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  ONLY when HTF20 aligned WITH trade

### L17.  `T4=T4a AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=110  W=44/L=66  WR=40.0%
- Sharpen: sharpest is H60=H60a (49/66 of losers there)
- **Sharp: n=56  W=7/L=49  WR=12.5%**
- **Dir: ?**  •  4h trend WITH trade; RSI 50-60 upper neutral; session=ny_mid  •  ONLY when HTF60 aligned WITH trade

### L18.  `H60=H60a AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=109  W=31/L=78  WR=28.4%
- Sharpen: sharpest is H20=H20a (37/78 of losers there)
- **Sharp: n=37  W=0/L=37  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; session=ny_mid  •  ONLY when HTF20 aligned WITH trade

### L19.  `RSI=RSI4 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=109  W=31/L=78  WR=28.4%
- Sharpen: sharpest is H20=H20a (37/78 of losers there)
- **Sharp: n=37  W=0/L=37  WR=0.0%**
- **Dir: SHORT**  •  RSI 50-60 upper neutral; session=ny_mid  •  ONLY when HTF20 aligned WITH trade

### L20.  `H60=H60a AND RSI=RSI4 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=109  W=31/L=78  WR=28.4%
- Sharpen: sharpest is H20=H20a (37/78 of losers there)
- **Sharp: n=37  W=0/L=37  WR=0.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; session=ny_mid  •  ONLY when HTF20 aligned WITH trade

### L21.  `H60=H60e AND BBP=BBP4 AND RSI=RSI3`
- Raw: n=109  W=32/L=77  WR=29.4%
- Sharpen: sharpest is H20=H20a (30/77 of losers there)
- **Sharp: n=32  W=2/L=30  WR=6.2%**
- **Dir: ?**  •  HTF60 strongly against; upper third; RSI 40-50 lower neutral  •  ONLY when HTF20 aligned WITH trade

### L22.  `BBP=BBP4 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=109  W=32/L=77  WR=29.4%
- Sharpen: sharpest is H20=H20a (30/77 of losers there)
- **Sharp: n=32  W=2/L=30  WR=6.2%**
- **Dir: LONG**  •  upper third; RSI 40-50 lower neutral  •  ONLY when HTF20 aligned WITH trade

### L23.  `H60=H60e AND BBP=BBP4 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=109  W=32/L=77  WR=29.4%
- Sharpen: sharpest is H20=H20a (30/77 of losers there)
- **Sharp: n=32  W=2/L=30  WR=6.2%**
- **Dir: LONG**  •  HTF60 strongly against; upper third; RSI 40-50 lower neutral  •  ONLY when HTF20 aligned WITH trade

### L24.  `T1=T1c AND T4=T4a AND BBP=BBP3 AND RSI=RSI3`
- Raw: n=109  W=39/L=70  WR=35.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=109  W=39/L=70  WR=35.8%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; middle of band; RSI 40-50 lower neutral

### L25.  `H60=H60a AND T4=T4c AND ZS=ZS1`
- Raw: n=107  W=37/L=70  WR=34.6%
- Sharpen: sharpest is BBP=BBP0 (50/70 of losers there)
- **Sharp: n=69  W=19/L=50  WR=27.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when deep below lower band

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
