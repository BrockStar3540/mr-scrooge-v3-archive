# NZD_JPY — R27 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50a**  (EMA50 up >0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **1,977**  (W=1,270 / L=707)  -  WR: **64.2%**

## Session distribution

- asia: n=459  W=304/L=155  WR=66.2%
- london_open: n=342  W=216/L=126  WR=63.2%
- ny_mid: n=305  W=202/L=103  WR=66.2%
- ny_close: n=260  W=174/L=86  WR=66.9%
- ny_open: n=218  W=134/L=84  WR=61.5%
- off_hours: n=134  W=77/L=57  WR=57.5%
- asia_late: n=133  W=80/L=53  WR=60.2%
- london: n=126  W=83/L=43  WR=65.9%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60a AND T1=T1a AND RSI=RSI7`
- Raw: n=240  W=208/L=32  WR=86.7%
- Refine: exclude session_bucket=off_hours drops 10/32 losers (31%)
- **Final: n=224  W=202/L=22  WR=90.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI>80 extreme overbought  •  AVOID when session=off_hours

### W02.  `H60=H60a AND T4=T4a AND RSI=RSI7`
- Raw: n=240  W=208/L=32  WR=86.7%
- Refine: exclude session_bucket=off_hours drops 10/32 losers (31%)
- **Final: n=224  W=202/L=22  WR=90.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI>80 extreme overbought  •  AVOID when session=off_hours

### W03.  `H60=H60a AND RSI=RSI7 AND direction_exec=long`
- Raw: n=240  W=208/L=32  WR=86.7%
- Refine: exclude session_bucket=off_hours drops 10/32 losers (31%)
- **Final: n=224  W=202/L=22  WR=90.2%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI>80 extreme overbought  •  AVOID when session=off_hours

### W04.  `T1=T1a AND T4=T4a AND RSI=RSI7`
- Raw: n=240  W=208/L=32  WR=86.7%
- Refine: exclude session_bucket=off_hours drops 10/32 losers (31%)
- **Final: n=224  W=202/L=22  WR=90.2%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI>80 extreme overbought  •  AVOID when session=off_hours

### W05.  `T1=T1a AND RSI=RSI7 AND direction_exec=long`
- Raw: n=240  W=208/L=32  WR=86.7%
- Refine: exclude session_bucket=off_hours drops 10/32 losers (31%)
- **Final: n=224  W=202/L=22  WR=90.2%**
- **Dir: LONG**  •  1h trend WITH trade; RSI>80 extreme overbought  •  AVOID when session=off_hours

### W06.  `T4=T4a AND RSI=RSI7 AND direction_exec=long`
- Raw: n=240  W=208/L=32  WR=86.7%
- Refine: exclude session_bucket=off_hours drops 10/32 losers (31%)
- **Final: n=224  W=202/L=22  WR=90.2%**
- **Dir: LONG**  •  4h trend WITH trade; RSI>80 extreme overbought  •  AVOID when session=off_hours

### W07.  `H60=H60a AND T1=T1a AND T4=T4a AND RSI=RSI7`
- Raw: n=240  W=208/L=32  WR=86.7%
- Refine: exclude session_bucket=off_hours drops 10/32 losers (31%)
- **Final: n=224  W=202/L=22  WR=90.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; RSI>80 extreme overbought  •  AVOID when session=off_hours

### W08.  `H60=H60a AND T1=T1a AND RSI=RSI7 AND direction_exec=long`
- Raw: n=240  W=208/L=32  WR=86.7%
- Refine: exclude session_bucket=off_hours drops 10/32 losers (31%)
- **Final: n=224  W=202/L=22  WR=90.2%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI>80 extreme overbought  •  AVOID when session=off_hours

### W09.  `H60=H60a AND T4=T4a AND RSI=RSI7 AND direction_exec=long`
- Raw: n=240  W=208/L=32  WR=86.7%
- Refine: exclude session_bucket=off_hours drops 10/32 losers (31%)
- **Final: n=224  W=202/L=22  WR=90.2%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI>80 extreme overbought  •  AVOID when session=off_hours

### W10.  `T1=T1a AND T4=T4a AND RSI=RSI7 AND direction_exec=long`
- Raw: n=240  W=208/L=32  WR=86.7%
- Refine: exclude session_bucket=off_hours drops 10/32 losers (31%)
- **Final: n=224  W=202/L=22  WR=90.2%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; RSI>80 extreme overbought  •  AVOID when session=off_hours

### W11.  `H20=H20a AND H60=H60a AND RSI=RSI7`
- Raw: n=181  W=156/L=25  WR=86.2%
- Refine: exclude session_bucket=off_hours drops 10/25 losers (40%)
- **Final: n=165  W=150/L=15  WR=90.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI>80 extreme overbought  •  AVOID when session=off_hours

### W12.  `H20=H20a AND T1=T1a AND RSI=RSI7`
- Raw: n=181  W=156/L=25  WR=86.2%
- Refine: exclude session_bucket=off_hours drops 10/25 losers (40%)
- **Final: n=165  W=150/L=15  WR=90.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI>80 extreme overbought  •  AVOID when session=off_hours

### W13.  `H20=H20a AND T4=T4a AND RSI=RSI7`
- Raw: n=181  W=156/L=25  WR=86.2%
- Refine: exclude session_bucket=off_hours drops 10/25 losers (40%)
- **Final: n=165  W=150/L=15  WR=90.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI>80 extreme overbought  •  AVOID when session=off_hours

### W14.  `H20=H20a AND RSI=RSI7 AND direction_exec=long`
- Raw: n=181  W=156/L=25  WR=86.2%
- Refine: exclude session_bucket=off_hours drops 10/25 losers (40%)
- **Final: n=165  W=150/L=15  WR=90.9%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI>80 extreme overbought  •  AVOID when session=off_hours

### W15.  `H20=H20a AND H60=H60a AND T1=T1a AND RSI=RSI7`
- Raw: n=181  W=156/L=25  WR=86.2%
- Refine: exclude session_bucket=off_hours drops 10/25 losers (40%)
- **Final: n=165  W=150/L=15  WR=90.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; RSI>80 extreme overbought  •  AVOID when session=off_hours

### W16.  `H20=H20a AND H60=H60a AND T4=T4a AND RSI=RSI7`
- Raw: n=181  W=156/L=25  WR=86.2%
- Refine: exclude session_bucket=off_hours drops 10/25 losers (40%)
- **Final: n=165  W=150/L=15  WR=90.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade; RSI>80 extreme overbought  •  AVOID when session=off_hours

### W17.  `H20=H20a AND H60=H60a AND RSI=RSI7 AND direction_exec=long`
- Raw: n=181  W=156/L=25  WR=86.2%
- Refine: exclude session_bucket=off_hours drops 10/25 losers (40%)
- **Final: n=165  W=150/L=15  WR=90.9%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI>80 extreme overbought  •  AVOID when session=off_hours

### W18.  `H20=H20a AND T1=T1a AND T4=T4a AND RSI=RSI7`
- Raw: n=181  W=156/L=25  WR=86.2%
- Refine: exclude session_bucket=off_hours drops 10/25 losers (40%)
- **Final: n=165  W=150/L=15  WR=90.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; RSI>80 extreme overbought  •  AVOID when session=off_hours

### W19.  `H20=H20a AND T1=T1a AND RSI=RSI7 AND direction_exec=long`
- Raw: n=181  W=156/L=25  WR=86.2%
- Refine: exclude session_bucket=off_hours drops 10/25 losers (40%)
- **Final: n=165  W=150/L=15  WR=90.9%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI>80 extreme overbought  •  AVOID when session=off_hours

### W20.  `H20=H20a AND T4=T4a AND RSI=RSI7 AND direction_exec=long`
- Raw: n=181  W=156/L=25  WR=86.2%
- Refine: exclude session_bucket=off_hours drops 10/25 losers (40%)
- **Final: n=165  W=150/L=15  WR=90.9%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI>80 extreme overbought  •  AVOID when session=off_hours

### W21.  `H60=H60a AND BBP=BBP4 AND RSI=RSI7`
- Raw: n=159  W=142/L=17  WR=89.3%
- Refine: exclude session_bucket=off_hours drops 5/17 losers (29%)
- **Final: n=154  W=142/L=12  WR=92.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; upper third; RSI>80 extreme overbought  •  AVOID when session=off_hours

### W22.  `T1=T1a AND BBP=BBP4 AND RSI=RSI7`
- Raw: n=159  W=142/L=17  WR=89.3%
- Refine: exclude session_bucket=off_hours drops 5/17 losers (29%)
- **Final: n=154  W=142/L=12  WR=92.2%**
- **Dir: ?**  •  1h trend WITH trade; upper third; RSI>80 extreme overbought  •  AVOID when session=off_hours

### W23.  `T4=T4a AND BBP=BBP4 AND RSI=RSI7`
- Raw: n=159  W=142/L=17  WR=89.3%
- Refine: exclude session_bucket=off_hours drops 5/17 losers (29%)
- **Final: n=154  W=142/L=12  WR=92.2%**
- **Dir: ?**  •  4h trend WITH trade; upper third; RSI>80 extreme overbought  •  AVOID when session=off_hours

### W24.  `BBP=BBP4 AND RSI=RSI7 AND direction_exec=long`
- Raw: n=159  W=142/L=17  WR=89.3%
- Refine: exclude session_bucket=off_hours drops 5/17 losers (29%)
- **Final: n=154  W=142/L=12  WR=92.2%**
- **Dir: LONG**  •  upper third; RSI>80 extreme overbought  •  AVOID when session=off_hours

### W25.  `H60=H60a AND T1=T1a AND BBP=BBP4 AND RSI=RSI7`
- Raw: n=159  W=142/L=17  WR=89.3%
- Refine: exclude session_bucket=off_hours drops 5/17 losers (29%)
- **Final: n=154  W=142/L=12  WR=92.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; upper third; RSI>80 extreme overbought  •  AVOID when session=off_hours

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND T1=T1c AND RSI=RSI7`
- Raw: n=178  W=54/L=124  WR=30.3%
- Sharpen: sharpest is session_bucket=ny_open (26/124 of losers there)
- **Sharp: n=26  W=0/L=26  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI>80 extreme overbought  •  ONLY when session=ny_open

