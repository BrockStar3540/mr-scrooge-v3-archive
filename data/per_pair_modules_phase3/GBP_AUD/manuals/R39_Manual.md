# GBP_AUD — R39 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20d**  (EMA20 down 0.15-0.5x)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **3,853**  (W=2,373 / L=1,480)  -  WR: **61.6%**

## Session distribution

- london_open: n=923  W=581/L=342  WR=62.9%
- asia: n=717  W=453/L=264  WR=63.2%
- ny_mid: n=708  W=419/L=289  WR=59.2%
- ny_close: n=559  W=345/L=214  WR=61.7%
- london: n=412  W=254/L=158  WR=61.7%
- ny_open: n=364  W=219/L=145  WR=60.2%
- asia_late: n=93  W=56/L=37  WR=60.2%
- off_hours: n=77  W=46/L=31  WR=59.7%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60a AND T1=T1a AND RSI=RSI2`
- Raw: n=165  W=156/L=9  WR=94.5%
- Refine: exclude session_bucket=london_open drops 9/9 losers (100%)
- **Final: n=129  W=129/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 30-40 weak  •  AVOID when session=london_open

### W02.  `H60=H60a AND RSI=RSI2 AND direction_exec=short`
- Raw: n=165  W=156/L=9  WR=94.5%
- Refine: exclude session_bucket=london_open drops 9/9 losers (100%)
- **Final: n=129  W=129/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; RSI 30-40 weak  •  AVOID when session=london_open

### W03.  `T1=T1a AND RSI=RSI2 AND direction_exec=short`
- Raw: n=165  W=156/L=9  WR=94.5%
- Refine: exclude session_bucket=london_open drops 9/9 losers (100%)
- **Final: n=129  W=129/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 30-40 weak  •  AVOID when session=london_open

### W04.  `H60=H60a AND T1=T1a AND RSI=RSI2 AND direction_exec=short`
- Raw: n=165  W=156/L=9  WR=94.5%
- Refine: exclude session_bucket=london_open drops 9/9 losers (100%)
- **Final: n=129  W=129/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 30-40 weak  •  AVOID when session=london_open

### W05.  `H20=H20a AND RSI=RSI3 AND session_bucket=ny_close`
- Raw: n=161  W=145/L=16  WR=90.1%
- Refine: exclude T1=T1c drops 15/16 losers (94%)
- **Final: n=67  W=66/L=1  WR=98.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 40-50 lower neutral; session=ny_close  •  AVOID when 1h trend AGAINST trade

### W06.  `H20=H20a AND T4=T4c AND session_bucket=ny_close`
- Raw: n=145  W=129/L=16  WR=89.0%
- Refine: exclude T1=T1c drops 15/16 losers (94%)
- **Final: n=61  W=60/L=1  WR=98.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; session=ny_close  •  AVOID when 1h trend AGAINST trade

### W07.  `H20=H20a AND T4=T4c AND RSI=RSI3 AND session_bucket=ny_close`
- Raw: n=145  W=129/L=16  WR=89.0%
- Refine: exclude T1=T1c drops 15/16 losers (94%)
- **Final: n=61  W=60/L=1  WR=98.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral; session=ny_close  •  AVOID when 1h trend AGAINST trade

### W08.  `H60=H60a AND T4=T4c AND BBP=BBP4 AND RSI=RSI3`
- Raw: n=131  W=113/L=18  WR=86.3%
- Refine: exclude ZS=ZS3 drops 11/18 losers (61%)
- **Final: n=89  W=82/L=7  WR=92.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; upper third; RSI 40-50 lower neutral  •  AVOID when zscore -1 to +1 neutral

### W09.  `T4=T4c AND BBP=BBP4 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=131  W=113/L=18  WR=86.3%
- Refine: exclude ZS=ZS3 drops 11/18 losers (61%)
- **Final: n=89  W=82/L=7  WR=92.1%**
- **Dir: SHORT**  •  4h trend AGAINST trade; upper third; RSI 40-50 lower neutral  •  AVOID when zscore -1 to +1 neutral

