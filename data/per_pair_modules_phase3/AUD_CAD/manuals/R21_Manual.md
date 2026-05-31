# AUD_CAD — R21 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **2,347**  (W=1,522 / L=825)  -  WR: **64.8%**

## Session distribution

- asia: n=740  W=465/L=275  WR=62.8%
- ny_mid: n=675  W=447/L=228  WR=66.2%
- london_open: n=256  W=153/L=103  WR=59.8%
- ny_close: n=172  W=126/L=46  WR=73.3%
- ny_open: n=155  W=93/L=62  WR=60.0%
- london: n=141  W=98/L=43  WR=69.5%
- asia_late: n=116  W=77/L=39  WR=66.4%
- off_hours: n=92  W=63/L=29  WR=68.5%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60a AND BBP=BBP4 AND session_bucket=ny_mid`
- Raw: n=204  W=177/L=27  WR=86.8%
- Refine: exclude H20=H20a drops 27/27 losers (100%)
- **Final: n=42  W=42/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; upper third; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

### W02.  `T1=T1a AND BBP=BBP4 AND session_bucket=ny_mid`
- Raw: n=204  W=177/L=27  WR=86.8%
- Refine: exclude H20=H20a drops 27/27 losers (100%)
- **Final: n=42  W=42/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; upper third; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

### W03.  `BBP=BBP4 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=204  W=177/L=27  WR=86.8%
- Refine: exclude H20=H20a drops 27/27 losers (100%)
- **Final: n=42  W=42/L=0  WR=100.0%**
- **Dir: LONG**  •  upper third; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

### W04.  `H60=H60a AND T1=T1a AND BBP=BBP4 AND session_bucket=ny_mid`
- Raw: n=204  W=177/L=27  WR=86.8%
- Refine: exclude H20=H20a drops 27/27 losers (100%)
- **Final: n=42  W=42/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; upper third; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

### W05.  `H60=H60a AND BBP=BBP4 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=204  W=177/L=27  WR=86.8%
- Refine: exclude H20=H20a drops 27/27 losers (100%)
- **Final: n=42  W=42/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; upper third; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

### W06.  `T1=T1a AND BBP=BBP4 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=204  W=177/L=27  WR=86.8%
- Refine: exclude H20=H20a drops 27/27 losers (100%)
- **Final: n=42  W=42/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend WITH trade; upper third; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

### W07.  `H60=H60a AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=195  W=173/L=22  WR=88.7%
- Refine: exclude H20=H20a drops 22/22 losers (100%)
- **Final: n=40  W=40/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; zscore +1 to +2 overbought; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

### W08.  `T1=T1a AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=195  W=173/L=22  WR=88.7%
- Refine: exclude H20=H20a drops 22/22 losers (100%)
- **Final: n=40  W=40/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; zscore +1 to +2 overbought; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

### W09.  `ZS=ZS4 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=195  W=173/L=22  WR=88.7%
- Refine: exclude H20=H20a drops 22/22 losers (100%)
- **Final: n=40  W=40/L=0  WR=100.0%**
- **Dir: LONG**  •  zscore +1 to +2 overbought; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

### W10.  `H60=H60a AND T1=T1a AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=195  W=173/L=22  WR=88.7%
- Refine: exclude H20=H20a drops 22/22 losers (100%)
- **Final: n=40  W=40/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; zscore +1 to +2 overbought; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

### W11.  `H60=H60a AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=195  W=173/L=22  WR=88.7%
- Refine: exclude H20=H20a drops 22/22 losers (100%)
- **Final: n=40  W=40/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; upper third; zscore +1 to +2 overbought; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

### W12.  `H60=H60a AND ZS=ZS4 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=195  W=173/L=22  WR=88.7%
- Refine: exclude H20=H20a drops 22/22 losers (100%)
- **Final: n=40  W=40/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; zscore +1 to +2 overbought; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

### W13.  `T1=T1a AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=195  W=173/L=22  WR=88.7%
- Refine: exclude H20=H20a drops 22/22 losers (100%)
- **Final: n=40  W=40/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; upper third; zscore +1 to +2 overbought; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

### W14.  `T1=T1a AND ZS=ZS4 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=195  W=173/L=22  WR=88.7%
- Refine: exclude H20=H20a drops 22/22 losers (100%)
- **Final: n=40  W=40/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend WITH trade; zscore +1 to +2 overbought; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

