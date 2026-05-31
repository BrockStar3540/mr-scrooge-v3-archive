# GBP_JPY — R23 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50a**  (EMA50 up >0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **3,953**  (W=2,403 / L=1,550)  -  WR: **60.8%**

## Session distribution

- london_open: n=1114  W=658/L=456  WR=59.1%
- asia: n=946  W=573/L=373  WR=60.6%
- ny_open: n=456  W=269/L=187  WR=59.0%
- ny_mid: n=439  W=283/L=156  WR=64.5%
- asia_late: n=364  W=225/L=139  WR=61.8%
- london: n=327  W=198/L=129  WR=60.6%
- ny_close: n=307  W=197/L=110  WR=64.2%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60a AND BBP=BBP4 AND RSI=RSI6`
- Raw: n=352  W=300/L=52  WR=85.2%
- Refine: exclude session_bucket=ny_mid drops 19/52 losers (37%)
- **Final: n=281  W=248/L=33  WR=88.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; upper third; RSI 70-80 overbought  •  AVOID when session=ny_mid

### W02.  `T1=T1a AND BBP=BBP4 AND RSI=RSI6`
- Raw: n=352  W=300/L=52  WR=85.2%
- Refine: exclude session_bucket=ny_mid drops 19/52 losers (37%)
- **Final: n=281  W=248/L=33  WR=88.3%**
- **Dir: ?**  •  1h trend WITH trade; upper third; RSI 70-80 overbought  •  AVOID when session=ny_mid

### W03.  `BBP=BBP4 AND RSI=RSI6 AND direction_exec=long`
- Raw: n=352  W=300/L=52  WR=85.2%
- Refine: exclude session_bucket=ny_mid drops 19/52 losers (37%)
- **Final: n=281  W=248/L=33  WR=88.3%**
- **Dir: LONG**  •  upper third; RSI 70-80 overbought  •  AVOID when session=ny_mid

### W04.  `H60=H60a AND T1=T1a AND BBP=BBP4 AND RSI=RSI6`
- Raw: n=352  W=300/L=52  WR=85.2%
- Refine: exclude session_bucket=ny_mid drops 19/52 losers (37%)
- **Final: n=281  W=248/L=33  WR=88.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; upper third; RSI 70-80 overbought  •  AVOID when session=ny_mid

### W05.  `H60=H60a AND BBP=BBP4 AND RSI=RSI6 AND direction_exec=long`
- Raw: n=352  W=300/L=52  WR=85.2%
- Refine: exclude session_bucket=ny_mid drops 19/52 losers (37%)
- **Final: n=281  W=248/L=33  WR=88.3%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; upper third; RSI 70-80 overbought  •  AVOID when session=ny_mid

### W06.  `T1=T1a AND BBP=BBP4 AND RSI=RSI6 AND direction_exec=long`
- Raw: n=352  W=300/L=52  WR=85.2%
- Refine: exclude session_bucket=ny_mid drops 19/52 losers (37%)
- **Final: n=281  W=248/L=33  WR=88.3%**
- **Dir: LONG**  •  1h trend WITH trade; upper third; RSI 70-80 overbought  •  AVOID when session=ny_mid

### W07.  `H20=H20a AND H60=H60a AND BBP=BBP4 AND RSI=RSI6`
- Raw: n=320  W=273/L=47  WR=85.3%
- Refine: exclude session_bucket=ny_mid drops 18/47 losers (38%)
- **Final: n=258  W=229/L=29  WR=88.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; upper third; RSI 70-80 overbought  •  AVOID when session=ny_mid

### W08.  `H20=H20a AND T1=T1a AND BBP=BBP4 AND RSI=RSI6`
- Raw: n=320  W=273/L=47  WR=85.3%
- Refine: exclude session_bucket=ny_mid drops 18/47 losers (38%)
- **Final: n=258  W=229/L=29  WR=88.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; upper third; RSI 70-80 overbought  •  AVOID when session=ny_mid

### W09.  `H20=H20a AND BBP=BBP4 AND RSI=RSI6 AND direction_exec=long`
- Raw: n=320  W=273/L=47  WR=85.3%
- Refine: exclude session_bucket=ny_mid drops 18/47 losers (38%)
- **Final: n=258  W=229/L=29  WR=88.8%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; upper third; RSI 70-80 overbought  •  AVOID when session=ny_mid

### W10.  `H60=H60a AND T1=T1a AND T4=T4a AND session_bucket=london_open`
- Raw: n=276  W=235/L=41  WR=85.1%
- Refine: exclude RSI=RSI7 drops 12/41 losers (29%)
- **Final: n=235  W=206/L=29  WR=87.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; session=london_open  •  AVOID when RSI>80 extreme overbought

### W11.  `T1=T1a AND T4=T4a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=276  W=235/L=41  WR=85.1%
- Refine: exclude RSI=RSI7 drops 12/41 losers (29%)
- **Final: n=235  W=206/L=29  WR=87.7%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; session=london_open  •  AVOID when RSI>80 extreme overbought

