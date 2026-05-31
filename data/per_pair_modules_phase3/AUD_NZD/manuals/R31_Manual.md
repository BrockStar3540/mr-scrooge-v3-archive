# AUD_NZD — R31 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **3,996**  (W=2,566 / L=1,430)  -  WR: **64.2%**

## Session distribution

- asia: n=1439  W=916/L=523  WR=63.7%
- ny_mid: n=571  W=368/L=203  WR=64.4%
- london_open: n=534  W=351/L=183  WR=65.7%
- ny_open: n=377  W=251/L=126  WR=66.6%
- ny_close: n=331  W=209/L=122  WR=63.1%
- off_hours: n=305  W=193/L=112  WR=63.3%
- london: n=268  W=164/L=104  WR=61.2%
- asia_late: n=171  W=114/L=57  WR=66.7%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND H60=H60a AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=238  W=204/L=34  WR=85.7%
- Refine: exclude BBP=BBP6 drops 16/34 losers (47%)
- **Final: n=185  W=167/L=18  WR=90.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 50-60 upper neutral; session=asia  •  AVOID when deep above upper band

### W02.  `H20=H20a AND RSI=RSI4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=238  W=204/L=34  WR=85.7%
- Refine: exclude BBP=BBP6 drops 16/34 losers (47%)
- **Final: n=185  W=167/L=18  WR=90.3%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 50-60 upper neutral; session=asia  •  AVOID when deep above upper band

### W03.  `H60=H60a AND T4=T4c AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=167  W=142/L=25  WR=85.0%
- Refine: exclude H20=H20b drops 10/25 losers (40%)
- **Final: n=139  W=124/L=15  WR=89.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral; session=asia  •  AVOID when HTF20 slightly aligned

### W04.  `T4=T4c AND RSI=RSI4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=167  W=142/L=25  WR=85.0%
- Refine: exclude H20=H20b drops 10/25 losers (40%)
- **Final: n=139  W=124/L=15  WR=89.2%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 50-60 upper neutral; session=asia  •  AVOID when HTF20 slightly aligned

### W05.  `H20=H20a AND T1=T1c AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=142  W=123/L=19  WR=86.6%
- Refine: exclude H60=H60e drops 6/19 losers (32%)
- **Final: n=132  W=119/L=13  WR=90.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 50-60 upper neutral; session=asia  •  AVOID when HTF60 strongly against

### W06.  `H60=H60a AND T1=T1c AND BBP=BBP5 AND RSI=RSI4`
- Raw: n=114  W=99/L=15  WR=86.8%
- Refine: exclude H20=H20e drops 3/15 losers (20%)
- **Final: n=109  W=97/L=12  WR=89.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; just touched upper band; RSI 50-60 upper neutral  •  AVOID when HTF20 strongly against

### W07.  `T1=T1c AND BBP=BBP5 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=114  W=99/L=15  WR=86.8%
- Refine: exclude H20=H20e drops 3/15 losers (20%)
- **Final: n=109  W=97/L=12  WR=89.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; just touched upper band; RSI 50-60 upper neutral  •  AVOID when HTF20 strongly against

### W08.  `H60=H60e AND BBP=BBP2 AND session_bucket=london_open`
- Raw: n=109  W=96/L=13  WR=88.1%
- Refine: exclude T1=T1a drops 11/13 losers (85%)
- **Final: n=54  W=52/L=2  WR=96.3%**
- **Dir: ?**  •  HTF60 strongly against; lower third; session=london_open  •  AVOID when 1h trend WITH trade

### W09.  `BBP=BBP2 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=109  W=96/L=13  WR=88.1%
- Refine: exclude T1=T1a drops 11/13 losers (85%)
- **Final: n=54  W=52/L=2  WR=96.3%**
- **Dir: SHORT**  •  lower third; session=london_open  •  AVOID when 1h trend WITH trade

### W10.  `H60=H60e AND BBP=BBP2 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=109  W=96/L=13  WR=88.1%
- Refine: exclude T1=T1a drops 11/13 losers (85%)
- **Final: n=54  W=52/L=2  WR=96.3%**
- **Dir: SHORT**  •  HTF60 strongly against; lower third; session=london_open  •  AVOID when 1h trend WITH trade

### W11.  `H60=H60e AND ZS=ZS2 AND session_bucket=london_open`
- Raw: n=104  W=92/L=12  WR=88.5%
- Refine: exclude T1=T1a drops 10/12 losers (83%)
- **Final: n=54  W=52/L=2  WR=96.3%**
- **Dir: ?**  •  HTF60 strongly against; zscore -2 to -1 oversold; session=london_open  •  AVOID when 1h trend WITH trade

