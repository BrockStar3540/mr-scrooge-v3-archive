# NZD_CAD — R20 Manual

## Regime centroid (locked factors)

- **BB = BB2**  (normal bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **1,516**  (W=983 / L=533)  -  WR: **64.8%**

## Session distribution

- asia: n=457  W=297/L=160  WR=65.0%
- ny_mid: n=256  W=169/L=87  WR=66.0%
- london_open: n=227  W=141/L=86  WR=62.1%
- ny_close: n=160  W=104/L=56  WR=65.0%
- ny_open: n=151  W=92/L=59  WR=60.9%
- london: n=121  W=81/L=40  WR=66.9%
- asia_late: n=108  W=76/L=32  WR=70.4%
- off_hours: n=36  W=23/L=13  WR=63.9%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1a AND T4=T4a AND session_bucket=asia`
- Raw: n=182  W=159/L=23  WR=87.4%
- Refine: exclude H20=H20e drops 5/23 losers (22%)
- **Final: n=177  W=159/L=18  WR=89.8%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; session=asia  •  AVOID when HTF20 strongly against

### W02.  `T1=T1a AND T4=T4a AND direction_exec=long AND session_bucket=asia`
- Raw: n=182  W=159/L=23  WR=87.4%
- Refine: exclude H20=H20e drops 5/23 losers (22%)
- **Final: n=177  W=159/L=18  WR=89.8%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; session=asia  •  AVOID when HTF20 strongly against

### W03.  `H20=H20a AND T4=T4a AND session_bucket=asia`
- Raw: n=171  W=151/L=20  WR=88.3%
- Refine: exclude RSI=RSI7 drops 6/20 losers (30%)
- **Final: n=151  W=137/L=14  WR=90.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=asia  •  AVOID when RSI>80 extreme overbought

### W04.  `H20=H20a AND T4=T4a AND direction_exec=long AND session_bucket=asia`
- Raw: n=165  W=145/L=20  WR=87.9%
- Refine: exclude RSI=RSI7 drops 6/20 losers (30%)
- **Final: n=145  W=131/L=14  WR=90.3%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=asia  •  AVOID when RSI>80 extreme overbought

### W05.  `H20=H20a AND T1=T1a AND T4=T4a AND session_bucket=asia`
- Raw: n=146  W=131/L=15  WR=89.7%
- Refine: exclude H60=H60b drops 6/15 losers (40%)
- **Final: n=127  W=118/L=9  WR=92.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; session=asia  •  AVOID when HTF60 slightly aligned

### W06.  `H60=H60a AND T4=T4a AND session_bucket=asia`
- Raw: n=133  W=114/L=19  WR=85.7%
- Refine: exclude H20=H20e drops 7/19 losers (37%)
- **Final: n=118  W=106/L=12  WR=89.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; session=asia  •  AVOID when HTF20 strongly against

### W07.  `T4=T4a AND BBP=BBP4 AND session_bucket=asia`
- Raw: n=123  W=109/L=14  WR=88.6%
- Refine: exclude RSI=RSI7 drops 6/14 losers (43%)
- **Final: n=111  W=103/L=8  WR=92.8%**
- **Dir: ?**  •  4h trend WITH trade; upper third; session=asia  •  AVOID when RSI>80 extreme overbought

### W08.  `H20=H20a AND H60=H60a AND T1=T1a AND BBP=BBP4`
- Raw: n=121  W=105/L=16  WR=86.8%
- Refine: exclude RSI=RSI5 drops 8/16 losers (50%)
- **Final: n=91  W=83/L=8  WR=91.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; upper third  •  AVOID when RSI 60-70 strong

### W09.  `H20=H20a AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=109  W=101/L=8  WR=92.7%
- Refine: exclude session_bucket=ny_mid drops 3/8 losers (38%)
- **Final: n=95  W=90/L=5  WR=94.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; upper third; RSI 50-60 upper neutral  •  AVOID when session=ny_mid

### W10.  `T4=T4a AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=104  W=92/L=12  WR=88.5%
- Refine: exclude T1=T1a drops 10/12 losers (83%)
- **Final: n=50  W=48/L=2  WR=96.0%**
- **Dir: ?**  •  4h trend WITH trade; RSI 60-70 strong; session=asia  •  AVOID when 1h trend WITH trade

### W11.  `T4=T4a AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=104  W=91/L=13  WR=87.5%
- Refine: exclude RSI=RSI7 drops 6/13 losers (46%)
- **Final: n=92  W=85/L=7  WR=92.4%**
- **Dir: ?**  •  4h trend WITH trade; zscore +1 to +2 overbought; session=asia  •  AVOID when RSI>80 extreme overbought

### W12.  `T4=T4a AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=104  W=91/L=13  WR=87.5%
- Refine: exclude RSI=RSI7 drops 6/13 losers (46%)
- **Final: n=92  W=85/L=7  WR=92.4%**
- **Dir: ?**  •  4h trend WITH trade; upper third; zscore +1 to +2 overbought; session=asia  •  AVOID when RSI>80 extreme overbought

### W13.  `T4=T4a AND BBP=BBP4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=103  W=89/L=14  WR=86.4%
- Refine: exclude RSI=RSI7 drops 6/14 losers (43%)
- **Final: n=91  W=83/L=8  WR=91.2%**
- **Dir: LONG**  •  4h trend WITH trade; upper third; session=asia  •  AVOID when RSI>80 extreme overbought

### W14.  `H20=H20a AND H60=H60a AND T4=T4a AND ZS=ZS4`
- Raw: n=103  W=88/L=15  WR=85.4%
- Refine: exclude RSI=RSI5 drops 8/15 losers (53%)
- **Final: n=70  W=63/L=7  WR=90.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade; zscore +1 to +2 overbought  •  AVOID when RSI 60-70 strong

### W15.  `T1=T1a AND T4=T4a AND BBP=BBP4 AND session_bucket=asia`
- Raw: n=102  W=89/L=13  WR=87.3%
- Refine: exclude RSI=RSI7 drops 6/13 losers (46%)
- **Final: n=90  W=83/L=7  WR=92.2%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; upper third; session=asia  •  AVOID when RSI>80 extreme overbought

### W16.  `H20=H20a AND H60=H60a AND ZS=ZS4 AND direction_exec=long`
- Raw: n=99  W=87/L=12  WR=87.9%
- Refine: exclude session_bucket=ny_open drops 5/12 losers (42%)
- **Final: n=84  W=77/L=7  WR=91.7%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; zscore +1 to +2 overbought  •  AVOID when session=ny_open

### W17.  `H20=H20a AND T4=T4a AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=97  W=89/L=8  WR=91.8%
- Refine: exclude session_bucket=ny_mid drops 3/8 losers (38%)
- **Final: n=83  W=78/L=5  WR=94.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; upper third; RSI 50-60 upper neutral  •  AVOID when session=ny_mid

### W18.  `H20=H20a AND H60=H60a AND T4=T4a AND session_bucket=asia`
- Raw: n=96  W=84/L=12  WR=87.5%
- Refine: exclude BBP=BBP2 drops 5/12 losers (42%)
- **Final: n=85  W=78/L=7  WR=91.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade; session=asia  •  AVOID when lower third

### W19.  `H20=H20a AND H60=H60a AND T1=T1a AND ZS=ZS4`
- Raw: n=93  W=83/L=10  WR=89.2%
- Refine: exclude RSI=RSI6 drops 5/10 losers (50%)
- **Final: n=71  W=66/L=5  WR=93.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; zscore +1 to +2 overbought  •  AVOID when RSI 70-80 overbought

### W20.  `H20=H20a AND BBP=BBP4 AND session_bucket=asia`
- Raw: n=91  W=83/L=8  WR=91.2%
- Refine: exclude RSI=RSI7 drops 6/8 losers (75%)
- **Final: n=79  W=77/L=2  WR=97.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; upper third; session=asia  •  AVOID when RSI>80 extreme overbought

### W21.  `H20=H20a AND T1=T1a AND BBP=BBP4 AND session_bucket=asia`
- Raw: n=87  W=79/L=8  WR=90.8%
- Refine: exclude RSI=RSI7 drops 6/8 losers (75%)
- **Final: n=75  W=73/L=2  WR=97.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; upper third; session=asia  •  AVOID when RSI>80 extreme overbought

### W22.  `H20=H20a AND T4=T4a AND BBP=BBP4 AND session_bucket=asia`
- Raw: n=87  W=79/L=8  WR=90.8%
- Refine: exclude RSI=RSI7 drops 6/8 losers (75%)
- **Final: n=75  W=73/L=2  WR=97.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; upper third; session=asia  •  AVOID when RSI>80 extreme overbought

### W23.  `H20=H20a AND BBP=BBP4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=87  W=79/L=8  WR=90.8%
- Refine: exclude RSI=RSI7 drops 6/8 losers (75%)
- **Final: n=75  W=73/L=2  WR=97.3%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; upper third; session=asia  •  AVOID when RSI>80 extreme overbought

### W24.  `H20=H20a AND BBP=BBP4 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=85  W=77/L=8  WR=90.6%
- Refine: exclude H60=H60e drops 4/8 losers (50%)
- **Final: n=62  W=58/L=4  WR=93.5%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; upper third; RSI 50-60 upper neutral  •  AVOID when HTF60 strongly against

### W25.  `T1=T1a AND T4=T4a AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=85  W=73/L=12  WR=85.9%
- Refine: exclude RSI=RSI7 drops 6/12 losers (50%)
- **Final: n=73  W=67/L=6  WR=91.8%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; zscore +1 to +2 overbought; session=asia  •  AVOID when RSI>80 extreme overbought

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1c AND T4=T4c AND session_bucket=asia`
- Raw: n=163  W=61/L=102  WR=37.4%
- Sharpen: sharpest is H60=H60a (44/102 of losers there)
- **Sharp: n=57  W=13/L=44  WR=22.8%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=asia  •  ONLY when HTF60 aligned WITH trade

### L02.  `T1=T1c AND T4=T4c AND direction_exec=short AND session_bucket=asia`
- Raw: n=163  W=61/L=102  WR=37.4%
- Sharpen: sharpest is H60=H60a (44/102 of losers there)
- **Sharp: n=57  W=13/L=44  WR=22.8%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=asia  •  ONLY when HTF60 aligned WITH trade

### L03.  `H20=H20e AND T1=T1c AND T4=T4c AND session_bucket=asia`
- Raw: n=120  W=43/L=77  WR=35.8%
- Sharpen: sharpest is ZS=ZS5 (20/77 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L04.  `T4=T4c AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=84  W=31/L=53  WR=36.9%
- Sharpen: sharpest is H60=H60a (23/53 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 60-70 strong; session=asia  •  ONLY when HTF60 aligned WITH trade

### L05.  `T4=T4c AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=81  W=27/L=54  WR=33.3%
- Sharpen: sharpest is session_bucket=asia (28/54 of losers there)
- **Sharp: n=28  W=0/L=28  WR=0.0%**
- **Dir: ?**  •  4h trend AGAINST trade; deep above upper band; zscore +2 to +3 deep overbought  •  ONLY when session=asia

### L06.  `T4=T4c AND BBP=BBP4 AND session_bucket=asia`
- Raw: n=77  W=28/L=49  WR=36.4%
- Sharpen: sharpest is H60=H60a (19/49 of losers there)
- **Sharp: n=25  W=6/L=19  WR=24.0%**
- **Dir: ?**  •  4h trend AGAINST trade; upper third; session=asia  •  ONLY when HTF60 aligned WITH trade

### L07.  `H20=H20e AND T1=T1c AND T4=T4c AND ZS=ZS5`
- Raw: n=71  W=27/L=44  WR=38.0%
- Sharpen: sharpest is session_bucket=asia (20/44 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when session=asia

### L08.  `H60=H60a AND T4=T4c AND session_bucket=asia`
- Raw: n=67  W=17/L=50  WR=25.4%
- Sharpen: sharpest is RSI=RSI5 (23/50 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=asia  •  ONLY when RSI 60-70 strong

### L09.  `T4=T4c AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=67  W=25/L=42  WR=37.3%
- Sharpen: sharpest is H60=H60a (18/42 of losers there)
- **Sharp: n=22  W=4/L=18  WR=18.2%**
- **Dir: ?**  •  4h trend AGAINST trade; zscore +1 to +2 overbought; session=asia  •  ONLY when HTF60 aligned WITH trade

### L10.  `T4=T4c AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=67  W=25/L=42  WR=37.3%
- Sharpen: sharpest is H60=H60a (18/42 of losers there)
- **Sharp: n=22  W=4/L=18  WR=18.2%**
- **Dir: ?**  •  4h trend AGAINST trade; upper third; zscore +1 to +2 overbought; session=asia  •  ONLY when HTF60 aligned WITH trade

### L11.  `T4=T4c AND BBP=BBP6 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=65  W=25/L=40  WR=38.5%
- Sharpen: sharpest is session_bucket=asia (23/40 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; deep above upper band; zscore +2 to +3 deep overbought  •  ONLY when session=asia

### L12.  `H20=H20e AND H60=H60a AND session_bucket=asia`
- Raw: n=64  W=21/L=43  WR=32.8%
- Sharpen: sharpest is ZS=ZS4 (18/43 of losers there)
- **Sharp: n=22  W=4/L=18  WR=18.2%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; session=asia  •  ONLY when zscore +1 to +2 overbought

### L13.  `H20=H20e AND T4=T4c AND BBP=BBP6`
- Raw: n=62  W=18/L=44  WR=29.0%
- Sharpen: sharpest is ZS=ZS5 (37/44 of losers there)
- **Sharp: n=48  W=11/L=37  WR=22.9%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; deep above upper band  •  ONLY when zscore +2 to +3 deep overbought

### L14.  `T1=T1c AND T4=T4c AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=62  W=24/L=38  WR=38.7%
- Sharpen: sharpest is session_bucket=asia (23/38 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; deep above upper band; zscore +2 to +3 deep overbought  •  ONLY when session=asia

### L15.  `H60=H60a AND T4=T4c AND direction_exec=short AND session_bucket=asia`
- Raw: n=61  W=17/L=44  WR=27.9%
- Sharpen: sharpest is RSI=RSI5 (17/44 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=asia  •  ONLY when RSI 60-70 strong

### L16.  `H60=H60e AND T1=T1c AND ZS=ZS5`
- Raw: n=61  W=23/L=38  WR=37.7%
- Sharpen: sharpest is session_bucket=london_open (10/38 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when session=london_open

### L17.  `H20=H20e AND BBP=BBP4 AND session_bucket=asia`
- Raw: n=60  W=21/L=39  WR=35.0%
- Sharpen: sharpest is RSI=RSI4 (19/39 of losers there)
- **Sharp: n=21  W=2/L=19  WR=9.5%**
- **Dir: ?**  •  HTF20 strongly against; upper third; session=asia  •  ONLY when RSI 50-60 upper neutral

### L18.  `H60=H60e AND ZS=ZS5 AND direction_exec=short`
- Raw: n=60  W=21/L=39  WR=35.0%
- Sharpen: sharpest is session_bucket=london_open (10/39 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; zscore +2 to +3 deep overbought  •  ONLY when session=london_open

### L19.  `H60=H60e AND T1=T1c AND ZS=ZS5 AND direction_exec=short`
- Raw: n=59  W=21/L=38  WR=35.6%
- Sharpen: sharpest is session_bucket=london_open (10/38 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when session=london_open

### L20.  `H20=H20e AND BBP=BBP6 AND direction_exec=short`
- Raw: n=59  W=22/L=37  WR=37.3%
- Sharpen: sharpest is T4=T4c (35/37 of losers there)
- **Sharp: n=51  W=16/L=35  WR=31.4%**
- **Dir: SHORT**  •  HTF20 strongly against; deep above upper band  •  ONLY when 4h trend AGAINST trade

### L21.  `H20=H20e AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=58  W=17/L=41  WR=29.3%
- Sharpen: sharpest is T4=T4c (37/41 of losers there)
- **Sharp: n=48  W=11/L=37  WR=22.9%**
- **Dir: ?**  •  HTF20 strongly against; deep above upper band; zscore +2 to +3 deep overbought  •  ONLY when 4h trend AGAINST trade

### L22.  `H60=H60a AND T1=T1c AND T4=T4c AND session_bucket=asia`
- Raw: n=57  W=13/L=44  WR=22.8%
- Sharpen: sharpest is RSI=RSI5 (17/44 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; session=asia  •  ONLY when RSI 60-70 strong

### L23.  `T1=T1c AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=56  W=20/L=36  WR=35.7%
- Sharpen: sharpest is RSI=RSI6 (16/36 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; zscore +2 to +3 deep overbought; session=asia  •  ONLY when RSI 70-80 overbought

### L24.  `ZS=ZS5 AND direction_exec=short AND session_bucket=asia`
- Raw: n=56  W=20/L=36  WR=35.7%
- Sharpen: sharpest is RSI=RSI6 (16/36 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: SHORT**  •  zscore +2 to +3 deep overbought; session=asia  •  ONLY when RSI 70-80 overbought

### L25.  `T1=T1c AND ZS=ZS5 AND direction_exec=short AND session_bucket=asia`
- Raw: n=56  W=20/L=36  WR=35.7%
- Sharpen: sharpest is RSI=RSI6 (16/36 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; zscore +2 to +3 deep overbought; session=asia  •  ONLY when RSI 70-80 overbought

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(45/33) | H20e(36/50) |
| H60 | H60a(45/37) | H60e(34/43) |
| T1 | T1a(52/41) | T1c(48/59) |
| T4 | T4a(56/40) | T4c(44/60) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(52/41) | short(48/59) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
