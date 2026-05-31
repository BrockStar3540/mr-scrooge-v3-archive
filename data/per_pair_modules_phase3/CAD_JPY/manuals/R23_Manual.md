# CAD_JPY — R23 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50e**  (EMA50 down >0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **3,909**  (W=2,395 / L=1,514)  -  WR: **61.3%**

## Session distribution

- asia: n=1157  W=721/L=436  WR=62.3%
- ny_close: n=735  W=468/L=267  WR=63.7%
- ny_mid: n=675  W=407/L=268  WR=60.3%
- ny_open: n=473  W=282/L=191  WR=59.6%
- london_open: n=339  W=199/L=140  WR=58.7%
- london: n=244  W=158/L=86  WR=64.8%
- asia_late: n=189  W=103/L=86  WR=54.5%
- off_hours: n=97  W=57/L=40  WR=58.8%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND T4=T4c AND session_bucket=asia`
- Raw: n=175  W=153/L=22  WR=87.4%
- Refine: exclude H60=H60d drops 7/22 losers (32%)
- **Final: n=166  W=151/L=15  WR=91.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; session=asia  •  AVOID when HTF60 mildly against

### W02.  `H20=H20a AND H60=H60a AND session_bucket=asia`
- Raw: n=166  W=151/L=15  WR=91.0%
- Refine: exclude BBP=BBP4 drops 10/15 losers (67%)
- **Final: n=95  W=90/L=5  WR=94.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=asia  •  AVOID when upper third

### W03.  `H20=H20a AND T1=T1c AND session_bucket=asia`
- Raw: n=166  W=151/L=15  WR=91.0%
- Refine: exclude BBP=BBP4 drops 10/15 losers (67%)
- **Final: n=95  W=90/L=5  WR=94.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; session=asia  •  AVOID when upper third

### W04.  `H20=H20a AND direction_exec=long AND session_bucket=asia`
- Raw: n=166  W=151/L=15  WR=91.0%
- Refine: exclude BBP=BBP4 drops 10/15 losers (67%)
- **Final: n=95  W=90/L=5  WR=94.7%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; session=asia  •  AVOID when upper third

### W05.  `H20=H20a AND H60=H60a AND T1=T1c AND session_bucket=asia`
- Raw: n=166  W=151/L=15  WR=91.0%
- Refine: exclude BBP=BBP4 drops 10/15 losers (67%)
- **Final: n=95  W=90/L=5  WR=94.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade; session=asia  •  AVOID when upper third

### W06.  `H20=H20a AND H60=H60a AND T4=T4c AND session_bucket=asia`
- Raw: n=166  W=151/L=15  WR=91.0%
- Refine: exclude BBP=BBP4 drops 10/15 losers (67%)
- **Final: n=95  W=90/L=5  WR=94.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend AGAINST trade; session=asia  •  AVOID when upper third

### W07.  `H20=H20a AND H60=H60a AND direction_exec=long AND session_bucket=asia`
- Raw: n=166  W=151/L=15  WR=91.0%
- Refine: exclude BBP=BBP4 drops 10/15 losers (67%)
- **Final: n=95  W=90/L=5  WR=94.7%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=asia  •  AVOID when upper third

### W08.  `H20=H20a AND T1=T1c AND T4=T4c AND session_bucket=asia`
- Raw: n=166  W=151/L=15  WR=91.0%
- Refine: exclude BBP=BBP4 drops 10/15 losers (67%)
- **Final: n=95  W=90/L=5  WR=94.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; session=asia  •  AVOID when upper third

### W09.  `H20=H20a AND T1=T1c AND direction_exec=long AND session_bucket=asia`
- Raw: n=166  W=151/L=15  WR=91.0%
- Refine: exclude BBP=BBP4 drops 10/15 losers (67%)
- **Final: n=95  W=90/L=5  WR=94.7%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; session=asia  •  AVOID when upper third

### W10.  `H20=H20a AND T4=T4c AND direction_exec=long AND session_bucket=asia`
- Raw: n=166  W=151/L=15  WR=91.0%
- Refine: exclude BBP=BBP4 drops 10/15 losers (67%)
- **Final: n=95  W=90/L=5  WR=94.7%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; session=asia  •  AVOID when upper third

### W11.  `H20=H20a AND RSI=RSI1 AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=166  W=142/L=24  WR=85.5%
- Refine: no further refinement
- **Final: n=166  W=142/L=24  WR=85.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 20-30 oversold; zscore -2 to -1 oversold; session=asia

