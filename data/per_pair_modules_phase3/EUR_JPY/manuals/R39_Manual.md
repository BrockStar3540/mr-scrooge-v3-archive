# EUR_JPY — R39 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **4,388**  (W=2,776 / L=1,612)  -  WR: **63.3%**

## Session distribution

- asia: n=1807  W=1144/L=663  WR=63.3%
- ny_close: n=1078  W=694/L=384  WR=64.4%
- ny_open: n=378  W=239/L=139  WR=63.2%
- off_hours: n=276  W=164/L=112  WR=59.4%
- london: n=245  W=153/L=92  WR=62.4%
- ny_mid: n=222  W=135/L=87  WR=60.8%
- asia_late: n=216  W=144/L=72  WR=66.7%
- london_open: n=166  W=103/L=63  WR=62.0%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60e AND T1=T1a AND RSI=RSI3`
- Raw: n=115  W=98/L=17  WR=85.2%
- Refine: exclude session_bucket=asia drops 12/17 losers (71%)
- **Final: n=62  W=57/L=5  WR=91.9%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when session=asia

### W02.  `T4=T4c AND BBP=BBP3 AND session_bucket=ny_close`
- Raw: n=115  W=98/L=17  WR=85.2%
- Refine: exclude H60=H60d drops 6/17 losers (35%)
- **Final: n=91  W=80/L=11  WR=87.9%**
- **Dir: ?**  •  4h trend AGAINST trade; middle of band; session=ny_close  •  AVOID when HTF60 mildly against

### W03.  `T4=T4c AND BBP=BBP3 AND ZS=ZS3 AND session_bucket=ny_close`
- Raw: n=115  W=98/L=17  WR=85.2%
- Refine: exclude H60=H60d drops 6/17 losers (35%)
- **Final: n=91  W=80/L=11  WR=87.9%**
- **Dir: ?**  •  4h trend AGAINST trade; middle of band; zscore -1 to +1 neutral; session=ny_close  •  AVOID when HTF60 mildly against

### W04.  `T1=T1a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=112  W=97/L=15  WR=86.6%
- Refine: exclude BBP=BBP0 drops 6/15 losers (40%)
- **Final: n=98  W=89/L=9  WR=90.8%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when deep below lower band

### W05.  `T1=T1a AND T4=T4c AND RSI=RSI3 AND direction_exec=short`
- Raw: n=112  W=97/L=15  WR=86.6%
- Refine: exclude BBP=BBP0 drops 6/15 losers (40%)
- **Final: n=98  W=89/L=9  WR=90.8%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when deep below lower band

### W06.  `T1=T1a AND BBP=BBP1 AND ZS=ZS1`
- Raw: n=112  W=96/L=16  WR=85.7%
- Refine: exclude H20=H20a drops 9/16 losers (56%)
- **Final: n=75  W=68/L=7  WR=90.7%**
- **Dir: ?**  •  1h trend WITH trade; just touched lower band; zscore -3 to -2 deep oversold  •  AVOID when HTF20 aligned WITH trade

### W07.  `H60=H60e AND T1=T1c AND BBP=BBP5 AND RSI=RSI4`
- Raw: n=111  W=98/L=13  WR=88.3%
- Refine: exclude H20=H20e drops 10/13 losers (77%)
- **Final: n=48  W=45/L=3  WR=93.8%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; just touched upper band; RSI 50-60 upper neutral  •  AVOID when HTF20 strongly against

### W08.  `H60=H60a AND T4=T4a AND BBP=BBP6 AND RSI=RSI5`
- Raw: n=107  W=93/L=14  WR=86.9%
- Refine: exclude ZS=ZS5 drops 12/14 losers (86%)
- **Final: n=30  W=28/L=2  WR=93.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; deep above upper band; RSI 60-70 strong  •  AVOID when zscore +2 to +3 deep overbought

### W09.  `T1=T1a AND direction_exec=long AND session_bucket=asia_late`
- Raw: n=105  W=91/L=14  WR=86.7%
- Refine: exclude H20=H20a drops 14/14 losers (100%)
- **Final: n=56  W=56/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend WITH trade; session=asia_late  •  AVOID when HTF20 aligned WITH trade

### W10.  `H60=H60e AND T1=T1a AND T4=T4c AND RSI=RSI3`
- Raw: n=103  W=88/L=15  WR=85.4%
- Refine: exclude session_bucket=asia drops 10/15 losers (67%)
- **Final: n=62  W=57/L=5  WR=91.9%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when session=asia

### W11.  `H60=H60e AND T1=T1a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=103  W=88/L=15  WR=85.4%
- Refine: exclude session_bucket=asia drops 10/15 losers (67%)
- **Final: n=62  W=57/L=5  WR=91.9%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend WITH trade; RSI 40-50 lower neutral  •  AVOID when session=asia

