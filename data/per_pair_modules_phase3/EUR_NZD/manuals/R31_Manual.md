# EUR_NZD — R31 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20d**  (EMA20 down 0.15-0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **5,503**  (W=3,434 / L=2,069)  -  WR: **62.4%**

## Session distribution

- asia: n=1968  W=1221/L=747  WR=62.0%
- ny_close: n=1138  W=720/L=418  WR=63.3%
- london: n=604  W=388/L=216  WR=64.2%
- asia_late: n=560  W=361/L=199  WR=64.5%
- off_hours: n=369  W=215/L=154  WR=58.3%
- ny_open: n=340  W=224/L=116  WR=65.9%
- london_open: n=312  W=182/L=130  WR=58.3%
- ny_mid: n=212  W=123/L=89  WR=58.0%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T4=T4c AND RSI=RSI3 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=234  W=203/L=31  WR=86.8%
- Refine: exclude H20=H20a drops 10/31 losers (32%)
- **Final: n=217  W=196/L=21  WR=90.3%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when HTF20 aligned WITH trade

### W02.  `H60=H60e AND ZS=ZS1 AND direction_exec=long`
- Raw: n=183  W=166/L=17  WR=90.7%
- Refine: exclude session_bucket=asia drops 10/17 losers (59%)
- **Final: n=129  W=122/L=7  WR=94.6%**
- **Dir: LONG**  •  HTF60 strongly against; zscore -3 to -2 deep oversold  •  AVOID when session=asia

### W03.  `RSI=RSI3 AND ZS=ZS1 AND direction_exec=long AND session_bucket=asia`
- Raw: n=180  W=156/L=24  WR=86.7%
- Refine: exclude H60=H60a drops 19/24 losers (79%)
- **Final: n=80  W=75/L=5  WR=93.8%**
- **Dir: LONG**  •  RSI 40-50 lower neutral; zscore -3 to -2 deep oversold; session=asia  •  AVOID when HTF60 aligned WITH trade

### W04.  `H60=H60e AND T1=T1c AND ZS=ZS1 AND direction_exec=long`
- Raw: n=158  W=142/L=16  WR=89.9%
- Refine: exclude session_bucket=asia drops 10/16 losers (62%)
- **Final: n=108  W=102/L=6  WR=94.4%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend AGAINST trade; zscore -3 to -2 deep oversold  •  AVOID when session=asia

### W05.  `T4=T4c AND BBP=BBP1 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=146  W=128/L=18  WR=87.7%
- Refine: exclude session_bucket=asia drops 12/18 losers (67%)
- **Final: n=75  W=69/L=6  WR=92.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; just touched lower band; RSI 40-50 lower neutral  •  AVOID when session=asia

### W06.  `H60=H60e AND T4=T4c AND ZS=ZS1 AND direction_exec=long`
- Raw: n=137  W=125/L=12  WR=91.2%
- Refine: exclude session_bucket=asia drops 10/12 losers (83%)
- **Final: n=93  W=91/L=2  WR=97.8%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  AVOID when session=asia

### W07.  `BBP=BBP0 AND RSI=RSI3 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=135  W=115/L=20  WR=85.2%
- Refine: exclude session_bucket=asia_late drops 14/20 losers (70%)
- **Final: n=106  W=100/L=6  WR=94.3%**
- **Dir: LONG**  •  deep below lower band; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when session=asia_late

### W08.  `H60=H60e AND RSI=RSI3 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=130  W=120/L=10  WR=92.3%
- Refine: exclude H20=H20a drops 5/10 losers (50%)
- **Final: n=114  W=109/L=5  WR=95.6%**
- **Dir: LONG**  •  HTF60 strongly against; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when HTF20 aligned WITH trade

### W09.  `H60=H60e AND BBP=BBP1 AND direction_exec=long`
- Raw: n=129  W=113/L=16  WR=87.6%
- Refine: exclude session_bucket=asia drops 10/16 losers (62%)
- **Final: n=101  W=95/L=6  WR=94.1%**
- **Dir: LONG**  •  HTF60 strongly against; just touched lower band  •  AVOID when session=asia

