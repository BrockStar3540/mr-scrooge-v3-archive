# EUR_AUD — R31 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20d**  (EMA20 down 0.15-0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **4,948**  (W=3,090 / L=1,858)  -  WR: **62.4%**

## Session distribution

- asia: n=1917  W=1211/L=706  WR=63.2%
- london_open: n=686  W=439/L=247  WR=64.0%
- ny_close: n=650  W=407/L=243  WR=62.6%
- ny_open: n=469  W=281/L=188  WR=59.9%
- london: n=404  W=267/L=137  WR=66.1%
- asia_late: n=357  W=218/L=139  WR=61.1%
- ny_mid: n=289  W=176/L=113  WR=60.9%
- off_hours: n=176  W=91/L=85  WR=51.7%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20e AND H60=H60e AND T4=T4c AND BBP=BBP0`
- Raw: n=267  W=228/L=39  WR=85.4%
- Refine: exclude session_bucket=ny_open drops 8/39 losers (21%)
- **Final: n=255  W=224/L=31  WR=87.8%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; deep below lower band  •  AVOID when session=ny_open

### W02.  `H60=H60e AND T1=T1c AND T4=T4c AND BBP=BBP0`
- Raw: n=255  W=218/L=37  WR=85.5%
- Refine: exclude RSI=RSI3 drops 18/37 losers (49%)
- **Final: n=179  W=160/L=19  WR=89.4%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; deep below lower band  •  AVOID when RSI 40-50 lower neutral

### W03.  `H20=H20e AND H60=H60e AND T1=T1c AND BBP=BBP0`
- Raw: n=234  W=199/L=35  WR=85.0%
- Refine: exclude session_bucket=ny_open drops 8/35 losers (23%)
- **Final: n=226  W=199/L=27  WR=88.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; deep below lower band  •  AVOID when session=ny_open

### W04.  `T1=T1c AND T4=T4c AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=234  W=199/L=35  WR=85.0%
- Refine: exclude session_bucket=asia drops 33/35 losers (94%)
- **Final: n=98  W=96/L=2  WR=98.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; deep below lower band; zscore -3 to -2 deep oversold  •  AVOID when session=asia

### W05.  `T4=T4c AND BBP=BBP0 AND RSI=RSI2`
- Raw: n=210  W=184/L=26  WR=87.6%
- Refine: exclude session_bucket=asia drops 21/26 losers (81%)
- **Final: n=88  W=83/L=5  WR=94.3%**
- **Dir: ?**  •  4h trend AGAINST trade; deep below lower band; RSI 30-40 weak  •  AVOID when session=asia

### W06.  `T4=T4c AND BBP=BBP0 AND RSI=RSI2 AND direction_exec=long`
- Raw: n=197  W=172/L=25  WR=87.3%
- Refine: exclude session_bucket=asia drops 21/25 losers (84%)
- **Final: n=87  W=83/L=4  WR=95.4%**
- **Dir: LONG**  •  4h trend AGAINST trade; deep below lower band; RSI 30-40 weak  •  AVOID when session=asia

### W07.  `H60=H60e AND BBP=BBP0 AND RSI=RSI2`
- Raw: n=193  W=168/L=25  WR=87.0%
- Refine: exclude session_bucket=asia drops 21/25 losers (84%)
- **Final: n=83  W=79/L=4  WR=95.2%**
- **Dir: ?**  •  HTF60 strongly against; deep below lower band; RSI 30-40 weak  •  AVOID when session=asia

### W08.  `H60=H60e AND BBP=BBP0 AND RSI=RSI2 AND direction_exec=long`
- Raw: n=193  W=168/L=25  WR=87.0%
- Refine: exclude session_bucket=asia drops 21/25 losers (84%)
- **Final: n=83  W=79/L=4  WR=95.2%**
- **Dir: LONG**  •  HTF60 strongly against; deep below lower band; RSI 30-40 weak  •  AVOID when session=asia

### W09.  `T1=T1c AND T4=T4c AND BBP=BBP0 AND RSI=RSI2`
- Raw: n=191  W=166/L=25  WR=86.9%
- Refine: exclude session_bucket=asia drops 21/25 losers (84%)
- **Final: n=81  W=77/L=4  WR=95.1%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; deep below lower band; RSI 30-40 weak  •  AVOID when session=asia

### W10.  `H60=H60e AND T1=T1c AND BBP=BBP0 AND RSI=RSI2`
- Raw: n=187  W=162/L=25  WR=86.6%
- Refine: exclude session_bucket=asia drops 21/25 losers (84%)
- **Final: n=77  W=73/L=4  WR=94.8%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; deep below lower band; RSI 30-40 weak  •  AVOID when session=asia

