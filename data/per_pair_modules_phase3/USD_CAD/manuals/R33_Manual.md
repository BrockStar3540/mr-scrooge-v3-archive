# USD_CAD — R33 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50e**  (EMA50 down >0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **1,814**  (W=1,155 / L=659)  -  WR: **63.7%**

## Session distribution

- ny_mid: n=525  W=333/L=192  WR=63.4%
- ny_open: n=386  W=245/L=141  WR=63.5%
- london_open: n=301  W=195/L=106  WR=64.8%
- ny_close: n=183  W=115/L=68  WR=62.8%
- asia: n=178  W=116/L=62  WR=65.2%
- london: n=177  W=114/L=63  WR=64.4%
- asia_late: n=54  W=29/L=25  WR=53.7%
- off_hours: n=10  W=8/L=2  WR=80.0%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1a AND T4=T4a AND session_bucket=london_open`
- Raw: n=179  W=158/L=21  WR=88.3%
- Refine: exclude RSI=RSI2 drops 10/21 losers (48%)
- **Final: n=136  W=125/L=11  WR=91.9%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; session=london_open  •  AVOID when RSI 30-40 weak

### W02.  `T1=T1a AND direction_exec=short AND session_bucket=london_open`
- Raw: n=179  W=158/L=21  WR=88.3%
- Refine: exclude RSI=RSI2 drops 10/21 losers (48%)
- **Final: n=136  W=125/L=11  WR=91.9%**
- **Dir: SHORT**  •  1h trend WITH trade; session=london_open  •  AVOID when RSI 30-40 weak

### W03.  `T4=T4a AND direction_exec=short AND session_bucket=london_open`
- Raw: n=179  W=158/L=21  WR=88.3%
- Refine: exclude RSI=RSI2 drops 10/21 losers (48%)
- **Final: n=136  W=125/L=11  WR=91.9%**
- **Dir: SHORT**  •  4h trend WITH trade; session=london_open  •  AVOID when RSI 30-40 weak

### W04.  `T1=T1a AND T4=T4a AND direction_exec=short AND session_bucket=london_open`
- Raw: n=179  W=158/L=21  WR=88.3%
- Refine: exclude RSI=RSI2 drops 10/21 losers (48%)
- **Final: n=136  W=125/L=11  WR=91.9%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend WITH trade; session=london_open  •  AVOID when RSI 30-40 weak

### W05.  `H20=H20a AND T1=T1a AND session_bucket=london_open`
- Raw: n=113  W=97/L=16  WR=85.8%
- Refine: exclude RSI=RSI2 drops 10/16 losers (62%)
- **Final: n=70  W=64/L=6  WR=91.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=london_open  •  AVOID when RSI 30-40 weak

### W06.  `H20=H20a AND T4=T4a AND session_bucket=london_open`
- Raw: n=113  W=97/L=16  WR=85.8%
- Refine: exclude RSI=RSI2 drops 10/16 losers (62%)
- **Final: n=70  W=64/L=6  WR=91.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=london_open  •  AVOID when RSI 30-40 weak

### W07.  `H20=H20a AND direction_exec=short AND session_bucket=london_open`
- Raw: n=113  W=97/L=16  WR=85.8%
- Refine: exclude RSI=RSI2 drops 10/16 losers (62%)
- **Final: n=70  W=64/L=6  WR=91.4%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; session=london_open  •  AVOID when RSI 30-40 weak

### W08.  `H20=H20a AND T1=T1a AND T4=T4a AND session_bucket=london_open`
- Raw: n=113  W=97/L=16  WR=85.8%
- Refine: exclude RSI=RSI2 drops 10/16 losers (62%)
- **Final: n=70  W=64/L=6  WR=91.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; session=london_open  •  AVOID when RSI 30-40 weak

### W09.  `H20=H20a AND T1=T1a AND direction_exec=short AND session_bucket=london_open`
- Raw: n=113  W=97/L=16  WR=85.8%
- Refine: exclude RSI=RSI2 drops 10/16 losers (62%)
- **Final: n=70  W=64/L=6  WR=91.4%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=london_open  •  AVOID when RSI 30-40 weak

### W10.  `H20=H20a AND T4=T4a AND direction_exec=short AND session_bucket=london_open`
- Raw: n=113  W=97/L=16  WR=85.8%
- Refine: exclude RSI=RSI2 drops 10/16 losers (62%)
- **Final: n=70  W=64/L=6  WR=91.4%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=london_open  •  AVOID when RSI 30-40 weak

### W11.  `T1=T1a AND RSI=RSI1 AND session_bucket=london_open`
- Raw: n=104  W=93/L=11  WR=89.4%
- Refine: exclude H60=H60e drops 6/11 losers (55%)
- **Final: n=92  W=87/L=5  WR=94.6%**
- **Dir: ?**  •  1h trend WITH trade; RSI 20-30 oversold; session=london_open  •  AVOID when HTF60 strongly against

### W12.  `T4=T4a AND RSI=RSI1 AND session_bucket=london_open`
- Raw: n=104  W=93/L=11  WR=89.4%
- Refine: exclude H60=H60e drops 6/11 losers (55%)
- **Final: n=92  W=87/L=5  WR=94.6%**
- **Dir: ?**  •  4h trend WITH trade; RSI 20-30 oversold; session=london_open  •  AVOID when HTF60 strongly against

### W13.  `RSI=RSI1 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=104  W=93/L=11  WR=89.4%
- Refine: exclude H60=H60e drops 6/11 losers (55%)
- **Final: n=92  W=87/L=5  WR=94.6%**
- **Dir: SHORT**  •  RSI 20-30 oversold; session=london_open  •  AVOID when HTF60 strongly against