### W15.  `BBP=BBP4 AND ZS=ZS4 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=195  W=173/L=22  WR=88.7%
- Refine: exclude H20=H20a drops 22/22 losers (100%)
- **Final: n=40  W=40/L=0  WR=100.0%**
- **Dir: LONG**  •  upper third; zscore +1 to +2 overbought; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

### W16.  `H60=H60a AND T4=T4a AND BBP=BBP4 AND session_bucket=ny_mid`
- Raw: n=182  W=155/L=27  WR=85.2%
- Refine: exclude H20=H20a drops 27/27 losers (100%)
- **Final: n=42  W=42/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; upper third; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

### W17.  `T1=T1a AND T4=T4a AND BBP=BBP4 AND session_bucket=ny_mid`
- Raw: n=182  W=155/L=27  WR=85.2%
- Refine: exclude H20=H20a drops 27/27 losers (100%)
- **Final: n=42  W=42/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; upper third; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

### W18.  `T4=T4a AND BBP=BBP4 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=182  W=155/L=27  WR=85.2%
- Refine: exclude H20=H20a drops 27/27 losers (100%)
- **Final: n=42  W=42/L=0  WR=100.0%**
- **Dir: LONG**  •  4h trend WITH trade; upper third; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

### W19.  `H60=H60a AND T4=T4a AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=173  W=151/L=22  WR=87.3%
- Refine: exclude H20=H20a drops 22/22 losers (100%)
- **Final: n=40  W=40/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; zscore +1 to +2 overbought; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

### W20.  `T1=T1a AND T4=T4a AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=173  W=151/L=22  WR=87.3%
- Refine: exclude H20=H20a drops 22/22 losers (100%)
- **Final: n=40  W=40/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; zscore +1 to +2 overbought; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

### W21.  `T4=T4a AND ZS=ZS4 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=173  W=151/L=22  WR=87.3%
- Refine: exclude H20=H20a drops 22/22 losers (100%)
- **Final: n=40  W=40/L=0  WR=100.0%**
- **Dir: LONG**  •  4h trend WITH trade; zscore +1 to +2 overbought; session=ny_mid  •  AVOID when HTF20 aligned WITH trade

### W22.  `H20=H20a AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=155  W=133/L=22  WR=85.8%
- Refine: exclude RSI=RSI6 drops 12/22 losers (55%)
- **Final: n=105  W=95/L=10  WR=90.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; zscore +1 to +2 overbought; session=ny_mid  •  AVOID when RSI 70-80 overbought

### W23.  `H20=H20a AND H60=H60a AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=155  W=133/L=22  WR=85.8%
- Refine: exclude RSI=RSI6 drops 12/22 losers (55%)
- **Final: n=105  W=95/L=10  WR=90.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; zscore +1 to +2 overbought; session=ny_mid  •  AVOID when RSI 70-80 overbought

### W24.  `H20=H20a AND T1=T1a AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=155  W=133/L=22  WR=85.8%
- Refine: exclude RSI=RSI6 drops 12/22 losers (55%)
- **Final: n=105  W=95/L=10  WR=90.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; zscore +1 to +2 overbought; session=ny_mid  •  AVOID when RSI 70-80 overbought

### W25.  `H20=H20a AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=155  W=133/L=22  WR=85.8%
- Refine: exclude RSI=RSI6 drops 12/22 losers (55%)
- **Final: n=105  W=95/L=10  WR=90.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; upper third; zscore +1 to +2 overbought; session=ny_mid  •  AVOID when RSI 70-80 overbought

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND BBP=BBP4 AND session_bucket=ny_mid`
- Raw: n=157  W=61/L=96  WR=38.9%
- Sharpen: sharpest is H20=H20d (22/96 of losers there)
- **Sharp: n=23  W=1/L=22  WR=4.3%**
- **Dir: ?**  •  HTF60 strongly against; upper third; session=ny_mid  •  ONLY when HTF20 mildly against

### L02.  `T1=T1c AND BBP=BBP4 AND session_bucket=ny_mid`
- Raw: n=157  W=61/L=96  WR=38.9%
- Sharpen: sharpest is H20=H20d (22/96 of losers there)
- **Sharp: n=23  W=1/L=22  WR=4.3%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; session=ny_mid  •  ONLY when HTF20 mildly against

### L03.  `BBP=BBP4 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=157  W=61/L=96  WR=38.9%
- Sharpen: sharpest is H20=H20d (22/96 of losers there)
- **Sharp: n=23  W=1/L=22  WR=4.3%**
- **Dir: SHORT**  •  upper third; session=ny_mid  •  ONLY when HTF20 mildly against

