# GBP_USD — R35 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **4,836**  (W=3,046 / L=1,790)  -  WR: **63.0%**

## Session distribution

- asia: n=1285  W=828/L=457  WR=64.4%
- ny_mid: n=1080  W=657/L=423  WR=60.8%
- ny_close: n=895  W=556/L=339  WR=62.1%
- london_open: n=506  W=328/L=178  WR=64.8%
- london: n=381  W=249/L=132  WR=65.4%
- ny_open: n=327  W=207/L=120  WR=63.3%
- asia_late: n=270  W=161/L=109  WR=59.6%
- off_hours: n=92  W=60/L=32  WR=65.2%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND H60=H60a AND T1=T1a AND session_bucket=asia`
- Raw: n=181  W=156/L=25  WR=86.2%
- Refine: no further refinement
- **Final: n=181  W=156/L=25  WR=86.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; session=asia

### W02.  `H20=H20a AND H60=H60a AND direction_exec=short AND session_bucket=asia`
- Raw: n=181  W=156/L=25  WR=86.2%
- Refine: no further refinement
- **Final: n=181  W=156/L=25  WR=86.2%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=asia

### W03.  `H60=H60a AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=148  W=132/L=16  WR=89.2%
- Refine: exclude T4=T4a drops 13/16 losers (81%)
- **Final: n=68  W=65/L=3  WR=95.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; zscore -3 to -2 deep oversold; session=asia  •  AVOID when 4h trend WITH trade

### W04.  `H60=H60a AND RSI=RSI2 AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=138  W=126/L=12  WR=91.3%
- Refine: exclude T4=T4a drops 9/12 losers (75%)
- **Final: n=68  W=65/L=3  WR=95.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 30-40 weak; zscore -3 to -2 deep oversold; session=asia  •  AVOID when 4h trend WITH trade

### W05.  `H20=H20a AND H60=H60a AND BBP=BBP0 AND RSI=RSI2`
- Raw: n=129  W=111/L=18  WR=86.0%
- Refine: exclude session_bucket=london drops 7/18 losers (39%)
- **Final: n=112  W=101/L=11  WR=90.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; deep below lower band; RSI 30-40 weak  •  AVOID when session=london

### W06.  `T4=T4c AND RSI=RSI3 AND session_bucket=ny_open`
- Raw: n=119  W=103/L=16  WR=86.6%
- Refine: exclude direction_exec=short drops 15/16 losers (94%)
- **Final: n=51  W=50/L=1  WR=98.0%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; session=ny_open  •  AVOID when short

### W07.  `H20=H20a AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=117  W=105/L=12  WR=89.7%
- Refine: exclude H60=H60e drops 3/12 losers (25%)
- **Final: n=112  W=103/L=9  WR=92.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; zscore -3 to -2 deep oversold; session=asia  •  AVOID when HTF60 strongly against

### W08.  `H20=H20a AND RSI=RSI2 AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=117  W=105/L=12  WR=89.7%
- Refine: exclude H60=H60e drops 3/12 losers (25%)
- **Final: n=112  W=103/L=9  WR=92.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 30-40 weak; zscore -3 to -2 deep oversold; session=asia  •  AVOID when HTF60 strongly against

### W09.  `H20=H20a AND ZS=ZS1 AND session_bucket=ny_close`
- Raw: n=115  W=105/L=10  WR=91.3%
- Refine: exclude BBP=BBP0 drops 9/10 losers (90%)
- **Final: n=69  W=68/L=1  WR=98.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; zscore -3 to -2 deep oversold; session=ny_close  •  AVOID when deep below lower band

### W10.  `H20=H20a AND H60=H60a AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=106  W=97/L=9  WR=91.5%
- Refine: no further refinement
- **Final: n=106  W=97/L=9  WR=91.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; zscore -3 to -2 deep oversold; session=asia

### W11.  `H20=H20a AND T4=T4c AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=99  W=85/L=14  WR=85.9%
- Refine: exclude ZS=ZS3 drops 4/14 losers (29%)
- **Final: n=85  W=75/L=10  WR=88.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 30-40 weak; session=asia  •  AVOID when zscore -1 to +1 neutral

### W12.  `H60=H60a AND T1=T1a AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=94  W=81/L=13  WR=86.2%
- Refine: exclude T4=T4a drops 13/13 losers (100%)
- **Final: n=24  W=24/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; zscore -3 to -2 deep oversold; session=asia  •  AVOID when 4h trend WITH trade

