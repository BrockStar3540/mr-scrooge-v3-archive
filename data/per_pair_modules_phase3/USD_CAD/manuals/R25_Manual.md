# USD_CAD — R25 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **2,308**  (W=1,478 / L=830)  -  WR: **64.0%**

## Session distribution

- ny_mid: n=733  W=462/L=271  WR=63.0%
- ny_open: n=574  W=359/L=215  WR=62.5%
- ny_close: n=379  W=253/L=126  WR=66.8%
- asia: n=260  W=172/L=88  WR=66.2%
- london_open: n=151  W=96/L=55  WR=63.6%
- london: n=136  W=90/L=46  WR=66.2%
- asia_late: n=48  W=32/L=16  WR=66.7%
- off_hours: n=27  W=14/L=13  WR=51.9%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1a AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=324  W=282/L=42  WR=87.0%
- Refine: exclude H60=H60e drops 20/42 losers (48%)
- **Final: n=262  W=240/L=22  WR=91.6%**
- **Dir: SHORT**  •  1h trend WITH trade; session=ny_open  •  AVOID when HTF60 strongly against

### W02.  `T1=T1a AND T4=T4a AND session_bucket=ny_open`
- Raw: n=318  W=282/L=36  WR=88.7%
- Refine: exclude H60=H60e drops 20/36 losers (56%)
- **Final: n=256  W=240/L=16  WR=93.8%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; session=ny_open  •  AVOID when HTF60 strongly against

### W03.  `T4=T4a AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=318  W=282/L=36  WR=88.7%
- Refine: exclude H60=H60e drops 20/36 losers (56%)
- **Final: n=256  W=240/L=16  WR=93.8%**
- **Dir: SHORT**  •  4h trend WITH trade; session=ny_open  •  AVOID when HTF60 strongly against

### W04.  `T1=T1a AND T4=T4a AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=318  W=282/L=36  WR=88.7%
- Refine: exclude H60=H60e drops 20/36 losers (56%)
- **Final: n=256  W=240/L=16  WR=93.8%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend WITH trade; session=ny_open  •  AVOID when HTF60 strongly against

### W05.  `H20=H20a AND RSI=RSI2 AND direction_exec=short`
- Raw: n=294  W=250/L=44  WR=85.0%
- Refine: exclude session_bucket=ny_mid drops 23/44 losers (52%)
- **Final: n=251  W=230/L=21  WR=91.6%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 30-40 weak  •  AVOID when session=ny_mid

### W06.  `H20=H20a AND T4=T4a AND RSI=RSI2`
- Raw: n=267  W=227/L=40  WR=85.0%
- Refine: exclude session_bucket=ny_mid drops 23/40 losers (57%)
- **Final: n=224  W=207/L=17  WR=92.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 30-40 weak  •  AVOID when session=ny_mid

### W07.  `H20=H20a AND T4=T4a AND RSI=RSI2 AND direction_exec=short`
- Raw: n=263  W=226/L=37  WR=85.9%
- Refine: exclude session_bucket=ny_mid drops 23/37 losers (62%)
- **Final: n=220  W=206/L=14  WR=93.6%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 30-40 weak  •  AVOID when session=ny_mid

### W08.  `H20=H20a AND T1=T1a AND T4=T4a AND RSI=RSI2`
- Raw: n=255  W=218/L=37  WR=85.5%
- Refine: exclude session_bucket=ny_mid drops 23/37 losers (62%)
- **Final: n=212  W=198/L=14  WR=93.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; RSI 30-40 weak  •  AVOID when session=ny_mid

### W09.  `H60=H60a AND T1=T1a AND session_bucket=ny_open`
- Raw: n=236  W=220/L=16  WR=93.2%
- Refine: exclude H20=H20d drops 12/16 losers (75%)
- **Final: n=169  W=165/L=4  WR=97.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=ny_open  •  AVOID when HTF20 mildly against

