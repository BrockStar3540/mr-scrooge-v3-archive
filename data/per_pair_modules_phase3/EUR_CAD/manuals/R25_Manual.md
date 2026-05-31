# EUR_CAD — R25 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50e**  (EMA50 down >0.5x)
- **ADR = ADR5**  (>110% overshoot)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **2,887**  (W=1,751 / L=1,136)  -  WR: **60.7%**

## Session distribution

- ny_mid: n=728  W=453/L=275  WR=62.2%
- ny_close: n=476  W=287/L=189  WR=60.3%
- ny_open: n=465  W=273/L=192  WR=58.7%
- asia: n=451  W=268/L=183  WR=59.4%
- london_open: n=446  W=280/L=166  WR=62.8%
- off_hours: n=116  W=63/L=53  WR=54.3%
- asia_late: n=107  W=68/L=39  WR=63.6%
- london: n=98  W=59/L=39  WR=60.2%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND H60=H60a AND session_bucket=asia_late`
- Raw: n=67  W=66/L=1  WR=98.5%
- Refine: no further refinement
- **Final: n=67  W=66/L=1  WR=98.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=asia_late

### W02.  `H20=H20a AND T1=T1a AND session_bucket=asia_late`
- Raw: n=67  W=66/L=1  WR=98.5%
- Refine: no further refinement
- **Final: n=67  W=66/L=1  WR=98.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=asia_late

### W03.  `H20=H20a AND T4=T4a AND session_bucket=asia_late`
- Raw: n=67  W=66/L=1  WR=98.5%
- Refine: no further refinement
- **Final: n=67  W=66/L=1  WR=98.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=asia_late

### W04.  `H20=H20a AND direction_exec=short AND session_bucket=asia_late`
- Raw: n=67  W=66/L=1  WR=98.5%
- Refine: no further refinement
- **Final: n=67  W=66/L=1  WR=98.5%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; session=asia_late

### W05.  `H60=H60a AND T1=T1a AND session_bucket=asia_late`
- Raw: n=67  W=66/L=1  WR=98.5%
- Refine: no further refinement
- **Final: n=67  W=66/L=1  WR=98.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=asia_late

### W06.  `H60=H60a AND T4=T4a AND session_bucket=asia_late`
- Raw: n=67  W=66/L=1  WR=98.5%
- Refine: no further refinement
- **Final: n=67  W=66/L=1  WR=98.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; session=asia_late

### W07.  `H60=H60a AND direction_exec=short AND session_bucket=asia_late`
- Raw: n=67  W=66/L=1  WR=98.5%
- Refine: no further refinement
- **Final: n=67  W=66/L=1  WR=98.5%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; session=asia_late

### W08.  `T1=T1a AND T4=T4a AND session_bucket=asia_late`
- Raw: n=67  W=66/L=1  WR=98.5%
- Refine: no further refinement
- **Final: n=67  W=66/L=1  WR=98.5%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; session=asia_late

### W09.  `T1=T1a AND direction_exec=short AND session_bucket=asia_late`
- Raw: n=67  W=66/L=1  WR=98.5%
- Refine: no further refinement
- **Final: n=67  W=66/L=1  WR=98.5%**
- **Dir: SHORT**  •  1h trend WITH trade; session=asia_late

### W10.  `T4=T4a AND direction_exec=short AND session_bucket=asia_late`
- Raw: n=67  W=66/L=1  WR=98.5%
- Refine: no further refinement
- **Final: n=67  W=66/L=1  WR=98.5%**
- **Dir: SHORT**  •  4h trend WITH trade; session=asia_late

### W11.  `H20=H20a AND H60=H60a AND T1=T1a AND session_bucket=asia_late`
- Raw: n=67  W=66/L=1  WR=98.5%
- Refine: no further refinement
- **Final: n=67  W=66/L=1  WR=98.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; session=asia_late

### W12.  `H20=H20a AND H60=H60a AND T4=T4a AND session_bucket=asia_late`
- Raw: n=67  W=66/L=1  WR=98.5%
- Refine: no further refinement
- **Final: n=67  W=66/L=1  WR=98.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade; session=asia_late

### W13.  `H20=H20a AND H60=H60a AND direction_exec=short AND session_bucket=asia_late`
- Raw: n=67  W=66/L=1  WR=98.5%
- Refine: no further refinement
- **Final: n=67  W=66/L=1  WR=98.5%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=asia_late

### W14.  `H20=H20a AND T1=T1a AND T4=T4a AND session_bucket=asia_late`
- Raw: n=67  W=66/L=1  WR=98.5%
- Refine: no further refinement
- **Final: n=67  W=66/L=1  WR=98.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; session=asia_late

### W15.  `H20=H20a AND T1=T1a AND direction_exec=short AND session_bucket=asia_late`
- Raw: n=67  W=66/L=1  WR=98.5%
- Refine: no further refinement
- **Final: n=67  W=66/L=1  WR=98.5%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=asia_late

### W16.  `H20=H20a AND T4=T4a AND direction_exec=short AND session_bucket=asia_late`
- Raw: n=67  W=66/L=1  WR=98.5%
- Refine: no further refinement
- **Final: n=67  W=66/L=1  WR=98.5%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=asia_late

### W17.  `H60=H60a AND T1=T1a AND T4=T4a AND session_bucket=asia_late`
- Raw: n=67  W=66/L=1  WR=98.5%
- Refine: no further refinement
- **Final: n=67  W=66/L=1  WR=98.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; session=asia_late

### W18.  `H60=H60a AND T1=T1a AND direction_exec=short AND session_bucket=asia_late`
- Raw: n=67  W=66/L=1  WR=98.5%
- Refine: no further refinement
- **Final: n=67  W=66/L=1  WR=98.5%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=asia_late

### W19.  `H60=H60a AND T4=T4a AND direction_exec=short AND session_bucket=asia_late`
- Raw: n=67  W=66/L=1  WR=98.5%
- Refine: no further refinement
- **Final: n=67  W=66/L=1  WR=98.5%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend WITH trade; session=asia_late

### W20.  `T1=T1a AND T4=T4a AND direction_exec=short AND session_bucket=asia_late`
- Raw: n=67  W=66/L=1  WR=98.5%
- Refine: no further refinement
- **Final: n=67  W=66/L=1  WR=98.5%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend WITH trade; session=asia_late

### W21.  `H20=H20e AND BBP=BBP2 AND session_bucket=ny_open`
- Raw: n=64  W=55/L=9  WR=85.9%
- Refine: exclude H60=H60c drops 3/9 losers (33%)
- **Final: n=54  W=48/L=6  WR=88.9%**
- **Dir: ?**  •  HTF20 strongly against; lower third; session=ny_open  •  AVOID when HTF60 neutral

### W22.  `H20=H20e AND T4=T4c AND BBP=BBP2 AND session_bucket=ny_open`
- Raw: n=64  W=55/L=9  WR=85.9%
- Refine: exclude H60=H60c drops 3/9 losers (33%)
- **Final: n=54  W=48/L=6  WR=88.9%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; lower third; session=ny_open  •  AVOID when HTF60 neutral

### W23.  `H20=H20e AND ZS=ZS2 AND session_bucket=ny_open`
- Raw: n=62  W=53/L=9  WR=85.5%
- Refine: exclude H60=H60c drops 3/9 losers (33%)
- **Final: n=52  W=46/L=6  WR=88.5%**
- **Dir: ?**  •  HTF20 strongly against; zscore -2 to -1 oversold; session=ny_open  •  AVOID when HTF60 neutral

### W24.  `H20=H20e AND T4=T4c AND ZS=ZS2 AND session_bucket=ny_open`
- Raw: n=62  W=53/L=9  WR=85.5%
- Refine: exclude H60=H60c drops 3/9 losers (33%)
- **Final: n=52  W=46/L=6  WR=88.5%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; zscore -2 to -1 oversold; session=ny_open  •  AVOID when HTF60 neutral

### W25.  `H20=H20e AND BBP=BBP2 AND ZS=ZS2 AND session_bucket=ny_open`
- Raw: n=62  W=53/L=9  WR=85.5%
- Refine: exclude H60=H60c drops 3/9 losers (33%)
- **Final: n=52  W=46/L=6  WR=88.5%**
- **Dir: ?**  •  HTF20 strongly against; lower third; zscore -2 to -1 oversold; session=ny_open  •  AVOID when HTF60 neutral

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20a AND T4=T4a AND session_bucket=ny_open`
- Raw: n=165  W=66/L=99  WR=40.0%
- Sharpen: sharpest is BBP=BBP2 (37/99 of losers there)
- **Sharp: n=43  W=6/L=37  WR=14.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=ny_open  •  ONLY when lower third

