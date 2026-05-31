# USD_CHF — R38 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **1,924**  (W=1,222 / L=702)  -  WR: **63.5%**

## Session distribution

- ny_close: n=563  W=367/L=196  WR=65.2%
- ny_mid: n=443  W=270/L=173  WR=60.9%
- asia: n=318  W=204/L=114  WR=64.2%
- ny_open: n=271  W=167/L=104  WR=61.6%
- london: n=172  W=111/L=61  WR=64.5%
- london_open: n=101  W=67/L=34  WR=66.3%
- off_hours: n=56  W=36/L=20  WR=64.3%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60e AND T1=T1a AND session_bucket=ny_open`
- Raw: n=113  W=98/L=15  WR=86.7%
- Refine: exclude H20=H20c drops 14/15 losers (93%)
- **Final: n=72  W=71/L=1  WR=98.6%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; session=ny_open  •  AVOID when HTF20 neutral

### W02.  `H60=H60e AND T4=T4a AND session_bucket=ny_open`
- Raw: n=113  W=98/L=15  WR=86.7%
- Refine: exclude H20=H20c drops 14/15 losers (93%)
- **Final: n=72  W=71/L=1  WR=98.6%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; session=ny_open  •  AVOID when HTF20 neutral

### W03.  `H60=H60e AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=113  W=98/L=15  WR=86.7%
- Refine: exclude H20=H20c drops 14/15 losers (93%)
- **Final: n=72  W=71/L=1  WR=98.6%**
- **Dir: LONG**  •  HTF60 strongly against; session=ny_open  •  AVOID when HTF20 neutral

### W04.  `T1=T1a AND T4=T4a AND session_bucket=ny_open`
- Raw: n=113  W=98/L=15  WR=86.7%
- Refine: exclude H20=H20c drops 14/15 losers (93%)
- **Final: n=72  W=71/L=1  WR=98.6%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; session=ny_open  •  AVOID when HTF20 neutral

### W05.  `T4=T4a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=113  W=98/L=15  WR=86.7%
- Refine: exclude H20=H20c drops 14/15 losers (93%)
- **Final: n=72  W=71/L=1  WR=98.6%**
- **Dir: LONG**  •  4h trend WITH trade; session=ny_open  •  AVOID when HTF20 neutral

### W06.  `H60=H60e AND T1=T1a AND T4=T4a AND session_bucket=ny_open`
- Raw: n=113  W=98/L=15  WR=86.7%
- Refine: exclude H20=H20c drops 14/15 losers (93%)
- **Final: n=72  W=71/L=1  WR=98.6%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend WITH trade; session=ny_open  •  AVOID when HTF20 neutral

### W07.  `H60=H60e AND T1=T1a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=113  W=98/L=15  WR=86.7%
- Refine: exclude H20=H20c drops 14/15 losers (93%)
- **Final: n=72  W=71/L=1  WR=98.6%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend WITH trade; session=ny_open  •  AVOID when HTF20 neutral

### W08.  `H60=H60e AND T4=T4a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=113  W=98/L=15  WR=86.7%
- Refine: exclude H20=H20c drops 14/15 losers (93%)
- **Final: n=72  W=71/L=1  WR=98.6%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend WITH trade; session=ny_open  •  AVOID when HTF20 neutral

### W09.  `T1=T1a AND T4=T4a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=113  W=98/L=15  WR=86.7%
- Refine: exclude H20=H20c drops 14/15 losers (93%)
- **Final: n=72  W=71/L=1  WR=98.6%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; session=ny_open  •  AVOID when HTF20 neutral

### W10.  `T4=T4c AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=110  W=95/L=15  WR=86.4%
- Refine: exclude H60=H60c drops 11/15 losers (73%)
- **Final: n=65  W=61/L=4  WR=93.8%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 60-70 strong; session=ny_mid  •  AVOID when HTF60 neutral

### W11.  `T4=T4a AND BBP=BBP4 AND session_bucket=ny_open`
- Raw: n=102  W=92/L=10  WR=90.2%
- Refine: exclude H20=H20c drops 8/10 losers (80%)
- **Final: n=67  W=65/L=2  WR=97.0%**
- **Dir: ?**  •  4h trend WITH trade; upper third; session=ny_open  •  AVOID when HTF20 neutral

