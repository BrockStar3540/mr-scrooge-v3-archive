# GBP_USD — R22 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **4,397**  (W=2,748 / L=1,649)  -  WR: **62.5%**

## Session distribution

- asia: n=1290  W=832/L=458  WR=64.5%
- ny_close: n=1154  W=709/L=445  WR=61.4%
- ny_open: n=579  W=359/L=220  WR=62.0%
- ny_mid: n=476  W=297/L=179  WR=62.4%
- london: n=436  W=256/L=180  WR=58.7%
- london_open: n=241  W=151/L=90  WR=62.7%
- off_hours: n=153  W=102/L=51  WR=66.7%
- asia_late: n=68  W=42/L=26  WR=61.8%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T4=T4a AND BBP=BBP1 AND direction_exec=long`
- Raw: n=129  W=112/L=17  WR=86.8%
- Refine: exclude H60=H60a drops 10/17 losers (59%)
- **Final: n=95  W=88/L=7  WR=92.6%**
- **Dir: LONG**  •  4h trend WITH trade; just touched lower band  •  AVOID when HTF60 aligned WITH trade

### W02.  `T4=T4a AND BBP=BBP1 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=129  W=112/L=17  WR=86.8%
- Refine: exclude H60=H60a drops 10/17 losers (59%)
- **Final: n=95  W=88/L=7  WR=92.6%**
- **Dir: LONG**  •  4h trend WITH trade; just touched lower band; zscore -3 to -2 deep oversold  •  AVOID when HTF60 aligned WITH trade

### W03.  `H60=H60d AND direction_exec=short AND session_bucket=asia`
- Raw: n=117  W=102/L=15  WR=87.2%
- Refine: exclude H20=H20e drops 15/15 losers (100%)
- **Final: n=47  W=47/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 mildly against; session=asia  •  AVOID when HTF20 strongly against

### W04.  `RSI=RSI3 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=115  W=105/L=10  WR=91.3%
- Refine: exclude H60=H60a drops 9/10 losers (90%)
- **Final: n=42  W=41/L=1  WR=97.6%**
- **Dir: SHORT**  •  RSI 40-50 lower neutral; zscore +2 to +3 deep overbought  •  AVOID when HTF60 aligned WITH trade

### W05.  `RSI=RSI4 AND ZS=ZS4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=115  W=99/L=16  WR=86.1%
- Refine: exclude H60=H60e drops 13/16 losers (81%)
- **Final: n=69  W=66/L=3  WR=95.7%**
- **Dir: SHORT**  •  RSI 50-60 upper neutral; zscore +1 to +2 overbought; session=asia  •  AVOID when HTF60 strongly against

### W06.  `T1=T1a AND RSI=RSI3 AND ZS=ZS5`
- Raw: n=110  W=95/L=15  WR=86.4%
- Refine: exclude direction_exec=long drops 5/15 losers (33%)
- **Final: n=105  W=95/L=10  WR=90.5%**
- **Dir: ?**  •  1h trend WITH trade; RSI 40-50 lower neutral; zscore +2 to +3 deep overbought  •  AVOID when long

### W07.  `T1=T1a AND RSI=RSI3 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=105  W=95/L=10  WR=90.5%
- Refine: exclude H60=H60a drops 9/10 losers (90%)
- **Final: n=42  W=41/L=1  WR=97.6%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 40-50 lower neutral; zscore +2 to +3 deep overbought  •  AVOID when HTF60 aligned WITH trade

### W08.  `H20=H20a AND T1=T1c AND T4=T4a AND BBP=BBP1`
- Raw: n=102  W=87/L=15  WR=85.3%
- Refine: exclude session_bucket=ny_mid drops 11/15 losers (73%)
- **Final: n=75  W=71/L=4  WR=94.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; just touched lower band  •  AVOID when session=ny_mid

### W09.  `T1=T1a AND T4=T4a AND RSI=RSI4 AND session_bucket=ny_close`
- Raw: n=100  W=85/L=15  WR=85.0%
- Refine: exclude H20=H20e drops 7/15 losers (47%)
- **Final: n=92  W=84/L=8  WR=91.3%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral; session=ny_close  •  AVOID when HTF20 strongly against

### W10.  `H20=H20a AND H60=H60a AND RSI=RSI4 AND session_bucket=ny_close`
- Raw: n=98  W=92/L=6  WR=93.9%
- Refine: exclude BBP=BBP5 drops 5/6 losers (83%)
- **Final: n=72  W=71/L=1  WR=98.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 50-60 upper neutral; session=ny_close  •  AVOID when just touched upper band

