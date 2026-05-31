# EUR_NZD — R36 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR3**  (60-90%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **4,434**  (W=2,698 / L=1,736)  -  WR: **60.8%**

## Session distribution

- asia: n=1257  W=755/L=502  WR=60.1%
- london_open: n=1070  W=648/L=422  WR=60.6%
- ny_open: n=836  W=504/L=332  WR=60.3%
- london: n=363  W=233/L=130  WR=64.2%
- ny_mid: n=353  W=227/L=126  WR=64.3%
- ny_close: n=250  W=140/L=110  WR=56.0%
- asia_late: n=188  W=124/L=64  WR=66.0%
- off_hours: n=117  W=67/L=50  WR=57.3%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60a AND T1=T1a AND BBP=BBP2 AND direction_exec=long`
- Raw: n=150  W=128/L=22  WR=85.3%
- Refine: exclude H20=H20d drops 10/22 losers (45%)
- **Final: n=122  W=110/L=12  WR=90.2%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; lower third  •  AVOID when HTF20 mildly against

### W02.  `T1=T1a AND direction_exec=short AND session_bucket=london_open`
- Raw: n=144  W=124/L=20  WR=86.1%
- Refine: exclude H20=H20a drops 13/20 losers (65%)
- **Final: n=92  W=85/L=7  WR=92.4%**
- **Dir: SHORT**  •  1h trend WITH trade; session=london_open  •  AVOID when HTF20 aligned WITH trade

### W03.  `T1=T1a AND T4=T4c AND direction_exec=short AND session_bucket=london_open`
- Raw: n=144  W=124/L=20  WR=86.1%
- Refine: exclude H20=H20a drops 13/20 losers (65%)
- **Final: n=92  W=85/L=7  WR=92.4%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend AGAINST trade; session=london_open  •  AVOID when HTF20 aligned WITH trade

### W04.  `H60=H60e AND BBP=BBP5 AND direction_exec=short`
- Raw: n=130  W=111/L=19  WR=85.4%
- Refine: exclude T1=T1a drops 10/19 losers (53%)
- **Final: n=120  W=111/L=9  WR=92.5%**
- **Dir: SHORT**  •  HTF60 strongly against; just touched upper band  •  AVOID when 1h trend WITH trade

### W05.  `H60=H60e AND BBP=BBP5 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=130  W=111/L=19  WR=85.4%
- Refine: exclude T1=T1a drops 10/19 losers (53%)
- **Final: n=120  W=111/L=9  WR=92.5%**
- **Dir: SHORT**  •  HTF60 strongly against; just touched upper band; zscore +2 to +3 deep overbought  •  AVOID when 1h trend WITH trade

### W06.  `H60=H60e AND T1=T1c AND BBP=BBP5`
- Raw: n=128  W=111/L=17  WR=86.7%
- Refine: exclude direction_exec=long drops 8/17 losers (47%)
- **Final: n=120  W=111/L=9  WR=92.5%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; just touched upper band  •  AVOID when long

### W07.  `H60=H60e AND T1=T1c AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=128  W=111/L=17  WR=86.7%
- Refine: exclude direction_exec=long drops 8/17 losers (47%)
- **Final: n=120  W=111/L=9  WR=92.5%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; just touched upper band; zscore +2 to +3 deep overbought  •  AVOID when long

### W08.  `H60=H60a AND T4=T4a AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=124  W=106/L=18  WR=85.5%
- Refine: exclude T1=T1a drops 18/18 losers (100%)
- **Final: n=52  W=52/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; deep above upper band; zscore +2 to +3 deep overbought  •  AVOID when 1h trend WITH trade

### W09.  `T1=T1c AND T4=T4a AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=121  W=106/L=15  WR=87.6%
- Refine: exclude H60=H60b drops 7/15 losers (47%)
- **Final: n=99  W=91/L=8  WR=91.9%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when HTF60 slightly aligned

### W10.  `H60=H60e AND T1=T1c AND BBP=BBP5 AND direction_exec=short`
- Raw: n=120  W=111/L=9  WR=92.5%
- Refine: exclude session_bucket=london_open drops 7/9 losers (78%)
- **Final: n=66  W=64/L=2  WR=97.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; just touched upper band  •  AVOID when session=london_open

### W11.  `H20=H20e AND H60=H60a AND BBP=BBP2 AND direction_exec=long`
- Raw: n=115  W=104/L=11  WR=90.4%
- Refine: exclude session_bucket=london_open drops 6/11 losers (55%)
- **Final: n=101  W=96/L=5  WR=95.0%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 aligned WITH trade; lower third  •  AVOID when session=london_open

