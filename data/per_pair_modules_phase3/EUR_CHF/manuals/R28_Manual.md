# EUR_CHF — R28 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_0**  (5m ATR <33% stop)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20d**  (EMA20 down 0.15-0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **829**  (W=533 / L=296)  -  WR: **64.3%**

## Session distribution

- ny_close: n=201  W=137/L=64  WR=68.2%
- ny_open: n=182  W=111/L=71  WR=61.0%
- asia: n=176  W=118/L=58  WR=67.0%
- ny_mid: n=119  W=70/L=49  WR=58.8%
- london_open: n=96  W=66/L=30  WR=68.8%
- london: n=33  W=17/L=16  WR=51.5%
- off_hours: n=16  W=12/L=4  WR=75.0%
- asia_late: n=6  W=2/L=4  WR=33.3%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20d AND T1=T1a AND T4=T4a`
- Raw: n=76  W=66/L=10  WR=86.8%
- Refine: exclude H60=H60b drops 8/10 losers (80%)
- **Final: n=52  W=50/L=2  WR=96.2%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when HTF60 slightly aligned

### W02.  `H20=H20d AND T1=T1a AND direction_exec=short`
- Raw: n=76  W=66/L=10  WR=86.8%
- Refine: exclude H60=H60b drops 8/10 losers (80%)
- **Final: n=52  W=50/L=2  WR=96.2%**
- **Dir: SHORT**  •  HTF20 mildly against; 1h trend WITH trade  •  AVOID when HTF60 slightly aligned

### W03.  `H20=H20d AND T4=T4a AND direction_exec=short`
- Raw: n=76  W=66/L=10  WR=86.8%
- Refine: exclude H60=H60b drops 8/10 losers (80%)
- **Final: n=52  W=50/L=2  WR=96.2%**
- **Dir: SHORT**  •  HTF20 mildly against; 4h trend WITH trade  •  AVOID when HTF60 slightly aligned

### W04.  `H20=H20d AND T1=T1a AND T4=T4a AND direction_exec=short`
- Raw: n=76  W=66/L=10  WR=86.8%
- Refine: exclude H60=H60b drops 8/10 losers (80%)
- **Final: n=52  W=50/L=2  WR=96.2%**
- **Dir: SHORT**  •  HTF20 mildly against; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when HTF60 slightly aligned

### W05.  `H60=H60c AND T1=T1c AND T4=T4c`
- Raw: n=75  W=67/L=8  WR=89.3%
- Refine: exclude ZS=ZS4 drops 6/8 losers (75%)
- **Final: n=61  W=59/L=2  WR=96.7%**
- **Dir: ?**  •  HTF60 neutral; 1h trend AGAINST trade; 4h trend AGAINST trade  •  AVOID when zscore +1 to +2 overbought

### W06.  `H60=H60c AND T1=T1c AND direction_exec=long`
- Raw: n=75  W=67/L=8  WR=89.3%
- Refine: exclude ZS=ZS4 drops 6/8 losers (75%)
- **Final: n=61  W=59/L=2  WR=96.7%**
- **Dir: LONG**  •  HTF60 neutral; 1h trend AGAINST trade  •  AVOID when zscore +1 to +2 overbought

### W07.  `H60=H60c AND T4=T4c AND direction_exec=long`
- Raw: n=75  W=67/L=8  WR=89.3%
- Refine: exclude ZS=ZS4 drops 6/8 losers (75%)
- **Final: n=61  W=59/L=2  WR=96.7%**
- **Dir: LONG**  •  HTF60 neutral; 4h trend AGAINST trade  •  AVOID when zscore +1 to +2 overbought

### W08.  `H60=H60c AND T1=T1c AND T4=T4c AND direction_exec=long`
- Raw: n=75  W=67/L=8  WR=89.3%
- Refine: exclude ZS=ZS4 drops 6/8 losers (75%)
- **Final: n=61  W=59/L=2  WR=96.7%**
- **Dir: LONG**  •  HTF60 neutral; 1h trend AGAINST trade; 4h trend AGAINST trade  •  AVOID when zscore +1 to +2 overbought

### W09.  `H20=H20e AND H60=H60e AND session_bucket=asia`
- Raw: n=71  W=61/L=10  WR=85.9%
- Refine: exclude RSI=RSI1 drops 10/10 losers (100%)
- **Final: n=22  W=22/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; session=asia  •  AVOID when RSI 20-30 oversold

### W10.  `H20=H20e AND T1=T1c AND session_bucket=asia`
- Raw: n=71  W=61/L=10  WR=85.9%
- Refine: exclude RSI=RSI1 drops 10/10 losers (100%)
- **Final: n=22  W=22/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; session=asia  •  AVOID when RSI 20-30 oversold

### W11.  `H20=H20e AND T4=T4c AND session_bucket=asia`
- Raw: n=71  W=61/L=10  WR=85.9%
- Refine: exclude RSI=RSI1 drops 10/10 losers (100%)
- **Final: n=22  W=22/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; session=asia  •  AVOID when RSI 20-30 oversold

### W12.  `H20=H20e AND direction_exec=long AND session_bucket=asia`
- Raw: n=71  W=61/L=10  WR=85.9%
- Refine: exclude RSI=RSI1 drops 10/10 losers (100%)
- **Final: n=22  W=22/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 strongly against; session=asia  •  AVOID when RSI 20-30 oversold

### W13.  `H20=H20e AND H60=H60e AND T1=T1c AND session_bucket=asia`
- Raw: n=71  W=61/L=10  WR=85.9%
- Refine: exclude RSI=RSI1 drops 10/10 losers (100%)
- **Final: n=22  W=22/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; session=asia  •  AVOID when RSI 20-30 oversold

### W14.  `H20=H20e AND H60=H60e AND T4=T4c AND session_bucket=asia`
- Raw: n=71  W=61/L=10  WR=85.9%
- Refine: exclude RSI=RSI1 drops 10/10 losers (100%)
- **Final: n=22  W=22/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; session=asia  •  AVOID when RSI 20-30 oversold

### W15.  `H20=H20e AND H60=H60e AND direction_exec=long AND session_bucket=asia`
- Raw: n=71  W=61/L=10  WR=85.9%
- Refine: exclude RSI=RSI1 drops 10/10 losers (100%)
- **Final: n=22  W=22/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 strongly against; session=asia  •  AVOID when RSI 20-30 oversold

### W16.  `H20=H20e AND T1=T1c AND T4=T4c AND session_bucket=asia`
- Raw: n=71  W=61/L=10  WR=85.9%
- Refine: exclude RSI=RSI1 drops 10/10 losers (100%)
- **Final: n=22  W=22/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; session=asia  •  AVOID when RSI 20-30 oversold

### W17.  `H20=H20e AND T1=T1c AND direction_exec=long AND session_bucket=asia`
- Raw: n=71  W=61/L=10  WR=85.9%
- Refine: exclude RSI=RSI1 drops 10/10 losers (100%)
- **Final: n=22  W=22/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade; session=asia  •  AVOID when RSI 20-30 oversold

### W18.  `H20=H20e AND T4=T4c AND direction_exec=long AND session_bucket=asia`
- Raw: n=71  W=61/L=10  WR=85.9%
- Refine: exclude RSI=RSI1 drops 10/10 losers (100%)
- **Final: n=22  W=22/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend AGAINST trade; session=asia  •  AVOID when RSI 20-30 oversold

### W19.  `T1=T1c AND RSI=RSI1 AND session_bucket=asia`
- Raw: n=67  W=57/L=10  WR=85.1%
- Refine: exclude H20=H20e drops 10/10 losers (100%)
- **Final: n=18  W=18/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 20-30 oversold; session=asia  •  AVOID when HTF20 strongly against

### W20.  `T4=T4c AND RSI=RSI1 AND session_bucket=asia`
- Raw: n=67  W=57/L=10  WR=85.1%
- Refine: exclude H20=H20e drops 10/10 losers (100%)
- **Final: n=18  W=18/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 20-30 oversold; session=asia  •  AVOID when HTF20 strongly against

### W21.  `RSI=RSI1 AND direction_exec=long AND session_bucket=asia`
- Raw: n=67  W=57/L=10  WR=85.1%
- Refine: exclude H20=H20e drops 10/10 losers (100%)
- **Final: n=18  W=18/L=0  WR=100.0%**
- **Dir: LONG**  •  RSI 20-30 oversold; session=asia  •  AVOID when HTF20 strongly against

### W22.  `T1=T1c AND T4=T4c AND RSI=RSI1 AND session_bucket=asia`
- Raw: n=67  W=57/L=10  WR=85.1%
- Refine: exclude H20=H20e drops 10/10 losers (100%)
- **Final: n=18  W=18/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 20-30 oversold; session=asia  •  AVOID when HTF20 strongly against

### W23.  `T1=T1c AND RSI=RSI1 AND direction_exec=long AND session_bucket=asia`
- Raw: n=67  W=57/L=10  WR=85.1%
- Refine: exclude H20=H20e drops 10/10 losers (100%)
- **Final: n=18  W=18/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 20-30 oversold; session=asia  •  AVOID when HTF20 strongly against

### W24.  `T4=T4c AND RSI=RSI1 AND direction_exec=long AND session_bucket=asia`
- Raw: n=67  W=57/L=10  WR=85.1%
- Refine: exclude H20=H20e drops 10/10 losers (100%)
- **Final: n=18  W=18/L=0  WR=100.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 20-30 oversold; session=asia  •  AVOID when HTF20 strongly against

### W25.  `T1=T1a AND T4=T4a AND session_bucket=london_open`
- Raw: n=62  W=60/L=2  WR=96.8%
- Refine: exclude H20=H20e drops 2/2 losers (100%)
- **Final: n=60  W=60/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; session=london_open  •  AVOID when HTF20 strongly against

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60c AND T1=T1a AND T4=T4a`
- Raw: n=62  W=18/L=44  WR=29.0%
- Sharpen: sharpest is BBP=BBP1 (10/44 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: ?**  •  HTF60 neutral; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when just touched lower band

### L02.  `H60=H60c AND T1=T1a AND direction_exec=short`
- Raw: n=62  W=18/L=44  WR=29.0%
- Sharpen: sharpest is BBP=BBP1 (10/44 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: SHORT**  •  HTF60 neutral; 1h trend WITH trade  •  ONLY when just touched lower band

### L03.  `H60=H60c AND T4=T4a AND direction_exec=short`
- Raw: n=62  W=18/L=44  WR=29.0%
- Sharpen: sharpest is BBP=BBP1 (10/44 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: SHORT**  •  HTF60 neutral; 4h trend WITH trade  •  ONLY when just touched lower band

### L04.  `H60=H60c AND T1=T1a AND T4=T4a AND direction_exec=short`
- Raw: n=62  W=18/L=44  WR=29.0%
- Sharpen: sharpest is BBP=BBP1 (10/44 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: SHORT**  •  HTF60 neutral; 1h trend WITH trade; 4h trend WITH trade  •  ONLY when just touched lower band

### L05.  `H20=H20b AND T1=T1c AND T4=T4c`
- Raw: n=62  W=24/L=38  WR=38.7%
- Sharpen: sharpest is H60=H60e (31/38 of losers there)
- **Sharp: n=38  W=7/L=31  WR=18.4%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when HTF60 strongly against

### L06.  `H20=H20b AND T1=T1c AND direction_exec=long`
- Raw: n=62  W=24/L=38  WR=38.7%
- Sharpen: sharpest is H60=H60e (31/38 of losers there)
- **Sharp: n=38  W=7/L=31  WR=18.4%**
- **Dir: LONG**  •  HTF20 slightly aligned; 1h trend AGAINST trade  •  ONLY when HTF60 strongly against

### L07.  `H20=H20b AND T4=T4c AND direction_exec=long`
- Raw: n=62  W=24/L=38  WR=38.7%
- Sharpen: sharpest is H60=H60e (31/38 of losers there)
- **Sharp: n=38  W=7/L=31  WR=18.4%**
- **Dir: LONG**  •  HTF20 slightly aligned; 4h trend AGAINST trade  •  ONLY when HTF60 strongly against

### L08.  `H20=H20b AND T1=T1c AND T4=T4c AND direction_exec=long`
- Raw: n=62  W=24/L=38  WR=38.7%
- Sharpen: sharpest is H60=H60e (31/38 of losers there)
- **Sharp: n=38  W=7/L=31  WR=18.4%**
- **Dir: LONG**  •  HTF20 slightly aligned; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when HTF60 strongly against

### L09.  `H20=H20a AND H60=H60a AND session_bucket=asia`
- Raw: n=41  W=11/L=30  WR=26.8%
- Sharpen: sharpest is RSI=RSI2 (12/30 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=asia  •  ONLY when RSI 30-40 weak

### L10.  `H20=H20a AND T1=T1a AND session_bucket=asia`
- Raw: n=41  W=11/L=30  WR=26.8%
- Sharpen: sharpest is RSI=RSI2 (12/30 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=asia  •  ONLY when RSI 30-40 weak

### L11.  `H20=H20a AND T4=T4a AND session_bucket=asia`
- Raw: n=41  W=11/L=30  WR=26.8%
- Sharpen: sharpest is RSI=RSI2 (12/30 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=asia  •  ONLY when RSI 30-40 weak

### L12.  `H20=H20a AND direction_exec=short AND session_bucket=asia`
- Raw: n=41  W=11/L=30  WR=26.8%
- Sharpen: sharpest is RSI=RSI2 (12/30 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; session=asia  •  ONLY when RSI 30-40 weak

### L13.  `H60=H60c AND T1=T1a AND RSI=RSI2`
- Raw: n=41  W=11/L=30  WR=26.8%
- Sharpen: sharpest is session_bucket=ny_close (19/30 of losers there)
- **Sharp: n=22  W=3/L=19  WR=13.6%**
- **Dir: ?**  •  HTF60 neutral; 1h trend WITH trade; RSI 30-40 weak  •  ONLY when session=ny_close

### L14.  `H60=H60c AND T4=T4a AND RSI=RSI2`
- Raw: n=41  W=11/L=30  WR=26.8%
- Sharpen: sharpest is session_bucket=ny_close (19/30 of losers there)
- **Sharp: n=22  W=3/L=19  WR=13.6%**
- **Dir: ?**  •  HTF60 neutral; 4h trend WITH trade; RSI 30-40 weak  •  ONLY when session=ny_close

### L15.  `H60=H60c AND RSI=RSI2 AND direction_exec=short`
- Raw: n=41  W=11/L=30  WR=26.8%
- Sharpen: sharpest is session_bucket=ny_close (19/30 of losers there)
- **Sharp: n=22  W=3/L=19  WR=13.6%**
- **Dir: SHORT**  •  HTF60 neutral; RSI 30-40 weak  •  ONLY when session=ny_close

### L16.  `H20=H20a AND H60=H60a AND T1=T1a AND session_bucket=asia`
- Raw: n=41  W=11/L=30  WR=26.8%
- Sharpen: sharpest is RSI=RSI2 (12/30 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; session=asia  •  ONLY when RSI 30-40 weak

### L17.  `H20=H20a AND H60=H60a AND T4=T4a AND session_bucket=asia`
- Raw: n=41  W=11/L=30  WR=26.8%
- Sharpen: sharpest is RSI=RSI2 (12/30 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade; session=asia  •  ONLY when RSI 30-40 weak

### L18.  `H20=H20a AND H60=H60a AND direction_exec=short AND session_bucket=asia`
- Raw: n=41  W=11/L=30  WR=26.8%
- Sharpen: sharpest is RSI=RSI2 (12/30 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=asia  •  ONLY when RSI 30-40 weak

### L19.  `H20=H20a AND T1=T1a AND T4=T4a AND session_bucket=asia`
- Raw: n=41  W=11/L=30  WR=26.8%
- Sharpen: sharpest is RSI=RSI2 (12/30 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; session=asia  •  ONLY when RSI 30-40 weak

### L20.  `H20=H20a AND T1=T1a AND direction_exec=short AND session_bucket=asia`
- Raw: n=41  W=11/L=30  WR=26.8%
- Sharpen: sharpest is RSI=RSI2 (12/30 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=asia  •  ONLY when RSI 30-40 weak

### L21.  `H20=H20a AND T4=T4a AND direction_exec=short AND session_bucket=asia`
- Raw: n=41  W=11/L=30  WR=26.8%
- Sharpen: sharpest is RSI=RSI2 (12/30 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=asia  •  ONLY when RSI 30-40 weak

### L22.  `H60=H60c AND T1=T1a AND T4=T4a AND RSI=RSI2`
- Raw: n=41  W=11/L=30  WR=26.8%
- Sharpen: sharpest is session_bucket=ny_close (19/30 of losers there)
- **Sharp: n=22  W=3/L=19  WR=13.6%**
- **Dir: ?**  •  HTF60 neutral; 1h trend WITH trade; 4h trend WITH trade; RSI 30-40 weak  •  ONLY when session=ny_close

### L23.  `H60=H60c AND T1=T1a AND RSI=RSI2 AND direction_exec=short`
- Raw: n=41  W=11/L=30  WR=26.8%
- Sharpen: sharpest is session_bucket=ny_close (19/30 of losers there)
- **Sharp: n=22  W=3/L=19  WR=13.6%**
- **Dir: SHORT**  •  HTF60 neutral; 1h trend WITH trade; RSI 30-40 weak  •  ONLY when session=ny_close

### L24.  `H60=H60c AND T4=T4a AND RSI=RSI2 AND direction_exec=short`
- Raw: n=41  W=11/L=30  WR=26.8%
- Sharpen: sharpest is session_bucket=ny_close (19/30 of losers there)
- **Sharp: n=22  W=3/L=19  WR=13.6%**
- **Dir: SHORT**  •  HTF60 neutral; 4h trend WITH trade; RSI 30-40 weak  •  ONLY when session=ny_close

### L25.  `H20=H20b AND H60=H60e AND T1=T1c`
- Raw: n=38  W=7/L=31  WR=18.4%
- Sharpen: sharpest is session_bucket=ny_open (13/31 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 strongly against; 1h trend AGAINST trade  •  ONLY when session=ny_open

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20d(12/3) | H20b(5/13) |
| H60 | H60a(37/22) | H60e(24/38) |
| T1 | T1a(56/42) | T1c(44/58) |
| T4 | T4a(51/46) | T4c(49/54) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(55/44) | long(45/56) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
