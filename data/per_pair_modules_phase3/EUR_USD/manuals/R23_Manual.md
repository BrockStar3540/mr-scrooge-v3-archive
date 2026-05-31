# EUR_USD — R23 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50a**  (EMA50 up >0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **1,987**  (W=1,241 / L=746)  -  WR: **62.5%**

## Session distribution

- ny_close: n=574  W=364/L=210  WR=63.4%
- ny_open: n=335  W=207/L=128  WR=61.8%
- ny_mid: n=312  W=195/L=117  WR=62.5%
- asia: n=258  W=167/L=91  WR=64.7%
- london: n=187  W=123/L=64  WR=65.8%
- london_open: n=183  W=109/L=74  WR=59.6%
- asia_late: n=88  W=46/L=42  WR=52.3%
- off_hours: n=50  W=30/L=20  WR=60.0%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1c AND T4=T4c AND session_bucket=asia`
- Raw: n=152  W=141/L=11  WR=92.8%
- Refine: exclude ZS=ZS2 drops 4/11 losers (36%)
- **Final: n=134  W=127/L=7  WR=94.8%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=asia  •  AVOID when zscore -2 to -1 oversold

### W02.  `T1=T1c AND direction_exec=short AND session_bucket=asia`
- Raw: n=152  W=141/L=11  WR=92.8%
- Refine: exclude ZS=ZS2 drops 4/11 losers (36%)
- **Final: n=134  W=127/L=7  WR=94.8%**
- **Dir: SHORT**  •  1h trend AGAINST trade; session=asia  •  AVOID when zscore -2 to -1 oversold

### W03.  `T4=T4c AND direction_exec=short AND session_bucket=asia`
- Raw: n=152  W=141/L=11  WR=92.8%
- Refine: exclude ZS=ZS2 drops 4/11 losers (36%)
- **Final: n=134  W=127/L=7  WR=94.8%**
- **Dir: SHORT**  •  4h trend AGAINST trade; session=asia  •  AVOID when zscore -2 to -1 oversold

### W04.  `T1=T1c AND T4=T4c AND direction_exec=short AND session_bucket=asia`
- Raw: n=152  W=141/L=11  WR=92.8%
- Refine: exclude ZS=ZS2 drops 4/11 losers (36%)
- **Final: n=134  W=127/L=7  WR=94.8%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=asia  •  AVOID when zscore -2 to -1 oversold

### W05.  `H60=H60a AND T1=T1a AND RSI=RSI7`
- Raw: n=150  W=130/L=20  WR=86.7%
- Refine: exclude session_bucket=ny_close drops 10/20 losers (50%)
- **Final: n=106  W=96/L=10  WR=90.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI>80 extreme overbought  •  AVOID when session=ny_close

### W06.  `H60=H60a AND T4=T4a AND RSI=RSI7`
- Raw: n=150  W=130/L=20  WR=86.7%
- Refine: exclude session_bucket=ny_close drops 10/20 losers (50%)
- **Final: n=106  W=96/L=10  WR=90.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI>80 extreme overbought  •  AVOID when session=ny_close

### W07.  `H60=H60a AND RSI=RSI7 AND direction_exec=long`
- Raw: n=150  W=130/L=20  WR=86.7%
- Refine: exclude session_bucket=ny_close drops 10/20 losers (50%)
- **Final: n=106  W=96/L=10  WR=90.6%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI>80 extreme overbought  •  AVOID when session=ny_close

### W08.  `H60=H60a AND T1=T1a AND T4=T4a AND RSI=RSI7`
- Raw: n=150  W=130/L=20  WR=86.7%
- Refine: exclude session_bucket=ny_close drops 10/20 losers (50%)
- **Final: n=106  W=96/L=10  WR=90.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; RSI>80 extreme overbought  •  AVOID when session=ny_close

### W09.  `H60=H60a AND T1=T1a AND RSI=RSI7 AND direction_exec=long`
- Raw: n=150  W=130/L=20  WR=86.7%
- Refine: exclude session_bucket=ny_close drops 10/20 losers (50%)
- **Final: n=106  W=96/L=10  WR=90.6%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI>80 extreme overbought  •  AVOID when session=ny_close

### W10.  `H60=H60a AND T4=T4a AND RSI=RSI7 AND direction_exec=long`
- Raw: n=150  W=130/L=20  WR=86.7%
- Refine: exclude session_bucket=ny_close drops 10/20 losers (50%)
- **Final: n=106  W=96/L=10  WR=90.6%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI>80 extreme overbought  •  AVOID when session=ny_close

### W11.  `H20=H20e AND T1=T1c AND session_bucket=asia`
- Raw: n=122  W=111/L=11  WR=91.0%
- Refine: exclude ZS=ZS2 drops 4/11 losers (36%)
- **Final: n=106  W=99/L=7  WR=93.4%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; session=asia  •  AVOID when zscore -2 to -1 oversold

### W12.  `H20=H20e AND T4=T4c AND session_bucket=asia`
- Raw: n=122  W=111/L=11  WR=91.0%
- Refine: exclude ZS=ZS2 drops 4/11 losers (36%)
- **Final: n=106  W=99/L=7  WR=93.4%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; session=asia  •  AVOID when zscore -2 to -1 oversold

### W13.  `H20=H20e AND direction_exec=short AND session_bucket=asia`
- Raw: n=122  W=111/L=11  WR=91.0%
- Refine: exclude ZS=ZS2 drops 4/11 losers (36%)
- **Final: n=106  W=99/L=7  WR=93.4%**
- **Dir: SHORT**  •  HTF20 strongly against; session=asia  •  AVOID when zscore -2 to -1 oversold

### W14.  `H20=H20e AND T1=T1c AND T4=T4c AND session_bucket=asia`
- Raw: n=122  W=111/L=11  WR=91.0%
- Refine: exclude ZS=ZS2 drops 4/11 losers (36%)
- **Final: n=106  W=99/L=7  WR=93.4%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; session=asia  •  AVOID when zscore -2 to -1 oversold

### W15.  `H20=H20e AND T1=T1c AND direction_exec=short AND session_bucket=asia`
- Raw: n=122  W=111/L=11  WR=91.0%
- Refine: exclude ZS=ZS2 drops 4/11 losers (36%)
- **Final: n=106  W=99/L=7  WR=93.4%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; session=asia  •  AVOID when zscore -2 to -1 oversold

### W16.  `H20=H20e AND T4=T4c AND direction_exec=short AND session_bucket=asia`
- Raw: n=122  W=111/L=11  WR=91.0%
- Refine: exclude ZS=ZS2 drops 4/11 losers (36%)
- **Final: n=106  W=99/L=7  WR=93.4%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade; session=asia  •  AVOID when zscore -2 to -1 oversold

### W17.  `H60=H60e AND T1=T1c AND session_bucket=asia`
- Raw: n=111  W=102/L=9  WR=91.9%
- Refine: exclude ZS=ZS2 drops 4/9 losers (44%)
- **Final: n=95  W=90/L=5  WR=94.7%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; session=asia  •  AVOID when zscore -2 to -1 oversold

### W18.  `H60=H60e AND T4=T4c AND session_bucket=asia`
- Raw: n=111  W=102/L=9  WR=91.9%
- Refine: exclude ZS=ZS2 drops 4/9 losers (44%)
- **Final: n=95  W=90/L=5  WR=94.7%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; session=asia  •  AVOID when zscore -2 to -1 oversold

### W19.  `H60=H60e AND direction_exec=short AND session_bucket=asia`
- Raw: n=111  W=102/L=9  WR=91.9%
- Refine: exclude ZS=ZS2 drops 4/9 losers (44%)
- **Final: n=95  W=90/L=5  WR=94.7%**
- **Dir: SHORT**  •  HTF60 strongly against; session=asia  •  AVOID when zscore -2 to -1 oversold

### W20.  `H60=H60e AND T1=T1c AND T4=T4c AND session_bucket=asia`
- Raw: n=111  W=102/L=9  WR=91.9%
- Refine: exclude ZS=ZS2 drops 4/9 losers (44%)
- **Final: n=95  W=90/L=5  WR=94.7%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; session=asia  •  AVOID when zscore -2 to -1 oversold

### W21.  `H60=H60e AND T1=T1c AND direction_exec=short AND session_bucket=asia`
- Raw: n=111  W=102/L=9  WR=91.9%
- Refine: exclude ZS=ZS2 drops 4/9 losers (44%)
- **Final: n=95  W=90/L=5  WR=94.7%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; session=asia  •  AVOID when zscore -2 to -1 oversold

### W22.  `H60=H60e AND T4=T4c AND direction_exec=short AND session_bucket=asia`
- Raw: n=111  W=102/L=9  WR=91.9%
- Refine: exclude ZS=ZS2 drops 4/9 losers (44%)
- **Final: n=95  W=90/L=5  WR=94.7%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend AGAINST trade; session=asia  •  AVOID when zscore -2 to -1 oversold

### W23.  `H60=H60a AND BBP=BBP4 AND RSI=RSI7`
- Raw: n=98  W=89/L=9  WR=90.8%
- Refine: exclude session_bucket=ny_close drops 6/9 losers (67%)
- **Final: n=62  W=59/L=3  WR=95.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; upper third; RSI>80 extreme overbought  •  AVOID when session=ny_close

### W24.  `H60=H60a AND T1=T1a AND BBP=BBP4 AND RSI=RSI7`
- Raw: n=98  W=89/L=9  WR=90.8%
- Refine: exclude session_bucket=ny_close drops 6/9 losers (67%)
- **Final: n=62  W=59/L=3  WR=95.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; upper third; RSI>80 extreme overbought  •  AVOID when session=ny_close

### W25.  `H60=H60a AND T4=T4a AND BBP=BBP4 AND RSI=RSI7`
- Raw: n=98  W=89/L=9  WR=90.8%
- Refine: exclude session_bucket=ny_close drops 6/9 losers (67%)
- **Final: n=62  W=59/L=3  WR=95.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; upper third; RSI>80 extreme overbought  •  AVOID when session=ny_close

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND T1=T1c AND RSI=RSI7`
- Raw: n=135  W=53/L=82  WR=39.3%
- Sharpen: sharpest is BBP=BBP4 (58/82 of losers there)
- **Sharp: n=80  W=22/L=58  WR=27.5%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI>80 extreme overbought  •  ONLY when upper third