### W12.  `H20=H20e AND H60=H60a AND ZS=ZS2`
- Raw: n=115  W=98/L=17  WR=85.2%
- Refine: exclude direction_exec=short drops 9/17 losers (53%)
- **Final: n=90  W=82/L=8  WR=91.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; zscore -2 to -1 oversold  •  AVOID when short

### W13.  `H20=H20e AND H60=H60a AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=115  W=98/L=17  WR=85.2%
- Refine: exclude direction_exec=short drops 9/17 losers (53%)
- **Final: n=90  W=82/L=8  WR=91.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; lower third; zscore -2 to -1 oversold  •  AVOID when short

### W14.  `H20=H20e AND H60=H60a AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=111  W=95/L=16  WR=85.6%
- Refine: exclude BBP=BBP5 drops 6/16 losers (38%)
- **Final: n=95  W=85/L=10  WR=89.5%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; RSI 50-60 upper neutral; session=asia  •  AVOID when just touched upper band

### W15.  `T1=T1a AND ZS=ZS1 AND direction_exec=long`
- Raw: n=107  W=95/L=12  WR=88.8%
- Refine: exclude H60=H60b drops 6/12 losers (50%)
- **Final: n=89  W=83/L=6  WR=93.3%**
- **Dir: LONG**  •  1h trend WITH trade; zscore -3 to -2 deep oversold  •  AVOID when HTF60 slightly aligned

### W16.  `T1=T1a AND T4=T4c AND RSI=RSI3 AND session_bucket=london_open`
- Raw: n=107  W=94/L=13  WR=87.9%
- Refine: exclude H20=H20a drops 13/13 losers (100%)
- **Final: n=55  W=55/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral; session=london_open  •  AVOID when HTF20 aligned WITH trade

### W17.  `T1=T1a AND RSI=RSI3 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=107  W=94/L=13  WR=87.9%
- Refine: exclude H20=H20a drops 13/13 losers (100%)
- **Final: n=55  W=55/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 40-50 lower neutral; session=london_open  •  AVOID when HTF20 aligned WITH trade

### W18.  `H20=H20e AND H60=H60a AND T1=T1a AND BBP=BBP2`
- Raw: n=101  W=90/L=11  WR=89.1%
- Refine: exclude RSI=RSI3 drops 6/11 losers (55%)
- **Final: n=88  W=83/L=5  WR=94.3%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend WITH trade; lower third  •  AVOID when RSI 40-50 lower neutral

### W19.  `T1=T1a AND T4=T4c AND ZS=ZS1`
- Raw: n=97  W=90/L=7  WR=92.8%
- Refine: exclude session_bucket=ny_close drops 4/7 losers (57%)
- **Final: n=93  W=90/L=3  WR=96.8%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  AVOID when session=ny_close

### W20.  `T1=T1a AND ZS=ZS1 AND session_bucket=london_open`
- Raw: n=96  W=88/L=8  WR=91.7%
- Refine: exclude H60=H60b drops 6/8 losers (75%)
- **Final: n=78  W=76/L=2  WR=97.4%**
- **Dir: ?**  •  1h trend WITH trade; zscore -3 to -2 deep oversold; session=london_open  •  AVOID when HTF60 slightly aligned

### W21.  `T1=T1a AND BBP=BBP1 AND ZS=ZS1`
- Raw: n=93  W=83/L=10  WR=89.2%
- Refine: exclude H60=H60b drops 6/10 losers (60%)
- **Final: n=71  W=67/L=4  WR=94.4%**
- **Dir: ?**  •  1h trend WITH trade; just touched lower band; zscore -3 to -2 deep oversold  •  AVOID when HTF60 slightly aligned

### W22.  `H20=H20e AND H60=H60a AND T4=T4a AND BBP=BBP2`
- Raw: n=93  W=83/L=10  WR=89.2%
- Refine: exclude session_bucket=london_open drops 6/10 losers (60%)
- **Final: n=79  W=75/L=4  WR=94.9%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 4h trend WITH trade; lower third  •  AVOID when session=london_open

### W23.  `T1=T1a AND BBP=BBP2 AND session_bucket=ny_open`
- Raw: n=92  W=82/L=10  WR=89.1%
- Refine: exclude H20=H20a drops 10/10 losers (100%)
- **Final: n=62  W=62/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; lower third; session=ny_open  •  AVOID when HTF20 aligned WITH trade

### W24.  `H20=H20e AND H60=H60a AND ZS=ZS2 AND direction_exec=long`
- Raw: n=90  W=82/L=8  WR=91.1%
- Refine: exclude session_bucket=london_open drops 4/8 losers (50%)
- **Final: n=80  W=76/L=4  WR=95.0%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 aligned WITH trade; zscore -2 to -1 oversold  •  AVOID when session=london_open