### W12.  `H20=H20a AND T1=T1a AND T4=T4a AND session_bucket=london_open`
- Raw: n=224  W=192/L=32  WR=85.7%
- Refine: exclude RSI=RSI7 drops 12/32 losers (38%)
- **Final: n=183  W=163/L=20  WR=89.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; session=london_open  •  AVOID when RSI>80 extreme overbought

### W13.  `H60=H60a AND T4=T4a AND BBP=BBP4 AND session_bucket=london_open`
- Raw: n=188  W=164/L=24  WR=87.2%
- Refine: exclude RSI=RSI7 drops 7/24 losers (29%)
- **Final: n=159  W=142/L=17  WR=89.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; upper third; session=london_open  •  AVOID when RSI>80 extreme overbought

### W14.  `T4=T4a AND BBP=BBP4 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=188  W=164/L=24  WR=87.2%
- Refine: exclude RSI=RSI7 drops 7/24 losers (29%)
- **Final: n=159  W=142/L=17  WR=89.3%**
- **Dir: LONG**  •  4h trend WITH trade; upper third; session=london_open  •  AVOID when RSI>80 extreme overbought

### W15.  `T1=T1a AND T4=T4a AND BBP=BBP4 AND session_bucket=london_open`
- Raw: n=179  W=154/L=25  WR=86.0%
- Refine: no further refinement
- **Final: n=179  W=154/L=25  WR=86.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; upper third; session=london_open

### W16.  `H60=H60a AND T4=T4a AND ZS=ZS4 AND session_bucket=london_open`
- Raw: n=173  W=149/L=24  WR=86.1%
- Refine: no further refinement
- **Final: n=173  W=149/L=24  WR=86.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; zscore +1 to +2 overbought; session=london_open

### W17.  `T4=T4a AND ZS=ZS4 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=173  W=149/L=24  WR=86.1%
- Refine: no further refinement
- **Final: n=173  W=149/L=24  WR=86.1%**
- **Dir: LONG**  •  4h trend WITH trade; zscore +1 to +2 overbought; session=london_open

### W18.  `T1=T1a AND T4=T4a AND ZS=ZS4 AND session_bucket=london_open`
- Raw: n=172  W=147/L=25  WR=85.5%
- Refine: no further refinement
- **Final: n=172  W=147/L=25  WR=85.5%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; zscore +1 to +2 overbought; session=london_open

### W19.  `H20=H20b AND H60=H60a AND T1=T1a`
- Raw: n=159  W=138/L=21  WR=86.8%
- Refine: exclude ZS=ZS4 drops 15/21 losers (71%)
- **Final: n=86  W=80/L=6  WR=93.0%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 1h trend WITH trade  •  AVOID when zscore +1 to +2 overbought

### W20.  `H20=H20b AND T1=T1a AND direction_exec=long`
- Raw: n=159  W=138/L=21  WR=86.8%
- Refine: exclude ZS=ZS4 drops 15/21 losers (71%)
- **Final: n=86  W=80/L=6  WR=93.0%**
- **Dir: LONG**  •  HTF20 slightly aligned; 1h trend WITH trade  •  AVOID when zscore +1 to +2 overbought

### W21.  `H20=H20b AND H60=H60a AND T1=T1a AND direction_exec=long`
- Raw: n=159  W=138/L=21  WR=86.8%
- Refine: exclude ZS=ZS4 drops 15/21 losers (71%)
- **Final: n=86  W=80/L=6  WR=93.0%**
- **Dir: LONG**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 1h trend WITH trade  •  AVOID when zscore +1 to +2 overbought

### W22.  `H20=H20b AND T1=T1a AND T4=T4a`
- Raw: n=158  W=138/L=20  WR=87.3%
- Refine: exclude ZS=ZS4 drops 14/20 losers (70%)
- **Final: n=86  W=80/L=6  WR=93.0%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when zscore +1 to +2 overbought

### W23.  `H20=H20b AND H60=H60a AND T1=T1a AND T4=T4a`
- Raw: n=158  W=138/L=20  WR=87.3%
- Refine: exclude ZS=ZS4 drops 14/20 losers (70%)
- **Final: n=86  W=80/L=6  WR=93.0%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when zscore +1 to +2 overbought

