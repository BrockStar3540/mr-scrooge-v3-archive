# GBP_JPY — R39 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20d**  (EMA20 down 0.15-0.5x)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **6,541**  (W=3,947 / L=2,594)  -  WR: **60.3%**

## Session distribution

- asia: n=1812  W=1107/L=705  WR=61.1%
- london_open: n=1291  W=778/L=513  WR=60.3%
- ny_open: n=1061  W=637/L=424  WR=60.0%
- ny_mid: n=775  W=470/L=305  WR=60.6%
- london: n=685  W=417/L=268  WR=60.9%
- asia_late: n=482  W=286/L=196  WR=59.3%
- ny_close: n=344  W=215/L=129  WR=62.5%
- off_hours: n=91  W=37/L=54  WR=40.7%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND BBP=BBP3 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=137  W=118/L=19  WR=86.1%
- Refine: exclude T1=T1c drops 11/19 losers (58%)
- **Final: n=87  W=79/L=8  WR=90.8%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; middle of band; RSI 50-60 upper neutral  •  AVOID when 1h trend AGAINST trade

### W02.  `H20=H20a AND H60=H60a AND BBP=BBP3 AND RSI=RSI4`
- Raw: n=127  W=108/L=19  WR=85.0%
- Refine: exclude T1=T1c drops 11/19 losers (58%)
- **Final: n=77  W=69/L=8  WR=89.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; middle of band; RSI 50-60 upper neutral  •  AVOID when 1h trend AGAINST trade

### W03.  `T4=T4a AND BBP=BBP4 AND RSI=RSI4 AND session_bucket=ny_open`
- Raw: n=115  W=100/L=15  WR=87.0%
- Refine: exclude H20=H20d drops 4/15 losers (27%)
- **Final: n=102  W=91/L=11  WR=89.2%**
- **Dir: ?**  •  4h trend WITH trade; upper third; RSI 50-60 upper neutral; session=ny_open  •  AVOID when HTF20 mildly against

### W04.  `H20=H20a AND H60=H60a AND ZS=ZS0`
- Raw: n=111  W=98/L=13  WR=88.3%
- Refine: exclude T1=T1a drops 7/13 losers (54%)
- **Final: n=94  W=88/L=6  WR=93.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; zscore <-3 extreme  •  AVOID when 1h trend WITH trade

### W05.  `H20=H20a AND ZS=ZS0 AND direction_exec=long`
- Raw: n=111  W=98/L=13  WR=88.3%
- Refine: exclude T1=T1a drops 7/13 losers (54%)
- **Final: n=94  W=88/L=6  WR=93.6%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; zscore <-3 extreme  •  AVOID when 1h trend WITH trade

### W06.  `H20=H20a AND H60=H60a AND BBP=BBP0 AND ZS=ZS0`
- Raw: n=111  W=98/L=13  WR=88.3%
- Refine: exclude T1=T1a drops 7/13 losers (54%)
- **Final: n=94  W=88/L=6  WR=93.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; deep below lower band; zscore <-3 extreme  •  AVOID when 1h trend WITH trade

### W07.  `H20=H20a AND H60=H60a AND ZS=ZS0 AND direction_exec=long`
- Raw: n=111  W=98/L=13  WR=88.3%
- Refine: exclude T1=T1a drops 7/13 losers (54%)
- **Final: n=94  W=88/L=6  WR=93.6%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; zscore <-3 extreme  •  AVOID when 1h trend WITH trade

### W08.  `H20=H20a AND BBP=BBP0 AND ZS=ZS0 AND direction_exec=long`
- Raw: n=111  W=98/L=13  WR=88.3%
- Refine: exclude T1=T1a drops 7/13 losers (54%)
- **Final: n=94  W=88/L=6  WR=93.6%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; deep below lower band; zscore <-3 extreme  •  AVOID when 1h trend WITH trade

