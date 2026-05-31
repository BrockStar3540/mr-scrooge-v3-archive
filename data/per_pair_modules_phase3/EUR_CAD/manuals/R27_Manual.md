# EUR_CAD — R27 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **3,668**  (W=2,341 / L=1,327)  -  WR: **63.8%**

## Session distribution

- ny_close: n=1714  W=1085/L=629  WR=63.3%
- asia: n=997  W=672/L=325  WR=67.4%
- off_hours: n=319  W=203/L=116  WR=63.6%
- london: n=149  W=91/L=58  WR=61.1%
- ny_mid: n=134  W=78/L=56  WR=58.2%
- asia_late: n=129  W=72/L=57  WR=55.8%
- ny_open: n=114  W=68/L=46  WR=59.6%
- london_open: n=112  W=72/L=40  WR=64.3%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND H60=H60a AND T1=T1a AND session_bucket=asia`
- Raw: n=217  W=186/L=31  WR=85.7%
- Refine: exclude RSI=RSI1 drops 8/31 losers (26%)
- **Final: n=203  W=180/L=23  WR=88.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; session=asia  •  AVOID when RSI 20-30 oversold

### W02.  `H20=H20a AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=167  W=143/L=24  WR=85.6%
- Refine: exclude H60=H60b drops 12/24 losers (50%)
- **Final: n=134  W=122/L=12  WR=91.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 30-40 weak; session=asia  •  AVOID when HTF60 slightly aligned

### W03.  `H20=H20a AND T1=T1a AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=164  W=143/L=21  WR=87.2%
- Refine: exclude H60=H60b drops 12/21 losers (57%)
- **Final: n=131  W=122/L=9  WR=93.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 30-40 weak; session=asia  •  AVOID when HTF60 slightly aligned

### W04.  `H20=H20a AND T4=T4a AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=164  W=143/L=21  WR=87.2%
- Refine: exclude H60=H60b drops 12/21 losers (57%)
- **Final: n=131  W=122/L=9  WR=93.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 30-40 weak; session=asia  •  AVOID when HTF60 slightly aligned

### W05.  `H20=H20a AND RSI=RSI2 AND direction_exec=short AND session_bucket=asia`
- Raw: n=164  W=143/L=21  WR=87.2%
- Refine: exclude H60=H60b drops 12/21 losers (57%)
- **Final: n=131  W=122/L=9  WR=93.1%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 30-40 weak; session=asia  •  AVOID when HTF60 slightly aligned

### W06.  `H20=H20a AND H60=H60a AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=131  W=122/L=9  WR=93.1%
- Refine: exclude ZS=ZS2 drops 6/9 losers (67%)
- **Final: n=91  W=88/L=3  WR=96.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 30-40 weak; session=asia  •  AVOID when zscore -2 to -1 oversold

### W07.  `H60=H60a AND ZS=ZS5 AND direction_exec=short`
- Raw: n=120  W=106/L=14  WR=88.3%
- Refine: exclude BBP=BBP5 drops 12/14 losers (86%)
- **Final: n=58  W=56/L=2  WR=96.6%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; zscore +2 to +3 deep overbought  •  AVOID when just touched upper band

### W08.  `T1=T1a AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=120  W=102/L=18  WR=85.0%
- Refine: exclude H20=H20e drops 7/18 losers (39%)
- **Final: n=96  W=85/L=11  WR=88.5%**
- **Dir: ?**  •  1h trend WITH trade; zscore -3 to -2 deep oversold; session=asia  •  AVOID when HTF20 strongly against

### W09.  `T1=T1a AND ZS=ZS5 AND direction_exec=short`
- Raw: n=114  W=98/L=16  WR=86.0%
- Refine: exclude BBP=BBP5 drops 14/16 losers (88%)
- **Final: n=52  W=50/L=2  WR=96.2%**
- **Dir: SHORT**  •  1h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when just touched upper band

### W10.  `H60=H60a AND T1=T1a AND ZS=ZS5`
- Raw: n=111  W=97/L=14  WR=87.4%
- Refine: exclude BBP=BBP5 drops 12/14 losers (86%)
- **Final: n=52  W=50/L=2  WR=96.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when just touched upper band

### W11.  `H60=H60a AND T1=T1a AND ZS=ZS5 AND direction_exec=short`
- Raw: n=111  W=97/L=14  WR=87.4%
- Refine: exclude BBP=BBP5 drops 12/14 losers (86%)
- **Final: n=52  W=50/L=2  WR=96.2%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when just touched upper band

### W12.  `T4=T4a AND ZS=ZS5 AND direction_exec=short`
- Raw: n=107  W=95/L=12  WR=88.8%
- Refine: exclude BBP=BBP5 drops 10/12 losers (83%)
- **Final: n=58  W=56/L=2  WR=96.6%**
- **Dir: SHORT**  •  4h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when just touched upper band