### W10.  `H60=H60a AND T4=T4a AND session_bucket=ny_open`
- Raw: n=236  W=220/L=16  WR=93.2%
- Refine: exclude H20=H20d drops 12/16 losers (75%)
- **Final: n=169  W=165/L=4  WR=97.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; session=ny_open  •  AVOID when HTF20 mildly against

### W11.  `H60=H60a AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=236  W=220/L=16  WR=93.2%
- Refine: exclude H20=H20d drops 12/16 losers (75%)
- **Final: n=169  W=165/L=4  WR=97.6%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; session=ny_open  •  AVOID when HTF20 mildly against

### W12.  `H60=H60a AND T1=T1a AND T4=T4a AND session_bucket=ny_open`
- Raw: n=236  W=220/L=16  WR=93.2%
- Refine: exclude H20=H20d drops 12/16 losers (75%)
- **Final: n=169  W=165/L=4  WR=97.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; session=ny_open  •  AVOID when HTF20 mildly against

### W13.  `H60=H60a AND T1=T1a AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=236  W=220/L=16  WR=93.2%
- Refine: exclude H20=H20d drops 12/16 losers (75%)
- **Final: n=169  W=165/L=4  WR=97.6%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=ny_open  •  AVOID when HTF20 mildly against

### W14.  `H60=H60a AND T4=T4a AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=236  W=220/L=16  WR=93.2%
- Refine: exclude H20=H20d drops 12/16 losers (75%)
- **Final: n=169  W=165/L=4  WR=97.6%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend WITH trade; session=ny_open  •  AVOID when HTF20 mildly against

### W15.  `T4=T4a AND BBP=BBP2 AND session_bucket=ny_open`
- Raw: n=206  W=191/L=15  WR=92.7%
- Refine: exclude H20=H20b drops 8/15 losers (53%)
- **Final: n=168  W=161/L=7  WR=95.8%**
- **Dir: ?**  •  4h trend WITH trade; lower third; session=ny_open  •  AVOID when HTF20 slightly aligned

### W16.  `T4=T4a AND ZS=ZS2 AND session_bucket=ny_open`
- Raw: n=206  W=191/L=15  WR=92.7%
- Refine: exclude H20=H20b drops 8/15 losers (53%)
- **Final: n=168  W=161/L=7  WR=95.8%**
- **Dir: ?**  •  4h trend WITH trade; zscore -2 to -1 oversold; session=ny_open  •  AVOID when HTF20 slightly aligned

### W17.  `T4=T4a AND BBP=BBP2 AND ZS=ZS2 AND session_bucket=ny_open`
- Raw: n=206  W=191/L=15  WR=92.7%
- Refine: exclude H20=H20b drops 8/15 losers (53%)
- **Final: n=168  W=161/L=7  WR=95.8%**
- **Dir: ?**  •  4h trend WITH trade; lower third; zscore -2 to -1 oversold; session=ny_open  •  AVOID when HTF20 slightly aligned

### W18.  `T1=T1a AND BBP=BBP2 AND session_bucket=ny_open`
- Raw: n=203  W=185/L=18  WR=91.1%
- Refine: exclude H20=H20b drops 8/18 losers (44%)
- **Final: n=165  W=155/L=10  WR=93.9%**
- **Dir: ?**  •  1h trend WITH trade; lower third; session=ny_open  •  AVOID when HTF20 slightly aligned

### W19.  `BBP=BBP2 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=203  W=185/L=18  WR=91.1%
- Refine: exclude H20=H20b drops 8/18 losers (44%)
- **Final: n=165  W=155/L=10  WR=93.9%**
- **Dir: SHORT**  •  lower third; session=ny_open  •  AVOID when HTF20 slightly aligned

### W20.  `T1=T1a AND BBP=BBP2 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=203  W=185/L=18  WR=91.1%
- Refine: exclude H20=H20b drops 8/18 losers (44%)
- **Final: n=165  W=155/L=10  WR=93.9%**
- **Dir: SHORT**  •  1h trend WITH trade; lower third; session=ny_open  •  AVOID when HTF20 slightly aligned