### W12.  `H60=H60a AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=141  W=122/L=19  WR=86.5%
- Refine: exclude H20=H20e drops 18/19 losers (95%)
- **Final: n=74  W=73/L=1  WR=98.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 30-40 weak; session=asia  •  AVOID when HTF20 strongly against

### W13.  `H60=H60a AND T1=T1c AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=141  W=122/L=19  WR=86.5%
- Refine: exclude H20=H20e drops 18/19 losers (95%)
- **Final: n=74  W=73/L=1  WR=98.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 30-40 weak; session=asia  •  AVOID when HTF20 strongly against

### W14.  `H60=H60a AND T4=T4c AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=141  W=122/L=19  WR=86.5%
- Refine: exclude H20=H20e drops 18/19 losers (95%)
- **Final: n=74  W=73/L=1  WR=98.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 30-40 weak; session=asia  •  AVOID when HTF20 strongly against

### W15.  `H60=H60a AND RSI=RSI2 AND direction_exec=long AND session_bucket=asia`
- Raw: n=141  W=122/L=19  WR=86.5%
- Refine: exclude H20=H20e drops 18/19 losers (95%)
- **Final: n=74  W=73/L=1  WR=98.6%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 30-40 weak; session=asia  •  AVOID when HTF20 strongly against

### W16.  `H20=H20a AND T1=T1c AND BBP=BBP4`
- Raw: n=101  W=88/L=13  WR=87.1%
- Refine: exclude RSI=RSI1 drops 5/13 losers (38%)
- **Final: n=88  W=80/L=8  WR=90.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; upper third  •  AVOID when RSI 20-30 oversold

### W17.  `H20=H20a AND T1=T1c AND ZS=ZS4`
- Raw: n=95  W=82/L=13  WR=86.3%
- Refine: exclude RSI=RSI1 drops 5/13 losers (38%)
- **Final: n=82  W=74/L=8  WR=90.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; zscore +1 to +2 overbought  •  AVOID when RSI 20-30 oversold

### W18.  `H20=H20a AND T1=T1c AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=95  W=82/L=13  WR=86.3%
- Refine: exclude RSI=RSI1 drops 5/13 losers (38%)
- **Final: n=82  W=74/L=8  WR=90.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; upper third; zscore +1 to +2 overbought  •  AVOID when RSI 20-30 oversold

### W19.  `H20=H20a AND H60=H60a AND T1=T1c AND BBP=BBP4`
- Raw: n=93  W=80/L=13  WR=86.0%
- Refine: exclude RSI=RSI1 drops 5/13 losers (38%)
- **Final: n=80  W=72/L=8  WR=90.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade; upper third  •  AVOID when RSI 20-30 oversold

### W20.  `H20=H20a AND H60=H60a AND T1=T1c AND ZS=ZS4`
- Raw: n=93  W=80/L=13  WR=86.0%
- Refine: exclude RSI=RSI1 drops 5/13 losers (38%)
- **Final: n=80  W=72/L=8  WR=90.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade; zscore +1 to +2 overbought  •  AVOID when RSI 20-30 oversold

### W21.  `H20=H20a AND T1=T1c AND BBP=BBP4 AND direction_exec=long`
- Raw: n=93  W=80/L=13  WR=86.0%
- Refine: exclude RSI=RSI1 drops 5/13 losers (38%)
- **Final: n=80  W=72/L=8  WR=90.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; upper third  •  AVOID when RSI 20-30 oversold

### W22.  `H20=H20a AND T1=T1c AND ZS=ZS4 AND direction_exec=long`
- Raw: n=93  W=80/L=13  WR=86.0%
- Refine: exclude RSI=RSI1 drops 5/13 losers (38%)
- **Final: n=80  W=72/L=8  WR=90.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; zscore +1 to +2 overbought  •  AVOID when RSI 20-30 oversold

### W23.  `H20=H20a AND H60=H60a AND session_bucket=ny_mid`
- Raw: n=90  W=79/L=11  WR=87.8%
- Refine: exclude BBP=BBP3 drops 5/11 losers (45%)
- **Final: n=76  W=70/L=6  WR=92.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=ny_mid  •  AVOID when middle of band

