# EUR_NZD — R37 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_3**  (5m ATR >120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50e**  (EMA50 down >0.5x)
- **ADR = ADR3**  (60-90%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **2,963**  (W=1,730 / L=1,233)  -  WR: **58.4%**

## Session distribution

- ny_mid: n=1142  W=659/L=483  WR=57.7%
- asia: n=865  W=510/L=355  WR=59.0%
- london_open: n=346  W=209/L=137  WR=60.4%
- ny_open: n=301  W=174/L=127  WR=57.8%
- london: n=139  W=79/L=60  WR=56.8%
- asia_late: n=91  W=54/L=37  WR=59.3%
- ny_close: n=40  W=23/L=17  WR=57.5%
- off_hours: n=39  W=22/L=17  WR=56.4%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1c AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=138  W=119/L=19  WR=86.2%
- Refine: exclude T4=T4a drops 13/19 losers (68%)
- **Final: n=92  W=86/L=6  WR=93.5%**
- **Dir: ?**  •  1h trend AGAINST trade; lower third; RSI 40-50 lower neutral  •  AVOID when 4h trend WITH trade

### W02.  `T1=T1c AND BBP=BBP2 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=137  W=119/L=18  WR=86.9%
- Refine: exclude T4=T4a drops 12/18 losers (67%)
- **Final: n=92  W=86/L=6  WR=93.5%**
- **Dir: LONG**  •  1h trend AGAINST trade; lower third; RSI 40-50 lower neutral  •  AVOID when 4h trend WITH trade

### W03.  `H60=H60e AND T1=T1c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=128  W=113/L=15  WR=88.3%
- Refine: exclude session_bucket=ny_mid drops 14/15 losers (93%)
- **Final: n=87  W=86/L=1  WR=98.9%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when session=ny_mid

### W04.  `H20=H20e AND H60=H60e AND T1=T1c AND RSI=RSI3`
- Raw: n=114  W=99/L=15  WR=86.8%
- Refine: exclude session_bucket=ny_mid drops 14/15 losers (93%)
- **Final: n=73  W=72/L=1  WR=98.6%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when session=ny_mid

### W05.  `T1=T1c AND RSI=RSI3 AND session_bucket=london_open`
- Raw: n=107  W=94/L=13  WR=87.9%
- Refine: exclude H20=H20b drops 11/13 losers (85%)
- **Final: n=88  W=86/L=2  WR=97.7%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 40-50 lower neutral; session=london_open  •  AVOID when HTF20 slightly aligned

### W06.  `T4=T4c AND BBP=BBP2 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=104  W=92/L=12  WR=88.5%
- Refine: exclude session_bucket=london_open drops 9/12 losers (75%)
- **Final: n=70  W=67/L=3  WR=95.7%**
- **Dir: LONG**  •  4h trend AGAINST trade; lower third; RSI 40-50 lower neutral  •  AVOID when session=london_open

### W07.  `T1=T1c AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=97  W=84/L=13  WR=86.6%
- Refine: exclude T4=T4a drops 13/13 losers (100%)
- **Final: n=59  W=59/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when 4h trend WITH trade

### W08.  `T1=T1c AND BBP=BBP2 AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=97  W=84/L=13  WR=86.6%
- Refine: exclude T4=T4a drops 13/13 losers (100%)
- **Final: n=59  W=59/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; lower third; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when 4h trend WITH trade

### W09.  `T1=T1c AND RSI=RSI3 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=96  W=84/L=12  WR=87.5%
- Refine: exclude T4=T4a drops 12/12 losers (100%)
- **Final: n=59  W=59/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when 4h trend WITH trade

### W10.  `H60=H60e AND T1=T1c AND BBP=BBP1`
- Raw: n=94  W=80/L=14  WR=85.1%
- Refine: exclude RSI=RSI0 drops 5/14 losers (36%)
- **Final: n=89  W=80/L=9  WR=89.9%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; just touched lower band  •  AVOID when RSI<20 extreme oversold

### W11.  `H60=H60e AND T1=T1c AND BBP=BBP1 AND ZS=ZS1`
- Raw: n=94  W=80/L=14  WR=85.1%
- Refine: exclude RSI=RSI0 drops 5/14 losers (36%)
- **Final: n=89  W=80/L=9  WR=89.9%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; just touched lower band; zscore -3 to -2 deep oversold  •  AVOID when RSI<20 extreme oversold

### W12.  `H60=H60e AND T1=T1c AND BBP=BBP1 AND direction_exec=long`
- Raw: n=94  W=80/L=14  WR=85.1%
- Refine: exclude RSI=RSI0 drops 5/14 losers (36%)
- **Final: n=89  W=80/L=9  WR=89.9%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend AGAINST trade; just touched lower band  •  AVOID when RSI<20 extreme oversold

### W13.  `T1=T1c AND T4=T4c AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=92  W=86/L=6  WR=93.5%
- Refine: exclude ZS=ZS3 drops 6/6 losers (100%)
- **Final: n=59  W=59/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; lower third; RSI 40-50 lower neutral  •  AVOID when zscore -1 to +1 neutral

### W14.  `H60=H60e AND T1=T1c AND session_bucket=london_open`
- Raw: n=83  W=76/L=7  WR=91.6%
- Refine: exclude RSI=RSI2 drops 6/7 losers (86%)
- **Final: n=61  W=60/L=1  WR=98.4%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; session=london_open  •  AVOID when RSI 30-40 weak

### W15.  `H60=H60e AND T1=T1c AND direction_exec=long AND session_bucket=london_open`
- Raw: n=83  W=76/L=7  WR=91.6%
- Refine: exclude RSI=RSI2 drops 6/7 losers (86%)
- **Final: n=61  W=60/L=1  WR=98.4%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend AGAINST trade; session=london_open  •  AVOID when RSI 30-40 weak

### W16.  `T1=T1c AND RSI=RSI3 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=80  W=68/L=12  WR=85.0%
- Refine: exclude H20=H20b drops 11/12 losers (92%)
- **Final: n=61  W=60/L=1  WR=98.4%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 40-50 lower neutral; session=london_open  •  AVOID when HTF20 slightly aligned

### W17.  `H60=H60a AND T1=T1c AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=79  W=68/L=11  WR=86.1%
- Refine: exclude RSI=RSI1 drops 9/11 losers (82%)
- **Final: n=58  W=56/L=2  WR=96.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; zscore -2 to -1 oversold; session=asia  •  AVOID when RSI 20-30 oversold

### W18.  `H60=H60a AND ZS=ZS2 AND direction_exec=long AND session_bucket=asia`
- Raw: n=79  W=68/L=11  WR=86.1%
- Refine: exclude RSI=RSI1 drops 9/11 losers (82%)
- **Final: n=58  W=56/L=2  WR=96.6%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; zscore -2 to -1 oversold; session=asia  •  AVOID when RSI 20-30 oversold

### W19.  `H20=H20a AND H60=H60e AND ZS=ZS1`
- Raw: n=76  W=69/L=7  WR=90.8%
- Refine: exclude T1=T1a drops 7/7 losers (100%)
- **Final: n=40  W=40/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; zscore -3 to -2 deep oversold  •  AVOID when 1h trend WITH trade

### W20.  `T4=T4c AND RSI=RSI3 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=71  W=65/L=6  WR=91.5%
- Refine: exclude T1=T1a drops 6/6 losers (100%)
- **Final: n=59  W=59/L=0  WR=100.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when 1h trend WITH trade

### W21.  `H60=H60a AND T1=T1c AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=71  W=64/L=7  WR=90.1%
- Refine: exclude ZS=ZS3 drops 6/7 losers (86%)
- **Final: n=43  W=42/L=1  WR=97.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; lower third; RSI 40-50 lower neutral  •  AVOID when zscore -1 to +1 neutral

### W22.  `H60=H60a AND BBP=BBP2 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=70  W=64/L=6  WR=91.4%
- Refine: exclude ZS=ZS3 drops 6/6 losers (100%)
- **Final: n=42  W=42/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; lower third; RSI 40-50 lower neutral  •  AVOID when zscore -1 to +1 neutral

### W23.  `H60=H60e AND T1=T1c AND T4=T4c AND session_bucket=london_open`
- Raw: n=69  W=62/L=7  WR=89.9%
- Refine: exclude H20=H20a drops 6/7 losers (86%)
- **Final: n=51  W=50/L=1  WR=98.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; session=london_open  •  AVOID when HTF20 aligned WITH trade

### W24.  `H20=H20a AND T1=T1c AND ZS=ZS1`
- Raw: n=66  W=66/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=66  W=66/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; zscore -3 to -2 deep oversold

### W25.  `H20=H20b AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=62  W=56/L=6  WR=90.3%
- Refine: exclude ZS=ZS3 drops 6/6 losers (100%)
- **Final: n=34  W=34/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 slightly aligned; lower third; RSI 40-50 lower neutral  •  AVOID when zscore -1 to +1 neutral

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T4=T4a AND BBP=BBP2 AND session_bucket=ny_mid`
- Raw: n=212  W=82/L=130  WR=38.7%
- Sharpen: no sharper sub-pattern
- **Sharp: n=212  W=82/L=130  WR=38.7%**
- **Dir: ?**  •  4h trend WITH trade; lower third; session=ny_mid

### L02.  `H60=H60e AND T4=T4a AND ZS=ZS2`
- Raw: n=193  W=75/L=118  WR=38.9%
- Sharpen: sharpest is RSI=RSI3 (39/118 of losers there)
- **Sharp: n=45  W=6/L=39  WR=13.3%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; zscore -2 to -1 oversold  •  ONLY when RSI 40-50 lower neutral

### L03.  `H60=H60e AND T4=T4a AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=193  W=75/L=118  WR=38.9%
- Sharpen: sharpest is RSI=RSI3 (39/118 of losers there)
- **Sharp: n=45  W=6/L=39  WR=13.3%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; lower third; zscore -2 to -1 oversold  •  ONLY when RSI 40-50 lower neutral

### L04.  `T4=T4a AND ZS=ZS2 AND session_bucket=ny_mid`
- Raw: n=180  W=64/L=116  WR=35.6%
- Sharpen: sharpest is T1=T1c (27/116 of losers there)
- **Sharp: n=30  W=3/L=27  WR=10.0%**
- **Dir: ?**  •  4h trend WITH trade; zscore -2 to -1 oversold; session=ny_mid  •  ONLY when 1h trend AGAINST trade

### L05.  `T4=T4a AND BBP=BBP2 AND ZS=ZS2 AND session_bucket=ny_mid`
- Raw: n=180  W=64/L=116  WR=35.6%
- Sharpen: sharpest is T1=T1c (27/116 of losers there)
- **Sharp: n=30  W=3/L=27  WR=10.0%**
- **Dir: ?**  •  4h trend WITH trade; lower third; zscore -2 to -1 oversold; session=ny_mid  •  ONLY when 1h trend AGAINST trade

### L06.  `H60=H60e AND T1=T1a AND T4=T4a AND BBP=BBP2`
- Raw: n=171  W=68/L=103  WR=39.8%
- Sharpen: sharpest is RSI=RSI3 (46/103 of losers there)
- **Sharp: n=57  W=11/L=46  WR=19.3%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend WITH trade; lower third  •  ONLY when RSI 40-50 lower neutral

### L07.  `H60=H60e AND T4=T4a AND BBP=BBP2 AND direction_exec=short`
- Raw: n=171  W=68/L=103  WR=39.8%
- Sharpen: sharpest is RSI=RSI3 (46/103 of losers there)
- **Sharp: n=57  W=11/L=46  WR=19.3%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend WITH trade; lower third  •  ONLY when RSI 40-50 lower neutral

### L08.  `H60=H60e AND ZS=ZS2 AND direction_exec=short`
- Raw: n=148  W=59/L=89  WR=39.9%
- Sharpen: sharpest is RSI=RSI3 (34/89 of losers there)
- **Sharp: n=34  W=0/L=34  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; zscore -2 to -1 oversold  •  ONLY when RSI 40-50 lower neutral

### L09.  `H60=H60e AND T1=T1a AND ZS=ZS2 AND direction_exec=short`
- Raw: n=148  W=59/L=89  WR=39.9%
- Sharpen: sharpest is RSI=RSI3 (34/89 of losers there)
- **Sharp: n=34  W=0/L=34  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend WITH trade; zscore -2 to -1 oversold  •  ONLY when RSI 40-50 lower neutral

### L10.  `H60=H60e AND BBP=BBP2 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=148  W=59/L=89  WR=39.9%
- Sharpen: sharpest is RSI=RSI3 (34/89 of losers there)
- **Sharp: n=34  W=0/L=34  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; lower third; zscore -2 to -1 oversold  •  ONLY when RSI 40-50 lower neutral

### L11.  `T4=T4a AND RSI=RSI2 AND ZS=ZS2 AND session_bucket=ny_mid`
- Raw: n=134  W=49/L=85  WR=36.6%
- Sharpen: sharpest is T1=T1c (19/85 of losers there)
- **Sharp: n=20  W=1/L=19  WR=5.0%**
- **Dir: ?**  •  4h trend WITH trade; RSI 30-40 weak; zscore -2 to -1 oversold; session=ny_mid  •  ONLY when 1h trend AGAINST trade

### L12.  `H60=H60e AND T1=T1a AND T4=T4a AND ZS=ZS2`
- Raw: n=133  W=47/L=86  WR=35.3%
- Sharpen: sharpest is RSI=RSI3 (34/86 of losers there)
- **Sharp: n=34  W=0/L=34  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend WITH trade; zscore -2 to -1 oversold  •  ONLY when RSI 40-50 lower neutral

### L13.  `H60=H60e AND T4=T4a AND ZS=ZS2 AND direction_exec=short`
- Raw: n=133  W=47/L=86  WR=35.3%
- Sharpen: sharpest is RSI=RSI3 (34/86 of losers there)
- **Sharp: n=34  W=0/L=34  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend WITH trade; zscore -2 to -1 oversold  •  ONLY when RSI 40-50 lower neutral

### L14.  `H60=H60e AND RSI=RSI3 AND direction_exec=short`
- Raw: n=133  W=51/L=82  WR=38.3%
- Sharpen: sharpest is ZS=ZS2 (34/82 of losers there)
- **Sharp: n=34  W=0/L=34  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 40-50 lower neutral  •  ONLY when zscore -2 to -1 oversold

### L15.  `H60=H60e AND T4=T4a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=129  W=51/L=78  WR=39.5%
- Sharpen: sharpest is ZS=ZS2 (34/78 of losers there)
- **Sharp: n=34  W=0/L=34  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when zscore -2 to -1 oversold

### L16.  `H60=H60a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=127  W=48/L=79  WR=37.8%
- Sharpen: sharpest is T1=T1a (71/79 of losers there)
- **Sharp: n=91  W=20/L=71  WR=22.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral  •  ONLY when 1h trend WITH trade

### L17.  `T4=T4a AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=126  W=45/L=81  WR=35.7%
- Sharpen: sharpest is direction_exec=short (64/81 of losers there)
- **Sharp: n=76  W=12/L=64  WR=15.8%**
- **Dir: ?**  •  4h trend WITH trade; lower third; RSI 40-50 lower neutral  •  ONLY when short

### L18.  `H60=H60a AND T4=T4c AND RSI=RSI1`
- Raw: n=124  W=47/L=77  WR=37.9%
- Sharpen: sharpest is ZS=ZS1 (42/77 of losers there)
- **Sharp: n=50  W=8/L=42  WR=16.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when zscore -3 to -2 deep oversold

### L19.  `T1=T1a AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=122  W=31/L=91  WR=25.4%
- Sharpen: sharpest is T4=T4a (63/91 of losers there)
- **Sharp: n=75  W=12/L=63  WR=16.0%**
- **Dir: ?**  •  1h trend WITH trade; lower third; RSI 40-50 lower neutral  •  ONLY when 4h trend WITH trade

### L20.  `H60=H60a AND T4=T4c AND direction_exec=short`
- Raw: n=121  W=46/L=75  WR=38.0%
- Sharpen: sharpest is RSI=RSI3 (27/75 of losers there)
- **Sharp: n=29  W=2/L=27  WR=6.9%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade  •  ONLY when RSI 40-50 lower neutral

### L21.  `H20=H20d AND H60=H60e AND RSI=RSI3`
- Raw: n=121  W=47/L=74  WR=38.8%
- Sharpen: sharpest is ZS=ZS2 (30/74 of losers there)
- **Sharp: n=30  W=0/L=30  WR=0.0%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 strongly against; RSI 40-50 lower neutral  •  ONLY when zscore -2 to -1 oversold

### L22.  `H20=H20d AND H60=H60e AND T4=T4a AND RSI=RSI3`
- Raw: n=121  W=47/L=74  WR=38.8%
- Sharpen: sharpest is ZS=ZS2 (30/74 of losers there)
- **Sharp: n=30  W=0/L=30  WR=0.0%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 strongly against; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when zscore -2 to -1 oversold

### L23.  `H20=H20d AND H60=H60e AND RSI=RSI3 AND direction_exec=short`
- Raw: n=121  W=47/L=74  WR=38.8%
- Sharpen: sharpest is ZS=ZS2 (30/74 of losers there)
- **Sharp: n=30  W=0/L=30  WR=0.0%**
- **Dir: SHORT**  •  HTF20 mildly against; HTF60 strongly against; RSI 40-50 lower neutral  •  ONLY when zscore -2 to -1 oversold

### L24.  `H60=H60a AND T1=T1a AND RSI=RSI3`
- Raw: n=121  W=48/L=73  WR=39.7%
- Sharpen: sharpest is direction_exec=short (71/73 of losers there)
- **Sharp: n=91  W=20/L=71  WR=22.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when short

### L25.  `RSI=RSI3 AND direction_exec=short AND session_bucket=asia`
- Raw: n=114  W=41/L=73  WR=36.0%
- Sharpen: sharpest is ZS=ZS2 (28/73 of losers there)
- **Sharp: n=32  W=4/L=28  WR=12.5%**
- **Dir: SHORT**  •  RSI 40-50 lower neutral; session=asia  •  ONLY when zscore -2 to -1 oversold

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
