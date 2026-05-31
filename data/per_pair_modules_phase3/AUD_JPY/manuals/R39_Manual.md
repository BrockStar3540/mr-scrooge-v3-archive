# AUD_JPY — R39 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50e**  (EMA50 down >0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **3,633**  (W=2,176 / L=1,457)  -  WR: **59.9%**

## Session distribution

- asia: n=1395  W=868/L=527  WR=62.2%
- london_open: n=751  W=442/L=309  WR=58.9%
- ny_mid: n=687  W=403/L=284  WR=58.7%
- asia_late: n=246  W=130/L=116  WR=52.8%
- ny_open: n=183  W=114/L=69  WR=62.3%
- ny_close: n=136  W=81/L=55  WR=59.6%
- london: n=130  W=82/L=48  WR=63.1%
- off_hours: n=105  W=56/L=49  WR=53.3%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60e AND T4=T4c AND RSI=RSI2 AND ZS=ZS2`
- Raw: n=89  W=77/L=12  WR=86.5%
- Refine: exclude session_bucket=london drops 8/12 losers (67%)
- **Final: n=81  W=77/L=4  WR=95.1%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 30-40 weak; zscore -2 to -1 oversold  •  AVOID when session=london

### W02.  `T1=T1a AND T4=T4c AND RSI=RSI2 AND ZS=ZS2`
- Raw: n=89  W=77/L=12  WR=86.5%
- Refine: exclude session_bucket=london drops 8/12 losers (67%)
- **Final: n=81  W=77/L=4  WR=95.1%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 30-40 weak; zscore -2 to -1 oversold  •  AVOID when session=london

### W03.  `T4=T4c AND RSI=RSI2 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=89  W=77/L=12  WR=86.5%
- Refine: exclude session_bucket=london drops 8/12 losers (67%)
- **Final: n=81  W=77/L=4  WR=95.1%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 30-40 weak; zscore -2 to -1 oversold  •  AVOID when session=london

### W04.  `H20=H20a AND BBP=BBP2 AND RSI=RSI1 AND session_bucket=asia`
- Raw: n=66  W=58/L=8  WR=87.9%
- Refine: exclude H60=H60e drops 4/8 losers (50%)
- **Final: n=51  W=47/L=4  WR=92.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; lower third; RSI 20-30 oversold; session=asia  •  AVOID when HTF60 strongly against

### W05.  `H20=H20a AND RSI=RSI1 AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=58  W=51/L=7  WR=87.9%
- Refine: exclude H60=H60e drops 4/7 losers (57%)
- **Final: n=43  W=40/L=3  WR=93.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 20-30 oversold; zscore -2 to -1 oversold; session=asia  •  AVOID when HTF60 strongly against

### W06.  `T4=T4c AND BBP=BBP0 AND session_bucket=london_open`
- Raw: n=54  W=48/L=6  WR=88.9%
- Refine: exclude H20=H20e drops 6/6 losers (100%)
- **Final: n=40  W=40/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend AGAINST trade; deep below lower band; session=london_open  •  AVOID when HTF20 strongly against

### W07.  `T4=T4a AND RSI=RSI2 AND ZS=ZS3 AND session_bucket=london_open`
- Raw: n=54  W=48/L=6  WR=88.9%
- Refine: exclude H60=H60e drops 6/6 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend WITH trade; RSI 30-40 weak; zscore -1 to +1 neutral; session=london_open  •  AVOID when HTF60 strongly against

### W08.  `H60=H60e AND BBP=BBP2 AND session_bucket=ny_open`
- Raw: n=54  W=46/L=8  WR=85.2%
- Refine: exclude T4=T4a drops 8/8 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; lower third; session=ny_open  •  AVOID when 4h trend WITH trade

### W09.  `T1=T1a AND BBP=BBP2 AND session_bucket=ny_open`
- Raw: n=54  W=46/L=8  WR=85.2%
- Refine: exclude T4=T4a drops 8/8 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; lower third; session=ny_open  •  AVOID when 4h trend WITH trade

### W10.  `BBP=BBP2 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=54  W=46/L=8  WR=85.2%
- Refine: exclude T4=T4a drops 8/8 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: SHORT**  •  lower third; session=ny_open  •  AVOID when 4h trend WITH trade

### W11.  `H60=H60e AND T1=T1a AND BBP=BBP2 AND session_bucket=ny_open`
- Raw: n=54  W=46/L=8  WR=85.2%
- Refine: exclude T4=T4a drops 8/8 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; lower third; session=ny_open  •  AVOID when 4h trend WITH trade

