# EUR_CAD — R21 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR3**  (60-90%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **3,331**  (W=2,047 / L=1,284)  -  WR: **61.5%**

## Session distribution

- ny_mid: n=1415  W=879/L=536  WR=62.1%
- ny_close: n=490  W=320/L=170  WR=65.3%
- ny_open: n=470  W=270/L=200  WR=57.4%
- london_open: n=455  W=277/L=178  WR=60.9%
- london: n=214  W=127/L=87  WR=59.3%
- asia: n=147  W=95/L=52  WR=64.6%
- off_hours: n=128  W=72/L=56  WR=56.2%
- asia_late: n=12  W=7/L=5  WR=58.3%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1a AND T4=T4a AND RSI=RSI6`
- Raw: n=129  W=116/L=13  WR=89.9%
- Refine: exclude session_bucket=ny_mid drops 8/13 losers (62%)
- **Final: n=115  W=110/L=5  WR=95.7%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 70-80 overbought  •  AVOID when session=ny_mid

### W02.  `T4=T4a AND RSI=RSI6 AND direction_exec=long`
- Raw: n=129  W=116/L=13  WR=89.9%
- Refine: exclude session_bucket=ny_mid drops 8/13 losers (62%)
- **Final: n=115  W=110/L=5  WR=95.7%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 70-80 overbought  •  AVOID when session=ny_mid

### W03.  `T1=T1a AND T4=T4a AND RSI=RSI6 AND direction_exec=long`
- Raw: n=129  W=116/L=13  WR=89.9%
- Refine: exclude session_bucket=ny_mid drops 8/13 losers (62%)
- **Final: n=115  W=110/L=5  WR=95.7%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; RSI 70-80 overbought  •  AVOID when session=ny_mid

### W04.  `T1=T1a AND RSI=RSI6 AND session_bucket=london_open`
- Raw: n=111  W=106/L=5  WR=95.5%
- Refine: exclude ZS=ZS4 drops 5/5 losers (100%)
- **Final: n=65  W=65/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; RSI 70-80 overbought; session=london_open  •  AVOID when zscore +1 to +2 overbought

### W05.  `T4=T4a AND RSI=RSI6 AND session_bucket=london_open`
- Raw: n=111  W=106/L=5  WR=95.5%
- Refine: exclude ZS=ZS4 drops 5/5 losers (100%)
- **Final: n=65  W=65/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend WITH trade; RSI 70-80 overbought; session=london_open  •  AVOID when zscore +1 to +2 overbought

### W06.  `RSI=RSI6 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=111  W=106/L=5  WR=95.5%
- Refine: exclude ZS=ZS4 drops 5/5 losers (100%)
- **Final: n=65  W=65/L=0  WR=100.0%**
- **Dir: LONG**  •  RSI 70-80 overbought; session=london_open  •  AVOID when zscore +1 to +2 overbought

### W07.  `T1=T1a AND T4=T4a AND RSI=RSI6 AND session_bucket=london_open`
- Raw: n=111  W=106/L=5  WR=95.5%
- Refine: exclude ZS=ZS4 drops 5/5 losers (100%)
- **Final: n=65  W=65/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 70-80 overbought; session=london_open  •  AVOID when zscore +1 to +2 overbought

### W08.  `T1=T1a AND RSI=RSI6 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=111  W=106/L=5  WR=95.5%
- Refine: exclude ZS=ZS4 drops 5/5 losers (100%)
- **Final: n=65  W=65/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 70-80 overbought; session=london_open  •  AVOID when zscore +1 to +2 overbought

### W09.  `T4=T4a AND RSI=RSI6 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=111  W=106/L=5  WR=95.5%
- Refine: exclude ZS=ZS4 drops 5/5 losers (100%)
- **Final: n=65  W=65/L=0  WR=100.0%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 70-80 overbought; session=london_open  •  AVOID when zscore +1 to +2 overbought

### W10.  `H20=H20a AND RSI=RSI3 AND session_bucket=ny_open`
- Raw: n=108  W=92/L=16  WR=85.2%
- Refine: exclude T1=T1a drops 16/16 losers (100%)
- **Final: n=25  W=25/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 40-50 lower neutral; session=ny_open  •  AVOID when 1h trend WITH trade

### W11.  `H60=H60a AND RSI=RSI3 AND session_bucket=ny_open`
- Raw: n=108  W=92/L=16  WR=85.2%
- Refine: exclude T1=T1a drops 16/16 losers (100%)
- **Final: n=25  W=25/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral; session=ny_open  •  AVOID when 1h trend WITH trade

