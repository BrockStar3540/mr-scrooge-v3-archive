# NZD_CAD — R23 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **1,987**  (W=1,251 / L=736)  -  WR: **63.0%**

## Session distribution

- ny_mid: n=516  W=326/L=190  WR=63.2%
- ny_close: n=496  W=304/L=192  WR=61.3%
- asia: n=341  W=214/L=127  WR=62.8%
- ny_open: n=222  W=139/L=83  WR=62.6%
- london_open: n=206  W=134/L=72  WR=65.0%
- london: n=112  W=70/L=42  WR=62.5%
- off_hours: n=74  W=51/L=23  WR=68.9%
- asia_late: n=20  W=13/L=7  WR=65.0%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1a AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=211  W=185/L=26  WR=87.7%
- Refine: exclude H20=H20a drops 18/26 losers (69%)
- **Final: n=129  W=121/L=8  WR=93.8%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

### W02.  `T1=T1a AND T4=T4c AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=153  W=137/L=16  WR=89.5%
- Refine: exclude H20=H20a drops 8/16 losers (50%)
- **Final: n=129  W=121/L=8  WR=93.8%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend AGAINST trade; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

### W03.  `H20=H20e AND T1=T1a AND session_bucket=ny_mid`
- Raw: n=129  W=121/L=8  WR=93.8%
- Refine: exclude ZS=ZS4 drops 8/8 losers (100%)
- **Final: n=74  W=74/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; session=ny_mid  •  AVOID when zscore +1 to +2 overbought

### W04.  `H20=H20e AND T1=T1a AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=129  W=121/L=8  WR=93.8%
- Refine: exclude ZS=ZS4 drops 8/8 losers (100%)
- **Final: n=74  W=74/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; session=ny_mid  •  AVOID when zscore +1 to +2 overbought

### W05.  `H20=H20e AND T1=T1a AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=129  W=121/L=8  WR=93.8%
- Refine: exclude ZS=ZS4 drops 8/8 losers (100%)
- **Final: n=74  W=74/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend WITH trade; session=ny_mid  •  AVOID when zscore +1 to +2 overbought

### W06.  `T1=T1a AND T4=T4c AND RSI=RSI5`
- Raw: n=120  W=105/L=15  WR=87.5%
- Refine: exclude H60=H60e drops 4/15 losers (27%)
- **Final: n=113  W=102/L=11  WR=90.3%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when HTF60 strongly against

### W07.  `H20=H20e AND T1=T1a AND T4=T4c AND RSI=RSI5`
- Raw: n=120  W=105/L=15  WR=87.5%
- Refine: exclude H60=H60e drops 4/15 losers (27%)
- **Final: n=113  W=102/L=11  WR=90.3%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when HTF60 strongly against

### W08.  `H60=H60a AND T1=T1a AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=115  W=99/L=16  WR=86.1%
- Refine: exclude H20=H20a drops 8/16 losers (50%)
- **Final: n=91  W=83/L=8  WR=91.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

### W09.  `T4=T4c AND RSI=RSI5 AND direction_exec=long`
- Raw: n=113  W=102/L=11  WR=90.3%
- Refine: exclude ZS=ZS3 drops 5/11 losers (45%)
- **Final: n=89  W=83/L=6  WR=93.3%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when zscore -1 to +1 neutral

### W10.  `H20=H20e AND T4=T4c AND RSI=RSI5 AND direction_exec=long`
- Raw: n=113  W=102/L=11  WR=90.3%
- Refine: exclude ZS=ZS3 drops 5/11 losers (45%)
- **Final: n=89  W=83/L=6  WR=93.3%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when zscore -1 to +1 neutral

### W11.  `T1=T1a AND T4=T4c AND RSI=RSI5 AND direction_exec=long`
- Raw: n=113  W=102/L=11  WR=90.3%
- Refine: exclude ZS=ZS3 drops 5/11 losers (45%)
- **Final: n=89  W=83/L=6  WR=93.3%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when zscore -1 to +1 neutral

### W12.  `H60=H60a AND T1=T1a AND T4=T4c AND RSI=RSI5`
- Raw: n=109  W=98/L=11  WR=89.9%
- Refine: exclude ZS=ZS3 drops 5/11 losers (45%)
- **Final: n=89  W=83/L=6  WR=93.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when zscore -1 to +1 neutral

