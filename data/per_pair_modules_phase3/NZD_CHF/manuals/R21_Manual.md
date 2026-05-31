# NZD_CHF — R21 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **1,287**  (W=834 / L=453)  -  WR: **64.8%**

## Session distribution

- ny_mid: n=584  W=390/L=194  WR=66.8%
- london_open: n=261  W=168/L=93  WR=64.4%
- ny_open: n=233  W=140/L=93  WR=60.1%
- london: n=92  W=57/L=35  WR=62.0%
- ny_close: n=59  W=42/L=17  WR=71.2%
- asia: n=31  W=20/L=11  WR=64.5%
- off_hours: n=27  W=17/L=10  WR=63.0%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60a AND T1=T1a AND direction_exec=long`
- Raw: n=240  W=206/L=34  WR=85.8%
- Refine: exclude H20=H20c drops 21/34 losers (62%)
- **Final: n=159  W=146/L=13  WR=91.8%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade  •  AVOID when HTF20 neutral

### W02.  `H60=H60a AND T1=T1a AND RSI=RSI5`
- Raw: n=174  W=151/L=23  WR=86.8%
- Refine: exclude H20=H20c drops 14/23 losers (61%)
- **Final: n=140  W=131/L=9  WR=93.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when HTF20 neutral

### W03.  `H60=H60a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=174  W=151/L=23  WR=86.8%
- Refine: exclude H20=H20c drops 14/23 losers (61%)
- **Final: n=140  W=131/L=9  WR=93.6%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 60-70 strong  •  AVOID when HTF20 neutral

### W04.  `H60=H60a AND T1=T1a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=174  W=151/L=23  WR=86.8%
- Refine: exclude H20=H20c drops 14/23 losers (61%)
- **Final: n=140  W=131/L=9  WR=93.6%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when HTF20 neutral

### W05.  `T1=T1a AND T4=T4c AND RSI=RSI5`
- Raw: n=167  W=145/L=22  WR=86.8%
- Refine: exclude H20=H20c drops 6/22 losers (27%)
- **Final: n=159  W=143/L=16  WR=89.9%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when HTF20 neutral

### W06.  `T4=T4c AND RSI=RSI5 AND direction_exec=long`
- Raw: n=167  W=145/L=22  WR=86.8%
- Refine: exclude H20=H20c drops 6/22 losers (27%)
- **Final: n=159  W=143/L=16  WR=89.9%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when HTF20 neutral

### W07.  `T1=T1a AND T4=T4c AND RSI=RSI5 AND direction_exec=long`
- Raw: n=167  W=145/L=22  WR=86.8%
- Refine: exclude H20=H20c drops 6/22 losers (27%)
- **Final: n=159  W=143/L=16  WR=89.9%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when HTF20 neutral

### W08.  `H20=H20a AND T1=T1a AND direction_exec=long`
- Raw: n=151  W=131/L=20  WR=86.8%
- Refine: exclude H60=H60e drops 13/20 losers (65%)
- **Final: n=130  W=123/L=7  WR=94.6%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade  •  AVOID when HTF60 strongly against

### W09.  `H20=H20a AND H60=H60a AND RSI=RSI5`
- Raw: n=148  W=128/L=20  WR=86.5%
- Refine: exclude T1=T1c drops 18/20 losers (90%)
- **Final: n=109  W=107/L=2  WR=98.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 60-70 strong  •  AVOID when 1h trend AGAINST trade

### W10.  `T1=T1a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=147  W=131/L=16  WR=89.1%
- Refine: exclude H20=H20c drops 8/16 losers (50%)
- **Final: n=121  W=113/L=8  WR=93.4%**
- **Dir: LONG**  •  1h trend WITH trade; session=london_open  •  AVOID when HTF20 neutral

### W11.  `T1=T1a AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=145  W=131/L=14  WR=90.3%
- Refine: exclude H20=H20c drops 8/14 losers (57%)
- **Final: n=119  W=113/L=6  WR=95.0%**
- **Dir: ?**  •  1h trend WITH trade; RSI 60-70 strong; session=london_open  •  AVOID when HTF20 neutral

### W12.  `RSI=RSI5 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=145  W=131/L=14  WR=90.3%
- Refine: exclude H20=H20c drops 8/14 losers (57%)
- **Final: n=119  W=113/L=6  WR=95.0%**
- **Dir: LONG**  •  RSI 60-70 strong; session=london_open  •  AVOID when HTF20 neutral

