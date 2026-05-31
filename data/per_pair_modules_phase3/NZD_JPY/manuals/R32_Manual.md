# NZD_JPY — R32 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **3,642**  (W=2,234 / L=1,408)  -  WR: **61.3%**

## Session distribution

- asia: n=1077  W=661/L=416  WR=61.4%
- ny_mid: n=1062  W=638/L=424  WR=60.1%
- london_open: n=741  W=448/L=293  WR=60.5%
- ny_close: n=325  W=211/L=114  WR=64.9%
- ny_open: n=170  W=101/L=69  WR=59.4%
- london: n=123  W=81/L=42  WR=65.9%
- off_hours: n=96  W=61/L=35  WR=63.5%
- asia_late: n=48  W=33/L=15  WR=68.8%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60a AND T4=T4a AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=215  W=183/L=32  WR=85.1%
- Refine: exclude T1=T1c drops 21/32 losers (66%)
- **Final: n=138  W=127/L=11  WR=92.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when 1h trend AGAINST trade

### W02.  `T1=T1a AND T4=T4a AND BBP=BBP4 AND direction_exec=long`
- Raw: n=159  W=139/L=20  WR=87.4%
- Refine: exclude RSI=RSI3 drops 8/20 losers (40%)
- **Final: n=151  W=139/L=12  WR=92.1%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; upper third  •  AVOID when RSI 40-50 lower neutral

### W03.  `H60=H60a AND T1=T1a AND T4=T4a AND BBP=BBP4`
- Raw: n=154  W=139/L=15  WR=90.3%
- Refine: exclude H20=H20d drops 3/15 losers (20%)
- **Final: n=151  W=139/L=12  WR=92.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; upper third  •  AVOID when HTF20 mildly against

### W04.  `H20=H20a AND RSI=RSI4 AND ZS=ZS3 AND direction_exec=long`
- Raw: n=150  W=132/L=18  WR=88.0%
- Refine: exclude strategy_id=TF2_pullback_EMA20_long drops 6/18 losers (33%)
- **Final: n=122  W=110/L=12  WR=90.2%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  AVOID when strategy=TF2_pullback_EMA20_long

### W05.  `T1=T1a AND T4=T4a AND ZS=ZS4 AND direction_exec=long`
- Raw: n=142  W=127/L=15  WR=89.4%
- Refine: exclude H60=H60b drops 4/15 losers (27%)
- **Final: n=138  W=127/L=11  WR=92.0%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; zscore +1 to +2 overbought  •  AVOID when HTF60 slightly aligned

### W06.  `H60=H60a AND T1=T1a AND T4=T4a AND ZS=ZS4`
- Raw: n=138  W=127/L=11  WR=92.0%
- Refine: exclude session_bucket=asia_late drops 3/11 losers (27%)
- **Final: n=135  W=127/L=8  WR=94.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; zscore +1 to +2 overbought  •  AVOID when session=asia_late

### W07.  `H60=H60e AND T4=T4a AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=130  W=114/L=16  WR=87.7%
- Refine: exclude H20=H20d drops 4/16 losers (25%)
- **Final: n=122  W=110/L=12  WR=90.2%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; lower third; RSI 40-50 lower neutral  •  AVOID when HTF20 mildly against

### W08.  `T4=T4a AND BBP=BBP2 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=130  W=114/L=16  WR=87.7%
- Refine: exclude H20=H20d drops 4/16 losers (25%)
- **Final: n=122  W=110/L=12  WR=90.2%**
- **Dir: SHORT**  •  4h trend WITH trade; lower third; RSI 40-50 lower neutral  •  AVOID when HTF20 mildly against

### W09.  `H20=H20a AND H60=H60a AND RSI=RSI4 AND ZS=ZS3`
- Raw: n=127  W=111/L=16  WR=87.4%
- Refine: exclude strategy_id=TF2_pullback_EMA20_long drops 6/16 losers (38%)
- **Final: n=102  W=92/L=10  WR=90.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  AVOID when strategy=TF2_pullback_EMA20_long

### W10.  `T4=T4a AND RSI=RSI4 AND ZS=ZS3 AND direction_exec=long`
- Raw: n=127  W=111/L=16  WR=87.4%
- Refine: exclude session_bucket=ny_mid drops 4/16 losers (25%)
- **Final: n=115  W=103/L=12  WR=89.6%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  AVOID when session=ny_mid

### W11.  `T4=T4c AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=125  W=117/L=8  WR=93.6%
- Refine: exclude session_bucket=ny_mid drops 7/8 losers (88%)
- **Final: n=95  W=94/L=1  WR=98.9%**
- **Dir: ?**  •  4h trend AGAINST trade; deep below lower band; zscore -3 to -2 deep oversold  •  AVOID when session=ny_mid

