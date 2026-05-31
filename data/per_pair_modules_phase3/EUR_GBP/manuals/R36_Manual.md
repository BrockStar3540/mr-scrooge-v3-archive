# EUR_GBP — R36 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR5**  (>110% overshoot)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **1,027**  (W=639 / L=388)  -  WR: **62.2%**

## Session distribution

- ny_mid: n=381  W=239/L=142  WR=62.7%
- london_open: n=269  W=167/L=102  WR=62.1%
- ny_close: n=192  W=119/L=73  WR=62.0%
- ny_open: n=136  W=82/L=54  WR=60.3%
- london: n=48  W=32/L=16  WR=66.7%
- asia: n=1  W=0/L=1  WR=0.0%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1a AND T4=T4a AND session_bucket=ny_close`
- Raw: n=101  W=87/L=14  WR=86.1%
- Refine: exclude ZS=ZS3 drops 8/14 losers (57%)
- **Final: n=82  W=76/L=6  WR=92.7%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; session=ny_close  •  AVOID when zscore -1 to +1 neutral

### W02.  `T1=T1a AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=101  W=87/L=14  WR=86.1%
- Refine: exclude ZS=ZS3 drops 8/14 losers (57%)
- **Final: n=82  W=76/L=6  WR=92.7%**
- **Dir: LONG**  •  1h trend WITH trade; session=ny_close  •  AVOID when zscore -1 to +1 neutral

### W03.  `T4=T4a AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=101  W=87/L=14  WR=86.1%
- Refine: exclude ZS=ZS3 drops 8/14 losers (57%)
- **Final: n=82  W=76/L=6  WR=92.7%**
- **Dir: LONG**  •  4h trend WITH trade; session=ny_close  •  AVOID when zscore -1 to +1 neutral

### W04.  `T1=T1a AND T4=T4a AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=101  W=87/L=14  WR=86.1%
- Refine: exclude ZS=ZS3 drops 8/14 losers (57%)
- **Final: n=82  W=76/L=6  WR=92.7%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; session=ny_close  •  AVOID when zscore -1 to +1 neutral

### W05.  `T1=T1a AND RSI=RSI6 AND session_bucket=ny_close`
- Raw: n=76  W=69/L=7  WR=90.8%
- Refine: exclude H60=H60e drops 7/7 losers (100%)
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; RSI 70-80 overbought; session=ny_close  •  AVOID when HTF60 strongly against

### W06.  `T4=T4a AND RSI=RSI6 AND session_bucket=ny_close`
- Raw: n=76  W=69/L=7  WR=90.8%
- Refine: exclude H60=H60e drops 7/7 losers (100%)
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend WITH trade; RSI 70-80 overbought; session=ny_close  •  AVOID when HTF60 strongly against

### W07.  `RSI=RSI6 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=76  W=69/L=7  WR=90.8%
- Refine: exclude H60=H60e drops 7/7 losers (100%)
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: LONG**  •  RSI 70-80 overbought; session=ny_close  •  AVOID when HTF60 strongly against

### W08.  `T1=T1a AND T4=T4a AND RSI=RSI6 AND session_bucket=ny_close`
- Raw: n=76  W=69/L=7  WR=90.8%
- Refine: exclude H60=H60e drops 7/7 losers (100%)
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 70-80 overbought; session=ny_close  •  AVOID when HTF60 strongly against

### W09.  `T1=T1a AND RSI=RSI6 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=76  W=69/L=7  WR=90.8%
- Refine: exclude H60=H60e drops 7/7 losers (100%)
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 70-80 overbought; session=ny_close  •  AVOID when HTF60 strongly against

### W10.  `T4=T4a AND RSI=RSI6 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=76  W=69/L=7  WR=90.8%
- Refine: exclude H60=H60e drops 7/7 losers (100%)
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 70-80 overbought; session=ny_close  •  AVOID when HTF60 strongly against

### W11.  `H20=H20d AND BBP=BBP4 AND RSI=RSI6 AND session_bucket=london_open`
- Raw: n=75  W=64/L=11  WR=85.3%
- Refine: exclude H60=H60a drops 5/11 losers (45%)
- **Final: n=52  W=46/L=6  WR=88.5%**
- **Dir: ?**  •  HTF20 mildly against; upper third; RSI 70-80 overbought; session=london_open  •  AVOID when HTF60 aligned WITH trade