### L02.  `H60=H60e AND T4=T4c AND RSI=RSI7`
- Raw: n=178  W=54/L=124  WR=30.3%
- Sharpen: sharpest is session_bucket=ny_open (26/124 of losers there)
- **Sharp: n=26  W=0/L=26  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI>80 extreme overbought  •  ONLY when session=ny_open

### L03.  `H60=H60e AND RSI=RSI7 AND direction_exec=short`
- Raw: n=178  W=54/L=124  WR=30.3%
- Sharpen: sharpest is session_bucket=ny_open (26/124 of losers there)
- **Sharp: n=26  W=0/L=26  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI>80 extreme overbought  •  ONLY when session=ny_open

### L04.  `T1=T1c AND T4=T4c AND RSI=RSI7`
- Raw: n=178  W=54/L=124  WR=30.3%
- Sharpen: sharpest is session_bucket=ny_open (26/124 of losers there)
- **Sharp: n=26  W=0/L=26  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI>80 extreme overbought  •  ONLY when session=ny_open

### L05.  `T1=T1c AND RSI=RSI7 AND direction_exec=short`
- Raw: n=178  W=54/L=124  WR=30.3%
- Sharpen: sharpest is session_bucket=ny_open (26/124 of losers there)
- **Sharp: n=26  W=0/L=26  WR=0.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI>80 extreme overbought  •  ONLY when session=ny_open