### W12.  `H60=H60e AND T4=T4a AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=109  W=95/L=14  WR=87.2%
- Refine: exclude H20=H20d drops 4/14 losers (29%)
- **Final: n=101  W=91/L=10  WR=90.1%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when HTF20 mildly against

### W13.  `T4=T4a AND RSI=RSI3 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=109  W=95/L=14  WR=87.2%
- Refine: exclude H20=H20d drops 4/14 losers (29%)
- **Final: n=101  W=91/L=10  WR=90.1%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  AVOID when HTF20 mildly against

### W14.  `T4=T4a AND BBP=BBP2 AND RSI=RSI3 AND session_bucket=ny_mid`
- Raw: n=109  W=93/L=16  WR=85.3%
- Refine: exclude H60=H60a drops 13/16 losers (81%)
- **Final: n=57  W=54/L=3  WR=94.7%**
- **Dir: ?**  •  4h trend WITH trade; lower third; RSI 40-50 lower neutral; session=ny_mid  •  AVOID when HTF60 aligned WITH trade

### W15.  `H20=H20e AND RSI=RSI4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=106  W=91/L=15  WR=85.8%
- Refine: exclude T4=T4c drops 15/15 losers (100%)
- **Final: n=59  W=59/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 50-60 upper neutral; session=asia  •  AVOID when 4h trend AGAINST trade

### W16.  `T4=T4c AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=105  W=92/L=13  WR=87.6%
- Refine: exclude BBP=BBP1 drops 13/13 losers (100%)
- **Final: n=58  W=58/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend AGAINST trade; zscore -3 to -2 deep oversold; session=asia  •  AVOID when just touched lower band

### W17.  `H20=H20e AND H60=H60a AND T4=T4a AND BBP=BBP4`
- Raw: n=103  W=96/L=7  WR=93.2%
- Refine: exclude session_bucket=asia_late drops 3/7 losers (43%)
- **Final: n=98  W=94/L=4  WR=95.9%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 4h trend WITH trade; upper third  •  AVOID when session=asia_late

### W18.  `H20=H20e AND H60=H60a AND T4=T4a AND ZS=ZS4`
- Raw: n=101  W=95/L=6  WR=94.1%
- Refine: exclude session_bucket=asia_late drops 3/6 losers (50%)
- **Final: n=96  W=93/L=3  WR=96.9%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 4h trend WITH trade; zscore +1 to +2 overbought  •  AVOID when session=asia_late

### W19.  `H20=H20a AND H60=H60e AND BBP=BBP2`
- Raw: n=95  W=82/L=13  WR=86.3%
- Refine: exclude T1=T1c drops 13/13 losers (100%)
- **Final: n=57  W=57/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; lower third  •  AVOID when 1h trend AGAINST trade

### W20.  `H20=H20e AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=95  W=81/L=14  WR=85.3%
- Refine: exclude direction_exec=short drops 9/14 losers (64%)
- **Final: n=69  W=64/L=5  WR=92.8%**
- **Dir: ?**  •  HTF20 strongly against; zscore +1 to +2 overbought; session=asia  •  AVOID when short

### W21.  `H20=H20e AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=95  W=81/L=14  WR=85.3%
- Refine: exclude direction_exec=short drops 9/14 losers (64%)
- **Final: n=69  W=64/L=5  WR=92.8%**
- **Dir: ?**  •  HTF20 strongly against; upper third; zscore +1 to +2 overbought; session=asia  •  AVOID when short

### W22.  `H20=H20a AND BBP=BBP2 AND direction_exec=short`
- Raw: n=91  W=78/L=13  WR=85.7%
- Refine: exclude T1=T1c drops 13/13 losers (100%)
- **Final: n=53  W=53/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; lower third  •  AVOID when 1h trend AGAINST trade

### W23.  `H20=H20a AND H60=H60e AND BBP=BBP2 AND direction_exec=short`
- Raw: n=91  W=78/L=13  WR=85.7%
- Refine: exclude T1=T1c drops 13/13 losers (100%)
- **Final: n=53  W=53/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 strongly against; lower third  •  AVOID when 1h trend AGAINST trade

### W24.  `T4=T4a AND BBP=BBP3 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=89  W=78/L=11  WR=87.6%
- Refine: exclude T1=T1a drops 7/11 losers (64%)
- **Final: n=57  W=53/L=4  WR=93.0%**
- **Dir: LONG**  •  4h trend WITH trade; middle of band; RSI 50-60 upper neutral  •  AVOID when 1h trend WITH trade

