# EUR_NZD — R25 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR3**  (60-90%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **4,749**  (W=2,904 / L=1,845)  -  WR: **61.1%**

## Session distribution

- asia: n=1254  W=775/L=479  WR=61.8%
- london_open: n=1063  W=640/L=423  WR=60.2%
- ny_mid: n=648  W=383/L=265  WR=59.1%
- london: n=577  W=369/L=208  WR=64.0%
- ny_open: n=430  W=256/L=174  WR=59.5%
- ny_close: n=428  W=275/L=153  WR=64.3%
- asia_late: n=270  W=161/L=109  WR=59.6%
- off_hours: n=79  W=45/L=34  WR=57.0%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1c AND T4=T4c AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=156  W=134/L=22  WR=85.9%
- Refine: exclude H20=H20d drops 11/22 losers (50%)
- **Final: n=145  W=134/L=11  WR=92.4%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when HTF20 mildly against

### W02.  `H20=H20a AND T4=T4c AND direction_exec=short AND session_bucket=london`
- Raw: n=104  W=90/L=14  WR=86.5%
- Refine: exclude T1=T1b drops 6/14 losers (43%)
- **Final: n=77  W=69/L=8  WR=89.6%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; session=london  •  AVOID when 1h trend flat

### W03.  `H20=H20a AND T1=T1c AND RSI=RSI3 AND session_bucket=london_open`
- Raw: n=101  W=88/L=13  WR=87.1%
- Refine: exclude BBP=BBP2 drops 9/13 losers (69%)
- **Final: n=89  W=85/L=4  WR=95.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 40-50 lower neutral; session=london_open  •  AVOID when lower third

### W04.  `H60=H60e AND RSI=RSI4 AND direction_exec=long`
- Raw: n=97  W=85/L=12  WR=87.6%
- Refine: exclude T1=T1a drops 11/12 losers (92%)
- **Final: n=64  W=63/L=1  WR=98.4%**
- **Dir: LONG**  •  HTF60 strongly against; RSI 50-60 upper neutral  •  AVOID when 1h trend WITH trade

### W05.  `H60=H60a AND T1=T1a AND BBP=BBP3 AND RSI=RSI2`
- Raw: n=88  W=80/L=8  WR=90.9%
- Refine: exclude H20=H20d drops 5/8 losers (62%)
- **Final: n=71  W=68/L=3  WR=95.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; middle of band; RSI 30-40 weak  •  AVOID when HTF20 mildly against

### W06.  `H60=H60a AND BBP=BBP3 AND RSI=RSI2 AND direction_exec=short`
- Raw: n=88  W=80/L=8  WR=90.9%
- Refine: exclude H20=H20d drops 5/8 losers (62%)
- **Final: n=71  W=68/L=3  WR=95.8%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; middle of band; RSI 30-40 weak  •  AVOID when HTF20 mildly against

### W07.  `H20=H20a AND BBP=BBP4 AND RSI=RSI3 AND session_bucket=london_open`
- Raw: n=83  W=74/L=9  WR=89.2%
- Refine: exclude T1=T1a drops 9/9 losers (100%)
- **Final: n=48  W=48/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; upper third; RSI 40-50 lower neutral; session=london_open  •  AVOID when 1h trend WITH trade

### W08.  `T1=T1a AND T4=T4c AND BBP=BBP3 AND RSI=RSI2`
- Raw: n=83  W=73/L=10  WR=88.0%
- Refine: exclude strategy_id=charlie_pullback_continuation_v2 drops 4/10 losers (40%)
- **Final: n=73  W=67/L=6  WR=91.8%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; middle of band; RSI 30-40 weak  •  AVOID when strategy=charlie_pullback_continuation_v2

### W09.  `H20=H20e AND T4=T4c AND session_bucket=ny_close`
- Raw: n=80  W=70/L=10  WR=87.5%
- Refine: exclude BBP=BBP4 drops 10/10 losers (100%)
- **Final: n=48  W=48/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; session=ny_close  •  AVOID when upper third

### W10.  `T4=T4a AND BBP=BBP4 AND session_bucket=ny_mid`
- Raw: n=80  W=70/L=10  WR=87.5%
- Refine: exclude ZS=ZS3 drops 5/10 losers (50%)
- **Final: n=66  W=61/L=5  WR=92.4%**
- **Dir: ?**  •  4h trend WITH trade; upper third; session=ny_mid  •  AVOID when zscore -1 to +1 neutral

