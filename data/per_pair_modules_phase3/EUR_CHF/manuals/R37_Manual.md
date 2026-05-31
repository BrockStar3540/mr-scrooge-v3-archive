# EUR_CHF — R37 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **1,631**  (W=1,032 / L=599)  -  WR: **63.3%**

## Session distribution

- london_open: n=540  W=340/L=200  WR=63.0%
- ny_mid: n=503  W=321/L=182  WR=63.8%
- london: n=307  W=186/L=121  WR=60.6%
- ny_open: n=118  W=81/L=37  WR=68.6%
- ny_close: n=98  W=64/L=34  WR=65.3%
- asia: n=46  W=29/L=17  WR=63.0%
- off_hours: n=13  W=7/L=6  WR=53.8%
- asia_late: n=6  W=4/L=2  WR=66.7%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1a AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=296  W=273/L=23  WR=92.2%
- Refine: exclude T4=T4a drops 18/23 losers (78%)
- **Final: n=171  W=166/L=5  WR=97.1%**
- **Dir: LONG**  •  1h trend WITH trade; session=ny_mid  •  AVOID when 4h trend WITH trade

### W02.  `T1=T1a AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=199  W=183/L=16  WR=92.0%
- Refine: exclude BBP=BBP4 drops 14/16 losers (88%)
- **Final: n=79  W=77/L=2  WR=97.5%**
- **Dir: ?**  •  1h trend WITH trade; RSI 60-70 strong; session=ny_mid  •  AVOID when upper third

### W03.  `RSI=RSI5 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=199  W=183/L=16  WR=92.0%
- Refine: exclude BBP=BBP4 drops 14/16 losers (88%)
- **Final: n=79  W=77/L=2  WR=97.5%**
- **Dir: LONG**  •  RSI 60-70 strong; session=ny_mid  •  AVOID when upper third

### W04.  `T1=T1a AND RSI=RSI5 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=199  W=183/L=16  WR=92.0%
- Refine: exclude BBP=BBP4 drops 14/16 losers (88%)
- **Final: n=79  W=77/L=2  WR=97.5%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 60-70 strong; session=ny_mid  •  AVOID when upper third

### W05.  `T1=T1a AND BBP=BBP4 AND session_bucket=ny_mid`
- Raw: n=180  W=161/L=19  WR=89.4%
- Refine: exclude T4=T4a drops 14/19 losers (74%)
- **Final: n=128  W=123/L=5  WR=96.1%**
- **Dir: ?**  •  1h trend WITH trade; upper third; session=ny_mid  •  AVOID when 4h trend WITH trade

### W06.  `BBP=BBP4 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=180  W=161/L=19  WR=89.4%
- Refine: exclude T4=T4a drops 14/19 losers (74%)
- **Final: n=128  W=123/L=5  WR=96.1%**
- **Dir: LONG**  •  upper third; session=ny_mid  •  AVOID when 4h trend WITH trade

### W07.  `T1=T1a AND BBP=BBP4 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=180  W=161/L=19  WR=89.4%
- Refine: exclude T4=T4a drops 14/19 losers (74%)
- **Final: n=128  W=123/L=5  WR=96.1%**
- **Dir: LONG**  •  1h trend WITH trade; upper third; session=ny_mid  •  AVOID when 4h trend WITH trade

### W08.  `T1=T1a AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=171  W=166/L=5  WR=97.1%
- Refine: exclude H60=H60e drops 4/5 losers (80%)
- **Final: n=87  W=86/L=1  WR=98.9%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; session=ny_mid  •  AVOID when HTF60 strongly against

### W09.  `T4=T4c AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=171  W=166/L=5  WR=97.1%
- Refine: exclude H60=H60e drops 4/5 losers (80%)
- **Final: n=87  W=86/L=1  WR=98.9%**
- **Dir: LONG**  •  4h trend AGAINST trade; session=ny_mid  •  AVOID when HTF60 strongly against

### W10.  `T1=T1a AND T4=T4c AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=171  W=166/L=5  WR=97.1%
- Refine: exclude H60=H60e drops 4/5 losers (80%)
- **Final: n=87  W=86/L=1  WR=98.9%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend AGAINST trade; session=ny_mid  •  AVOID when HTF60 strongly against

### W11.  `T1=T1a AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=159  W=145/L=14  WR=91.2%
- Refine: exclude T4=T4a drops 10/14 losers (71%)
- **Final: n=116  W=112/L=4  WR=96.6%**
- **Dir: ?**  •  1h trend WITH trade; zscore +1 to +2 overbought; session=ny_mid  •  AVOID when 4h trend WITH trade