### L02.  `H60=H60e AND T4=T4c AND RSI=RSI7`
- Raw: n=135  W=53/L=82  WR=39.3%
- Sharpen: sharpest is BBP=BBP4 (58/82 of losers there)
- **Sharp: n=80  W=22/L=58  WR=27.5%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI>80 extreme overbought  •  ONLY when upper third

### L03.  `H60=H60e AND RSI=RSI7 AND direction_exec=short`
- Raw: n=135  W=53/L=82  WR=39.3%
- Sharpen: sharpest is BBP=BBP4 (58/82 of losers there)
- **Sharp: n=80  W=22/L=58  WR=27.5%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI>80 extreme overbought  •  ONLY when upper third

### L04.  `H60=H60e AND T1=T1c AND T4=T4c AND RSI=RSI7`
- Raw: n=135  W=53/L=82  WR=39.3%
- Sharpen: sharpest is BBP=BBP4 (58/82 of losers there)
- **Sharp: n=80  W=22/L=58  WR=27.5%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI>80 extreme overbought  •  ONLY when upper third

### L05.  `H60=H60e AND T1=T1c AND RSI=RSI7 AND direction_exec=short`
- Raw: n=135  W=53/L=82  WR=39.3%
- Sharpen: sharpest is BBP=BBP4 (58/82 of losers there)
- **Sharp: n=80  W=22/L=58  WR=27.5%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI>80 extreme overbought  •  ONLY when upper third