### L02.  `H20=H20e AND BBP=BBP2 AND RSI=RSI0`
- Raw: n=135  W=48/L=87  WR=35.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=135  W=48/L=87  WR=35.6%**
- **Dir: ?**  •  HTF20 strongly against; lower third; RSI<20 extreme oversold

### L03.  `H60=H60e AND BBP=BBP2 AND RSI=RSI0`
- Raw: n=135  W=48/L=87  WR=35.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=135  W=48/L=87  WR=35.6%**
- **Dir: ?**  •  HTF60 strongly against; lower third; RSI<20 extreme oversold

### L04.  `H20=H20e AND H60=H60e AND BBP=BBP2 AND RSI=RSI0`
- Raw: n=135  W=48/L=87  WR=35.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=135  W=48/L=87  WR=35.6%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; lower third; RSI<20 extreme oversold

### L05.  `H20=H20e AND T1=T1c AND BBP=BBP2 AND RSI=RSI0`
- Raw: n=135  W=48/L=87  WR=35.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=135  W=48/L=87  WR=35.6%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; lower third; RSI<20 extreme oversold

### L06.  `H20=H20e AND T4=T4c AND BBP=BBP2 AND RSI=RSI0`
- Raw: n=135  W=48/L=87  WR=35.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=135  W=48/L=87  WR=35.6%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; lower third; RSI<20 extreme oversold