### L06.  `T4=T4c AND RSI=RSI7 AND direction_exec=short`
- Raw: n=178  W=54/L=124  WR=30.3%
- Sharpen: sharpest is session_bucket=ny_open (26/124 of losers there)
- **Sharp: n=26  W=0/L=26  WR=0.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI>80 extreme overbought  •  ONLY when session=ny_open

### L07.  `H60=H60e AND T1=T1c AND T4=T4c AND RSI=RSI7`
- Raw: n=178  W=54/L=124  WR=30.3%
- Sharpen: sharpest is session_bucket=ny_open (26/124 of losers there)
- **Sharp: n=26  W=0/L=26  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI>80 extreme overbought  •  ONLY when session=ny_open

### L08.  `H60=H60e AND T1=T1c AND RSI=RSI7 AND direction_exec=short`
- Raw: n=178  W=54/L=124  WR=30.3%
- Sharpen: sharpest is session_bucket=ny_open (26/124 of losers there)
- **Sharp: n=26  W=0/L=26  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI>80 extreme overbought  •  ONLY when session=ny_open

### L09.  `H60=H60e AND T4=T4c AND RSI=RSI7 AND direction_exec=short`
- Raw: n=178  W=54/L=124  WR=30.3%
- Sharpen: sharpest is session_bucket=ny_open (26/124 of losers there)
- **Sharp: n=26  W=0/L=26  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI>80 extreme overbought  •  ONLY when session=ny_open

### L10.  `T1=T1c AND T4=T4c AND RSI=RSI7 AND direction_exec=short`
- Raw: n=178  W=54/L=124  WR=30.3%
- Sharpen: sharpest is session_bucket=ny_open (26/124 of losers there)
- **Sharp: n=26  W=0/L=26  WR=0.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI>80 extreme overbought  •  ONLY when session=ny_open

### L11.  `H20=H20e AND H60=H60e AND RSI=RSI7`
- Raw: n=135  W=39/L=96  WR=28.9%
- Sharpen: sharpest is session_bucket=ny_close (22/96 of losers there)
- **Sharp: n=25  W=3/L=22  WR=12.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI>80 extreme overbought  •  ONLY when session=ny_close

### L12.  `H20=H20e AND T1=T1c AND RSI=RSI7`
- Raw: n=135  W=39/L=96  WR=28.9%
- Sharpen: sharpest is session_bucket=ny_close (22/96 of losers there)
- **Sharp: n=25  W=3/L=22  WR=12.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI>80 extreme overbought  •  ONLY when session=ny_close

