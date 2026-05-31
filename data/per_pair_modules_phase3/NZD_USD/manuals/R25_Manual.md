# NZD_USD — R25 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **2,379**  (W=1,523 / L=856)  -  WR: **64.0%**

## Session distribution

- ny_mid: n=749  W=473/L=276  WR=63.2%
- asia: n=401  W=256/L=145  WR=63.8%
- london_open: n=387  W=263/L=124  WR=68.0%
- ny_close: n=373  W=247/L=126  WR=66.2%
- ny_open: n=256  W=163/L=93  WR=63.7%
- asia_late: n=84  W=44/L=40  WR=52.4%
- london: n=82  W=51/L=31  WR=62.2%
- off_hours: n=47  W=26/L=21  WR=55.3%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60a AND T1=T1c AND RSI=RSI5`
- Raw: n=220  W=195/L=25  WR=88.6%
- Refine: exclude T4=T4a drops 13/25 losers (52%)
- **Final: n=181  W=169/L=12  WR=93.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 60-70 strong  •  AVOID when 4h trend WITH trade

### W02.  `H60=H60a AND RSI=RSI5 AND direction_exec=short`
- Raw: n=220  W=195/L=25  WR=88.6%
- Refine: exclude T4=T4a drops 13/25 losers (52%)
- **Final: n=181  W=169/L=12  WR=93.4%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; RSI 60-70 strong  •  AVOID when 4h trend WITH trade

### W03.  `H60=H60a AND T1=T1c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=220  W=195/L=25  WR=88.6%
- Refine: exclude T4=T4a drops 13/25 losers (52%)
- **Final: n=181  W=169/L=12  WR=93.4%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 60-70 strong  •  AVOID when 4h trend WITH trade

### W04.  `H60=H60a AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=200  W=173/L=27  WR=86.5%
- Refine: exclude H20=H20a drops 19/27 losers (70%)
- **Final: n=115  W=107/L=8  WR=93.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

### W05.  `H60=H60a AND T1=T1c AND T4=T4c AND RSI=RSI5`
- Raw: n=181  W=169/L=12  WR=93.4%
- Refine: exclude H20=H20a drops 7/12 losers (58%)
- **Final: n=129  W=124/L=5  WR=96.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when HTF20 aligned WITH trade

### W06.  `H60=H60a AND T4=T4c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=181  W=169/L=12  WR=93.4%
- Refine: exclude H20=H20a drops 7/12 losers (58%)
- **Final: n=129  W=124/L=5  WR=96.1%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when HTF20 aligned WITH trade

### W07.  `T1=T1a AND T4=T4a AND session_bucket=asia`
- Raw: n=167  W=142/L=25  WR=85.0%
- Refine: exclude H60=H60a drops 15/25 losers (60%)
- **Final: n=103  W=93/L=10  WR=90.3%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; session=asia  •  AVOID when HTF60 aligned WITH trade

### W08.  `T4=T4a AND direction_exec=long AND session_bucket=asia`
- Raw: n=167  W=142/L=25  WR=85.0%
- Refine: exclude H60=H60a drops 15/25 losers (60%)
- **Final: n=103  W=93/L=10  WR=90.3%**
- **Dir: LONG**  •  4h trend WITH trade; session=asia  •  AVOID when HTF60 aligned WITH trade

### W09.  `T1=T1a AND T4=T4a AND direction_exec=long AND session_bucket=asia`
- Raw: n=167  W=142/L=25  WR=85.0%
- Refine: exclude H60=H60a drops 15/25 losers (60%)
- **Final: n=103  W=93/L=10  WR=90.3%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; session=asia  •  AVOID when HTF60 aligned WITH trade

### W10.  `T4=T4a AND RSI=RSI6 AND session_bucket=asia`
- Raw: n=151  W=133/L=18  WR=88.1%
- Refine: exclude H60=H60a drops 12/18 losers (67%)
- **Final: n=106  W=100/L=6  WR=94.3%**
- **Dir: ?**  •  4h trend WITH trade; RSI 70-80 overbought; session=asia  •  AVOID when HTF60 aligned WITH trade

### W11.  `H20=H20a AND T1=T1c AND T4=T4a`
- Raw: n=146  W=126/L=20  WR=86.3%
- Refine: exclude ZS=ZS2 drops 7/20 losers (35%)
- **Final: n=129  W=116/L=13  WR=89.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade  •  AVOID when zscore -2 to -1 oversold

