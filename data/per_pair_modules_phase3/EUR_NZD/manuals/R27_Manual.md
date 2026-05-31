# EUR_NZD — R27 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_3**  (5m ATR >120%)
- **A1 = A1_2**  (1h ATR 4-8x)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50e**  (EMA50 down >0.5x)
- **ADR = ADR5**  (>110% overshoot)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **5,152**  (W=2,984 / L=2,168)  -  WR: **57.9%**

## Session distribution

- asia: n=1192  W=648/L=544  WR=54.4%
- ny_close: n=916  W=549/L=367  WR=59.9%
- ny_mid: n=899  W=533/L=366  WR=59.3%
- ny_open: n=707  W=417/L=290  WR=59.0%
- london_open: n=679  W=397/L=282  WR=58.5%
- london: n=475  W=283/L=192  WR=59.6%
- off_hours: n=207  W=111/L=96  WR=53.6%
- asia_late: n=77  W=46/L=31  WR=59.7%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND H60=H60a AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=118  W=101/L=17  WR=85.6%
- Refine: exclude BBP=BBP0 drops 10/17 losers (59%)
- **Final: n=91  W=84/L=7  WR=92.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  AVOID when deep below lower band

### W02.  `H20=H20a AND H60=H60a AND session_bucket=london`
- Raw: n=112  W=96/L=16  WR=85.7%
- Refine: exclude RSI=RSI3 drops 8/16 losers (50%)
- **Final: n=94  W=86/L=8  WR=91.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=london  •  AVOID when RSI 40-50 lower neutral

### W03.  `H20=H20a AND H60=H60a AND RSI=RSI2 AND session_bucket=london`
- Raw: n=94  W=86/L=8  WR=91.5%
- Refine: exclude ZS=ZS3 drops 4/8 losers (50%)
- **Final: n=70  W=66/L=4  WR=94.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 30-40 weak; session=london  •  AVOID when zscore -1 to +1 neutral

### W04.  `H20=H20a AND H60=H60a AND BBP=BBP1 AND RSI=RSI2`
- Raw: n=91  W=84/L=7  WR=92.3%
- Refine: exclude session_bucket=asia drops 5/7 losers (71%)
- **Final: n=61  W=59/L=2  WR=96.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; just touched lower band; RSI 30-40 weak  •  AVOID when session=asia

### W05.  `H60=H60e AND BBP=BBP2 AND RSI=RSI3 AND session_bucket=ny_close`
- Raw: n=75  W=65/L=10  WR=86.7%
- Refine: exclude ZS=ZS3 drops 2/10 losers (20%)
- **Final: n=71  W=63/L=8  WR=88.7%**
- **Dir: ?**  •  HTF60 strongly against; lower third; RSI 40-50 lower neutral; session=ny_close  •  AVOID when zscore -1 to +1 neutral

### W06.  `T1=T1c AND BBP=BBP2 AND RSI=RSI3 AND session_bucket=ny_close`
- Raw: n=75  W=65/L=10  WR=86.7%
- Refine: exclude ZS=ZS3 drops 2/10 losers (20%)
- **Final: n=71  W=63/L=8  WR=88.7%**
- **Dir: ?**  •  1h trend AGAINST trade; lower third; RSI 40-50 lower neutral; session=ny_close  •  AVOID when zscore -1 to +1 neutral

### W07.  `T4=T4c AND BBP=BBP2 AND RSI=RSI3 AND session_bucket=ny_close`
- Raw: n=75  W=65/L=10  WR=86.7%
- Refine: exclude ZS=ZS3 drops 2/10 losers (20%)
- **Final: n=71  W=63/L=8  WR=88.7%**
- **Dir: ?**  •  4h trend AGAINST trade; lower third; RSI 40-50 lower neutral; session=ny_close  •  AVOID when zscore -1 to +1 neutral

### W08.  `BBP=BBP2 AND RSI=RSI3 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=75  W=65/L=10  WR=86.7%
- Refine: exclude ZS=ZS3 drops 2/10 losers (20%)
- **Final: n=71  W=63/L=8  WR=88.7%**
- **Dir: LONG**  •  lower third; RSI 40-50 lower neutral; session=ny_close  •  AVOID when zscore -1 to +1 neutral