### W13.  `H60=H60a AND T4=T4a AND ZS=ZS5`
- Raw: n=103  W=94/L=9  WR=91.3%
- Refine: exclude strategy_id=delta_tag_and_go_v2 drops 5/9 losers (56%)
- **Final: n=85  W=81/L=4  WR=95.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when strategy=delta_tag_and_go_v2

### W14.  `H60=H60a AND T4=T4a AND ZS=ZS5 AND direction_exec=short`
- Raw: n=103  W=94/L=9  WR=91.3%
- Refine: exclude strategy_id=delta_tag_and_go_v2 drops 5/9 losers (56%)
- **Final: n=85  W=81/L=4  WR=95.3%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when strategy=delta_tag_and_go_v2

### W15.  `T1=T1a AND ZS=ZS1 AND direction_exec=short AND session_bucket=asia`
- Raw: n=100  W=86/L=14  WR=86.0%
- Refine: exclude H20=H20b drops 4/14 losers (29%)
- **Final: n=93  W=83/L=10  WR=89.2%**
- **Dir: SHORT**  •  1h trend WITH trade; zscore -3 to -2 deep oversold; session=asia  •  AVOID when HTF20 slightly aligned

### W16.  `T4=T4a AND RSI=RSI3 AND ZS=ZS5`
- Raw: n=99  W=86/L=13  WR=86.9%
- Refine: exclude BBP=BBP5 drops 12/13 losers (92%)
- **Final: n=51  W=50/L=1  WR=98.0%**
- **Dir: ?**  •  4h trend WITH trade; RSI 40-50 lower neutral; zscore +2 to +3 deep overbought  •  AVOID when just touched upper band

### W17.  `H20=H20a AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=97  W=87/L=10  WR=89.7%
- Refine: exclude RSI=RSI1 drops 4/10 losers (40%)
- **Final: n=89  W=83/L=6  WR=93.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; zscore -3 to -2 deep oversold; session=asia  •  AVOID when RSI 20-30 oversold

### W18.  `T1=T1a AND T4=T4a AND ZS=ZS5`
- Raw: n=97  W=86/L=11  WR=88.7%
- Refine: exclude BBP=BBP5 drops 9/11 losers (82%)
- **Final: n=52  W=50/L=2  WR=96.2%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when just touched upper band

### W19.  `T1=T1a AND T4=T4a AND ZS=ZS5 AND direction_exec=short`
- Raw: n=97  W=86/L=11  WR=88.7%
- Refine: exclude BBP=BBP5 drops 9/11 losers (82%)
- **Final: n=52  W=50/L=2  WR=96.2%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when just touched upper band

### W20.  `RSI=RSI3 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=97  W=84/L=13  WR=86.6%
- Refine: exclude BBP=BBP5 drops 12/13 losers (92%)
- **Final: n=51  W=50/L=1  WR=98.0%**
- **Dir: SHORT**  •  RSI 40-50 lower neutral; zscore +2 to +3 deep overbought  •  AVOID when just touched upper band

### W21.  `H60=H60a AND RSI=RSI3 AND ZS=ZS5`
- Raw: n=96  W=84/L=12  WR=87.5%
- Refine: exclude BBP=BBP5 drops 11/12 losers (92%)
- **Final: n=51  W=50/L=1  WR=98.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral; zscore +2 to +3 deep overbought  •  AVOID when just touched upper band

### W22.  `H60=H60a AND RSI=RSI3 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=96  W=84/L=12  WR=87.5%
- Refine: exclude BBP=BBP5 drops 11/12 losers (92%)
- **Final: n=51  W=50/L=1  WR=98.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral; zscore +2 to +3 deep overbought  •  AVOID when just touched upper band

### W23.  `BBP=BBP0 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=94  W=86/L=8  WR=91.5%
- Refine: exclude session_bucket=london_open drops 5/8 losers (62%)
- **Final: n=72  W=69/L=3  WR=95.8%**
- **Dir: LONG**  •  deep below lower band; RSI 40-50 lower neutral  •  AVOID when session=london_open

### W24.  `H60=H60a AND T1=T1a AND T4=T4a AND ZS=ZS5`
- Raw: n=94  W=85/L=9  WR=90.4%
- Refine: exclude strategy_id=delta_tag_and_go_v2 drops 5/9 losers (56%)
- **Final: n=78  W=74/L=4  WR=94.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when strategy=delta_tag_and_go_v2

### W25.  `H20=H20d AND T1=T1a AND T4=T4c`
- Raw: n=93  W=82/L=11  WR=88.2%
- Refine: exclude ZS=ZS2 drops 4/11 losers (36%)
- **Final: n=79  W=72/L=7  WR=91.1%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend WITH trade; 4h trend AGAINST trade  •  AVOID when zscore -2 to -1 oversold

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND T1=T1c AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=103  W=38/L=65  WR=36.9%
- Sharpen: sharpest is H60=H60e (53/65 of losers there)
- **Sharp: n=67  W=14/L=53  WR=20.9%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 30-40 weak; session=asia  •  ONLY when HTF60 strongly against