### W12.  `ZS=ZS4 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=159  W=145/L=14  WR=91.2%
- Refine: exclude T4=T4a drops 10/14 losers (71%)
- **Final: n=116  W=112/L=4  WR=96.6%**
- **Dir: LONG**  •  zscore +1 to +2 overbought; session=ny_mid  •  AVOID when 4h trend WITH trade

### W13.  `T1=T1a AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=159  W=145/L=14  WR=91.2%
- Refine: exclude T4=T4a drops 10/14 losers (71%)
- **Final: n=116  W=112/L=4  WR=96.6%**
- **Dir: ?**  •  1h trend WITH trade; upper third; zscore +1 to +2 overbought; session=ny_mid  •  AVOID when 4h trend WITH trade

### W14.  `T1=T1a AND ZS=ZS4 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=159  W=145/L=14  WR=91.2%
- Refine: exclude T4=T4a drops 10/14 losers (71%)
- **Final: n=116  W=112/L=4  WR=96.6%**
- **Dir: LONG**  •  1h trend WITH trade; zscore +1 to +2 overbought; session=ny_mid  •  AVOID when 4h trend WITH trade

### W15.  `BBP=BBP4 AND ZS=ZS4 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=159  W=145/L=14  WR=91.2%
- Refine: exclude T4=T4a drops 10/14 losers (71%)
- **Final: n=116  W=112/L=4  WR=96.6%**
- **Dir: LONG**  •  upper third; zscore +1 to +2 overbought; session=ny_mid  •  AVOID when 4h trend WITH trade

### W16.  `H20=H20a AND T4=T4a AND session_bucket=london_open`
- Raw: n=158  W=137/L=21  WR=86.7%
- Refine: exclude RSI=RSI4 drops 18/21 losers (86%)
- **Final: n=65  W=62/L=3  WR=95.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=london_open  •  AVOID when RSI 50-60 upper neutral

### W17.  `H20=H20e AND T1=T1a AND session_bucket=ny_mid`
- Raw: n=150  W=141/L=9  WR=94.0%
- Refine: exclude ZS=ZS3 drops 3/9 losers (33%)
- **Final: n=136  W=130/L=6  WR=95.6%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; session=ny_mid  •  AVOID when zscore -1 to +1 neutral

### W18.  `H20=H20e AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=150  W=141/L=9  WR=94.0%
- Refine: exclude ZS=ZS3 drops 3/9 losers (33%)
- **Final: n=136  W=130/L=6  WR=95.6%**
- **Dir: LONG**  •  HTF20 strongly against; session=ny_mid  •  AVOID when zscore -1 to +1 neutral

### W19.  `H20=H20e AND T1=T1a AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=150  W=141/L=9  WR=94.0%
- Refine: exclude ZS=ZS3 drops 3/9 losers (33%)
- **Final: n=136  W=130/L=6  WR=95.6%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend WITH trade; session=ny_mid  •  AVOID when zscore -1 to +1 neutral

### W20.  `T4=T4a AND direction_exec=short AND session_bucket=london_open`
- Raw: n=142  W=121/L=21  WR=85.2%
- Refine: exclude T1=T1a drops 12/21 losers (57%)
- **Final: n=102  W=93/L=9  WR=91.2%**
- **Dir: SHORT**  •  4h trend WITH trade; session=london_open  •  AVOID when 1h trend WITH trade

### W21.  `H60=H60e AND T4=T4c AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=133  W=116/L=17  WR=87.2%
- Refine: exclude session_bucket=ny_close drops 6/17 losers (35%)
- **Final: n=126  W=115/L=11  WR=91.3%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; upper third; RSI 50-60 upper neutral  •  AVOID when session=ny_close

### W22.  `H60=H60e AND T1=T1a AND session_bucket=ny_mid`
- Raw: n=131  W=121/L=10  WR=92.4%
- Refine: exclude RSI=RSI5 drops 8/10 losers (80%)
- **Final: n=62  W=60/L=2  WR=96.8%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; session=ny_mid  •  AVOID when RSI 60-70 strong

### W23.  `H60=H60e AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=131  W=121/L=10  WR=92.4%
- Refine: exclude RSI=RSI5 drops 8/10 losers (80%)
- **Final: n=62  W=60/L=2  WR=96.8%**
- **Dir: LONG**  •  HTF60 strongly against; session=ny_mid  •  AVOID when RSI 60-70 strong

### W24.  `H60=H60e AND T1=T1a AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=131  W=121/L=10  WR=92.4%
- Refine: exclude RSI=RSI5 drops 8/10 losers (80%)
- **Final: n=62  W=60/L=2  WR=96.8%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend WITH trade; session=ny_mid  •  AVOID when RSI 60-70 strong

