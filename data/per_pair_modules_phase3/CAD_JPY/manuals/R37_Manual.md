# CAD_JPY — R37 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR1**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **3,354**  (W=2,173 / L=1,181)  -  WR: **64.8%**

## Session distribution

- asia: n=1025  W=661/L=364  WR=64.5%
- ny_close: n=472  W=304/L=168  WR=64.4%
- ny_mid: n=395  W=255/L=140  WR=64.6%
- london_open: n=385  W=259/L=126  WR=67.3%
- ny_open: n=357  W=232/L=125  WR=65.0%
- london: n=322  W=200/L=122  WR=62.1%
- asia_late: n=288  W=188/L=100  WR=65.3%
- off_hours: n=110  W=74/L=36  WR=67.3%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `BBP=BBP0 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=175  W=149/L=26  WR=85.1%
- Refine: exclude T4=T4c drops 15/26 losers (58%)
- **Final: n=121  W=110/L=11  WR=90.9%**
- **Dir: LONG**  •  deep below lower band; zscore -3 to -2 deep oversold  •  AVOID when 4h trend AGAINST trade

### W02.  `H60=H60a AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=174  W=149/L=25  WR=85.6%
- Refine: exclude T4=T4c drops 15/25 losers (60%)
- **Final: n=120  W=110/L=10  WR=91.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; deep below lower band; zscore -3 to -2 deep oversold  •  AVOID when 4h trend AGAINST trade

### W03.  `H60=H60a AND BBP=BBP0 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=174  W=149/L=25  WR=85.6%
- Refine: exclude T4=T4c drops 15/25 losers (60%)
- **Final: n=120  W=110/L=10  WR=91.7%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; deep below lower band; zscore -3 to -2 deep oversold  •  AVOID when 4h trend AGAINST trade

### W04.  `T4=T4a AND BBP=BBP0 AND RSI=RSI3`
- Raw: n=170  W=153/L=17  WR=90.0%
- Refine: exclude session_bucket=london_open drops 5/17 losers (29%)
- **Final: n=159  W=147/L=12  WR=92.5%**
- **Dir: ?**  •  4h trend WITH trade; deep below lower band; RSI 40-50 lower neutral  •  AVOID when session=london_open

### W05.  `T4=T4a AND BBP=BBP0 AND direction_exec=long`
- Raw: n=142  W=128/L=14  WR=90.1%
- Refine: exclude T1=T1a drops 13/14 losers (93%)
- **Final: n=49  W=48/L=1  WR=98.0%**
- **Dir: LONG**  •  4h trend WITH trade; deep below lower band  •  AVOID when 1h trend WITH trade

### W06.  `H60=H60a AND T4=T4a AND BBP=BBP0`
- Raw: n=141  W=128/L=13  WR=90.8%
- Refine: exclude session_bucket=london drops 6/13 losers (46%)
- **Final: n=119  W=112/L=7  WR=94.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; deep below lower band  •  AVOID when session=london

### W07.  `H60=H60a AND T4=T4a AND BBP=BBP0 AND direction_exec=long`
- Raw: n=141  W=128/L=13  WR=90.8%
- Refine: exclude session_bucket=london drops 6/13 losers (46%)
- **Final: n=119  W=112/L=7  WR=94.1%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend WITH trade; deep below lower band  •  AVOID when session=london

### W08.  `T1=T1a AND T4=T4a AND BBP=BBP0`
- Raw: n=136  W=116/L=20  WR=85.3%
- Refine: exclude H20=H20a drops 16/20 losers (80%)
- **Final: n=56  W=52/L=4  WR=92.9%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; deep below lower band  •  AVOID when HTF20 aligned WITH trade

### W09.  `H60=H60a AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=127  W=111/L=16  WR=87.4%
- Refine: exclude T1=T1c drops 13/16 losers (81%)
- **Final: n=87  W=84/L=3  WR=96.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; session=ny_mid  •  AVOID when 1h trend AGAINST trade

### W10.  `RSI=RSI4 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=127  W=111/L=16  WR=87.4%
- Refine: exclude T1=T1c drops 13/16 losers (81%)
- **Final: n=87  W=84/L=3  WR=96.6%**
- **Dir: LONG**  •  RSI 50-60 upper neutral; session=ny_mid  •  AVOID when 1h trend AGAINST trade

### W11.  `H60=H60a AND RSI=RSI4 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=127  W=111/L=16  WR=87.4%
- Refine: exclude T1=T1c drops 13/16 losers (81%)
- **Final: n=87  W=84/L=3  WR=96.6%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; session=ny_mid  •  AVOID when 1h trend AGAINST trade

