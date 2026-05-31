# GBP_NZD — R31 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20d**  (EMA20 down 0.15-0.5x)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **4,616**  (W=2,675 / L=1,941)  -  WR: **58.0%**

## Session distribution

- asia: n=1327  W=790/L=537  WR=59.5%
- london_open: n=846  W=499/L=347  WR=59.0%
- ny_mid: n=759  W=439/L=320  WR=57.8%
- ny_open: n=602  W=333/L=269  WR=55.3%
- ny_close: n=505  W=286/L=219  WR=56.6%
- london: n=200  W=129/L=71  WR=64.5%
- asia_late: n=190  W=108/L=82  WR=56.8%
- off_hours: n=187  W=91/L=96  WR=48.7%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20e AND T1=T1a AND T4=T4c AND session_bucket=asia`
- Raw: n=128  W=109/L=19  WR=85.2%
- Refine: exclude H60=H60a drops 14/19 losers (74%)
- **Final: n=74  W=69/L=5  WR=93.2%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; session=asia  •  AVOID when HTF60 aligned WITH trade

### W02.  `T4=T4c AND BBP=BBP4 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=116  W=102/L=14  WR=87.9%
- Refine: exclude session_bucket=ny_close drops 9/14 losers (64%)
- **Final: n=100  W=95/L=5  WR=95.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; upper third; RSI 40-50 lower neutral  •  AVOID when session=ny_close

### W03.  `H20=H20a AND T1=T1c AND T4=T4c AND direction_exec=short`
- Raw: n=107  W=97/L=10  WR=90.7%
- Refine: exclude session_bucket=london_open drops 8/10 losers (80%)
- **Final: n=75  W=73/L=2  WR=97.3%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade  •  AVOID when session=london_open

### W04.  `H60=H60a AND BBP=BBP4 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=98  W=84/L=14  WR=85.7%
- Refine: exclude T4=T4a drops 13/14 losers (93%)
- **Final: n=58  W=57/L=1  WR=98.3%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; upper third; RSI 40-50 lower neutral  •  AVOID when 4h trend WITH trade

### W05.  `H60=H60e AND T1=T1c AND T4=T4c AND BBP=BBP0`
- Raw: n=92  W=79/L=13  WR=85.9%
- Refine: exclude ZS=ZS1 drops 13/13 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; deep below lower band  •  AVOID when zscore -3 to -2 deep oversold

### W06.  `H20=H20a AND T4=T4c AND BBP=BBP4 AND direction_exec=short`
- Raw: n=90  W=77/L=13  WR=85.6%
- Refine: exclude session_bucket=london_open drops 8/13 losers (62%)
- **Final: n=71  W=66/L=5  WR=93.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; upper third  •  AVOID when session=london_open

### W07.  `BBP=BBP4 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=84  W=74/L=10  WR=88.1%
- Refine: exclude H60=H60d drops 5/10 losers (50%)
- **Final: n=74  W=69/L=5  WR=93.2%**
- **Dir: LONG**  •  upper third; RSI 50-60 upper neutral  •  AVOID when HTF60 mildly against

### W08.  `H60=H60c AND T1=T1a AND T4=T4c AND session_bucket=asia`
- Raw: n=82  W=74/L=8  WR=90.2%
- Refine: exclude BBP=BBP1 drops 4/8 losers (50%)
- **Final: n=67  W=63/L=4  WR=94.0%**
- **Dir: ?**  •  HTF60 neutral; 1h trend WITH trade; 4h trend AGAINST trade; session=asia  •  AVOID when just touched lower band

### W09.  `T1=T1a AND BBP=BBP3 AND session_bucket=london_open`
- Raw: n=82  W=70/L=12  WR=85.4%
- Refine: exclude strategy_id=bravo_failed_momentum drops 4/12 losers (33%)
- **Final: n=76  W=68/L=8  WR=89.5%**
- **Dir: ?**  •  1h trend WITH trade; middle of band; session=london_open  •  AVOID when strategy=bravo_failed_momentum

### W10.  `T1=T1a AND BBP=BBP3 AND ZS=ZS3 AND session_bucket=london_open`
- Raw: n=82  W=70/L=12  WR=85.4%
- Refine: exclude strategy_id=bravo_failed_momentum drops 4/12 losers (33%)
- **Final: n=76  W=68/L=8  WR=89.5%**
- **Dir: ?**  •  1h trend WITH trade; middle of band; zscore -1 to +1 neutral; session=london_open  •  AVOID when strategy=bravo_failed_momentum

### W11.  `H20=H20e AND H60=H60c AND BBP=BBP3 AND RSI=RSI3`
- Raw: n=80  W=69/L=11  WR=86.2%
- Refine: exclude session_bucket=asia drops 6/11 losers (55%)
- **Final: n=62  W=57/L=5  WR=91.9%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 neutral; middle of band; RSI 40-50 lower neutral  •  AVOID when session=asia

