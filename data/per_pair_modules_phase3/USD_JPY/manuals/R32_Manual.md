# USD_JPY — R32 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50a**  (EMA50 up >0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **3,491**  (W=2,132 / L=1,359)  -  WR: **61.1%**

## Session distribution

- asia: n=994  W=601/L=393  WR=60.5%
- london_open: n=824  W=501/L=323  WR=60.8%
- ny_mid: n=572  W=351/L=221  WR=61.4%
- ny_close: n=430  W=263/L=167  WR=61.2%
- ny_open: n=423  W=266/L=157  WR=62.9%
- london: n=133  W=81/L=52  WR=60.9%
- asia_late: n=109  W=65/L=44  WR=59.6%
- off_hours: n=6  W=4/L=2  WR=66.7%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60e AND RSI=RSI4 AND session_bucket=ny_open`
- Raw: n=127  W=117/L=10  WR=92.1%
- Refine: exclude T1=T1c drops 10/10 losers (100%)
- **Final: n=70  W=70/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; RSI 50-60 upper neutral; session=ny_open  •  AVOID when 1h trend AGAINST trade

### W02.  `T4=T4c AND BBP=BBP6 AND RSI=RSI5`
- Raw: n=107  W=91/L=16  WR=85.0%
- Refine: exclude session_bucket=asia drops 5/16 losers (31%)
- **Final: n=96  W=85/L=11  WR=88.5%**
- **Dir: ?**  •  4h trend AGAINST trade; deep above upper band; RSI 60-70 strong  •  AVOID when session=asia

### W03.  `H60=H60e AND T4=T4a AND session_bucket=ny_open`
- Raw: n=105  W=102/L=3  WR=97.1%
- Refine: exclude RSI=RSI5 drops 3/3 losers (100%)
- **Final: n=70  W=70/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; session=ny_open  •  AVOID when RSI 60-70 strong

### W04.  `T1=T1a AND BBP=BBP5 AND RSI=RSI6`
- Raw: n=99  W=91/L=8  WR=91.9%
- Refine: exclude session_bucket=ny_close drops 6/8 losers (75%)
- **Final: n=93  W=91/L=2  WR=97.8%**
- **Dir: ?**  •  1h trend WITH trade; just touched upper band; RSI 70-80 overbought  •  AVOID when session=ny_close

### W05.  `T4=T4a AND BBP=BBP5 AND RSI=RSI6`
- Raw: n=99  W=91/L=8  WR=91.9%
- Refine: exclude session_bucket=ny_close drops 6/8 losers (75%)
- **Final: n=93  W=91/L=2  WR=97.8%**
- **Dir: ?**  •  4h trend WITH trade; just touched upper band; RSI 70-80 overbought  •  AVOID when session=ny_close

### W06.  `BBP=BBP5 AND RSI=RSI6 AND direction_exec=long`
- Raw: n=99  W=91/L=8  WR=91.9%
- Refine: exclude session_bucket=ny_close drops 6/8 losers (75%)
- **Final: n=93  W=91/L=2  WR=97.8%**
- **Dir: LONG**  •  just touched upper band; RSI 70-80 overbought  •  AVOID when session=ny_close

### W07.  `T1=T1a AND T4=T4a AND BBP=BBP5 AND RSI=RSI6`
- Raw: n=99  W=91/L=8  WR=91.9%
- Refine: exclude session_bucket=ny_close drops 6/8 losers (75%)
- **Final: n=93  W=91/L=2  WR=97.8%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; just touched upper band; RSI 70-80 overbought  •  AVOID when session=ny_close

### W08.  `T1=T1a AND BBP=BBP5 AND RSI=RSI6 AND ZS=ZS5`
- Raw: n=99  W=91/L=8  WR=91.9%
- Refine: exclude session_bucket=ny_close drops 6/8 losers (75%)
- **Final: n=93  W=91/L=2  WR=97.8%**
- **Dir: ?**  •  1h trend WITH trade; just touched upper band; RSI 70-80 overbought; zscore +2 to +3 deep overbought  •  AVOID when session=ny_close

### W09.  `T1=T1a AND BBP=BBP5 AND RSI=RSI6 AND direction_exec=long`
- Raw: n=99  W=91/L=8  WR=91.9%
- Refine: exclude session_bucket=ny_close drops 6/8 losers (75%)
- **Final: n=93  W=91/L=2  WR=97.8%**
- **Dir: LONG**  •  1h trend WITH trade; just touched upper band; RSI 70-80 overbought  •  AVOID when session=ny_close

### W10.  `T4=T4a AND BBP=BBP5 AND RSI=RSI6 AND ZS=ZS5`
- Raw: n=99  W=91/L=8  WR=91.9%
- Refine: exclude session_bucket=ny_close drops 6/8 losers (75%)
- **Final: n=93  W=91/L=2  WR=97.8%**
- **Dir: ?**  •  4h trend WITH trade; just touched upper band; RSI 70-80 overbought; zscore +2 to +3 deep overbought  •  AVOID when session=ny_close

### W11.  `T4=T4a AND BBP=BBP5 AND RSI=RSI6 AND direction_exec=long`
- Raw: n=99  W=91/L=8  WR=91.9%
- Refine: exclude session_bucket=ny_close drops 6/8 losers (75%)
- **Final: n=93  W=91/L=2  WR=97.8%**
- **Dir: LONG**  •  4h trend WITH trade; just touched upper band; RSI 70-80 overbought  •  AVOID when session=ny_close

### W12.  `BBP=BBP5 AND RSI=RSI6 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=99  W=91/L=8  WR=91.9%
- Refine: exclude session_bucket=ny_close drops 6/8 losers (75%)
- **Final: n=93  W=91/L=2  WR=97.8%**
- **Dir: LONG**  •  just touched upper band; RSI 70-80 overbought; zscore +2 to +3 deep overbought  •  AVOID when session=ny_close

