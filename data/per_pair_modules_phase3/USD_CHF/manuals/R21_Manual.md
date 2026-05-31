# USD_CHF — R21 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20d**  (EMA20 down 0.15-0.5x)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **2,534**  (W=1,647 / L=887)  -  WR: **65.0%**

## Session distribution

- ny_mid: n=841  W=568/L=273  WR=67.5%
- london_open: n=550  W=377/L=173  WR=68.5%
- ny_close: n=468  W=283/L=185  WR=60.5%
- ny_open: n=303  W=191/L=112  WR=63.0%
- asia: n=221  W=132/L=89  WR=59.7%
- london: n=86  W=57/L=29  WR=66.3%
- asia_late: n=59  W=35/L=24  WR=59.3%
- off_hours: n=6  W=4/L=2  WR=66.7%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND H60=H60a AND T1=T1c`
- Raw: n=168  W=148/L=20  WR=88.1%
- Refine: exclude BBP=BBP4 drops 17/20 losers (85%)
- **Final: n=85  W=82/L=3  WR=96.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade  •  AVOID when upper third

### W02.  `H20=H20a AND H60=H60a AND T1=T1c AND T4=T4a`
- Raw: n=131  W=112/L=19  WR=85.5%
- Refine: exclude BBP=BBP4 drops 17/19 losers (89%)
- **Final: n=62  W=60/L=2  WR=96.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade  •  AVOID when upper third

### W03.  `T4=T4c AND RSI=RSI2 AND session_bucket=ny_mid`
- Raw: n=126  W=111/L=15  WR=88.1%
- Refine: exclude BBP=BBP2 drops 14/15 losers (93%)
- **Final: n=66  W=65/L=1  WR=98.5%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 30-40 weak; session=ny_mid  •  AVOID when lower third

### W04.  `H20=H20a AND H60=H60a AND T1=T1c AND direction_exec=short`
- Raw: n=126  W=109/L=17  WR=86.5%
- Refine: exclude session_bucket=london_open drops 14/17 losers (82%)
- **Final: n=67  W=64/L=3  WR=95.5%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade  •  AVOID when session=london_open

### W05.  `T4=T4c AND ZS=ZS1 AND session_bucket=ny_mid`
- Raw: n=115  W=100/L=15  WR=87.0%
- Refine: exclude direction_exec=short drops 14/15 losers (93%)
- **Final: n=67  W=66/L=1  WR=98.5%**
- **Dir: ?**  •  4h trend AGAINST trade; zscore -3 to -2 deep oversold; session=ny_mid  •  AVOID when short

### W06.  `H60=H60e AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=96  W=82/L=14  WR=85.4%
- Refine: exclude ZS=ZS1 drops 13/14 losers (93%)
- **Final: n=65  W=64/L=1  WR=98.5%**
- **Dir: SHORT**  •  HTF60 strongly against; session=ny_mid  •  AVOID when zscore -3 to -2 deep oversold

### W07.  `H20=H20a AND T1=T1a AND T4=T4a AND BBP=BBP2`
- Raw: n=96  W=82/L=14  WR=85.4%
- Refine: exclude H60=H60a drops 10/14 losers (71%)
- **Final: n=46  W=42/L=4  WR=91.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; lower third  •  AVOID when HTF60 aligned WITH trade

### W08.  `T1=T1c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=94  W=86/L=8  WR=91.5%
- Refine: exclude BBP=BBP3 drops 5/8 losers (62%)
- **Final: n=83  W=80/L=3  WR=96.4%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 60-70 strong  •  AVOID when middle of band

### W09.  `T1=T1c AND T4=T4c AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=88  W=75/L=13  WR=85.2%
- Refine: exclude H60=H60d drops 7/13 losers (54%)
- **Final: n=78  W=72/L=6  WR=92.3%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_mid  •  AVOID when HTF60 mildly against

### W10.  `H60=H60a AND ZS=ZS5 AND direction_exec=short`
- Raw: n=84  W=77/L=7  WR=91.7%
- Refine: exclude BBP=BBP5 drops 7/7 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; zscore +2 to +3 deep overbought  •  AVOID when just touched upper band

### W11.  `T1=T1a AND ZS=ZS3 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=84  W=72/L=12  WR=85.7%
- Refine: exclude T4=T4c drops 12/12 losers (100%)
- **Final: n=22  W=22/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend WITH trade; zscore -1 to +1 neutral; session=ny_mid  •  AVOID when 4h trend AGAINST trade

