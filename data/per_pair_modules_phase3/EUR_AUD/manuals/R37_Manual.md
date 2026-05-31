# EUR_AUD — R37 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_3**  (5m ATR >120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50e**  (EMA50 down >0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **2,449**  (W=1,403 / L=1,046)  -  WR: **57.3%**

## Session distribution

- ny_mid: n=1076  W=610/L=466  WR=56.7%
- asia: n=683  W=388/L=295  WR=56.8%
- london_open: n=301  W=170/L=131  WR=56.5%
- ny_open: n=193  W=117/L=76  WR=60.6%
- asia_late: n=86  W=50/L=36  WR=58.1%
- ny_close: n=80  W=51/L=29  WR=63.7%
- london: n=23  W=14/L=9  WR=60.9%
- off_hours: n=7  W=3/L=4  WR=42.9%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND H60=H60a AND session_bucket=ny_open`
- Raw: n=62  W=59/L=3  WR=95.2%
- Refine: exclude T4=T4c drops 3/3 losers (100%)
- **Final: n=53  W=53/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=ny_open  •  AVOID when 4h trend AGAINST trade

### W02.  `H20=H20a AND T1=T1a AND session_bucket=ny_open`
- Raw: n=62  W=59/L=3  WR=95.2%
- Refine: exclude T4=T4c drops 3/3 losers (100%)
- **Final: n=53  W=53/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=ny_open  •  AVOID when 4h trend AGAINST trade

### W03.  `H20=H20a AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=62  W=59/L=3  WR=95.2%
- Refine: exclude T4=T4c drops 3/3 losers (100%)
- **Final: n=53  W=53/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; session=ny_open  •  AVOID when 4h trend AGAINST trade

### W04.  `H20=H20a AND H60=H60a AND T1=T1a AND session_bucket=ny_open`
- Raw: n=62  W=59/L=3  WR=95.2%
- Refine: exclude T4=T4c drops 3/3 losers (100%)
- **Final: n=53  W=53/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; session=ny_open  •  AVOID when 4h trend AGAINST trade

### W05.  `H20=H20a AND H60=H60a AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=62  W=59/L=3  WR=95.2%
- Refine: exclude T4=T4c drops 3/3 losers (100%)
- **Final: n=53  W=53/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=ny_open  •  AVOID when 4h trend AGAINST trade

### W06.  `H20=H20a AND T1=T1a AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=62  W=59/L=3  WR=95.2%
- Refine: exclude T4=T4c drops 3/3 losers (100%)
- **Final: n=53  W=53/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=ny_open  •  AVOID when 4h trend AGAINST trade

### W07.  `T4=T4a AND RSI=RSI2 AND ZS=ZS4`
- Raw: n=61  W=53/L=8  WR=86.9%
- Refine: exclude strategy_id=bravo_expansion_continuation drops 3/8 losers (38%)
- **Final: n=52  W=47/L=5  WR=90.4%**
- **Dir: ?**  •  4h trend WITH trade; RSI 30-40 weak; zscore +1 to +2 overbought  •  AVOID when strategy=bravo_expansion_continuation

### W08.  `T4=T4a AND BBP=BBP4 AND RSI=RSI2 AND ZS=ZS4`
- Raw: n=61  W=53/L=8  WR=86.9%
- Refine: exclude strategy_id=bravo_expansion_continuation drops 3/8 losers (38%)
- **Final: n=52  W=47/L=5  WR=90.4%**
- **Dir: ?**  •  4h trend WITH trade; upper third; RSI 30-40 weak; zscore +1 to +2 overbought  •  AVOID when strategy=bravo_expansion_continuation

### W09.  `H20=H20a AND T4=T4a AND session_bucket=ny_open`
- Raw: n=53  W=53/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=53  W=53/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=ny_open

### W10.  `H20=H20a AND H60=H60a AND T4=T4a AND session_bucket=ny_open`
- Raw: n=53  W=53/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=53  W=53/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade; session=ny_open

### W11.  `H20=H20a AND T1=T1a AND T4=T4a AND session_bucket=ny_open`
- Raw: n=53  W=53/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=53  W=53/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; session=ny_open

### W12.  `H20=H20a AND T4=T4a AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=53  W=53/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=53  W=53/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=ny_open