### W14.  `T1=T1a AND T4=T4a AND RSI=RSI1 AND session_bucket=london_open`
- Raw: n=104  W=93/L=11  WR=89.4%
- Refine: exclude H60=H60e drops 6/11 losers (55%)
- **Final: n=92  W=87/L=5  WR=94.6%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 20-30 oversold; session=london_open  •  AVOID when HTF60 strongly against

### W15.  `T1=T1a AND RSI=RSI1 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=104  W=93/L=11  WR=89.4%
- Refine: exclude H60=H60e drops 6/11 losers (55%)
- **Final: n=92  W=87/L=5  WR=94.6%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 20-30 oversold; session=london_open  •  AVOID when HTF60 strongly against

### W16.  `T4=T4a AND RSI=RSI1 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=104  W=93/L=11  WR=89.4%
- Refine: exclude H60=H60e drops 6/11 losers (55%)
- **Final: n=92  W=87/L=5  WR=94.6%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 20-30 oversold; session=london_open  •  AVOID when HTF60 strongly against

### W17.  `H60=H60a AND T1=T1a AND session_bucket=london_open`
- Raw: n=102  W=88/L=14  WR=86.3%
- Refine: exclude RSI=RSI2 drops 10/14 losers (71%)
- **Final: n=71  W=67/L=4  WR=94.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=london_open  •  AVOID when RSI 30-40 weak

### W18.  `H60=H60a AND T4=T4a AND session_bucket=london_open`
- Raw: n=102  W=88/L=14  WR=86.3%
- Refine: exclude RSI=RSI2 drops 10/14 losers (71%)
- **Final: n=71  W=67/L=4  WR=94.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; session=london_open  •  AVOID when RSI 30-40 weak

### W19.  `H60=H60a AND direction_exec=short AND session_bucket=london_open`
- Raw: n=102  W=88/L=14  WR=86.3%
- Refine: exclude RSI=RSI2 drops 10/14 losers (71%)
- **Final: n=71  W=67/L=4  WR=94.4%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; session=london_open  •  AVOID when RSI 30-40 weak

### W20.  `H60=H60a AND T1=T1a AND T4=T4a AND session_bucket=london_open`
- Raw: n=102  W=88/L=14  WR=86.3%
- Refine: exclude RSI=RSI2 drops 10/14 losers (71%)
- **Final: n=71  W=67/L=4  WR=94.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; session=london_open  •  AVOID when RSI 30-40 weak

### W21.  `H60=H60a AND T1=T1a AND direction_exec=short AND session_bucket=london_open`
- Raw: n=102  W=88/L=14  WR=86.3%
- Refine: exclude RSI=RSI2 drops 10/14 losers (71%)
- **Final: n=71  W=67/L=4  WR=94.4%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=london_open  •  AVOID when RSI 30-40 weak

### W22.  `H60=H60a AND T4=T4a AND direction_exec=short AND session_bucket=london_open`
- Raw: n=102  W=88/L=14  WR=86.3%
- Refine: exclude RSI=RSI2 drops 10/14 losers (71%)
- **Final: n=71  W=67/L=4  WR=94.4%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend WITH trade; session=london_open  •  AVOID when RSI 30-40 weak

### W23.  `H60=H60a AND T1=T1a AND RSI=RSI0`
- Raw: n=93  W=80/L=13  WR=86.0%
- Refine: exclude session_bucket=ny_open drops 4/13 losers (31%)
- **Final: n=83  W=74/L=9  WR=89.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI<20 extreme oversold  •  AVOID when session=ny_open

