# EUR_AUD — R39 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50e**  (EMA50 down >0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **2,690**  (W=1,666 / L=1,024)  -  WR: **61.9%**

## Session distribution

- asia: n=693  W=423/L=270  WR=61.0%
- ny_close: n=520  W=341/L=179  WR=65.6%
- ny_mid: n=467  W=281/L=186  WR=60.2%
- london_open: n=359  W=223/L=136  WR=62.1%
- london: n=292  W=185/L=107  WR=63.4%
- ny_open: n=178  W=105/L=73  WR=59.0%
- asia_late: n=131  W=82/L=49  WR=62.6%
- off_hours: n=50  W=26/L=24  WR=52.0%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND RSI=RSI2 AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=78  W=68/L=10  WR=87.2%
- Refine: no further refinement
- **Final: n=78  W=68/L=10  WR=87.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 30-40 weak; zscore -2 to -1 oversold; session=asia

### W02.  `H60=H60a AND RSI=RSI2 AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=78  W=68/L=10  WR=87.2%
- Refine: no further refinement
- **Final: n=78  W=68/L=10  WR=87.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 30-40 weak; zscore -2 to -1 oversold; session=asia

### W03.  `T1=T1a AND RSI=RSI2 AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=78  W=68/L=10  WR=87.2%
- Refine: no further refinement
- **Final: n=78  W=68/L=10  WR=87.2%**
- **Dir: ?**  •  1h trend WITH trade; RSI 30-40 weak; zscore -2 to -1 oversold; session=asia

### W04.  `T4=T4a AND RSI=RSI2 AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=78  W=68/L=10  WR=87.2%
- Refine: no further refinement
- **Final: n=78  W=68/L=10  WR=87.2%**
- **Dir: ?**  •  4h trend WITH trade; RSI 30-40 weak; zscore -2 to -1 oversold; session=asia

### W05.  `RSI=RSI2 AND ZS=ZS2 AND direction_exec=short AND session_bucket=asia`
- Raw: n=78  W=68/L=10  WR=87.2%
- Refine: no further refinement
- **Final: n=78  W=68/L=10  WR=87.2%**
- **Dir: SHORT**  •  RSI 30-40 weak; zscore -2 to -1 oversold; session=asia

### W06.  `H20=H20a AND BBP=BBP2 AND RSI=RSI1 AND session_bucket=ny_mid`
- Raw: n=69  W=64/L=5  WR=92.8%
- Refine: no further refinement
- **Final: n=69  W=64/L=5  WR=92.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; lower third; RSI 20-30 oversold; session=ny_mid

### W07.  `H60=H60a AND BBP=BBP2 AND RSI=RSI1 AND session_bucket=ny_mid`
- Raw: n=69  W=64/L=5  WR=92.8%
- Refine: no further refinement
- **Final: n=69  W=64/L=5  WR=92.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; lower third; RSI 20-30 oversold; session=ny_mid

### W08.  `T1=T1a AND BBP=BBP2 AND RSI=RSI1 AND session_bucket=ny_mid`
- Raw: n=69  W=64/L=5  WR=92.8%
- Refine: no further refinement
- **Final: n=69  W=64/L=5  WR=92.8%**
- **Dir: ?**  •  1h trend WITH trade; lower third; RSI 20-30 oversold; session=ny_mid

### W09.  `T4=T4a AND BBP=BBP2 AND RSI=RSI1 AND session_bucket=ny_mid`
- Raw: n=69  W=64/L=5  WR=92.8%
- Refine: no further refinement
- **Final: n=69  W=64/L=5  WR=92.8%**
- **Dir: ?**  •  4h trend WITH trade; lower third; RSI 20-30 oversold; session=ny_mid

### W10.  `BBP=BBP2 AND RSI=RSI1 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=69  W=64/L=5  WR=92.8%
- Refine: no further refinement
- **Final: n=69  W=64/L=5  WR=92.8%**
- **Dir: SHORT**  •  lower third; RSI 20-30 oversold; session=ny_mid