### W21.  `T1=T1a AND ZS=ZS2 AND session_bucket=ny_open`
- Raw: n=202  W=185/L=17  WR=91.6%
- Refine: exclude H20=H20b drops 8/17 losers (47%)
- **Final: n=164  W=155/L=9  WR=94.5%**
- **Dir: ?**  •  1h trend WITH trade; zscore -2 to -1 oversold; session=ny_open  •  AVOID when HTF20 slightly aligned

### W22.  `ZS=ZS2 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=202  W=185/L=17  WR=91.6%
- Refine: exclude H20=H20b drops 8/17 losers (47%)
- **Final: n=164  W=155/L=9  WR=94.5%**
- **Dir: SHORT**  •  zscore -2 to -1 oversold; session=ny_open  •  AVOID when HTF20 slightly aligned

### W23.  `T1=T1a AND BBP=BBP2 AND ZS=ZS2 AND session_bucket=ny_open`
- Raw: n=202  W=185/L=17  WR=91.6%
- Refine: exclude H20=H20b drops 8/17 losers (47%)
- **Final: n=164  W=155/L=9  WR=94.5%**
- **Dir: ?**  •  1h trend WITH trade; lower third; zscore -2 to -1 oversold; session=ny_open  •  AVOID when HTF20 slightly aligned

### W24.  `T1=T1a AND ZS=ZS2 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=202  W=185/L=17  WR=91.6%
- Refine: exclude H20=H20b drops 8/17 losers (47%)
- **Final: n=164  W=155/L=9  WR=94.5%**
- **Dir: SHORT**  •  1h trend WITH trade; zscore -2 to -1 oversold; session=ny_open  •  AVOID when HTF20 slightly aligned

