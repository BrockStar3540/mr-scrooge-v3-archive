# AUD_NZD — R28 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_3**  (5m ATR >120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50e**  (EMA50 down >0.5x)
- **ADR = ADR5**  (>110% overshoot)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **861**  (W=522 / L=339)  -  WR: **60.6%**

## Session distribution

- asia: n=402  W=235/L=167  WR=58.5%
- ny_mid: n=115  W=74/L=41  WR=64.3%
- london_open: n=98  W=65/L=33  WR=66.3%
- ny_close: n=76  W=46/L=30  WR=60.5%
- london: n=66  W=40/L=26  WR=60.6%
- asia_late: n=53  W=36/L=17  WR=67.9%
- ny_open: n=37  W=19/L=18  WR=51.4%
- off_hours: n=14  W=7/L=7  WR=50.0%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60e AND direction_exec=short AND session_bucket=london_open`
- Raw: n=62  W=54/L=8  WR=87.1%
- Refine: exclude H20=H20d drops 7/8 losers (88%)
- **Final: n=39  W=38/L=1  WR=97.4%**
- **Dir: SHORT**  •  HTF60 strongly against; session=london_open  •  AVOID when HTF20 mildly against

### W02.  `H60=H60e AND T1=T1a AND session_bucket=ny_mid`
- Raw: n=56  W=50/L=6  WR=89.3%
- Refine: exclude H20=H20c drops 5/6 losers (83%)
- **Final: n=51  W=50/L=1  WR=98.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; session=ny_mid  •  AVOID when HTF20 neutral

### W03.  `T1=T1a AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=56  W=50/L=6  WR=89.3%
- Refine: exclude H20=H20c drops 5/6 losers (83%)
- **Final: n=51  W=50/L=1  WR=98.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; session=ny_mid  •  AVOID when HTF20 neutral

### W04.  `T1=T1a AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=56  W=50/L=6  WR=89.3%
- Refine: exclude H20=H20c drops 5/6 losers (83%)
- **Final: n=51  W=50/L=1  WR=98.0%**
- **Dir: SHORT**  •  1h trend WITH trade; session=ny_mid  •  AVOID when HTF20 neutral

### W05.  `H60=H60e AND T1=T1a AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=56  W=50/L=6  WR=89.3%
- Refine: exclude H20=H20c drops 5/6 losers (83%)
- **Final: n=51  W=50/L=1  WR=98.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend WITH trade; session=ny_mid  •  AVOID when HTF20 neutral

### W06.  `H60=H60e AND T1=T1a AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=56  W=50/L=6  WR=89.3%
- Refine: exclude H20=H20c drops 5/6 losers (83%)
- **Final: n=51  W=50/L=1  WR=98.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend WITH trade; session=ny_mid  •  AVOID when HTF20 neutral

### W07.  `T1=T1a AND T4=T4a AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=56  W=50/L=6  WR=89.3%
- Refine: exclude H20=H20c drops 5/6 losers (83%)
- **Final: n=51  W=50/L=1  WR=98.0%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend WITH trade; session=ny_mid  •  AVOID when HTF20 neutral

### W08.  `H20=H20e AND H60=H60e AND session_bucket=ny_mid`
- Raw: n=51  W=50/L=1  WR=98.0%
- Refine: no further refinement
- **Final: n=51  W=50/L=1  WR=98.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; session=ny_mid

### W09.  `H20=H20e AND T1=T1a AND session_bucket=ny_mid`
- Raw: n=51  W=50/L=1  WR=98.0%
- Refine: no further refinement
- **Final: n=51  W=50/L=1  WR=98.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; session=ny_mid

### W10.  `H20=H20e AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=51  W=50/L=1  WR=98.0%
- Refine: no further refinement
- **Final: n=51  W=50/L=1  WR=98.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; session=ny_mid

