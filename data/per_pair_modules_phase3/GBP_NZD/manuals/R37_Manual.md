# GBP_NZD — R37 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_3**  (5m ATR >120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **3,283**  (W=1,889 / L=1,394)  -  WR: **57.5%**

## Session distribution

- ny_mid: n=928  W=529/L=399  WR=57.0%
- asia: n=834  W=488/L=346  WR=58.5%
- london_open: n=654  W=397/L=257  WR=60.7%
- london: n=241  W=143/L=98  WR=59.3%
- ny_open: n=198  W=102/L=96  WR=51.5%
- asia_late: n=194  W=112/L=82  WR=57.7%
- ny_close: n=180  W=89/L=91  WR=49.4%
- off_hours: n=54  W=29/L=25  WR=53.7%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60e AND T1=T1a AND session_bucket=ny_mid`
- Raw: n=131  W=113/L=18  WR=86.3%
- Refine: exclude ZS=ZS2 drops 10/18 losers (56%)
- **Final: n=110  W=102/L=8  WR=92.7%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; session=ny_mid  •  AVOID when zscore -2 to -1 oversold

### W02.  `H20=H20a AND T1=T1a AND T4=T4c AND session_bucket=asia`
- Raw: n=92  W=81/L=11  WR=88.0%
- Refine: exclude RSI=RSI4 drops 11/11 losers (100%)
- **Final: n=49  W=49/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade; session=asia  •  AVOID when RSI 50-60 upper neutral

### W03.  `T1=T1a AND BBP=BBP2 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=87  W=75/L=12  WR=86.2%
- Refine: exclude H60=H60e drops 9/12 losers (75%)
- **Final: n=56  W=53/L=3  WR=94.6%**
- **Dir: LONG**  •  1h trend WITH trade; lower third; RSI 50-60 upper neutral  •  AVOID when HTF60 strongly against

### W04.  `T1=T1a AND T4=T4c AND ZS=ZS5 AND session_bucket=ny_mid`
- Raw: n=85  W=77/L=8  WR=90.6%
- Refine: exclude H60=H60c drops 7/8 losers (88%)
- **Final: n=57  W=56/L=1  WR=98.2%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought; session=ny_mid  •  AVOID when HTF60 neutral

### W05.  `H20=H20e AND T1=T1a AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=81  W=73/L=8  WR=90.1%
- Refine: exclude T4=T4a drops 8/8 losers (100%)
- **Final: n=51  W=51/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend WITH trade; session=ny_mid  •  AVOID when 4h trend WITH trade

### W06.  `H60=H60e AND T1=T1a AND T4=T4c AND ZS=ZS5`
- Raw: n=80  W=68/L=12  WR=85.0%
- Refine: exclude session_bucket=ny_open drops 8/12 losers (67%)
- **Final: n=72  W=68/L=4  WR=94.4%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  AVOID when session=ny_open

### W07.  `H60=H60e AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=75  W=69/L=6  WR=92.0%
- Refine: exclude H20=H20b drops 6/6 losers (100%)
- **Final: n=51  W=51/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; session=ny_mid  •  AVOID when HTF20 slightly aligned

### W08.  `H60=H60e AND T4=T4c AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=75  W=69/L=6  WR=92.0%
- Refine: exclude H20=H20b drops 6/6 losers (100%)
- **Final: n=51  W=51/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 50-60 upper neutral; session=ny_mid  •  AVOID when HTF20 slightly aligned

### W09.  `H20=H20e AND T1=T1a AND ZS=ZS5 AND session_bucket=ny_mid`
- Raw: n=74  W=67/L=7  WR=90.5%
- Refine: exclude H60=H60c drops 7/7 losers (100%)
- **Final: n=46  W=46/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; zscore +2 to +3 deep overbought; session=ny_mid  •  AVOID when HTF60 neutral

### W10.  `H20=H20a AND RSI=RSI3 AND direction_exec=short AND session_bucket=asia`
- Raw: n=74  W=65/L=9  WR=87.8%
- Refine: exclude T4=T4a drops 6/9 losers (67%)
- **Final: n=63  W=60/L=3  WR=95.2%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 40-50 lower neutral; session=asia  •  AVOID when 4h trend WITH trade

### W11.  `T1=T1a AND RSI=RSI4 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=73  W=64/L=9  WR=87.7%
- Refine: exclude H20=H20e drops 7/9 losers (78%)
- **Final: n=44  W=42/L=2  WR=95.5%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 50-60 upper neutral; zscore -2 to -1 oversold  •  AVOID when HTF20 strongly against

