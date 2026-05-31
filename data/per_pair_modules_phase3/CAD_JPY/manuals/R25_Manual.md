# CAD_JPY — R25 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50a**  (EMA50 up >0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **2,919**  (W=1,822 / L=1,097)  -  WR: **62.4%**

## Session distribution

- asia: n=806  W=500/L=306  WR=62.0%
- ny_open: n=517  W=306/L=211  WR=59.2%
- ny_close: n=462  W=292/L=170  WR=63.2%
- london_open: n=371  W=231/L=140  WR=62.3%
- ny_mid: n=300  W=200/L=100  WR=66.7%
- london: n=229  W=147/L=82  WR=64.2%
- off_hours: n=138  W=82/L=56  WR=59.4%
- asia_late: n=96  W=64/L=32  WR=66.7%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND H60=H60e AND T4=T4c AND RSI=RSI5`
- Raw: n=113  W=98/L=15  WR=86.7%
- Refine: exclude session_bucket=asia_late drops 6/15 losers (40%)
- **Final: n=93  W=84/L=9  WR=90.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when session=asia_late

### W02.  `H20=H20a AND T1=T1c AND T4=T4c AND RSI=RSI5`
- Raw: n=113  W=98/L=15  WR=86.7%
- Refine: exclude session_bucket=asia_late drops 6/15 losers (40%)
- **Final: n=93  W=84/L=9  WR=90.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when session=asia_late

### W03.  `H20=H20a AND T4=T4c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=113  W=98/L=15  WR=86.7%
- Refine: exclude session_bucket=asia_late drops 6/15 losers (40%)
- **Final: n=93  W=84/L=9  WR=90.3%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 60-70 strong  •  AVOID when session=asia_late

### W04.  `T4=T4c AND BBP=BBP5 AND RSI=RSI5`
- Raw: n=77  W=66/L=11  WR=85.7%
- Refine: exclude session_bucket=ny_open drops 10/11 losers (91%)
- **Final: n=35  W=34/L=1  WR=97.1%**
- **Dir: ?**  •  4h trend AGAINST trade; just touched upper band; RSI 60-70 strong  •  AVOID when session=ny_open

### W05.  `T4=T4c AND BBP=BBP5 AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=77  W=66/L=11  WR=85.7%
- Refine: exclude session_bucket=ny_open drops 10/11 losers (91%)
- **Final: n=35  W=34/L=1  WR=97.1%**
- **Dir: ?**  •  4h trend AGAINST trade; just touched upper band; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when session=ny_open

### W06.  `H20=H20e AND BBP=BBP3 AND RSI=RSI6`
- Raw: n=65  W=56/L=9  WR=86.2%
- Refine: exclude session_bucket=off_hours drops 2/9 losers (22%)
- **Final: n=60  W=53/L=7  WR=88.3%**
- **Dir: ?**  •  HTF20 strongly against; middle of band; RSI 70-80 overbought  •  AVOID when session=off_hours

### W07.  `H20=H20e AND BBP=BBP3 AND RSI=RSI6 AND ZS=ZS3`
- Raw: n=65  W=56/L=9  WR=86.2%
- Refine: exclude session_bucket=off_hours drops 2/9 losers (22%)
- **Final: n=60  W=53/L=7  WR=88.3%**
- **Dir: ?**  •  HTF20 strongly against; middle of band; RSI 70-80 overbought; zscore -1 to +1 neutral  •  AVOID when session=off_hours

### W08.  `H60=H60e AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=64  W=61/L=3  WR=95.3%
- Refine: exclude BBP=BBP2 drops 2/3 losers (67%)
- **Final: n=52  W=51/L=1  WR=98.1%**
- **Dir: ?**  •  HTF60 strongly against; RSI 60-70 strong; session=ny_mid  •  AVOID when lower third

### W09.  `T1=T1c AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=64  W=61/L=3  WR=95.3%
- Refine: exclude BBP=BBP2 drops 2/3 losers (67%)
- **Final: n=52  W=51/L=1  WR=98.1%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 60-70 strong; session=ny_mid  •  AVOID when lower third

