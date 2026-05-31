# GBP_USD — R30 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR3**  (60-90%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **3,329**  (W=2,049 / L=1,280)  -  WR: **61.6%**

## Session distribution

- ny_close: n=631  W=386/L=245  WR=61.2%
- ny_open: n=617  W=357/L=260  WR=57.9%
- asia: n=516  W=323/L=193  WR=62.6%
- ny_mid: n=494  W=305/L=189  WR=61.7%
- london_open: n=491  W=322/L=169  WR=65.6%
- london: n=360  W=235/L=125  WR=65.3%
- off_hours: n=113  W=56/L=57  WR=49.6%
- asia_late: n=107  W=65/L=42  WR=60.7%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T4=T4a AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=229  W=195/L=34  WR=85.2%
- Refine: exclude H60=H60d drops 21/34 losers (62%)
- **Final: n=149  W=136/L=13  WR=91.3%**
- **Dir: ?**  •  4h trend WITH trade; RSI 60-70 strong; session=london_open  •  AVOID when HTF60 mildly against

### W02.  `T4=T4a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=197  W=174/L=23  WR=88.3%
- Refine: exclude BBP=BBP5 drops 10/23 losers (43%)
- **Final: n=175  W=162/L=13  WR=92.6%**
- **Dir: LONG**  •  4h trend WITH trade; session=london_open  •  AVOID when just touched upper band

### W03.  `H20=H20a AND T4=T4a AND session_bucket=london_open`
- Raw: n=190  W=167/L=23  WR=87.9%
- Refine: exclude BBP=BBP5 drops 10/23 losers (43%)
- **Final: n=168  W=155/L=13  WR=92.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=london_open  •  AVOID when just touched upper band

### W04.  `H20=H20a AND T4=T4a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=185  W=164/L=21  WR=88.6%
- Refine: exclude BBP=BBP5 drops 10/21 losers (48%)
- **Final: n=163  W=152/L=11  WR=93.3%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=london_open  •  AVOID when just touched upper band

### W05.  `T4=T4a AND RSI=RSI5 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=166  W=143/L=23  WR=86.1%
- Refine: exclude BBP=BBP5 drops 10/23 losers (43%)
- **Final: n=144  W=131/L=13  WR=91.0%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 60-70 strong; session=london_open  •  AVOID when just touched upper band

### W06.  `H20=H20a AND T4=T4a AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=157  W=136/L=21  WR=86.6%
- Refine: exclude BBP=BBP5 drops 10/21 losers (48%)
- **Final: n=135  W=124/L=11  WR=91.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 60-70 strong; session=london_open  •  AVOID when just touched upper band

### W07.  `T1=T1a AND T4=T4a AND session_bucket=london_open`
- Raw: n=149  W=136/L=13  WR=91.3%
- Refine: exclude BBP=BBP5 drops 6/13 losers (46%)
- **Final: n=135  W=128/L=7  WR=94.8%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; session=london_open  •  AVOID when just touched upper band

### W08.  `T1=T1a AND T4=T4a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=149  W=136/L=13  WR=91.3%
- Refine: exclude BBP=BBP5 drops 6/13 losers (46%)
- **Final: n=135  W=128/L=7  WR=94.8%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; session=london_open  •  AVOID when just touched upper band

### W09.  `T1=T1a AND ZS=ZS5 AND session_bucket=ny_open`
- Raw: n=146  W=126/L=20  WR=86.3%
- Refine: exclude H20=H20d drops 7/20 losers (35%)
- **Final: n=129  W=116/L=13  WR=89.9%**
- **Dir: ?**  •  1h trend WITH trade; zscore +2 to +3 deep overbought; session=ny_open  •  AVOID when HTF20 mildly against

### W10.  `T4=T4a AND BBP=BBP6 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=138  W=118/L=20  WR=85.5%
- Refine: exclude H60=H60e drops 17/20 losers (85%)
- **Final: n=68  W=65/L=3  WR=95.6%**
- **Dir: LONG**  •  4h trend WITH trade; deep above upper band; zscore +2 to +3 deep overbought  •  AVOID when HTF60 strongly against

### W11.  `H20=H20a AND T1=T1a AND T4=T4a AND session_bucket=london_open`
- Raw: n=137  W=126/L=11  WR=92.0%
- Refine: exclude BBP=BBP5 drops 6/11 losers (55%)
- **Final: n=123  W=118/L=5  WR=95.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; session=london_open  •  AVOID when just touched upper band