### W12.  `BBP=BBP5 AND RSI=RSI4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=73  W=64/L=9  WR=87.7%
- Refine: exclude H60=H60e drops 9/9 losers (100%)
- **Final: n=50  W=50/L=0  WR=100.0%**
- **Dir: SHORT**  •  just touched upper band; RSI 50-60 upper neutral; session=asia  •  AVOID when HTF60 strongly against

### W13.  `RSI=RSI4 AND ZS=ZS5 AND direction_exec=short AND session_bucket=asia`
- Raw: n=73  W=64/L=9  WR=87.7%
- Refine: exclude H60=H60e drops 9/9 losers (100%)
- **Final: n=50  W=50/L=0  WR=100.0%**
- **Dir: SHORT**  •  RSI 50-60 upper neutral; zscore +2 to +3 deep overbought; session=asia  •  AVOID when HTF60 strongly against

### W14.  `T4=T4c AND RSI=RSI3 AND direction_exec=short AND session_bucket=asia`
- Raw: n=71  W=62/L=9  WR=87.3%
- Refine: exclude ZS=ZS4 drops 5/9 losers (56%)
- **Final: n=64  W=60/L=4  WR=93.8%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; session=asia  •  AVOID when zscore +1 to +2 overbought

### W15.  `H60=H60e AND T1=T1a AND BBP=BBP1`
- Raw: n=70  W=65/L=5  WR=92.9%
- Refine: exclude session_bucket=london drops 4/5 losers (80%)
- **Final: n=66  W=65/L=1  WR=98.5%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; just touched lower band  •  AVOID when session=london

### W16.  `H60=H60e AND T1=T1a AND BBP=BBP1 AND ZS=ZS1`
- Raw: n=70  W=65/L=5  WR=92.9%
- Refine: exclude session_bucket=london drops 4/5 losers (80%)
- **Final: n=66  W=65/L=1  WR=98.5%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; just touched lower band; zscore -3 to -2 deep oversold  •  AVOID when session=london

### W17.  `H60=H60e AND BBP=BBP1 AND direction_exec=long`
- Raw: n=69  W=64/L=5  WR=92.8%
- Refine: exclude session_bucket=ny_close drops 2/5 losers (40%)
- **Final: n=65  W=62/L=3  WR=95.4%**
- **Dir: LONG**  •  HTF60 strongly against; just touched lower band  •  AVOID when session=ny_close

### W18.  `H60=H60e AND BBP=BBP1 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=69  W=64/L=5  WR=92.8%
- Refine: exclude session_bucket=ny_close drops 2/5 losers (40%)
- **Final: n=65  W=62/L=3  WR=95.4%**
- **Dir: LONG**  •  HTF60 strongly against; just touched lower band; zscore -3 to -2 deep oversold  •  AVOID when session=ny_close

### W19.  `H20=H20e AND ZS=ZS5 AND direction_exec=short`
- Raw: n=68  W=61/L=7  WR=89.7%
- Refine: exclude H60=H60c drops 7/7 losers (100%)
- **Final: n=40  W=40/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 strongly against; zscore +2 to +3 deep overbought  •  AVOID when HTF60 neutral

### W20.  `H20=H20e AND T4=T4c AND ZS=ZS5 AND direction_exec=short`
- Raw: n=66  W=59/L=7  WR=89.4%
- Refine: exclude H60=H60c drops 7/7 losers (100%)
- **Final: n=38  W=38/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  AVOID when HTF60 neutral

### W21.  `H20=H20e AND RSI=RSI4 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=65  W=58/L=7  WR=89.2%
- Refine: exclude H60=H60c drops 7/7 losers (100%)
- **Final: n=40  W=40/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when HTF60 neutral

### W22.  `T4=T4c AND ZS=ZS5 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=65  W=56/L=9  WR=86.2%
- Refine: exclude H60=H60b drops 8/9 losers (89%)
- **Final: n=57  W=56/L=1  WR=98.2%**
- **Dir: LONG**  •  4h trend AGAINST trade; zscore +2 to +3 deep overbought; session=ny_mid  •  AVOID when HTF60 slightly aligned

### W23.  `T1=T1a AND T4=T4a AND BBP=BBP1 AND direction_exec=long`
- Raw: n=63  W=55/L=8  WR=87.3%
- Refine: exclude H20=H20c drops 7/8 losers (88%)
- **Final: n=56  W=55/L=1  WR=98.2%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; just touched lower band  •  AVOID when HTF20 neutral

