# AUD_JPY — R21 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_3**  (5m ATR >120%)
- **A1 = A1_2**  (1h ATR 4-8x)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR5**  (>110% overshoot)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **3,381**  (W=1,835 / L=1,546)  -  WR: **54.3%**

## Session distribution

- asia: n=968  W=538/L=430  WR=55.6%
- ny_mid: n=842  W=429/L=413  WR=51.0%
- ny_close: n=486  W=276/L=210  WR=56.8%
- london_open: n=407  W=235/L=172  WR=57.7%
- ny_open: n=274  W=153/L=121  WR=55.8%
- london: n=241  W=107/L=134  WR=44.4%
- asia_late: n=93  W=57/L=36  WR=61.3%
- off_hours: n=70  W=40/L=30  WR=57.1%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20e AND RSI=RSI2 AND session_bucket=london_open`
- Raw: n=53  W=53/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=53  W=53/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; RSI 30-40 weak; session=london_open

### W02.  `H60=H60e AND RSI=RSI2 AND session_bucket=london_open`
- Raw: n=53  W=53/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=53  W=53/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; RSI 30-40 weak; session=london_open

### W03.  `T1=T1a AND RSI=RSI2 AND session_bucket=london_open`
- Raw: n=53  W=53/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=53  W=53/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; RSI 30-40 weak; session=london_open

### W04.  `T4=T4a AND RSI=RSI2 AND session_bucket=london_open`
- Raw: n=53  W=53/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=53  W=53/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend WITH trade; RSI 30-40 weak; session=london_open

### W05.  `RSI=RSI2 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=53  W=53/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=53  W=53/L=0  WR=100.0%**
- **Dir: SHORT**  •  RSI 30-40 weak; session=london_open

### W06.  `H20=H20e AND H60=H60e AND RSI=RSI2 AND session_bucket=london_open`
- Raw: n=53  W=53/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=53  W=53/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 30-40 weak; session=london_open

### W07.  `H20=H20e AND T1=T1a AND RSI=RSI2 AND session_bucket=london_open`
- Raw: n=53  W=53/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=53  W=53/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; RSI 30-40 weak; session=london_open

### W08.  `H20=H20e AND T4=T4a AND RSI=RSI2 AND session_bucket=london_open`
- Raw: n=53  W=53/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=53  W=53/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; RSI 30-40 weak; session=london_open

### W09.  `H20=H20e AND RSI=RSI2 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=53  W=53/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=53  W=53/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 30-40 weak; session=london_open

### W10.  `H60=H60e AND T1=T1a AND RSI=RSI2 AND session_bucket=london_open`
- Raw: n=53  W=53/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=53  W=53/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; RSI 30-40 weak; session=london_open

### W11.  `H60=H60e AND T4=T4a AND RSI=RSI2 AND session_bucket=london_open`
- Raw: n=53  W=53/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=53  W=53/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; RSI 30-40 weak; session=london_open

### W12.  `H60=H60e AND RSI=RSI2 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=53  W=53/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=53  W=53/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 30-40 weak; session=london_open

### W13.  `T1=T1a AND T4=T4a AND RSI=RSI2 AND session_bucket=london_open`
- Raw: n=53  W=53/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=53  W=53/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 30-40 weak; session=london_open

### W14.  `T1=T1a AND RSI=RSI2 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=53  W=53/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=53  W=53/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 30-40 weak; session=london_open

### W15.  `T4=T4a AND RSI=RSI2 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=53  W=53/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=53  W=53/L=0  WR=100.0%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 30-40 weak; session=london_open

### W16.  `H60=H60e AND RSI=RSI2 AND strategy_id=alpha_pullback_v2`
- Raw: n=51  W=45/L=6  WR=88.2%
- Refine: exclude ZS=ZS1 drops 3/6 losers (50%)
- **Final: n=35  W=32/L=3  WR=91.4%**
- **Dir: ?**  •  HTF60 strongly against; RSI 30-40 weak; strategy=alpha_pullback_v2  •  AVOID when zscore -3 to -2 deep oversold