### W12.  `T1=T1a AND T4=T4a AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=118  W=105/L=13  WR=89.0%
- Refine: exclude BBP=BBP5 drops 6/13 losers (46%)
- **Final: n=104  W=97/L=7  WR=93.3%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 60-70 strong; session=london_open  •  AVOID when just touched upper band

### W13.  `H20=H20a AND BBP=BBP4 AND session_bucket=london_open`
- Raw: n=118  W=103/L=15  WR=87.3%
- Refine: exclude H60=H60d drops 6/15 losers (40%)
- **Final: n=104  W=95/L=9  WR=91.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; upper third; session=london_open  •  AVOID when HTF60 mildly against

### W14.  `T4=T4a AND ZS=ZS5 AND session_bucket=london_open`
- Raw: n=118  W=101/L=17  WR=85.6%
- Refine: exclude BBP=BBP5 drops 10/17 losers (59%)
- **Final: n=96  W=89/L=7  WR=92.7%**
- **Dir: ?**  •  4h trend WITH trade; zscore +2 to +3 deep overbought; session=london_open  •  AVOID when just touched upper band

### W15.  `T4=T4a AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=117  W=100/L=17  WR=85.5%
- Refine: exclude ZS=ZS3 drops 7/17 losers (41%)
- **Final: n=101  W=91/L=10  WR=90.1%**
- **Dir: SHORT**  •  4h trend WITH trade; session=ny_close  •  AVOID when zscore -1 to +1 neutral

### W16.  `T1=T1c AND T4=T4a AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=117  W=100/L=17  WR=85.5%
- Refine: exclude ZS=ZS3 drops 7/17 losers (41%)
- **Final: n=101  W=91/L=10  WR=90.1%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend WITH trade; session=ny_close  •  AVOID when zscore -1 to +1 neutral

### W17.  `T1=T1a AND T4=T4a AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=114  W=97/L=17  WR=85.1%
- Refine: exclude RSI=RSI5 drops 17/17 losers (100%)
- **Final: n=34  W=34/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; deep above upper band; zscore +2 to +3 deep overbought  •  AVOID when RSI 60-70 strong

### W18.  `H60=H60e AND T4=T4a AND session_bucket=london_open`
- Raw: n=113  W=103/L=10  WR=91.2%
- Refine: exclude BBP=BBP5 drops 6/10 losers (60%)
- **Final: n=107  W=103/L=4  WR=96.3%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; session=london_open  •  AVOID when just touched upper band

### W19.  `BBP=BBP2 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=113  W=103/L=10  WR=91.2%
- Refine: exclude H20=H20a drops 8/10 losers (80%)
- **Final: n=76  W=74/L=2  WR=97.4%**
- **Dir: SHORT**  •  lower third; session=ny_close  •  AVOID when HTF20 aligned WITH trade

### W20.  `T4=T4a AND BBP=BBP4 AND session_bucket=london_open`
- Raw: n=112  W=98/L=14  WR=87.5%
- Refine: exclude H60=H60d drops 9/14 losers (64%)
- **Final: n=82  W=77/L=5  WR=93.9%**
- **Dir: ?**  •  4h trend WITH trade; upper third; session=london_open  •  AVOID when HTF60 mildly against

### W21.  `T4=T4a AND ZS=ZS4 AND session_bucket=london_open`
- Raw: n=109  W=96/L=13  WR=88.1%
- Refine: exclude H60=H60d drops 8/13 losers (62%)
- **Final: n=80  W=75/L=5  WR=93.8%**
- **Dir: ?**  •  4h trend WITH trade; zscore +1 to +2 overbought; session=london_open  •  AVOID when HTF60 mildly against

### W22.  `T4=T4a AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=london_open`
- Raw: n=109  W=96/L=13  WR=88.1%
- Refine: exclude H60=H60d drops 8/13 losers (62%)
- **Final: n=80  W=75/L=5  WR=93.8%**
- **Dir: ?**  •  4h trend WITH trade; upper third; zscore +1 to +2 overbought; session=london_open  •  AVOID when HTF60 mildly against