### W11.  `H20=H20e AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=51  W=50/L=1  WR=98.0%
- Refine: no further refinement
- **Final: n=51  W=50/L=1  WR=98.0%**
- **Dir: SHORT**  •  HTF20 strongly against; session=ny_mid

### W12.  `H20=H20e AND H60=H60e AND T1=T1a AND session_bucket=ny_mid`
- Raw: n=51  W=50/L=1  WR=98.0%
- Refine: no further refinement
- **Final: n=51  W=50/L=1  WR=98.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend WITH trade; session=ny_mid

### W13.  `H20=H20e AND H60=H60e AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=51  W=50/L=1  WR=98.0%
- Refine: no further refinement
- **Final: n=51  W=50/L=1  WR=98.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend WITH trade; session=ny_mid

### W14.  `H20=H20e AND H60=H60e AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=51  W=50/L=1  WR=98.0%
- Refine: no further refinement
- **Final: n=51  W=50/L=1  WR=98.0%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; session=ny_mid

### W15.  `H20=H20e AND T1=T1a AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=51  W=50/L=1  WR=98.0%
- Refine: no further refinement
- **Final: n=51  W=50/L=1  WR=98.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend WITH trade; session=ny_mid

### W16.  `H20=H20e AND T1=T1a AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=51  W=50/L=1  WR=98.0%
- Refine: no further refinement
- **Final: n=51  W=50/L=1  WR=98.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend WITH trade; session=ny_mid

### W17.  `H20=H20e AND T4=T4a AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=51  W=50/L=1  WR=98.0%
- Refine: no further refinement
- **Final: n=51  W=50/L=1  WR=98.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend WITH trade; session=ny_mid

### W18.  `T1=T1a AND BBP=BBP1 AND ZS=ZS1`
- Raw: n=49  W=43/L=6  WR=87.8%
- Refine: exclude session_bucket=ny_close drops 5/6 losers (83%)
- **Final: n=39  W=38/L=1  WR=97.4%**
- **Dir: ?**  •  1h trend WITH trade; just touched lower band; zscore -3 to -2 deep oversold  •  AVOID when session=ny_close

### W19.  `H20=H20a AND H60=H60a AND T4=T4a`
- Raw: n=48  W=41/L=7  WR=85.4%
- Refine: exclude session_bucket=asia drops 7/7 losers (100%)
- **Final: n=12  W=12/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade  •  AVOID when session=asia

### W20.  `H20=H20a AND T4=T4a AND direction_exec=long`
- Raw: n=48  W=41/L=7  WR=85.4%
- Refine: exclude session_bucket=asia drops 7/7 losers (100%)
- **Final: n=12  W=12/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend WITH trade  •  AVOID when session=asia

### W21.  `H20=H20a AND H60=H60a AND T4=T4a AND direction_exec=long`
- Raw: n=48  W=41/L=7  WR=85.4%
- Refine: exclude session_bucket=asia drops 7/7 losers (100%)
- **Final: n=12  W=12/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade  •  AVOID when session=asia

### W22.  `H60=H60e AND T1=T1a AND BBP=BBP1`
- Raw: n=47  W=41/L=6  WR=87.2%
- Refine: exclude session_bucket=ny_close drops 5/6 losers (83%)
- **Final: n=37  W=36/L=1  WR=97.3%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; just touched lower band  •  AVOID when session=ny_close

### W23.  `T1=T1a AND BBP=BBP1 AND direction_exec=short`
- Raw: n=47  W=41/L=6  WR=87.2%
- Refine: exclude session_bucket=ny_close drops 5/6 losers (83%)
- **Final: n=37  W=36/L=1  WR=97.3%**
- **Dir: SHORT**  •  1h trend WITH trade; just touched lower band  •  AVOID when session=ny_close

### W24.  `H60=H60e AND T1=T1a AND BBP=BBP1 AND ZS=ZS1`
- Raw: n=47  W=41/L=6  WR=87.2%
- Refine: exclude session_bucket=ny_close drops 5/6 losers (83%)
- **Final: n=37  W=36/L=1  WR=97.3%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; just touched lower band; zscore -3 to -2 deep oversold  •  AVOID when session=ny_close