### W12.  `T1=T1a AND T4=T4a AND session_bucket=london`
- Raw: n=99  W=93/L=6  WR=93.9%
- Refine: exclude H20=H20a drops 6/6 losers (100%)
- **Final: n=80  W=80/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; session=london  •  AVOID when HTF20 aligned WITH trade

### W13.  `T1=T1a AND direction_exec=long AND session_bucket=london`
- Raw: n=99  W=93/L=6  WR=93.9%
- Refine: exclude H20=H20a drops 6/6 losers (100%)
- **Final: n=80  W=80/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend WITH trade; session=london  •  AVOID when HTF20 aligned WITH trade

### W14.  `T4=T4a AND direction_exec=long AND session_bucket=london`
- Raw: n=99  W=93/L=6  WR=93.9%
- Refine: exclude H20=H20a drops 6/6 losers (100%)
- **Final: n=80  W=80/L=0  WR=100.0%**
- **Dir: LONG**  •  4h trend WITH trade; session=london  •  AVOID when HTF20 aligned WITH trade

### W15.  `T1=T1a AND T4=T4a AND direction_exec=long AND session_bucket=london`
- Raw: n=99  W=93/L=6  WR=93.9%
- Refine: exclude H20=H20a drops 6/6 losers (100%)
- **Final: n=80  W=80/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; session=london  •  AVOID when HTF20 aligned WITH trade

### W16.  `H60=H60e AND RSI=RSI6 AND session_bucket=ny_open`
- Raw: n=99  W=85/L=14  WR=85.9%
- Refine: exclude H20=H20c drops 14/14 losers (100%)
- **Final: n=58  W=58/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; RSI 70-80 overbought; session=ny_open  •  AVOID when HTF20 neutral

### W17.  `T1=T1a AND RSI=RSI6 AND session_bucket=ny_open`
- Raw: n=99  W=85/L=14  WR=85.9%
- Refine: exclude H20=H20c drops 14/14 losers (100%)
- **Final: n=58  W=58/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; RSI 70-80 overbought; session=ny_open  •  AVOID when HTF20 neutral

### W18.  `T4=T4a AND RSI=RSI6 AND session_bucket=ny_open`
- Raw: n=99  W=85/L=14  WR=85.9%
- Refine: exclude H20=H20c drops 14/14 losers (100%)
- **Final: n=58  W=58/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend WITH trade; RSI 70-80 overbought; session=ny_open  •  AVOID when HTF20 neutral

### W19.  `RSI=RSI6 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=99  W=85/L=14  WR=85.9%
- Refine: exclude H20=H20c drops 14/14 losers (100%)
- **Final: n=58  W=58/L=0  WR=100.0%**
- **Dir: LONG**  •  RSI 70-80 overbought; session=ny_open  •  AVOID when HTF20 neutral

### W20.  `H60=H60e AND T1=T1a AND RSI=RSI6 AND session_bucket=ny_open`
- Raw: n=99  W=85/L=14  WR=85.9%
- Refine: exclude H20=H20c drops 14/14 losers (100%)
- **Final: n=58  W=58/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; RSI 70-80 overbought; session=ny_open  •  AVOID when HTF20 neutral

### W21.  `H60=H60e AND T4=T4a AND RSI=RSI6 AND session_bucket=ny_open`
- Raw: n=99  W=85/L=14  WR=85.9%
- Refine: exclude H20=H20c drops 14/14 losers (100%)
- **Final: n=58  W=58/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; RSI 70-80 overbought; session=ny_open  •  AVOID when HTF20 neutral

### W22.  `H60=H60e AND RSI=RSI6 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=99  W=85/L=14  WR=85.9%
- Refine: exclude H20=H20c drops 14/14 losers (100%)
- **Final: n=58  W=58/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 strongly against; RSI 70-80 overbought; session=ny_open  •  AVOID when HTF20 neutral

### W23.  `T1=T1a AND T4=T4a AND RSI=RSI6 AND session_bucket=ny_open`
- Raw: n=99  W=85/L=14  WR=85.9%
- Refine: exclude H20=H20c drops 14/14 losers (100%)
- **Final: n=58  W=58/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 70-80 overbought; session=ny_open  •  AVOID when HTF20 neutral

### W24.  `T1=T1a AND RSI=RSI6 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=99  W=85/L=14  WR=85.9%
- Refine: exclude H20=H20c drops 14/14 losers (100%)
- **Final: n=58  W=58/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 70-80 overbought; session=ny_open  •  AVOID when HTF20 neutral