### W25.  `BBP=BBP2 AND ZS=ZS2 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=202  W=185/L=17  WR=91.6%
- Refine: exclude H20=H20b drops 8/17 losers (47%)
- **Final: n=164  W=155/L=9  WR=94.5%**
- **Dir: SHORT**  •  lower third; zscore -2 to -1 oversold; session=ny_open  •  AVOID when HTF20 slightly aligned

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1c AND BBP=BBP2 AND RSI=RSI1`
- Raw: n=273  W=107/L=166  WR=39.2%
- Sharpen: sharpest is session_bucket=ny_open (61/166 of losers there)
- **Sharp: n=77  W=16/L=61  WR=20.8%**
- **Dir: ?**  •  1h trend AGAINST trade; lower third; RSI 20-30 oversold  •  ONLY when session=ny_open

### L02.  `BBP=BBP2 AND RSI=RSI1 AND direction_exec=long`
- Raw: n=273  W=107/L=166  WR=39.2%
- Sharpen: sharpest is session_bucket=ny_open (61/166 of losers there)
- **Sharp: n=77  W=16/L=61  WR=20.8%**
- **Dir: LONG**  •  lower third; RSI 20-30 oversold  •  ONLY when session=ny_open

### L03.  `T1=T1c AND BBP=BBP2 AND RSI=RSI1 AND direction_exec=long`
- Raw: n=273  W=107/L=166  WR=39.2%
- Sharpen: sharpest is session_bucket=ny_open (61/166 of losers there)
- **Sharp: n=77  W=16/L=61  WR=20.8%**
- **Dir: LONG**  •  1h trend AGAINST trade; lower third; RSI 20-30 oversold  •  ONLY when session=ny_open

### L04.  `T4=T4c AND BBP=BBP2 AND RSI=RSI1`
- Raw: n=270  W=101/L=169  WR=37.4%
- Sharpen: sharpest is session_bucket=ny_open (64/169 of losers there)
- **Sharp: n=74  W=10/L=64  WR=13.5%**
- **Dir: ?**  •  4h trend AGAINST trade; lower third; RSI 20-30 oversold  •  ONLY when session=ny_open

### L05.  `T1=T1c AND T4=T4c AND BBP=BBP2 AND RSI=RSI1`
- Raw: n=266  W=101/L=165  WR=38.0%
- Sharpen: sharpest is session_bucket=ny_open (60/165 of losers there)
- **Sharp: n=70  W=10/L=60  WR=14.3%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; lower third; RSI 20-30 oversold  •  ONLY when session=ny_open

### L06.  `T4=T4c AND BBP=BBP2 AND RSI=RSI1 AND direction_exec=long`
- Raw: n=266  W=101/L=165  WR=38.0%
- Sharpen: sharpest is session_bucket=ny_open (60/165 of losers there)
- **Sharp: n=70  W=10/L=60  WR=14.3%**
- **Dir: LONG**  •  4h trend AGAINST trade; lower third; RSI 20-30 oversold  •  ONLY when session=ny_open

### L07.  `T4=T4c AND RSI=RSI1 AND ZS=ZS2`
- Raw: n=256  W=99/L=157  WR=38.7%
- Sharpen: sharpest is session_bucket=ny_open (63/157 of losers there)
- **Sharp: n=73  W=10/L=63  WR=13.7%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 20-30 oversold; zscore -2 to -1 oversold  •  ONLY when session=ny_open

### L08.  `T4=T4c AND BBP=BBP2 AND RSI=RSI1 AND ZS=ZS2`
- Raw: n=256  W=99/L=157  WR=38.7%
- Sharpen: sharpest is session_bucket=ny_open (63/157 of losers there)
- **Sharp: n=73  W=10/L=63  WR=13.7%**
- **Dir: ?**  •  4h trend AGAINST trade; lower third; RSI 20-30 oversold; zscore -2 to -1 oversold  •  ONLY when session=ny_open

### L09.  `T1=T1c AND T4=T4c AND RSI=RSI1 AND ZS=ZS2`
- Raw: n=253  W=99/L=154  WR=39.1%
- Sharpen: sharpest is session_bucket=ny_open (60/154 of losers there)
- **Sharp: n=70  W=10/L=60  WR=14.3%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 20-30 oversold; zscore -2 to -1 oversold  •  ONLY when session=ny_open

### L10.  `T4=T4c AND RSI=RSI1 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=253  W=99/L=154  WR=39.1%
- Sharpen: sharpest is session_bucket=ny_open (60/154 of losers there)
- **Sharp: n=70  W=10/L=60  WR=14.3%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 20-30 oversold; zscore -2 to -1 oversold  •  ONLY when session=ny_open

### L11.  `T1=T1c AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=250  W=77/L=173  WR=30.8%
- Sharpen: sharpest is H20=H20e (91/173 of losers there)
- **Sharp: n=100  W=9/L=91  WR=9.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; session=ny_open  •  ONLY when HTF20 strongly against

### L12.  `T1=T1c AND T4=T4c AND session_bucket=ny_open`
- Raw: n=241  W=69/L=172  WR=28.6%
- Sharpen: sharpest is H20=H20e (91/172 of losers there)
- **Sharp: n=100  W=9/L=91  WR=9.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_open  •  ONLY when HTF20 strongly against

### L13.  `T4=T4c AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=241  W=69/L=172  WR=28.6%
- Sharpen: sharpest is H20=H20e (91/172 of losers there)
- **Sharp: n=100  W=9/L=91  WR=9.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; session=ny_open  •  ONLY when HTF20 strongly against

### L14.  `T1=T1c AND T4=T4c AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=241  W=69/L=172  WR=28.6%
- Sharpen: sharpest is H20=H20e (91/172 of losers there)
- **Sharp: n=100  W=9/L=91  WR=9.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_open  •  ONLY when HTF20 strongly against