### W12.  `H20=H20a AND T4=T4a AND direction_exec=short`
- Raw: n=146  W=126/L=20  WR=86.3%
- Refine: exclude ZS=ZS2 drops 7/20 losers (35%)
- **Final: n=129  W=116/L=13  WR=89.9%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend WITH trade  •  AVOID when zscore -2 to -1 oversold

### W13.  `H20=H20a AND T1=T1c AND T4=T4a AND direction_exec=short`
- Raw: n=146  W=126/L=20  WR=86.3%
- Refine: exclude ZS=ZS2 drops 7/20 losers (35%)
- **Final: n=129  W=116/L=13  WR=89.9%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade  •  AVOID when zscore -2 to -1 oversold

### W14.  `H60=H60a AND T1=T1c AND BBP=BBP4 AND RSI=RSI5`
- Raw: n=141  W=125/L=16  WR=88.7%
- Refine: exclude T4=T4a drops 8/16 losers (50%)
- **Final: n=115  W=107/L=8  WR=93.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; upper third; RSI 60-70 strong  •  AVOID when 4h trend WITH trade

### W15.  `H60=H60a AND BBP=BBP4 AND RSI=RSI5 AND direction_exec=short`
- Raw: n=141  W=125/L=16  WR=88.7%
- Refine: exclude T4=T4a drops 8/16 losers (50%)
- **Final: n=115  W=107/L=8  WR=93.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; upper third; RSI 60-70 strong  •  AVOID when 4h trend WITH trade

### W16.  `H60=H60a AND T1=T1c AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=140  W=119/L=21  WR=85.0%
- Refine: exclude H20=H20a drops 18/21 losers (86%)
- **Final: n=98  W=95/L=3  WR=96.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

### W17.  `H60=H60a AND T4=T4c AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=140  W=119/L=21  WR=85.0%
- Refine: exclude H20=H20a drops 18/21 losers (86%)
- **Final: n=98  W=95/L=3  WR=96.9%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

### W18.  `H20=H20e AND H60=H60a AND T1=T1c AND RSI=RSI5`
- Raw: n=138  W=120/L=18  WR=87.0%
- Refine: exclude T4=T4a drops 13/18 losers (72%)
- **Final: n=113  W=108/L=5  WR=95.6%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 60-70 strong  •  AVOID when 4h trend WITH trade

### W19.  `H20=H20e AND H60=H60a AND RSI=RSI5 AND direction_exec=short`
- Raw: n=138  W=120/L=18  WR=87.0%
- Refine: exclude T4=T4a drops 13/18 losers (72%)
- **Final: n=113  W=108/L=5  WR=95.6%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 aligned WITH trade; RSI 60-70 strong  •  AVOID when 4h trend WITH trade

### W20.  `T1=T1a AND T4=T4a AND RSI=RSI6 AND session_bucket=asia`
- Raw: n=137  W=121/L=16  WR=88.3%
- Refine: exclude H60=H60a drops 12/16 losers (75%)
- **Final: n=92  W=88/L=4  WR=95.7%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 70-80 overbought; session=asia  •  AVOID when HTF60 aligned WITH trade

### W21.  `T4=T4a AND RSI=RSI6 AND direction_exec=long AND session_bucket=asia`
- Raw: n=137  W=121/L=16  WR=88.3%
- Refine: exclude H60=H60a drops 12/16 losers (75%)
- **Final: n=92  W=88/L=4  WR=95.7%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 70-80 overbought; session=asia  •  AVOID when HTF60 aligned WITH trade

### W22.  `H20=H20a AND T4=T4a AND session_bucket=london_open`
- Raw: n=133  W=123/L=10  WR=92.5%
- Refine: exclude H60=H60e drops 7/10 losers (70%)
- **Final: n=65  W=62/L=3  WR=95.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=london_open  •  AVOID when HTF60 strongly against

### W23.  `H20=H20a AND BBP=BBP4 AND session_bucket=london_open`
- Raw: n=132  W=116/L=16  WR=87.9%
- Refine: exclude ZS=ZS3 drops 6/16 losers (38%)
- **Final: n=118  W=108/L=10  WR=91.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; upper third; session=london_open  •  AVOID when zscore -1 to +1 neutral

### W24.  `H60=H60e AND T4=T4a AND session_bucket=asia`
- Raw: n=131  W=119/L=12  WR=90.8%
- Refine: exclude ZS=ZS4 drops 11/12 losers (92%)
- **Final: n=67  W=66/L=1  WR=98.5%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; session=asia  •  AVOID when zscore +1 to +2 overbought