### W12.  `H20=H20d AND H60=H60c AND T1=T1a`
- Raw: n=74  W=64/L=10  WR=86.5%
- Refine: exclude session_bucket=ny_open drops 10/10 losers (100%)
- **Final: n=62  W=62/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 neutral; 1h trend WITH trade  •  AVOID when session=ny_open

### W13.  `H20=H20d AND H60=H60c AND T4=T4a`
- Raw: n=74  W=64/L=10  WR=86.5%
- Refine: exclude session_bucket=ny_open drops 10/10 losers (100%)
- **Final: n=62  W=62/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 neutral; 4h trend WITH trade  •  AVOID when session=ny_open

### W14.  `H20=H20d AND H60=H60c AND direction_exec=long`
- Raw: n=74  W=64/L=10  WR=86.5%
- Refine: exclude session_bucket=ny_open drops 10/10 losers (100%)
- **Final: n=62  W=62/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 mildly against; HTF60 neutral  •  AVOID when session=ny_open

### W15.  `H60=H60c AND T1=T1a AND T4=T4a`
- Raw: n=74  W=64/L=10  WR=86.5%
- Refine: exclude session_bucket=ny_open drops 10/10 losers (100%)
- **Final: n=62  W=62/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 neutral; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when session=ny_open

### W16.  `H60=H60c AND T1=T1a AND direction_exec=long`
- Raw: n=74  W=64/L=10  WR=86.5%
- Refine: exclude session_bucket=ny_open drops 10/10 losers (100%)
- **Final: n=62  W=62/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 neutral; 1h trend WITH trade  •  AVOID when session=ny_open

### W17.  `H60=H60c AND T4=T4a AND direction_exec=long`
- Raw: n=74  W=64/L=10  WR=86.5%
- Refine: exclude session_bucket=ny_open drops 10/10 losers (100%)
- **Final: n=62  W=62/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 neutral; 4h trend WITH trade  •  AVOID when session=ny_open

### W18.  `H20=H20d AND H60=H60c AND T1=T1a AND T4=T4a`
- Raw: n=74  W=64/L=10  WR=86.5%
- Refine: exclude session_bucket=ny_open drops 10/10 losers (100%)
- **Final: n=62  W=62/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 neutral; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when session=ny_open

### W19.  `H20=H20d AND H60=H60c AND T1=T1a AND direction_exec=long`
- Raw: n=74  W=64/L=10  WR=86.5%
- Refine: exclude session_bucket=ny_open drops 10/10 losers (100%)
- **Final: n=62  W=62/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 mildly against; HTF60 neutral; 1h trend WITH trade  •  AVOID when session=ny_open

### W20.  `H20=H20d AND H60=H60c AND T4=T4a AND direction_exec=long`
- Raw: n=74  W=64/L=10  WR=86.5%
- Refine: exclude session_bucket=ny_open drops 10/10 losers (100%)
- **Final: n=62  W=62/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 mildly against; HTF60 neutral; 4h trend WITH trade  •  AVOID when session=ny_open

### W21.  `H60=H60c AND T1=T1a AND T4=T4a AND direction_exec=long`
- Raw: n=74  W=64/L=10  WR=86.5%
- Refine: exclude session_bucket=ny_open drops 10/10 losers (100%)
- **Final: n=62  W=62/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 neutral; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when session=ny_open

### W22.  `H20=H20d AND H60=H60c AND BBP=BBP4`
- Raw: n=64  W=56/L=8  WR=87.5%
- Refine: exclude session_bucket=ny_open drops 8/8 losers (100%)
- **Final: n=54  W=54/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 neutral; upper third  •  AVOID when session=ny_open

### W23.  `H60=H60c AND T1=T1a AND BBP=BBP4`
- Raw: n=64  W=56/L=8  WR=87.5%
- Refine: exclude session_bucket=ny_open drops 8/8 losers (100%)
- **Final: n=54  W=54/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 neutral; 1h trend WITH trade; upper third  •  AVOID when session=ny_open

### W24.  `H60=H60c AND T4=T4a AND BBP=BBP4`
- Raw: n=64  W=56/L=8  WR=87.5%
- Refine: exclude session_bucket=ny_open drops 8/8 losers (100%)
- **Final: n=54  W=54/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 neutral; 4h trend WITH trade; upper third  •  AVOID when session=ny_open

