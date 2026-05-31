# EUR_CHF — R25 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20d**  (EMA20 down 0.15-0.5x)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **696**  (W=447 / L=249)  -  WR: **64.2%**

## Session distribution

- london_open: n=338  W=217/L=121  WR=64.2%
- ny_open: n=116  W=73/L=43  WR=62.9%
- ny_mid: n=115  W=81/L=34  WR=70.4%
- london: n=57  W=34/L=23  WR=59.6%
- asia: n=44  W=26/L=18  WR=59.1%
- asia_late: n=18  W=12/L=6  WR=66.7%
- ny_close: n=8  W=4/L=4  WR=50.0%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20e AND T1=T1a AND RSI=RSI2`
- Raw: n=68  W=65/L=3  WR=95.6%
- Refine: exclude BBP=BBP0 drops 2/3 losers (67%)
- **Final: n=64  W=63/L=1  WR=98.4%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; RSI 30-40 weak  •  AVOID when deep below lower band

### W02.  `T4=T4c AND direction_exec=short AND session_bucket=london_open`
- Raw: n=63  W=54/L=9  WR=85.7%
- Refine: exclude ZS=ZS1 drops 8/9 losers (89%)
- **Final: n=31  W=30/L=1  WR=96.8%**
- **Dir: SHORT**  •  4h trend AGAINST trade; session=london_open  •  AVOID when zscore -3 to -2 deep oversold

### W03.  `H20=H20e AND H60=H60e AND BBP=BBP2`
- Raw: n=61  W=52/L=9  WR=85.2%
- Refine: exclude session_bucket=ny_open drops 3/9 losers (33%)
- **Final: n=58  W=52/L=6  WR=89.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; lower third  •  AVOID when session=ny_open

### W04.  `H60=H60a AND T4=T4c AND session_bucket=london_open`
- Raw: n=61  W=52/L=9  WR=85.2%
- Refine: exclude ZS=ZS1 drops 8/9 losers (89%)
- **Final: n=29  W=28/L=1  WR=96.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=london_open  •  AVOID when zscore -3 to -2 deep oversold

### W05.  `H20=H20e AND H60=H60e AND BBP=BBP2 AND direction_exec=long`
- Raw: n=61  W=52/L=9  WR=85.2%
- Refine: exclude session_bucket=ny_open drops 3/9 losers (33%)
- **Final: n=58  W=52/L=6  WR=89.7%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 strongly against; lower third  •  AVOID when session=ny_open

### W06.  `H60=H60a AND T4=T4c AND direction_exec=short AND session_bucket=london_open`
- Raw: n=61  W=52/L=9  WR=85.2%
- Refine: exclude ZS=ZS1 drops 8/9 losers (89%)
- **Final: n=29  W=28/L=1  WR=96.6%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=london_open  •  AVOID when zscore -3 to -2 deep oversold

### W07.  `H20=H20e AND RSI=RSI2 AND direction_exec=short`
- Raw: n=60  W=58/L=2  WR=96.7%
- Refine: exclude BBP=BBP0 drops 2/2 losers (100%)
- **Final: n=56  W=56/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 30-40 weak  •  AVOID when deep below lower band

### W08.  `H20=H20e AND T1=T1a AND RSI=RSI2 AND direction_exec=short`
- Raw: n=60  W=58/L=2  WR=96.7%
- Refine: exclude BBP=BBP0 drops 2/2 losers (100%)
- **Final: n=56  W=56/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend WITH trade; RSI 30-40 weak  •  AVOID when deep below lower band

### W09.  `H20=H20e AND BBP=BBP2 AND direction_exec=short`
- Raw: n=58  W=55/L=3  WR=94.8%
- Refine: exclude RSI=RSI3 drops 3/3 losers (100%)
- **Final: n=38  W=38/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 strongly against; lower third  •  AVOID when RSI 40-50 lower neutral

### W10.  `H60=H60a AND RSI=RSI3 AND session_bucket=london_open`
- Raw: n=56  W=48/L=8  WR=85.7%
- Refine: exclude ZS=ZS1 drops 6/8 losers (75%)
- **Final: n=28  W=26/L=2  WR=92.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral; session=london_open  •  AVOID when zscore -3 to -2 deep oversold

### W11.  `H60=H60a AND RSI=RSI3 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=56  W=48/L=8  WR=85.7%
- Refine: exclude ZS=ZS1 drops 6/8 losers (75%)
- **Final: n=28  W=26/L=2  WR=92.9%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral; session=london_open  •  AVOID when zscore -3 to -2 deep oversold

