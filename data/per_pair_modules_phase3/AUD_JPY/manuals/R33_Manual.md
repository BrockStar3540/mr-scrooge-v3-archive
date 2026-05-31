# AUD_JPY — R33 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_2**  (1h ATR 4-8x)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50e**  (EMA50 down >0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **2,019**  (W=1,199 / L=820)  -  WR: **59.4%**

## Session distribution

- asia: n=765  W=463/L=302  WR=60.5%
- ny_close: n=507  W=306/L=201  WR=60.4%
- london: n=211  W=115/L=96  WR=54.5%
- ny_mid: n=146  W=79/L=67  WR=54.1%
- ny_open: n=125  W=79/L=46  WR=63.2%
- london_open: n=102  W=63/L=39  WR=61.8%
- off_hours: n=89  W=53/L=36  WR=59.6%
- asia_late: n=74  W=41/L=33  WR=55.4%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20e AND T4=T4c AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=74  W=63/L=11  WR=85.1%
- Refine: exclude BBP=BBP0 drops 6/11 losers (55%)
- **Final: n=56  W=51/L=5  WR=91.1%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 30-40 weak; session=asia  •  AVOID when deep below lower band

### W02.  `H60=H60e AND T4=T4c AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=74  W=63/L=11  WR=85.1%
- Refine: exclude BBP=BBP0 drops 6/11 losers (55%)
- **Final: n=56  W=51/L=5  WR=91.1%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 30-40 weak; session=asia  •  AVOID when deep below lower band

### W03.  `T1=T1a AND T4=T4c AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=74  W=63/L=11  WR=85.1%
- Refine: exclude BBP=BBP0 drops 6/11 losers (55%)
- **Final: n=56  W=51/L=5  WR=91.1%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 30-40 weak; session=asia  •  AVOID when deep below lower band

### W04.  `T4=T4c AND RSI=RSI2 AND direction_exec=short AND session_bucket=asia`
- Raw: n=74  W=63/L=11  WR=85.1%
- Refine: exclude BBP=BBP0 drops 6/11 losers (55%)
- **Final: n=56  W=51/L=5  WR=91.1%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 30-40 weak; session=asia  •  AVOID when deep below lower band

### W05.  `H20=H20a AND RSI=RSI3 AND ZS=ZS3 AND session_bucket=asia`
- Raw: n=49  W=46/L=3  WR=93.9%
- Refine: exclude T4=T4c drops 3/3 losers (100%)
- **Final: n=10  W=10/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 40-50 lower neutral; zscore -1 to +1 neutral; session=asia  •  AVOID when 4h trend AGAINST trade

### W06.  `H60=H60a AND RSI=RSI3 AND ZS=ZS3 AND session_bucket=asia`
- Raw: n=49  W=46/L=3  WR=93.9%
- Refine: exclude T4=T4c drops 3/3 losers (100%)
- **Final: n=10  W=10/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral; zscore -1 to +1 neutral; session=asia  •  AVOID when 4h trend AGAINST trade

### W07.  `T1=T1c AND RSI=RSI3 AND ZS=ZS3 AND session_bucket=asia`
- Raw: n=49  W=46/L=3  WR=93.9%
- Refine: exclude T4=T4c drops 3/3 losers (100%)
- **Final: n=10  W=10/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 40-50 lower neutral; zscore -1 to +1 neutral; session=asia  •  AVOID when 4h trend AGAINST trade

### W08.  `RSI=RSI3 AND ZS=ZS3 AND direction_exec=long AND session_bucket=asia`
- Raw: n=49  W=46/L=3  WR=93.9%
- Refine: exclude T4=T4c drops 3/3 losers (100%)
- **Final: n=10  W=10/L=0  WR=100.0%**
- **Dir: LONG**  •  RSI 40-50 lower neutral; zscore -1 to +1 neutral; session=asia  •  AVOID when 4h trend AGAINST trade

### W09.  `H20=H20a AND RSI=RSI1 AND ZS=ZS1`
- Raw: n=44  W=38/L=6  WR=86.4%
- Refine: exclude session_bucket=london drops 6/6 losers (100%)
- **Final: n=25  W=25/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 20-30 oversold; zscore -3 to -2 deep oversold  •  AVOID when session=london

### W10.  `H60=H60a AND RSI=RSI1 AND ZS=ZS1`
- Raw: n=44  W=38/L=6  WR=86.4%
- Refine: exclude session_bucket=london drops 6/6 losers (100%)
- **Final: n=25  W=25/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 20-30 oversold; zscore -3 to -2 deep oversold  •  AVOID when session=london

