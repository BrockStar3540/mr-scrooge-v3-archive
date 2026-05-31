# USD_CAD — R32 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20d**  (EMA20 down 0.15-0.5x)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **1,805**  (W=1,151 / L=654)  -  WR: **63.8%**

## Session distribution

- london_open: n=448  W=266/L=182  WR=59.4%
- ny_close: n=299  W=192/L=107  WR=64.2%
- ny_open: n=290  W=193/L=97  WR=66.6%
- ny_mid: n=288  W=188/L=100  WR=65.3%
- asia: n=256  W=168/L=88  WR=65.6%
- london: n=159  W=98/L=61  WR=61.6%
- asia_late: n=45  W=32/L=13  WR=71.1%
- off_hours: n=20  W=14/L=6  WR=70.0%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60e AND T1=T1a AND T4=T4c`
- Raw: n=86  W=74/L=12  WR=86.0%
- Refine: exclude BBP=BBP1 drops 8/12 losers (67%)
- **Final: n=73  W=69/L=4  WR=94.5%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend AGAINST trade  •  AVOID when just touched lower band

### W02.  `H60=H60e AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=82  W=72/L=10  WR=87.8%
- Refine: exclude T1=T1c drops 10/10 losers (100%)
- **Final: n=24  W=24/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; session=ny_mid  •  AVOID when 1h trend AGAINST trade

### W03.  `H60=H60e AND T1=T1a AND T4=T4c AND RSI=RSI3`
- Raw: n=80  W=68/L=12  WR=85.0%
- Refine: exclude BBP=BBP1 drops 8/12 losers (67%)
- **Final: n=67  W=63/L=4  WR=94.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when just touched lower band

### W04.  `H20=H20a AND BBP=BBP2 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=79  W=70/L=9  WR=88.6%
- Refine: exclude T4=T4c drops 3/9 losers (33%)
- **Final: n=71  W=65/L=6  WR=91.5%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; lower third; RSI 40-50 lower neutral  •  AVOID when 4h trend AGAINST trade

### W05.  `H60=H60e AND T1=T1a AND direction_exec=short`
- Raw: n=76  W=67/L=9  WR=88.2%
- Refine: exclude session_bucket=london_open drops 5/9 losers (56%)
- **Final: n=71  W=67/L=4  WR=94.4%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend WITH trade  •  AVOID when session=london_open

### W06.  `T1=T1a AND RSI=RSI2 AND ZS=ZS2`
- Raw: n=72  W=62/L=10  WR=86.1%
- Refine: exclude session_bucket=ny_close drops 5/10 losers (50%)
- **Final: n=62  W=57/L=5  WR=91.9%**
- **Dir: ?**  •  1h trend WITH trade; RSI 30-40 weak; zscore -2 to -1 oversold  •  AVOID when session=ny_close

### W07.  `RSI=RSI2 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=72  W=62/L=10  WR=86.1%
- Refine: exclude session_bucket=ny_close drops 5/10 losers (50%)
- **Final: n=62  W=57/L=5  WR=91.9%**
- **Dir: SHORT**  •  RSI 30-40 weak; zscore -2 to -1 oversold  •  AVOID when session=ny_close

### W08.  `T1=T1a AND BBP=BBP2 AND RSI=RSI2 AND ZS=ZS2`
- Raw: n=72  W=62/L=10  WR=86.1%
- Refine: exclude session_bucket=ny_close drops 5/10 losers (50%)
- **Final: n=62  W=57/L=5  WR=91.9%**
- **Dir: ?**  •  1h trend WITH trade; lower third; RSI 30-40 weak; zscore -2 to -1 oversold  •  AVOID when session=ny_close

### W09.  `T1=T1a AND RSI=RSI2 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=72  W=62/L=10  WR=86.1%
- Refine: exclude session_bucket=ny_close drops 5/10 losers (50%)
- **Final: n=62  W=57/L=5  WR=91.9%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 30-40 weak; zscore -2 to -1 oversold  •  AVOID when session=ny_close

### W10.  `BBP=BBP2 AND RSI=RSI2 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=72  W=62/L=10  WR=86.1%
- Refine: exclude session_bucket=ny_close drops 5/10 losers (50%)
- **Final: n=62  W=57/L=5  WR=91.9%**
- **Dir: SHORT**  •  lower third; RSI 30-40 weak; zscore -2 to -1 oversold  •  AVOID when session=ny_close

### W11.  `H60=H60b AND T1=T1c AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=71  W=63/L=8  WR=88.7%
- Refine: exclude session_bucket=ny_open drops 4/8 losers (50%)
- **Final: n=57  W=53/L=4  WR=93.0%**
- **Dir: ?**  •  HTF60 slightly aligned; 1h trend AGAINST trade; lower third; RSI 40-50 lower neutral  •  AVOID when session=ny_open