### W11.  `H20=H20e AND T1=T1c AND T4=T4c AND session_bucket=ny_close`
- Raw: n=80  W=70/L=10  WR=87.5%
- Refine: exclude BBP=BBP4 drops 10/10 losers (100%)
- **Final: n=48  W=48/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_close  •  AVOID when upper third

### W12.  `H20=H20e AND T4=T4c AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=80  W=70/L=10  WR=87.5%
- Refine: exclude BBP=BBP4 drops 10/10 losers (100%)
- **Final: n=48  W=48/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend AGAINST trade; session=ny_close  •  AVOID when upper third

### W13.  `H20=H20e AND H60=H60e AND RSI=RSI4 AND direction_exec=long`
- Raw: n=80  W=69/L=11  WR=86.2%
- Refine: exclude T1=T1a drops 11/11 losers (100%)
- **Final: n=47  W=47/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 strongly against; RSI 50-60 upper neutral  •  AVOID when 1h trend WITH trade

### W14.  `T4=T4c AND BBP=BBP3 AND RSI=RSI2 AND direction_exec=short`
- Raw: n=79  W=69/L=10  WR=87.3%
- Refine: exclude strategy_id=charlie_pullback_continuation_v2 drops 4/10 losers (40%)
- **Final: n=69  W=63/L=6  WR=91.3%**
- **Dir: SHORT**  •  4h trend AGAINST trade; middle of band; RSI 30-40 weak  •  AVOID when strategy=charlie_pullback_continuation_v2

### W15.  `H20=H20a AND T1=T1a AND direction_exec=long`
- Raw: n=78  W=70/L=8  WR=89.7%
- Refine: exclude BBP=BBP1 drops 7/8 losers (88%)
- **Final: n=71  W=70/L=1  WR=98.6%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade  •  AVOID when just touched lower band

### W16.  `H20=H20a AND T1=T1a AND T4=T4c AND direction_exec=long`
- Raw: n=78  W=70/L=8  WR=89.7%
- Refine: exclude BBP=BBP1 drops 7/8 losers (88%)
- **Final: n=71  W=70/L=1  WR=98.6%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade  •  AVOID when just touched lower band

### W17.  `H20=H20b AND RSI=RSI3 AND session_bucket=london_open`
- Raw: n=78  W=68/L=10  WR=87.2%
- Refine: exclude H60=H60a drops 9/10 losers (90%)
- **Final: n=53  W=52/L=1  WR=98.1%**
- **Dir: ?**  •  HTF20 slightly aligned; RSI 40-50 lower neutral; session=london_open  •  AVOID when HTF60 aligned WITH trade

### W18.  `H60=H60a AND T1=T1c AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=77  W=69/L=8  WR=89.6%
- Refine: exclude H20=H20e drops 6/8 losers (75%)
- **Final: n=44  W=42/L=2  WR=95.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when HTF20 strongly against

### W19.  `T4=T4c AND RSI=RSI3 AND direction_exec=short AND session_bucket=london`
- Raw: n=76  W=68/L=8  WR=89.5%
- Refine: exclude T1=T1b drops 6/8 losers (75%)
- **Final: n=49  W=47/L=2  WR=95.9%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; session=london  •  AVOID when 1h trend flat

### W20.  `H20=H20e AND T1=T1c AND RSI=RSI4 AND direction_exec=long`
- Raw: n=75  W=66/L=9  WR=88.0%
- Refine: exclude ZS=ZS4 drops 9/9 losers (100%)
- **Final: n=51  W=51/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when zscore +1 to +2 overbought

### W21.  `T4=T4c AND BBP=BBP2 AND RSI=RSI3 AND session_bucket=london`
- Raw: n=74  W=67/L=7  WR=90.5%
- Refine: exclude T1=T1b drops 6/7 losers (86%)
- **Final: n=47  W=46/L=1  WR=97.9%**
- **Dir: ?**  •  4h trend AGAINST trade; lower third; RSI 40-50 lower neutral; session=london  •  AVOID when 1h trend flat

### W22.  `T1=T1c AND RSI=RSI3 AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=74  W=66/L=8  WR=89.2%
- Refine: exclude BBP=BBP1 drops 6/8 losers (75%)
- **Final: n=34  W=32/L=2  WR=94.1%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold; session=asia  •  AVOID when just touched lower band

### W23.  `RSI=RSI3 AND ZS=ZS1 AND direction_exec=long AND session_bucket=asia`
- Raw: n=74  W=66/L=8  WR=89.2%
- Refine: exclude BBP=BBP1 drops 6/8 losers (75%)
- **Final: n=34  W=32/L=2  WR=94.1%**
- **Dir: LONG**  •  RSI 40-50 lower neutral; zscore -3 to -2 deep oversold; session=asia  •  AVOID when just touched lower band

