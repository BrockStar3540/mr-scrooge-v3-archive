# NZD_JPY — R24 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50a**  (EMA50 up >0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **1,720**  (W=1,057 / L=663)  -  WR: **61.5%**

## Session distribution

- asia: n=727  W=440/L=287  WR=60.5%
- ny_mid: n=538  W=344/L=194  WR=63.9%
- london_open: n=240  W=137/L=103  WR=57.1%
- ny_open: n=105  W=67/L=38  WR=63.8%
- ny_close: n=59  W=37/L=22  WR=62.7%
- london: n=37  W=23/L=14  WR=62.2%
- off_hours: n=9  W=6/L=3  WR=66.7%
- asia_late: n=5  W=3/L=2  WR=60.0%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60a AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=84  W=72/L=12  WR=85.7%
- Refine: exclude BBP=BBP4 drops 11/12 losers (92%)
- **Final: n=41  W=40/L=1  WR=97.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 70-80 overbought; session=ny_mid  •  AVOID when upper third

### W02.  `T1=T1a AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=84  W=72/L=12  WR=85.7%
- Refine: exclude BBP=BBP4 drops 11/12 losers (92%)
- **Final: n=41  W=40/L=1  WR=97.6%**
- **Dir: ?**  •  1h trend WITH trade; RSI 70-80 overbought; session=ny_mid  •  AVOID when upper third

### W03.  `RSI=RSI6 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=84  W=72/L=12  WR=85.7%
- Refine: exclude BBP=BBP4 drops 11/12 losers (92%)
- **Final: n=41  W=40/L=1  WR=97.6%**
- **Dir: LONG**  •  RSI 70-80 overbought; session=ny_mid  •  AVOID when upper third

### W04.  `H60=H60a AND T1=T1a AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=84  W=72/L=12  WR=85.7%
- Refine: exclude BBP=BBP4 drops 11/12 losers (92%)
- **Final: n=41  W=40/L=1  WR=97.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 70-80 overbought; session=ny_mid  •  AVOID when upper third

### W05.  `H60=H60a AND RSI=RSI6 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=84  W=72/L=12  WR=85.7%
- Refine: exclude BBP=BBP4 drops 11/12 losers (92%)
- **Final: n=41  W=40/L=1  WR=97.6%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 70-80 overbought; session=ny_mid  •  AVOID when upper third

### W06.  `T1=T1a AND RSI=RSI6 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=84  W=72/L=12  WR=85.7%
- Refine: exclude BBP=BBP4 drops 11/12 losers (92%)
- **Final: n=41  W=40/L=1  WR=97.6%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 70-80 overbought; session=ny_mid  •  AVOID when upper third

### W07.  `H20=H20a AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=82  W=72/L=10  WR=87.8%
- Refine: exclude BBP=BBP4 drops 9/10 losers (90%)
- **Final: n=41  W=40/L=1  WR=97.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 70-80 overbought; session=ny_mid  •  AVOID when upper third

### W08.  `H20=H20a AND H60=H60a AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=82  W=72/L=10  WR=87.8%
- Refine: exclude BBP=BBP4 drops 9/10 losers (90%)
- **Final: n=41  W=40/L=1  WR=97.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 70-80 overbought; session=ny_mid  •  AVOID when upper third

### W09.  `H20=H20a AND T1=T1a AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=82  W=72/L=10  WR=87.8%
- Refine: exclude BBP=BBP4 drops 9/10 losers (90%)
- **Final: n=41  W=40/L=1  WR=97.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 70-80 overbought; session=ny_mid  •  AVOID when upper third

### W10.  `H20=H20a AND RSI=RSI6 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=82  W=72/L=10  WR=87.8%
- Refine: exclude BBP=BBP4 drops 9/10 losers (90%)
- **Final: n=41  W=40/L=1  WR=97.6%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 70-80 overbought; session=ny_mid  •  AVOID when upper third

### W11.  `H60=H60a AND T4=T4a AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=74  W=64/L=10  WR=86.5%
- Refine: exclude BBP=BBP4 drops 9/10 losers (90%)
- **Final: n=41  W=40/L=1  WR=97.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 70-80 overbought; session=ny_mid  •  AVOID when upper third

### W12.  `T1=T1a AND T4=T4a AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=74  W=64/L=10  WR=86.5%
- Refine: exclude BBP=BBP4 drops 9/10 losers (90%)
- **Final: n=41  W=40/L=1  WR=97.6%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 70-80 overbought; session=ny_mid  •  AVOID when upper third