### W11.  `H60=H60d AND T4=T4a AND session_bucket=asia`
- Raw: n=94  W=81/L=13  WR=86.2%
- Refine: exclude H20=H20e drops 10/13 losers (77%)
- **Final: n=64  W=61/L=3  WR=95.3%**
- **Dir: ?**  •  HTF60 mildly against; 4h trend WITH trade; session=asia  •  AVOID when HTF20 strongly against

### W12.  `H60=H60a AND T1=T1a AND T4=T4a AND session_bucket=ny_close`
- Raw: n=94  W=80/L=14  WR=85.1%
- Refine: exclude H20=H20e drops 13/14 losers (93%)
- **Final: n=64  W=63/L=1  WR=98.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; session=ny_close  •  AVOID when HTF20 strongly against

### W13.  `H20=H20a AND H60=H60a AND T1=T1a AND session_bucket=ny_close`
- Raw: n=93  W=90/L=3  WR=96.8%
- Refine: exclude RSI=RSI3 drops 3/3 losers (100%)
- **Final: n=52  W=52/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; session=ny_close  •  AVOID when RSI 40-50 lower neutral

### W14.  `H60=H60d AND T1=T1a AND BBP=BBP6`
- Raw: n=90  W=82/L=8  WR=91.1%
- Refine: exclude session_bucket=london_open drops 8/8 losers (100%)
- **Final: n=61  W=61/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 mildly against; 1h trend WITH trade; deep above upper band  •  AVOID when session=london_open

### W15.  `H20=H20a AND T4=T4a AND BBP=BBP1 AND direction_exec=long`
- Raw: n=90  W=79/L=11  WR=87.8%
- Refine: exclude session_bucket=ny_mid drops 7/11 losers (64%)
- **Final: n=59  W=55/L=4  WR=93.2%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend WITH trade; just touched lower band  •  AVOID when session=ny_mid

### W16.  `H60=H60d AND T1=T1a AND direction_exec=short AND session_bucket=asia`
- Raw: n=88  W=81/L=7  WR=92.0%
- Refine: exclude T4=T4c drops 7/7 losers (100%)
- **Final: n=54  W=54/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 mildly against; 1h trend WITH trade; session=asia  •  AVOID when 4h trend AGAINST trade

### W17.  `H60=H60a AND T1=T1a AND BBP=BBP4 AND session_bucket=ny_close`
- Raw: n=88  W=80/L=8  WR=90.9%
- Refine: exclude RSI=RSI3 drops 8/8 losers (100%)
- **Final: n=34  W=34/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; upper third; session=ny_close  •  AVOID when RSI 40-50 lower neutral

### W18.  `T1=T1c AND T4=T4a AND BBP=BBP1 AND direction_exec=long`
- Raw: n=88  W=75/L=13  WR=85.2%
- Refine: exclude H60=H60a drops 6/13 losers (46%)
- **Final: n=76  W=69/L=7  WR=90.8%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend WITH trade; just touched lower band  •  AVOID when HTF60 aligned WITH trade

### W19.  `H20=H20e AND RSI=RSI3 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=87  W=77/L=10  WR=88.5%
- Refine: exclude session_bucket=asia drops 7/10 losers (70%)
- **Final: n=48  W=45/L=3  WR=93.8%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 40-50 lower neutral; zscore +2 to +3 deep overbought  •  AVOID when session=asia

### W20.  `H20=H20a AND BBP=BBP1 AND session_bucket=asia`
- Raw: n=86  W=77/L=9  WR=89.5%
- Refine: exclude H60=H60a drops 8/9 losers (89%)
- **Final: n=60  W=59/L=1  WR=98.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; just touched lower band; session=asia  •  AVOID when HTF60 aligned WITH trade

### W21.  `H20=H20a AND BBP=BBP1 AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=86  W=77/L=9  WR=89.5%
- Refine: exclude H60=H60a drops 8/9 losers (89%)
- **Final: n=60  W=59/L=1  WR=98.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; just touched lower band; zscore -3 to -2 deep oversold; session=asia  •  AVOID when HTF60 aligned WITH trade

### W22.  `H60=H60a AND T1=T1a AND RSI=RSI4 AND session_bucket=ny_close`
- Raw: n=86  W=77/L=9  WR=89.5%
- Refine: exclude BBP=BBP2 drops 7/9 losers (78%)
- **Final: n=72  W=70/L=2  WR=97.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 50-60 upper neutral; session=ny_close  •  AVOID when lower third

### W23.  `RSI=RSI4 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=82  W=71/L=11  WR=86.6%
- Refine: exclude H60=H60b drops 7/11 losers (64%)
- **Final: n=71  W=67/L=4  WR=94.4%**
- **Dir: LONG**  •  RSI 50-60 upper neutral; session=london_open  •  AVOID when HTF60 slightly aligned