### L06.  `H60=H60e AND T4=T4c AND RSI=RSI7 AND direction_exec=short`
- Raw: n=135  W=53/L=82  WR=39.3%
- Sharpen: sharpest is BBP=BBP4 (58/82 of losers there)
- **Sharp: n=80  W=22/L=58  WR=27.5%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI>80 extreme overbought  •  ONLY when upper third

### L07.  `T1=T1a AND T4=T4a AND session_bucket=asia`
- Raw: n=106  W=26/L=80  WR=24.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=106  W=26/L=80  WR=24.5%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; session=asia

### L08.  `T1=T1a AND direction_exec=long AND session_bucket=asia`
- Raw: n=106  W=26/L=80  WR=24.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=106  W=26/L=80  WR=24.5%**
- **Dir: LONG**  •  1h trend WITH trade; session=asia

### L09.  `T4=T4a AND direction_exec=long AND session_bucket=asia`
- Raw: n=106  W=26/L=80  WR=24.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=106  W=26/L=80  WR=24.5%**
- **Dir: LONG**  •  4h trend WITH trade; session=asia

### L10.  `T1=T1a AND T4=T4a AND direction_exec=long AND session_bucket=asia`
- Raw: n=106  W=26/L=80  WR=24.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=106  W=26/L=80  WR=24.5%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; session=asia