### W24.  `H60=H60e AND RSI=RSI4 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=62  W=57/L=5  WR=91.9%
- Refine: exclude T4=T4a drops 5/5 losers (100%)
- **Final: n=51  W=51/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 strongly against; RSI 50-60 upper neutral; session=ny_mid  •  AVOID when 4h trend WITH trade

### W25.  `H60=H60e AND T4=T4a AND BBP=BBP1 AND direction_exec=long`
- Raw: n=61  W=56/L=5  WR=91.8%
- Refine: exclude RSI=RSI3 drops 5/5 losers (100%)
- **Final: n=22  W=22/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend WITH trade; just touched lower band  •  AVOID when RSI 40-50 lower neutral

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=397  W=158/L=239  WR=39.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=397  W=158/L=239  WR=39.8%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral

### L02.  `H20=H20e AND RSI=RSI3 AND direction_exec=long`
- Raw: n=264  W=104/L=160  WR=39.4%
- Sharpen: sharpest is session_bucket=ny_close (38/160 of losers there)
- **Sharp: n=41  W=3/L=38  WR=7.3%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 40-50 lower neutral  •  ONLY when session=ny_close

### L03.  `RSI=RSI4 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=220  W=78/L=142  WR=35.5%
- Sharpen: sharpest is H60=H60a (50/142 of losers there)
- **Sharp: n=52  W=2/L=50  WR=3.8%**
- **Dir: SHORT**  •  RSI 50-60 upper neutral; session=ny_mid  •  ONLY when HTF60 aligned WITH trade

### L04.  `H60=H60a AND T1=T1c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=217  W=83/L=134  WR=38.2%
- Sharpen: sharpest is H20=H20e (61/134 of losers there)
- **Sharp: n=86  W=25/L=61  WR=29.1%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when HTF20 strongly against

### L05.  `T1=T1c AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=193  W=75/L=118  WR=38.9%
- Sharpen: sharpest is H20=H20a (53/118 of losers there)
- **Sharp: n=56  W=3/L=53  WR=5.4%**
- **Dir: SHORT**  •  1h trend AGAINST trade; session=ny_mid  •  ONLY when HTF20 aligned WITH trade

### L06.  `H20=H20a AND T1=T1c AND T4=T4a AND direction_exec=short`
- Raw: n=193  W=75/L=118  WR=38.9%
- Sharpen: sharpest is RSI=RSI4 (81/118 of losers there)
- **Sharp: n=103  W=22/L=81  WR=21.4%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when RSI 50-60 upper neutral

### L07.  `H20=H20e AND H60=H60a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=183  W=65/L=118  WR=35.5%
- Sharpen: sharpest is session_bucket=ny_close (33/118 of losers there)
- **Sharp: n=34  W=1/L=33  WR=2.9%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 aligned WITH trade; RSI 40-50 lower neutral  •  ONLY when session=ny_close

### L08.  `H20=H20a AND T4=T4a AND RSI=RSI4 AND direction_exec=short`
- Raw: n=177  W=66/L=111  WR=37.3%
- Sharpen: sharpest is T1=T1c (81/111 of losers there)
- **Sharp: n=103  W=22/L=81  WR=21.4%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when 1h trend AGAINST trade

### L09.  `T4=T4a AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=174  W=64/L=110  WR=36.8%
- Sharpen: sharpest is H20=H20a (75/110 of losers there)
- **Sharp: n=85  W=10/L=75  WR=11.8%**
- **Dir: ?**  •  4h trend WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when HTF20 aligned WITH trade

### L10.  `H20=H20a AND T1=T1c AND RSI=RSI4 AND direction_exec=short`
- Raw: n=158  W=48/L=110  WR=30.4%
- Sharpen: sharpest is session_bucket=ny_mid (53/110 of losers there)
- **Sharp: n=56  W=3/L=53  WR=5.4%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when session=ny_mid

### L11.  `H60=H60c AND T4=T4c AND direction_exec=long`
- Raw: n=157  W=58/L=99  WR=36.9%
- Sharpen: sharpest is ZS=ZS4 (39/99 of losers there)
- **Sharp: n=51  W=12/L=39  WR=23.5%**
- **Dir: LONG**  •  HTF60 neutral; 4h trend AGAINST trade  •  ONLY when zscore +1 to +2 overbought