### W24.  `H20=H20a AND T4=T4c AND RSI=RSI3 AND session_bucket=london`
- Raw: n=73  W=66/L=7  WR=90.4%
- Refine: exclude T1=T1b drops 6/7 losers (86%)
- **Final: n=46  W=45/L=1  WR=97.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral; session=london  •  AVOID when 1h trend flat

### W25.  `T4=T4c AND RSI=RSI3 AND ZS=ZS2 AND session_bucket=london`
- Raw: n=72  W=65/L=7  WR=90.3%
- Refine: exclude T1=T1b drops 6/7 losers (86%)
- **Final: n=45  W=44/L=1  WR=97.8%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold; session=london  •  AVOID when 1h trend flat

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1a AND BBP=BBP2 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=230  W=89/L=141  WR=38.7%
- Sharpen: sharpest is H60=H60a (72/141 of losers there)
- **Sharp: n=88  W=16/L=72  WR=18.2%**
- **Dir: SHORT**  •  1h trend WITH trade; lower third; RSI 40-50 lower neutral  •  ONLY when HTF60 aligned WITH trade

### L02.  `T4=T4a AND BBP=BBP2 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=209  W=82/L=127  WR=39.2%
- Sharpen: sharpest is ZS=ZS2 (97/127 of losers there)
- **Sharp: n=147  W=50/L=97  WR=34.0%**
- **Dir: SHORT**  •  4h trend WITH trade; lower third; RSI 40-50 lower neutral  •  ONLY when zscore -2 to -1 oversold

### L03.  `T1=T1c AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=193  W=76/L=117  WR=39.4%
- Sharpen: sharpest is H20=H20a (33/117 of losers there)
- **Sharp: n=33  W=0/L=33  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_mid  •  ONLY when HTF20 aligned WITH trade

### L04.  `T4=T4c AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=193  W=76/L=117  WR=39.4%
- Sharpen: sharpest is H20=H20a (33/117 of losers there)
- **Sharp: n=33  W=0/L=33  WR=0.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; session=ny_mid  •  ONLY when HTF20 aligned WITH trade

### L05.  `T1=T1c AND T4=T4c AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=193  W=76/L=117  WR=39.4%
- Sharpen: sharpest is H20=H20a (33/117 of losers there)
- **Sharp: n=33  W=0/L=33  WR=0.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_mid  •  ONLY when HTF20 aligned WITH trade