### W13.  `H60=H60a AND T1=T1a AND RSI=RSI6 AND ZS=ZS5`
- Raw: n=95  W=82/L=13  WR=86.3%
- Refine: exclude session_bucket=ny_close drops 6/13 losers (46%)
- **Final: n=89  W=82/L=7  WR=92.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 70-80 overbought; zscore +2 to +3 deep overbought  •  AVOID when session=ny_close

### W14.  `H60=H60a AND T4=T4a AND RSI=RSI6 AND ZS=ZS5`
- Raw: n=95  W=82/L=13  WR=86.3%
- Refine: exclude session_bucket=ny_close drops 6/13 losers (46%)
- **Final: n=89  W=82/L=7  WR=92.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 70-80 overbought; zscore +2 to +3 deep overbought  •  AVOID when session=ny_close

### W15.  `H60=H60a AND RSI=RSI6 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=95  W=82/L=13  WR=86.3%
- Refine: exclude session_bucket=ny_close drops 6/13 losers (46%)
- **Final: n=89  W=82/L=7  WR=92.1%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 70-80 overbought; zscore +2 to +3 deep overbought  •  AVOID when session=ny_close

### W16.  `H20=H20e AND T1=T1a AND T4=T4a AND BBP=BBP5`
- Raw: n=86  W=74/L=12  WR=86.0%
- Refine: exclude RSI=RSI5 drops 9/12 losers (75%)
- **Final: n=69  W=66/L=3  WR=95.7%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend WITH trade; just touched upper band  •  AVOID when RSI 60-70 strong

### W17.  `H20=H20e AND T4=T4a AND BBP=BBP5 AND direction_exec=long`
- Raw: n=86  W=74/L=12  WR=86.0%
- Refine: exclude RSI=RSI5 drops 9/12 losers (75%)
- **Final: n=69  W=66/L=3  WR=95.7%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend WITH trade; just touched upper band  •  AVOID when RSI 60-70 strong

### W18.  `T1=T1c AND T4=T4c AND BBP=BBP6 AND RSI=RSI5`
- Raw: n=85  W=73/L=12  WR=85.9%
- Refine: exclude session_bucket=asia drops 5/12 losers (42%)
- **Final: n=74  W=67/L=7  WR=90.5%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; deep above upper band; RSI 60-70 strong  •  AVOID when session=asia

### W19.  `T4=T4c AND BBP=BBP6 AND RSI=RSI5 AND direction_exec=short`
- Raw: n=85  W=73/L=12  WR=85.9%
- Refine: exclude session_bucket=asia drops 5/12 losers (42%)
- **Final: n=74  W=67/L=7  WR=90.5%**
- **Dir: SHORT**  •  4h trend AGAINST trade; deep above upper band; RSI 60-70 strong  •  AVOID when session=asia

### W20.  `H60=H60a AND RSI=RSI4 AND session_bucket=ny_close`
- Raw: n=84  W=76/L=8  WR=90.5%
- Refine: exclude BBP=BBP4 drops 4/8 losers (50%)
- **Final: n=76  W=72/L=4  WR=94.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; session=ny_close  •  AVOID when upper third

