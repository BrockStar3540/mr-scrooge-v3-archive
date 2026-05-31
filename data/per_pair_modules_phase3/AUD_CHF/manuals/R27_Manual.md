# AUD_CHF — R27 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20d**  (EMA20 down 0.15-0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **999**  (W=657 / L=342)  -  WR: **65.8%**

## Session distribution

- ny_mid: n=338  W=228/L=110  WR=67.5%
- asia: n=263  W=170/L=93  WR=64.6%
- london_open: n=200  W=134/L=66  WR=67.0%
- london: n=100  W=59/L=41  WR=59.0%
- ny_open: n=76  W=54/L=22  WR=71.1%
- ny_close: n=18  W=12/L=6  WR=66.7%
- asia_late: n=3  W=0/L=3  WR=0.0%
- off_hours: n=1  W=0/L=1  WR=0.0%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60e AND T4=T4a AND session_bucket=london_open`
- Raw: n=74  W=66/L=8  WR=89.2%
- Refine: exclude H20=H20d drops 5/8 losers (62%)
- **Final: n=69  W=66/L=3  WR=95.7%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; session=london_open  •  AVOID when HTF20 mildly against

### W02.  `T1=T1a AND T4=T4a AND session_bucket=london_open`
- Raw: n=74  W=66/L=8  WR=89.2%
- Refine: exclude H20=H20d drops 5/8 losers (62%)
- **Final: n=69  W=66/L=3  WR=95.7%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; session=london_open  •  AVOID when HTF20 mildly against

### W03.  `T4=T4a AND direction_exec=short AND session_bucket=london_open`
- Raw: n=74  W=66/L=8  WR=89.2%
- Refine: exclude H20=H20d drops 5/8 losers (62%)
- **Final: n=69  W=66/L=3  WR=95.7%**
- **Dir: SHORT**  •  4h trend WITH trade; session=london_open  •  AVOID when HTF20 mildly against

### W04.  `H60=H60e AND T1=T1a AND T4=T4a AND session_bucket=london_open`
- Raw: n=74  W=66/L=8  WR=89.2%
- Refine: exclude H20=H20d drops 5/8 losers (62%)
- **Final: n=69  W=66/L=3  WR=95.7%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend WITH trade; session=london_open  •  AVOID when HTF20 mildly against

### W05.  `H60=H60e AND T4=T4a AND direction_exec=short AND session_bucket=london_open`
- Raw: n=74  W=66/L=8  WR=89.2%
- Refine: exclude H20=H20d drops 5/8 losers (62%)
- **Final: n=69  W=66/L=3  WR=95.7%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend WITH trade; session=london_open  •  AVOID when HTF20 mildly against

### W06.  `T1=T1a AND T4=T4a AND direction_exec=short AND session_bucket=london_open`
- Raw: n=74  W=66/L=8  WR=89.2%
- Refine: exclude H20=H20d drops 5/8 losers (62%)
- **Final: n=69  W=66/L=3  WR=95.7%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend WITH trade; session=london_open  •  AVOID when HTF20 mildly against

### W07.  `H20=H20e AND T4=T4a AND session_bucket=london_open`
- Raw: n=69  W=66/L=3  WR=95.7%
- Refine: exclude BBP=BBP4 drops 3/3 losers (100%)
- **Final: n=48  W=48/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; session=london_open  •  AVOID when upper third

### W08.  `H20=H20e AND H60=H60e AND T4=T4a AND session_bucket=london_open`
- Raw: n=69  W=66/L=3  WR=95.7%
- Refine: exclude BBP=BBP4 drops 3/3 losers (100%)
- **Final: n=48  W=48/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend WITH trade; session=london_open  •  AVOID when upper third

### W09.  `H20=H20e AND T1=T1a AND T4=T4a AND session_bucket=london_open`
- Raw: n=69  W=66/L=3  WR=95.7%
- Refine: exclude BBP=BBP4 drops 3/3 losers (100%)
- **Final: n=48  W=48/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend WITH trade; session=london_open  •  AVOID when upper third

### W10.  `H20=H20e AND T4=T4a AND direction_exec=short AND session_bucket=london_open`
- Raw: n=69  W=66/L=3  WR=95.7%
- Refine: exclude BBP=BBP4 drops 3/3 losers (100%)
- **Final: n=48  W=48/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend WITH trade; session=london_open  •  AVOID when upper third

### W11.  `ZS=ZS2 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=63  W=54/L=9  WR=85.7%
- Refine: exclude T4=T4c drops 9/9 losers (100%)
- **Final: n=20  W=20/L=0  WR=100.0%**
- **Dir: LONG**  •  zscore -2 to -1 oversold; session=ny_mid  •  AVOID when 4h trend AGAINST trade