### W11.  `H60=H60e AND T4=T4c AND BBP=BBP0 AND RSI=RSI2`
- Raw: n=185  W=166/L=19  WR=89.7%
- Refine: exclude session_bucket=asia drops 15/19 losers (79%)
- **Final: n=81  W=77/L=4  WR=95.1%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; deep below lower band; RSI 30-40 weak  •  AVOID when session=asia

### W12.  `T4=T4c AND BBP=BBP0 AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=169  W=147/L=22  WR=87.0%
- Refine: exclude session_bucket=asia drops 21/22 losers (95%)
- **Final: n=75  W=74/L=1  WR=98.7%**
- **Dir: ?**  •  4h trend AGAINST trade; deep below lower band; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  AVOID when session=asia

### W13.  `H60=H60e AND BBP=BBP0 AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=152  W=131/L=21  WR=86.2%
- Refine: exclude session_bucket=asia drops 21/21 losers (100%)
- **Final: n=70  W=70/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; deep below lower band; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  AVOID when session=asia

### W14.  `H20=H20e AND H60=H60e AND T4=T4c AND session_bucket=london`
- Raw: n=147  W=126/L=21  WR=85.7%
- Refine: exclude RSI=RSI4 drops 10/21 losers (48%)
- **Final: n=105  W=94/L=11  WR=89.5%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; session=london  •  AVOID when RSI 50-60 upper neutral

### W15.  `T4=T4c AND RSI=RSI2 AND session_bucket=london_open`
- Raw: n=115  W=98/L=17  WR=85.2%
- Refine: exclude BBP=BBP3 drops 8/17 losers (47%)
- **Final: n=97  W=88/L=9  WR=90.7%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 30-40 weak; session=london_open  •  AVOID when middle of band

### W16.  `RSI=RSI2 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=115  W=98/L=17  WR=85.2%
- Refine: exclude BBP=BBP3 drops 8/17 losers (47%)
- **Final: n=97  W=88/L=9  WR=90.7%**
- **Dir: LONG**  •  RSI 30-40 weak; session=london_open  •  AVOID when middle of band

### W17.  `T4=T4c AND RSI=RSI2 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=115  W=98/L=17  WR=85.2%
- Refine: exclude BBP=BBP3 drops 8/17 losers (47%)
- **Final: n=97  W=88/L=9  WR=90.7%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 30-40 weak; session=london_open  •  AVOID when middle of band

### W18.  `H20=H20e AND RSI=RSI3 AND session_bucket=london`
- Raw: n=108  W=93/L=15  WR=86.1%
- Refine: exclude T1=T1c drops 15/15 losers (100%)
- **Final: n=43  W=43/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; RSI 40-50 lower neutral; session=london  •  AVOID when 1h trend AGAINST trade

### W19.  `H20=H20e AND RSI=RSI3 AND direction_exec=long AND session_bucket=london`
- Raw: n=108  W=93/L=15  WR=86.1%
- Refine: exclude T1=T1c drops 15/15 losers (100%)
- **Final: n=43  W=43/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 40-50 lower neutral; session=london  •  AVOID when 1h trend AGAINST trade

### W20.  `H20=H20e AND H60=H60e AND RSI=RSI3 AND session_bucket=london`
- Raw: n=100  W=85/L=15  WR=85.0%
- Refine: exclude T1=T1c drops 15/15 losers (100%)
- **Final: n=43  W=43/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 40-50 lower neutral; session=london  •  AVOID when 1h trend AGAINST trade

### W21.  `H20=H20e AND T4=T4c AND RSI=RSI3 AND session_bucket=london`
- Raw: n=99  W=88/L=11  WR=88.9%
- Refine: exclude T1=T1c drops 11/11 losers (100%)
- **Final: n=43  W=43/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 40-50 lower neutral; session=london  •  AVOID when 1h trend AGAINST trade

### W22.  `BBP=BBP4 AND RSI=RSI2 AND direction_exec=short`
- Raw: n=99  W=85/L=14  WR=85.9%
- Refine: exclude session_bucket=asia drops 7/14 losers (50%)
- **Final: n=71  W=64/L=7  WR=90.1%**
- **Dir: SHORT**  •  upper third; RSI 30-40 weak  •  AVOID when session=asia

