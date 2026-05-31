# EUR_USD — R25 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **3,053**  (W=1,904 / L=1,149)  -  WR: **62.4%**

## Session distribution

- ny_mid: n=1006  W=622/L=384  WR=61.8%
- ny_open: n=664  W=404/L=260  WR=60.8%
- ny_close: n=525  W=350/L=175  WR=66.7%
- asia: n=303  W=197/L=106  WR=65.0%
- london_open: n=302  W=184/L=118  WR=60.9%
- london: n=174  W=95/L=79  WR=54.6%
- off_hours: n=79  W=52/L=27  WR=65.8%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T4=T4c AND direction_exec=short AND session_bucket=london_open`
- Raw: n=155  W=135/L=20  WR=87.1%
- Refine: exclude BBP=BBP2 drops 14/20 losers (70%)
- **Final: n=125  W=119/L=6  WR=95.2%**
- **Dir: SHORT**  •  4h trend AGAINST trade; session=london_open  •  AVOID when lower third

### W02.  `H60=H60d AND T1=T1a AND session_bucket=ny_mid`
- Raw: n=143  W=127/L=16  WR=88.8%
- Refine: exclude BBP=BBP2 drops 15/16 losers (94%)
- **Final: n=118  W=117/L=1  WR=99.2%**
- **Dir: ?**  •  HTF60 mildly against; 1h trend WITH trade; session=ny_mid  •  AVOID when lower third

### W03.  `H20=H20e AND T1=T1a AND T4=T4c AND RSI=RSI3`
- Raw: n=135  W=115/L=20  WR=85.2%
- Refine: exclude session_bucket=ny_open drops 13/20 losers (65%)
- **Final: n=94  W=87/L=7  WR=92.6%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when session=ny_open

### W04.  `T1=T1a AND RSI=RSI3 AND ZS=ZS3`
- Raw: n=124  W=107/L=17  WR=86.3%
- Refine: exclude H60=H60a drops 14/17 losers (82%)
- **Final: n=70  W=67/L=3  WR=95.7%**
- **Dir: ?**  •  1h trend WITH trade; RSI 40-50 lower neutral; zscore -1 to +1 neutral  •  AVOID when HTF60 aligned WITH trade

### W05.  `T1=T1a AND RSI=RSI3 AND ZS=ZS3 AND direction_exec=short`
- Raw: n=104  W=91/L=13  WR=87.5%
- Refine: exclude H60=H60a drops 13/13 losers (100%)
- **Final: n=54  W=54/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 40-50 lower neutral; zscore -1 to +1 neutral  •  AVOID when HTF60 aligned WITH trade

### W06.  `H20=H20e AND T4=T4c AND session_bucket=london_open`
- Raw: n=102  W=92/L=10  WR=90.2%
- Refine: exclude BBP=BBP2 drops 9/10 losers (90%)
- **Final: n=79  W=78/L=1  WR=98.7%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; session=london_open  •  AVOID when lower third

### W07.  `H20=H20a AND T4=T4c AND ZS=ZS5`
- Raw: n=102  W=90/L=12  WR=88.2%
- Refine: exclude RSI=RSI4 drops 12/12 losers (100%)
- **Final: n=54  W=54/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  AVOID when RSI 50-60 upper neutral

### W08.  `T1=T1a AND T4=T4c AND RSI=RSI3 AND ZS=ZS3`
- Raw: n=99  W=86/L=13  WR=86.9%
- Refine: exclude H60=H60a drops 13/13 losers (100%)
- **Final: n=49  W=49/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral; zscore -1 to +1 neutral  •  AVOID when HTF60 aligned WITH trade

### W09.  `T4=T4a AND BBP=BBP0 AND direction_exec=long`
- Raw: n=95  W=89/L=6  WR=93.7%
- Refine: exclude session_bucket=ny_open drops 3/6 losers (50%)
- **Final: n=81  W=78/L=3  WR=96.3%**
- **Dir: LONG**  •  4h trend WITH trade; deep below lower band  •  AVOID when session=ny_open

### W10.  `T4=T4c AND ZS=ZS5 AND direction_exec=short`
- Raw: n=95  W=83/L=12  WR=87.4%
- Refine: exclude session_bucket=ny_mid drops 7/12 losers (58%)
- **Final: n=84  W=79/L=5  WR=94.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  AVOID when session=ny_mid

### W11.  `T4=T4a AND BBP=BBP4 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=95  W=83/L=12  WR=87.4%
- Refine: exclude H60=H60d drops 8/12 losers (67%)
- **Final: n=74  W=70/L=4  WR=94.6%**
- **Dir: SHORT**  •  4h trend WITH trade; upper third; RSI 50-60 upper neutral  •  AVOID when HTF60 mildly against

