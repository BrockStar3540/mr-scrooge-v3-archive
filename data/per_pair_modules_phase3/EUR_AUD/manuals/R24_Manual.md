# EUR_AUD — R24 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **6,100**  (W=3,604 / L=2,496)  -  WR: **59.1%**

## Session distribution

- asia: n=2431  W=1455/L=976  WR=59.9%
- ny_mid: n=1035  W=568/L=467  WR=54.9%
- london_open: n=606  W=370/L=236  WR=61.1%
- ny_close: n=599  W=360/L=239  WR=60.1%
- ny_open: n=572  W=338/L=234  WR=59.1%
- london: n=372  W=229/L=143  WR=61.6%
- asia_late: n=288  W=164/L=124  WR=56.9%
- off_hours: n=197  W=120/L=77  WR=60.9%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `BBP=BBP2 AND RSI=RSI5 AND direction_exec=long`
- Raw: n=116  W=100/L=16  WR=86.2%
- Refine: exclude T4=T4c drops 11/16 losers (69%)
- **Final: n=67  W=62/L=5  WR=92.5%**
- **Dir: LONG**  •  lower third; RSI 60-70 strong  •  AVOID when 4h trend AGAINST trade

### W02.  `T1=T1a AND BBP=BBP2 AND RSI=RSI5 AND direction_exec=long`
- Raw: n=116  W=100/L=16  WR=86.2%
- Refine: exclude T4=T4c drops 11/16 losers (69%)
- **Final: n=67  W=62/L=5  WR=92.5%**
- **Dir: LONG**  •  1h trend WITH trade; lower third; RSI 60-70 strong  •  AVOID when 4h trend AGAINST trade

### W03.  `T4=T4a AND ZS=ZS2 AND direction_exec=long`
- Raw: n=107  W=92/L=15  WR=86.0%
- Refine: exclude session_bucket=london_open drops 6/15 losers (40%)
- **Final: n=100  W=91/L=9  WR=91.0%**
- **Dir: LONG**  •  4h trend WITH trade; zscore -2 to -1 oversold  •  AVOID when session=london_open

### W04.  `T4=T4a AND BBP=BBP2 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=107  W=92/L=15  WR=86.0%
- Refine: exclude session_bucket=london_open drops 6/15 losers (40%)
- **Final: n=100  W=91/L=9  WR=91.0%**
- **Dir: LONG**  •  4h trend WITH trade; lower third; zscore -2 to -1 oversold  •  AVOID when session=london_open

### W05.  `H60=H60e AND BBP=BBP2 AND RSI=RSI5`
- Raw: n=102  W=87/L=15  WR=85.3%
- Refine: exclude T4=T4c drops 11/15 losers (73%)
- **Final: n=53  W=49/L=4  WR=92.5%**
- **Dir: ?**  •  HTF60 strongly against; lower third; RSI 60-70 strong  •  AVOID when 4h trend AGAINST trade

### W06.  `H60=H60e AND T1=T1a AND BBP=BBP2 AND RSI=RSI5`
- Raw: n=102  W=87/L=15  WR=85.3%
- Refine: exclude T4=T4c drops 11/15 losers (73%)
- **Final: n=53  W=49/L=4  WR=92.5%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; lower third; RSI 60-70 strong  •  AVOID when 4h trend AGAINST trade

### W07.  `H60=H60e AND BBP=BBP2 AND RSI=RSI5 AND direction_exec=long`
- Raw: n=102  W=87/L=15  WR=85.3%
- Refine: exclude T4=T4c drops 11/15 losers (73%)
- **Final: n=53  W=49/L=4  WR=92.5%**
- **Dir: LONG**  •  HTF60 strongly against; lower third; RSI 60-70 strong  •  AVOID when 4h trend AGAINST trade

### W08.  `RSI=RSI5 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=97  W=83/L=14  WR=85.6%
- Refine: exclude T4=T4c drops 11/14 losers (79%)
- **Final: n=56  W=53/L=3  WR=94.6%**
- **Dir: LONG**  •  RSI 60-70 strong; zscore -2 to -1 oversold  •  AVOID when 4h trend AGAINST trade

### W09.  `T1=T1a AND RSI=RSI5 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=97  W=83/L=14  WR=85.6%
- Refine: exclude T4=T4c drops 11/14 losers (79%)
- **Final: n=56  W=53/L=3  WR=94.6%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 60-70 strong; zscore -2 to -1 oversold  •  AVOID when 4h trend AGAINST trade

