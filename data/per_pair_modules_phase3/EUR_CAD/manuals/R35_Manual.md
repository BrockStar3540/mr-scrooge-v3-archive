# EUR_CAD — R35 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50e**  (EMA50 down >0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **1,778**  (W=1,127 / L=651)  -  WR: **63.4%**

## Session distribution

- asia: n=610  W=383/L=227  WR=62.8%
- ny_close: n=236  W=149/L=87  WR=63.1%
- ny_open: n=217  W=126/L=91  WR=58.1%
- london_open: n=210  W=132/L=78  WR=62.9%
- london: n=192  W=125/L=67  WR=65.1%
- ny_mid: n=155  W=106/L=49  WR=68.4%
- asia_late: n=114  W=74/L=40  WR=64.9%
- off_hours: n=44  W=32/L=12  WR=72.7%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60a AND BBP=BBP2 AND session_bucket=asia`
- Raw: n=146  W=127/L=19  WR=87.0%
- Refine: no further refinement
- **Final: n=146  W=127/L=19  WR=87.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; lower third; session=asia

### W02.  `H60=H60a AND T1=T1a AND BBP=BBP2 AND session_bucket=asia`
- Raw: n=146  W=127/L=19  WR=87.0%
- Refine: no further refinement
- **Final: n=146  W=127/L=19  WR=87.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; lower third; session=asia

### W03.  `H60=H60a AND T4=T4a AND BBP=BBP2 AND session_bucket=asia`
- Raw: n=146  W=127/L=19  WR=87.0%
- Refine: no further refinement
- **Final: n=146  W=127/L=19  WR=87.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; lower third; session=asia

### W04.  `H60=H60a AND BBP=BBP2 AND direction_exec=short AND session_bucket=asia`
- Raw: n=146  W=127/L=19  WR=87.0%
- Refine: no further refinement
- **Final: n=146  W=127/L=19  WR=87.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; lower third; session=asia

### W05.  `H60=H60a AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=139  W=121/L=18  WR=87.1%
- Refine: no further refinement
- **Final: n=139  W=121/L=18  WR=87.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; zscore -2 to -1 oversold; session=asia

### W06.  `H60=H60a AND T1=T1a AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=139  W=121/L=18  WR=87.1%
- Refine: no further refinement
- **Final: n=139  W=121/L=18  WR=87.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; zscore -2 to -1 oversold; session=asia

### W07.  `H60=H60a AND T4=T4a AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=139  W=121/L=18  WR=87.1%
- Refine: no further refinement
- **Final: n=139  W=121/L=18  WR=87.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; zscore -2 to -1 oversold; session=asia

### W08.  `H60=H60a AND BBP=BBP2 AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=139  W=121/L=18  WR=87.1%
- Refine: no further refinement
- **Final: n=139  W=121/L=18  WR=87.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; lower third; zscore -2 to -1 oversold; session=asia

### W09.  `H60=H60a AND ZS=ZS2 AND direction_exec=short AND session_bucket=asia`
- Raw: n=139  W=121/L=18  WR=87.1%
- Refine: no further refinement
- **Final: n=139  W=121/L=18  WR=87.1%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; zscore -2 to -1 oversold; session=asia

### W10.  `H20=H20a AND H60=H60a AND BBP=BBP2 AND session_bucket=asia`
- Raw: n=118  W=103/L=15  WR=87.3%
- Refine: no further refinement
- **Final: n=118  W=103/L=15  WR=87.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; lower third; session=asia

### W11.  `H20=H20a AND T1=T1a AND BBP=BBP2 AND session_bucket=asia`
- Raw: n=118  W=103/L=15  WR=87.3%
- Refine: no further refinement
- **Final: n=118  W=103/L=15  WR=87.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; lower third; session=asia

