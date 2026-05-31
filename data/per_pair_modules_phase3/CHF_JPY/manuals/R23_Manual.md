# CHF_JPY — R23 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_3**  (5m ATR >120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50a**  (EMA50 up >0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **3,994**  (W=2,317 / L=1,677)  -  WR: **58.0%**

## Session distribution

- ny_mid: n=1284  W=745/L=539  WR=58.0%
- london_open: n=1254  W=736/L=518  WR=58.7%
- asia: n=811  W=467/L=344  WR=57.6%
- ny_open: n=264  W=138/L=126  WR=52.3%
- london: n=157  W=91/L=66  WR=58.0%
- ny_close: n=111  W=74/L=37  WR=66.7%
- asia_late: n=76  W=46/L=30  WR=60.5%
- off_hours: n=37  W=20/L=17  WR=54.1%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20c AND T1=T1a AND RSI=RSI5`
- Raw: n=110  W=102/L=8  WR=92.7%
- Refine: exclude BBP=BBP5 drops 6/8 losers (75%)
- **Final: n=68  W=66/L=2  WR=97.1%**
- **Dir: ?**  •  HTF20 neutral; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when just touched upper band

### W02.  `H20=H20c AND T4=T4a AND RSI=RSI5`
- Raw: n=110  W=102/L=8  WR=92.7%
- Refine: exclude BBP=BBP5 drops 6/8 losers (75%)
- **Final: n=68  W=66/L=2  WR=97.1%**
- **Dir: ?**  •  HTF20 neutral; 4h trend WITH trade; RSI 60-70 strong  •  AVOID when just touched upper band

### W03.  `H20=H20c AND RSI=RSI5 AND direction_exec=long`
- Raw: n=110  W=102/L=8  WR=92.7%
- Refine: exclude BBP=BBP5 drops 6/8 losers (75%)
- **Final: n=68  W=66/L=2  WR=97.1%**
- **Dir: LONG**  •  HTF20 neutral; RSI 60-70 strong  •  AVOID when just touched upper band

### W04.  `H20=H20c AND T1=T1a AND T4=T4a AND RSI=RSI5`
- Raw: n=110  W=102/L=8  WR=92.7%
- Refine: exclude BBP=BBP5 drops 6/8 losers (75%)
- **Final: n=68  W=66/L=2  WR=97.1%**
- **Dir: ?**  •  HTF20 neutral; 1h trend WITH trade; 4h trend WITH trade; RSI 60-70 strong  •  AVOID when just touched upper band

### W05.  `H20=H20c AND T1=T1a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=110  W=102/L=8  WR=92.7%
- Refine: exclude BBP=BBP5 drops 6/8 losers (75%)
- **Final: n=68  W=66/L=2  WR=97.1%**
- **Dir: LONG**  •  HTF20 neutral; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when just touched upper band

### W06.  `H20=H20c AND T4=T4a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=110  W=102/L=8  WR=92.7%
- Refine: exclude BBP=BBP5 drops 6/8 losers (75%)
- **Final: n=68  W=66/L=2  WR=97.1%**
- **Dir: LONG**  •  HTF20 neutral; 4h trend WITH trade; RSI 60-70 strong  •  AVOID when just touched upper band

### W07.  `H20=H20c AND H60=H60a AND RSI=RSI5`
- Raw: n=106  W=98/L=8  WR=92.5%
- Refine: exclude BBP=BBP5 drops 6/8 losers (75%)
- **Final: n=64  W=62/L=2  WR=96.9%**
- **Dir: ?**  •  HTF20 neutral; HTF60 aligned WITH trade; RSI 60-70 strong  •  AVOID when just touched upper band

### W08.  `H20=H20c AND H60=H60a AND T1=T1a AND RSI=RSI5`
- Raw: n=106  W=98/L=8  WR=92.5%
- Refine: exclude BBP=BBP5 drops 6/8 losers (75%)
- **Final: n=64  W=62/L=2  WR=96.9%**
- **Dir: ?**  •  HTF20 neutral; HTF60 aligned WITH trade; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when just touched upper band

