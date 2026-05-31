# AUD_CAD — R27 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50e**  (EMA50 down >0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **3,150**  (W=1,924 / L=1,226)  -  WR: **61.1%**

## Session distribution

- asia: n=1073  W=656/L=417  WR=61.1%
- ny_close: n=673  W=419/L=254  WR=62.3%
- london_open: n=374  W=225/L=149  WR=60.2%
- ny_mid: n=317  W=192/L=125  WR=60.6%
- london: n=241  W=143/L=98  WR=59.3%
- ny_open: n=162  W=91/L=71  WR=56.2%
- off_hours: n=157  W=99/L=58  WR=63.1%
- asia_late: n=153  W=99/L=54  WR=64.7%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20b AND H60=H60e AND session_bucket=asia`
- Raw: n=126  W=109/L=17  WR=86.5%
- Refine: exclude RSI=RSI2 drops 16/17 losers (94%)
- **Final: n=82  W=81/L=1  WR=98.8%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 strongly against; session=asia  •  AVOID when RSI 30-40 weak

### W02.  `H20=H20b AND T4=T4a AND session_bucket=asia`
- Raw: n=126  W=109/L=17  WR=86.5%
- Refine: exclude RSI=RSI2 drops 16/17 losers (94%)
- **Final: n=82  W=81/L=1  WR=98.8%**
- **Dir: ?**  •  HTF20 slightly aligned; 4h trend WITH trade; session=asia  •  AVOID when RSI 30-40 weak

### W03.  `H20=H20b AND direction_exec=short AND session_bucket=asia`
- Raw: n=126  W=109/L=17  WR=86.5%
- Refine: exclude RSI=RSI2 drops 16/17 losers (94%)
- **Final: n=82  W=81/L=1  WR=98.8%**
- **Dir: SHORT**  •  HTF20 slightly aligned; session=asia  •  AVOID when RSI 30-40 weak

### W04.  `H20=H20b AND H60=H60e AND T4=T4a AND session_bucket=asia`
- Raw: n=126  W=109/L=17  WR=86.5%
- Refine: exclude RSI=RSI2 drops 16/17 losers (94%)
- **Final: n=82  W=81/L=1  WR=98.8%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 strongly against; 4h trend WITH trade; session=asia  •  AVOID when RSI 30-40 weak

### W05.  `H20=H20b AND H60=H60e AND direction_exec=short AND session_bucket=asia`
- Raw: n=126  W=109/L=17  WR=86.5%
- Refine: exclude RSI=RSI2 drops 16/17 losers (94%)
- **Final: n=82  W=81/L=1  WR=98.8%**
- **Dir: SHORT**  •  HTF20 slightly aligned; HTF60 strongly against; session=asia  •  AVOID when RSI 30-40 weak

### W06.  `H20=H20b AND T4=T4a AND direction_exec=short AND session_bucket=asia`
- Raw: n=126  W=109/L=17  WR=86.5%
- Refine: exclude RSI=RSI2 drops 16/17 losers (94%)
- **Final: n=82  W=81/L=1  WR=98.8%**
- **Dir: SHORT**  •  HTF20 slightly aligned; 4h trend WITH trade; session=asia  •  AVOID when RSI 30-40 weak

### W07.  `H20=H20b AND T1=T1a AND session_bucket=asia`
- Raw: n=111  W=95/L=16  WR=85.6%
- Refine: exclude RSI=RSI2 drops 16/16 losers (100%)
- **Final: n=67  W=67/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend WITH trade; session=asia  •  AVOID when RSI 30-40 weak

### W08.  `H20=H20b AND H60=H60e AND T1=T1a AND session_bucket=asia`
- Raw: n=111  W=95/L=16  WR=85.6%
- Refine: exclude RSI=RSI2 drops 16/16 losers (100%)
- **Final: n=67  W=67/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 strongly against; 1h trend WITH trade; session=asia  •  AVOID when RSI 30-40 weak

### W09.  `H20=H20b AND T1=T1a AND T4=T4a AND session_bucket=asia`
- Raw: n=111  W=95/L=16  WR=85.6%
- Refine: exclude RSI=RSI2 drops 16/16 losers (100%)
- **Final: n=67  W=67/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend WITH trade; 4h trend WITH trade; session=asia  •  AVOID when RSI 30-40 weak

### W10.  `H20=H20b AND T1=T1a AND direction_exec=short AND session_bucket=asia`
- Raw: n=111  W=95/L=16  WR=85.6%
- Refine: exclude RSI=RSI2 drops 16/16 losers (100%)
- **Final: n=67  W=67/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 slightly aligned; 1h trend WITH trade; session=asia  •  AVOID when RSI 30-40 weak

### W11.  `H20=H20b AND BBP=BBP2 AND session_bucket=asia`
- Raw: n=72  W=67/L=5  WR=93.1%
- Refine: exclude RSI=RSI2 drops 4/5 losers (80%)
- **Final: n=52  W=51/L=1  WR=98.1%**
- **Dir: ?**  •  HTF20 slightly aligned; lower third; session=asia  •  AVOID when RSI 30-40 weak

### W12.  `H20=H20b AND RSI=RSI1 AND session_bucket=asia`
- Raw: n=67  W=67/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=67  W=67/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 slightly aligned; RSI 20-30 oversold; session=asia

### W13.  `H20=H20b AND H60=H60e AND RSI=RSI1 AND session_bucket=asia`
- Raw: n=67  W=67/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=67  W=67/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 strongly against; RSI 20-30 oversold; session=asia

### W14.  `H20=H20b AND T1=T1a AND RSI=RSI1 AND session_bucket=asia`
- Raw: n=67  W=67/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=67  W=67/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend WITH trade; RSI 20-30 oversold; session=asia

### W15.  `H20=H20b AND T4=T4a AND RSI=RSI1 AND session_bucket=asia`
- Raw: n=67  W=67/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=67  W=67/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 slightly aligned; 4h trend WITH trade; RSI 20-30 oversold; session=asia

### W16.  `H20=H20b AND RSI=RSI1 AND direction_exec=short AND session_bucket=asia`
- Raw: n=67  W=67/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=67  W=67/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 slightly aligned; RSI 20-30 oversold; session=asia

### W17.  `H20=H20b AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=65  W=61/L=4  WR=93.8%
- Refine: exclude RSI=RSI2 drops 3/4 losers (75%)
- **Final: n=46  W=45/L=1  WR=97.8%**
- **Dir: ?**  •  HTF20 slightly aligned; zscore -2 to -1 oversold; session=asia  •  AVOID when RSI 30-40 weak

