# NZD_CAD — R32 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50e**  (EMA50 down >0.5x)
- **ADR = ADR5**  (>110% overshoot)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **1,141**  (W=715 / L=426)  -  WR: **62.7%**

## Session distribution

- asia: n=395  W=251/L=144  WR=63.5%
- london: n=172  W=104/L=68  WR=60.5%
- london_open: n=166  W=104/L=62  WR=62.7%
- off_hours: n=125  W=75/L=50  WR=60.0%
- ny_mid: n=91  W=51/L=40  WR=56.0%
- ny_close: n=83  W=56/L=27  WR=67.5%
- ny_open: n=58  W=36/L=22  WR=62.1%
- asia_late: n=51  W=38/L=13  WR=74.5%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=70  W=67/L=3  WR=95.7%
- Refine: exclude BBP=BBP0 drops 2/3 losers (67%)
- **Final: n=60  W=59/L=1  WR=98.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 30-40 weak; session=asia  •  AVOID when deep below lower band

### W02.  `H60=H60e AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=70  W=67/L=3  WR=95.7%
- Refine: exclude BBP=BBP0 drops 2/3 losers (67%)
- **Final: n=60  W=59/L=1  WR=98.3%**
- **Dir: ?**  •  HTF60 strongly against; RSI 30-40 weak; session=asia  •  AVOID when deep below lower band

### W03.  `T1=T1a AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=70  W=67/L=3  WR=95.7%
- Refine: exclude BBP=BBP0 drops 2/3 losers (67%)
- **Final: n=60  W=59/L=1  WR=98.3%**
- **Dir: ?**  •  1h trend WITH trade; RSI 30-40 weak; session=asia  •  AVOID when deep below lower band

### W04.  `T4=T4a AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=70  W=67/L=3  WR=95.7%
- Refine: exclude BBP=BBP0 drops 2/3 losers (67%)
- **Final: n=60  W=59/L=1  WR=98.3%**
- **Dir: ?**  •  4h trend WITH trade; RSI 30-40 weak; session=asia  •  AVOID when deep below lower band

### W05.  `RSI=RSI2 AND direction_exec=short AND session_bucket=asia`
- Raw: n=70  W=67/L=3  WR=95.7%
- Refine: exclude BBP=BBP0 drops 2/3 losers (67%)
- **Final: n=60  W=59/L=1  WR=98.3%**
- **Dir: SHORT**  •  RSI 30-40 weak; session=asia  •  AVOID when deep below lower band

### W06.  `H20=H20a AND H60=H60e AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=70  W=67/L=3  WR=95.7%
- Refine: exclude BBP=BBP0 drops 2/3 losers (67%)
- **Final: n=60  W=59/L=1  WR=98.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; RSI 30-40 weak; session=asia  •  AVOID when deep below lower band

### W07.  `H20=H20a AND T1=T1a AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=70  W=67/L=3  WR=95.7%
- Refine: exclude BBP=BBP0 drops 2/3 losers (67%)
- **Final: n=60  W=59/L=1  WR=98.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 30-40 weak; session=asia  •  AVOID when deep below lower band

### W08.  `H20=H20a AND T4=T4a AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=70  W=67/L=3  WR=95.7%
- Refine: exclude BBP=BBP0 drops 2/3 losers (67%)
- **Final: n=60  W=59/L=1  WR=98.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 30-40 weak; session=asia  •  AVOID when deep below lower band

### W09.  `H20=H20a AND RSI=RSI2 AND direction_exec=short AND session_bucket=asia`
- Raw: n=70  W=67/L=3  WR=95.7%
- Refine: exclude BBP=BBP0 drops 2/3 losers (67%)
- **Final: n=60  W=59/L=1  WR=98.3%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 30-40 weak; session=asia  •  AVOID when deep below lower band

### W10.  `H60=H60e AND T1=T1a AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=70  W=67/L=3  WR=95.7%
- Refine: exclude BBP=BBP0 drops 2/3 losers (67%)
- **Final: n=60  W=59/L=1  WR=98.3%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; RSI 30-40 weak; session=asia  •  AVOID when deep below lower band

### W11.  `H60=H60e AND T4=T4a AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=70  W=67/L=3  WR=95.7%
- Refine: exclude BBP=BBP0 drops 2/3 losers (67%)
- **Final: n=60  W=59/L=1  WR=98.3%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; RSI 30-40 weak; session=asia  •  AVOID when deep below lower band

