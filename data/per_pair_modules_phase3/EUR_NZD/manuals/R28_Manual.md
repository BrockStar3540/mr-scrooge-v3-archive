# EUR_NZD — R28 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR3**  (60-90%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **3,372**  (W=2,048 / L=1,324)  -  WR: **60.7%**

## Session distribution

- asia: n=1485  W=908/L=577  WR=61.1%
- ny_close: n=627  W=381/L=246  WR=60.8%
- london: n=348  W=218/L=130  WR=62.6%
- off_hours: n=314  W=179/L=135  WR=57.0%
- ny_open: n=234  W=144/L=90  WR=61.5%
- asia_late: n=162  W=93/L=69  WR=57.4%
- london_open: n=153  W=93/L=60  WR=60.8%
- ny_mid: n=49  W=32/L=17  WR=65.3%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60e AND T1=T1a AND RSI=RSI4 AND direction_exec=long`
- Raw: n=181  W=160/L=21  WR=88.4%
- Refine: exclude T4=T4c drops 21/21 losers (100%)
- **Final: n=66  W=66/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when 4h trend AGAINST trade

### W02.  `RSI=RSI4 AND direction_exec=long AND session_bucket=london`
- Raw: n=167  W=147/L=20  WR=88.0%
- Refine: exclude T4=T4c drops 18/20 losers (90%)
- **Final: n=76  W=74/L=2  WR=97.4%**
- **Dir: LONG**  •  RSI 50-60 upper neutral; session=london  •  AVOID when 4h trend AGAINST trade

### W03.  `H60=H60e AND T4=T4a AND RSI=RSI4 AND direction_exec=long`
- Raw: n=165  W=148/L=17  WR=89.7%
- Refine: exclude T1=T1c drops 17/17 losers (100%)
- **Final: n=66  W=66/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when 1h trend AGAINST trade

### W04.  `T4=T4a AND RSI=RSI4 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=163  W=144/L=19  WR=88.3%
- Refine: exclude BBP=BBP5 drops 13/19 losers (68%)
- **Final: n=90  W=84/L=6  WR=93.3%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when just touched upper band

### W05.  `H60=H60e AND RSI=RSI4 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=157  W=135/L=22  WR=86.0%
- Refine: exclude T4=T4c drops 17/22 losers (77%)
- **Final: n=97  W=92/L=5  WR=94.8%**
- **Dir: LONG**  •  HTF60 strongly against; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when 4h trend AGAINST trade

### W06.  `H20=H20a AND T4=T4a AND RSI=RSI4 AND direction_exec=long`
- Raw: n=141  W=123/L=18  WR=87.2%
- Refine: exclude session_bucket=ny_close drops 11/18 losers (61%)
- **Final: n=98  W=91/L=7  WR=92.9%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when session=ny_close

### W07.  `T1=T1a AND RSI=RSI4 AND direction_exec=long AND session_bucket=london`
- Raw: n=131  W=114/L=17  WR=87.0%
- Refine: exclude T4=T4c drops 15/17 losers (88%)
- **Final: n=76  W=74/L=2  WR=97.4%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 50-60 upper neutral; session=london  •  AVOID when 4h trend AGAINST trade

### W08.  `T1=T1a AND RSI=RSI4 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=117  W=101/L=16  WR=86.3%
- Refine: exclude H20=H20a drops 11/16 losers (69%)
- **Final: n=85  W=80/L=5  WR=94.1%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 50-60 upper neutral; session=ny_close  •  AVOID when HTF20 aligned WITH trade

### W09.  `H60=H60e AND direction_exec=long AND session_bucket=off_hours`
- Raw: n=114  W=100/L=14  WR=87.7%
- Refine: exclude RSI=RSI3 drops 14/14 losers (100%)
- **Final: n=71  W=71/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 strongly against; session=off_hours  •  AVOID when RSI 40-50 lower neutral

### W10.  `H20=H20e AND H60=H60e AND RSI=RSI4 AND direction_exec=long`
- Raw: n=111  W=95/L=16  WR=85.6%
- Refine: exclude session_bucket=asia drops 12/16 losers (75%)
- **Final: n=80  W=76/L=4  WR=95.0%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 strongly against; RSI 50-60 upper neutral  •  AVOID when session=asia

### W11.  `H60=H60a AND T4=T4c AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=110  W=97/L=13  WR=88.2%
- Refine: exclude T1=T1c drops 6/13 losers (46%)
- **Final: n=91  W=84/L=7  WR=92.3%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=ny_close  •  AVOID when 1h trend AGAINST trade

