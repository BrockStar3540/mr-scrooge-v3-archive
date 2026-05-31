# AUD_NZD — R35 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20d**  (EMA20 down 0.15-0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR3**  (60-90%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **1,342**  (W=834 / L=508)  -  WR: **62.1%**

## Session distribution

- asia: n=429  W=270/L=159  WR=62.9%
- ny_mid: n=258  W=163/L=95  WR=63.2%
- ny_close: n=171  W=104/L=67  WR=60.8%
- off_hours: n=134  W=78/L=56  WR=58.2%
- london_open: n=121  W=74/L=47  WR=61.2%
- london: n=109  W=68/L=41  WR=62.4%
- ny_open: n=90  W=57/L=33  WR=63.3%
- asia_late: n=30  W=20/L=10  WR=66.7%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND H60=H60a AND T4=T4a`
- Raw: n=75  W=65/L=10  WR=86.7%
- Refine: exclude RSI=RSI2 drops 10/10 losers (100%)
- **Final: n=41  W=41/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade  •  AVOID when RSI 30-40 weak

### W02.  `H20=H20a AND T4=T4a AND direction_exec=long`
- Raw: n=75  W=65/L=10  WR=86.7%
- Refine: exclude RSI=RSI2 drops 10/10 losers (100%)
- **Final: n=41  W=41/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend WITH trade  •  AVOID when RSI 30-40 weak

### W03.  `H20=H20a AND H60=H60a AND T4=T4a AND direction_exec=long`
- Raw: n=75  W=65/L=10  WR=86.7%
- Refine: exclude RSI=RSI2 drops 10/10 losers (100%)
- **Final: n=41  W=41/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade  •  AVOID when RSI 30-40 weak

### W04.  `H20=H20a AND T1=T1c AND T4=T4a`
- Raw: n=69  W=59/L=10  WR=85.5%
- Refine: exclude RSI=RSI2 drops 10/10 losers (100%)
- **Final: n=35  W=35/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade  •  AVOID when RSI 30-40 weak

### W05.  `H20=H20a AND H60=H60a AND T1=T1c AND T4=T4a`
- Raw: n=69  W=59/L=10  WR=85.5%
- Refine: exclude RSI=RSI2 drops 10/10 losers (100%)
- **Final: n=35  W=35/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade  •  AVOID when RSI 30-40 weak

### W06.  `H20=H20a AND T1=T1c AND T4=T4a AND direction_exec=long`
- Raw: n=69  W=59/L=10  WR=85.5%
- Refine: exclude RSI=RSI2 drops 10/10 losers (100%)
- **Final: n=35  W=35/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade  •  AVOID when RSI 30-40 weak

### W07.  `T1=T1a AND T4=T4a AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=67  W=57/L=10  WR=85.1%
- Refine: exclude BBP=BBP0 drops 8/10 losers (80%)
- **Final: n=40  W=38/L=2  WR=95.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; zscore -3 to -2 deep oversold; session=asia  •  AVOID when deep below lower band

### W08.  `H60=H60e AND T4=T4a AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=55  W=48/L=7  WR=87.3%
- Refine: exclude H20=H20d drops 5/7 losers (71%)
- **Final: n=42  W=40/L=2  WR=95.2%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; zscore -3 to -2 deep oversold; session=asia  •  AVOID when HTF20 mildly against

### W09.  `T4=T4a AND ZS=ZS1 AND direction_exec=short AND session_bucket=asia`
- Raw: n=55  W=48/L=7  WR=87.3%
- Refine: exclude H20=H20d drops 5/7 losers (71%)
- **Final: n=42  W=40/L=2  WR=95.2%**
- **Dir: SHORT**  •  4h trend WITH trade; zscore -3 to -2 deep oversold; session=asia  •  AVOID when HTF20 mildly against

### W10.  `T1=T1c AND T4=T4a AND session_bucket=asia`
- Raw: n=55  W=47/L=8  WR=85.5%
- Refine: exclude H20=H20d drops 8/8 losers (100%)
- **Final: n=29  W=29/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; session=asia  •  AVOID when HTF20 mildly against

### W11.  `H60=H60a AND T1=T1c AND T4=T4a AND session_bucket=asia`
- Raw: n=55  W=47/L=8  WR=85.5%
- Refine: exclude H20=H20d drops 8/8 losers (100%)
- **Final: n=29  W=29/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; session=asia  •  AVOID when HTF20 mildly against