### W13.  `T1=T1a AND RSI=RSI5 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=145  W=131/L=14  WR=90.3%
- Refine: exclude H20=H20c drops 8/14 losers (57%)
- **Final: n=119  W=113/L=6  WR=95.0%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 60-70 strong; session=london_open  •  AVOID when HTF20 neutral

### W14.  `H20=H20a AND T1=T1a AND RSI=RSI5`
- Raw: n=130  W=116/L=14  WR=89.2%
- Refine: exclude H60=H60e drops 11/14 losers (79%)
- **Final: n=111  W=108/L=3  WR=97.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when HTF60 strongly against

### W15.  `H20=H20a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=130  W=116/L=14  WR=89.2%
- Refine: exclude H60=H60e drops 11/14 losers (79%)
- **Final: n=111  W=108/L=3  WR=97.3%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 60-70 strong  •  AVOID when HTF60 strongly against

### W16.  `H20=H20a AND T1=T1a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=130  W=116/L=14  WR=89.2%
- Refine: exclude H60=H60e drops 11/14 losers (79%)
- **Final: n=111  W=108/L=3  WR=97.3%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when HTF60 strongly against

### W17.  `H20=H20a AND H60=H60a AND T1=T1a`
- Raw: n=128  W=122/L=6  WR=95.3%
- Refine: exclude RSI=RSI4 drops 4/6 losers (67%)
- **Final: n=109  W=107/L=2  WR=98.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade  •  AVOID when RSI 50-60 upper neutral

### W18.  `H20=H20a AND H60=H60a AND direction_exec=long`
- Raw: n=128  W=122/L=6  WR=95.3%
- Refine: exclude RSI=RSI4 drops 4/6 losers (67%)
- **Final: n=109  W=107/L=2  WR=98.2%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade  •  AVOID when RSI 50-60 upper neutral

### W19.  `H20=H20a AND H60=H60a AND T1=T1a AND direction_exec=long`
- Raw: n=128  W=122/L=6  WR=95.3%
- Refine: exclude RSI=RSI4 drops 4/6 losers (67%)
- **Final: n=109  W=107/L=2  WR=98.2%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade  •  AVOID when RSI 50-60 upper neutral

### W20.  `H60=H60a AND T1=T1a AND T4=T4c`
- Raw: n=125  W=109/L=16  WR=87.2%
- Refine: exclude H20=H20c drops 12/16 losers (75%)
- **Final: n=95  W=91/L=4  WR=95.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade  •  AVOID when HTF20 neutral

### W21.  `H60=H60a AND T1=T1a AND BBP=BBP4`
- Raw: n=125  W=108/L=17  WR=86.4%
- Refine: exclude H20=H20c drops 11/17 losers (65%)
- **Final: n=96  W=90/L=6  WR=93.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; upper third  •  AVOID when HTF20 neutral

### W22.  `H60=H60a AND BBP=BBP4 AND direction_exec=long`
- Raw: n=125  W=108/L=17  WR=86.4%
- Refine: exclude H20=H20c drops 11/17 losers (65%)
- **Final: n=96  W=90/L=6  WR=93.8%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; upper third  •  AVOID when HTF20 neutral

### W23.  `H60=H60a AND T1=T1a AND BBP=BBP4 AND direction_exec=long`
- Raw: n=125  W=108/L=17  WR=86.4%
- Refine: exclude H20=H20c drops 11/17 losers (65%)
- **Final: n=96  W=90/L=6  WR=93.8%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; upper third  •  AVOID when HTF20 neutral

### W24.  `H20=H20a AND H60=H60a AND BBP=BBP4`
- Raw: n=121  W=111/L=10  WR=91.7%
- Refine: exclude session_bucket=ny_mid drops 9/10 losers (90%)
- **Final: n=65  W=64/L=1  WR=98.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; upper third  •  AVOID when session=ny_mid