### W09.  `H20=H20e AND BBP=BBP2 AND RSI=RSI3 AND session_bucket=ny_close`
- Raw: n=73  W=63/L=10  WR=86.3%
- Refine: exclude ZS=ZS3 drops 2/10 losers (20%)
- **Final: n=71  W=63/L=8  WR=88.7%**
- **Dir: ?**  •  HTF20 strongly against; lower third; RSI 40-50 lower neutral; session=ny_close  •  AVOID when zscore -1 to +1 neutral

### W10.  `H20=H20e AND RSI=RSI3 AND ZS=ZS2 AND session_bucket=ny_close`
- Raw: n=71  W=63/L=8  WR=88.7%
- Refine: no further refinement
- **Final: n=71  W=63/L=8  WR=88.7%**
- **Dir: ?**  •  HTF20 strongly against; RSI 40-50 lower neutral; zscore -2 to -1 oversold; session=ny_close

### W11.  `H60=H60e AND RSI=RSI3 AND ZS=ZS2 AND session_bucket=ny_close`
- Raw: n=71  W=63/L=8  WR=88.7%
- Refine: no further refinement
- **Final: n=71  W=63/L=8  WR=88.7%**
- **Dir: ?**  •  HTF60 strongly against; RSI 40-50 lower neutral; zscore -2 to -1 oversold; session=ny_close

### W12.  `T1=T1c AND RSI=RSI3 AND ZS=ZS2 AND session_bucket=ny_close`
- Raw: n=71  W=63/L=8  WR=88.7%
- Refine: no further refinement
- **Final: n=71  W=63/L=8  WR=88.7%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold; session=ny_close

### W13.  `T4=T4c AND RSI=RSI3 AND ZS=ZS2 AND session_bucket=ny_close`
- Raw: n=71  W=63/L=8  WR=88.7%
- Refine: no further refinement
- **Final: n=71  W=63/L=8  WR=88.7%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold; session=ny_close

### W14.  `RSI=RSI3 AND ZS=ZS2 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=71  W=63/L=8  WR=88.7%
- Refine: no further refinement
- **Final: n=71  W=63/L=8  WR=88.7%**
- **Dir: LONG**  •  RSI 40-50 lower neutral; zscore -2 to -1 oversold; session=ny_close

### W15.  `H20=H20a AND T1=T1a AND RSI=RSI2 AND session_bucket=london`
- Raw: n=70  W=64/L=6  WR=91.4%
- Refine: exclude ZS=ZS3 drops 4/6 losers (67%)
- **Final: n=48  W=46/L=2  WR=95.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 30-40 weak; session=london  •  AVOID when zscore -1 to +1 neutral

### W16.  `H20=H20a AND T4=T4a AND RSI=RSI2 AND session_bucket=london`
- Raw: n=70  W=64/L=6  WR=91.4%
- Refine: exclude ZS=ZS3 drops 4/6 losers (67%)
- **Final: n=48  W=46/L=2  WR=95.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 30-40 weak; session=london  •  AVOID when zscore -1 to +1 neutral

### W17.  `H20=H20a AND RSI=RSI2 AND direction_exec=short AND session_bucket=london`
- Raw: n=70  W=64/L=6  WR=91.4%
- Refine: exclude ZS=ZS3 drops 4/6 losers (67%)
- **Final: n=48  W=46/L=2  WR=95.8%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 30-40 weak; session=london  •  AVOID when zscore -1 to +1 neutral

### W18.  `H20=H20a AND T1=T1a AND BBP=BBP1 AND RSI=RSI2`
- Raw: n=66  W=59/L=7  WR=89.4%
- Refine: exclude session_bucket=asia drops 5/7 losers (71%)
- **Final: n=36  W=34/L=2  WR=94.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; just touched lower band; RSI 30-40 weak  •  AVOID when session=asia

### W19.  `H20=H20a AND T4=T4a AND BBP=BBP1 AND RSI=RSI2`
- Raw: n=66  W=59/L=7  WR=89.4%
- Refine: exclude session_bucket=asia drops 5/7 losers (71%)
- **Final: n=36  W=34/L=2  WR=94.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; just touched lower band; RSI 30-40 weak  •  AVOID when session=asia