### W12.  `H20=H20a AND T4=T4a AND BBP=BBP2 AND session_bucket=asia`
- Raw: n=118  W=103/L=15  WR=87.3%
- Refine: no further refinement
- **Final: n=118  W=103/L=15  WR=87.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; lower third; session=asia

### W13.  `H20=H20a AND BBP=BBP2 AND direction_exec=short AND session_bucket=asia`
- Raw: n=118  W=103/L=15  WR=87.3%
- Refine: no further refinement
- **Final: n=118  W=103/L=15  WR=87.3%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; lower third; session=asia

### W14.  `H20=H20a AND H60=H60a AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=111  W=97/L=14  WR=87.4%
- Refine: exclude strategy_id=RG1_range_bound_scalp_long drops 3/14 losers (21%)
- **Final: n=102  W=91/L=11  WR=89.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; zscore -2 to -1 oversold; session=asia  •  AVOID when strategy=RG1_range_bound_scalp_long

### W15.  `H20=H20a AND T1=T1a AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=111  W=97/L=14  WR=87.4%
- Refine: exclude strategy_id=RG1_range_bound_scalp_long drops 3/14 losers (21%)
- **Final: n=102  W=91/L=11  WR=89.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; zscore -2 to -1 oversold; session=asia  •  AVOID when strategy=RG1_range_bound_scalp_long

### W16.  `H20=H20a AND T4=T4a AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=111  W=97/L=14  WR=87.4%
- Refine: exclude strategy_id=RG1_range_bound_scalp_long drops 3/14 losers (21%)
- **Final: n=102  W=91/L=11  WR=89.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; zscore -2 to -1 oversold; session=asia  •  AVOID when strategy=RG1_range_bound_scalp_long

### W17.  `H20=H20a AND ZS=ZS2 AND direction_exec=short AND session_bucket=asia`
- Raw: n=111  W=97/L=14  WR=87.4%
- Refine: exclude strategy_id=RG1_range_bound_scalp_long drops 3/14 losers (21%)
- **Final: n=102  W=91/L=11  WR=89.2%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; zscore -2 to -1 oversold; session=asia  •  AVOID when strategy=RG1_range_bound_scalp_long

### W18.  `H20=H20a AND BBP=BBP2 AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=84  W=72/L=12  WR=85.7%
- Refine: exclude strategy_id=bravo_expansion_continuation drops 2/12 losers (17%)
- **Final: n=82  W=72/L=10  WR=87.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; lower third; RSI 30-40 weak; session=asia  •  AVOID when strategy=bravo_expansion_continuation

### W19.  `H60=H60a AND BBP=BBP2 AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=84  W=72/L=12  WR=85.7%
- Refine: exclude strategy_id=bravo_expansion_continuation drops 2/12 losers (17%)
- **Final: n=82  W=72/L=10  WR=87.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; lower third; RSI 30-40 weak; session=asia  •  AVOID when strategy=bravo_expansion_continuation

### W20.  `H20=H20a AND RSI=RSI2 AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=77  W=66/L=11  WR=85.7%
- Refine: exclude strategy_id=bravo_expansion_continuation drops 2/11 losers (18%)
- **Final: n=75  W=66/L=9  WR=88.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 30-40 weak; zscore -2 to -1 oversold; session=asia  •  AVOID when strategy=bravo_expansion_continuation

### W21.  `H60=H60a AND RSI=RSI2 AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=77  W=66/L=11  WR=85.7%
- Refine: exclude strategy_id=bravo_expansion_continuation drops 2/11 losers (18%)
- **Final: n=75  W=66/L=9  WR=88.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 30-40 weak; zscore -2 to -1 oversold; session=asia  •  AVOID when strategy=bravo_expansion_continuation

### W22.  `T1=T1a AND RSI=RSI1 AND session_bucket=ny_open`
- Raw: n=73  W=65/L=8  WR=89.0%
- Refine: exclude H20=H20b drops 6/8 losers (75%)
- **Final: n=54  W=52/L=2  WR=96.3%**
- **Dir: ?**  •  1h trend WITH trade; RSI 20-30 oversold; session=ny_open  •  AVOID when HTF20 slightly aligned

