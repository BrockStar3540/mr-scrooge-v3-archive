# NZD_CAD — R21 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **3,250**  (W=2,154 / L=1,096)  -  WR: **66.3%**

## Session distribution

- asia: n=876  W=573/L=303  WR=65.4%
- ny_mid: n=852  W=560/L=292  WR=65.7%
- london_open: n=539  W=362/L=177  WR=67.2%
- ny_open: n=396  W=252/L=144  WR=63.6%
- london: n=259  W=187/L=72  WR=72.2%
- ny_close: n=192  W=127/L=65  WR=66.1%
- off_hours: n=70  W=42/L=28  WR=60.0%
- asia_late: n=66  W=51/L=15  WR=77.3%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND T1=T1a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=215  W=188/L=27  WR=87.4%
- Refine: exclude H60=H60a drops 25/27 losers (93%)
- **Final: n=154  W=152/L=2  WR=98.7%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when HTF60 aligned WITH trade

### W02.  `T1=T1a AND RSI=RSI4 AND session_bucket=london_open`
- Raw: n=178  W=153/L=25  WR=86.0%
- Refine: exclude BBP=BBP4 drops 14/25 losers (56%)
- **Final: n=110  W=99/L=11  WR=90.0%**
- **Dir: ?**  •  1h trend WITH trade; RSI 50-60 upper neutral; session=london_open  •  AVOID when upper third

### W03.  `H20=H20a AND H60=H60c AND T1=T1a`
- Raw: n=171  W=150/L=21  WR=87.7%
- Refine: exclude RSI=RSI4 drops 18/21 losers (86%)
- **Final: n=125  W=122/L=3  WR=97.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 neutral; 1h trend WITH trade  •  AVOID when RSI 50-60 upper neutral

### W04.  `H20=H20a AND T1=T1a AND BBP=BBP2`
- Raw: n=160  W=140/L=20  WR=87.5%
- Refine: exclude H60=H60a drops 14/20 losers (70%)
- **Final: n=106  W=100/L=6  WR=94.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; lower third  •  AVOID when HTF60 aligned WITH trade

### W05.  `T4=T4a AND RSI=RSI4 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=144  W=126/L=18  WR=87.5%
- Refine: exclude H20=H20b drops 8/18 losers (44%)
- **Final: n=136  W=126/L=10  WR=92.6%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 50-60 upper neutral; session=ny_mid  •  AVOID when HTF20 slightly aligned

### W06.  `H20=H20a AND T1=T1a AND T4=T4c AND RSI=RSI3`
- Raw: n=138  W=121/L=17  WR=87.7%
- Refine: exclude session_bucket=london_open drops 7/17 losers (41%)
- **Final: n=131  W=121/L=10  WR=92.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when session=london_open

### W07.  `RSI=RSI3 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=132  W=114/L=18  WR=86.4%
- Refine: exclude H60=H60e drops 16/18 losers (89%)
- **Final: n=46  W=44/L=2  WR=95.7%**
- **Dir: SHORT**  •  RSI 40-50 lower neutral; session=london_open  •  AVOID when HTF60 strongly against

### W08.  `H20=H20a AND T4=T4a AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=127  W=113/L=14  WR=89.0%
- Refine: exclude BBP=BBP3 drops 6/14 losers (43%)
- **Final: n=111  W=103/L=8  WR=92.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral; session=ny_mid  •  AVOID when middle of band

### W09.  `H20=H20a AND T1=T1a AND ZS=ZS2`
- Raw: n=127  W=108/L=19  WR=85.0%
- Refine: exclude T4=T4c drops 12/19 losers (63%)
- **Final: n=96  W=89/L=7  WR=92.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; zscore -2 to -1 oversold  •  AVOID when 4h trend AGAINST trade

### W10.  `H20=H20a AND T1=T1a AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=127  W=108/L=19  WR=85.0%
- Refine: exclude T4=T4c drops 12/19 losers (63%)
- **Final: n=96  W=89/L=7  WR=92.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; lower third; zscore -2 to -1 oversold  •  AVOID when 4h trend AGAINST trade

### W11.  `H20=H20e AND T1=T1a AND T4=T4c AND session_bucket=london_open`
- Raw: n=125  W=107/L=18  WR=85.6%
- Refine: exclude RSI=RSI3 drops 12/18 losers (67%)
- **Final: n=88  W=82/L=6  WR=93.2%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; session=london_open  •  AVOID when RSI 40-50 lower neutral

