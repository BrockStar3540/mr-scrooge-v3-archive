# AUD_JPY — R38 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR3**  (60-90%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **3,161**  (W=1,928 / L=1,233)  -  WR: **61.0%**

## Session distribution

- asia: n=972  W=590/L=382  WR=60.7%
- ny_mid: n=785  W=490/L=295  WR=62.4%
- london_open: n=595  W=368/L=227  WR=61.8%
- london: n=321  W=187/L=134  WR=58.3%
- ny_open: n=281  W=159/L=122  WR=56.6%
- ny_close: n=153  W=101/L=52  WR=66.0%
- asia_late: n=54  W=33/L=21  WR=61.1%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60a AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=184  W=159/L=25  WR=86.4%
- Refine: exclude BBP=BBP4 drops 24/25 losers (96%)
- **Final: n=80  W=79/L=1  WR=98.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 60-70 strong; session=ny_mid  •  AVOID when upper third

### W02.  `T4=T4a AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=184  W=159/L=25  WR=86.4%
- Refine: exclude BBP=BBP4 drops 24/25 losers (96%)
- **Final: n=80  W=79/L=1  WR=98.8%**
- **Dir: ?**  •  4h trend WITH trade; RSI 60-70 strong; session=ny_mid  •  AVOID when upper third

### W03.  `RSI=RSI5 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=184  W=159/L=25  WR=86.4%
- Refine: exclude BBP=BBP4 drops 24/25 losers (96%)
- **Final: n=80  W=79/L=1  WR=98.8%**
- **Dir: LONG**  •  RSI 60-70 strong; session=ny_mid  •  AVOID when upper third

### W04.  `H60=H60a AND T4=T4a AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=184  W=159/L=25  WR=86.4%
- Refine: exclude BBP=BBP4 drops 24/25 losers (96%)
- **Final: n=80  W=79/L=1  WR=98.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 60-70 strong; session=ny_mid  •  AVOID when upper third

### W05.  `H60=H60a AND RSI=RSI5 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=184  W=159/L=25  WR=86.4%
- Refine: exclude BBP=BBP4 drops 24/25 losers (96%)
- **Final: n=80  W=79/L=1  WR=98.8%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 60-70 strong; session=ny_mid  •  AVOID when upper third

### W06.  `T4=T4a AND RSI=RSI5 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=184  W=159/L=25  WR=86.4%
- Refine: exclude BBP=BBP4 drops 24/25 losers (96%)
- **Final: n=80  W=79/L=1  WR=98.8%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 60-70 strong; session=ny_mid  •  AVOID when upper third

### W07.  `H20=H20e AND T1=T1a AND RSI=RSI3`
- Raw: n=141  W=126/L=15  WR=89.4%
- Refine: exclude BBP=BBP2 drops 14/15 losers (93%)
- **Final: n=94  W=93/L=1  WR=98.9%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when lower third

### W08.  `H60=H60e AND T1=T1a AND session_bucket=asia`
- Raw: n=132  W=115/L=17  WR=87.1%
- Refine: exclude ZS=ZS3 drops 10/17 losers (59%)
- **Final: n=96  W=89/L=7  WR=92.7%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; session=asia  •  AVOID when zscore -1 to +1 neutral

### W09.  `T1=T1a AND T4=T4c AND session_bucket=asia`
- Raw: n=132  W=115/L=17  WR=87.1%
- Refine: exclude ZS=ZS3 drops 10/17 losers (59%)
- **Final: n=96  W=89/L=7  WR=92.7%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; session=asia  •  AVOID when zscore -1 to +1 neutral

### W10.  `T1=T1a AND direction_exec=short AND session_bucket=asia`
- Raw: n=132  W=115/L=17  WR=87.1%
- Refine: exclude ZS=ZS3 drops 10/17 losers (59%)
- **Final: n=96  W=89/L=7  WR=92.7%**
- **Dir: SHORT**  •  1h trend WITH trade; session=asia  •  AVOID when zscore -1 to +1 neutral

### W11.  `H20=H20e AND H60=H60e AND T1=T1a AND session_bucket=asia`
- Raw: n=132  W=115/L=17  WR=87.1%
- Refine: exclude ZS=ZS3 drops 10/17 losers (59%)
- **Final: n=96  W=89/L=7  WR=92.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend WITH trade; session=asia  •  AVOID when zscore -1 to +1 neutral