### L07.  `H20=H20e AND BBP=BBP2 AND RSI=RSI0 AND direction_exec=long`
- Raw: n=135  W=48/L=87  WR=35.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=135  W=48/L=87  WR=35.6%**
- **Dir: LONG**  •  HTF20 strongly against; lower third; RSI<20 extreme oversold

### L08.  `H60=H60e AND T1=T1c AND BBP=BBP2 AND RSI=RSI0`
- Raw: n=135  W=48/L=87  WR=35.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=135  W=48/L=87  WR=35.6%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; lower third; RSI<20 extreme oversold

### L09.  `H60=H60e AND T4=T4c AND BBP=BBP2 AND RSI=RSI0`
- Raw: n=135  W=48/L=87  WR=35.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=135  W=48/L=87  WR=35.6%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; lower third; RSI<20 extreme oversold

### L10.  `H60=H60e AND BBP=BBP2 AND RSI=RSI0 AND direction_exec=long`
- Raw: n=135  W=48/L=87  WR=35.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=135  W=48/L=87  WR=35.6%**
- **Dir: LONG**  •  HTF60 strongly against; lower third; RSI<20 extreme oversold

### L11.  `H20=H20e AND RSI=RSI0 AND ZS=ZS2`
- Raw: n=125  W=44/L=81  WR=35.2%
- Sharpen: no sharper sub-pattern
- **Sharp: n=125  W=44/L=81  WR=35.2%**
- **Dir: ?**  •  HTF20 strongly against; RSI<20 extreme oversold; zscore -2 to -1 oversold

### L12.  `H60=H60e AND RSI=RSI0 AND ZS=ZS2`
- Raw: n=125  W=44/L=81  WR=35.2%
- Sharpen: no sharper sub-pattern
- **Sharp: n=125  W=44/L=81  WR=35.2%**
- **Dir: ?**  •  HTF60 strongly against; RSI<20 extreme oversold; zscore -2 to -1 oversold

### L13.  `H20=H20e AND H60=H60e AND RSI=RSI0 AND ZS=ZS2`
- Raw: n=125  W=44/L=81  WR=35.2%
- Sharpen: no sharper sub-pattern
- **Sharp: n=125  W=44/L=81  WR=35.2%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI<20 extreme oversold; zscore -2 to -1 oversold

### L14.  `H20=H20e AND T1=T1c AND RSI=RSI0 AND ZS=ZS2`
- Raw: n=125  W=44/L=81  WR=35.2%
- Sharpen: no sharper sub-pattern
- **Sharp: n=125  W=44/L=81  WR=35.2%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI<20 extreme oversold; zscore -2 to -1 oversold