### W23.  `T4=T4a AND BBP=BBP4 AND RSI=RSI2`
- Raw: n=96  W=82/L=14  WR=85.4%
- Refine: exclude session_bucket=asia drops 7/14 losers (50%)
- **Final: n=68  W=61/L=7  WR=89.7%**
- **Dir: ?**  •  4h trend WITH trade; upper third; RSI 30-40 weak  •  AVOID when session=asia

### W24.  `H60=H60a AND BBP=BBP4 AND RSI=RSI2`
- Raw: n=95  W=82/L=13  WR=86.3%
- Refine: exclude session_bucket=asia drops 7/13 losers (54%)
- **Final: n=67  W=61/L=6  WR=91.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; upper third; RSI 30-40 weak  •  AVOID when session=asia

### W25.  `H60=H60a AND BBP=BBP4 AND RSI=RSI2 AND direction_exec=short`
- Raw: n=95  W=82/L=13  WR=86.3%
- Refine: exclude session_bucket=asia drops 7/13 losers (54%)
- **Final: n=67  W=61/L=6  WR=91.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; upper third; RSI 30-40 weak  •  AVOID when session=asia

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60a AND T4=T4a AND BBP=BBP0`
- Raw: n=235  W=94/L=141  WR=40.0%
- Sharpen: sharpest is session_bucket=london_open (27/141 of losers there)
- **Sharp: n=27  W=0/L=27  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; deep below lower band  •  ONLY when session=london_open

### L02.  `H60=H60a AND T4=T4a AND BBP=BBP0 AND direction_exec=short`
- Raw: n=235  W=94/L=141  WR=40.0%
- Sharpen: sharpest is session_bucket=london_open (27/141 of losers there)
- **Sharp: n=27  W=0/L=27  WR=0.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend WITH trade; deep below lower band  •  ONLY when session=london_open

### L03.  `H20=H20a AND direction_exec=short AND session_bucket=london_open`
- Raw: n=221  W=88/L=133  WR=39.8%
- Sharpen: sharpest is ZS=ZS1 (28/133 of losers there)
- **Sharp: n=31  W=3/L=28  WR=9.7%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; session=london_open  •  ONLY when zscore -3 to -2 deep oversold

### L04.  `T4=T4a AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=211  W=81/L=130  WR=38.4%
- Sharpen: sharpest is session_bucket=london_open (27/130 of losers there)
- **Sharp: n=27  W=0/L=27  WR=0.0%**
- **Dir: ?**  •  4h trend WITH trade; deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when session=london_open

### L05.  `H20=H20a AND T1=T1a AND session_bucket=london_open`
- Raw: n=206  W=81/L=125  WR=39.3%
- Sharpen: sharpest is ZS=ZS1 (28/125 of losers there)
- **Sharp: n=31  W=3/L=28  WR=9.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=london_open  •  ONLY when zscore -3 to -2 deep oversold

### L06.  `H20=H20a AND T1=T1a AND direction_exec=short AND session_bucket=london_open`
- Raw: n=206  W=81/L=125  WR=39.3%
- Sharpen: sharpest is ZS=ZS1 (28/125 of losers there)
- **Sharp: n=31  W=3/L=28  WR=9.7%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=london_open  •  ONLY when zscore -3 to -2 deep oversold

### L07.  `T4=T4a AND BBP=BBP0 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=203  W=79/L=124  WR=38.9%
- Sharpen: sharpest is session_bucket=london_open (27/124 of losers there)
- **Sharp: n=27  W=0/L=27  WR=0.0%**
- **Dir: SHORT**  •  4h trend WITH trade; deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when session=london_open

### L08.  `H60=H60a AND T4=T4a AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=187  W=71/L=116  WR=38.0%
- Sharpen: sharpest is session_bucket=london_open (26/116 of losers there)
- **Sharp: n=26  W=0/L=26  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when session=london_open