### L02.  `H20=H20e AND T4=T4c AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=103  W=38/L=65  WR=36.9%
- Sharpen: sharpest is H60=H60e (53/65 of losers there)
- **Sharp: n=61  W=8/L=53  WR=13.1%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 30-40 weak; session=asia  •  ONLY when HTF60 strongly against

### L03.  `H20=H20e AND RSI=RSI2 AND direction_exec=long AND session_bucket=asia`
- Raw: n=103  W=38/L=65  WR=36.9%
- Sharpen: sharpest is H60=H60e (53/65 of losers there)
- **Sharp: n=67  W=14/L=53  WR=20.9%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 30-40 weak; session=asia  •  ONLY when HTF60 strongly against

### L04.  `H20=H20c AND H60=H60a AND T1=T1a`
- Raw: n=103  W=41/L=62  WR=39.8%
- Sharpen: sharpest is RSI=RSI3 (28/62 of losers there)
- **Sharp: n=36  W=8/L=28  WR=22.2%**
- **Dir: ?**  •  HTF20 neutral; HTF60 aligned WITH trade; 1h trend WITH trade  •  ONLY when RSI 40-50 lower neutral

### L05.  `H20=H20c AND T1=T1a AND direction_exec=short`
- Raw: n=103  W=41/L=62  WR=39.8%
- Sharpen: sharpest is RSI=RSI3 (28/62 of losers there)
- **Sharp: n=36  W=8/L=28  WR=22.2%**
- **Dir: SHORT**  •  HTF20 neutral; 1h trend WITH trade  •  ONLY when RSI 40-50 lower neutral

### L06.  `H20=H20c AND H60=H60a AND T1=T1a AND direction_exec=short`
- Raw: n=103  W=41/L=62  WR=39.8%
- Sharpen: sharpest is RSI=RSI3 (28/62 of losers there)
- **Sharp: n=36  W=8/L=28  WR=22.2%**
- **Dir: SHORT**  •  HTF20 neutral; HTF60 aligned WITH trade; 1h trend WITH trade  •  ONLY when RSI 40-50 lower neutral