### W10.  `H60=H60a AND T1=T1c AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=124  W=107/L=17  WR=86.3%
- Refine: exclude ZS=ZS2 drops 8/17 losers (47%)
- **Final: n=88  W=79/L=9  WR=89.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 40-50 lower neutral; session=asia  •  AVOID when zscore -2 to -1 oversold

### W11.  `T1=T1c AND RSI=RSI3 AND direction_exec=short AND session_bucket=asia`
- Raw: n=124  W=107/L=17  WR=86.3%
- Refine: exclude ZS=ZS2 drops 8/17 losers (47%)
- **Final: n=88  W=79/L=9  WR=89.8%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 40-50 lower neutral; session=asia  •  AVOID when zscore -2 to -1 oversold

### W12.  `T1=T1a AND ZS=ZS1 AND session_bucket=ny_mid`
- Raw: n=123  W=113/L=10  WR=91.9%
- Refine: exclude H20=H20a drops 10/10 losers (100%)
- **Final: n=72  W=72/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; zscore -3 to -2 deep oversold; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

### W13.  `T1=T1a AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=121  W=103/L=18  WR=85.1%
- Refine: exclude H20=H20a drops 10/18 losers (56%)
- **Final: n=98  W=90/L=8  WR=91.8%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

### W14.  `H60=H60a AND ZS=ZS1 AND session_bucket=ny_mid`
- Raw: n=118  W=103/L=15  WR=87.3%
- Refine: exclude RSI=RSI3 drops 15/15 losers (100%)
- **Final: n=68  W=68/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; zscore -3 to -2 deep oversold; session=ny_mid  •  AVOID when RSI 40-50 lower neutral

### W15.  `ZS=ZS1 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=118  W=103/L=15  WR=87.3%
- Refine: exclude RSI=RSI3 drops 15/15 losers (100%)
- **Final: n=68  W=68/L=0  WR=100.0%**
- **Dir: SHORT**  •  zscore -3 to -2 deep oversold; session=ny_mid  •  AVOID when RSI 40-50 lower neutral

### W16.  `H60=H60a AND ZS=ZS1 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=118  W=103/L=15  WR=87.3%
- Refine: exclude RSI=RSI3 drops 15/15 losers (100%)
- **Final: n=68  W=68/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; zscore -3 to -2 deep oversold; session=ny_mid  •  AVOID when RSI 40-50 lower neutral

### W17.  `H20=H20a AND H60=H60a AND RSI=RSI3 AND session_bucket=ny_close`
- Raw: n=117  W=107/L=10  WR=91.5%
- Refine: exclude T1=T1c drops 9/10 losers (90%)
- **Final: n=67  W=66/L=1  WR=98.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 40-50 lower neutral; session=ny_close  •  AVOID when 1h trend AGAINST trade

### W18.  `H20=H20a AND RSI=RSI3 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=117  W=107/L=10  WR=91.5%
- Refine: exclude T1=T1c drops 9/10 losers (90%)
- **Final: n=67  W=66/L=1  WR=98.5%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 40-50 lower neutral; session=ny_close  •  AVOID when 1h trend AGAINST trade

### W19.  `H20=H20a AND H60=H60a AND T4=T4c AND session_bucket=ny_close`
- Raw: n=111  W=101/L=10  WR=91.0%
- Refine: exclude T1=T1c drops 9/10 losers (90%)
- **Final: n=61  W=60/L=1  WR=98.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend AGAINST trade; session=ny_close  •  AVOID when 1h trend AGAINST trade

### W20.  `H20=H20a AND T4=T4c AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=111  W=101/L=10  WR=91.0%
- Refine: exclude T1=T1c drops 9/10 losers (90%)
- **Final: n=61  W=60/L=1  WR=98.4%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; session=ny_close  •  AVOID when 1h trend AGAINST trade