### W13.  `H60=H60a AND T4=T4c AND RSI=RSI5 AND direction_exec=long`
- Raw: n=109  W=98/L=11  WR=89.9%
- Refine: exclude ZS=ZS3 drops 5/11 losers (45%)
- **Final: n=89  W=83/L=6  WR=93.3%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when zscore -1 to +1 neutral

### W14.  `H20=H20e AND H60=H60a AND BBP=BBP3`
- Raw: n=106  W=91/L=15  WR=85.8%
- Refine: exclude T4=T4a drops 9/15 losers (60%)
- **Final: n=66  W=60/L=6  WR=90.9%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; middle of band  •  AVOID when 4h trend WITH trade

### W15.  `H20=H20e AND H60=H60a AND BBP=BBP3 AND ZS=ZS3`
- Raw: n=106  W=91/L=15  WR=85.8%
- Refine: exclude T4=T4a drops 9/15 losers (60%)
- **Final: n=66  W=60/L=6  WR=90.9%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; middle of band; zscore -1 to +1 neutral  •  AVOID when 4h trend WITH trade

### W16.  `H20=H20e AND H60=H60a AND session_bucket=ny_open`
- Raw: n=105  W=90/L=15  WR=85.7%
- Refine: exclude ZS=ZS4 drops 13/15 losers (87%)
- **Final: n=83  W=81/L=2  WR=97.6%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; session=ny_open  •  AVOID when zscore +1 to +2 overbought

### W17.  `H20=H20e AND H60=H60a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=105  W=90/L=15  WR=85.7%
- Refine: exclude ZS=ZS4 drops 13/15 losers (87%)
- **Final: n=83  W=81/L=2  WR=97.6%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 aligned WITH trade; session=ny_open  •  AVOID when zscore +1 to +2 overbought

### W18.  `H20=H20e AND H60=H60a AND T4=T4c AND ZS=ZS3`
- Raw: n=98  W=86/L=12  WR=87.8%
- Refine: exclude direction_exec=long drops 12/12 losers (100%)
- **Final: n=40  W=40/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 4h trend AGAINST trade; zscore -1 to +1 neutral  •  AVOID when long

### W19.  `H20=H20e AND T4=T4c AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=96  W=83/L=13  WR=86.5%
- Refine: exclude ZS=ZS1 drops 6/13 losers (46%)
- **Final: n=90  W=83/L=7  WR=92.2%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 50-60 upper neutral; session=ny_mid  •  AVOID when zscore -3 to -2 deep oversold

### W20.  `H20=H20e AND T1=T1c AND ZS=ZS3 AND direction_exec=short`
- Raw: n=94  W=80/L=14  WR=85.1%
- Refine: exclude H60=H60e drops 14/14 losers (100%)
- **Final: n=40  W=40/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; zscore -1 to +1 neutral  •  AVOID when HTF60 strongly against

### W21.  `T4=T4c AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=91  W=86/L=5  WR=94.5%
- Refine: exclude session_bucket=asia drops 3/5 losers (60%)
- **Final: n=77  W=75/L=2  WR=97.4%**
- **Dir: ?**  •  4h trend AGAINST trade; deep above upper band; zscore +2 to +3 deep overbought  •  AVOID when session=asia

### W22.  `H20=H20e AND H60=H60a AND T1=T1a AND session_bucket=ny_mid`
- Raw: n=91  W=83/L=8  WR=91.2%
- Refine: exclude ZS=ZS4 drops 8/8 losers (100%)
- **Final: n=42  W=42/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend WITH trade; session=ny_mid  •  AVOID when zscore +1 to +2 overbought

### W23.  `T1=T1a AND ZS=ZS2 AND direction_exec=long`
- Raw: n=89  W=76/L=13  WR=85.4%
- Refine: exclude session_bucket=ny_close drops 6/13 losers (46%)
- **Final: n=75  W=68/L=7  WR=90.7%**
- **Dir: LONG**  •  1h trend WITH trade; zscore -2 to -1 oversold  •  AVOID when session=ny_close

### W24.  `T1=T1a AND BBP=BBP2 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=89  W=76/L=13  WR=85.4%
- Refine: exclude session_bucket=ny_close drops 6/13 losers (46%)
- **Final: n=75  W=68/L=7  WR=90.7%**
- **Dir: LONG**  •  1h trend WITH trade; lower third; zscore -2 to -1 oversold  •  AVOID when session=ny_close