### W12.  `T4=T4c AND RSI=RSI3 AND session_bucket=ny_open`
- Raw: n=108  W=92/L=16  WR=85.2%
- Refine: exclude T1=T1a drops 16/16 losers (100%)
- **Final: n=25  W=25/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; session=ny_open  •  AVOID when 1h trend WITH trade

### W13.  `RSI=RSI3 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=108  W=92/L=16  WR=85.2%
- Refine: exclude T1=T1a drops 16/16 losers (100%)
- **Final: n=25  W=25/L=0  WR=100.0%**
- **Dir: SHORT**  •  RSI 40-50 lower neutral; session=ny_open  •  AVOID when 1h trend WITH trade

### W14.  `H20=H20a AND H60=H60a AND RSI=RSI3 AND session_bucket=ny_open`
- Raw: n=108  W=92/L=16  WR=85.2%
- Refine: exclude T1=T1a drops 16/16 losers (100%)
- **Final: n=25  W=25/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 40-50 lower neutral; session=ny_open  •  AVOID when 1h trend WITH trade

### W15.  `H20=H20a AND T4=T4c AND RSI=RSI3 AND session_bucket=ny_open`
- Raw: n=108  W=92/L=16  WR=85.2%
- Refine: exclude T1=T1a drops 16/16 losers (100%)
- **Final: n=25  W=25/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral; session=ny_open  •  AVOID when 1h trend WITH trade

### W16.  `H20=H20a AND RSI=RSI3 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=108  W=92/L=16  WR=85.2%
- Refine: exclude T1=T1a drops 16/16 losers (100%)
- **Final: n=25  W=25/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 40-50 lower neutral; session=ny_open  •  AVOID when 1h trend WITH trade

### W17.  `H60=H60a AND T4=T4c AND RSI=RSI3 AND session_bucket=ny_open`
- Raw: n=108  W=92/L=16  WR=85.2%
- Refine: exclude T1=T1a drops 16/16 losers (100%)
- **Final: n=25  W=25/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral; session=ny_open  •  AVOID when 1h trend WITH trade

### W18.  `H60=H60a AND RSI=RSI3 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=108  W=92/L=16  WR=85.2%
- Refine: exclude T1=T1a drops 16/16 losers (100%)
- **Final: n=25  W=25/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral; session=ny_open  •  AVOID when 1h trend WITH trade

### W19.  `T4=T4c AND RSI=RSI3 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=108  W=92/L=16  WR=85.2%
- Refine: exclude T1=T1a drops 16/16 losers (100%)
- **Final: n=25  W=25/L=0  WR=100.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; session=ny_open  •  AVOID when 1h trend WITH trade

### W20.  `T4=T4c AND ZS=ZS2 AND session_bucket=ny_open`
- Raw: n=100  W=91/L=9  WR=91.0%
- Refine: exclude T1=T1a drops 8/9 losers (89%)
- **Final: n=41  W=40/L=1  WR=97.6%**
- **Dir: ?**  •  4h trend AGAINST trade; zscore -2 to -1 oversold; session=ny_open  •  AVOID when 1h trend WITH trade

### W21.  `T4=T4c AND BBP=BBP2 AND ZS=ZS2 AND session_bucket=ny_open`
- Raw: n=100  W=91/L=9  WR=91.0%
- Refine: exclude T1=T1a drops 8/9 losers (89%)
- **Final: n=41  W=40/L=1  WR=97.6%**
- **Dir: ?**  •  4h trend AGAINST trade; lower third; zscore -2 to -1 oversold; session=ny_open  •  AVOID when 1h trend WITH trade

### W22.  `T4=T4a AND direction_exec=long AND session_bucket=london`
- Raw: n=100  W=85/L=15  WR=85.0%
- Refine: exclude RSI=RSI4 drops 15/15 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: LONG**  •  4h trend WITH trade; session=london  •  AVOID when RSI 50-60 upper neutral

### W23.  `T1=T1a AND T4=T4a AND direction_exec=long AND session_bucket=london`
- Raw: n=100  W=85/L=15  WR=85.0%
- Refine: exclude RSI=RSI4 drops 15/15 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; session=london  •  AVOID when RSI 50-60 upper neutral

### W24.  `H20=H20a AND ZS=ZS2 AND session_bucket=ny_open`
- Raw: n=97  W=85/L=12  WR=87.6%
- Refine: exclude T1=T1a drops 12/12 losers (100%)
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; zscore -2 to -1 oversold; session=ny_open  •  AVOID when 1h trend WITH trade

