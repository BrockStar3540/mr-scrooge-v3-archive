# EUR_USD — R27 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **2,608**  (W=1,661 / L=947)  -  WR: **63.7%**

## Session distribution

- ny_mid: n=866  W=554/L=312  WR=64.0%
- london_open: n=522  W=322/L=200  WR=61.7%
- ny_open: n=505  W=320/L=185  WR=63.4%
- london: n=288  W=195/L=93  WR=67.7%
- ny_close: n=241  W=149/L=92  WR=61.8%
- asia: n=123  W=82/L=41  WR=66.7%
- asia_late: n=63  W=39/L=24  WR=61.9%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20e AND H60=H60e AND T1=T1a AND direction_exec=long`
- Raw: n=160  W=136/L=24  WR=85.0%
- Refine: exclude RSI=RSI4 drops 23/24 losers (96%)
- **Final: n=51  W=50/L=1  WR=98.0%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 strongly against; 1h trend WITH trade  •  AVOID when RSI 50-60 upper neutral

### W02.  `H60=H60e AND T1=T1a AND T4=T4c AND direction_exec=long`
- Raw: n=153  W=132/L=21  WR=86.3%
- Refine: exclude BBP=BBP2 drops 12/21 losers (57%)
- **Final: n=123  W=114/L=9  WR=92.7%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend AGAINST trade  •  AVOID when lower third

### W03.  `T4=T4c AND RSI=RSI3 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=139  W=121/L=18  WR=87.1%
- Refine: exclude H20=H20b drops 7/18 losers (39%)
- **Final: n=129  W=118/L=11  WR=91.5%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when HTF20 slightly aligned

### W04.  `BBP=BBP0 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=131  W=112/L=19  WR=85.5%
- Refine: exclude T4=T4a drops 14/19 losers (74%)
- **Final: n=81  W=76/L=5  WR=93.8%**
- **Dir: LONG**  •  deep below lower band; RSI 40-50 lower neutral  •  AVOID when 4h trend WITH trade

### W05.  `H60=H60a AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=127  W=112/L=15  WR=88.2%
- Refine: exclude H20=H20e drops 9/15 losers (60%)
- **Final: n=93  W=87/L=6  WR=93.5%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; session=ny_open  •  AVOID when HTF20 strongly against

### W06.  `T4=T4c AND BBP=BBP0 AND RSI=RSI3`
- Raw: n=119  W=102/L=17  WR=85.7%
- Refine: exclude direction_exec=short drops 12/17 losers (71%)
- **Final: n=81  W=76/L=5  WR=93.8%**
- **Dir: ?**  •  4h trend AGAINST trade; deep below lower band; RSI 40-50 lower neutral  •  AVOID when short

### W07.  `H60=H60a AND T1=T1a AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=116  W=102/L=14  WR=87.9%
- Refine: exclude H20=H20e drops 8/14 losers (57%)
- **Final: n=91  W=85/L=6  WR=93.4%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=ny_open  •  AVOID when HTF20 strongly against

### W08.  `H20=H20a AND H60=H60a AND T1=T1a AND direction_exec=short`
- Raw: n=112  W=96/L=16  WR=85.7%
- Refine: exclude session_bucket=ny_mid drops 11/16 losers (69%)
- **Final: n=101  W=96/L=5  WR=95.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade  •  AVOID when session=ny_mid

### W09.  `H20=H20a AND RSI=RSI3 AND session_bucket=ny_open`
- Raw: n=109  W=98/L=11  WR=89.9%
- Refine: exclude T4=T4a drops 10/11 losers (91%)
- **Final: n=74  W=73/L=1  WR=98.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 40-50 lower neutral; session=ny_open  •  AVOID when 4h trend WITH trade

### W10.  `H20=H20a AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=103  W=92/L=11  WR=89.3%
- Refine: exclude T4=T4a drops 10/11 losers (91%)
- **Final: n=58  W=57/L=1  WR=98.3%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; session=ny_open  •  AVOID when 4h trend WITH trade

### W11.  `H60=H60e AND BBP=BBP0 AND direction_exec=long`
- Raw: n=103  W=90/L=13  WR=87.4%
- Refine: exclude T4=T4a drops 12/13 losers (92%)
- **Final: n=53  W=52/L=1  WR=98.1%**
- **Dir: LONG**  •  HTF60 strongly against; deep below lower band  •  AVOID when 4h trend WITH trade