### W25.  `H60=H60a AND BBP=BBP4 AND RSI=RSI5`
- Raw: n=85  W=77/L=8  WR=90.6%
- Refine: exclude session_bucket=ny_mid drops 6/8 losers (75%)
- **Final: n=48  W=46/L=2  WR=95.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; upper third; RSI 60-70 strong  •  AVOID when session=ny_mid

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1c AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=163  W=48/L=115  WR=29.4%
- Sharpen: sharpest is H20=H20a (78/115 of losers there)
- **Sharp: n=93  W=15/L=78  WR=16.1%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; session=ny_mid  •  ONLY when HTF20 aligned WITH trade

### L02.  `T1=T1c AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=161  W=64/L=97  WR=39.8%
- Sharpen: sharpest is H20=H20a (78/97 of losers there)
- **Sharp: n=93  W=15/L=78  WR=16.1%**
- **Dir: SHORT**  •  1h trend AGAINST trade; session=ny_mid  •  ONLY when HTF20 aligned WITH trade

### L03.  `H20=H20a AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=157  W=57/L=100  WR=36.3%
- Sharpen: sharpest is T1=T1c (78/100 of losers there)
- **Sharp: n=93  W=15/L=78  WR=16.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=ny_mid  •  ONLY when 1h trend AGAINST trade

### L04.  `T4=T4a AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=141  W=48/L=93  WR=34.0%
- Sharpen: sharpest is T1=T1c (86/93 of losers there)
- **Sharp: n=113  W=27/L=86  WR=23.9%**
- **Dir: SHORT**  •  4h trend WITH trade; session=ny_mid  •  ONLY when 1h trend AGAINST trade

### L05.  `H20=H20a AND T4=T4a AND RSI=RSI5`
- Raw: n=126  W=38/L=88  WR=30.2%
- Sharpen: sharpest is T1=T1c (69/88 of losers there)
- **Sharp: n=85  W=16/L=69  WR=18.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when 1h trend AGAINST trade

### L06.  `H20=H20a AND T4=T4a AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=121  W=36/L=85  WR=29.8%
- Sharpen: sharpest is T1=T1c (78/85 of losers there)
- **Sharp: n=93  W=15/L=78  WR=16.1%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=ny_mid  •  ONLY when 1h trend AGAINST trade

### L07.  `H60=H60e AND T4=T4a AND RSI=RSI5`
- Raw: n=116  W=36/L=80  WR=31.0%
- Sharpen: sharpest is T1=T1c (61/80 of losers there)
- **Sharp: n=75  W=14/L=61  WR=18.7%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when 1h trend AGAINST trade

### L08.  `H20=H20a AND H60=H60e AND T4=T4a AND RSI=RSI5`
- Raw: n=116  W=36/L=80  WR=31.0%
- Sharpen: sharpest is T1=T1c (61/80 of losers there)
- **Sharp: n=75  W=14/L=61  WR=18.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when 1h trend AGAINST trade

### L09.  `T1=T1c AND T4=T4a AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=113  W=27/L=86  WR=23.9%
- Sharpen: sharpest is H20=H20a (78/86 of losers there)
- **Sharp: n=93  W=15/L=78  WR=16.1%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend WITH trade; session=ny_mid  •  ONLY when HTF20 aligned WITH trade

### L10.  `H20=H20a AND T1=T1c AND RSI=RSI5`
- Raw: n=109  W=40/L=69  WR=36.7%
- Sharpen: sharpest is T4=T4a (69/69 of losers there)
- **Sharp: n=85  W=16/L=69  WR=18.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when 4h trend WITH trade

### L11.  `H60=H60e AND RSI=RSI5 AND direction_exec=short`
- Raw: n=106  W=41/L=65  WR=38.7%
- Sharpen: sharpest is T4=T4a (61/65 of losers there)
- **Sharp: n=75  W=14/L=61  WR=18.7%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 60-70 strong  •  ONLY when 4h trend WITH trade

### L12.  `H20=H20a AND RSI=RSI5 AND direction_exec=short`
- Raw: n=101  W=38/L=63  WR=37.6%
- Sharpen: sharpest is T4=T4a (63/63 of losers there)
- **Sharp: n=77  W=14/L=63  WR=18.2%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 60-70 strong  •  ONLY when 4h trend WITH trade

