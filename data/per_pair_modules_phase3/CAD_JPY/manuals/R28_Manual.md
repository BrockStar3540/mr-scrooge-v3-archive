# CAD_JPY — R28 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **3,849**  (W=2,447 / L=1,402)  -  WR: **63.6%**

## Session distribution

- asia: n=1523  W=975/L=548  WR=64.0%
- ny_close: n=616  W=401/L=215  WR=65.1%
- london_open: n=484  W=301/L=183  WR=62.2%
- london: n=366  W=231/L=135  WR=63.1%
- ny_open: n=293  W=179/L=114  WR=61.1%
- ny_mid: n=284  W=185/L=99  WR=65.1%
- off_hours: n=156  W=98/L=58  WR=62.8%
- asia_late: n=127  W=77/L=50  WR=60.6%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1c AND BBP=BBP2 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=188  W=161/L=27  WR=85.6%
- Refine: exclude session_bucket=asia drops 21/27 losers (78%)
- **Final: n=91  W=85/L=6  WR=93.4%**
- **Dir: LONG**  •  1h trend AGAINST trade; lower third; RSI 40-50 lower neutral  •  AVOID when session=asia

### W02.  `T1=T1c AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=183  W=156/L=27  WR=85.2%
- Refine: exclude direction_exec=short drops 8/27 losers (30%)
- **Final: n=160  W=141/L=19  WR=88.1%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when short

### W03.  `T1=T1c AND BBP=BBP2 AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=183  W=156/L=27  WR=85.2%
- Refine: exclude direction_exec=short drops 8/27 losers (30%)
- **Final: n=160  W=141/L=19  WR=88.1%**
- **Dir: ?**  •  1h trend AGAINST trade; lower third; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when short

### W04.  `H60=H60a AND T1=T1c AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=168  W=143/L=25  WR=85.1%
- Refine: exclude T4=T4c drops 24/25 losers (96%)
- **Final: n=43  W=42/L=1  WR=97.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; lower third; RSI 40-50 lower neutral  •  AVOID when 4h trend AGAINST trade

### W05.  `T1=T1c AND RSI=RSI3 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=160  W=141/L=19  WR=88.1%
- Refine: exclude session_bucket=asia drops 15/19 losers (79%)
- **Final: n=79  W=75/L=4  WR=94.9%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when session=asia

### W06.  `H60=H60a AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=149  W=127/L=22  WR=85.2%
- Refine: exclude T4=T4c drops 21/22 losers (95%)
- **Final: n=31  W=30/L=1  WR=96.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when 4h trend AGAINST trade

### W07.  `H60=H60a AND BBP=BBP2 AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=149  W=127/L=22  WR=85.2%
- Refine: exclude T4=T4c drops 21/22 losers (95%)
- **Final: n=31  W=30/L=1  WR=96.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; lower third; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when 4h trend AGAINST trade

### W08.  `H60=H60a AND RSI=RSI3 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=149  W=127/L=22  WR=85.2%
- Refine: exclude T4=T4c drops 21/22 losers (95%)
- **Final: n=31  W=30/L=1  WR=96.8%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when 4h trend AGAINST trade

### W09.  `H60=H60a AND T1=T1c AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=141  W=123/L=18  WR=87.2%
- Refine: exclude session_bucket=asia drops 14/18 losers (78%)
- **Final: n=62  W=58/L=4  WR=93.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when session=asia

### W10.  `H20=H20a AND BBP=BBP2 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=132  W=115/L=17  WR=87.1%
- Refine: exclude session_bucket=asia drops 13/17 losers (76%)
- **Final: n=70  W=66/L=4  WR=94.3%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; lower third; RSI 40-50 lower neutral  •  AVOID when session=asia

### W11.  `H60=H60a AND T4=T4a AND ZS=ZS3`
- Raw: n=130  W=113/L=17  WR=86.9%
- Refine: exclude RSI=RSI2 drops 12/17 losers (71%)
- **Final: n=80  W=75/L=5  WR=93.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; zscore -1 to +1 neutral  •  AVOID when RSI 30-40 weak