### W25.  `H60=H60a AND T4=T4c AND direction_exec=long`
- Raw: n=121  W=105/L=16  WR=86.8%
- Refine: exclude H20=H20c drops 12/16 losers (75%)
- **Final: n=91  W=87/L=4  WR=95.6%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade  •  AVOID when HTF20 neutral

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND T1=T1c AND direction_exec=short`
- Raw: n=211  W=79/L=132  WR=37.4%
- Sharpen: sharpest is H20=H20e (79/132 of losers there)
- **Sharp: n=101  W=22/L=79  WR=21.8%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade  •  ONLY when HTF20 strongly against

### L02.  `H60=H60e AND T1=T1c AND RSI=RSI5`
- Raw: n=150  W=52/L=98  WR=34.7%
- Sharpen: sharpest is H20=H20e (70/98 of losers there)
- **Sharp: n=82  W=12/L=70  WR=14.6%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when HTF20 strongly against

### L03.  `H60=H60e AND RSI=RSI5 AND direction_exec=short`
- Raw: n=150  W=52/L=98  WR=34.7%
- Sharpen: sharpest is H20=H20e (70/98 of losers there)
- **Sharp: n=82  W=12/L=70  WR=14.6%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 60-70 strong  •  ONLY when HTF20 strongly against

### L04.  `H60=H60e AND T1=T1c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=150  W=52/L=98  WR=34.7%
- Sharpen: sharpest is H20=H20e (70/98 of losers there)
- **Sharp: n=82  W=12/L=70  WR=14.6%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when HTF20 strongly against

### L05.  `T1=T1c AND T4=T4a AND RSI=RSI5`
- Raw: n=137  W=46/L=91  WR=33.6%
- Sharpen: sharpest is H20=H20e (55/91 of losers there)
- **Sharp: n=66  W=11/L=55  WR=16.7%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when HTF20 strongly against

### L06.  `T4=T4a AND RSI=RSI5 AND direction_exec=short`
- Raw: n=137  W=46/L=91  WR=33.6%
- Sharpen: sharpest is H20=H20e (55/91 of losers there)
- **Sharp: n=66  W=11/L=55  WR=16.7%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 60-70 strong  •  ONLY when HTF20 strongly against

### L07.  `T1=T1c AND T4=T4a AND RSI=RSI5 AND direction_exec=short`
- Raw: n=137  W=46/L=91  WR=33.6%
- Sharpen: sharpest is H20=H20e (55/91 of losers there)
- **Sharp: n=66  W=11/L=55  WR=16.7%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when HTF20 strongly against

### L08.  `H20=H20e AND T1=T1c AND direction_exec=short`
- Raw: n=131  W=46/L=85  WR=35.1%
- Sharpen: sharpest is H60=H60e (79/85 of losers there)
- **Sharp: n=101  W=22/L=79  WR=21.8%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade  •  ONLY when HTF60 strongly against

### L09.  `H20=H20e AND H60=H60e AND RSI=RSI5`
- Raw: n=129  W=50/L=79  WR=38.8%
- Sharpen: sharpest is T1=T1c (70/79 of losers there)
- **Sharp: n=82  W=12/L=70  WR=14.6%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 60-70 strong  •  ONLY when 1h trend AGAINST trade

### L10.  `H60=H60e AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=125  W=45/L=80  WR=36.0%
- Sharpen: sharpest is session_bucket=london_open (32/80 of losers there)
- **Sharp: n=33  W=1/L=32  WR=3.0%**
- **Dir: ?**  •  HTF60 strongly against; upper third; zscore +1 to +2 overbought  •  ONLY when session=london_open

### L11.  `T1=T1c AND direction_exec=short AND session_bucket=london_open`
- Raw: n=114  W=37/L=77  WR=32.5%
- Sharpen: sharpest is ZS=ZS4 (39/77 of losers there)
- **Sharp: n=48  W=9/L=39  WR=18.8%**
- **Dir: SHORT**  •  1h trend AGAINST trade; session=london_open  •  ONLY when zscore +1 to +2 overbought

### L12.  `H60=H60e AND T1=T1c AND T4=T4c`
- Raw: n=109  W=42/L=67  WR=38.5%
- Sharpen: sharpest is BBP=BBP4 (36/67 of losers there)
- **Sharp: n=37  W=1/L=36  WR=2.7%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when upper third

### L13.  `H60=H60e AND T1=T1c AND T4=T4c AND direction_exec=short`
- Raw: n=109  W=42/L=67  WR=38.5%
- Sharpen: sharpest is BBP=BBP4 (36/67 of losers there)
- **Sharp: n=37  W=1/L=36  WR=2.7%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when upper third