### W25.  `H20=H20a AND BBP=BBP3 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=89  W=77/L=12  WR=86.5%
- Refine: exclude T1=T1a drops 8/12 losers (67%)
- **Final: n=52  W=48/L=4  WR=92.3%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; middle of band; RSI 50-60 upper neutral  •  AVOID when 1h trend WITH trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20a AND T1=T1c AND T4=T4a AND session_bucket=asia`
- Raw: n=203  W=79/L=124  WR=38.9%
- Sharpen: sharpest is RSI=RSI3 (63/124 of losers there)
- **Sharp: n=80  W=17/L=63  WR=21.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; session=asia  •  ONLY when RSI 40-50 lower neutral

### L02.  `RSI=RSI4 AND ZS=ZS3 AND direction_exec=short`
- Raw: n=174  W=57/L=117  WR=32.8%
- Sharpen: sharpest is H20=H20e (69/117 of losers there)
- **Sharp: n=85  W=16/L=69  WR=18.8%**
- **Dir: SHORT**  •  RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  ONLY when HTF20 strongly against

### L03.  `H60=H60e AND RSI=RSI4 AND ZS=ZS3`
- Raw: n=162  W=59/L=103  WR=36.4%
- Sharpen: sharpest is H20=H20e (54/103 of losers there)
- **Sharp: n=66  W=12/L=54  WR=18.2%**
- **Dir: ?**  •  HTF60 strongly against; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  ONLY when HTF20 strongly against

### L04.  `H20=H20a AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=155  W=54/L=101  WR=34.8%
- Sharpen: sharpest is T4=T4a (63/101 of losers there)
- **Sharp: n=82  W=19/L=63  WR=23.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 40-50 lower neutral; session=asia  •  ONLY when 4h trend WITH trade

### L05.  `H60=H60e AND RSI=RSI4 AND ZS=ZS3 AND direction_exec=short`
- Raw: n=154  W=53/L=101  WR=34.4%
- Sharpen: sharpest is H20=H20e (54/101 of losers there)
- **Sharp: n=66  W=12/L=54  WR=18.2%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  ONLY when HTF20 strongly against

### L06.  `T1=T1c AND T4=T4a AND ZS=ZS1`
- Raw: n=151  W=60/L=91  WR=39.7%
- Sharpen: sharpest is BBP=BBP0 (42/91 of losers there)
- **Sharp: n=53  W=11/L=42  WR=20.8%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  ONLY when deep below lower band

### L07.  `H60=H60e AND T4=T4c AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=149  W=58/L=91  WR=38.9%
- Sharpen: sharpest is H20=H20a (44/91 of losers there)
- **Sharp: n=53  W=9/L=44  WR=17.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; upper third; RSI 50-60 upper neutral  •  ONLY when HTF20 aligned WITH trade

### L08.  `H20=H20a AND H60=H60a AND T4=T4a AND session_bucket=asia`
- Raw: n=145  W=57/L=88  WR=39.3%
- Sharpen: sharpest is RSI=RSI3 (41/88 of losers there)
- **Sharp: n=54  W=13/L=41  WR=24.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade; session=asia  •  ONLY when RSI 40-50 lower neutral

### L09.  `H20=H20a AND T1=T1c AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=141  W=50/L=91  WR=35.5%
- Sharpen: sharpest is T4=T4a (63/91 of losers there)
- **Sharp: n=80  W=17/L=63  WR=21.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 40-50 lower neutral; session=asia  •  ONLY when 4h trend WITH trade

### L10.  `T1=T1c AND RSI=RSI3 AND direction_exec=long AND session_bucket=asia`
- Raw: n=133  W=50/L=83  WR=37.6%
- Sharpen: sharpest is T4=T4a (46/83 of losers there)
- **Sharp: n=63  W=17/L=46  WR=27.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 40-50 lower neutral; session=asia  •  ONLY when 4h trend WITH trade

### L11.  `H20=H20e AND RSI=RSI4 AND session_bucket=london_open`
- Raw: n=132  W=52/L=80  WR=39.4%
- Sharpen: sharpest is ZS=ZS3 (30/80 of losers there)
- **Sharp: n=39  W=9/L=30  WR=23.1%**
- **Dir: ?**  •  HTF20 strongly against; RSI 50-60 upper neutral; session=london_open  •  ONLY when zscore -1 to +1 neutral

### L12.  `H20=H20a AND RSI=RSI3 AND direction_exec=long AND session_bucket=asia`
- Raw: n=130  W=48/L=82  WR=36.9%
- Sharpen: sharpest is T4=T4a (44/82 of losers there)
- **Sharp: n=57  W=13/L=44  WR=22.8%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 40-50 lower neutral; session=asia  •  ONLY when 4h trend WITH trade

