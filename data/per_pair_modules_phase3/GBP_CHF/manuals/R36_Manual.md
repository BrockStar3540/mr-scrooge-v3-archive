# GBP_CHF — R36 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **1,499**  (W=951 / L=548)  -  WR: **63.4%**

## Session distribution

- ny_close: n=445  W=278/L=167  WR=62.5%
- ny_open: n=364  W=240/L=124  WR=65.9%
- ny_mid: n=271  W=170/L=101  WR=62.7%
- asia: n=145  W=92/L=53  WR=63.4%
- london_open: n=110  W=72/L=38  WR=65.5%
- london: n=94  W=58/L=36  WR=61.7%
- off_hours: n=49  W=29/L=20  WR=59.2%
- asia_late: n=21  W=12/L=9  WR=57.1%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1a AND BBP=BBP4 AND RSI=RSI6`
- Raw: n=137  W=123/L=14  WR=89.8%
- Refine: exclude session_bucket=asia drops 6/14 losers (43%)
- **Final: n=131  W=123/L=8  WR=93.9%**
- **Dir: ?**  •  1h trend WITH trade; upper third; RSI 70-80 overbought  •  AVOID when session=asia

### W02.  `BBP=BBP4 AND RSI=RSI6 AND direction_exec=long`
- Raw: n=137  W=123/L=14  WR=89.8%
- Refine: exclude session_bucket=asia drops 6/14 losers (43%)
- **Final: n=131  W=123/L=8  WR=93.9%**
- **Dir: LONG**  •  upper third; RSI 70-80 overbought  •  AVOID when session=asia

### W03.  `T1=T1a AND BBP=BBP4 AND RSI=RSI6 AND direction_exec=long`
- Raw: n=137  W=123/L=14  WR=89.8%
- Refine: exclude session_bucket=asia drops 6/14 losers (43%)
- **Final: n=131  W=123/L=8  WR=93.9%**
- **Dir: LONG**  •  1h trend WITH trade; upper third; RSI 70-80 overbought  •  AVOID when session=asia

### W04.  `T1=T1a AND RSI=RSI6 AND ZS=ZS4`
- Raw: n=128  W=114/L=14  WR=89.1%
- Refine: exclude session_bucket=asia drops 6/14 losers (43%)
- **Final: n=122  W=114/L=8  WR=93.4%**
- **Dir: ?**  •  1h trend WITH trade; RSI 70-80 overbought; zscore +1 to +2 overbought  •  AVOID when session=asia

### W05.  `RSI=RSI6 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=128  W=114/L=14  WR=89.1%
- Refine: exclude session_bucket=asia drops 6/14 losers (43%)
- **Final: n=122  W=114/L=8  WR=93.4%**
- **Dir: LONG**  •  RSI 70-80 overbought; zscore +1 to +2 overbought  •  AVOID when session=asia

### W06.  `T1=T1a AND BBP=BBP4 AND RSI=RSI6 AND ZS=ZS4`
- Raw: n=128  W=114/L=14  WR=89.1%
- Refine: exclude session_bucket=asia drops 6/14 losers (43%)
- **Final: n=122  W=114/L=8  WR=93.4%**
- **Dir: ?**  •  1h trend WITH trade; upper third; RSI 70-80 overbought; zscore +1 to +2 overbought  •  AVOID when session=asia

### W07.  `T1=T1a AND RSI=RSI6 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=128  W=114/L=14  WR=89.1%
- Refine: exclude session_bucket=asia drops 6/14 losers (43%)
- **Final: n=122  W=114/L=8  WR=93.4%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 70-80 overbought; zscore +1 to +2 overbought  •  AVOID when session=asia

### W08.  `BBP=BBP4 AND RSI=RSI6 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=128  W=114/L=14  WR=89.1%
- Refine: exclude session_bucket=asia drops 6/14 losers (43%)
- **Final: n=122  W=114/L=8  WR=93.4%**
- **Dir: LONG**  •  upper third; RSI 70-80 overbought; zscore +1 to +2 overbought  •  AVOID when session=asia

### W09.  `H60=H60e AND T1=T1a AND RSI=RSI6`
- Raw: n=127  W=109/L=18  WR=85.8%
- Refine: exclude H20=H20d drops 9/18 losers (50%)
- **Final: n=93  W=84/L=9  WR=90.3%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; RSI 70-80 overbought  •  AVOID when HTF20 mildly against