### W12.  `H60=H60c AND T1=T1a AND direction_exec=short`
- Raw: n=124  W=106/L=18  WR=85.5%
- Refine: exclude RSI=RSI4 drops 18/18 losers (100%)
- **Final: n=78  W=78/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 neutral; 1h trend WITH trade  •  AVOID when RSI 50-60 upper neutral

### W13.  `H20=H20a AND H60=H60c AND T1=T1a AND direction_exec=short`
- Raw: n=124  W=106/L=18  WR=85.5%
- Refine: exclude RSI=RSI4 drops 18/18 losers (100%)
- **Final: n=78  W=78/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 neutral; 1h trend WITH trade  •  AVOID when RSI 50-60 upper neutral

### W14.  `H20=H20a AND T4=T4c AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=121  W=105/L=16  WR=86.8%
- Refine: exclude T1=T1c drops 12/16 losers (75%)
- **Final: n=69  W=65/L=4  WR=94.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral; session=asia  •  AVOID when 1h trend AGAINST trade

### W15.  `H20=H20c AND RSI=RSI3 AND direction_exec=short`
- Raw: n=117  W=100/L=17  WR=85.5%
- Refine: exclude ZS=ZS2 drops 10/17 losers (59%)
- **Final: n=84  W=77/L=7  WR=91.7%**
- **Dir: SHORT**  •  HTF20 neutral; RSI 40-50 lower neutral  •  AVOID when zscore -2 to -1 oversold

### W16.  `H20=H20a AND T1=T1a AND T4=T4a AND session_bucket=london_open`
- Raw: n=116  W=105/L=11  WR=90.5%
- Refine: exclude BBP=BBP4 drops 8/11 losers (73%)
- **Final: n=80  W=77/L=3  WR=96.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; session=london_open  •  AVOID when upper third

### W17.  `H20=H20a AND T1=T1a AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=116  W=104/L=12  WR=89.7%
- Refine: exclude H60=H60a drops 9/12 losers (75%)
- **Final: n=83  W=80/L=3  WR=96.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; lower third; RSI 40-50 lower neutral  •  AVOID when HTF60 aligned WITH trade

### W18.  `H20=H20a AND T1=T1a AND T4=T4a AND BBP=BBP2`
- Raw: n=115  W=107/L=8  WR=93.0%
- Refine: exclude H60=H60a drops 5/8 losers (62%)
- **Final: n=83  W=80/L=3  WR=96.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; lower third  •  AVOID when HTF60 aligned WITH trade

### W19.  `H20=H20e AND BBP=BBP5 AND RSI=RSI4`
- Raw: n=113  W=97/L=16  WR=85.8%
- Refine: exclude T4=T4c drops 15/16 losers (94%)
- **Final: n=39  W=38/L=1  WR=97.4%**
- **Dir: ?**  •  HTF20 strongly against; just touched upper band; RSI 50-60 upper neutral  •  AVOID when 4h trend AGAINST trade

### W20.  `H20=H20e AND BBP=BBP5 AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=113  W=97/L=16  WR=85.8%
- Refine: exclude T4=T4c drops 15/16 losers (94%)
- **Final: n=39  W=38/L=1  WR=97.4%**
- **Dir: ?**  •  HTF20 strongly against; just touched upper band; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when 4h trend AGAINST trade

### W21.  `H20=H20a AND BBP=BBP2 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=110  W=94/L=16  WR=85.5%
- Refine: exclude H60=H60a drops 12/16 losers (75%)
- **Final: n=81  W=77/L=4  WR=95.1%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; lower third; RSI 40-50 lower neutral  •  AVOID when HTF60 aligned WITH trade

### W22.  `T4=T4c AND BBP=BBP4 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=105  W=91/L=14  WR=86.7%
- Refine: exclude session_bucket=ny_open drops 7/14 losers (50%)
- **Final: n=92  W=85/L=7  WR=92.4%**
- **Dir: SHORT**  •  4h trend AGAINST trade; upper third; RSI 40-50 lower neutral  •  AVOID when session=ny_open

### W23.  `H20=H20a AND T4=T4a AND BBP=BBP2 AND direction_exec=short`
- Raw: n=103  W=88/L=15  WR=85.4%
- Refine: exclude session_bucket=asia drops 11/15 losers (73%)
- **Final: n=70  W=66/L=4  WR=94.3%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend WITH trade; lower third  •  AVOID when session=asia

### W24.  `H20=H20e AND H60=H60e AND T4=T4c AND session_bucket=london_open`
- Raw: n=102  W=88/L=14  WR=86.3%
- Refine: exclude T1=T1c drops 6/14 losers (43%)
- **Final: n=95  W=87/L=8  WR=91.6%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; session=london_open  •  AVOID when 1h trend AGAINST trade