### L14.  `T1=T1c AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=108  W=31/L=77  WR=28.7%
- Sharpen: sharpest is ZS=ZS4 (39/77 of losers there)
- **Sharp: n=42  W=3/L=39  WR=7.1%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 60-70 strong; session=london_open  •  ONLY when zscore +1 to +2 overbought

### L15.  `RSI=RSI5 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=108  W=31/L=77  WR=28.7%
- Sharpen: sharpest is ZS=ZS4 (39/77 of losers there)
- **Sharp: n=42  W=3/L=39  WR=7.1%**
- **Dir: SHORT**  •  RSI 60-70 strong; session=london_open  •  ONLY when zscore +1 to +2 overbought

### L16.  `T1=T1c AND RSI=RSI5 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=108  W=31/L=77  WR=28.7%
- Sharpen: sharpest is ZS=ZS4 (39/77 of losers there)
- **Sharp: n=42  W=3/L=39  WR=7.1%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 60-70 strong; session=london_open  •  ONLY when zscore +1 to +2 overbought

### L17.  `H20=H20e AND T1=T1c AND RSI=RSI5`
- Raw: n=106  W=30/L=76  WR=28.3%
- Sharpen: sharpest is H60=H60e (70/76 of losers there)
- **Sharp: n=82  W=12/L=70  WR=14.6%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when HTF60 strongly against

### L18.  `H20=H20e AND RSI=RSI5 AND direction_exec=short`
- Raw: n=106  W=30/L=76  WR=28.3%
- Sharpen: sharpest is H60=H60e (70/76 of losers there)
- **Sharp: n=82  W=12/L=70  WR=14.6%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 60-70 strong  •  ONLY when HTF60 strongly against

### L19.  `H20=H20e AND T1=T1c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=106  W=30/L=76  WR=28.3%
- Sharpen: sharpest is H60=H60e (70/76 of losers there)
- **Sharp: n=82  W=12/L=70  WR=14.6%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 60-70 strong  •  ONLY when HTF60 strongly against

### L20.  `H60=H60e AND T1=T1c AND T4=T4a`
- Raw: n=106  W=39/L=67  WR=36.8%
- Sharpen: sharpest is H20=H20e (55/67 of losers there)
- **Sharp: n=68  W=13/L=55  WR=19.1%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when HTF20 strongly against

### L21.  `H60=H60e AND T4=T4a AND direction_exec=short`
- Raw: n=106  W=39/L=67  WR=36.8%
- Sharpen: sharpest is H20=H20e (55/67 of losers there)
- **Sharp: n=68  W=13/L=55  WR=19.1%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend WITH trade  •  ONLY when HTF20 strongly against

### L22.  `T1=T1c AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=105  W=42/L=63  WR=40.0%
- Sharpen: sharpest is T4=T4c (35/63 of losers there)
- **Sharp: n=42  W=7/L=35  WR=16.7%**
- **Dir: SHORT**  •  1h trend AGAINST trade; session=ny_open  •  ONLY when 4h trend AGAINST trade

### L23.  `H60=H60e AND T1=T1c AND T4=T4a AND direction_exec=short`
- Raw: n=102  W=37/L=65  WR=36.3%
- Sharpen: sharpest is H20=H20e (55/65 of losers there)
- **Sharp: n=68  W=13/L=55  WR=19.1%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when HTF20 strongly against

### L24.  `H20=H20e AND H60=H60e AND T1=T1c`
- Raw: n=101  W=22/L=79  WR=21.8%
- Sharpen: sharpest is BBP=BBP4 (48/79 of losers there)
- **Sharp: n=51  W=3/L=48  WR=5.9%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade  •  ONLY when upper third

### L25.  `H20=H20e AND H60=H60e AND direction_exec=short`
- Raw: n=101  W=22/L=79  WR=21.8%
- Sharpen: sharpest is BBP=BBP4 (48/79 of losers there)
- **Sharp: n=51  W=3/L=48  WR=5.9%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against  •  ONLY when upper third

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | H20e(24/30) |
| H60 | H60a(37/16), H60d(15/7) | H60e(18/39), H60b(8/14) |
| T1 | T1a(59/34) | T1c(41/66) |
| T4 | T4c(52/43) | T4a(45/54) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(57/36) | short(43/64) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