### W12.  `ZS=ZS2 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=104  W=92/L=12  WR=88.5%
- Refine: exclude T1=T1a drops 10/12 losers (83%)
- **Final: n=54  W=52/L=2  WR=96.3%**
- **Dir: SHORT**  •  zscore -2 to -1 oversold; session=london_open  •  AVOID when 1h trend WITH trade

### W13.  `H60=H60e AND BBP=BBP2 AND ZS=ZS2 AND session_bucket=london_open`
- Raw: n=104  W=92/L=12  WR=88.5%
- Refine: exclude T1=T1a drops 10/12 losers (83%)
- **Final: n=54  W=52/L=2  WR=96.3%**
- **Dir: ?**  •  HTF60 strongly against; lower third; zscore -2 to -1 oversold; session=london_open  •  AVOID when 1h trend WITH trade

### W14.  `H60=H60e AND ZS=ZS2 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=104  W=92/L=12  WR=88.5%
- Refine: exclude T1=T1a drops 10/12 losers (83%)
- **Final: n=54  W=52/L=2  WR=96.3%**
- **Dir: SHORT**  •  HTF60 strongly against; zscore -2 to -1 oversold; session=london_open  •  AVOID when 1h trend WITH trade

### W15.  `BBP=BBP2 AND ZS=ZS2 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=104  W=92/L=12  WR=88.5%
- Refine: exclude T1=T1a drops 10/12 losers (83%)
- **Final: n=54  W=52/L=2  WR=96.3%**
- **Dir: SHORT**  •  lower third; zscore -2 to -1 oversold; session=london_open  •  AVOID when 1h trend WITH trade

### W16.  `H60=H60e AND T4=T4c AND session_bucket=london`
- Raw: n=102  W=87/L=15  WR=85.3%
- Refine: exclude RSI=RSI4 drops 10/15 losers (67%)
- **Final: n=75  W=70/L=5  WR=93.3%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; session=london  •  AVOID when RSI 50-60 upper neutral

### W17.  `T4=T4c AND direction_exec=short AND session_bucket=london`
- Raw: n=102  W=87/L=15  WR=85.3%
- Refine: exclude RSI=RSI4 drops 10/15 losers (67%)
- **Final: n=75  W=70/L=5  WR=93.3%**
- **Dir: SHORT**  •  4h trend AGAINST trade; session=london  •  AVOID when RSI 50-60 upper neutral

### W18.  `H60=H60e AND T4=T4c AND direction_exec=short AND session_bucket=london`
- Raw: n=102  W=87/L=15  WR=85.3%
- Refine: exclude RSI=RSI4 drops 10/15 losers (67%)
- **Final: n=75  W=70/L=5  WR=93.3%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend AGAINST trade; session=london  •  AVOID when RSI 50-60 upper neutral

### W19.  `T4=T4c AND RSI=RSI3 AND session_bucket=london`
- Raw: n=100  W=89/L=11  WR=89.0%
- Refine: exclude H60=H60a drops 6/11 losers (55%)
- **Final: n=75  W=70/L=5  WR=93.3%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; session=london  •  AVOID when HTF60 aligned WITH trade

### W20.  `H20=H20a AND T4=T4c AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=100  W=88/L=12  WR=88.0%
- Refine: exclude ZS=ZS4 drops 9/12 losers (75%)
- **Final: n=62  W=59/L=3  WR=95.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral; session=asia  •  AVOID when zscore +1 to +2 overbought

### W21.  `H60=H60a AND BBP=BBP5 AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=91  W=78/L=13  WR=85.7%
- Refine: exclude H20=H20d drops 4/13 losers (31%)
- **Final: n=87  W=78/L=9  WR=89.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; just touched upper band; RSI 50-60 upper neutral; session=asia  •  AVOID when HTF20 mildly against

### W22.  `BBP=BBP5 AND RSI=RSI4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=91  W=78/L=13  WR=85.7%
- Refine: exclude H20=H20d drops 4/13 losers (31%)
- **Final: n=87  W=78/L=9  WR=89.7%**
- **Dir: LONG**  •  just touched upper band; RSI 50-60 upper neutral; session=asia  •  AVOID when HTF20 mildly against

### W23.  `H20=H20e AND T4=T4c AND session_bucket=london`
- Raw: n=89  W=79/L=10  WR=88.8%
- Refine: exclude T1=T1a drops 8/10 losers (80%)
- **Final: n=47  W=45/L=2  WR=95.7%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; session=london  •  AVOID when 1h trend WITH trade