### W24.  `H20=H20a AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=90  W=79/L=11  WR=87.8%
- Refine: exclude BBP=BBP3 drops 5/11 losers (45%)
- **Final: n=76  W=70/L=6  WR=92.1%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; session=ny_mid  •  AVOID when middle of band

### W25.  `H20=H20a AND H60=H60a AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=90  W=79/L=11  WR=87.8%
- Refine: exclude BBP=BBP3 drops 5/11 losers (45%)
- **Final: n=76  W=70/L=6  WR=92.1%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=ny_mid  •  AVOID when middle of band

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=204  W=78/L=126  WR=38.2%
- Sharpen: sharpest is RSI=RSI1 (97/126 of losers there)
- **Sharp: n=135  W=38/L=97  WR=28.1%**
- **Dir: ?**  •  HTF20 strongly against; zscore -2 to -1 oversold; session=asia  •  ONLY when RSI 20-30 oversold

### L02.  `H20=H20e AND BBP=BBP2 AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=204  W=78/L=126  WR=38.2%
- Sharpen: sharpest is RSI=RSI1 (97/126 of losers there)
- **Sharp: n=135  W=38/L=97  WR=28.1%**
- **Dir: ?**  •  HTF20 strongly against; lower third; zscore -2 to -1 oversold; session=asia  •  ONLY when RSI 20-30 oversold

### L03.  `T1=T1a AND T4=T4a AND RSI=RSI3`
- Raw: n=186  W=73/L=113  WR=39.2%
- Sharpen: sharpest is session_bucket=asia (68/113 of losers there)
- **Sharp: n=99  W=31/L=68  WR=31.3%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when session=asia

### L04.  `T1=T1a AND T4=T4a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=186  W=73/L=113  WR=39.2%
- Sharpen: sharpest is session_bucket=asia (68/113 of losers there)
- **Sharp: n=99  W=31/L=68  WR=31.3%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when session=asia

### L05.  `H60=H60e AND T1=T1a AND T4=T4a AND RSI=RSI3`
- Raw: n=182  W=72/L=110  WR=39.6%
- Sharpen: sharpest is session_bucket=asia (68/110 of losers there)
- **Sharp: n=99  W=31/L=68  WR=31.3%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when session=asia

### L06.  `H20=H20e AND T1=T1c AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=180  W=72/L=108  WR=40.0%
- Sharpen: sharpest is RSI=RSI1 (81/108 of losers there)
- **Sharp: n=113  W=32/L=81  WR=28.3%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; zscore -2 to -1 oversold; session=asia  •  ONLY when RSI 20-30 oversold

### L07.  `H20=H20e AND ZS=ZS2 AND direction_exec=long AND session_bucket=asia`
- Raw: n=180  W=72/L=108  WR=40.0%
- Sharpen: sharpest is RSI=RSI1 (81/108 of losers there)
- **Sharp: n=113  W=32/L=81  WR=28.3%**
- **Dir: LONG**  •  HTF20 strongly against; zscore -2 to -1 oversold; session=asia  •  ONLY when RSI 20-30 oversold

### L08.  `H20=H20e AND T4=T4c AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=169  W=62/L=107  WR=36.7%
- Sharpen: sharpest is RSI=RSI1 (81/107 of losers there)
- **Sharp: n=113  W=32/L=81  WR=28.3%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; zscore -2 to -1 oversold; session=asia  •  ONLY when RSI 20-30 oversold

### L09.  `H20=H20e AND H60=H60a AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=168  W=61/L=107  WR=36.3%
- Sharpen: sharpest is RSI=RSI1 (81/107 of losers there)
- **Sharp: n=113  W=32/L=81  WR=28.3%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; zscore -2 to -1 oversold; session=asia  •  ONLY when RSI 20-30 oversold

### L10.  `H20=H20e AND BBP=BBP2 AND RSI=RSI1 AND session_bucket=asia`
- Raw: n=146  W=46/L=100  WR=31.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=146  W=46/L=100  WR=31.5%**
- **Dir: ?**  •  HTF20 strongly against; lower third; RSI 20-30 oversold; session=asia

### L11.  `H20=H20e AND T4=T4a AND session_bucket=asia`
- Raw: n=138  W=50/L=88  WR=36.2%
- Sharpen: sharpest is H60=H60e (87/88 of losers there)
- **Sharp: n=125  W=38/L=87  WR=30.4%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; session=asia  •  ONLY when HTF60 strongly against