### W12.  `H60=H60e AND T4=T4a AND ZS=ZS5 AND direction_exec=long`
- Raw: n=106  W=94/L=12  WR=88.7%
- Refine: exclude RSI=RSI3 drops 7/12 losers (58%)
- **Final: n=97  W=92/L=5  WR=94.8%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when RSI 40-50 lower neutral

### W13.  `T4=T4a AND BBP=BBP6 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=106  W=92/L=14  WR=86.8%
- Refine: exclude ZS=ZS6 drops 8/14 losers (57%)
- **Final: n=90  W=84/L=6  WR=93.3%**
- **Dir: LONG**  •  4h trend WITH trade; deep above upper band; RSI 50-60 upper neutral  •  AVOID when zscore >+3 extreme

### W14.  `T4=T4c AND RSI=RSI4 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=105  W=90/L=15  WR=85.7%
- Refine: exclude H20=H20a drops 6/15 losers (40%)
- **Final: n=99  W=90/L=9  WR=90.9%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 50-60 upper neutral; session=ny_close  •  AVOID when HTF20 aligned WITH trade

### W15.  `T4=T4a AND BBP=BBP6 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=100  W=86/L=14  WR=86.0%
- Refine: exclude RSI=RSI3 drops 8/14 losers (57%)
- **Final: n=90  W=84/L=6  WR=93.3%**
- **Dir: LONG**  •  4h trend WITH trade; deep above upper band; zscore +2 to +3 deep overbought  •  AVOID when RSI 40-50 lower neutral

### W16.  `H60=H60a AND T1=T1a AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=99  W=87/L=12  WR=87.9%
- Refine: exclude BBP=BBP6 drops 6/12 losers (50%)
- **Final: n=93  W=87/L=6  WR=93.5%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=ny_close  •  AVOID when deep above upper band

### W17.  `H60=H60e AND T1=T1a AND T4=T4a AND direction_exec=long`
- Raw: n=97  W=88/L=9  WR=90.7%
- Refine: exclude session_bucket=asia drops 9/9 losers (100%)
- **Final: n=86  W=86/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when session=asia

### W18.  `H60=H60e AND T4=T4c AND session_bucket=off_hours`
- Raw: n=95  W=90/L=5  WR=94.7%
- Refine: exclude H20=H20c drops 5/5 losers (100%)
- **Final: n=76  W=76/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; session=off_hours  •  AVOID when HTF20 neutral

### W19.  `H60=H60e AND RSI=RSI4 AND direction_exec=long AND session_bucket=london`
- Raw: n=95  W=86/L=9  WR=90.5%
- Refine: exclude T4=T4c drops 9/9 losers (100%)
- **Final: n=48  W=48/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 strongly against; RSI 50-60 upper neutral; session=london  •  AVOID when 4h trend AGAINST trade

### W20.  `H60=H60a AND T1=T1a AND T4=T4c AND session_bucket=ny_close`
- Raw: n=94  W=84/L=10  WR=89.4%
- Refine: exclude H20=H20a drops 3/10 losers (30%)
- **Final: n=91  W=84/L=7  WR=92.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade; session=ny_close  •  AVOID when HTF20 aligned WITH trade

### W21.  `H60=H60e AND RSI=RSI4 AND session_bucket=off_hours`
- Raw: n=91  W=82/L=9  WR=90.1%
- Refine: exclude T4=T4a drops 9/9 losers (100%)
- **Final: n=71  W=71/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; RSI 50-60 upper neutral; session=off_hours  •  AVOID when 4h trend WITH trade

### W22.  `H60=H60e AND T4=T4c AND direction_exec=long AND session_bucket=off_hours`
- Raw: n=90  W=85/L=5  WR=94.4%
- Refine: exclude H20=H20c drops 5/5 losers (100%)
- **Final: n=71  W=71/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend AGAINST trade; session=off_hours  •  AVOID when HTF20 neutral

### W23.  `BBP=BBP4 AND direction_exec=long AND session_bucket=london`
- Raw: n=89  W=79/L=10  WR=88.8%
- Refine: exclude H60=H60a drops 6/10 losers (60%)
- **Final: n=69  W=65/L=4  WR=94.2%**
- **Dir: LONG**  •  upper third; session=london  •  AVOID when HTF60 aligned WITH trade

### W24.  `H60=H60e AND BBP=BBP5 AND direction_exec=long`
- Raw: n=88  W=77/L=11  WR=87.5%
- Refine: exclude H20=H20e drops 5/11 losers (45%)
- **Final: n=76  W=70/L=6  WR=92.1%**
- **Dir: LONG**  •  HTF60 strongly against; just touched upper band  •  AVOID when HTF20 strongly against