### W09.  `T1=T1c AND RSI=RSI3 AND ZS=ZS0`
- Raw: n=111  W=96/L=15  WR=86.5%
- Refine: exclude H20=H20d drops 7/15 losers (47%)
- **Final: n=104  W=96/L=8  WR=92.3%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 40-50 lower neutral; zscore <-3 extreme  •  AVOID when HTF20 mildly against

### W10.  `T1=T1c AND BBP=BBP0 AND RSI=RSI3 AND ZS=ZS0`
- Raw: n=111  W=96/L=15  WR=86.5%
- Refine: exclude H20=H20d drops 7/15 losers (47%)
- **Final: n=104  W=96/L=8  WR=92.3%**
- **Dir: ?**  •  1h trend AGAINST trade; deep below lower band; RSI 40-50 lower neutral; zscore <-3 extreme  •  AVOID when HTF20 mildly against

### W11.  `H60=H60a AND T1=T1c AND ZS=ZS0`
- Raw: n=110  W=96/L=14  WR=87.3%
- Refine: exclude session_bucket=asia drops 14/14 losers (100%)
- **Final: n=60  W=60/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; zscore <-3 extreme  •  AVOID when session=asia

### W12.  `H60=H60a AND T1=T1c AND BBP=BBP0 AND ZS=ZS0`
- Raw: n=110  W=96/L=14  WR=87.3%
- Refine: exclude session_bucket=asia drops 14/14 losers (100%)
- **Final: n=60  W=60/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; deep below lower band; zscore <-3 extreme  •  AVOID when session=asia

### W13.  `H60=H60a AND T1=T1c AND ZS=ZS0 AND direction_exec=long`
- Raw: n=110  W=96/L=14  WR=87.3%
- Refine: exclude session_bucket=asia drops 14/14 losers (100%)
- **Final: n=60  W=60/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; zscore <-3 extreme  •  AVOID when session=asia

### W14.  `H60=H60e AND T1=T1a AND RSI=RSI3 AND ZS=ZS4`
- Raw: n=106  W=94/L=12  WR=88.7%
- Refine: exclude session_bucket=london_open drops 6/12 losers (50%)
- **Final: n=89  W=83/L=6  WR=93.3%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; RSI 40-50 lower neutral; zscore +1 to +2 overbought  •  AVOID when session=london_open

### W15.  `T1=T1a AND RSI=RSI3 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=106  W=94/L=12  WR=88.7%
- Refine: exclude session_bucket=london_open drops 6/12 losers (50%)
- **Final: n=89  W=83/L=6  WR=93.3%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 40-50 lower neutral; zscore +1 to +2 overbought  •  AVOID when session=london_open

### W16.  `T1=T1c AND T4=T4a AND RSI=RSI3 AND ZS=ZS0`
- Raw: n=103  W=88/L=15  WR=85.4%
- Refine: exclude H20=H20d drops 7/15 losers (47%)
- **Final: n=96  W=88/L=8  WR=91.7%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 40-50 lower neutral; zscore <-3 extreme  •  AVOID when HTF20 mildly against

### W17.  `T4=T4a AND RSI=RSI4 AND ZS=ZS4 AND session_bucket=ny_open`
- Raw: n=100  W=85/L=15  WR=85.0%
- Refine: exclude H20=H20d drops 4/15 losers (27%)
- **Final: n=87  W=76/L=11  WR=87.4%**
- **Dir: ?**  •  4h trend WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought; session=ny_open  •  AVOID when HTF20 mildly against

### W18.  `H60=H60e AND T4=T4c AND RSI=RSI3 AND ZS=ZS4`
- Raw: n=95  W=85/L=10  WR=89.5%
- Refine: exclude session_bucket=london_open drops 6/10 losers (60%)
- **Final: n=72  W=68/L=4  WR=94.4%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 40-50 lower neutral; zscore +1 to +2 overbought  •  AVOID when session=london_open

### W19.  `T4=T4c AND RSI=RSI3 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=95  W=85/L=10  WR=89.5%
- Refine: exclude session_bucket=london_open drops 6/10 losers (60%)
- **Final: n=72  W=68/L=4  WR=94.4%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 40-50 lower neutral; zscore +1 to +2 overbought  •  AVOID when session=london_open