### W25.  `H60=H60e AND T1=T1a AND BBP=BBP1 AND direction_exec=short`
- Raw: n=47  W=41/L=6  WR=87.2%
- Refine: exclude session_bucket=ny_close drops 5/6 losers (83%)
- **Final: n=37  W=36/L=1  WR=97.3%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend WITH trade; just touched lower band  •  AVOID when session=ny_close

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60a AND T1=T1c AND session_bucket=ny_mid`
- Raw: n=47  W=16/L=31  WR=34.0%
- Sharpen: sharpest is RSI=RSI1 (24/31 of losers there)
- **Sharp: n=28  W=4/L=24  WR=14.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=ny_mid  •  ONLY when RSI 20-30 oversold

### L02.  `T1=T1c AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=47  W=16/L=31  WR=34.0%
- Sharpen: sharpest is RSI=RSI1 (24/31 of losers there)
- **Sharp: n=28  W=4/L=24  WR=14.3%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_mid  •  ONLY when RSI 20-30 oversold

### L03.  `T1=T1c AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=47  W=16/L=31  WR=34.0%
- Sharpen: sharpest is RSI=RSI1 (24/31 of losers there)
- **Sharp: n=28  W=4/L=24  WR=14.3%**
- **Dir: LONG**  •  1h trend AGAINST trade; session=ny_mid  •  ONLY when RSI 20-30 oversold

### L04.  `H60=H60a AND T1=T1c AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=47  W=16/L=31  WR=34.0%
- Sharpen: sharpest is RSI=RSI1 (24/31 of losers there)
- **Sharp: n=28  W=4/L=24  WR=14.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_mid  •  ONLY when RSI 20-30 oversold

### L05.  `H60=H60a AND T1=T1c AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=47  W=16/L=31  WR=34.0%
- Sharpen: sharpest is RSI=RSI1 (24/31 of losers there)
- **Sharp: n=28  W=4/L=24  WR=14.3%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=ny_mid  •  ONLY when RSI 20-30 oversold

### L06.  `T1=T1c AND T4=T4c AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=47  W=16/L=31  WR=34.0%
- Sharpen: sharpest is RSI=RSI1 (24/31 of losers there)
- **Sharp: n=28  W=4/L=24  WR=14.3%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_mid  •  ONLY when RSI 20-30 oversold

