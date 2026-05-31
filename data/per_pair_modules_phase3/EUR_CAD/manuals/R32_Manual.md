# EUR_CAD — R32 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR3**  (60-90%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **2,334**  (W=1,425 / L=909)  -  WR: **61.1%**

## Session distribution

- ny_mid: n=906  W=564/L=342  WR=62.3%
- london: n=322  W=188/L=134  WR=58.4%
- ny_close: n=313  W=197/L=116  WR=62.9%
- london_open: n=295  W=173/L=122  WR=58.6%
- ny_open: n=276  W=168/L=108  WR=60.9%
- asia: n=154  W=93/L=61  WR=60.4%
- off_hours: n=56  W=34/L=22  WR=60.7%
- asia_late: n=12  W=8/L=4  WR=66.7%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1c AND direction_exec=long AND session_bucket=asia`
- Raw: n=82  W=72/L=10  WR=87.8%
- Refine: exclude T4=T4a drops 7/10 losers (70%)
- **Final: n=64  W=61/L=3  WR=95.3%**
- **Dir: LONG**  •  1h trend AGAINST trade; session=asia  •  AVOID when 4h trend WITH trade

### W02.  `H20=H20e AND H60=H60e AND T4=T4c AND ZS=ZS1`
- Raw: n=82  W=72/L=10  WR=87.8%
- Refine: exclude RSI=RSI3 drops 8/10 losers (80%)
- **Final: n=68  W=66/L=2  WR=97.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  AVOID when RSI 40-50 lower neutral

### W03.  `H20=H20e AND T4=T4c AND ZS=ZS1 AND direction_exec=long`
- Raw: n=82  W=72/L=10  WR=87.8%
- Refine: exclude RSI=RSI3 drops 8/10 losers (80%)
- **Final: n=68  W=66/L=2  WR=97.1%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  AVOID when RSI 40-50 lower neutral

### W04.  `H20=H20e AND T1=T1c AND T4=T4c AND ZS=ZS1`
- Raw: n=72  W=62/L=10  WR=86.1%
- Refine: exclude RSI=RSI3 drops 8/10 losers (80%)
- **Final: n=58  W=56/L=2  WR=96.6%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  AVOID when RSI 40-50 lower neutral

### W05.  `H60=H60e AND direction_exec=long AND session_bucket=asia`
- Raw: n=70  W=64/L=6  WR=91.4%
- Refine: exclude ZS=ZS3 drops 4/6 losers (67%)
- **Final: n=44  W=42/L=2  WR=95.5%**
- **Dir: LONG**  •  HTF60 strongly against; session=asia  •  AVOID when zscore -1 to +1 neutral

### W06.  `T4=T4c AND direction_exec=long AND session_bucket=asia`
- Raw: n=67  W=63/L=4  WR=94.0%
- Refine: exclude ZS=ZS3 drops 3/4 losers (75%)
- **Final: n=42  W=41/L=1  WR=97.6%**
- **Dir: LONG**  •  4h trend AGAINST trade; session=asia  •  AVOID when zscore -1 to +1 neutral

### W07.  `H60=H60e AND T1=T1c AND session_bucket=asia`
- Raw: n=67  W=62/L=5  WR=92.5%
- Refine: exclude H20=H20a drops 2/5 losers (40%)
- **Final: n=64  W=61/L=3  WR=95.3%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; session=asia  •  AVOID when HTF20 aligned WITH trade

### W08.  `H60=H60e AND T1=T1c AND direction_exec=long AND session_bucket=asia`
- Raw: n=67  W=62/L=5  WR=92.5%
- Refine: exclude H20=H20a drops 2/5 losers (40%)
- **Final: n=64  W=61/L=3  WR=95.3%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend AGAINST trade; session=asia  •  AVOID when HTF20 aligned WITH trade

### W09.  `H60=H60a AND T4=T4a AND BBP=BBP3 AND session_bucket=ny_mid`
- Raw: n=67  W=57/L=10  WR=85.1%
- Refine: exclude RSI=RSI3 drops 6/10 losers (60%)
- **Final: n=43  W=39/L=4  WR=90.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; middle of band; session=ny_mid  •  AVOID when RSI 40-50 lower neutral

### W10.  `T1=T1c AND T4=T4c AND session_bucket=asia`
- Raw: n=64  W=61/L=3  WR=95.3%
- Refine: exclude ZS=ZS3 drops 2/3 losers (67%)
- **Final: n=42  W=41/L=1  WR=97.6%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=asia  •  AVOID when zscore -1 to +1 neutral

### W11.  `T1=T1c AND T4=T4c AND direction_exec=long AND session_bucket=asia`
- Raw: n=64  W=61/L=3  WR=95.3%
- Refine: exclude ZS=ZS3 drops 2/3 losers (67%)
- **Final: n=42  W=41/L=1  WR=97.6%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=asia  •  AVOID when zscore -1 to +1 neutral

### W12.  `H60=H60e AND T4=T4c AND session_bucket=asia`
- Raw: n=63  W=59/L=4  WR=93.7%
- Refine: exclude ZS=ZS3 drops 3/4 losers (75%)
- **Final: n=42  W=41/L=1  WR=97.6%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; session=asia  •  AVOID when zscore -1 to +1 neutral

### W13.  `H60=H60e AND T4=T4c AND direction_exec=long AND session_bucket=asia`
- Raw: n=63  W=59/L=4  WR=93.7%
- Refine: exclude ZS=ZS3 drops 3/4 losers (75%)
- **Final: n=42  W=41/L=1  WR=97.6%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend AGAINST trade; session=asia  •  AVOID when zscore -1 to +1 neutral

### W14.  `H20=H20e AND T4=T4c AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=62  W=56/L=6  WR=90.3%
- Refine: exclude session_bucket=london drops 6/6 losers (100%)
- **Final: n=47  W=47/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  AVOID when session=london