### W10.  `H60=H60e AND RSI=RSI6 AND direction_exec=long`
- Raw: n=127  W=109/L=18  WR=85.8%
- Refine: exclude H20=H20d drops 9/18 losers (50%)
- **Final: n=93  W=84/L=9  WR=90.3%**
- **Dir: LONG**  •  HTF60 strongly against; RSI 70-80 overbought  •  AVOID when HTF20 mildly against

### W11.  `H60=H60e AND T1=T1a AND RSI=RSI6 AND direction_exec=long`
- Raw: n=127  W=109/L=18  WR=85.8%
- Refine: exclude H20=H20d drops 9/18 losers (50%)
- **Final: n=93  W=84/L=9  WR=90.3%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend WITH trade; RSI 70-80 overbought  •  AVOID when HTF20 mildly against

### W12.  `H20=H20a AND H60=H60e AND RSI=RSI6`
- Raw: n=124  W=109/L=15  WR=87.9%
- Refine: exclude T1=T1c drops 8/15 losers (53%)
- **Final: n=89  W=82/L=7  WR=92.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; RSI 70-80 overbought  •  AVOID when 1h trend AGAINST trade

### W13.  `H60=H60e AND T1=T1a AND T4=T4a AND RSI=RSI6`
- Raw: n=123  W=105/L=18  WR=85.4%
- Refine: exclude H20=H20d drops 9/18 losers (50%)
- **Final: n=93  W=84/L=9  WR=90.3%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend WITH trade; RSI 70-80 overbought  •  AVOID when HTF20 mildly against

### W14.  `H60=H60e AND T4=T4a AND RSI=RSI6 AND direction_exec=long`
- Raw: n=123  W=105/L=18  WR=85.4%
- Refine: exclude H20=H20d drops 9/18 losers (50%)
- **Final: n=93  W=84/L=9  WR=90.3%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend WITH trade; RSI 70-80 overbought  •  AVOID when HTF20 mildly against

### W15.  `H20=H20a AND T1=T1a AND RSI=RSI6`
- Raw: n=117  W=100/L=17  WR=85.5%
- Refine: exclude BBP=BBP6 drops 11/17 losers (65%)
- **Final: n=84  W=78/L=6  WR=92.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 70-80 overbought  •  AVOID when deep above upper band

### W16.  `H20=H20a AND RSI=RSI6 AND direction_exec=long`
- Raw: n=117  W=100/L=17  WR=85.5%
- Refine: exclude BBP=BBP6 drops 11/17 losers (65%)
- **Final: n=84  W=78/L=6  WR=92.9%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 70-80 overbought  •  AVOID when deep above upper band

### W17.  `H20=H20a AND T1=T1a AND RSI=RSI6 AND direction_exec=long`
- Raw: n=117  W=100/L=17  WR=85.5%
- Refine: exclude BBP=BBP6 drops 11/17 losers (65%)
- **Final: n=84  W=78/L=6  WR=92.9%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 70-80 overbought  •  AVOID when deep above upper band

### W18.  `H20=H20a AND T4=T4a AND RSI=RSI6`
- Raw: n=111  W=98/L=13  WR=88.3%
- Refine: exclude H60=H60b drops 6/13 losers (46%)
- **Final: n=99  W=92/L=7  WR=92.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 70-80 overbought  •  AVOID when HTF60 slightly aligned

### W19.  `H20=H20a AND T1=T1a AND T4=T4a AND RSI=RSI6`
- Raw: n=111  W=98/L=13  WR=88.3%
- Refine: exclude H60=H60b drops 6/13 losers (46%)
- **Final: n=99  W=92/L=7  WR=92.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; RSI 70-80 overbought  •  AVOID when HTF60 slightly aligned

### W20.  `H20=H20a AND T4=T4a AND RSI=RSI6 AND direction_exec=long`
- Raw: n=111  W=98/L=13  WR=88.3%
- Refine: exclude H60=H60b drops 6/13 losers (46%)
- **Final: n=99  W=92/L=7  WR=92.9%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 70-80 overbought  •  AVOID when HTF60 slightly aligned

### W21.  `T1=T1a AND T4=T4a AND BBP=BBP4 AND RSI=RSI6`
- Raw: n=99  W=85/L=14  WR=85.9%
- Refine: exclude session_bucket=asia drops 6/14 losers (43%)
- **Final: n=93  W=85/L=8  WR=91.4%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; upper third; RSI 70-80 overbought  •  AVOID when session=asia

