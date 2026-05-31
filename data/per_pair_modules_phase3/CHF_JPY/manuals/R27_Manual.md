# CHF_JPY — R27 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **6,794**  (W=4,145 / L=2,649)  -  WR: **61.0%**

## Session distribution

- asia: n=1796  W=1099/L=697  WR=61.2%
- london_open: n=1478  W=884/L=594  WR=59.8%
- ny_mid: n=1141  W=698/L=443  WR=61.2%
- ny_open: n=745  W=459/L=286  WR=61.6%
- london: n=625  W=396/L=229  WR=63.4%
- ny_close: n=559  W=352/L=207  WR=63.0%
- asia_late: n=383  W=220/L=163  WR=57.4%
- off_hours: n=67  W=37/L=30  WR=55.2%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND H60=H60a AND RSI=RSI3 AND ZS=ZS3`
- Raw: n=179  W=153/L=26  WR=85.5%
- Refine: exclude BBP=BBP2 drops 7/26 losers (27%)
- **Final: n=161  W=142/L=19  WR=88.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 40-50 lower neutral; zscore -1 to +1 neutral  •  AVOID when lower third

### W02.  `H20=H20a AND RSI=RSI3 AND ZS=ZS3 AND direction_exec=long`
- Raw: n=179  W=153/L=26  WR=85.5%
- Refine: exclude BBP=BBP2 drops 7/26 losers (27%)
- **Final: n=161  W=142/L=19  WR=88.2%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 40-50 lower neutral; zscore -1 to +1 neutral  •  AVOID when lower third

### W03.  `H20=H20a AND RSI=RSI3 AND session_bucket=london_open`
- Raw: n=146  W=126/L=20  WR=86.3%
- Refine: exclude ZS=ZS4 drops 13/20 losers (65%)
- **Final: n=99  W=92/L=7  WR=92.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 40-50 lower neutral; session=london_open  •  AVOID when zscore +1 to +2 overbought

### W04.  `T4=T4a AND RSI=RSI2 AND session_bucket=ny_close`
- Raw: n=137  W=120/L=17  WR=87.6%
- Refine: exclude ZS=ZS3 drops 7/17 losers (41%)
- **Final: n=123  W=113/L=10  WR=91.9%**
- **Dir: ?**  •  4h trend WITH trade; RSI 30-40 weak; session=ny_close  •  AVOID when zscore -1 to +1 neutral

### W05.  `H20=H20a AND H60=H60a AND RSI=RSI3 AND session_bucket=london_open`
- Raw: n=137  W=118/L=19  WR=86.1%
- Refine: exclude BBP=BBP4 drops 13/19 losers (68%)
- **Final: n=90  W=84/L=6  WR=93.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 40-50 lower neutral; session=london_open  •  AVOID when upper third

### W06.  `H20=H20a AND RSI=RSI3 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=137  W=118/L=19  WR=86.1%
- Refine: exclude BBP=BBP4 drops 13/19 losers (68%)
- **Final: n=90  W=84/L=6  WR=93.3%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 40-50 lower neutral; session=london_open  •  AVOID when upper third

### W07.  `H60=H60e AND RSI=RSI2 AND session_bucket=ny_close`
- Raw: n=134  W=115/L=19  WR=85.8%
- Refine: exclude ZS=ZS3 drops 7/19 losers (37%)
- **Final: n=121  W=109/L=12  WR=90.1%**
- **Dir: ?**  •  HTF60 strongly against; RSI 30-40 weak; session=ny_close  •  AVOID when zscore -1 to +1 neutral

### W08.  `T1=T1a AND RSI=RSI2 AND session_bucket=ny_close`
- Raw: n=134  W=115/L=19  WR=85.8%
- Refine: exclude ZS=ZS3 drops 7/19 losers (37%)
- **Final: n=121  W=109/L=12  WR=90.1%**
- **Dir: ?**  •  1h trend WITH trade; RSI 30-40 weak; session=ny_close  •  AVOID when zscore -1 to +1 neutral

