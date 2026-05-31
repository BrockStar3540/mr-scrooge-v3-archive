# CAD_JPY — R27 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **3,131**  (W=1,987 / L=1,144)  -  WR: **63.5%**

## Session distribution

- asia: n=1249  W=809/L=440  WR=64.8%
- ny_close: n=533  W=333/L=200  WR=62.5%
- london_open: n=415  W=265/L=150  WR=63.9%
- london: n=314  W=198/L=116  WR=63.1%
- asia_late: n=244  W=148/L=96  WR=60.7%
- ny_open: n=189  W=119/L=70  WR=63.0%
- off_hours: n=98  W=63/L=35  WR=64.3%
- ny_mid: n=89  W=52/L=37  WR=58.4%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1a AND T4=T4a AND ZS=ZS1 AND direction_exec=long`
- Raw: n=105  W=90/L=15  WR=85.7%
- Refine: exclude session_bucket=asia drops 10/15 losers (67%)
- **Final: n=64  W=59/L=5  WR=92.2%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  AVOID when session=asia

### W02.  `H60=H60a AND T4=T4c AND BBP=BBP4`
- Raw: n=94  W=85/L=9  WR=90.4%
- Refine: exclude session_bucket=london_open drops 4/9 losers (44%)
- **Final: n=88  W=83/L=5  WR=94.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; upper third  •  AVOID when session=london_open

### W03.  `T4=T4c AND BBP=BBP4 AND direction_exec=long`
- Raw: n=94  W=85/L=9  WR=90.4%
- Refine: exclude session_bucket=london_open drops 4/9 losers (44%)
- **Final: n=88  W=83/L=5  WR=94.3%**
- **Dir: LONG**  •  4h trend AGAINST trade; upper third  •  AVOID when session=london_open

### W04.  `H60=H60a AND T4=T4c AND BBP=BBP4 AND direction_exec=long`
- Raw: n=94  W=85/L=9  WR=90.4%
- Refine: exclude session_bucket=london_open drops 4/9 losers (44%)
- **Final: n=88  W=83/L=5  WR=94.3%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; upper third  •  AVOID when session=london_open

### W05.  `H60=H60a AND RSI=RSI5 AND session_bucket=ny_open`
- Raw: n=90  W=82/L=8  WR=91.1%
- Refine: exclude ZS=ZS5 drops 6/8 losers (75%)
- **Final: n=73  W=71/L=2  WR=97.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 60-70 strong; session=ny_open  •  AVOID when zscore +2 to +3 deep overbought

### W06.  `T1=T1a AND RSI=RSI5 AND session_bucket=ny_open`
- Raw: n=90  W=82/L=8  WR=91.1%
- Refine: exclude ZS=ZS5 drops 6/8 losers (75%)
- **Final: n=73  W=71/L=2  WR=97.3%**
- **Dir: ?**  •  1h trend WITH trade; RSI 60-70 strong; session=ny_open  •  AVOID when zscore +2 to +3 deep overbought

### W07.  `RSI=RSI5 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=90  W=82/L=8  WR=91.1%
- Refine: exclude ZS=ZS5 drops 6/8 losers (75%)
- **Final: n=73  W=71/L=2  WR=97.3%**
- **Dir: LONG**  •  RSI 60-70 strong; session=ny_open  •  AVOID when zscore +2 to +3 deep overbought

### W08.  `H60=H60a AND T1=T1a AND RSI=RSI5 AND session_bucket=ny_open`
- Raw: n=90  W=82/L=8  WR=91.1%
- Refine: exclude ZS=ZS5 drops 6/8 losers (75%)
- **Final: n=73  W=71/L=2  WR=97.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong; session=ny_open  •  AVOID when zscore +2 to +3 deep overbought

### W09.  `H60=H60a AND RSI=RSI5 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=90  W=82/L=8  WR=91.1%
- Refine: exclude ZS=ZS5 drops 6/8 losers (75%)
- **Final: n=73  W=71/L=2  WR=97.3%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 60-70 strong; session=ny_open  •  AVOID when zscore +2 to +3 deep overbought

### W10.  `T1=T1a AND RSI=RSI5 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=90  W=82/L=8  WR=91.1%
- Refine: exclude ZS=ZS5 drops 6/8 losers (75%)
- **Final: n=73  W=71/L=2  WR=97.3%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 60-70 strong; session=ny_open  •  AVOID when zscore +2 to +3 deep overbought

### W11.  `H60=H60a AND T1=T1a AND T4=T4c AND BBP=BBP4`
- Raw: n=88  W=79/L=9  WR=89.8%
- Refine: exclude session_bucket=london_open drops 4/9 losers (44%)
- **Final: n=82  W=77/L=5  WR=93.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade; upper third  •  AVOID when session=london_open