### W18.  `H20=H20b AND BBP=BBP2 AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=65  W=61/L=4  WR=93.8%
- Refine: exclude RSI=RSI2 drops 3/4 losers (75%)
- **Final: n=46  W=45/L=1  WR=97.8%**
- **Dir: ?**  •  HTF20 slightly aligned; lower third; zscore -2 to -1 oversold; session=asia  •  AVOID when RSI 30-40 weak

### W19.  `H20=H20b AND H60=H60e AND BBP=BBP2 AND session_bucket=asia`
- Raw: n=63  W=59/L=4  WR=93.7%
- Refine: exclude RSI=RSI2 drops 3/4 losers (75%)
- **Final: n=52  W=51/L=1  WR=98.1%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 strongly against; lower third; session=asia  •  AVOID when RSI 30-40 weak

### W20.  `H20=H20b AND T4=T4a AND BBP=BBP2 AND session_bucket=asia`
- Raw: n=63  W=59/L=4  WR=93.7%
- Refine: exclude RSI=RSI2 drops 3/4 losers (75%)
- **Final: n=52  W=51/L=1  WR=98.1%**
- **Dir: ?**  •  HTF20 slightly aligned; 4h trend WITH trade; lower third; session=asia  •  AVOID when RSI 30-40 weak

### W21.  `H20=H20b AND BBP=BBP2 AND direction_exec=short AND session_bucket=asia`
- Raw: n=63  W=59/L=4  WR=93.7%
- Refine: exclude RSI=RSI2 drops 3/4 losers (75%)
- **Final: n=52  W=51/L=1  WR=98.1%**
- **Dir: SHORT**  •  HTF20 slightly aligned; lower third; session=asia  •  AVOID when RSI 30-40 weak

### W22.  `H20=H20b AND T1=T1a AND BBP=BBP2 AND session_bucket=asia`
- Raw: n=60  W=57/L=3  WR=95.0%
- Refine: exclude RSI=RSI2 drops 3/3 losers (100%)
- **Final: n=49  W=49/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend WITH trade; lower third; session=asia  •  AVOID when RSI 30-40 weak

### W23.  `H20=H20b AND H60=H60e AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=57  W=53/L=4  WR=93.0%
- Refine: exclude RSI=RSI2 drops 3/4 losers (75%)
- **Final: n=46  W=45/L=1  WR=97.8%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 strongly against; zscore -2 to -1 oversold; session=asia  •  AVOID when RSI 30-40 weak