### W25.  `H60=H60a AND T1=T1c AND RSI=RSI5 AND ZS=ZS4`
- Raw: n=121  W=111/L=10  WR=91.7%
- Refine: exclude T4=T4a drops 4/10 losers (40%)
- **Final: n=103  W=97/L=6  WR=94.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 60-70 strong; zscore +1 to +2 overbought  •  AVOID when 4h trend WITH trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND H60=H60e AND T4=T4c`
- Raw: n=244  W=93/L=151  WR=38.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=244  W=93/L=151  WR=38.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade

### L02.  `H20=H20e AND H60=H60e AND T4=T4c AND direction_exec=short`
- Raw: n=238  W=91/L=147  WR=38.2%
- Sharpen: no sharper sub-pattern
- **Sharp: n=238  W=91/L=147  WR=38.2%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade

### L03.  `H20=H20e AND H60=H60e AND T1=T1c AND T4=T4c`
- Raw: n=235  W=90/L=145  WR=38.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=235  W=90/L=145  WR=38.3%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade

### L04.  `H60=H60e AND T4=T4c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=184  W=72/L=112  WR=39.1%
- Sharpen: sharpest is BBP=BBP6 (17/112 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when deep above upper band

### L05.  `H60=H60e AND T1=T1c AND T4=T4c AND RSI=RSI5`
- Raw: n=181  W=71/L=110  WR=39.2%
- Sharpen: sharpest is BBP=BBP6 (17/110 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when deep above upper band

### L06.  `H60=H60e AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=156  W=55/L=101  WR=35.3%
- Sharpen: sharpest is BBP=BBP6 (16/101 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; RSI 60-70 strong; session=ny_mid  •  ONLY when deep above upper band

### L07.  `T4=T4c AND RSI=RSI6 AND session_bucket=asia`
- Raw: n=144  W=45/L=99  WR=31.2%
- Sharpen: sharpest is H60=H60a (74/99 of losers there)
- **Sharp: n=90  W=16/L=74  WR=17.8%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 70-80 overbought; session=asia  •  ONLY when HTF60 aligned WITH trade

### L08.  `H20=H20e AND H60=H60e AND T4=T4c AND BBP=BBP4`
- Raw: n=143  W=57/L=86  WR=39.9%
- Sharpen: sharpest is session_bucket=asia (15/86 of losers there)
- **Sharp: n=16  W=1/L=15  WR=6.2%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; upper third  •  ONLY when session=asia

### L09.  `T1=T1c AND RSI=RSI6 AND session_bucket=asia`
- Raw: n=142  W=56/L=86  WR=39.4%
- Sharpen: sharpest is H60=H60a (59/86 of losers there)
- **Sharp: n=74  W=15/L=59  WR=20.3%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 70-80 overbought; session=asia  •  ONLY when HTF60 aligned WITH trade

### L10.  `RSI=RSI6 AND direction_exec=short AND session_bucket=asia`
- Raw: n=142  W=56/L=86  WR=39.4%
- Sharpen: sharpest is H60=H60a (59/86 of losers there)
- **Sharp: n=74  W=15/L=59  WR=20.3%**
- **Dir: SHORT**  •  RSI 70-80 overbought; session=asia  •  ONLY when HTF60 aligned WITH trade

### L11.  `T1=T1c AND RSI=RSI6 AND direction_exec=short AND session_bucket=asia`
- Raw: n=142  W=56/L=86  WR=39.4%
- Sharpen: sharpest is H60=H60a (59/86 of losers there)
- **Sharp: n=74  W=15/L=59  WR=20.3%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 70-80 overbought; session=asia  •  ONLY when HTF60 aligned WITH trade

### L12.  `H60=H60e AND T1=T1a AND RSI=RSI5`
- Raw: n=137  W=52/L=85  WR=38.0%
- Sharpen: sharpest is T4=T4a (78/85 of losers there)
- **Sharp: n=111  W=33/L=78  WR=29.7%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; RSI 60-70 strong  •  ONLY when 4h trend WITH trade

### L13.  `H60=H60e AND RSI=RSI5 AND direction_exec=long`
- Raw: n=137  W=52/L=85  WR=38.0%
- Sharpen: sharpest is T4=T4a (78/85 of losers there)
- **Sharp: n=111  W=33/L=78  WR=29.7%**
- **Dir: LONG**  •  HTF60 strongly against; RSI 60-70 strong  •  ONLY when 4h trend WITH trade

### L14.  `H60=H60e AND T1=T1a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=137  W=52/L=85  WR=38.0%
- Sharpen: sharpest is T4=T4a (78/85 of losers there)
- **Sharp: n=111  W=33/L=78  WR=29.7%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend WITH trade; RSI 60-70 strong  •  ONLY when 4h trend WITH trade

### L15.  `H20=H20e AND H60=H60e AND T4=T4c AND ZS=ZS4`
- Raw: n=137  W=53/L=84  WR=38.7%
- Sharpen: sharpest is session_bucket=asia (15/84 of losers there)
- **Sharp: n=16  W=1/L=15  WR=6.2%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  ONLY when session=asia

### L16.  `H60=H60a AND RSI=RSI6 AND session_bucket=asia`
- Raw: n=135  W=49/L=86  WR=36.3%
- Sharpen: sharpest is T4=T4c (74/86 of losers there)
- **Sharp: n=90  W=16/L=74  WR=17.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 70-80 overbought; session=asia  •  ONLY when 4h trend AGAINST trade

### L17.  `T1=T1c AND T4=T4c AND RSI=RSI6 AND session_bucket=asia`
- Raw: n=128  W=44/L=84  WR=34.4%
- Sharpen: sharpest is H20=H20e (50/84 of losers there)
- **Sharp: n=58  W=8/L=50  WR=13.8%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 70-80 overbought; session=asia  •  ONLY when HTF20 strongly against

### L18.  `T4=T4c AND RSI=RSI6 AND direction_exec=short AND session_bucket=asia`
- Raw: n=128  W=44/L=84  WR=34.4%
- Sharpen: sharpest is H20=H20e (50/84 of losers there)
- **Sharp: n=58  W=8/L=50  WR=13.8%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 70-80 overbought; session=asia  •  ONLY when HTF20 strongly against

### L19.  `H20=H20e AND H60=H60e AND T1=T1c AND session_bucket=ny_mid`
- Raw: n=126  W=49/L=77  WR=38.9%
- Sharpen: sharpest is ZS=ZS5 (38/77 of losers there)
- **Sharp: n=53  W=15/L=38  WR=28.3%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; session=ny_mid  •  ONLY when zscore +2 to +3 deep overbought

### L20.  `H20=H20e AND H60=H60e AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=126  W=49/L=77  WR=38.9%
- Sharpen: sharpest is ZS=ZS5 (38/77 of losers there)
- **Sharp: n=53  W=15/L=38  WR=28.3%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; session=ny_mid  •  ONLY when zscore +2 to +3 deep overbought

### L21.  `T4=T4c AND BBP=BBP5 AND RSI=RSI6`
- Raw: n=125  W=47/L=78  WR=37.6%
- Sharpen: sharpest is session_bucket=asia (19/78 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: ?**  •  4h trend AGAINST trade; just touched upper band; RSI 70-80 overbought  •  ONLY when session=asia

### L22.  `T4=T4c AND BBP=BBP5 AND RSI=RSI6 AND ZS=ZS5`
- Raw: n=125  W=47/L=78  WR=37.6%
- Sharpen: sharpest is session_bucket=asia (19/78 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: ?**  •  4h trend AGAINST trade; just touched upper band; RSI 70-80 overbought; zscore +2 to +3 deep overbought  •  ONLY when session=asia

### L23.  `H60=H60a AND T4=T4c AND session_bucket=asia`
- Raw: n=120  W=38/L=82  WR=31.7%
- Sharpen: sharpest is RSI=RSI6 (74/82 of losers there)
- **Sharp: n=90  W=16/L=74  WR=17.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=asia  •  ONLY when RSI 70-80 overbought

### L24.  `H60=H60e AND T1=T1a AND T4=T4a AND RSI=RSI5`
- Raw: n=111  W=33/L=78  WR=29.7%
- Sharpen: sharpest is ZS=ZS5 (18/78 of losers there)
- **Sharp: n=19  W=1/L=18  WR=5.3%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when zscore +2 to +3 deep overbought

### L25.  `H60=H60e AND T4=T4a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=111  W=33/L=78  WR=29.7%
- Sharpen: sharpest is ZS=ZS5 (18/78 of losers there)
- **Sharp: n=19  W=1/L=18  WR=5.3%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend WITH trade; RSI 60-70 strong  •  ONLY when zscore +2 to +3 deep overbought

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(53/41) | H20e(42/55) |
| H60 | H60a(49/38) | H60e(39/51) |
| T1 | T1a(51/45) | T1c(49/55) |
| T4 | T4a(55/44) | T4c(45/56) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(51/45) | short(49/55) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
