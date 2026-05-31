# AUD_CHF — R36 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **1,922**  (W=1,211 / L=711)  -  WR: **63.0%**

## Session distribution

- ny_mid: n=589  W=377/L=212  WR=64.0%
- london_open: n=425  W=261/L=164  WR=61.4%
- asia: n=413  W=259/L=154  WR=62.7%
- ny_open: n=157  W=89/L=68  WR=56.7%
- london: n=156  W=106/L=50  WR=67.9%
- ny_close: n=142  W=91/L=51  WR=64.1%
- asia_late: n=38  W=28/L=10  WR=73.7%
- off_hours: n=2  W=0/L=2  WR=0.0%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1a AND RSI=RSI6 AND direction_exec=long`
- Raw: n=139  W=126/L=13  WR=90.6%
- Refine: exclude BBP=BBP4 drops 11/13 losers (85%)
- **Final: n=62  W=60/L=2  WR=96.8%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 70-80 overbought  •  AVOID when upper third

### W02.  `T1=T1a AND T4=T4a AND RSI=RSI6`
- Raw: n=137  W=124/L=13  WR=90.5%
- Refine: exclude BBP=BBP4 drops 11/13 losers (85%)
- **Final: n=62  W=60/L=2  WR=96.8%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 70-80 overbought  •  AVOID when upper third

### W03.  `T4=T4a AND RSI=RSI6 AND direction_exec=long`
- Raw: n=137  W=124/L=13  WR=90.5%
- Refine: exclude BBP=BBP4 drops 11/13 losers (85%)
- **Final: n=62  W=60/L=2  WR=96.8%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 70-80 overbought  •  AVOID when upper third

### W04.  `T1=T1a AND T4=T4a AND RSI=RSI6 AND direction_exec=long`
- Raw: n=137  W=124/L=13  WR=90.5%
- Refine: exclude BBP=BBP4 drops 11/13 losers (85%)
- **Final: n=62  W=60/L=2  WR=96.8%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; RSI 70-80 overbought  •  AVOID when upper third

### W05.  `H60=H60a AND T1=T1a AND RSI=RSI6`
- Raw: n=122  W=112/L=10  WR=91.8%
- Refine: exclude ZS=ZS4 drops 10/10 losers (100%)
- **Final: n=62  W=62/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 70-80 overbought  •  AVOID when zscore +1 to +2 overbought

### W06.  `H60=H60a AND RSI=RSI6 AND direction_exec=long`
- Raw: n=122  W=112/L=10  WR=91.8%
- Refine: exclude ZS=ZS4 drops 10/10 losers (100%)
- **Final: n=62  W=62/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 70-80 overbought  •  AVOID when zscore +1 to +2 overbought

### W07.  `H60=H60a AND T1=T1a AND RSI=RSI6 AND direction_exec=long`
- Raw: n=122  W=112/L=10  WR=91.8%
- Refine: exclude ZS=ZS4 drops 10/10 losers (100%)
- **Final: n=62  W=62/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 70-80 overbought  •  AVOID when zscore +1 to +2 overbought

### W08.  `H60=H60a AND T4=T4a AND RSI=RSI6`
- Raw: n=120  W=110/L=10  WR=91.7%
- Refine: exclude ZS=ZS4 drops 10/10 losers (100%)
- **Final: n=62  W=62/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 70-80 overbought  •  AVOID when zscore +1 to +2 overbought

### W09.  `H60=H60a AND T1=T1a AND T4=T4a AND RSI=RSI6`
- Raw: n=120  W=110/L=10  WR=91.7%
- Refine: exclude ZS=ZS4 drops 10/10 losers (100%)
- **Final: n=62  W=62/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; RSI 70-80 overbought  •  AVOID when zscore +1 to +2 overbought

### W10.  `H60=H60a AND T4=T4a AND RSI=RSI6 AND direction_exec=long`
- Raw: n=120  W=110/L=10  WR=91.7%
- Refine: exclude ZS=ZS4 drops 10/10 losers (100%)
- **Final: n=62  W=62/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 70-80 overbought  •  AVOID when zscore +1 to +2 overbought

### W11.  `H20=H20b AND H60=H60a AND T1=T1a`
- Raw: n=101  W=88/L=13  WR=87.1%
- Refine: exclude session_bucket=ny_mid drops 10/13 losers (77%)
- **Final: n=67  W=64/L=3  WR=95.5%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 1h trend WITH trade  •  AVOID when session=ny_mid

### W12.  `H20=H20b AND H60=H60a AND T4=T4a`
- Raw: n=101  W=88/L=13  WR=87.1%
- Refine: exclude session_bucket=ny_mid drops 10/13 losers (77%)
- **Final: n=67  W=64/L=3  WR=95.5%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 4h trend WITH trade  •  AVOID when session=ny_mid

### W13.  `H20=H20b AND H60=H60a AND direction_exec=long`
- Raw: n=101  W=88/L=13  WR=87.1%
- Refine: exclude session_bucket=ny_mid drops 10/13 losers (77%)
- **Final: n=67  W=64/L=3  WR=95.5%**
- **Dir: LONG**  •  HTF20 slightly aligned; HTF60 aligned WITH trade  •  AVOID when session=ny_mid

### W14.  `H20=H20b AND H60=H60a AND T1=T1a AND T4=T4a`
- Raw: n=101  W=88/L=13  WR=87.1%
- Refine: exclude session_bucket=ny_mid drops 10/13 losers (77%)
- **Final: n=67  W=64/L=3  WR=95.5%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when session=ny_mid

### W15.  `H20=H20b AND H60=H60a AND T1=T1a AND direction_exec=long`
- Raw: n=101  W=88/L=13  WR=87.1%
- Refine: exclude session_bucket=ny_mid drops 10/13 losers (77%)
- **Final: n=67  W=64/L=3  WR=95.5%**
- **Dir: LONG**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 1h trend WITH trade  •  AVOID when session=ny_mid

### W16.  `H20=H20b AND H60=H60a AND T4=T4a AND direction_exec=long`
- Raw: n=101  W=88/L=13  WR=87.1%
- Refine: exclude session_bucket=ny_mid drops 10/13 losers (77%)
- **Final: n=67  W=64/L=3  WR=95.5%**
- **Dir: LONG**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 4h trend WITH trade  •  AVOID when session=ny_mid

### W17.  `H20=H20a AND H60=H60a AND T4=T4c`
- Raw: n=83  W=73/L=10  WR=88.0%
- Refine: exclude RSI=RSI4 drops 8/10 losers (80%)
- **Final: n=62  W=60/L=2  WR=96.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend AGAINST trade  •  AVOID when RSI 50-60 upper neutral

### W18.  `H20=H20a AND T1=T1a AND T4=T4c`
- Raw: n=83  W=73/L=10  WR=88.0%
- Refine: exclude RSI=RSI4 drops 8/10 losers (80%)
- **Final: n=62  W=60/L=2  WR=96.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade  •  AVOID when RSI 50-60 upper neutral

### W19.  `H20=H20a AND T4=T4c AND direction_exec=long`
- Raw: n=83  W=73/L=10  WR=88.0%
- Refine: exclude RSI=RSI4 drops 8/10 losers (80%)
- **Final: n=62  W=60/L=2  WR=96.8%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade  •  AVOID when RSI 50-60 upper neutral

### W20.  `H60=H60a AND T1=T1a AND T4=T4c`
- Raw: n=83  W=73/L=10  WR=88.0%
- Refine: exclude RSI=RSI4 drops 8/10 losers (80%)
- **Final: n=62  W=60/L=2  WR=96.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade  •  AVOID when RSI 50-60 upper neutral

### W21.  `H60=H60a AND T4=T4c AND direction_exec=long`
- Raw: n=83  W=73/L=10  WR=88.0%
- Refine: exclude RSI=RSI4 drops 8/10 losers (80%)
- **Final: n=62  W=60/L=2  WR=96.8%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade  •  AVOID when RSI 50-60 upper neutral

### W22.  `T1=T1a AND T4=T4c AND direction_exec=long`
- Raw: n=83  W=73/L=10  WR=88.0%
- Refine: exclude RSI=RSI4 drops 8/10 losers (80%)
- **Final: n=62  W=60/L=2  WR=96.8%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend AGAINST trade  •  AVOID when RSI 50-60 upper neutral

### W23.  `H20=H20a AND H60=H60a AND T1=T1a AND T4=T4c`
- Raw: n=83  W=73/L=10  WR=88.0%
- Refine: exclude RSI=RSI4 drops 8/10 losers (80%)
- **Final: n=62  W=60/L=2  WR=96.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade  •  AVOID when RSI 50-60 upper neutral

### W24.  `H20=H20a AND H60=H60a AND T4=T4c AND direction_exec=long`
- Raw: n=83  W=73/L=10  WR=88.0%
- Refine: exclude RSI=RSI4 drops 8/10 losers (80%)
- **Final: n=62  W=60/L=2  WR=96.8%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend AGAINST trade  •  AVOID when RSI 50-60 upper neutral

### W25.  `H20=H20a AND T1=T1a AND T4=T4c AND direction_exec=long`
- Raw: n=83  W=73/L=10  WR=88.0%
- Refine: exclude RSI=RSI4 drops 8/10 losers (80%)
- **Final: n=62  W=60/L=2  WR=96.8%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade  •  AVOID when RSI 50-60 upper neutral

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1c AND RSI=RSI6 AND direction_exec=short`
- Raw: n=98  W=31/L=67  WR=31.6%
- Sharpen: sharpest is H60=H60e (62/67 of losers there)
- **Sharp: n=81  W=19/L=62  WR=23.5%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when HTF60 strongly against