### W11.  `H20=H20a AND RSI=RSI1 AND ZS=ZS2 AND session_bucket=ny_mid`
- Raw: n=66  W=62/L=4  WR=93.9%
- Refine: no further refinement
- **Final: n=66  W=62/L=4  WR=93.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 20-30 oversold; zscore -2 to -1 oversold; session=ny_mid

### W12.  `H60=H60a AND RSI=RSI1 AND ZS=ZS2 AND session_bucket=ny_mid`
- Raw: n=66  W=62/L=4  WR=93.9%
- Refine: no further refinement
- **Final: n=66  W=62/L=4  WR=93.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 20-30 oversold; zscore -2 to -1 oversold; session=ny_mid

### W13.  `T1=T1a AND RSI=RSI1 AND ZS=ZS2 AND session_bucket=ny_mid`
- Raw: n=66  W=62/L=4  WR=93.9%
- Refine: no further refinement
- **Final: n=66  W=62/L=4  WR=93.9%**
- **Dir: ?**  •  1h trend WITH trade; RSI 20-30 oversold; zscore -2 to -1 oversold; session=ny_mid

### W14.  `T4=T4a AND RSI=RSI1 AND ZS=ZS2 AND session_bucket=ny_mid`
- Raw: n=66  W=62/L=4  WR=93.9%
- Refine: no further refinement
- **Final: n=66  W=62/L=4  WR=93.9%**
- **Dir: ?**  •  4h trend WITH trade; RSI 20-30 oversold; zscore -2 to -1 oversold; session=ny_mid

### W15.  `RSI=RSI1 AND ZS=ZS2 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=66  W=62/L=4  WR=93.9%
- Refine: no further refinement
- **Final: n=66  W=62/L=4  WR=93.9%**
- **Dir: SHORT**  •  RSI 20-30 oversold; zscore -2 to -1 oversold; session=ny_mid

### W16.  `H20=H20a AND BBP=BBP1 AND session_bucket=ny_mid`
- Raw: n=63  W=54/L=9  WR=85.7%
- Refine: exclude RSI=RSI2 drops 8/9 losers (89%)
- **Final: n=38  W=37/L=1  WR=97.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; just touched lower band; session=ny_mid  •  AVOID when RSI 30-40 weak

### W17.  `H60=H60a AND BBP=BBP1 AND session_bucket=ny_mid`
- Raw: n=63  W=54/L=9  WR=85.7%
- Refine: exclude RSI=RSI2 drops 8/9 losers (89%)
- **Final: n=38  W=37/L=1  WR=97.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; just touched lower band; session=ny_mid  •  AVOID when RSI 30-40 weak

### W18.  `T1=T1a AND BBP=BBP1 AND session_bucket=ny_mid`
- Raw: n=63  W=54/L=9  WR=85.7%
- Refine: exclude RSI=RSI2 drops 8/9 losers (89%)
- **Final: n=38  W=37/L=1  WR=97.4%**
- **Dir: ?**  •  1h trend WITH trade; just touched lower band; session=ny_mid  •  AVOID when RSI 30-40 weak

### W19.  `T4=T4a AND BBP=BBP1 AND session_bucket=ny_mid`
- Raw: n=63  W=54/L=9  WR=85.7%
- Refine: exclude RSI=RSI2 drops 8/9 losers (89%)
- **Final: n=38  W=37/L=1  WR=97.4%**
- **Dir: ?**  •  4h trend WITH trade; just touched lower band; session=ny_mid  •  AVOID when RSI 30-40 weak

### W20.  `BBP=BBP1 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=63  W=54/L=9  WR=85.7%
- Refine: exclude RSI=RSI2 drops 8/9 losers (89%)
- **Final: n=38  W=37/L=1  WR=97.4%**
- **Dir: SHORT**  •  just touched lower band; session=ny_mid  •  AVOID when RSI 30-40 weak

### W21.  `H20=H20a AND H60=H60a AND BBP=BBP1 AND session_bucket=ny_mid`
- Raw: n=63  W=54/L=9  WR=85.7%
- Refine: exclude RSI=RSI2 drops 8/9 losers (89%)
- **Final: n=38  W=37/L=1  WR=97.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; just touched lower band; session=ny_mid  •  AVOID when RSI 30-40 weak