### W24.  `T1=T1a AND T4=T4a AND ZS=ZS5 AND direction_exec=short`
- Raw: n=81  W=72/L=9  WR=88.9%
- Refine: exclude session_bucket=asia drops 7/9 losers (78%)
- **Final: n=48  W=46/L=2  WR=95.8%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when session=asia

### W25.  `H20=H20e AND H60=H60d AND T1=T1a AND RSI=RSI4`
- Raw: n=81  W=70/L=11  WR=86.4%
- Refine: exclude session_bucket=london_open drops 10/11 losers (91%)
- **Final: n=44  W=43/L=1  WR=97.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 mildly against; 1h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when session=london_open

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND H60=H60e AND RSI=RSI4 AND direction_exec=short`
- Raw: n=149  W=51/L=98  WR=34.2%
- Sharpen: sharpest is T1=T1a (47/98 of losers there)
- **Sharp: n=55  W=8/L=47  WR=14.5%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; RSI 50-60 upper neutral  •  ONLY when 1h trend WITH trade

### L02.  `T4=T4c AND ZS=ZS1 AND direction_exec=short`
- Raw: n=146  W=53/L=93  WR=36.3%
- Sharpen: sharpest is BBP=BBP1 (60/93 of losers there)
- **Sharp: n=73  W=13/L=60  WR=17.8%**
- **Dir: SHORT**  •  4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when just touched lower band

### L03.  `T4=T4c AND RSI=RSI3 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=131  W=51/L=80  WR=38.9%
- Sharpen: sharpest is BBP=BBP1 (50/80 of losers there)
- **Sharp: n=63  W=13/L=50  WR=20.6%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when just touched lower band

### L04.  `H20=H20e AND H60=H60e AND ZS=ZS5`
- Raw: n=125  W=46/L=79  WR=36.8%
- Sharpen: sharpest is session_bucket=ny_close (29/79 of losers there)
- **Sharp: n=33  W=4/L=29  WR=12.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; zscore +2 to +3 deep overbought  •  ONLY when session=ny_close

### L05.  `H20=H20e AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=121  W=44/L=77  WR=36.4%
- Sharpen: sharpest is T1=T1c (39/77 of losers there)
- **Sharp: n=47  W=8/L=39  WR=17.0%**
- **Dir: LONG**  •  HTF20 strongly against; session=ny_close  •  ONLY when 1h trend AGAINST trade

### L06.  `H20=H20e AND T1=T1c AND T4=T4c AND session_bucket=ny_close`
- Raw: n=118  W=44/L=74  WR=37.3%
- Sharpen: sharpest is H60=H60e (41/74 of losers there)
- **Sharp: n=41  W=0/L=41  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_close  •  ONLY when HTF60 strongly against

### L07.  `H20=H20e AND H60=H60e AND session_bucket=ny_close`
- Raw: n=113  W=34/L=79  WR=30.1%
- Sharpen: sharpest is T1=T1c (55/79 of losers there)
- **Sharp: n=58  W=3/L=55  WR=5.2%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; session=ny_close  •  ONLY when 1h trend AGAINST trade

### L08.  `H20=H20e AND T4=T4c AND direction_exec=long AND session_bucket=asia`
- Raw: n=113  W=44/L=69  WR=38.9%
- Sharpen: sharpest is H60=H60b (27/69 of losers there)
- **Sharp: n=31  W=4/L=27  WR=12.9%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend AGAINST trade; session=asia  •  ONLY when HTF60 slightly aligned