### W09.  `H20=H20c AND H60=H60a AND T4=T4a AND RSI=RSI5`
- Raw: n=106  W=98/L=8  WR=92.5%
- Refine: exclude BBP=BBP5 drops 6/8 losers (75%)
- **Final: n=64  W=62/L=2  WR=96.9%**
- **Dir: ?**  •  HTF20 neutral; HTF60 aligned WITH trade; 4h trend WITH trade; RSI 60-70 strong  •  AVOID when just touched upper band

### W10.  `H20=H20c AND H60=H60a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=106  W=98/L=8  WR=92.5%
- Refine: exclude BBP=BBP5 drops 6/8 losers (75%)
- **Final: n=64  W=62/L=2  WR=96.9%**
- **Dir: LONG**  •  HTF20 neutral; HTF60 aligned WITH trade; RSI 60-70 strong  •  AVOID when just touched upper band

### W11.  `T1=T1a AND T4=T4c AND session_bucket=london_open`
- Raw: n=99  W=85/L=14  WR=85.9%
- Refine: exclude RSI=RSI4 drops 12/14 losers (86%)
- **Final: n=79  W=77/L=2  WR=97.5%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; session=london_open  •  AVOID when RSI 50-60 upper neutral

### W12.  `H20=H20c AND H60=H60a AND ZS=ZS4`
- Raw: n=88  W=75/L=13  WR=85.2%
- Refine: exclude RSI=RSI4 drops 11/13 losers (85%)
- **Final: n=63  W=61/L=2  WR=96.8%**
- **Dir: ?**  •  HTF20 neutral; HTF60 aligned WITH trade; zscore +1 to +2 overbought  •  AVOID when RSI 50-60 upper neutral

### W13.  `H20=H20c AND T1=T1a AND ZS=ZS4`
- Raw: n=88  W=75/L=13  WR=85.2%
- Refine: exclude RSI=RSI4 drops 11/13 losers (85%)
- **Final: n=63  W=61/L=2  WR=96.8%**
- **Dir: ?**  •  HTF20 neutral; 1h trend WITH trade; zscore +1 to +2 overbought  •  AVOID when RSI 50-60 upper neutral

### W14.  `H20=H20c AND T4=T4a AND ZS=ZS4`
- Raw: n=88  W=75/L=13  WR=85.2%
- Refine: exclude RSI=RSI4 drops 11/13 losers (85%)
- **Final: n=63  W=61/L=2  WR=96.8%**
- **Dir: ?**  •  HTF20 neutral; 4h trend WITH trade; zscore +1 to +2 overbought  •  AVOID when RSI 50-60 upper neutral

### W15.  `H20=H20c AND ZS=ZS4 AND direction_exec=long`
- Raw: n=88  W=75/L=13  WR=85.2%
- Refine: exclude RSI=RSI4 drops 11/13 losers (85%)
- **Final: n=63  W=61/L=2  WR=96.8%**
- **Dir: LONG**  •  HTF20 neutral; zscore +1 to +2 overbought  •  AVOID when RSI 50-60 upper neutral

### W16.  `H20=H20c AND H60=H60a AND T1=T1a AND ZS=ZS4`
- Raw: n=88  W=75/L=13  WR=85.2%
- Refine: exclude RSI=RSI4 drops 11/13 losers (85%)
- **Final: n=63  W=61/L=2  WR=96.8%**
- **Dir: ?**  •  HTF20 neutral; HTF60 aligned WITH trade; 1h trend WITH trade; zscore +1 to +2 overbought  •  AVOID when RSI 50-60 upper neutral