### W21.  `H60=H60a AND T1=T1a AND ZS=ZS1 AND session_bucket=ny_mid`
- Raw: n=109  W=99/L=10  WR=90.8%
- Refine: exclude RSI=RSI3 drops 10/10 losers (100%)
- **Final: n=68  W=68/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; zscore -3 to -2 deep oversold; session=ny_mid  •  AVOID when RSI 40-50 lower neutral

### W22.  `T1=T1a AND ZS=ZS1 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=109  W=99/L=10  WR=90.8%
- Refine: exclude RSI=RSI3 drops 10/10 losers (100%)
- **Final: n=68  W=68/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend WITH trade; zscore -3 to -2 deep oversold; session=ny_mid  •  AVOID when RSI 40-50 lower neutral

### W23.  `H60=H60a AND T4=T4a AND RSI=RSI2`
- Raw: n=104  W=95/L=9  WR=91.3%
- Refine: exclude session_bucket=london_open drops 9/9 losers (100%)
- **Final: n=68  W=68/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 30-40 weak  •  AVOID when session=london_open

### W24.  `T1=T1a AND T4=T4a AND RSI=RSI2`
- Raw: n=104  W=95/L=9  WR=91.3%
- Refine: exclude session_bucket=london_open drops 9/9 losers (100%)
- **Final: n=68  W=68/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 30-40 weak  •  AVOID when session=london_open

### W25.  `T4=T4a AND RSI=RSI2 AND direction_exec=short`
- Raw: n=104  W=95/L=9  WR=91.3%
- Refine: exclude session_bucket=london_open drops 9/9 losers (100%)
- **Final: n=68  W=68/L=0  WR=100.0%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 30-40 weak  •  AVOID when session=london_open

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND T1=T1c AND session_bucket=ny_mid`
- Raw: n=244  W=88/L=156  WR=36.1%
- Sharpen: sharpest is RSI=RSI2 (61/156 of losers there)
- **Sharp: n=69  W=8/L=61  WR=11.6%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; session=ny_mid  •  ONLY when RSI 30-40 weak

### L02.  `T1=T1c AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=244  W=88/L=156  WR=36.1%
- Sharpen: sharpest is RSI=RSI2 (61/156 of losers there)
- **Sharp: n=69  W=8/L=61  WR=11.6%**
- **Dir: LONG**  •  1h trend AGAINST trade; session=ny_mid  •  ONLY when RSI 30-40 weak

### L03.  `H60=H60e AND T1=T1c AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=244  W=88/L=156  WR=36.1%
- Sharpen: sharpest is RSI=RSI2 (61/156 of losers there)
- **Sharp: n=69  W=8/L=61  WR=11.6%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend AGAINST trade; session=ny_mid  •  ONLY when RSI 30-40 weak

### L04.  `H60=H60e AND T1=T1c AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=167  W=65/L=102  WR=38.9%
- Sharpen: sharpest is RSI=RSI2 (42/102 of losers there)
- **Sharp: n=50  W=8/L=42  WR=16.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade; session=ny_mid  •  ONLY when RSI 30-40 weak

### L05.  `T1=T1c AND T4=T4a AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=167  W=65/L=102  WR=38.9%
- Sharpen: sharpest is RSI=RSI2 (42/102 of losers there)
- **Sharp: n=50  W=8/L=42  WR=16.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend WITH trade; session=ny_mid  •  ONLY when RSI 30-40 weak

### L06.  `T1=T1a AND T4=T4c AND session_bucket=asia`
- Raw: n=148  W=57/L=91  WR=38.5%
- Sharpen: sharpest is H60=H60e (59/91 of losers there)
- **Sharp: n=86  W=27/L=59  WR=31.4%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; session=asia  •  ONLY when HTF60 strongly against