### W12.  `H20=H20e AND direction_exec=short AND session_bucket=london_open`
- Raw: n=55  W=48/L=7  WR=87.3%
- Refine: exclude ZS=ZS1 drops 7/7 losers (100%)
- **Final: n=22  W=22/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 strongly against; session=london_open  •  AVOID when zscore -3 to -2 deep oversold

### W13.  `T4=T4c AND RSI=RSI3 AND session_bucket=london_open`
- Raw: n=55  W=48/L=7  WR=87.3%
- Refine: exclude ZS=ZS1 drops 6/7 losers (86%)
- **Final: n=27  W=26/L=1  WR=96.3%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; session=london_open  •  AVOID when zscore -3 to -2 deep oversold

### W14.  `H60=H60a AND T4=T4c AND RSI=RSI3 AND session_bucket=london_open`
- Raw: n=55  W=48/L=7  WR=87.3%
- Refine: exclude ZS=ZS1 drops 6/7 losers (86%)
- **Final: n=27  W=26/L=1  WR=96.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral; session=london_open  •  AVOID when zscore -3 to -2 deep oversold

### W15.  `T4=T4c AND RSI=RSI3 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=55  W=48/L=7  WR=87.3%
- Refine: exclude ZS=ZS1 drops 6/7 losers (86%)
- **Final: n=27  W=26/L=1  WR=96.3%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; session=london_open  •  AVOID when zscore -3 to -2 deep oversold

### W16.  `H20=H20e AND ZS=ZS2 AND direction_exec=short`
- Raw: n=52  W=50/L=2  WR=96.2%
- Refine: exclude session_bucket=ny_close drops 2/2 losers (100%)
- **Final: n=50  W=50/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 strongly against; zscore -2 to -1 oversold  •  AVOID when session=ny_close

### W17.  `H20=H20e AND BBP=BBP2 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=52  W=50/L=2  WR=96.2%
- Refine: exclude session_bucket=ny_close drops 2/2 losers (100%)
- **Final: n=50  W=50/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 strongly against; lower third; zscore -2 to -1 oversold  •  AVOID when session=ny_close

### W18.  `H60=H60a AND T1=T1c AND T4=T4c`
- Raw: n=51  W=46/L=5  WR=90.2%
- Refine: exclude ZS=ZS1 drops 5/5 losers (100%)
- **Final: n=26  W=26/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade  •  AVOID when zscore -3 to -2 deep oversold

### W19.  `T4=T4c AND BBP=BBP2 AND session_bucket=ny_mid`
- Raw: n=51  W=45/L=6  WR=88.2%
- Refine: exclude H20=H20a drops 6/6 losers (100%)
- **Final: n=44  W=44/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend AGAINST trade; lower third; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

### W20.  `H20=H20e AND T1=T1a AND BBP=BBP2`
- Raw: n=48  W=45/L=3  WR=93.8%
- Refine: exclude RSI=RSI3 drops 3/3 losers (100%)
- **Final: n=42  W=42/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; lower third  •  AVOID when RSI 40-50 lower neutral

### W21.  `H60=H60a AND T1=T1c AND RSI=RSI3`
- Raw: n=48  W=42/L=6  WR=87.5%
- Refine: exclude session_bucket=london_open drops 6/6 losers (100%)
- **Final: n=16  W=16/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when session=london_open

### W22.  `H60=H60a AND T1=T1c AND RSI=RSI3 AND direction_exec=short`
- Raw: n=48  W=42/L=6  WR=87.5%
- Refine: exclude session_bucket=london_open drops 6/6 losers (100%)
- **Final: n=16  W=16/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when session=london_open

### W23.  `H20=H20e AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=47  W=41/L=6  WR=87.2%
- Refine: exclude session_bucket=ny_open drops 4/6 losers (67%)
- **Final: n=42  W=40/L=2  WR=95.2%**
- **Dir: ?**  •  HTF20 strongly against; lower third; RSI 40-50 lower neutral  •  AVOID when session=ny_open

### W24.  `T4=T4c AND ZS=ZS2 AND session_bucket=ny_mid`
- Raw: n=45  W=40/L=5  WR=88.9%
- Refine: exclude H20=H20a drops 5/5 losers (100%)
- **Final: n=40  W=40/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend AGAINST trade; zscore -2 to -1 oversold; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