### W12.  `H60=H60e AND RSI=RSI2 AND direction_exec=short AND session_bucket=asia`
- Raw: n=70  W=67/L=3  WR=95.7%
- Refine: exclude BBP=BBP0 drops 2/3 losers (67%)
- **Final: n=60  W=59/L=1  WR=98.3%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 30-40 weak; session=asia  •  AVOID when deep below lower band

### W13.  `T1=T1a AND T4=T4a AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=70  W=67/L=3  WR=95.7%
- Refine: exclude BBP=BBP0 drops 2/3 losers (67%)
- **Final: n=60  W=59/L=1  WR=98.3%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 30-40 weak; session=asia  •  AVOID when deep below lower band

### W14.  `T1=T1a AND RSI=RSI2 AND direction_exec=short AND session_bucket=asia`
- Raw: n=70  W=67/L=3  WR=95.7%
- Refine: exclude BBP=BBP0 drops 2/3 losers (67%)
- **Final: n=60  W=59/L=1  WR=98.3%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 30-40 weak; session=asia  •  AVOID when deep below lower band

### W15.  `T4=T4a AND RSI=RSI2 AND direction_exec=short AND session_bucket=asia`
- Raw: n=70  W=67/L=3  WR=95.7%
- Refine: exclude BBP=BBP0 drops 2/3 losers (67%)
- **Final: n=60  W=59/L=1  WR=98.3%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 30-40 weak; session=asia  •  AVOID when deep below lower band

### W16.  `H20=H20a AND BBP=BBP2 AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=42  W=42/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=42  W=42/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; lower third; RSI 30-40 weak; session=asia

### W17.  `H60=H60e AND BBP=BBP2 AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=42  W=42/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=42  W=42/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; lower third; RSI 30-40 weak; session=asia

### W18.  `T1=T1a AND BBP=BBP2 AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=42  W=42/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=42  W=42/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; lower third; RSI 30-40 weak; session=asia

### W19.  `T4=T4a AND BBP=BBP2 AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=42  W=42/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=42  W=42/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend WITH trade; lower third; RSI 30-40 weak; session=asia

### W20.  `BBP=BBP2 AND RSI=RSI2 AND direction_exec=short AND session_bucket=asia`
- Raw: n=42  W=42/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=42  W=42/L=0  WR=100.0%**
- **Dir: SHORT**  •  lower third; RSI 30-40 weak; session=asia

### W21.  `T1=T1c AND RSI=RSI3 AND ZS=ZS3`
- Raw: n=42  W=37/L=5  WR=88.1%
- Refine: exclude session_bucket=asia drops 5/5 losers (100%)
- **Final: n=20  W=20/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 40-50 lower neutral; zscore -1 to +1 neutral  •  AVOID when session=asia

### W22.  `RSI=RSI3 AND ZS=ZS3 AND direction_exec=long`
- Raw: n=42  W=37/L=5  WR=88.1%
- Refine: exclude session_bucket=asia drops 5/5 losers (100%)
- **Final: n=20  W=20/L=0  WR=100.0%**
- **Dir: LONG**  •  RSI 40-50 lower neutral; zscore -1 to +1 neutral  •  AVOID when session=asia

### W23.  `T1=T1c AND RSI=RSI3 AND ZS=ZS3 AND direction_exec=long`
- Raw: n=42  W=37/L=5  WR=88.1%
- Refine: exclude session_bucket=asia drops 5/5 losers (100%)
- **Final: n=20  W=20/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 40-50 lower neutral; zscore -1 to +1 neutral  •  AVOID when session=asia

### W24.  `H60=H60e AND BBP=BBP4 AND session_bucket=asia`
- Raw: n=41  W=35/L=6  WR=85.4%
- Refine: exclude T4=T4c drops 4/6 losers (67%)
- **Final: n=29  W=27/L=2  WR=93.1%**
- **Dir: ?**  •  HTF60 strongly against; upper third; session=asia  •  AVOID when 4h trend AGAINST trade