### W21.  `H60=H60e AND T4=T4c AND BBP=BBP6 AND RSI=RSI5`
- Raw: n=84  W=72/L=12  WR=85.7%
- Refine: exclude session_bucket=asia drops 5/12 losers (42%)
- **Final: n=73  W=66/L=7  WR=90.4%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; deep above upper band; RSI 60-70 strong  •  AVOID when session=asia

### W22.  `H60=H60e AND T1=T1a AND session_bucket=ny_open`
- Raw: n=82  W=79/L=3  WR=96.3%
- Refine: exclude RSI=RSI5 drops 3/3 losers (100%)
- **Final: n=70  W=70/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; session=ny_open  •  AVOID when RSI 60-70 strong

### W23.  `H60=H60e AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=82  W=79/L=3  WR=96.3%
- Refine: exclude RSI=RSI5 drops 3/3 losers (100%)
- **Final: n=70  W=70/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 strongly against; session=ny_open  •  AVOID when RSI 60-70 strong

### W24.  `H60=H60e AND T1=T1a AND T4=T4a AND session_bucket=ny_open`
- Raw: n=82  W=79/L=3  WR=96.3%
- Refine: exclude RSI=RSI5 drops 3/3 losers (100%)
- **Final: n=70  W=70/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend WITH trade; session=ny_open  •  AVOID when RSI 60-70 strong

### W25.  `H60=H60e AND T1=T1a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=82  W=79/L=3  WR=96.3%
- Refine: exclude RSI=RSI5 drops 3/3 losers (100%)
- **Final: n=70  W=70/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend WITH trade; session=ny_open  •  AVOID when RSI 60-70 strong

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1c AND RSI=RSI6 AND direction_exec=short`
- Raw: n=328  W=127/L=201  WR=38.7%
- Sharpen: no sharper sub-pattern
- **Sharp: n=328  W=127/L=201  WR=38.7%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 70-80 overbought

### L02.  `T1=T1c AND T4=T4c AND RSI=RSI6`
- Raw: n=318  W=123/L=195  WR=38.7%
- Sharpen: no sharper sub-pattern
- **Sharp: n=318  W=123/L=195  WR=38.7%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 70-80 overbought

### L03.  `T4=T4c AND RSI=RSI6 AND direction_exec=short`
- Raw: n=318  W=123/L=195  WR=38.7%
- Sharpen: no sharper sub-pattern
- **Sharp: n=318  W=123/L=195  WR=38.7%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 70-80 overbought

### L04.  `T1=T1c AND T4=T4c AND RSI=RSI6 AND direction_exec=short`
- Raw: n=318  W=123/L=195  WR=38.7%
- Sharpen: no sharper sub-pattern
- **Sharp: n=318  W=123/L=195  WR=38.7%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 70-80 overbought

### L05.  `H60=H60e AND T1=T1c AND RSI=RSI6`
- Raw: n=242  W=90/L=152  WR=37.2%
- Sharpen: sharpest is H20=H20a (33/152 of losers there)
- **Sharp: n=33  W=0/L=33  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when HTF20 aligned WITH trade

### L06.  `H60=H60e AND RSI=RSI6 AND direction_exec=short`
- Raw: n=242  W=90/L=152  WR=37.2%
- Sharpen: sharpest is H20=H20a (33/152 of losers there)
- **Sharp: n=33  W=0/L=33  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 70-80 overbought  •  ONLY when HTF20 aligned WITH trade

### L07.  `H60=H60e AND T1=T1c AND RSI=RSI6 AND direction_exec=short`
- Raw: n=242  W=90/L=152  WR=37.2%
- Sharpen: sharpest is H20=H20a (33/152 of losers there)
- **Sharp: n=33  W=0/L=33  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when HTF20 aligned WITH trade

### L08.  `H60=H60e AND T4=T4c AND RSI=RSI6`
- Raw: n=232  W=86/L=146  WR=37.1%
- Sharpen: sharpest is H20=H20a (33/146 of losers there)
- **Sharp: n=33  W=0/L=33  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when HTF20 aligned WITH trade

### L09.  `H60=H60e AND T1=T1c AND T4=T4c AND RSI=RSI6`
- Raw: n=232  W=86/L=146  WR=37.1%
- Sharpen: sharpest is H20=H20a (33/146 of losers there)
- **Sharp: n=33  W=0/L=33  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when HTF20 aligned WITH trade

### L10.  `H60=H60e AND T4=T4c AND RSI=RSI6 AND direction_exec=short`
- Raw: n=232  W=86/L=146  WR=37.1%
- Sharpen: sharpest is H20=H20a (33/146 of losers there)
- **Sharp: n=33  W=0/L=33  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when HTF20 aligned WITH trade

### L11.  `H60=H60e AND T1=T1c AND session_bucket=ny_close`
- Raw: n=188  W=75/L=113  WR=39.9%
- Sharpen: sharpest is BBP=BBP2 (27/113 of losers there)
- **Sharp: n=28  W=1/L=27  WR=3.6%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; session=ny_close  •  ONLY when lower third

### L12.  `H60=H60e AND T4=T4c AND session_bucket=ny_close`
- Raw: n=188  W=75/L=113  WR=39.9%
- Sharpen: sharpest is BBP=BBP2 (27/113 of losers there)
- **Sharp: n=28  W=1/L=27  WR=3.6%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; session=ny_close  •  ONLY when lower third

### L13.  `H60=H60e AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=188  W=75/L=113  WR=39.9%
- Sharpen: sharpest is BBP=BBP2 (27/113 of losers there)
- **Sharp: n=28  W=1/L=27  WR=3.6%**
- **Dir: SHORT**  •  HTF60 strongly against; session=ny_close  •  ONLY when lower third