### W12.  `T1=T1a AND T4=T4c AND BBP=BBP4 AND direction_exec=long`
- Raw: n=88  W=79/L=9  WR=89.8%
- Refine: exclude session_bucket=london_open drops 4/9 losers (44%)
- **Final: n=82  W=77/L=5  WR=93.9%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend AGAINST trade; upper third  •  AVOID when session=london_open

### W13.  `T4=T4a AND RSI=RSI5 AND session_bucket=ny_open`
- Raw: n=88  W=75/L=13  WR=85.2%
- Refine: exclude H60=H60e drops 5/13 losers (38%)
- **Final: n=81  W=73/L=8  WR=90.1%**
- **Dir: ?**  •  4h trend WITH trade; RSI 60-70 strong; session=ny_open  •  AVOID when HTF60 strongly against

### W14.  `H60=H60a AND T4=T4c AND ZS=ZS4`
- Raw: n=82  W=73/L=9  WR=89.0%
- Refine: exclude session_bucket=london_open drops 4/9 losers (44%)
- **Final: n=76  W=71/L=5  WR=93.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  AVOID when session=london_open

### W15.  `T4=T4c AND ZS=ZS4 AND direction_exec=long`
- Raw: n=82  W=73/L=9  WR=89.0%
- Refine: exclude session_bucket=london_open drops 4/9 losers (44%)
- **Final: n=76  W=71/L=5  WR=93.4%**
- **Dir: LONG**  •  4h trend AGAINST trade; zscore +1 to +2 overbought  •  AVOID when session=london_open

### W16.  `H60=H60a AND T4=T4c AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=82  W=73/L=9  WR=89.0%
- Refine: exclude session_bucket=london_open drops 4/9 losers (44%)
- **Final: n=76  W=71/L=5  WR=93.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; upper third; zscore +1 to +2 overbought  •  AVOID when session=london_open

### W17.  `H60=H60a AND T4=T4c AND ZS=ZS4 AND direction_exec=long`
- Raw: n=82  W=73/L=9  WR=89.0%
- Refine: exclude session_bucket=london_open drops 4/9 losers (44%)
- **Final: n=76  W=71/L=5  WR=93.4%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  AVOID when session=london_open

### W18.  `T4=T4c AND BBP=BBP4 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=82  W=73/L=9  WR=89.0%
- Refine: exclude session_bucket=london_open drops 4/9 losers (44%)
- **Final: n=76  W=71/L=5  WR=93.4%**
- **Dir: LONG**  •  4h trend AGAINST trade; upper third; zscore +1 to +2 overbought  •  AVOID when session=london_open

### W19.  `H60=H60a AND T4=T4a AND RSI=RSI5 AND session_bucket=ny_open`
- Raw: n=81  W=73/L=8  WR=90.1%
- Refine: exclude ZS=ZS5 drops 6/8 losers (75%)
- **Final: n=64  W=62/L=2  WR=96.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 60-70 strong; session=ny_open  •  AVOID when zscore +2 to +3 deep overbought

### W20.  `T1=T1a AND T4=T4a AND RSI=RSI5 AND session_bucket=ny_open`
- Raw: n=81  W=73/L=8  WR=90.1%
- Refine: exclude ZS=ZS5 drops 6/8 losers (75%)
- **Final: n=64  W=62/L=2  WR=96.9%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 60-70 strong; session=ny_open  •  AVOID when zscore +2 to +3 deep overbought

### W21.  `T4=T4a AND RSI=RSI5 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=81  W=73/L=8  WR=90.1%
- Refine: exclude ZS=ZS5 drops 6/8 losers (75%)
- **Final: n=64  W=62/L=2  WR=96.9%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 60-70 strong; session=ny_open  •  AVOID when zscore +2 to +3 deep overbought

### W22.  `H60=H60a AND T1=T1a AND T4=T4c AND ZS=ZS4`
- Raw: n=78  W=69/L=9  WR=88.5%
- Refine: exclude session_bucket=london_open drops 4/9 losers (44%)
- **Final: n=72  W=67/L=5  WR=93.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  AVOID when session=london_open

### W23.  `T1=T1a AND T4=T4c AND ZS=ZS4 AND direction_exec=long`
- Raw: n=78  W=69/L=9  WR=88.5%
- Refine: exclude session_bucket=london_open drops 4/9 losers (44%)
- **Final: n=72  W=67/L=5  WR=93.1%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  AVOID when session=london_open