### W15.  `H60=H60e AND T1=T1c AND T4=T4c AND session_bucket=asia`
- Raw: n=60  W=57/L=3  WR=95.0%
- Refine: exclude ZS=ZS3 drops 2/3 losers (67%)
- **Final: n=42  W=41/L=1  WR=97.6%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; session=asia  •  AVOID when zscore -1 to +1 neutral

### W16.  `T1=T1a AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=60  W=55/L=5  WR=91.7%
- Refine: exclude session_bucket=london_open drops 3/5 losers (60%)
- **Final: n=57  W=55/L=2  WR=96.5%**
- **Dir: ?**  •  1h trend WITH trade; just touched upper band; zscore +2 to +3 deep overbought  •  AVOID when session=london_open

### W17.  `H20=H20d AND H60=H60e AND BBP=BBP2`
- Raw: n=56  W=50/L=6  WR=89.3%
- Refine: exclude RSI=RSI2 drops 6/6 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 strongly against; lower third  •  AVOID when RSI 30-40 weak

### W18.  `H20=H20d AND BBP=BBP2 AND direction_exec=long`
- Raw: n=56  W=50/L=6  WR=89.3%
- Refine: exclude RSI=RSI2 drops 6/6 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 mildly against; lower third  •  AVOID when RSI 30-40 weak

### W19.  `H20=H20d AND H60=H60e AND T4=T4c AND BBP=BBP2`
- Raw: n=56  W=50/L=6  WR=89.3%
- Refine: exclude RSI=RSI2 drops 6/6 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 strongly against; 4h trend AGAINST trade; lower third  •  AVOID when RSI 30-40 weak

### W20.  `H20=H20d AND H60=H60e AND BBP=BBP2 AND direction_exec=long`
- Raw: n=56  W=50/L=6  WR=89.3%
- Refine: exclude RSI=RSI2 drops 6/6 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 mildly against; HTF60 strongly against; lower third  •  AVOID when RSI 30-40 weak

### W21.  `H20=H20d AND T4=T4c AND BBP=BBP2 AND direction_exec=long`
- Raw: n=56  W=50/L=6  WR=89.3%
- Refine: exclude RSI=RSI2 drops 6/6 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 mildly against; 4h trend AGAINST trade; lower third  •  AVOID when RSI 30-40 weak

### W22.  `H20=H20a AND T4=T4a AND ZS=ZS3 AND session_bucket=ny_mid`
- Raw: n=55  W=47/L=8  WR=85.5%
- Refine: exclude RSI=RSI4 drops 3/8 losers (38%)
- **Final: n=48  W=43/L=5  WR=89.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; zscore -1 to +1 neutral; session=ny_mid  •  AVOID when RSI 50-60 upper neutral

### W23.  `H20=H20e AND H60=H60e AND session_bucket=asia`
- Raw: n=54  W=51/L=3  WR=94.4%
- Refine: exclude ZS=ZS3 drops 2/3 losers (67%)
- **Final: n=34  W=33/L=1  WR=97.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; session=asia  •  AVOID when zscore -1 to +1 neutral

### W24.  `H20=H20e AND T1=T1c AND session_bucket=asia`
- Raw: n=54  W=51/L=3  WR=94.4%
- Refine: exclude ZS=ZS3 drops 2/3 losers (67%)
- **Final: n=34  W=33/L=1  WR=97.1%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; session=asia  •  AVOID when zscore -1 to +1 neutral

