# AUD_CHF — R33 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_0**  (5m ATR <33% stop)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20d**  (EMA20 down 0.15-0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **1,282**  (W=831 / L=451)  -  WR: **64.8%**

## Session distribution

- asia: n=453  W=310/L=143  WR=68.4%
- ny_close: n=308  W=192/L=116  WR=62.3%
- london_open: n=132  W=91/L=41  WR=68.9%
- ny_mid: n=104  W=68/L=36  WR=65.4%
- ny_open: n=92  W=51/L=41  WR=55.4%
- london: n=90  W=52/L=38  WR=57.8%
- off_hours: n=52  W=35/L=17  WR=67.3%
- asia_late: n=51  W=32/L=19  WR=62.7%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T4=T4c AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=114  W=98/L=16  WR=86.0%
- Refine: exclude H20=H20b drops 5/16 losers (31%)
- **Final: n=99  W=88/L=11  WR=88.9%**
- **Dir: ?**  •  4h trend AGAINST trade; upper third; zscore +1 to +2 overbought  •  AVOID when HTF20 slightly aligned

### W02.  `H20=H20a AND T4=T4c AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=101  W=86/L=15  WR=85.1%
- Refine: exclude H60=H60a drops 15/15 losers (100%)
- **Final: n=20  W=20/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 30-40 weak; session=asia  •  AVOID when HTF60 aligned WITH trade

### W03.  `T4=T4c AND BBP=BBP4 AND direction_exec=long`
- Raw: n=98  W=84/L=14  WR=85.7%
- Refine: exclude H20=H20b drops 6/14 losers (43%)
- **Final: n=80  W=72/L=8  WR=90.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; upper third  •  AVOID when HTF20 slightly aligned

### W04.  `H60=H60a AND T4=T4c AND BBP=BBP4`
- Raw: n=90  W=78/L=12  WR=86.7%
- Refine: exclude H20=H20b drops 6/12 losers (50%)
- **Final: n=72  W=66/L=6  WR=91.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; upper third  •  AVOID when HTF20 slightly aligned

### W05.  `H60=H60a AND T4=T4c AND BBP=BBP4 AND direction_exec=long`
- Raw: n=90  W=78/L=12  WR=86.7%
- Refine: exclude H20=H20b drops 6/12 losers (50%)
- **Final: n=72  W=66/L=6  WR=91.7%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; upper third  •  AVOID when HTF20 slightly aligned

### W06.  `T1=T1c AND BBP=BBP0 AND RSI=RSI2`
- Raw: n=87  W=74/L=13  WR=85.1%
- Refine: exclude ZS=ZS1 drops 9/13 losers (69%)
- **Final: n=49  W=45/L=4  WR=91.8%**
- **Dir: ?**  •  1h trend AGAINST trade; deep below lower band; RSI 30-40 weak  •  AVOID when zscore -3 to -2 deep oversold

### W07.  `BBP=BBP0 AND RSI=RSI2 AND direction_exec=long`
- Raw: n=87  W=74/L=13  WR=85.1%
- Refine: exclude ZS=ZS1 drops 9/13 losers (69%)
- **Final: n=49  W=45/L=4  WR=91.8%**
- **Dir: LONG**  •  deep below lower band; RSI 30-40 weak  •  AVOID when zscore -3 to -2 deep oversold

### W08.  `T1=T1c AND BBP=BBP0 AND RSI=RSI2 AND direction_exec=long`
- Raw: n=87  W=74/L=13  WR=85.1%
- Refine: exclude ZS=ZS1 drops 9/13 losers (69%)
- **Final: n=49  W=45/L=4  WR=91.8%**
- **Dir: LONG**  •  1h trend AGAINST trade; deep below lower band; RSI 30-40 weak  •  AVOID when zscore -3 to -2 deep oversold