### W24.  `H60=H60e AND RSI=RSI3 AND ZS=ZS5`
- Raw: n=89  W=78/L=11  WR=87.6%
- Refine: exclude session_bucket=asia drops 6/11 losers (55%)
- **Final: n=64  W=59/L=5  WR=92.2%**
- **Dir: ?**  •  HTF60 strongly against; RSI 40-50 lower neutral; zscore +2 to +3 deep overbought  •  AVOID when session=asia

### W25.  `RSI=RSI3 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=89  W=78/L=11  WR=87.6%
- Refine: exclude session_bucket=asia drops 6/11 losers (55%)
- **Final: n=64  W=59/L=5  WR=92.2%**
- **Dir: SHORT**  •  RSI 40-50 lower neutral; zscore +2 to +3 deep overbought  •  AVOID when session=asia

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND H60=H60e AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=158  W=53/L=105  WR=33.5%
- Sharpen: sharpest is T4=T4a (32/105 of losers there)
- **Sharp: n=36  W=4/L=32  WR=11.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 50-60 upper neutral; session=asia  •  ONLY when 4h trend WITH trade

### L02.  `H20=H20e AND RSI=RSI4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=158  W=53/L=105  WR=33.5%
- Sharpen: sharpest is T4=T4a (32/105 of losers there)
- **Sharp: n=36  W=4/L=32  WR=11.1%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 50-60 upper neutral; session=asia  •  ONLY when 4h trend WITH trade

### L03.  `H20=H20a AND H60=H60a AND T1=T1a AND RSI=RSI3`
- Raw: n=128  W=50/L=78  WR=39.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=128  W=50/L=78  WR=39.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; RSI 40-50 lower neutral

### L04.  `H20=H20a AND T1=T1a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=128  W=50/L=78  WR=39.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=128  W=50/L=78  WR=39.1%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 40-50 lower neutral

### L05.  `H20=H20e AND T1=T1a AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=110  W=41/L=69  WR=37.3%
- Sharpen: sharpest is H60=H60e (64/69 of losers there)
- **Sharp: n=92  W=28/L=64  WR=30.4%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; RSI 50-60 upper neutral; session=asia  •  ONLY when HTF60 strongly against