### W23.  `T4=T4a AND RSI=RSI1 AND session_bucket=ny_open`
- Raw: n=73  W=65/L=8  WR=89.0%
- Refine: exclude H20=H20b drops 6/8 losers (75%)
- **Final: n=54  W=52/L=2  WR=96.3%**
- **Dir: ?**  •  4h trend WITH trade; RSI 20-30 oversold; session=ny_open  •  AVOID when HTF20 slightly aligned

### W24.  `RSI=RSI1 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=73  W=65/L=8  WR=89.0%
- Refine: exclude H20=H20b drops 6/8 losers (75%)
- **Final: n=54  W=52/L=2  WR=96.3%**
- **Dir: SHORT**  •  RSI 20-30 oversold; session=ny_open  •  AVOID when HTF20 slightly aligned

### W25.  `T1=T1a AND T4=T4a AND RSI=RSI1 AND session_bucket=ny_open`
- Raw: n=73  W=65/L=8  WR=89.0%
- Refine: exclude H20=H20b drops 6/8 losers (75%)
- **Final: n=54  W=52/L=2  WR=96.3%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 20-30 oversold; session=ny_open  •  AVOID when HTF20 slightly aligned

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND T4=T4c AND BBP=BBP2`
- Raw: n=185  W=73/L=112  WR=39.5%
- Sharpen: sharpest is RSI=RSI1 (36/112 of losers there)
- **Sharp: n=40  W=4/L=36  WR=10.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; lower third  •  ONLY when RSI 20-30 oversold

### L02.  `H20=H20e AND H60=H60e AND T4=T4c AND BBP=BBP2`
- Raw: n=185  W=73/L=112  WR=39.5%
- Sharpen: sharpest is RSI=RSI1 (36/112 of losers there)
- **Sharp: n=40  W=4/L=36  WR=10.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; lower third  •  ONLY when RSI 20-30 oversold

### L03.  `H20=H20e AND T4=T4c AND BBP=BBP2 AND direction_exec=long`
- Raw: n=185  W=73/L=112  WR=39.5%
- Sharpen: sharpest is RSI=RSI1 (36/112 of losers there)
- **Sharp: n=40  W=4/L=36  WR=10.0%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend AGAINST trade; lower third  •  ONLY when RSI 20-30 oversold

### L04.  `H20=H20e AND T1=T1c AND BBP=BBP2`
- Raw: n=183  W=73/L=110  WR=39.9%
- Sharpen: sharpest is RSI=RSI1 (37/110 of losers there)
- **Sharp: n=44  W=7/L=37  WR=15.9%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; lower third  •  ONLY when RSI 20-30 oversold

### L05.  `H20=H20e AND H60=H60e AND T1=T1c AND BBP=BBP2`
- Raw: n=183  W=73/L=110  WR=39.9%
- Sharpen: sharpest is RSI=RSI1 (37/110 of losers there)
- **Sharp: n=44  W=7/L=37  WR=15.9%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; lower third  •  ONLY when RSI 20-30 oversold

### L06.  `H20=H20e AND T1=T1c AND BBP=BBP2 AND direction_exec=long`
- Raw: n=183  W=73/L=110  WR=39.9%
- Sharpen: sharpest is RSI=RSI1 (37/110 of losers there)
- **Sharp: n=44  W=7/L=37  WR=15.9%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade; lower third  •  ONLY when RSI 20-30 oversold

### L07.  `H20=H20e AND T1=T1c AND T4=T4c AND BBP=BBP2`
- Raw: n=177  W=68/L=109  WR=38.4%
- Sharpen: sharpest is RSI=RSI1 (36/109 of losers there)
- **Sharp: n=40  W=4/L=36  WR=10.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; lower third  •  ONLY when RSI 20-30 oversold

### L08.  `T4=T4c AND BBP=BBP2 AND session_bucket=asia`
- Raw: n=122  W=44/L=78  WR=36.1%
- Sharpen: sharpest is H60=H60e (78/78 of losers there)
- **Sharp: n=108  W=30/L=78  WR=27.8%**
- **Dir: ?**  •  4h trend AGAINST trade; lower third; session=asia  •  ONLY when HTF60 strongly against

### L09.  `T1=T1c AND BBP=BBP2 AND session_bucket=asia`
- Raw: n=119  W=39/L=80  WR=32.8%
- Sharpen: sharpest is H60=H60e (78/80 of losers there)
- **Sharp: n=108  W=30/L=78  WR=27.8%**
- **Dir: ?**  •  1h trend AGAINST trade; lower third; session=asia  •  ONLY when HTF60 strongly against

### L10.  `BBP=BBP2 AND direction_exec=long AND session_bucket=asia`
- Raw: n=119  W=39/L=80  WR=32.8%
- Sharpen: sharpest is H60=H60e (78/80 of losers there)
- **Sharp: n=108  W=30/L=78  WR=27.8%**
- **Dir: LONG**  •  lower third; session=asia  •  ONLY when HTF60 strongly against

### L11.  `T1=T1c AND BBP=BBP2 AND direction_exec=long AND session_bucket=asia`
- Raw: n=119  W=39/L=80  WR=32.8%
- Sharpen: sharpest is H60=H60e (78/80 of losers there)
- **Sharp: n=108  W=30/L=78  WR=27.8%**
- **Dir: LONG**  •  1h trend AGAINST trade; lower third; session=asia  •  ONLY when HTF60 strongly against

### L12.  `T1=T1c AND T4=T4c AND BBP=BBP2 AND session_bucket=asia`
- Raw: n=116  W=38/L=78  WR=32.8%
- Sharpen: sharpest is H60=H60e (78/78 of losers there)
- **Sharp: n=108  W=30/L=78  WR=27.8%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; lower third; session=asia  •  ONLY when HTF60 strongly against

### L13.  `T4=T4c AND BBP=BBP2 AND direction_exec=long AND session_bucket=asia`
- Raw: n=116  W=38/L=78  WR=32.8%
- Sharpen: sharpest is H60=H60e (78/78 of losers there)
- **Sharp: n=108  W=30/L=78  WR=27.8%**
- **Dir: LONG**  •  4h trend AGAINST trade; lower third; session=asia  •  ONLY when HTF60 strongly against

### L14.  `T4=T4c AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=115  W=40/L=75  WR=34.8%
- Sharpen: sharpest is H60=H60e (75/75 of losers there)
- **Sharp: n=102  W=27/L=75  WR=26.5%**
- **Dir: ?**  •  4h trend AGAINST trade; zscore -2 to -1 oversold; session=asia  •  ONLY when HTF60 strongly against