### W22.  `T4=T4a AND BBP=BBP4 AND RSI=RSI6 AND direction_exec=long`
- Raw: n=99  W=85/L=14  WR=85.9%
- Refine: exclude session_bucket=asia drops 6/14 losers (43%)
- **Final: n=93  W=85/L=8  WR=91.4%**
- **Dir: LONG**  •  4h trend WITH trade; upper third; RSI 70-80 overbought  •  AVOID when session=asia

### W23.  `H20=H20a AND T4=T4a AND ZS=ZS5`
- Raw: n=98  W=86/L=12  WR=87.8%
- Refine: exclude H60=H60d drops 8/12 losers (67%)
- **Final: n=82  W=78/L=4  WR=95.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  AVOID when HTF60 mildly against

### W24.  `H60=H60a AND T1=T1a AND session_bucket=ny_open`
- Raw: n=94  W=87/L=7  WR=92.6%
- Refine: exclude ZS=ZS5 drops 7/7 losers (100%)
- **Final: n=62  W=62/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=ny_open  •  AVOID when zscore +2 to +3 deep overbought

### W25.  `H60=H60a AND T1=T1a AND RSI=RSI6`
- Raw: n=94  W=83/L=11  WR=88.3%
- Refine: exclude H20=H20e drops 11/11 losers (100%)
- **Final: n=63  W=63/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 70-80 overbought  •  AVOID when HTF20 strongly against

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1c AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=128  W=49/L=79  WR=38.3%
- Sharpen: sharpest is RSI=RSI6 (26/79 of losers there)
- **Sharp: n=27  W=1/L=26  WR=3.7%**
- **Dir: SHORT**  •  1h trend AGAINST trade; session=ny_mid  •  ONLY when RSI 70-80 overbought

### L02.  `H60=H60a AND T1=T1c AND RSI=RSI6`
- Raw: n=110  W=44/L=66  WR=40.0%
- Sharpen: sharpest is H20=H20e (47/66 of losers there)
- **Sharp: n=66  W=19/L=47  WR=28.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when HTF20 strongly against

### L03.  `H60=H60a AND RSI=RSI6 AND direction_exec=short`
- Raw: n=110  W=44/L=66  WR=40.0%
- Sharpen: sharpest is H20=H20e (47/66 of losers there)
- **Sharp: n=66  W=19/L=47  WR=28.8%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; RSI 70-80 overbought  •  ONLY when HTF20 strongly against

### L04.  `H60=H60a AND T1=T1c AND RSI=RSI6 AND direction_exec=short`
- Raw: n=110  W=44/L=66  WR=40.0%
- Sharpen: sharpest is H20=H20e (47/66 of losers there)
- **Sharp: n=66  W=19/L=47  WR=28.8%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when HTF20 strongly against