### W25.  `T4=T4a AND RSI=RSI6 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=99  W=85/L=14  WR=85.9%
- Refine: exclude H20=H20c drops 14/14 losers (100%)
- **Final: n=58  W=58/L=0  WR=100.0%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 70-80 overbought; session=ny_open  •  AVOID when HTF20 neutral

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1c AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=129  W=50/L=79  WR=38.8%
- Sharpen: sharpest is H20=H20a (40/79 of losers there)
- **Sharp: n=40  W=0/L=40  WR=0.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; session=ny_open  •  ONLY when HTF20 aligned WITH trade

### L02.  `H20=H20a AND RSI=RSI5 AND session_bucket=ny_close`
- Raw: n=111  W=43/L=68  WR=38.7%
- Sharpen: sharpest is T4=T4c (26/68 of losers there)
- **Sharp: n=31  W=5/L=26  WR=16.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 60-70 strong; session=ny_close  •  ONLY when 4h trend AGAINST trade

### L03.  `H60=H60a AND T1=T1c AND session_bucket=ny_open`
- Raw: n=103  W=30/L=73  WR=29.1%
- Sharpen: sharpest is H20=H20a (40/73 of losers there)
- **Sharp: n=40  W=0/L=40  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=ny_open  •  ONLY when HTF20 aligned WITH trade

### L04.  `H60=H60a AND T4=T4c AND session_bucket=ny_open`
- Raw: n=103  W=30/L=73  WR=29.1%
- Sharpen: sharpest is H20=H20a (40/73 of losers there)
- **Sharp: n=40  W=0/L=40  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=ny_open  •  ONLY when HTF20 aligned WITH trade

### L05.  `H60=H60a AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=103  W=30/L=73  WR=29.1%
- Sharpen: sharpest is H20=H20a (40/73 of losers there)
- **Sharp: n=40  W=0/L=40  WR=0.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; session=ny_open  •  ONLY when HTF20 aligned WITH trade

### L06.  `T1=T1c AND T4=T4c AND session_bucket=ny_open`
- Raw: n=103  W=30/L=73  WR=29.1%
- Sharpen: sharpest is H20=H20a (40/73 of losers there)
- **Sharp: n=40  W=0/L=40  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_open  •  ONLY when HTF20 aligned WITH trade

### L07.  `T4=T4c AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=103  W=30/L=73  WR=29.1%
- Sharpen: sharpest is H20=H20a (40/73 of losers there)
- **Sharp: n=40  W=0/L=40  WR=0.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; session=ny_open  •  ONLY when HTF20 aligned WITH trade

### L08.  `H60=H60a AND T1=T1c AND T4=T4c AND session_bucket=ny_open`
- Raw: n=103  W=30/L=73  WR=29.1%
- Sharpen: sharpest is H20=H20a (40/73 of losers there)
- **Sharp: n=40  W=0/L=40  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_open  •  ONLY when HTF20 aligned WITH trade

### L09.  `H60=H60a AND T1=T1c AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=103  W=30/L=73  WR=29.1%
- Sharpen: sharpest is H20=H20a (40/73 of losers there)
- **Sharp: n=40  W=0/L=40  WR=0.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=ny_open  •  ONLY when HTF20 aligned WITH trade

### L10.  `H60=H60a AND T4=T4c AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=103  W=30/L=73  WR=29.1%
- Sharpen: sharpest is H20=H20a (40/73 of losers there)
- **Sharp: n=40  W=0/L=40  WR=0.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=ny_open  •  ONLY when HTF20 aligned WITH trade

### L11.  `T1=T1c AND T4=T4c AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=103  W=30/L=73  WR=29.1%
- Sharpen: sharpest is H20=H20a (40/73 of losers there)
- **Sharp: n=40  W=0/L=40  WR=0.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_open  •  ONLY when HTF20 aligned WITH trade

### L12.  `H20=H20a AND T4=T4c AND ZS=ZS5`
- Raw: n=98  W=35/L=63  WR=35.7%
- Sharpen: sharpest is H60=H60a (57/63 of losers there)
- **Sharp: n=74  W=17/L=57  WR=23.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when HTF60 aligned WITH trade