### W12.  `T1=T1c AND T4=T4a AND direction_exec=long AND session_bucket=asia`
- Raw: n=55  W=47/L=8  WR=85.5%
- Refine: exclude H20=H20d drops 8/8 losers (100%)
- **Final: n=29  W=29/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend WITH trade; session=asia  •  AVOID when HTF20 mildly against

### W13.  `H60=H60a AND T1=T1c AND session_bucket=ny_open`
- Raw: n=51  W=44/L=7  WR=86.3%
- Refine: exclude ZS=ZS3 drops 6/7 losers (86%)
- **Final: n=33  W=32/L=1  WR=97.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=ny_open  •  AVOID when zscore -1 to +1 neutral

### W14.  `H60=H60a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=51  W=44/L=7  WR=86.3%
- Refine: exclude ZS=ZS3 drops 6/7 losers (86%)
- **Final: n=33  W=32/L=1  WR=97.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; session=ny_open  •  AVOID when zscore -1 to +1 neutral

### W15.  `T1=T1c AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=51  W=44/L=7  WR=86.3%
- Refine: exclude ZS=ZS3 drops 6/7 losers (86%)
- **Final: n=33  W=32/L=1  WR=97.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; session=ny_open  •  AVOID when zscore -1 to +1 neutral

### W16.  `H60=H60a AND T1=T1c AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=51  W=44/L=7  WR=86.3%
- Refine: exclude ZS=ZS3 drops 6/7 losers (86%)
- **Final: n=33  W=32/L=1  WR=97.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=ny_open  •  AVOID when zscore -1 to +1 neutral

### W17.  `H20=H20e AND H60=H60e AND session_bucket=london_open`
- Raw: n=49  W=45/L=4  WR=91.8%
- Refine: exclude BBP=BBP2 drops 3/4 losers (75%)
- **Final: n=33  W=32/L=1  WR=97.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; session=london_open  •  AVOID when lower third

### W18.  `H20=H20e AND T1=T1a AND session_bucket=london_open`
- Raw: n=49  W=45/L=4  WR=91.8%
- Refine: exclude BBP=BBP2 drops 3/4 losers (75%)
- **Final: n=33  W=32/L=1  WR=97.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; session=london_open  •  AVOID when lower third

### W19.  `H20=H20e AND T4=T4a AND session_bucket=london_open`
- Raw: n=49  W=45/L=4  WR=91.8%
- Refine: exclude BBP=BBP2 drops 3/4 losers (75%)
- **Final: n=33  W=32/L=1  WR=97.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; session=london_open  •  AVOID when lower third

### W20.  `H20=H20e AND direction_exec=short AND session_bucket=london_open`
- Raw: n=49  W=45/L=4  WR=91.8%
- Refine: exclude BBP=BBP2 drops 3/4 losers (75%)
- **Final: n=33  W=32/L=1  WR=97.0%**
- **Dir: SHORT**  •  HTF20 strongly against; session=london_open  •  AVOID when lower third

### W21.  `H20=H20e AND H60=H60e AND T1=T1a AND session_bucket=london_open`
- Raw: n=49  W=45/L=4  WR=91.8%
- Refine: exclude BBP=BBP2 drops 3/4 losers (75%)
- **Final: n=33  W=32/L=1  WR=97.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend WITH trade; session=london_open  •  AVOID when lower third

### W22.  `H20=H20e AND H60=H60e AND T4=T4a AND session_bucket=london_open`
- Raw: n=49  W=45/L=4  WR=91.8%
- Refine: exclude BBP=BBP2 drops 3/4 losers (75%)
- **Final: n=33  W=32/L=1  WR=97.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend WITH trade; session=london_open  •  AVOID when lower third

### W23.  `H20=H20e AND H60=H60e AND direction_exec=short AND session_bucket=london_open`
- Raw: n=49  W=45/L=4  WR=91.8%
- Refine: exclude BBP=BBP2 drops 3/4 losers (75%)
- **Final: n=33  W=32/L=1  WR=97.0%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; session=london_open  •  AVOID when lower third

### W24.  `H20=H20e AND T1=T1a AND T4=T4a AND session_bucket=london_open`
- Raw: n=49  W=45/L=4  WR=91.8%
- Refine: exclude BBP=BBP2 drops 3/4 losers (75%)
- **Final: n=33  W=32/L=1  WR=97.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend WITH trade; session=london_open  •  AVOID when lower third

