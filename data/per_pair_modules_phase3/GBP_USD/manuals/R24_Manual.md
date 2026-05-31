# GBP_USD — R24 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50e**  (EMA50 down >0.5x)
- **ADR = ADR3**  (60-90%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **2,781**  (W=1,755 / L=1,026)  -  WR: **63.1%**

## Session distribution

- asia: n=1139  W=717/L=422  WR=62.9%
- ny_close: n=629  W=397/L=232  WR=63.1%
- london: n=259  W=169/L=90  WR=65.3%
- ny_open: n=243  W=154/L=89  WR=63.4%
- asia_late: n=225  W=141/L=84  WR=62.7%
- off_hours: n=128  W=79/L=49  WR=61.7%
- london_open: n=116  W=73/L=43  WR=62.9%
- ny_mid: n=42  W=25/L=17  WR=59.5%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=147  W=127/L=20  WR=86.4%
- Refine: exclude session_bucket=off_hours drops 8/20 losers (40%)
- **Final: n=137  W=125/L=12  WR=91.2%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when session=off_hours

### W02.  `T1=T1c AND T4=T4c AND RSI=RSI3 AND direction_exec=long`
- Raw: n=136  W=116/L=20  WR=85.3%
- Refine: exclude session_bucket=off_hours drops 8/20 losers (40%)
- **Final: n=126  W=114/L=12  WR=90.5%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when session=off_hours

### W03.  `H20=H20d AND H60=H60e AND T4=T4a`
- Raw: n=125  W=111/L=14  WR=88.8%
- Refine: exclude ZS=ZS3 drops 8/14 losers (57%)
- **Final: n=113  W=107/L=6  WR=94.7%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 strongly against; 4h trend WITH trade  •  AVOID when zscore -1 to +1 neutral

### W04.  `H60=H60e AND T1=T1c AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=116  W=106/L=10  WR=91.4%
- Refine: exclude H20=H20d drops 6/10 losers (60%)
- **Final: n=71  W=67/L=4  WR=94.4%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 30-40 weak; session=asia  •  AVOID when HTF20 mildly against

### W05.  `H60=H60e AND RSI=RSI2 AND direction_exec=long AND session_bucket=asia`
- Raw: n=116  W=106/L=10  WR=91.4%
- Refine: exclude H20=H20d drops 6/10 losers (60%)
- **Final: n=71  W=67/L=4  WR=94.4%**
- **Dir: LONG**  •  HTF60 strongly against; RSI 30-40 weak; session=asia  •  AVOID when HTF20 mildly against

### W06.  `T1=T1c AND BBP=BBP4 AND session_bucket=asia`
- Raw: n=111  W=99/L=12  WR=89.2%
- Refine: exclude H60=H60d drops 6/12 losers (50%)
- **Final: n=83  W=77/L=6  WR=92.8%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; session=asia  •  AVOID when HTF60 mildly against

### W07.  `T1=T1c AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=101  W=91/L=10  WR=90.1%
- Refine: exclude H20=H20e drops 7/10 losers (70%)
- **Final: n=57  W=54/L=3  WR=94.7%**
- **Dir: ?**  •  1h trend AGAINST trade; zscore +1 to +2 overbought; session=asia  •  AVOID when HTF20 strongly against

### W08.  `T1=T1c AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=101  W=91/L=10  WR=90.1%
- Refine: exclude H20=H20e drops 7/10 losers (70%)
- **Final: n=57  W=54/L=3  WR=94.7%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; zscore +1 to +2 overbought; session=asia  •  AVOID when HTF20 strongly against

### W09.  `T1=T1c AND BBP=BBP4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=101  W=89/L=12  WR=88.1%
- Refine: exclude H60=H60d drops 6/12 losers (50%)
- **Final: n=83  W=77/L=6  WR=92.8%**
- **Dir: LONG**  •  1h trend AGAINST trade; upper third; session=asia  •  AVOID when HTF60 mildly against

### W10.  `T4=T4a AND RSI=RSI2 AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=100  W=85/L=15  WR=85.0%
- Refine: exclude BBP=BBP1 drops 15/15 losers (100%)
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend WITH trade; RSI 30-40 weak; zscore -3 to -2 deep oversold; session=asia  •  AVOID when just touched lower band

### W11.  `ZS=ZS4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=95  W=81/L=14  WR=85.3%
- Refine: exclude H20=H20e drops 11/14 losers (79%)
- **Final: n=47  W=44/L=3  WR=93.6%**
- **Dir: LONG**  •  zscore +1 to +2 overbought; session=asia  •  AVOID when HTF20 strongly against

### W12.  `H20=H20a AND H60=H60a AND T1=T1a AND BBP=BBP0`
- Raw: n=95  W=81/L=14  WR=85.3%
- Refine: exclude session_bucket=asia_late drops 6/14 losers (43%)
- **Final: n=87  W=79/L=8  WR=90.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; deep below lower band  •  AVOID when session=asia_late

### W13.  `H20=H20a AND H60=H60a AND T4=T4a AND BBP=BBP0`
- Raw: n=95  W=81/L=14  WR=85.3%
- Refine: exclude session_bucket=asia_late drops 6/14 losers (43%)
- **Final: n=87  W=79/L=8  WR=90.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade; deep below lower band  •  AVOID when session=asia_late

### W14.  `H20=H20a AND H60=H60a AND BBP=BBP0 AND direction_exec=short`
- Raw: n=95  W=81/L=14  WR=85.3%
- Refine: exclude session_bucket=asia_late drops 6/14 losers (43%)
- **Final: n=87  W=79/L=8  WR=90.8%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; deep below lower band  •  AVOID when session=asia_late

### W15.  `BBP=BBP4 AND ZS=ZS4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=95  W=81/L=14  WR=85.3%
- Refine: exclude H20=H20e drops 11/14 losers (79%)
- **Final: n=47  W=44/L=3  WR=93.6%**
- **Dir: LONG**  •  upper third; zscore +1 to +2 overbought; session=asia  •  AVOID when HTF20 strongly against

### W16.  `T1=T1c AND ZS=ZS4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=91  W=81/L=10  WR=89.0%
- Refine: exclude H60=H60d drops 5/10 losers (50%)
- **Final: n=74  W=69/L=5  WR=93.2%**
- **Dir: LONG**  •  1h trend AGAINST trade; zscore +1 to +2 overbought; session=asia  •  AVOID when HTF60 mildly against

### W17.  `H20=H20a AND T1=T1a AND RSI=RSI0`
- Raw: n=91  W=78/L=13  WR=85.7%
- Refine: exclude BBP=BBP1 drops 6/13 losers (46%)
- **Final: n=72  W=65/L=7  WR=90.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI<20 extreme oversold  •  AVOID when just touched lower band

### W18.  `H20=H20a AND T4=T4a AND RSI=RSI0`
- Raw: n=91  W=78/L=13  WR=85.7%
- Refine: exclude BBP=BBP1 drops 6/13 losers (46%)
- **Final: n=72  W=65/L=7  WR=90.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI<20 extreme oversold  •  AVOID when just touched lower band

### W19.  `H20=H20a AND RSI=RSI0 AND direction_exec=short`
- Raw: n=91  W=78/L=13  WR=85.7%
- Refine: exclude BBP=BBP1 drops 6/13 losers (46%)
- **Final: n=72  W=65/L=7  WR=90.3%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI<20 extreme oversold  •  AVOID when just touched lower band

### W20.  `T1=T1a AND T4=T4a AND RSI=RSI0`
- Raw: n=91  W=78/L=13  WR=85.7%
- Refine: exclude BBP=BBP1 drops 6/13 losers (46%)
- **Final: n=72  W=65/L=7  WR=90.3%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI<20 extreme oversold  •  AVOID when just touched lower band

### W21.  `T1=T1a AND RSI=RSI0 AND direction_exec=short`
- Raw: n=91  W=78/L=13  WR=85.7%
- Refine: exclude BBP=BBP1 drops 6/13 losers (46%)
- **Final: n=72  W=65/L=7  WR=90.3%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI<20 extreme oversold  •  AVOID when just touched lower band

### W22.  `T4=T4a AND RSI=RSI0 AND direction_exec=short`
- Raw: n=91  W=78/L=13  WR=85.7%
- Refine: exclude BBP=BBP1 drops 6/13 losers (46%)
- **Final: n=72  W=65/L=7  WR=90.3%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI<20 extreme oversold  •  AVOID when just touched lower band

### W23.  `H20=H20a AND T1=T1a AND T4=T4a AND RSI=RSI0`
- Raw: n=91  W=78/L=13  WR=85.7%
- Refine: exclude BBP=BBP1 drops 6/13 losers (46%)
- **Final: n=72  W=65/L=7  WR=90.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; RSI<20 extreme oversold  •  AVOID when just touched lower band

### W24.  `H20=H20a AND T1=T1a AND RSI=RSI0 AND direction_exec=short`
- Raw: n=91  W=78/L=13  WR=85.7%
- Refine: exclude BBP=BBP1 drops 6/13 losers (46%)
- **Final: n=72  W=65/L=7  WR=90.3%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI<20 extreme oversold  •  AVOID when just touched lower band

### W25.  `H20=H20a AND T4=T4a AND RSI=RSI0 AND direction_exec=short`
- Raw: n=91  W=78/L=13  WR=85.7%
- Refine: exclude BBP=BBP1 drops 6/13 losers (46%)
- **Final: n=72  W=65/L=7  WR=90.3%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI<20 extreme oversold  •  AVOID when just touched lower band

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60a AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=226  W=88/L=138  WR=38.9%
- Sharpen: sharpest is BBP=BBP0 (27/138 of losers there)
- **Sharp: n=27  W=0/L=27  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 30-40 weak; session=asia  •  ONLY when deep below lower band

### L02.  `T1=T1a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=112  W=34/L=78  WR=30.4%
- Sharpen: sharpest is H20=H20e (27/78 of losers there)
- **Sharp: n=27  W=0/L=27  WR=0.0%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when HTF20 strongly against

### L03.  `T1=T1a AND T4=T4a AND RSI=RSI3`
- Raw: n=112  W=43/L=69  WR=38.4%
- Sharpen: sharpest is H20=H20e (25/69 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when HTF20 strongly against

### L04.  `T1=T1a AND T4=T4a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=103  W=34/L=69  WR=33.0%
- Sharpen: sharpest is H20=H20e (25/69 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when HTF20 strongly against

### L05.  `H20=H20e AND H60=H60a AND RSI=RSI2`
- Raw: n=96  W=29/L=67  WR=30.2%
- Sharpen: sharpest is T1=T1c (41/67 of losers there)
- **Sharp: n=50  W=9/L=41  WR=18.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; RSI 30-40 weak  •  ONLY when 1h trend AGAINST trade

### L06.  `T1=T1a AND RSI=RSI3 AND session_bucket=asia`
- Raw: n=95  W=29/L=66  WR=30.5%
- Sharpen: sharpest is H60=H60a (26/66 of losers there)
- **Sharp: n=29  W=3/L=26  WR=10.3%**
- **Dir: ?**  •  1h trend WITH trade; RSI 40-50 lower neutral; session=asia  •  ONLY when HTF60 aligned WITH trade

### L07.  `T1=T1c AND RSI=RSI1 AND session_bucket=ny_close`
- Raw: n=90  W=36/L=54  WR=40.0%
- Sharpen: sharpest is H60=H60a (11/54 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 20-30 oversold; session=ny_close  •  ONLY when HTF60 aligned WITH trade

### L08.  `T4=T4c AND RSI=RSI1 AND session_bucket=ny_close`
- Raw: n=90  W=36/L=54  WR=40.0%
- Sharpen: sharpest is H60=H60a (11/54 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 20-30 oversold; session=ny_close  •  ONLY when HTF60 aligned WITH trade

### L09.  `RSI=RSI1 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=90  W=36/L=54  WR=40.0%
- Sharpen: sharpest is H60=H60a (11/54 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: LONG**  •  RSI 20-30 oversold; session=ny_close  •  ONLY when HTF60 aligned WITH trade

### L10.  `H20=H20e AND H60=H60e AND T1=T1c AND BBP=BBP0`
- Raw: n=90  W=36/L=54  WR=40.0%
- Sharpen: sharpest is session_bucket=london_open (17/54 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; deep below lower band  •  ONLY when session=london_open

### L11.  `H20=H20e AND H60=H60e AND T4=T4c AND BBP=BBP0`
- Raw: n=90  W=36/L=54  WR=40.0%
- Sharpen: sharpest is session_bucket=london_open (17/54 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; deep below lower band  •  ONLY when session=london_open

### L12.  `H20=H20e AND H60=H60e AND BBP=BBP0 AND direction_exec=long`
- Raw: n=90  W=36/L=54  WR=40.0%
- Sharpen: sharpest is session_bucket=london_open (17/54 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 strongly against; deep below lower band  •  ONLY when session=london_open

### L13.  `T1=T1c AND T4=T4c AND RSI=RSI1 AND session_bucket=ny_close`
- Raw: n=90  W=36/L=54  WR=40.0%
- Sharpen: sharpest is H60=H60a (11/54 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 20-30 oversold; session=ny_close  •  ONLY when HTF60 aligned WITH trade

### L14.  `T1=T1c AND RSI=RSI1 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=90  W=36/L=54  WR=40.0%
- Sharpen: sharpest is H60=H60a (11/54 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 20-30 oversold; session=ny_close  •  ONLY when HTF60 aligned WITH trade

### L15.  `T4=T4c AND RSI=RSI1 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=90  W=36/L=54  WR=40.0%
- Sharpen: sharpest is H60=H60a (11/54 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 20-30 oversold; session=ny_close  •  ONLY when HTF60 aligned WITH trade

### L16.  `T4=T4c AND RSI=RSI2 AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=88  W=34/L=54  WR=38.6%
- Sharpen: sharpest is BBP=BBP0 (18/54 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 30-40 weak; zscore -3 to -2 deep oversold; session=asia  •  ONLY when deep below lower band

### L17.  `H20=H20e AND T1=T1c AND RSI=RSI0`
- Raw: n=82  W=28/L=54  WR=34.1%
- Sharpen: sharpest is BBP=BBP2 (26/54 of losers there)
- **Sharp: n=35  W=9/L=26  WR=25.7%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI<20 extreme oversold  •  ONLY when lower third

### L18.  `H20=H20e AND T4=T4c AND RSI=RSI0`
- Raw: n=82  W=28/L=54  WR=34.1%
- Sharpen: sharpest is BBP=BBP2 (26/54 of losers there)
- **Sharp: n=35  W=9/L=26  WR=25.7%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI<20 extreme oversold  •  ONLY when lower third

### L19.  `H20=H20e AND RSI=RSI0 AND direction_exec=long`
- Raw: n=82  W=28/L=54  WR=34.1%
- Sharpen: sharpest is BBP=BBP2 (26/54 of losers there)
- **Sharp: n=35  W=9/L=26  WR=25.7%**
- **Dir: LONG**  •  HTF20 strongly against; RSI<20 extreme oversold  •  ONLY when lower third

### L20.  `T1=T1c AND T4=T4c AND RSI=RSI0`
- Raw: n=82  W=28/L=54  WR=34.1%
- Sharpen: sharpest is BBP=BBP2 (26/54 of losers there)
- **Sharp: n=35  W=9/L=26  WR=25.7%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI<20 extreme oversold  •  ONLY when lower third

### L21.  `T1=T1c AND RSI=RSI0 AND direction_exec=long`
- Raw: n=82  W=28/L=54  WR=34.1%
- Sharpen: sharpest is BBP=BBP2 (26/54 of losers there)
- **Sharp: n=35  W=9/L=26  WR=25.7%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI<20 extreme oversold  •  ONLY when lower third

### L22.  `T4=T4c AND RSI=RSI0 AND direction_exec=long`
- Raw: n=82  W=28/L=54  WR=34.1%
- Sharpen: sharpest is BBP=BBP2 (26/54 of losers there)
- **Sharp: n=35  W=9/L=26  WR=25.7%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI<20 extreme oversold  •  ONLY when lower third

### L23.  `H20=H20e AND T1=T1c AND T4=T4c AND RSI=RSI0`
- Raw: n=82  W=28/L=54  WR=34.1%
- Sharpen: sharpest is BBP=BBP2 (26/54 of losers there)
- **Sharp: n=35  W=9/L=26  WR=25.7%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI<20 extreme oversold  •  ONLY when lower third

### L24.  `H20=H20e AND T1=T1c AND RSI=RSI0 AND direction_exec=long`
- Raw: n=82  W=28/L=54  WR=34.1%
- Sharpen: sharpest is BBP=BBP2 (26/54 of losers there)
- **Sharp: n=35  W=9/L=26  WR=25.7%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI<20 extreme oversold  •  ONLY when lower third

### L25.  `H20=H20e AND T4=T4c AND RSI=RSI0 AND direction_exec=long`
- Raw: n=82  W=28/L=54  WR=34.1%
- Sharpen: sharpest is BBP=BBP2 (26/54 of losers there)
- **Sharp: n=35  W=9/L=26  WR=25.7%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI<20 extreme oversold  •  ONLY when lower third

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(43/34), H20d(15/9) | H20e(33/44) |
| H60 | H60e(44/39) | H60a(38/44) |
| T1 | T1a(52/46) | T1c(48/54) |
| T4 | T4a(56/44) | T4c(44/56) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(53/46) | long(47/54) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