### W25.  `H60=H60e AND BBP=BBP5 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=88  W=77/L=11  WR=87.5%
- Refine: exclude H20=H20e drops 5/11 losers (45%)
- **Final: n=76  W=70/L=6  WR=92.1%**
- **Dir: LONG**  •  HTF60 strongly against; just touched upper band; zscore +2 to +3 deep overbought  •  AVOID when HTF20 strongly against

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `RSI=RSI4 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=317  W=126/L=191  WR=39.7%
- Sharpen: sharpest is T4=T4c (101/191 of losers there)
- **Sharp: n=136  W=35/L=101  WR=25.7%**
- **Dir: SHORT**  •  RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when 4h trend AGAINST trade

### L02.  `BBP=BBP5 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=185  W=67/L=118  WR=36.2%
- Sharpen: sharpest is H60=H60e (56/118 of losers there)
- **Sharp: n=74  W=18/L=56  WR=24.3%**
- **Dir: SHORT**  •  just touched upper band; zscore +2 to +3 deep overbought  •  ONLY when HTF60 strongly against

### L03.  `BBP=BBP5 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=182  W=65/L=117  WR=35.7%
- Sharpen: sharpest is H60=H60e (56/117 of losers there)
- **Sharp: n=74  W=18/L=56  WR=24.3%**
- **Dir: SHORT**  •  just touched upper band; RSI 50-60 upper neutral  •  ONLY when HTF60 strongly against

### L04.  `BBP=BBP5 AND RSI=RSI4 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=182  W=65/L=117  WR=35.7%
- Sharpen: sharpest is H60=H60e (56/117 of losers there)
- **Sharp: n=74  W=18/L=56  WR=24.3%**
- **Dir: SHORT**  •  just touched upper band; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when HTF60 strongly against

### L05.  `T1=T1c AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=179  W=64/L=115  WR=35.8%
- Sharpen: sharpest is H60=H60e (55/115 of losers there)
- **Sharp: n=67  W=12/L=55  WR=17.9%**
- **Dir: SHORT**  •  1h trend AGAINST trade; session=ny_close  •  ONLY when HTF60 strongly against

### L06.  `H60=H60a AND T1=T1c AND T4=T4c`
- Raw: n=160  W=60/L=100  WR=37.5%
- Sharpen: sharpest is direction_exec=short (48/100 of losers there)
- **Sharp: n=54  W=6/L=48  WR=11.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when short

### L07.  `T4=T4c AND ZS=ZS5 AND direction_exec=short`
- Raw: n=150  W=46/L=104  WR=30.7%
- Sharpen: sharpest is session_bucket=london (26/104 of losers there)
- **Sharp: n=26  W=0/L=26  WR=0.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when session=london

### L08.  `T4=T4c AND BBP=BBP6 AND RSI=RSI4`
- Raw: n=142  W=46/L=96  WR=32.4%
- Sharpen: sharpest is T1=T1c (37/96 of losers there)
- **Sharp: n=41  W=4/L=37  WR=9.8%**
- **Dir: ?**  •  4h trend AGAINST trade; deep above upper band; RSI 50-60 upper neutral  •  ONLY when 1h trend AGAINST trade

### L09.  `T1=T1a AND T4=T4c AND RSI=RSI4 AND direction_exec=short`
- Raw: n=138  W=47/L=91  WR=34.1%
- Sharpen: sharpest is H60=H60e (43/91 of losers there)
- **Sharp: n=53  W=10/L=43  WR=18.9%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when HTF60 strongly against

### L10.  `T4=T4c AND RSI=RSI4 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=136  W=35/L=101  WR=25.7%
- Sharpen: sharpest is BBP=BBP6 (45/101 of losers there)
- **Sharp: n=51  W=6/L=45  WR=11.8%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when deep above upper band

### L11.  `H60=H60a AND ZS=ZS5 AND direction_exec=short`
- Raw: n=136  W=54/L=82  WR=39.7%
- Sharpen: sharpest is T4=T4c (56/82 of losers there)
- **Sharp: n=76  W=20/L=56  WR=26.3%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; zscore +2 to +3 deep overbought  •  ONLY when 4h trend AGAINST trade

### L12.  `H60=H60a AND T1=T1c AND RSI=RSI4 AND direction_exec=short`
- Raw: n=134  W=52/L=82  WR=38.8%
- Sharpen: sharpest is T4=T4c (36/82 of losers there)
- **Sharp: n=36  W=0/L=36  WR=0.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when 4h trend AGAINST trade