### W25.  `H20=H20e AND T4=T4c AND session_bucket=asia`
- Raw: n=54  W=51/L=3  WR=94.4%
- Refine: exclude ZS=ZS3 drops 2/3 losers (67%)
- **Final: n=36  W=35/L=1  WR=97.2%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; session=asia  •  AVOID when zscore -1 to +1 neutral

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20a AND H60=H60a AND T4=T4a AND ZS=ZS2`
- Raw: n=140  W=53/L=87  WR=37.9%
- Sharpen: sharpest is RSI=RSI3 (26/87 of losers there)
- **Sharp: n=33  W=7/L=26  WR=21.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade; zscore -2 to -1 oversold  •  ONLY when RSI 40-50 lower neutral

### L02.  `H20=H20a AND T4=T4a AND ZS=ZS2 AND direction_exec=short`
- Raw: n=140  W=53/L=87  WR=37.9%
- Sharpen: sharpest is RSI=RSI3 (26/87 of losers there)
- **Sharp: n=33  W=7/L=26  WR=21.2%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend WITH trade; zscore -2 to -1 oversold  •  ONLY when RSI 40-50 lower neutral

### L03.  `H20=H20a AND T1=T1a AND T4=T4a AND ZS=ZS2`
- Raw: n=129  W=49/L=80  WR=38.0%
- Sharpen: sharpest is RSI=RSI3 (26/80 of losers there)
- **Sharp: n=33  W=7/L=26  WR=21.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; zscore -2 to -1 oversold  •  ONLY when RSI 40-50 lower neutral

### L04.  `T1=T1a AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=103  W=40/L=63  WR=38.8%
- Sharpen: sharpest is session_bucket=asia (19/63 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; lower third; RSI 40-50 lower neutral  •  ONLY when session=asia

### L05.  `T1=T1a AND BBP=BBP2 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=83  W=30/L=53  WR=36.1%
- Sharpen: sharpest is session_bucket=asia (19/53 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: SHORT**  •  1h trend WITH trade; lower third; RSI 40-50 lower neutral  •  ONLY when session=asia

### L06.  `H60=H60c AND T1=T1c AND direction_exec=long`
- Raw: n=82  W=29/L=53  WR=35.4%
- Sharpen: sharpest is RSI=RSI1 (10/53 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: LONG**  •  HTF60 neutral; 1h trend AGAINST trade  •  ONLY when RSI 20-30 oversold

### L07.  `T1=T1a AND T4=T4a AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=80  W=30/L=50  WR=37.5%
- Sharpen: sharpest is session_bucket=asia (19/50 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; lower third; RSI 40-50 lower neutral  •  ONLY when session=asia

### L08.  `T4=T4a AND BBP=BBP1 AND RSI=RSI2`
- Raw: n=78  W=28/L=50  WR=35.9%
- Sharpen: sharpest is H20=H20a (28/50 of losers there)
- **Sharp: n=32  W=4/L=28  WR=12.5%**
- **Dir: ?**  •  4h trend WITH trade; just touched lower band; RSI 30-40 weak  •  ONLY when HTF20 aligned WITH trade

### L09.  `T4=T4a AND BBP=BBP1 AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=78  W=28/L=50  WR=35.9%
- Sharpen: sharpest is H20=H20a (28/50 of losers there)
- **Sharp: n=32  W=4/L=28  WR=12.5%**
- **Dir: ?**  •  4h trend WITH trade; just touched lower band; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when HTF20 aligned WITH trade

### L10.  `T1=T1a AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=76  W=27/L=49  WR=35.5%
- Sharpen: sharpest is H20=H20a (29/49 of losers there)
- **Sharp: n=36  W=7/L=29  WR=19.4%**
- **Dir: ?**  •  1h trend WITH trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  ONLY when HTF20 aligned WITH trade

### L11.  `T1=T1a AND BBP=BBP2 AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=76  W=27/L=49  WR=35.5%
- Sharpen: sharpest is H20=H20a (29/49 of losers there)
- **Sharp: n=36  W=7/L=29  WR=19.4%**
- **Dir: ?**  •  1h trend WITH trade; lower third; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  ONLY when HTF20 aligned WITH trade

### L12.  `T1=T1a AND direction_exec=short AND session_bucket=asia`
- Raw: n=69  W=19/L=50  WR=27.5%
- Sharpen: sharpest is T4=T4a (42/50 of losers there)
- **Sharp: n=47  W=5/L=42  WR=10.6%**
- **Dir: SHORT**  •  1h trend WITH trade; session=asia  •  ONLY when 4h trend WITH trade

### L13.  `H20=H20a AND T4=T4a AND ZS=ZS1`
- Raw: n=65  W=24/L=41  WR=36.9%
- Sharpen: sharpest is RSI=RSI2 (35/41 of losers there)
- **Sharp: n=45  W=10/L=35  WR=22.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  ONLY when RSI 30-40 weak

### L14.  `T1=T1a AND T4=T4a AND session_bucket=london_open`
- Raw: n=64  W=21/L=43  WR=32.8%
- Sharpen: sharpest is ZS=ZS1 (11/43 of losers there)
- **Sharp: n=13  W=2/L=11  WR=15.4%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; session=london_open  •  ONLY when zscore -3 to -2 deep oversold

### L15.  `T4=T4a AND direction_exec=short AND session_bucket=london_open`
- Raw: n=64  W=21/L=43  WR=32.8%
- Sharpen: sharpest is ZS=ZS1 (11/43 of losers there)
- **Sharp: n=13  W=2/L=11  WR=15.4%**
- **Dir: SHORT**  •  4h trend WITH trade; session=london_open  •  ONLY when zscore -3 to -2 deep oversold

### L16.  `T1=T1a AND T4=T4a AND direction_exec=short AND session_bucket=london_open`
- Raw: n=64  W=21/L=43  WR=32.8%
- Sharpen: sharpest is ZS=ZS1 (11/43 of losers there)
- **Sharp: n=13  W=2/L=11  WR=15.4%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend WITH trade; session=london_open  •  ONLY when zscore -3 to -2 deep oversold

### L17.  `H20=H20a AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=61  W=17/L=44  WR=27.9%
- Sharpen: sharpest is session_bucket=asia (19/44 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; lower third; RSI 40-50 lower neutral  •  ONLY when session=asia

### L18.  `T1=T1a AND RSI=RSI3 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=61  W=21/L=40  WR=34.4%
- Sharpen: sharpest is H20=H20a (29/40 of losers there)
- **Sharp: n=36  W=7/L=29  WR=19.4%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  ONLY when HTF20 aligned WITH trade

### L19.  `T1=T1a AND T4=T4a AND BBP=BBP1 AND RSI=RSI2`
- Raw: n=61  W=22/L=39  WR=36.1%
- Sharpen: sharpest is H20=H20a (24/39 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; just touched lower band; RSI 30-40 weak  •  ONLY when HTF20 aligned WITH trade

### L20.  `T4=T4a AND BBP=BBP1 AND RSI=RSI2 AND direction_exec=short`
- Raw: n=61  W=22/L=39  WR=36.1%
- Sharpen: sharpest is H20=H20a (24/39 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: SHORT**  •  4h trend WITH trade; just touched lower band; RSI 30-40 weak  •  ONLY when HTF20 aligned WITH trade

### L21.  `T1=T1a AND T4=T4a AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=58  W=21/L=37  WR=36.2%
- Sharpen: sharpest is H20=H20a (26/37 of losers there)
- **Sharp: n=33  W=7/L=26  WR=21.2%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  ONLY when HTF20 aligned WITH trade

### L22.  `H60=H60a AND T1=T1a AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=54  W=21/L=33  WR=38.9%
- Sharpen: sharpest is H20=H20a (29/33 of losers there)
- **Sharp: n=36  W=7/L=29  WR=19.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  ONLY when HTF20 aligned WITH trade

### L23.  `H60=H60a AND T1=T1a AND session_bucket=asia`
- Raw: n=52  W=9/L=43  WR=17.3%
- Sharpen: sharpest is T4=T4a (41/43 of losers there)
- **Sharp: n=46  W=5/L=41  WR=10.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=asia  •  ONLY when 4h trend WITH trade

### L24.  `H60=H60a AND direction_exec=short AND session_bucket=asia`
- Raw: n=52  W=9/L=43  WR=17.3%
- Sharpen: sharpest is T4=T4a (41/43 of losers there)
- **Sharp: n=46  W=5/L=41  WR=10.9%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; session=asia  •  ONLY when 4h trend WITH trade

### L25.  `H60=H60a AND T1=T1a AND direction_exec=short AND session_bucket=asia`
- Raw: n=52  W=9/L=43  WR=17.3%
- Sharpen: sharpest is T4=T4a (41/43 of losers there)
- **Sharp: n=46  W=5/L=41  WR=10.9%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=asia  •  ONLY when 4h trend WITH trade

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20e(38/25) | H20a(26/38) |
| H60 | H60e(45/35) | H60a(36/45) |
| T1 | — | — |
| T4 | T4c(54/45) | T4a(46/55) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(53/46) | short(47/54) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