### L14.  `H60=H60e AND T1=T1c AND T4=T4c AND session_bucket=ny_close`
- Raw: n=188  W=75/L=113  WR=39.9%
- Sharpen: sharpest is BBP=BBP2 (27/113 of losers there)
- **Sharp: n=28  W=1/L=27  WR=3.6%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_close  •  ONLY when lower third

### L15.  `H60=H60e AND T1=T1c AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=188  W=75/L=113  WR=39.9%
- Sharpen: sharpest is BBP=BBP2 (27/113 of losers there)
- **Sharp: n=28  W=1/L=27  WR=3.6%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; session=ny_close  •  ONLY when lower third

### L16.  `H60=H60e AND T4=T4c AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=188  W=75/L=113  WR=39.9%
- Sharpen: sharpest is BBP=BBP2 (27/113 of losers there)
- **Sharp: n=28  W=1/L=27  WR=3.6%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend AGAINST trade; session=ny_close  •  ONLY when lower third

### L17.  `T1=T1c AND RSI=RSI6 AND session_bucket=asia`
- Raw: n=151  W=59/L=92  WR=39.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=151  W=59/L=92  WR=39.1%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 70-80 overbought; session=asia

### L18.  `RSI=RSI6 AND direction_exec=short AND session_bucket=asia`
- Raw: n=151  W=59/L=92  WR=39.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=151  W=59/L=92  WR=39.1%**
- **Dir: SHORT**  •  RSI 70-80 overbought; session=asia

### L19.  `T1=T1c AND RSI=RSI6 AND direction_exec=short AND session_bucket=asia`
- Raw: n=151  W=59/L=92  WR=39.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=151  W=59/L=92  WR=39.1%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 70-80 overbought; session=asia

### L20.  `T1=T1c AND T4=T4c AND RSI=RSI6 AND session_bucket=asia`
- Raw: n=141  W=55/L=86  WR=39.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=141  W=55/L=86  WR=39.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 70-80 overbought; session=asia

### L21.  `T4=T4c AND RSI=RSI6 AND direction_exec=short AND session_bucket=asia`
- Raw: n=141  W=55/L=86  WR=39.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=141  W=55/L=86  WR=39.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 70-80 overbought; session=asia

### L22.  `T4=T4a AND RSI=RSI5 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=126  W=50/L=76  WR=39.7%
- Sharpen: sharpest is session_bucket=ny_mid (19/76 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  ONLY when session=ny_mid

### L23.  `H60=H60a AND T4=T4a AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=125  W=50/L=75  WR=40.0%
- Sharpen: sharpest is session_bucket=ny_mid (19/75 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  ONLY when session=ny_mid

### L24.  `H20=H20a AND T1=T1c AND RSI=RSI6`
- Raw: n=119  W=37/L=82  WR=31.1%
- Sharpen: sharpest is H60=H60e (33/82 of losers there)
- **Sharp: n=33  W=0/L=33  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when HTF60 strongly against

### L25.  `H20=H20a AND T4=T4c AND RSI=RSI6`
- Raw: n=119  W=37/L=82  WR=31.1%
- Sharpen: sharpest is H60=H60e (33/82 of losers there)
- **Sharp: n=33  W=0/L=33  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when HTF60 strongly against

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | — |
| T1 | T1a(53/46) | T1c(47/54) |
| T4 | T4a(53/47) | T4c(47/53) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
