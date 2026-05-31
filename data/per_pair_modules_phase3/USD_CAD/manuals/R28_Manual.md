# USD_CAD — R28 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **2,066**  (W=1,302 / L=764)  -  WR: **63.0%**

## Session distribution

- ny_mid: n=999  W=626/L=373  WR=62.7%
- ny_open: n=442  W=267/L=175  WR=60.4%
- ny_close: n=263  W=178/L=85  WR=67.7%
- london_open: n=186  W=122/L=64  WR=65.6%
- london: n=144  W=87/L=57  WR=60.4%
- asia_late: n=31  W=22/L=9  WR=71.0%
- off_hours: n=1  W=0/L=1  WR=0.0%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND T4=T4a AND BBP=BBP4 AND direction_exec=short`
- Raw: n=103  W=88/L=15  WR=85.4%
- Refine: exclude session_bucket=ny_close drops 7/15 losers (47%)
- **Final: n=83  W=75/L=8  WR=90.4%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend WITH trade; upper third  •  AVOID when session=ny_close

### W02.  `T4=T4c AND ZS=ZS5 AND session_bucket=ny_mid`
- Raw: n=87  W=78/L=9  WR=89.7%
- Refine: exclude H20=H20e drops 7/9 losers (78%)
- **Final: n=63  W=61/L=2  WR=96.8%**
- **Dir: ?**  •  4h trend AGAINST trade; zscore +2 to +3 deep overbought; session=ny_mid  •  AVOID when HTF20 strongly against

### W03.  `H20=H20a AND T1=T1c AND T4=T4a AND BBP=BBP4`
- Raw: n=79  W=71/L=8  WR=89.9%
- Refine: exclude ZS=ZS4 drops 8/8 losers (100%)
- **Final: n=14  W=14/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; upper third  •  AVOID when zscore +1 to +2 overbought

### W04.  `T1=T1c AND T4=T4c AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=77  W=66/L=11  WR=85.7%
- Refine: exclude session_bucket=london drops 6/11 losers (55%)
- **Final: n=69  W=64/L=5  WR=92.8%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when session=london

### W05.  `H20=H20e AND T1=T1a AND BBP=BBP3`
- Raw: n=76  W=66/L=10  WR=86.8%
- Refine: exclude RSI=RSI3 drops 3/10 losers (30%)
- **Final: n=69  W=62/L=7  WR=89.9%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; middle of band  •  AVOID when RSI 40-50 lower neutral

### W06.  `H20=H20e AND T1=T1a AND BBP=BBP3 AND ZS=ZS3`
- Raw: n=76  W=66/L=10  WR=86.8%
- Refine: exclude RSI=RSI3 drops 3/10 losers (30%)
- **Final: n=69  W=62/L=7  WR=89.9%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; middle of band; zscore -1 to +1 neutral  •  AVOID when RSI 40-50 lower neutral

### W07.  `H60=H60a AND T1=T1a AND T4=T4c AND ZS=ZS3`
- Raw: n=71  W=61/L=10  WR=85.9%
- Refine: exclude session_bucket=ny_mid drops 5/10 losers (50%)
- **Final: n=56  W=51/L=5  WR=91.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade; zscore -1 to +1 neutral  •  AVOID when session=ny_mid

### W08.  `T1=T1c AND T4=T4c AND ZS=ZS5 AND direction_exec=short`
- Raw: n=69  W=62/L=7  WR=89.9%
- Refine: exclude session_bucket=london drops 6/7 losers (86%)
- **Final: n=61  W=60/L=1  WR=98.4%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  AVOID when session=london

### W09.  `H20=H20e AND T1=T1c AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=69  W=59/L=10  WR=85.5%
- Refine: exclude session_bucket=ny_close drops 7/10 losers (70%)
- **Final: n=45  W=42/L=3  WR=93.3%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; upper third; RSI 50-60 upper neutral  •  AVOID when session=ny_close

### W10.  `H20=H20e AND T1=T1c AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=66  W=57/L=9  WR=86.4%
- Refine: exclude session_bucket=ny_close drops 6/9 losers (67%)
- **Final: n=43  W=40/L=3  WR=93.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when session=ny_close

### W11.  `H20=H20a AND T1=T1c AND T4=T4a AND ZS=ZS4`
- Raw: n=65  W=57/L=8  WR=87.7%
- Refine: exclude session_bucket=ny_mid drops 5/8 losers (62%)
- **Final: n=37  W=34/L=3  WR=91.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; zscore +1 to +2 overbought  •  AVOID when session=ny_mid