### L02.  `T1=T1c AND T4=T4c AND RSI=RSI6`
- Raw: n=95  W=31/L=64  WR=32.6%
- Sharpen: sharpest is H60=H60e (59/64 of losers there)
- **Sharp: n=78  W=19/L=59  WR=24.4%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when HTF60 strongly against

### L03.  `T4=T4c AND RSI=RSI6 AND direction_exec=short`
- Raw: n=95  W=31/L=64  WR=32.6%
- Sharpen: sharpest is H60=H60e (59/64 of losers there)
- **Sharp: n=78  W=19/L=59  WR=24.4%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when HTF60 strongly against

### L04.  `T1=T1c AND T4=T4c AND RSI=RSI6 AND direction_exec=short`
- Raw: n=95  W=31/L=64  WR=32.6%
- Sharpen: sharpest is H60=H60e (59/64 of losers there)
- **Sharp: n=78  W=19/L=59  WR=24.4%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when HTF60 strongly against

### L05.  `H20=H20d AND H60=H60e AND T1=T1c`
- Raw: n=86  W=28/L=58  WR=32.6%
- Sharpen: sharpest is RSI=RSI6 (40/58 of losers there)
- **Sharp: n=43  W=3/L=40  WR=7.0%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 strongly against; 1h trend AGAINST trade  •  ONLY when RSI 70-80 overbought