### W17.  `RSI=RSI2 AND strategy_id=alpha_pullback_v2 AND direction_exec=short`
- Raw: n=51  W=45/L=6  WR=88.2%
- Refine: exclude ZS=ZS1 drops 3/6 losers (50%)
- **Final: n=35  W=32/L=3  WR=91.4%**
- **Dir: SHORT**  •  RSI 30-40 weak; strategy=alpha_pullback_v2  •  AVOID when zscore -3 to -2 deep oversold

### W18.  `H60=H60e AND RSI=RSI2 AND strategy_id=alpha_pullback_v2 AND direction_exec=short`
- Raw: n=51  W=45/L=6  WR=88.2%
- Refine: exclude ZS=ZS1 drops 3/6 losers (50%)
- **Final: n=35  W=32/L=3  WR=91.4%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 30-40 weak; strategy=alpha_pullback_v2  •  AVOID when zscore -3 to -2 deep oversold

### W19.  `H60=H60e AND T1=T1c AND BBP=BBP2 AND RSI=RSI2`
- Raw: n=48  W=42/L=6  WR=87.5%
- Refine: exclude H20=H20b drops 6/6 losers (100%)
- **Final: n=23  W=23/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; lower third; RSI 30-40 weak  •  AVOID when HTF20 slightly aligned

### W20.  `H60=H60e AND T1=T1c AND RSI=RSI2 AND ZS=ZS2`
- Raw: n=48  W=42/L=6  WR=87.5%
- Refine: exclude H20=H20b drops 6/6 losers (100%)
- **Final: n=23  W=23/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 30-40 weak; zscore -2 to -1 oversold  •  AVOID when HTF20 slightly aligned

### W21.  `H60=H60e AND T1=T1c AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=48  W=42/L=6  WR=87.5%
- Refine: exclude H20=H20b drops 6/6 losers (100%)
- **Final: n=23  W=23/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; zscore -2 to -1 oversold; session=asia  •  AVOID when HTF20 slightly aligned

### W22.  `T1=T1c AND BBP=BBP2 AND RSI=RSI2 AND direction_exec=short`
- Raw: n=48  W=42/L=6  WR=87.5%
- Refine: exclude H20=H20b drops 6/6 losers (100%)
- **Final: n=23  W=23/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; lower third; RSI 30-40 weak  •  AVOID when HTF20 slightly aligned

### W23.  `T1=T1c AND RSI=RSI2 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=48  W=42/L=6  WR=87.5%
- Refine: exclude H20=H20b drops 6/6 losers (100%)
- **Final: n=23  W=23/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 30-40 weak; zscore -2 to -1 oversold  •  AVOID when HTF20 slightly aligned

### W24.  `T1=T1c AND ZS=ZS2 AND direction_exec=short AND session_bucket=asia`
- Raw: n=48  W=42/L=6  WR=87.5%
- Refine: exclude H20=H20b drops 6/6 losers (100%)
- **Final: n=23  W=23/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; zscore -2 to -1 oversold; session=asia  •  AVOID when HTF20 slightly aligned

### W25.  `H60=H60e AND T1=T1a AND RSI=RSI2 AND strategy_id=alpha_pullback_v2`
- Raw: n=46  W=41/L=5  WR=89.1%
- Refine: exclude ZS=ZS2 drops 2/5 losers (40%)
- **Final: n=36  W=33/L=3  WR=91.7%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; RSI 30-40 weak; strategy=alpha_pullback_v2  •  AVOID when zscore -2 to -1 oversold

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20a AND H60=H60a AND session_bucket=ny_mid`
- Raw: n=367  W=146/L=221  WR=39.8%
- Sharpen: sharpest is ZS=ZS1 (99/221 of losers there)
- **Sharp: n=142  W=43/L=99  WR=30.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=ny_mid  •  ONLY when zscore -3 to -2 deep oversold

### L02.  `H20=H20a AND T1=T1c AND session_bucket=ny_mid`
- Raw: n=367  W=146/L=221  WR=39.8%
- Sharpen: sharpest is ZS=ZS1 (99/221 of losers there)
- **Sharp: n=142  W=43/L=99  WR=30.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; session=ny_mid  •  ONLY when zscore -3 to -2 deep oversold

### L03.  `H20=H20a AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=367  W=146/L=221  WR=39.8%
- Sharpen: sharpest is ZS=ZS1 (99/221 of losers there)
- **Sharp: n=142  W=43/L=99  WR=30.3%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; session=ny_mid  •  ONLY when zscore -3 to -2 deep oversold

