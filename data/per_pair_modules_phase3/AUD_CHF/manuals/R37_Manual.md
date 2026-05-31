# AUD_CHF — R37 Manual

## Regime centroid (locked factors)

- **BB = BB2**  (normal bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20d**  (EMA20 down 0.15-0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **747**  (W=467 / L=280)  -  WR: **62.5%**

## Session distribution

- asia: n=266  W=159/L=107  WR=59.8%
- ny_mid: n=121  W=78/L=43  WR=64.5%
- ny_open: n=113  W=72/L=41  WR=63.7%
- london_open: n=110  W=75/L=35  WR=68.2%
- ny_close: n=66  W=38/L=28  WR=57.6%
- london: n=28  W=16/L=12  WR=57.1%
- off_hours: n=24  W=15/L=9  WR=62.5%
- asia_late: n=19  W=14/L=5  WR=73.7%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60a AND T4=T4c AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=66  W=58/L=8  WR=87.9%
- Refine: exclude BBP=BBP1 drops 6/8 losers (75%)
- **Final: n=44  W=42/L=2  WR=95.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 30-40 weak; session=asia  •  AVOID when just touched lower band

### W02.  `T1=T1c AND T4=T4c AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=66  W=58/L=8  WR=87.9%
- Refine: exclude BBP=BBP1 drops 6/8 losers (75%)
- **Final: n=44  W=42/L=2  WR=95.5%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 30-40 weak; session=asia  •  AVOID when just touched lower band

### W03.  `T4=T4c AND RSI=RSI2 AND direction_exec=long AND session_bucket=asia`
- Raw: n=66  W=58/L=8  WR=87.9%
- Refine: exclude BBP=BBP1 drops 6/8 losers (75%)
- **Final: n=44  W=42/L=2  WR=95.5%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 30-40 weak; session=asia  •  AVOID when just touched lower band

### W04.  `H60=H60e AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=56  W=51/L=5  WR=91.1%
- Refine: exclude BBP=BBP2 drops 3/5 losers (60%)
- **Final: n=41  W=39/L=2  WR=95.1%**
- **Dir: SHORT**  •  HTF60 strongly against; session=ny_open  •  AVOID when lower third

### W05.  `H20=H20a AND T4=T4c AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=54  W=46/L=8  WR=85.2%
- Refine: exclude BBP=BBP1 drops 6/8 losers (75%)
- **Final: n=40  W=38/L=2  WR=95.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 30-40 weak; session=asia  •  AVOID when just touched lower band

### W06.  `H60=H60e AND T1=T1a AND session_bucket=ny_open`
- Raw: n=53  W=49/L=4  WR=92.5%
- Refine: exclude RSI=RSI1 drops 3/4 losers (75%)
- **Final: n=38  W=37/L=1  WR=97.4%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; session=ny_open  •  AVOID when RSI 20-30 oversold

### W07.  `T1=T1a AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=53  W=49/L=4  WR=92.5%
- Refine: exclude RSI=RSI1 drops 3/4 losers (75%)
- **Final: n=38  W=37/L=1  WR=97.4%**
- **Dir: SHORT**  •  1h trend WITH trade; session=ny_open  •  AVOID when RSI 20-30 oversold

### W08.  `H60=H60e AND T1=T1a AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=53  W=49/L=4  WR=92.5%
- Refine: exclude RSI=RSI1 drops 3/4 losers (75%)
- **Final: n=38  W=37/L=1  WR=97.4%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend WITH trade; session=ny_open  •  AVOID when RSI 20-30 oversold

### W09.  `H60=H60e AND T4=T4a AND session_bucket=ny_open`
- Raw: n=53  W=48/L=5  WR=90.6%
- Refine: exclude BBP=BBP2 drops 3/5 losers (60%)
- **Final: n=38  W=36/L=2  WR=94.7%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; session=ny_open  •  AVOID when lower third

### W10.  `T4=T4a AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=53  W=48/L=5  WR=90.6%
- Refine: exclude BBP=BBP2 drops 3/5 losers (60%)
- **Final: n=38  W=36/L=2  WR=94.7%**
- **Dir: SHORT**  •  4h trend WITH trade; session=ny_open  •  AVOID when lower third

### W11.  `H60=H60e AND T4=T4a AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=53  W=48/L=5  WR=90.6%
- Refine: exclude BBP=BBP2 drops 3/5 losers (60%)
- **Final: n=38  W=36/L=2  WR=94.7%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend WITH trade; session=ny_open  •  AVOID when lower third

### W12.  `T1=T1a AND T4=T4a AND session_bucket=ny_open`
- Raw: n=50  W=46/L=4  WR=92.0%
- Refine: exclude RSI=RSI1 drops 3/4 losers (75%)
- **Final: n=35  W=34/L=1  WR=97.1%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; session=ny_open  •  AVOID when RSI 20-30 oversold

### W13.  `H60=H60e AND T1=T1a AND T4=T4a AND session_bucket=ny_open`
- Raw: n=50  W=46/L=4  WR=92.0%
- Refine: exclude RSI=RSI1 drops 3/4 losers (75%)
- **Final: n=35  W=34/L=1  WR=97.1%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend WITH trade; session=ny_open  •  AVOID when RSI 20-30 oversold

### W14.  `T1=T1a AND T4=T4a AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=50  W=46/L=4  WR=92.0%
- Refine: exclude RSI=RSI1 drops 3/4 losers (75%)
- **Final: n=35  W=34/L=1  WR=97.1%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend WITH trade; session=ny_open  •  AVOID when RSI 20-30 oversold

### W15.  `T4=T4c AND BBP=BBP2 AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=41  W=36/L=5  WR=87.8%
- Refine: exclude H20=H20e drops 4/5 losers (80%)
- **Final: n=27  W=26/L=1  WR=96.3%**
- **Dir: ?**  •  4h trend AGAINST trade; lower third; RSI 30-40 weak; session=asia  •  AVOID when HTF20 strongly against

### W16.  `H20=H20e AND H60=H60e AND session_bucket=ny_open`
- Raw: n=40  W=37/L=3  WR=92.5%
- Refine: exclude BBP=BBP1 drops 2/3 losers (67%)
- **Final: n=30  W=29/L=1  WR=96.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; session=ny_open  •  AVOID when just touched lower band

### W17.  `H20=H20e AND T1=T1a AND session_bucket=ny_open`
- Raw: n=40  W=37/L=3  WR=92.5%
- Refine: exclude BBP=BBP1 drops 2/3 losers (67%)
- **Final: n=30  W=29/L=1  WR=96.7%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; session=ny_open  •  AVOID when just touched lower band

### W18.  `H20=H20e AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=40  W=37/L=3  WR=92.5%
- Refine: exclude BBP=BBP1 drops 2/3 losers (67%)
- **Final: n=30  W=29/L=1  WR=96.7%**
- **Dir: SHORT**  •  HTF20 strongly against; session=ny_open  •  AVOID when just touched lower band

### W19.  `H20=H20e AND H60=H60e AND T1=T1a AND session_bucket=ny_open`
- Raw: n=40  W=37/L=3  WR=92.5%
- Refine: exclude BBP=BBP1 drops 2/3 losers (67%)
- **Final: n=30  W=29/L=1  WR=96.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend WITH trade; session=ny_open  •  AVOID when just touched lower band

### W20.  `H20=H20e AND H60=H60e AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=40  W=37/L=3  WR=92.5%
- Refine: exclude BBP=BBP1 drops 2/3 losers (67%)
- **Final: n=30  W=29/L=1  WR=96.7%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; session=ny_open  •  AVOID when just touched lower band

### W21.  `H20=H20e AND T1=T1a AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=40  W=37/L=3  WR=92.5%
- Refine: exclude BBP=BBP1 drops 2/3 losers (67%)
- **Final: n=30  W=29/L=1  WR=96.7%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend WITH trade; session=ny_open  •  AVOID when just touched lower band

### W22.  `T1=T1c AND ZS=ZS3 AND session_bucket=asia`
- Raw: n=39  W=35/L=4  WR=89.7%
- Refine: exclude strategy_id=alpha_extended_fade_v2 drops 2/4 losers (50%)
- **Final: n=37  W=35/L=2  WR=94.6%**
- **Dir: ?**  •  1h trend AGAINST trade; zscore -1 to +1 neutral; session=asia  •  AVOID when strategy=alpha_extended_fade_v2

### W23.  `H20=H20e AND T4=T4a AND session_bucket=ny_open`
- Raw: n=37  W=34/L=3  WR=91.9%
- Refine: exclude BBP=BBP1 drops 2/3 losers (67%)
- **Final: n=27  W=26/L=1  WR=96.3%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; session=ny_open  •  AVOID when just touched lower band

### W24.  `H20=H20e AND H60=H60e AND T4=T4a AND session_bucket=ny_open`
- Raw: n=37  W=34/L=3  WR=91.9%
- Refine: exclude BBP=BBP1 drops 2/3 losers (67%)
- **Final: n=27  W=26/L=1  WR=96.3%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend WITH trade; session=ny_open  •  AVOID when just touched lower band

### W25.  `H20=H20e AND T1=T1a AND T4=T4a AND session_bucket=ny_open`
- Raw: n=37  W=34/L=3  WR=91.9%
- Refine: exclude BBP=BBP1 drops 2/3 losers (67%)
- **Final: n=27  W=26/L=1  WR=96.3%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend WITH trade; session=ny_open  •  AVOID when just touched lower band

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND T1=T1a AND session_bucket=asia`
- Raw: n=102  W=40/L=62  WR=39.2%
- Sharpen: sharpest is T4=T4a (43/62 of losers there)
- **Sharp: n=60  W=17/L=43  WR=28.3%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; session=asia  •  ONLY when 4h trend WITH trade

### L02.  `H20=H20e AND T1=T1a AND direction_exec=short AND session_bucket=asia`
- Raw: n=102  W=40/L=62  WR=39.2%
- Sharpen: sharpest is T4=T4a (43/62 of losers there)
- **Sharp: n=60  W=17/L=43  WR=28.3%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend WITH trade; session=asia  •  ONLY when 4h trend WITH trade

### L03.  `H20=H20e AND H60=H60e AND T1=T1a AND session_bucket=asia`
- Raw: n=100  W=40/L=60  WR=40.0%
- Sharpen: sharpest is T4=T4a (41/60 of losers there)
- **Sharp: n=58  W=17/L=41  WR=29.3%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend WITH trade; session=asia  •  ONLY when 4h trend WITH trade

### L04.  `T4=T4a AND direction_exec=short AND session_bucket=asia`
- Raw: n=76  W=27/L=49  WR=35.5%
- Sharpen: sharpest is RSI=RSI2 (29/49 of losers there)
- **Sharp: n=38  W=9/L=29  WR=23.7%**
- **Dir: SHORT**  •  4h trend WITH trade; session=asia  •  ONLY when RSI 30-40 weak

### L05.  `T1=T1a AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=76  W=30/L=46  WR=39.5%
- Sharpen: sharpest is T4=T4a (29/46 of losers there)
- **Sharp: n=38  W=9/L=29  WR=23.7%**
- **Dir: ?**  •  1h trend WITH trade; RSI 30-40 weak; session=asia  •  ONLY when 4h trend WITH trade

### L06.  `RSI=RSI2 AND direction_exec=short AND session_bucket=asia`
- Raw: n=76  W=30/L=46  WR=39.5%
- Sharpen: sharpest is T4=T4a (29/46 of losers there)
- **Sharp: n=38  W=9/L=29  WR=23.7%**
- **Dir: SHORT**  •  RSI 30-40 weak; session=asia  •  ONLY when 4h trend WITH trade

### L07.  `T1=T1a AND RSI=RSI2 AND direction_exec=short AND session_bucket=asia`
- Raw: n=76  W=30/L=46  WR=39.5%
- Sharpen: sharpest is T4=T4a (29/46 of losers there)
- **Sharp: n=38  W=9/L=29  WR=23.7%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 30-40 weak; session=asia  •  ONLY when 4h trend WITH trade

### L08.  `H60=H60e AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=75  W=30/L=45  WR=40.0%
- Sharpen: sharpest is T4=T4a (28/45 of losers there)
- **Sharp: n=37  W=9/L=28  WR=24.3%**
- **Dir: ?**  •  HTF60 strongly against; RSI 30-40 weak; session=asia  •  ONLY when 4h trend WITH trade

### L09.  `H60=H60e AND T1=T1a AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=75  W=30/L=45  WR=40.0%
- Sharpen: sharpest is T4=T4a (28/45 of losers there)
- **Sharp: n=37  W=9/L=28  WR=24.3%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; RSI 30-40 weak; session=asia  •  ONLY when 4h trend WITH trade

### L10.  `H60=H60e AND RSI=RSI2 AND direction_exec=short AND session_bucket=asia`
- Raw: n=75  W=30/L=45  WR=40.0%
- Sharpen: sharpest is T4=T4a (28/45 of losers there)
- **Sharp: n=37  W=9/L=28  WR=24.3%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 30-40 weak; session=asia  •  ONLY when 4h trend WITH trade

### L11.  `T1=T1a AND T4=T4a AND session_bucket=asia`
- Raw: n=74  W=25/L=49  WR=33.8%
- Sharpen: sharpest is ZS=ZS3 (18/49 of losers there)
- **Sharp: n=20  W=2/L=18  WR=10.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; session=asia  •  ONLY when zscore -1 to +1 neutral

### L12.  `T1=T1a AND T4=T4a AND direction_exec=short AND session_bucket=asia`
- Raw: n=74  W=25/L=49  WR=33.8%
- Sharpen: sharpest is ZS=ZS3 (18/49 of losers there)
- **Sharp: n=20  W=2/L=18  WR=10.0%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend WITH trade; session=asia  •  ONLY when zscore -1 to +1 neutral

### L13.  `H60=H60e AND T4=T4a AND session_bucket=asia`
- Raw: n=74  W=27/L=47  WR=36.5%
- Sharpen: sharpest is RSI=RSI2 (28/47 of losers there)
- **Sharp: n=37  W=9/L=28  WR=24.3%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; session=asia  •  ONLY when RSI 30-40 weak

### L14.  `H60=H60e AND T4=T4a AND direction_exec=short AND session_bucket=asia`
- Raw: n=74  W=27/L=47  WR=36.5%
- Sharpen: sharpest is RSI=RSI2 (28/47 of losers there)
- **Sharp: n=37  W=9/L=28  WR=24.3%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend WITH trade; session=asia  •  ONLY when RSI 30-40 weak

### L15.  `H60=H60e AND T1=T1a AND T4=T4a AND session_bucket=asia`
- Raw: n=72  W=25/L=47  WR=34.7%
- Sharpen: sharpest is ZS=ZS3 (17/47 of losers there)
- **Sharp: n=19  W=2/L=17  WR=10.5%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend WITH trade; session=asia  •  ONLY when zscore -1 to +1 neutral

### L16.  `H20=H20e AND T4=T4a AND session_bucket=asia`
- Raw: n=62  W=19/L=43  WR=30.6%
- Sharpen: sharpest is ZS=ZS3 (18/43 of losers there)
- **Sharp: n=22  W=4/L=18  WR=18.2%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; session=asia  •  ONLY when zscore -1 to +1 neutral

### L17.  `H20=H20e AND T4=T4a AND direction_exec=short AND session_bucket=asia`
- Raw: n=62  W=19/L=43  WR=30.6%
- Sharpen: sharpest is ZS=ZS3 (18/43 of losers there)
- **Sharp: n=22  W=4/L=18  WR=18.2%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend WITH trade; session=asia  •  ONLY when zscore -1 to +1 neutral

### L18.  `H20=H20e AND T1=T1a AND T4=T4a AND session_bucket=asia`
- Raw: n=60  W=17/L=43  WR=28.3%
- Sharpen: sharpest is ZS=ZS3 (18/43 of losers there)
- **Sharp: n=20  W=2/L=18  WR=10.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend WITH trade; session=asia  •  ONLY when zscore -1 to +1 neutral

### L19.  `H20=H20e AND H60=H60e AND T4=T4a AND session_bucket=asia`
- Raw: n=60  W=19/L=41  WR=31.7%
- Sharpen: sharpest is ZS=ZS3 (17/41 of losers there)
- **Sharp: n=21  W=4/L=17  WR=19.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend WITH trade; session=asia  •  ONLY when zscore -1 to +1 neutral

### L20.  `H60=H60a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=57  W=21/L=36  WR=36.8%
- Sharpen: sharpest is RSI=RSI2 (26/36 of losers there)
- **Sharp: n=32  W=6/L=26  WR=18.8%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; session=ny_open  •  ONLY when RSI 30-40 weak

### L21.  `H60=H60a AND T1=T1c AND session_bucket=ny_open`
- Raw: n=53  W=18/L=35  WR=34.0%
- Sharpen: sharpest is RSI=RSI2 (26/35 of losers there)
- **Sharp: n=32  W=6/L=26  WR=18.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=ny_open  •  ONLY when RSI 30-40 weak

### L22.  `T1=T1c AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=53  W=18/L=35  WR=34.0%
- Sharpen: sharpest is RSI=RSI2 (26/35 of losers there)
- **Sharp: n=32  W=6/L=26  WR=18.8%**
- **Dir: LONG**  •  1h trend AGAINST trade; session=ny_open  •  ONLY when RSI 30-40 weak

### L23.  `H60=H60a AND T1=T1c AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=53  W=18/L=35  WR=34.0%
- Sharpen: sharpest is RSI=RSI2 (26/35 of losers there)
- **Sharp: n=32  W=6/L=26  WR=18.8%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=ny_open  •  ONLY when RSI 30-40 weak

### L24.  `H60=H60a AND T4=T4c AND session_bucket=ny_open`
- Raw: n=53  W=21/L=32  WR=39.6%
- Sharpen: sharpest is RSI=RSI2 (22/32 of losers there)
- **Sharp: n=28  W=6/L=22  WR=21.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=ny_open  •  ONLY when RSI 30-40 weak

### L25.  `T4=T4c AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=53  W=21/L=32  WR=39.6%
- Sharpen: sharpest is RSI=RSI2 (22/32 of losers there)
- **Sharp: n=28  W=6/L=22  WR=21.4%**
- **Dir: LONG**  •  4h trend AGAINST trade; session=ny_open  •  ONLY when RSI 30-40 weak

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | — |
| T1 | T1c(57/49) | T1a(43/51) |
| T4 | T4c(58/48) | T4a(42/52) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