### W13.  `H60=H60a AND ZS=ZS1 AND direction_exec=short AND session_bucket=asia`
- Raw: n=94  W=81/L=13  WR=86.2%
- Refine: exclude T4=T4a drops 13/13 losers (100%)
- **Final: n=24  W=24/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; zscore -3 to -2 deep oversold; session=asia  •  AVOID when 4h trend WITH trade

### W14.  `H20=H20a AND RSI=RSI3 AND ZS=ZS3 AND direction_exec=long`
- Raw: n=90  W=78/L=12  WR=86.7%
- Refine: exclude H60=H60e drops 6/12 losers (50%)
- **Final: n=65  W=59/L=6  WR=90.8%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 40-50 lower neutral; zscore -1 to +1 neutral  •  AVOID when HTF60 strongly against

### W15.  `H20=H20a AND RSI=RSI2 AND ZS=ZS1 AND session_bucket=ny_close`
- Raw: n=89  W=81/L=8  WR=91.0%
- Refine: exclude BBP=BBP0 drops 7/8 losers (88%)
- **Final: n=49  W=48/L=1  WR=98.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 30-40 weak; zscore -3 to -2 deep oversold; session=ny_close  •  AVOID when deep below lower band

### W16.  `H60=H60e AND T4=T4c AND BBP=BBP2 AND session_bucket=ny_mid`
- Raw: n=88  W=75/L=13  WR=85.2%
- Refine: exclude RSI=RSI2 drops 11/13 losers (85%)
- **Final: n=38  W=36/L=2  WR=94.7%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; lower third; session=ny_mid  •  AVOID when RSI 30-40 weak

### W17.  `H60=H60a AND BBP=BBP0 AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=87  W=80/L=7  WR=92.0%
- Refine: exclude T4=T4a drops 7/7 losers (100%)
- **Final: n=44  W=44/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; deep below lower band; zscore -3 to -2 deep oversold; session=asia  •  AVOID when 4h trend WITH trade

### W18.  `H20=H20a AND T4=T4c AND ZS=ZS1 AND session_bucket=ny_close`
- Raw: n=86  W=78/L=8  WR=90.7%
- Refine: exclude BBP=BBP0 drops 8/8 losers (100%)
- **Final: n=50  W=50/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold; session=ny_close  •  AVOID when deep below lower band

### W19.  `H60=H60a AND BBP=BBP0 AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=84  W=80/L=4  WR=95.2%
- Refine: exclude T4=T4a drops 4/4 losers (100%)
- **Final: n=50  W=50/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; deep below lower band; RSI 30-40 weak; session=asia  •  AVOID when 4h trend WITH trade

### W20.  `H60=H60a AND T1=T1a AND session_bucket=london_open`
- Raw: n=83  W=71/L=12  WR=85.5%
- Refine: exclude H20=H20b drops 11/12 losers (92%)
- **Final: n=47  W=46/L=1  WR=97.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=london_open  •  AVOID when HTF20 slightly aligned

### W21.  `H60=H60a AND direction_exec=short AND session_bucket=london_open`
- Raw: n=83  W=71/L=12  WR=85.5%
- Refine: exclude H20=H20b drops 11/12 losers (92%)
- **Final: n=47  W=46/L=1  WR=97.9%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; session=london_open  •  AVOID when HTF20 slightly aligned

### W22.  `H60=H60a AND T1=T1a AND direction_exec=short AND session_bucket=london_open`
- Raw: n=83  W=71/L=12  WR=85.5%
- Refine: exclude H20=H20b drops 11/12 losers (92%)
- **Final: n=47  W=46/L=1  WR=97.9%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=london_open  •  AVOID when HTF20 slightly aligned

### W23.  `T4=T4c AND RSI=RSI3 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=82  W=70/L=12  WR=85.4%
- Refine: exclude BBP=BBP4 drops 8/12 losers (67%)
- **Final: n=67  W=63/L=4  WR=94.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; session=ny_mid  •  AVOID when upper third

### W24.  `H20=H20e AND RSI=RSI3 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=80  W=74/L=6  WR=92.5%
- Refine: exclude BBP=BBP4 drops 3/6 losers (50%)
- **Final: n=71  W=68/L=3  WR=95.8%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 40-50 lower neutral; session=ny_mid  •  AVOID when upper third