### W12.  `H20=H20e AND T4=T4c AND ZS=ZS1 AND session_bucket=ny_mid`
- Raw: n=83  W=71/L=12  WR=85.5%
- Refine: exclude direction_exec=short drops 11/12 losers (92%)
- **Final: n=57  W=56/L=1  WR=98.2%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; zscore -3 to -2 deep oversold; session=ny_mid  •  AVOID when short

### W13.  `H60=H60c AND T1=T1c AND T4=T4c`
- Raw: n=80  W=71/L=9  WR=88.8%
- Refine: exclude ZS=ZS3 drops 3/9 losers (33%)
- **Final: n=72  W=66/L=6  WR=91.7%**
- **Dir: ?**  •  HTF60 neutral; 1h trend AGAINST trade; 4h trend AGAINST trade  •  AVOID when zscore -1 to +1 neutral

### W14.  `H20=H20a AND ZS=ZS5 AND direction_exec=short`
- Raw: n=76  W=68/L=8  WR=89.5%
- Refine: exclude T1=T1a drops 8/8 losers (100%)
- **Final: n=35  W=35/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; zscore +2 to +3 deep overbought  •  AVOID when 1h trend WITH trade

### W15.  `H60=H60e AND T4=T4c AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=74  W=65/L=9  WR=87.8%
- Refine: exclude BBP=BBP1 drops 8/9 losers (89%)
- **Final: n=58  W=57/L=1  WR=98.3%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend AGAINST trade; session=ny_mid  •  AVOID when just touched lower band

### W16.  `T1=T1c AND T4=T4c AND ZS=ZS1 AND session_bucket=ny_mid`
- Raw: n=73  W=69/L=4  WR=94.5%
- Refine: exclude H60=H60d drops 3/4 losers (75%)
- **Final: n=67  W=66/L=1  WR=98.5%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold; session=ny_mid  •  AVOID when HTF60 mildly against

### W17.  `T4=T4c AND BBP=BBP1 AND direction_exec=long`
- Raw: n=72  W=62/L=10  WR=86.1%
- Refine: exclude session_bucket=asia drops 4/10 losers (40%)
- **Final: n=66  W=60/L=6  WR=90.9%**
- **Dir: LONG**  •  4h trend AGAINST trade; just touched lower band  •  AVOID when session=asia

### W18.  `T1=T1c AND T4=T4c AND BBP=BBP1 AND direction_exec=long`
- Raw: n=72  W=62/L=10  WR=86.1%
- Refine: exclude session_bucket=asia drops 4/10 losers (40%)
- **Final: n=66  W=60/L=6  WR=90.9%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; just touched lower band  •  AVOID when session=asia

### W19.  `T4=T4c AND BBP=BBP1 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=72  W=62/L=10  WR=86.1%
- Refine: exclude session_bucket=asia drops 4/10 losers (40%)
- **Final: n=66  W=60/L=6  WR=90.9%**
- **Dir: LONG**  •  4h trend AGAINST trade; just touched lower band; zscore -3 to -2 deep oversold  •  AVOID when session=asia

### W20.  `H60=H60a AND T4=T4a AND BBP=BBP2 AND session_bucket=london_open`
- Raw: n=70  W=61/L=9  WR=87.1%
- Refine: exclude T1=T1c drops 9/9 losers (100%)
- **Final: n=16  W=16/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; lower third; session=london_open  •  AVOID when 1h trend AGAINST trade

### W21.  `H20=H20a AND H60=H60a AND T1=T1c AND session_bucket=ny_mid`
- Raw: n=69  W=67/L=2  WR=97.1%
- Refine: exclude ZS=ZS3 drops 2/2 losers (100%)
- **Final: n=60  W=60/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade; session=ny_mid  •  AVOID when zscore -1 to +1 neutral

### W22.  `H20=H20a AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=69  W=59/L=10  WR=85.5%
- Refine: exclude T1=T1a drops 10/10 losers (100%)
- **Final: n=39  W=39/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; just touched upper band; zscore +2 to +3 deep overbought  •  AVOID when 1h trend WITH trade

### W23.  `H20=H20e AND H60=H60a AND T1=T1a AND RSI=RSI3`
- Raw: n=69  W=59/L=10  WR=85.5%
- Refine: exclude session_bucket=london drops 6/10 losers (60%)
- **Final: n=59  W=55/L=4  WR=93.2%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when session=london

### W24.  `T4=T4c AND ZS=ZS1 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=67  W=66/L=1  WR=98.5%
- Refine: no further refinement
- **Final: n=67  W=66/L=1  WR=98.5%**
- **Dir: LONG**  •  4h trend AGAINST trade; zscore -3 to -2 deep oversold; session=ny_mid