### L07.  `H60=H60e AND T4=T4a AND BBP=BBP3 AND RSI=RSI3`
- Raw: n=143  W=55/L=88  WR=38.5%
- Sharpen: sharpest is T1=T1c (59/88 of losers there)
- **Sharp: n=83  W=24/L=59  WR=28.9%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; middle of band; RSI 40-50 lower neutral  •  ONLY when 1h trend AGAINST trade

### L08.  `T4=T4a AND BBP=BBP3 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=143  W=55/L=88  WR=38.5%
- Sharpen: sharpest is T1=T1c (59/88 of losers there)
- **Sharp: n=83  W=24/L=59  WR=28.9%**
- **Dir: LONG**  •  4h trend WITH trade; middle of band; RSI 40-50 lower neutral  •  ONLY when 1h trend AGAINST trade

### L09.  `T1=T1a AND direction_exec=long AND session_bucket=asia`
- Raw: n=136  W=49/L=87  WR=36.0%
- Sharpen: sharpest is RSI=RSI3 (67/87 of losers there)
- **Sharp: n=90  W=23/L=67  WR=25.6%**
- **Dir: LONG**  •  1h trend WITH trade; session=asia  •  ONLY when RSI 40-50 lower neutral

### L10.  `H60=H60e AND T1=T1c AND RSI=RSI2`
- Raw: n=135  W=36/L=99  WR=26.7%
- Sharpen: sharpest is session_bucket=ny_mid (61/99 of losers there)
- **Sharp: n=69  W=8/L=61  WR=11.6%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 30-40 weak  •  ONLY when session=ny_mid

### L11.  `H60=H60e AND RSI=RSI2 AND direction_exec=long`
- Raw: n=135  W=36/L=99  WR=26.7%
- Sharpen: sharpest is session_bucket=ny_mid (61/99 of losers there)
- **Sharp: n=69  W=8/L=61  WR=11.6%**
- **Dir: LONG**  •  HTF60 strongly against; RSI 30-40 weak  •  ONLY when session=ny_mid

### L12.  `T1=T1c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=135  W=36/L=99  WR=26.7%
- Sharpen: sharpest is session_bucket=ny_mid (61/99 of losers there)
- **Sharp: n=69  W=8/L=61  WR=11.6%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 30-40 weak  •  ONLY when session=ny_mid

### L13.  `H60=H60e AND T1=T1c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=135  W=36/L=99  WR=26.7%
- Sharpen: sharpest is session_bucket=ny_mid (61/99 of losers there)
- **Sharp: n=69  W=8/L=61  WR=11.6%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 30-40 weak  •  ONLY when session=ny_mid

### L14.  `H20=H20a AND T4=T4a AND session_bucket=ny_open`
- Raw: n=132  W=48/L=84  WR=36.4%
- Sharpen: sharpest is T1=T1a (31/84 of losers there)
- **Sharp: n=34  W=3/L=31  WR=8.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=ny_open  •  ONLY when 1h trend WITH trade

### L15.  `H20=H20e AND H60=H60e AND BBP=BBP3 AND RSI=RSI3`
- Raw: n=128  W=51/L=77  WR=39.8%
- Sharpen: sharpest is T4=T4a (49/77 of losers there)
- **Sharp: n=68  W=19/L=49  WR=27.9%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; middle of band; RSI 40-50 lower neutral  •  ONLY when 4h trend WITH trade

### L16.  `H20=H20e AND BBP=BBP3 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=128  W=51/L=77  WR=39.8%
- Sharpen: sharpest is T4=T4a (49/77 of losers there)
- **Sharp: n=68  W=19/L=49  WR=27.9%**
- **Dir: LONG**  •  HTF20 strongly against; middle of band; RSI 40-50 lower neutral  •  ONLY when 4h trend WITH trade