### L15.  `T4=T4c AND BBP=BBP2 AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=115  W=40/L=75  WR=34.8%
- Sharpen: sharpest is H60=H60e (75/75 of losers there)
- **Sharp: n=102  W=27/L=75  WR=26.5%**
- **Dir: ?**  •  4h trend AGAINST trade; lower third; zscore -2 to -1 oversold; session=asia  •  ONLY when HTF60 strongly against

### L16.  `T1=T1c AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=112  W=35/L=77  WR=31.2%
- Sharpen: sharpest is H60=H60e (75/77 of losers there)
- **Sharp: n=102  W=27/L=75  WR=26.5%**
- **Dir: ?**  •  1h trend AGAINST trade; zscore -2 to -1 oversold; session=asia  •  ONLY when HTF60 strongly against

### L17.  `ZS=ZS2 AND direction_exec=long AND session_bucket=asia`
- Raw: n=112  W=35/L=77  WR=31.2%
- Sharpen: sharpest is H60=H60e (75/77 of losers there)
- **Sharp: n=102  W=27/L=75  WR=26.5%**
- **Dir: LONG**  •  zscore -2 to -1 oversold; session=asia  •  ONLY when HTF60 strongly against

### L18.  `T1=T1c AND BBP=BBP2 AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=112  W=35/L=77  WR=31.2%
- Sharpen: sharpest is H60=H60e (75/77 of losers there)
- **Sharp: n=102  W=27/L=75  WR=26.5%**
- **Dir: ?**  •  1h trend AGAINST trade; lower third; zscore -2 to -1 oversold; session=asia  •  ONLY when HTF60 strongly against

