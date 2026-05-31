# NZD_CAD — R39 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **1,309**  (W=843 / L=466)  -  WR: **64.4%**

## Session distribution

- asia: n=419  W=256/L=163  WR=61.1%
- ny_close: n=225  W=156/L=69  WR=69.3%
- london_open: n=160  W=100/L=60  WR=62.5%
- ny_open: n=159  W=113/L=46  WR=71.1%
- ny_mid: n=118  W=73/L=45  WR=61.9%
- asia_late: n=92  W=60/L=32  WR=65.2%
- london: n=70  W=43/L=27  WR=61.4%
- off_hours: n=66  W=42/L=24  WR=63.6%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T4=T4c AND direction_exec=long AND session_bucket=london_open`
- Raw: n=88  W=75/L=13  WR=85.2%
- Refine: exclude T1=T1c drops 13/13 losers (100%)
- **Final: n=25  W=25/L=0  WR=100.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; session=london_open  •  AVOID when 1h trend AGAINST trade

### W02.  `H60=H60e AND T4=T4c AND session_bucket=london_open`
- Raw: n=80  W=68/L=12  WR=85.0%
- Refine: exclude T1=T1c drops 12/12 losers (100%)
- **Final: n=25  W=25/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; session=london_open  •  AVOID when 1h trend AGAINST trade

### W03.  `H60=H60e AND direction_exec=long AND session_bucket=london_open`
- Raw: n=80  W=68/L=12  WR=85.0%
- Refine: exclude T1=T1c drops 12/12 losers (100%)
- **Final: n=25  W=25/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 strongly against; session=london_open  •  AVOID when 1h trend AGAINST trade

### W04.  `H60=H60e AND T4=T4c AND direction_exec=long AND session_bucket=london_open`
- Raw: n=80  W=68/L=12  WR=85.0%
- Refine: exclude T1=T1c drops 12/12 losers (100%)
- **Final: n=25  W=25/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend AGAINST trade; session=london_open  •  AVOID when 1h trend AGAINST trade

### W05.  `H20=H20e AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=62  W=53/L=9  WR=85.5%
- Refine: exclude T4=T4c drops 9/9 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  AVOID when 4h trend AGAINST trade

### W06.  `H20=H20c AND T1=T1a AND RSI=RSI1`
- Raw: n=59  W=52/L=7  WR=88.1%
- Refine: exclude ZS=ZS3 drops 4/7 losers (57%)
- **Final: n=51  W=48/L=3  WR=94.1%**
- **Dir: ?**  •  HTF20 neutral; 1h trend WITH trade; RSI 20-30 oversold  •  AVOID when zscore -1 to +1 neutral

### W07.  `H20=H20c AND RSI=RSI1 AND direction_exec=short`
- Raw: n=59  W=52/L=7  WR=88.1%
- Refine: exclude ZS=ZS3 drops 4/7 losers (57%)
- **Final: n=51  W=48/L=3  WR=94.1%**
- **Dir: SHORT**  •  HTF20 neutral; RSI 20-30 oversold  •  AVOID when zscore -1 to +1 neutral

### W08.  `H20=H20c AND T1=T1a AND RSI=RSI1 AND direction_exec=short`
- Raw: n=59  W=52/L=7  WR=88.1%
- Refine: exclude ZS=ZS3 drops 4/7 losers (57%)
- **Final: n=51  W=48/L=3  WR=94.1%**
- **Dir: SHORT**  •  HTF20 neutral; 1h trend WITH trade; RSI 20-30 oversold  •  AVOID when zscore -1 to +1 neutral

### W09.  `H20=H20c AND H60=H60a AND RSI=RSI1`
- Raw: n=56  W=52/L=4  WR=92.9%
- Refine: exclude ZS=ZS3 drops 4/4 losers (100%)
- **Final: n=48  W=48/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 neutral; HTF60 aligned WITH trade; RSI 20-30 oversold  •  AVOID when zscore -1 to +1 neutral

### W10.  `H20=H20c AND H60=H60a AND T1=T1a AND RSI=RSI1`
- Raw: n=56  W=52/L=4  WR=92.9%
- Refine: exclude ZS=ZS3 drops 4/4 losers (100%)
- **Final: n=48  W=48/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 neutral; HTF60 aligned WITH trade; 1h trend WITH trade; RSI 20-30 oversold  •  AVOID when zscore -1 to +1 neutral

### W11.  `H20=H20c AND H60=H60a AND RSI=RSI1 AND direction_exec=short`
- Raw: n=56  W=52/L=4  WR=92.9%
- Refine: exclude ZS=ZS3 drops 4/4 losers (100%)
- **Final: n=48  W=48/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 neutral; HTF60 aligned WITH trade; RSI 20-30 oversold  •  AVOID when zscore -1 to +1 neutral