### L12.  `H60=H60a AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=157  W=60/L=97  WR=38.2%
- Sharpen: sharpest is BBP=BBP1 (63/97 of losers there)
- **Sharp: n=90  W=27/L=63  WR=30.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when just touched lower band

### L13.  `H20=H20a AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=143  W=56/L=87  WR=39.2%
- Sharpen: sharpest is ZS=ZS5 (51/87 of losers there)
- **Sharp: n=52  W=1/L=51  WR=1.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 50-60 upper neutral; session=ny_mid  •  ONLY when zscore +2 to +3 deep overbought

### L14.  `H20=H20e AND H60=H60a AND T1=T1c AND direction_exec=long`
- Raw: n=142  W=48/L=94  WR=33.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=142  W=48/L=94  WR=33.8%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend AGAINST trade

### L15.  `T1=T1c AND RSI=RSI4 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=133  W=43/L=90  WR=32.3%
- Sharpen: sharpest is H20=H20a (53/90 of losers there)
- **Sharp: n=56  W=3/L=53  WR=5.4%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; session=ny_mid  •  ONLY when HTF20 aligned WITH trade

### L16.  `H20=H20e AND T1=T1c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=133  W=46/L=87  WR=34.6%
- Sharpen: sharpest is session_bucket=asia (30/87 of losers there)
- **Sharp: n=35  W=5/L=30  WR=14.3%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when session=asia

### L17.  `T4=T4a AND ZS=ZS5 AND direction_exec=short`
- Raw: n=130  W=50/L=80  WR=38.5%
- Sharpen: sharpest is session_bucket=ny_mid (53/80 of losers there)
- **Sharp: n=55  W=2/L=53  WR=3.6%**
- **Dir: SHORT**  •  4h trend WITH trade; zscore +2 to +3 deep overbought  •  ONLY when session=ny_mid

### L18.  `H20=H20a AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=128  W=38/L=90  WR=29.7%
- Sharpen: sharpest is T4=T4a (75/90 of losers there)
- **Sharp: n=85  W=10/L=75  WR=11.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when 4h trend WITH trade

### L19.  `H60=H60a AND T4=T4c AND ZS=ZS1`
- Raw: n=128  W=50/L=78  WR=39.1%
- Sharpen: sharpest is session_bucket=ny_close (17/78 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when session=ny_close

### L20.  `H60=H60c AND BBP=BBP4 AND direction_exec=long`
- Raw: n=120  W=45/L=75  WR=37.5%
- Sharpen: sharpest is T4=T4c (43/75 of losers there)
- **Sharp: n=60  W=17/L=43  WR=28.3%**
- **Dir: LONG**  •  HTF60 neutral; upper third  •  ONLY when 4h trend AGAINST trade

### L21.  `H60=H60a AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=118  W=47/L=71  WR=39.8%
- Sharpen: sharpest is ZS=ZS3 (24/71 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; session=ny_mid  •  ONLY when zscore -1 to +1 neutral

### L22.  `T4=T4a AND RSI=RSI4 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=117  W=44/L=73  WR=37.6%
- Sharpen: sharpest is session_bucket=ny_mid (53/73 of losers there)
- **Sharp: n=55  W=2/L=53  WR=3.6%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when session=ny_mid

### L23.  `T4=T4a AND BBP=BBP2 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=115  W=40/L=75  WR=34.8%
- Sharpen: sharpest is session_bucket=ny_open (15/75 of losers there)
- **Sharp: n=16  W=1/L=15  WR=6.2%**
- **Dir: LONG**  •  4h trend WITH trade; lower third; RSI 40-50 lower neutral  •  ONLY when session=ny_open

### L24.  `H60=H60a AND T1=T1c AND ZS=ZS5`
- Raw: n=115  W=42/L=73  WR=36.5%
- Sharpen: sharpest is T4=T4a (58/73 of losers there)
- **Sharp: n=61  W=3/L=58  WR=4.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when 4h trend WITH trade

### L25.  `H20=H20a AND H60=H60a AND RSI=RSI4 AND direction_exec=short`
- Raw: n=114  W=38/L=76  WR=33.3%
- Sharpen: sharpest is ZS=ZS5 (48/76 of losers there)
- **Sharp: n=48  W=0/L=48  WR=0.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 50-60 upper neutral  •  ONLY when zscore +2 to +3 deep overbought

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | H60e(38/31) | H60a(30/38) |
| T1 | T1a(54/49) | T1c(46/51) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(54/45) | long(46/55) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