### W12.  `H60=H60e AND T4=T4c AND ZS=ZS3 AND session_bucket=ny_close`
- Raw: n=99  W=86/L=13  WR=86.9%
- Refine: exclude BBP=BBP2 drops 3/13 losers (23%)
- **Final: n=90  W=80/L=10  WR=88.9%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; zscore -1 to +1 neutral; session=ny_close  •  AVOID when lower third

### W13.  `T4=T4c AND BBP=BBP3 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=94  W=81/L=13  WR=86.2%
- Refine: exclude H60=H60d drops 6/13 losers (46%)
- **Final: n=70  W=63/L=7  WR=90.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; middle of band; session=ny_close  •  AVOID when HTF60 mildly against

### W14.  `T1=T1a AND BBP=BBP6 AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=91  W=80/L=11  WR=87.9%
- Refine: exclude ZS=ZS6 drops 6/11 losers (55%)
- **Final: n=71  W=66/L=5  WR=93.0%**
- **Dir: ?**  •  1h trend WITH trade; deep above upper band; RSI 60-70 strong; session=asia  •  AVOID when zscore >+3 extreme

### W15.  `BBP=BBP6 AND RSI=RSI5 AND direction_exec=long AND session_bucket=asia`
- Raw: n=91  W=80/L=11  WR=87.9%
- Refine: exclude ZS=ZS6 drops 6/11 losers (55%)
- **Final: n=71  W=66/L=5  WR=93.0%**
- **Dir: LONG**  •  deep above upper band; RSI 60-70 strong; session=asia  •  AVOID when zscore >+3 extreme

### W16.  `H20=H20e AND T4=T4c AND direction_exec=long`
- Raw: n=89  W=80/L=9  WR=89.9%
- Refine: exclude BBP=BBP2 drops 5/9 losers (56%)
- **Final: n=78  W=74/L=4  WR=94.9%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend AGAINST trade  •  AVOID when lower third

### W17.  `H20=H20e AND T1=T1a AND T4=T4c AND direction_exec=long`
- Raw: n=89  W=80/L=9  WR=89.9%
- Refine: exclude BBP=BBP2 drops 5/9 losers (56%)
- **Final: n=78  W=74/L=4  WR=94.9%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend AGAINST trade  •  AVOID when lower third

### W18.  `T1=T1a AND BBP=BBP1 AND direction_exec=long`
- Raw: n=88  W=76/L=12  WR=86.4%
- Refine: exclude H20=H20a drops 8/12 losers (67%)
- **Final: n=52  W=48/L=4  WR=92.3%**
- **Dir: LONG**  •  1h trend WITH trade; just touched lower band  •  AVOID when HTF20 aligned WITH trade

### W19.  `T1=T1a AND BBP=BBP1 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=88  W=76/L=12  WR=86.4%
- Refine: exclude H20=H20a drops 8/12 losers (67%)
- **Final: n=52  W=48/L=4  WR=92.3%**
- **Dir: LONG**  •  1h trend WITH trade; just touched lower band; zscore -3 to -2 deep oversold  •  AVOID when HTF20 aligned WITH trade

### W20.  `H20=H20a AND H60=H60e AND session_bucket=ny_close`
- Raw: n=85  W=75/L=10  WR=88.2%
- Refine: exclude BBP=BBP2 drops 3/10 losers (30%)
- **Final: n=82  W=75/L=7  WR=91.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; session=ny_close  •  AVOID when lower third

### W21.  `H20=H20a AND H60=H60e AND T4=T4c AND session_bucket=ny_close`
- Raw: n=84  W=75/L=9  WR=89.3%
- Refine: exclude RSI=RSI4 drops 8/9 losers (89%)
- **Final: n=38  W=37/L=1  WR=97.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 4h trend AGAINST trade; session=ny_close  •  AVOID when RSI 50-60 upper neutral

### W22.  `H20=H20a AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=84  W=73/L=11  WR=86.9%
- Refine: exclude BBP=BBP2 drops 3/11 losers (27%)
- **Final: n=81  W=73/L=8  WR=90.1%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; session=ny_close  •  AVOID when lower third

### W23.  `H20=H20e AND T4=T4c AND ZS=ZS3 AND session_bucket=ny_close`
- Raw: n=84  W=73/L=11  WR=86.9%
- Refine: exclude BBP=BBP3 drops 8/11 losers (73%)
- **Final: n=37  W=34/L=3  WR=91.9%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; zscore -1 to +1 neutral; session=ny_close  •  AVOID when middle of band

### W24.  `H20=H20a AND T4=T4c AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=82  W=71/L=11  WR=86.6%
- Refine: exclude BBP=BBP2 drops 3/11 losers (27%)
- **Final: n=79  W=71/L=8  WR=89.9%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; session=ny_close  •  AVOID when lower third