### W12.  `H20=H20e AND T1=T1a AND T4=T4c AND session_bucket=asia`
- Raw: n=132  W=115/L=17  WR=87.1%
- Refine: exclude ZS=ZS3 drops 10/17 losers (59%)
- **Final: n=96  W=89/L=7  WR=92.7%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; session=asia  •  AVOID when zscore -1 to +1 neutral

### W13.  `H20=H20e AND T1=T1a AND direction_exec=short AND session_bucket=asia`
- Raw: n=132  W=115/L=17  WR=87.1%
- Refine: exclude ZS=ZS3 drops 10/17 losers (59%)
- **Final: n=96  W=89/L=7  WR=92.7%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend WITH trade; session=asia  •  AVOID when zscore -1 to +1 neutral

### W14.  `H60=H60e AND T1=T1a AND T4=T4c AND session_bucket=asia`
- Raw: n=132  W=115/L=17  WR=87.1%
- Refine: exclude ZS=ZS3 drops 10/17 losers (59%)
- **Final: n=96  W=89/L=7  WR=92.7%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; session=asia  •  AVOID when zscore -1 to +1 neutral

### W15.  `H60=H60e AND T1=T1a AND direction_exec=short AND session_bucket=asia`
- Raw: n=132  W=115/L=17  WR=87.1%
- Refine: exclude ZS=ZS3 drops 10/17 losers (59%)
- **Final: n=96  W=89/L=7  WR=92.7%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend WITH trade; session=asia  •  AVOID when zscore -1 to +1 neutral

### W16.  `T1=T1a AND T4=T4c AND direction_exec=short AND session_bucket=asia`
- Raw: n=132  W=115/L=17  WR=87.1%
- Refine: exclude ZS=ZS3 drops 10/17 losers (59%)
- **Final: n=96  W=89/L=7  WR=92.7%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend AGAINST trade; session=asia  •  AVOID when zscore -1 to +1 neutral

### W17.  `H60=H60e AND T1=T1a AND RSI=RSI3`
- Raw: n=125  W=114/L=11  WR=91.2%
- Refine: exclude BBP=BBP2 drops 10/11 losers (91%)
- **Final: n=84  W=83/L=1  WR=98.8%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when lower third

### W18.  `T1=T1a AND T4=T4c AND RSI=RSI3`
- Raw: n=125  W=114/L=11  WR=91.2%
- Refine: exclude BBP=BBP2 drops 10/11 losers (91%)
- **Final: n=84  W=83/L=1  WR=98.8%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when lower third

### W19.  `T1=T1a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=125  W=114/L=11  WR=91.2%
- Refine: exclude BBP=BBP2 drops 10/11 losers (91%)
- **Final: n=84  W=83/L=1  WR=98.8%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when lower third

### W20.  `H20=H20e AND H60=H60e AND T1=T1a AND RSI=RSI3`
- Raw: n=125  W=114/L=11  WR=91.2%
- Refine: exclude BBP=BBP2 drops 10/11 losers (91%)
- **Final: n=84  W=83/L=1  WR=98.8%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when lower third

### W21.  `H20=H20e AND T1=T1a AND T4=T4c AND RSI=RSI3`
- Raw: n=125  W=114/L=11  WR=91.2%
- Refine: exclude BBP=BBP2 drops 10/11 losers (91%)
- **Final: n=84  W=83/L=1  WR=98.8%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when lower third

### W22.  `H20=H20e AND T1=T1a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=125  W=114/L=11  WR=91.2%
- Refine: exclude BBP=BBP2 drops 10/11 losers (91%)
- **Final: n=84  W=83/L=1  WR=98.8%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when lower third

### W23.  `H60=H60e AND T1=T1a AND T4=T4c AND RSI=RSI3`
- Raw: n=125  W=114/L=11  WR=91.2%
- Refine: exclude BBP=BBP2 drops 10/11 losers (91%)
- **Final: n=84  W=83/L=1  WR=98.8%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when lower third

### W24.  `H60=H60e AND T1=T1a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=125  W=114/L=11  WR=91.2%
- Refine: exclude BBP=BBP2 drops 10/11 losers (91%)
- **Final: n=84  W=83/L=1  WR=98.8%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when lower third