### W25.  `H20=H20a AND T4=T4c AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=102  W=88/L=14  WR=86.3%
- Refine: exclude ZS=ZS2 drops 14/14 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; lower third; RSI 40-50 lower neutral  •  AVOID when zscore -2 to -1 oversold

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND T1=T1c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=134  W=53/L=81  WR=39.6%
- Sharpen: sharpest is H60=H60c (26/81 of losers there)
- **Sharp: n=26  W=0/L=26  WR=0.0%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when HTF60 neutral

### L02.  `T1=T1c AND RSI=RSI4 AND session_bucket=london_open`
- Raw: n=124  W=48/L=76  WR=38.7%
- Sharpen: sharpest is direction_exec=short (42/76 of losers there)
- **Sharp: n=55  W=13/L=42  WR=23.6%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; session=london_open  •  ONLY when short

### L03.  `H20=H20e AND H60=H60a AND ZS=ZS3`
- Raw: n=120  W=42/L=78  WR=35.0%
- Sharpen: sharpest is session_bucket=asia (25/78 of losers there)
- **Sharp: n=31  W=6/L=25  WR=19.4%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; zscore -1 to +1 neutral  •  ONLY when session=asia

### L04.  `H20=H20e AND T4=T4c AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=110  W=44/L=66  WR=40.0%
- Sharpen: sharpest is RSI=RSI4 (41/66 of losers there)
- **Sharp: n=55  W=14/L=41  WR=25.5%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade; session=ny_mid  •  ONLY when RSI 50-60 upper neutral

### L05.  `T4=T4c AND RSI=RSI4 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=95  W=36/L=59  WR=37.9%
- Sharpen: sharpest is H20=H20e (41/59 of losers there)
- **Sharp: n=55  W=14/L=41  WR=25.5%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 50-60 upper neutral; session=ny_mid  •  ONLY when HTF20 strongly against

### L06.  `H20=H20e AND H60=H60a AND ZS=ZS3 AND direction_exec=short`
- Raw: n=90  W=32/L=58  WR=35.6%
- Sharpen: sharpest is session_bucket=asia (19/58 of losers there)
- **Sharp: n=23  W=4/L=19  WR=17.4%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 aligned WITH trade; zscore -1 to +1 neutral  •  ONLY when session=asia

### L07.  `H20=H20e AND T4=T4a AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=84  W=33/L=51  WR=39.3%
- Sharpen: sharpest is ZS=ZS3 (24/51 of losers there)
- **Sharp: n=26  W=2/L=24  WR=7.7%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; RSI 40-50 lower neutral; session=asia  •  ONLY when zscore -1 to +1 neutral

### L08.  `H20=H20e AND T1=T1c AND T4=T4c AND session_bucket=london_open`
- Raw: n=83  W=31/L=52  WR=37.3%
- Sharpen: sharpest is direction_exec=short (20/52 of losers there)
- **Sharp: n=23  W=3/L=20  WR=13.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; session=london_open  •  ONLY when short

### L09.  `H20=H20e AND T4=T4a AND RSI=RSI3 AND ZS=ZS3`
- Raw: n=80  W=28/L=52  WR=35.0%
- Sharpen: sharpest is session_bucket=asia (24/52 of losers there)
- **Sharp: n=26  W=2/L=24  WR=7.7%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; RSI 40-50 lower neutral; zscore -1 to +1 neutral  •  ONLY when session=asia