### L11.  `H20=H20a AND T1=T1a AND session_bucket=asia`
- Raw: n=93  W=26/L=67  WR=28.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=93  W=26/L=67  WR=28.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=asia

### L12.  `H20=H20a AND T4=T4a AND session_bucket=asia`
- Raw: n=93  W=26/L=67  WR=28.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=93  W=26/L=67  WR=28.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=asia

### L13.  `H20=H20a AND direction_exec=long AND session_bucket=asia`
- Raw: n=93  W=26/L=67  WR=28.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=93  W=26/L=67  WR=28.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; session=asia

### L14.  `H20=H20a AND T1=T1a AND T4=T4a AND session_bucket=asia`
- Raw: n=93  W=26/L=67  WR=28.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=93  W=26/L=67  WR=28.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; session=asia

### L15.  `H20=H20a AND T1=T1a AND direction_exec=long AND session_bucket=asia`
- Raw: n=93  W=26/L=67  WR=28.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=93  W=26/L=67  WR=28.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=asia

### L16.  `H20=H20a AND T4=T4a AND direction_exec=long AND session_bucket=asia`
- Raw: n=93  W=26/L=67  WR=28.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=93  W=26/L=67  WR=28.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=asia

### L17.  `T1=T1c AND T4=T4c AND session_bucket=london_open`
- Raw: n=87  W=33/L=54  WR=37.9%
- Sharpen: sharpest is H20=H20c (22/54 of losers there)
- **Sharp: n=22  W=0/L=22  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=london_open  •  ONLY when HTF20 neutral

### L18.  `T1=T1c AND direction_exec=short AND session_bucket=london_open`
- Raw: n=87  W=33/L=54  WR=37.9%
- Sharpen: sharpest is H20=H20c (22/54 of losers there)
- **Sharp: n=22  W=0/L=22  WR=0.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; session=london_open  •  ONLY when HTF20 neutral

### L19.  `T4=T4c AND direction_exec=short AND session_bucket=london_open`
- Raw: n=87  W=33/L=54  WR=37.9%
- Sharpen: sharpest is H20=H20c (22/54 of losers there)
- **Sharp: n=22  W=0/L=22  WR=0.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; session=london_open  •  ONLY when HTF20 neutral

### L20.  `T1=T1c AND T4=T4c AND direction_exec=short AND session_bucket=london_open`
- Raw: n=87  W=33/L=54  WR=37.9%
- Sharpen: sharpest is H20=H20c (22/54 of losers there)
- **Sharp: n=22  W=0/L=22  WR=0.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=london_open  •  ONLY when HTF20 neutral

### L21.  `H20=H20a AND H60=H60a AND session_bucket=asia`
- Raw: n=85  W=34/L=51  WR=40.0%
- Sharpen: sharpest is T1=T1a (51/51 of losers there)
- **Sharp: n=71  W=20/L=51  WR=28.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=asia  •  ONLY when 1h trend WITH trade

### L22.  `H60=H60e AND BBP=BBP4 AND RSI=RSI7`
- Raw: n=80  W=22/L=58  WR=27.5%
- Sharpen: sharpest is session_bucket=ny_open (12/58 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; upper third; RSI>80 extreme overbought  •  ONLY when session=ny_open

### L23.  `H60=H60e AND T1=T1c AND BBP=BBP4 AND RSI=RSI7`
- Raw: n=80  W=22/L=58  WR=27.5%
- Sharpen: sharpest is session_bucket=ny_open (12/58 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; upper third; RSI>80 extreme overbought  •  ONLY when session=ny_open

### L24.  `H60=H60e AND T4=T4c AND BBP=BBP4 AND RSI=RSI7`
- Raw: n=80  W=22/L=58  WR=27.5%
- Sharpen: sharpest is session_bucket=ny_open (12/58 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; upper third; RSI>80 extreme overbought  •  ONLY when session=ny_open

### L25.  `H60=H60e AND BBP=BBP4 AND RSI=RSI7 AND direction_exec=short`
- Raw: n=80  W=22/L=58  WR=27.5%
- Sharpen: sharpest is session_bucket=ny_open (12/58 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; upper third; RSI>80 extreme overbought  •  ONLY when session=ny_open

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | H60a(47/38) | H60e(40/50) |
| T1 | T1a(54/44) | T1c(45/54) |
| T4 | T4a(55/44) | T4c(45/56) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(55/44) | short(45/56) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
