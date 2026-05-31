# AUD_NZD — R21 Manual

## Regime centroid (locked factors)

- **BB = BB2**  (normal bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **2,509**  (W=1,602 / L=907)  -  WR: **63.9%**

## Session distribution

- asia: n=804  W=503/L=301  WR=62.6%
- ny_mid: n=637  W=421/L=216  WR=66.1%
- london_open: n=333  W=224/L=109  WR=67.3%
- off_hours: n=198  W=119/L=79  WR=60.1%
- ny_close: n=174  W=109/L=65  WR=62.6%
- ny_open: n=169  W=101/L=68  WR=59.8%
- london: n=128  W=84/L=44  WR=65.6%
- asia_late: n=66  W=41/L=25  WR=62.1%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20e AND H60=H60a AND T1=T1c`
- Raw: n=91  W=80/L=11  WR=87.9%
- Refine: exclude session_bucket=ny_mid drops 7/11 losers (64%)
- **Final: n=64  W=60/L=4  WR=93.8%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend AGAINST trade  •  AVOID when session=ny_mid

### W02.  `H20=H20e AND T1=T1c AND direction_exec=long`
- Raw: n=91  W=80/L=11  WR=87.9%
- Refine: exclude session_bucket=ny_mid drops 7/11 losers (64%)
- **Final: n=64  W=60/L=4  WR=93.8%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade  •  AVOID when session=ny_mid

### W03.  `H20=H20e AND H60=H60a AND T1=T1c AND direction_exec=long`
- Raw: n=91  W=80/L=11  WR=87.9%
- Refine: exclude session_bucket=ny_mid drops 7/11 losers (64%)
- **Final: n=64  W=60/L=4  WR=93.8%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend AGAINST trade  •  AVOID when session=ny_mid

### W04.  `H20=H20e AND H60=H60a AND T4=T4a`
- Raw: n=84  W=72/L=12  WR=85.7%
- Refine: exclude session_bucket=ny_mid drops 8/12 losers (67%)
- **Final: n=62  W=58/L=4  WR=93.5%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 4h trend WITH trade  •  AVOID when session=ny_mid

### W05.  `H20=H20e AND T4=T4a AND direction_exec=long`
- Raw: n=84  W=72/L=12  WR=85.7%
- Refine: exclude session_bucket=ny_mid drops 8/12 losers (67%)
- **Final: n=62  W=58/L=4  WR=93.5%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend WITH trade  •  AVOID when session=ny_mid

### W06.  `H20=H20e AND H60=H60a AND T4=T4a AND direction_exec=long`
- Raw: n=84  W=72/L=12  WR=85.7%
- Refine: exclude session_bucket=ny_mid drops 8/12 losers (67%)
- **Final: n=62  W=58/L=4  WR=93.5%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 aligned WITH trade; 4h trend WITH trade  •  AVOID when session=ny_mid

### W07.  `H60=H60e AND RSI=RSI2 AND direction_exec=short`
- Raw: n=80  W=68/L=12  WR=85.0%
- Refine: exclude BBP=BBP3 drops 6/12 losers (50%)
- **Final: n=72  W=66/L=6  WR=91.7%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 30-40 weak  •  AVOID when middle of band

### W08.  `H20=H20e AND H60=H60a AND RSI=RSI3`
- Raw: n=78  W=67/L=11  WR=85.9%
- Refine: exclude session_bucket=ny_mid drops 7/11 losers (64%)
- **Final: n=55  W=51/L=4  WR=92.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; RSI 40-50 lower neutral  •  AVOID when session=ny_mid

### W09.  `H20=H20e AND RSI=RSI3 AND direction_exec=long`
- Raw: n=78  W=67/L=11  WR=85.9%
- Refine: exclude session_bucket=ny_mid drops 7/11 losers (64%)
- **Final: n=55  W=51/L=4  WR=92.7%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 40-50 lower neutral  •  AVOID when session=ny_mid

### W10.  `H20=H20e AND H60=H60a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=78  W=67/L=11  WR=85.9%
- Refine: exclude session_bucket=ny_mid drops 7/11 losers (64%)
- **Final: n=55  W=51/L=4  WR=92.7%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 aligned WITH trade; RSI 40-50 lower neutral  •  AVOID when session=ny_mid

### W11.  `H20=H20e AND H60=H60a AND T1=T1c AND T4=T4a`
- Raw: n=76  W=70/L=6  WR=92.1%
- Refine: exclude session_bucket=ny_mid drops 4/6 losers (67%)
- **Final: n=58  W=56/L=2  WR=96.6%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade  •  AVOID when session=ny_mid

### W12.  `H20=H20e AND T1=T1c AND T4=T4a AND direction_exec=long`
- Raw: n=76  W=70/L=6  WR=92.1%
- Refine: exclude session_bucket=ny_mid drops 4/6 losers (67%)
- **Final: n=58  W=56/L=2  WR=96.6%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend WITH trade  •  AVOID when session=ny_mid

### W13.  `H20=H20e AND H60=H60a AND T4=T4a AND RSI=RSI3`
- Raw: n=72  W=63/L=9  WR=87.5%
- Refine: exclude session_bucket=ny_mid drops 7/9 losers (78%)
- **Final: n=51  W=49/L=2  WR=96.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when session=ny_mid

### W14.  `H20=H20e AND T4=T4a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=72  W=63/L=9  WR=87.5%
- Refine: exclude session_bucket=ny_mid drops 7/9 losers (78%)
- **Final: n=51  W=49/L=2  WR=96.1%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when session=ny_mid

### W15.  `H20=H20a AND H60=H60a AND T1=T1a AND session_bucket=ny_mid`
- Raw: n=70  W=68/L=2  WR=97.1%
- Refine: exclude BBP=BBP3 drops 2/2 losers (100%)
- **Final: n=58  W=58/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; session=ny_mid  •  AVOID when middle of band

### W16.  `H20=H20a AND T1=T1a AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=70  W=68/L=2  WR=97.1%
- Refine: exclude BBP=BBP3 drops 2/2 losers (100%)
- **Final: n=58  W=58/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=ny_mid  •  AVOID when middle of band

### W17.  `H20=H20e AND H60=H60a AND T1=T1c AND RSI=RSI3`
- Raw: n=70  W=63/L=7  WR=90.0%
- Refine: exclude T4=T4c drops 2/7 losers (29%)
- **Final: n=68  W=63/L=5  WR=92.6%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when 4h trend AGAINST trade

### W18.  `H20=H20e AND T1=T1c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=70  W=63/L=7  WR=90.0%
- Refine: exclude T4=T4c drops 2/7 losers (29%)
- **Final: n=68  W=63/L=5  WR=92.6%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when 4h trend AGAINST trade

### W19.  `H20=H20e AND T4=T4c AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=67  W=59/L=8  WR=88.1%
- Refine: exclude session_bucket=asia drops 8/8 losers (100%)
- **Final: n=39  W=39/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when session=asia

### W20.  `H60=H60a AND T1=T1a AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=61  W=52/L=9  WR=85.2%
- Refine: exclude ZS=ZS1 drops 5/9 losers (56%)
- **Final: n=51  W=47/L=4  WR=92.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade; session=ny_mid  •  AVOID when zscore -3 to -2 deep oversold

### W21.  `T1=T1a AND T4=T4c AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=61  W=52/L=9  WR=85.2%
- Refine: exclude ZS=ZS1 drops 5/9 losers (56%)
- **Final: n=51  W=47/L=4  WR=92.2%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend AGAINST trade; session=ny_mid  •  AVOID when zscore -3 to -2 deep oversold

### W22.  `H20=H20a AND H60=H60a AND RSI=RSI5`
- Raw: n=60  W=58/L=2  WR=96.7%
- Refine: exclude ZS=ZS3 drops 2/2 losers (100%)
- **Final: n=56  W=56/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 60-70 strong  •  AVOID when zscore -1 to +1 neutral

### W23.  `H20=H20a AND T1=T1a AND RSI=RSI5`
- Raw: n=60  W=58/L=2  WR=96.7%
- Refine: exclude ZS=ZS3 drops 2/2 losers (100%)
- **Final: n=56  W=56/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when zscore -1 to +1 neutral

### W24.  `H20=H20a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=60  W=58/L=2  WR=96.7%
- Refine: exclude ZS=ZS3 drops 2/2 losers (100%)
- **Final: n=56  W=56/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 60-70 strong  •  AVOID when zscore -1 to +1 neutral

### W25.  `H20=H20a AND H60=H60a AND T1=T1a AND RSI=RSI5`
- Raw: n=60  W=58/L=2  WR=96.7%
- Refine: exclude ZS=ZS3 drops 2/2 losers (100%)
- **Final: n=56  W=56/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when zscore -1 to +1 neutral

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T4=T4a AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=92  W=34/L=58  WR=37.0%
- Sharpen: sharpest is H20=H20a (22/58 of losers there)
- **Sharp: n=28  W=6/L=22  WR=21.4%**
- **Dir: ?**  •  4h trend WITH trade; just touched upper band; zscore +2 to +3 deep overbought  •  ONLY when HTF20 aligned WITH trade

### L02.  `H20=H20a AND H60=H60e AND direction_exec=short`
- Raw: n=81  W=31/L=50  WR=38.3%
- Sharpen: sharpest is session_bucket=asia (15/50 of losers there)
- **Sharp: n=17  W=2/L=15  WR=11.8%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 strongly against  •  ONLY when session=asia

### L03.  `T1=T1c AND T4=T4a AND ZS=ZS5`
- Raw: n=72  W=24/L=48  WR=33.3%
- Sharpen: sharpest is RSI=RSI5 (22/48 of losers there)
- **Sharp: n=22  W=0/L=22  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  ONLY when RSI 60-70 strong

### L04.  `H60=H60e AND T1=T1c AND RSI=RSI5`
- Raw: n=71  W=19/L=52  WR=26.8%
- Sharpen: sharpest is H20=H20e (34/52 of losers there)
- **Sharp: n=37  W=3/L=34  WR=8.1%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when HTF20 strongly against

### L05.  `H60=H60e AND RSI=RSI5 AND direction_exec=short`
- Raw: n=71  W=19/L=52  WR=26.8%
- Sharpen: sharpest is H20=H20e (34/52 of losers there)
- **Sharp: n=37  W=3/L=34  WR=8.1%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 60-70 strong  •  ONLY when HTF20 strongly against

### L06.  `T1=T1c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=71  W=19/L=52  WR=26.8%
- Sharpen: sharpest is H20=H20e (34/52 of losers there)
- **Sharp: n=37  W=3/L=34  WR=8.1%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when HTF20 strongly against

### L07.  `H60=H60e AND T1=T1c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=71  W=19/L=52  WR=26.8%
- Sharpen: sharpest is H20=H20e (34/52 of losers there)
- **Sharp: n=37  W=3/L=34  WR=8.1%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when HTF20 strongly against

### L08.  `H20=H20a AND H60=H60e AND T1=T1a`
- Raw: n=70  W=24/L=46  WR=34.3%
- Sharpen: sharpest is session_bucket=asia (14/46 of losers there)
- **Sharp: n=15  W=1/L=14  WR=6.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend WITH trade  •  ONLY when session=asia

### L09.  `H20=H20a AND T1=T1a AND direction_exec=short`
- Raw: n=70  W=24/L=46  WR=34.3%
- Sharpen: sharpest is session_bucket=asia (14/46 of losers there)
- **Sharp: n=15  W=1/L=14  WR=6.7%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend WITH trade  •  ONLY when session=asia

### L10.  `H20=H20a AND H60=H60e AND T1=T1a AND direction_exec=short`
- Raw: n=70  W=24/L=46  WR=34.3%
- Sharpen: sharpest is session_bucket=asia (14/46 of losers there)
- **Sharp: n=15  W=1/L=14  WR=6.7%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend WITH trade  •  ONLY when session=asia

### L11.  `T1=T1c AND T4=T4a AND session_bucket=ny_close`
- Raw: n=68  W=27/L=41  WR=39.7%
- Sharpen: sharpest is BBP=BBP2 (14/41 of losers there)
- **Sharp: n=17  W=3/L=14  WR=17.6%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; session=ny_close  •  ONLY when lower third

### L12.  `H20=H20a AND H60=H60e AND RSI=RSI3`
- Raw: n=64  W=24/L=40  WR=37.5%
- Sharpen: sharpest is session_bucket=asia (13/40 of losers there)
- **Sharp: n=14  W=1/L=13  WR=7.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; RSI 40-50 lower neutral  •  ONLY when session=asia

### L13.  `H20=H20a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=64  W=24/L=40  WR=37.5%
- Sharpen: sharpest is session_bucket=asia (13/40 of losers there)
- **Sharp: n=14  W=1/L=13  WR=7.1%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 40-50 lower neutral  •  ONLY when session=asia

### L14.  `H20=H20a AND H60=H60e AND RSI=RSI3 AND direction_exec=short`
- Raw: n=64  W=24/L=40  WR=37.5%
- Sharpen: sharpest is session_bucket=asia (13/40 of losers there)
- **Sharp: n=14  W=1/L=13  WR=7.1%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 strongly against; RSI 40-50 lower neutral  •  ONLY when session=asia

### L15.  `T1=T1c AND T4=T4a AND BBP=BBP5`
- Raw: n=62  W=22/L=40  WR=35.5%
- Sharpen: sharpest is RSI=RSI5 (15/40 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; just touched upper band  •  ONLY when RSI 60-70 strong

### L16.  `T1=T1c AND T4=T4a AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=62  W=22/L=40  WR=35.5%
- Sharpen: sharpest is RSI=RSI5 (15/40 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; just touched upper band; zscore +2 to +3 deep overbought  •  ONLY when RSI 60-70 strong

### L17.  `H20=H20a AND H60=H60e AND T1=T1a AND T4=T4c`
- Raw: n=61  W=21/L=40  WR=34.4%
- Sharpen: sharpest is ZS=ZS1 (12/40 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend WITH trade; 4h trend AGAINST trade  •  ONLY when zscore -3 to -2 deep oversold

### L18.  `H20=H20a AND T1=T1a AND T4=T4c AND direction_exec=short`
- Raw: n=61  W=21/L=40  WR=34.4%
- Sharpen: sharpest is ZS=ZS1 (12/40 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade  •  ONLY when zscore -3 to -2 deep oversold

### L19.  `H20=H20a AND H60=H60e AND T4=T4c AND RSI=RSI3`
- Raw: n=59  W=23/L=36  WR=39.0%
- Sharpen: sharpest is session_bucket=asia (12/36 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when session=asia

### L20.  `H20=H20a AND T4=T4c AND RSI=RSI3 AND direction_exec=short`
- Raw: n=59  W=23/L=36  WR=39.0%
- Sharpen: sharpest is session_bucket=asia (12/36 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when session=asia

### L21.  `H60=H60e AND T4=T4a AND RSI=RSI5`
- Raw: n=57  W=17/L=40  WR=29.8%
- Sharpen: sharpest is ZS=ZS5 (22/40 of losers there)
- **Sharp: n=22  W=0/L=22  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when zscore +2 to +3 deep overbought

### L22.  `T1=T1c AND T4=T4a AND RSI=RSI5`
- Raw: n=57  W=17/L=40  WR=29.8%
- Sharpen: sharpest is ZS=ZS5 (22/40 of losers there)
- **Sharp: n=22  W=0/L=22  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when zscore +2 to +3 deep overbought

### L23.  `T4=T4a AND RSI=RSI5 AND direction_exec=short`
- Raw: n=57  W=17/L=40  WR=29.8%
- Sharpen: sharpest is ZS=ZS5 (22/40 of losers there)
- **Sharp: n=22  W=0/L=22  WR=0.0%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 60-70 strong  •  ONLY when zscore +2 to +3 deep overbought

### L24.  `H60=H60e AND T1=T1c AND T4=T4a AND RSI=RSI5`
- Raw: n=57  W=17/L=40  WR=29.8%
- Sharpen: sharpest is ZS=ZS5 (22/40 of losers there)
- **Sharp: n=22  W=0/L=22  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when zscore +2 to +3 deep overbought

### L25.  `H60=H60e AND T4=T4a AND RSI=RSI5 AND direction_exec=short`
- Raw: n=57  W=17/L=40  WR=29.8%
- Sharpen: sharpest is ZS=ZS5 (22/40 of losers there)
- **Sharp: n=22  W=0/L=22  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when zscore +2 to +3 deep overbought

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | H60a(52/47) | H60e(48/53) |
| T1 | — | — |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(52/47) | short(48/53) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