### W10.  `H60=H60e AND BBP=BBP1 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=129  W=113/L=16  WR=87.6%
- Refine: exclude session_bucket=asia drops 10/16 losers (62%)
- **Final: n=101  W=95/L=6  WR=94.1%**
- **Dir: LONG**  •  HTF60 strongly against; just touched lower band; zscore -3 to -2 deep oversold  •  AVOID when session=asia

### W11.  `H60=H60e AND T1=T1c AND T4=T4c AND ZS=ZS1`
- Raw: n=112  W=101/L=11  WR=90.2%
- Refine: exclude session_bucket=asia drops 10/11 losers (91%)
- **Final: n=72  W=71/L=1  WR=98.6%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  AVOID when session=asia

### W12.  `H20=H20e AND H60=H60e AND ZS=ZS1`
- Raw: n=112  W=99/L=13  WR=88.4%
- Refine: exclude session_bucket=asia drops 12/13 losers (92%)
- **Final: n=60  W=59/L=1  WR=98.3%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; zscore -3 to -2 deep oversold  •  AVOID when session=asia

### W13.  `H60=H60e AND T1=T1c AND BBP=BBP1 AND direction_exec=long`
- Raw: n=112  W=97/L=15  WR=86.6%
- Refine: exclude session_bucket=asia drops 10/15 losers (67%)
- **Final: n=88  W=83/L=5  WR=94.3%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend AGAINST trade; just touched lower band  •  AVOID when session=asia

### W14.  `H20=H20d AND RSI=RSI3 AND direction_exec=long AND session_bucket=asia`
- Raw: n=111  W=95/L=16  WR=85.6%
- Refine: exclude H60=H60e drops 11/16 losers (69%)
- **Final: n=85  W=80/L=5  WR=94.1%**
- **Dir: LONG**  •  HTF20 mildly against; RSI 40-50 lower neutral; session=asia  •  AVOID when HTF60 strongly against

### W15.  `H20=H20e AND H60=H60e AND ZS=ZS1 AND direction_exec=long`
- Raw: n=109  W=98/L=11  WR=89.9%
- Refine: exclude session_bucket=asia drops 10/11 losers (91%)
- **Final: n=59  W=58/L=1  WR=98.3%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 strongly against; zscore -3 to -2 deep oversold  •  AVOID when session=asia

### W16.  `H60=H60e AND BBP=BBP2 AND RSI=RSI3 AND session_bucket=ny_close`
- Raw: n=102  W=87/L=15  WR=85.3%
- Refine: exclude T4=T4a drops 9/15 losers (60%)
- **Final: n=82  W=76/L=6  WR=92.7%**
- **Dir: ?**  •  HTF60 strongly against; lower third; RSI 40-50 lower neutral; session=ny_close  •  AVOID when 4h trend WITH trade

### W17.  `H20=H20d AND H60=H60a AND session_bucket=asia`
- Raw: n=101  W=88/L=13  WR=87.1%
- Refine: exclude T4=T4c drops 12/13 losers (92%)
- **Final: n=56  W=55/L=1  WR=98.2%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 aligned WITH trade; session=asia  •  AVOID when 4h trend AGAINST trade

### W18.  `H20=H20e AND H60=H60e AND T4=T4a AND direction_exec=long`
- Raw: n=100  W=88/L=12  WR=88.0%
- Refine: exclude ZS=ZS3 drops 6/12 losers (50%)
- **Final: n=68  W=62/L=6  WR=91.2%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 strongly against; 4h trend WITH trade  •  AVOID when zscore -1 to +1 neutral