### L15.  `H20=H20e AND T4=T4c AND RSI=RSI0 AND ZS=ZS2`
- Raw: n=125  W=44/L=81  WR=35.2%
- Sharpen: no sharper sub-pattern
- **Sharp: n=125  W=44/L=81  WR=35.2%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI<20 extreme oversold; zscore -2 to -1 oversold

### L16.  `H20=H20e AND BBP=BBP2 AND RSI=RSI0 AND ZS=ZS2`
- Raw: n=125  W=44/L=81  WR=35.2%
- Sharpen: no sharper sub-pattern
- **Sharp: n=125  W=44/L=81  WR=35.2%**
- **Dir: ?**  •  HTF20 strongly against; lower third; RSI<20 extreme oversold; zscore -2 to -1 oversold

### L17.  `H20=H20e AND RSI=RSI0 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=125  W=44/L=81  WR=35.2%
- Sharpen: no sharper sub-pattern
- **Sharp: n=125  W=44/L=81  WR=35.2%**
- **Dir: LONG**  •  HTF20 strongly against; RSI<20 extreme oversold; zscore -2 to -1 oversold

### L18.  `H60=H60e AND T1=T1c AND RSI=RSI0 AND ZS=ZS2`
- Raw: n=125  W=44/L=81  WR=35.2%
- Sharpen: no sharper sub-pattern
- **Sharp: n=125  W=44/L=81  WR=35.2%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI<20 extreme oversold; zscore -2 to -1 oversold

### L19.  `H60=H60e AND T4=T4c AND RSI=RSI0 AND ZS=ZS2`
- Raw: n=125  W=44/L=81  WR=35.2%
- Sharpen: no sharper sub-pattern
- **Sharp: n=125  W=44/L=81  WR=35.2%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI<20 extreme oversold; zscore -2 to -1 oversold

### L20.  `H60=H60e AND BBP=BBP2 AND RSI=RSI0 AND ZS=ZS2`
- Raw: n=125  W=44/L=81  WR=35.2%
- Sharpen: no sharper sub-pattern
- **Sharp: n=125  W=44/L=81  WR=35.2%**
- **Dir: ?**  •  HTF60 strongly against; lower third; RSI<20 extreme oversold; zscore -2 to -1 oversold

### L21.  `H60=H60e AND RSI=RSI0 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=125  W=44/L=81  WR=35.2%
- Sharpen: no sharper sub-pattern
- **Sharp: n=125  W=44/L=81  WR=35.2%**
- **Dir: LONG**  •  HTF60 strongly against; RSI<20 extreme oversold; zscore -2 to -1 oversold

### L22.  `H20=H20a AND RSI=RSI1 AND session_bucket=ny_open`
- Raw: n=96  W=34/L=62  WR=35.4%
- Sharpen: sharpest is BBP=BBP2 (31/62 of losers there)
- **Sharp: n=35  W=4/L=31  WR=11.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 20-30 oversold; session=ny_open  •  ONLY when lower third

### L23.  `H20=H20a AND T4=T4a AND RSI=RSI1 AND session_bucket=ny_open`
- Raw: n=96  W=34/L=62  WR=35.4%
- Sharpen: sharpest is BBP=BBP2 (31/62 of losers there)
- **Sharp: n=35  W=4/L=31  WR=11.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 20-30 oversold; session=ny_open  •  ONLY when lower third

### L24.  `T1=T1c AND BBP=BBP2 AND session_bucket=asia`
- Raw: n=83  W=33/L=50  WR=39.8%
- Sharpen: sharpest is H20=H20e (35/50 of losers there)
- **Sharp: n=47  W=12/L=35  WR=25.5%**
- **Dir: ?**  •  1h trend AGAINST trade; lower third; session=asia  •  ONLY when HTF20 strongly against

### L25.  `BBP=BBP2 AND direction_exec=long AND session_bucket=asia`
- Raw: n=83  W=33/L=50  WR=39.8%
- Sharpen: sharpest is H20=H20e (35/50 of losers there)
- **Sharp: n=47  W=12/L=35  WR=25.5%**
- **Dir: LONG**  •  lower third; session=asia  •  ONLY when HTF20 strongly against

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(45/33) | H20e(33/45) |
| H60 | H60a(38/28) | H60e(29/38) |
| T1 | T1a(54/44) | T1c(46/56) |
| T4 | T4a(54/45) | T4c(46/55) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(54/44) | long(46/56) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