### W12.  `H60=H60e AND BBP=BBP2 AND RSI=RSI2 AND session_bucket=ny_open`
- Raw: n=54  W=46/L=8  WR=85.2%
- Refine: exclude T4=T4a drops 8/8 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; lower third; RSI 30-40 weak; session=ny_open  •  AVOID when 4h trend WITH trade

### W13.  `H60=H60e AND BBP=BBP2 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=54  W=46/L=8  WR=85.2%
- Refine: exclude T4=T4a drops 8/8 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 strongly against; lower third; session=ny_open  •  AVOID when 4h trend WITH trade

### W14.  `T1=T1a AND BBP=BBP2 AND RSI=RSI2 AND session_bucket=ny_open`
- Raw: n=54  W=46/L=8  WR=85.2%
- Refine: exclude T4=T4a drops 8/8 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; lower third; RSI 30-40 weak; session=ny_open  •  AVOID when 4h trend WITH trade

### W15.  `T1=T1a AND BBP=BBP2 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=54  W=46/L=8  WR=85.2%
- Refine: exclude T4=T4a drops 8/8 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend WITH trade; lower third; session=ny_open  •  AVOID when 4h trend WITH trade

### W16.  `BBP=BBP2 AND RSI=RSI2 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=54  W=46/L=8  WR=85.2%
- Refine: exclude T4=T4a drops 8/8 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: SHORT**  •  lower third; RSI 30-40 weak; session=ny_open  •  AVOID when 4h trend WITH trade

### W17.  `H20=H20c AND H60=H60e AND ZS=ZS1`
- Raw: n=48  W=44/L=4  WR=91.7%
- Refine: exclude BBP=BBP1 drops 4/4 losers (100%)
- **Final: n=14  W=14/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 neutral; HTF60 strongly against; zscore -3 to -2 deep oversold  •  AVOID when just touched lower band

### W18.  `H20=H20c AND T1=T1a AND ZS=ZS1`
- Raw: n=48  W=44/L=4  WR=91.7%
- Refine: exclude BBP=BBP1 drops 4/4 losers (100%)
- **Final: n=14  W=14/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 neutral; 1h trend WITH trade; zscore -3 to -2 deep oversold  •  AVOID when just touched lower band

### W19.  `H20=H20c AND T4=T4a AND ZS=ZS1`
- Raw: n=48  W=44/L=4  WR=91.7%
- Refine: exclude BBP=BBP1 drops 4/4 losers (100%)
- **Final: n=14  W=14/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 neutral; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  AVOID when just touched lower band

### W20.  `H20=H20c AND ZS=ZS1 AND direction_exec=short`
- Raw: n=48  W=44/L=4  WR=91.7%
- Refine: exclude BBP=BBP1 drops 4/4 losers (100%)
- **Final: n=14  W=14/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 neutral; zscore -3 to -2 deep oversold  •  AVOID when just touched lower band

### W21.  `H20=H20c AND H60=H60e AND T1=T1a AND ZS=ZS1`
- Raw: n=48  W=44/L=4  WR=91.7%
- Refine: exclude BBP=BBP1 drops 4/4 losers (100%)
- **Final: n=14  W=14/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 neutral; HTF60 strongly against; 1h trend WITH trade; zscore -3 to -2 deep oversold  •  AVOID when just touched lower band

### W22.  `H20=H20c AND H60=H60e AND T4=T4a AND ZS=ZS1`
- Raw: n=48  W=44/L=4  WR=91.7%
- Refine: exclude BBP=BBP1 drops 4/4 losers (100%)
- **Final: n=14  W=14/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 neutral; HTF60 strongly against; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  AVOID when just touched lower band

### W23.  `H20=H20c AND H60=H60e AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=48  W=44/L=4  WR=91.7%
- Refine: exclude BBP=BBP1 drops 4/4 losers (100%)
- **Final: n=14  W=14/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 neutral; HTF60 strongly against; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  AVOID when just touched lower band

### W24.  `H20=H20c AND H60=H60e AND ZS=ZS1 AND direction_exec=short`
- Raw: n=48  W=44/L=4  WR=91.7%
- Refine: exclude BBP=BBP1 drops 4/4 losers (100%)
- **Final: n=14  W=14/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 neutral; HTF60 strongly against; zscore -3 to -2 deep oversold  •  AVOID when just touched lower band