### W25.  `T1=T1a AND T4=T4c AND BBP=BBP4 AND session_bucket=ny_mid`
- Raw: n=128  W=123/L=5  WR=96.1%
- Refine: exclude H60=H60e drops 4/5 losers (80%)
- **Final: n=62  W=61/L=1  WR=98.4%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; upper third; session=ny_mid  •  AVOID when HTF60 strongly against

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1c AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=207  W=48/L=159  WR=23.2%
- Sharpen: sharpest is T4=T4a (99/159 of losers there)
- **Sharp: n=109  W=10/L=99  WR=9.2%**
- **Dir: SHORT**  •  1h trend AGAINST trade; session=ny_mid  •  ONLY when 4h trend WITH trade

### L02.  `T1=T1c AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=146  W=27/L=119  WR=18.5%
- Sharpen: sharpest is T4=T4a (62/119 of losers there)
- **Sharp: n=69  W=7/L=62  WR=10.1%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 60-70 strong; session=ny_mid  •  ONLY when 4h trend WITH trade

### L03.  `RSI=RSI5 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=146  W=27/L=119  WR=18.5%
- Sharpen: sharpest is T4=T4a (62/119 of losers there)
- **Sharp: n=69  W=7/L=62  WR=10.1%**
- **Dir: SHORT**  •  RSI 60-70 strong; session=ny_mid  •  ONLY when 4h trend WITH trade

### L04.  `T1=T1c AND RSI=RSI5 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=146  W=27/L=119  WR=18.5%
- Sharpen: sharpest is T4=T4a (62/119 of losers there)
- **Sharp: n=69  W=7/L=62  WR=10.1%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 60-70 strong; session=ny_mid  •  ONLY when 4h trend WITH trade

### L05.  `H20=H20e AND T4=T4c AND session_bucket=london_open`
- Raw: n=138  W=52/L=86  WR=37.7%
- Sharpen: sharpest is ZS=ZS5 (34/86 of losers there)
- **Sharp: n=34  W=0/L=34  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; session=london_open  •  ONLY when zscore +2 to +3 deep overbought

### L06.  `T1=T1c AND BBP=BBP4 AND session_bucket=ny_mid`
- Raw: n=128  W=38/L=90  WR=29.7%
- Sharpen: sharpest is T4=T4a (64/90 of losers there)
- **Sharp: n=70  W=6/L=64  WR=8.6%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; session=ny_mid  •  ONLY when 4h trend WITH trade

### L07.  `BBP=BBP4 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=128  W=38/L=90  WR=29.7%
- Sharpen: sharpest is T4=T4a (64/90 of losers there)
- **Sharp: n=70  W=6/L=64  WR=8.6%**
- **Dir: SHORT**  •  upper third; session=ny_mid  •  ONLY when 4h trend WITH trade

### L08.  `T1=T1c AND BBP=BBP4 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=128  W=38/L=90  WR=29.7%
- Sharpen: sharpest is T4=T4a (64/90 of losers there)
- **Sharp: n=70  W=6/L=64  WR=8.6%**
- **Dir: SHORT**  •  1h trend AGAINST trade; upper third; session=ny_mid  •  ONLY when 4h trend WITH trade

### L09.  `T4=T4a AND BBP=BBP4 AND session_bucket=ny_mid`
- Raw: n=122  W=44/L=78  WR=36.1%
- Sharpen: sharpest is T1=T1c (64/78 of losers there)
- **Sharp: n=70  W=6/L=64  WR=8.6%**
- **Dir: ?**  •  4h trend WITH trade; upper third; session=ny_mid  •  ONLY when 1h trend AGAINST trade

### L10.  `T1=T1c AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=110  W=26/L=84  WR=23.6%
- Sharpen: sharpest is T4=T4a (59/84 of losers there)
- **Sharp: n=65  W=6/L=59  WR=9.2%**
- **Dir: ?**  •  1h trend AGAINST trade; zscore +1 to +2 overbought; session=ny_mid  •  ONLY when 4h trend WITH trade

### L11.  `ZS=ZS4 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=110  W=26/L=84  WR=23.6%
- Sharpen: sharpest is T4=T4a (59/84 of losers there)
- **Sharp: n=65  W=6/L=59  WR=9.2%**
- **Dir: SHORT**  •  zscore +1 to +2 overbought; session=ny_mid  •  ONLY when 4h trend WITH trade