### W25.  `H20=H20e AND T1=T1a AND direction_exec=short AND session_bucket=london_open`
- Raw: n=49  W=45/L=4  WR=91.8%
- Refine: exclude BBP=BBP2 drops 3/4 losers (75%)
- **Final: n=33  W=32/L=1  WR=97.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend WITH trade; session=london_open  •  AVOID when lower third

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20d AND H60=H60a AND T4=T4c`
- Raw: n=65  W=22/L=43  WR=33.8%
- Sharpen: sharpest is session_bucket=asia (18/43 of losers there)
- **Sharp: n=21  W=3/L=18  WR=14.3%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 aligned WITH trade; 4h trend AGAINST trade  •  ONLY when session=asia

### L02.  `H20=H20d AND T1=T1c AND T4=T4c`
- Raw: n=65  W=22/L=43  WR=33.8%
- Sharpen: sharpest is session_bucket=asia (18/43 of losers there)
- **Sharp: n=21  W=3/L=18  WR=14.3%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when session=asia

### L03.  `H20=H20d AND T4=T4c AND direction_exec=long`
- Raw: n=65  W=22/L=43  WR=33.8%
- Sharpen: sharpest is session_bucket=asia (18/43 of losers there)
- **Sharp: n=21  W=3/L=18  WR=14.3%**
- **Dir: LONG**  •  HTF20 mildly against; 4h trend AGAINST trade  •  ONLY when session=asia

### L04.  `H20=H20d AND H60=H60a AND T1=T1c AND T4=T4c`
- Raw: n=65  W=22/L=43  WR=33.8%
- Sharpen: sharpest is session_bucket=asia (18/43 of losers there)
- **Sharp: n=21  W=3/L=18  WR=14.3%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when session=asia

### L05.  `H20=H20d AND H60=H60a AND T4=T4c AND direction_exec=long`
- Raw: n=65  W=22/L=43  WR=33.8%
- Sharpen: sharpest is session_bucket=asia (18/43 of losers there)
- **Sharp: n=21  W=3/L=18  WR=14.3%**
- **Dir: LONG**  •  HTF20 mildly against; HTF60 aligned WITH trade; 4h trend AGAINST trade  •  ONLY when session=asia

### L06.  `H20=H20d AND T1=T1c AND T4=T4c AND direction_exec=long`
- Raw: n=65  W=22/L=43  WR=33.8%
- Sharpen: sharpest is session_bucket=asia (18/43 of losers there)
- **Sharp: n=21  W=3/L=18  WR=14.3%**
- **Dir: LONG**  •  HTF20 mildly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when session=asia

### L07.  `T4=T4c AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=56  W=18/L=38  WR=32.1%
- Sharpen: sharpest is BBP=BBP1 (24/38 of losers there)
- **Sharp: n=29  W=5/L=24  WR=17.2%**
- **Dir: ?**  •  4h trend AGAINST trade; zscore -3 to -2 deep oversold; session=asia  •  ONLY when just touched lower band

### L08.  `H20=H20d AND T4=T4c AND RSI=RSI3`
- Raw: n=53  W=21/L=32  WR=39.6%
- Sharpen: sharpest is ZS=ZS2 (12/32 of losers there)
- **Sharp: n=14  W=2/L=12  WR=14.3%**
- **Dir: ?**  •  HTF20 mildly against; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when zscore -2 to -1 oversold

### L09.  `H20=H20d AND H60=H60a AND T4=T4c AND RSI=RSI3`
- Raw: n=53  W=21/L=32  WR=39.6%
- Sharpen: sharpest is ZS=ZS2 (12/32 of losers there)
- **Sharp: n=14  W=2/L=12  WR=14.3%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when zscore -2 to -1 oversold

### L10.  `H20=H20d AND T1=T1c AND T4=T4c AND RSI=RSI3`
- Raw: n=53  W=21/L=32  WR=39.6%
- Sharpen: sharpest is ZS=ZS2 (12/32 of losers there)
- **Sharp: n=14  W=2/L=12  WR=14.3%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when zscore -2 to -1 oversold

### L11.  `H20=H20d AND T4=T4c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=53  W=21/L=32  WR=39.6%
- Sharpen: sharpest is ZS=ZS2 (12/32 of losers there)
- **Sharp: n=14  W=2/L=12  WR=14.3%**
- **Dir: LONG**  •  HTF20 mildly against; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when zscore -2 to -1 oversold