### W25.  `H60=H60a AND RSI=RSI3 AND ZS=ZS3`
- Raw: n=41  W=35/L=6  WR=85.4%
- Refine: exclude session_bucket=asia drops 6/6 losers (100%)
- **Final: n=20  W=20/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral; zscore -1 to +1 neutral  •  AVOID when session=asia

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND H60=H60a AND session_bucket=ny_mid`
- Raw: n=45  W=14/L=31  WR=31.1%
- Sharpen: sharpest is BBP=BBP2 (16/31 of losers there)
- **Sharp: n=18  W=2/L=16  WR=11.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; session=ny_mid  •  ONLY when lower third

### L02.  `H20=H20e AND T1=T1c AND session_bucket=ny_mid`
- Raw: n=45  W=14/L=31  WR=31.1%
- Sharpen: sharpest is BBP=BBP2 (16/31 of losers there)
- **Sharp: n=18  W=2/L=16  WR=11.1%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; session=ny_mid  •  ONLY when lower third

### L03.  `H20=H20e AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=45  W=14/L=31  WR=31.1%
- Sharpen: sharpest is BBP=BBP2 (16/31 of losers there)
- **Sharp: n=18  W=2/L=16  WR=11.1%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; session=ny_mid  •  ONLY when lower third

### L04.  `H20=H20e AND RSI=RSI1 AND session_bucket=ny_mid`
- Raw: n=45  W=14/L=31  WR=31.1%
- Sharpen: sharpest is BBP=BBP2 (16/31 of losers there)
- **Sharp: n=18  W=2/L=16  WR=11.1%**
- **Dir: ?**  •  HTF20 strongly against; RSI 20-30 oversold; session=ny_mid  •  ONLY when lower third

### L05.  `H20=H20e AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=45  W=14/L=31  WR=31.1%
- Sharpen: sharpest is BBP=BBP2 (16/31 of losers there)
- **Sharp: n=18  W=2/L=16  WR=11.1%**
- **Dir: LONG**  •  HTF20 strongly against; session=ny_mid  •  ONLY when lower third

### L06.  `H60=H60a AND T1=T1c AND session_bucket=ny_mid`
- Raw: n=45  W=14/L=31  WR=31.1%
- Sharpen: sharpest is BBP=BBP2 (16/31 of losers there)
- **Sharp: n=18  W=2/L=16  WR=11.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=ny_mid  •  ONLY when lower third

### L07.  `H60=H60a AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=45  W=14/L=31  WR=31.1%
- Sharpen: sharpest is BBP=BBP2 (16/31 of losers there)
- **Sharp: n=18  W=2/L=16  WR=11.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=ny_mid  •  ONLY when lower third

### L08.  `H60=H60a AND RSI=RSI1 AND session_bucket=ny_mid`
- Raw: n=45  W=14/L=31  WR=31.1%
- Sharpen: sharpest is BBP=BBP2 (16/31 of losers there)
- **Sharp: n=18  W=2/L=16  WR=11.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 20-30 oversold; session=ny_mid  •  ONLY when lower third

### L09.  `H60=H60a AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=45  W=14/L=31  WR=31.1%
- Sharpen: sharpest is BBP=BBP2 (16/31 of losers there)
- **Sharp: n=18  W=2/L=16  WR=11.1%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; session=ny_mid  •  ONLY when lower third

### L10.  `T1=T1c AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=45  W=14/L=31  WR=31.1%
- Sharpen: sharpest is BBP=BBP2 (16/31 of losers there)
- **Sharp: n=18  W=2/L=16  WR=11.1%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_mid  •  ONLY when lower third

### L11.  `T1=T1c AND RSI=RSI1 AND session_bucket=ny_mid`
- Raw: n=45  W=14/L=31  WR=31.1%
- Sharpen: sharpest is BBP=BBP2 (16/31 of losers there)
- **Sharp: n=18  W=2/L=16  WR=11.1%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 20-30 oversold; session=ny_mid  •  ONLY when lower third

### L12.  `T1=T1c AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=45  W=14/L=31  WR=31.1%
- Sharpen: sharpest is BBP=BBP2 (16/31 of losers there)
- **Sharp: n=18  W=2/L=16  WR=11.1%**
- **Dir: LONG**  •  1h trend AGAINST trade; session=ny_mid  •  ONLY when lower third

### L13.  `T4=T4c AND RSI=RSI1 AND session_bucket=ny_mid`
- Raw: n=45  W=14/L=31  WR=31.1%
- Sharpen: sharpest is BBP=BBP2 (16/31 of losers there)
- **Sharp: n=18  W=2/L=16  WR=11.1%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 20-30 oversold; session=ny_mid  •  ONLY when lower third