### W13.  `H60=H60a AND T4=T4a AND RSI=RSI2 AND ZS=ZS4`
- Raw: n=50  W=43/L=7  WR=86.0%
- Refine: exclude session_bucket=asia drops 5/7 losers (71%)
- **Final: n=34  W=32/L=2  WR=94.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 30-40 weak; zscore +1 to +2 overbought  •  AVOID when session=asia

### W14.  `T1=T1a AND T4=T4a AND RSI=RSI2 AND ZS=ZS4`
- Raw: n=50  W=43/L=7  WR=86.0%
- Refine: exclude session_bucket=asia drops 5/7 losers (71%)
- **Final: n=34  W=32/L=2  WR=94.1%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 30-40 weak; zscore +1 to +2 overbought  •  AVOID when session=asia

### W15.  `T4=T4a AND RSI=RSI2 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=50  W=43/L=7  WR=86.0%
- Refine: exclude session_bucket=asia drops 5/7 losers (71%)
- **Final: n=34  W=32/L=2  WR=94.1%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 30-40 weak; zscore +1 to +2 overbought  •  AVOID when session=asia

### W16.  `H20=H20e AND RSI=RSI2 AND ZS=ZS1 AND session_bucket=ny_mid`
- Raw: n=44  W=44/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=44  W=44/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; RSI 30-40 weak; zscore -3 to -2 deep oversold; session=ny_mid

### W17.  `H20=H20a AND T4=T4a AND RSI=RSI2 AND ZS=ZS4`
- Raw: n=44  W=40/L=4  WR=90.9%
- Refine: exclude session_bucket=asia drops 3/4 losers (75%)
- **Final: n=30  W=29/L=1  WR=96.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 30-40 weak; zscore +1 to +2 overbought  •  AVOID when session=asia

### W18.  `H20=H20a AND RSI=RSI2 AND session_bucket=ny_open`
- Raw: n=37  W=37/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=37  W=37/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 30-40 weak; session=ny_open

### W19.  `H20=H20a AND H60=H60a AND RSI=RSI2 AND session_bucket=ny_open`
- Raw: n=37  W=37/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=37  W=37/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 30-40 weak; session=ny_open

### W20.  `H20=H20a AND T1=T1a AND RSI=RSI2 AND session_bucket=ny_open`
- Raw: n=37  W=37/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=37  W=37/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 30-40 weak; session=ny_open

### W21.  `H20=H20a AND T4=T4a AND RSI=RSI2 AND session_bucket=ny_open`
- Raw: n=37  W=37/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=37  W=37/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 30-40 weak; session=ny_open

### W22.  `H20=H20a AND RSI=RSI2 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=37  W=37/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=37  W=37/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 30-40 weak; session=ny_open

### W23.  `H20=H20a AND T1=T1c AND session_bucket=london_open`
- Raw: n=36  W=31/L=5  WR=86.1%
- Refine: exclude strategy_id=bravo_expansion_continuation drops 2/5 losers (40%)
- **Final: n=33  W=30/L=3  WR=90.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; session=london_open  •  AVOID when strategy=bravo_expansion_continuation

### W24.  `H20=H20a AND BBP=BBP3 AND RSI=RSI1`
- Raw: n=36  W=31/L=5  WR=86.1%
- Refine: no further refinement
- **Final: n=36  W=31/L=5  WR=86.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; middle of band; RSI 20-30 oversold