### W12.  `H20=H20c AND T4=T4c AND BBP=BBP2`
- Raw: n=56  W=48/L=8  WR=85.7%
- Refine: exclude H60=H60e drops 8/8 losers (100%)
- **Final: n=26  W=26/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 neutral; 4h trend AGAINST trade; lower third  •  AVOID when HTF60 strongly against

### W13.  `H20=H20c AND T4=T4c AND RSI=RSI2`
- Raw: n=50  W=47/L=3  WR=94.0%
- Refine: exclude ZS=ZS2 drops 3/3 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 neutral; 4h trend AGAINST trade; RSI 30-40 weak  •  AVOID when zscore -2 to -1 oversold

### W14.  `H20=H20b AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=49  W=47/L=2  WR=95.9%
- Refine: exclude RSI=RSI2 drops 2/2 losers (100%)
- **Final: n=33  W=33/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 slightly aligned; upper third; zscore +1 to +2 overbought  •  AVOID when RSI 30-40 weak

### W15.  `H20=H20e AND RSI=RSI2 AND session_bucket=ny_close`
- Raw: n=49  W=42/L=7  WR=85.7%
- Refine: exclude H60=H60a drops 6/7 losers (86%)
- **Final: n=28  W=27/L=1  WR=96.4%**
- **Dir: ?**  •  HTF20 strongly against; RSI 30-40 weak; session=ny_close  •  AVOID when HTF60 aligned WITH trade

### W16.  `H20=H20e AND T4=T4a AND session_bucket=ny_close`
- Raw: n=47  W=41/L=6  WR=87.2%
- Refine: exclude H60=H60a drops 6/6 losers (100%)
- **Final: n=26  W=26/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; session=ny_close  •  AVOID when HTF60 aligned WITH trade

### W17.  `H20=H20b AND H60=H60a AND T4=T4a`
- Raw: n=47  W=40/L=7  WR=85.1%
- Refine: exclude RSI=RSI2 drops 4/7 losers (57%)
- **Final: n=39  W=36/L=3  WR=92.3%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 4h trend WITH trade  •  AVOID when RSI 30-40 weak

### W18.  `H20=H20b AND T1=T1a AND T4=T4a`
- Raw: n=47  W=40/L=7  WR=85.1%
- Refine: exclude RSI=RSI2 drops 4/7 losers (57%)
- **Final: n=39  W=36/L=3  WR=92.3%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when RSI 30-40 weak

### W19.  `H20=H20b AND T4=T4a AND direction_exec=short`
- Raw: n=47  W=40/L=7  WR=85.1%
- Refine: exclude RSI=RSI2 drops 4/7 losers (57%)
- **Final: n=39  W=36/L=3  WR=92.3%**
- **Dir: SHORT**  •  HTF20 slightly aligned; 4h trend WITH trade  •  AVOID when RSI 30-40 weak

### W20.  `H20=H20b AND H60=H60a AND T1=T1a AND T4=T4a`
- Raw: n=47  W=40/L=7  WR=85.1%
- Refine: exclude RSI=RSI2 drops 4/7 losers (57%)
- **Final: n=39  W=36/L=3  WR=92.3%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when RSI 30-40 weak

### W21.  `H20=H20b AND H60=H60a AND T4=T4a AND direction_exec=short`
- Raw: n=47  W=40/L=7  WR=85.1%
- Refine: exclude RSI=RSI2 drops 4/7 losers (57%)
- **Final: n=39  W=36/L=3  WR=92.3%**
- **Dir: SHORT**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 4h trend WITH trade  •  AVOID when RSI 30-40 weak

### W22.  `H20=H20b AND T1=T1a AND T4=T4a AND direction_exec=short`
- Raw: n=47  W=40/L=7  WR=85.1%
- Refine: exclude RSI=RSI2 drops 4/7 losers (57%)
- **Final: n=39  W=36/L=3  WR=92.3%**
- **Dir: SHORT**  •  HTF20 slightly aligned; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when RSI 30-40 weak

### W23.  `H20=H20c AND T1=T1c AND RSI=RSI2`
- Raw: n=46  W=41/L=5  WR=89.1%
- Refine: exclude ZS=ZS2 drops 4/5 losers (80%)
- **Final: n=27  W=26/L=1  WR=96.3%**
- **Dir: ?**  •  HTF20 neutral; 1h trend AGAINST trade; RSI 30-40 weak  •  AVOID when zscore -2 to -1 oversold