### W12.  `T4=T4a AND BBP=BBP0 AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=122  W=108/L=14  WR=88.5%
- Refine: exclude session_bucket=london_open drops 5/14 losers (36%)
- **Final: n=111  W=102/L=9  WR=91.9%**
- **Dir: ?**  •  4h trend WITH trade; deep below lower band; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when session=london_open

### W13.  `T4=T4a AND BBP=BBP0 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=121  W=110/L=11  WR=90.9%
- Refine: exclude T1=T1a drops 10/11 losers (91%)
- **Final: n=39  W=38/L=1  WR=97.4%**
- **Dir: LONG**  •  4h trend WITH trade; deep below lower band; zscore -3 to -2 deep oversold  •  AVOID when 1h trend WITH trade

### W14.  `H60=H60a AND T4=T4a AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=120  W=110/L=10  WR=91.7%
- Refine: exclude T1=T1a drops 9/10 losers (90%)
- **Final: n=39  W=38/L=1  WR=97.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; deep below lower band; zscore -3 to -2 deep oversold  •  AVOID when 1h trend WITH trade

### W15.  `H60=H60e AND T4=T4a AND session_bucket=ny_close`
- Raw: n=119  W=103/L=16  WR=86.6%
- Refine: exclude H20=H20a drops 3/16 losers (19%)
- **Final: n=116  W=103/L=13  WR=88.8%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; session=ny_close  •  AVOID when HTF20 aligned WITH trade

### W16.  `T4=T4a AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=119  W=103/L=16  WR=86.6%
- Refine: exclude H20=H20a drops 3/16 losers (19%)
- **Final: n=116  W=103/L=13  WR=88.8%**
- **Dir: SHORT**  •  4h trend WITH trade; session=ny_close  •  AVOID when HTF20 aligned WITH trade

### W17.  `H60=H60e AND T4=T4a AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=119  W=103/L=16  WR=86.6%
- Refine: exclude H20=H20a drops 3/16 losers (19%)
- **Final: n=116  W=103/L=13  WR=88.8%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend WITH trade; session=ny_close  •  AVOID when HTF20 aligned WITH trade

### W18.  `T1=T1a AND BBP=BBP0 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=118  W=102/L=16  WR=86.4%
- Refine: exclude RSI=RSI3 drops 11/16 losers (69%)
- **Final: n=63  W=58/L=5  WR=92.1%**
- **Dir: LONG**  •  1h trend WITH trade; deep below lower band; zscore -3 to -2 deep oversold  •  AVOID when RSI 40-50 lower neutral

### W19.  `H60=H60a AND T1=T1a AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=117  W=102/L=15  WR=87.2%
- Refine: exclude H20=H20d drops 7/15 losers (47%)
- **Final: n=90  W=82/L=8  WR=91.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; deep below lower band; zscore -3 to -2 deep oversold  •  AVOID when HTF20 mildly against

### W20.  `T1=T1a AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=111  W=98/L=13  WR=88.3%
- Refine: exclude H60=H60e drops 10/13 losers (77%)
- **Final: n=87  W=84/L=3  WR=96.6%**
- **Dir: ?**  •  1h trend WITH trade; RSI 50-60 upper neutral; session=ny_mid  •  AVOID when HTF60 strongly against

### W21.  `T4=T4a AND BBP=BBP0 AND session_bucket=asia`
- Raw: n=111  W=96/L=15  WR=86.5%
- Refine: exclude H20=H20a drops 10/15 losers (67%)
- **Final: n=67  W=62/L=5  WR=92.5%**
- **Dir: ?**  •  4h trend WITH trade; deep below lower band; session=asia  •  AVOID when HTF20 aligned WITH trade

### W22.  `H20=H20a AND H60=H60a AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=100  W=90/L=10  WR=90.0%
- Refine: exclude session_bucket=ny_close drops 2/10 losers (20%)
- **Final: n=95  W=87/L=8  WR=91.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; deep below lower band; zscore -3 to -2 deep oversold  •  AVOID when session=ny_close

### W23.  `H20=H20a AND BBP=BBP0 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=100  W=90/L=10  WR=90.0%
- Refine: exclude session_bucket=ny_close drops 2/10 losers (20%)
- **Final: n=95  W=87/L=8  WR=91.6%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; deep below lower band; zscore -3 to -2 deep oversold  •  AVOID when session=ny_close

### W24.  `H20=H20e AND H60=H60e AND T4=T4a AND session_bucket=ny_close`
- Raw: n=100  W=87/L=13  WR=87.0%
- Refine: exclude ZS=ZS3 drops 3/13 losers (23%)
- **Final: n=91  W=81/L=10  WR=89.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend WITH trade; session=ny_close  •  AVOID when zscore -1 to +1 neutral