### W25.  `T1=T1c AND T4=T4a AND BBP=BBP6 AND direction_exec=short`
- Raw: n=86  W=76/L=10  WR=88.4%
- Refine: exclude H20=H20e drops 7/10 losers (70%)
- **Final: n=72  W=69/L=3  WR=95.8%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend WITH trade; deep above upper band  •  AVOID when HTF20 strongly against

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1a AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=208  W=70/L=138  WR=33.7%
- Sharpen: sharpest is H60=H60a (76/138 of losers there)
- **Sharp: n=99  W=23/L=76  WR=23.2%**
- **Dir: ?**  •  1h trend WITH trade; just touched upper band; zscore +2 to +3 deep overbought  •  ONLY when HTF60 aligned WITH trade

### L02.  `BBP=BBP5 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=199  W=69/L=130  WR=34.7%
- Sharpen: sharpest is H20=H20a (33/130 of losers there)
- **Sharp: n=33  W=0/L=33  WR=0.0%**
- **Dir: LONG**  •  just touched upper band; zscore +2 to +3 deep overbought  •  ONLY when HTF20 aligned WITH trade

### L03.  `T1=T1c AND T4=T4a AND session_bucket=london_open`
- Raw: n=191  W=69/L=122  WR=36.1%
- Sharpen: sharpest is RSI=RSI3 (71/122 of losers there)
- **Sharp: n=82  W=11/L=71  WR=13.4%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; session=london_open  •  ONLY when RSI 40-50 lower neutral

### L04.  `T4=T4a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=189  W=67/L=122  WR=35.4%
- Sharpen: sharpest is H60=H60b (48/122 of losers there)
- **Sharp: n=59  W=11/L=48  WR=18.6%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when HTF60 slightly aligned

### L05.  `T1=T1a AND BBP=BBP5 AND direction_exec=long`
- Raw: n=182  W=60/L=122  WR=33.0%
- Sharpen: sharpest is H60=H60a (70/122 of losers there)
- **Sharp: n=83  W=13/L=70  WR=15.7%**
- **Dir: LONG**  •  1h trend WITH trade; just touched upper band  •  ONLY when HTF60 aligned WITH trade

### L06.  `T1=T1a AND BBP=BBP5 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=182  W=60/L=122  WR=33.0%
- Sharpen: sharpest is H60=H60a (70/122 of losers there)
- **Sharp: n=83  W=13/L=70  WR=15.7%**
- **Dir: LONG**  •  1h trend WITH trade; just touched upper band; zscore +2 to +3 deep overbought  •  ONLY when HTF60 aligned WITH trade

### L07.  `H60=H60a AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=171  W=56/L=115  WR=32.7%
- Sharpen: sharpest is T1=T1a (76/115 of losers there)
- **Sharp: n=99  W=23/L=76  WR=23.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; just touched upper band; zscore +2 to +3 deep overbought  •  ONLY when 1h trend WITH trade

### L08.  `H20=H20e AND H60=H60b AND session_bucket=london_open`
- Raw: n=170  W=54/L=116  WR=31.8%
- Sharpen: sharpest is RSI=RSI3 (48/116 of losers there)
- **Sharp: n=59  W=11/L=48  WR=18.6%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 slightly aligned; session=london_open  •  ONLY when RSI 40-50 lower neutral

### L09.  `H20=H20a AND RSI=RSI4 AND direction_exec=long`
- Raw: n=166  W=65/L=101  WR=39.2%
- Sharpen: sharpest is session_bucket=asia (37/101 of losers there)
- **Sharp: n=44  W=7/L=37  WR=15.9%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 50-60 upper neutral  •  ONLY when session=asia

### L10.  `H20=H20e AND T1=T1c AND BBP=BBP4`
- Raw: n=165  W=66/L=99  WR=40.0%
- Sharpen: sharpest is session_bucket=london_open (36/99 of losers there)
- **Sharp: n=44  W=8/L=36  WR=18.2%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; upper third  •  ONLY when session=london_open

### L11.  `T4=T4a AND BBP=BBP5 AND direction_exec=long`
- Raw: n=155  W=55/L=100  WR=35.5%
- Sharpen: sharpest is H20=H20a (29/100 of losers there)
- **Sharp: n=29  W=0/L=29  WR=0.0%**
- **Dir: LONG**  •  4h trend WITH trade; just touched upper band  •  ONLY when HTF20 aligned WITH trade

### L12.  `T4=T4a AND BBP=BBP5 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=155  W=55/L=100  WR=35.5%
- Sharpen: sharpest is H20=H20a (29/100 of losers there)
- **Sharp: n=29  W=0/L=29  WR=0.0%**
- **Dir: LONG**  •  4h trend WITH trade; just touched upper band; zscore +2 to +3 deep overbought  •  ONLY when HTF20 aligned WITH trade

