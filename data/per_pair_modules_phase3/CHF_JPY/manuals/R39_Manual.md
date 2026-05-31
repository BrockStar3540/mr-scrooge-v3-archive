# CHF_JPY — R39 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_2**  (1h ATR 4-8x)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **3,908**  (W=2,338 / L=1,570)  -  WR: **59.8%**

## Session distribution

- asia: n=1481  W=868/L=613  WR=58.6%
- ny_close: n=756  W=490/L=266  WR=64.8%
- ny_open: n=505  W=299/L=206  WR=59.2%
- ny_mid: n=375  W=234/L=141  WR=62.4%
- london: n=347  W=217/L=130  WR=62.5%
- off_hours: n=244  W=118/L=126  WR=48.4%
- london_open: n=118  W=63/L=55  WR=53.4%
- asia_late: n=82  W=49/L=33  WR=59.8%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60e AND T4=T4c AND session_bucket=london`
- Raw: n=147  W=128/L=19  WR=87.1%
- Refine: exclude BBP=BBP1 drops 13/19 losers (68%)
- **Final: n=118  W=112/L=6  WR=94.9%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; session=london  •  AVOID when just touched lower band

### W02.  `H60=H60a AND ZS=ZS3 AND session_bucket=ny_close`
- Raw: n=144  W=124/L=20  WR=86.1%
- Refine: exclude RSI=RSI3 drops 18/20 losers (90%)
- **Final: n=45  W=43/L=2  WR=95.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; zscore -1 to +1 neutral; session=ny_close  •  AVOID when RSI 40-50 lower neutral

### W03.  `H60=H60a AND T1=T1c AND T4=T4a AND BBP=BBP3`
- Raw: n=140  W=123/L=17  WR=87.9%
- Refine: exclude H20=H20a drops 15/17 losers (88%)
- **Final: n=68  W=66/L=2  WR=97.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; middle of band  •  AVOID when HTF20 aligned WITH trade

### W04.  `H60=H60a AND T4=T4a AND BBP=BBP3 AND RSI=RSI3`
- Raw: n=137  W=122/L=15  WR=89.1%
- Refine: exclude H20=H20a drops 11/15 losers (73%)
- **Final: n=60  W=56/L=4  WR=93.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; middle of band; RSI 40-50 lower neutral  •  AVOID when HTF20 aligned WITH trade

### W05.  `T1=T1a AND RSI=RSI3 AND session_bucket=london`
- Raw: n=137  W=120/L=17  WR=87.6%
- Refine: exclude BBP=BBP1 drops 13/17 losers (76%)
- **Final: n=108  W=104/L=4  WR=96.3%**
- **Dir: ?**  •  1h trend WITH trade; RSI 40-50 lower neutral; session=london  •  AVOID when just touched lower band

### W06.  `T4=T4c AND direction_exec=short AND session_bucket=london`
- Raw: n=137  W=118/L=19  WR=86.1%
- Refine: exclude BBP=BBP1 drops 13/19 losers (68%)
- **Final: n=108  W=102/L=6  WR=94.4%**
- **Dir: SHORT**  •  4h trend AGAINST trade; session=london  •  AVOID when just touched lower band

### W07.  `H60=H60e AND T4=T4c AND direction_exec=short AND session_bucket=london`
- Raw: n=137  W=118/L=19  WR=86.1%
- Refine: exclude BBP=BBP1 drops 13/19 losers (68%)
- **Final: n=108  W=102/L=6  WR=94.4%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend AGAINST trade; session=london  •  AVOID when just touched lower band

### W08.  `H60=H60e AND RSI=RSI3 AND session_bucket=london`
- Raw: n=135  W=116/L=19  WR=85.9%
- Refine: exclude BBP=BBP1 drops 13/19 losers (68%)
- **Final: n=106  W=100/L=6  WR=94.3%**
- **Dir: ?**  •  HTF60 strongly against; RSI 40-50 lower neutral; session=london  •  AVOID when just touched lower band

### W09.  `T4=T4c AND RSI=RSI3 AND session_bucket=london`
- Raw: n=135  W=116/L=19  WR=85.9%
- Refine: exclude BBP=BBP1 drops 13/19 losers (68%)
- **Final: n=106  W=100/L=6  WR=94.3%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; session=london  •  AVOID when just touched lower band

### W10.  `H60=H60e AND T4=T4c AND RSI=RSI3 AND session_bucket=london`
- Raw: n=135  W=116/L=19  WR=85.9%
- Refine: exclude BBP=BBP1 drops 13/19 losers (68%)
- **Final: n=106  W=100/L=6  WR=94.3%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 40-50 lower neutral; session=london  •  AVOID when just touched lower band

### W11.  `H20=H20a AND H60=H60a AND ZS=ZS3 AND session_bucket=asia`
- Raw: n=134  W=117/L=17  WR=87.3%
- Refine: exclude BBP=BBP3 drops 15/17 losers (88%)
- **Final: n=63  W=61/L=2  WR=96.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; zscore -1 to +1 neutral; session=asia  •  AVOID when middle of band

### W12.  `H60=H60e AND T1=T1a AND T4=T4c AND session_bucket=london`
- Raw: n=133  W=116/L=17  WR=87.2%
- Refine: exclude BBP=BBP1 drops 13/17 losers (76%)
- **Final: n=104  W=100/L=4  WR=96.2%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; session=london  •  AVOID when just touched lower band

### W13.  `H60=H60e AND T1=T1a AND RSI=RSI3 AND session_bucket=london`
- Raw: n=133  W=116/L=17  WR=87.2%
- Refine: exclude BBP=BBP1 drops 13/17 losers (76%)
- **Final: n=104  W=100/L=4  WR=96.2%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; RSI 40-50 lower neutral; session=london  •  AVOID when just touched lower band

### W14.  `T1=T1a AND T4=T4c AND RSI=RSI3 AND session_bucket=london`
- Raw: n=133  W=116/L=17  WR=87.2%
- Refine: exclude BBP=BBP1 drops 13/17 losers (76%)
- **Final: n=104  W=100/L=4  WR=96.2%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral; session=london  •  AVOID when just touched lower band

### W15.  `H60=H60a AND ZS=ZS3 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=133  W=115/L=18  WR=86.5%
- Refine: exclude T4=T4c drops 11/18 losers (61%)
- **Final: n=78  W=71/L=7  WR=91.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; zscore -1 to +1 neutral; session=ny_close  •  AVOID when 4h trend AGAINST trade