### W10.  `T4=T4c AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=64  W=61/L=3  WR=95.3%
- Refine: exclude BBP=BBP2 drops 2/3 losers (67%)
- **Final: n=52  W=51/L=1  WR=98.1%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 60-70 strong; session=ny_mid  •  AVOID when lower third

### W11.  `RSI=RSI5 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=64  W=61/L=3  WR=95.3%
- Refine: exclude BBP=BBP2 drops 2/3 losers (67%)
- **Final: n=52  W=51/L=1  WR=98.1%**
- **Dir: SHORT**  •  RSI 60-70 strong; session=ny_mid  •  AVOID when lower third

### W12.  `H60=H60e AND T1=T1c AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=64  W=61/L=3  WR=95.3%
- Refine: exclude BBP=BBP2 drops 2/3 losers (67%)
- **Final: n=52  W=51/L=1  WR=98.1%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 60-70 strong; session=ny_mid  •  AVOID when lower third

### W13.  `H60=H60e AND T4=T4c AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=64  W=61/L=3  WR=95.3%
- Refine: exclude BBP=BBP2 drops 2/3 losers (67%)
- **Final: n=52  W=51/L=1  WR=98.1%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 60-70 strong; session=ny_mid  •  AVOID when lower third

### W14.  `H60=H60e AND RSI=RSI5 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=64  W=61/L=3  WR=95.3%
- Refine: exclude BBP=BBP2 drops 2/3 losers (67%)
- **Final: n=52  W=51/L=1  WR=98.1%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 60-70 strong; session=ny_mid  •  AVOID when lower third

### W15.  `T1=T1c AND T4=T4c AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=64  W=61/L=3  WR=95.3%
- Refine: exclude BBP=BBP2 drops 2/3 losers (67%)
- **Final: n=52  W=51/L=1  WR=98.1%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 60-70 strong; session=ny_mid  •  AVOID when lower third

### W16.  `T1=T1c AND RSI=RSI5 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=64  W=61/L=3  WR=95.3%
- Refine: exclude BBP=BBP2 drops 2/3 losers (67%)
- **Final: n=52  W=51/L=1  WR=98.1%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 60-70 strong; session=ny_mid  •  AVOID when lower third

### W17.  `T4=T4c AND RSI=RSI5 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=64  W=61/L=3  WR=95.3%
- Refine: exclude BBP=BBP2 drops 2/3 losers (67%)
- **Final: n=52  W=51/L=1  WR=98.1%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 60-70 strong; session=ny_mid  •  AVOID when lower third

### W18.  `H20=H20e AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=63  W=55/L=8  WR=87.3%
- Refine: exclude H60=H60a drops 5/8 losers (62%)
- **Final: n=58  W=55/L=3  WR=94.8%**
- **Dir: ?**  •  HTF20 strongly against; RSI 60-70 strong; session=ny_mid  •  AVOID when HTF60 aligned WITH trade

### W19.  `H20=H20e AND H60=H60e AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=58  W=55/L=3  WR=94.8%
- Refine: exclude BBP=BBP2 drops 2/3 losers (67%)
- **Final: n=50  W=49/L=1  WR=98.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 60-70 strong; session=ny_mid  •  AVOID when lower third

### W20.  `H20=H20e AND T1=T1c AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=58  W=55/L=3  WR=94.8%
- Refine: exclude BBP=BBP2 drops 2/3 losers (67%)
- **Final: n=50  W=49/L=1  WR=98.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 60-70 strong; session=ny_mid  •  AVOID when lower third

### W21.  `H20=H20e AND T4=T4c AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=58  W=55/L=3  WR=94.8%
- Refine: exclude BBP=BBP2 drops 2/3 losers (67%)
- **Final: n=50  W=49/L=1  WR=98.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 60-70 strong; session=ny_mid  •  AVOID when lower third

### W22.  `H20=H20e AND RSI=RSI5 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=58  W=55/L=3  WR=94.8%
- Refine: exclude BBP=BBP2 drops 2/3 losers (67%)
- **Final: n=50  W=49/L=1  WR=98.0%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 60-70 strong; session=ny_mid  •  AVOID when lower third