### W24.  `H60=H60a AND T4=T4a AND RSI=RSI0`
- Raw: n=93  W=80/L=13  WR=86.0%
- Refine: exclude session_bucket=ny_open drops 4/13 losers (31%)
- **Final: n=83  W=74/L=9  WR=89.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI<20 extreme oversold  •  AVOID when session=ny_open

### W25.  `H60=H60a AND RSI=RSI0 AND direction_exec=short`
- Raw: n=93  W=80/L=13  WR=86.0%
- Refine: exclude session_bucket=ny_open drops 4/13 losers (31%)
- **Final: n=83  W=74/L=9  WR=89.2%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; RSI<20 extreme oversold  •  AVOID when session=ny_open

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1c AND T4=T4c AND RSI=RSI0`
- Raw: n=176  W=59/L=117  WR=33.5%
- Sharpen: sharpest is session_bucket=london_open (18/117 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI<20 extreme oversold  •  ONLY when session=london_open

### L02.  `T1=T1c AND RSI=RSI0 AND direction_exec=long`
- Raw: n=176  W=59/L=117  WR=33.5%
- Sharpen: sharpest is session_bucket=london_open (18/117 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI<20 extreme oversold  •  ONLY when session=london_open

### L03.  `T4=T4c AND RSI=RSI0 AND direction_exec=long`
- Raw: n=176  W=59/L=117  WR=33.5%
- Sharpen: sharpest is session_bucket=london_open (18/117 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI<20 extreme oversold  •  ONLY when session=london_open

### L04.  `T1=T1c AND T4=T4c AND RSI=RSI0 AND direction_exec=long`
- Raw: n=176  W=59/L=117  WR=33.5%
- Sharpen: sharpest is session_bucket=london_open (18/117 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI<20 extreme oversold  •  ONLY when session=london_open

### L05.  `T1=T1c AND T4=T4c AND session_bucket=london_open`
- Raw: n=122  W=37/L=85  WR=30.3%
- Sharpen: sharpest is H20=H20e (48/85 of losers there)
- **Sharp: n=56  W=8/L=48  WR=14.3%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=london_open  •  ONLY when HTF20 strongly against

### L06.  `T1=T1c AND direction_exec=long AND session_bucket=london_open`
- Raw: n=122  W=37/L=85  WR=30.3%
- Sharpen: sharpest is H20=H20e (48/85 of losers there)
- **Sharp: n=56  W=8/L=48  WR=14.3%**
- **Dir: LONG**  •  1h trend AGAINST trade; session=london_open  •  ONLY when HTF20 strongly against

### L07.  `T4=T4c AND direction_exec=long AND session_bucket=london_open`
- Raw: n=122  W=37/L=85  WR=30.3%
- Sharpen: sharpest is H20=H20e (48/85 of losers there)
- **Sharp: n=56  W=8/L=48  WR=14.3%**
- **Dir: LONG**  •  4h trend AGAINST trade; session=london_open  •  ONLY when HTF20 strongly against

### L08.  `T1=T1c AND T4=T4c AND direction_exec=long AND session_bucket=london_open`
- Raw: n=122  W=37/L=85  WR=30.3%
- Sharpen: sharpest is H20=H20e (48/85 of losers there)
- **Sharp: n=56  W=8/L=48  WR=14.3%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=london_open  •  ONLY when HTF20 strongly against

### L09.  `T1=T1c AND BBP=BBP2 AND RSI=RSI0`
- Raw: n=112  W=40/L=72  WR=35.7%
- Sharpen: sharpest is session_bucket=london_open (14/72 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; lower third; RSI<20 extreme oversold  •  ONLY when session=london_open

### L10.  `T4=T4c AND BBP=BBP2 AND RSI=RSI0`
- Raw: n=112  W=40/L=72  WR=35.7%
- Sharpen: sharpest is session_bucket=london_open (14/72 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  4h trend AGAINST trade; lower third; RSI<20 extreme oversold  •  ONLY when session=london_open

### L11.  `BBP=BBP2 AND RSI=RSI0 AND direction_exec=long`
- Raw: n=112  W=40/L=72  WR=35.7%
- Sharpen: sharpest is session_bucket=london_open (14/72 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: LONG**  •  lower third; RSI<20 extreme oversold  •  ONLY when session=london_open

### L12.  `T1=T1c AND T4=T4c AND BBP=BBP2 AND RSI=RSI0`
- Raw: n=112  W=40/L=72  WR=35.7%
- Sharpen: sharpest is session_bucket=london_open (14/72 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; lower third; RSI<20 extreme oversold  •  ONLY when session=london_open

### L13.  `T1=T1c AND BBP=BBP2 AND RSI=RSI0 AND direction_exec=long`
- Raw: n=112  W=40/L=72  WR=35.7%
- Sharpen: sharpest is session_bucket=london_open (14/72 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; lower third; RSI<20 extreme oversold  •  ONLY when session=london_open

### L14.  `T4=T4c AND BBP=BBP2 AND RSI=RSI0 AND direction_exec=long`
- Raw: n=112  W=40/L=72  WR=35.7%
- Sharpen: sharpest is session_bucket=london_open (14/72 of losers there)
- **Sharp: n=14  W=0/L=14  WR=0.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; lower third; RSI<20 extreme oversold  •  ONLY when session=london_open

### L15.  `H20=H20e AND H60=H60d AND RSI=RSI0`
- Raw: n=105  W=40/L=65  WR=38.1%
- Sharpen: sharpest is session_bucket=london_open (18/65 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 mildly against; RSI<20 extreme oversold  •  ONLY when session=london_open

### L16.  `H20=H20e AND T1=T1c AND RSI=RSI0`
- Raw: n=105  W=40/L=65  WR=38.1%
- Sharpen: sharpest is session_bucket=london_open (18/65 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI<20 extreme oversold  •  ONLY when session=london_open

### L17.  `H20=H20e AND T4=T4c AND RSI=RSI0`
- Raw: n=105  W=40/L=65  WR=38.1%
- Sharpen: sharpest is session_bucket=london_open (18/65 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI<20 extreme oversold  •  ONLY when session=london_open

### L18.  `H20=H20e AND RSI=RSI0 AND direction_exec=long`
- Raw: n=105  W=40/L=65  WR=38.1%
- Sharpen: sharpest is session_bucket=london_open (18/65 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: LONG**  •  HTF20 strongly against; RSI<20 extreme oversold  •  ONLY when session=london_open

### L19.  `H60=H60d AND T1=T1c AND RSI=RSI0`
- Raw: n=105  W=40/L=65  WR=38.1%
- Sharpen: sharpest is session_bucket=london_open (18/65 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: ?**  •  HTF60 mildly against; 1h trend AGAINST trade; RSI<20 extreme oversold  •  ONLY when session=london_open

### L20.  `H60=H60d AND T4=T4c AND RSI=RSI0`
- Raw: n=105  W=40/L=65  WR=38.1%
- Sharpen: sharpest is session_bucket=london_open (18/65 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: ?**  •  HTF60 mildly against; 4h trend AGAINST trade; RSI<20 extreme oversold  •  ONLY when session=london_open

### L21.  `H60=H60d AND RSI=RSI0 AND direction_exec=long`
- Raw: n=105  W=40/L=65  WR=38.1%
- Sharpen: sharpest is session_bucket=london_open (18/65 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: LONG**  •  HTF60 mildly against; RSI<20 extreme oversold  •  ONLY when session=london_open

### L22.  `H20=H20e AND H60=H60d AND T1=T1c AND RSI=RSI0`
- Raw: n=105  W=40/L=65  WR=38.1%
- Sharpen: sharpest is session_bucket=london_open (18/65 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 mildly against; 1h trend AGAINST trade; RSI<20 extreme oversold  •  ONLY when session=london_open

### L23.  `H20=H20e AND H60=H60d AND T4=T4c AND RSI=RSI0`
- Raw: n=105  W=40/L=65  WR=38.1%
- Sharpen: sharpest is session_bucket=london_open (18/65 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 mildly against; 4h trend AGAINST trade; RSI<20 extreme oversold  •  ONLY when session=london_open

### L24.  `H20=H20e AND H60=H60d AND RSI=RSI0 AND direction_exec=long`
- Raw: n=105  W=40/L=65  WR=38.1%
- Sharpen: sharpest is session_bucket=london_open (18/65 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 mildly against; RSI<20 extreme oversold  •  ONLY when session=london_open

### L25.  `H20=H20e AND T1=T1c AND T4=T4c AND RSI=RSI0`
- Raw: n=105  W=40/L=65  WR=38.1%
- Sharpen: sharpest is session_bucket=london_open (18/65 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI<20 extreme oversold  •  ONLY when session=london_open

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | H60a(37/31) | H60e(36/42) |
| T1 | T1a(51/44) | T1c(49/56) |
| T4 | T4a(50/44) | T4c(50/56) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(51/44) | long(49/56) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