### L04.  `H20=H20a AND H60=H60a AND T1=T1c AND session_bucket=ny_mid`
- Raw: n=367  W=146/L=221  WR=39.8%
- Sharpen: sharpest is ZS=ZS1 (99/221 of losers there)
- **Sharp: n=142  W=43/L=99  WR=30.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade; session=ny_mid  •  ONLY when zscore -3 to -2 deep oversold

### L05.  `H20=H20a AND H60=H60a AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=367  W=146/L=221  WR=39.8%
- Sharpen: sharpest is ZS=ZS1 (99/221 of losers there)
- **Sharp: n=142  W=43/L=99  WR=30.3%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=ny_mid  •  ONLY when zscore -3 to -2 deep oversold

### L06.  `H20=H20a AND T1=T1c AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=367  W=146/L=221  WR=39.8%
- Sharpen: sharpest is ZS=ZS1 (99/221 of losers there)
- **Sharp: n=142  W=43/L=99  WR=30.3%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; session=ny_mid  •  ONLY when zscore -3 to -2 deep oversold

### L07.  `H60=H60a AND T4=T4c AND ZS=ZS2`
- Raw: n=296  W=118/L=178  WR=39.9%
- Sharpen: sharpest is RSI=RSI0 (34/178 of losers there)
- **Sharp: n=37  W=3/L=34  WR=8.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; zscore -2 to -1 oversold  •  ONLY when RSI<20 extreme oversold

### L08.  `T4=T4c AND ZS=ZS2 AND direction_exec=long`
- Raw: n=296  W=118/L=178  WR=39.9%
- Sharpen: sharpest is RSI=RSI0 (34/178 of losers there)
- **Sharp: n=37  W=3/L=34  WR=8.1%**
- **Dir: LONG**  •  4h trend AGAINST trade; zscore -2 to -1 oversold  •  ONLY when RSI<20 extreme oversold

### L09.  `H60=H60a AND T4=T4c AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=296  W=118/L=178  WR=39.9%
- Sharpen: sharpest is RSI=RSI0 (34/178 of losers there)
- **Sharp: n=37  W=3/L=34  WR=8.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; lower third; zscore -2 to -1 oversold  •  ONLY when RSI<20 extreme oversold

### L10.  `H60=H60a AND T4=T4c AND ZS=ZS2 AND direction_exec=long`
- Raw: n=296  W=118/L=178  WR=39.9%
- Sharpen: sharpest is RSI=RSI0 (34/178 of losers there)
- **Sharp: n=37  W=3/L=34  WR=8.1%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; zscore -2 to -1 oversold  •  ONLY when RSI<20 extreme oversold

### L11.  `T4=T4c AND BBP=BBP2 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=296  W=118/L=178  WR=39.9%
- Sharpen: sharpest is RSI=RSI0 (34/178 of losers there)
- **Sharp: n=37  W=3/L=34  WR=8.1%**
- **Dir: LONG**  •  4h trend AGAINST trade; lower third; zscore -2 to -1 oversold  •  ONLY when RSI<20 extreme oversold

### L12.  `H60=H60a AND T4=T4c AND BBP=BBP2 AND RSI=RSI2`
- Raw: n=202  W=74/L=128  WR=36.6%
- Sharpen: sharpest is session_bucket=london_open (22/128 of losers there)
- **Sharp: n=22  W=0/L=22  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; lower third; RSI 30-40 weak  •  ONLY when session=london_open

### L13.  `T4=T4c AND BBP=BBP2 AND RSI=RSI2 AND direction_exec=long`
- Raw: n=202  W=74/L=128  WR=36.6%
- Sharpen: sharpest is session_bucket=london_open (22/128 of losers there)
- **Sharp: n=22  W=0/L=22  WR=0.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; lower third; RSI 30-40 weak  •  ONLY when session=london_open