### W16.  `H60=H60a AND T1=T1c AND ZS=ZS3 AND session_bucket=ny_close`
- Raw: n=126  W=112/L=14  WR=88.9%
- Refine: exclude T4=T4c drops 9/14 losers (64%)
- **Final: n=76  W=71/L=5  WR=93.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; zscore -1 to +1 neutral; session=ny_close  •  AVOID when 4h trend AGAINST trade

### W17.  `T1=T1a AND T4=T4c AND direction_exec=short AND session_bucket=london`
- Raw: n=123  W=106/L=17  WR=86.2%
- Refine: exclude BBP=BBP1 drops 13/17 losers (76%)
- **Final: n=94  W=90/L=4  WR=95.7%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend AGAINST trade; session=london  •  AVOID when just touched lower band

### W18.  `T1=T1a AND RSI=RSI3 AND direction_exec=short AND session_bucket=london`
- Raw: n=123  W=106/L=17  WR=86.2%
- Refine: exclude BBP=BBP1 drops 13/17 losers (76%)
- **Final: n=94  W=90/L=4  WR=95.7%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 40-50 lower neutral; session=london  •  AVOID when just touched lower band

### W19.  `T1=T1c AND ZS=ZS3 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=122  W=107/L=15  WR=87.7%
- Refine: exclude T4=T4c drops 10/15 losers (67%)
- **Final: n=68  W=63/L=5  WR=92.6%**
- **Dir: LONG**  •  1h trend AGAINST trade; zscore -1 to +1 neutral; session=ny_close  •  AVOID when 4h trend AGAINST trade

### W20.  `T4=T4a AND BBP=BBP3 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=118  W=105/L=13  WR=89.0%
- Refine: exclude H20=H20a drops 11/13 losers (85%)
- **Final: n=41  W=39/L=2  WR=95.1%**
- **Dir: LONG**  •  4h trend WITH trade; middle of band; RSI 40-50 lower neutral  •  AVOID when HTF20 aligned WITH trade

### W21.  `T1=T1c AND T4=T4a AND BBP=BBP3 AND direction_exec=long`
- Raw: n=118  W=101/L=17  WR=85.6%
- Refine: exclude H20=H20a drops 15/17 losers (88%)
- **Final: n=46  W=44/L=2  WR=95.7%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend WITH trade; middle of band  •  AVOID when HTF20 aligned WITH trade

### W22.  `H20=H20c AND H60=H60a AND T1=T1a AND RSI=RSI4`
- Raw: n=113  W=99/L=14  WR=87.6%
- Refine: exclude session_bucket=asia drops 8/14 losers (57%)
- **Final: n=87  W=81/L=6  WR=93.1%**
- **Dir: ?**  •  HTF20 neutral; HTF60 aligned WITH trade; 1h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when session=asia

### W23.  `H20=H20c AND T1=T1a AND RSI=RSI4 AND direction_exec=long`
- Raw: n=113  W=99/L=14  WR=87.6%
- Refine: exclude session_bucket=asia drops 8/14 losers (57%)
- **Final: n=87  W=81/L=6  WR=93.1%**
- **Dir: LONG**  •  HTF20 neutral; 1h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when session=asia