### W24.  `H20=H20b AND T4=T4a AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=57  W=53/L=4  WR=93.0%
- Refine: exclude RSI=RSI2 drops 3/4 losers (75%)
- **Final: n=46  W=45/L=1  WR=97.8%**
- **Dir: ?**  •  HTF20 slightly aligned; 4h trend WITH trade; zscore -2 to -1 oversold; session=asia  •  AVOID when RSI 30-40 weak

### W25.  `H20=H20b AND ZS=ZS2 AND direction_exec=short AND session_bucket=asia`
- Raw: n=57  W=53/L=4  WR=93.0%
- Refine: exclude RSI=RSI2 drops 3/4 losers (75%)
- **Final: n=46  W=45/L=1  WR=97.8%**
- **Dir: SHORT**  •  HTF20 slightly aligned; zscore -2 to -1 oversold; session=asia  •  AVOID when RSI 30-40 weak

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60a AND RSI=RSI2 AND session_bucket=ny_close`
- Raw: n=160  W=64/L=96  WR=40.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=160  W=64/L=96  WR=40.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 30-40 weak; session=ny_close

### L02.  `T1=T1c AND RSI=RSI2 AND session_bucket=ny_close`
- Raw: n=160  W=64/L=96  WR=40.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=160  W=64/L=96  WR=40.0%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 30-40 weak; session=ny_close

### L03.  `RSI=RSI2 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=160  W=64/L=96  WR=40.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=160  W=64/L=96  WR=40.0%**
- **Dir: LONG**  •  RSI 30-40 weak; session=ny_close

### L04.  `H60=H60a AND T1=T1c AND RSI=RSI2 AND session_bucket=ny_close`
- Raw: n=160  W=64/L=96  WR=40.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=160  W=64/L=96  WR=40.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 30-40 weak; session=ny_close

### L05.  `H60=H60a AND RSI=RSI2 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=160  W=64/L=96  WR=40.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=160  W=64/L=96  WR=40.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 30-40 weak; session=ny_close

### L06.  `T1=T1c AND RSI=RSI2 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=160  W=64/L=96  WR=40.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=160  W=64/L=96  WR=40.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 30-40 weak; session=ny_close

### L07.  `H20=H20e AND RSI=RSI2 AND session_bucket=ny_close`
- Raw: n=123  W=49/L=74  WR=39.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=123  W=49/L=74  WR=39.8%**
- **Dir: ?**  •  HTF20 strongly against; RSI 30-40 weak; session=ny_close

### L08.  `H20=H20e AND H60=H60a AND RSI=RSI2 AND session_bucket=ny_close`
- Raw: n=123  W=49/L=74  WR=39.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=123  W=49/L=74  WR=39.8%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; RSI 30-40 weak; session=ny_close

### L09.  `H20=H20e AND T1=T1c AND RSI=RSI2 AND session_bucket=ny_close`
- Raw: n=123  W=49/L=74  WR=39.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=123  W=49/L=74  WR=39.8%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 30-40 weak; session=ny_close

### L10.  `H20=H20e AND RSI=RSI2 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=123  W=49/L=74  WR=39.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=123  W=49/L=74  WR=39.8%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 30-40 weak; session=ny_close

### L11.  `T4=T4c AND BBP=BBP4 AND RSI=RSI2`
- Raw: n=102  W=40/L=62  WR=39.2%
- Sharpen: sharpest is session_bucket=asia (16/62 of losers there)
- **Sharp: n=20  W=4/L=16  WR=20.0%**
- **Dir: ?**  •  4h trend AGAINST trade; upper third; RSI 30-40 weak  •  ONLY when session=asia

### L12.  `H20=H20d AND H60=H60a AND session_bucket=asia`
- Raw: n=91  W=26/L=65  WR=28.6%
- Sharpen: sharpest is RSI=RSI1 (32/65 of losers there)
- **Sharp: n=40  W=8/L=32  WR=20.0%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 aligned WITH trade; session=asia  •  ONLY when RSI 20-30 oversold

### L13.  `H20=H20d AND T4=T4c AND session_bucket=asia`
- Raw: n=91  W=26/L=65  WR=28.6%
- Sharpen: sharpest is RSI=RSI1 (32/65 of losers there)
- **Sharp: n=40  W=8/L=32  WR=20.0%**
- **Dir: ?**  •  HTF20 mildly against; 4h trend AGAINST trade; session=asia  •  ONLY when RSI 20-30 oversold