### L13.  `H20=H20e AND T4=T4c AND RSI=RSI7`
- Raw: n=135  W=39/L=96  WR=28.9%
- Sharpen: sharpest is session_bucket=ny_close (22/96 of losers there)
- **Sharp: n=25  W=3/L=22  WR=12.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI>80 extreme overbought  •  ONLY when session=ny_close

### L14.  `H20=H20e AND RSI=RSI7 AND direction_exec=short`
- Raw: n=135  W=39/L=96  WR=28.9%
- Sharpen: sharpest is session_bucket=ny_close (22/96 of losers there)
- **Sharp: n=25  W=3/L=22  WR=12.0%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI>80 extreme overbought  •  ONLY when session=ny_close

### L15.  `H20=H20e AND H60=H60e AND T1=T1c AND RSI=RSI7`
- Raw: n=135  W=39/L=96  WR=28.9%
- Sharpen: sharpest is session_bucket=ny_close (22/96 of losers there)
- **Sharp: n=25  W=3/L=22  WR=12.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; RSI>80 extreme overbought  •  ONLY when session=ny_close

### L16.  `H20=H20e AND H60=H60e AND T4=T4c AND RSI=RSI7`
- Raw: n=135  W=39/L=96  WR=28.9%
- Sharpen: sharpest is session_bucket=ny_close (22/96 of losers there)
- **Sharp: n=25  W=3/L=22  WR=12.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; RSI>80 extreme overbought  •  ONLY when session=ny_close

### L17.  `H20=H20e AND H60=H60e AND RSI=RSI7 AND direction_exec=short`
- Raw: n=135  W=39/L=96  WR=28.9%
- Sharpen: sharpest is session_bucket=ny_close (22/96 of losers there)
- **Sharp: n=25  W=3/L=22  WR=12.0%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; RSI>80 extreme overbought  •  ONLY when session=ny_close

### L18.  `H20=H20e AND T1=T1c AND T4=T4c AND RSI=RSI7`
- Raw: n=135  W=39/L=96  WR=28.9%
- Sharpen: sharpest is session_bucket=ny_close (22/96 of losers there)
- **Sharp: n=25  W=3/L=22  WR=12.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI>80 extreme overbought  •  ONLY when session=ny_close

### L19.  `H20=H20e AND T1=T1c AND RSI=RSI7 AND direction_exec=short`
- Raw: n=135  W=39/L=96  WR=28.9%
- Sharpen: sharpest is session_bucket=ny_close (22/96 of losers there)
- **Sharp: n=25  W=3/L=22  WR=12.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI>80 extreme overbought  •  ONLY when session=ny_close

### L20.  `H20=H20e AND T4=T4c AND RSI=RSI7 AND direction_exec=short`
- Raw: n=135  W=39/L=96  WR=28.9%
- Sharpen: sharpest is session_bucket=ny_close (22/96 of losers there)
- **Sharp: n=25  W=3/L=22  WR=12.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI>80 extreme overbought  •  ONLY when session=ny_close

### L21.  `H60=H60e AND BBP=BBP4 AND RSI=RSI7`
- Raw: n=117  W=29/L=88  WR=24.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=117  W=29/L=88  WR=24.8%**
- **Dir: ?**  •  HTF60 strongly against; upper third; RSI>80 extreme overbought

### L22.  `T1=T1c AND BBP=BBP4 AND RSI=RSI7`
- Raw: n=117  W=29/L=88  WR=24.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=117  W=29/L=88  WR=24.8%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; RSI>80 extreme overbought

### L23.  `T4=T4c AND BBP=BBP4 AND RSI=RSI7`
- Raw: n=117  W=29/L=88  WR=24.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=117  W=29/L=88  WR=24.8%**
- **Dir: ?**  •  4h trend AGAINST trade; upper third; RSI>80 extreme overbought

### L24.  `BBP=BBP4 AND RSI=RSI7 AND direction_exec=short`
- Raw: n=117  W=29/L=88  WR=24.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=117  W=29/L=88  WR=24.8%**
- **Dir: SHORT**  •  upper third; RSI>80 extreme overbought

### L25.  `H60=H60e AND T1=T1c AND BBP=BBP4 AND RSI=RSI7`
- Raw: n=117  W=29/L=88  WR=24.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=117  W=29/L=88  WR=24.8%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; upper third; RSI>80 extreme overbought

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | H20e(40/46) |
| H60 | H60a(55/43) | H60e(45/57) |
| T1 | T1a(55/43) | T1c(45/57) |
| T4 | T4a(55/43) | T4c(45/57) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(55/43) | short(45/57) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