### W10.  `BBP=BBP2 AND RSI=RSI5 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=97  W=83/L=14  WR=85.6%
- Refine: exclude T4=T4c drops 11/14 losers (79%)
- **Final: n=56  W=53/L=3  WR=94.6%**
- **Dir: LONG**  •  lower third; RSI 60-70 strong; zscore -2 to -1 oversold  •  AVOID when 4h trend AGAINST trade

### W11.  `T1=T1a AND T4=T4a AND ZS=ZS2 AND direction_exec=long`
- Raw: n=94  W=80/L=14  WR=85.1%
- Refine: exclude RSI=RSI4 drops 11/14 losers (79%)
- **Final: n=56  W=53/L=3  WR=94.6%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; zscore -2 to -1 oversold  •  AVOID when RSI 50-60 upper neutral

### W12.  `H60=H60e AND T4=T4a AND session_bucket=ny_close`
- Raw: n=81  W=71/L=10  WR=87.7%
- Refine: exclude BBP=BBP3 drops 4/10 losers (40%)
- **Final: n=69  W=63/L=6  WR=91.3%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; session=ny_close  •  AVOID when middle of band

### W13.  `H20=H20e AND H60=H60e AND T4=T4a AND session_bucket=ny_close`
- Raw: n=81  W=71/L=10  WR=87.7%
- Refine: exclude BBP=BBP3 drops 4/10 losers (40%)
- **Final: n=69  W=63/L=6  WR=91.3%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend WITH trade; session=ny_close  •  AVOID when middle of band

### W14.  `H20=H20e AND T1=T1a AND T4=T4a AND session_bucket=ny_close`
- Raw: n=81  W=71/L=10  WR=87.7%
- Refine: exclude BBP=BBP3 drops 4/10 losers (40%)
- **Final: n=69  W=63/L=6  WR=91.3%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend WITH trade; session=ny_close  •  AVOID when middle of band

### W15.  `H20=H20e AND T4=T4a AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=81  W=71/L=10  WR=87.7%
- Refine: exclude BBP=BBP3 drops 4/10 losers (40%)
- **Final: n=69  W=63/L=6  WR=91.3%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend WITH trade; session=ny_close  •  AVOID when middle of band

### W16.  `H60=H60e AND T1=T1a AND T4=T4a AND session_bucket=ny_close`
- Raw: n=81  W=71/L=10  WR=87.7%
- Refine: exclude BBP=BBP3 drops 4/10 losers (40%)
- **Final: n=69  W=63/L=6  WR=91.3%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend WITH trade; session=ny_close  •  AVOID when middle of band

### W17.  `H60=H60e AND T4=T4a AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=81  W=71/L=10  WR=87.7%
- Refine: exclude BBP=BBP3 drops 4/10 losers (40%)
- **Final: n=69  W=63/L=6  WR=91.3%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend WITH trade; session=ny_close  •  AVOID when middle of band

### W18.  `H60=H60a AND T4=T4c AND ZS=ZS6`
- Raw: n=77  W=71/L=6  WR=92.2%
- Refine: exclude session_bucket=asia drops 6/6 losers (100%)
- **Final: n=42  W=42/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; zscore >+3 extreme  •  AVOID when session=asia

### W19.  `H60=H60a AND T1=T1c AND T4=T4c AND ZS=ZS6`
- Raw: n=77  W=71/L=6  WR=92.2%
- Refine: exclude session_bucket=asia drops 6/6 losers (100%)
- **Final: n=42  W=42/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; zscore >+3 extreme  •  AVOID when session=asia

### W20.  `H60=H60a AND T4=T4c AND BBP=BBP6 AND ZS=ZS6`
- Raw: n=77  W=71/L=6  WR=92.2%
- Refine: exclude session_bucket=asia drops 6/6 losers (100%)
- **Final: n=42  W=42/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; deep above upper band; zscore >+3 extreme  •  AVOID when session=asia

### W21.  `H60=H60a AND T4=T4c AND ZS=ZS6 AND direction_exec=short`
- Raw: n=77  W=71/L=6  WR=92.2%
- Refine: exclude session_bucket=asia drops 6/6 losers (100%)
- **Final: n=42  W=42/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; zscore >+3 extreme  •  AVOID when session=asia