### W23.  `T1=T1a AND BBP=BBP4 AND session_bucket=london_open`
- Raw: n=109  W=95/L=14  WR=87.2%
- Refine: exclude T4=T4c drops 9/14 losers (64%)
- **Final: n=74  W=69/L=5  WR=93.2%**
- **Dir: ?**  •  1h trend WITH trade; upper third; session=london_open  •  AVOID when 4h trend AGAINST trade

### W24.  `T1=T1a AND ZS=ZS4 AND session_bucket=london_open`
- Raw: n=107  W=93/L=14  WR=86.9%
- Refine: exclude T4=T4c drops 9/14 losers (64%)
- **Final: n=74  W=69/L=5  WR=93.2%**
- **Dir: ?**  •  1h trend WITH trade; zscore +1 to +2 overbought; session=london_open  •  AVOID when 4h trend AGAINST trade

### W25.  `H20=H20a AND BBP=BBP4 AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=107  W=93/L=14  WR=86.9%
- Refine: exclude H60=H60d drops 5/14 losers (36%)
- **Final: n=94  W=85/L=9  WR=90.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; upper third; RSI 60-70 strong; session=london_open  •  AVOID when HTF60 mildly against

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T4=T4c AND ZS=ZS5 AND direction_exec=short`
- Raw: n=323  W=122/L=201  WR=37.8%
- Sharpen: sharpest is T1=T1c (186/201 of losers there)
- **Sharp: n=278  W=92/L=186  WR=33.1%**
- **Dir: SHORT**  •  4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when 1h trend AGAINST trade

### L02.  `T1=T1c AND T4=T4c AND ZS=ZS5`
- Raw: n=278  W=92/L=186  WR=33.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=278  W=92/L=186  WR=33.1%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought

### L03.  `T1=T1c AND T4=T4c AND ZS=ZS5 AND direction_exec=short`
- Raw: n=278  W=92/L=186  WR=33.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=278  W=92/L=186  WR=33.1%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought

### L04.  `T1=T1a AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=260  W=102/L=158  WR=39.2%
- Sharpen: sharpest is T4=T4c (58/158 of losers there)
- **Sharp: n=67  W=9/L=58  WR=13.4%**
- **Dir: LONG**  •  1h trend WITH trade; session=ny_close  •  ONLY when 4h trend AGAINST trade

### L05.  `H60=H60a AND T4=T4c AND ZS=ZS5`
- Raw: n=252  W=95/L=157  WR=37.7%
- Sharpen: sharpest is H20=H20a (58/157 of losers there)
- **Sharp: n=72  W=14/L=58  WR=19.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when HTF20 aligned WITH trade

### L06.  `T4=T4c AND RSI=RSI5 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=245  W=93/L=152  WR=38.0%
- Sharpen: sharpest is H20=H20a (47/152 of losers there)
- **Sharp: n=58  W=11/L=47  WR=19.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  ONLY when HTF20 aligned WITH trade

### L07.  `H60=H60a AND ZS=ZS5 AND direction_exec=short`
- Raw: n=232  W=83/L=149  WR=35.8%
- Sharpen: sharpest is H20=H20a (31/149 of losers there)
- **Sharp: n=33  W=2/L=31  WR=6.1%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; zscore +2 to +3 deep overbought  •  ONLY when HTF20 aligned WITH trade

### L08.  `T1=T1c AND RSI=RSI5 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=232  W=91/L=141  WR=39.2%
- Sharpen: sharpest is H60=H60a (120/141 of losers there)
- **Sharp: n=175  W=55/L=120  WR=31.4%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 60-70 strong; session=ny_open  •  ONLY when HTF60 aligned WITH trade

### L09.  `T1=T1c AND T4=T4c AND session_bucket=ny_open`
- Raw: n=225  W=89/L=136  WR=39.6%
- Sharpen: sharpest is H60=H60a (110/136 of losers there)
- **Sharp: n=165  W=55/L=110  WR=33.3%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_open  •  ONLY when HTF60 aligned WITH trade

### L10.  `T1=T1c AND T4=T4c AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=225  W=89/L=136  WR=39.6%
- Sharpen: sharpest is H60=H60a (110/136 of losers there)
- **Sharp: n=165  W=55/L=110  WR=33.3%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_open  •  ONLY when HTF60 aligned WITH trade