### W19.  `T1=T1a AND RSI=RSI3 AND direction_exec=long AND session_bucket=asia`
- Raw: n=100  W=87/L=13  WR=87.0%
- Refine: exclude H20=H20e drops 13/13 losers (100%)
- **Final: n=27  W=27/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 40-50 lower neutral; session=asia  •  AVOID when HTF20 strongly against

### W20.  `H60=H60a AND T1=T1a AND direction_exec=long AND session_bucket=london`
- Raw: n=99  W=86/L=13  WR=86.9%
- Refine: exclude H20=H20d drops 3/13 losers (23%)
- **Final: n=95  W=85/L=10  WR=89.5%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=london  •  AVOID when HTF20 mildly against

### W21.  `H60=H60b AND RSI=RSI3 AND ZS=ZS3`
- Raw: n=97  W=83/L=14  WR=85.6%
- Refine: exclude strategy_id=alpha_breakout_retest_v2 drops 5/14 losers (36%)
- **Final: n=86  W=77/L=9  WR=89.5%**
- **Dir: ?**  •  HTF60 slightly aligned; RSI 40-50 lower neutral; zscore -1 to +1 neutral  •  AVOID when strategy=alpha_breakout_retest_v2

### W22.  `H60=H60b AND T4=T4c AND ZS=ZS3`
- Raw: n=96  W=82/L=14  WR=85.4%
- Refine: exclude RSI=RSI2 drops 6/14 losers (43%)
- **Final: n=89  W=81/L=8  WR=91.0%**
- **Dir: ?**  •  HTF60 slightly aligned; 4h trend AGAINST trade; zscore -1 to +1 neutral  •  AVOID when RSI 30-40 weak

### W23.  `H20=H20d AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=93  W=88/L=5  WR=94.6%
- Refine: exclude session_bucket=ny_mid drops 3/5 losers (60%)
- **Final: n=90  W=88/L=2  WR=97.8%**
- **Dir: ?**  •  HTF20 mildly against; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when session=ny_mid

### W24.  `H20=H20e AND H60=H60e AND T4=T4c AND ZS=ZS1`
- Raw: n=93  W=82/L=11  WR=88.2%
- Refine: exclude session_bucket=asia drops 10/11 losers (91%)
- **Final: n=53  W=52/L=1  WR=98.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  AVOID when session=asia

### W25.  `H60=H60e AND T4=T4c AND BBP=BBP1 AND direction_exec=long`
- Raw: n=93  W=82/L=11  WR=88.2%
- Refine: exclude session_bucket=asia drops 10/11 losers (91%)
- **Final: n=65  W=64/L=1  WR=98.5%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend AGAINST trade; just touched lower band  •  AVOID when session=asia

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1a AND BBP=BBP0 AND direction_exec=short`
- Raw: n=199  W=78/L=121  WR=39.2%
- Sharpen: sharpest is H60=H60a (35/121 of losers there)
- **Sharp: n=39  W=4/L=35  WR=10.3%**
- **Dir: SHORT**  •  1h trend WITH trade; deep below lower band  •  ONLY when HTF60 aligned WITH trade

### L02.  `T4=T4a AND RSI=RSI3 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=188  W=75/L=113  WR=39.9%
- Sharpen: sharpest is T1=T1c (30/113 of losers there)
- **Sharp: n=35  W=5/L=30  WR=14.3%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when 1h trend AGAINST trade

### L03.  `BBP=BBP0 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=187  W=71/L=116  WR=38.0%
- Sharpen: sharpest is H60=H60a (39/116 of losers there)
- **Sharp: n=43  W=4/L=39  WR=9.3%**
- **Dir: SHORT**  •  deep below lower band; RSI 40-50 lower neutral  •  ONLY when HTF60 aligned WITH trade

### L04.  `T4=T4a AND BBP=BBP0 AND direction_exec=short`
- Raw: n=176  W=70/L=106  WR=39.8%
- Sharpen: sharpest is H60=H60a (34/106 of losers there)
- **Sharp: n=38  W=4/L=34  WR=10.5%**
- **Dir: SHORT**  •  4h trend WITH trade; deep below lower band  •  ONLY when HTF60 aligned WITH trade

