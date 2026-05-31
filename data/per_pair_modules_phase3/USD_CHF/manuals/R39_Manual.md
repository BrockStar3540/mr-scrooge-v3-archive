# USD_CHF — R39 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50e**  (EMA50 down >0.5x)
- **ADR = ADR5**  (>110% overshoot)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **1,335**  (W=844 / L=491)  -  WR: **63.2%**

## Session distribution

- ny_mid: n=307  W=200/L=107  WR=65.1%
- ny_open: n=261  W=157/L=104  WR=60.2%
- london_open: n=235  W=146/L=89  WR=62.1%
- ny_close: n=215  W=143/L=72  WR=66.5%
- london: n=201  W=129/L=72  WR=64.2%
- asia: n=91  W=54/L=37  WR=59.3%
- off_hours: n=13  W=8/L=5  WR=61.5%
- asia_late: n=12  W=7/L=5  WR=58.3%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1a AND T4=T4a AND session_bucket=ny_open`
- Raw: n=142  W=122/L=20  WR=85.9%
- Refine: exclude RSI=RSI1 drops 19/20 losers (95%)
- **Final: n=66  W=65/L=1  WR=98.5%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; session=ny_open  •  AVOID when RSI 20-30 oversold

### W02.  `T1=T1a AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=142  W=122/L=20  WR=85.9%
- Refine: exclude RSI=RSI1 drops 19/20 losers (95%)
- **Final: n=66  W=65/L=1  WR=98.5%**
- **Dir: SHORT**  •  1h trend WITH trade; session=ny_open  •  AVOID when RSI 20-30 oversold

### W03.  `T4=T4a AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=142  W=122/L=20  WR=85.9%
- Refine: exclude RSI=RSI1 drops 19/20 losers (95%)
- **Final: n=66  W=65/L=1  WR=98.5%**
- **Dir: SHORT**  •  4h trend WITH trade; session=ny_open  •  AVOID when RSI 20-30 oversold

### W04.  `T1=T1a AND T4=T4a AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=142  W=122/L=20  WR=85.9%
- Refine: exclude RSI=RSI1 drops 19/20 losers (95%)
- **Final: n=66  W=65/L=1  WR=98.5%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend WITH trade; session=ny_open  •  AVOID when RSI 20-30 oversold

### W05.  `H20=H20b AND H60=H60a AND T1=T1a`
- Raw: n=127  W=108/L=19  WR=85.0%
- Refine: exclude session_bucket=ny_mid drops 11/19 losers (58%)
- **Final: n=107  W=99/L=8  WR=92.5%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 1h trend WITH trade  •  AVOID when session=ny_mid

### W06.  `H20=H20b AND H60=H60a AND T4=T4a`
- Raw: n=127  W=108/L=19  WR=85.0%
- Refine: exclude session_bucket=ny_mid drops 11/19 losers (58%)
- **Final: n=107  W=99/L=8  WR=92.5%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 4h trend WITH trade  •  AVOID when session=ny_mid

### W07.  `H20=H20b AND H60=H60a AND direction_exec=short`
- Raw: n=127  W=108/L=19  WR=85.0%
- Refine: exclude session_bucket=ny_mid drops 11/19 losers (58%)
- **Final: n=107  W=99/L=8  WR=92.5%**
- **Dir: SHORT**  •  HTF20 slightly aligned; HTF60 aligned WITH trade  •  AVOID when session=ny_mid

### W08.  `H20=H20b AND T1=T1a AND T4=T4a`
- Raw: n=127  W=108/L=19  WR=85.0%
- Refine: exclude session_bucket=ny_mid drops 11/19 losers (58%)
- **Final: n=107  W=99/L=8  WR=92.5%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when session=ny_mid

### W09.  `H20=H20b AND T1=T1a AND direction_exec=short`
- Raw: n=127  W=108/L=19  WR=85.0%
- Refine: exclude session_bucket=ny_mid drops 11/19 losers (58%)
- **Final: n=107  W=99/L=8  WR=92.5%**
- **Dir: SHORT**  •  HTF20 slightly aligned; 1h trend WITH trade  •  AVOID when session=ny_mid