### W22.  `H20=H20e AND ZS=ZS5 AND direction_exec=short`
- Raw: n=74  W=64/L=10  WR=86.5%
- Refine: exclude T1=T1a drops 5/10 losers (50%)
- **Final: n=52  W=47/L=5  WR=90.4%**
- **Dir: SHORT**  •  HTF20 strongly against; zscore +2 to +3 deep overbought  •  AVOID when 1h trend WITH trade

### W23.  `H20=H20e AND T4=T4c AND ZS=ZS5 AND direction_exec=short`
- Raw: n=74  W=64/L=10  WR=86.5%
- Refine: exclude T1=T1a drops 5/10 losers (50%)
- **Final: n=52  W=47/L=5  WR=90.4%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  AVOID when 1h trend WITH trade

### W24.  `H60=H60e AND T4=T4a AND RSI=RSI5 AND session_bucket=ny_close`
- Raw: n=71  W=63/L=8  WR=88.7%
- Refine: exclude BBP=BBP3 drops 4/8 losers (50%)
- **Final: n=65  W=61/L=4  WR=93.8%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; RSI 60-70 strong; session=ny_close  •  AVOID when middle of band

### W25.  `T1=T1a AND T4=T4a AND RSI=RSI5 AND session_bucket=ny_close`
- Raw: n=71  W=63/L=8  WR=88.7%
- Refine: exclude BBP=BBP3 drops 4/8 losers (50%)
- **Final: n=65  W=61/L=4  WR=93.8%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 60-70 strong; session=ny_close  •  AVOID when middle of band

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1c AND T4=T4c AND session_bucket=ny_open`
- Raw: n=209  W=82/L=127  WR=39.2%
- Sharpen: no sharper sub-pattern
- **Sharp: n=209  W=82/L=127  WR=39.2%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_open

### L02.  `H20=H20a AND RSI=RSI5 AND session_bucket=ny_close`
- Raw: n=184  W=64/L=120  WR=34.8%
- Sharpen: sharpest is T4=T4c (47/120 of losers there)
- **Sharp: n=60  W=13/L=47  WR=21.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 60-70 strong; session=ny_close  •  ONLY when 4h trend AGAINST trade

### L03.  `H60=H60a AND RSI=RSI5 AND session_bucket=ny_close`
- Raw: n=184  W=64/L=120  WR=34.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=184  W=64/L=120  WR=34.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 60-70 strong; session=ny_close

### L04.  `T1=T1c AND RSI=RSI5 AND session_bucket=ny_close`
- Raw: n=184  W=64/L=120  WR=34.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=184  W=64/L=120  WR=34.8%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 60-70 strong; session=ny_close

### L05.  `RSI=RSI5 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=184  W=64/L=120  WR=34.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=184  W=64/L=120  WR=34.8%**
- **Dir: SHORT**  •  RSI 60-70 strong; session=ny_close

### L06.  `H60=H60a AND T1=T1c AND RSI=RSI5 AND session_bucket=ny_close`
- Raw: n=184  W=64/L=120  WR=34.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=184  W=64/L=120  WR=34.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 60-70 strong; session=ny_close

### L07.  `H60=H60a AND RSI=RSI5 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=184  W=64/L=120  WR=34.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=184  W=64/L=120  WR=34.8%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; RSI 60-70 strong; session=ny_close

### L08.  `T1=T1c AND RSI=RSI5 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=184  W=64/L=120  WR=34.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=184  W=64/L=120  WR=34.8%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 60-70 strong; session=ny_close

### L09.  `H20=H20e AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=176  W=62/L=114  WR=35.2%
- Sharpen: sharpest is RSI=RSI5 (50/114 of losers there)
- **Sharp: n=60  W=10/L=50  WR=16.7%**
- **Dir: ?**  •  HTF20 strongly against; zscore +1 to +2 overbought; session=ny_mid  •  ONLY when RSI 60-70 strong

### L10.  `H60=H60e AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=176  W=62/L=114  WR=35.2%
- Sharpen: sharpest is RSI=RSI5 (50/114 of losers there)
- **Sharp: n=60  W=10/L=50  WR=16.7%**
- **Dir: ?**  •  HTF60 strongly against; zscore +1 to +2 overbought; session=ny_mid  •  ONLY when RSI 60-70 strong

### L11.  `ZS=ZS4 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=176  W=62/L=114  WR=35.2%
- Sharpen: sharpest is RSI=RSI5 (50/114 of losers there)
- **Sharp: n=60  W=10/L=50  WR=16.7%**
- **Dir: LONG**  •  zscore +1 to +2 overbought; session=ny_mid  •  ONLY when RSI 60-70 strong