### L07.  `H20=H20c AND T1=T1a AND T4=T4a`
- Raw: n=85  W=32/L=53  WR=37.6%
- Sharpen: sharpest is ZS=ZS1 (14/53 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  HTF20 neutral; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when zscore -3 to -2 deep oversold

### L08.  `H20=H20c AND H60=H60a AND T1=T1a AND T4=T4a`
- Raw: n=85  W=32/L=53  WR=37.6%
- Sharpen: sharpest is ZS=ZS1 (14/53 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  HTF20 neutral; HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when zscore -3 to -2 deep oversold

### L09.  `H20=H20c AND T1=T1a AND T4=T4a AND direction_exec=short`
- Raw: n=85  W=32/L=53  WR=37.6%
- Sharpen: sharpest is ZS=ZS1 (14/53 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: SHORT**  •  HTF20 neutral; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when zscore -3 to -2 deep oversold

### L10.  `H60=H60e AND ZS=ZS5 AND direction_exec=long`
- Raw: n=78  W=27/L=51  WR=34.6%
- Sharpen: sharpest is BBP=BBP6 (29/51 of losers there)
- **Sharp: n=35  W=6/L=29  WR=17.1%**
- **Dir: LONG**  •  HTF60 strongly against; zscore +2 to +3 deep overbought  •  ONLY when deep above upper band

### L11.  `H60=H60b AND T4=T4a AND direction_exec=short`
- Raw: n=77  W=28/L=49  WR=36.4%
- Sharpen: sharpest is T1=T1c (26/49 of losers there)
- **Sharp: n=27  W=1/L=26  WR=3.7%**
- **Dir: SHORT**  •  HTF60 slightly aligned; 4h trend WITH trade  •  ONLY when 1h trend AGAINST trade

### L12.  `T1=T1c AND T4=T4a AND ZS=ZS4`
- Raw: n=74  W=26/L=48  WR=35.1%
- Sharpen: sharpest is H60=H60b (21/48 of losers there)
- **Sharp: n=22  W=1/L=21  WR=4.5%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; zscore +1 to +2 overbought  •  ONLY when HTF60 slightly aligned

### L13.  `T1=T1c AND T4=T4a AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=74  W=26/L=48  WR=35.1%
- Sharpen: sharpest is H60=H60b (21/48 of losers there)
- **Sharp: n=22  W=1/L=21  WR=4.5%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; upper third; zscore +1 to +2 overbought  •  ONLY when HTF60 slightly aligned

### L14.  `H20=H20c AND T4=T4a AND RSI=RSI2`
- Raw: n=71  W=28/L=43  WR=39.4%
- Sharpen: sharpest is ZS=ZS1 (14/43 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  HTF20 neutral; 4h trend WITH trade; RSI 30-40 weak  •  ONLY when zscore -3 to -2 deep oversold

### L15.  `H60=H60e AND T1=T1c AND ZS=ZS5`
- Raw: n=70  W=25/L=45  WR=35.7%
- Sharpen: sharpest is BBP=BBP6 (25/45 of losers there)
- **Sharp: n=30  W=5/L=25  WR=16.7%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when deep above upper band

### L16.  `T1=T1c AND ZS=ZS5 AND direction_exec=long`
- Raw: n=70  W=25/L=45  WR=35.7%
- Sharpen: sharpest is BBP=BBP6 (25/45 of losers there)
- **Sharp: n=30  W=5/L=25  WR=16.7%**
- **Dir: LONG**  •  1h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when deep above upper band

### L17.  `H60=H60e AND T1=T1c AND ZS=ZS5 AND direction_exec=long`
- Raw: n=70  W=25/L=45  WR=35.7%
- Sharpen: sharpest is BBP=BBP6 (25/45 of losers there)
- **Sharp: n=30  W=5/L=25  WR=16.7%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when deep above upper band

### L18.  `H20=H20b AND T4=T4a AND BBP=BBP3`
- Raw: n=68  W=26/L=42  WR=38.2%
- Sharpen: sharpest is T1=T1c (13/42 of losers there)
- **Sharp: n=15  W=2/L=13  WR=13.3%**
- **Dir: ?**  •  HTF20 slightly aligned; 4h trend WITH trade; middle of band  •  ONLY when 1h trend AGAINST trade

### L19.  `H20=H20b AND T4=T4a AND BBP=BBP3 AND ZS=ZS3`
- Raw: n=68  W=26/L=42  WR=38.2%
- Sharpen: sharpest is T1=T1c (13/42 of losers there)
- **Sharp: n=15  W=2/L=13  WR=13.3%**
- **Dir: ?**  •  HTF20 slightly aligned; 4h trend WITH trade; middle of band; zscore -1 to +1 neutral  •  ONLY when 1h trend AGAINST trade

### L20.  `H20=H20e AND H60=H60e AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=67  W=14/L=53  WR=20.9%
- Sharpen: sharpest is T4=T4c (53/53 of losers there)
- **Sharp: n=61  W=8/L=53  WR=13.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 30-40 weak; session=asia  •  ONLY when 4h trend AGAINST trade

### L21.  `T4=T4c AND ZS=ZS5 AND direction_exec=long`
- Raw: n=65  W=21/L=44  WR=32.3%
- Sharpen: sharpest is BBP=BBP6 (29/44 of losers there)
- **Sharp: n=35  W=6/L=29  WR=17.1%**
- **Dir: LONG**  •  4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when deep above upper band

### L22.  `H60=H60e AND RSI=RSI3 AND ZS=ZS5`
- Raw: n=65  W=26/L=39  WR=40.0%
- Sharpen: sharpest is BBP=BBP6 (27/39 of losers there)
- **Sharp: n=33  W=6/L=27  WR=18.2%**
- **Dir: ?**  •  HTF60 strongly against; RSI 40-50 lower neutral; zscore +2 to +3 deep overbought  •  ONLY when deep above upper band

### L23.  `T4=T4c AND RSI=RSI3 AND ZS=ZS5`
- Raw: n=65  W=26/L=39  WR=40.0%
- Sharpen: sharpest is BBP=BBP6 (27/39 of losers there)
- **Sharp: n=33  W=6/L=27  WR=18.2%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; zscore +2 to +3 deep overbought  •  ONLY when deep above upper band

### L24.  `H60=H60e AND RSI=RSI3 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=65  W=26/L=39  WR=40.0%
- Sharpen: sharpest is BBP=BBP6 (27/39 of losers there)
- **Sharp: n=33  W=6/L=27  WR=18.2%**
- **Dir: LONG**  •  HTF60 strongly against; RSI 40-50 lower neutral; zscore +2 to +3 deep overbought  •  ONLY when deep above upper band

### L25.  `H20=H20a AND T1=T1c AND BBP=BBP4`
- Raw: n=64  W=22/L=42  WR=34.4%
- Sharpen: sharpest is ZS=ZS4 (36/42 of losers there)
- **Sharp: n=50  W=14/L=36  WR=28.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; upper third  •  ONLY when zscore +1 to +2 overbought

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(34/27) | H20e(28/35) |
| H60 | — | — |
| T1 | T1a(53/48) | T1c(47/52) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
