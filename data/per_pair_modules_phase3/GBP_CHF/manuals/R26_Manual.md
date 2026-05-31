# GBP_CHF — R26 Manual

## Regime centroid (locked factors)

- **BB = BB2**  (normal bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **1,491**  (W=929 / L=562)  -  WR: **62.3%**

## Session distribution

- london_open: n=501  W=308/L=193  WR=61.5%
- ny_open: n=299  W=186/L=113  WR=62.2%
- ny_mid: n=258  W=175/L=83  WR=67.8%
- london: n=151  W=90/L=61  WR=59.6%
- asia: n=146  W=87/L=59  WR=59.6%
- ny_close: n=103  W=66/L=37  WR=64.1%
- off_hours: n=23  W=11/L=12  WR=47.8%
- asia_late: n=10  W=6/L=4  WR=60.0%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20e AND direction_exec=short AND session_bucket=asia`
- Raw: n=52  W=46/L=6  WR=88.5%
- Refine: exclude RSI=RSI5 drops 6/6 losers (100%)
- **Final: n=20  W=20/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 strongly against; session=asia  •  AVOID when RSI 60-70 strong

### W02.  `H20=H20e AND H60=H60a AND T1=T1c AND session_bucket=asia`
- Raw: n=52  W=46/L=6  WR=88.5%
- Refine: exclude RSI=RSI5 drops 6/6 losers (100%)
- **Final: n=20  W=20/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend AGAINST trade; session=asia  •  AVOID when RSI 60-70 strong

### W03.  `H20=H20e AND H60=H60a AND direction_exec=short AND session_bucket=asia`
- Raw: n=52  W=46/L=6  WR=88.5%
- Refine: exclude RSI=RSI5 drops 6/6 losers (100%)
- **Final: n=20  W=20/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 aligned WITH trade; session=asia  •  AVOID when RSI 60-70 strong

### W04.  `H20=H20e AND T1=T1c AND direction_exec=short AND session_bucket=asia`
- Raw: n=52  W=46/L=6  WR=88.5%
- Refine: exclude RSI=RSI5 drops 6/6 losers (100%)
- **Final: n=20  W=20/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; session=asia  •  AVOID when RSI 60-70 strong

### W05.  `BBP=BBP4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=49  W=42/L=7  WR=85.7%
- Refine: exclude T4=T4c drops 5/7 losers (71%)
- **Final: n=32  W=30/L=2  WR=93.8%**
- **Dir: SHORT**  •  upper third; session=asia  •  AVOID when 4h trend AGAINST trade

### W06.  `H60=H60e AND T4=T4c AND direction_exec=long AND session_bucket=london_open`
- Raw: n=48  W=42/L=6  WR=87.5%
- Refine: exclude RSI=RSI5 drops 6/6 losers (100%)
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend AGAINST trade; session=london_open  •  AVOID when RSI 60-70 strong

### W07.  `H60=H60a AND BBP=BBP4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=47  W=40/L=7  WR=85.1%
- Refine: exclude T4=T4c drops 5/7 losers (71%)
- **Final: n=32  W=30/L=2  WR=93.8%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; upper third; session=asia  •  AVOID when 4h trend AGAINST trade

### W08.  `H20=H20d AND T1=T1a AND RSI=RSI4`
- Raw: n=46  W=43/L=3  WR=93.5%
- Refine: exclude BBP=BBP3 drops 2/3 losers (67%)
- **Final: n=38  W=37/L=1  WR=97.4%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when middle of band

### W09.  `H20=H20d AND RSI=RSI4 AND direction_exec=long`
- Raw: n=46  W=43/L=3  WR=93.5%
- Refine: exclude BBP=BBP3 drops 2/3 losers (67%)
- **Final: n=38  W=37/L=1  WR=97.4%**
- **Dir: LONG**  •  HTF20 mildly against; RSI 50-60 upper neutral  •  AVOID when middle of band

### W10.  `H20=H20d AND T1=T1a AND RSI=RSI4 AND direction_exec=long`
- Raw: n=46  W=43/L=3  WR=93.5%
- Refine: exclude BBP=BBP3 drops 2/3 losers (67%)
- **Final: n=38  W=37/L=1  WR=97.4%**
- **Dir: LONG**  •  HTF20 mildly against; 1h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when middle of band

### W11.  `H60=H60d AND T4=T4c AND BBP=BBP4`
- Raw: n=43  W=38/L=5  WR=88.4%
- Refine: exclude H20=H20d drops 2/5 losers (40%)
- **Final: n=41  W=38/L=3  WR=92.7%**
- **Dir: ?**  •  HTF60 mildly against; 4h trend AGAINST trade; upper third  •  AVOID when HTF20 mildly against

### W12.  `H20=H20b AND T1=T1a AND RSI=RSI5`
- Raw: n=42  W=40/L=2  WR=95.2%
- Refine: exclude H60=H60b drops 2/2 losers (100%)
- **Final: n=22  W=22/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when HTF60 slightly aligned

### W13.  `H20=H20b AND RSI=RSI5 AND direction_exec=long`
- Raw: n=42  W=40/L=2  WR=95.2%
- Refine: exclude H60=H60b drops 2/2 losers (100%)
- **Final: n=22  W=22/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 slightly aligned; RSI 60-70 strong  •  AVOID when HTF60 slightly aligned

### W14.  `H20=H20b AND T1=T1a AND RSI=RSI5 AND direction_exec=long`
- Raw: n=42  W=40/L=2  WR=95.2%
- Refine: exclude H60=H60b drops 2/2 losers (100%)
- **Final: n=22  W=22/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 slightly aligned; 1h trend WITH trade; RSI 60-70 strong  •  AVOID when HTF60 slightly aligned

### W15.  `H60=H60d AND T4=T4c AND ZS=ZS4`
- Raw: n=42  W=38/L=4  WR=90.5%
- Refine: exclude session_bucket=ny_open drops 4/4 losers (100%)
- **Final: n=21  W=21/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 mildly against; 4h trend AGAINST trade; zscore +1 to +2 overbought  •  AVOID when session=ny_open

### W16.  `ZS=ZS4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=42  W=38/L=4  WR=90.5%
- Refine: exclude H20=H20c drops 2/4 losers (50%)
- **Final: n=40  W=38/L=2  WR=95.0%**
- **Dir: SHORT**  •  zscore +1 to +2 overbought; session=asia  •  AVOID when HTF20 neutral

### W17.  `H60=H60d AND T4=T4c AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=42  W=38/L=4  WR=90.5%
- Refine: exclude session_bucket=ny_open drops 4/4 losers (100%)
- **Final: n=21  W=21/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 mildly against; 4h trend AGAINST trade; upper third; zscore +1 to +2 overbought  •  AVOID when session=ny_open

### W18.  `BBP=BBP4 AND ZS=ZS4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=42  W=38/L=4  WR=90.5%
- Refine: exclude H20=H20c drops 2/4 losers (50%)
- **Final: n=40  W=38/L=2  WR=95.0%**
- **Dir: SHORT**  •  upper third; zscore +1 to +2 overbought; session=asia  •  AVOID when HTF20 neutral

### W19.  `H60=H60e AND T4=T4c AND RSI=RSI4 AND session_bucket=london_open`
- Raw: n=42  W=36/L=6  WR=85.7%
- Refine: exclude H20=H20b drops 6/6 losers (100%)
- **Final: n=34  W=34/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 50-60 upper neutral; session=london_open  •  AVOID when HTF20 slightly aligned

### W20.  `RSI=RSI4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=41  W=37/L=4  WR=90.2%
- Refine: exclude H20=H20c drops 3/4 losers (75%)
- **Final: n=38  W=37/L=1  WR=97.4%**
- **Dir: SHORT**  •  RSI 50-60 upper neutral; session=asia  •  AVOID when HTF20 neutral

### W21.  `H20=H20e AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=41  W=36/L=5  WR=87.8%
- Refine: exclude H60=H60d drops 4/5 losers (80%)
- **Final: n=30  W=29/L=1  WR=96.7%**
- **Dir: LONG**  •  HTF20 strongly against; session=ny_mid  •  AVOID when HTF60 mildly against

### W22.  `H20=H20e AND T1=T1a AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=41  W=36/L=5  WR=87.8%
- Refine: exclude H60=H60d drops 4/5 losers (80%)
- **Final: n=30  W=29/L=1  WR=96.7%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend WITH trade; session=ny_mid  •  AVOID when HTF60 mildly against

### W23.  `H20=H20e AND T4=T4a AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=41  W=36/L=5  WR=87.8%
- Refine: exclude H60=H60d drops 4/5 losers (80%)
- **Final: n=30  W=29/L=1  WR=96.7%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend WITH trade; session=ny_mid  •  AVOID when HTF60 mildly against

### W24.  `T1=T1a AND T4=T4c AND RSI=RSI4 AND session_bucket=london_open`
- Raw: n=41  W=36/L=5  WR=87.8%
- Refine: exclude H60=H60c drops 2/5 losers (40%)
- **Final: n=38  W=35/L=3  WR=92.1%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral; session=london_open  •  AVOID when HTF60 neutral

### W25.  `H20=H20c AND H60=H60a AND session_bucket=ny_mid`
- Raw: n=40  W=36/L=4  WR=90.0%
- Refine: exclude RSI=RSI5 drops 3/4 losers (75%)
- **Final: n=25  W=24/L=1  WR=96.0%**
- **Dir: ?**  •  HTF20 neutral; HTF60 aligned WITH trade; session=ny_mid  •  AVOID when RSI 60-70 strong

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T4=T4a AND RSI=RSI5 AND session_bucket=london_open`
- Raw: n=105  W=42/L=63  WR=40.0%
- Sharpen: sharpest is H20=H20d (19/63 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: ?**  •  4h trend WITH trade; RSI 60-70 strong; session=london_open  •  ONLY when HTF20 mildly against

### L02.  `T4=T4a AND direction_exec=short AND session_bucket=london_open`
- Raw: n=81  W=31/L=50  WR=38.3%
- Sharpen: sharpest is H60=H60a (21/50 of losers there)
- **Sharp: n=26  W=5/L=21  WR=19.2%**
- **Dir: SHORT**  •  4h trend WITH trade; session=london_open  •  ONLY when HTF60 aligned WITH trade

### L03.  `T4=T4a AND ZS=ZS4 AND session_bucket=london_open`
- Raw: n=74  W=27/L=47  WR=36.5%
- Sharpen: sharpest is RSI=RSI5 (24/47 of losers there)
- **Sharp: n=29  W=5/L=24  WR=17.2%**
- **Dir: ?**  •  4h trend WITH trade; zscore +1 to +2 overbought; session=london_open  •  ONLY when RSI 60-70 strong

### L04.  `T4=T4a AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=london_open`
- Raw: n=74  W=27/L=47  WR=36.5%
- Sharpen: sharpest is RSI=RSI5 (24/47 of losers there)
- **Sharp: n=29  W=5/L=24  WR=17.2%**
- **Dir: ?**  •  4h trend WITH trade; upper third; zscore +1 to +2 overbought; session=london_open  •  ONLY when RSI 60-70 strong

### L05.  `H20=H20c AND H60=H60e AND session_bucket=london_open`
- Raw: n=72  W=27/L=45  WR=37.5%
- Sharpen: sharpest is direction_exec=long (28/45 of losers there)
- **Sharp: n=38  W=10/L=28  WR=26.3%**
- **Dir: ?**  •  HTF20 neutral; HTF60 strongly against; session=london_open  •  ONLY when long

### L06.  `H20=H20c AND H60=H60e AND T4=T4a AND session_bucket=london_open`
- Raw: n=64  W=25/L=39  WR=39.1%
- Sharpen: sharpest is direction_exec=long (28/39 of losers there)
- **Sharp: n=38  W=10/L=28  WR=26.3%**
- **Dir: ?**  •  HTF20 neutral; HTF60 strongly against; 4h trend WITH trade; session=london_open  •  ONLY when long

### L07.  `H60=H60e AND T4=T4c AND RSI=RSI5`
- Raw: n=62  W=22/L=40  WR=35.5%
- Sharpen: sharpest is H20=H20c (13/40 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when HTF20 neutral

### L08.  `H60=H60e AND direction_exec=long AND session_bucket=asia`
- Raw: n=62  W=22/L=40  WR=35.5%
- Sharpen: sharpest is T4=T4c (23/40 of losers there)
- **Sharp: n=29  W=6/L=23  WR=20.7%**
- **Dir: LONG**  •  HTF60 strongly against; session=asia  •  ONLY when 4h trend AGAINST trade

### L09.  `T1=T1c AND T4=T4a AND session_bucket=london_open`
- Raw: n=61  W=18/L=43  WR=29.5%
- Sharpen: sharpest is H20=H20d (12/43 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; session=london_open  •  ONLY when HTF20 mildly against

### L10.  `T1=T1a AND direction_exec=long AND session_bucket=asia`
- Raw: n=60  W=21/L=39  WR=35.0%
- Sharpen: sharpest is T4=T4c (18/39 of losers there)
- **Sharp: n=23  W=5/L=18  WR=21.7%**
- **Dir: LONG**  •  1h trend WITH trade; session=asia  •  ONLY when 4h trend AGAINST trade

### L11.  `H20=H20e AND H60=H60a AND T4=T4c AND RSI=RSI5`
- Raw: n=58  W=21/L=37  WR=36.2%
- Sharpen: sharpest is BBP=BBP4 (20/37 of losers there)
- **Sharp: n=28  W=8/L=20  WR=28.6%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when upper third

### L12.  `H60=H60e AND T4=T4c AND direction_exec=short`
- Raw: n=55  W=19/L=36  WR=34.5%
- Sharpen: sharpest is H20=H20c (20/36 of losers there)
- **Sharp: n=22  W=2/L=20  WR=9.1%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend AGAINST trade  •  ONLY when HTF20 neutral

### L13.  `T4=T4a AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=54  W=21/L=33  WR=38.9%
- Sharpen: sharpest is H20=H20b (13/33 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: ?**  •  4h trend WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when HTF20 slightly aligned

### L14.  `H60=H60e AND T1=T1a AND session_bucket=asia`
- Raw: n=53  W=21/L=32  WR=39.6%
- Sharpen: sharpest is H20=H20a (28/32 of losers there)
- **Sharp: n=41  W=13/L=28  WR=31.7%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; session=asia  •  ONLY when HTF20 aligned WITH trade

### L15.  `H60=H60e AND T1=T1a AND direction_exec=long AND session_bucket=asia`
- Raw: n=53  W=21/L=32  WR=39.6%
- Sharpen: sharpest is H20=H20a (28/32 of losers there)
- **Sharp: n=41  W=13/L=28  WR=31.7%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend WITH trade; session=asia  •  ONLY when HTF20 aligned WITH trade

### L16.  `H20=H20c AND H60=H60e AND RSI=RSI5`
- Raw: n=52  W=17/L=35  WR=32.7%
- Sharpen: sharpest is T1=T1c (13/35 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: ?**  •  HTF20 neutral; HTF60 strongly against; RSI 60-70 strong  •  ONLY when 1h trend AGAINST trade

### L17.  `T1=T1c AND T4=T4a AND direction_exec=short AND session_bucket=london_open`
- Raw: n=52  W=18/L=34  WR=34.6%
- Sharpen: sharpest is H20=H20d (12/34 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend WITH trade; session=london_open  •  ONLY when HTF20 mildly against

### L18.  `T4=T4a AND RSI=RSI4 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=52  W=19/L=33  WR=36.5%
- Sharpen: sharpest is H60=H60a (18/33 of losers there)
- **Sharp: n=20  W=2/L=18  WR=10.0%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 50-60 upper neutral; session=london_open  •  ONLY when HTF60 aligned WITH trade

### L19.  `H60=H60e AND T1=T1c AND T4=T4c AND direction_exec=short`
- Raw: n=51  W=17/L=34  WR=33.3%
- Sharpen: sharpest is session_bucket=ny_mid (15/34 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when session=ny_mid

### L20.  `H20=H20c AND T4=T4a AND direction_exec=long AND session_bucket=london_open`
- Raw: n=51  W=19/L=32  WR=37.3%
- Sharpen: sharpest is H60=H60e (28/32 of losers there)
- **Sharp: n=38  W=10/L=28  WR=26.3%**
- **Dir: LONG**  •  HTF20 neutral; 4h trend WITH trade; session=london_open  •  ONLY when HTF60 strongly against

### L21.  `H20=H20c AND H60=H60e AND direction_exec=short`
- Raw: n=48  W=17/L=31  WR=35.4%
- Sharpen: sharpest is T4=T4c (20/31 of losers there)
- **Sharp: n=22  W=2/L=20  WR=9.1%**
- **Dir: SHORT**  •  HTF20 neutral; HTF60 strongly against  •  ONLY when 4h trend AGAINST trade

### L22.  `T1=T1c AND ZS=ZS5 AND session_bucket=ny_open`
- Raw: n=48  W=18/L=30  WR=37.5%
- Sharpen: sharpest is T4=T4a (16/30 of losers there)
- **Sharp: n=16  W=0/L=16  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; zscore +2 to +3 deep overbought; session=ny_open  •  ONLY when 4h trend WITH trade

### L23.  `H20=H20c AND T1=T1a AND ZS=ZS5`
- Raw: n=45  W=16/L=29  WR=35.6%
- Sharpen: sharpest is BBP=BBP6 (10/29 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: ?**  •  HTF20 neutral; 1h trend WITH trade; zscore +2 to +3 deep overbought  •  ONLY when deep above upper band

### L24.  `T1=T1c AND ZS=ZS5 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=45  W=18/L=27  WR=40.0%
- Sharpen: sharpest is T4=T4a (13/27 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; zscore +2 to +3 deep overbought; session=ny_open  •  ONLY when 4h trend WITH trade

### L25.  `H20=H20c AND T4=T4a AND ZS=ZS5`
- Raw: n=44  W=15/L=29  WR=34.1%
- Sharpen: sharpest is BBP=BBP6 (10/29 of losers there)
- **Sharp: n=10  W=0/L=10  WR=0.0%**
- **Dir: ?**  •  HTF20 neutral; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  ONLY when deep above upper band

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | — |
| T1 | — | — |
| T4 | T4c(51/46) | T4a(49/54) |
| BBP | — | — |
| RSI | — | RSI5(43/48) |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