### W12.  `T4=T4a AND ZS=ZS3 AND direction_exec=long`
- Raw: n=130  W=113/L=17  WR=86.9%
- Refine: exclude RSI=RSI2 drops 12/17 losers (71%)
- **Final: n=80  W=75/L=5  WR=93.8%**
- **Dir: LONG**  •  4h trend WITH trade; zscore -1 to +1 neutral  •  AVOID when RSI 30-40 weak

### W13.  `H60=H60a AND T4=T4a AND ZS=ZS3 AND direction_exec=long`
- Raw: n=130  W=113/L=17  WR=86.9%
- Refine: exclude RSI=RSI2 drops 12/17 losers (71%)
- **Final: n=80  W=75/L=5  WR=93.8%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend WITH trade; zscore -1 to +1 neutral  •  AVOID when RSI 30-40 weak

### W14.  `T1=T1c AND T4=T4c AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=129  W=111/L=18  WR=86.0%
- Refine: exclude session_bucket=asia drops 15/18 losers (83%)
- **Final: n=63  W=60/L=3  WR=95.2%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when session=asia

### W15.  `H20=H20a AND T1=T1a AND RSI=RSI2`
- Raw: n=128  W=110/L=18  WR=85.9%
- Refine: exclude session_bucket=london drops 12/18 losers (67%)
- **Final: n=110  W=104/L=6  WR=94.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 30-40 weak  •  AVOID when session=london

### W16.  `H20=H20a AND RSI=RSI2 AND direction_exec=short`
- Raw: n=128  W=110/L=18  WR=85.9%
- Refine: exclude session_bucket=london drops 12/18 losers (67%)
- **Final: n=110  W=104/L=6  WR=94.5%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 30-40 weak  •  AVOID when session=london

### W17.  `H20=H20a AND T1=T1a AND T4=T4a AND RSI=RSI2`
- Raw: n=128  W=110/L=18  WR=85.9%
- Refine: exclude session_bucket=london drops 12/18 losers (67%)
- **Final: n=110  W=104/L=6  WR=94.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; RSI 30-40 weak  •  AVOID when session=london

### W18.  `H20=H20a AND T1=T1a AND RSI=RSI2 AND direction_exec=short`
- Raw: n=128  W=110/L=18  WR=85.9%
- Refine: exclude session_bucket=london drops 12/18 losers (67%)
- **Final: n=110  W=104/L=6  WR=94.5%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 30-40 weak  •  AVOID when session=london

### W19.  `H20=H20a AND T4=T4a AND RSI=RSI2 AND direction_exec=short`
- Raw: n=128  W=110/L=18  WR=85.9%
- Refine: exclude session_bucket=london drops 12/18 losers (67%)
- **Final: n=110  W=104/L=6  WR=94.5%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 30-40 weak  •  AVOID when session=london

### W20.  `T4=T4c AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=126  W=113/L=13  WR=89.7%
- Refine: exclude ZS=ZS2 drops 9/13 losers (69%)
- **Final: n=103  W=99/L=4  WR=96.1%**
- **Dir: LONG**  •  4h trend AGAINST trade; session=ny_mid  •  AVOID when zscore -2 to -1 oversold

### W21.  `H60=H60a AND T1=T1c AND T4=T4a AND ZS=ZS3`
- Raw: n=124  W=107/L=17  WR=86.3%
- Refine: exclude RSI=RSI2 drops 12/17 losers (71%)
- **Final: n=74  W=69/L=5  WR=93.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; zscore -1 to +1 neutral  •  AVOID when RSI 30-40 weak

### W22.  `T1=T1c AND T4=T4a AND ZS=ZS3 AND direction_exec=long`
- Raw: n=124  W=107/L=17  WR=86.3%
- Refine: exclude RSI=RSI2 drops 12/17 losers (71%)
- **Final: n=74  W=69/L=5  WR=93.2%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend WITH trade; zscore -1 to +1 neutral  •  AVOID when RSI 30-40 weak

### W23.  `H20=H20a AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=117  W=102/L=15  WR=87.2%
- Refine: exclude ZS=ZS2 drops 11/15 losers (73%)
- **Final: n=89  W=85/L=4  WR=95.5%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; session=ny_mid  •  AVOID when zscore -2 to -1 oversold