### L06.  `H20=H20d AND H60=H60e AND T4=T4c`
- Raw: n=86  W=28/L=58  WR=32.6%
- Sharpen: sharpest is RSI=RSI6 (40/58 of losers there)
- **Sharp: n=43  W=3/L=40  WR=7.0%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 strongly against; 4h trend AGAINST trade  •  ONLY when RSI 70-80 overbought

### L07.  `H20=H20d AND H60=H60e AND direction_exec=short`
- Raw: n=86  W=28/L=58  WR=32.6%
- Sharpen: sharpest is RSI=RSI6 (40/58 of losers there)
- **Sharp: n=43  W=3/L=40  WR=7.0%**
- **Dir: SHORT**  •  HTF20 mildly against; HTF60 strongly against  •  ONLY when RSI 70-80 overbought

### L08.  `H20=H20d AND H60=H60e AND T1=T1c AND T4=T4c`
- Raw: n=86  W=28/L=58  WR=32.6%
- Sharpen: sharpest is RSI=RSI6 (40/58 of losers there)
- **Sharp: n=43  W=3/L=40  WR=7.0%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when RSI 70-80 overbought

### L09.  `H20=H20d AND H60=H60e AND T1=T1c AND direction_exec=short`
- Raw: n=86  W=28/L=58  WR=32.6%
- Sharpen: sharpest is RSI=RSI6 (40/58 of losers there)
- **Sharp: n=43  W=3/L=40  WR=7.0%**
- **Dir: SHORT**  •  HTF20 mildly against; HTF60 strongly against; 1h trend AGAINST trade  •  ONLY when RSI 70-80 overbought

### L10.  `H20=H20d AND H60=H60e AND T4=T4c AND direction_exec=short`
- Raw: n=86  W=28/L=58  WR=32.6%
- Sharpen: sharpest is RSI=RSI6 (40/58 of losers there)
- **Sharp: n=43  W=3/L=40  WR=7.0%**
- **Dir: SHORT**  •  HTF20 mildly against; HTF60 strongly against; 4h trend AGAINST trade  •  ONLY when RSI 70-80 overbought

### L11.  `H60=H60e AND T1=T1c AND RSI=RSI6`
- Raw: n=81  W=19/L=62  WR=23.5%
- Sharpen: sharpest is H20=H20d (40/62 of losers there)
- **Sharp: n=43  W=3/L=40  WR=7.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when HTF20 mildly against

### L12.  `H60=H60e AND RSI=RSI6 AND direction_exec=short`
- Raw: n=81  W=19/L=62  WR=23.5%
- Sharpen: sharpest is H20=H20d (40/62 of losers there)
- **Sharp: n=43  W=3/L=40  WR=7.0%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 70-80 overbought  •  ONLY when HTF20 mildly against

### L13.  `H60=H60e AND T1=T1c AND RSI=RSI6 AND direction_exec=short`
- Raw: n=81  W=19/L=62  WR=23.5%
- Sharpen: sharpest is H20=H20d (40/62 of losers there)
- **Sharp: n=43  W=3/L=40  WR=7.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when HTF20 mildly against