### L15.  `H20=H20e AND RSI=RSI2 AND direction_exec=long`
- Raw: n=238  W=93/L=145  WR=39.1%
- Sharpen: sharpest is session_bucket=ny_open (73/145 of losers there)
- **Sharp: n=77  W=4/L=73  WR=5.2%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 30-40 weak  •  ONLY when session=ny_open

### L16.  `H20=H20e AND T1=T1c AND RSI=RSI2`
- Raw: n=234  W=93/L=141  WR=39.7%
- Sharpen: sharpest is session_bucket=ny_open (73/141 of losers there)
- **Sharp: n=77  W=4/L=73  WR=5.2%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 30-40 weak  •  ONLY when session=ny_open

### L17.  `H20=H20e AND T1=T1c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=234  W=93/L=141  WR=39.7%
- Sharpen: sharpest is session_bucket=ny_open (73/141 of losers there)
- **Sharp: n=77  W=4/L=73  WR=5.2%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 30-40 weak  •  ONLY when session=ny_open

### L18.  `H20=H20e AND T4=T4c AND RSI=RSI2`
- Raw: n=220  W=84/L=136  WR=38.2%
- Sharpen: sharpest is session_bucket=ny_open (73/136 of losers there)
- **Sharp: n=77  W=4/L=73  WR=5.2%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when session=ny_open

### L19.  `H20=H20e AND T4=T4c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=213  W=78/L=135  WR=36.6%
- Sharpen: sharpest is session_bucket=ny_open (73/135 of losers there)
- **Sharp: n=77  W=4/L=73  WR=5.2%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when session=ny_open

### L20.  `H20=H20e AND T1=T1c AND T4=T4c AND RSI=RSI2`
- Raw: n=209  W=78/L=131  WR=37.3%
- Sharpen: sharpest is session_bucket=ny_open (73/131 of losers there)
- **Sharp: n=77  W=4/L=73  WR=5.2%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 30-40 weak  •  ONLY when session=ny_open

### L21.  `H20=H20e AND T4=T4c AND BBP=BBP2`
- Raw: n=195  W=76/L=119  WR=39.0%
- Sharpen: sharpest is session_bucket=ny_open (45/119 of losers there)
- **Sharp: n=50  W=5/L=45  WR=10.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; lower third  •  ONLY when session=ny_open

### L22.  `H20=H20e AND T4=T4c AND ZS=ZS2`
- Raw: n=187  W=73/L=114  WR=39.0%
- Sharpen: sharpest is session_bucket=ny_open (44/114 of losers there)
- **Sharp: n=49  W=5/L=44  WR=10.2%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; zscore -2 to -1 oversold  •  ONLY when session=ny_open

### L23.  `H20=H20e AND T4=T4c AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=187  W=73/L=114  WR=39.0%
- Sharpen: sharpest is session_bucket=ny_open (44/114 of losers there)
- **Sharp: n=49  W=5/L=44  WR=10.2%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; lower third; zscore -2 to -1 oversold  •  ONLY when session=ny_open

### L24.  `H20=H20e AND T4=T4c AND ZS=ZS2 AND direction_exec=long`
- Raw: n=183  W=73/L=110  WR=39.9%
- Sharpen: sharpest is session_bucket=ny_open (41/110 of losers there)
- **Sharp: n=46  W=5/L=41  WR=10.9%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend AGAINST trade; zscore -2 to -1 oversold  •  ONLY when session=ny_open

### L25.  `H60=H60e AND T1=T1c AND session_bucket=ny_open`
- Raw: n=167  W=36/L=131  WR=21.6%
- Sharpen: sharpest is H20=H20e (77/131 of losers there)
- **Sharp: n=84  W=7/L=77  WR=8.3%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; session=ny_open  •  ONLY when HTF20 strongly against

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(38/33) | H20e(34/39) |
| H60 | H60a(54/29), H60b(10/2) | H60e(31/54), H60d(2/11) |
| T1 | T1a(64/34) | T1c(36/66) |
| T4 | T4a(62/36) | T4c(38/64) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(62/36) | long(38/64) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