### W25.  `H60=H60a AND BBP=BBP6 AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=79  W=68/L=11  WR=86.1%
- Refine: exclude ZS=ZS6 drops 6/11 losers (55%)
- **Final: n=59  W=54/L=5  WR=91.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; deep above upper band; RSI 60-70 strong; session=asia  •  AVOID when zscore >+3 extreme

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND T1=T1c AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=146  W=52/L=94  WR=35.6%
- Sharpen: sharpest is BBP=BBP6 (27/94 of losers there)
- **Sharp: n=27  W=0/L=27  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 60-70 strong; session=asia  •  ONLY when deep above upper band

### L02.  `H20=H20e AND RSI=RSI5 AND direction_exec=short AND session_bucket=asia`
- Raw: n=146  W=52/L=94  WR=35.6%
- Sharpen: sharpest is BBP=BBP6 (27/94 of losers there)
- **Sharp: n=27  W=0/L=27  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 60-70 strong; session=asia  •  ONLY when deep above upper band

### L03.  `H20=H20e AND H60=H60e AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=135  W=42/L=93  WR=31.1%
- Sharpen: sharpest is BBP=BBP6 (27/93 of losers there)
- **Sharp: n=27  W=0/L=27  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 60-70 strong; session=asia  •  ONLY when deep above upper band

### L04.  `H20=H20e AND T4=T4c AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=123  W=49/L=74  WR=39.8%
- Sharpen: sharpest is H60=H60e (74/74 of losers there)
- **Sharp: n=103  W=29/L=74  WR=28.2%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 60-70 strong; session=asia  •  ONLY when HTF60 strongly against

### L05.  `H60=H60a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=120  W=46/L=74  WR=38.3%
- Sharpen: sharpest is ZS=ZS2 (30/74 of losers there)
- **Sharp: n=38  W=8/L=30  WR=21.1%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral  •  ONLY when zscore -2 to -1 oversold

### L06.  `T4=T4a AND ZS=ZS3 AND session_bucket=ny_close`
- Raw: n=120  W=46/L=74  WR=38.3%
- Sharpen: sharpest is direction_exec=long (68/74 of losers there)
- **Sharp: n=103  W=35/L=68  WR=34.0%**
- **Dir: ?**  •  4h trend WITH trade; zscore -1 to +1 neutral; session=ny_close  •  ONLY when long

### L07.  `T4=T4c AND BBP=BBP6 AND RSI=RSI5`
- Raw: n=118  W=46/L=72  WR=39.0%
- Sharpen: sharpest is H60=H60e (53/72 of losers there)
- **Sharp: n=77  W=24/L=53  WR=31.2%**
- **Dir: ?**  •  4h trend AGAINST trade; deep above upper band; RSI 60-70 strong  •  ONLY when HTF60 strongly against

### L08.  `T4=T4c AND BBP=BBP4 AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=113  W=42/L=71  WR=37.2%
- Sharpen: sharpest is H60=H60e (50/71 of losers there)
- **Sharp: n=61  W=11/L=50  WR=18.0%**
- **Dir: ?**  •  4h trend AGAINST trade; upper third; RSI 50-60 upper neutral; session=asia  •  ONLY when HTF60 strongly against

### L09.  `T4=T4a AND ZS=ZS3 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=103  W=35/L=68  WR=34.0%
- Sharpen: sharpest is BBP=BBP3 (49/68 of losers there)
- **Sharp: n=67  W=18/L=49  WR=26.9%**
- **Dir: LONG**  •  4h trend WITH trade; zscore -1 to +1 neutral; session=ny_close  •  ONLY when middle of band

### L10.  `H60=H60a AND T1=T1c AND RSI=RSI3`
- Raw: n=96  W=36/L=60  WR=37.5%
- Sharpen: sharpest is ZS=ZS2 (32/60 of losers there)
- **Sharp: n=41  W=9/L=32  WR=22.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when zscore -2 to -1 oversold

### L11.  `T1=T1c AND RSI=RSI5 AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=92  W=35/L=57  WR=38.0%
- Sharpen: sharpest is H20=H20e (41/57 of losers there)
- **Sharp: n=49  W=8/L=41  WR=16.3%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 60-70 strong; zscore +2 to +3 deep overbought; session=asia  •  ONLY when HTF20 strongly against

### L12.  `T1=T1c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=91  W=33/L=58  WR=36.3%
- Sharpen: sharpest is ZS=ZS2 (29/58 of losers there)
- **Sharp: n=37  W=8/L=29  WR=21.6%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when zscore -2 to -1 oversold