### L14.  `H60=H60e AND T4=T4c AND RSI=RSI6`
- Raw: n=78  W=19/L=59  WR=24.4%
- Sharpen: sharpest is H20=H20d (40/59 of losers there)
- **Sharp: n=43  W=3/L=40  WR=7.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when HTF20 mildly against

### L15.  `H60=H60e AND T1=T1c AND T4=T4c AND RSI=RSI6`
- Raw: n=78  W=19/L=59  WR=24.4%
- Sharpen: sharpest is H20=H20d (40/59 of losers there)
- **Sharp: n=43  W=3/L=40  WR=7.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when HTF20 mildly against

### L16.  `H60=H60e AND T4=T4c AND RSI=RSI6 AND direction_exec=short`
- Raw: n=78  W=19/L=59  WR=24.4%
- Sharpen: sharpest is H20=H20d (40/59 of losers there)
- **Sharp: n=43  W=3/L=40  WR=7.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when HTF20 mildly against

### L17.  `H20=H20d AND H60=H60a AND T1=T1a`
- Raw: n=73  W=27/L=46  WR=37.0%
- Sharpen: sharpest is BBP=BBP4 (21/46 of losers there)
- **Sharp: n=24  W=3/L=21  WR=12.5%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 aligned WITH trade; 1h trend WITH trade  •  ONLY when upper third

### L18.  `H20=H20d AND H60=H60a AND T4=T4a`
- Raw: n=73  W=27/L=46  WR=37.0%
- Sharpen: sharpest is BBP=BBP4 (21/46 of losers there)
- **Sharp: n=24  W=3/L=21  WR=12.5%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 aligned WITH trade; 4h trend WITH trade  •  ONLY when upper third

### L19.  `H20=H20d AND H60=H60a AND direction_exec=long`
- Raw: n=73  W=27/L=46  WR=37.0%
- Sharpen: sharpest is BBP=BBP4 (21/46 of losers there)
- **Sharp: n=24  W=3/L=21  WR=12.5%**
- **Dir: LONG**  •  HTF20 mildly against; HTF60 aligned WITH trade  •  ONLY when upper third

### L20.  `H20=H20d AND T1=T1a AND T4=T4a`
- Raw: n=73  W=27/L=46  WR=37.0%
- Sharpen: sharpest is BBP=BBP4 (21/46 of losers there)
- **Sharp: n=24  W=3/L=21  WR=12.5%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when upper third

### L21.  `H20=H20d AND T1=T1a AND direction_exec=long`
- Raw: n=73  W=27/L=46  WR=37.0%
- Sharpen: sharpest is BBP=BBP4 (21/46 of losers there)
- **Sharp: n=24  W=3/L=21  WR=12.5%**
- **Dir: LONG**  •  HTF20 mildly against; 1h trend WITH trade  •  ONLY when upper third

### L22.  `H20=H20d AND T4=T4a AND direction_exec=long`
- Raw: n=73  W=27/L=46  WR=37.0%
- Sharpen: sharpest is BBP=BBP4 (21/46 of losers there)
- **Sharp: n=24  W=3/L=21  WR=12.5%**
- **Dir: LONG**  •  HTF20 mildly against; 4h trend WITH trade  •  ONLY when upper third

### L23.  `H20=H20d AND H60=H60a AND T1=T1a AND T4=T4a`
- Raw: n=73  W=27/L=46  WR=37.0%
- Sharpen: sharpest is BBP=BBP4 (21/46 of losers there)
- **Sharp: n=24  W=3/L=21  WR=12.5%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when upper third

### L24.  `H20=H20d AND H60=H60a AND T1=T1a AND direction_exec=long`
- Raw: n=73  W=27/L=46  WR=37.0%
- Sharpen: sharpest is BBP=BBP4 (21/46 of losers there)
- **Sharp: n=24  W=3/L=21  WR=12.5%**
- **Dir: LONG**  •  HTF20 mildly against; HTF60 aligned WITH trade; 1h trend WITH trade  •  ONLY when upper third

### L25.  `H20=H20d AND H60=H60a AND T4=T4a AND direction_exec=long`
- Raw: n=73  W=27/L=46  WR=37.0%
- Sharpen: sharpest is BBP=BBP4 (21/46 of losers there)
- **Sharp: n=24  W=3/L=21  WR=12.5%**
- **Dir: LONG**  •  HTF20 mildly against; HTF60 aligned WITH trade; 4h trend WITH trade  •  ONLY when upper third

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20b(13/4), H20a(44/37) | H20d(6/15), H20e(36/43) |
| H60 | H60a(50/45) | H60e(44/51) |
| T1 | T1a(54/46) | T1c(46/54) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(54/47) | short(46/53) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