### L13.  `H60=H60b AND T4=T4a AND session_bucket=london_open`
- Raw: n=153  W=50/L=103  WR=32.7%
- Sharpen: sharpest is RSI=RSI3 (48/103 of losers there)
- **Sharp: n=59  W=11/L=48  WR=18.6%**
- **Dir: ?**  •  HTF60 slightly aligned; 4h trend WITH trade; session=london_open  •  ONLY when RSI 40-50 lower neutral

### L14.  `H20=H20e AND H60=H60b AND T4=T4a AND session_bucket=london_open`
- Raw: n=153  W=50/L=103  WR=32.7%
- Sharpen: sharpest is RSI=RSI3 (48/103 of losers there)
- **Sharp: n=59  W=11/L=48  WR=18.6%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 slightly aligned; 4h trend WITH trade; session=london_open  •  ONLY when RSI 40-50 lower neutral

### L15.  `T1=T1a AND T4=T4c AND ZS=ZS5`
- Raw: n=150  W=57/L=93  WR=38.0%
- Sharpen: sharpest is direction_exec=long (68/93 of losers there)
- **Sharp: n=91  W=23/L=68  WR=25.3%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when long

### L16.  `H20=H20e AND T1=T1c AND session_bucket=london_open`
- Raw: n=140  W=51/L=89  WR=36.4%
- Sharpen: sharpest is BBP=BBP4 (36/89 of losers there)
- **Sharp: n=44  W=8/L=36  WR=18.2%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; session=london_open  •  ONLY when upper third

### L17.  `T1=T1a AND T4=T4a AND BBP=BBP5`
- Raw: n=138  W=46/L=92  WR=33.3%
- Sharpen: sharpest is H60=H60a (49/92 of losers there)
- **Sharp: n=58  W=9/L=49  WR=15.5%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; just touched upper band  •  ONLY when HTF60 aligned WITH trade

### L18.  `T1=T1a AND T4=T4a AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=138  W=46/L=92  WR=33.3%
- Sharpen: sharpest is H60=H60a (49/92 of losers there)
- **Sharp: n=58  W=9/L=49  WR=15.5%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; just touched upper band; zscore +2 to +3 deep overbought  •  ONLY when HTF60 aligned WITH trade

### L19.  `T1=T1a AND T4=T4a AND BBP=BBP5 AND direction_exec=long`
- Raw: n=138  W=46/L=92  WR=33.3%
- Sharpen: sharpest is H60=H60a (49/92 of losers there)
- **Sharp: n=58  W=9/L=49  WR=15.5%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; just touched upper band  •  ONLY when HTF60 aligned WITH trade

### L20.  `H20=H20e AND H60=H60b AND direction_exec=long`
- Raw: n=137  W=43/L=94  WR=31.4%
- Sharpen: sharpest is RSI=RSI3 (48/94 of losers there)
- **Sharp: n=59  W=11/L=48  WR=18.6%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 slightly aligned  •  ONLY when RSI 40-50 lower neutral

### L21.  `H60=H60b AND T4=T4a AND direction_exec=long`
- Raw: n=137  W=43/L=94  WR=31.4%
- Sharpen: sharpest is RSI=RSI3 (48/94 of losers there)
- **Sharp: n=59  W=11/L=48  WR=18.6%**
- **Dir: LONG**  •  HTF60 slightly aligned; 4h trend WITH trade  •  ONLY when RSI 40-50 lower neutral

### L22.  `H20=H20e AND H60=H60b AND T4=T4a AND direction_exec=long`
- Raw: n=137  W=43/L=94  WR=31.4%
- Sharpen: sharpest is RSI=RSI3 (48/94 of losers there)
- **Sharp: n=59  W=11/L=48  WR=18.6%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 slightly aligned; 4h trend WITH trade  •  ONLY when RSI 40-50 lower neutral

### L23.  `T1=T1c AND T4=T4a AND RSI=RSI3`
- Raw: n=134  W=39/L=95  WR=29.1%
- Sharpen: sharpest is session_bucket=london_open (71/95 of losers there)
- **Sharp: n=82  W=11/L=71  WR=13.4%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when session=london_open

### L24.  `T1=T1c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=134  W=39/L=95  WR=29.1%
- Sharpen: sharpest is session_bucket=london_open (71/95 of losers there)
- **Sharp: n=82  W=11/L=71  WR=13.4%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when session=london_open

### L25.  `T1=T1c AND T4=T4a AND RSI=RSI3 AND direction_exec=long`
- Raw: n=134  W=39/L=95  WR=29.1%
- Sharpen: sharpest is session_bucket=london_open (71/95 of losers there)
- **Sharp: n=82  W=11/L=71  WR=13.4%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when session=london_open

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | H60a(42/37) | — |
| T1 | T1a(52/45) | T1c(48/55) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