### L12.  `H20=H20e AND H60=H60e AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=176  W=62/L=114  WR=35.2%
- Sharpen: sharpest is RSI=RSI5 (50/114 of losers there)
- **Sharp: n=60  W=10/L=50  WR=16.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; zscore +1 to +2 overbought; session=ny_mid  •  ONLY when RSI 60-70 strong

### L13.  `H20=H20e AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=176  W=62/L=114  WR=35.2%
- Sharpen: sharpest is RSI=RSI5 (50/114 of losers there)
- **Sharp: n=60  W=10/L=50  WR=16.7%**
- **Dir: ?**  •  HTF20 strongly against; upper third; zscore +1 to +2 overbought; session=ny_mid  •  ONLY when RSI 60-70 strong

### L14.  `H20=H20e AND ZS=ZS4 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=176  W=62/L=114  WR=35.2%
- Sharpen: sharpest is RSI=RSI5 (50/114 of losers there)
- **Sharp: n=60  W=10/L=50  WR=16.7%**
- **Dir: LONG**  •  HTF20 strongly against; zscore +1 to +2 overbought; session=ny_mid  •  ONLY when RSI 60-70 strong

### L15.  `H60=H60e AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=176  W=62/L=114  WR=35.2%
- Sharpen: sharpest is RSI=RSI5 (50/114 of losers there)
- **Sharp: n=60  W=10/L=50  WR=16.7%**
- **Dir: ?**  •  HTF60 strongly against; upper third; zscore +1 to +2 overbought; session=ny_mid  •  ONLY when RSI 60-70 strong

### L16.  `H60=H60e AND ZS=ZS4 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=176  W=62/L=114  WR=35.2%
- Sharpen: sharpest is RSI=RSI5 (50/114 of losers there)
- **Sharp: n=60  W=10/L=50  WR=16.7%**
- **Dir: LONG**  •  HTF60 strongly against; zscore +1 to +2 overbought; session=ny_mid  •  ONLY when RSI 60-70 strong

### L17.  `BBP=BBP4 AND ZS=ZS4 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=176  W=62/L=114  WR=35.2%
- Sharpen: sharpest is RSI=RSI5 (50/114 of losers there)
- **Sharp: n=60  W=10/L=50  WR=16.7%**
- **Dir: LONG**  •  upper third; zscore +1 to +2 overbought; session=ny_mid  •  ONLY when RSI 60-70 strong

### L18.  `H20=H20a AND H60=H60a AND RSI=RSI5 AND session_bucket=ny_close`
- Raw: n=176  W=64/L=112  WR=36.4%
- Sharpen: no sharper sub-pattern
- **Sharp: n=176  W=64/L=112  WR=36.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 60-70 strong; session=ny_close

### L19.  `H20=H20a AND T1=T1c AND RSI=RSI5 AND session_bucket=ny_close`
- Raw: n=176  W=64/L=112  WR=36.4%
- Sharpen: no sharper sub-pattern
- **Sharp: n=176  W=64/L=112  WR=36.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 60-70 strong; session=ny_close

### L20.  `H20=H20a AND RSI=RSI5 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=176  W=64/L=112  WR=36.4%
- Sharpen: no sharper sub-pattern
- **Sharp: n=176  W=64/L=112  WR=36.4%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 60-70 strong; session=ny_close

### L21.  `H20=H20e AND H60=H60e AND T4=T4a AND RSI=RSI4`
- Raw: n=161  W=64/L=97  WR=39.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=161  W=64/L=97  WR=39.8%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend WITH trade; RSI 50-60 upper neutral

### L22.  `H20=H20e AND T4=T4a AND RSI=RSI4 AND direction_exec=long`
- Raw: n=161  W=64/L=97  WR=39.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=161  W=64/L=97  WR=39.8%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend WITH trade; RSI 50-60 upper neutral

### L23.  `H60=H60a AND T4=T4c AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=160  W=59/L=101  WR=36.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=160  W=59/L=101  WR=36.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; zscore +1 to +2 overbought; session=asia

### L24.  `T1=T1c AND T4=T4c AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=160  W=59/L=101  WR=36.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=160  W=59/L=101  WR=36.9%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore +1 to +2 overbought; session=asia

### L25.  `T4=T4c AND ZS=ZS4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=160  W=59/L=101  WR=36.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=160  W=59/L=101  WR=36.9%**
- **Dir: SHORT**  •  4h trend AGAINST trade; zscore +1 to +2 overbought; session=asia

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
