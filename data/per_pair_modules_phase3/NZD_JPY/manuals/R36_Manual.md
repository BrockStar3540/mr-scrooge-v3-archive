# NZD_JPY — R36 Manual

## Regime centroid (locked factors)

- **BB = BB2**  (normal bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **2,285**  (W=1,436 / L=849)  -  WR: **62.8%**

## Session distribution

- asia: n=813  W=512/L=301  WR=63.0%
- london_open: n=347  W=217/L=130  WR=62.5%
- ny_mid: n=266  W=174/L=92  WR=65.4%
- ny_open: n=253  W=140/L=113  WR=55.3%
- ny_close: n=215  W=131/L=84  WR=60.9%
- london: n=196  W=135/L=61  WR=68.9%
- off_hours: n=141  W=88/L=53  WR=62.4%
- asia_late: n=54  W=39/L=15  WR=72.2%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1c AND T4=T4c AND direction_exec=long AND session_bucket=asia`
- Raw: n=135  W=115/L=20  WR=85.2%
- Refine: exclude BBP=BBP4 drops 15/20 losers (75%)
- **Final: n=90  W=85/L=5  WR=94.4%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=asia  •  AVOID when upper third

### W02.  `T4=T4c AND BBP=BBP5 AND RSI=RSI4`
- Raw: n=106  W=92/L=14  WR=86.8%
- Refine: exclude session_bucket=ny_close drops 6/14 losers (43%)
- **Final: n=94  W=86/L=8  WR=91.5%**
- **Dir: ?**  •  4h trend AGAINST trade; just touched upper band; RSI 50-60 upper neutral  •  AVOID when session=ny_close

### W03.  `T4=T4c AND BBP=BBP5 AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=106  W=92/L=14  WR=86.8%
- Refine: exclude session_bucket=ny_close drops 6/14 losers (43%)
- **Final: n=94  W=86/L=8  WR=91.5%**
- **Dir: ?**  •  4h trend AGAINST trade; just touched upper band; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when session=ny_close

### W04.  `T4=T4c AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=95  W=93/L=2  WR=97.9%
- Refine: exclude RSI=RSI3 drops 2/2 losers (100%)
- **Final: n=87  W=87/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend AGAINST trade; zscore +2 to +3 deep overbought; session=asia  •  AVOID when RSI 40-50 lower neutral

### W05.  `T1=T1c AND T4=T4a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=90  W=80/L=10  WR=88.9%
- Refine: exclude session_bucket=london_open drops 3/10 losers (30%)
- **Final: n=87  W=80/L=7  WR=92.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when session=london_open

### W06.  `H60=H60e AND T1=T1c AND BBP=BBP5`
- Raw: n=89  W=76/L=13  WR=85.4%
- Refine: exclude T4=T4a drops 8/13 losers (62%)
- **Final: n=65  W=60/L=5  WR=92.3%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; just touched upper band  •  AVOID when 4h trend WITH trade

### W07.  `H60=H60e AND T1=T1c AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=89  W=76/L=13  WR=85.4%
- Refine: exclude T4=T4a drops 8/13 losers (62%)
- **Final: n=65  W=60/L=5  WR=92.3%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; just touched upper band; zscore +2 to +3 deep overbought  •  AVOID when 4h trend WITH trade

### W08.  `H60=H60e AND T4=T4c AND BBP=BBP5`
- Raw: n=84  W=76/L=8  WR=90.5%
- Refine: exclude H20=H20d drops 4/8 losers (50%)
- **Final: n=80  W=76/L=4  WR=95.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; just touched upper band  •  AVOID when HTF20 mildly against

### W09.  `H60=H60e AND T4=T4c AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=84  W=76/L=8  WR=90.5%
- Refine: exclude H20=H20d drops 4/8 losers (50%)
- **Final: n=80  W=76/L=4  WR=95.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; just touched upper band; zscore +2 to +3 deep overbought  •  AVOID when HTF20 mildly against

### W10.  `H20=H20a AND T1=T1c AND T4=T4c AND session_bucket=asia`
- Raw: n=82  W=70/L=12  WR=85.4%
- Refine: exclude BBP=BBP4 drops 10/12 losers (83%)
- **Final: n=54  W=52/L=2  WR=96.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; session=asia  •  AVOID when upper third

### W11.  `T4=T4c AND RSI=RSI4 AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=81  W=81/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=81  W=81/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought; session=asia

### W12.  `T1=T1c AND T4=T4c AND BBP=BBP5 AND RSI=RSI4`
- Raw: n=81  W=70/L=11  WR=86.4%
- Refine: exclude session_bucket=ny_close drops 6/11 losers (55%)
- **Final: n=73  W=68/L=5  WR=93.2%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; just touched upper band; RSI 50-60 upper neutral  •  AVOID when session=ny_close

### W13.  `H60=H60e AND T1=T1a AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=78  W=68/L=10  WR=87.2%
- Refine: exclude session_bucket=ny_mid drops 5/10 losers (50%)
- **Final: n=68  W=63/L=5  WR=92.6%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; lower third; RSI 40-50 lower neutral  •  AVOID when session=ny_mid

### W14.  `H20=H20e AND H60=H60e AND BBP=BBP5`
- Raw: n=76  W=68/L=8  WR=89.5%
- Refine: exclude session_bucket=london drops 3/8 losers (38%)
- **Final: n=73  W=68/L=5  WR=93.2%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; just touched upper band  •  AVOID when session=london

### W15.  `H20=H20e AND H60=H60e AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=76  W=68/L=8  WR=89.5%
- Refine: exclude session_bucket=london drops 3/8 losers (38%)
- **Final: n=73  W=68/L=5  WR=93.2%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; just touched upper band; zscore +2 to +3 deep overbought  •  AVOID when session=london

### W16.  `H60=H60e AND ZS=ZS4 AND session_bucket=london_open`
- Raw: n=76  W=66/L=10  WR=86.8%
- Refine: exclude H20=H20d drops 5/10 losers (50%)
- **Final: n=67  W=62/L=5  WR=92.5%**
- **Dir: ?**  •  HTF60 strongly against; zscore +1 to +2 overbought; session=london_open  •  AVOID when HTF20 mildly against

### W17.  `H60=H60e AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=london_open`
- Raw: n=76  W=66/L=10  WR=86.8%
- Refine: exclude H20=H20d drops 5/10 losers (50%)
- **Final: n=67  W=62/L=5  WR=92.5%**
- **Dir: ?**  •  HTF60 strongly against; upper third; zscore +1 to +2 overbought; session=london_open  •  AVOID when HTF20 mildly against

### W18.  `H60=H60e AND T1=T1c AND BBP=BBP5 AND RSI=RSI4`
- Raw: n=75  W=66/L=9  WR=88.0%
- Refine: exclude H20=H20d drops 4/9 losers (44%)
- **Final: n=71  W=66/L=5  WR=93.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; just touched upper band; RSI 50-60 upper neutral  •  AVOID when HTF20 mildly against

### W19.  `H20=H20e AND T4=T4c AND BBP=BBP5`
- Raw: n=72  W=64/L=8  WR=88.9%
- Refine: exclude direction_exec=long drops 8/8 losers (100%)
- **Final: n=42  W=42/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; just touched upper band  •  AVOID when long

### W20.  `H20=H20e AND T4=T4c AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=72  W=64/L=8  WR=88.9%
- Refine: exclude direction_exec=long drops 8/8 losers (100%)
- **Final: n=42  W=42/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; just touched upper band; zscore +2 to +3 deep overbought  •  AVOID when long

### W21.  `H20=H20e AND BBP=BBP5 AND direction_exec=short`
- Raw: n=72  W=62/L=10  WR=86.1%
- Refine: exclude T4=T4a drops 10/10 losers (100%)
- **Final: n=42  W=42/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 strongly against; just touched upper band  •  AVOID when 4h trend WITH trade

### W22.  `H20=H20e AND BBP=BBP5 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=72  W=62/L=10  WR=86.1%
- Refine: exclude T4=T4a drops 10/10 losers (100%)
- **Final: n=42  W=42/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 strongly against; just touched upper band; zscore +2 to +3 deep overbought  •  AVOID when 4h trend WITH trade

### W23.  `H60=H60e AND T1=T1a AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=71  W=62/L=9  WR=87.3%
- Refine: exclude session_bucket=ny_mid drops 4/9 losers (44%)
- **Final: n=63  W=58/L=5  WR=92.1%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when session=ny_mid

### W24.  `H60=H60e AND ZS=ZS4 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=70  W=61/L=9  WR=87.1%
- Refine: exclude H20=H20d drops 5/9 losers (56%)
- **Final: n=61  W=57/L=4  WR=93.4%**
- **Dir: SHORT**  •  HTF60 strongly against; zscore +1 to +2 overbought; session=london_open  •  AVOID when HTF20 mildly against

### W25.  `H60=H60e AND T4=T4a AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=70  W=60/L=10  WR=85.7%
- Refine: exclude H20=H20e drops 8/10 losers (80%)
- **Final: n=37  W=35/L=2  WR=94.6%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when HTF20 strongly against

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1a AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=135  W=54/L=81  WR=40.0%
- Sharpen: sharpest is H60=H60a (36/81 of losers there)
- **Sharp: n=42  W=6/L=36  WR=14.3%**
- **Dir: ?**  •  1h trend WITH trade; RSI 40-50 lower neutral; session=asia  •  ONLY when HTF60 aligned WITH trade

### L02.  `T1=T1a AND T4=T4a AND direction_exec=short AND session_bucket=asia`
- Raw: n=105  W=42/L=63  WR=40.0%
- Sharpen: sharpest is ZS=ZS5 (19/63 of losers there)
- **Sharp: n=22  W=3/L=19  WR=13.6%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend WITH trade; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L03.  `T1=T1a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=100  W=30/L=70  WR=30.0%
- Sharpen: sharpest is T4=T4c (54/70 of losers there)
- **Sharp: n=65  W=11/L=54  WR=16.9%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when 4h trend AGAINST trade

### L04.  `H60=H60a AND T1=T1a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=97  W=30/L=67  WR=30.9%
- Sharpen: sharpest is T4=T4c (52/67 of losers there)
- **Sharp: n=63  W=11/L=52  WR=17.5%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when 4h trend AGAINST trade

### L05.  `T1=T1a AND T4=T4c AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=83  W=32/L=51  WR=38.6%
- Sharpen: sharpest is direction_exec=long (29/51 of losers there)
- **Sharp: n=32  W=3/L=29  WR=9.4%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral; session=asia  •  ONLY when long

### L06.  `BBP=BBP2 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=80  W=25/L=55  WR=31.2%
- Sharpen: sharpest is T1=T1a (36/55 of losers there)
- **Sharp: n=45  W=9/L=36  WR=20.0%**
- **Dir: SHORT**  •  lower third; RSI 50-60 upper neutral  •  ONLY when 1h trend WITH trade

### L07.  `H60=H60a AND T1=T1a AND T4=T4c AND RSI=RSI3`
- Raw: n=80  W=27/L=53  WR=33.8%
- Sharpen: sharpest is direction_exec=long (52/53 of losers there)
- **Sharp: n=63  W=11/L=52  WR=17.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when long

### L08.  `H60=H60e AND BBP=BBP2 AND RSI=RSI4`
- Raw: n=79  W=29/L=50  WR=36.7%
- Sharpen: sharpest is T4=T4a (28/50 of losers there)
- **Sharp: n=33  W=5/L=28  WR=15.2%**
- **Dir: ?**  •  HTF60 strongly against; lower third; RSI 50-60 upper neutral  •  ONLY when 4h trend WITH trade

### L09.  `T1=T1a AND T4=T4a AND BBP=BBP5`
- Raw: n=75  W=29/L=46  WR=38.7%
- Sharpen: sharpest is session_bucket=asia (25/46 of losers there)
- **Sharp: n=28  W=3/L=25  WR=10.7%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; just touched upper band  •  ONLY when session=asia

### L10.  `T1=T1a AND T4=T4a AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=75  W=29/L=46  WR=38.7%
- Sharpen: sharpest is session_bucket=asia (25/46 of losers there)
- **Sharp: n=28  W=3/L=25  WR=10.7%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; just touched upper band; zscore +2 to +3 deep overbought  •  ONLY when session=asia

### L11.  `T1=T1a AND BBP=BBP0 AND RSI=RSI3`
- Raw: n=74  W=23/L=51  WR=31.1%
- Sharpen: sharpest is T4=T4c (29/51 of losers there)
- **Sharp: n=34  W=5/L=29  WR=14.7%**
- **Dir: ?**  •  1h trend WITH trade; deep below lower band; RSI 40-50 lower neutral  •  ONLY when 4h trend AGAINST trade

### L12.  `H60=H60a AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=74  W=25/L=49  WR=33.8%
- Sharpen: sharpest is H20=H20b (16/49 of losers there)
- **Sharp: n=18  W=2/L=16  WR=11.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when HTF20 slightly aligned

### L13.  `H60=H60a AND RSI=RSI3 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=74  W=25/L=49  WR=33.8%
- Sharpen: sharpest is H20=H20b (16/49 of losers there)
- **Sharp: n=18  W=2/L=16  WR=11.1%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when HTF20 slightly aligned

### L14.  `T1=T1a AND T4=T4a AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=73  W=24/L=49  WR=32.9%
- Sharpen: sharpest is session_bucket=asia (30/49 of losers there)
- **Sharp: n=30  W=0/L=30  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when session=asia

### L15.  `H60=H60a AND T1=T1c AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=73  W=29/L=44  WR=39.7%
- Sharpen: sharpest is H20=H20d (8/44 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when HTF20 mildly against

### L16.  `T4=T4a AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=70  W=19/L=51  WR=27.1%
- Sharpen: sharpest is RSI=RSI4 (45/51 of losers there)
- **Sharp: n=51  W=6/L=45  WR=11.8%**
- **Dir: ?**  •  4h trend WITH trade; zscore +2 to +3 deep overbought; session=asia  •  ONLY when RSI 50-60 upper neutral

### L17.  `H60=H60e AND BBP=BBP2 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=70  W=20/L=50  WR=28.6%
- Sharpen: sharpest is T4=T4a (28/50 of losers there)
- **Sharp: n=33  W=5/L=28  WR=15.2%**
- **Dir: SHORT**  •  HTF60 strongly against; lower third; RSI 50-60 upper neutral  •  ONLY when 4h trend WITH trade

### L18.  `T1=T1c AND T4=T4c AND session_bucket=ny_close`
- Raw: n=69  W=20/L=49  WR=29.0%
- Sharpen: sharpest is H20=H20e (21/49 of losers there)
- **Sharp: n=24  W=3/L=21  WR=12.5%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_close  •  ONLY when HTF20 strongly against

### L19.  `T1=T1a AND T4=T4c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=65  W=11/L=54  WR=16.9%
- Sharpen: sharpest is BBP=BBP0 (16/54 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when deep below lower band

### L20.  `T1=T1a AND T4=T4a AND ZS=ZS3 AND direction_exec=short`
- Raw: n=61  W=24/L=37  WR=39.3%
- Sharpen: sharpest is session_bucket=london_open (8/37 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend WITH trade; zscore -1 to +1 neutral  •  ONLY when session=london_open

### L21.  `H20=H20a AND T4=T4a AND BBP=BBP5`
- Raw: n=60  W=19/L=41  WR=31.7%
- Sharpen: sharpest is direction_exec=long (26/41 of losers there)
- **Sharp: n=28  W=2/L=26  WR=7.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; just touched upper band  •  ONLY when long

### L22.  `T4=T4a AND RSI=RSI4 AND session_bucket=ny_open`
- Raw: n=60  W=19/L=41  WR=31.7%
- Sharpen: sharpest is H20=H20c (17/41 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: ?**  •  4h trend WITH trade; RSI 50-60 upper neutral; session=ny_open  •  ONLY when HTF20 neutral

### L23.  `H20=H20a AND T4=T4a AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=60  W=19/L=41  WR=31.7%
- Sharpen: sharpest is direction_exec=long (26/41 of losers there)
- **Sharp: n=28  W=2/L=26  WR=7.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; just touched upper band; zscore +2 to +3 deep overbought  •  ONLY when long

### L24.  `H60=H60a AND T4=T4c AND ZS=ZS1`
- Raw: n=60  W=23/L=37  WR=38.3%
- Sharpen: sharpest is T1=T1a (18/37 of losers there)
- **Sharp: n=24  W=6/L=18  WR=25.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when 1h trend WITH trade

### L25.  `H60=H60a AND T4=T4c AND ZS=ZS1 AND direction_exec=long`
- Raw: n=60  W=23/L=37  WR=38.3%
- Sharpen: sharpest is T1=T1a (18/37 of losers there)
- **Sharp: n=24  W=6/L=18  WR=25.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when 1h trend WITH trade

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | H60e(49/41) | H60a(39/48) |
| T1 | T1c(54/48) | T1a(46/52) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