### L19.  `T1=T1c AND ZS=ZS2 AND direction_exec=long AND session_bucket=asia`
- Raw: n=112  W=35/L=77  WR=31.2%
- Sharpen: sharpest is H60=H60e (75/77 of losers there)
- **Sharp: n=102  W=27/L=75  WR=26.5%**
- **Dir: LONG**  •  1h trend AGAINST trade; zscore -2 to -1 oversold; session=asia  •  ONLY when HTF60 strongly against

### L20.  `BBP=BBP2 AND ZS=ZS2 AND direction_exec=long AND session_bucket=asia`
- Raw: n=112  W=35/L=77  WR=31.2%
- Sharpen: sharpest is H60=H60e (75/77 of losers there)
- **Sharp: n=102  W=27/L=75  WR=26.5%**
- **Dir: LONG**  •  lower third; zscore -2 to -1 oversold; session=asia  •  ONLY when HTF60 strongly against

### L21.  `T1=T1c AND T4=T4c AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=109  W=34/L=75  WR=31.2%
- Sharpen: sharpest is H60=H60e (75/75 of losers there)
- **Sharp: n=102  W=27/L=75  WR=26.5%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore -2 to -1 oversold; session=asia  •  ONLY when HTF60 strongly against

### L22.  `T4=T4c AND ZS=ZS2 AND direction_exec=long AND session_bucket=asia`
- Raw: n=109  W=34/L=75  WR=31.2%
- Sharpen: sharpest is H60=H60e (75/75 of losers there)
- **Sharp: n=102  W=27/L=75  WR=26.5%**
- **Dir: LONG**  •  4h trend AGAINST trade; zscore -2 to -1 oversold; session=asia  •  ONLY when HTF60 strongly against

### L23.  `H60=H60e AND BBP=BBP2 AND session_bucket=asia`
- Raw: n=108  W=30/L=78  WR=27.8%
- Sharpen: sharpest is RSI=RSI1 (32/78 of losers there)
- **Sharp: n=36  W=4/L=32  WR=11.1%**
- **Dir: ?**  •  HTF60 strongly against; lower third; session=asia  •  ONLY when RSI 20-30 oversold

### L24.  `H60=H60e AND T1=T1c AND BBP=BBP2 AND session_bucket=asia`
- Raw: n=108  W=30/L=78  WR=27.8%
- Sharpen: sharpest is RSI=RSI1 (32/78 of losers there)
- **Sharp: n=36  W=4/L=32  WR=11.1%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; lower third; session=asia  •  ONLY when RSI 20-30 oversold

### L25.  `H60=H60e AND T4=T4c AND BBP=BBP2 AND session_bucket=asia`
- Raw: n=108  W=30/L=78  WR=27.8%
- Sharpen: sharpest is RSI=RSI1 (32/78 of losers there)
- **Sharp: n=36  W=4/L=32  WR=11.1%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; lower third; session=asia  •  ONLY when RSI 20-30 oversold

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(39/24) | H20e(26/38) |
| H60 | H60a(40/27) | H60e(27/40) |
| T1 | T1a(59/42) | T1c(41/58) |
| T4 | T4a(57/43) | T4c(43/57) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(58/43) | long(42/57) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