### W25.  `H60=H60a AND BBP=BBP3 AND RSI=RSI1`
- Raw: n=36  W=31/L=5  WR=86.1%
- Refine: no further refinement
- **Final: n=36  W=31/L=5  WR=86.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; middle of band; RSI 20-30 oversold

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND RSI=RSI1 AND session_bucket=asia`
- Raw: n=106  W=42/L=64  WR=39.6%
- Sharpen: sharpest is BBP=BBP2 (36/64 of losers there)
- **Sharp: n=49  W=13/L=36  WR=26.5%**
- **Dir: ?**  •  HTF20 strongly against; RSI 20-30 oversold; session=asia  •  ONLY when lower third

### L02.  `H60=H60e AND RSI=RSI1 AND session_bucket=asia`
- Raw: n=106  W=42/L=64  WR=39.6%
- Sharpen: sharpest is BBP=BBP2 (36/64 of losers there)
- **Sharp: n=49  W=13/L=36  WR=26.5%**
- **Dir: ?**  •  HTF60 strongly against; RSI 20-30 oversold; session=asia  •  ONLY when lower third

### L03.  `T1=T1c AND RSI=RSI1 AND session_bucket=asia`
- Raw: n=106  W=42/L=64  WR=39.6%
- Sharpen: sharpest is BBP=BBP2 (36/64 of losers there)
- **Sharp: n=49  W=13/L=36  WR=26.5%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 20-30 oversold; session=asia  •  ONLY when lower third

### L04.  `T4=T4c AND RSI=RSI1 AND session_bucket=asia`
- Raw: n=106  W=42/L=64  WR=39.6%
- Sharpen: sharpest is BBP=BBP2 (36/64 of losers there)
- **Sharp: n=49  W=13/L=36  WR=26.5%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 20-30 oversold; session=asia  •  ONLY when lower third

### L05.  `RSI=RSI1 AND direction_exec=long AND session_bucket=asia`
- Raw: n=106  W=42/L=64  WR=39.6%
- Sharpen: sharpest is BBP=BBP2 (36/64 of losers there)
- **Sharp: n=49  W=13/L=36  WR=26.5%**
- **Dir: LONG**  •  RSI 20-30 oversold; session=asia  •  ONLY when lower third

### L06.  `H20=H20e AND H60=H60e AND RSI=RSI1 AND session_bucket=asia`
- Raw: n=106  W=42/L=64  WR=39.6%
- Sharpen: sharpest is BBP=BBP2 (36/64 of losers there)
- **Sharp: n=49  W=13/L=36  WR=26.5%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 20-30 oversold; session=asia  •  ONLY when lower third

### L07.  `H20=H20e AND T1=T1c AND RSI=RSI1 AND session_bucket=asia`
- Raw: n=106  W=42/L=64  WR=39.6%
- Sharpen: sharpest is BBP=BBP2 (36/64 of losers there)
- **Sharp: n=49  W=13/L=36  WR=26.5%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 20-30 oversold; session=asia  •  ONLY when lower third

### L08.  `H20=H20e AND T4=T4c AND RSI=RSI1 AND session_bucket=asia`
- Raw: n=106  W=42/L=64  WR=39.6%
- Sharpen: sharpest is BBP=BBP2 (36/64 of losers there)
- **Sharp: n=49  W=13/L=36  WR=26.5%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 20-30 oversold; session=asia  •  ONLY when lower third

### L09.  `H20=H20e AND RSI=RSI1 AND direction_exec=long AND session_bucket=asia`
- Raw: n=106  W=42/L=64  WR=39.6%
- Sharpen: sharpest is BBP=BBP2 (36/64 of losers there)
- **Sharp: n=49  W=13/L=36  WR=26.5%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 20-30 oversold; session=asia  •  ONLY when lower third

### L10.  `H60=H60e AND T1=T1c AND RSI=RSI1 AND session_bucket=asia`
- Raw: n=106  W=42/L=64  WR=39.6%
- Sharpen: sharpest is BBP=BBP2 (36/64 of losers there)
- **Sharp: n=49  W=13/L=36  WR=26.5%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 20-30 oversold; session=asia  •  ONLY when lower third

### L11.  `H60=H60e AND T4=T4c AND RSI=RSI1 AND session_bucket=asia`
- Raw: n=106  W=42/L=64  WR=39.6%
- Sharpen: sharpest is BBP=BBP2 (36/64 of losers there)
- **Sharp: n=49  W=13/L=36  WR=26.5%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 20-30 oversold; session=asia  •  ONLY when lower third

### L12.  `H60=H60e AND RSI=RSI1 AND direction_exec=long AND session_bucket=asia`
- Raw: n=106  W=42/L=64  WR=39.6%
- Sharpen: sharpest is BBP=BBP2 (36/64 of losers there)
- **Sharp: n=49  W=13/L=36  WR=26.5%**
- **Dir: LONG**  •  HTF60 strongly against; RSI 20-30 oversold; session=asia  •  ONLY when lower third

### L13.  `T1=T1c AND T4=T4c AND RSI=RSI1 AND session_bucket=asia`
- Raw: n=106  W=42/L=64  WR=39.6%
- Sharpen: sharpest is BBP=BBP2 (36/64 of losers there)
- **Sharp: n=49  W=13/L=36  WR=26.5%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 20-30 oversold; session=asia  •  ONLY when lower third

### L14.  `T1=T1c AND RSI=RSI1 AND direction_exec=long AND session_bucket=asia`
- Raw: n=106  W=42/L=64  WR=39.6%
- Sharpen: sharpest is BBP=BBP2 (36/64 of losers there)
- **Sharp: n=49  W=13/L=36  WR=26.5%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 20-30 oversold; session=asia  •  ONLY when lower third

### L15.  `T4=T4c AND RSI=RSI1 AND direction_exec=long AND session_bucket=asia`
- Raw: n=106  W=42/L=64  WR=39.6%
- Sharpen: sharpest is BBP=BBP2 (36/64 of losers there)
- **Sharp: n=49  W=13/L=36  WR=26.5%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 20-30 oversold; session=asia  •  ONLY when lower third

### L16.  `H60=H60a AND T1=T1a AND T4=T4c`
- Raw: n=93  W=37/L=56  WR=39.8%
- Sharpen: sharpest is session_bucket=asia (10/56 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade  •  ONLY when session=asia

### L17.  `H60=H60a AND T4=T4c AND direction_exec=short`
- Raw: n=93  W=37/L=56  WR=39.8%
- Sharpen: sharpest is session_bucket=asia (10/56 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade  •  ONLY when session=asia

### L18.  `T1=T1a AND T4=T4c AND direction_exec=short`
- Raw: n=93  W=37/L=56  WR=39.8%
- Sharpen: sharpest is session_bucket=asia (10/56 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend AGAINST trade  •  ONLY when session=asia

### L19.  `H60=H60a AND T1=T1a AND T4=T4c AND direction_exec=short`
- Raw: n=93  W=37/L=56  WR=39.8%
- Sharpen: sharpest is session_bucket=asia (10/56 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade  •  ONLY when session=asia

### L20.  `T1=T1c AND T4=T4c AND BBP=BBP4`
- Raw: n=92  W=36/L=56  WR=39.1%
- Sharpen: sharpest is ZS=ZS4 (42/56 of losers there)
- **Sharp: n=62  W=20/L=42  WR=32.3%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; upper third  •  ONLY when zscore +1 to +2 overbought

### L21.  `T1=T1c AND T4=T4c AND BBP=BBP4 AND direction_exec=long`
- Raw: n=92  W=36/L=56  WR=39.1%
- Sharpen: sharpest is ZS=ZS4 (42/56 of losers there)
- **Sharp: n=62  W=20/L=42  WR=32.3%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; upper third  •  ONLY when zscore +1 to +2 overbought

### L22.  `H60=H60e AND T1=T1c AND session_bucket=ny_open`
- Raw: n=88  W=34/L=54  WR=38.6%
- Sharpen: sharpest is H20=H20e (38/54 of losers there)
- **Sharp: n=41  W=3/L=38  WR=7.3%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; session=ny_open  •  ONLY when HTF20 strongly against

### L23.  `H60=H60e AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=88  W=34/L=54  WR=38.6%
- Sharpen: sharpest is H20=H20e (38/54 of losers there)
- **Sharp: n=41  W=3/L=38  WR=7.3%**
- **Dir: LONG**  •  HTF60 strongly against; session=ny_open  •  ONLY when HTF20 strongly against

### L24.  `T1=T1c AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=88  W=34/L=54  WR=38.6%
- Sharpen: sharpest is H20=H20e (38/54 of losers there)
- **Sharp: n=41  W=3/L=38  WR=7.3%**
- **Dir: LONG**  •  1h trend AGAINST trade; session=ny_open  •  ONLY when HTF20 strongly against

### L25.  `H60=H60e AND T1=T1c AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=88  W=34/L=54  WR=38.6%
- Sharpen: sharpest is H20=H20e (38/54 of losers there)
- **Sharp: n=41  W=3/L=38  WR=7.3%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend AGAINST trade; session=ny_open  •  ONLY when HTF20 strongly against

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | H20e(42/47) |
| H60 | — | — |
| T1 | — | — |
| T4 | T4a(54/46) | T4c(46/54) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