### W17.  `H20=H20c AND H60=H60a AND T4=T4a AND ZS=ZS4`
- Raw: n=88  W=75/L=13  WR=85.2%
- Refine: exclude RSI=RSI4 drops 11/13 losers (85%)
- **Final: n=63  W=61/L=2  WR=96.8%**
- **Dir: ?**  •  HTF20 neutral; HTF60 aligned WITH trade; 4h trend WITH trade; zscore +1 to +2 overbought  •  AVOID when RSI 50-60 upper neutral

### W18.  `H20=H20c AND H60=H60a AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=88  W=75/L=13  WR=85.2%
- Refine: exclude RSI=RSI4 drops 11/13 losers (85%)
- **Final: n=63  W=61/L=2  WR=96.8%**
- **Dir: ?**  •  HTF20 neutral; HTF60 aligned WITH trade; upper third; zscore +1 to +2 overbought  •  AVOID when RSI 50-60 upper neutral

### W19.  `H20=H20c AND H60=H60a AND ZS=ZS4 AND direction_exec=long`
- Raw: n=88  W=75/L=13  WR=85.2%
- Refine: exclude RSI=RSI4 drops 11/13 losers (85%)
- **Final: n=63  W=61/L=2  WR=96.8%**
- **Dir: LONG**  •  HTF20 neutral; HTF60 aligned WITH trade; zscore +1 to +2 overbought  •  AVOID when RSI 50-60 upper neutral

### W20.  `H20=H20c AND T1=T1a AND T4=T4a AND ZS=ZS4`
- Raw: n=88  W=75/L=13  WR=85.2%
- Refine: exclude RSI=RSI4 drops 11/13 losers (85%)
- **Final: n=63  W=61/L=2  WR=96.8%**
- **Dir: ?**  •  HTF20 neutral; 1h trend WITH trade; 4h trend WITH trade; zscore +1 to +2 overbought  •  AVOID when RSI 50-60 upper neutral

### W21.  `H20=H20c AND T1=T1a AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=88  W=75/L=13  WR=85.2%
- Refine: exclude RSI=RSI4 drops 11/13 losers (85%)
- **Final: n=63  W=61/L=2  WR=96.8%**
- **Dir: ?**  •  HTF20 neutral; 1h trend WITH trade; upper third; zscore +1 to +2 overbought  •  AVOID when RSI 50-60 upper neutral

### W22.  `H20=H20c AND T1=T1a AND ZS=ZS4 AND direction_exec=long`
- Raw: n=88  W=75/L=13  WR=85.2%
- Refine: exclude RSI=RSI4 drops 11/13 losers (85%)
- **Final: n=63  W=61/L=2  WR=96.8%**
- **Dir: LONG**  •  HTF20 neutral; 1h trend WITH trade; zscore +1 to +2 overbought  •  AVOID when RSI 50-60 upper neutral

### W23.  `H20=H20c AND T4=T4a AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=88  W=75/L=13  WR=85.2%
- Refine: exclude RSI=RSI4 drops 11/13 losers (85%)
- **Final: n=63  W=61/L=2  WR=96.8%**
- **Dir: ?**  •  HTF20 neutral; 4h trend WITH trade; upper third; zscore +1 to +2 overbought  •  AVOID when RSI 50-60 upper neutral

### W24.  `H20=H20c AND T4=T4a AND ZS=ZS4 AND direction_exec=long`
- Raw: n=88  W=75/L=13  WR=85.2%
- Refine: exclude RSI=RSI4 drops 11/13 losers (85%)
- **Final: n=63  W=61/L=2  WR=96.8%**
- **Dir: LONG**  •  HTF20 neutral; 4h trend WITH trade; zscore +1 to +2 overbought  •  AVOID when RSI 50-60 upper neutral