### W10.  `H20=H20b AND T4=T4a AND direction_exec=short`
- Raw: n=127  W=108/L=19  WR=85.0%
- Refine: exclude session_bucket=ny_mid drops 11/19 losers (58%)
- **Final: n=107  W=99/L=8  WR=92.5%**
- **Dir: SHORT**  •  HTF20 slightly aligned; 4h trend WITH trade  •  AVOID when session=ny_mid

### W11.  `H20=H20b AND H60=H60a AND T1=T1a AND T4=T4a`
- Raw: n=127  W=108/L=19  WR=85.0%
- Refine: exclude session_bucket=ny_mid drops 11/19 losers (58%)
- **Final: n=107  W=99/L=8  WR=92.5%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when session=ny_mid

### W12.  `H20=H20b AND H60=H60a AND T1=T1a AND direction_exec=short`
- Raw: n=127  W=108/L=19  WR=85.0%
- Refine: exclude session_bucket=ny_mid drops 11/19 losers (58%)
- **Final: n=107  W=99/L=8  WR=92.5%**
- **Dir: SHORT**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 1h trend WITH trade  •  AVOID when session=ny_mid

### W13.  `H20=H20b AND H60=H60a AND T4=T4a AND direction_exec=short`
- Raw: n=127  W=108/L=19  WR=85.0%
- Refine: exclude session_bucket=ny_mid drops 11/19 losers (58%)
- **Final: n=107  W=99/L=8  WR=92.5%**
- **Dir: SHORT**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 4h trend WITH trade  •  AVOID when session=ny_mid

### W14.  `H20=H20b AND T1=T1a AND T4=T4a AND direction_exec=short`
- Raw: n=127  W=108/L=19  WR=85.0%
- Refine: exclude session_bucket=ny_mid drops 11/19 losers (58%)
- **Final: n=107  W=99/L=8  WR=92.5%**
- **Dir: SHORT**  •  HTF20 slightly aligned; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when session=ny_mid

### W15.  `T4=T4a AND direction_exec=short AND session_bucket=london`
- Raw: n=124  W=114/L=10  WR=91.9%
- Refine: exclude H60=H60a drops 10/10 losers (100%)
- **Final: n=46  W=46/L=0  WR=100.0%**
- **Dir: SHORT**  •  4h trend WITH trade; session=london  •  AVOID when HTF60 aligned WITH trade

### W16.  `H20=H20b AND H60=H60a AND RSI=RSI1`
- Raw: n=117  W=100/L=17  WR=85.5%
- Refine: exclude session_bucket=ny_mid drops 9/17 losers (53%)
- **Final: n=107  W=99/L=8  WR=92.5%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; RSI 20-30 oversold  •  AVOID when session=ny_mid

### W17.  `H20=H20b AND T1=T1a AND RSI=RSI1`
- Raw: n=117  W=100/L=17  WR=85.5%
- Refine: exclude session_bucket=ny_mid drops 9/17 losers (53%)
- **Final: n=107  W=99/L=8  WR=92.5%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend WITH trade; RSI 20-30 oversold  •  AVOID when session=ny_mid

### W18.  `H20=H20b AND T4=T4a AND RSI=RSI1`
- Raw: n=117  W=100/L=17  WR=85.5%
- Refine: exclude session_bucket=ny_mid drops 9/17 losers (53%)
- **Final: n=107  W=99/L=8  WR=92.5%**
- **Dir: ?**  •  HTF20 slightly aligned; 4h trend WITH trade; RSI 20-30 oversold  •  AVOID when session=ny_mid

### W19.  `H20=H20b AND RSI=RSI1 AND direction_exec=short`
- Raw: n=117  W=100/L=17  WR=85.5%
- Refine: exclude session_bucket=ny_mid drops 9/17 losers (53%)
- **Final: n=107  W=99/L=8  WR=92.5%**
- **Dir: SHORT**  •  HTF20 slightly aligned; RSI 20-30 oversold  •  AVOID when session=ny_mid

### W20.  `H20=H20b AND H60=H60a AND T1=T1a AND RSI=RSI1`
- Raw: n=117  W=100/L=17  WR=85.5%
- Refine: exclude session_bucket=ny_mid drops 9/17 losers (53%)
- **Final: n=107  W=99/L=8  WR=92.5%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 1h trend WITH trade; RSI 20-30 oversold  •  AVOID when session=ny_mid