### W12.  `H20=H20a AND RSI=RSI3 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=70  W=62/L=8  WR=88.6%
- Refine: exclude T4=T4c drops 3/8 losers (38%)
- **Final: n=62  W=57/L=5  WR=91.9%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when 4h trend AGAINST trade

### W13.  `H20=H20e AND H60=H60e AND T1=T1c AND BBP=BBP1`
- Raw: n=70  W=60/L=10  WR=85.7%
- Refine: exclude session_bucket=london_open drops 5/10 losers (50%)
- **Final: n=59  W=54/L=5  WR=91.5%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; just touched lower band  •  AVOID when session=london_open

### W14.  `H20=H20e AND H60=H60e AND T1=T1a AND T4=T4c`
- Raw: n=69  W=61/L=8  WR=88.4%
- Refine: exclude BBP=BBP1 drops 6/8 losers (75%)
- **Final: n=58  W=56/L=2  WR=96.6%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend WITH trade; 4h trend AGAINST trade  •  AVOID when just touched lower band

### W15.  `H60=H60e AND T1=T1c AND T4=T4a AND BBP=BBP1`
- Raw: n=68  W=58/L=10  WR=85.3%
- Refine: exclude session_bucket=london drops 3/10 losers (30%)
- **Final: n=65  W=58/L=7  WR=89.2%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade; just touched lower band  •  AVOID when session=london

### W16.  `H60=H60e AND T1=T1a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=66  W=57/L=9  WR=86.4%
- Refine: exclude session_bucket=london_open drops 5/9 losers (56%)
- **Final: n=61  W=57/L=4  WR=93.4%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when session=london_open

### W17.  `H20=H20e AND direction_exec=long AND session_bucket=london`
- Raw: n=61  W=56/L=5  WR=91.8%
- Refine: exclude BBP=BBP4 drops 2/5 losers (40%)
- **Final: n=59  W=56/L=3  WR=94.9%**
- **Dir: LONG**  •  HTF20 strongly against; session=london  •  AVOID when upper third

### W18.  `H60=H60b AND T1=T1c AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=60  W=54/L=6  WR=90.0%
- Refine: exclude session_bucket=ny_open drops 4/6 losers (67%)
- **Final: n=50  W=48/L=2  WR=96.0%**
- **Dir: ?**  •  HTF60 slightly aligned; 1h trend AGAINST trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when session=ny_open

### W19.  `T1=T1a AND T4=T4c AND RSI=RSI2 AND session_bucket=london_open`
- Raw: n=60  W=52/L=8  WR=86.7%
- Refine: exclude H60=H60c drops 6/8 losers (75%)
- **Final: n=50  W=48/L=2  WR=96.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 30-40 weak; session=london_open  •  AVOID when HTF60 neutral

### W20.  `T4=T4c AND RSI=RSI2 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=60  W=52/L=8  WR=86.7%
- Refine: exclude H60=H60c drops 6/8 losers (75%)
- **Final: n=50  W=48/L=2  WR=96.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 30-40 weak; session=london_open  •  AVOID when HTF60 neutral

### W21.  `H60=H60e AND T1=T1c AND BBP=BBP1 AND RSI=RSI3`
- Raw: n=58  W=52/L=6  WR=89.7%
- Refine: exclude session_bucket=london_open drops 3/6 losers (50%)
- **Final: n=49  W=46/L=3  WR=93.9%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; just touched lower band; RSI 40-50 lower neutral  •  AVOID when session=london_open

### W22.  `H20=H20a AND T1=T1a AND session_bucket=ny_open`
- Raw: n=57  W=49/L=8  WR=86.0%
- Refine: exclude ZS=ZS1 drops 5/8 losers (62%)
- **Final: n=43  W=40/L=3  WR=93.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=ny_open  •  AVOID when zscore -3 to -2 deep oversold

### W23.  `H20=H20e AND T4=T4a AND direction_exec=short`
- Raw: n=56  W=49/L=7  WR=87.5%
- Refine: exclude ZS=ZS1 drops 5/7 losers (71%)
- **Final: n=43  W=41/L=2  WR=95.3%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend WITH trade  •  AVOID when zscore -3 to -2 deep oversold

### W24.  `H20=H20a AND T4=T4a AND RSI=RSI3 AND session_bucket=ny_mid`
- Raw: n=56  W=49/L=7  WR=87.5%
- Refine: exclude ZS=ZS4 drops 3/7 losers (43%)
- **Final: n=52  W=48/L=4  WR=92.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral; session=ny_mid  •  AVOID when zscore +1 to +2 overbought