### L17.  `H60=H60e AND T1=T1a AND session_bucket=asia`
- Raw: n=120  W=38/L=82  WR=31.7%
- Sharpen: sharpest is RSI=RSI3 (67/82 of losers there)
- **Sharp: n=90  W=23/L=67  WR=25.6%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; session=asia  •  ONLY when RSI 40-50 lower neutral

### L18.  `H60=H60e AND T1=T1a AND direction_exec=long AND session_bucket=asia`
- Raw: n=120  W=38/L=82  WR=31.7%
- Sharpen: sharpest is RSI=RSI3 (67/82 of losers there)
- **Sharp: n=90  W=23/L=67  WR=25.6%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend WITH trade; session=asia  •  ONLY when RSI 40-50 lower neutral

### L19.  `H20=H20e AND T1=T1c AND session_bucket=ny_mid`
- Raw: n=119  W=41/L=78  WR=34.5%
- Sharpen: sharpest is BBP=BBP2 (17/78 of losers there)
- **Sharp: n=18  W=1/L=17  WR=5.6%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; session=ny_mid  •  ONLY when lower third

### L20.  `H60=H60e AND RSI=RSI3 AND ZS=ZS4`
- Raw: n=116  W=41/L=75  WR=35.3%
- Sharpen: sharpest is T4=T4a (42/75 of losers there)
- **Sharp: n=48  W=6/L=42  WR=12.5%**
- **Dir: ?**  •  HTF60 strongly against; RSI 40-50 lower neutral; zscore +1 to +2 overbought  •  ONLY when 4h trend WITH trade

### L21.  `RSI=RSI3 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=116  W=41/L=75  WR=35.3%
- Sharpen: sharpest is T4=T4a (42/75 of losers there)
- **Sharp: n=48  W=6/L=42  WR=12.5%**
- **Dir: LONG**  •  RSI 40-50 lower neutral; zscore +1 to +2 overbought  •  ONLY when 4h trend WITH trade

### L22.  `H60=H60e AND BBP=BBP4 AND RSI=RSI3 AND ZS=ZS4`
- Raw: n=116  W=41/L=75  WR=35.3%
- Sharpen: sharpest is T4=T4a (42/75 of losers there)
- **Sharp: n=48  W=6/L=42  WR=12.5%**
- **Dir: ?**  •  HTF60 strongly against; upper third; RSI 40-50 lower neutral; zscore +1 to +2 overbought  •  ONLY when 4h trend WITH trade

### L23.  `H60=H60e AND RSI=RSI3 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=116  W=41/L=75  WR=35.3%
- Sharpen: sharpest is T4=T4a (42/75 of losers there)
- **Sharp: n=48  W=6/L=42  WR=12.5%**
- **Dir: LONG**  •  HTF60 strongly against; RSI 40-50 lower neutral; zscore +1 to +2 overbought  •  ONLY when 4h trend WITH trade

### L24.  `BBP=BBP4 AND RSI=RSI3 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=116  W=41/L=75  WR=35.3%
- Sharpen: sharpest is T4=T4a (42/75 of losers there)
- **Sharp: n=48  W=6/L=42  WR=12.5%**
- **Dir: LONG**  •  upper third; RSI 40-50 lower neutral; zscore +1 to +2 overbought  •  ONLY when 4h trend WITH trade

### L25.  `H60=H60e AND ZS=ZS1 AND session_bucket=ny_mid`
- Raw: n=115  W=42/L=73  WR=36.5%
- Sharpen: sharpest is RSI=RSI2 (45/73 of losers there)
- **Sharp: n=53  W=8/L=45  WR=15.1%**
- **Dir: ?**  •  HTF60 strongly against; zscore -3 to -2 deep oversold; session=ny_mid  •  ONLY when RSI 30-40 weak

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20b(14/9) | H20e(32/39) |
| H60 | H60a(55/44) | H60e(43/55) |
| T1 | T1a(52/46) | T1c(48/54) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(56/45) | long(44/55) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