### W12.  `H60=H60a AND T1=T1a AND RSI=RSI3 AND session_bucket=ny_open`
- Raw: n=102  W=87/L=15  WR=85.3%
- Refine: exclude T4=T4a drops 9/15 losers (60%)
- **Final: n=74  W=68/L=6  WR=91.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 40-50 lower neutral; session=ny_open  •  AVOID when 4h trend WITH trade

### W13.  `T4=T4c AND BBP=BBP0 AND direction_exec=long`
- Raw: n=101  W=92/L=9  WR=91.1%
- Refine: exclude session_bucket=ny_open drops 4/9 losers (44%)
- **Final: n=95  W=90/L=5  WR=94.7%**
- **Dir: LONG**  •  4h trend AGAINST trade; deep below lower band  •  AVOID when session=ny_open

### W14.  `T1=T1c AND T4=T4a AND RSI=RSI4 AND session_bucket=ny_open`
- Raw: n=100  W=85/L=15  WR=85.0%
- Refine: exclude BBP=BBP4 drops 9/15 losers (60%)
- **Final: n=61  W=55/L=6  WR=90.2%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 50-60 upper neutral; session=ny_open  •  AVOID when upper third

### W15.  `H20=H20a AND BBP=BBP2 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=99  W=87/L=12  WR=87.9%
- Refine: exclude T4=T4a drops 12/12 losers (100%)
- **Final: n=40  W=40/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; lower third; RSI 40-50 lower neutral  •  AVOID when 4h trend WITH trade

### W16.  `H20=H20a AND T1=T1a AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=97  W=90/L=7  WR=92.8%
- Refine: exclude H60=H60c drops 6/7 losers (86%)
- **Final: n=78  W=77/L=1  WR=98.7%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=ny_open  •  AVOID when HTF60 neutral

### W17.  `H20=H20a AND T1=T1a AND T4=T4c AND RSI=RSI3`
- Raw: n=96  W=84/L=12  WR=87.5%
- Refine: exclude BBP=BBP4 drops 7/12 losers (58%)
- **Final: n=85  W=80/L=5  WR=94.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when upper third

### W18.  `T1=T1a AND RSI=RSI3 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=96  W=83/L=13  WR=86.5%
- Refine: exclude H20=H20b drops 7/13 losers (54%)
- **Final: n=81  W=75/L=6  WR=92.6%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 40-50 lower neutral; session=london_open  •  AVOID when HTF20 slightly aligned

### W19.  `H20=H20a AND T4=T4c AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=96  W=82/L=14  WR=85.4%
- Refine: exclude direction_exec=long drops 14/14 losers (100%)
- **Final: n=40  W=40/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; lower third; RSI 40-50 lower neutral  •  AVOID when long

### W20.  `H20=H20e AND T4=T4c AND ZS=ZS1 AND direction_exec=long`
- Raw: n=94  W=85/L=9  WR=90.4%
- Refine: exclude H60=H60c drops 5/9 losers (56%)
- **Final: n=87  W=83/L=4  WR=95.4%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  AVOID when HTF60 neutral

### W21.  `H60=H60a AND RSI=RSI3 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=94  W=85/L=9  WR=90.4%
- Refine: exclude ZS=ZS1 drops 8/9 losers (89%)
- **Final: n=66  W=65/L=1  WR=98.5%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral; session=ny_open  •  AVOID when zscore -3 to -2 deep oversold

### W22.  `H20=H20a AND T1=T1a AND BBP=BBP2 AND direction_exec=short`
- Raw: n=93  W=83/L=10  WR=89.2%
- Refine: exclude RSI=RSI4 drops 4/10 losers (40%)
- **Final: n=88  W=82/L=6  WR=93.2%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend WITH trade; lower third  •  AVOID when RSI 50-60 upper neutral

### W23.  `H20=H20e AND T1=T1a AND RSI=RSI3 AND session_bucket=london_open`
- Raw: n=93  W=82/L=11  WR=88.2%
- Refine: exclude H60=H60a drops 9/11 losers (82%)
- **Final: n=66  W=64/L=2  WR=97.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; RSI 40-50 lower neutral; session=london_open  •  AVOID when HTF60 aligned WITH trade

### W24.  `T4=T4c AND BBP=BBP0 AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=93  W=82/L=11  WR=88.2%
- Refine: exclude session_bucket=ny_mid drops 7/11 losers (64%)
- **Final: n=82  W=78/L=4  WR=95.1%**
- **Dir: ?**  •  4h trend AGAINST trade; deep below lower band; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when session=ny_mid