### L05.  `T1=T1c AND BBP=BBP4 AND RSI=RSI6`
- Raw: n=92  W=29/L=63  WR=31.5%
- Sharpen: sharpest is T4=T4a (19/63 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; RSI 70-80 overbought  •  ONLY when 4h trend WITH trade

### L06.  `BBP=BBP4 AND RSI=RSI6 AND direction_exec=short`
- Raw: n=92  W=29/L=63  WR=31.5%
- Sharpen: sharpest is T4=T4a (19/63 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: SHORT**  •  upper third; RSI 70-80 overbought  •  ONLY when 4h trend WITH trade

### L07.  `T1=T1c AND BBP=BBP4 AND RSI=RSI6 AND direction_exec=short`
- Raw: n=92  W=29/L=63  WR=31.5%
- Sharpen: sharpest is T4=T4a (19/63 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; upper third; RSI 70-80 overbought  •  ONLY when 4h trend WITH trade

### L08.  `H20=H20e AND T1=T1c AND RSI=RSI6`
- Raw: n=88  W=29/L=59  WR=33.0%
- Sharpen: sharpest is session_bucket=london_open (21/59 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when session=london_open

### L09.  `H20=H20e AND RSI=RSI6 AND direction_exec=short`
- Raw: n=88  W=29/L=59  WR=33.0%
- Sharpen: sharpest is session_bucket=london_open (21/59 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 70-80 overbought  •  ONLY when session=london_open

### L10.  `H20=H20e AND T1=T1c AND RSI=RSI6 AND direction_exec=short`
- Raw: n=88  W=29/L=59  WR=33.0%
- Sharpen: sharpest is session_bucket=london_open (21/59 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when session=london_open

### L11.  `T1=T1c AND RSI=RSI6 AND ZS=ZS4`
- Raw: n=84  W=25/L=59  WR=29.8%
- Sharpen: sharpest is T4=T4a (19/59 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 70-80 overbought; zscore +1 to +2 overbought  •  ONLY when 4h trend WITH trade

### L12.  `RSI=RSI6 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=84  W=25/L=59  WR=29.8%
- Sharpen: sharpest is T4=T4a (19/59 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: SHORT**  •  RSI 70-80 overbought; zscore +1 to +2 overbought  •  ONLY when 4h trend WITH trade

### L13.  `T1=T1c AND BBP=BBP4 AND RSI=RSI6 AND ZS=ZS4`
- Raw: n=84  W=25/L=59  WR=29.8%
- Sharpen: sharpest is T4=T4a (19/59 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; RSI 70-80 overbought; zscore +1 to +2 overbought  •  ONLY when 4h trend WITH trade

### L14.  `T1=T1c AND RSI=RSI6 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=84  W=25/L=59  WR=29.8%
- Sharpen: sharpest is T4=T4a (19/59 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 70-80 overbought; zscore +1 to +2 overbought  •  ONLY when 4h trend WITH trade

### L15.  `BBP=BBP4 AND RSI=RSI6 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=84  W=25/L=59  WR=29.8%
- Sharpen: sharpest is T4=T4a (19/59 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: SHORT**  •  upper third; RSI 70-80 overbought; zscore +1 to +2 overbought  •  ONLY when 4h trend WITH trade

### L16.  `H20=H20e AND T4=T4c AND RSI=RSI6`
- Raw: n=83  W=25/L=58  WR=30.1%
- Sharpen: sharpest is session_bucket=london_open (21/58 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when session=london_open

### L17.  `H20=H20e AND T1=T1c AND T4=T4c AND RSI=RSI6`
- Raw: n=83  W=25/L=58  WR=30.1%
- Sharpen: sharpest is session_bucket=london_open (21/58 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when session=london_open

### L18.  `H20=H20e AND T4=T4c AND RSI=RSI6 AND direction_exec=short`
- Raw: n=83  W=25/L=58  WR=30.1%
- Sharpen: sharpest is session_bucket=london_open (21/58 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when session=london_open

### L19.  `H60=H60a AND T1=T1c AND session_bucket=ny_mid`
- Raw: n=82  W=32/L=50  WR=39.0%
- Sharpen: sharpest is H20=H20b (22/50 of losers there)
- **Sharp: n=22  W=0/L=22  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=ny_mid  •  ONLY when HTF20 slightly aligned

### L20.  `H60=H60a AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=82  W=32/L=50  WR=39.0%
- Sharpen: sharpest is H20=H20b (22/50 of losers there)
- **Sharp: n=22  W=0/L=22  WR=0.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; session=ny_mid  •  ONLY when HTF20 slightly aligned

### L21.  `H60=H60a AND T1=T1c AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=82  W=32/L=50  WR=39.0%
- Sharpen: sharpest is H20=H20b (22/50 of losers there)
- **Sharp: n=22  W=0/L=22  WR=0.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=ny_mid  •  ONLY when HTF20 slightly aligned

### L22.  `T1=T1c AND T4=T4c AND BBP=BBP4 AND RSI=RSI6`
- Raw: n=73  W=29/L=44  WR=39.7%
- Sharpen: sharpest is H20=H20e (24/44 of losers there)
- **Sharp: n=31  W=7/L=24  WR=22.6%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; upper third; RSI 70-80 overbought  •  ONLY when HTF20 strongly against

### L23.  `T4=T4c AND BBP=BBP4 AND RSI=RSI6 AND direction_exec=short`
- Raw: n=73  W=29/L=44  WR=39.7%
- Sharpen: sharpest is H20=H20e (24/44 of losers there)
- **Sharp: n=31  W=7/L=24  WR=22.6%**
- **Dir: SHORT**  •  4h trend AGAINST trade; upper third; RSI 70-80 overbought  •  ONLY when HTF20 strongly against

### L24.  `H20=H20e AND H60=H60a AND T1=T1c AND RSI=RSI6`
- Raw: n=66  W=19/L=47  WR=28.8%
- Sharpen: sharpest is session_bucket=ny_mid (16/47 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when session=ny_mid

### L25.  `H20=H20e AND H60=H60a AND T4=T4c AND RSI=RSI6`
- Raw: n=66  W=19/L=47  WR=28.8%
- Sharpen: sharpest is session_bucket=ny_mid (16/47 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when session=ny_mid

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(39/23) | H20e(23/38) |
| H60 | — | — |
| T1 | T1a(59/41) | T1c(41/59) |
| T4 | T4a(54/46) | T4c(46/54) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(58/42) | short(42/58) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