### L06.  `H60=H60a AND T1=T1a AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=107  W=41/L=66  WR=38.3%
- Sharpen: sharpest is session_bucket=london_open (15/66 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  ONLY when session=london_open

### L07.  `T1=T1a AND RSI=RSI3 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=107  W=41/L=66  WR=38.3%
- Sharpen: sharpest is session_bucket=london_open (15/66 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  ONLY when session=london_open

### L08.  `H60=H60e AND T4=T4a AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=101  W=37/L=64  WR=36.6%
- Sharpen: sharpest is H20=H20e (32/64 of losers there)
- **Sharp: n=36  W=4/L=32  WR=11.1%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; RSI 50-60 upper neutral; session=asia  •  ONLY when HTF20 strongly against

### L09.  `T4=T4a AND RSI=RSI4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=101  W=37/L=64  WR=36.6%
- Sharpen: sharpest is H20=H20e (32/64 of losers there)
- **Sharp: n=36  W=4/L=32  WR=11.1%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 50-60 upper neutral; session=asia  •  ONLY when HTF20 strongly against

### L10.  `H60=H60e AND T4=T4a AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=95  W=37/L=58  WR=38.9%
- Sharpen: sharpest is H20=H20e (34/58 of losers there)
- **Sharp: n=42  W=8/L=34  WR=19.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; upper third; RSI 50-60 upper neutral  •  ONLY when HTF20 strongly against

### L11.  `T4=T4a AND BBP=BBP4 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=95  W=37/L=58  WR=38.9%
- Sharpen: sharpest is H20=H20e (34/58 of losers there)
- **Sharp: n=42  W=8/L=34  WR=19.0%**
- **Dir: SHORT**  •  4h trend WITH trade; upper third; RSI 50-60 upper neutral  •  ONLY when HTF20 strongly against

### L12.  `H60=H60a AND T1=T1a AND T4=T4a AND RSI=RSI3`
- Raw: n=92  W=35/L=57  WR=38.0%
- Sharpen: sharpest is session_bucket=london (16/57 of losers there)
- **Sharp: n=18  W=2/L=16  WR=11.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when session=london

### L13.  `T1=T1a AND T4=T4a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=92  W=35/L=57  WR=38.0%
- Sharpen: sharpest is session_bucket=london (16/57 of losers there)
- **Sharp: n=18  W=2/L=16  WR=11.1%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when session=london

### L14.  `H60=H60e AND T4=T4a AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=90  W=35/L=55  WR=38.9%
- Sharpen: sharpest is H20=H20e (32/55 of losers there)
- **Sharp: n=40  W=8/L=32  WR=20.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when HTF20 strongly against

### L15.  `T4=T4a AND RSI=RSI4 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=90  W=35/L=55  WR=38.9%
- Sharpen: sharpest is H20=H20e (32/55 of losers there)
- **Sharp: n=40  W=8/L=32  WR=20.0%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when HTF20 strongly against

### L16.  `H20=H20a AND H60=H60a AND session_bucket=london`
- Raw: n=87  W=30/L=57  WR=34.5%
- Sharpen: sharpest is RSI=RSI3 (38/57 of losers there)
- **Sharp: n=49  W=11/L=38  WR=22.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=london  •  ONLY when RSI 40-50 lower neutral

### L17.  `H20=H20a AND direction_exec=long AND session_bucket=london`
- Raw: n=87  W=30/L=57  WR=34.5%
- Sharpen: sharpest is RSI=RSI3 (38/57 of losers there)
- **Sharp: n=49  W=11/L=38  WR=22.4%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; session=london  •  ONLY when RSI 40-50 lower neutral

### L18.  `H20=H20a AND H60=H60a AND direction_exec=long AND session_bucket=london`
- Raw: n=87  W=30/L=57  WR=34.5%
- Sharpen: sharpest is RSI=RSI3 (38/57 of losers there)
- **Sharp: n=49  W=11/L=38  WR=22.4%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=london  •  ONLY when RSI 40-50 lower neutral

### L19.  `H60=H60a AND T1=T1a AND T4=T4c AND ZS=ZS2`
- Raw: n=86  W=33/L=53  WR=38.4%
- Sharpen: sharpest is H20=H20a (26/53 of losers there)
- **Sharp: n=33  W=7/L=26  WR=21.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade; zscore -2 to -1 oversold  •  ONLY when HTF20 aligned WITH trade

### L20.  `T1=T1a AND T4=T4c AND ZS=ZS2 AND direction_exec=long`
- Raw: n=86  W=33/L=53  WR=38.4%
- Sharpen: sharpest is H20=H20a (26/53 of losers there)
- **Sharp: n=33  W=7/L=26  WR=21.2%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend AGAINST trade; zscore -2 to -1 oversold  •  ONLY when HTF20 aligned WITH trade

### L21.  `H20=H20e AND BBP=BBP4 AND session_bucket=asia`
- Raw: n=84  W=32/L=52  WR=38.1%
- Sharpen: sharpest is H60=H60e (48/52 of losers there)
- **Sharp: n=65  W=17/L=48  WR=26.2%**
- **Dir: ?**  •  HTF20 strongly against; upper third; session=asia  •  ONLY when HTF60 strongly against

### L22.  `H60=H60a AND T4=T4a AND session_bucket=london`
- Raw: n=80  W=28/L=52  WR=35.0%
- Sharpen: sharpest is RSI=RSI3 (37/52 of losers there)
- **Sharp: n=42  W=5/L=37  WR=11.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; session=london  •  ONLY when RSI 40-50 lower neutral

### L23.  `T4=T4a AND direction_exec=long AND session_bucket=london`
- Raw: n=80  W=28/L=52  WR=35.0%
- Sharpen: sharpest is RSI=RSI3 (37/52 of losers there)
- **Sharp: n=42  W=5/L=37  WR=11.9%**
- **Dir: LONG**  •  4h trend WITH trade; session=london  •  ONLY when RSI 40-50 lower neutral

### L24.  `H60=H60a AND T4=T4a AND direction_exec=long AND session_bucket=london`
- Raw: n=80  W=28/L=52  WR=35.0%
- Sharpen: sharpest is RSI=RSI3 (37/52 of losers there)
- **Sharp: n=42  W=5/L=37  WR=11.9%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend WITH trade; session=london  •  ONLY when RSI 40-50 lower neutral

### L25.  `H60=H60e AND T1=T1a AND BBP=BBP4 AND session_bucket=asia`
- Raw: n=80  W=32/L=48  WR=40.0%
- Sharpen: sharpest is H20=H20e (32/48 of losers there)
- **Sharp: n=38  W=6/L=32  WR=15.8%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; upper third; session=asia  •  ONLY when HTF20 strongly against

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