### W12.  `H20=H20e AND T1=T1a AND BBP=BBP3 AND direction_exec=long`
- Raw: n=63  W=56/L=7  WR=88.9%
- Refine: exclude RSI=RSI4 drops 7/7 losers (100%)
- **Final: n=20  W=20/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend WITH trade; middle of band  •  AVOID when RSI 50-60 upper neutral

### W13.  `H60=H60c AND T4=T4a AND BBP=BBP2`
- Raw: n=62  W=53/L=9  WR=85.5%
- Refine: exclude session_bucket=ny_mid drops 6/9 losers (67%)
- **Final: n=43  W=40/L=3  WR=93.0%**
- **Dir: ?**  •  HTF60 neutral; 4h trend WITH trade; lower third  •  AVOID when session=ny_mid

### W14.  `T4=T4c AND RSI=RSI4 AND ZS=ZS5 AND session_bucket=ny_mid`
- Raw: n=61  W=58/L=3  WR=95.1%
- Refine: exclude H60=H60c drops 3/3 losers (100%)
- **Final: n=52  W=52/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought; session=ny_mid  •  AVOID when HTF60 neutral

### W15.  `H20=H20a AND H60=H60c AND RSI=RSI3`
- Raw: n=61  W=55/L=6  WR=90.2%
- Refine: exclude T1=T1a drops 6/6 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 neutral; RSI 40-50 lower neutral  •  AVOID when 1h trend WITH trade

### W16.  `H20=H20d AND H60=H60a AND T1=T1a AND T4=T4c`
- Raw: n=61  W=53/L=8  WR=86.9%
- Refine: exclude RSI=RSI2 drops 8/8 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade  •  AVOID when RSI 30-40 weak

### W17.  `H60=H60c AND T4=T4a AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=60  W=51/L=9  WR=85.0%
- Refine: exclude session_bucket=ny_mid drops 6/9 losers (67%)
- **Final: n=41  W=38/L=3  WR=92.7%**
- **Dir: ?**  •  HTF60 neutral; 4h trend WITH trade; lower third; RSI 40-50 lower neutral  •  AVOID when session=ny_mid

### W18.  `T4=T4a AND direction_exec=long AND session_bucket=london`
- Raw: n=59  W=55/L=4  WR=93.2%
- Refine: exclude ZS=ZS4 drops 4/4 losers (100%)
- **Final: n=38  W=38/L=0  WR=100.0%**
- **Dir: LONG**  •  4h trend WITH trade; session=london  •  AVOID when zscore +1 to +2 overbought

### W19.  `T1=T1c AND T4=T4c AND ZS=ZS1 AND session_bucket=ny_mid`
- Raw: n=58  W=50/L=8  WR=86.2%
- Refine: exclude direction_exec=short drops 8/8 losers (100%)
- **Final: n=38  W=38/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold; session=ny_mid  •  AVOID when short

### W20.  `T1=T1a AND BBP=BBP2 AND session_bucket=london_open`
- Raw: n=57  W=49/L=8  WR=86.0%
- Refine: exclude RSI=RSI4 drops 6/8 losers (75%)
- **Final: n=48  W=46/L=2  WR=95.8%**
- **Dir: ?**  •  1h trend WITH trade; lower third; session=london_open  •  AVOID when RSI 50-60 upper neutral

### W21.  `T1=T1a AND ZS=ZS2 AND session_bucket=london_open`
- Raw: n=57  W=49/L=8  WR=86.0%
- Refine: exclude RSI=RSI4 drops 6/8 losers (75%)
- **Final: n=48  W=46/L=2  WR=95.8%**
- **Dir: ?**  •  1h trend WITH trade; zscore -2 to -1 oversold; session=london_open  •  AVOID when RSI 50-60 upper neutral

### W22.  `T1=T1a AND BBP=BBP2 AND ZS=ZS2 AND session_bucket=london_open`
- Raw: n=57  W=49/L=8  WR=86.0%
- Refine: exclude RSI=RSI4 drops 6/8 losers (75%)
- **Final: n=48  W=46/L=2  WR=95.8%**
- **Dir: ?**  •  1h trend WITH trade; lower third; zscore -2 to -1 oversold; session=london_open  •  AVOID when RSI 50-60 upper neutral

### W23.  `T1=T1a AND RSI=RSI3 AND session_bucket=london_open`
- Raw: n=56  W=52/L=4  WR=92.9%
- Refine: exclude T4=T4c drops 4/4 losers (100%)
- **Final: n=40  W=40/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; RSI 40-50 lower neutral; session=london_open  •  AVOID when 4h trend AGAINST trade