### W24.  `T1=T1a AND RSI=RSI5 AND ZS=ZS3 AND session_bucket=asia`
- Raw: n=72  W=62/L=10  WR=86.1%
- Refine: exclude H20=H20e drops 4/10 losers (40%)
- **Final: n=65  W=59/L=6  WR=90.8%**
- **Dir: ?**  •  1h trend WITH trade; RSI 60-70 strong; zscore -1 to +1 neutral; session=asia  •  AVOID when HTF20 strongly against

### W25.  `RSI=RSI5 AND ZS=ZS3 AND direction_exec=long AND session_bucket=asia`
- Raw: n=72  W=62/L=10  WR=86.1%
- Refine: exclude H20=H20e drops 4/10 losers (40%)
- **Final: n=65  W=59/L=6  WR=90.8%**
- **Dir: LONG**  •  RSI 60-70 strong; zscore -1 to +1 neutral; session=asia  •  AVOID when HTF20 strongly against

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND T1=T1c AND T4=T4a`
- Raw: n=103  W=39/L=64  WR=37.9%
- Sharpen: sharpest is RSI=RSI4 (45/64 of losers there)
- **Sharp: n=58  W=13/L=45  WR=22.4%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when RSI 50-60 upper neutral

### L02.  `H20=H20e AND H60=H60e AND T4=T4a`
- Raw: n=101  W=39/L=62  WR=38.6%
- Sharpen: sharpest is BBP=BBP4 (31/62 of losers there)
- **Sharp: n=36  W=5/L=31  WR=13.9%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend WITH trade  •  ONLY when upper third

### L03.  `H20=H20e AND T4=T4a AND direction_exec=short`
- Raw: n=101  W=39/L=62  WR=38.6%
- Sharpen: sharpest is BBP=BBP4 (31/62 of losers there)
- **Sharp: n=36  W=5/L=31  WR=13.9%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend WITH trade  •  ONLY when upper third

### L04.  `H20=H20e AND H60=H60e AND T4=T4a AND direction_exec=short`
- Raw: n=101  W=39/L=62  WR=38.6%
- Sharpen: sharpest is BBP=BBP4 (31/62 of losers there)
- **Sharp: n=36  W=5/L=31  WR=13.9%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; 4h trend WITH trade  •  ONLY when upper third

### L05.  `T1=T1c AND T4=T4a AND BBP=BBP4`
- Raw: n=100  W=30/L=70  WR=30.0%
- Sharpen: sharpest is session_bucket=asia (37/70 of losers there)
- **Sharp: n=42  W=5/L=37  WR=11.9%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; upper third  •  ONLY when session=asia

### L06.  `H20=H20e AND H60=H60e AND T1=T1c AND T4=T4a`
- Raw: n=97  W=35/L=62  WR=36.1%
- Sharpen: sharpest is RSI=RSI4 (43/62 of losers there)
- **Sharp: n=52  W=9/L=43  WR=17.3%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when RSI 50-60 upper neutral

### L07.  `H20=H20e AND T1=T1c AND T4=T4a AND direction_exec=short`
- Raw: n=97  W=35/L=62  WR=36.1%
- Sharpen: sharpest is RSI=RSI4 (43/62 of losers there)
- **Sharp: n=52  W=9/L=43  WR=17.3%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when RSI 50-60 upper neutral

### L08.  `H20=H20e AND T4=T4a AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=93  W=37/L=56  WR=39.8%
- Sharpen: sharpest is H60=H60e (21/56 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when HTF60 strongly against

### L09.  `T1=T1c AND T4=T4a AND ZS=ZS4`
- Raw: n=90  W=25/L=65  WR=27.8%
- Sharpen: sharpest is session_bucket=asia (37/65 of losers there)
- **Sharp: n=42  W=5/L=37  WR=11.9%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; zscore +1 to +2 overbought  •  ONLY when session=asia

### L10.  `T1=T1c AND T4=T4a AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=90  W=25/L=65  WR=27.8%
- Sharpen: sharpest is session_bucket=asia (37/65 of losers there)
- **Sharp: n=42  W=5/L=37  WR=11.9%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; upper third; zscore +1 to +2 overbought  •  ONLY when session=asia

### L11.  `T1=T1c AND T4=T4a AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=74  W=26/L=48  WR=35.1%
- Sharpen: sharpest is H60=H60e (32/48 of losers there)
- **Sharp: n=38  W=6/L=32  WR=15.8%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; upper third; RSI 50-60 upper neutral  •  ONLY when HTF60 strongly against

### L12.  `H60=H60e AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=72  W=22/L=50  WR=30.6%
- Sharpen: sharpest is BBP=BBP4 (23/50 of losers there)
- **Sharp: n=26  W=3/L=23  WR=11.5%**
- **Dir: SHORT**  •  HTF60 strongly against; session=ny_open  •  ONLY when upper third

### L13.  `H60=H60e AND T1=T1c AND session_bucket=ny_open`
- Raw: n=67  W=20/L=47  WR=29.9%
- Sharpen: sharpest is BBP=BBP4 (21/47 of losers there)
- **Sharp: n=24  W=3/L=21  WR=12.5%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; session=ny_open  •  ONLY when upper third

### L14.  `T1=T1c AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=67  W=20/L=47  WR=29.9%
- Sharpen: sharpest is BBP=BBP4 (21/47 of losers there)
- **Sharp: n=24  W=3/L=21  WR=12.5%**
- **Dir: SHORT**  •  1h trend AGAINST trade; session=ny_open  •  ONLY when upper third

### L15.  `H60=H60e AND T1=T1c AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=67  W=20/L=47  WR=29.9%
- Sharpen: sharpest is BBP=BBP4 (21/47 of losers there)
- **Sharp: n=24  W=3/L=21  WR=12.5%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; session=ny_open  •  ONLY when upper third

### L16.  `T1=T1c AND T4=T4a AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=66  W=21/L=45  WR=31.8%
- Sharpen: sharpest is H60=H60e (30/45 of losers there)
- **Sharp: n=35  W=5/L=30  WR=14.3%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when HTF60 strongly against

### L17.  `H60=H60e AND ZS=ZS3 AND session_bucket=london_open`
- Raw: n=62  W=24/L=38  WR=38.7%
- Sharpen: sharpest is BBP=BBP4 (12/38 of losers there)
- **Sharp: n=13  W=1/L=12  WR=7.7%**
- **Dir: ?**  •  HTF60 strongly against; zscore -1 to +1 neutral; session=london_open  •  ONLY when upper third

### L18.  `ZS=ZS3 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=62  W=24/L=38  WR=38.7%
- Sharpen: sharpest is BBP=BBP4 (12/38 of losers there)
- **Sharp: n=13  W=1/L=12  WR=7.7%**
- **Dir: SHORT**  •  zscore -1 to +1 neutral; session=london_open  •  ONLY when upper third

### L19.  `H60=H60e AND ZS=ZS3 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=62  W=24/L=38  WR=38.7%
- Sharpen: sharpest is BBP=BBP4 (12/38 of losers there)
- **Sharp: n=13  W=1/L=12  WR=7.7%**
- **Dir: SHORT**  •  HTF60 strongly against; zscore -1 to +1 neutral; session=london_open  •  ONLY when upper third

### L20.  `H60=H60e AND T4=T4a AND BBP=BBP4`
- Raw: n=61  W=11/L=50  WR=18.0%
- Sharpen: sharpest is H20=H20e (31/50 of losers there)
- **Sharp: n=36  W=5/L=31  WR=13.9%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; upper third  •  ONLY when HTF20 strongly against

### L21.  `T4=T4a AND BBP=BBP4 AND direction_exec=short`
- Raw: n=61  W=11/L=50  WR=18.0%
- Sharpen: sharpest is H20=H20e (31/50 of losers there)
- **Sharp: n=36  W=5/L=31  WR=13.9%**
- **Dir: SHORT**  •  4h trend WITH trade; upper third  •  ONLY when HTF20 strongly against

### L22.  `H60=H60e AND T4=T4a AND BBP=BBP4 AND direction_exec=short`
- Raw: n=61  W=11/L=50  WR=18.0%
- Sharpen: sharpest is H20=H20e (31/50 of losers there)
- **Sharp: n=36  W=5/L=31  WR=13.9%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend WITH trade; upper third  •  ONLY when HTF20 strongly against

### L23.  `H60=H60e AND T1=T1c AND T4=T4a AND BBP=BBP4`
- Raw: n=58  W=10/L=48  WR=17.2%
- Sharpen: no sharper sub-pattern
- **Sharp: n=58  W=10/L=48  WR=17.2%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade; upper third

### L24.  `T1=T1c AND T4=T4a AND BBP=BBP4 AND direction_exec=short`
- Raw: n=58  W=10/L=48  WR=17.2%
- Sharpen: no sharper sub-pattern
- **Sharp: n=58  W=10/L=48  WR=17.2%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend WITH trade; upper third

### L25.  `H20=H20e AND T1=T1c AND T4=T4a AND RSI=RSI4`
- Raw: n=58  W=13/L=45  WR=22.4%
- Sharpen: sharpest is ZS=ZS4 (23/45 of losers there)
- **Sharp: n=25  W=2/L=23  WR=8.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when zscore +1 to +2 overbought

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | H60a(56/45) | H60e(43/54) |
| T1 | T1a(56/45) | T1c(44/55) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(56/46) | short(44/54) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