### W11.  `T1=T1c AND RSI=RSI1 AND ZS=ZS1`
- Raw: n=44  W=38/L=6  WR=86.4%
- Refine: exclude session_bucket=london drops 6/6 losers (100%)
- **Final: n=25  W=25/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 20-30 oversold; zscore -3 to -2 deep oversold  •  AVOID when session=london

### W12.  `RSI=RSI1 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=44  W=38/L=6  WR=86.4%
- Refine: exclude session_bucket=london drops 6/6 losers (100%)
- **Final: n=25  W=25/L=0  WR=100.0%**
- **Dir: LONG**  •  RSI 20-30 oversold; zscore -3 to -2 deep oversold  •  AVOID when session=london

### W13.  `H20=H20a AND H60=H60a AND RSI=RSI1 AND ZS=ZS1`
- Raw: n=44  W=38/L=6  WR=86.4%
- Refine: exclude session_bucket=london drops 6/6 losers (100%)
- **Final: n=25  W=25/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 20-30 oversold; zscore -3 to -2 deep oversold  •  AVOID when session=london

### W14.  `H20=H20a AND T1=T1c AND RSI=RSI1 AND ZS=ZS1`
- Raw: n=44  W=38/L=6  WR=86.4%
- Refine: exclude session_bucket=london drops 6/6 losers (100%)
- **Final: n=25  W=25/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 20-30 oversold; zscore -3 to -2 deep oversold  •  AVOID when session=london

### W15.  `H20=H20a AND RSI=RSI1 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=44  W=38/L=6  WR=86.4%
- Refine: exclude session_bucket=london drops 6/6 losers (100%)
- **Final: n=25  W=25/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 20-30 oversold; zscore -3 to -2 deep oversold  •  AVOID when session=london

### W16.  `H60=H60a AND T1=T1c AND RSI=RSI1 AND ZS=ZS1`
- Raw: n=44  W=38/L=6  WR=86.4%
- Refine: exclude session_bucket=london drops 6/6 losers (100%)
- **Final: n=25  W=25/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 20-30 oversold; zscore -3 to -2 deep oversold  •  AVOID when session=london

### W17.  `H60=H60a AND RSI=RSI1 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=44  W=38/L=6  WR=86.4%
- Refine: exclude session_bucket=london drops 6/6 losers (100%)
- **Final: n=25  W=25/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 20-30 oversold; zscore -3 to -2 deep oversold  •  AVOID when session=london

### W18.  `T1=T1c AND RSI=RSI1 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=44  W=38/L=6  WR=86.4%
- Refine: exclude session_bucket=london drops 6/6 losers (100%)
- **Final: n=25  W=25/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 20-30 oversold; zscore -3 to -2 deep oversold  •  AVOID when session=london

### W19.  `H20=H20a AND BBP=BBP3 AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=43  W=40/L=3  WR=93.0%
- Refine: exclude T4=T4c drops 3/3 losers (100%)
- **Final: n=8  W=8/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; middle of band; RSI 40-50 lower neutral; session=asia  •  AVOID when 4h trend AGAINST trade

### W20.  `H60=H60a AND BBP=BBP3 AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=43  W=40/L=3  WR=93.0%
- Refine: exclude T4=T4c drops 3/3 losers (100%)
- **Final: n=8  W=8/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; middle of band; RSI 40-50 lower neutral; session=asia  •  AVOID when 4h trend AGAINST trade

### W21.  `T1=T1c AND BBP=BBP3 AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=43  W=40/L=3  WR=93.0%
- Refine: exclude T4=T4c drops 3/3 losers (100%)
- **Final: n=8  W=8/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; middle of band; RSI 40-50 lower neutral; session=asia  •  AVOID when 4h trend AGAINST trade

### W22.  `BBP=BBP3 AND RSI=RSI3 AND direction_exec=long AND session_bucket=asia`
- Raw: n=43  W=40/L=3  WR=93.0%
- Refine: exclude T4=T4c drops 3/3 losers (100%)
- **Final: n=8  W=8/L=0  WR=100.0%**
- **Dir: LONG**  •  middle of band; RSI 40-50 lower neutral; session=asia  •  AVOID when 4h trend AGAINST trade

### W23.  `H20=H20a AND BBP=BBP1 AND session_bucket=ny_close`
- Raw: n=42  W=37/L=5  WR=88.1%
- Refine: exclude RSI=RSI3 drops 5/5 losers (100%)
- **Final: n=20  W=20/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; just touched lower band; session=ny_close  •  AVOID when RSI 40-50 lower neutral