### W20.  `H20=H20a AND BBP=BBP1 AND RSI=RSI2 AND direction_exec=short`
- Raw: n=66  W=59/L=7  WR=89.4%
- Refine: exclude session_bucket=asia drops 5/7 losers (71%)
- **Final: n=36  W=34/L=2  WR=94.4%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; just touched lower band; RSI 30-40 weak  •  AVOID when session=asia

### W21.  `H20=H20e AND H60=H60a AND BBP=BBP1`
- Raw: n=63  W=57/L=6  WR=90.5%
- Refine: exclude session_bucket=asia drops 4/6 losers (67%)
- **Final: n=42  W=40/L=2  WR=95.2%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; just touched lower band  •  AVOID when session=asia

### W22.  `H20=H20e AND H60=H60a AND BBP=BBP1 AND ZS=ZS1`
- Raw: n=63  W=57/L=6  WR=90.5%
- Refine: exclude session_bucket=asia drops 4/6 losers (67%)
- **Final: n=42  W=40/L=2  WR=95.2%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; just touched lower band; zscore -3 to -2 deep oversold  •  AVOID when session=asia

### W23.  `T1=T1a AND RSI=RSI2 AND ZS=ZS5`
- Raw: n=62  W=54/L=8  WR=87.1%
- Refine: exclude H20=H20e drops 6/8 losers (75%)
- **Final: n=33  W=31/L=2  WR=93.9%**
- **Dir: ?**  •  1h trend WITH trade; RSI 30-40 weak; zscore +2 to +3 deep overbought  •  AVOID when HTF20 strongly against

### W24.  `RSI=RSI2 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=62  W=54/L=8  WR=87.1%
- Refine: exclude H20=H20e drops 6/8 losers (75%)
- **Final: n=33  W=31/L=2  WR=93.9%**
- **Dir: SHORT**  •  RSI 30-40 weak; zscore +2 to +3 deep overbought  •  AVOID when HTF20 strongly against

### W25.  `T1=T1a AND RSI=RSI2 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=62  W=54/L=8  WR=87.1%
- Refine: exclude H20=H20e drops 6/8 losers (75%)
- **Final: n=33  W=31/L=2  WR=93.9%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 30-40 weak; zscore +2 to +3 deep overbought  •  AVOID when HTF20 strongly against

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND T1=T1a AND ZS=ZS2`
- Raw: n=175  W=68/L=107  WR=38.9%
- Sharpen: sharpest is H20=H20e (82/107 of losers there)
- **Sharp: n=107  W=25/L=82  WR=23.4%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; zscore -2 to -1 oversold  •  ONLY when HTF20 strongly against

### L02.  `H60=H60e AND T1=T1a AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=175  W=68/L=107  WR=38.9%
- Sharpen: sharpest is H20=H20e (82/107 of losers there)
- **Sharp: n=107  W=25/L=82  WR=23.4%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; lower third; zscore -2 to -1 oversold  •  ONLY when HTF20 strongly against

### L03.  `H20=H20a AND T1=T1c AND RSI=RSI1 AND session_bucket=asia`
- Raw: n=161  W=59/L=102  WR=36.6%
- Sharpen: sharpest is ZS=ZS1 (48/102 of losers there)
- **Sharp: n=54  W=6/L=48  WR=11.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 20-30 oversold; session=asia  •  ONLY when zscore -3 to -2 deep oversold

### L04.  `H20=H20a AND T4=T4c AND RSI=RSI1 AND session_bucket=asia`
- Raw: n=161  W=59/L=102  WR=36.6%
- Sharpen: sharpest is ZS=ZS1 (48/102 of losers there)
- **Sharp: n=54  W=6/L=48  WR=11.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 20-30 oversold; session=asia  •  ONLY when zscore -3 to -2 deep oversold

### L05.  `H20=H20a AND RSI=RSI1 AND direction_exec=long AND session_bucket=asia`
- Raw: n=161  W=59/L=102  WR=36.6%
- Sharpen: sharpest is ZS=ZS1 (48/102 of losers there)
- **Sharp: n=54  W=6/L=48  WR=11.1%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 20-30 oversold; session=asia  •  ONLY when zscore -3 to -2 deep oversold