### W21.  `H20=H20b AND H60=H60a AND T4=T4a AND RSI=RSI1`
- Raw: n=117  W=100/L=17  WR=85.5%
- Refine: exclude session_bucket=ny_mid drops 9/17 losers (53%)
- **Final: n=107  W=99/L=8  WR=92.5%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 4h trend WITH trade; RSI 20-30 oversold  •  AVOID when session=ny_mid

### W22.  `H20=H20b AND H60=H60a AND RSI=RSI1 AND direction_exec=short`
- Raw: n=117  W=100/L=17  WR=85.5%
- Refine: exclude session_bucket=ny_mid drops 9/17 losers (53%)
- **Final: n=107  W=99/L=8  WR=92.5%**
- **Dir: SHORT**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; RSI 20-30 oversold  •  AVOID when session=ny_mid

### W23.  `H20=H20b AND T1=T1a AND T4=T4a AND RSI=RSI1`
- Raw: n=117  W=100/L=17  WR=85.5%
- Refine: exclude session_bucket=ny_mid drops 9/17 losers (53%)
- **Final: n=107  W=99/L=8  WR=92.5%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend WITH trade; 4h trend WITH trade; RSI 20-30 oversold  •  AVOID when session=ny_mid

### W24.  `H20=H20b AND T1=T1a AND RSI=RSI1 AND direction_exec=short`
- Raw: n=117  W=100/L=17  WR=85.5%
- Refine: exclude session_bucket=ny_mid drops 9/17 losers (53%)
- **Final: n=107  W=99/L=8  WR=92.5%**
- **Dir: SHORT**  •  HTF20 slightly aligned; 1h trend WITH trade; RSI 20-30 oversold  •  AVOID when session=ny_mid