### W09.  `T4=T4c AND ZS=ZS4 AND direction_exec=long`
- Raw: n=84  W=73/L=11  WR=86.9%
- Refine: exclude H20=H20b drops 5/11 losers (45%)
- **Final: n=69  W=63/L=6  WR=91.3%**
- **Dir: LONG**  •  4h trend AGAINST trade; zscore +1 to +2 overbought  •  AVOID when HTF20 slightly aligned

### W10.  `T4=T4c AND BBP=BBP4 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=84  W=73/L=11  WR=86.9%
- Refine: exclude H20=H20b drops 5/11 losers (45%)
- **Final: n=69  W=63/L=6  WR=91.3%**
- **Dir: LONG**  •  4h trend AGAINST trade; upper third; zscore +1 to +2 overbought  •  AVOID when HTF20 slightly aligned

### W11.  `H60=H60a AND T1=T1c AND T4=T4c AND BBP=BBP4`
- Raw: n=84  W=72/L=12  WR=85.7%
- Refine: exclude H20=H20b drops 6/12 losers (50%)
- **Final: n=66  W=60/L=6  WR=90.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; upper third  •  AVOID when HTF20 slightly aligned

### W12.  `H60=H60a AND T1=T1c AND session_bucket=london_open`
- Raw: n=80  W=71/L=9  WR=88.8%
- Refine: exclude ZS=ZS3 drops 6/9 losers (67%)
- **Final: n=64  W=61/L=3  WR=95.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=london_open  •  AVOID when zscore -1 to +1 neutral

### W13.  `H60=H60a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=80  W=71/L=9  WR=88.8%
- Refine: exclude ZS=ZS3 drops 6/9 losers (67%)
- **Final: n=64  W=61/L=3  WR=95.3%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; session=london_open  •  AVOID when zscore -1 to +1 neutral

### W14.  `T1=T1c AND direction_exec=long AND session_bucket=london_open`
- Raw: n=80  W=71/L=9  WR=88.8%
- Refine: exclude ZS=ZS3 drops 6/9 losers (67%)
- **Final: n=64  W=61/L=3  WR=95.3%**
- **Dir: LONG**  •  1h trend AGAINST trade; session=london_open  •  AVOID when zscore -1 to +1 neutral

### W15.  `H60=H60a AND T1=T1c AND direction_exec=long AND session_bucket=london_open`
- Raw: n=80  W=71/L=9  WR=88.8%
- Refine: exclude ZS=ZS3 drops 6/9 losers (67%)
- **Final: n=64  W=61/L=3  WR=95.3%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=london_open  •  AVOID when zscore -1 to +1 neutral

### W16.  `T1=T1c AND T4=T4c AND ZS=ZS4`
- Raw: n=78  W=67/L=11  WR=85.9%
- Refine: exclude H20=H20b drops 5/11 losers (45%)
- **Final: n=63  W=57/L=6  WR=90.5%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  AVOID when HTF20 slightly aligned

### W17.  `T1=T1c AND T4=T4c AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=78  W=67/L=11  WR=85.9%
- Refine: exclude H20=H20b drops 5/11 losers (45%)
- **Final: n=63  W=57/L=6  WR=90.5%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; upper third; zscore +1 to +2 overbought  •  AVOID when HTF20 slightly aligned

### W18.  `T1=T1c AND T4=T4c AND ZS=ZS4 AND direction_exec=long`
- Raw: n=78  W=67/L=11  WR=85.9%
- Refine: exclude H20=H20b drops 5/11 losers (45%)
- **Final: n=63  W=57/L=6  WR=90.5%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  AVOID when HTF20 slightly aligned

### W19.  `H60=H60a AND T4=T4c AND ZS=ZS4`
- Raw: n=76  W=67/L=9  WR=88.2%
- Refine: exclude H20=H20b drops 5/9 losers (56%)
- **Final: n=61  W=57/L=4  WR=93.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  AVOID when HTF20 slightly aligned