### L06.  `T1=T1c AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=161  W=60/L=101  WR=37.3%
- Sharpen: sharpest is H60=H60a (23/101 of losers there)
- **Sharp: n=26  W=3/L=23  WR=11.5%**
- **Dir: ?**  •  1h trend AGAINST trade; zscore -3 to -2 deep oversold; session=asia  •  ONLY when HTF60 aligned WITH trade

### L07.  `T4=T4c AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=161  W=63/L=98  WR=39.1%
- Sharpen: sharpest is H20=H20a (52/98 of losers there)
- **Sharp: n=74  W=22/L=52  WR=29.7%**
- **Dir: ?**  •  4h trend AGAINST trade; zscore -3 to -2 deep oversold; session=asia  •  ONLY when HTF20 aligned WITH trade

### L08.  `H20=H20d AND T4=T4c AND BBP=BBP2`
- Raw: n=154  W=60/L=94  WR=39.0%
- Sharpen: sharpest is ZS=ZS2 (91/94 of losers there)
- **Sharp: n=138  W=47/L=91  WR=34.1%**
- **Dir: ?**  •  HTF20 mildly against; 4h trend AGAINST trade; lower third  •  ONLY when zscore -2 to -1 oversold

### L09.  `T1=T1c AND ZS=ZS1 AND direction_exec=long AND session_bucket=asia`
- Raw: n=154  W=60/L=94  WR=39.0%
- Sharpen: sharpest is RSI=RSI1 (58/94 of losers there)
- **Sharp: n=85  W=27/L=58  WR=31.8%**
- **Dir: LONG**  •  1h trend AGAINST trade; zscore -3 to -2 deep oversold; session=asia  •  ONLY when RSI 20-30 oversold

### L10.  `H60=H60e AND T1=T1a AND T4=T4a AND ZS=ZS2`
- Raw: n=153  W=58/L=95  WR=37.9%
- Sharpen: sharpest is H20=H20e (77/95 of losers there)
- **Sharp: n=102  W=25/L=77  WR=24.5%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend WITH trade; zscore -2 to -1 oversold  •  ONLY when HTF20 strongly against

### L11.  `H60=H60e AND RSI=RSI2 AND session_bucket=london`
- Raw: n=152  W=57/L=95  WR=37.5%
- Sharpen: sharpest is H20=H20e (61/95 of losers there)
- **Sharp: n=86  W=25/L=61  WR=29.1%**
- **Dir: ?**  •  HTF60 strongly against; RSI 30-40 weak; session=london  •  ONLY when HTF20 strongly against

### L12.  `T1=T1c AND T4=T4c AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=150  W=56/L=94  WR=37.3%
- Sharpen: sharpest is H20=H20a (52/94 of losers there)
- **Sharp: n=74  W=22/L=52  WR=29.7%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold; session=asia  •  ONLY when HTF20 aligned WITH trade

### L13.  `T4=T4a AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=147  W=46/L=101  WR=31.3%
- Sharpen: sharpest is T1=T1a (86/101 of losers there)
- **Sharp: n=112  W=26/L=86  WR=23.2%**
- **Dir: ?**  •  4h trend WITH trade; lower third; RSI 40-50 lower neutral  •  ONLY when 1h trend WITH trade

### L14.  `T1=T1a AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=143  W=41/L=102  WR=28.7%
- Sharpen: sharpest is ZS=ZS2 (89/102 of losers there)
- **Sharp: n=112  W=23/L=89  WR=20.5%**
- **Dir: ?**  •  1h trend WITH trade; lower third; RSI 40-50 lower neutral  •  ONLY when zscore -2 to -1 oversold

### L15.  `H20=H20e AND H60=H60e AND T1=T1a AND BBP=BBP2`
- Raw: n=138  W=42/L=96  WR=30.4%
- Sharpen: sharpest is ZS=ZS2 (82/96 of losers there)
- **Sharp: n=107  W=25/L=82  WR=23.4%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend WITH trade; lower third  •  ONLY when zscore -2 to -1 oversold

### L16.  `H20=H20d AND T4=T4c AND ZS=ZS2`
- Raw: n=138  W=47/L=91  WR=34.1%
- Sharpen: sharpest is RSI=RSI2 (67/91 of losers there)
- **Sharp: n=93  W=26/L=67  WR=28.0%**
- **Dir: ?**  •  HTF20 mildly against; 4h trend AGAINST trade; zscore -2 to -1 oversold  •  ONLY when RSI 30-40 weak