### W25.  `H20=H20e AND T4=T4a AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=100  W=87/L=13  WR=87.0%
- Refine: exclude ZS=ZS3 drops 3/13 losers (23%)
- **Final: n=91  W=81/L=10  WR=89.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend WITH trade; session=ny_close  •  AVOID when zscore -1 to +1 neutral

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20a AND T1=T1c AND RSI=RSI4 AND direction_exec=short`
- Raw: n=134  W=53/L=81  WR=39.6%
- Sharpen: sharpest is session_bucket=london (16/81 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when session=london

### L02.  `T4=T4c AND BBP=BBP0 AND RSI=RSI3`
- Raw: n=103  W=34/L=69  WR=33.0%
- Sharpen: sharpest is T1=T1a (34/69 of losers there)
- **Sharp: n=42  W=8/L=34  WR=19.0%**
- **Dir: ?**  •  4h trend AGAINST trade; deep below lower band; RSI 40-50 lower neutral  •  ONLY when 1h trend WITH trade

### L03.  `T4=T4c AND BBP=BBP0 AND direction_exec=short`
- Raw: n=98  W=33/L=65  WR=33.7%
- Sharpen: sharpest is T1=T1a (29/65 of losers there)
- **Sharp: n=31  W=2/L=29  WR=6.5%**
- **Dir: SHORT**  •  4h trend AGAINST trade; deep below lower band  •  ONLY when 1h trend WITH trade

### L04.  `T4=T4c AND RSI=RSI3 AND session_bucket=ny_close`
- Raw: n=95  W=37/L=58  WR=38.9%
- Sharpen: sharpest is H60=H60a (35/58 of losers there)
- **Sharp: n=44  W=9/L=35  WR=20.5%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; session=ny_close  •  ONLY when HTF60 aligned WITH trade

### L05.  `H60=H60e AND T4=T4c AND BBP=BBP0`
- Raw: n=92  W=27/L=65  WR=29.3%
- Sharpen: sharpest is T1=T1a (29/65 of losers there)
- **Sharp: n=31  W=2/L=29  WR=6.5%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; deep below lower band  •  ONLY when 1h trend WITH trade

### L06.  `H60=H60e AND T4=T4c AND BBP=BBP0 AND direction_exec=short`
- Raw: n=92  W=27/L=65  WR=29.3%
- Sharpen: sharpest is T1=T1a (29/65 of losers there)
- **Sharp: n=31  W=2/L=29  WR=6.5%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend AGAINST trade; deep below lower band  •  ONLY when 1h trend WITH trade

### L07.  `H60=H60a AND T4=T4c AND session_bucket=ny_close`
- Raw: n=88  W=30/L=58  WR=34.1%
- Sharpen: sharpest is T1=T1c (38/58 of losers there)
- **Sharp: n=47  W=9/L=38  WR=19.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=ny_close  •  ONLY when 1h trend AGAINST trade

### L08.  `T4=T4c AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=88  W=30/L=58  WR=34.1%
- Sharpen: sharpest is T1=T1c (38/58 of losers there)
- **Sharp: n=47  W=9/L=38  WR=19.1%**
- **Dir: LONG**  •  4h trend AGAINST trade; session=ny_close  •  ONLY when 1h trend AGAINST trade

### L09.  `H60=H60a AND T4=T4c AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=88  W=30/L=58  WR=34.1%
- Sharpen: sharpest is T1=T1c (38/58 of losers there)
- **Sharp: n=47  W=9/L=38  WR=19.1%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=ny_close  •  ONLY when 1h trend AGAINST trade

### L10.  `H60=H60e AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=88  W=31/L=57  WR=35.2%
- Sharpen: sharpest is T1=T1c (47/57 of losers there)
- **Sharp: n=64  W=17/L=47  WR=26.6%**
- **Dir: ?**  •  HTF60 strongly against; RSI 50-60 upper neutral; session=ny_mid  •  ONLY when 1h trend AGAINST trade

### L11.  `RSI=RSI4 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=88  W=31/L=57  WR=35.2%
- Sharpen: sharpest is T1=T1c (47/57 of losers there)
- **Sharp: n=64  W=17/L=47  WR=26.6%**
- **Dir: SHORT**  •  RSI 50-60 upper neutral; session=ny_mid  •  ONLY when 1h trend AGAINST trade

### L12.  `H60=H60e AND RSI=RSI4 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=88  W=31/L=57  WR=35.2%
- Sharpen: sharpest is T1=T1c (47/57 of losers there)
- **Sharp: n=64  W=17/L=47  WR=26.6%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 50-60 upper neutral; session=ny_mid  •  ONLY when 1h trend AGAINST trade

### L13.  `H20=H20a AND RSI=RSI3 AND session_bucket=ny_close`
- Raw: n=83  W=30/L=53  WR=36.1%
- Sharpen: sharpest is T1=T1c (34/53 of losers there)
- **Sharp: n=44  W=10/L=34  WR=22.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 40-50 lower neutral; session=ny_close  •  ONLY when 1h trend AGAINST trade