### W24.  `H60=H60a AND BBP=BBP3 AND session_bucket=ny_close`
- Raw: n=103  W=90/L=13  WR=87.4%
- Refine: exclude T4=T4c drops 9/13 losers (69%)
- **Final: n=65  W=61/L=4  WR=93.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; middle of band; session=ny_close  •  AVOID when 4h trend AGAINST trade

### W25.  `H60=H60a AND BBP=BBP3 AND ZS=ZS3 AND session_bucket=ny_close`
- Raw: n=103  W=90/L=13  WR=87.4%
- Refine: exclude T4=T4c drops 9/13 losers (69%)
- **Final: n=65  W=61/L=4  WR=93.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; middle of band; zscore -1 to +1 neutral; session=ny_close  •  AVOID when 4h trend AGAINST trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND RSI=RSI3 AND ZS=ZS3 AND direction_exec=short`
- Raw: n=230  W=91/L=139  WR=39.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=230  W=91/L=139  WR=39.6%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 40-50 lower neutral; zscore -1 to +1 neutral

### L02.  `H60=H60e AND T4=T4c AND BBP=BBP3`
- Raw: n=182  W=68/L=114  WR=37.4%
- Sharpen: no sharper sub-pattern
- **Sharp: n=182  W=68/L=114  WR=37.4%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; middle of band

### L03.  `H60=H60e AND T4=T4c AND BBP=BBP3 AND ZS=ZS3`
- Raw: n=182  W=68/L=114  WR=37.4%
- Sharpen: no sharper sub-pattern
- **Sharp: n=182  W=68/L=114  WR=37.4%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; middle of band; zscore -1 to +1 neutral

### L04.  `H20=H20a AND H60=H60a AND ZS=ZS4`
- Raw: n=164  W=60/L=104  WR=36.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=164  W=60/L=104  WR=36.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; zscore +1 to +2 overbought

### L05.  `H20=H20a AND H60=H60a AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=164  W=60/L=104  WR=36.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=164  W=60/L=104  WR=36.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; upper third; zscore +1 to +2 overbought

### L06.  `H20=H20a AND H60=H60a AND ZS=ZS4 AND direction_exec=long`
- Raw: n=164  W=60/L=104  WR=36.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=164  W=60/L=104  WR=36.6%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; zscore +1 to +2 overbought

### L07.  `H60=H60e AND T4=T4c AND RSI=RSI3 AND ZS=ZS3`
- Raw: n=160  W=60/L=100  WR=37.5%
- Sharpen: sharpest is H20=H20c (24/100 of losers there)
- **Sharp: n=28  W=4/L=24  WR=14.3%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 40-50 lower neutral; zscore -1 to +1 neutral  •  ONLY when HTF20 neutral

### L08.  `H60=H60e AND BBP=BBP3 AND RSI=RSI3`
- Raw: n=158  W=61/L=97  WR=38.6%
- Sharpen: sharpest is T4=T4c (67/97 of losers there)
- **Sharp: n=99  W=32/L=67  WR=32.3%**
- **Dir: ?**  •  HTF60 strongly against; middle of band; RSI 40-50 lower neutral  •  ONLY when 4h trend AGAINST trade

### L09.  `H60=H60e AND BBP=BBP3 AND RSI=RSI3 AND ZS=ZS3`
- Raw: n=158  W=61/L=97  WR=38.6%
- Sharpen: sharpest is T4=T4c (67/97 of losers there)
- **Sharp: n=99  W=32/L=67  WR=32.3%**
- **Dir: ?**  •  HTF60 strongly against; middle of band; RSI 40-50 lower neutral; zscore -1 to +1 neutral  •  ONLY when 4h trend AGAINST trade

### L10.  `T4=T4c AND BBP=BBP3 AND direction_exec=short`
- Raw: n=151  W=56/L=95  WR=37.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=151  W=56/L=95  WR=37.1%**
- **Dir: SHORT**  •  4h trend AGAINST trade; middle of band

### L11.  `H60=H60e AND T4=T4c AND BBP=BBP3 AND direction_exec=short`
- Raw: n=151  W=56/L=95  WR=37.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=151  W=56/L=95  WR=37.1%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend AGAINST trade; middle of band

### L12.  `T4=T4c AND BBP=BBP3 AND ZS=ZS3 AND direction_exec=short`
- Raw: n=151  W=56/L=95  WR=37.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=151  W=56/L=95  WR=37.1%**
- **Dir: SHORT**  •  4h trend AGAINST trade; middle of band; zscore -1 to +1 neutral