### W12.  `T1=T1c AND BBP=BBP0 AND direction_exec=long`
- Raw: n=95  W=81/L=14  WR=85.3%
- Refine: exclude T4=T4c drops 10/14 losers (71%)
- **Final: n=85  W=81/L=4  WR=95.3%**
- **Dir: LONG**  •  1h trend AGAINST trade; deep below lower band  •  AVOID when 4h trend AGAINST trade

### W13.  `H20=H20e AND T1=T1a AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=92  W=80/L=12  WR=87.0%
- Refine: exclude ZS=ZS2 drops 9/12 losers (75%)
- **Final: n=62  W=59/L=3  WR=95.2%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend WITH trade; session=ny_mid  •  AVOID when zscore -2 to -1 oversold

### W14.  `H20=H20e AND T4=T4a AND BBP=BBP0`
- Raw: n=91  W=85/L=6  WR=93.4%
- Refine: exclude session_bucket=ny_open drops 3/6 losers (50%)
- **Final: n=81  W=78/L=3  WR=96.3%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; deep below lower band  •  AVOID when session=ny_open

### W15.  `T1=T1c AND T4=T4a AND BBP=BBP0`
- Raw: n=89  W=85/L=4  WR=95.5%
- Refine: exclude session_bucket=asia drops 3/4 losers (75%)
- **Final: n=70  W=69/L=1  WR=98.6%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; deep below lower band  •  AVOID when session=asia

### W16.  `H60=H60e AND T1=T1c AND T4=T4a AND ZS=ZS1`
- Raw: n=89  W=76/L=13  WR=85.4%
- Refine: exclude RSI=RSI3 drops 11/13 losers (85%)
- **Final: n=36  W=34/L=2  WR=94.4%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  AVOID when RSI 40-50 lower neutral

### W17.  `H60=H60e AND T1=T1c AND ZS=ZS1 AND direction_exec=long`
- Raw: n=89  W=76/L=13  WR=85.4%
- Refine: exclude RSI=RSI3 drops 11/13 losers (85%)
- **Final: n=36  W=34/L=2  WR=94.4%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend AGAINST trade; zscore -3 to -2 deep oversold  •  AVOID when RSI 40-50 lower neutral

### W18.  `T4=T4a AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=88  W=83/L=5  WR=94.3%
- Refine: exclude H60=H60e drops 5/5 losers (100%)
- **Final: n=50  W=50/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend WITH trade; deep below lower band; zscore -3 to -2 deep oversold  •  AVOID when HTF60 strongly against

### W19.  `H20=H20e AND direction_exec=short AND session_bucket=london_open`
- Raw: n=88  W=79/L=9  WR=89.8%
- Refine: exclude BBP=BBP2 drops 9/9 losers (100%)
- **Final: n=67  W=67/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 strongly against; session=london_open  •  AVOID when lower third

### W20.  `H60=H60e AND T4=T4c AND session_bucket=london_open`
- Raw: n=88  W=79/L=9  WR=89.8%
- Refine: exclude BBP=BBP2 drops 9/9 losers (100%)
- **Final: n=67  W=67/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; session=london_open  •  AVOID when lower third

### W21.  `H60=H60e AND direction_exec=short AND session_bucket=london_open`
- Raw: n=88  W=79/L=9  WR=89.8%
- Refine: exclude BBP=BBP2 drops 9/9 losers (100%)
- **Final: n=67  W=67/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 strongly against; session=london_open  •  AVOID when lower third

### W22.  `H20=H20e AND H60=H60e AND T4=T4c AND session_bucket=london_open`
- Raw: n=88  W=79/L=9  WR=89.8%
- Refine: exclude BBP=BBP2 drops 9/9 losers (100%)
- **Final: n=67  W=67/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; session=london_open  •  AVOID when lower third

### W23.  `H20=H20e AND H60=H60e AND direction_exec=short AND session_bucket=london_open`
- Raw: n=88  W=79/L=9  WR=89.8%
- Refine: exclude BBP=BBP2 drops 9/9 losers (100%)
- **Final: n=67  W=67/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; session=london_open  •  AVOID when lower third

### W24.  `H20=H20e AND T4=T4c AND direction_exec=short AND session_bucket=london_open`
- Raw: n=88  W=79/L=9  WR=89.8%
- Refine: exclude BBP=BBP2 drops 9/9 losers (100%)
- **Final: n=67  W=67/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade; session=london_open  •  AVOID when lower third