### W09.  `RSI=RSI2 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=134  W=115/L=19  WR=85.8%
- Refine: exclude ZS=ZS3 drops 7/19 losers (37%)
- **Final: n=121  W=109/L=12  WR=90.1%**
- **Dir: SHORT**  •  RSI 30-40 weak; session=ny_close  •  AVOID when zscore -1 to +1 neutral

### W10.  `H60=H60e AND T1=T1a AND RSI=RSI2 AND session_bucket=ny_close`
- Raw: n=134  W=115/L=19  WR=85.8%
- Refine: exclude ZS=ZS3 drops 7/19 losers (37%)
- **Final: n=121  W=109/L=12  WR=90.1%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; RSI 30-40 weak; session=ny_close  •  AVOID when zscore -1 to +1 neutral

### W11.  `H60=H60e AND RSI=RSI2 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=134  W=115/L=19  WR=85.8%
- Refine: exclude ZS=ZS3 drops 7/19 losers (37%)
- **Final: n=121  W=109/L=12  WR=90.1%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 30-40 weak; session=ny_close  •  AVOID when zscore -1 to +1 neutral

### W12.  `T1=T1a AND RSI=RSI2 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=134  W=115/L=19  WR=85.8%
- Refine: exclude ZS=ZS3 drops 7/19 losers (37%)
- **Final: n=121  W=109/L=12  WR=90.1%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 30-40 weak; session=ny_close  •  AVOID when zscore -1 to +1 neutral

### W13.  `H20=H20a AND T1=T1c AND RSI=RSI3 AND session_bucket=london_open`
- Raw: n=132  W=114/L=18  WR=86.4%
- Refine: exclude BBP=BBP4 drops 12/18 losers (67%)
- **Final: n=88  W=82/L=6  WR=93.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 40-50 lower neutral; session=london_open  •  AVOID when upper third

### W14.  `H60=H60e AND T4=T4a AND RSI=RSI2 AND session_bucket=ny_close`
- Raw: n=130  W=114/L=16  WR=87.7%
- Refine: exclude ZS=ZS3 drops 6/16 losers (38%)
- **Final: n=119  W=109/L=10  WR=91.6%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; RSI 30-40 weak; session=ny_close  •  AVOID when zscore -1 to +1 neutral

### W15.  `T1=T1a AND T4=T4a AND RSI=RSI2 AND session_bucket=ny_close`
- Raw: n=130  W=114/L=16  WR=87.7%
- Refine: exclude ZS=ZS3 drops 6/16 losers (38%)
- **Final: n=119  W=109/L=10  WR=91.6%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 30-40 weak; session=ny_close  •  AVOID when zscore -1 to +1 neutral

### W16.  `T4=T4a AND RSI=RSI2 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=130  W=114/L=16  WR=87.7%
- Refine: exclude ZS=ZS3 drops 6/16 losers (38%)
- **Final: n=119  W=109/L=10  WR=91.6%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 30-40 weak; session=ny_close  •  AVOID when zscore -1 to +1 neutral

### W17.  `H20=H20a AND BBP=BBP1 AND RSI=RSI3`
- Raw: n=124  W=111/L=13  WR=89.5%
- Refine: exclude session_bucket=london drops 6/13 losers (46%)
- **Final: n=118  W=111/L=7  WR=94.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; just touched lower band; RSI 40-50 lower neutral  •  AVOID when session=london

### W18.  `H20=H20a AND BBP=BBP1 AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=124  W=111/L=13  WR=89.5%
- Refine: exclude session_bucket=london drops 6/13 losers (46%)
- **Final: n=118  W=111/L=7  WR=94.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; just touched lower band; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when session=london

### W19.  `H20=H20a AND H60=H60a AND BBP=BBP3 AND RSI=RSI3`
- Raw: n=118  W=104/L=14  WR=88.1%
- Refine: exclude session_bucket=asia drops 6/14 losers (43%)
- **Final: n=95  W=87/L=8  WR=91.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; middle of band; RSI 40-50 lower neutral  •  AVOID when session=asia

### W20.  `H20=H20a AND BBP=BBP3 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=118  W=104/L=14  WR=88.1%
- Refine: exclude session_bucket=asia drops 6/14 losers (43%)
- **Final: n=95  W=87/L=8  WR=91.6%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; middle of band; RSI 40-50 lower neutral  •  AVOID when session=asia