### W20.  `H60=H60a AND T4=T4c AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=76  W=67/L=9  WR=88.2%
- Refine: exclude H20=H20b drops 5/9 losers (56%)
- **Final: n=61  W=57/L=4  WR=93.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; upper third; zscore +1 to +2 overbought  •  AVOID when HTF20 slightly aligned

### W21.  `H60=H60a AND T4=T4c AND ZS=ZS4 AND direction_exec=long`
- Raw: n=76  W=67/L=9  WR=88.2%
- Refine: exclude H20=H20b drops 5/9 losers (56%)
- **Final: n=61  W=57/L=4  WR=93.4%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  AVOID when HTF20 slightly aligned

### W22.  `T1=T1c AND T4=T4c AND BBP=BBP0`
- Raw: n=76  W=65/L=11  WR=85.5%
- Refine: exclude session_bucket=london drops 4/11 losers (36%)
- **Final: n=70  W=63/L=7  WR=90.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; deep below lower band  •  AVOID when session=london

### W23.  `T1=T1c AND T4=T4c AND BBP=BBP0 AND direction_exec=long`
- Raw: n=76  W=65/L=11  WR=85.5%
- Refine: exclude session_bucket=london drops 4/11 losers (36%)
- **Final: n=70  W=63/L=7  WR=90.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; deep below lower band  •  AVOID when session=london

### W24.  `H20=H20a AND T4=T4c AND BBP=BBP4`
- Raw: n=72  W=65/L=7  WR=90.3%
- Refine: exclude session_bucket=ny_close drops 4/7 losers (57%)
- **Final: n=50  W=47/L=3  WR=94.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; upper third  •  AVOID when session=ny_close

### W25.  `H20=H20a AND T4=T4c AND BBP=BBP4 AND direction_exec=long`
- Raw: n=72  W=65/L=7  WR=90.3%
- Refine: exclude session_bucket=ny_close drops 4/7 losers (57%)
- **Final: n=50  W=47/L=3  WR=94.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; upper third  •  AVOID when session=ny_close

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1a AND T4=T4a AND session_bucket=ny_close`
- Raw: n=79  W=29/L=50  WR=36.7%
- Sharpen: sharpest is RSI=RSI2 (45/50 of losers there)
- **Sharp: n=65  W=20/L=45  WR=30.8%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; session=ny_close  •  ONLY when RSI 30-40 weak

### L02.  `T4=T4a AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=79  W=29/L=50  WR=36.7%
- Sharpen: sharpest is RSI=RSI2 (45/50 of losers there)
- **Sharp: n=65  W=20/L=45  WR=30.8%**
- **Dir: SHORT**  •  4h trend WITH trade; session=ny_close  •  ONLY when RSI 30-40 weak

### L03.  `T1=T1a AND T4=T4a AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=79  W=29/L=50  WR=36.7%
- Sharpen: sharpest is RSI=RSI2 (45/50 of losers there)
- **Sharp: n=65  W=20/L=45  WR=30.8%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend WITH trade; session=ny_close  •  ONLY when RSI 30-40 weak

### L04.  `T4=T4a AND BBP=BBP4 AND direction_exec=short`
- Raw: n=73  W=29/L=44  WR=39.7%
- Sharpen: sharpest is H20=H20e (37/44 of losers there)
- **Sharp: n=51  W=14/L=37  WR=27.5%**
- **Dir: SHORT**  •  4h trend WITH trade; upper third  •  ONLY when HTF20 strongly against

### L05.  `H60=H60e AND T4=T4a AND session_bucket=ny_close`
- Raw: n=69  W=24/L=45  WR=34.8%
- Sharpen: sharpest is RSI=RSI2 (40/45 of losers there)
- **Sharp: n=55  W=15/L=40  WR=27.3%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; session=ny_close  •  ONLY when RSI 30-40 weak

### L06.  `H60=H60e AND T1=T1a AND T4=T4a AND session_bucket=ny_close`
- Raw: n=69  W=24/L=45  WR=34.8%
- Sharpen: sharpest is RSI=RSI2 (40/45 of losers there)
- **Sharp: n=55  W=15/L=40  WR=27.3%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend WITH trade; session=ny_close  •  ONLY when RSI 30-40 weak