### W25.  `T1=T1c AND T4=T4a AND RSI=RSI5`
- Raw: n=67  W=60/L=7  WR=89.6%
- Refine: exclude BBP=BBP3 drops 5/7 losers (71%)
- **Final: n=62  W=60/L=2  WR=96.8%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 60-70 strong  •  AVOID when middle of band

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T4=T4c AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=133  W=52/L=81  WR=39.1%
- Sharpen: sharpest is H60=H60d (13/81 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; session=ny_close  •  ONLY when HTF60 mildly against

### L02.  `BBP=BBP4 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=79  W=30/L=49  WR=38.0%
- Sharpen: sharpest is H20=H20e (31/49 of losers there)
- **Sharp: n=43  W=12/L=31  WR=27.9%**
- **Dir: LONG**  •  upper third; session=ny_close  •  ONLY when HTF20 strongly against

### L03.  `T4=T4a AND ZS=ZS1 AND session_bucket=ny_mid`
- Raw: n=77  W=25/L=52  WR=32.5%
- Sharpen: sharpest is RSI=RSI2 (33/52 of losers there)
- **Sharp: n=44  W=11/L=33  WR=25.0%**
- **Dir: ?**  •  4h trend WITH trade; zscore -3 to -2 deep oversold; session=ny_mid  •  ONLY when RSI 30-40 weak

### L04.  `H60=H60a AND T1=T1a AND direction_exec=long`
- Raw: n=74  W=27/L=47  WR=36.5%
- Sharpen: sharpest is BBP=BBP4 (14/47 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade  •  ONLY when upper third

### L05.  `ZS=ZS4 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=73  W=29/L=44  WR=39.7%
- Sharpen: sharpest is H20=H20e (29/44 of losers there)
- **Sharp: n=40  W=11/L=29  WR=27.5%**
- **Dir: LONG**  •  zscore +1 to +2 overbought; session=ny_close  •  ONLY when HTF20 strongly against

### L06.  `BBP=BBP4 AND ZS=ZS4 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=73  W=29/L=44  WR=39.7%
- Sharpen: sharpest is H20=H20e (29/44 of losers there)
- **Sharp: n=40  W=11/L=29  WR=27.5%**
- **Dir: LONG**  •  upper third; zscore +1 to +2 overbought; session=ny_close  •  ONLY when HTF20 strongly against

### L07.  `H60=H60a AND T1=T1c AND T4=T4a AND RSI=RSI2`
- Raw: n=71  W=28/L=43  WR=39.4%
- Sharpen: sharpest is H20=H20b (41/43 of losers there)
- **Sharp: n=53  W=12/L=41  WR=22.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; RSI 30-40 weak  •  ONLY when HTF20 slightly aligned

### L08.  `H60=H60a AND T4=T4a AND RSI=RSI2 AND direction_exec=long`
- Raw: n=71  W=28/L=43  WR=39.4%
- Sharpen: sharpest is H20=H20b (41/43 of losers there)
- **Sharp: n=53  W=12/L=41  WR=22.6%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 30-40 weak  •  ONLY when HTF20 slightly aligned

### L09.  `H20=H20b AND H60=H60a AND T1=T1c`
- Raw: n=70  W=27/L=43  WR=38.6%
- Sharpen: sharpest is ZS=ZS1 (25/43 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 1h trend AGAINST trade  •  ONLY when zscore -3 to -2 deep oversold

### L10.  `H20=H20b AND H60=H60a AND direction_exec=long`
- Raw: n=70  W=27/L=43  WR=38.6%
- Sharpen: sharpest is ZS=ZS1 (25/43 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: LONG**  •  HTF20 slightly aligned; HTF60 aligned WITH trade  •  ONLY when zscore -3 to -2 deep oversold

### L11.  `H20=H20b AND H60=H60a AND T1=T1c AND direction_exec=long`
- Raw: n=70  W=27/L=43  WR=38.6%
- Sharpen: sharpest is ZS=ZS1 (25/43 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: LONG**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 1h trend AGAINST trade  •  ONLY when zscore -3 to -2 deep oversold

### L12.  `H20=H20b AND H60=H60a AND T4=T4a`
- Raw: n=69  W=27/L=42  WR=39.1%
- Sharpen: sharpest is ZS=ZS1 (25/42 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 4h trend WITH trade  •  ONLY when zscore -3 to -2 deep oversold

### L13.  `H20=H20b AND H60=H60a AND T1=T1c AND T4=T4a`
- Raw: n=69  W=27/L=42  WR=39.1%
- Sharpen: sharpest is ZS=ZS1 (25/42 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when zscore -3 to -2 deep oversold

### L14.  `H20=H20b AND H60=H60a AND T4=T4a AND direction_exec=long`
- Raw: n=69  W=27/L=42  WR=39.1%
- Sharpen: sharpest is ZS=ZS1 (25/42 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: LONG**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 4h trend WITH trade  •  ONLY when zscore -3 to -2 deep oversold

### L15.  `H20=H20b AND T1=T1c AND RSI=RSI2`
- Raw: n=68  W=24/L=44  WR=35.3%
- Sharpen: sharpest is H60=H60a (42/44 of losers there)
- **Sharp: n=54  W=12/L=42  WR=22.2%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend AGAINST trade; RSI 30-40 weak  •  ONLY when HTF60 aligned WITH trade

### L16.  `H20=H20b AND RSI=RSI2 AND direction_exec=long`
- Raw: n=68  W=24/L=44  WR=35.3%
- Sharpen: sharpest is H60=H60a (42/44 of losers there)
- **Sharp: n=54  W=12/L=42  WR=22.2%**
- **Dir: LONG**  •  HTF20 slightly aligned; RSI 30-40 weak  •  ONLY when HTF60 aligned WITH trade

### L17.  `H20=H20b AND T1=T1c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=68  W=24/L=44  WR=35.3%
- Sharpen: sharpest is H60=H60a (42/44 of losers there)
- **Sharp: n=54  W=12/L=42  WR=22.2%**
- **Dir: LONG**  •  HTF20 slightly aligned; 1h trend AGAINST trade; RSI 30-40 weak  •  ONLY when HTF60 aligned WITH trade

### L18.  `H60=H60e AND ZS=ZS5 AND direction_exec=long`
- Raw: n=67  W=22/L=45  WR=32.8%
- Sharpen: sharpest is BBP=BBP6 (21/45 of losers there)
- **Sharp: n=25  W=4/L=21  WR=16.0%**
- **Dir: LONG**  •  HTF60 strongly against; zscore +2 to +3 deep overbought  •  ONLY when deep above upper band

### L19.  `H20=H20b AND T4=T4a AND RSI=RSI2`
- Raw: n=67  W=24/L=43  WR=35.8%
- Sharpen: sharpest is H60=H60a (41/43 of losers there)
- **Sharp: n=53  W=12/L=41  WR=22.6%**
- **Dir: ?**  •  HTF20 slightly aligned; 4h trend WITH trade; RSI 30-40 weak  •  ONLY when HTF60 aligned WITH trade

### L20.  `H20=H20b AND T1=T1c AND T4=T4a AND RSI=RSI2`
- Raw: n=67  W=24/L=43  WR=35.8%
- Sharpen: sharpest is H60=H60a (41/43 of losers there)
- **Sharp: n=53  W=12/L=41  WR=22.6%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend AGAINST trade; 4h trend WITH trade; RSI 30-40 weak  •  ONLY when HTF60 aligned WITH trade

### L21.  `H20=H20b AND T4=T4a AND RSI=RSI2 AND direction_exec=long`
- Raw: n=67  W=24/L=43  WR=35.8%
- Sharpen: sharpest is H60=H60a (41/43 of losers there)
- **Sharp: n=53  W=12/L=41  WR=22.6%**
- **Dir: LONG**  •  HTF20 slightly aligned; 4h trend WITH trade; RSI 30-40 weak  •  ONLY when HTF60 aligned WITH trade

### L22.  `T4=T4c AND BBP=BBP4 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=66  W=26/L=40  WR=39.4%
- Sharpen: sharpest is H20=H20e (28/40 of losers there)
- **Sharp: n=38  W=10/L=28  WR=26.3%**
- **Dir: LONG**  •  4h trend AGAINST trade; upper third; session=ny_close  •  ONLY when HTF20 strongly against

### L23.  `H20=H20e AND H60=H60e AND T4=T4c AND RSI=RSI3`
- Raw: n=65  W=25/L=40  WR=38.5%
- Sharpen: sharpest is BBP=BBP2 (23/40 of losers there)
- **Sharp: n=26  W=3/L=23  WR=11.5%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when lower third

### L24.  `H60=H60a AND T4=T4a AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=65  W=26/L=39  WR=40.0%
- Sharpen: sharpest is H20=H20b (19/39 of losers there)
- **Sharp: n=23  W=4/L=19  WR=17.4%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend WITH trade; session=ny_mid  •  ONLY when HTF20 slightly aligned

### L25.  `T1=T1a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=64  W=17/L=47  WR=26.6%
- Sharpen: sharpest is ZS=ZS5 (15/47 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 60-70 strong  •  ONLY when zscore +2 to +3 deep overbought

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(42/36) | H20e(34/42) |
| H60 | — | — |
| T1 | — | — |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(54/41) | long(46/59) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