### W20.  `H20=H20a AND T1=T1c AND ZS=ZS0`
- Raw: n=94  W=88/L=6  WR=93.6%
- Refine: exclude RSI=RSI2 drops 6/6 losers (100%)
- **Final: n=84  W=84/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; zscore <-3 extreme  •  AVOID when RSI 30-40 weak

### W21.  `H20=H20a AND H60=H60a AND T1=T1c AND ZS=ZS0`
- Raw: n=94  W=88/L=6  WR=93.6%
- Refine: exclude RSI=RSI2 drops 6/6 losers (100%)
- **Final: n=84  W=84/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade; zscore <-3 extreme  •  AVOID when RSI 30-40 weak

### W22.  `H20=H20a AND T1=T1c AND BBP=BBP0 AND ZS=ZS0`
- Raw: n=94  W=88/L=6  WR=93.6%
- Refine: exclude RSI=RSI2 drops 6/6 losers (100%)
- **Final: n=84  W=84/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; deep below lower band; zscore <-3 extreme  •  AVOID when RSI 30-40 weak

### W23.  `H20=H20a AND T1=T1c AND ZS=ZS0 AND direction_exec=long`
- Raw: n=94  W=88/L=6  WR=93.6%
- Refine: exclude RSI=RSI2 drops 6/6 losers (100%)
- **Final: n=84  W=84/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; zscore <-3 extreme  •  AVOID when RSI 30-40 weak

### W24.  `H60=H60a AND T1=T1a AND T4=T4c AND BBP=BBP2`
- Raw: n=94  W=80/L=14  WR=85.1%
- Refine: exclude RSI=RSI3 drops 12/14 losers (86%)
- **Final: n=47  W=45/L=2  WR=95.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade; lower third  •  AVOID when RSI 40-50 lower neutral

### W25.  `T4=T4c AND BBP=BBP3 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=94  W=80/L=14  WR=85.1%
- Refine: exclude H20=H20d drops 6/14 losers (43%)
- **Final: n=76  W=68/L=8  WR=89.5%**
- **Dir: LONG**  •  4h trend AGAINST trade; middle of band; RSI 50-60 upper neutral  •  AVOID when HTF20 mildly against

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `RSI=RSI4 AND ZS=ZS3 AND direction_exec=short`
- Raw: n=254  W=98/L=156  WR=38.6%
- Sharpen: sharpest is BBP=BBP3 (115/156 of losers there)
- **Sharp: n=159  W=44/L=115  WR=27.7%**
- **Dir: SHORT**  •  RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  ONLY when middle of band

### L02.  `H60=H60e AND RSI=RSI4 AND ZS=ZS3`
- Raw: n=237  W=91/L=146  WR=38.4%
- Sharpen: sharpest is BBP=BBP3 (107/146 of losers there)
- **Sharp: n=148  W=41/L=107  WR=27.7%**
- **Dir: ?**  •  HTF60 strongly against; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  ONLY when middle of band

### L03.  `H60=H60e AND RSI=RSI4 AND ZS=ZS3 AND direction_exec=short`
- Raw: n=237  W=91/L=146  WR=38.4%
- Sharpen: sharpest is BBP=BBP3 (107/146 of losers there)
- **Sharp: n=148  W=41/L=107  WR=27.7%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  ONLY when middle of band

### L04.  `BBP=BBP4 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=196  W=64/L=132  WR=32.7%
- Sharpen: sharpest is H20=H20e (33/132 of losers there)
- **Sharp: n=35  W=2/L=33  WR=5.7%**
- **Dir: LONG**  •  upper third; RSI 40-50 lower neutral  •  ONLY when HTF20 strongly against

### L05.  `H60=H60a AND BBP=BBP4 AND RSI=RSI3`
- Raw: n=187  W=64/L=123  WR=34.2%
- Sharpen: sharpest is H20=H20e (33/123 of losers there)
- **Sharp: n=35  W=2/L=33  WR=5.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; upper third; RSI 40-50 lower neutral  •  ONLY when HTF20 strongly against