### L13.  `H20=H20a AND T1=T1c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=101  W=38/L=63  WR=37.6%
- Sharpen: sharpest is T4=T4a (63/63 of losers there)
- **Sharp: n=77  W=14/L=63  WR=18.2%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when 4h trend WITH trade

### L14.  `H60=H60e AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=99  W=34/L=65  WR=34.3%
- Sharpen: sharpest is RSI=RSI5 (42/65 of losers there)
- **Sharp: n=50  W=8/L=42  WR=16.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; session=ny_mid  •  ONLY when RSI 60-70 strong

### L15.  `H60=H60e AND T4=T4a AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=99  W=34/L=65  WR=34.3%
- Sharpen: sharpest is RSI=RSI5 (42/65 of losers there)
- **Sharp: n=50  W=8/L=42  WR=16.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend WITH trade; session=ny_mid  •  ONLY when RSI 60-70 strong

### L16.  `H60=H60e AND T1=T1c AND RSI=RSI5`
- Raw: n=99  W=38/L=61  WR=38.4%
- Sharpen: sharpest is T4=T4a (61/61 of losers there)
- **Sharp: n=75  W=14/L=61  WR=18.7%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when 4h trend WITH trade

### L17.  `H20=H20a AND H60=H60e AND T1=T1c AND RSI=RSI5`
- Raw: n=99  W=38/L=61  WR=38.4%
- Sharpen: sharpest is T4=T4a (61/61 of losers there)
- **Sharp: n=75  W=14/L=61  WR=18.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when 4h trend WITH trade

### L18.  `H20=H20a AND H60=H60e AND RSI=RSI5 AND direction_exec=short`
- Raw: n=99  W=38/L=61  WR=38.4%
- Sharpen: sharpest is T4=T4a (61/61 of losers there)
- **Sharp: n=75  W=14/L=61  WR=18.7%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 strongly against; RSI 60-70 strong  •  ONLY when 4h trend WITH trade

### L19.  `H60=H60e AND T1=T1c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=99  W=38/L=61  WR=38.4%
- Sharpen: sharpest is T4=T4a (61/61 of losers there)
- **Sharp: n=75  W=14/L=61  WR=18.7%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when 4h trend WITH trade

### L20.  `H20=H20a AND T4=T4a AND ZS=ZS5`
- Raw: n=97  W=35/L=62  WR=36.1%
- Sharpen: sharpest is BBP=BBP6 (37/62 of losers there)
- **Sharp: n=43  W=6/L=37  WR=14.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  ONLY when deep above upper band

### L21.  `T4=T4a AND RSI=RSI4 AND session_bucket=ny_mid`
- Raw: n=97  W=36/L=61  WR=37.1%
- Sharpen: sharpest is direction_exec=short (31/61 of losers there)
- **Sharp: n=34  W=3/L=31  WR=8.8%**
- **Dir: ?**  •  4h trend WITH trade; RSI 50-60 upper neutral; session=ny_mid  •  ONLY when short

### L22.  `H60=H60a AND T1=T1a AND session_bucket=ny_close`
- Raw: n=95  W=36/L=59  WR=37.9%
- Sharpen: sharpest is H20=H20e (46/59 of losers there)
- **Sharp: n=60  W=14/L=46  WR=23.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=ny_close  •  ONLY when HTF20 strongly against

### L23.  `H20=H20a AND T1=T1c AND session_bucket=ny_mid`
- Raw: n=93  W=15/L=78  WR=16.1%
- Sharpen: sharpest is RSI=RSI4 (31/78 of losers there)
- **Sharp: n=34  W=3/L=31  WR=8.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; session=ny_mid  •  ONLY when RSI 50-60 upper neutral

### L24.  `H20=H20a AND T1=T1c AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=93  W=15/L=78  WR=16.1%
- Sharpen: sharpest is RSI=RSI4 (31/78 of losers there)
- **Sharp: n=34  W=3/L=31  WR=8.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; session=ny_mid  •  ONLY when RSI 50-60 upper neutral

### L25.  `H20=H20a AND T1=T1c AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=93  W=15/L=78  WR=16.1%
- Sharpen: sharpest is RSI=RSI4 (31/78 of losers there)
- **Sharp: n=34  W=3/L=31  WR=8.8%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; session=ny_mid  •  ONLY when RSI 50-60 upper neutral

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | — |
| T1 | T1a(54/45) | T1c(46/55) |
| T4 | T4c(56/43) | T4a(43/56) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