### W25.  `H60=H60a AND ZS=ZS2 AND session_bucket=ny_open`
- Raw: n=97  W=85/L=12  WR=87.6%
- Refine: exclude T1=T1a drops 12/12 losers (100%)
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; zscore -2 to -1 oversold; session=ny_open  •  AVOID when 1h trend WITH trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND H60=H60e AND session_bucket=ny_open`
- Raw: n=193  W=64/L=129  WR=33.2%
- Sharpen: sharpest is T1=T1a (75/129 of losers there)
- **Sharp: n=97  W=22/L=75  WR=22.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; session=ny_open  •  ONLY when 1h trend WITH trade

### L02.  `H20=H20e AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=183  W=60/L=123  WR=32.8%
- Sharpen: sharpest is T1=T1a (75/123 of losers there)
- **Sharp: n=97  W=22/L=75  WR=22.7%**
- **Dir: LONG**  •  HTF20 strongly against; session=ny_open  •  ONLY when 1h trend WITH trade

### L03.  `H60=H60e AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=183  W=60/L=123  WR=32.8%
- Sharpen: sharpest is T1=T1a (75/123 of losers there)
- **Sharp: n=97  W=22/L=75  WR=22.7%**
- **Dir: LONG**  •  HTF60 strongly against; session=ny_open  •  ONLY when 1h trend WITH trade

### L04.  `H20=H20e AND H60=H60e AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=183  W=60/L=123  WR=32.8%
- Sharpen: sharpest is T1=T1a (75/123 of losers there)
- **Sharp: n=97  W=22/L=75  WR=22.7%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 strongly against; session=ny_open  •  ONLY when 1h trend WITH trade

### L05.  `T4=T4a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=181  W=70/L=111  WR=38.7%
- Sharpen: sharpest is H20=H20e (108/111 of losers there)
- **Sharp: n=149  W=41/L=108  WR=27.5%**
- **Dir: LONG**  •  4h trend WITH trade; session=ny_open  •  ONLY when HTF20 strongly against

### L06.  `H20=H20e AND T4=T4a AND session_bucket=ny_open`
- Raw: n=149  W=41/L=108  WR=27.5%
- Sharpen: sharpest is ZS=ZS2 (58/108 of losers there)
- **Sharp: n=68  W=10/L=58  WR=14.7%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; session=ny_open  •  ONLY when zscore -2 to -1 oversold

### L07.  `H60=H60e AND T4=T4a AND session_bucket=ny_open`
- Raw: n=149  W=41/L=108  WR=27.5%
- Sharpen: sharpest is ZS=ZS2 (58/108 of losers there)
- **Sharp: n=68  W=10/L=58  WR=14.7%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; session=ny_open  •  ONLY when zscore -2 to -1 oversold

### L08.  `H20=H20e AND H60=H60e AND T4=T4a AND session_bucket=ny_open`
- Raw: n=149  W=41/L=108  WR=27.5%
- Sharpen: sharpest is ZS=ZS2 (58/108 of losers there)
- **Sharp: n=68  W=10/L=58  WR=14.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend WITH trade; session=ny_open  •  ONLY when zscore -2 to -1 oversold

### L09.  `H20=H20e AND T4=T4a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=149  W=41/L=108  WR=27.5%
- Sharpen: sharpest is ZS=ZS2 (58/108 of losers there)
- **Sharp: n=68  W=10/L=58  WR=14.7%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend WITH trade; session=ny_open  •  ONLY when zscore -2 to -1 oversold

### L10.  `H60=H60e AND T4=T4a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=149  W=41/L=108  WR=27.5%
- Sharpen: sharpest is ZS=ZS2 (58/108 of losers there)
- **Sharp: n=68  W=10/L=58  WR=14.7%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend WITH trade; session=ny_open  •  ONLY when zscore -2 to -1 oversold

### L11.  `T1=T1c AND RSI=RSI6 AND direction_exec=short`
- Raw: n=145  W=41/L=104  WR=28.3%
- Sharpen: sharpest is session_bucket=london_open (66/104 of losers there)
- **Sharp: n=72  W=6/L=66  WR=8.3%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when session=london_open

### L12.  `H20=H20e AND T1=T1a AND ZS=ZS4 AND direction_exec=long`
- Raw: n=135  W=53/L=82  WR=39.3%
- Sharpen: sharpest is T4=T4a (73/82 of losers there)
- **Sharp: n=109  W=36/L=73  WR=33.0%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend WITH trade; zscore +1 to +2 overbought  •  ONLY when 4h trend WITH trade

### L13.  `H20=H20e AND T1=T1a AND T4=T4a AND BBP=BBP4`
- Raw: n=130  W=48/L=82  WR=36.9%
- Sharpen: sharpest is session_bucket=ny_mid (56/82 of losers there)
- **Sharp: n=71  W=15/L=56  WR=21.1%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend WITH trade; upper third  •  ONLY when session=ny_mid