### L06.  `T1=T1c AND RSI=RSI2 AND session_bucket=ny_mid`
- Raw: n=177  W=70/L=107  WR=39.5%
- Sharpen: sharpest is H20=H20a (24/107 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 30-40 weak; session=ny_mid  •  ONLY when HTF20 aligned WITH trade

### L07.  `RSI=RSI2 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=177  W=70/L=107  WR=39.5%
- Sharpen: sharpest is H20=H20a (24/107 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: LONG**  •  RSI 30-40 weak; session=ny_mid  •  ONLY when HTF20 aligned WITH trade

### L08.  `T1=T1c AND RSI=RSI2 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=177  W=70/L=107  WR=39.5%
- Sharpen: sharpest is H20=H20a (24/107 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 30-40 weak; session=ny_mid  •  ONLY when HTF20 aligned WITH trade

### L09.  `T1=T1a AND T4=T4a AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=171  W=62/L=109  WR=36.3%
- Sharpen: sharpest is H60=H60a (46/109 of losers there)
- **Sharp: n=56  W=10/L=46  WR=17.9%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; lower third; RSI 40-50 lower neutral  •  ONLY when HTF60 aligned WITH trade

### L10.  `T1=T1a AND RSI=RSI3 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=164  W=58/L=106  WR=35.4%
- Sharpen: sharpest is H60=H60a (51/106 of losers there)
- **Sharp: n=63  W=12/L=51  WR=19.0%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  ONLY when HTF60 aligned WITH trade

### L11.  `T4=T4a AND RSI=RSI4 AND direction_exec=short`
- Raw: n=154  W=51/L=103  WR=33.1%
- Sharpen: sharpest is H60=H60b (33/103 of losers there)
- **Sharp: n=41  W=8/L=33  WR=19.5%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when HTF60 slightly aligned

### L12.  `T4=T4a AND RSI=RSI3 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=147  W=50/L=97  WR=34.0%
- Sharpen: sharpest is H20=H20a (56/97 of losers there)
- **Sharp: n=75  W=19/L=56  WR=25.3%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  ONLY when HTF20 aligned WITH trade

### L13.  `T1=T1a AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=141  W=46/L=95  WR=32.6%
- Sharpen: sharpest is H20=H20e (27/95 of losers there)
- **Sharp: n=27  W=0/L=27  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when HTF20 strongly against

### L14.  `T1=T1a AND BBP=BBP0 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=135  W=46/L=89  WR=34.1%
- Sharpen: sharpest is H60=H60a (35/89 of losers there)
- **Sharp: n=42  W=7/L=35  WR=16.7%**
- **Dir: SHORT**  •  1h trend WITH trade; deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when HTF60 aligned WITH trade

### L15.  `T1=T1a AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=135  W=47/L=88  WR=34.8%
- Sharpen: sharpest is H20=H20a (56/88 of losers there)
- **Sharp: n=64  W=8/L=56  WR=12.5%**
- **Dir: ?**  •  1h trend WITH trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when HTF20 aligned WITH trade

### L16.  `T1=T1a AND T4=T4a AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=128  W=46/L=82  WR=35.9%
- Sharpen: sharpest is H20=H20e (16/82 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when HTF20 strongly against

### L17.  `T1=T1a AND RSI=RSI4 AND direction_exec=short`
- Raw: n=126  W=43/L=83  WR=34.1%
- Sharpen: sharpest is H60=H60a (31/83 of losers there)
- **Sharp: n=37  W=6/L=31  WR=16.2%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when HTF60 aligned WITH trade

### L18.  `H20=H20a AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=125  W=50/L=75  WR=40.0%
- Sharpen: sharpest is T1=T1a (56/75 of losers there)
- **Sharp: n=64  W=8/L=56  WR=12.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when 1h trend WITH trade

### L19.  `T1=T1a AND T4=T4a AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=123  W=35/L=88  WR=28.5%
- Sharpen: sharpest is session_bucket=london (20/88 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  ONLY when session=london

### L20.  `BBP=BBP3 AND RSI=RSI2 AND direction_exec=long`
- Raw: n=122  W=47/L=75  WR=38.5%
- Sharpen: sharpest is H20=H20c (28/75 of losers there)
- **Sharp: n=33  W=5/L=28  WR=15.2%**
- **Dir: LONG**  •  middle of band; RSI 30-40 weak  •  ONLY when HTF20 neutral

### L21.  `BBP=BBP3 AND RSI=RSI2 AND ZS=ZS3 AND direction_exec=long`
- Raw: n=122  W=47/L=75  WR=38.5%
- Sharpen: sharpest is H20=H20c (28/75 of losers there)
- **Sharp: n=33  W=5/L=28  WR=15.2%**
- **Dir: LONG**  •  middle of band; RSI 30-40 weak; zscore -1 to +1 neutral  •  ONLY when HTF20 neutral

### L22.  `T1=T1c AND BBP=BBP3 AND RSI=RSI2`
- Raw: n=119  W=43/L=76  WR=36.1%
- Sharpen: sharpest is H20=H20c (28/76 of losers there)
- **Sharp: n=33  W=5/L=28  WR=15.2%**
- **Dir: ?**  •  1h trend AGAINST trade; middle of band; RSI 30-40 weak  •  ONLY when HTF20 neutral

### L23.  `T1=T1c AND BBP=BBP3 AND RSI=RSI2 AND ZS=ZS3`
- Raw: n=119  W=43/L=76  WR=36.1%
- Sharpen: sharpest is H20=H20c (28/76 of losers there)
- **Sharp: n=33  W=5/L=28  WR=15.2%**
- **Dir: ?**  •  1h trend AGAINST trade; middle of band; RSI 30-40 weak; zscore -1 to +1 neutral  •  ONLY when HTF20 neutral

### L24.  `T1=T1c AND BBP=BBP3 AND RSI=RSI2 AND direction_exec=long`
- Raw: n=118  W=43/L=75  WR=36.4%
- Sharpen: sharpest is H20=H20c (28/75 of losers there)
- **Sharp: n=33  W=5/L=28  WR=15.2%**
- **Dir: LONG**  •  1h trend AGAINST trade; middle of band; RSI 30-40 weak  •  ONLY when HTF20 neutral

### L25.  `T1=T1c AND T4=T4c AND RSI=RSI2 AND session_bucket=ny_mid`
- Raw: n=117  W=38/L=79  WR=32.5%
- Sharpen: sharpest is H20=H20a (24/79 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 30-40 weak; session=ny_mid  •  ONLY when HTF20 aligned WITH trade

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
