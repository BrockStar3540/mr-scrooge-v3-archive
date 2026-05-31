# NZD_JPY — R34 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **3,496**  (W=2,184 / L=1,312)  -  WR: **62.5%**

## Session distribution

- asia: n=861  W=556/L=305  WR=64.6%
- ny_close: n=605  W=380/L=225  WR=62.8%
- london: n=493  W=328/L=165  WR=66.5%
- ny_open: n=482  W=286/L=196  WR=59.3%
- ny_mid: n=471  W=282/L=189  WR=59.9%
- london_open: n=395  W=241/L=154  WR=61.0%
- off_hours: n=127  W=74/L=53  WR=58.3%
- asia_late: n=62  W=37/L=25  WR=59.7%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1c AND BBP=BBP4 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=283  W=241/L=42  WR=85.2%
- Refine: exclude session_bucket=asia drops 20/42 losers (48%)
- **Final: n=209  W=187/L=22  WR=89.5%**
- **Dir: SHORT**  •  1h trend AGAINST trade; upper third; RSI 50-60 upper neutral  •  AVOID when session=asia

### W02.  `T1=T1c AND RSI=RSI4 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=259  W=221/L=38  WR=85.3%
- Refine: exclude session_bucket=asia drops 19/38 losers (50%)
- **Final: n=186  W=167/L=19  WR=89.8%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when session=asia

### W03.  `H60=H60a AND T4=T4a AND session_bucket=london`
- Raw: n=193  W=165/L=28  WR=85.5%
- Refine: exclude ZS=ZS5 drops 14/28 losers (50%)
- **Final: n=143  W=129/L=14  WR=90.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; session=london  •  AVOID when zscore +2 to +3 deep overbought

### W04.  `H60=H60a AND T4=T4a AND direction_exec=long AND session_bucket=london`
- Raw: n=193  W=165/L=28  WR=85.5%
- Refine: exclude ZS=ZS5 drops 14/28 losers (50%)
- **Final: n=143  W=129/L=14  WR=90.2%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend WITH trade; session=london  •  AVOID when zscore +2 to +3 deep overbought

### W05.  `H60=H60a AND T1=T1a AND T4=T4a AND session_bucket=london`
- Raw: n=192  W=165/L=27  WR=85.9%
- Refine: exclude ZS=ZS5 drops 14/27 losers (52%)
- **Final: n=142  W=129/L=13  WR=90.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; session=london  •  AVOID when zscore +2 to +3 deep overbought

### W06.  `H60=H60e AND BBP=BBP6 AND direction_exec=short`
- Raw: n=168  W=147/L=21  WR=87.5%
- Refine: exclude H20=H20e drops 21/21 losers (100%)
- **Final: n=68  W=68/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 strongly against; deep above upper band  •  AVOID when HTF20 strongly against

### W07.  `H60=H60e AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=157  W=136/L=21  WR=86.6%
- Refine: exclude H20=H20e drops 21/21 losers (100%)
- **Final: n=54  W=54/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; deep above upper band; zscore +2 to +3 deep overbought  •  AVOID when HTF20 strongly against

### W08.  `H60=H60e AND T1=T1c AND BBP=BBP6`
- Raw: n=150  W=129/L=21  WR=86.0%
- Refine: exclude H20=H20e drops 21/21 losers (100%)
- **Final: n=52  W=52/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; deep above upper band  •  AVOID when HTF20 strongly against

### W09.  `H60=H60e AND T1=T1c AND BBP=BBP6 AND direction_exec=short`
- Raw: n=150  W=129/L=21  WR=86.0%
- Refine: exclude H20=H20e drops 21/21 losers (100%)
- **Final: n=52  W=52/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; deep above upper band  •  AVOID when HTF20 strongly against

### W10.  `T4=T4a AND RSI=RSI5 AND session_bucket=london`
- Raw: n=148  W=126/L=22  WR=85.1%
- Refine: exclude H20=H20e drops 11/22 losers (50%)
- **Final: n=119  W=108/L=11  WR=90.8%**
- **Dir: ?**  •  4h trend WITH trade; RSI 60-70 strong; session=london  •  AVOID when HTF20 strongly against