### W12.  `BBP=BBP2 AND ZS=ZS2 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=63  W=54/L=9  WR=85.7%
- Refine: exclude T4=T4c drops 9/9 losers (100%)
- **Final: n=20  W=20/L=0  WR=100.0%**
- **Dir: LONG**  •  lower third; zscore -2 to -1 oversold; session=ny_mid  •  AVOID when 4h trend AGAINST trade

### W13.  `H60=H60a AND BBP=BBP2 AND session_bucket=ny_mid`
- Raw: n=62  W=54/L=8  WR=87.1%
- Refine: exclude ZS=ZS3 drops 3/8 losers (38%)
- **Final: n=55  W=50/L=5  WR=90.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; lower third; session=ny_mid  •  AVOID when zscore -1 to +1 neutral

### W14.  `H60=H60a AND BBP=BBP2 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=62  W=54/L=8  WR=87.1%
- Refine: exclude ZS=ZS3 drops 3/8 losers (38%)
- **Final: n=55  W=50/L=5  WR=90.9%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; lower third; session=ny_mid  •  AVOID when zscore -1 to +1 neutral

### W15.  `H20=H20a AND ZS=ZS2 AND session_bucket=ny_mid`
- Raw: n=61  W=52/L=9  WR=85.2%
- Refine: exclude T4=T4c drops 9/9 losers (100%)
- **Final: n=20  W=20/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; zscore -2 to -1 oversold; session=ny_mid  •  AVOID when 4h trend AGAINST trade

### W16.  `H20=H20a AND BBP=BBP2 AND ZS=ZS2 AND session_bucket=ny_mid`
- Raw: n=61  W=52/L=9  WR=85.2%
- Refine: exclude T4=T4c drops 9/9 losers (100%)
- **Final: n=20  W=20/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; lower third; zscore -2 to -1 oversold; session=ny_mid  •  AVOID when 4h trend AGAINST trade

### W17.  `H20=H20a AND ZS=ZS2 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=61  W=52/L=9  WR=85.2%
- Refine: exclude T4=T4c drops 9/9 losers (100%)
- **Final: n=20  W=20/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; zscore -2 to -1 oversold; session=ny_mid  •  AVOID when 4h trend AGAINST trade

### W18.  `H20=H20a AND H60=H60a AND BBP=BBP2 AND session_bucket=ny_mid`
- Raw: n=60  W=52/L=8  WR=86.7%
- Refine: exclude ZS=ZS3 drops 3/8 losers (38%)
- **Final: n=53  W=48/L=5  WR=90.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; lower third; session=ny_mid  •  AVOID when zscore -1 to +1 neutral

### W19.  `H60=H60a AND T1=T1c AND BBP=BBP2 AND session_bucket=ny_mid`
- Raw: n=56  W=48/L=8  WR=85.7%
- Refine: exclude ZS=ZS3 drops 3/8 losers (38%)
- **Final: n=49  W=44/L=5  WR=89.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; lower third; session=ny_mid  •  AVOID when zscore -1 to +1 neutral

### W20.  `H60=H60a AND ZS=ZS2 AND session_bucket=ny_mid`
- Raw: n=55  W=50/L=5  WR=90.9%
- Refine: exclude T4=T4c drops 5/5 losers (100%)
- **Final: n=20  W=20/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; zscore -2 to -1 oversold; session=ny_mid  •  AVOID when 4h trend AGAINST trade

### W21.  `H60=H60a AND BBP=BBP2 AND ZS=ZS2 AND session_bucket=ny_mid`
- Raw: n=55  W=50/L=5  WR=90.9%
- Refine: exclude T4=T4c drops 5/5 losers (100%)
- **Final: n=20  W=20/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; lower third; zscore -2 to -1 oversold; session=ny_mid  •  AVOID when 4h trend AGAINST trade

### W22.  `H60=H60a AND ZS=ZS2 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=55  W=50/L=5  WR=90.9%
- Refine: exclude T4=T4c drops 5/5 losers (100%)
- **Final: n=20  W=20/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; zscore -2 to -1 oversold; session=ny_mid  •  AVOID when 4h trend AGAINST trade