### L13.  `H20=H20a AND H60=H60a AND ZS=ZS5`
- Raw: n=95  W=18/L=77  WR=18.9%
- Sharpen: sharpest is session_bucket=ny_open (23/77 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; zscore +2 to +3 deep overbought  •  ONLY when session=ny_open

### L14.  `H20=H20a AND T1=T1c AND ZS=ZS5`
- Raw: n=95  W=18/L=77  WR=18.9%
- Sharpen: sharpest is session_bucket=ny_open (23/77 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when session=ny_open

### L15.  `H20=H20a AND ZS=ZS5 AND direction_exec=short`
- Raw: n=95  W=18/L=77  WR=18.9%
- Sharpen: sharpest is session_bucket=ny_open (23/77 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; zscore +2 to +3 deep overbought  •  ONLY when session=ny_open

### L16.  `H20=H20a AND H60=H60a AND T1=T1c AND ZS=ZS5`
- Raw: n=95  W=18/L=77  WR=18.9%
- Sharpen: sharpest is session_bucket=ny_open (23/77 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when session=ny_open

### L17.  `H20=H20a AND H60=H60a AND ZS=ZS5 AND direction_exec=short`
- Raw: n=95  W=18/L=77  WR=18.9%
- Sharpen: sharpest is session_bucket=ny_open (23/77 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; zscore +2 to +3 deep overbought  •  ONLY when session=ny_open

### L18.  `H20=H20a AND T1=T1c AND ZS=ZS5 AND direction_exec=short`
- Raw: n=95  W=18/L=77  WR=18.9%
- Sharpen: sharpest is session_bucket=ny_open (23/77 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when session=ny_open

### L19.  `H60=H60a AND RSI=RSI6 AND session_bucket=ny_open`
- Raw: n=93  W=28/L=65  WR=30.1%
- Sharpen: sharpest is H20=H20a (40/65 of losers there)
- **Sharp: n=40  W=0/L=40  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 70-80 overbought; session=ny_open  •  ONLY when HTF20 aligned WITH trade

### L20.  `T1=T1c AND RSI=RSI6 AND session_bucket=ny_open`
- Raw: n=93  W=28/L=65  WR=30.1%
- Sharpen: sharpest is H20=H20a (40/65 of losers there)
- **Sharp: n=40  W=0/L=40  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 70-80 overbought; session=ny_open  •  ONLY when HTF20 aligned WITH trade

### L21.  `T4=T4c AND RSI=RSI6 AND session_bucket=ny_open`
- Raw: n=93  W=28/L=65  WR=30.1%
- Sharpen: sharpest is H20=H20a (40/65 of losers there)
- **Sharp: n=40  W=0/L=40  WR=0.0%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 70-80 overbought; session=ny_open  •  ONLY when HTF20 aligned WITH trade

### L22.  `RSI=RSI6 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=93  W=28/L=65  WR=30.1%
- Sharpen: sharpest is H20=H20a (40/65 of losers there)
- **Sharp: n=40  W=0/L=40  WR=0.0%**
- **Dir: SHORT**  •  RSI 70-80 overbought; session=ny_open  •  ONLY when HTF20 aligned WITH trade

### L23.  `H60=H60a AND T1=T1c AND RSI=RSI6 AND session_bucket=ny_open`
- Raw: n=93  W=28/L=65  WR=30.1%
- Sharpen: sharpest is H20=H20a (40/65 of losers there)
- **Sharp: n=40  W=0/L=40  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 70-80 overbought; session=ny_open  •  ONLY when HTF20 aligned WITH trade

### L24.  `H60=H60a AND T4=T4c AND RSI=RSI6 AND session_bucket=ny_open`
- Raw: n=93  W=28/L=65  WR=30.1%
- Sharpen: sharpest is H20=H20a (40/65 of losers there)
- **Sharp: n=40  W=0/L=40  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 70-80 overbought; session=ny_open  •  ONLY when HTF20 aligned WITH trade

### L25.  `H60=H60a AND RSI=RSI6 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=93  W=28/L=65  WR=30.1%
- Sharpen: sharpest is H20=H20a (40/65 of losers there)
- **Sharp: n=40  W=0/L=40  WR=0.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; RSI 70-80 overbought; session=ny_open  •  ONLY when HTF20 aligned WITH trade

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20e(39/29) | H20a(28/41) |
| H60 | H60e(44/33) | H60a(38/48) |
| T1 | T1a(52/43) | T1c(48/57) |
| T4 | T4a(55/42) | T4c(45/58) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(52/43) | short(48/57) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