### W11.  `H60=H60a AND RSI=RSI5 AND session_bucket=london`
- Raw: n=146  W=126/L=20  WR=86.3%
- Refine: exclude T4=T4c drops 9/20 losers (45%)
- **Final: n=119  W=108/L=11  WR=90.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 60-70 strong; session=london  •  AVOID when 4h trend AGAINST trade

### W12.  `T1=T1a AND RSI=RSI5 AND session_bucket=london`
- Raw: n=146  W=126/L=20  WR=86.3%
- Refine: exclude T4=T4c drops 9/20 losers (45%)
- **Final: n=119  W=108/L=11  WR=90.8%**
- **Dir: ?**  •  1h trend WITH trade; RSI 60-70 strong; session=london  •  AVOID when 4h trend AGAINST trade

### W13.  `RSI=RSI5 AND direction_exec=long AND session_bucket=london`
- Raw: n=146  W=126/L=20  WR=86.3%
- Refine: exclude T4=T4c drops 9/20 losers (45%)
- **Final: n=119  W=108/L=11  WR=90.8%**
- **Dir: LONG**  •  RSI 60-70 strong; session=london  •  AVOID when 4h trend AGAINST trade

### W14.  `H60=H60a AND T1=T1a AND RSI=RSI5 AND session_bucket=london`
- Raw: n=146  W=126/L=20  WR=86.3%
- Refine: exclude T4=T4c drops 9/20 losers (45%)
- **Final: n=119  W=108/L=11  WR=90.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong; session=london  •  AVOID when 4h trend AGAINST trade

### W15.  `H60=H60a AND RSI=RSI5 AND direction_exec=long AND session_bucket=london`
- Raw: n=146  W=126/L=20  WR=86.3%
- Refine: exclude T4=T4c drops 9/20 losers (45%)
- **Final: n=119  W=108/L=11  WR=90.8%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 60-70 strong; session=london  •  AVOID when 4h trend AGAINST trade

### W16.  `T1=T1a AND RSI=RSI5 AND direction_exec=long AND session_bucket=london`
- Raw: n=146  W=126/L=20  WR=86.3%
- Refine: exclude T4=T4c drops 9/20 losers (45%)
- **Final: n=119  W=108/L=11  WR=90.8%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 60-70 strong; session=london  •  AVOID when 4h trend AGAINST trade

### W17.  `H60=H60e AND T4=T4c AND BBP=BBP6`
- Raw: n=144  W=125/L=19  WR=86.8%
- Refine: exclude H20=H20e drops 19/19 losers (100%)
- **Final: n=62  W=62/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; deep above upper band  •  AVOID when HTF20 strongly against

### W18.  `H60=H60e AND T4=T4c AND BBP=BBP6 AND direction_exec=short`
- Raw: n=144  W=125/L=19  WR=86.8%
- Refine: exclude H20=H20e drops 19/19 losers (100%)
- **Final: n=62  W=62/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend AGAINST trade; deep above upper band  •  AVOID when HTF20 strongly against

### W19.  `H60=H60e AND BBP=BBP6 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=141  W=120/L=21  WR=85.1%
- Refine: exclude H20=H20e drops 21/21 losers (100%)
- **Final: n=54  W=54/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 strongly against; deep above upper band; zscore +2 to +3 deep overbought  •  AVOID when HTF20 strongly against

### W20.  `BBP=BBP4 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=133  W=120/L=13  WR=90.2%
- Refine: exclude H20=H20e drops 10/13 losers (77%)
- **Final: n=76  W=73/L=3  WR=96.1%**
- **Dir: SHORT**  •  upper third; session=ny_close  •  AVOID when HTF20 strongly against

### W21.  `T1=T1c AND BBP=BBP4 AND session_bucket=ny_close`
- Raw: n=132  W=120/L=12  WR=90.9%
- Refine: exclude H60=H60a drops 3/12 losers (25%)
- **Final: n=125  W=116/L=9  WR=92.8%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; session=ny_close  •  AVOID when HTF60 aligned WITH trade