### W23.  `H20=H20b AND H60=H60e AND T1=T1c`
- Raw: n=56  W=50/L=6  WR=89.3%
- Refine: exclude BBP=BBP4 drops 6/6 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 strongly against; 1h trend AGAINST trade  •  AVOID when upper third

### W24.  `H20=H20b AND H60=H60e AND T4=T4c`
- Raw: n=56  W=50/L=6  WR=89.3%
- Refine: exclude BBP=BBP4 drops 6/6 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 strongly against; 4h trend AGAINST trade  •  AVOID when upper third

### W25.  `H20=H20b AND H60=H60e AND direction_exec=short`
- Raw: n=56  W=50/L=6  WR=89.3%
- Refine: exclude BBP=BBP4 drops 6/6 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 slightly aligned; HTF60 strongly against  •  AVOID when upper third

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND RSI=RSI6 AND session_bucket=asia`
- Raw: n=175  W=63/L=112  WR=36.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=175  W=63/L=112  WR=36.0%**
- **Dir: ?**  •  HTF60 strongly against; RSI 70-80 overbought; session=asia

### L02.  `T1=T1c AND RSI=RSI6 AND session_bucket=asia`
- Raw: n=175  W=63/L=112  WR=36.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=175  W=63/L=112  WR=36.0%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 70-80 overbought; session=asia

### L03.  `T4=T4c AND RSI=RSI6 AND session_bucket=asia`
- Raw: n=175  W=63/L=112  WR=36.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=175  W=63/L=112  WR=36.0%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 70-80 overbought; session=asia

### L04.  `RSI=RSI6 AND direction_exec=short AND session_bucket=asia`
- Raw: n=175  W=63/L=112  WR=36.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=175  W=63/L=112  WR=36.0%**
- **Dir: SHORT**  •  RSI 70-80 overbought; session=asia

### L05.  `H60=H60e AND T1=T1c AND RSI=RSI6 AND session_bucket=asia`
- Raw: n=175  W=63/L=112  WR=36.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=175  W=63/L=112  WR=36.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 70-80 overbought; session=asia

### L06.  `H60=H60e AND T4=T4c AND RSI=RSI6 AND session_bucket=asia`
- Raw: n=175  W=63/L=112  WR=36.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=175  W=63/L=112  WR=36.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 70-80 overbought; session=asia

### L07.  `H60=H60e AND RSI=RSI6 AND direction_exec=short AND session_bucket=asia`
- Raw: n=175  W=63/L=112  WR=36.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=175  W=63/L=112  WR=36.0%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 70-80 overbought; session=asia

### L08.  `T1=T1c AND T4=T4c AND RSI=RSI6 AND session_bucket=asia`
- Raw: n=175  W=63/L=112  WR=36.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=175  W=63/L=112  WR=36.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 70-80 overbought; session=asia

### L09.  `T1=T1c AND RSI=RSI6 AND direction_exec=short AND session_bucket=asia`
- Raw: n=175  W=63/L=112  WR=36.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=175  W=63/L=112  WR=36.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 70-80 overbought; session=asia

### L10.  `T4=T4c AND RSI=RSI6 AND direction_exec=short AND session_bucket=asia`
- Raw: n=175  W=63/L=112  WR=36.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=175  W=63/L=112  WR=36.0%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 70-80 overbought; session=asia

### L11.  `H60=H60e AND BBP=BBP4 AND RSI=RSI6 AND session_bucket=asia`
- Raw: n=126  W=41/L=85  WR=32.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=126  W=41/L=85  WR=32.5%**
- **Dir: ?**  •  HTF60 strongly against; upper third; RSI 70-80 overbought; session=asia

### L12.  `T1=T1c AND BBP=BBP4 AND RSI=RSI6 AND session_bucket=asia`
- Raw: n=126  W=41/L=85  WR=32.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=126  W=41/L=85  WR=32.5%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; RSI 70-80 overbought; session=asia

### L13.  `T4=T4c AND BBP=BBP4 AND RSI=RSI6 AND session_bucket=asia`
- Raw: n=126  W=41/L=85  WR=32.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=126  W=41/L=85  WR=32.5%**
- **Dir: ?**  •  4h trend AGAINST trade; upper third; RSI 70-80 overbought; session=asia

### L14.  `BBP=BBP4 AND RSI=RSI6 AND direction_exec=short AND session_bucket=asia`
- Raw: n=126  W=41/L=85  WR=32.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=126  W=41/L=85  WR=32.5%**
- **Dir: SHORT**  •  upper third; RSI 70-80 overbought; session=asia

### L15.  `H60=H60e AND RSI=RSI6 AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=118  W=41/L=77  WR=34.7%
- Sharpen: no sharper sub-pattern
- **Sharp: n=118  W=41/L=77  WR=34.7%**
- **Dir: ?**  •  HTF60 strongly against; RSI 70-80 overbought; zscore +1 to +2 overbought; session=asia