### L04.  `H60=H60e AND T1=T1c AND BBP=BBP4 AND session_bucket=ny_mid`
- Raw: n=157  W=61/L=96  WR=38.9%
- Sharpen: sharpest is H20=H20d (22/96 of losers there)
- **Sharp: n=23  W=1/L=22  WR=4.3%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; upper third; session=ny_mid  •  ONLY when HTF20 mildly against

### L05.  `H60=H60e AND BBP=BBP4 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=157  W=61/L=96  WR=38.9%
- Sharpen: sharpest is H20=H20d (22/96 of losers there)
- **Sharp: n=23  W=1/L=22  WR=4.3%**
- **Dir: SHORT**  •  HTF60 strongly against; upper third; session=ny_mid  •  ONLY when HTF20 mildly against

### L06.  `T1=T1c AND BBP=BBP4 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=157  W=61/L=96  WR=38.9%
- Sharpen: sharpest is H20=H20d (22/96 of losers there)
- **Sharp: n=23  W=1/L=22  WR=4.3%**
- **Dir: SHORT**  •  1h trend AGAINST trade; upper third; session=ny_mid  •  ONLY when HTF20 mildly against

### L07.  `H60=H60e AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=148  W=55/L=93  WR=37.2%
- Sharpen: sharpest is H20=H20d (21/93 of losers there)
- **Sharp: n=22  W=1/L=21  WR=4.5%**
- **Dir: ?**  •  HTF60 strongly against; zscore +1 to +2 overbought; session=ny_mid  •  ONLY when HTF20 mildly against

### L08.  `T1=T1c AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=148  W=55/L=93  WR=37.2%
- Sharpen: sharpest is H20=H20d (21/93 of losers there)
- **Sharp: n=22  W=1/L=21  WR=4.5%**
- **Dir: ?**  •  1h trend AGAINST trade; zscore +1 to +2 overbought; session=ny_mid  •  ONLY when HTF20 mildly against

### L09.  `ZS=ZS4 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=148  W=55/L=93  WR=37.2%
- Sharpen: sharpest is H20=H20d (21/93 of losers there)
- **Sharp: n=22  W=1/L=21  WR=4.5%**
- **Dir: SHORT**  •  zscore +1 to +2 overbought; session=ny_mid  •  ONLY when HTF20 mildly against

### L10.  `H60=H60e AND T1=T1c AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=148  W=55/L=93  WR=37.2%
- Sharpen: sharpest is H20=H20d (21/93 of losers there)
- **Sharp: n=22  W=1/L=21  WR=4.5%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; zscore +1 to +2 overbought; session=ny_mid  •  ONLY when HTF20 mildly against

### L11.  `H60=H60e AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=148  W=55/L=93  WR=37.2%
- Sharpen: sharpest is H20=H20d (21/93 of losers there)
- **Sharp: n=22  W=1/L=21  WR=4.5%**
- **Dir: ?**  •  HTF60 strongly against; upper third; zscore +1 to +2 overbought; session=ny_mid  •  ONLY when HTF20 mildly against

### L12.  `H60=H60e AND ZS=ZS4 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=148  W=55/L=93  WR=37.2%
- Sharpen: sharpest is H20=H20d (21/93 of losers there)
- **Sharp: n=22  W=1/L=21  WR=4.5%**
- **Dir: SHORT**  •  HTF60 strongly against; zscore +1 to +2 overbought; session=ny_mid  •  ONLY when HTF20 mildly against

### L13.  `T1=T1c AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=148  W=55/L=93  WR=37.2%
- Sharpen: sharpest is H20=H20d (21/93 of losers there)
- **Sharp: n=22  W=1/L=21  WR=4.5%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; zscore +1 to +2 overbought; session=ny_mid  •  ONLY when HTF20 mildly against

### L14.  `T1=T1c AND ZS=ZS4 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=148  W=55/L=93  WR=37.2%
- Sharpen: sharpest is H20=H20d (21/93 of losers there)
- **Sharp: n=22  W=1/L=21  WR=4.5%**
- **Dir: SHORT**  •  1h trend AGAINST trade; zscore +1 to +2 overbought; session=ny_mid  •  ONLY when HTF20 mildly against