### L12.  `H60=H60e AND T4=T4c AND session_bucket=asia`
- Raw: n=51  W=16/L=35  WR=31.4%
- Sharpen: sharpest is H20=H20e (18/35 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; session=asia  •  ONLY when HTF20 strongly against

### L13.  `T4=T4c AND direction_exec=short AND session_bucket=asia`
- Raw: n=51  W=16/L=35  WR=31.4%
- Sharpen: sharpest is H20=H20e (18/35 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; session=asia  •  ONLY when HTF20 strongly against

### L14.  `H60=H60e AND T4=T4c AND direction_exec=short AND session_bucket=asia`
- Raw: n=51  W=16/L=35  WR=31.4%
- Sharpen: sharpest is H20=H20e (18/35 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend AGAINST trade; session=asia  •  ONLY when HTF20 strongly against

### L15.  `T1=T1a AND T4=T4c AND RSI=RSI3`
- Raw: n=50  W=20/L=30  WR=40.0%
- Sharpen: sharpest is H20=H20e (14/30 of losers there)
- **Sharp: n=17  W=3/L=14  WR=17.6%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when HTF20 strongly against

### L16.  `H60=H60e AND T1=T1a AND T4=T4c AND RSI=RSI3`
- Raw: n=50  W=20/L=30  WR=40.0%
- Sharpen: sharpest is H20=H20e (14/30 of losers there)
- **Sharp: n=17  W=3/L=14  WR=17.6%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when HTF20 strongly against

### L17.  `T1=T1a AND T4=T4c AND RSI=RSI3 AND direction_exec=short`
- Raw: n=50  W=20/L=30  WR=40.0%
- Sharpen: sharpest is H20=H20e (14/30 of losers there)
- **Sharp: n=17  W=3/L=14  WR=17.6%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when HTF20 strongly against

### L18.  `T4=T4c AND BBP=BBP0 AND session_bucket=asia`
- Raw: n=46  W=18/L=28  WR=39.1%
- Sharpen: sharpest is H60=H60e (13/28 of losers there)
- **Sharp: n=16  W=3/L=13  WR=18.8%**
- **Dir: ?**  •  4h trend AGAINST trade; deep below lower band; session=asia  •  ONLY when HTF60 strongly against

### L19.  `T1=T1c AND T4=T4c AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=44  W=15/L=29  WR=34.1%
- Sharpen: sharpest is BBP=BBP1 (20/29 of losers there)
- **Sharp: n=25  W=5/L=20  WR=20.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold; session=asia  •  ONLY when just touched lower band

### L20.  `H20=H20a AND H60=H60a AND session_bucket=london_open`
- Raw: n=41  W=16/L=25  WR=39.0%
- Sharpen: sharpest is BBP=BBP0 (8/25 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=london_open  •  ONLY when deep below lower band

### L21.  `H20=H20a AND T1=T1c AND session_bucket=london_open`
- Raw: n=41  W=16/L=25  WR=39.0%
- Sharpen: sharpest is BBP=BBP0 (8/25 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; session=london_open  •  ONLY when deep below lower band

### L22.  `H20=H20a AND T4=T4c AND session_bucket=london_open`
- Raw: n=41  W=16/L=25  WR=39.0%
- Sharpen: sharpest is BBP=BBP0 (8/25 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; session=london_open  •  ONLY when deep below lower band

### L23.  `H20=H20a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=41  W=16/L=25  WR=39.0%
- Sharpen: sharpest is BBP=BBP0 (8/25 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; session=london_open  •  ONLY when deep below lower band

### L24.  `H20=H20a AND H60=H60a AND T1=T1c AND session_bucket=london_open`
- Raw: n=41  W=16/L=25  WR=39.0%
- Sharpen: sharpest is BBP=BBP0 (8/25 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade; session=london_open  •  ONLY when deep below lower band

### L25.  `H20=H20a AND H60=H60a AND T4=T4c AND session_bucket=london_open`
- Raw: n=41  W=16/L=25  WR=39.0%
- Sharpen: sharpest is BBP=BBP0 (8/25 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend AGAINST trade; session=london_open  •  ONLY when deep below lower band

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | H60a(54/48) | H60e(46/52) |
| T1 | — | — |
| T4 | T4a(54/45) | T4c(46/55) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(54/48) | short(46/52) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