### W25.  `H60=H60e AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=91  W=82/L=9  WR=90.1%
- Refine: exclude direction_exec=long drops 8/9 losers (89%)
- **Final: n=43  W=42/L=1  WR=97.7%**
- **Dir: ?**  •  HTF60 strongly against; just touched upper band; zscore +2 to +3 deep overbought  •  AVOID when long

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20a AND H60=H60a AND T1=T1c AND direction_exec=short`
- Raw: n=125  W=43/L=82  WR=34.4%
- Sharpen: sharpest is session_bucket=ny_mid (14/82 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade  •  ONLY when session=ny_mid

### L02.  `T1=T1c AND direction_exec=long AND session_bucket=london_open`
- Raw: n=123  W=47/L=76  WR=38.2%
- Sharpen: sharpest is RSI=RSI3 (59/76 of losers there)
- **Sharp: n=81  W=22/L=59  WR=27.2%**
- **Dir: LONG**  •  1h trend AGAINST trade; session=london_open  •  ONLY when RSI 40-50 lower neutral

### L03.  `T4=T4a AND ZS=ZS1 AND direction_exec=short`
- Raw: n=115  W=46/L=69  WR=40.0%
- Sharpen: sharpest is H60=H60a (35/69 of losers there)
- **Sharp: n=44  W=9/L=35  WR=20.5%**
- **Dir: SHORT**  •  4h trend WITH trade; zscore -3 to -2 deep oversold  •  ONLY when HTF60 aligned WITH trade

### L04.  `T4=T4a AND BBP=BBP2 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=113  W=44/L=69  WR=38.9%
- Sharpen: sharpest is session_bucket=ny_open (27/69 of losers there)
- **Sharp: n=27  W=0/L=27  WR=0.0%**
- **Dir: LONG**  •  4h trend WITH trade; lower third; RSI 40-50 lower neutral  •  ONLY when session=ny_open

### L05.  `T4=T4a AND RSI=RSI3 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=105  W=39/L=66  WR=37.1%
- Sharpen: sharpest is session_bucket=ny_open (27/66 of losers there)
- **Sharp: n=27  W=0/L=27  WR=0.0%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  ONLY when session=ny_open

### L06.  `T4=T4a AND BBP=BBP1 AND RSI=RSI3`
- Raw: n=105  W=42/L=63  WR=40.0%
- Sharpen: sharpest is H20=H20e (28/63 of losers there)
- **Sharp: n=30  W=2/L=28  WR=6.7%**
- **Dir: ?**  •  4h trend WITH trade; just touched lower band; RSI 40-50 lower neutral  •  ONLY when HTF20 strongly against

### L07.  `T4=T4a AND BBP=BBP1 AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=105  W=42/L=63  WR=40.0%
- Sharpen: sharpest is H20=H20e (28/63 of losers there)
- **Sharp: n=30  W=2/L=28  WR=6.7%**
- **Dir: ?**  •  4h trend WITH trade; just touched lower band; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when HTF20 strongly against

### L08.  `H20=H20e AND H60=H60e AND BBP=BBP2`
- Raw: n=104  W=39/L=65  WR=37.5%
- Sharpen: sharpest is T4=T4a (28/65 of losers there)
- **Sharp: n=30  W=2/L=28  WR=6.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; lower third  •  ONLY when 4h trend WITH trade

### L09.  `H60=H60a AND T1=T1c AND session_bucket=london_open`
- Raw: n=100  W=40/L=60  WR=40.0%
- Sharpen: sharpest is RSI=RSI3 (28/60 of losers there)
- **Sharp: n=37  W=9/L=28  WR=24.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=london_open  •  ONLY when RSI 40-50 lower neutral

### L10.  `T4=T4a AND RSI=RSI3 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=98  W=36/L=62  WR=36.7%
- Sharpen: sharpest is H20=H20e (27/62 of losers there)
- **Sharp: n=29  W=2/L=27  WR=6.9%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when HTF20 strongly against

### L11.  `H60=H60e AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=98  W=39/L=59  WR=39.8%
- Sharpen: sharpest is H20=H20e (41/59 of losers there)
- **Sharp: n=43  W=2/L=41  WR=4.7%**
- **Dir: LONG**  •  HTF60 strongly against; session=ny_open  •  ONLY when HTF20 strongly against

### L12.  `H20=H20e AND H60=H60e AND ZS=ZS2`
- Raw: n=97  W=36/L=61  WR=37.1%
- Sharpen: sharpest is T4=T4a (28/61 of losers there)
- **Sharp: n=30  W=2/L=28  WR=6.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; zscore -2 to -1 oversold  •  ONLY when 4h trend WITH trade