### W21.  `H20=H20a AND T1=T1c AND BBP=BBP3 AND RSI=RSI3`
- Raw: n=116  W=102/L=14  WR=87.9%
- Refine: exclude session_bucket=asia drops 6/14 losers (43%)
- **Final: n=93  W=85/L=8  WR=91.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; middle of band; RSI 40-50 lower neutral  •  AVOID when session=asia

### W22.  `H20=H20e AND T4=T4a AND RSI=RSI2 AND session_bucket=ny_close`
- Raw: n=115  W=100/L=15  WR=87.0%
- Refine: exclude ZS=ZS3 drops 5/15 losers (33%)
- **Final: n=108  W=98/L=10  WR=90.7%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; RSI 30-40 weak; session=ny_close  •  AVOID when zscore -1 to +1 neutral

### W23.  `T1=T1a AND T4=T4a AND BBP=BBP1 AND session_bucket=asia`
- Raw: n=94  W=80/L=14  WR=85.1%
- Refine: exclude H20=H20e drops 13/14 losers (93%)
- **Final: n=36  W=35/L=1  WR=97.2%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; just touched lower band; session=asia  •  AVOID when HTF20 strongly against

### W24.  `H20=H20a AND T4=T4a AND BBP=BBP1 AND RSI=RSI3`
- Raw: n=89  W=82/L=7  WR=92.1%
- Refine: exclude session_bucket=london drops 4/7 losers (57%)
- **Final: n=85  W=82/L=3  WR=96.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; just touched lower band; RSI 40-50 lower neutral  •  AVOID when session=london

### W25.  `H20=H20a AND H60=H60a AND BBP=BBP1 AND RSI=RSI3`
- Raw: n=89  W=81/L=8  WR=91.0%
- Refine: exclude T4=T4c drops 6/8 losers (75%)
- **Final: n=54  W=52/L=2  WR=96.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; just touched lower band; RSI 40-50 lower neutral  •  AVOID when 4h trend AGAINST trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND H60=H60e AND T4=T4c AND RSI=RSI3`
- Raw: n=321  W=126/L=195  WR=39.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=321  W=126/L=195  WR=39.3%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; RSI 40-50 lower neutral

### L02.  `H20=H20e AND T4=T4c AND RSI=RSI3 AND direction_exec=short`
- Raw: n=321  W=126/L=195  WR=39.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=321  W=126/L=195  WR=39.3%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 40-50 lower neutral

### L03.  `H20=H20e AND T1=T1a AND T4=T4c AND RSI=RSI3`
- Raw: n=305  W=121/L=184  WR=39.7%
- Sharpen: no sharper sub-pattern
- **Sharp: n=305  W=121/L=184  WR=39.7%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral

### L04.  `H20=H20c AND H60=H60a AND session_bucket=asia`
- Raw: n=153  W=59/L=94  WR=38.6%
- Sharpen: sharpest is T4=T4a (26/94 of losers there)
- **Sharp: n=29  W=3/L=26  WR=10.3%**
- **Dir: ?**  •  HTF20 neutral; HTF60 aligned WITH trade; session=asia  •  ONLY when 4h trend WITH trade

### L05.  `H20=H20c AND T1=T1c AND session_bucket=asia`
- Raw: n=153  W=59/L=94  WR=38.6%
- Sharpen: sharpest is T4=T4a (26/94 of losers there)
- **Sharp: n=29  W=3/L=26  WR=10.3%**
- **Dir: ?**  •  HTF20 neutral; 1h trend AGAINST trade; session=asia  •  ONLY when 4h trend WITH trade

### L06.  `H20=H20c AND direction_exec=long AND session_bucket=asia`
- Raw: n=153  W=59/L=94  WR=38.6%
- Sharpen: sharpest is T4=T4a (26/94 of losers there)
- **Sharp: n=29  W=3/L=26  WR=10.3%**
- **Dir: LONG**  •  HTF20 neutral; session=asia  •  ONLY when 4h trend WITH trade

### L07.  `H20=H20c AND H60=H60a AND T1=T1c AND session_bucket=asia`
- Raw: n=153  W=59/L=94  WR=38.6%
- Sharpen: sharpest is T4=T4a (26/94 of losers there)
- **Sharp: n=29  W=3/L=26  WR=10.3%**
- **Dir: ?**  •  HTF20 neutral; HTF60 aligned WITH trade; 1h trend AGAINST trade; session=asia  •  ONLY when 4h trend WITH trade

### L08.  `H20=H20c AND H60=H60a AND direction_exec=long AND session_bucket=asia`
- Raw: n=153  W=59/L=94  WR=38.6%
- Sharpen: sharpest is T4=T4a (26/94 of losers there)
- **Sharp: n=29  W=3/L=26  WR=10.3%**
- **Dir: LONG**  •  HTF20 neutral; HTF60 aligned WITH trade; session=asia  •  ONLY when 4h trend WITH trade

### L09.  `H20=H20c AND T1=T1c AND direction_exec=long AND session_bucket=asia`
- Raw: n=153  W=59/L=94  WR=38.6%
- Sharpen: sharpest is T4=T4a (26/94 of losers there)
- **Sharp: n=29  W=3/L=26  WR=10.3%**
- **Dir: LONG**  •  HTF20 neutral; 1h trend AGAINST trade; session=asia  •  ONLY when 4h trend WITH trade

### L10.  `H20=H20a AND T4=T4c AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=152  W=60/L=92  WR=39.5%
- Sharpen: sharpest is RSI=RSI2 (88/92 of losers there)
- **Sharp: n=130  W=42/L=88  WR=32.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when RSI 30-40 weak