### L13.  `H60=H60e AND BBP=BBP3 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=140  W=54/L=86  WR=38.6%
- Sharpen: sharpest is T4=T4c (56/86 of losers there)
- **Sharp: n=81  W=25/L=56  WR=30.9%**
- **Dir: SHORT**  •  HTF60 strongly against; middle of band; RSI 40-50 lower neutral  •  ONLY when 4h trend AGAINST trade

### L14.  `H60=H60e AND BBP=BBP4 AND session_bucket=asia`
- Raw: n=138  W=55/L=83  WR=39.9%
- Sharpen: sharpest is RSI=RSI3 (31/83 of losers there)
- **Sharp: n=38  W=7/L=31  WR=18.4%**
- **Dir: ?**  •  HTF60 strongly against; upper third; session=asia  •  ONLY when RSI 40-50 lower neutral

### L15.  `T4=T4c AND RSI=RSI3 AND ZS=ZS3 AND direction_exec=short`
- Raw: n=136  W=48/L=88  WR=35.3%
- Sharpen: sharpest is H20=H20c (24/88 of losers there)
- **Sharp: n=28  W=4/L=24  WR=14.3%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; zscore -1 to +1 neutral  •  ONLY when HTF20 neutral

### L16.  `BBP=BBP4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=134  W=53/L=81  WR=39.6%
- Sharpen: sharpest is RSI=RSI3 (31/81 of losers there)
- **Sharp: n=38  W=7/L=31  WR=18.4%**
- **Dir: SHORT**  •  upper third; session=asia  •  ONLY when RSI 40-50 lower neutral

### L17.  `H60=H60a AND T1=T1c AND session_bucket=london`
- Raw: n=127  W=50/L=77  WR=39.4%
- Sharpen: sharpest is ZS=ZS2 (30/77 of losers there)
- **Sharp: n=37  W=7/L=30  WR=18.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=london  •  ONLY when zscore -2 to -1 oversold

### L18.  `H60=H60e AND BBP=BBP4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=125  W=48/L=77  WR=38.4%
- Sharpen: sharpest is RSI=RSI3 (31/77 of losers there)
- **Sharp: n=38  W=7/L=31  WR=18.4%**
- **Dir: SHORT**  •  HTF60 strongly against; upper third; session=asia  •  ONLY when RSI 40-50 lower neutral

### L19.  `H20=H20c AND H60=H60e AND RSI=RSI4`
- Raw: n=123  W=45/L=78  WR=36.6%
- Sharpen: sharpest is session_bucket=asia_late (19/78 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: ?**  •  HTF20 neutral; HTF60 strongly against; RSI 50-60 upper neutral  •  ONLY when session=asia_late

### L20.  `H20=H20c AND RSI=RSI4 AND direction_exec=short`
- Raw: n=123  W=45/L=78  WR=36.6%
- Sharpen: sharpest is session_bucket=asia_late (19/78 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: SHORT**  •  HTF20 neutral; RSI 50-60 upper neutral  •  ONLY when session=asia_late

### L21.  `H20=H20c AND H60=H60e AND RSI=RSI4 AND direction_exec=short`
- Raw: n=123  W=45/L=78  WR=36.6%
- Sharpen: sharpest is session_bucket=asia_late (19/78 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: SHORT**  •  HTF20 neutral; HTF60 strongly against; RSI 50-60 upper neutral  •  ONLY when session=asia_late

### L22.  `H20=H20a AND T1=T1c AND ZS=ZS4`
- Raw: n=117  W=39/L=78  WR=33.3%
- Sharpen: sharpest is RSI=RSI4 (34/78 of losers there)
- **Sharp: n=43  W=9/L=34  WR=20.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; zscore +1 to +2 overbought  •  ONLY when RSI 50-60 upper neutral

### L23.  `H20=H20a AND T1=T1c AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=117  W=39/L=78  WR=33.3%
- Sharpen: sharpest is RSI=RSI4 (34/78 of losers there)
- **Sharp: n=43  W=9/L=34  WR=20.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; upper third; zscore +1 to +2 overbought  •  ONLY when RSI 50-60 upper neutral

### L24.  `H20=H20a AND T1=T1c AND ZS=ZS4 AND direction_exec=long`
- Raw: n=117  W=39/L=78  WR=33.3%
- Sharpen: sharpest is RSI=RSI4 (34/78 of losers there)
- **Sharp: n=43  W=9/L=34  WR=20.9%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; zscore +1 to +2 overbought  •  ONLY when RSI 50-60 upper neutral

### L25.  `T1=T1c AND T4=T4a AND session_bucket=london`
- Raw: n=116  W=40/L=76  WR=34.5%
- Sharpen: sharpest is BBP=BBP0 (19/76 of losers there)
- **Sharp: n=20  W=1/L=19  WR=5.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; session=london  •  ONLY when deep below lower band

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | H60a(56/43) | H60e(43/56) |
| T1 | — | — |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(53/46) | short(47/54) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