### L05.  `ZS=ZS1 AND direction_exec=short AND session_bucket=asia`
- Raw: n=166  W=65/L=101  WR=39.2%
- Sharpen: sharpest is T4=T4c (46/101 of losers there)
- **Sharp: n=50  W=4/L=46  WR=8.0%**
- **Dir: SHORT**  •  zscore -3 to -2 deep oversold; session=asia  •  ONLY when 4h trend AGAINST trade

### L06.  `BBP=BBP0 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=154  W=55/L=99  WR=35.7%
- Sharpen: sharpest is H60=H60a (40/99 of losers there)
- **Sharp: n=44  W=4/L=40  WR=9.1%**
- **Dir: SHORT**  •  deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when HTF60 aligned WITH trade

### L07.  `T1=T1a AND BBP=BBP0 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=145  W=53/L=92  WR=36.6%
- Sharpen: sharpest is H60=H60a (35/92 of losers there)
- **Sharp: n=39  W=4/L=35  WR=10.3%**
- **Dir: SHORT**  •  1h trend WITH trade; deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when HTF60 aligned WITH trade

### L08.  `BBP=BBP2 AND RSI=RSI3 AND direction_exec=short AND session_bucket=asia`
- Raw: n=138  W=53/L=85  WR=38.4%
- Sharpen: no sharper sub-pattern
- **Sharp: n=138  W=53/L=85  WR=38.4%**
- **Dir: SHORT**  •  lower third; RSI 40-50 lower neutral; session=asia

### L09.  `BBP=BBP0 AND RSI=RSI3 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=133  W=46/L=87  WR=34.6%
- Sharpen: sharpest is H60=H60a (39/87 of losers there)
- **Sharp: n=43  W=4/L=39  WR=9.3%**
- **Dir: SHORT**  •  deep below lower band; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when HTF60 aligned WITH trade

### L10.  `RSI=RSI3 AND ZS=ZS1 AND direction_exec=short AND session_bucket=asia`
- Raw: n=132  W=41/L=91  WR=31.1%
- Sharpen: sharpest is T4=T4c (37/91 of losers there)
- **Sharp: n=41  W=4/L=37  WR=9.8%**
- **Dir: SHORT**  •  RSI 40-50 lower neutral; zscore -3 to -2 deep oversold; session=asia  •  ONLY when 4h trend AGAINST trade

### L11.  `BBP=BBP6 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=124  W=43/L=81  WR=34.7%
- Sharpen: sharpest is session_bucket=asia (35/81 of losers there)
- **Sharp: n=44  W=9/L=35  WR=20.5%**
- **Dir: LONG**  •  deep above upper band; RSI 40-50 lower neutral  •  ONLY when session=asia