### W25.  `T1=T1a AND T4=T4c AND RSI=RSI3 AND direction_exec=short`
- Raw: n=125  W=114/L=11  WR=91.2%
- Refine: exclude BBP=BBP2 drops 10/11 losers (91%)
- **Final: n=84  W=83/L=1  WR=98.8%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when lower third

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND RSI=RSI5 AND direction_exec=short`
- Raw: n=357  W=135/L=222  WR=37.8%
- Sharpen: sharpest is ZS=ZS5 (57/222 of losers there)
- **Sharp: n=69  W=12/L=57  WR=17.4%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 60-70 strong  •  ONLY when zscore +2 to +3 deep overbought

### L02.  `H60=H60e AND T4=T4c AND RSI=RSI5`
- Raw: n=342  W=126/L=216  WR=36.8%
- Sharpen: sharpest is ZS=ZS5 (57/216 of losers there)
- **Sharp: n=69  W=12/L=57  WR=17.4%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when zscore +2 to +3 deep overbought

### L03.  `T4=T4c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=342  W=126/L=216  WR=36.8%
- Sharpen: sharpest is ZS=ZS5 (57/216 of losers there)
- **Sharp: n=69  W=12/L=57  WR=17.4%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when zscore +2 to +3 deep overbought

### L04.  `H60=H60e AND T4=T4c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=342  W=126/L=216  WR=36.8%
- Sharpen: sharpest is ZS=ZS5 (57/216 of losers there)
- **Sharp: n=69  W=12/L=57  WR=17.4%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when zscore +2 to +3 deep overbought

### L05.  `H60=H60e AND T1=T1c AND RSI=RSI5`
- Raw: n=329  W=126/L=203  WR=38.3%
- Sharpen: sharpest is ZS=ZS5 (53/203 of losers there)
- **Sharp: n=65  W=12/L=53  WR=18.5%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when zscore +2 to +3 deep overbought

### L06.  `T1=T1c AND T4=T4c AND RSI=RSI5`
- Raw: n=329  W=126/L=203  WR=38.3%
- Sharpen: sharpest is ZS=ZS5 (53/203 of losers there)
- **Sharp: n=65  W=12/L=53  WR=18.5%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when zscore +2 to +3 deep overbought

### L07.  `T1=T1c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=329  W=126/L=203  WR=38.3%
- Sharpen: sharpest is ZS=ZS5 (53/203 of losers there)
- **Sharp: n=65  W=12/L=53  WR=18.5%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when zscore +2 to +3 deep overbought

### L08.  `H60=H60e AND T1=T1c AND T4=T4c AND RSI=RSI5`
- Raw: n=329  W=126/L=203  WR=38.3%
- Sharpen: sharpest is ZS=ZS5 (53/203 of losers there)
- **Sharp: n=65  W=12/L=53  WR=18.5%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when zscore +2 to +3 deep overbought

### L09.  `H60=H60e AND T1=T1c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=329  W=126/L=203  WR=38.3%
- Sharpen: sharpest is ZS=ZS5 (53/203 of losers there)
- **Sharp: n=65  W=12/L=53  WR=18.5%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when zscore +2 to +3 deep overbought

### L10.  `T1=T1c AND T4=T4c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=329  W=126/L=203  WR=38.3%
- Sharpen: sharpest is ZS=ZS5 (53/203 of losers there)
- **Sharp: n=65  W=12/L=53  WR=18.5%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when zscore +2 to +3 deep overbought

### L11.  `H20=H20e AND H60=H60e AND RSI=RSI5`
- Raw: n=312  W=118/L=194  WR=37.8%
- Sharpen: sharpest is ZS=ZS5 (54/194 of losers there)
- **Sharp: n=66  W=12/L=54  WR=18.2%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 60-70 strong  •  ONLY when zscore +2 to +3 deep overbought

### L12.  `H20=H20e AND RSI=RSI5 AND direction_exec=short`
- Raw: n=312  W=118/L=194  WR=37.8%
- Sharpen: sharpest is ZS=ZS5 (54/194 of losers there)
- **Sharp: n=66  W=12/L=54  WR=18.2%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 60-70 strong  •  ONLY when zscore +2 to +3 deep overbought

### L13.  `H20=H20e AND H60=H60e AND RSI=RSI5 AND direction_exec=short`
- Raw: n=312  W=118/L=194  WR=37.8%
- Sharpen: sharpest is ZS=ZS5 (54/194 of losers there)
- **Sharp: n=66  W=12/L=54  WR=18.2%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; RSI 60-70 strong  •  ONLY when zscore +2 to +3 deep overbought