### W24.  `H20=H20a AND H60=H60a AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=115  W=98/L=17  WR=85.2%
- Refine: exclude T4=T4c drops 16/17 losers (94%)
- **Final: n=35  W=34/L=1  WR=97.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; lower third; RSI 40-50 lower neutral  •  AVOID when 4h trend AGAINST trade

### W25.  `H20=H20a AND T1=T1c AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=111  W=97/L=14  WR=87.4%
- Refine: exclude ZS=ZS2 drops 11/14 losers (79%)
- **Final: n=85  W=82/L=3  WR=96.5%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; session=ny_mid  •  AVOID when zscore -2 to -1 oversold

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1a AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=146  W=52/L=94  WR=35.6%
- Sharpen: sharpest is ZS=ZS2 (83/94 of losers there)
- **Sharp: n=117  W=34/L=83  WR=29.1%**
- **Dir: ?**  •  1h trend WITH trade; lower third; RSI 40-50 lower neutral  •  ONLY when zscore -2 to -1 oversold

### L02.  `RSI=RSI3 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=124  W=42/L=82  WR=33.9%
- Sharpen: sharpest is T1=T1a (72/82 of losers there)
- **Sharp: n=99  W=27/L=72  WR=27.3%**
- **Dir: SHORT**  •  RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  ONLY when 1h trend WITH trade

### L03.  `BBP=BBP2 AND RSI=RSI3 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=124  W=42/L=82  WR=33.9%
- Sharpen: sharpest is T1=T1a (72/82 of losers there)
- **Sharp: n=99  W=27/L=72  WR=27.3%**
- **Dir: SHORT**  •  lower third; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  ONLY when 1h trend WITH trade

### L04.  `T1=T1a AND BBP=BBP2 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=124  W=44/L=80  WR=35.5%
- Sharpen: sharpest is ZS=ZS2 (72/80 of losers there)
- **Sharp: n=99  W=27/L=72  WR=27.3%**
- **Dir: SHORT**  •  1h trend WITH trade; lower third; RSI 40-50 lower neutral  •  ONLY when zscore -2 to -1 oversold

### L05.  `H60=H60e AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=124  W=45/L=79  WR=36.3%
- Sharpen: sharpest is ZS=ZS2 (68/79 of losers there)
- **Sharp: n=99  W=31/L=68  WR=31.3%**
- **Dir: ?**  •  HTF60 strongly against; lower third; RSI 40-50 lower neutral  •  ONLY when zscore -2 to -1 oversold

### L06.  `H60=H60e AND BBP=BBP2 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=124  W=45/L=79  WR=36.3%
- Sharpen: sharpest is ZS=ZS2 (68/79 of losers there)
- **Sharp: n=99  W=31/L=68  WR=31.3%**
- **Dir: SHORT**  •  HTF60 strongly against; lower third; RSI 40-50 lower neutral  •  ONLY when zscore -2 to -1 oversold

### L07.  `H20=H20e AND RSI=RSI3 AND ZS=ZS3 AND direction_exec=short`
- Raw: n=119  W=46/L=73  WR=38.7%
- Sharpen: sharpest is T4=T4c (28/73 of losers there)
- **Sharp: n=36  W=8/L=28  WR=22.2%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 40-50 lower neutral; zscore -1 to +1 neutral  •  ONLY when 4h trend AGAINST trade