### L11.  `H60=H60a AND T1=T1c AND ZS=ZS5`
- Raw: n=220  W=67/L=153  WR=30.5%
- Sharpen: sharpest is H20=H20a (38/153 of losers there)
- **Sharp: n=40  W=2/L=38  WR=5.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when HTF20 aligned WITH trade

### L12.  `T1=T1c AND T4=T4c AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=219  W=79/L=140  WR=36.1%
- Sharpen: sharpest is H20=H20a (47/140 of losers there)
- **Sharp: n=58  W=11/L=47  WR=19.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  ONLY when HTF20 aligned WITH trade

### L13.  `H60=H60a AND T1=T1c AND ZS=ZS5 AND direction_exec=short`
- Raw: n=213  W=67/L=146  WR=31.5%
- Sharpen: sharpest is H20=H20a (31/146 of losers there)
- **Sharp: n=33  W=2/L=31  WR=6.1%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when HTF20 aligned WITH trade

### L14.  `H60=H60a AND T4=T4c AND ZS=ZS5 AND direction_exec=short`
- Raw: n=211  W=83/L=128  WR=39.3%
- Sharpen: sharpest is H20=H20a (31/128 of losers there)
- **Sharp: n=33  W=2/L=31  WR=6.1%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when HTF20 aligned WITH trade

### L15.  `H60=H60a AND T1=T1c AND session_bucket=ny_open`
- Raw: n=205  W=77/L=128  WR=37.6%
- Sharpen: sharpest is direction_exec=short (120/128 of losers there)
- **Sharp: n=175  W=55/L=120  WR=31.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=ny_open  •  ONLY when short

### L16.  `H20=H20e AND T1=T1c AND T4=T4c AND ZS=ZS5`
- Raw: n=203  W=74/L=129  WR=36.5%
- Sharpen: sharpest is H60=H60e (23/129 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when HTF60 strongly against

### L17.  `H60=H60a AND RSI=RSI5 AND session_bucket=ny_open`
- Raw: n=195  W=68/L=127  WR=34.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=195  W=68/L=127  WR=34.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 60-70 strong; session=ny_open

### L18.  `H60=H60a AND T1=T1c AND RSI=RSI5 AND session_bucket=ny_open`
- Raw: n=195  W=68/L=127  WR=34.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=195  W=68/L=127  WR=34.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 60-70 strong; session=ny_open

### L19.  `H60=H60a AND T1=T1c AND T4=T4c AND ZS=ZS5`
- Raw: n=192  W=67/L=125  WR=34.9%
- Sharpen: sharpest is H20=H20a (31/125 of losers there)
- **Sharp: n=33  W=2/L=31  WR=6.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when HTF20 aligned WITH trade

### L20.  `T4=T4c AND direction_exec=short AND session_bucket=london_open`
- Raw: n=191  W=74/L=117  WR=38.7%
- Sharpen: sharpest is BBP=BBP6 (42/117 of losers there)
- **Sharp: n=42  W=0/L=42  WR=0.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; session=london_open  •  ONLY when deep above upper band

### L21.  `H20=H20a AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=186  W=51/L=135  WR=27.4%
- Sharpen: sharpest is T4=T4c (43/135 of losers there)
- **Sharp: n=48  W=5/L=43  WR=10.4%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; session=ny_close  •  ONLY when 4h trend AGAINST trade

### L22.  `H60=H60a AND T4=T4c AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=185  W=66/L=119  WR=35.7%
- Sharpen: sharpest is H20=H20a (50/119 of losers there)
- **Sharp: n=64  W=14/L=50  WR=21.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  ONLY when HTF20 aligned WITH trade

### L23.  `T1=T1c AND T4=T4c AND BBP=BBP5`
- Raw: n=180  W=63/L=117  WR=35.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=180  W=63/L=117  WR=35.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; just touched upper band

### L24.  `T1=T1c AND T4=T4c AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=180  W=63/L=117  WR=35.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=180  W=63/L=117  WR=35.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; just touched upper band; zscore +2 to +3 deep overbought

### L25.  `T1=T1c AND T4=T4c AND BBP=BBP5 AND direction_exec=short`
- Raw: n=180  W=63/L=117  WR=35.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=180  W=63/L=117  WR=35.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; just touched upper band

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | H60a(32/38) |
| T1 | T1a(52/44) | T1c(48/56) |
| T4 | T4a(55/43) | T4c(45/57) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