### W25.  `T4=T4c AND BBP=BBP2 AND ZS=ZS2 AND session_bucket=ny_mid`
- Raw: n=45  W=40/L=5  WR=88.9%
- Refine: exclude H20=H20a drops 5/5 losers (100%)
- **Final: n=40  W=40/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend AGAINST trade; lower third; zscore -2 to -1 oversold; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1a AND T4=T4a AND RSI=RSI3`
- Raw: n=67  W=23/L=44  WR=34.3%
- Sharpen: sharpest is ZS=ZS5 (7/44 of losers there)
- **Sharp: n=7  W=0/L=7  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when zscore +2 to +3 deep overbought

### L02.  `H20=H20a AND T1=T1a AND RSI=RSI3`
- Raw: n=66  W=22/L=44  WR=33.3%
- Sharpen: sharpest is session_bucket=ny_mid (15/44 of losers there)
- **Sharp: n=17  W=2/L=15  WR=11.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when session=ny_mid

### L03.  `H20=H20a AND H60=H60e AND T4=T4a`
- Raw: n=60  W=23/L=37  WR=38.3%
- Sharpen: sharpest is BBP=BBP2 (22/37 of losers there)
- **Sharp: n=23  W=1/L=22  WR=4.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 4h trend WITH trade  •  ONLY when lower third

### L04.  `H20=H20a AND H60=H60e AND direction_exec=long`
- Raw: n=60  W=23/L=37  WR=38.3%
- Sharpen: sharpest is BBP=BBP2 (22/37 of losers there)
- **Sharp: n=23  W=1/L=22  WR=4.3%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 strongly against  •  ONLY when lower third

### L05.  `H20=H20a AND H60=H60e AND T4=T4a AND direction_exec=long`
- Raw: n=60  W=23/L=37  WR=38.3%
- Sharpen: sharpest is BBP=BBP2 (22/37 of losers there)
- **Sharp: n=23  W=1/L=22  WR=4.3%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 strongly against; 4h trend WITH trade  •  ONLY when lower third

### L06.  `H20=H20a AND T1=T1a AND T4=T4a AND RSI=RSI3`
- Raw: n=59  W=21/L=38  WR=35.6%
- Sharpen: sharpest is H60=H60e (22/38 of losers there)
- **Sharp: n=30  W=8/L=22  WR=26.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when HTF60 strongly against

### L07.  `T4=T4a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=53  W=21/L=32  WR=39.6%
- Sharpen: sharpest is ZS=ZS2 (18/32 of losers there)
- **Sharp: n=22  W=4/L=18  WR=18.2%**
- **Dir: LONG**  •  4h trend WITH trade; session=london_open  •  ONLY when zscore -2 to -1 oversold

### L08.  `T4=T4a AND RSI=RSI3 AND session_bucket=london_open`
- Raw: n=50  W=17/L=33  WR=34.0%
- Sharpen: sharpest is ZS=ZS2 (17/33 of losers there)
- **Sharp: n=21  W=4/L=17  WR=19.0%**
- **Dir: ?**  •  4h trend WITH trade; RSI 40-50 lower neutral; session=london_open  •  ONLY when zscore -2 to -1 oversold

### L09.  `H20=H20a AND T1=T1c AND direction_exec=long`
- Raw: n=49  W=19/L=30  WR=38.8%
- Sharpen: sharpest is BBP=BBP2 (20/30 of losers there)
- **Sharp: n=25  W=5/L=20  WR=20.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade  •  ONLY when lower third

### L10.  `H20=H20a AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=48  W=17/L=31  WR=35.4%
- Sharpen: sharpest is H60=H60e (16/31 of losers there)
- **Sharp: n=17  W=1/L=16  WR=5.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; lower third; RSI 40-50 lower neutral  •  ONLY when HTF60 strongly against

### L11.  `H60=H60e AND RSI=RSI3 AND session_bucket=london_open`
- Raw: n=46  W=17/L=29  WR=37.0%
- Sharpen: sharpest is ZS=ZS2 (15/29 of losers there)
- **Sharp: n=19  W=4/L=15  WR=21.1%**
- **Dir: ?**  •  HTF60 strongly against; RSI 40-50 lower neutral; session=london_open  •  ONLY when zscore -2 to -1 oversold

### L12.  `RSI=RSI3 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=46  W=17/L=29  WR=37.0%
- Sharpen: sharpest is ZS=ZS2 (15/29 of losers there)
- **Sharp: n=19  W=4/L=15  WR=21.1%**
- **Dir: LONG**  •  RSI 40-50 lower neutral; session=london_open  •  ONLY when zscore -2 to -1 oversold