### L07.  `H60=H60e AND T4=T4a AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=69  W=24/L=45  WR=34.8%
- Sharpen: sharpest is RSI=RSI2 (40/45 of losers there)
- **Sharp: n=55  W=15/L=40  WR=27.3%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend WITH trade; session=ny_close  •  ONLY when RSI 30-40 weak

### L08.  `T1=T1a AND T4=T4a AND RSI=RSI2 AND session_bucket=ny_close`
- Raw: n=65  W=20/L=45  WR=30.8%
- Sharpen: sharpest is ZS=ZS3 (16/45 of losers there)
- **Sharp: n=19  W=3/L=16  WR=15.8%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 30-40 weak; session=ny_close  •  ONLY when zscore -1 to +1 neutral

### L09.  `T4=T4a AND RSI=RSI2 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=65  W=20/L=45  WR=30.8%
- Sharpen: sharpest is ZS=ZS3 (16/45 of losers there)
- **Sharp: n=19  W=3/L=16  WR=15.8%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 30-40 weak; session=ny_close  •  ONLY when zscore -1 to +1 neutral

### L10.  `H60=H60e AND T4=T4a AND BBP=BBP4`
- Raw: n=65  W=25/L=40  WR=38.5%
- Sharpen: sharpest is H20=H20e (33/40 of losers there)
- **Sharp: n=43  W=10/L=33  WR=23.3%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; upper third  •  ONLY when HTF20 strongly against

### L11.  `H60=H60e AND T4=T4a AND BBP=BBP4 AND direction_exec=short`
- Raw: n=65  W=25/L=40  WR=38.5%
- Sharpen: sharpest is H20=H20e (33/40 of losers there)
- **Sharp: n=43  W=10/L=33  WR=23.3%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend WITH trade; upper third  •  ONLY when HTF20 strongly against

### L12.  `H60=H60e AND T1=T1a AND T4=T4a AND BBP=BBP4`
- Raw: n=63  W=25/L=38  WR=39.7%
- Sharpen: sharpest is H20=H20e (31/38 of losers there)
- **Sharp: n=41  W=10/L=31  WR=24.4%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend WITH trade; upper third  •  ONLY when HTF20 strongly against

### L13.  `H20=H20e AND T4=T4a AND ZS=ZS3`
- Raw: n=61  W=23/L=38  WR=37.7%
- Sharpen: sharpest is RSI=RSI3 (16/38 of losers there)
- **Sharp: n=20  W=4/L=16  WR=20.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; zscore -1 to +1 neutral  •  ONLY when RSI 40-50 lower neutral

### L14.  `H20=H20e AND T1=T1a AND T4=T4a AND ZS=ZS3`
- Raw: n=61  W=23/L=38  WR=37.7%
- Sharpen: sharpest is RSI=RSI3 (16/38 of losers there)
- **Sharp: n=20  W=4/L=16  WR=20.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend WITH trade; zscore -1 to +1 neutral  •  ONLY when RSI 40-50 lower neutral

### L15.  `H20=H20e AND T4=T4a AND ZS=ZS3 AND direction_exec=short`
- Raw: n=61  W=23/L=38  WR=37.7%
- Sharpen: sharpest is RSI=RSI3 (16/38 of losers there)
- **Sharp: n=20  W=4/L=16  WR=20.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend WITH trade; zscore -1 to +1 neutral  •  ONLY when RSI 40-50 lower neutral

### L16.  `H20=H20e AND H60=H60e AND T4=T4a AND ZS=ZS3`
- Raw: n=59  W=22/L=37  WR=37.3%
- Sharpen: sharpest is RSI=RSI3 (16/37 of losers there)
- **Sharp: n=20  W=4/L=16  WR=20.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend WITH trade; zscore -1 to +1 neutral  •  ONLY when RSI 40-50 lower neutral