### L13.  `H20=H20e AND H60=H60e AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=97  W=36/L=61  WR=37.1%
- Sharpen: sharpest is T4=T4a (28/61 of losers there)
- **Sharp: n=30  W=2/L=28  WR=6.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; lower third; zscore -2 to -1 oversold  •  ONLY when 4h trend WITH trade

### L14.  `H20=H20e AND T1=T1c AND session_bucket=ny_open`
- Raw: n=95  W=35/L=60  WR=36.8%
- Sharpen: sharpest is direction_exec=long (59/60 of losers there)
- **Sharp: n=65  W=6/L=59  WR=9.2%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; session=ny_open  •  ONLY when long

### L15.  `H60=H60e AND T1=T1c AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=92  W=35/L=57  WR=38.0%
- Sharpen: sharpest is H20=H20e (41/57 of losers there)
- **Sharp: n=43  W=2/L=41  WR=4.7%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend AGAINST trade; session=ny_open  •  ONLY when HTF20 strongly against

### L16.  `H60=H60e AND RSI=RSI3 AND session_bucket=ny_open`
- Raw: n=86  W=32/L=54  WR=37.2%
- Sharpen: sharpest is H20=H20e (42/54 of losers there)
- **Sharp: n=50  W=8/L=42  WR=16.0%**
- **Dir: ?**  •  HTF60 strongly against; RSI 40-50 lower neutral; session=ny_open  •  ONLY when HTF20 strongly against

### L17.  `H20=H20a AND H60=H60a AND RSI=RSI4 AND direction_exec=short`
- Raw: n=86  W=33/L=53  WR=38.4%
- Sharpen: sharpest is session_bucket=ny_mid (14/53 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 50-60 upper neutral  •  ONLY when session=ny_mid

### L18.  `T1=T1c AND RSI=RSI3 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=81  W=22/L=59  WR=27.2%
- Sharpen: sharpest is T4=T4c (28/59 of losers there)
- **Sharp: n=32  W=4/L=28  WR=12.5%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 40-50 lower neutral; session=london_open  •  ONLY when 4h trend AGAINST trade

### L19.  `H60=H60e AND T1=T1c AND RSI=RSI3 AND session_bucket=ny_open`
- Raw: n=81  W=29/L=52  WR=35.8%
- Sharpen: sharpest is H20=H20e (41/52 of losers there)
- **Sharp: n=49  W=8/L=41  WR=16.3%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 40-50 lower neutral; session=ny_open  •  ONLY when HTF20 strongly against

### L20.  `H60=H60a AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=81  W=30/L=51  WR=37.0%
- Sharpen: sharpest is direction_exec=long (25/51 of losers there)
- **Sharp: n=27  W=2/L=25  WR=7.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; just touched upper band; zscore +2 to +3 deep overbought  •  ONLY when long

### L21.  `H20=H20e AND BBP=BBP2 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=79  W=31/L=48  WR=39.2%
- Sharpen: sharpest is T4=T4a (22/48 of losers there)
- **Sharp: n=22  W=0/L=22  WR=0.0%**
- **Dir: LONG**  •  HTF20 strongly against; lower third; RSI 40-50 lower neutral  •  ONLY when 4h trend WITH trade

### L22.  `H20=H20e AND T4=T4a AND BBP=BBP2`
- Raw: n=78  W=25/L=53  WR=32.1%
- Sharpen: sharpest is H60=H60e (28/53 of losers there)
- **Sharp: n=30  W=2/L=28  WR=6.7%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; lower third  •  ONLY when HTF60 strongly against

### L23.  `H20=H20e AND H60=H60e AND T4=T4a AND RSI=RSI3`
- Raw: n=76  W=28/L=48  WR=36.8%
- Sharpen: sharpest is direction_exec=long (36/48 of losers there)
- **Sharp: n=38  W=2/L=36  WR=5.3%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when long

### L24.  `H20=H20a AND H60=H60a AND session_bucket=ny_mid`
- Raw: n=75  W=27/L=48  WR=36.0%
- Sharpen: sharpest is direction_exec=short (25/48 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=ny_mid  •  ONLY when short

### L25.  `H20=H20a AND H60=H60a AND T1=T1c AND session_bucket=london_open`
- Raw: n=75  W=29/L=46  WR=38.7%
- Sharpen: sharpest is RSI=RSI3 (18/46 of losers there)
- **Sharp: n=20  W=2/L=18  WR=10.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade; session=london_open  •  ONLY when RSI 40-50 lower neutral

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | H60e(42/36) | H60a(35/42) |
| T1 | — | — |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