### L13.  `H60=H60e AND BBP=BBP4 AND session_bucket=ny_mid`
- Raw: n=128  W=50/L=78  WR=39.1%
- Sharpen: sharpest is T1=T1c (43/78 of losers there)
- **Sharp: n=61  W=18/L=43  WR=29.5%**
- **Dir: ?**  •  HTF60 strongly against; upper third; session=ny_mid  •  ONLY when 1h trend AGAINST trade

### L14.  `H20=H20a AND T4=T4a AND ZS=ZS1`
- Raw: n=124  W=45/L=79  WR=36.3%
- Sharpen: sharpest is BBP=BBP0 (30/79 of losers there)
- **Sharp: n=38  W=8/L=30  WR=21.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  ONLY when deep below lower band

### L15.  `H20=H20a AND H60=H60a AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=121  W=48/L=73  WR=39.7%
- Sharpen: sharpest is T4=T4a (41/73 of losers there)
- **Sharp: n=54  W=13/L=41  WR=24.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 40-50 lower neutral; session=asia  •  ONLY when 4h trend WITH trade

### L16.  `T1=T1c AND T4=T4a AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=119  W=42/L=77  WR=35.3%
- Sharpen: sharpest is H20=H20a (63/77 of losers there)
- **Sharp: n=80  W=17/L=63  WR=21.2%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 40-50 lower neutral; session=asia  •  ONLY when HTF20 aligned WITH trade

### L17.  `H60=H60e AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=119  W=46/L=73  WR=38.7%
- Sharpen: no sharper sub-pattern
- **Sharp: n=119  W=46/L=73  WR=38.7%**
- **Dir: ?**  •  HTF60 strongly against; zscore +1 to +2 overbought; session=ny_mid

### L18.  `H60=H60e AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=119  W=46/L=73  WR=38.7%
- Sharpen: no sharper sub-pattern
- **Sharp: n=119  W=46/L=73  WR=38.7%**
- **Dir: ?**  •  HTF60 strongly against; upper third; zscore +1 to +2 overbought; session=ny_mid

### L19.  `BBP=BBP3 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=118  W=40/L=78  WR=33.9%
- Sharpen: sharpest is T4=T4c (46/78 of losers there)
- **Sharp: n=57  W=11/L=46  WR=19.3%**
- **Dir: SHORT**  •  middle of band; RSI 50-60 upper neutral  •  ONLY when 4h trend AGAINST trade

### L20.  `BBP=BBP3 AND RSI=RSI4 AND ZS=ZS3 AND direction_exec=short`
- Raw: n=118  W=40/L=78  WR=33.9%
- Sharpen: sharpest is T4=T4c (46/78 of losers there)
- **Sharp: n=57  W=11/L=46  WR=19.3%**
- **Dir: SHORT**  •  middle of band; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  ONLY when 4h trend AGAINST trade

### L21.  `H20=H20e AND T1=T1c AND T4=T4c`
- Raw: n=118  W=45/L=73  WR=38.1%
- Sharpen: sharpest is BBP=BBP2 (32/73 of losers there)
- **Sharp: n=40  W=8/L=32  WR=20.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when lower third

### L22.  `T1=T1c AND T4=T4c AND BBP=BBP2`
- Raw: n=115  W=43/L=72  WR=37.4%
- Sharpen: sharpest is session_bucket=ny_mid (33/72 of losers there)
- **Sharp: n=37  W=4/L=33  WR=10.8%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; lower third  •  ONLY when session=ny_mid

### L23.  `H60=H60e AND BBP=BBP4 AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=113  W=41/L=72  WR=36.3%
- Sharpen: sharpest is H20=H20d (14/72 of losers there)
- **Sharp: n=15  W=1/L=14  WR=6.7%**
- **Dir: ?**  •  HTF60 strongly against; upper third; RSI 50-60 upper neutral; session=ny_mid  •  ONLY when HTF20 mildly against

### L24.  `T4=T4c AND BBP=BBP2 AND session_bucket=ny_mid`
- Raw: n=111  W=40/L=71  WR=36.0%
- Sharpen: sharpest is RSI=RSI3 (67/71 of losers there)
- **Sharp: n=88  W=21/L=67  WR=23.9%**
- **Dir: ?**  •  4h trend AGAINST trade; lower third; session=ny_mid  •  ONLY when RSI 40-50 lower neutral

### L25.  `H60=H60a AND T4=T4c AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=110  W=38/L=72  WR=34.5%
- Sharpen: sharpest is session_bucket=ny_mid (38/72 of losers there)
- **Sharp: n=41  W=3/L=38  WR=7.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; lower third; RSI 40-50 lower neutral  •  ONLY when session=ny_mid

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | — |
| T1 | T1a(54/47) | T1c(46/53) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