### W24.  `H20=H20c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=46  W=41/L=5  WR=89.1%
- Refine: exclude ZS=ZS2 drops 4/5 losers (80%)
- **Final: n=27  W=26/L=1  WR=96.3%**
- **Dir: LONG**  •  HTF20 neutral; RSI 30-40 weak  •  AVOID when zscore -2 to -1 oversold

### W25.  `H20=H20c AND T1=T1c AND RSI=RSI2 AND direction_exec=long`
- Raw: n=46  W=41/L=5  WR=89.1%
- Refine: exclude ZS=ZS2 drops 4/5 losers (80%)
- **Final: n=27  W=26/L=1  WR=96.3%**
- **Dir: LONG**  •  HTF20 neutral; 1h trend AGAINST trade; RSI 30-40 weak  •  AVOID when zscore -2 to -1 oversold

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T4=T4a AND direction_exec=short AND session_bucket=london_open`
- Raw: n=69  W=23/L=46  WR=33.3%
- Sharpen: sharpest is RSI=RSI4 (18/46 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: SHORT**  •  4h trend WITH trade; session=london_open  •  ONLY when RSI 50-60 upper neutral

### L02.  `T1=T1c AND RSI=RSI1 AND session_bucket=asia`
- Raw: n=61  W=22/L=39  WR=36.1%
- Sharpen: sharpest is H20=H20e (21/39 of losers there)
- **Sharp: n=23  W=2/L=21  WR=8.7%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 20-30 oversold; session=asia  •  ONLY when HTF20 strongly against

### L03.  `T4=T4c AND RSI=RSI1 AND session_bucket=asia`
- Raw: n=61  W=22/L=39  WR=36.1%
- Sharpen: sharpest is H20=H20e (21/39 of losers there)
- **Sharp: n=23  W=2/L=21  WR=8.7%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 20-30 oversold; session=asia  •  ONLY when HTF20 strongly against

### L04.  `RSI=RSI1 AND direction_exec=long AND session_bucket=asia`
- Raw: n=61  W=22/L=39  WR=36.1%
- Sharpen: sharpest is H20=H20e (21/39 of losers there)
- **Sharp: n=23  W=2/L=21  WR=8.7%**
- **Dir: LONG**  •  RSI 20-30 oversold; session=asia  •  ONLY when HTF20 strongly against

### L05.  `T1=T1c AND T4=T4c AND RSI=RSI1 AND session_bucket=asia`
- Raw: n=61  W=22/L=39  WR=36.1%
- Sharpen: sharpest is H20=H20e (21/39 of losers there)
- **Sharp: n=23  W=2/L=21  WR=8.7%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 20-30 oversold; session=asia  •  ONLY when HTF20 strongly against

### L06.  `T1=T1c AND RSI=RSI1 AND direction_exec=long AND session_bucket=asia`
- Raw: n=61  W=22/L=39  WR=36.1%
- Sharpen: sharpest is H20=H20e (21/39 of losers there)
- **Sharp: n=23  W=2/L=21  WR=8.7%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 20-30 oversold; session=asia  •  ONLY when HTF20 strongly against

### L07.  `T4=T4c AND RSI=RSI1 AND direction_exec=long AND session_bucket=asia`
- Raw: n=61  W=22/L=39  WR=36.1%
- Sharpen: sharpest is H20=H20e (21/39 of losers there)
- **Sharp: n=23  W=2/L=21  WR=8.7%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 20-30 oversold; session=asia  •  ONLY when HTF20 strongly against

### L08.  `H60=H60a AND T4=T4a AND session_bucket=london_open`
- Raw: n=55  W=21/L=34  WR=38.2%
- Sharpen: sharpest is RSI=RSI4 (18/34 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; session=london_open  •  ONLY when RSI 50-60 upper neutral

### L09.  `H60=H60a AND direction_exec=short AND session_bucket=london_open`
- Raw: n=55  W=21/L=34  WR=38.2%
- Sharpen: sharpest is RSI=RSI4 (18/34 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; session=london_open  •  ONLY when RSI 50-60 upper neutral

### L10.  `H60=H60a AND T4=T4a AND direction_exec=short AND session_bucket=london_open`
- Raw: n=55  W=21/L=34  WR=38.2%
- Sharpen: sharpest is RSI=RSI4 (18/34 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend WITH trade; session=london_open  •  ONLY when RSI 50-60 upper neutral

### L11.  `H20=H20a AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=48  W=15/L=33  WR=31.2%
- Sharpen: sharpest is T1=T1c (18/33 of losers there)
- **Sharp: n=20  W=2/L=18  WR=10.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when 1h trend AGAINST trade