### L14.  `H20=H20a AND H60=H60a AND T4=T4c AND session_bucket=ny_close`
- Raw: n=78  W=26/L=52  WR=33.3%
- Sharpen: sharpest is T1=T1c (38/52 of losers there)
- **Sharp: n=47  W=9/L=38  WR=19.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend AGAINST trade; session=ny_close  •  ONLY when 1h trend AGAINST trade

### L15.  `H20=H20a AND T4=T4c AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=78  W=26/L=52  WR=33.3%
- Sharpen: sharpest is T1=T1c (38/52 of losers there)
- **Sharp: n=47  W=9/L=38  WR=19.1%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; session=ny_close  •  ONLY when 1h trend AGAINST trade

### L16.  `T4=T4c AND BBP=BBP0 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=76  W=24/L=52  WR=31.6%
- Sharpen: sharpest is T1=T1a (22/52 of losers there)
- **Sharp: n=24  W=2/L=22  WR=8.3%**
- **Dir: SHORT**  •  4h trend AGAINST trade; deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when 1h trend WITH trade

### L17.  `H20=H20d AND H60=H60a AND T4=T4c`
- Raw: n=74  W=29/L=45  WR=39.2%
- Sharpen: sharpest is RSI=RSI4 (28/45 of losers there)
- **Sharp: n=36  W=8/L=28  WR=22.2%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 aligned WITH trade; 4h trend AGAINST trade  •  ONLY when RSI 50-60 upper neutral

### L18.  `H20=H20d AND T4=T4c AND direction_exec=long`
- Raw: n=74  W=29/L=45  WR=39.2%
- Sharpen: sharpest is RSI=RSI4 (28/45 of losers there)
- **Sharp: n=36  W=8/L=28  WR=22.2%**
- **Dir: LONG**  •  HTF20 mildly against; 4h trend AGAINST trade  •  ONLY when RSI 50-60 upper neutral

### L19.  `H20=H20d AND H60=H60a AND T4=T4c AND direction_exec=long`
- Raw: n=74  W=29/L=45  WR=39.2%
- Sharpen: sharpest is RSI=RSI4 (28/45 of losers there)
- **Sharp: n=36  W=8/L=28  WR=22.2%**
- **Dir: LONG**  •  HTF20 mildly against; HTF60 aligned WITH trade; 4h trend AGAINST trade  •  ONLY when RSI 50-60 upper neutral

### L20.  `H60=H60e AND T1=T1c AND session_bucket=ny_mid`
- Raw: n=73  W=19/L=54  WR=26.0%
- Sharpen: sharpest is BBP=BBP4 (21/54 of losers there)
- **Sharp: n=22  W=1/L=21  WR=4.5%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; session=ny_mid  •  ONLY when upper third

### L21.  `T1=T1c AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=73  W=19/L=54  WR=26.0%
- Sharpen: sharpest is BBP=BBP4 (21/54 of losers there)
- **Sharp: n=22  W=1/L=21  WR=4.5%**
- **Dir: SHORT**  •  1h trend AGAINST trade; session=ny_mid  •  ONLY when upper third

### L22.  `H60=H60e AND T1=T1c AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=73  W=19/L=54  WR=26.0%
- Sharpen: sharpest is BBP=BBP4 (21/54 of losers there)
- **Sharp: n=22  W=1/L=21  WR=4.5%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; session=ny_mid  •  ONLY when upper third

### L23.  `T4=T4c AND BBP=BBP0 AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=73  W=28/L=45  WR=38.4%
- Sharpen: sharpest is H60=H60e (30/45 of losers there)
- **Sharp: n=39  W=9/L=30  WR=23.1%**
- **Dir: ?**  •  4h trend AGAINST trade; deep below lower band; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when HTF60 strongly against

### L24.  `H60=H60e AND T4=T4c AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=70  W=18/L=52  WR=25.7%
- Sharpen: sharpest is T1=T1a (22/52 of losers there)
- **Sharp: n=24  W=2/L=22  WR=8.3%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when 1h trend WITH trade

### L25.  `H20=H20d AND T1=T1a AND T4=T4c`
- Raw: n=70  W=27/L=43  WR=38.6%
- Sharpen: sharpest is RSI=RSI4 (28/43 of losers there)
- **Sharp: n=36  W=8/L=28  WR=22.2%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend WITH trade; 4h trend AGAINST trade  •  ONLY when RSI 50-60 upper neutral

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | H60a(53/47) | H60e(46/52) |
| T1 | — | — |
| T4 | T4a(54/47) | T4c(46/53) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(54/48) | short(46/52) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