### L13.  `T1=T1c AND T4=T4a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=91  W=33/L=58  WR=36.3%
- Sharpen: sharpest is ZS=ZS2 (29/58 of losers there)
- **Sharp: n=37  W=8/L=29  WR=21.6%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when zscore -2 to -1 oversold

### L14.  `H60=H60e AND BBP=BBP6 AND RSI=RSI5`
- Raw: n=91  W=34/L=57  WR=37.4%
- Sharpen: sharpest is session_bucket=asia (40/57 of losers there)
- **Sharp: n=53  W=13/L=40  WR=24.5%**
- **Dir: ?**  •  HTF60 strongly against; deep above upper band; RSI 60-70 strong  •  ONLY when session=asia

### L15.  `T4=T4c AND RSI=RSI4 AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=90  W=31/L=59  WR=34.4%
- Sharpen: sharpest is H60=H60e (43/59 of losers there)
- **Sharp: n=54  W=11/L=43  WR=20.4%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought; session=asia  •  ONLY when HTF60 strongly against

### L16.  `H60=H60e AND T1=T1c AND BBP=BBP6 AND RSI=RSI5`
- Raw: n=89  W=34/L=55  WR=38.2%
- Sharpen: sharpest is session_bucket=asia (40/55 of losers there)
- **Sharp: n=53  W=13/L=40  WR=24.5%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; deep above upper band; RSI 60-70 strong  •  ONLY when session=asia

### L17.  `H60=H60e AND BBP=BBP6 AND RSI=RSI5 AND direction_exec=short`
- Raw: n=89  W=34/L=55  WR=38.2%
- Sharpen: sharpest is session_bucket=asia (40/55 of losers there)
- **Sharp: n=53  W=13/L=40  WR=24.5%**
- **Dir: SHORT**  •  HTF60 strongly against; deep above upper band; RSI 60-70 strong  •  ONLY when session=asia

### L18.  `BBP=BBP3 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=88  W=35/L=53  WR=39.8%
- Sharpen: sharpest is T4=T4a (49/53 of losers there)
- **Sharp: n=67  W=18/L=49  WR=26.9%**
- **Dir: LONG**  •  middle of band; session=ny_close  •  ONLY when 4h trend WITH trade

### L19.  `BBP=BBP3 AND ZS=ZS3 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=88  W=35/L=53  WR=39.8%
- Sharpen: sharpest is T4=T4a (49/53 of losers there)
- **Sharp: n=67  W=18/L=49  WR=26.9%**
- **Dir: LONG**  •  middle of band; zscore -1 to +1 neutral; session=ny_close  •  ONLY when 4h trend WITH trade

### L20.  `H60=H60a AND T1=T1c AND T4=T4a AND RSI=RSI3`
- Raw: n=87  W=33/L=54  WR=37.9%
- Sharpen: sharpest is ZS=ZS2 (26/54 of losers there)
- **Sharp: n=34  W=8/L=26  WR=23.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when zscore -2 to -1 oversold

### L21.  `H60=H60a AND T1=T1c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=87  W=33/L=54  WR=37.9%
- Sharpen: sharpest is ZS=ZS2 (26/54 of losers there)
- **Sharp: n=34  W=8/L=26  WR=23.5%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when zscore -2 to -1 oversold

### L22.  `T1=T1c AND T4=T4c AND BBP=BBP6 AND RSI=RSI5`
- Raw: n=86  W=30/L=56  WR=34.9%
- Sharpen: sharpest is H20=H20e (39/56 of losers there)
- **Sharp: n=50  W=11/L=39  WR=22.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; deep above upper band; RSI 60-70 strong  •  ONLY when HTF20 strongly against

### L23.  `T4=T4c AND BBP=BBP6 AND RSI=RSI5 AND direction_exec=short`
- Raw: n=86  W=30/L=56  WR=34.9%
- Sharpen: sharpest is H20=H20e (39/56 of losers there)
- **Sharp: n=50  W=11/L=39  WR=22.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; deep above upper band; RSI 60-70 strong  •  ONLY when HTF20 strongly against

### L24.  `H60=H60b AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=86  W=34/L=52  WR=39.5%
- Sharpen: sharpest is T4=T4c (14/52 of losers there)
- **Sharp: n=15  W=1/L=14  WR=6.7%**
- **Dir: LONG**  •  HTF60 slightly aligned; session=ny_close  •  ONLY when 4h trend AGAINST trade

### L25.  `H20=H20a AND H60=H60a AND RSI=RSI3`
- Raw: n=85  W=34/L=51  WR=40.0%
- Sharpen: sharpest is ZS=ZS2 (18/51 of losers there)
- **Sharp: n=22  W=4/L=18  WR=18.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 40-50 lower neutral  •  ONLY when zscore -2 to -1 oversold

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | — |
| T1 | T1a(54/44) | T1c(46/56) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