### W24.  `H20=H20b AND T1=T1a AND T4=T4a AND direction_exec=long`
- Raw: n=158  W=138/L=20  WR=87.3%
- Refine: exclude ZS=ZS4 drops 14/20 losers (70%)
- **Final: n=86  W=80/L=6  WR=93.0%**
- **Dir: LONG**  •  HTF20 slightly aligned; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when zscore +1 to +2 overbought

### W25.  `H20=H20a AND RSI=RSI6 AND session_bucket=asia`
- Raw: n=132  W=122/L=10  WR=92.4%
- Refine: exclude strategy_id=bravo_expansion_continuation drops 2/10 losers (20%)
- **Final: n=126  W=118/L=8  WR=93.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 70-80 overbought; session=asia  •  AVOID when strategy=bravo_expansion_continuation

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND T1=T1c AND RSI=RSI6`
- Raw: n=548  W=210/L=338  WR=38.3%
- Sharpen: sharpest is session_bucket=asia (88/338 of losers there)
- **Sharp: n=102  W=14/L=88  WR=13.7%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when session=asia

### L02.  `H60=H60e AND RSI=RSI6 AND direction_exec=short`
- Raw: n=548  W=210/L=338  WR=38.3%
- Sharpen: sharpest is session_bucket=asia (88/338 of losers there)
- **Sharp: n=102  W=14/L=88  WR=13.7%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 70-80 overbought  •  ONLY when session=asia

### L03.  `T1=T1c AND RSI=RSI6 AND direction_exec=short`
- Raw: n=548  W=210/L=338  WR=38.3%
- Sharpen: sharpest is session_bucket=asia (88/338 of losers there)
- **Sharp: n=102  W=14/L=88  WR=13.7%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when session=asia

### L04.  `H60=H60e AND T1=T1c AND RSI=RSI6 AND direction_exec=short`
- Raw: n=548  W=210/L=338  WR=38.3%
- Sharpen: sharpest is session_bucket=asia (88/338 of losers there)
- **Sharp: n=102  W=14/L=88  WR=13.7%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when session=asia

### L05.  `H60=H60e AND T4=T4c AND RSI=RSI6`
- Raw: n=494  W=190/L=304  WR=38.5%
- Sharpen: sharpest is session_bucket=asia (88/304 of losers there)
- **Sharp: n=102  W=14/L=88  WR=13.7%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when session=asia

### L06.  `T1=T1c AND T4=T4c AND RSI=RSI6`
- Raw: n=494  W=190/L=304  WR=38.5%
- Sharpen: sharpest is session_bucket=asia (88/304 of losers there)
- **Sharp: n=102  W=14/L=88  WR=13.7%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when session=asia

### L07.  `T4=T4c AND RSI=RSI6 AND direction_exec=short`
- Raw: n=494  W=190/L=304  WR=38.5%
- Sharpen: sharpest is session_bucket=asia (88/304 of losers there)
- **Sharp: n=102  W=14/L=88  WR=13.7%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when session=asia

### L08.  `H60=H60e AND T1=T1c AND T4=T4c AND RSI=RSI6`
- Raw: n=494  W=190/L=304  WR=38.5%
- Sharpen: sharpest is session_bucket=asia (88/304 of losers there)
- **Sharp: n=102  W=14/L=88  WR=13.7%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when session=asia

### L09.  `H60=H60e AND T4=T4c AND RSI=RSI6 AND direction_exec=short`
- Raw: n=494  W=190/L=304  WR=38.5%
- Sharpen: sharpest is session_bucket=asia (88/304 of losers there)
- **Sharp: n=102  W=14/L=88  WR=13.7%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when session=asia

### L10.  `T1=T1c AND T4=T4c AND RSI=RSI6 AND direction_exec=short`
- Raw: n=494  W=190/L=304  WR=38.5%
- Sharpen: sharpest is session_bucket=asia (88/304 of losers there)
- **Sharp: n=102  W=14/L=88  WR=13.7%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when session=asia

### L11.  `H60=H60e AND T1=T1c AND session_bucket=london_open`
- Raw: n=459  W=175/L=284  WR=38.1%
- Sharpen: sharpest is T4=T4c (156/284 of losers there)
- **Sharp: n=220  W=64/L=156  WR=29.1%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; session=london_open  •  ONLY when 4h trend AGAINST trade

### L12.  `T1=T1c AND direction_exec=short AND session_bucket=london_open`
- Raw: n=459  W=175/L=284  WR=38.1%
- Sharpen: sharpest is T4=T4c (156/284 of losers there)
- **Sharp: n=220  W=64/L=156  WR=29.1%**
- **Dir: SHORT**  •  1h trend AGAINST trade; session=london_open  •  ONLY when 4h trend AGAINST trade

### L13.  `H60=H60e AND T1=T1c AND direction_exec=short AND session_bucket=london_open`
- Raw: n=459  W=175/L=284  WR=38.1%
- Sharpen: sharpest is T4=T4c (156/284 of losers there)
- **Sharp: n=220  W=64/L=156  WR=29.1%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; session=london_open  •  ONLY when 4h trend AGAINST trade

### L14.  `H20=H20e AND H60=H60e AND RSI=RSI6`
- Raw: n=447  W=175/L=272  WR=39.1%
- Sharpen: sharpest is session_bucket=asia (88/272 of losers there)
- **Sharp: n=102  W=14/L=88  WR=13.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 70-80 overbought  •  ONLY when session=asia

### L15.  `H20=H20e AND T1=T1c AND RSI=RSI6`
- Raw: n=447  W=175/L=272  WR=39.1%
- Sharpen: sharpest is session_bucket=asia (88/272 of losers there)
- **Sharp: n=102  W=14/L=88  WR=13.7%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when session=asia

### L16.  `H20=H20e AND RSI=RSI6 AND direction_exec=short`
- Raw: n=447  W=175/L=272  WR=39.1%
- Sharpen: sharpest is session_bucket=asia (88/272 of losers there)
- **Sharp: n=102  W=14/L=88  WR=13.7%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 70-80 overbought  •  ONLY when session=asia

### L17.  `H20=H20e AND H60=H60e AND T1=T1c AND RSI=RSI6`
- Raw: n=447  W=175/L=272  WR=39.1%
- Sharpen: sharpest is session_bucket=asia (88/272 of losers there)
- **Sharp: n=102  W=14/L=88  WR=13.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when session=asia

### L18.  `H20=H20e AND H60=H60e AND RSI=RSI6 AND direction_exec=short`
- Raw: n=447  W=175/L=272  WR=39.1%
- Sharpen: sharpest is session_bucket=asia (88/272 of losers there)
- **Sharp: n=102  W=14/L=88  WR=13.7%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; RSI 70-80 overbought  •  ONLY when session=asia

### L19.  `H20=H20e AND T1=T1c AND RSI=RSI6 AND direction_exec=short`
- Raw: n=447  W=175/L=272  WR=39.1%
- Sharpen: sharpest is session_bucket=asia (88/272 of losers there)
- **Sharp: n=102  W=14/L=88  WR=13.7%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when session=asia

### L20.  `H20=H20e AND T4=T4c AND RSI=RSI6`
- Raw: n=393  W=155/L=238  WR=39.4%
- Sharpen: sharpest is session_bucket=asia (88/238 of losers there)
- **Sharp: n=102  W=14/L=88  WR=13.7%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when session=asia

### L21.  `H20=H20e AND H60=H60e AND T4=T4c AND RSI=RSI6`
- Raw: n=393  W=155/L=238  WR=39.4%
- Sharpen: sharpest is session_bucket=asia (88/238 of losers there)
- **Sharp: n=102  W=14/L=88  WR=13.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when session=asia

### L22.  `H20=H20e AND T1=T1c AND T4=T4c AND RSI=RSI6`
- Raw: n=393  W=155/L=238  WR=39.4%
- Sharpen: sharpest is session_bucket=asia (88/238 of losers there)
- **Sharp: n=102  W=14/L=88  WR=13.7%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when session=asia

### L23.  `H20=H20e AND T4=T4c AND RSI=RSI6 AND direction_exec=short`
- Raw: n=393  W=155/L=238  WR=39.4%
- Sharpen: sharpest is session_bucket=asia (88/238 of losers there)
- **Sharp: n=102  W=14/L=88  WR=13.7%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when session=asia

### L24.  `H20=H20e AND H60=H60e AND session_bucket=asia`
- Raw: n=344  W=121/L=223  WR=35.2%
- Sharpen: sharpest is RSI=RSI6 (88/223 of losers there)
- **Sharp: n=102  W=14/L=88  WR=13.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; session=asia  •  ONLY when RSI 70-80 overbought

### L25.  `H20=H20e AND direction_exec=short AND session_bucket=asia`
- Raw: n=344  W=121/L=223  WR=35.2%
- Sharpen: sharpest is RSI=RSI6 (88/223 of losers there)
- **Sharp: n=102  W=14/L=88  WR=13.7%**
- **Dir: SHORT**  •  HTF20 strongly against; session=asia  •  ONLY when RSI 70-80 overbought

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(47/35) | H20e(37/48) |
| H60 | H60a(64/35) | H60e(36/64) |
| T1 | T1a(62/36) | T1c(38/64) |
| T4 | T4a(56/45) | T4c(44/55) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(64/35) | short(36/65) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