### L08.  `T1=T1a AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=117  W=34/L=83  WR=29.1%
- Sharpen: sharpest is session_bucket=london_open (14/83 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  ONLY when session=london_open

### L09.  `T1=T1a AND BBP=BBP2 AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=117  W=34/L=83  WR=29.1%
- Sharpen: sharpest is session_bucket=london_open (14/83 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; lower third; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  ONLY when session=london_open

### L10.  `T4=T4a AND RSI=RSI3 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=115  W=42/L=73  WR=36.5%
- Sharpen: sharpest is T1=T1a (63/73 of losers there)
- **Sharp: n=90  W=27/L=63  WR=30.0%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  ONLY when 1h trend WITH trade

### L11.  `H60=H60e AND T1=T1a AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=109  W=39/L=70  WR=35.8%
- Sharpen: sharpest is ZS=ZS2 (62/70 of losers there)
- **Sharp: n=87  W=25/L=62  WR=28.7%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; lower third; RSI 40-50 lower neutral  •  ONLY when zscore -2 to -1 oversold

### L12.  `H20=H20e AND H60=H60e AND RSI=RSI3 AND ZS=ZS3`
- Raw: n=105  W=40/L=65  WR=38.1%
- Sharpen: sharpest is T4=T4c (28/65 of losers there)
- **Sharp: n=36  W=8/L=28  WR=22.2%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 40-50 lower neutral; zscore -1 to +1 neutral  •  ONLY when 4h trend AGAINST trade

### L13.  `T1=T1a AND T4=T4a AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=105  W=40/L=65  WR=38.1%
- Sharpen: sharpest is ZS=ZS2 (63/65 of losers there)
- **Sharp: n=90  W=27/L=63  WR=30.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; lower third; RSI 40-50 lower neutral  •  ONLY when zscore -2 to -1 oversold

### L14.  `H60=H60e AND T4=T4a AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=105  W=41/L=64  WR=39.0%
- Sharpen: sharpest is ZS=ZS2 (59/64 of losers there)
- **Sharp: n=90  W=31/L=59  WR=34.4%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; lower third; RSI 40-50 lower neutral  •  ONLY when zscore -2 to -1 oversold

### L15.  `H60=H60e AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=103  W=40/L=63  WR=38.8%
- Sharpen: sharpest is RSI=RSI3 (26/63 of losers there)
- **Sharp: n=28  W=2/L=26  WR=7.1%**
- **Dir: SHORT**  •  HTF60 strongly against; session=ny_mid  •  ONLY when RSI 40-50 lower neutral

### L16.  `T1=T1a AND RSI=RSI3 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=99  W=27/L=72  WR=27.3%
- Sharpen: sharpest is session_bucket=london_open (14/72 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  ONLY when session=london_open

### L17.  `H60=H60e AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=99  W=31/L=68  WR=31.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=99  W=31/L=68  WR=31.3%**
- **Dir: ?**  •  HTF60 strongly against; RSI 40-50 lower neutral; zscore -2 to -1 oversold

### L18.  `H60=H60e AND BBP=BBP2 AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=99  W=31/L=68  WR=31.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=99  W=31/L=68  WR=31.3%**
- **Dir: ?**  •  HTF60 strongly against; lower third; RSI 40-50 lower neutral; zscore -2 to -1 oversold

### L19.  `H60=H60e AND RSI=RSI3 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=99  W=31/L=68  WR=31.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=99  W=31/L=68  WR=31.3%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 40-50 lower neutral; zscore -2 to -1 oversold

### L20.  `H60=H60a AND RSI=RSI2 AND session_bucket=london_open`
- Raw: n=95  W=29/L=66  WR=30.5%
- Sharpen: sharpest is H20=H20e (17/66 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 30-40 weak; session=london_open  •  ONLY when HTF20 strongly against

### L21.  `T1=T1c AND RSI=RSI2 AND session_bucket=london_open`
- Raw: n=95  W=29/L=66  WR=30.5%
- Sharpen: sharpest is H20=H20e (17/66 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 30-40 weak; session=london_open  •  ONLY when HTF20 strongly against

### L22.  `RSI=RSI2 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=95  W=29/L=66  WR=30.5%
- Sharpen: sharpest is H20=H20e (17/66 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: LONG**  •  RSI 30-40 weak; session=london_open  •  ONLY when HTF20 strongly against

### L23.  `H60=H60a AND T1=T1c AND RSI=RSI2 AND session_bucket=london_open`
- Raw: n=95  W=29/L=66  WR=30.5%
- Sharpen: sharpest is H20=H20e (17/66 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 30-40 weak; session=london_open  •  ONLY when HTF20 strongly against

### L24.  `H60=H60a AND RSI=RSI2 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=95  W=29/L=66  WR=30.5%
- Sharpen: sharpest is H20=H20e (17/66 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 30-40 weak; session=london_open  •  ONLY when HTF20 strongly against

### L25.  `T1=T1c AND RSI=RSI2 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=95  W=29/L=66  WR=30.5%
- Sharpen: sharpest is H20=H20e (17/66 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 30-40 weak; session=london_open  •  ONLY when HTF20 strongly against

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | H60a(48/42) | — |
| T1 | — | — |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