### L09.  `T4=T4c AND BBP=BBP2 AND RSI=RSI3 AND session_bucket=ny_close`
- Raw: n=108  W=39/L=69  WR=36.1%
- Sharpen: sharpest is H60=H60d (16/69 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: ?**  •  4h trend AGAINST trade; lower third; RSI 40-50 lower neutral; session=ny_close  •  ONLY when HTF60 mildly against

### L10.  `T4=T4c AND RSI=RSI3 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=107  W=40/L=67  WR=37.4%
- Sharpen: sharpest is H60=H60e (30/67 of losers there)
- **Sharp: n=39  W=9/L=30  WR=23.1%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; session=ny_close  •  ONLY when HTF60 strongly against

### L11.  `T1=T1a AND T4=T4c AND ZS=ZS1 AND direction_exec=short`
- Raw: n=106  W=41/L=65  WR=38.7%
- Sharpen: sharpest is BBP=BBP1 (38/65 of losers there)
- **Sharp: n=51  W=13/L=38  WR=25.5%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when just touched lower band

### L12.  `T4=T4c AND RSI=RSI3 AND ZS=ZS2 AND session_bucket=ny_close`
- Raw: n=103  W=37/L=66  WR=35.9%
- Sharpen: sharpest is H60=H60d (15/66 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold; session=ny_close  •  ONLY when HTF60 mildly against

### L13.  `H60=H60b AND T1=T1c AND T4=T4c AND direction_exec=long`
- Raw: n=101  W=40/L=61  WR=39.6%
- Sharpen: sharpest is session_bucket=asia (33/61 of losers there)
- **Sharp: n=37  W=4/L=33  WR=10.8%**
- **Dir: LONG**  •  HTF60 slightly aligned; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when session=asia

### L14.  `T4=T4a AND BBP=BBP6 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=99  W=36/L=63  WR=36.4%
- Sharpen: sharpest is T1=T1c (31/63 of losers there)
- **Sharp: n=37  W=6/L=31  WR=16.2%**
- **Dir: LONG**  •  4h trend WITH trade; deep above upper band; zscore +2 to +3 deep overbought  •  ONLY when 1h trend AGAINST trade

### L15.  `H60=H60e AND T4=T4c AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=99  W=37/L=62  WR=37.4%
- Sharpen: sharpest is T1=T1c (24/62 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend AGAINST trade; session=ny_close  •  ONLY when 1h trend AGAINST trade

### L16.  `H20=H20a AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=97  W=36/L=61  WR=37.1%
- Sharpen: sharpest is BBP=BBP2 (14/61 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; session=ny_mid  •  ONLY when lower third

### L17.  `H20=H20e AND H60=H60e AND T4=T4c AND session_bucket=ny_close`
- Raw: n=96  W=31/L=65  WR=32.3%
- Sharpen: sharpest is T1=T1c (41/65 of losers there)
- **Sharp: n=41  W=0/L=41  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; session=ny_close  •  ONLY when 1h trend AGAINST trade

### L18.  `T4=T4a AND BBP=BBP0 AND direction_exec=short`
- Raw: n=96  W=36/L=60  WR=37.5%
- Sharpen: sharpest is session_bucket=ny_mid (13/60 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: SHORT**  •  4h trend WITH trade; deep below lower band  •  ONLY when session=ny_mid

### L19.  `H20=H20a AND H60=H60a AND T1=T1c AND T4=T4c`
- Raw: n=96  W=36/L=60  WR=37.5%
- Sharpen: sharpest is BBP=BBP2 (13/60 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when lower third

### L20.  `H60=H60b AND direction_exec=long AND session_bucket=asia`
- Raw: n=95  W=34/L=61  WR=35.8%
- Sharpen: sharpest is H20=H20e (27/61 of losers there)
- **Sharp: n=31  W=4/L=27  WR=12.9%**
- **Dir: LONG**  •  HTF60 slightly aligned; session=asia  •  ONLY when HTF20 strongly against

### L21.  `H60=H60b AND T1=T1c AND T4=T4c AND RSI=RSI3`
- Raw: n=92  W=31/L=61  WR=33.7%
- Sharpen: sharpest is H20=H20a (33/61 of losers there)
- **Sharp: n=39  W=6/L=33  WR=15.4%**
- **Dir: ?**  •  HTF60 slightly aligned; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when HTF20 aligned WITH trade

### L22.  `H20=H20a AND T1=T1c AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=91  W=35/L=56  WR=38.5%
- Sharpen: sharpest is BBP=BBP2 (13/56 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_mid  •  ONLY when lower third

### L23.  `BBP=BBP4 AND RSI=RSI4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=91  W=35/L=56  WR=38.5%
- Sharpen: sharpest is T4=T4c (26/56 of losers there)
- **Sharp: n=30  W=4/L=26  WR=13.3%**
- **Dir: LONG**  •  upper third; RSI 50-60 upper neutral; session=asia  •  ONLY when 4h trend AGAINST trade

### L24.  `T1=T1c AND T4=T4a AND BBP=BBP6`
- Raw: n=88  W=33/L=55  WR=37.5%
- Sharpen: sharpest is direction_exec=long (34/55 of losers there)
- **Sharp: n=40  W=6/L=34  WR=15.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; deep above upper band  •  ONLY when long

### L25.  `H60=H60e AND ZS=ZS1 AND direction_exec=short`
- Raw: n=87  W=21/L=66  WR=24.1%
- Sharpen: sharpest is session_bucket=asia (27/66 of losers there)
- **Sharp: n=27  W=0/L=27  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; zscore -3 to -2 deep oversold  •  ONLY when session=asia

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | H60a(40/34) | — |
| T1 | T1a(53/46) | T1c(46/53) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