### L11.  `T4=T4a AND RSI=RSI2 AND ZS=ZS3 AND direction_exec=long`
- Raw: n=146  W=58/L=88  WR=39.7%
- Sharpen: sharpest is session_bucket=london_open (14/88 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 30-40 weak; zscore -1 to +1 neutral  •  ONLY when session=london_open

### L12.  `H60=H60e AND BBP=BBP1 AND session_bucket=london_open`
- Raw: n=133  W=51/L=82  WR=38.3%
- Sharpen: sharpest is T1=T1c (26/82 of losers there)
- **Sharp: n=30  W=4/L=26  WR=13.3%**
- **Dir: ?**  •  HTF60 strongly against; just touched lower band; session=london_open  •  ONLY when 1h trend AGAINST trade

### L13.  `H60=H60e AND BBP=BBP1 AND ZS=ZS1 AND session_bucket=london_open`
- Raw: n=133  W=51/L=82  WR=38.3%
- Sharpen: sharpest is T1=T1c (26/82 of losers there)
- **Sharp: n=30  W=4/L=26  WR=13.3%**
- **Dir: ?**  •  HTF60 strongly against; just touched lower band; zscore -3 to -2 deep oversold; session=london_open  •  ONLY when 1h trend AGAINST trade

### L14.  `H20=H20c AND H60=H60a AND RSI=RSI2`
- Raw: n=128  W=45/L=83  WR=35.2%
- Sharpen: sharpest is ZS=ZS2 (43/83 of losers there)
- **Sharp: n=54  W=11/L=43  WR=20.4%**
- **Dir: ?**  •  HTF20 neutral; HTF60 aligned WITH trade; RSI 30-40 weak  •  ONLY when zscore -2 to -1 oversold

### L15.  `H20=H20c AND T1=T1c AND RSI=RSI2`
- Raw: n=128  W=45/L=83  WR=35.2%
- Sharpen: sharpest is ZS=ZS2 (43/83 of losers there)
- **Sharp: n=54  W=11/L=43  WR=20.4%**
- **Dir: ?**  •  HTF20 neutral; 1h trend AGAINST trade; RSI 30-40 weak  •  ONLY when zscore -2 to -1 oversold

### L16.  `H20=H20c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=128  W=45/L=83  WR=35.2%
- Sharpen: sharpest is ZS=ZS2 (43/83 of losers there)
- **Sharp: n=54  W=11/L=43  WR=20.4%**
- **Dir: LONG**  •  HTF20 neutral; RSI 30-40 weak  •  ONLY when zscore -2 to -1 oversold

### L17.  `H20=H20c AND H60=H60a AND T1=T1c AND RSI=RSI2`
- Raw: n=128  W=45/L=83  WR=35.2%
- Sharpen: sharpest is ZS=ZS2 (43/83 of losers there)
- **Sharp: n=54  W=11/L=43  WR=20.4%**
- **Dir: ?**  •  HTF20 neutral; HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 30-40 weak  •  ONLY when zscore -2 to -1 oversold

### L18.  `H20=H20c AND H60=H60a AND RSI=RSI2 AND direction_exec=long`
- Raw: n=128  W=45/L=83  WR=35.2%
- Sharpen: sharpest is ZS=ZS2 (43/83 of losers there)
- **Sharp: n=54  W=11/L=43  WR=20.4%**
- **Dir: LONG**  •  HTF20 neutral; HTF60 aligned WITH trade; RSI 30-40 weak  •  ONLY when zscore -2 to -1 oversold

### L19.  `H20=H20c AND T1=T1c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=128  W=45/L=83  WR=35.2%
- Sharpen: sharpest is ZS=ZS2 (43/83 of losers there)
- **Sharp: n=54  W=11/L=43  WR=20.4%**
- **Dir: LONG**  •  HTF20 neutral; 1h trend AGAINST trade; RSI 30-40 weak  •  ONLY when zscore -2 to -1 oversold

### L20.  `H20=H20c AND H60=H60a AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=126  W=43/L=83  WR=34.1%
- Sharpen: sharpest is ZS=ZS2 (43/83 of losers there)
- **Sharp: n=54  W=11/L=43  WR=20.4%**
- **Dir: ?**  •  HTF20 neutral; HTF60 aligned WITH trade; RSI 30-40 weak; session=asia  •  ONLY when zscore -2 to -1 oversold

### L21.  `H20=H20c AND T1=T1c AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=126  W=43/L=83  WR=34.1%
- Sharpen: sharpest is ZS=ZS2 (43/83 of losers there)
- **Sharp: n=54  W=11/L=43  WR=20.4%**
- **Dir: ?**  •  HTF20 neutral; 1h trend AGAINST trade; RSI 30-40 weak; session=asia  •  ONLY when zscore -2 to -1 oversold

### L22.  `H20=H20c AND RSI=RSI2 AND direction_exec=long AND session_bucket=asia`
- Raw: n=126  W=43/L=83  WR=34.1%
- Sharpen: sharpest is ZS=ZS2 (43/83 of losers there)
- **Sharp: n=54  W=11/L=43  WR=20.4%**
- **Dir: LONG**  •  HTF20 neutral; RSI 30-40 weak; session=asia  •  ONLY when zscore -2 to -1 oversold

### L23.  `H20=H20e AND BBP=BBP3 AND RSI=RSI3`
- Raw: n=126  W=47/L=79  WR=37.3%
- Sharpen: sharpest is H60=H60e (56/79 of losers there)
- **Sharp: n=71  W=15/L=56  WR=21.1%**
- **Dir: ?**  •  HTF20 strongly against; middle of band; RSI 40-50 lower neutral  •  ONLY when HTF60 strongly against

### L24.  `H20=H20e AND BBP=BBP3 AND RSI=RSI3 AND ZS=ZS3`
- Raw: n=126  W=47/L=79  WR=37.3%
- Sharpen: sharpest is H60=H60e (56/79 of losers there)
- **Sharp: n=71  W=15/L=56  WR=21.1%**
- **Dir: ?**  •  HTF20 strongly against; middle of band; RSI 40-50 lower neutral; zscore -1 to +1 neutral  •  ONLY when HTF60 strongly against

### L25.  `H20=H20e AND H60=H60e AND RSI=RSI3 AND ZS=ZS3`
- Raw: n=120  W=34/L=86  WR=28.3%
- Sharpen: sharpest is BBP=BBP3 (56/86 of losers there)
- **Sharp: n=71  W=15/L=56  WR=21.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 40-50 lower neutral; zscore -1 to +1 neutral  •  ONLY when middle of band

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | — |
| T1 | T1a(52/45) | T1c(48/55) |
| T4 | T4a(55/45) | T4c(45/55) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(51/46) | long(49/54) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