### L14.  `H60=H60a AND T4=T4c AND RSI=RSI2 AND ZS=ZS2`
- Raw: n=182  W=68/L=114  WR=37.4%
- Sharpen: sharpest is session_bucket=london_open (22/114 of losers there)
- **Sharp: n=22  W=0/L=22  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 30-40 weak; zscore -2 to -1 oversold  •  ONLY when session=london_open

### L15.  `T4=T4c AND RSI=RSI2 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=182  W=68/L=114  WR=37.4%
- Sharpen: sharpest is session_bucket=london_open (22/114 of losers there)
- **Sharp: n=22  W=0/L=22  WR=0.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 30-40 weak; zscore -2 to -1 oversold  •  ONLY when session=london_open

### L16.  `H60=H60a AND T4=T4c AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=176  W=68/L=108  WR=38.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=176  W=68/L=108  WR=38.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 30-40 weak; session=asia

### L17.  `T4=T4c AND RSI=RSI2 AND direction_exec=long AND session_bucket=asia`
- Raw: n=176  W=68/L=108  WR=38.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=176  W=68/L=108  WR=38.6%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 30-40 weak; session=asia

### L18.  `H20=H20a AND T4=T4c AND BBP=BBP2 AND RSI=RSI2`
- Raw: n=170  W=63/L=107  WR=37.1%
- Sharpen: sharpest is session_bucket=london_open (22/107 of losers there)
- **Sharp: n=22  W=0/L=22  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; lower third; RSI 30-40 weak  •  ONLY when session=london_open

### L19.  `T1=T1c AND T4=T4c AND BBP=BBP2 AND RSI=RSI2`
- Raw: n=167  W=63/L=104  WR=37.7%
- Sharpen: sharpest is session_bucket=london_open (22/104 of losers there)
- **Sharp: n=22  W=0/L=22  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; lower third; RSI 30-40 weak  •  ONLY when session=london_open

### L20.  `H60=H60a AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=162  W=62/L=100  WR=38.3%
- Sharpen: sharpest is session_bucket=ny_mid (60/100 of losers there)
- **Sharp: n=83  W=23/L=60  WR=27.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when session=ny_mid

### L21.  `T1=T1c AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=162  W=62/L=100  WR=38.3%
- Sharpen: sharpest is session_bucket=ny_mid (60/100 of losers there)
- **Sharp: n=83  W=23/L=60  WR=27.7%**
- **Dir: ?**  •  1h trend AGAINST trade; deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when session=ny_mid

### L22.  `BBP=BBP0 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=162  W=62/L=100  WR=38.3%
- Sharpen: sharpest is session_bucket=ny_mid (60/100 of losers there)
- **Sharp: n=83  W=23/L=60  WR=27.7%**
- **Dir: LONG**  •  deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when session=ny_mid

### L23.  `H60=H60a AND T1=T1c AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=162  W=62/L=100  WR=38.3%
- Sharpen: sharpest is session_bucket=ny_mid (60/100 of losers there)
- **Sharp: n=83  W=23/L=60  WR=27.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when session=ny_mid

### L24.  `H60=H60a AND BBP=BBP0 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=162  W=62/L=100  WR=38.3%
- Sharpen: sharpest is session_bucket=ny_mid (60/100 of losers there)
- **Sharp: n=83  W=23/L=60  WR=27.7%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when session=ny_mid

### L25.  `T1=T1c AND BBP=BBP0 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=162  W=62/L=100  WR=38.3%
- Sharpen: sharpest is session_bucket=ny_mid (60/100 of losers there)
- **Sharp: n=83  W=23/L=60  WR=27.7%**
- **Dir: LONG**  •  1h trend AGAINST trade; deep below lower band; zscore -3 to -2 deep oversold  •  ONLY when session=ny_mid

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20e(53/44) | H20a(44/54) |
| H60 | H60e(54/45) | H60a(46/55) |
| T1 | T1a(53/45) | T1c(47/55) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(54/45) | long(46/55) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