### W25.  `H60=H60c AND BBP=BBP4 AND direction_exec=long`
- Raw: n=64  W=56/L=8  WR=87.5%
- Refine: exclude session_bucket=ny_open drops 8/8 losers (100%)
- **Final: n=54  W=54/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 neutral; upper third  •  AVOID when session=ny_open

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1c AND T4=T4c AND session_bucket=ny_close`
- Raw: n=91  W=32/L=59  WR=35.2%
- Sharpen: sharpest is H20=H20c (24/59 of losers there)
- **Sharp: n=30  W=6/L=24  WR=20.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_close  •  ONLY when HTF20 neutral

### L02.  `T1=T1c AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=91  W=32/L=59  WR=35.2%
- Sharpen: sharpest is H20=H20c (24/59 of losers there)
- **Sharp: n=30  W=6/L=24  WR=20.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; session=ny_close  •  ONLY when HTF20 neutral

### L03.  `T4=T4c AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=91  W=32/L=59  WR=35.2%
- Sharpen: sharpest is H20=H20c (24/59 of losers there)
- **Sharp: n=30  W=6/L=24  WR=20.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; session=ny_close  •  ONLY when HTF20 neutral

### L04.  `T1=T1c AND T4=T4c AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=91  W=32/L=59  WR=35.2%
- Sharpen: sharpest is H20=H20c (24/59 of losers there)
- **Sharp: n=30  W=6/L=24  WR=20.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_close  •  ONLY when HTF20 neutral

### L05.  `H20=H20b AND RSI=RSI6 AND session_bucket=london_open`
- Raw: n=78  W=28/L=50  WR=35.9%
- Sharpen: sharpest is H60=H60c (14/50 of losers there)
- **Sharp: n=16  W=2/L=14  WR=12.5%**
- **Dir: ?**  •  HTF20 slightly aligned; RSI 70-80 overbought; session=london_open  •  ONLY when HTF60 neutral

### L06.  `T1=T1c AND RSI=RSI6 AND session_bucket=ny_close`
- Raw: n=70  W=24/L=46  WR=34.3%
- Sharpen: sharpest is H20=H20c (24/46 of losers there)
- **Sharp: n=30  W=6/L=24  WR=20.0%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 70-80 overbought; session=ny_close  •  ONLY when HTF20 neutral

### L07.  `T4=T4c AND RSI=RSI6 AND session_bucket=ny_close`
- Raw: n=70  W=24/L=46  WR=34.3%
- Sharpen: sharpest is H20=H20c (24/46 of losers there)
- **Sharp: n=30  W=6/L=24  WR=20.0%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 70-80 overbought; session=ny_close  •  ONLY when HTF20 neutral

### L08.  `RSI=RSI6 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=70  W=24/L=46  WR=34.3%
- Sharpen: sharpest is H20=H20c (24/46 of losers there)
- **Sharp: n=30  W=6/L=24  WR=20.0%**
- **Dir: SHORT**  •  RSI 70-80 overbought; session=ny_close  •  ONLY when HTF20 neutral

### L09.  `T1=T1c AND T4=T4c AND RSI=RSI6 AND session_bucket=ny_close`
- Raw: n=70  W=24/L=46  WR=34.3%
- Sharpen: sharpest is H20=H20c (24/46 of losers there)
- **Sharp: n=30  W=6/L=24  WR=20.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 70-80 overbought; session=ny_close  •  ONLY when HTF20 neutral

### L10.  `T1=T1c AND RSI=RSI6 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=70  W=24/L=46  WR=34.3%
- Sharpen: sharpest is H20=H20c (24/46 of losers there)
- **Sharp: n=30  W=6/L=24  WR=20.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 70-80 overbought; session=ny_close  •  ONLY when HTF20 neutral

### L11.  `T4=T4c AND RSI=RSI6 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=70  W=24/L=46  WR=34.3%
- Sharpen: sharpest is H20=H20c (24/46 of losers there)
- **Sharp: n=30  W=6/L=24  WR=20.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 70-80 overbought; session=ny_close  •  ONLY when HTF20 neutral