### W22.  `H20=H20a AND T1=T1a AND BBP=BBP1 AND session_bucket=ny_mid`
- Raw: n=63  W=54/L=9  WR=85.7%
- Refine: exclude RSI=RSI2 drops 8/9 losers (89%)
- **Final: n=38  W=37/L=1  WR=97.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; just touched lower band; session=ny_mid  •  AVOID when RSI 30-40 weak

### W23.  `H20=H20a AND T4=T4a AND BBP=BBP1 AND session_bucket=ny_mid`
- Raw: n=63  W=54/L=9  WR=85.7%
- Refine: exclude RSI=RSI2 drops 8/9 losers (89%)
- **Final: n=38  W=37/L=1  WR=97.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; just touched lower band; session=ny_mid  •  AVOID when RSI 30-40 weak

### W24.  `H20=H20a AND BBP=BBP1 AND ZS=ZS1 AND session_bucket=ny_mid`
- Raw: n=63  W=54/L=9  WR=85.7%
- Refine: exclude RSI=RSI2 drops 8/9 losers (89%)
- **Final: n=38  W=37/L=1  WR=97.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; just touched lower band; zscore -3 to -2 deep oversold; session=ny_mid  •  AVOID when RSI 30-40 weak

### W25.  `H20=H20a AND BBP=BBP1 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=63  W=54/L=9  WR=85.7%
- Refine: exclude RSI=RSI2 drops 8/9 losers (89%)
- **Final: n=38  W=37/L=1  WR=97.4%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; just touched lower band; session=ny_mid  •  AVOID when RSI 30-40 weak

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND RSI=RSI1 AND session_bucket=ny_mid`
- Raw: n=112  W=30/L=82  WR=26.8%
- Sharpen: sharpest is ZS=ZS2 (43/82 of losers there)
- **Sharp: n=51  W=8/L=43  WR=15.7%**
- **Dir: ?**  •  HTF20 strongly against; RSI 20-30 oversold; session=ny_mid  •  ONLY when zscore -2 to -1 oversold

### L02.  `H60=H60e AND RSI=RSI1 AND session_bucket=ny_mid`
- Raw: n=112  W=30/L=82  WR=26.8%
- Sharpen: sharpest is ZS=ZS2 (43/82 of losers there)
- **Sharp: n=51  W=8/L=43  WR=15.7%**
- **Dir: ?**  •  HTF60 strongly against; RSI 20-30 oversold; session=ny_mid  •  ONLY when zscore -2 to -1 oversold

### L03.  `T1=T1c AND RSI=RSI1 AND session_bucket=ny_mid`
- Raw: n=112  W=30/L=82  WR=26.8%
- Sharpen: sharpest is ZS=ZS2 (43/82 of losers there)
- **Sharp: n=51  W=8/L=43  WR=15.7%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 20-30 oversold; session=ny_mid  •  ONLY when zscore -2 to -1 oversold

### L04.  `T4=T4c AND RSI=RSI1 AND session_bucket=ny_mid`
- Raw: n=112  W=30/L=82  WR=26.8%
- Sharpen: sharpest is ZS=ZS2 (43/82 of losers there)
- **Sharp: n=51  W=8/L=43  WR=15.7%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 20-30 oversold; session=ny_mid  •  ONLY when zscore -2 to -1 oversold

### L05.  `RSI=RSI1 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=112  W=30/L=82  WR=26.8%
- Sharpen: sharpest is ZS=ZS2 (43/82 of losers there)
- **Sharp: n=51  W=8/L=43  WR=15.7%**
- **Dir: LONG**  •  RSI 20-30 oversold; session=ny_mid  •  ONLY when zscore -2 to -1 oversold

### L06.  `H20=H20e AND H60=H60e AND RSI=RSI1 AND session_bucket=ny_mid`
- Raw: n=112  W=30/L=82  WR=26.8%
- Sharpen: sharpest is ZS=ZS2 (43/82 of losers there)
- **Sharp: n=51  W=8/L=43  WR=15.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 20-30 oversold; session=ny_mid  •  ONLY when zscore -2 to -1 oversold