### L15.  `BBP=BBP4 AND ZS=ZS4 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=148  W=55/L=93  WR=37.2%
- Sharpen: sharpest is H20=H20d (21/93 of losers there)
- **Sharp: n=22  W=1/L=21  WR=4.5%**
- **Dir: SHORT**  •  upper third; zscore +1 to +2 overbought; session=ny_mid  •  ONLY when HTF20 mildly against

### L16.  `H20=H20e AND RSI=RSI6 AND session_bucket=asia`
- Raw: n=147  W=55/L=92  WR=37.4%
- Sharpen: sharpest is BBP=BBP4 (51/92 of losers there)
- **Sharp: n=69  W=18/L=51  WR=26.1%**
- **Dir: ?**  •  HTF20 strongly against; RSI 70-80 overbought; session=asia  •  ONLY when upper third

### L17.  `H20=H20e AND T1=T1c AND RSI=RSI6 AND session_bucket=asia`
- Raw: n=147  W=55/L=92  WR=37.4%
- Sharpen: sharpest is BBP=BBP4 (51/92 of losers there)
- **Sharp: n=69  W=18/L=51  WR=26.1%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 70-80 overbought; session=asia  •  ONLY when upper third

### L18.  `H20=H20e AND T4=T4c AND RSI=RSI6 AND session_bucket=asia`
- Raw: n=147  W=55/L=92  WR=37.4%
- Sharpen: sharpest is BBP=BBP4 (51/92 of losers there)
- **Sharp: n=69  W=18/L=51  WR=26.1%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 70-80 overbought; session=asia  •  ONLY when upper third

### L19.  `H20=H20e AND RSI=RSI6 AND direction_exec=short AND session_bucket=asia`
- Raw: n=147  W=55/L=92  WR=37.4%
- Sharpen: sharpest is BBP=BBP4 (51/92 of losers there)
- **Sharp: n=69  W=18/L=51  WR=26.1%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 70-80 overbought; session=asia  •  ONLY when upper third

### L20.  `H60=H60e AND T4=T4c AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=138  W=54/L=84  WR=39.1%
- Sharpen: sharpest is H20=H20d (21/84 of losers there)
- **Sharp: n=22  W=1/L=21  WR=4.5%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; zscore +1 to +2 overbought; session=ny_mid  •  ONLY when HTF20 mildly against

### L21.  `T1=T1c AND T4=T4c AND ZS=ZS4 AND session_bucket=ny_mid`
- Raw: n=138  W=54/L=84  WR=39.1%
- Sharpen: sharpest is H20=H20d (21/84 of losers there)
- **Sharp: n=22  W=1/L=21  WR=4.5%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore +1 to +2 overbought; session=ny_mid  •  ONLY when HTF20 mildly against

### L22.  `T4=T4c AND ZS=ZS4 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=138  W=54/L=84  WR=39.1%
- Sharpen: sharpest is H20=H20d (21/84 of losers there)
- **Sharp: n=22  W=1/L=21  WR=4.5%**
- **Dir: SHORT**  •  4h trend AGAINST trade; zscore +1 to +2 overbought; session=ny_mid  •  ONLY when HTF20 mildly against

### L23.  `H20=H20e AND H60=H60e AND RSI=RSI6 AND session_bucket=asia`
- Raw: n=119  W=45/L=74  WR=37.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=119  W=45/L=74  WR=37.8%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 70-80 overbought; session=asia

### L24.  `H60=H60e AND BBP=BBP4 AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=83  W=32/L=51  WR=38.6%
- Sharpen: sharpest is H20=H20d (22/51 of losers there)
- **Sharp: n=23  W=1/L=22  WR=4.3%**
- **Dir: ?**  •  HTF60 strongly against; upper third; RSI 70-80 overbought; session=ny_mid  •  ONLY when HTF20 mildly against

### L25.  `T1=T1c AND BBP=BBP4 AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=83  W=32/L=51  WR=38.6%
- Sharpen: sharpest is H20=H20d (22/51 of losers there)
- **Sharp: n=23  W=1/L=22  WR=4.3%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; RSI 70-80 overbought; session=ny_mid  •  ONLY when HTF20 mildly against

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | H60a(50/43) | H60e(44/50) |
| T1 | T1a(53/45) | T1c(47/55) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(52/47) | short(48/53) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