### W24.  `H60=H60e AND T4=T4a AND session_bucket=london`
- Raw: n=56  W=49/L=7  WR=87.5%
- Refine: exclude RSI=RSI5 drops 6/7 losers (86%)
- **Final: n=36  W=35/L=1  WR=97.2%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; session=london  •  AVOID when RSI 60-70 strong

### W25.  `T1=T1a AND T4=T4c AND BBP=BBP3 AND direction_exec=long`
- Raw: n=55  W=49/L=6  WR=89.1%
- Refine: exclude H60=H60e drops 4/6 losers (67%)
- **Final: n=37  W=35/L=2  WR=94.6%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend AGAINST trade; middle of band  •  AVOID when HTF60 strongly against

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `RSI=RSI4 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=88  W=35/L=53  WR=39.8%
- Sharpen: sharpest is T1=T1a (44/53 of losers there)
- **Sharp: n=63  W=19/L=44  WR=30.2%**
- **Dir: LONG**  •  RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when 1h trend WITH trade

### L02.  `H20=H20e AND T4=T4c AND BBP=BBP4 AND direction_exec=long`
- Raw: n=78  W=24/L=54  WR=30.8%
- Sharpen: sharpest is T1=T1a (39/54 of losers there)
- **Sharp: n=44  W=5/L=39  WR=11.4%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend AGAINST trade; upper third  •  ONLY when 1h trend WITH trade

### L03.  `H20=H20e AND T1=T1a AND BBP=BBP4`
- Raw: n=76  W=24/L=52  WR=31.6%
- Sharpen: sharpest is T4=T4c (42/52 of losers there)
- **Sharp: n=47  W=5/L=42  WR=10.6%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; upper third  •  ONLY when 4h trend AGAINST trade

### L04.  `H60=H60a AND T1=T1c AND ZS=ZS3`
- Raw: n=71  W=26/L=45  WR=36.6%
- Sharpen: sharpest is BBP=BBP3 (30/45 of losers there)
- **Sharp: n=39  W=9/L=30  WR=23.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; zscore -1 to +1 neutral  •  ONLY when middle of band

### L05.  `H20=H20e AND T1=T1a AND BBP=BBP4 AND direction_exec=long`
- Raw: n=69  W=20/L=49  WR=29.0%
- Sharpen: sharpest is T4=T4c (39/49 of losers there)
- **Sharp: n=44  W=5/L=39  WR=11.4%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend WITH trade; upper third  •  ONLY when 4h trend AGAINST trade

### L06.  `T4=T4a AND ZS=ZS5 AND session_bucket=ny_mid`
- Raw: n=68  W=26/L=42  WR=38.2%
- Sharpen: sharpest is T1=T1a (16/42 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: ?**  •  4h trend WITH trade; zscore +2 to +3 deep overbought; session=ny_mid  •  ONLY when 1h trend WITH trade

### L07.  `H20=H20e AND T4=T4c AND ZS=ZS4 AND direction_exec=long`
- Raw: n=64  W=22/L=42  WR=34.4%
- Sharpen: sharpest is T1=T1a (30/42 of losers there)
- **Sharp: n=35  W=5/L=30  WR=14.3%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  ONLY when 1h trend WITH trade

### L08.  `T1=T1a AND RSI=RSI4 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=63  W=19/L=44  WR=30.2%
- Sharpen: sharpest is BBP=BBP5 (26/44 of losers there)
- **Sharp: n=27  W=1/L=26  WR=3.7%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when just touched upper band