### L07.  `H20=H20e AND T1=T1c AND RSI=RSI1 AND session_bucket=ny_mid`
- Raw: n=112  W=30/L=82  WR=26.8%
- Sharpen: sharpest is ZS=ZS2 (43/82 of losers there)
- **Sharp: n=51  W=8/L=43  WR=15.7%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 20-30 oversold; session=ny_mid  •  ONLY when zscore -2 to -1 oversold

### L08.  `H20=H20e AND T4=T4c AND RSI=RSI1 AND session_bucket=ny_mid`
- Raw: n=112  W=30/L=82  WR=26.8%
- Sharpen: sharpest is ZS=ZS2 (43/82 of losers there)
- **Sharp: n=51  W=8/L=43  WR=15.7%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 20-30 oversold; session=ny_mid  •  ONLY when zscore -2 to -1 oversold

### L09.  `H20=H20e AND RSI=RSI1 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=112  W=30/L=82  WR=26.8%
- Sharpen: sharpest is ZS=ZS2 (43/82 of losers there)
- **Sharp: n=51  W=8/L=43  WR=15.7%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 20-30 oversold; session=ny_mid  •  ONLY when zscore -2 to -1 oversold

### L10.  `H60=H60e AND T1=T1c AND RSI=RSI1 AND session_bucket=ny_mid`
- Raw: n=112  W=30/L=82  WR=26.8%
- Sharpen: sharpest is ZS=ZS2 (43/82 of losers there)
- **Sharp: n=51  W=8/L=43  WR=15.7%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 20-30 oversold; session=ny_mid  •  ONLY when zscore -2 to -1 oversold

### L11.  `H60=H60e AND T4=T4c AND RSI=RSI1 AND session_bucket=ny_mid`
- Raw: n=112  W=30/L=82  WR=26.8%
- Sharpen: sharpest is ZS=ZS2 (43/82 of losers there)
- **Sharp: n=51  W=8/L=43  WR=15.7%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 20-30 oversold; session=ny_mid  •  ONLY when zscore -2 to -1 oversold

### L12.  `H60=H60e AND RSI=RSI1 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=112  W=30/L=82  WR=26.8%
- Sharpen: sharpest is ZS=ZS2 (43/82 of losers there)
- **Sharp: n=51  W=8/L=43  WR=15.7%**
- **Dir: LONG**  •  HTF60 strongly against; RSI 20-30 oversold; session=ny_mid  •  ONLY when zscore -2 to -1 oversold

### L13.  `T1=T1c AND T4=T4c AND RSI=RSI1 AND session_bucket=ny_mid`
- Raw: n=112  W=30/L=82  WR=26.8%
- Sharpen: sharpest is ZS=ZS2 (43/82 of losers there)
- **Sharp: n=51  W=8/L=43  WR=15.7%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 20-30 oversold; session=ny_mid  •  ONLY when zscore -2 to -1 oversold

### L14.  `T1=T1c AND RSI=RSI1 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=112  W=30/L=82  WR=26.8%
- Sharpen: sharpest is ZS=ZS2 (43/82 of losers there)
- **Sharp: n=51  W=8/L=43  WR=15.7%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 20-30 oversold; session=ny_mid  •  ONLY when zscore -2 to -1 oversold

### L15.  `T4=T4c AND RSI=RSI1 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=112  W=30/L=82  WR=26.8%
- Sharpen: sharpest is ZS=ZS2 (43/82 of losers there)
- **Sharp: n=51  W=8/L=43  WR=15.7%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 20-30 oversold; session=ny_mid  •  ONLY when zscore -2 to -1 oversold

### L16.  `H20=H20e AND BBP=BBP2 AND session_bucket=ny_mid`
- Raw: n=108  W=39/L=69  WR=36.1%
- Sharpen: sharpest is RSI=RSI1 (44/69 of losers there)
- **Sharp: n=54  W=10/L=44  WR=18.5%**
- **Dir: ?**  •  HTF20 strongly against; lower third; session=ny_mid  •  ONLY when RSI 20-30 oversold

