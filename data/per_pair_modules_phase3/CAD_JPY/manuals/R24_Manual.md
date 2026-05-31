# CAD_JPY — R24 Manual

## Regime centroid (locked factors)

- **BB = BB2**  (normal bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **2,261**  (W=1,417 / L=844)  -  WR: **62.7%**

## Session distribution

- asia: n=580  W=367/L=213  WR=63.3%
- london_open: n=387  W=242/L=145  WR=62.5%
- ny_mid: n=346  W=216/L=130  WR=62.4%
- ny_close: n=280  W=166/L=114  WR=59.3%
- london: n=245  W=152/L=93  WR=62.0%
- ny_open: n=239  W=155/L=84  WR=64.9%
- asia_late: n=110  W=71/L=39  WR=64.5%
- off_hours: n=74  W=48/L=26  WR=64.9%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1a AND T4=T4c AND session_bucket=london_open`
- Raw: n=108  W=92/L=16  WR=85.2%
- Refine: exclude RSI=RSI3 drops 10/16 losers (62%)
- **Final: n=58  W=52/L=6  WR=89.7%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; session=london_open  •  AVOID when RSI 40-50 lower neutral

### W02.  `H20=H20e AND T1=T1a AND session_bucket=london_open`
- Raw: n=100  W=91/L=9  WR=91.0%
- Refine: exclude ZS=ZS5 drops 9/9 losers (100%)
- **Final: n=71  W=71/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; session=london_open  •  AVOID when zscore +2 to +3 deep overbought

### W03.  `T4=T4c AND BBP=BBP0 AND RSI=RSI3`
- Raw: n=95  W=82/L=13  WR=86.3%
- Refine: exclude T1=T1a drops 9/13 losers (69%)
- **Final: n=66  W=62/L=4  WR=93.9%**
- **Dir: ?**  •  4h trend AGAINST trade; deep below lower band; RSI 40-50 lower neutral  •  AVOID when 1h trend WITH trade

### W04.  `H60=H60a AND T4=T4c AND ZS=ZS1`
- Raw: n=92  W=80/L=12  WR=87.0%
- Refine: exclude session_bucket=ny_mid drops 9/12 losers (75%)
- **Final: n=73  W=70/L=3  WR=95.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  AVOID when session=ny_mid

### W05.  `T4=T4c AND ZS=ZS1 AND direction_exec=long`
- Raw: n=92  W=80/L=12  WR=87.0%
- Refine: exclude session_bucket=ny_mid drops 9/12 losers (75%)
- **Final: n=73  W=70/L=3  WR=95.9%**
- **Dir: LONG**  •  4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  AVOID when session=ny_mid

### W06.  `H60=H60a AND T4=T4c AND ZS=ZS1 AND direction_exec=long`
- Raw: n=92  W=80/L=12  WR=87.0%
- Refine: exclude session_bucket=ny_mid drops 9/12 losers (75%)
- **Final: n=73  W=70/L=3  WR=95.9%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  AVOID when session=ny_mid

### W07.  `T4=T4c AND BBP=BBP0 AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=85  W=74/L=11  WR=87.1%
- Refine: exclude T1=T1a drops 9/11 losers (82%)
- **Final: n=56  W=54/L=2  WR=96.4%**
- **Dir: ?**  •  4h trend AGAINST trade; deep below lower band; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when 1h trend WITH trade

### W08.  `H60=H60a AND T4=T4c AND BBP=BBP0`
- Raw: n=82  W=74/L=8  WR=90.2%
- Refine: exclude session_bucket=london_open drops 6/8 losers (75%)
- **Final: n=76  W=74/L=2  WR=97.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; deep below lower band  •  AVOID when session=london_open

### W09.  `T4=T4c AND BBP=BBP0 AND direction_exec=long`
- Raw: n=82  W=74/L=8  WR=90.2%
- Refine: exclude session_bucket=london_open drops 6/8 losers (75%)
- **Final: n=76  W=74/L=2  WR=97.4%**
- **Dir: LONG**  •  4h trend AGAINST trade; deep below lower band  •  AVOID when session=london_open

### W10.  `H60=H60a AND T4=T4c AND BBP=BBP0 AND direction_exec=long`
- Raw: n=82  W=74/L=8  WR=90.2%
- Refine: exclude session_bucket=london_open drops 6/8 losers (75%)
- **Final: n=76  W=74/L=2  WR=97.4%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; deep below lower band  •  AVOID when session=london_open

### W11.  `T1=T1c AND T4=T4c AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=80  W=69/L=11  WR=86.2%
- Refine: exclude session_bucket=ny_open drops 7/11 losers (64%)
- **Final: n=73  W=69/L=4  WR=94.5%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when session=ny_open

### W12.  `H60=H60a AND T1=T1c AND T4=T4c AND ZS=ZS1`
- Raw: n=79  W=68/L=11  WR=86.1%
- Refine: exclude session_bucket=ny_mid drops 9/11 losers (82%)
- **Final: n=60  W=58/L=2  WR=96.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  AVOID when session=ny_mid

### W13.  `T1=T1c AND T4=T4c AND ZS=ZS1 AND direction_exec=long`
- Raw: n=79  W=68/L=11  WR=86.1%
- Refine: exclude session_bucket=ny_mid drops 9/11 losers (82%)
- **Final: n=60  W=58/L=2  WR=96.7%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  AVOID when session=ny_mid

### W14.  `H60=H60a AND T1=T1a AND RSI=RSI5`
- Raw: n=77  W=71/L=6  WR=92.2%
- Refine: exclude BBP=BBP6 drops 6/6 losers (100%)
- **Final: n=51  W=51/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when deep above upper band

### W15.  `H60=H60a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=77  W=71/L=6  WR=92.2%
- Refine: exclude BBP=BBP6 drops 6/6 losers (100%)
- **Final: n=51  W=51/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 60-70 strong  •  AVOID when deep above upper band

### W16.  `T1=T1a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=77  W=71/L=6  WR=92.2%
- Refine: exclude BBP=BBP6 drops 6/6 losers (100%)
- **Final: n=51  W=51/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 60-70 strong  •  AVOID when deep above upper band

### W17.  `H60=H60a AND T1=T1a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=77  W=71/L=6  WR=92.2%
- Refine: exclude BBP=BBP6 drops 6/6 losers (100%)
- **Final: n=51  W=51/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when deep above upper band

### W18.  `T1=T1c AND T4=T4c AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=76  W=65/L=11  WR=85.5%
- Refine: exclude RSI=RSI4 drops 9/11 losers (82%)
- **Final: n=62  W=60/L=2  WR=96.8%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; deep below lower band; zscore -3 to -2 deep oversold  •  AVOID when RSI 50-60 upper neutral

### W19.  `H60=H60a AND T1=T1c AND T4=T4c AND BBP=BBP0`
- Raw: n=74  W=66/L=8  WR=89.2%
- Refine: exclude session_bucket=london_open drops 6/8 losers (75%)
- **Final: n=68  W=66/L=2  WR=97.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; deep below lower band  •  AVOID when session=london_open

### W20.  `T1=T1c AND T4=T4c AND BBP=BBP0 AND direction_exec=long`
- Raw: n=74  W=66/L=8  WR=89.2%
- Refine: exclude session_bucket=london_open drops 6/8 losers (75%)
- **Final: n=68  W=66/L=2  WR=97.1%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; deep below lower band  •  AVOID when session=london_open

### W21.  `H60=H60e AND T1=T1a AND session_bucket=london_open`
- Raw: n=70  W=60/L=10  WR=85.7%
- Refine: exclude RSI=RSI3 drops 10/10 losers (100%)
- **Final: n=26  W=26/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; session=london_open  •  AVOID when RSI 40-50 lower neutral

### W22.  `T1=T1a AND direction_exec=short AND session_bucket=london_open`
- Raw: n=70  W=60/L=10  WR=85.7%
- Refine: exclude RSI=RSI3 drops 10/10 losers (100%)
- **Final: n=26  W=26/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend WITH trade; session=london_open  •  AVOID when RSI 40-50 lower neutral

### W23.  `H60=H60e AND T1=T1a AND direction_exec=short AND session_bucket=london_open`
- Raw: n=70  W=60/L=10  WR=85.7%
- Refine: exclude RSI=RSI3 drops 10/10 losers (100%)
- **Final: n=26  W=26/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend WITH trade; session=london_open  •  AVOID when RSI 40-50 lower neutral

### W24.  `H60=H60a AND T4=T4c AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=69  W=64/L=5  WR=92.8%
- Refine: exclude BBP=BBP1 drops 3/5 losers (60%)
- **Final: n=50  W=48/L=2  WR=96.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when just touched lower band

### W25.  `T4=T4c AND RSI=RSI3 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=69  W=64/L=5  WR=92.8%
- Refine: exclude BBP=BBP1 drops 3/5 losers (60%)
- **Final: n=50  W=48/L=2  WR=96.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when just touched lower band

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1c AND T4=T4a AND session_bucket=london_open`
- Raw: n=92  W=32/L=60  WR=34.8%
- Sharpen: sharpest is RSI=RSI5 (21/60 of losers there)
- **Sharp: n=22  W=1/L=21  WR=4.5%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; session=london_open  •  ONLY when RSI 60-70 strong

### L02.  `H60=H60e AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=87  W=32/L=55  WR=36.8%
- Sharpen: sharpest is T4=T4a (36/55 of losers there)
- **Sharp: n=37  W=1/L=36  WR=2.7%**
- **Dir: ?**  •  HTF60 strongly against; deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when 4h trend WITH trade

### L03.  `BBP=BBP0 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=87  W=32/L=55  WR=36.8%
- Sharpen: sharpest is T4=T4a (36/55 of losers there)
- **Sharp: n=37  W=1/L=36  WR=2.7%**
- **Dir: SHORT**  •  deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when 4h trend WITH trade

### L04.  `H60=H60e AND BBP=BBP0 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=87  W=32/L=55  WR=36.8%
- Sharpen: sharpest is T4=T4a (36/55 of losers there)
- **Sharp: n=37  W=1/L=36  WR=2.7%**
- **Dir: SHORT**  •  HTF60 strongly against; deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when 4h trend WITH trade

### L05.  `H20=H20a AND T1=T1c AND session_bucket=london_open`
- Raw: n=71  W=17/L=54  WR=23.9%
- Sharpen: sharpest is RSI=RSI5 (22/54 of losers there)
- **Sharp: n=23  W=1/L=22  WR=4.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; session=london_open  •  ONLY when RSI 60-70 strong

### L06.  `H60=H60e AND T1=T1c AND T4=T4c AND ZS=ZS5`
- Raw: n=71  W=28/L=43  WR=39.4%
- Sharpen: sharpest is session_bucket=london (15/43 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when session=london

### L07.  `T4=T4a AND BBP=BBP0 AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=68  W=24/L=44  WR=35.3%
- Sharpen: sharpest is T1=T1a (30/44 of losers there)
- **Sharp: n=33  W=3/L=30  WR=9.1%**
- **Dir: ?**  •  4h trend WITH trade; deep below lower band; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when 1h trend WITH trade

### L08.  `T1=T1a AND T4=T4a AND session_bucket=ny_close`
- Raw: n=64  W=25/L=39  WR=39.1%
- Sharpen: sharpest is BBP=BBP0 (12/39 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; session=ny_close  •  ONLY when deep below lower band

### L09.  `T1=T1a AND BBP=BBP3 AND RSI=RSI4`
- Raw: n=63  W=22/L=41  WR=34.9%
- Sharpen: sharpest is H20=H20d (11/41 of losers there)
- **Sharp: n=12  W=1/L=11  WR=8.3%**
- **Dir: ?**  •  1h trend WITH trade; middle of band; RSI 50-60 upper neutral  •  ONLY when HTF20 mildly against

### L10.  `T1=T1a AND BBP=BBP3 AND RSI=RSI4 AND ZS=ZS3`
- Raw: n=63  W=22/L=41  WR=34.9%
- Sharpen: sharpest is H20=H20d (11/41 of losers there)
- **Sharp: n=12  W=1/L=11  WR=8.3%**
- **Dir: ?**  •  1h trend WITH trade; middle of band; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  ONLY when HTF20 mildly against

### L11.  `H60=H60e AND T4=T4a AND ZS=ZS1`
- Raw: n=62  W=15/L=47  WR=24.2%
- Sharpen: sharpest is BBP=BBP0 (36/47 of losers there)
- **Sharp: n=37  W=1/L=36  WR=2.7%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  ONLY when deep below lower band

### L12.  `T4=T4a AND ZS=ZS1 AND direction_exec=short`
- Raw: n=62  W=15/L=47  WR=24.2%
- Sharpen: sharpest is BBP=BBP0 (36/47 of losers there)
- **Sharp: n=37  W=1/L=36  WR=2.7%**
- **Dir: SHORT**  •  4h trend WITH trade; zscore -3 to -2 deep oversold  •  ONLY when deep below lower band

### L13.  `H60=H60e AND T4=T4a AND ZS=ZS1 AND direction_exec=short`
- Raw: n=62  W=15/L=47  WR=24.2%
- Sharpen: sharpest is BBP=BBP0 (36/47 of losers there)
- **Sharp: n=37  W=1/L=36  WR=2.7%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  ONLY when deep below lower band

### L14.  `H60=H60e AND T1=T1a AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=62  W=21/L=41  WR=33.9%
- Sharpen: sharpest is T4=T4a (31/41 of losers there)
- **Sharp: n=32  W=1/L=31  WR=3.1%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when 4h trend WITH trade

### L15.  `T1=T1a AND BBP=BBP0 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=62  W=21/L=41  WR=33.9%
- Sharpen: sharpest is T4=T4a (31/41 of losers there)
- **Sharp: n=32  W=1/L=31  WR=3.1%**
- **Dir: SHORT**  •  1h trend WITH trade; deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when 4h trend WITH trade

### L16.  `T1=T1a AND BBP=BBP0 AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=62  W=23/L=39  WR=37.1%
- Sharpen: sharpest is T4=T4a (30/39 of losers there)
- **Sharp: n=33  W=3/L=30  WR=9.1%**
- **Dir: ?**  •  1h trend WITH trade; deep below lower band; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when 4h trend WITH trade

### L17.  `T1=T1a AND T4=T4a AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=61  W=16/L=45  WR=26.2%
- Sharpen: sharpest is H60=H60e (31/45 of losers there)
- **Sharp: n=34  W=3/L=31  WR=8.8%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  ONLY when HTF60 strongly against

### L18.  `T4=T4a AND RSI=RSI4 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=59  W=23/L=36  WR=39.0%
- Sharpen: sharpest is T1=T1a (21/36 of losers there)
- **Sharp: n=30  W=9/L=21  WR=30.0%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 50-60 upper neutral; session=ny_close  •  ONLY when 1h trend WITH trade

### L19.  `T1=T1a AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=58  W=22/L=36  WR=37.9%
- Sharpen: sharpest is BBP=BBP4 (21/36 of losers there)
- **Sharp: n=27  W=6/L=21  WR=22.2%**
- **Dir: LONG**  •  1h trend WITH trade; session=ny_close  •  ONLY when upper third

### L20.  `T1=T1a AND T4=T4a AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=57  W=17/L=40  WR=29.8%
- Sharpen: sharpest is H60=H60e (31/40 of losers there)
- **Sharp: n=32  W=1/L=31  WR=3.1%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when HTF60 strongly against

### L21.  `H20=H20a AND T1=T1a AND session_bucket=ny_close`
- Raw: n=56  W=18/L=38  WR=32.1%
- Sharpen: sharpest is H60=H60e (12/38 of losers there)
- **Sharp: n=13  W=1/L=12  WR=7.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=ny_close  •  ONLY when HTF60 strongly against

### L22.  `H60=H60e AND T1=T1c AND BBP=BBP6`
- Raw: n=55  W=17/L=38  WR=30.9%
- Sharpen: sharpest is RSI=RSI5 (21/38 of losers there)
- **Sharp: n=22  W=1/L=21  WR=4.5%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; deep above upper band  •  ONLY when RSI 60-70 strong

### L23.  `T1=T1c AND BBP=BBP6 AND direction_exec=short`
- Raw: n=55  W=17/L=38  WR=30.9%
- Sharpen: sharpest is RSI=RSI5 (21/38 of losers there)
- **Sharp: n=22  W=1/L=21  WR=4.5%**
- **Dir: SHORT**  •  1h trend AGAINST trade; deep above upper band  •  ONLY when RSI 60-70 strong

### L24.  `H60=H60e AND T1=T1c AND BBP=BBP6 AND direction_exec=short`
- Raw: n=55  W=17/L=38  WR=30.9%
- Sharpen: sharpest is RSI=RSI5 (21/38 of losers there)
- **Sharp: n=22  W=1/L=21  WR=4.5%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; deep above upper band  •  ONLY when RSI 60-70 strong

### L25.  `T1=T1a AND RSI=RSI4 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=55  W=20/L=35  WR=36.4%
- Sharpen: sharpest is ZS=ZS4 (17/35 of losers there)
- **Sharp: n=21  W=4/L=17  WR=19.0%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 50-60 upper neutral; session=ny_close  •  ONLY when zscore +1 to +2 overbought

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | H20a(41/47) |
| H60 | — | — |
| T1 | T1a(55/45) | T1c(45/55) |
| T4 | T4c(52/46) | T4a(48/54) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