### W25.  `H20=H20a AND T1=T1a AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=75  W=66/L=9  WR=88.0%
- Refine: exclude H60=H60e drops 3/9 losers (33%)
- **Final: n=72  W=66/L=6  WR=91.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; zscore -3 to -2 deep oversold; session=asia  •  AVOID when HTF60 strongly against

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND H60=H60e AND T1=T1c AND RSI=RSI2`
- Raw: n=283  W=110/L=173  WR=38.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=283  W=110/L=173  WR=38.9%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; RSI 30-40 weak

### L02.  `H20=H20e AND H60=H60e AND RSI=RSI2 AND direction_exec=long`
- Raw: n=278  W=110/L=168  WR=39.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=278  W=110/L=168  WR=39.6%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 strongly against; RSI 30-40 weak

### L03.  `H20=H20e AND BBP=BBP2 AND session_bucket=asia`
- Raw: n=203  W=81/L=122  WR=39.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=203  W=81/L=122  WR=39.9%**
- **Dir: ?**  •  HTF20 strongly against; lower third; session=asia

### L04.  `H20=H20e AND BBP=BBP2 AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=164  W=64/L=100  WR=39.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=164  W=64/L=100  WR=39.0%**
- **Dir: ?**  •  HTF20 strongly against; lower third; RSI 30-40 weak; session=asia

### L05.  `H20=H20e AND T1=T1c AND T4=T4a AND RSI=RSI2`
- Raw: n=150  W=50/L=100  WR=33.3%
- Sharpen: sharpest is BBP=BBP1 (23/100 of losers there)
- **Sharp: n=27  W=4/L=23  WR=14.8%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend WITH trade; RSI 30-40 weak  •  ONLY when just touched lower band

### L06.  `H20=H20e AND T4=T4c AND BBP=BBP2 AND session_bucket=asia`
- Raw: n=148  W=58/L=90  WR=39.2%
- Sharpen: no sharper sub-pattern
- **Sharp: n=148  W=58/L=90  WR=39.2%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; lower third; session=asia

### L07.  `H20=H20e AND RSI=RSI2 AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=146  W=57/L=89  WR=39.0%
- Sharpen: sharpest is T1=T1a (55/89 of losers there)
- **Sharp: n=81  W=26/L=55  WR=32.1%**
- **Dir: ?**  •  HTF20 strongly against; RSI 30-40 weak; zscore -2 to -1 oversold; session=asia  •  ONLY when 1h trend WITH trade

### L08.  `H20=H20e AND T4=T4a AND RSI=RSI2 AND direction_exec=long`
- Raw: n=145  W=50/L=95  WR=34.5%
- Sharpen: sharpest is BBP=BBP1 (23/95 of losers there)
- **Sharp: n=27  W=4/L=23  WR=14.8%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend WITH trade; RSI 30-40 weak  •  ONLY when just touched lower band

### L09.  `H20=H20e AND H60=H60e AND T1=T1c AND session_bucket=asia`
- Raw: n=133  W=50/L=83  WR=37.6%
- Sharpen: sharpest is BBP=BBP0 (23/83 of losers there)
- **Sharp: n=29  W=6/L=23  WR=20.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; session=asia  •  ONLY when deep below lower band

### L10.  `H20=H20e AND H60=H60e AND direction_exec=long AND session_bucket=asia`
- Raw: n=133  W=50/L=83  WR=37.6%
- Sharpen: sharpest is BBP=BBP0 (23/83 of losers there)
- **Sharp: n=29  W=6/L=23  WR=20.7%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 strongly against; session=asia  •  ONLY when deep below lower band

### L11.  `T1=T1c AND T4=T4a AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=126  W=42/L=84  WR=33.3%
- Sharpen: sharpest is session_bucket=ny_mid (22/84 of losers there)
- **Sharp: n=23  W=1/L=22  WR=4.3%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; lower third; RSI 40-50 lower neutral  •  ONLY when session=ny_mid

### L12.  `H20=H20a AND T4=T4a AND BBP=BBP2 AND session_bucket=ny_mid`
- Raw: n=116  W=46/L=70  WR=39.7%
- Sharpen: sharpest is RSI=RSI3 (35/70 of losers there)
- **Sharp: n=42  W=7/L=35  WR=16.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; lower third; session=ny_mid  •  ONLY when RSI 40-50 lower neutral

### L13.  `H60=H60e AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=114  W=38/L=76  WR=33.3%
- Sharpen: sharpest is BBP=BBP0 (44/76 of losers there)
- **Sharp: n=58  W=14/L=44  WR=24.1%**
- **Dir: ?**  •  HTF60 strongly against; zscore -3 to -2 deep oversold; session=asia  •  ONLY when deep below lower band

### L14.  `T1=T1c AND T4=T4a AND BBP=BBP2 AND session_bucket=ny_mid`
- Raw: n=110  W=44/L=66  WR=40.0%
- Sharpen: sharpest is RSI=RSI3 (22/66 of losers there)
- **Sharp: n=23  W=1/L=22  WR=4.3%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; lower third; session=ny_mid  •  ONLY when RSI 40-50 lower neutral