### W25.  `H20=H20c AND BBP=BBP4 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=88  W=75/L=13  WR=85.2%
- Refine: exclude RSI=RSI4 drops 11/13 losers (85%)
- **Final: n=63  W=61/L=2  WR=96.8%**
- **Dir: LONG**  •  HTF20 neutral; upper third; zscore +1 to +2 overbought  •  AVOID when RSI 50-60 upper neutral

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T4=T4c AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=291  W=115/L=176  WR=39.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=291  W=115/L=176  WR=39.5%**
- **Dir: ?**  •  4h trend AGAINST trade; just touched upper band; zscore +2 to +3 deep overbought

### L02.  `H20=H20e AND T4=T4c AND ZS=ZS5`
- Raw: n=287  W=111/L=176  WR=38.7%
- Sharpen: no sharper sub-pattern
- **Sharp: n=287  W=111/L=176  WR=38.7%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; zscore +2 to +3 deep overbought

### L03.  `H20=H20e AND H60=H60e AND T4=T4c AND ZS=ZS5`
- Raw: n=287  W=111/L=176  WR=38.7%
- Sharpen: no sharper sub-pattern
- **Sharp: n=287  W=111/L=176  WR=38.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; zscore +2 to +3 deep overbought

### L04.  `H20=H20e AND T1=T1c AND T4=T4c AND ZS=ZS5`
- Raw: n=287  W=111/L=176  WR=38.7%
- Sharpen: no sharper sub-pattern
- **Sharp: n=287  W=111/L=176  WR=38.7%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought

### L05.  `H20=H20e AND T4=T4c AND ZS=ZS5 AND direction_exec=short`
- Raw: n=287  W=111/L=176  WR=38.7%
- Sharpen: no sharper sub-pattern
- **Sharp: n=287  W=111/L=176  WR=38.7%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade; zscore +2 to +3 deep overbought

### L06.  `T4=T4c AND RSI=RSI6 AND ZS=ZS5`
- Raw: n=285  W=112/L=173  WR=39.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=285  W=112/L=173  WR=39.3%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 70-80 overbought; zscore +2 to +3 deep overbought

### L07.  `H60=H60e AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=270  W=105/L=165  WR=38.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=270  W=105/L=165  WR=38.9%**
- **Dir: ?**  •  HTF60 strongly against; RSI 60-70 strong; session=london_open

### L08.  `T1=T1c AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=270  W=105/L=165  WR=38.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=270  W=105/L=165  WR=38.9%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 60-70 strong; session=london_open

### L09.  `RSI=RSI5 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=270  W=105/L=165  WR=38.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=270  W=105/L=165  WR=38.9%**
- **Dir: SHORT**  •  RSI 60-70 strong; session=london_open

### L10.  `H60=H60e AND T1=T1c AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=270  W=105/L=165  WR=38.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=270  W=105/L=165  WR=38.9%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 60-70 strong; session=london_open

### L11.  `H60=H60e AND RSI=RSI5 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=270  W=105/L=165  WR=38.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=270  W=105/L=165  WR=38.9%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 60-70 strong; session=london_open

### L12.  `T1=T1c AND RSI=RSI5 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=270  W=105/L=165  WR=38.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=270  W=105/L=165  WR=38.9%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 60-70 strong; session=london_open

### L13.  `H60=H60e AND T4=T4c AND RSI=RSI6 AND ZS=ZS5`
- Raw: n=229  W=88/L=141  WR=38.4%
- Sharpen: no sharper sub-pattern
- **Sharp: n=229  W=88/L=141  WR=38.4%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 70-80 overbought; zscore +2 to +3 deep overbought

### L14.  `T1=T1c AND T4=T4c AND RSI=RSI6 AND ZS=ZS5`
- Raw: n=229  W=88/L=141  WR=38.4%
- Sharpen: no sharper sub-pattern
- **Sharp: n=229  W=88/L=141  WR=38.4%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 70-80 overbought; zscore +2 to +3 deep overbought

### L15.  `T4=T4c AND RSI=RSI6 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=229  W=88/L=141  WR=38.4%
- Sharpen: no sharper sub-pattern
- **Sharp: n=229  W=88/L=141  WR=38.4%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 70-80 overbought; zscore +2 to +3 deep overbought