### L09.  `H20=H20e AND T1=T1a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=63  W=23/L=40  WR=36.5%
- Sharpen: sharpest is ZS=ZS1 (14/40 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when zscore -3 to -2 deep oversold

### L10.  `H60=H60e AND T1=T1c AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=61  W=22/L=39  WR=36.1%
- Sharpen: sharpest is RSI=RSI3 (27/39 of losers there)
- **Sharp: n=36  W=9/L=27  WR=25.0%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend AGAINST trade; session=ny_open  •  ONLY when RSI 40-50 lower neutral

### L11.  `H60=H60e AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=59  W=16/L=43  WR=27.1%
- Sharpen: sharpest is T1=T1a (19/43 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when 1h trend WITH trade

### L12.  `H60=H60a AND T4=T4c AND session_bucket=london`
- Raw: n=59  W=18/L=41  WR=30.5%
- Sharpen: sharpest is BBP=BBP4 (24/41 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=london  •  ONLY when upper third

### L13.  `T1=T1a AND BBP=BBP5 AND RSI=RSI4`
- Raw: n=59  W=23/L=36  WR=39.0%
- Sharpen: sharpest is direction_exec=long (26/36 of losers there)
- **Sharp: n=27  W=1/L=26  WR=3.7%**
- **Dir: ?**  •  1h trend WITH trade; just touched upper band; RSI 50-60 upper neutral  •  ONLY when long

### L14.  `T1=T1a AND BBP=BBP5 AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=59  W=23/L=36  WR=39.0%
- Sharpen: sharpest is direction_exec=long (26/36 of losers there)
- **Sharp: n=27  W=1/L=26  WR=3.7%**
- **Dir: ?**  •  1h trend WITH trade; just touched upper band; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when long

### L15.  `H60=H60a AND T1=T1c AND RSI=RSI4 AND ZS=ZS3`
- Raw: n=57  W=20/L=37  WR=35.1%
- Sharpen: sharpest is session_bucket=ny_mid (21/37 of losers there)
- **Sharp: n=28  W=7/L=21  WR=25.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  ONLY when session=ny_mid

### L16.  `T1=T1c AND BBP=BBP3 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=56  W=20/L=36  WR=35.7%
- Sharpen: sharpest is session_bucket=ny_mid (16/36 of losers there)
- **Sharp: n=20  W=4/L=16  WR=20.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; middle of band; RSI 50-60 upper neutral  •  ONLY when session=ny_mid

### L17.  `H20=H20e AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=55  W=15/L=40  WR=27.3%
- Sharpen: sharpest is T1=T1a (14/40 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when 1h trend WITH trade

### L18.  `ZS=ZS1 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=55  W=16/L=39  WR=29.1%
- Sharpen: sharpest is T4=T4a (24/39 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: SHORT**  •  zscore -3 to -2 deep oversold; session=ny_mid  •  ONLY when 4h trend WITH trade

### L19.  `H20=H20a AND T1=T1c AND BBP=BBP3`
- Raw: n=55  W=20/L=35  WR=36.4%
- Sharpen: sharpest is H60=H60a (17/35 of losers there)
- **Sharp: n=22  W=5/L=17  WR=22.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; middle of band  •  ONLY when HTF60 aligned WITH trade

### L20.  `H20=H20a AND T1=T1c AND BBP=BBP3 AND ZS=ZS3`
- Raw: n=55  W=20/L=35  WR=36.4%
- Sharpen: sharpest is H60=H60a (17/35 of losers there)
- **Sharp: n=22  W=5/L=17  WR=22.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; middle of band; zscore -1 to +1 neutral  •  ONLY when HTF60 aligned WITH trade

### L21.  `H20=H20e AND T4=T4c AND ZS=ZS5`
- Raw: n=55  W=22/L=33  WR=40.0%
- Sharpen: sharpest is session_bucket=ny_close (20/33 of losers there)
- **Sharp: n=25  W=5/L=20  WR=20.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when session=ny_close

### L22.  `H20=H20e AND T1=T1a AND ZS=ZS4`
- Raw: n=54  W=14/L=40  WR=25.9%
- Sharpen: sharpest is T4=T4c (32/40 of losers there)
- **Sharp: n=37  W=5/L=32  WR=13.5%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; zscore +1 to +2 overbought  •  ONLY when 4h trend AGAINST trade

### L23.  `H20=H20e AND T1=T1a AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=54  W=14/L=40  WR=25.9%
- Sharpen: sharpest is T4=T4c (32/40 of losers there)
- **Sharp: n=37  W=5/L=32  WR=13.5%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; upper third; zscore +1 to +2 overbought  •  ONLY when 4h trend AGAINST trade

### L24.  `H20=H20e AND T1=T1a AND ZS=ZS5`
- Raw: n=54  W=17/L=37  WR=31.5%
- Sharpen: sharpest is session_bucket=ny_close (16/37 of losers there)
- **Sharp: n=17  W=1/L=16  WR=5.9%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; zscore +2 to +3 deep overbought  •  ONLY when session=ny_close

### L25.  `H60=H60d AND T4=T4c AND RSI=RSI4`
- Raw: n=53  W=21/L=32  WR=39.6%
- Sharpen: sharpest is H20=H20e (15/32 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: ?**  •  HTF60 mildly against; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when HTF20 strongly against

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(36/27) | H20e(26/34) |
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