### W22.  `H60=H60e AND RSI=RSI5 AND session_bucket=ny_close`
- Raw: n=129  W=115/L=14  WR=89.1%
- Refine: exclude H20=H20e drops 10/14 losers (71%)
- **Final: n=87  W=83/L=4  WR=95.4%**
- **Dir: ?**  •  HTF60 strongly against; RSI 60-70 strong; session=ny_close  •  AVOID when HTF20 strongly against

### W23.  `H60=H60e AND T1=T1c AND RSI=RSI5 AND session_bucket=ny_close`
- Raw: n=129  W=115/L=14  WR=89.1%
- Refine: exclude H20=H20e drops 10/14 losers (71%)
- **Final: n=87  W=83/L=4  WR=95.4%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 60-70 strong; session=ny_close  •  AVOID when HTF20 strongly against

### W24.  `H60=H60e AND RSI=RSI5 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=129  W=115/L=14  WR=89.1%
- Refine: exclude H20=H20e drops 10/14 losers (71%)
- **Final: n=87  W=83/L=4  WR=95.4%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 60-70 strong; session=ny_close  •  AVOID when HTF20 strongly against

### W25.  `T1=T1c AND BBP=BBP4 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=125  W=116/L=9  WR=92.8%
- Refine: exclude H20=H20e drops 6/9 losers (67%)
- **Final: n=76  W=73/L=3  WR=96.1%**
- **Dir: SHORT**  •  1h trend AGAINST trade; upper third; session=ny_close  •  AVOID when HTF20 strongly against

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `BBP=BBP4 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=234  W=90/L=144  WR=38.5%
- Sharpen: sharpest is T1=T1a (126/144 of losers there)
- **Sharp: n=191  W=65/L=126  WR=34.0%**
- **Dir: LONG**  •  upper third; RSI 50-60 upper neutral  •  ONLY when 1h trend WITH trade

### L02.  `T1=T1a AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=231  W=92/L=139  WR=39.8%
- Sharpen: sharpest is direction_exec=long (126/139 of losers there)
- **Sharp: n=191  W=65/L=126  WR=34.0%**
- **Dir: ?**  •  1h trend WITH trade; upper third; RSI 50-60 upper neutral  •  ONLY when long