### L17.  `H20=H20d AND T4=T4c AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=138  W=47/L=91  WR=34.1%
- Sharpen: sharpest is RSI=RSI2 (67/91 of losers there)
- **Sharp: n=93  W=26/L=67  WR=28.0%**
- **Dir: ?**  •  HTF20 mildly against; 4h trend AGAINST trade; lower third; zscore -2 to -1 oversold  •  ONLY when RSI 30-40 weak

### L18.  `H20=H20d AND RSI=RSI2 AND ZS=ZS2`
- Raw: n=134  W=51/L=83  WR=38.1%
- Sharpen: sharpest is T1=T1c (60/83 of losers there)
- **Sharp: n=76  W=16/L=60  WR=21.1%**
- **Dir: ?**  •  HTF20 mildly against; RSI 30-40 weak; zscore -2 to -1 oversold  •  ONLY when 1h trend AGAINST trade

### L19.  `H20=H20d AND BBP=BBP2 AND RSI=RSI2 AND ZS=ZS2`
- Raw: n=134  W=51/L=83  WR=38.1%
- Sharpen: sharpest is T1=T1c (60/83 of losers there)
- **Sharp: n=76  W=16/L=60  WR=21.1%**
- **Dir: ?**  •  HTF20 mildly against; lower third; RSI 30-40 weak; zscore -2 to -1 oversold  •  ONLY when 1h trend AGAINST trade

### L20.  `H20=H20e AND H60=H60e AND T4=T4a AND BBP=BBP2`
- Raw: n=133  W=42/L=91  WR=31.6%
- Sharpen: sharpest is ZS=ZS2 (77/91 of losers there)
- **Sharp: n=102  W=25/L=77  WR=24.5%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend WITH trade; lower third  •  ONLY when zscore -2 to -1 oversold

### L21.  `H20=H20d AND T1=T1c AND BBP=BBP2`
- Raw: n=133  W=46/L=87  WR=34.6%
- Sharpen: sharpest is RSI=RSI2 (63/87 of losers there)
- **Sharp: n=86  W=23/L=63  WR=26.7%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend AGAINST trade; lower third  •  ONLY when RSI 30-40 weak

### L22.  `H20=H20d AND BBP=BBP2 AND direction_exec=long`
- Raw: n=133  W=46/L=87  WR=34.6%
- Sharpen: sharpest is RSI=RSI2 (63/87 of losers there)
- **Sharp: n=86  W=23/L=63  WR=26.7%**
- **Dir: LONG**  •  HTF20 mildly against; lower third  •  ONLY when RSI 30-40 weak

### L23.  `H20=H20d AND T1=T1c AND T4=T4c AND BBP=BBP2`
- Raw: n=133  W=46/L=87  WR=34.6%
- Sharpen: sharpest is RSI=RSI2 (63/87 of losers there)
- **Sharp: n=86  W=23/L=63  WR=26.7%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend AGAINST trade; 4h trend AGAINST trade; lower third  •  ONLY when RSI 30-40 weak

### L24.  `H20=H20d AND T1=T1c AND BBP=BBP2 AND direction_exec=long`
- Raw: n=133  W=46/L=87  WR=34.6%
- Sharpen: sharpest is RSI=RSI2 (63/87 of losers there)
- **Sharp: n=86  W=23/L=63  WR=26.7%**
- **Dir: LONG**  •  HTF20 mildly against; 1h trend AGAINST trade; lower third  •  ONLY when RSI 30-40 weak

### L25.  `H20=H20d AND T4=T4c AND BBP=BBP2 AND direction_exec=long`
- Raw: n=133  W=46/L=87  WR=34.6%
- Sharpen: sharpest is RSI=RSI2 (63/87 of losers there)
- **Sharp: n=86  W=23/L=63  WR=26.7%**
- **Dir: LONG**  •  HTF20 mildly against; 4h trend AGAINST trade; lower third  •  ONLY when RSI 30-40 weak

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | H60a(53/44) | H60e(45/54) |
| T1 | T1a(52/46) | T1c(48/54) |
| T4 | T4a(52/46) | T4c(48/54) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(53/45) | long(47/55) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