### L13.  `H60=H60e AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=132  W=43/L=89  WR=32.6%
- Sharpen: sharpest is RSI=RSI4 (55/89 of losers there)
- **Sharp: n=65  W=10/L=55  WR=15.4%**
- **Dir: SHORT**  •  HTF60 strongly against; session=ny_close  •  ONLY when RSI 50-60 upper neutral

### L14.  `RSI=RSI4 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=130  W=41/L=89  WR=31.5%
- Sharpen: sharpest is H60=H60e (55/89 of losers there)
- **Sharp: n=65  W=10/L=55  WR=15.4%**
- **Dir: SHORT**  •  RSI 50-60 upper neutral; session=ny_close  •  ONLY when HTF60 strongly against

### L15.  `T1=T1a AND RSI=RSI4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=129  W=40/L=89  WR=31.0%
- Sharpen: sharpest is H60=H60e (41/89 of losers there)
- **Sharp: n=48  W=7/L=41  WR=14.6%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 50-60 upper neutral; session=asia  •  ONLY when HTF60 strongly against

### L16.  `H60=H60a AND RSI=RSI4 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=125  W=47/L=78  WR=37.6%
- Sharpen: sharpest is T4=T4c (55/78 of losers there)
- **Sharp: n=68  W=13/L=55  WR=19.1%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when 4h trend AGAINST trade

### L17.  `T1=T1c AND RSI=RSI4 AND session_bucket=ny_close`
- Raw: n=124  W=46/L=78  WR=37.1%
- Sharpen: sharpest is H60=H60e (47/78 of losers there)
- **Sharp: n=59  W=12/L=47  WR=20.3%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; session=ny_close  •  ONLY when HTF60 strongly against

### L18.  `H60=H60e AND ZS=ZS5 AND direction_exec=short`
- Raw: n=119  W=39/L=80  WR=32.8%
- Sharpen: sharpest is RSI=RSI4 (79/80 of losers there)
- **Sharp: n=107  W=28/L=79  WR=26.2%**
- **Dir: SHORT**  •  HTF60 strongly against; zscore +2 to +3 deep overbought  •  ONLY when RSI 50-60 upper neutral

### L19.  `RSI=RSI4 AND direction_exec=short AND session_bucket=london`
- Raw: n=117  W=36/L=81  WR=30.8%
- Sharpen: sharpest is T4=T4c (39/81 of losers there)
- **Sharp: n=42  W=3/L=39  WR=7.1%**
- **Dir: SHORT**  •  RSI 50-60 upper neutral; session=london  •  ONLY when 4h trend AGAINST trade

### L20.  `H20=H20e AND T4=T4c AND RSI=RSI4 AND direction_exec=short`
- Raw: n=115  W=37/L=78  WR=32.2%
- Sharpen: sharpest is BBP=BBP6 (31/78 of losers there)
- **Sharp: n=33  W=2/L=31  WR=6.1%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when deep above upper band

### L21.  `T4=T4c AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=114  W=44/L=70  WR=38.6%
- Sharpen: sharpest is H20=H20e (36/70 of losers there)
- **Sharp: n=46  W=10/L=36  WR=21.7%**
- **Dir: SHORT**  •  4h trend AGAINST trade; session=ny_close  •  ONLY when HTF20 strongly against

### L22.  `T1=T1c AND BBP=BBP5 AND direction_exec=short`
- Raw: n=113  W=42/L=71  WR=37.2%
- Sharpen: sharpest is H60=H60e (34/71 of losers there)
- **Sharp: n=40  W=6/L=34  WR=15.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; just touched upper band  •  ONLY when HTF60 strongly against

### L23.  `T1=T1c AND BBP=BBP5 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=113  W=42/L=71  WR=37.2%
- Sharpen: sharpest is H60=H60e (34/71 of losers there)
- **Sharp: n=40  W=6/L=34  WR=15.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; just touched upper band; zscore +2 to +3 deep overbought  •  ONLY when HTF60 strongly against

### L24.  `T1=T1c AND BBP=BBP5 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=112  W=42/L=70  WR=37.5%
- Sharpen: sharpest is H60=H60e (34/70 of losers there)
- **Sharp: n=40  W=6/L=34  WR=15.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; just touched upper band; RSI 50-60 upper neutral  •  ONLY when HTF60 strongly against

### L25.  `H60=H60a AND T4=T4c AND RSI=RSI4 AND direction_exec=short`
- Raw: n=109  W=29/L=80  WR=26.6%
- Sharpen: sharpest is T1=T1c (36/80 of losers there)
- **Sharp: n=36  W=0/L=36  WR=0.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when 1h trend AGAINST trade

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | — |
| T1 | T1a(53/44) | T1c(47/56) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(58/42) | short(42/58) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