### L03.  `T4=T4a AND BBP=BBP4 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=197  W=77/L=120  WR=39.1%
- Sharpen: sharpest is H60=H60b (20/120 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: LONG**  •  4h trend WITH trade; upper third; RSI 50-60 upper neutral  •  ONLY when HTF60 slightly aligned

### L04.  `RSI=RSI4 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=194  W=68/L=126  WR=35.1%
- Sharpen: sharpest is H60=H60b (19/126 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: LONG**  •  RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when HTF60 slightly aligned

### L05.  `BBP=BBP4 AND RSI=RSI4 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=194  W=68/L=126  WR=35.1%
- Sharpen: sharpest is H60=H60b (19/126 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: LONG**  •  upper third; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when HTF60 slightly aligned

### L06.  `T1=T1a AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=194  W=72/L=122  WR=37.1%
- Sharpen: sharpest is direction_exec=long (111/122 of losers there)
- **Sharp: n=161  W=50/L=111  WR=31.1%**
- **Dir: ?**  •  1h trend WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when long

### L07.  `T1=T1a AND BBP=BBP4 AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=194  W=72/L=122  WR=37.1%
- Sharpen: sharpest is direction_exec=long (111/122 of losers there)
- **Sharp: n=161  W=50/L=111  WR=31.1%**
- **Dir: ?**  •  1h trend WITH trade; upper third; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when long

### L08.  `T1=T1a AND BBP=BBP4 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=191  W=65/L=126  WR=34.0%
- Sharpen: sharpest is H60=H60b (20/126 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: LONG**  •  1h trend WITH trade; upper third; RSI 50-60 upper neutral  •  ONLY when HTF60 slightly aligned

### L09.  `H20=H20e AND T4=T4c AND BBP=BBP4 AND RSI=RSI5`
- Raw: n=185  W=70/L=115  WR=37.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=185  W=70/L=115  WR=37.8%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; upper third; RSI 60-70 strong

### L10.  `H20=H20e AND T4=T4c AND RSI=RSI5 AND ZS=ZS4`
- Raw: n=173  W=66/L=107  WR=38.2%
- Sharpen: sharpest is session_bucket=ny_mid (17/107 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 60-70 strong; zscore +1 to +2 overbought  •  ONLY when session=ny_mid

### L11.  `T1=T1a AND T4=T4a AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=171  W=62/L=109  WR=36.3%
- Sharpen: sharpest is H60=H60b (20/109 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; upper third; RSI 50-60 upper neutral  •  ONLY when HTF60 slightly aligned

### L12.  `H60=H60a AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=169  W=66/L=103  WR=39.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=169  W=66/L=103  WR=39.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought

### L13.  `H60=H60a AND BBP=BBP4 AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=169  W=66/L=103  WR=39.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=169  W=66/L=103  WR=39.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; upper third; RSI 50-60 upper neutral; zscore +1 to +2 overbought

### L14.  `H60=H60a AND RSI=RSI4 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=169  W=66/L=103  WR=39.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=169  W=66/L=103  WR=39.1%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought

### L15.  `H60=H60a AND T1=T1a AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=167  W=65/L=102  WR=38.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=167  W=65/L=102  WR=38.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; upper third; RSI 50-60 upper neutral

### L16.  `T4=T4a AND RSI=RSI4 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=166  W=59/L=107  WR=35.5%
- Sharpen: sharpest is H60=H60b (19/107 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when HTF60 slightly aligned

### L17.  `T1=T1a AND RSI=RSI4 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=161  W=50/L=111  WR=31.1%
- Sharpen: sharpest is H60=H60b (19/111 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when HTF60 slightly aligned

### L18.  `H20=H20a AND T1=T1a AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=150  W=56/L=94  WR=37.3%
- Sharpen: sharpest is H60=H60b (20/94 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; upper third; RSI 50-60 upper neutral  •  ONLY when HTF60 slightly aligned

### L19.  `T1=T1a AND T4=T4a AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=148  W=50/L=98  WR=33.8%
- Sharpen: sharpest is H60=H60b (19/98 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when HTF60 slightly aligned

### L20.  `H20=H20a AND RSI=RSI4 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=146  W=55/L=91  WR=37.7%
- Sharpen: sharpest is H60=H60b (19/91 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when HTF60 slightly aligned

### L21.  `H60=H60a AND T1=T1a AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=141  W=50/L=91  WR=35.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=141  W=50/L=91  WR=35.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought

### L22.  `H20=H20a AND T1=T1a AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=130  W=43/L=87  WR=33.1%
- Sharpen: sharpest is H60=H60b (19/87 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when HTF60 slightly aligned

### L23.  `T1=T1a AND BBP=BBP4 AND session_bucket=ny_close`
- Raw: n=110  W=29/L=81  WR=26.4%
- Sharpen: sharpest is T4=T4a (57/81 of losers there)
- **Sharp: n=72  W=15/L=57  WR=20.8%**
- **Dir: ?**  •  1h trend WITH trade; upper third; session=ny_close  •  ONLY when 4h trend WITH trade

### L24.  `BBP=BBP4 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=109  W=29/L=80  WR=26.6%
- Sharpen: sharpest is ZS=ZS4 (71/80 of losers there)
- **Sharp: n=92  W=21/L=71  WR=22.8%**
- **Dir: LONG**  •  upper third; session=ny_close  •  ONLY when zscore +1 to +2 overbought

### L25.  `H60=H60a AND RSI=RSI5 AND session_bucket=ny_close`
- Raw: n=105  W=40/L=65  WR=38.1%
- Sharpen: sharpest is H20=H20b (35/65 of losers there)
- **Sharp: n=48  W=13/L=35  WR=27.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 60-70 strong; session=ny_close  •  ONLY when HTF20 slightly aligned

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | H20e(33/41) |
| H60 | — | — |
| T1 | — | — |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