### W23.  `T1=T1a AND T4=T4a AND RSI=RSI3 AND ZS=ZS4`
- Raw: n=55  W=47/L=8  WR=85.5%
- Refine: exclude session_bucket=london drops 5/8 losers (62%)
- **Final: n=39  W=36/L=3  WR=92.3%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral; zscore +1 to +2 overbought  •  AVOID when session=london

### W24.  `H20=H20a AND H60=H60a AND ZS=ZS2 AND session_bucket=ny_mid`
- Raw: n=53  W=48/L=5  WR=90.6%
- Refine: exclude T4=T4c drops 5/5 losers (100%)
- **Final: n=20  W=20/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; zscore -2 to -1 oversold; session=ny_mid  •  AVOID when 4h trend AGAINST trade

### W25.  `T1=T1c AND BBP=BBP2 AND session_bucket=asia`
- Raw: n=53  W=47/L=6  WR=88.7%
- Refine: exclude RSI=RSI2 drops 6/6 losers (100%)
- **Final: n=37  W=37/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; lower third; session=asia  •  AVOID when RSI 30-40 weak

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T4=T4c AND BBP=BBP4 AND RSI=RSI3`
- Raw: n=69  W=27/L=42  WR=39.1%
- Sharpen: sharpest is session_bucket=london_open (14/42 of losers there)
- **Sharp: n=16  W=2/L=14  WR=12.5%**
- **Dir: ?**  •  4h trend AGAINST trade; upper third; RSI 40-50 lower neutral  •  ONLY when session=london_open

### L02.  `H20=H20e AND T4=T4c AND RSI=RSI3`
- Raw: n=56  W=22/L=34  WR=39.3%
- Sharpen: sharpest is session_bucket=london_open (9/34 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when session=london_open

### L03.  `H60=H60e AND T4=T4c AND RSI=RSI3`
- Raw: n=56  W=22/L=34  WR=39.3%
- Sharpen: sharpest is session_bucket=london_open (9/34 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when session=london_open

### L04.  `T4=T4c AND RSI=RSI3 AND direction_exec=short`
- Raw: n=56  W=22/L=34  WR=39.3%
- Sharpen: sharpest is session_bucket=london_open (9/34 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when session=london_open

### L05.  `H20=H20e AND H60=H60e AND T4=T4c AND RSI=RSI3`
- Raw: n=56  W=22/L=34  WR=39.3%
- Sharpen: sharpest is session_bucket=london_open (9/34 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when session=london_open

### L06.  `H20=H20e AND T1=T1a AND T4=T4c AND RSI=RSI3`
- Raw: n=56  W=22/L=34  WR=39.3%
- Sharpen: sharpest is session_bucket=london_open (9/34 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when session=london_open

### L07.  `H20=H20e AND T4=T4c AND RSI=RSI3 AND direction_exec=short`
- Raw: n=56  W=22/L=34  WR=39.3%
- Sharpen: sharpest is session_bucket=london_open (9/34 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when session=london_open

### L08.  `H60=H60e AND T1=T1a AND T4=T4c AND RSI=RSI3`
- Raw: n=56  W=22/L=34  WR=39.3%
- Sharpen: sharpest is session_bucket=london_open (9/34 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when session=london_open

### L09.  `H60=H60e AND T4=T4c AND RSI=RSI3 AND direction_exec=short`
- Raw: n=56  W=22/L=34  WR=39.3%
- Sharpen: sharpest is session_bucket=london_open (9/34 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when session=london_open

### L10.  `T1=T1a AND T4=T4c AND RSI=RSI3 AND direction_exec=short`
- Raw: n=56  W=22/L=34  WR=39.3%
- Sharpen: sharpest is session_bucket=london_open (9/34 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when session=london_open

### L11.  `T4=T4c AND RSI=RSI3 AND ZS=ZS4`
- Raw: n=52  W=18/L=34  WR=34.6%
- Sharpen: sharpest is session_bucket=london_open (11/34 of losers there)
- **Sharp: n=13  W=2/L=11  WR=15.4%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; zscore +1 to +2 overbought  •  ONLY when session=london_open

### L12.  `T4=T4c AND BBP=BBP4 AND RSI=RSI3 AND ZS=ZS4`
- Raw: n=52  W=18/L=34  WR=34.6%
- Sharpen: sharpest is session_bucket=london_open (11/34 of losers there)
- **Sharp: n=13  W=2/L=11  WR=15.4%**
- **Dir: ?**  •  4h trend AGAINST trade; upper third; RSI 40-50 lower neutral; zscore +1 to +2 overbought  •  ONLY when session=london_open

### L13.  `H60=H60a AND T4=T4c AND BBP=BBP4`
- Raw: n=52  W=19/L=33  WR=36.5%
- Sharpen: sharpest is session_bucket=ny_mid (8/33 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; upper third  •  ONLY when session=ny_mid

### L14.  `T1=T1c AND T4=T4c AND BBP=BBP4`
- Raw: n=52  W=19/L=33  WR=36.5%
- Sharpen: sharpest is session_bucket=ny_mid (8/33 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; upper third  •  ONLY when session=ny_mid

### L15.  `T4=T4c AND BBP=BBP4 AND direction_exec=long`
- Raw: n=52  W=19/L=33  WR=36.5%
- Sharpen: sharpest is session_bucket=ny_mid (8/33 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; upper third  •  ONLY when session=ny_mid

### L16.  `H60=H60a AND T1=T1c AND T4=T4c AND BBP=BBP4`
- Raw: n=52  W=19/L=33  WR=36.5%
- Sharpen: sharpest is session_bucket=ny_mid (8/33 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; upper third  •  ONLY when session=ny_mid

### L17.  `H60=H60a AND T4=T4c AND BBP=BBP4 AND direction_exec=long`
- Raw: n=52  W=19/L=33  WR=36.5%
- Sharpen: sharpest is session_bucket=ny_mid (8/33 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; upper third  •  ONLY when session=ny_mid

### L18.  `T1=T1c AND T4=T4c AND BBP=BBP4 AND direction_exec=long`
- Raw: n=52  W=19/L=33  WR=36.5%
- Sharpen: sharpest is session_bucket=ny_mid (8/33 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; upper third  •  ONLY when session=ny_mid

### L19.  `H20=H20a AND T4=T4c AND BBP=BBP4`
- Raw: n=51  W=19/L=32  WR=37.3%
- Sharpen: sharpest is session_bucket=ny_mid (8/32 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; upper third  •  ONLY when session=ny_mid

### L20.  `H20=H20a AND H60=H60a AND T4=T4c AND BBP=BBP4`
- Raw: n=51  W=19/L=32  WR=37.3%
- Sharpen: sharpest is session_bucket=ny_mid (8/32 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend AGAINST trade; upper third  •  ONLY when session=ny_mid

### L21.  `H20=H20a AND T1=T1c AND T4=T4c AND BBP=BBP4`
- Raw: n=51  W=19/L=32  WR=37.3%
- Sharpen: sharpest is session_bucket=ny_mid (8/32 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; upper third  •  ONLY when session=ny_mid

### L22.  `H20=H20a AND T4=T4c AND BBP=BBP4 AND direction_exec=long`
- Raw: n=51  W=19/L=32  WR=37.3%
- Sharpen: sharpest is session_bucket=ny_mid (8/32 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; upper third  •  ONLY when session=ny_mid

### L23.  `H60=H60a AND T4=T4c AND session_bucket=london_open`
- Raw: n=49  W=12/L=37  WR=24.5%
- Sharpen: sharpest is H20=H20a (37/37 of losers there)
- **Sharp: n=41  W=4/L=37  WR=9.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=london_open  •  ONLY when HTF20 aligned WITH trade

### L24.  `T1=T1c AND T4=T4c AND session_bucket=london_open`
- Raw: n=49  W=12/L=37  WR=24.5%
- Sharpen: sharpest is H20=H20a (37/37 of losers there)
- **Sharp: n=41  W=4/L=37  WR=9.8%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=london_open  •  ONLY when HTF20 aligned WITH trade

### L25.  `T4=T4c AND direction_exec=long AND session_bucket=london_open`
- Raw: n=49  W=12/L=37  WR=24.5%
- Sharpen: sharpest is H20=H20a (37/37 of losers there)
- **Sharp: n=41  W=4/L=37  WR=9.8%**
- **Dir: LONG**  •  4h trend AGAINST trade; session=london_open  •  ONLY when HTF20 aligned WITH trade

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(51/43) | H20e(44/52) |
| H60 | H60a(50/45) | — |
| T1 | — | — |
| T4 | — | — |
| BBP | — | — |
| RSI | — | RSI3(34/41) |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(52/46) | short(48/54) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