### W25.  `H20=H20c AND H60=H60e AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=48  W=44/L=4  WR=91.7%
- Refine: exclude BBP=BBP1 drops 4/4 losers (100%)
- **Final: n=14  W=14/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 neutral; HTF60 strongly against; zscore -3 to -2 deep oversold; session=asia  •  AVOID when just touched lower band

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND RSI=RSI3 AND direction_exec=short`
- Raw: n=206  W=81/L=125  WR=39.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=206  W=81/L=125  WR=39.3%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 40-50 lower neutral

### L02.  `H20=H20e AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=192  W=65/L=127  WR=33.9%
- Sharpen: sharpest is session_bucket=asia (54/127 of losers there)
- **Sharp: n=66  W=12/L=54  WR=18.2%**
- **Dir: ?**  •  HTF20 strongly against; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when session=asia

### L03.  `H20=H20e AND BBP=BBP1 AND ZS=ZS1`
- Raw: n=191  W=69/L=122  WR=36.1%
- Sharpen: sharpest is session_bucket=asia (52/122 of losers there)
- **Sharp: n=67  W=15/L=52  WR=22.4%**
- **Dir: ?**  •  HTF20 strongly against; just touched lower band; zscore -3 to -2 deep oversold  •  ONLY when session=asia

### L04.  `H20=H20e AND T4=T4a AND ZS=ZS1`
- Raw: n=183  W=65/L=118  WR=35.5%
- Sharpen: sharpest is BBP=BBP0 (43/118 of losers there)
- **Sharp: n=53  W=10/L=43  WR=18.9%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  ONLY when deep below lower band

### L05.  `H20=H20e AND H60=H60e AND T4=T4a AND ZS=ZS1`
- Raw: n=183  W=65/L=118  WR=35.5%
- Sharpen: sharpest is BBP=BBP0 (43/118 of losers there)
- **Sharp: n=53  W=10/L=43  WR=18.9%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  ONLY when deep below lower band

### L06.  `H20=H20e AND T1=T1a AND T4=T4a AND ZS=ZS1`
- Raw: n=183  W=65/L=118  WR=35.5%
- Sharpen: sharpest is BBP=BBP0 (43/118 of losers there)
- **Sharp: n=53  W=10/L=43  WR=18.9%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  ONLY when deep below lower band

### L07.  `H20=H20e AND T4=T4a AND ZS=ZS1 AND direction_exec=short`
- Raw: n=183  W=65/L=118  WR=35.5%
- Sharpen: sharpest is BBP=BBP0 (43/118 of losers there)
- **Sharp: n=53  W=10/L=43  WR=18.9%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend WITH trade; zscore -3 to -2 deep oversold  •  ONLY when deep below lower band

### L08.  `H20=H20e AND H60=H60e AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=169  W=56/L=113  WR=33.1%
- Sharpen: sharpest is session_bucket=asia (54/113 of losers there)
- **Sharp: n=64  W=10/L=54  WR=15.6%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when session=asia

### L09.  `H20=H20e AND T1=T1a AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=169  W=56/L=113  WR=33.1%
- Sharpen: sharpest is session_bucket=asia (54/113 of losers there)
- **Sharp: n=64  W=10/L=54  WR=15.6%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when session=asia

### L10.  `H20=H20e AND RSI=RSI2 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=169  W=56/L=113  WR=33.1%
- Sharpen: sharpest is session_bucket=asia (54/113 of losers there)
- **Sharp: n=64  W=10/L=54  WR=15.6%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when session=asia

### L11.  `H20=H20e AND H60=H60e AND BBP=BBP1`
- Raw: n=158  W=62/L=96  WR=39.2%
- Sharpen: sharpest is session_bucket=asia (47/96 of losers there)
- **Sharp: n=62  W=15/L=47  WR=24.2%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; just touched lower band  •  ONLY when session=asia

### L12.  `H20=H20e AND T1=T1a AND BBP=BBP1`
- Raw: n=158  W=62/L=96  WR=39.2%
- Sharpen: sharpest is session_bucket=asia (47/96 of losers there)
- **Sharp: n=62  W=15/L=47  WR=24.2%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; just touched lower band  •  ONLY when session=asia

### L13.  `H20=H20e AND BBP=BBP1 AND direction_exec=short`
- Raw: n=158  W=62/L=96  WR=39.2%
- Sharpen: sharpest is session_bucket=asia (47/96 of losers there)
- **Sharp: n=62  W=15/L=47  WR=24.2%**
- **Dir: SHORT**  •  HTF20 strongly against; just touched lower band  •  ONLY when session=asia

### L14.  `H20=H20e AND H60=H60e AND T1=T1a AND BBP=BBP1`
- Raw: n=158  W=62/L=96  WR=39.2%
- Sharpen: sharpest is session_bucket=asia (47/96 of losers there)
- **Sharp: n=62  W=15/L=47  WR=24.2%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend WITH trade; just touched lower band  •  ONLY when session=asia