### L14.  `H20=H20d AND direction_exec=long AND session_bucket=asia`
- Raw: n=91  W=26/L=65  WR=28.6%
- Sharpen: sharpest is RSI=RSI1 (32/65 of losers there)
- **Sharp: n=40  W=8/L=32  WR=20.0%**
- **Dir: LONG**  •  HTF20 mildly against; session=asia  •  ONLY when RSI 20-30 oversold

### L15.  `H20=H20d AND H60=H60a AND T4=T4c AND session_bucket=asia`
- Raw: n=91  W=26/L=65  WR=28.6%
- Sharpen: sharpest is RSI=RSI1 (32/65 of losers there)
- **Sharp: n=40  W=8/L=32  WR=20.0%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 aligned WITH trade; 4h trend AGAINST trade; session=asia  •  ONLY when RSI 20-30 oversold

### L16.  `H20=H20d AND H60=H60a AND direction_exec=long AND session_bucket=asia`
- Raw: n=91  W=26/L=65  WR=28.6%
- Sharpen: sharpest is RSI=RSI1 (32/65 of losers there)
- **Sharp: n=40  W=8/L=32  WR=20.0%**
- **Dir: LONG**  •  HTF20 mildly against; HTF60 aligned WITH trade; session=asia  •  ONLY when RSI 20-30 oversold

### L17.  `H20=H20d AND T4=T4c AND direction_exec=long AND session_bucket=asia`
- Raw: n=91  W=26/L=65  WR=28.6%
- Sharpen: sharpest is RSI=RSI1 (32/65 of losers there)
- **Sharp: n=40  W=8/L=32  WR=20.0%**
- **Dir: LONG**  •  HTF20 mildly against; 4h trend AGAINST trade; session=asia  •  ONLY when RSI 20-30 oversold

### L18.  `H60=H60a AND T4=T4c AND BBP=BBP4 AND RSI=RSI2`
- Raw: n=84  W=30/L=54  WR=35.7%
- Sharpen: sharpest is H20=H20d (9/54 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; upper third; RSI 30-40 weak  •  ONLY when HTF20 mildly against

### L19.  `T1=T1c AND T4=T4c AND BBP=BBP4 AND RSI=RSI2`
- Raw: n=84  W=30/L=54  WR=35.7%
- Sharpen: sharpest is H20=H20d (9/54 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; upper third; RSI 30-40 weak  •  ONLY when HTF20 mildly against

### L20.  `T4=T4c AND BBP=BBP4 AND RSI=RSI2 AND direction_exec=long`
- Raw: n=84  W=30/L=54  WR=35.7%
- Sharpen: sharpest is H20=H20d (9/54 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; upper third; RSI 30-40 weak  •  ONLY when HTF20 mildly against

### L21.  `H20=H20e AND H60=H60a AND RSI=RSI1`
- Raw: n=80  W=32/L=48  WR=40.0%
- Sharpen: sharpest is ZS=ZS1 (16/48 of losers there)
- **Sharp: n=18  W=2/L=16  WR=11.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; RSI 20-30 oversold  •  ONLY when zscore -3 to -2 deep oversold

### L22.  `H20=H20e AND T1=T1c AND RSI=RSI1`
- Raw: n=80  W=32/L=48  WR=40.0%
- Sharpen: sharpest is ZS=ZS1 (16/48 of losers there)
- **Sharp: n=18  W=2/L=16  WR=11.1%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when zscore -3 to -2 deep oversold

### L23.  `H20=H20e AND T4=T4c AND RSI=RSI1`
- Raw: n=80  W=32/L=48  WR=40.0%
- Sharpen: sharpest is ZS=ZS1 (16/48 of losers there)
- **Sharp: n=18  W=2/L=16  WR=11.1%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when zscore -3 to -2 deep oversold

### L24.  `H20=H20e AND RSI=RSI1 AND direction_exec=long`
- Raw: n=80  W=32/L=48  WR=40.0%
- Sharpen: sharpest is ZS=ZS1 (16/48 of losers there)
- **Sharp: n=18  W=2/L=16  WR=11.1%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 20-30 oversold  •  ONLY when zscore -3 to -2 deep oversold

### L25.  `H20=H20e AND H60=H60a AND T1=T1c AND RSI=RSI1`
- Raw: n=80  W=32/L=48  WR=40.0%
- Sharpen: sharpest is ZS=ZS1 (16/48 of losers there)
- **Sharp: n=18  W=2/L=16  WR=11.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when zscore -3 to -2 deep oversold

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(27/22) | — |
| H60 | H60e(54/46) | H60a(46/54) |
| T1 | T1a(53/47) | T1c(47/53) |
| T4 | T4a(55/46) | T4c(45/54) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(54/46) | long(46/54) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