### L17.  `H60=H60e AND BBP=BBP2 AND session_bucket=ny_mid`
- Raw: n=106  W=39/L=67  WR=36.8%
- Sharpen: sharpest is RSI=RSI1 (44/67 of losers there)
- **Sharp: n=54  W=10/L=44  WR=18.5%**
- **Dir: ?**  •  HTF60 strongly against; lower third; session=ny_mid  •  ONLY when RSI 20-30 oversold

### L18.  `T1=T1c AND BBP=BBP2 AND session_bucket=ny_mid`
- Raw: n=106  W=39/L=67  WR=36.8%
- Sharpen: sharpest is RSI=RSI1 (44/67 of losers there)
- **Sharp: n=54  W=10/L=44  WR=18.5%**
- **Dir: ?**  •  1h trend AGAINST trade; lower third; session=ny_mid  •  ONLY when RSI 20-30 oversold

### L19.  `T4=T4c AND BBP=BBP2 AND session_bucket=ny_mid`
- Raw: n=106  W=39/L=67  WR=36.8%
- Sharpen: sharpest is RSI=RSI1 (44/67 of losers there)
- **Sharp: n=54  W=10/L=44  WR=18.5%**
- **Dir: ?**  •  4h trend AGAINST trade; lower third; session=ny_mid  •  ONLY when RSI 20-30 oversold

### L20.  `BBP=BBP2 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=106  W=39/L=67  WR=36.8%
- Sharpen: sharpest is RSI=RSI1 (44/67 of losers there)
- **Sharp: n=54  W=10/L=44  WR=18.5%**
- **Dir: LONG**  •  lower third; session=ny_mid  •  ONLY when RSI 20-30 oversold

### L21.  `H20=H20e AND H60=H60e AND BBP=BBP2 AND session_bucket=ny_mid`
- Raw: n=106  W=39/L=67  WR=36.8%
- Sharpen: sharpest is RSI=RSI1 (44/67 of losers there)
- **Sharp: n=54  W=10/L=44  WR=18.5%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; lower third; session=ny_mid  •  ONLY when RSI 20-30 oversold

### L22.  `H20=H20e AND T1=T1c AND BBP=BBP2 AND session_bucket=ny_mid`
- Raw: n=106  W=39/L=67  WR=36.8%
- Sharpen: sharpest is RSI=RSI1 (44/67 of losers there)
- **Sharp: n=54  W=10/L=44  WR=18.5%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; lower third; session=ny_mid  •  ONLY when RSI 20-30 oversold

### L23.  `H20=H20e AND T4=T4c AND BBP=BBP2 AND session_bucket=ny_mid`
- Raw: n=106  W=39/L=67  WR=36.8%
- Sharpen: sharpest is RSI=RSI1 (44/67 of losers there)
- **Sharp: n=54  W=10/L=44  WR=18.5%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; lower third; session=ny_mid  •  ONLY when RSI 20-30 oversold

### L24.  `H20=H20e AND BBP=BBP2 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=106  W=39/L=67  WR=36.8%
- Sharpen: sharpest is RSI=RSI1 (44/67 of losers there)
- **Sharp: n=54  W=10/L=44  WR=18.5%**
- **Dir: LONG**  •  HTF20 strongly against; lower third; session=ny_mid  •  ONLY when RSI 20-30 oversold

### L25.  `H60=H60e AND T1=T1c AND BBP=BBP2 AND session_bucket=ny_mid`
- Raw: n=106  W=39/L=67  WR=36.8%
- Sharpen: sharpest is RSI=RSI1 (44/67 of losers there)
- **Sharp: n=54  W=10/L=44  WR=18.5%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; lower third; session=ny_mid  •  ONLY when RSI 20-30 oversold

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(57/41) | H20e(43/59) |
| H60 | H60a(56/42) | H60e(44/58) |
| T1 | T1a(56/42) | T1c(44/58) |
| T4 | T4a(56/41) | T4c(44/59) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(56/42) | long(44/58) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