### W25.  `H20=H20b AND T4=T4a AND RSI=RSI1 AND direction_exec=short`
- Raw: n=117  W=100/L=17  WR=85.5%
- Refine: exclude session_bucket=ny_mid drops 9/17 losers (53%)
- **Final: n=107  W=99/L=8  WR=92.5%**
- **Dir: SHORT**  •  HTF20 slightly aligned; 4h trend WITH trade; RSI 20-30 oversold  •  AVOID when session=ny_mid

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1c AND T4=T4c AND RSI=RSI0`
- Raw: n=166  W=62/L=104  WR=37.3%
- Sharpen: sharpest is session_bucket=ny_open (36/104 of losers there)
- **Sharp: n=38  W=2/L=36  WR=5.3%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI<20 extreme oversold  •  ONLY when session=ny_open

### L02.  `T1=T1c AND RSI=RSI0 AND direction_exec=long`
- Raw: n=166  W=62/L=104  WR=37.3%
- Sharpen: sharpest is session_bucket=ny_open (36/104 of losers there)
- **Sharp: n=38  W=2/L=36  WR=5.3%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI<20 extreme oversold  •  ONLY when session=ny_open

### L03.  `T4=T4c AND RSI=RSI0 AND direction_exec=long`
- Raw: n=166  W=62/L=104  WR=37.3%
- Sharpen: sharpest is session_bucket=ny_open (36/104 of losers there)
- **Sharp: n=38  W=2/L=36  WR=5.3%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI<20 extreme oversold  •  ONLY when session=ny_open

### L04.  `T1=T1c AND T4=T4c AND RSI=RSI0 AND direction_exec=long`
- Raw: n=166  W=62/L=104  WR=37.3%
- Sharpen: sharpest is session_bucket=ny_open (36/104 of losers there)
- **Sharp: n=38  W=2/L=36  WR=5.3%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI<20 extreme oversold  •  ONLY when session=ny_open

### L05.  `T1=T1c AND BBP=BBP2 AND RSI=RSI0`
- Raw: n=134  W=53/L=81  WR=39.6%
- Sharpen: sharpest is session_bucket=ny_open (28/81 of losers there)
- **Sharp: n=30  W=2/L=28  WR=6.7%**
- **Dir: ?**  •  1h trend AGAINST trade; lower third; RSI<20 extreme oversold  •  ONLY when session=ny_open

### L06.  `T4=T4c AND BBP=BBP2 AND RSI=RSI0`
- Raw: n=134  W=53/L=81  WR=39.6%
- Sharpen: sharpest is session_bucket=ny_open (28/81 of losers there)
- **Sharp: n=30  W=2/L=28  WR=6.7%**
- **Dir: ?**  •  4h trend AGAINST trade; lower third; RSI<20 extreme oversold  •  ONLY when session=ny_open

### L07.  `BBP=BBP2 AND RSI=RSI0 AND direction_exec=long`
- Raw: n=134  W=53/L=81  WR=39.6%
- Sharpen: sharpest is session_bucket=ny_open (28/81 of losers there)
- **Sharp: n=30  W=2/L=28  WR=6.7%**
- **Dir: LONG**  •  lower third; RSI<20 extreme oversold  •  ONLY when session=ny_open

### L08.  `T1=T1c AND T4=T4c AND BBP=BBP2 AND RSI=RSI0`
- Raw: n=134  W=53/L=81  WR=39.6%
- Sharpen: sharpest is session_bucket=ny_open (28/81 of losers there)
- **Sharp: n=30  W=2/L=28  WR=6.7%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; lower third; RSI<20 extreme oversold  •  ONLY when session=ny_open

### L09.  `T1=T1c AND BBP=BBP2 AND RSI=RSI0 AND direction_exec=long`
- Raw: n=134  W=53/L=81  WR=39.6%
- Sharpen: sharpest is session_bucket=ny_open (28/81 of losers there)
- **Sharp: n=30  W=2/L=28  WR=6.7%**
- **Dir: LONG**  •  1h trend AGAINST trade; lower third; RSI<20 extreme oversold  •  ONLY when session=ny_open

### L10.  `T4=T4c AND BBP=BBP2 AND RSI=RSI0 AND direction_exec=long`
- Raw: n=134  W=53/L=81  WR=39.6%
- Sharpen: sharpest is session_bucket=ny_open (28/81 of losers there)
- **Sharp: n=30  W=2/L=28  WR=6.7%**
- **Dir: LONG**  •  4h trend AGAINST trade; lower third; RSI<20 extreme oversold  •  ONLY when session=ny_open

### L11.  `T1=T1c AND RSI=RSI0 AND ZS=ZS2`
- Raw: n=133  W=53/L=80  WR=39.8%
- Sharpen: sharpest is session_bucket=ny_open (28/80 of losers there)
- **Sharp: n=30  W=2/L=28  WR=6.7%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI<20 extreme oversold; zscore -2 to -1 oversold  •  ONLY when session=ny_open

### L12.  `T4=T4c AND RSI=RSI0 AND ZS=ZS2`
- Raw: n=133  W=53/L=80  WR=39.8%
- Sharpen: sharpest is session_bucket=ny_open (28/80 of losers there)
- **Sharp: n=30  W=2/L=28  WR=6.7%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI<20 extreme oversold; zscore -2 to -1 oversold  •  ONLY when session=ny_open

### L13.  `RSI=RSI0 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=133  W=53/L=80  WR=39.8%
- Sharpen: sharpest is session_bucket=ny_open (28/80 of losers there)
- **Sharp: n=30  W=2/L=28  WR=6.7%**
- **Dir: LONG**  •  RSI<20 extreme oversold; zscore -2 to -1 oversold  •  ONLY when session=ny_open

### L14.  `T1=T1c AND T4=T4c AND RSI=RSI0 AND ZS=ZS2`
- Raw: n=133  W=53/L=80  WR=39.8%
- Sharpen: sharpest is session_bucket=ny_open (28/80 of losers there)
- **Sharp: n=30  W=2/L=28  WR=6.7%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI<20 extreme oversold; zscore -2 to -1 oversold  •  ONLY when session=ny_open

### L15.  `T1=T1c AND BBP=BBP2 AND RSI=RSI0 AND ZS=ZS2`
- Raw: n=133  W=53/L=80  WR=39.8%
- Sharpen: sharpest is session_bucket=ny_open (28/80 of losers there)
- **Sharp: n=30  W=2/L=28  WR=6.7%**
- **Dir: ?**  •  1h trend AGAINST trade; lower third; RSI<20 extreme oversold; zscore -2 to -1 oversold  •  ONLY when session=ny_open

