# NZD_USD — R30 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50a**  (EMA50 up >0.5x)
- **ADR = ADR3**  (60-90%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **1,333**  (W=854 / L=479)  -  WR: **64.1%**

## Session distribution

- asia: n=449  W=288/L=161  WR=64.1%
- ny_mid: n=307  W=192/L=115  WR=62.5%
- london_open: n=195  W=123/L=72  WR=63.1%
- ny_close: n=176  W=113/L=63  WR=64.2%
- off_hours: n=84  W=51/L=33  WR=60.7%
- london: n=56  W=40/L=16  WR=71.4%
- ny_open: n=40  W=31/L=9  WR=77.5%
- asia_late: n=26  W=16/L=10  WR=61.5%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60a AND ZS=ZS5 AND session_bucket=ny_mid`
- Raw: n=60  W=51/L=9  WR=85.0%
- Refine: exclude H20=H20c drops 7/9 losers (78%)
- **Final: n=32  W=30/L=2  WR=93.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; zscore +2 to +3 deep overbought; session=ny_mid  •  AVOID when HTF20 neutral

### W02.  `T1=T1a AND ZS=ZS5 AND session_bucket=ny_mid`
- Raw: n=60  W=51/L=9  WR=85.0%
- Refine: exclude H20=H20c drops 7/9 losers (78%)
- **Final: n=32  W=30/L=2  WR=93.8%**
- **Dir: ?**  •  1h trend WITH trade; zscore +2 to +3 deep overbought; session=ny_mid  •  AVOID when HTF20 neutral

### W03.  `T4=T4a AND ZS=ZS5 AND session_bucket=ny_mid`
- Raw: n=60  W=51/L=9  WR=85.0%
- Refine: exclude H20=H20c drops 7/9 losers (78%)
- **Final: n=32  W=30/L=2  WR=93.8%**
- **Dir: ?**  •  4h trend WITH trade; zscore +2 to +3 deep overbought; session=ny_mid  •  AVOID when HTF20 neutral

### W04.  `ZS=ZS5 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=60  W=51/L=9  WR=85.0%
- Refine: exclude H20=H20c drops 7/9 losers (78%)
- **Final: n=32  W=30/L=2  WR=93.8%**
- **Dir: LONG**  •  zscore +2 to +3 deep overbought; session=ny_mid  •  AVOID when HTF20 neutral

### W05.  `H60=H60a AND T1=T1a AND ZS=ZS5 AND session_bucket=ny_mid`
- Raw: n=60  W=51/L=9  WR=85.0%
- Refine: exclude H20=H20c drops 7/9 losers (78%)
- **Final: n=32  W=30/L=2  WR=93.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; zscore +2 to +3 deep overbought; session=ny_mid  •  AVOID when HTF20 neutral

### W06.  `H60=H60a AND T4=T4a AND ZS=ZS5 AND session_bucket=ny_mid`
- Raw: n=60  W=51/L=9  WR=85.0%
- Refine: exclude H20=H20c drops 7/9 losers (78%)
- **Final: n=32  W=30/L=2  WR=93.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; zscore +2 to +3 deep overbought; session=ny_mid  •  AVOID when HTF20 neutral

### W07.  `H60=H60a AND ZS=ZS5 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=60  W=51/L=9  WR=85.0%
- Refine: exclude H20=H20c drops 7/9 losers (78%)
- **Final: n=32  W=30/L=2  WR=93.8%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; zscore +2 to +3 deep overbought; session=ny_mid  •  AVOID when HTF20 neutral

### W08.  `T1=T1a AND T4=T4a AND ZS=ZS5 AND session_bucket=ny_mid`
- Raw: n=60  W=51/L=9  WR=85.0%
- Refine: exclude H20=H20c drops 7/9 losers (78%)
- **Final: n=32  W=30/L=2  WR=93.8%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; zscore +2 to +3 deep overbought; session=ny_mid  •  AVOID when HTF20 neutral

### W09.  `T1=T1a AND ZS=ZS5 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=60  W=51/L=9  WR=85.0%
- Refine: exclude H20=H20c drops 7/9 losers (78%)
- **Final: n=32  W=30/L=2  WR=93.8%**
- **Dir: LONG**  •  1h trend WITH trade; zscore +2 to +3 deep overbought; session=ny_mid  •  AVOID when HTF20 neutral

### W10.  `T4=T4a AND ZS=ZS5 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=60  W=51/L=9  WR=85.0%
- Refine: exclude H20=H20c drops 7/9 losers (78%)
- **Final: n=32  W=30/L=2  WR=93.8%**
- **Dir: LONG**  •  4h trend WITH trade; zscore +2 to +3 deep overbought; session=ny_mid  •  AVOID when HTF20 neutral

### W11.  `T1=T1c AND T4=T4c AND RSI=RSI5`
- Raw: n=59  W=53/L=6  WR=89.8%
- Refine: exclude BBP=BBP2 drops 6/6 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when lower third

### W12.  `T1=T1c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=59  W=53/L=6  WR=89.8%
- Refine: exclude BBP=BBP2 drops 6/6 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 60-70 strong  •  AVOID when lower third

### W13.  `T4=T4c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=59  W=53/L=6  WR=89.8%
- Refine: exclude BBP=BBP2 drops 6/6 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when lower third

### W14.  `T1=T1c AND T4=T4c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=59  W=53/L=6  WR=89.8%
- Refine: exclude BBP=BBP2 drops 6/6 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when lower third

### W15.  `T1=T1c AND RSI=RSI6 AND session_bucket=london_open`
- Raw: n=56  W=52/L=4  WR=92.9%
- Refine: exclude strategy_id=bravo_expansion_continuation drops 2/4 losers (50%)
- **Final: n=49  W=47/L=2  WR=95.9%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 70-80 overbought; session=london_open  •  AVOID when strategy=bravo_expansion_continuation

### W16.  `T4=T4c AND RSI=RSI6 AND session_bucket=london_open`
- Raw: n=56  W=52/L=4  WR=92.9%
- Refine: exclude strategy_id=bravo_expansion_continuation drops 2/4 losers (50%)
- **Final: n=49  W=47/L=2  WR=95.9%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 70-80 overbought; session=london_open  •  AVOID when strategy=bravo_expansion_continuation

### W17.  `RSI=RSI6 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=56  W=52/L=4  WR=92.9%
- Refine: exclude strategy_id=bravo_expansion_continuation drops 2/4 losers (50%)
- **Final: n=49  W=47/L=2  WR=95.9%**
- **Dir: SHORT**  •  RSI 70-80 overbought; session=london_open  •  AVOID when strategy=bravo_expansion_continuation

### W18.  `T1=T1c AND T4=T4c AND RSI=RSI6 AND session_bucket=london_open`
- Raw: n=56  W=52/L=4  WR=92.9%
- Refine: exclude strategy_id=bravo_expansion_continuation drops 2/4 losers (50%)
- **Final: n=49  W=47/L=2  WR=95.9%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 70-80 overbought; session=london_open  •  AVOID when strategy=bravo_expansion_continuation

### W19.  `T1=T1c AND RSI=RSI6 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=56  W=52/L=4  WR=92.9%
- Refine: exclude strategy_id=bravo_expansion_continuation drops 2/4 losers (50%)
- **Final: n=49  W=47/L=2  WR=95.9%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 70-80 overbought; session=london_open  •  AVOID when strategy=bravo_expansion_continuation

### W20.  `T4=T4c AND RSI=RSI6 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=56  W=52/L=4  WR=92.9%
- Refine: exclude strategy_id=bravo_expansion_continuation drops 2/4 losers (50%)
- **Final: n=49  W=47/L=2  WR=95.9%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 70-80 overbought; session=london_open  •  AVOID when strategy=bravo_expansion_continuation

### W21.  `H20=H20a AND H60=H60e AND T1=T1a`
- Raw: n=52  W=49/L=3  WR=94.2%
- Refine: exclude ZS=ZS6 drops 3/3 losers (100%)
- **Final: n=49  W=49/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend WITH trade  •  AVOID when zscore >+3 extreme

### W22.  `H20=H20a AND H60=H60e AND T4=T4a`
- Raw: n=52  W=49/L=3  WR=94.2%
- Refine: exclude ZS=ZS6 drops 3/3 losers (100%)
- **Final: n=49  W=49/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 4h trend WITH trade  •  AVOID when zscore >+3 extreme

### W23.  `H20=H20a AND H60=H60e AND RSI=RSI7`
- Raw: n=52  W=49/L=3  WR=94.2%
- Refine: exclude ZS=ZS6 drops 3/3 losers (100%)
- **Final: n=49  W=49/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; RSI>80 extreme overbought  •  AVOID when zscore >+3 extreme

### W24.  `H20=H20a AND H60=H60e AND direction_exec=long`
- Raw: n=52  W=49/L=3  WR=94.2%
- Refine: exclude ZS=ZS6 drops 3/3 losers (100%)
- **Final: n=49  W=49/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 strongly against  •  AVOID when zscore >+3 extreme

### W25.  `H20=H20a AND H60=H60e AND T1=T1a AND T4=T4a`
- Raw: n=52  W=49/L=3  WR=94.2%
- Refine: exclude ZS=ZS6 drops 3/3 losers (100%)
- **Final: n=49  W=49/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when zscore >+3 extreme

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60a AND RSI=RSI6 AND session_bucket=asia`
- Raw: n=108  W=40/L=68  WR=37.0%
- Sharpen: sharpest is BBP=BBP5 (21/68 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 70-80 overbought; session=asia  •  ONLY when just touched upper band

### L02.  `H20=H20e AND H60=H60e AND session_bucket=ny_mid`
- Raw: n=100  W=39/L=61  WR=39.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=100  W=39/L=61  WR=39.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; session=ny_mid

### L03.  `H20=H20e AND T1=T1c AND session_bucket=ny_mid`
- Raw: n=100  W=39/L=61  WR=39.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=100  W=39/L=61  WR=39.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; session=ny_mid

### L04.  `H20=H20e AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=100  W=39/L=61  WR=39.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=100  W=39/L=61  WR=39.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; session=ny_mid

### L05.  `H20=H20e AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=100  W=39/L=61  WR=39.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=100  W=39/L=61  WR=39.0%**
- **Dir: SHORT**  •  HTF20 strongly against; session=ny_mid

### L06.  `H20=H20e AND H60=H60e AND T1=T1c AND session_bucket=ny_mid`
- Raw: n=100  W=39/L=61  WR=39.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=100  W=39/L=61  WR=39.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; session=ny_mid

### L07.  `H20=H20e AND H60=H60e AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=100  W=39/L=61  WR=39.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=100  W=39/L=61  WR=39.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; session=ny_mid

### L08.  `H20=H20e AND H60=H60e AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=100  W=39/L=61  WR=39.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=100  W=39/L=61  WR=39.0%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; session=ny_mid

### L09.  `H20=H20e AND T1=T1c AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=100  W=39/L=61  WR=39.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=100  W=39/L=61  WR=39.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_mid

### L10.  `H20=H20e AND T1=T1c AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=100  W=39/L=61  WR=39.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=100  W=39/L=61  WR=39.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; session=ny_mid

### L11.  `H20=H20e AND T4=T4c AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=100  W=39/L=61  WR=39.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=100  W=39/L=61  WR=39.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade; session=ny_mid

### L12.  `H20=H20e AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=88  W=35/L=53  WR=39.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=88  W=35/L=53  WR=39.8%**
- **Dir: ?**  •  HTF20 strongly against; RSI 70-80 overbought; session=ny_mid

### L13.  `H20=H20e AND H60=H60e AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=88  W=35/L=53  WR=39.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=88  W=35/L=53  WR=39.8%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 70-80 overbought; session=ny_mid

### L14.  `H20=H20e AND T1=T1c AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=88  W=35/L=53  WR=39.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=88  W=35/L=53  WR=39.8%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 70-80 overbought; session=ny_mid

### L15.  `H20=H20e AND T4=T4c AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=88  W=35/L=53  WR=39.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=88  W=35/L=53  WR=39.8%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 70-80 overbought; session=ny_mid

### L16.  `H20=H20e AND RSI=RSI6 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=88  W=35/L=53  WR=39.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=88  W=35/L=53  WR=39.8%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 70-80 overbought; session=ny_mid

### L17.  `H20=H20e AND BBP=BBP4 AND session_bucket=ny_mid`
- Raw: n=68  W=24/L=44  WR=35.3%
- Sharpen: sharpest is RSI=RSI7 (8/44 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; upper third; session=ny_mid  •  ONLY when RSI>80 extreme overbought

### L18.  `H20=H20e AND H60=H60e AND BBP=BBP4 AND session_bucket=ny_mid`
- Raw: n=68  W=24/L=44  WR=35.3%
- Sharpen: sharpest is RSI=RSI7 (8/44 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; upper third; session=ny_mid  •  ONLY when RSI>80 extreme overbought

### L19.  `H20=H20e AND T1=T1c AND BBP=BBP4 AND session_bucket=ny_mid`
- Raw: n=68  W=24/L=44  WR=35.3%
- Sharpen: sharpest is RSI=RSI7 (8/44 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; upper third; session=ny_mid  •  ONLY when RSI>80 extreme overbought

### L20.  `H20=H20e AND T4=T4c AND BBP=BBP4 AND session_bucket=ny_mid`
- Raw: n=68  W=24/L=44  WR=35.3%
- Sharpen: sharpest is RSI=RSI7 (8/44 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; upper third; session=ny_mid  •  ONLY when RSI>80 extreme overbought

### L21.  `H20=H20e AND BBP=BBP4 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=68  W=24/L=44  WR=35.3%
- Sharpen: sharpest is RSI=RSI7 (8/44 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; upper third; session=ny_mid  •  ONLY when RSI>80 extreme overbought

### L22.  `H20=H20e AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=67  W=24/L=43  WR=35.8%
- Sharpen: sharpest is RSI=RSI7 (8/43 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; zscore +1 to +2 overbought; session=ny_mid  •  ONLY when RSI>80 extreme overbought

### L23.  `H20=H20e AND H60=H60e AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=67  W=24/L=43  WR=35.8%
- Sharpen: sharpest is RSI=RSI7 (8/43 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; zscore +1 to +2 overbought; session=ny_mid  •  ONLY when RSI>80 extreme overbought

### L24.  `H20=H20e AND T1=T1c AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=67  W=24/L=43  WR=35.8%
- Sharpen: sharpest is RSI=RSI7 (8/43 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; zscore +1 to +2 overbought; session=ny_mid  •  ONLY when RSI>80 extreme overbought

### L25.  `H20=H20e AND T4=T4c AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=67  W=24/L=43  WR=35.8%
- Sharpen: sharpest is RSI=RSI7 (8/43 of losers there)
- **Sharp: n=8  W=0/L=8  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; zscore +1 to +2 overbought; session=ny_mid  •  ONLY when RSI>80 extreme overbought

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(43/36) | H20e(41/48) |
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