### L12.  `H20=H20e AND RSI=RSI1 AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=135  W=38/L=97  WR=28.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=135  W=38/L=97  WR=28.1%**
- **Dir: ?**  •  HTF20 strongly against; RSI 20-30 oversold; zscore -2 to -1 oversold; session=asia

### L13.  `H60=H60a AND RSI=RSI1 AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=135  W=52/L=83  WR=38.5%
- Sharpen: sharpest is H20=H20e (81/83 of losers there)
- **Sharp: n=113  W=32/L=81  WR=28.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 20-30 oversold; zscore -2 to -1 oversold; session=asia  •  ONLY when HTF20 strongly against

### L14.  `T1=T1c AND RSI=RSI1 AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=135  W=52/L=83  WR=38.5%
- Sharpen: sharpest is H20=H20e (81/83 of losers there)
- **Sharp: n=113  W=32/L=81  WR=28.3%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 20-30 oversold; zscore -2 to -1 oversold; session=asia  •  ONLY when HTF20 strongly against

### L15.  `T4=T4c AND RSI=RSI1 AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=135  W=52/L=83  WR=38.5%
- Sharpen: sharpest is H20=H20e (81/83 of losers there)
- **Sharp: n=113  W=32/L=81  WR=28.3%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 20-30 oversold; zscore -2 to -1 oversold; session=asia  •  ONLY when HTF20 strongly against

### L16.  `RSI=RSI1 AND ZS=ZS2 AND direction_exec=long AND session_bucket=asia`
- Raw: n=135  W=52/L=83  WR=38.5%
- Sharpen: sharpest is H20=H20e (81/83 of losers there)
- **Sharp: n=113  W=32/L=81  WR=28.3%**
- **Dir: LONG**  •  RSI 20-30 oversold; zscore -2 to -1 oversold; session=asia  •  ONLY when HTF20 strongly against

### L17.  `H20=H20e AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=126  W=48/L=78  WR=38.1%
- Sharpen: sharpest is BBP=BBP1 (52/78 of losers there)
- **Sharp: n=72  W=20/L=52  WR=27.8%**
- **Dir: ?**  •  HTF20 strongly against; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when just touched lower band

### L18.  `H20=H20e AND H60=H60e AND session_bucket=asia`
- Raw: n=125  W=38/L=87  WR=30.4%
- Sharpen: sharpest is ZS=ZS5 (17/87 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L19.  `H20=H20e AND T1=T1a AND session_bucket=asia`
- Raw: n=125  W=38/L=87  WR=30.4%
- Sharpen: sharpest is ZS=ZS5 (17/87 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L20.  `H20=H20e AND direction_exec=short AND session_bucket=asia`
- Raw: n=125  W=38/L=87  WR=30.4%
- Sharpen: sharpest is ZS=ZS5 (17/87 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L21.  `H20=H20e AND H60=H60e AND T1=T1a AND session_bucket=asia`
- Raw: n=125  W=38/L=87  WR=30.4%
- Sharpen: sharpest is ZS=ZS5 (17/87 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend WITH trade; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L22.  `H20=H20e AND H60=H60e AND T4=T4a AND session_bucket=asia`
- Raw: n=125  W=38/L=87  WR=30.4%
- Sharpen: sharpest is ZS=ZS5 (17/87 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend WITH trade; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L23.  `H20=H20e AND H60=H60e AND direction_exec=short AND session_bucket=asia`
- Raw: n=125  W=38/L=87  WR=30.4%
- Sharpen: sharpest is ZS=ZS5 (17/87 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L24.  `H20=H20e AND T1=T1a AND T4=T4a AND session_bucket=asia`
- Raw: n=125  W=38/L=87  WR=30.4%
- Sharpen: sharpest is ZS=ZS5 (17/87 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend WITH trade; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L25.  `H20=H20e AND T1=T1a AND direction_exec=short AND session_bucket=asia`
- Raw: n=125  W=38/L=87  WR=30.4%
- Sharpen: sharpest is ZS=ZS5 (17/87 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend WITH trade; session=asia  •  ONLY when zscore +2 to +3 deep overbought

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(54/40) | H20e(40/54) |
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