### W12.  `T4=T4c AND RSI=RSI4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=79  W=68/L=11  WR=86.1%
- Refine: exclude ZS=ZS5 drops 8/11 losers (73%)
- **Final: n=54  W=51/L=3  WR=94.4%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 50-60 upper neutral; session=asia  •  AVOID when zscore +2 to +3 deep overbought

### W13.  `T4=T4c AND RSI=RSI3 AND session_bucket=asia_late`
- Raw: n=77  W=71/L=6  WR=92.2%
- Refine: exclude H20=H20a drops 5/6 losers (83%)
- **Final: n=42  W=41/L=1  WR=97.6%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; session=asia_late  •  AVOID when HTF20 aligned WITH trade

### W14.  `H60=H60b AND T1=T1a AND session_bucket=asia`
- Raw: n=77  W=70/L=7  WR=90.9%
- Refine: exclude H20=H20b drops 4/7 losers (57%)
- **Final: n=61  W=58/L=3  WR=95.1%**
- **Dir: ?**  •  HTF60 slightly aligned; 1h trend WITH trade; session=asia  •  AVOID when HTF20 slightly aligned

### W15.  `H60=H60b AND T1=T1a AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=77  W=70/L=7  WR=90.9%
- Refine: exclude H20=H20b drops 4/7 losers (57%)
- **Final: n=61  W=58/L=3  WR=95.1%**
- **Dir: ?**  •  HTF60 slightly aligned; 1h trend WITH trade; RSI 40-50 lower neutral; session=asia  •  AVOID when HTF20 slightly aligned

### W16.  `T1=T1a AND BBP=BBP3 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=75  W=64/L=11  WR=85.3%
- Refine: exclude strategy_id=bravo_failed_momentum drops 3/11 losers (27%)
- **Final: n=71  W=63/L=8  WR=88.7%**
- **Dir: SHORT**  •  1h trend WITH trade; middle of band; session=london_open  •  AVOID when strategy=bravo_failed_momentum

### W17.  `T1=T1a AND T4=T4c AND BBP=BBP4 AND ZS=ZS3`
- Raw: n=73  W=67/L=6  WR=91.8%
- Refine: exclude direction_exec=short drops 6/6 losers (100%)
- **Final: n=26  W=26/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; upper third; zscore -1 to +1 neutral  •  AVOID when short

### W18.  `T1=T1a AND BBP=BBP3 AND RSI=RSI3 AND session_bucket=london_open`
- Raw: n=71  W=61/L=10  WR=85.9%
- Refine: exclude strategy_id=bravo_failed_momentum drops 4/10 losers (40%)
- **Final: n=66  W=60/L=6  WR=90.9%**
- **Dir: ?**  •  1h trend WITH trade; middle of band; RSI 40-50 lower neutral; session=london_open  •  AVOID when strategy=bravo_failed_momentum

### W19.  `H20=H20a AND T1=T1a AND ZS=ZS5`
- Raw: n=70  W=62/L=8  WR=88.6%
- Refine: exclude H60=H60a drops 8/8 losers (100%)
- **Final: n=48  W=48/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when HTF60 aligned WITH trade

### W20.  `RSI=RSI3 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=69  W=60/L=9  WR=87.0%
- Refine: exclude session_bucket=ny_close drops 6/9 losers (67%)
- **Final: n=62  W=59/L=3  WR=95.2%**
- **Dir: SHORT**  •  RSI 40-50 lower neutral; zscore +2 to +3 deep overbought  •  AVOID when session=ny_close

### W21.  `H20=H20a AND H60=H60e AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=68  W=68/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=68  W=68/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 strongly against; session=ny_mid

### W22.  `T4=T4c AND BBP=BBP4 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=68  W=58/L=10  WR=85.3%
- Refine: exclude H60=H60d drops 5/10 losers (50%)
- **Final: n=58  W=53/L=5  WR=91.4%**
- **Dir: LONG**  •  4h trend AGAINST trade; upper third; RSI 50-60 upper neutral  •  AVOID when HTF60 mildly against

### W23.  `H60=H60b AND T1=T1a AND T4=T4c AND session_bucket=asia`
- Raw: n=65  W=60/L=5  WR=92.3%
- Refine: exclude H20=H20b drops 4/5 losers (80%)
- **Final: n=49  W=48/L=1  WR=98.0%**
- **Dir: ?**  •  HTF60 slightly aligned; 1h trend WITH trade; 4h trend AGAINST trade; session=asia  •  AVOID when HTF20 slightly aligned