### L12.  `H20=H20b AND H60=H60c AND T1=T1c`
- Raw: n=64  W=22/L=42  WR=34.4%
- Sharpen: sharpest is RSI=RSI5 (11/42 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 neutral; 1h trend AGAINST trade  •  ONLY when RSI 60-70 strong

### L13.  `H20=H20b AND H60=H60c AND T4=T4c`
- Raw: n=64  W=22/L=42  WR=34.4%
- Sharpen: sharpest is RSI=RSI5 (11/42 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 neutral; 4h trend AGAINST trade  •  ONLY when RSI 60-70 strong

### L14.  `H20=H20b AND H60=H60c AND direction_exec=short`
- Raw: n=64  W=22/L=42  WR=34.4%
- Sharpen: sharpest is RSI=RSI5 (11/42 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: SHORT**  •  HTF20 slightly aligned; HTF60 neutral  •  ONLY when RSI 60-70 strong

### L15.  `H60=H60c AND T1=T1c AND T4=T4c`
- Raw: n=64  W=22/L=42  WR=34.4%
- Sharpen: sharpest is RSI=RSI5 (11/42 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: ?**  •  HTF60 neutral; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when RSI 60-70 strong

### L16.  `H60=H60c AND T1=T1c AND direction_exec=short`
- Raw: n=64  W=22/L=42  WR=34.4%
- Sharpen: sharpest is RSI=RSI5 (11/42 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: SHORT**  •  HTF60 neutral; 1h trend AGAINST trade  •  ONLY when RSI 60-70 strong

### L17.  `H60=H60c AND T4=T4c AND direction_exec=short`
- Raw: n=64  W=22/L=42  WR=34.4%
- Sharpen: sharpest is RSI=RSI5 (11/42 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: SHORT**  •  HTF60 neutral; 4h trend AGAINST trade  •  ONLY when RSI 60-70 strong

### L18.  `H20=H20b AND H60=H60c AND T1=T1c AND T4=T4c`
- Raw: n=64  W=22/L=42  WR=34.4%
- Sharpen: sharpest is RSI=RSI5 (11/42 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 neutral; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when RSI 60-70 strong

### L19.  `H20=H20b AND H60=H60c AND T1=T1c AND direction_exec=short`
- Raw: n=64  W=22/L=42  WR=34.4%
- Sharpen: sharpest is RSI=RSI5 (11/42 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: SHORT**  •  HTF20 slightly aligned; HTF60 neutral; 1h trend AGAINST trade  •  ONLY when RSI 60-70 strong

### L20.  `H20=H20b AND H60=H60c AND T4=T4c AND direction_exec=short`
- Raw: n=64  W=22/L=42  WR=34.4%
- Sharpen: sharpest is RSI=RSI5 (11/42 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: SHORT**  •  HTF20 slightly aligned; HTF60 neutral; 4h trend AGAINST trade  •  ONLY when RSI 60-70 strong

### L21.  `H60=H60c AND T1=T1c AND T4=T4c AND direction_exec=short`
- Raw: n=64  W=22/L=42  WR=34.4%
- Sharpen: sharpest is RSI=RSI5 (11/42 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: SHORT**  •  HTF60 neutral; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when RSI 60-70 strong

### L22.  `H20=H20b AND BBP=BBP4 AND RSI=RSI6 AND session_bucket=london_open`
- Raw: n=63  W=20/L=43  WR=31.7%
- Sharpen: sharpest is T1=T1c (28/43 of losers there)
- **Sharp: n=32  W=4/L=28  WR=12.5%**
- **Dir: ?**  •  HTF20 slightly aligned; upper third; RSI 70-80 overbought; session=london_open  •  ONLY when 1h trend AGAINST trade

### L23.  `H20=H20d AND RSI=RSI6 AND session_bucket=ny_open`
- Raw: n=63  W=21/L=42  WR=33.3%
- Sharpen: sharpest is BBP=BBP4 (23/42 of losers there)
- **Sharp: n=30  W=7/L=23  WR=23.3%**
- **Dir: ?**  •  HTF20 mildly against; RSI 70-80 overbought; session=ny_open  •  ONLY when upper third

### L24.  `H20=H20b AND RSI=RSI6 AND ZS=ZS4 AND session_bucket=london_open`
- Raw: n=61  W=19/L=42  WR=31.1%
- Sharpen: sharpest is T1=T1c (28/42 of losers there)
- **Sharp: n=32  W=4/L=28  WR=12.5%**
- **Dir: ?**  •  HTF20 slightly aligned; RSI 70-80 overbought; zscore +1 to +2 overbought; session=london_open  •  ONLY when 1h trend AGAINST trade

### L25.  `H20=H20b AND H60=H60c AND BBP=BBP4`
- Raw: n=56  W=20/L=36  WR=35.7%
- Sharpen: sharpest is session_bucket=london_open (14/36 of losers there)
- **Sharp: n=16  W=2/L=14  WR=12.5%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 neutral; upper third  •  ONLY when session=london_open

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20d(41/33) | H20b(31/41) |
| H60 | H60e(45/38), H60d(7/0) | H60a(33/41), H60b(1/7) |
| T1 | T1a(53/43) | T1c(47/57) |
| T4 | T4a(54/43) | T4c(46/57) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(53/43) | short(47/57) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