### L13.  `H60=H60e AND T4=T4a AND RSI=RSI3 AND session_bucket=london_open`
- Raw: n=46  W=17/L=29  WR=37.0%
- Sharpen: sharpest is ZS=ZS2 (15/29 of losers there)
- **Sharp: n=19  W=4/L=15  WR=21.1%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; RSI 40-50 lower neutral; session=london_open  •  ONLY when zscore -2 to -1 oversold

### L14.  `H60=H60e AND RSI=RSI3 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=46  W=17/L=29  WR=37.0%
- Sharpen: sharpest is ZS=ZS2 (15/29 of losers there)
- **Sharp: n=19  W=4/L=15  WR=21.1%**
- **Dir: LONG**  •  HTF60 strongly against; RSI 40-50 lower neutral; session=london_open  •  ONLY when zscore -2 to -1 oversold

### L15.  `T4=T4a AND RSI=RSI3 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=46  W=17/L=29  WR=37.0%
- Sharpen: sharpest is ZS=ZS2 (15/29 of losers there)
- **Sharp: n=19  W=4/L=15  WR=21.1%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 40-50 lower neutral; session=london_open  •  ONLY when zscore -2 to -1 oversold

### L16.  `H20=H20a AND T1=T1c AND RSI=RSI2`
- Raw: n=44  W=12/L=32  WR=27.3%
- Sharpen: sharpest is BBP=BBP2 (21/32 of losers there)
- **Sharp: n=25  W=4/L=21  WR=16.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 30-40 weak  •  ONLY when lower third

### L17.  `H20=H20a AND T1=T1a AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=42  W=14/L=28  WR=33.3%
- Sharpen: sharpest is H60=H60e (13/28 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; lower third; RSI 40-50 lower neutral  •  ONLY when HTF60 strongly against

### L18.  `H60=H60e AND T1=T1a AND direction_exec=long`
- Raw: n=42  W=15/L=27  WR=35.7%
- Sharpen: sharpest is RSI=RSI3 (26/27 of losers there)
- **Sharp: n=34  W=8/L=26  WR=23.5%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend WITH trade  •  ONLY when RSI 40-50 lower neutral

### L19.  `H20=H20d AND T4=T4a AND RSI=RSI3`
- Raw: n=42  W=16/L=26  WR=38.1%
- Sharpen: sharpest is session_bucket=london_open (11/26 of losers there)
- **Sharp: n=14  W=3/L=11  WR=21.4%**
- **Dir: ?**  •  HTF20 mildly against; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when session=london_open

### L20.  `T1=T1c AND T4=T4a AND session_bucket=london_open`
- Raw: n=42  W=16/L=26  WR=38.1%
- Sharpen: sharpest is H20=H20d (11/26 of losers there)
- **Sharp: n=14  W=3/L=11  WR=21.4%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; session=london_open  •  ONLY when HTF20 mildly against

### L21.  `H20=H20a AND T4=T4a AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=41  W=16/L=25  WR=39.0%
- Sharpen: sharpest is H60=H60e (16/25 of losers there)
- **Sharp: n=17  W=1/L=16  WR=5.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; lower third; RSI 40-50 lower neutral  •  ONLY when HTF60 strongly against

### L22.  `H20=H20a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=40  W=13/L=27  WR=32.5%
- Sharpen: sharpest is BBP=BBP2 (15/27 of losers there)
- **Sharp: n=16  W=1/L=15  WR=6.2%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; session=london_open  •  ONLY when lower third

### L23.  `H20=H20a AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=40  W=15/L=25  WR=37.5%
- Sharpen: sharpest is H60=H60e (13/25 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  ONLY when HTF60 strongly against

### L24.  `H20=H20a AND BBP=BBP2 AND RSI=RSI3 AND ZS=ZS2`
- Raw: n=40  W=15/L=25  WR=37.5%
- Sharpen: sharpest is H60=H60e (13/25 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; lower third; RSI 40-50 lower neutral; zscore -2 to -1 oversold  •  ONLY when HTF60 strongly against

### L25.  `H20=H20a AND BBP=BBP2 AND direction_exec=long`
- Raw: n=38  W=5/L=33  WR=13.2%
- Sharpen: sharpest is H60=H60e (22/33 of losers there)
- **Sharp: n=23  W=1/L=22  WR=4.3%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; lower third  •  ONLY when HTF60 strongly against

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20e(52/23) | H20a(23/51) |
| H60 | H60b(9/2) | H60d(3/10) |
| T1 | T1c(58/44) | T1a(42/56) |
| T4 | T4c(58/43) | T4a(42/57) |
| BBP | — | — |
| RSI | RSI2(52/47) | RSI3(41/47) |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