### L17.  `H60=H60e AND T4=T4a AND RSI=RSI2 AND session_bucket=ny_close`
- Raw: n=55  W=15/L=40  WR=27.3%
- Sharpen: sharpest is H20=H20e (22/40 of losers there)
- **Sharp: n=26  W=4/L=22  WR=15.4%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; RSI 30-40 weak; session=ny_close  •  ONLY when HTF20 strongly against

### L18.  `H60=H60e AND T4=T4a AND ZS=ZS4`
- Raw: n=55  W=22/L=33  WR=40.0%
- Sharpen: sharpest is H20=H20e (27/33 of losers there)
- **Sharp: n=34  W=7/L=27  WR=20.6%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; zscore +1 to +2 overbought  •  ONLY when HTF20 strongly against

### L19.  `H60=H60e AND T4=T4a AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=55  W=22/L=33  WR=40.0%
- Sharpen: sharpest is H20=H20e (27/33 of losers there)
- **Sharp: n=34  W=7/L=27  WR=20.6%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; upper third; zscore +1 to +2 overbought  •  ONLY when HTF20 strongly against

### L20.  `H60=H60e AND T4=T4a AND ZS=ZS4 AND direction_exec=short`
- Raw: n=55  W=22/L=33  WR=40.0%
- Sharpen: sharpest is H20=H20e (27/33 of losers there)
- **Sharp: n=34  W=7/L=27  WR=20.6%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend WITH trade; zscore +1 to +2 overbought  •  ONLY when HTF20 strongly against

### L21.  `H60=H60e AND T1=T1a AND session_bucket=london_open`
- Raw: n=52  W=20/L=32  WR=38.5%
- Sharpen: sharpest is ZS=ZS1 (20/32 of losers there)
- **Sharp: n=24  W=4/L=20  WR=16.7%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; session=london_open  •  ONLY when zscore -3 to -2 deep oversold

### L22.  `H60=H60e AND direction_exec=short AND session_bucket=london_open`
- Raw: n=52  W=20/L=32  WR=38.5%
- Sharpen: sharpest is ZS=ZS1 (20/32 of losers there)
- **Sharp: n=24  W=4/L=20  WR=16.7%**
- **Dir: SHORT**  •  HTF60 strongly against; session=london_open  •  ONLY when zscore -3 to -2 deep oversold

### L23.  `T1=T1a AND direction_exec=short AND session_bucket=london_open`
- Raw: n=52  W=20/L=32  WR=38.5%
- Sharpen: sharpest is ZS=ZS1 (20/32 of losers there)
- **Sharp: n=24  W=4/L=20  WR=16.7%**
- **Dir: SHORT**  •  1h trend WITH trade; session=london_open  •  ONLY when zscore -3 to -2 deep oversold

### L24.  `H60=H60e AND T1=T1a AND direction_exec=short AND session_bucket=london_open`
- Raw: n=52  W=20/L=32  WR=38.5%
- Sharpen: sharpest is ZS=ZS1 (20/32 of losers there)
- **Sharp: n=24  W=4/L=20  WR=16.7%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend WITH trade; session=london_open  •  ONLY when zscore -3 to -2 deep oversold

### L25.  `H20=H20e AND T4=T4a AND BBP=BBP4`
- Raw: n=51  W=14/L=37  WR=27.5%
- Sharpen: sharpest is H60=H60e (33/37 of losers there)
- **Sharp: n=43  W=10/L=33  WR=23.3%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; upper third  •  ONLY when HTF60 strongly against

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(43/28) | H20e(27/37) |
| H60 | H60a(55/43) | H60e(40/55) |
| T1 | T1c(59/43) | T1a(41/57) |
| T4 | T4c(60/36) | T4a(40/64) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | ZS3(18/26) |
| strategy_id | — | — |
| direction_exec | long(59/43) | short(41/57) |
| session_bucket | asia(37/32) | — |

*Read: `bucket(winner%/loser%)`.*