### L07.  `H20=H20e AND H60=H60e AND T4=T4c`
- Raw: n=42  W=13/L=29  WR=31.0%
- Sharpen: sharpest is session_bucket=ny_open (9/29 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade  •  ONLY when session=ny_open

### L08.  `H20=H20e AND T4=T4c AND direction_exec=short`
- Raw: n=42  W=13/L=29  WR=31.0%
- Sharpen: sharpest is session_bucket=ny_open (9/29 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade  •  ONLY when session=ny_open

### L09.  `H20=H20e AND H60=H60e AND T4=T4c AND direction_exec=short`
- Raw: n=42  W=13/L=29  WR=31.0%
- Sharpen: sharpest is session_bucket=ny_open (9/29 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade  •  ONLY when session=ny_open

### L10.  `T1=T1c AND BBP=BBP1 AND ZS=ZS1`
- Raw: n=41  W=12/L=29  WR=29.3%
- Sharpen: sharpest is session_bucket=asia (17/29 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; just touched lower band; zscore -3 to -2 deep oversold  •  ONLY when session=asia

### L11.  `H60=H60a AND BBP=BBP1 AND ZS=ZS1`
- Raw: n=41  W=14/L=27  WR=34.1%
- Sharpen: sharpest is session_bucket=asia (17/27 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; just touched lower band; zscore -3 to -2 deep oversold  •  ONLY when session=asia

### L12.  `H60=H60a AND BBP=BBP1 AND direction_exec=long`
- Raw: n=41  W=14/L=27  WR=34.1%
- Sharpen: sharpest is session_bucket=asia (17/27 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; just touched lower band  •  ONLY when session=asia

### L13.  `BBP=BBP1 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=41  W=14/L=27  WR=34.1%
- Sharpen: sharpest is session_bucket=asia (17/27 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: LONG**  •  just touched lower band; zscore -3 to -2 deep oversold  •  ONLY when session=asia

### L14.  `H60=H60a AND BBP=BBP1 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=41  W=14/L=27  WR=34.1%
- Sharpen: sharpest is session_bucket=asia (17/27 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; just touched lower band; zscore -3 to -2 deep oversold  •  ONLY when session=asia

### L15.  `H20=H20a AND H60=H60a AND session_bucket=ny_mid`
- Raw: n=39  W=8/L=31  WR=20.5%
- Sharpen: sharpest is ZS=ZS1 (9/31 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=ny_mid  •  ONLY when zscore -3 to -2 deep oversold

### L16.  `H20=H20a AND T1=T1c AND session_bucket=ny_mid`
- Raw: n=39  W=8/L=31  WR=20.5%
- Sharpen: sharpest is ZS=ZS1 (9/31 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; session=ny_mid  •  ONLY when zscore -3 to -2 deep oversold

### L17.  `H20=H20a AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=39  W=8/L=31  WR=20.5%
- Sharpen: sharpest is ZS=ZS1 (9/31 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; session=ny_mid  •  ONLY when zscore -3 to -2 deep oversold

### L18.  `H20=H20a AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=39  W=8/L=31  WR=20.5%
- Sharpen: sharpest is ZS=ZS1 (9/31 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; session=ny_mid  •  ONLY when zscore -3 to -2 deep oversold

### L19.  `H20=H20a AND H60=H60a AND T1=T1c AND session_bucket=ny_mid`
- Raw: n=39  W=8/L=31  WR=20.5%
- Sharpen: sharpest is ZS=ZS1 (9/31 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade; session=ny_mid  •  ONLY when zscore -3 to -2 deep oversold

### L20.  `H20=H20a AND H60=H60a AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=39  W=8/L=31  WR=20.5%
- Sharpen: sharpest is ZS=ZS1 (9/31 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend AGAINST trade; session=ny_mid  •  ONLY when zscore -3 to -2 deep oversold

### L21.  `H20=H20a AND H60=H60a AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=39  W=8/L=31  WR=20.5%
- Sharpen: sharpest is ZS=ZS1 (9/31 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=ny_mid  •  ONLY when zscore -3 to -2 deep oversold

### L22.  `H20=H20a AND T1=T1c AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=39  W=8/L=31  WR=20.5%
- Sharpen: sharpest is ZS=ZS1 (9/31 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_mid  •  ONLY when zscore -3 to -2 deep oversold

### L23.  `H20=H20a AND T1=T1c AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=39  W=8/L=31  WR=20.5%
- Sharpen: sharpest is ZS=ZS1 (9/31 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; session=ny_mid  •  ONLY when zscore -3 to -2 deep oversold

### L24.  `H20=H20a AND T4=T4c AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=39  W=8/L=31  WR=20.5%
- Sharpen: sharpest is ZS=ZS1 (9/31 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; session=ny_mid  •  ONLY when zscore -3 to -2 deep oversold

### L25.  `H60=H60a AND T1=T1c AND BBP=BBP1`
- Raw: n=39  W=12/L=27  WR=30.8%
- Sharpen: sharpest is session_bucket=asia (17/27 of losers there)
- **Sharp: n=17  W=0/L=17  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; just touched lower band  •  ONLY when session=asia

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20e(25/19) | — |
| H60 | H60e(53/45) | H60a(47/55) |
| T1 | T1a(52/45) | T1c(48/55) |
| T4 | T4a(55/44) | T4c(45/56) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(53/45) | long(47/55) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