### W25.  `H60=H60e AND T4=T4c AND direction_exec=short AND session_bucket=london_open`
- Raw: n=88  W=79/L=9  WR=89.8%
- Refine: exclude BBP=BBP2 drops 9/9 losers (100%)
- **Final: n=67  W=67/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend AGAINST trade; session=london_open  •  AVOID when lower third

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20a AND T1=T1c AND T4=T4a AND direction_exec=long`
- Raw: n=149  W=59/L=90  WR=39.6%
- Sharpen: sharpest is session_bucket=london_open (30/90 of losers there)
- **Sharp: n=31  W=1/L=30  WR=3.2%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when session=london_open

### L02.  `H60=H60a AND T1=T1c AND T4=T4a AND direction_exec=long`
- Raw: n=149  W=59/L=90  WR=39.6%
- Sharpen: sharpest is session_bucket=london_open (30/90 of losers there)
- **Sharp: n=31  W=1/L=30  WR=3.2%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when session=london_open

### L03.  `H20=H20a AND T1=T1c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=131  W=51/L=80  WR=38.9%
- Sharpen: sharpest is session_bucket=london_open (25/80 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when session=london_open

### L04.  `T4=T4a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=120  W=35/L=85  WR=29.2%
- Sharpen: sharpest is RSI=RSI3 (25/85 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: LONG**  •  4h trend WITH trade; session=london_open  •  ONLY when RSI 40-50 lower neutral

### L05.  `T1=T1c AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=112  W=37/L=75  WR=33.0%
- Sharpen: sharpest is H20=H20e (31/75 of losers there)
- **Sharp: n=33  W=2/L=31  WR=6.1%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 60-70 strong; session=ny_mid  •  ONLY when HTF20 strongly against

### L06.  `RSI=RSI5 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=112  W=37/L=75  WR=33.0%
- Sharpen: sharpest is H20=H20e (31/75 of losers there)
- **Sharp: n=33  W=2/L=31  WR=6.1%**
- **Dir: SHORT**  •  RSI 60-70 strong; session=ny_mid  •  ONLY when HTF20 strongly against

### L07.  `T1=T1c AND RSI=RSI5 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=112  W=37/L=75  WR=33.0%
- Sharpen: sharpest is H20=H20e (31/75 of losers there)
- **Sharp: n=33  W=2/L=31  WR=6.1%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 60-70 strong; session=ny_mid  •  ONLY when HTF20 strongly against

### L08.  `H20=H20a AND T1=T1c AND T4=T4a AND ZS=ZS3`
- Raw: n=107  W=42/L=65  WR=39.3%
- Sharpen: sharpest is RSI=RSI3 (25/65 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; zscore -1 to +1 neutral  •  ONLY when RSI 40-50 lower neutral

### L09.  `H20=H20a AND T1=T1c AND T4=T4a AND RSI=RSI3`
- Raw: n=105  W=33/L=72  WR=31.4%
- Sharpen: sharpest is session_bucket=london_open (37/72 of losers there)
- **Sharp: n=38  W=1/L=37  WR=2.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when session=london_open

### L10.  `H20=H20a AND ZS=ZS2 AND session_bucket=ny_mid`
- Raw: n=103  W=40/L=63  WR=38.8%
- Sharpen: sharpest is direction_exec=short (47/63 of losers there)
- **Sharp: n=60  W=13/L=47  WR=21.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; zscore -2 to -1 oversold; session=ny_mid  •  ONLY when short

### L11.  `H20=H20a AND BBP=BBP2 AND ZS=ZS2 AND session_bucket=ny_mid`
- Raw: n=103  W=40/L=63  WR=38.8%
- Sharpen: sharpest is direction_exec=short (47/63 of losers there)
- **Sharp: n=60  W=13/L=47  WR=21.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; lower third; zscore -2 to -1 oversold; session=ny_mid  •  ONLY when short

### L12.  `H60=H60b AND T1=T1c AND session_bucket=ny_mid`
- Raw: n=102  W=33/L=69  WR=32.4%
- Sharpen: sharpest is RSI=RSI5 (31/69 of losers there)
- **Sharp: n=33  W=2/L=31  WR=6.1%**
- **Dir: ?**  •  HTF60 slightly aligned; 1h trend AGAINST trade; session=ny_mid  •  ONLY when RSI 60-70 strong

### L13.  `H20=H20e AND T1=T1a AND T4=T4a AND RSI=RSI4`
- Raw: n=102  W=38/L=64  WR=37.3%
- Sharpen: sharpest is ZS=ZS3 (28/64 of losers there)
- **Sharp: n=35  W=7/L=28  WR=20.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when zscore -1 to +1 neutral

### L14.  `H60=H60a AND BBP=BBP4 AND RSI=RSI5`
- Raw: n=99  W=34/L=65  WR=34.3%
- Sharpen: sharpest is T4=T4c (24/65 of losers there)
- **Sharp: n=26  W=2/L=24  WR=7.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; upper third; RSI 60-70 strong  •  ONLY when 4h trend AGAINST trade

### L15.  `T4=T4a AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=99  W=37/L=62  WR=37.4%
- Sharpen: sharpest is RSI=RSI5 (24/62 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: ?**  •  4h trend WITH trade; just touched upper band; zscore +2 to +3 deep overbought  •  ONLY when RSI 60-70 strong

### L16.  `H20=H20a AND T4=T4a AND BBP=BBP3`
- Raw: n=94  W=33/L=61  WR=35.1%
- Sharpen: sharpest is direction_exec=long (35/61 of losers there)
- **Sharp: n=37  W=2/L=35  WR=5.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; middle of band  •  ONLY when long

### L17.  `H20=H20a AND T4=T4a AND BBP=BBP3 AND ZS=ZS3`
- Raw: n=94  W=33/L=61  WR=35.1%
- Sharpen: sharpest is direction_exec=long (35/61 of losers there)
- **Sharp: n=37  W=2/L=35  WR=5.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; middle of band; zscore -1 to +1 neutral  •  ONLY when long

### L18.  `T1=T1c AND T4=T4a AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=94  W=35/L=59  WR=37.2%
- Sharpen: sharpest is H20=H20e (31/59 of losers there)
- **Sharp: n=33  W=2/L=31  WR=6.1%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 60-70 strong; session=ny_mid  •  ONLY when HTF20 strongly against

### L19.  `T4=T4a AND RSI=RSI5 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=94  W=35/L=59  WR=37.2%
- Sharpen: sharpest is H20=H20e (31/59 of losers there)
- **Sharp: n=33  W=2/L=31  WR=6.1%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 60-70 strong; session=ny_mid  •  ONLY when HTF20 strongly against

### L20.  `H60=H60a AND T1=T1c AND BBP=BBP4 AND RSI=RSI5`
- Raw: n=93  W=34/L=59  WR=36.6%
- Sharpen: sharpest is T4=T4c (18/59 of losers there)
- **Sharp: n=20  W=2/L=18  WR=10.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; upper third; RSI 60-70 strong  •  ONLY when 4h trend AGAINST trade

### L21.  `H60=H60a AND BBP=BBP4 AND RSI=RSI5 AND direction_exec=short`
- Raw: n=93  W=34/L=59  WR=36.6%
- Sharpen: sharpest is T4=T4c (18/59 of losers there)
- **Sharp: n=20  W=2/L=18  WR=10.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; upper third; RSI 60-70 strong  •  ONLY when 4h trend AGAINST trade

### L22.  `H60=H60a AND RSI=RSI5 AND ZS=ZS4`
- Raw: n=92  W=30/L=62  WR=32.6%
- Sharpen: sharpest is T4=T4c (24/62 of losers there)
- **Sharp: n=26  W=2/L=24  WR=7.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 60-70 strong; zscore +1 to +2 overbought  •  ONLY when 4h trend AGAINST trade

### L23.  `H60=H60a AND BBP=BBP4 AND RSI=RSI5 AND ZS=ZS4`
- Raw: n=92  W=30/L=62  WR=32.6%
- Sharpen: sharpest is T4=T4c (24/62 of losers there)
- **Sharp: n=26  W=2/L=24  WR=7.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; upper third; RSI 60-70 strong; zscore +1 to +2 overbought  •  ONLY when 4h trend AGAINST trade

### L24.  `H60=H60a AND T1=T1c AND T4=T4a AND RSI=RSI3`
- Raw: n=92  W=32/L=60  WR=34.8%
- Sharpen: sharpest is session_bucket=london_open (25/60 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when session=london_open

### L25.  `H60=H60a AND T1=T1c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=92  W=32/L=60  WR=34.8%
- Sharpen: sharpest is session_bucket=london_open (25/60 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when session=london_open

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | H60d(11/5), H60e(42/37) | H60a(38/45) |
| T1 | T1a(54/47) | T1c(46/53) |
| T4 | T4c(54/46) | T4a(46/54) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(54/47) | long(46/53) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