### L12.  `H20=H20a AND BBP=BBP0 AND direction_exec=short`
- Raw: n=122  W=40/L=82  WR=32.8%
- Sharpen: sharpest is T4=T4c (24/82 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; deep below lower band  •  ONLY when 4h trend AGAINST trade

### L13.  `H20=H20a AND T1=T1a AND BBP=BBP0`
- Raw: n=116  W=44/L=72  WR=37.9%
- Sharpen: sharpest is T4=T4c (24/72 of losers there)
- **Sharp: n=29  W=5/L=24  WR=17.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; deep below lower band  •  ONLY when 4h trend AGAINST trade

### L14.  `T4=T4c AND BBP=BBP4 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=115  W=46/L=69  WR=40.0%
- Sharpen: sharpest is H60=H60e (33/69 of losers there)
- **Sharp: n=43  W=10/L=33  WR=23.3%**
- **Dir: SHORT**  •  4h trend AGAINST trade; upper third; RSI 40-50 lower neutral  •  ONLY when HTF60 strongly against

### L15.  `T4=T4a AND BBP=BBP0 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=113  W=45/L=68  WR=39.8%
- Sharpen: sharpest is H60=H60a (34/68 of losers there)
- **Sharp: n=38  W=4/L=34  WR=10.5%**
- **Dir: SHORT**  •  4h trend WITH trade; deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when HTF60 aligned WITH trade

### L16.  `H20=H20a AND T1=T1a AND BBP=BBP0 AND direction_exec=short`
- Raw: n=111  W=39/L=72  WR=35.1%
- Sharpen: sharpest is T4=T4c (24/72 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend WITH trade; deep below lower band  •  ONLY when 4h trend AGAINST trade

### L17.  `BBP=BBP6 AND RSI=RSI3 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=111  W=43/L=68  WR=38.7%
- Sharpen: sharpest is T4=T4a (20/68 of losers there)
- **Sharp: n=22  W=2/L=20  WR=9.1%**
- **Dir: LONG**  •  deep above upper band; RSI 40-50 lower neutral; zscore +2 to +3 deep overbought  •  ONLY when 4h trend WITH trade

### L18.  `H20=H20a AND BBP=BBP0 AND RSI=RSI3`
- Raw: n=109  W=33/L=76  WR=30.3%
- Sharpen: sharpest is T4=T4c (33/76 of losers there)
- **Sharp: n=35  W=2/L=33  WR=5.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; deep below lower band; RSI 40-50 lower neutral  •  ONLY when 4h trend AGAINST trade

### L19.  `H20=H20e AND T4=T4c AND BBP=BBP6 AND direction_exec=long`
- Raw: n=106  W=42/L=64  WR=39.6%
- Sharpen: sharpest is session_bucket=asia (24/64 of losers there)
- **Sharp: n=28  W=4/L=24  WR=14.3%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend AGAINST trade; deep above upper band  •  ONLY when session=asia

### L20.  `T4=T4c AND ZS=ZS1 AND direction_exec=short`
- Raw: n=102  W=40/L=62  WR=39.2%
- Sharpen: sharpest is session_bucket=asia (46/62 of losers there)
- **Sharp: n=50  W=4/L=46  WR=8.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when session=asia

### L21.  `T1=T1a AND T4=T4c AND ZS=ZS1 AND direction_exec=short`
- Raw: n=101  W=40/L=61  WR=39.6%
- Sharpen: sharpest is session_bucket=asia (46/61 of losers there)
- **Sharp: n=50  W=4/L=46  WR=8.0%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when session=asia

### L22.  `H20=H20a AND H60=H60e AND T4=T4c AND session_bucket=asia`
- Raw: n=100  W=27/L=73  WR=27.0%
- Sharpen: sharpest is RSI=RSI3 (63/73 of losers there)
- **Sharp: n=74  W=11/L=63  WR=14.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 4h trend AGAINST trade; session=asia  •  ONLY when RSI 40-50 lower neutral

### L23.  `T1=T1a AND T4=T4c AND RSI=RSI3 AND ZS=ZS4`
- Raw: n=99  W=37/L=62  WR=37.4%
- Sharpen: sharpest is H60=H60e (35/62 of losers there)
- **Sharp: n=47  W=12/L=35  WR=25.5%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral; zscore +1 to +2 overbought  •  ONLY when HTF60 strongly against

### L24.  `H20=H20a AND BBP=BBP0 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=98  W=31/L=67  WR=31.6%
- Sharpen: sharpest is T4=T4c (24/67 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; deep below lower band; RSI 40-50 lower neutral  •  ONLY when 4h trend AGAINST trade

### L25.  `H60=H60a AND RSI=RSI3 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=96  W=38/L=58  WR=39.6%
- Sharpen: sharpest is BBP=BBP0 (39/58 of losers there)
- **Sharp: n=43  W=4/L=39  WR=9.3%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when deep below lower band

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | H20a(33/40) |
| H60 | — | — |
| T1 | — | — |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(54/46) | short(46/54) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