### L14.  `T4=T4c AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=45  W=14/L=31  WR=31.1%
- Sharpen: sharpest is BBP=BBP2 (16/31 of losers there)
- **Sharp: n=18  W=2/L=16  WR=11.1%**
- **Dir: LONG**  •  4h trend AGAINST trade; session=ny_mid  •  ONLY when lower third

### L15.  `RSI=RSI1 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=45  W=14/L=31  WR=31.1%
- Sharpen: sharpest is BBP=BBP2 (16/31 of losers there)
- **Sharp: n=18  W=2/L=16  WR=11.1%**
- **Dir: LONG**  •  RSI 20-30 oversold; session=ny_mid  •  ONLY when lower third

### L16.  `H20=H20e AND H60=H60a AND T1=T1c AND session_bucket=ny_mid`
- Raw: n=45  W=14/L=31  WR=31.1%
- Sharpen: sharpest is BBP=BBP2 (16/31 of losers there)
- **Sharp: n=18  W=2/L=16  WR=11.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend AGAINST trade; session=ny_mid  •  ONLY when lower third

### L17.  `H20=H20e AND H60=H60a AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=45  W=14/L=31  WR=31.1%
- Sharpen: sharpest is BBP=BBP2 (16/31 of losers there)
- **Sharp: n=18  W=2/L=16  WR=11.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 4h trend AGAINST trade; session=ny_mid  •  ONLY when lower third

### L18.  `H20=H20e AND H60=H60a AND RSI=RSI1 AND session_bucket=ny_mid`
- Raw: n=45  W=14/L=31  WR=31.1%
- Sharpen: sharpest is BBP=BBP2 (16/31 of losers there)
- **Sharp: n=18  W=2/L=16  WR=11.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; RSI 20-30 oversold; session=ny_mid  •  ONLY when lower third

### L19.  `H20=H20e AND H60=H60a AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=45  W=14/L=31  WR=31.1%
- Sharpen: sharpest is BBP=BBP2 (16/31 of losers there)
- **Sharp: n=18  W=2/L=16  WR=11.1%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 aligned WITH trade; session=ny_mid  •  ONLY when lower third

### L20.  `H20=H20e AND T1=T1c AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=45  W=14/L=31  WR=31.1%
- Sharpen: sharpest is BBP=BBP2 (16/31 of losers there)
- **Sharp: n=18  W=2/L=16  WR=11.1%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_mid  •  ONLY when lower third

### L21.  `H20=H20e AND T1=T1c AND RSI=RSI1 AND session_bucket=ny_mid`
- Raw: n=45  W=14/L=31  WR=31.1%
- Sharpen: sharpest is BBP=BBP2 (16/31 of losers there)
- **Sharp: n=18  W=2/L=16  WR=11.1%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 20-30 oversold; session=ny_mid  •  ONLY when lower third

### L22.  `H20=H20e AND T1=T1c AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=45  W=14/L=31  WR=31.1%
- Sharpen: sharpest is BBP=BBP2 (16/31 of losers there)
- **Sharp: n=18  W=2/L=16  WR=11.1%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade; session=ny_mid  •  ONLY when lower third

### L23.  `H20=H20e AND T4=T4c AND RSI=RSI1 AND session_bucket=ny_mid`
- Raw: n=45  W=14/L=31  WR=31.1%
- Sharpen: sharpest is BBP=BBP2 (16/31 of losers there)
- **Sharp: n=18  W=2/L=16  WR=11.1%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 20-30 oversold; session=ny_mid  •  ONLY when lower third

### L24.  `H20=H20e AND T4=T4c AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=45  W=14/L=31  WR=31.1%
- Sharpen: sharpest is BBP=BBP2 (16/31 of losers there)
- **Sharp: n=18  W=2/L=16  WR=11.1%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend AGAINST trade; session=ny_mid  •  ONLY when lower third

### L25.  `H20=H20e AND RSI=RSI1 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=45  W=14/L=31  WR=31.1%
- Sharpen: sharpest is BBP=BBP2 (16/31 of losers there)
- **Sharp: n=18  W=2/L=16  WR=11.1%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 20-30 oversold; session=ny_mid  •  ONLY when lower third

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | — |
| T1 | — | — |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