### L09.  `T1=T1a AND T4=T4a AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=174  W=69/L=105  WR=39.7%
- Sharpen: sharpest is session_bucket=london_open (23/105 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when session=london_open

### L10.  `T4=T4a AND BBP=BBP0 AND RSI=RSI2`
- Raw: n=150  W=55/L=95  WR=36.7%
- Sharpen: sharpest is session_bucket=london_open (21/95 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: ?**  •  4h trend WITH trade; deep below lower band; RSI 30-40 weak  •  ONLY when session=london_open

### L11.  `H20=H20a AND RSI=RSI3 AND session_bucket=london_open`
- Raw: n=146  W=52/L=94  WR=35.6%
- Sharpen: sharpest is ZS=ZS2 (21/94 of losers there)
- **Sharp: n=24  W=3/L=21  WR=12.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 40-50 lower neutral; session=london_open  •  ONLY when zscore -2 to -1 oversold

### L12.  `T4=T4a AND BBP=BBP0 AND RSI=RSI2 AND direction_exec=short`
- Raw: n=142  W=53/L=89  WR=37.3%
- Sharpen: sharpest is session_bucket=london_open (21/89 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: SHORT**  •  4h trend WITH trade; deep below lower band; RSI 30-40 weak  •  ONLY when session=london_open

### L13.  `T1=T1a AND T4=T4a AND BBP=BBP0 AND RSI=RSI2`
- Raw: n=138  W=53/L=85  WR=38.4%
- Sharpen: sharpest is session_bucket=london_open (17/85 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; deep below lower band; RSI 30-40 weak  •  ONLY when session=london_open

### L14.  `H20=H20a AND RSI=RSI3 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=135  W=48/L=87  WR=35.6%
- Sharpen: sharpest is ZS=ZS2 (21/87 of losers there)
- **Sharp: n=24  W=3/L=21  WR=12.5%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 40-50 lower neutral; session=london_open  •  ONLY when zscore -2 to -1 oversold

### L15.  `H60=H60e AND T1=T1a AND T4=T4c AND session_bucket=asia`
- Raw: n=134  W=51/L=83  WR=38.1%
- Sharpen: sharpest is ZS=ZS4 (20/83 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; session=asia  •  ONLY when zscore +1 to +2 overbought

### L16.  `T1=T1a AND T4=T4c AND direction_exec=long AND session_bucket=asia`
- Raw: n=134  W=51/L=83  WR=38.1%
- Sharpen: sharpest is ZS=ZS4 (20/83 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend AGAINST trade; session=asia  •  ONLY when zscore +1 to +2 overbought

### L17.  `H20=H20a AND T1=T1a AND RSI=RSI3 AND session_bucket=london_open`
- Raw: n=132  W=48/L=84  WR=36.4%
- Sharpen: sharpest is ZS=ZS2 (21/84 of losers there)
- **Sharp: n=24  W=3/L=21  WR=12.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 40-50 lower neutral; session=london_open  •  ONLY when zscore -2 to -1 oversold

### L18.  `H20=H20a AND T4=T4a AND RSI=RSI3 AND session_bucket=london_open`
- Raw: n=131  W=48/L=83  WR=36.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=131  W=48/L=83  WR=36.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral; session=london_open

### L19.  `H20=H20a AND H60=H60a AND RSI=RSI3 AND session_bucket=london_open`
- Raw: n=130  W=48/L=82  WR=36.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=130  W=48/L=82  WR=36.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 40-50 lower neutral; session=london_open

### L20.  `H60=H60a AND T4=T4a AND BBP=BBP0 AND RSI=RSI2`
- Raw: n=128  W=45/L=83  WR=35.2%
- Sharpen: sharpest is session_bucket=london_open (20/83 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; deep below lower band; RSI 30-40 weak  •  ONLY when session=london_open

### L21.  `T4=T4a AND BBP=BBP0 AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=123  W=44/L=79  WR=35.8%
- Sharpen: sharpest is session_bucket=london_open (20/79 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  4h trend WITH trade; deep below lower band; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when session=london_open

### L22.  `H20=H20e AND BBP=BBP1 AND direction_exec=long AND session_bucket=asia`
- Raw: n=89  W=33/L=56  WR=37.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=89  W=33/L=56  WR=37.1%**
- **Dir: LONG**  •  HTF20 strongly against; just touched lower band; session=asia

### L23.  `T1=T1c AND BBP=BBP6 AND direction_exec=long`
- Raw: n=86  W=34/L=52  WR=39.5%
- Sharpen: sharpest is RSI=RSI3 (29/52 of losers there)
- **Sharp: n=37  W=8/L=29  WR=21.6%**
- **Dir: LONG**  •  1h trend AGAINST trade; deep above upper band  •  ONLY when RSI 40-50 lower neutral

### L24.  `H20=H20e AND H60=H60e AND BBP=BBP1 AND session_bucket=asia`
- Raw: n=85  W=33/L=52  WR=38.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=85  W=33/L=52  WR=38.8%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; just touched lower band; session=asia

### L25.  `H20=H20a AND BBP=BBP4 AND session_bucket=london_open`
- Raw: n=81  W=29/L=52  WR=35.8%
- Sharpen: sharpest is T4=T4c (10/52 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; upper third; session=london_open  •  ONLY when 4h trend AGAINST trade

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20e(45/40) | H20a(40/45) |
| H60 | H60e(47/41) | H60a(42/48) |
| T1 | — | — |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