### L14.  `H20=H20e AND T4=T4c AND RSI=RSI5`
- Raw: n=297  W=109/L=188  WR=36.7%
- Sharpen: sharpest is ZS=ZS5 (54/188 of losers there)
- **Sharp: n=66  W=12/L=54  WR=18.2%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when zscore +2 to +3 deep overbought

### L15.  `H20=H20e AND H60=H60e AND T4=T4c AND RSI=RSI5`
- Raw: n=297  W=109/L=188  WR=36.7%
- Sharpen: sharpest is ZS=ZS5 (54/188 of losers there)
- **Sharp: n=66  W=12/L=54  WR=18.2%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when zscore +2 to +3 deep overbought

### L16.  `H20=H20e AND T4=T4c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=297  W=109/L=188  WR=36.7%
- Sharpen: sharpest is ZS=ZS5 (54/188 of losers there)
- **Sharp: n=66  W=12/L=54  WR=18.2%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when zscore +2 to +3 deep overbought

### L17.  `H20=H20e AND T1=T1c AND RSI=RSI5`
- Raw: n=284  W=109/L=175  WR=38.4%
- Sharpen: sharpest is ZS=ZS5 (50/175 of losers there)
- **Sharp: n=62  W=12/L=50  WR=19.4%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when zscore +2 to +3 deep overbought

### L18.  `H20=H20e AND H60=H60e AND T1=T1c AND RSI=RSI5`
- Raw: n=284  W=109/L=175  WR=38.4%
- Sharpen: sharpest is ZS=ZS5 (50/175 of losers there)
- **Sharp: n=62  W=12/L=50  WR=19.4%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when zscore +2 to +3 deep overbought

### L19.  `H20=H20e AND T1=T1c AND T4=T4c AND RSI=RSI5`
- Raw: n=284  W=109/L=175  WR=38.4%
- Sharpen: sharpest is ZS=ZS5 (50/175 of losers there)
- **Sharp: n=62  W=12/L=50  WR=19.4%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when zscore +2 to +3 deep overbought

### L20.  `H20=H20e AND T1=T1c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=284  W=109/L=175  WR=38.4%
- Sharpen: sharpest is ZS=ZS5 (50/175 of losers there)
- **Sharp: n=62  W=12/L=50  WR=19.4%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when zscore +2 to +3 deep overbought

### L21.  `H60=H60e AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=139  W=46/L=93  WR=33.1%
- Sharpen: sharpest is ZS=ZS5 (30/93 of losers there)
- **Sharp: n=31  W=1/L=30  WR=3.2%**
- **Dir: ?**  •  HTF60 strongly against; RSI 60-70 strong; session=ny_mid  •  ONLY when zscore +2 to +3 deep overbought

### L22.  `T4=T4c AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=139  W=46/L=93  WR=33.1%
- Sharpen: sharpest is ZS=ZS5 (30/93 of losers there)
- **Sharp: n=31  W=1/L=30  WR=3.2%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 60-70 strong; session=ny_mid  •  ONLY when zscore +2 to +3 deep overbought

### L23.  `RSI=RSI5 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=139  W=46/L=93  WR=33.1%
- Sharpen: sharpest is ZS=ZS5 (30/93 of losers there)
- **Sharp: n=31  W=1/L=30  WR=3.2%**
- **Dir: SHORT**  •  RSI 60-70 strong; session=ny_mid  •  ONLY when zscore +2 to +3 deep overbought

### L24.  `H60=H60e AND T4=T4c AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=139  W=46/L=93  WR=33.1%
- Sharpen: sharpest is ZS=ZS5 (30/93 of losers there)
- **Sharp: n=31  W=1/L=30  WR=3.2%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 60-70 strong; session=ny_mid  •  ONLY when zscore +2 to +3 deep overbought

### L25.  `H60=H60e AND RSI=RSI5 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=139  W=46/L=93  WR=33.1%
- Sharpen: sharpest is ZS=ZS5 (30/93 of losers there)
- **Sharp: n=31  W=1/L=30  WR=3.2%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 60-70 strong; session=ny_mid  •  ONLY when zscore +2 to +3 deep overbought

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(53/44) | H20e(43/51) |
| H60 | H60a(57/45) | H60e(43/55) |
| T1 | T1a(59/40) | T1c(40/58) |
| T4 | T4a(56/45) | T4c(44/55) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(57/45) | short(43/55) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