### W24.  `H60=H60a AND T4=T4c AND BBP=BBP4 AND direction_exec=short`
- Raw: n=64  W=57/L=7  WR=89.1%
- Refine: exclude RSI=RSI4 drops 6/7 losers (86%)
- **Final: n=58  W=57/L=1  WR=98.3%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; upper third  •  AVOID when RSI 50-60 upper neutral

### W25.  `H60=H60b AND T1=T1a AND ZS=ZS3 AND direction_exec=short`
- Raw: n=64  W=55/L=9  WR=85.9%
- Refine: exclude BBP=BBP3 drops 8/9 losers (89%)
- **Final: n=21  W=20/L=1  WR=95.2%**
- **Dir: SHORT**  •  HTF60 slightly aligned; 1h trend WITH trade; zscore -1 to +1 neutral  •  AVOID when middle of band

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND BBP=BBP4 AND RSI=RSI3`
- Raw: n=179  W=69/L=110  WR=38.5%
- Sharpen: sharpest is direction_exec=long (62/110 of losers there)
- **Sharp: n=81  W=19/L=62  WR=23.5%**
- **Dir: ?**  •  HTF60 strongly against; upper third; RSI 40-50 lower neutral  •  ONLY when long

### L02.  `T1=T1c AND RSI=RSI4 AND direction_exec=short`
- Raw: n=163  W=50/L=113  WR=30.7%
- Sharpen: sharpest is ZS=ZS3 (33/113 of losers there)
- **Sharp: n=36  W=3/L=33  WR=8.3%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when zscore -1 to +1 neutral

### L03.  `H20=H20e AND T1=T1a AND ZS=ZS2`
- Raw: n=160  W=64/L=96  WR=40.0%
- Sharpen: sharpest is T4=T4a (69/96 of losers there)
- **Sharp: n=90  W=21/L=69  WR=23.3%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; zscore -2 to -1 oversold  •  ONLY when 4h trend WITH trade

### L04.  `H20=H20e AND T1=T1a AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=160  W=64/L=96  WR=40.0%
- Sharpen: sharpest is T4=T4a (69/96 of losers there)
- **Sharp: n=90  W=21/L=69  WR=23.3%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; lower third; zscore -2 to -1 oversold  •  ONLY when 4h trend WITH trade

### L05.  `H20=H20e AND H60=H60a AND T1=T1c AND T4=T4c`
- Raw: n=157  W=58/L=99  WR=36.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=157  W=58/L=99  WR=36.9%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade

### L06.  `T1=T1c AND T4=T4c AND RSI=RSI3 AND session_bucket=ny_open`
- Raw: n=151  W=59/L=92  WR=39.1%
- Sharpen: sharpest is H60=H60b (30/92 of losers there)
- **Sharp: n=30  W=0/L=30  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 40-50 lower neutral; session=ny_open  •  ONLY when HTF60 slightly aligned

### L07.  `H20=H20e AND BBP=BBP4 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=149  W=49/L=100  WR=32.9%
- Sharpen: sharpest is H60=H60e (30/100 of losers there)
- **Sharp: n=30  W=0/L=30  WR=0.0%**
- **Dir: LONG**  •  HTF20 strongly against; upper third; RSI 40-50 lower neutral  •  ONLY when HTF60 strongly against