### L06.  `H60=H60a AND BBP=BBP4 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=187  W=64/L=123  WR=34.2%
- Sharpen: sharpest is H20=H20e (33/123 of losers there)
- **Sharp: n=35  W=2/L=33  WR=5.7%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; upper third; RSI 40-50 lower neutral  •  ONLY when HTF20 strongly against

### L07.  `T1=T1c AND RSI=RSI4 AND ZS=ZS3 AND direction_exec=short`
- Raw: n=181  W=71/L=110  WR=39.2%
- Sharpen: sharpest is BBP=BBP3 (79/110 of losers there)
- **Sharp: n=103  W=24/L=79  WR=23.3%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  ONLY when middle of band

### L08.  `H20=H20a AND T1=T1a AND T4=T4a AND RSI=RSI3`
- Raw: n=177  W=63/L=114  WR=35.6%
- Sharpen: sharpest is BBP=BBP0 (19/114 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when deep below lower band

### L09.  `H60=H60e AND T1=T1c AND RSI=RSI4 AND ZS=ZS3`
- Raw: n=173  W=67/L=106  WR=38.7%
- Sharpen: sharpest is BBP=BBP3 (76/106 of losers there)
- **Sharp: n=100  W=24/L=76  WR=24.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  ONLY when middle of band

### L10.  `H60=H60e AND T1=T1a AND BBP=BBP0 AND RSI=RSI3`
- Raw: n=173  W=69/L=104  WR=39.9%
- Sharpen: sharpest is ZS=ZS0 (42/104 of losers there)
- **Sharp: n=48  W=6/L=42  WR=12.5%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; deep below lower band; RSI 40-50 lower neutral  •  ONLY when zscore <-3 extreme

### L11.  `H20=H20e AND RSI=RSI4 AND ZS=ZS3 AND direction_exec=short`
- Raw: n=169  W=63/L=106  WR=37.3%
- Sharpen: sharpest is BBP=BBP3 (75/106 of losers there)
- **Sharp: n=105  W=30/L=75  WR=28.6%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  ONLY when middle of band

### L12.  `H20=H20e AND H60=H60e AND RSI=RSI4 AND ZS=ZS3`
- Raw: n=161  W=59/L=102  WR=36.6%
- Sharpen: sharpest is BBP=BBP3 (72/102 of losers there)
- **Sharp: n=102  W=30/L=72  WR=29.4%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  ONLY when middle of band

### L13.  `BBP=BBP3 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=159  W=44/L=115  WR=27.7%
- Sharpen: sharpest is T4=T4a (51/115 of losers there)
- **Sharp: n=63  W=12/L=51  WR=19.0%**
- **Dir: SHORT**  •  middle of band; RSI 50-60 upper neutral  •  ONLY when 4h trend WITH trade

### L14.  `BBP=BBP3 AND RSI=RSI4 AND ZS=ZS3 AND direction_exec=short`
- Raw: n=159  W=44/L=115  WR=27.7%
- Sharpen: sharpest is T4=T4a (51/115 of losers there)
- **Sharp: n=63  W=12/L=51  WR=19.0%**
- **Dir: SHORT**  •  middle of band; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  ONLY when 4h trend WITH trade

### L15.  `H20=H20a AND BBP=BBP4 AND RSI=RSI3 AND direction_exec=long`
- Raw: n=153  W=58/L=95  WR=37.9%
- Sharpen: sharpest is T1=T1c (74/95 of losers there)
- **Sharp: n=108  W=34/L=74  WR=31.5%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; upper third; RSI 40-50 lower neutral  •  ONLY when 1h trend AGAINST trade

### L16.  `H20=H20e AND H60=H60e AND RSI=RSI4 AND session_bucket=london_open`
- Raw: n=150  W=60/L=90  WR=40.0%
- Sharpen: sharpest is T4=T4c (57/90 of losers there)
- **Sharp: n=78  W=21/L=57  WR=26.9%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 50-60 upper neutral; session=london_open  •  ONLY when 4h trend AGAINST trade

### L17.  `H60=H60e AND BBP=BBP3 AND RSI=RSI4`
- Raw: n=148  W=41/L=107  WR=27.7%
- Sharpen: sharpest is T4=T4a (43/107 of losers there)
- **Sharp: n=52  W=9/L=43  WR=17.3%**
- **Dir: ?**  •  HTF60 strongly against; middle of band; RSI 50-60 upper neutral  •  ONLY when 4h trend WITH trade

### L18.  `H60=H60e AND BBP=BBP3 AND RSI=RSI4 AND ZS=ZS3`
- Raw: n=148  W=41/L=107  WR=27.7%
- Sharpen: sharpest is T4=T4a (43/107 of losers there)
- **Sharp: n=52  W=9/L=43  WR=17.3%**
- **Dir: ?**  •  HTF60 strongly against; middle of band; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  ONLY when 4h trend WITH trade

### L19.  `H60=H60e AND BBP=BBP3 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=148  W=41/L=107  WR=27.7%
- Sharpen: sharpest is T4=T4a (43/107 of losers there)
- **Sharp: n=52  W=9/L=43  WR=17.3%**
- **Dir: SHORT**  •  HTF60 strongly against; middle of band; RSI 50-60 upper neutral  •  ONLY when 4h trend WITH trade

### L20.  `T1=T1c AND RSI=RSI3 AND ZS=ZS4`
- Raw: n=147  W=58/L=89  WR=39.5%
- Sharpen: sharpest is H60=H60a (71/89 of losers there)
- **Sharp: n=94  W=23/L=71  WR=24.5%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 40-50 lower neutral; zscore +1 to +2 overbought  •  ONLY when HTF60 aligned WITH trade

### L21.  `H60=H60e AND T4=T4c AND BBP=BBP0 AND RSI=RSI3`
- Raw: n=147  W=58/L=89  WR=39.5%
- Sharpen: sharpest is ZS=ZS0 (34/89 of losers there)
- **Sharp: n=40  W=6/L=34  WR=15.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; deep below lower band; RSI 40-50 lower neutral  •  ONLY when zscore <-3 extreme

### L22.  `T1=T1c AND BBP=BBP4 AND RSI=RSI3 AND ZS=ZS4`
- Raw: n=147  W=58/L=89  WR=39.5%
- Sharpen: sharpest is H60=H60a (71/89 of losers there)
- **Sharp: n=94  W=23/L=71  WR=24.5%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; RSI 40-50 lower neutral; zscore +1 to +2 overbought  •  ONLY when HTF60 aligned WITH trade

### L23.  `H20=H20a AND H60=H60a AND BBP=BBP4 AND RSI=RSI3`
- Raw: n=145  W=58/L=87  WR=40.0%
- Sharpen: sharpest is T1=T1c (70/87 of losers there)
- **Sharp: n=104  W=34/L=70  WR=32.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; upper third; RSI 40-50 lower neutral  •  ONLY when 1h trend AGAINST trade

### L24.  `RSI=RSI3 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=138  W=45/L=93  WR=32.6%
- Sharpen: sharpest is T1=T1c (71/93 of losers there)
- **Sharp: n=94  W=23/L=71  WR=24.5%**
- **Dir: LONG**  •  RSI 40-50 lower neutral; zscore +1 to +2 overbought  •  ONLY when 1h trend AGAINST trade

### L25.  `BBP=BBP4 AND RSI=RSI3 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=138  W=45/L=93  WR=32.6%
- Sharpen: sharpest is T1=T1c (71/93 of losers there)
- **Sharp: n=94  W=23/L=71  WR=24.5%**
- **Dir: LONG**  •  upper third; RSI 40-50 lower neutral; zscore +1 to +2 overbought  •  ONLY when 1h trend AGAINST trade

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | — |
| T1 | — | — |
| T4 | T4c(52/47) | T4a(48/53) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