### W13.  `T4=T4a AND RSI=RSI6 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=74  W=64/L=10  WR=86.5%
- Refine: exclude BBP=BBP4 drops 9/10 losers (90%)
- **Final: n=41  W=40/L=1  WR=97.6%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 70-80 overbought; session=ny_mid  •  AVOID when upper third

### W14.  `H20=H20a AND T4=T4a AND RSI=RSI6 AND session_bucket=ny_mid`
- Raw: n=72  W=64/L=8  WR=88.9%
- Refine: exclude BBP=BBP4 drops 7/8 losers (88%)
- **Final: n=41  W=40/L=1  WR=97.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 70-80 overbought; session=ny_mid  •  AVOID when upper third

### W15.  `H20=H20a AND BBP=BBP3 AND RSI=RSI5`
- Raw: n=68  W=58/L=10  WR=85.3%
- Refine: exclude session_bucket=asia drops 6/10 losers (60%)
- **Final: n=43  W=39/L=4  WR=90.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; middle of band; RSI 60-70 strong  •  AVOID when session=asia

### W16.  `H20=H20a AND BBP=BBP3 AND RSI=RSI5 AND ZS=ZS3`
- Raw: n=68  W=58/L=10  WR=85.3%
- Refine: exclude session_bucket=asia drops 6/10 losers (60%)
- **Final: n=43  W=39/L=4  WR=90.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; middle of band; RSI 60-70 strong; zscore -1 to +1 neutral  •  AVOID when session=asia

### W17.  `H60=H60a AND ZS=ZS5 AND session_bucket=ny_mid`
- Raw: n=64  W=62/L=2  WR=96.9%
- Refine: exclude BBP=BBP5 drops 2/2 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; zscore +2 to +3 deep overbought; session=ny_mid  •  AVOID when just touched upper band

### W18.  `T1=T1a AND ZS=ZS5 AND session_bucket=ny_mid`
- Raw: n=64  W=62/L=2  WR=96.9%
- Refine: exclude BBP=BBP5 drops 2/2 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; zscore +2 to +3 deep overbought; session=ny_mid  •  AVOID when just touched upper band

### W19.  `T4=T4a AND ZS=ZS5 AND session_bucket=ny_mid`
- Raw: n=64  W=62/L=2  WR=96.9%
- Refine: exclude BBP=BBP5 drops 2/2 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend WITH trade; zscore +2 to +3 deep overbought; session=ny_mid  •  AVOID when just touched upper band

### W20.  `ZS=ZS5 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=64  W=62/L=2  WR=96.9%
- Refine: exclude BBP=BBP5 drops 2/2 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: LONG**  •  zscore +2 to +3 deep overbought; session=ny_mid  •  AVOID when just touched upper band

### W21.  `H60=H60a AND T1=T1a AND ZS=ZS5 AND session_bucket=ny_mid`
- Raw: n=64  W=62/L=2  WR=96.9%
- Refine: exclude BBP=BBP5 drops 2/2 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; zscore +2 to +3 deep overbought; session=ny_mid  •  AVOID when just touched upper band

### W22.  `H60=H60a AND T4=T4a AND ZS=ZS5 AND session_bucket=ny_mid`
- Raw: n=64  W=62/L=2  WR=96.9%
- Refine: exclude BBP=BBP5 drops 2/2 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; zscore +2 to +3 deep overbought; session=ny_mid  •  AVOID when just touched upper band

### W23.  `H60=H60a AND ZS=ZS5 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=64  W=62/L=2  WR=96.9%
- Refine: exclude BBP=BBP5 drops 2/2 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; zscore +2 to +3 deep overbought; session=ny_mid  •  AVOID when just touched upper band

### W24.  `T1=T1a AND T4=T4a AND ZS=ZS5 AND session_bucket=ny_mid`
- Raw: n=64  W=62/L=2  WR=96.9%
- Refine: exclude BBP=BBP5 drops 2/2 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; zscore +2 to +3 deep overbought; session=ny_mid  •  AVOID when just touched upper band

### W25.  `T1=T1a AND ZS=ZS5 AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=64  W=62/L=2  WR=96.9%
- Refine: exclude BBP=BBP5 drops 2/2 losers (100%)
- **Final: n=28  W=28/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend WITH trade; zscore +2 to +3 deep overbought; session=ny_mid  •  AVOID when just touched upper band

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=188  W=75/L=113  WR=39.9%
- Sharpen: sharpest is ZS=ZS5 (42/113 of losers there)
- **Sharp: n=43  W=1/L=42  WR=2.3%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; session=ny_mid  •  ONLY when zscore +2 to +3 deep overbought