### L08.  `H20=H20e AND T1=T1c AND BBP=BBP4 AND RSI=RSI3`
- Raw: n=148  W=57/L=91  WR=38.5%
- Sharpen: sharpest is H60=H60e (21/91 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; upper third; RSI 40-50 lower neutral  •  ONLY when HTF60 strongly against

### L09.  `H20=H20e AND T4=T4a AND ZS=ZS1`
- Raw: n=145  W=56/L=89  WR=38.6%
- Sharpen: sharpest is RSI=RSI2 (21/89 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  ONLY when RSI 30-40 weak

### L10.  `T1=T1a AND T4=T4a AND BBP=BBP0`
- Raw: n=142  W=51/L=91  WR=35.9%
- Sharpen: sharpest is RSI=RSI2 (21/91 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; deep below lower band  •  ONLY when RSI 30-40 weak

### L11.  `H20=H20e AND H60=H60a AND T4=T4a AND direction_exec=long`
- Raw: n=140  W=53/L=87  WR=37.9%
- Sharpen: sharpest is T1=T1a (44/87 of losers there)
- **Sharp: n=45  W=1/L=44  WR=2.2%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 aligned WITH trade; 4h trend WITH trade  •  ONLY when 1h trend WITH trade

### L12.  `H60=H60e AND T4=T4a AND BBP=BBP4`
- Raw: n=139  W=55/L=84  WR=39.6%
- Sharpen: sharpest is direction_exec=long (35/84 of losers there)
- **Sharp: n=45  W=10/L=35  WR=22.2%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; upper third  •  ONLY when long

### L13.  `H20=H20e AND H60=H60d AND RSI=RSI3`
- Raw: n=135  W=53/L=82  WR=39.3%
- Sharpen: sharpest is BBP=BBP2 (27/82 of losers there)
- **Sharp: n=35  W=8/L=27  WR=22.9%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 mildly against; RSI 40-50 lower neutral  •  ONLY when lower third

### L14.  `T4=T4a AND RSI=RSI4 AND direction_exec=short`
- Raw: n=121  W=34/L=87  WR=28.1%
- Sharpen: sharpest is ZS=ZS3 (31/87 of losers there)
- **Sharp: n=33  W=2/L=31  WR=6.1%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when zscore -1 to +1 neutral

### L15.  `H20=H20a AND T1=T1c AND T4=T4a AND session_bucket=asia`
- Raw: n=118  W=36/L=82  WR=30.5%
- Sharpen: sharpest is ZS=ZS3 (27/82 of losers there)
- **Sharp: n=32  W=5/L=27  WR=15.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; session=asia  •  ONLY when zscore -1 to +1 neutral

### L16.  `H20=H20e AND T1=T1a AND T4=T4a AND BBP=BBP2`
- Raw: n=117  W=38/L=79  WR=32.5%
- Sharpen: sharpest is ZS=ZS2 (69/79 of losers there)
- **Sharp: n=90  W=21/L=69  WR=23.3%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend WITH trade; lower third  •  ONLY when zscore -2 to -1 oversold

### L17.  `H60=H60e AND T4=T4a AND BBP=BBP4 AND RSI=RSI3`
- Raw: n=116  W=40/L=76  WR=34.5%
- Sharpen: sharpest is direction_exec=long (35/76 of losers there)
- **Sharp: n=37  W=2/L=35  WR=5.4%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; upper third; RSI 40-50 lower neutral  •  ONLY when long

### L18.  `H20=H20a AND H60=H60c AND T1=T1c AND session_bucket=asia`
- Raw: n=115  W=46/L=69  WR=40.0%
- Sharpen: sharpest is T4=T4a (37/69 of losers there)
- **Sharp: n=48  W=11/L=37  WR=22.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 neutral; 1h trend AGAINST trade; session=asia  •  ONLY when 4h trend WITH trade

### L19.  `RSI=RSI4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=114  W=41/L=73  WR=36.0%
- Sharpen: sharpest is T4=T4a (53/73 of losers there)
- **Sharp: n=71  W=18/L=53  WR=25.4%**
- **Dir: SHORT**  •  RSI 50-60 upper neutral; session=asia  •  ONLY when 4h trend WITH trade

### L20.  `H60=H60a AND T1=T1a AND BBP=BBP0`
- Raw: n=113  W=43/L=70  WR=38.1%
- Sharpen: sharpest is T4=T4a (50/70 of losers there)
- **Sharp: n=67  W=17/L=50  WR=25.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; deep below lower band  •  ONLY when 4h trend WITH trade

### L21.  `T1=T1c AND T4=T4a AND RSI=RSI4`
- Raw: n=112  W=39/L=73  WR=34.8%
- Sharpen: sharpest is direction_exec=short (73/73 of losers there)
- **Sharp: n=96  W=23/L=73  WR=24.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when short

### L22.  `H20=H20e AND H60=H60a AND BBP=BBP2 AND direction_exec=long`
- Raw: n=110  W=43/L=67  WR=39.1%
- Sharpen: sharpest is T1=T1a (17/67 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 aligned WITH trade; lower third  •  ONLY when 1h trend WITH trade

### L23.  `H20=H20e AND H60=H60a AND T4=T4c AND BBP=BBP2`
- Raw: n=108  W=38/L=70  WR=35.2%
- Sharpen: sharpest is session_bucket=london_open (16/70 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 4h trend AGAINST trade; lower third  •  ONLY when session=london_open

### L24.  `H20=H20e AND H60=H60e AND ZS=ZS3 AND direction_exec=long`
- Raw: n=108  W=41/L=67  WR=38.0%
- Sharpen: sharpest is RSI=RSI3 (66/67 of losers there)
- **Sharp: n=90  W=24/L=66  WR=26.7%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 strongly against; zscore -1 to +1 neutral  •  ONLY when RSI 40-50 lower neutral

### L25.  `T1=T1c AND T4=T4a AND ZS=ZS3 AND direction_exec=short`
- Raw: n=106  W=36/L=70  WR=34.0%
- Sharpen: sharpest is RSI=RSI4 (28/70 of losers there)
- **Sharp: n=30  W=2/L=28  WR=6.7%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend WITH trade; zscore -1 to +1 neutral  •  ONLY when RSI 50-60 upper neutral

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(44/38) | — |
| H60 | — | — |
| T1 | T1a(52/45) | T1c(48/55) |
| T4 | T4c(53/46) | T4a(47/54) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