### L14.  `T1=T1a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=129  W=51/L=78  WR=39.5%
- Sharpen: sharpest is H20=H20e (75/78 of losers there)
- **Sharp: n=97  W=22/L=75  WR=22.7%**
- **Dir: LONG**  •  1h trend WITH trade; session=ny_open  •  ONLY when HTF20 strongly against

### L15.  `H20=H20e AND T1=T1a AND T4=T4a AND ZS=ZS4`
- Raw: n=109  W=36/L=73  WR=33.0%
- Sharpen: sharpest is session_bucket=ny_mid (49/73 of losers there)
- **Sharp: n=58  W=9/L=49  WR=15.5%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend WITH trade; zscore +1 to +2 overbought  •  ONLY when session=ny_mid

### L16.  `T4=T4a AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=103  W=36/L=67  WR=35.0%
- Sharpen: sharpest is session_bucket=ny_open (51/67 of losers there)
- **Sharp: n=61  W=10/L=51  WR=16.4%**
- **Dir: ?**  •  4h trend WITH trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  ONLY when session=ny_open

### L17.  `RSI=RSI3 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=103  W=36/L=67  WR=35.0%
- Sharpen: sharpest is session_bucket=ny_open (51/67 of losers there)
- **Sharp: n=61  W=10/L=51  WR=16.4%**
- **Dir: LONG**  •  RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  ONLY when session=ny_open

### L18.  `T4=T4a AND BBP=BBP2 AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=103  W=36/L=67  WR=35.0%
- Sharpen: sharpest is session_bucket=ny_open (51/67 of losers there)
- **Sharp: n=61  W=10/L=51  WR=16.4%**
- **Dir: ?**  •  4h trend WITH trade; lower third; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  ONLY when session=ny_open

### L19.  `T4=T4a AND RSI=RSI3 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=103  W=36/L=67  WR=35.0%
- Sharpen: sharpest is session_bucket=ny_open (51/67 of losers there)
- **Sharp: n=61  W=10/L=51  WR=16.4%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  ONLY when session=ny_open

### L20.  `BBP=BBP2 AND RSI=RSI3 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=103  W=36/L=67  WR=35.0%
- Sharpen: sharpest is session_bucket=ny_open (51/67 of losers there)
- **Sharp: n=61  W=10/L=51  WR=16.4%**
- **Dir: LONG**  •  lower third; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  ONLY when session=ny_open

### L21.  `H20=H20e AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=102  W=40/L=62  WR=39.2%
- Sharpen: sharpest is session_bucket=ny_open (51/62 of losers there)
- **Sharp: n=61  W=10/L=51  WR=16.4%**
- **Dir: ?**  •  HTF20 strongly against; lower third; RSI 40-50 lower neutral  •  ONLY when session=ny_open

### L22.  `H60=H60e AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=99  W=39/L=60  WR=39.4%
- Sharpen: sharpest is session_bucket=ny_open (51/60 of losers there)
- **Sharp: n=61  W=10/L=51  WR=16.4%**
- **Dir: ?**  •  HTF60 strongly against; lower third; RSI 40-50 lower neutral  •  ONLY when session=ny_open

### L23.  `H60=H60b AND T1=T1c AND RSI=RSI6`
- Raw: n=98  W=26/L=72  WR=26.5%
- Sharpen: sharpest is T4=T4c (45/72 of losers there)
- **Sharp: n=45  W=0/L=45  WR=0.0%**
- **Dir: ?**  •  HTF60 slightly aligned; 1h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when 4h trend AGAINST trade

### L24.  `H60=H60b AND RSI=RSI6 AND direction_exec=short`
- Raw: n=98  W=26/L=72  WR=26.5%
- Sharpen: sharpest is T4=T4c (45/72 of losers there)
- **Sharp: n=45  W=0/L=45  WR=0.0%**
- **Dir: SHORT**  •  HTF60 slightly aligned; RSI 70-80 overbought  •  ONLY when 4h trend AGAINST trade

### L25.  `H60=H60b AND T1=T1c AND RSI=RSI6 AND direction_exec=short`
- Raw: n=98  W=26/L=72  WR=26.5%
- Sharpen: sharpest is T4=T4c (45/72 of losers there)
- **Sharp: n=45  W=0/L=45  WR=0.0%**
- **Dir: SHORT**  •  HTF60 slightly aligned; 1h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when 4h trend AGAINST trade

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | H60e(35/42) |
| T1 | — | — |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