### L15.  `T1=T1c AND T4=T4a AND RSI=RSI2 AND session_bucket=ny_close`
- Raw: n=108  W=40/L=68  WR=37.0%
- Sharpen: sharpest is H20=H20e (40/68 of losers there)
- **Sharp: n=54  W=14/L=40  WR=25.9%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 30-40 weak; session=ny_close  •  ONLY when HTF20 strongly against

### L16.  `T4=T4a AND RSI=RSI2 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=108  W=40/L=68  WR=37.0%
- Sharpen: sharpest is H20=H20e (40/68 of losers there)
- **Sharp: n=54  W=14/L=40  WR=25.9%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 30-40 weak; session=ny_close  •  ONLY when HTF20 strongly against

### L17.  `H60=H60e AND RSI=RSI2 AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=103  W=30/L=73  WR=29.1%
- Sharpen: sharpest is BBP=BBP0 (41/73 of losers there)
- **Sharp: n=47  W=6/L=41  WR=12.8%**
- **Dir: ?**  •  HTF60 strongly against; RSI 30-40 weak; zscore -3 to -2 deep oversold; session=asia  •  ONLY when deep below lower band

### L18.  `RSI=RSI3 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=103  W=35/L=68  WR=34.0%
- Sharpen: sharpest is H20=H20a (50/68 of losers there)
- **Sharp: n=67  W=17/L=50  WR=25.4%**
- **Dir: SHORT**  •  RSI 40-50 lower neutral; session=ny_mid  •  ONLY when HTF20 aligned WITH trade

### L19.  `T1=T1c AND T4=T4a AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=103  W=37/L=66  WR=35.9%
- Sharpen: sharpest is direction_exec=short (15/66 of losers there)
- **Sharp: n=16  W=1/L=15  WR=6.2%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  ONLY when short

### L20.  `H60=H60a AND T4=T4a AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=100  W=35/L=65  WR=35.0%
- Sharpen: sharpest is session_bucket=ny_mid (29/65 of losers there)
- **Sharp: n=34  W=5/L=29  WR=14.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; lower third; RSI 40-50 lower neutral  •  ONLY when session=ny_mid

### L21.  `H60=H60e AND T4=T4a AND RSI=RSI2 AND session_bucket=ny_close`
- Raw: n=100  W=37/L=63  WR=37.0%
- Sharpen: sharpest is BBP=BBP2 (22/63 of losers there)
- **Sharp: n=23  W=1/L=22  WR=4.3%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; RSI 30-40 weak; session=ny_close  •  ONLY when lower third

### L22.  `H20=H20e AND ZS=ZS1 AND session_bucket=ny_close`
- Raw: n=99  W=33/L=66  WR=33.3%
- Sharpen: sharpest is RSI=RSI2 (54/66 of losers there)
- **Sharp: n=69  W=15/L=54  WR=21.7%**
- **Dir: ?**  •  HTF20 strongly against; zscore -3 to -2 deep oversold; session=ny_close  •  ONLY when RSI 30-40 weak

### L23.  `H20=H20a AND RSI=RSI3 AND session_bucket=ny_mid`
- Raw: n=99  W=37/L=62  WR=37.4%
- Sharpen: sharpest is BBP=BBP2 (35/62 of losers there)
- **Sharp: n=42  W=7/L=35  WR=16.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 40-50 lower neutral; session=ny_mid  •  ONLY when lower third

### L24.  `H20=H20e AND T1=T1a AND BBP=BBP2 AND session_bucket=asia`
- Raw: n=98  W=38/L=60  WR=38.8%
- Sharpen: sharpest is RSI=RSI2 (60/60 of losers there)
- **Sharp: n=92  W=32/L=60  WR=34.8%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; lower third; session=asia  •  ONLY when RSI 30-40 weak

### L25.  `H20=H20e AND BBP=BBP2 AND direction_exec=short AND session_bucket=asia`
- Raw: n=98  W=38/L=60  WR=38.8%
- Sharpen: sharpest is RSI=RSI2 (60/60 of losers there)
- **Sharp: n=92  W=32/L=60  WR=34.8%**
- **Dir: SHORT**  •  HTF20 strongly against; lower third; session=asia  •  ONLY when RSI 30-40 weak

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(47/41) | — |
| H60 | H60a(44/37) | H60e(37/45) |
| T1 | T1a(53/46) | T1c(47/54) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