### W25.  `T1=T1a AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=53  W=46/L=7  WR=86.8%
- Refine: exclude BBP=BBP4 drops 5/7 losers (71%)
- **Final: n=42  W=40/L=2  WR=95.2%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; session=ny_mid  •  AVOID when upper third

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20a AND T1=T1c AND session_bucket=london_open`
- Raw: n=98  W=39/L=59  WR=39.8%
- Sharpen: sharpest is RSI=RSI2 (33/59 of losers there)
- **Sharp: n=45  W=12/L=33  WR=26.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; session=london_open  •  ONLY when RSI 30-40 weak

### L02.  `H20=H20a AND T1=T1c AND T4=T4c`
- Raw: n=95  W=37/L=58  WR=38.9%
- Sharpen: sharpest is H60=H60e (29/58 of losers there)
- **Sharp: n=34  W=5/L=29  WR=14.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when HTF60 strongly against

### L03.  `H20=H20a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=80  W=28/L=52  WR=35.0%
- Sharpen: sharpest is RSI=RSI2 (33/52 of losers there)
- **Sharp: n=45  W=12/L=33  WR=26.7%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; session=london_open  •  ONLY when RSI 30-40 weak

### L04.  `H20=H20a AND T4=T4a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=75  W=26/L=49  WR=34.7%
- Sharpen: sharpest is H60=H60e (11/49 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=london_open  •  ONLY when HTF60 strongly against

### L05.  `T1=T1c AND BBP=BBP2 AND RSI=RSI2`
- Raw: n=74  W=25/L=49  WR=33.8%
- Sharpen: sharpest is T4=T4c (19/49 of losers there)
- **Sharp: n=20  W=1/L=19  WR=5.0%**
- **Dir: ?**  •  1h trend AGAINST trade; lower third; RSI 30-40 weak  •  ONLY when 4h trend AGAINST trade

### L06.  `BBP=BBP2 AND RSI=RSI2 AND direction_exec=long`
- Raw: n=74  W=25/L=49  WR=33.8%
- Sharpen: sharpest is T4=T4c (19/49 of losers there)
- **Sharp: n=20  W=1/L=19  WR=5.0%**
- **Dir: LONG**  •  lower third; RSI 30-40 weak  •  ONLY when 4h trend AGAINST trade

### L07.  `T1=T1c AND BBP=BBP2 AND RSI=RSI2 AND direction_exec=long`
- Raw: n=74  W=25/L=49  WR=33.8%
- Sharpen: sharpest is T4=T4c (19/49 of losers there)
- **Sharp: n=20  W=1/L=19  WR=5.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; lower third; RSI 30-40 weak  •  ONLY when 4h trend AGAINST trade

### L08.  `T1=T1c AND RSI=RSI2 AND session_bucket=london_open`
- Raw: n=69  W=20/L=49  WR=29.0%
- Sharpen: sharpest is H60=H60b (22/49 of losers there)
- **Sharp: n=25  W=3/L=22  WR=12.0%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 30-40 weak; session=london_open  •  ONLY when HTF60 slightly aligned

### L09.  `T4=T4a AND RSI=RSI2 AND session_bucket=london_open`
- Raw: n=69  W=20/L=49  WR=29.0%
- Sharpen: sharpest is H60=H60b (22/49 of losers there)
- **Sharp: n=25  W=3/L=22  WR=12.0%**
- **Dir: ?**  •  4h trend WITH trade; RSI 30-40 weak; session=london_open  •  ONLY when HTF60 slightly aligned

### L10.  `RSI=RSI2 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=69  W=20/L=49  WR=29.0%
- Sharpen: sharpest is H60=H60b (22/49 of losers there)
- **Sharp: n=25  W=3/L=22  WR=12.0%**
- **Dir: LONG**  •  RSI 30-40 weak; session=london_open  •  ONLY when HTF60 slightly aligned

### L11.  `T1=T1c AND RSI=RSI2 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=69  W=20/L=49  WR=29.0%
- Sharpen: sharpest is H60=H60b (22/49 of losers there)
- **Sharp: n=25  W=3/L=22  WR=12.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 30-40 weak; session=london_open  •  ONLY when HTF60 slightly aligned

### L12.  `T1=T1c AND ZS=ZS1 AND session_bucket=london_open`
- Raw: n=65  W=23/L=42  WR=35.4%
- Sharpen: sharpest is RSI=RSI2 (18/42 of losers there)
- **Sharp: n=21  W=3/L=18  WR=14.3%**
- **Dir: ?**  •  1h trend AGAINST trade; zscore -3 to -2 deep oversold; session=london_open  •  ONLY when RSI 30-40 weak

### L13.  `T1=T1c AND RSI=RSI2 AND ZS=ZS2`
- Raw: n=63  W=19/L=44  WR=30.2%
- Sharpen: sharpest is T4=T4c (17/44 of losers there)
- **Sharp: n=18  W=1/L=17  WR=5.6%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 30-40 weak; zscore -2 to -1 oversold  •  ONLY when 4h trend AGAINST trade

### L14.  `RSI=RSI2 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=63  W=19/L=44  WR=30.2%
- Sharpen: sharpest is T4=T4c (17/44 of losers there)
- **Sharp: n=18  W=1/L=17  WR=5.6%**
- **Dir: LONG**  •  RSI 30-40 weak; zscore -2 to -1 oversold  •  ONLY when 4h trend AGAINST trade

### L15.  `T1=T1c AND BBP=BBP2 AND RSI=RSI2 AND ZS=ZS2`
- Raw: n=63  W=19/L=44  WR=30.2%
- Sharpen: sharpest is T4=T4c (17/44 of losers there)
- **Sharp: n=18  W=1/L=17  WR=5.6%**
- **Dir: ?**  •  1h trend AGAINST trade; lower third; RSI 30-40 weak; zscore -2 to -1 oversold  •  ONLY when 4h trend AGAINST trade

### L16.  `T1=T1c AND RSI=RSI2 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=63  W=19/L=44  WR=30.2%
- Sharpen: sharpest is T4=T4c (17/44 of losers there)
- **Sharp: n=18  W=1/L=17  WR=5.6%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 30-40 weak; zscore -2 to -1 oversold  •  ONLY when 4h trend AGAINST trade

### L17.  `BBP=BBP2 AND RSI=RSI2 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=63  W=19/L=44  WR=30.2%
- Sharpen: sharpest is T4=T4c (17/44 of losers there)
- **Sharp: n=18  W=1/L=17  WR=5.6%**
- **Dir: LONG**  •  lower third; RSI 30-40 weak; zscore -2 to -1 oversold  •  ONLY when 4h trend AGAINST trade

### L18.  `T1=T1c AND T4=T4c AND RSI=RSI2`
- Raw: n=63  W=21/L=42  WR=33.3%
- Sharpen: sharpest is H20=H20a (28/42 of losers there)
- **Sharp: n=33  W=5/L=28  WR=15.2%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when HTF20 aligned WITH trade

### L19.  `T4=T4c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=63  W=21/L=42  WR=33.3%
- Sharpen: sharpest is H20=H20a (28/42 of losers there)
- **Sharp: n=33  W=5/L=28  WR=15.2%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when HTF20 aligned WITH trade

### L20.  `T1=T1c AND T4=T4c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=63  W=21/L=42  WR=33.3%
- Sharpen: sharpest is H20=H20a (28/42 of losers there)
- **Sharp: n=33  W=5/L=28  WR=15.2%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when HTF20 aligned WITH trade

### L21.  `H60=H60a AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=63  W=22/L=41  WR=34.9%
- Sharpen: sharpest is RSI=RSI2 (9/41 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=ny_mid  •  ONLY when RSI 30-40 weak

### L22.  `T4=T4c AND BBP=BBP1 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=60  W=23/L=37  WR=38.3%
- Sharpen: sharpest is T1=T1c (14/37 of losers there)
- **Sharp: n=18  W=4/L=14  WR=22.2%**
- **Dir: SHORT**  •  4h trend AGAINST trade; just touched lower band; RSI 40-50 lower neutral  •  ONLY when 1h trend AGAINST trade

### L23.  `H20=H20a AND T4=T4c AND direction_exec=long`
- Raw: n=59  W=22/L=37  WR=37.3%
- Sharpen: sharpest is H60=H60e (33/37 of losers there)
- **Sharp: n=39  W=6/L=33  WR=15.4%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade  •  ONLY when HTF60 strongly against

### L24.  `H60=H60e AND T1=T1c AND T4=T4c AND RSI=RSI2`
- Raw: n=58  W=21/L=37  WR=36.2%
- Sharpen: sharpest is BBP=BBP2 (17/37 of losers there)
- **Sharp: n=18  W=1/L=17  WR=5.6%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when lower third

### L25.  `H60=H60e AND T4=T4c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=58  W=21/L=37  WR=36.2%
- Sharpen: sharpest is BBP=BBP2 (17/37 of losers there)
- **Sharp: n=18  W=1/L=17  WR=5.6%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when lower third

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20e(49/38) | H20a(34/48) |
| H60 | H60e(34/27) | H60a(26/33) |
| T1 | — | — |
| T4 | T4a(53/45) | T4c(47/55) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