### L16.  `T1=T1c AND RSI=RSI6 AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=118  W=41/L=77  WR=34.7%
- Sharpen: no sharper sub-pattern
- **Sharp: n=118  W=41/L=77  WR=34.7%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 70-80 overbought; zscore +1 to +2 overbought; session=asia

### L17.  `T4=T4c AND RSI=RSI6 AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=118  W=41/L=77  WR=34.7%
- Sharpen: no sharper sub-pattern
- **Sharp: n=118  W=41/L=77  WR=34.7%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 70-80 overbought; zscore +1 to +2 overbought; session=asia

### L18.  `RSI=RSI6 AND ZS=ZS4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=118  W=41/L=77  WR=34.7%
- Sharpen: no sharper sub-pattern
- **Sharp: n=118  W=41/L=77  WR=34.7%**
- **Dir: SHORT**  •  RSI 70-80 overbought; zscore +1 to +2 overbought; session=asia

### L19.  `H20=H20e AND H60=H60e AND RSI=RSI7`
- Raw: n=111  W=36/L=75  WR=32.4%
- Sharpen: sharpest is session_bucket=ny_close (21/75 of losers there)
- **Sharp: n=23  W=2/L=21  WR=8.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI>80 extreme overbought  •  ONLY when session=ny_close

### L20.  `H20=H20e AND T1=T1c AND RSI=RSI7`
- Raw: n=111  W=36/L=75  WR=32.4%
- Sharpen: sharpest is session_bucket=ny_close (21/75 of losers there)
- **Sharp: n=23  W=2/L=21  WR=8.7%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI>80 extreme overbought  •  ONLY when session=ny_close

### L21.  `H20=H20e AND T4=T4c AND RSI=RSI7`
- Raw: n=111  W=36/L=75  WR=32.4%
- Sharpen: sharpest is session_bucket=ny_close (21/75 of losers there)
- **Sharp: n=23  W=2/L=21  WR=8.7%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI>80 extreme overbought  •  ONLY when session=ny_close

### L22.  `H20=H20e AND RSI=RSI7 AND direction_exec=short`
- Raw: n=111  W=36/L=75  WR=32.4%
- Sharpen: sharpest is session_bucket=ny_close (21/75 of losers there)
- **Sharp: n=23  W=2/L=21  WR=8.7%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI>80 extreme overbought  •  ONLY when session=ny_close

### L23.  `H20=H20e AND H60=H60e AND T1=T1c AND RSI=RSI7`
- Raw: n=111  W=36/L=75  WR=32.4%
- Sharpen: sharpest is session_bucket=ny_close (21/75 of losers there)
- **Sharp: n=23  W=2/L=21  WR=8.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; RSI>80 extreme overbought  •  ONLY when session=ny_close

### L24.  `H20=H20e AND H60=H60e AND T4=T4c AND RSI=RSI7`
- Raw: n=111  W=36/L=75  WR=32.4%
- Sharpen: sharpest is session_bucket=ny_close (21/75 of losers there)
- **Sharp: n=23  W=2/L=21  WR=8.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; RSI>80 extreme overbought  •  ONLY when session=ny_close

### L25.  `H20=H20e AND H60=H60e AND RSI=RSI7 AND direction_exec=short`
- Raw: n=111  W=36/L=75  WR=32.4%
- Sharpen: sharpest is session_bucket=ny_close (21/75 of losers there)
- **Sharp: n=23  W=2/L=21  WR=8.7%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; RSI>80 extreme overbought  •  ONLY when session=ny_close

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(52/46) | H20e(44/51) |
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