### W24.  `H60=H60a AND BBP=BBP1 AND session_bucket=ny_close`
- Raw: n=42  W=37/L=5  WR=88.1%
- Refine: exclude RSI=RSI3 drops 5/5 losers (100%)
- **Final: n=20  W=20/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; just touched lower band; session=ny_close  •  AVOID when RSI 40-50 lower neutral

### W25.  `T1=T1c AND BBP=BBP1 AND session_bucket=ny_close`
- Raw: n=42  W=37/L=5  WR=88.1%
- Refine: exclude RSI=RSI3 drops 5/5 losers (100%)
- **Final: n=20  W=20/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; just touched lower band; session=ny_close  •  AVOID when RSI 40-50 lower neutral

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T4=T4a AND BBP=BBP1 AND ZS=ZS1`
- Raw: n=150  W=57/L=93  WR=38.0%
- Sharpen: sharpest is session_bucket=ny_close (22/93 of losers there)
- **Sharp: n=25  W=3/L=22  WR=12.0%**
- **Dir: ?**  •  4h trend WITH trade; just touched lower band; zscore -3 to -2 deep oversold  •  ONLY when session=ny_close

### L02.  `T4=T4a AND BBP=BBP2 AND RSI=RSI2`
- Raw: n=135  W=50/L=85  WR=37.0%
- Sharpen: sharpest is H20=H20a (18/85 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: ?**  •  4h trend WITH trade; lower third; RSI 30-40 weak  •  ONLY when HTF20 aligned WITH trade

### L03.  `H20=H20e AND T4=T4a AND BBP=BBP1`
- Raw: n=121  W=48/L=73  WR=39.7%
- Sharpen: sharpest is RSI=RSI1 (20/73 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; just touched lower band  •  ONLY when RSI 20-30 oversold

### L04.  `H60=H60e AND T4=T4a AND BBP=BBP1`
- Raw: n=121  W=48/L=73  WR=39.7%
- Sharpen: sharpest is RSI=RSI1 (20/73 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; just touched lower band  •  ONLY when RSI 20-30 oversold

### L05.  `T1=T1a AND T4=T4a AND BBP=BBP1`
- Raw: n=121  W=48/L=73  WR=39.7%
- Sharpen: sharpest is RSI=RSI1 (20/73 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; just touched lower band  •  ONLY when RSI 20-30 oversold

### L06.  `T4=T4a AND BBP=BBP1 AND direction_exec=short`
- Raw: n=121  W=48/L=73  WR=39.7%
- Sharpen: sharpest is RSI=RSI1 (20/73 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: SHORT**  •  4h trend WITH trade; just touched lower band  •  ONLY when RSI 20-30 oversold

### L07.  `H20=H20e AND H60=H60e AND T4=T4a AND BBP=BBP1`
- Raw: n=121  W=48/L=73  WR=39.7%
- Sharpen: sharpest is RSI=RSI1 (20/73 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend WITH trade; just touched lower band  •  ONLY when RSI 20-30 oversold

### L08.  `H20=H20e AND T1=T1a AND T4=T4a AND BBP=BBP1`
- Raw: n=121  W=48/L=73  WR=39.7%
- Sharpen: sharpest is RSI=RSI1 (20/73 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend WITH trade; just touched lower band  •  ONLY when RSI 20-30 oversold

### L09.  `H20=H20e AND T4=T4a AND BBP=BBP1 AND ZS=ZS1`
- Raw: n=121  W=48/L=73  WR=39.7%
- Sharpen: sharpest is RSI=RSI1 (20/73 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; just touched lower band; zscore -3 to -2 deep oversold  •  ONLY when RSI 20-30 oversold

### L10.  `H20=H20e AND T4=T4a AND BBP=BBP1 AND direction_exec=short`
- Raw: n=121  W=48/L=73  WR=39.7%
- Sharpen: sharpest is RSI=RSI1 (20/73 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend WITH trade; just touched lower band  •  ONLY when RSI 20-30 oversold

### L11.  `H60=H60e AND T1=T1a AND T4=T4a AND BBP=BBP1`
- Raw: n=121  W=48/L=73  WR=39.7%
- Sharpen: sharpest is RSI=RSI1 (20/73 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend WITH trade; just touched lower band  •  ONLY when RSI 20-30 oversold

### L12.  `H60=H60e AND T4=T4a AND BBP=BBP1 AND ZS=ZS1`
- Raw: n=121  W=48/L=73  WR=39.7%
- Sharpen: sharpest is RSI=RSI1 (20/73 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; just touched lower band; zscore -3 to -2 deep oversold  •  ONLY when RSI 20-30 oversold

### L13.  `H60=H60e AND T4=T4a AND BBP=BBP1 AND direction_exec=short`
- Raw: n=121  W=48/L=73  WR=39.7%
- Sharpen: sharpest is RSI=RSI1 (20/73 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend WITH trade; just touched lower band  •  ONLY when RSI 20-30 oversold

### L14.  `T1=T1a AND T4=T4a AND BBP=BBP1 AND ZS=ZS1`
- Raw: n=121  W=48/L=73  WR=39.7%
- Sharpen: sharpest is RSI=RSI1 (20/73 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; just touched lower band; zscore -3 to -2 deep oversold  •  ONLY when RSI 20-30 oversold

### L15.  `T1=T1a AND T4=T4a AND BBP=BBP1 AND direction_exec=short`
- Raw: n=121  W=48/L=73  WR=39.7%
- Sharpen: sharpest is RSI=RSI1 (20/73 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend WITH trade; just touched lower band  •  ONLY when RSI 20-30 oversold

### L16.  `T4=T4a AND BBP=BBP1 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=121  W=48/L=73  WR=39.7%
- Sharpen: sharpest is RSI=RSI1 (20/73 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: SHORT**  •  4h trend WITH trade; just touched lower band; zscore -3 to -2 deep oversold  •  ONLY when RSI 20-30 oversold

### L17.  `T4=T4a AND RSI=RSI2 AND ZS=ZS2`
- Raw: n=113  W=37/L=76  WR=32.7%
- Sharpen: sharpest is H20=H20a (15/76 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: ?**  •  4h trend WITH trade; RSI 30-40 weak; zscore -2 to -1 oversold  •  ONLY when HTF20 aligned WITH trade

### L18.  `T4=T4a AND BBP=BBP2 AND RSI=RSI2 AND ZS=ZS2`
- Raw: n=113  W=37/L=76  WR=32.7%
- Sharpen: sharpest is H20=H20a (15/76 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: ?**  •  4h trend WITH trade; lower third; RSI 30-40 weak; zscore -2 to -1 oversold  •  ONLY when HTF20 aligned WITH trade

### L19.  `H20=H20e AND T4=T4a AND RSI=RSI2 AND ZS=ZS2`
- Raw: n=98  W=37/L=61  WR=37.8%
- Sharpen: sharpest is session_bucket=ny_mid (12/61 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; RSI 30-40 weak; zscore -2 to -1 oversold  •  ONLY when session=ny_mid

### L20.  `H60=H60e AND T4=T4a AND RSI=RSI2 AND ZS=ZS2`
- Raw: n=98  W=37/L=61  WR=37.8%
- Sharpen: sharpest is session_bucket=ny_mid (12/61 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; RSI 30-40 weak; zscore -2 to -1 oversold  •  ONLY when session=ny_mid

### L21.  `T1=T1a AND T4=T4a AND RSI=RSI2 AND ZS=ZS2`
- Raw: n=98  W=37/L=61  WR=37.8%
- Sharpen: sharpest is session_bucket=ny_mid (12/61 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 30-40 weak; zscore -2 to -1 oversold  •  ONLY when session=ny_mid

### L22.  `T4=T4a AND RSI=RSI2 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=98  W=37/L=61  WR=37.8%
- Sharpen: sharpest is session_bucket=ny_mid (12/61 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 30-40 weak; zscore -2 to -1 oversold  •  ONLY when session=ny_mid

### L23.  `T4=T4a AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=88  W=35/L=53  WR=39.8%
- Sharpen: sharpest is H20=H20a (20/53 of losers there)
- **Sharp: n=24  W=4/L=20  WR=16.7%**
- **Dir: ?**  •  4h trend WITH trade; zscore -3 to -2 deep oversold; session=asia  •  ONLY when HTF20 aligned WITH trade

### L24.  `H20=H20a AND T4=T4a AND RSI=RSI2`
- Raw: n=87  W=34/L=53  WR=39.1%
- Sharpen: sharpest is BBP=BBP2 (18/53 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 30-40 weak  •  ONLY when lower third

### L25.  `H60=H60a AND T4=T4a AND RSI=RSI2`
- Raw: n=87  W=34/L=53  WR=39.1%
- Sharpen: sharpest is BBP=BBP2 (18/53 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 30-40 weak  •  ONLY when lower third

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | — |
| T1 | — | — |
| T4 | T4c(55/46) | T4a(45/54) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