### L16.  `H60=H60e AND T4=T4c AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=218  W=86/L=132  WR=39.4%
- Sharpen: no sharper sub-pattern
- **Sharp: n=218  W=86/L=132  WR=39.4%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 60-70 strong; session=london_open

### L17.  `T1=T1c AND T4=T4c AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=218  W=86/L=132  WR=39.4%
- Sharpen: no sharper sub-pattern
- **Sharp: n=218  W=86/L=132  WR=39.4%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 60-70 strong; session=london_open

### L18.  `T4=T4c AND RSI=RSI5 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=218  W=86/L=132  WR=39.4%
- Sharpen: no sharper sub-pattern
- **Sharp: n=218  W=86/L=132  WR=39.4%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 60-70 strong; session=london_open

### L19.  `H20=H20e AND T4=T4c AND RSI=RSI6 AND ZS=ZS5`
- Raw: n=216  W=83/L=133  WR=38.4%
- Sharpen: no sharper sub-pattern
- **Sharp: n=216  W=83/L=133  WR=38.4%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 70-80 overbought; zscore +2 to +3 deep overbought

### L20.  `H20=H20c AND T1=T1c AND T4=T4c`
- Raw: n=162  W=55/L=107  WR=34.0%
- Sharpen: sharpest is session_bucket=asia (32/107 of losers there)
- **Sharp: n=32  W=0/L=32  WR=0.0%**
- **Dir: ?**  •  HTF20 neutral; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when session=asia

### L21.  `H20=H20c AND T1=T1c AND direction_exec=short`
- Raw: n=162  W=55/L=107  WR=34.0%
- Sharpen: sharpest is session_bucket=asia (32/107 of losers there)
- **Sharp: n=32  W=0/L=32  WR=0.0%**
- **Dir: SHORT**  •  HTF20 neutral; 1h trend AGAINST trade  •  ONLY when session=asia

### L22.  `H20=H20c AND T4=T4c AND direction_exec=short`
- Raw: n=162  W=55/L=107  WR=34.0%
- Sharpen: sharpest is session_bucket=asia (32/107 of losers there)
- **Sharp: n=32  W=0/L=32  WR=0.0%**
- **Dir: SHORT**  •  HTF20 neutral; 4h trend AGAINST trade  •  ONLY when session=asia

### L23.  `H20=H20c AND T1=T1c AND T4=T4c AND direction_exec=short`
- Raw: n=162  W=55/L=107  WR=34.0%
- Sharpen: sharpest is session_bucket=asia (32/107 of losers there)
- **Sharp: n=32  W=0/L=32  WR=0.0%**
- **Dir: SHORT**  •  HTF20 neutral; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when session=asia

### L24.  `H20=H20c AND H60=H60e AND T1=T1c`
- Raw: n=160  W=55/L=105  WR=34.4%
- Sharpen: sharpest is session_bucket=asia (32/105 of losers there)
- **Sharp: n=32  W=0/L=32  WR=0.0%**
- **Dir: ?**  •  HTF20 neutral; HTF60 strongly against; 1h trend AGAINST trade  •  ONLY when session=asia

### L25.  `H20=H20c AND H60=H60e AND T4=T4c`
- Raw: n=160  W=55/L=105  WR=34.4%
- Sharpen: sharpest is session_bucket=asia (32/105 of losers there)
- **Sharp: n=32  W=0/L=32  WR=0.0%**
- **Dir: ?**  •  HTF20 neutral; HTF60 strongly against; 4h trend AGAINST trade  •  ONLY when session=asia

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | H20e(35/41) |
| H60 | H60a(53/43) | H60e(46/55) |
| T1 | T1a(55/43) | T1c(45/57) |
| T4 | T4a(53/45) | T4c(47/55) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(55/43) | short(45/57) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