### L15.  `H20=H20e AND H60=H60e AND BBP=BBP1 AND ZS=ZS1`
- Raw: n=158  W=62/L=96  WR=39.2%
- Sharpen: sharpest is session_bucket=asia (47/96 of losers there)
- **Sharp: n=62  W=15/L=47  WR=24.2%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; just touched lower band; zscore -3 to -2 deep oversold  •  ONLY when session=asia

### L16.  `H20=H20e AND H60=H60e AND BBP=BBP1 AND direction_exec=short`
- Raw: n=158  W=62/L=96  WR=39.2%
- Sharpen: sharpest is session_bucket=asia (47/96 of losers there)
- **Sharp: n=62  W=15/L=47  WR=24.2%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; just touched lower band  •  ONLY when session=asia

### L17.  `H20=H20e AND T1=T1a AND BBP=BBP1 AND ZS=ZS1`
- Raw: n=158  W=62/L=96  WR=39.2%
- Sharpen: sharpest is session_bucket=asia (47/96 of losers there)
- **Sharp: n=62  W=15/L=47  WR=24.2%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; just touched lower band; zscore -3 to -2 deep oversold  •  ONLY when session=asia

### L18.  `H20=H20e AND T1=T1a AND BBP=BBP1 AND direction_exec=short`
- Raw: n=158  W=62/L=96  WR=39.2%
- Sharpen: sharpest is session_bucket=asia (47/96 of losers there)
- **Sharp: n=62  W=15/L=47  WR=24.2%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend WITH trade; just touched lower band  •  ONLY when session=asia

### L19.  `H20=H20e AND BBP=BBP1 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=158  W=62/L=96  WR=39.2%
- Sharpen: sharpest is session_bucket=asia (47/96 of losers there)
- **Sharp: n=62  W=15/L=47  WR=24.2%**
- **Dir: SHORT**  •  HTF20 strongly against; just touched lower band; zscore -3 to -2 deep oversold  •  ONLY when session=asia

### L20.  `H20=H20e AND BBP=BBP1 AND RSI=RSI2`
- Raw: n=142  W=50/L=92  WR=35.2%
- Sharpen: sharpest is session_bucket=asia (44/92 of losers there)
- **Sharp: n=51  W=7/L=44  WR=13.7%**
- **Dir: ?**  •  HTF20 strongly against; just touched lower band; RSI 30-40 weak  •  ONLY when session=asia

### L21.  `H20=H20e AND BBP=BBP1 AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=142  W=50/L=92  WR=35.2%
- Sharpen: sharpest is session_bucket=asia (44/92 of losers there)
- **Sharp: n=51  W=7/L=44  WR=13.7%**
- **Dir: ?**  •  HTF20 strongly against; just touched lower band; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when session=asia

### L22.  `H20=H20e AND ZS=ZS2 AND session_bucket=ny_mid`
- Raw: n=135  W=53/L=82  WR=39.3%
- Sharpen: sharpest is H60=H60e (66/82 of losers there)
- **Sharp: n=90  W=24/L=66  WR=26.7%**
- **Dir: ?**  •  HTF20 strongly against; zscore -2 to -1 oversold; session=ny_mid  •  ONLY when HTF60 strongly against

### L23.  `H20=H20e AND BBP=BBP2 AND ZS=ZS2 AND session_bucket=ny_mid`
- Raw: n=135  W=53/L=82  WR=39.3%
- Sharpen: sharpest is H60=H60e (66/82 of losers there)
- **Sharp: n=90  W=24/L=66  WR=26.7%**
- **Dir: ?**  •  HTF20 strongly against; lower third; zscore -2 to -1 oversold; session=ny_mid  •  ONLY when HTF60 strongly against

### L24.  `H20=H20e AND T4=T4a AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=134  W=42/L=92  WR=31.3%
- Sharpen: sharpest is session_bucket=asia (54/92 of losers there)
- **Sharp: n=64  W=10/L=54  WR=15.6%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when session=asia

### L25.  `H20=H20e AND H60=H60e AND BBP=BBP1 AND RSI=RSI2`
- Raw: n=122  W=43/L=79  WR=35.2%
- Sharpen: sharpest is session_bucket=asia (44/79 of losers there)
- **Sharp: n=51  W=7/L=44  WR=13.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; just touched lower band; RSI 30-40 weak  •  ONLY when session=asia

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(50/40) | H20e(38/50) |
| H60 | H60a(55/48) | H60e(45/52) |
| T1 | — | — |
| T4 | T4c(56/46) | T4a(44/54) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(55/48) | short(45/52) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