### L12.  `T1=T1c AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=110  W=26/L=84  WR=23.6%
- Sharpen: sharpest is T4=T4a (59/84 of losers there)
- **Sharp: n=65  W=6/L=59  WR=9.2%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; zscore +1 to +2 overbought; session=ny_mid  •  ONLY when 4h trend WITH trade

### L13.  `T1=T1c AND ZS=ZS4 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=110  W=26/L=84  WR=23.6%
- Sharpen: sharpest is T4=T4a (59/84 of losers there)
- **Sharp: n=65  W=6/L=59  WR=9.2%**
- **Dir: SHORT**  •  1h trend AGAINST trade; zscore +1 to +2 overbought; session=ny_mid  •  ONLY when 4h trend WITH trade

### L14.  `BBP=BBP4 AND ZS=ZS4 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=110  W=26/L=84  WR=23.6%
- Sharpen: sharpest is T4=T4a (59/84 of losers there)
- **Sharp: n=65  W=6/L=59  WR=9.2%**
- **Dir: SHORT**  •  upper third; zscore +1 to +2 overbought; session=ny_mid  •  ONLY when 4h trend WITH trade

### L15.  `T1=T1c AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=109  W=10/L=99  WR=9.2%
- Sharpen: sharpest is H20=H20b (20/99 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; session=ny_mid  •  ONLY when HTF20 slightly aligned

### L16.  `T4=T4a AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=109  W=10/L=99  WR=9.2%
- Sharpen: sharpest is H20=H20b (20/99 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: SHORT**  •  4h trend WITH trade; session=ny_mid  •  ONLY when HTF20 slightly aligned

### L17.  `T1=T1c AND T4=T4a AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=109  W=10/L=99  WR=9.2%
- Sharpen: sharpest is H20=H20b (20/99 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend WITH trade; session=ny_mid  •  ONLY when HTF20 slightly aligned

### L18.  `T4=T4a AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=108  W=39/L=69  WR=36.1%
- Sharpen: sharpest is T1=T1c (59/69 of losers there)
- **Sharp: n=65  W=6/L=59  WR=9.2%**
- **Dir: ?**  •  4h trend WITH trade; zscore +1 to +2 overbought; session=ny_mid  •  ONLY when 1h trend AGAINST trade

### L19.  `T4=T4a AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=108  W=39/L=69  WR=36.1%
- Sharpen: sharpest is T1=T1c (59/69 of losers there)
- **Sharp: n=65  W=6/L=59  WR=9.2%**
- **Dir: ?**  •  4h trend WITH trade; upper third; zscore +1 to +2 overbought; session=ny_mid  •  ONLY when 1h trend AGAINST trade

### L20.  `T4=T4c AND direction_exec=long AND session_bucket=london_open`
- Raw: n=106  W=37/L=69  WR=34.9%
- Sharpen: sharpest is RSI=RSI5 (35/69 of losers there)
- **Sharp: n=36  W=1/L=35  WR=2.8%**
- **Dir: LONG**  •  4h trend AGAINST trade; session=london_open  •  ONLY when RSI 60-70 strong

### L21.  `H60=H60a AND T4=T4c AND RSI=RSI5`
- Raw: n=105  W=39/L=66  WR=37.1%
- Sharpen: sharpest is session_bucket=london_open (36/66 of losers there)
- **Sharp: n=51  W=15/L=36  WR=29.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when session=london_open

### L22.  `H60=H60a AND T1=T1c AND T4=T4c AND RSI=RSI5`
- Raw: n=105  W=39/L=66  WR=37.1%
- Sharpen: sharpest is session_bucket=london_open (36/66 of losers there)
- **Sharp: n=51  W=15/L=36  WR=29.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when session=london_open

### L23.  `H60=H60a AND T4=T4c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=105  W=39/L=66  WR=37.1%
- Sharpen: sharpest is session_bucket=london_open (36/66 of losers there)
- **Sharp: n=51  W=15/L=36  WR=29.4%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when session=london_open

### L24.  `H20=H20a AND T1=T1c AND session_bucket=ny_mid`
- Raw: n=100  W=17/L=83  WR=17.0%
- Sharpen: sharpest is T4=T4a (61/83 of losers there)
- **Sharp: n=70  W=9/L=61  WR=12.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; session=ny_mid  •  ONLY when 4h trend WITH trade

### L25.  `H20=H20a AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=100  W=17/L=83  WR=17.0%
- Sharpen: sharpest is T4=T4a (61/83 of losers there)
- **Sharp: n=70  W=9/L=61  WR=12.9%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; session=ny_mid  •  ONLY when 4h trend WITH trade

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | H60e(38/30) | H60a(31/38) |
| T1 | T1a(57/40) | T1c(43/60) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(56/42) | short(44/58) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