### L10.  `H20=H20e AND H60=H60a AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=76  W=29/L=47  WR=38.2%
- Sharpen: sharpest is T1=T1c (23/47 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 4h trend AGAINST trade; session=ny_mid  •  ONLY when 1h trend AGAINST trade

### L11.  `H20=H20e AND T1=T1c AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=74  W=27/L=47  WR=36.5%
- Sharpen: sharpest is H60=H60a (23/47 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_mid  •  ONLY when HTF60 aligned WITH trade

### L12.  `H20=H20e AND T4=T4c AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=73  W=21/L=52  WR=28.8%
- Sharpen: sharpest is T1=T1c (25/52 of losers there)
- **Sharp: n=30  W=5/L=25  WR=16.7%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 50-60 upper neutral; session=ny_mid  •  ONLY when 1h trend AGAINST trade

### L13.  `H20=H20e AND T4=T4a AND BBP=BBP2 AND direction_exec=short`
- Raw: n=71  W=26/L=45  WR=36.6%
- Sharpen: sharpest is ZS=ZS3 (24/45 of losers there)
- **Sharp: n=28  W=4/L=24  WR=14.3%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend WITH trade; lower third  •  ONLY when zscore -1 to +1 neutral

### L14.  `H20=H20e AND H60=H60a AND T1=T1c AND RSI=RSI3`
- Raw: n=71  W=27/L=44  WR=38.0%
- Sharpen: sharpest is direction_exec=long (29/44 of losers there)
- **Sharp: n=37  W=8/L=29  WR=21.6%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when long

### L15.  `H20=H20e AND T1=T1c AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=71  W=28/L=43  WR=39.4%
- Sharpen: sharpest is H60=H60c (18/43 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; lower third; RSI 40-50 lower neutral  •  ONLY when HTF60 neutral

### L16.  `H60=H60e AND T1=T1a AND T4=T4a AND ZS=ZS4`
- Raw: n=71  W=28/L=43  WR=39.4%
- Sharpen: sharpest is session_bucket=ny_open (23/43 of losers there)
- **Sharp: n=25  W=2/L=23  WR=8.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend WITH trade; zscore +1 to +2 overbought  •  ONLY when session=ny_open

### L17.  `T1=T1a AND RSI=RSI4 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=71  W=28/L=43  WR=39.4%
- Sharpen: sharpest is H60=H60e (14/43 of losers there)
- **Sharp: n=15  W=1/L=14  WR=6.7%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 50-60 upper neutral; session=ny_mid  •  ONLY when HTF60 strongly against

### L18.  `H20=H20e AND BBP=BBP2 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=70  W=27/L=43  WR=38.6%
- Sharpen: sharpest is T4=T4c (37/43 of losers there)
- **Sharp: n=49  W=12/L=37  WR=24.5%**
- **Dir: LONG**  •  HTF20 strongly against; lower third; RSI 40-50 lower neutral  •  ONLY when 4h trend AGAINST trade

### L19.  `H20=H20e AND H60=H60a AND RSI=RSI3 AND ZS=ZS3`
- Raw: n=68  W=21/L=47  WR=30.9%
- Sharpen: sharpest is session_bucket=asia (18/47 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; RSI 40-50 lower neutral; zscore -1 to +1 neutral  •  ONLY when session=asia

### L20.  `H60=H60e AND BBP=BBP4 AND session_bucket=ny_open`
- Raw: n=67  W=25/L=42  WR=37.3%
- Sharpen: sharpest is T4=T4a (29/42 of losers there)
- **Sharp: n=31  W=2/L=29  WR=6.5%**
- **Dir: ?**  •  HTF60 strongly against; upper third; session=ny_open  •  ONLY when 4h trend WITH trade

### L21.  `H20=H20e AND BBP=BBP2 AND ZS=ZS3`
- Raw: n=66  W=23/L=43  WR=34.8%
- Sharpen: sharpest is T4=T4a (26/43 of losers there)
- **Sharp: n=31  W=5/L=26  WR=16.1%**
- **Dir: ?**  •  HTF20 strongly against; lower third; zscore -1 to +1 neutral  •  ONLY when 4h trend WITH trade

### L22.  `T4=T4c AND RSI=RSI3 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=66  W=23/L=43  WR=34.8%
- Sharpen: sharpest is ZS=ZS2 (21/43 of losers there)
- **Sharp: n=22  W=1/L=21  WR=4.5%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; session=london_open  •  ONLY when zscore -2 to -1 oversold

### L23.  `T1=T1a AND BBP=BBP4 AND session_bucket=ny_open`
- Raw: n=66  W=24/L=42  WR=36.4%
- Sharpen: sharpest is H60=H60e (32/42 of losers there)
- **Sharp: n=38  W=6/L=32  WR=15.8%**
- **Dir: ?**  •  1h trend WITH trade; upper third; session=ny_open  •  ONLY when HTF60 strongly against

### L24.  `H60=H60e AND RSI=RSI4 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=66  W=24/L=42  WR=36.4%
- Sharpen: sharpest is ZS=ZS5 (23/42 of losers there)
- **Sharp: n=29  W=6/L=23  WR=20.7%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 50-60 upper neutral; session=ny_mid  •  ONLY when zscore +2 to +3 deep overbought

### L25.  `H20=H20e AND ZS=ZS3 AND direction_exec=short AND session_bucket=asia`
- Raw: n=66  W=26/L=40  WR=39.4%
- Sharpen: sharpest is T4=T4a (17/40 of losers there)
- **Sharp: n=19  W=2/L=17  WR=10.5%**
- **Dir: SHORT**  •  HTF20 strongly against; zscore -1 to +1 neutral; session=asia  •  ONLY when 4h trend WITH trade

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(46/35) | H20e(35/46) |
| H60 | — | H60a(39/46) |
| T1 | T1a(54/46) | T1c(45/52) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