### L16.  `T1=T1c AND RSI=RSI0 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=133  W=53/L=80  WR=39.8%
- Sharpen: sharpest is session_bucket=ny_open (28/80 of losers there)
- **Sharp: n=30  W=2/L=28  WR=6.7%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI<20 extreme oversold; zscore -2 to -1 oversold  •  ONLY when session=ny_open

### L17.  `T4=T4c AND BBP=BBP2 AND RSI=RSI0 AND ZS=ZS2`
- Raw: n=133  W=53/L=80  WR=39.8%
- Sharpen: sharpest is session_bucket=ny_open (28/80 of losers there)
- **Sharp: n=30  W=2/L=28  WR=6.7%**
- **Dir: ?**  •  4h trend AGAINST trade; lower third; RSI<20 extreme oversold; zscore -2 to -1 oversold  •  ONLY when session=ny_open

### L18.  `T4=T4c AND RSI=RSI0 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=133  W=53/L=80  WR=39.8%
- Sharpen: sharpest is session_bucket=ny_open (28/80 of losers there)
- **Sharp: n=30  W=2/L=28  WR=6.7%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI<20 extreme oversold; zscore -2 to -1 oversold  •  ONLY when session=ny_open

### L19.  `BBP=BBP2 AND RSI=RSI0 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=133  W=53/L=80  WR=39.8%
- Sharpen: sharpest is session_bucket=ny_open (28/80 of losers there)
- **Sharp: n=30  W=2/L=28  WR=6.7%**
- **Dir: LONG**  •  lower third; RSI<20 extreme oversold; zscore -2 to -1 oversold  •  ONLY when session=ny_open

### L20.  `T1=T1c AND T4=T4c AND session_bucket=ny_open`
- Raw: n=119  W=35/L=84  WR=29.4%
- Sharpen: sharpest is RSI=RSI0 (36/84 of losers there)
- **Sharp: n=38  W=2/L=36  WR=5.3%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_open  •  ONLY when RSI<20 extreme oversold

### L21.  `T1=T1c AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=119  W=35/L=84  WR=29.4%
- Sharpen: sharpest is RSI=RSI0 (36/84 of losers there)
- **Sharp: n=38  W=2/L=36  WR=5.3%**
- **Dir: LONG**  •  1h trend AGAINST trade; session=ny_open  •  ONLY when RSI<20 extreme oversold

### L22.  `T4=T4c AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=119  W=35/L=84  WR=29.4%
- Sharpen: sharpest is RSI=RSI0 (36/84 of losers there)
- **Sharp: n=38  W=2/L=36  WR=5.3%**
- **Dir: LONG**  •  4h trend AGAINST trade; session=ny_open  •  ONLY when RSI<20 extreme oversold

### L23.  `T1=T1c AND T4=T4c AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=119  W=35/L=84  WR=29.4%
- Sharpen: sharpest is RSI=RSI0 (36/84 of losers there)
- **Sharp: n=38  W=2/L=36  WR=5.3%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_open  •  ONLY when RSI<20 extreme oversold

### L24.  `H60=H60b AND T1=T1c AND direction_exec=long`
- Raw: n=119  W=47/L=72  WR=39.5%
- Sharpen: sharpest is T4=T4a (16/72 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: LONG**  •  HTF60 slightly aligned; 1h trend AGAINST trade  •  ONLY when 4h trend WITH trade

### L25.  `H20=H20e AND T1=T1c AND session_bucket=ny_open`
- Raw: n=103  W=33/L=70  WR=32.0%
- Sharpen: sharpest is RSI=RSI0 (25/70 of losers there)
- **Sharp: n=27  W=2/L=25  WR=7.4%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; session=ny_open  •  ONLY when RSI<20 extreme oversold

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(39/28) | H20e(30/41) |
| H60 | H60a(48/25) | H60e(29/50) |
| T1 | T1a(63/34) | T1c(37/66) |
| T4 | T4a(62/36) | T4c(38/64) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(65/33) | long(35/67) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