### L02.  `H20=H20e AND H60=H60e AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=188  W=75/L=113  WR=39.9%
- Sharpen: sharpest is ZS=ZS5 (42/113 of losers there)
- **Sharp: n=43  W=1/L=42  WR=2.3%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; session=ny_mid  •  ONLY when zscore +2 to +3 deep overbought

### L03.  `H20=H20e AND T1=T1c AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=188  W=75/L=113  WR=39.9%
- Sharpen: sharpest is ZS=ZS5 (42/113 of losers there)
- **Sharp: n=43  W=1/L=42  WR=2.3%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_mid  •  ONLY when zscore +2 to +3 deep overbought

### L04.  `H20=H20e AND T4=T4c AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=188  W=75/L=113  WR=39.9%
- Sharpen: sharpest is ZS=ZS5 (42/113 of losers there)
- **Sharp: n=43  W=1/L=42  WR=2.3%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade; session=ny_mid  •  ONLY when zscore +2 to +3 deep overbought

### L05.  `H20=H20e AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=134  W=47/L=87  WR=35.1%
- Sharpen: sharpest is ZS=ZS5 (24/87 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; RSI 60-70 strong; session=ny_mid  •  ONLY when zscore +2 to +3 deep overbought

### L06.  `H20=H20e AND H60=H60e AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=117  W=39/L=78  WR=33.3%
- Sharpen: sharpest is ZS=ZS5 (24/78 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 60-70 strong; session=ny_mid  •  ONLY when zscore +2 to +3 deep overbought

### L07.  `H20=H20e AND T1=T1c AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=117  W=39/L=78  WR=33.3%
- Sharpen: sharpest is ZS=ZS5 (24/78 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 60-70 strong; session=ny_mid  •  ONLY when zscore +2 to +3 deep overbought

### L08.  `H20=H20e AND T4=T4c AND RSI=RSI5 AND session_bucket=ny_mid`
- Raw: n=117  W=39/L=78  WR=33.3%
- Sharpen: sharpest is ZS=ZS5 (24/78 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 60-70 strong; session=ny_mid  •  ONLY when zscore +2 to +3 deep overbought

### L09.  `H20=H20e AND RSI=RSI5 AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=117  W=39/L=78  WR=33.3%
- Sharpen: sharpest is ZS=ZS5 (24/78 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 60-70 strong; session=ny_mid  •  ONLY when zscore +2 to +3 deep overbought

### L10.  `H20=H20a AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=115  W=42/L=73  WR=36.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=115  W=42/L=73  WR=36.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; zscore +2 to +3 deep overbought; session=asia

### L11.  `H60=H60e AND RSI=RSI6 AND session_bucket=asia`
- Raw: n=99  W=31/L=68  WR=31.3%
- Sharpen: sharpest is ZS=ZS4 (30/68 of losers there)
- **Sharp: n=36  W=6/L=30  WR=16.7%**
- **Dir: ?**  •  HTF60 strongly against; RSI 70-80 overbought; session=asia  •  ONLY when zscore +1 to +2 overbought

### L12.  `T1=T1c AND RSI=RSI6 AND session_bucket=asia`
- Raw: n=99  W=31/L=68  WR=31.3%
- Sharpen: sharpest is ZS=ZS4 (30/68 of losers there)
- **Sharp: n=36  W=6/L=30  WR=16.7%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 70-80 overbought; session=asia  •  ONLY when zscore +1 to +2 overbought

### L13.  `T4=T4c AND RSI=RSI6 AND session_bucket=asia`
- Raw: n=99  W=31/L=68  WR=31.3%
- Sharpen: sharpest is ZS=ZS4 (30/68 of losers there)
- **Sharp: n=36  W=6/L=30  WR=16.7%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 70-80 overbought; session=asia  •  ONLY when zscore +1 to +2 overbought

### L14.  `RSI=RSI6 AND direction_exec=short AND session_bucket=asia`
- Raw: n=99  W=31/L=68  WR=31.3%
- Sharpen: sharpest is ZS=ZS4 (30/68 of losers there)
- **Sharp: n=36  W=6/L=30  WR=16.7%**
- **Dir: SHORT**  •  RSI 70-80 overbought; session=asia  •  ONLY when zscore +1 to +2 overbought

### L15.  `H60=H60e AND T1=T1c AND RSI=RSI6 AND session_bucket=asia`
- Raw: n=99  W=31/L=68  WR=31.3%
- Sharpen: sharpest is ZS=ZS4 (30/68 of losers there)
- **Sharp: n=36  W=6/L=30  WR=16.7%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 70-80 overbought; session=asia  •  ONLY when zscore +1 to +2 overbought

### L16.  `H60=H60e AND T4=T4c AND RSI=RSI6 AND session_bucket=asia`
- Raw: n=99  W=31/L=68  WR=31.3%
- Sharpen: sharpest is ZS=ZS4 (30/68 of losers there)
- **Sharp: n=36  W=6/L=30  WR=16.7%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 70-80 overbought; session=asia  •  ONLY when zscore +1 to +2 overbought

### L17.  `H60=H60e AND RSI=RSI6 AND direction_exec=short AND session_bucket=asia`
- Raw: n=99  W=31/L=68  WR=31.3%
- Sharpen: sharpest is ZS=ZS4 (30/68 of losers there)
- **Sharp: n=36  W=6/L=30  WR=16.7%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 70-80 overbought; session=asia  •  ONLY when zscore +1 to +2 overbought

### L18.  `T1=T1c AND T4=T4c AND RSI=RSI6 AND session_bucket=asia`
- Raw: n=99  W=31/L=68  WR=31.3%
- Sharpen: sharpest is ZS=ZS4 (30/68 of losers there)
- **Sharp: n=36  W=6/L=30  WR=16.7%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 70-80 overbought; session=asia  •  ONLY when zscore +1 to +2 overbought

### L19.  `T1=T1c AND RSI=RSI6 AND direction_exec=short AND session_bucket=asia`
- Raw: n=99  W=31/L=68  WR=31.3%
- Sharpen: sharpest is ZS=ZS4 (30/68 of losers there)
- **Sharp: n=36  W=6/L=30  WR=16.7%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 70-80 overbought; session=asia  •  ONLY when zscore +1 to +2 overbought

### L20.  `T4=T4c AND RSI=RSI6 AND direction_exec=short AND session_bucket=asia`
- Raw: n=99  W=31/L=68  WR=31.3%
- Sharpen: sharpest is ZS=ZS4 (30/68 of losers there)
- **Sharp: n=36  W=6/L=30  WR=16.7%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 70-80 overbought; session=asia  •  ONLY when zscore +1 to +2 overbought

### L21.  `H20=H20a AND BBP=BBP6 AND session_bucket=asia`
- Raw: n=74  W=27/L=47  WR=36.5%
- Sharpen: sharpest is RSI=RSI6 (22/47 of losers there)
- **Sharp: n=28  W=6/L=22  WR=21.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; deep above upper band; session=asia  •  ONLY when RSI 70-80 overbought

### L22.  `H20=H20a AND BBP=BBP6 AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=74  W=27/L=47  WR=36.5%
- Sharpen: sharpest is RSI=RSI6 (22/47 of losers there)
- **Sharp: n=28  W=6/L=22  WR=21.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; deep above upper band; zscore +2 to +3 deep overbought; session=asia  •  ONLY when RSI 70-80 overbought

### L23.  `H60=H60e AND RSI=RSI6 AND ZS=ZS5`
- Raw: n=73  W=23/L=50  WR=31.5%
- Sharpen: sharpest is BBP=BBP5 (34/50 of losers there)
- **Sharp: n=38  W=4/L=34  WR=10.5%**
- **Dir: ?**  •  HTF60 strongly against; RSI 70-80 overbought; zscore +2 to +3 deep overbought  •  ONLY when just touched upper band

### L24.  `T1=T1c AND RSI=RSI6 AND ZS=ZS5`
- Raw: n=73  W=23/L=50  WR=31.5%
- Sharpen: sharpest is BBP=BBP5 (34/50 of losers there)
- **Sharp: n=38  W=4/L=34  WR=10.5%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 70-80 overbought; zscore +2 to +3 deep overbought  •  ONLY when just touched upper band

### L25.  `RSI=RSI6 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=73  W=23/L=50  WR=31.5%
- Sharpen: sharpest is BBP=BBP5 (34/50 of losers there)
- **Sharp: n=38  W=4/L=34  WR=10.5%**
- **Dir: SHORT**  •  RSI 70-80 overbought; zscore +2 to +3 deep overbought  •  ONLY when just touched upper band

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(54/44) | H20e(43/54) |
| H60 | H60a(58/40) | H60e(42/60) |
| T1 | T1a(56/41) | T1c(44/59) |
| T4 | T4a(56/42) | T4c(44/58) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(58/40) | short(42/60) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