### L12.  `T4=T4a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=46  W=17/L=29  WR=37.0%
- Sharpen: sharpest is BBP=BBP2 (10/29 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when lower third

### L13.  `H60=H60a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=45  W=17/L=28  WR=37.8%
- Sharpen: sharpest is BBP=BBP2 (9/28 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral  •  ONLY when lower third

### L14.  `H60=H60a AND T4=T4a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=45  W=17/L=28  WR=37.8%
- Sharpen: sharpest is BBP=BBP2 (9/28 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when lower third

### L15.  `H20=H20a AND T4=T4c AND ZS=ZS1`
- Raw: n=44  W=16/L=28  WR=36.4%
- Sharpen: sharpest is RSI=RSI2 (23/28 of losers there)
- **Sharp: n=32  W=9/L=23  WR=28.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when RSI 30-40 weak

### L16.  `T1=T1a AND T4=T4a AND RSI=RSI3`
- Raw: n=43  W=17/L=26  WR=39.5%
- Sharpen: sharpest is BBP=BBP2 (10/26 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when lower third

### L17.  `T1=T1a AND T4=T4a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=43  W=17/L=26  WR=39.5%
- Sharpen: sharpest is BBP=BBP2 (10/26 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when lower third

### L18.  `H20=H20e AND H60=H60d AND session_bucket=asia`
- Raw: n=42  W=13/L=29  WR=31.0%
- Sharpen: sharpest is RSI=RSI1 (17/29 of losers there)
- **Sharp: n=19  W=2/L=17  WR=10.5%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 mildly against; session=asia  •  ONLY when RSI 20-30 oversold

### L19.  `H60=H60d AND T1=T1c AND session_bucket=asia`
- Raw: n=42  W=13/L=29  WR=31.0%
- Sharpen: sharpest is RSI=RSI1 (17/29 of losers there)
- **Sharp: n=19  W=2/L=17  WR=10.5%**
- **Dir: ?**  •  HTF60 mildly against; 1h trend AGAINST trade; session=asia  •  ONLY when RSI 20-30 oversold

### L20.  `H60=H60d AND T4=T4c AND session_bucket=asia`
- Raw: n=42  W=13/L=29  WR=31.0%
- Sharpen: sharpest is RSI=RSI1 (17/29 of losers there)
- **Sharp: n=19  W=2/L=17  WR=10.5%**
- **Dir: ?**  •  HTF60 mildly against; 4h trend AGAINST trade; session=asia  •  ONLY when RSI 20-30 oversold

### L21.  `H60=H60d AND direction_exec=long AND session_bucket=asia`
- Raw: n=42  W=13/L=29  WR=31.0%
- Sharpen: sharpest is RSI=RSI1 (17/29 of losers there)
- **Sharp: n=19  W=2/L=17  WR=10.5%**
- **Dir: LONG**  •  HTF60 mildly against; session=asia  •  ONLY when RSI 20-30 oversold

### L22.  `H20=H20e AND H60=H60d AND T1=T1c AND session_bucket=asia`
- Raw: n=42  W=13/L=29  WR=31.0%
- Sharpen: sharpest is RSI=RSI1 (17/29 of losers there)
- **Sharp: n=19  W=2/L=17  WR=10.5%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 mildly against; 1h trend AGAINST trade; session=asia  •  ONLY when RSI 20-30 oversold

### L23.  `H20=H20e AND H60=H60d AND T4=T4c AND session_bucket=asia`
- Raw: n=42  W=13/L=29  WR=31.0%
- Sharpen: sharpest is RSI=RSI1 (17/29 of losers there)
- **Sharp: n=19  W=2/L=17  WR=10.5%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 mildly against; 4h trend AGAINST trade; session=asia  •  ONLY when RSI 20-30 oversold

### L24.  `H20=H20e AND H60=H60d AND direction_exec=long AND session_bucket=asia`
- Raw: n=42  W=13/L=29  WR=31.0%
- Sharpen: sharpest is RSI=RSI1 (17/29 of losers there)
- **Sharp: n=19  W=2/L=17  WR=10.5%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 mildly against; session=asia  •  ONLY when RSI 20-30 oversold

### L25.  `H60=H60d AND T1=T1c AND T4=T4c AND session_bucket=asia`
- Raw: n=42  W=13/L=29  WR=31.0%
- Sharpen: sharpest is RSI=RSI1 (17/29 of losers there)
- **Sharp: n=19  W=2/L=17  WR=10.5%**
- **Dir: ?**  •  HTF60 mildly against; 1h trend AGAINST trade; 4h trend AGAINST trade; session=asia  •  ONLY when RSI 20-30 oversold

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20b(15/7) | H20d(8/14) |
| H60 | — | — |
| T1 | — | — |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(53/46) | short(47/54) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
