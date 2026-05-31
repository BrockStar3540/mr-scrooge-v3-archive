# AUD_USD — R32 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **1,837**  (W=1,136 / L=701)  -  WR: **61.8%**

## Session distribution

- ny_mid: n=438  W=260/L=178  WR=59.4%
- london_open: n=341  W=205/L=136  WR=60.1%
- asia: n=340  W=218/L=122  WR=64.1%
- ny_close: n=339  W=216/L=123  WR=63.7%
- ny_open: n=271  W=165/L=106  WR=60.9%
- london: n=64  W=43/L=21  WR=67.2%
- off_hours: n=44  W=29/L=15  WR=65.9%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60a AND T4=T4c AND ZS=ZS1`
- Raw: n=133  W=118/L=15  WR=88.7%
- Refine: exclude session_bucket=london_open drops 4/15 losers (27%)
- **Final: n=129  W=118/L=11  WR=91.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  AVOID when session=london_open

### W02.  `T4=T4c AND ZS=ZS1 AND direction_exec=long`
- Raw: n=133  W=118/L=15  WR=88.7%
- Refine: exclude session_bucket=london_open drops 4/15 losers (27%)
- **Final: n=129  W=118/L=11  WR=91.5%**
- **Dir: LONG**  •  4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  AVOID when session=london_open

### W03.  `H60=H60a AND T4=T4c AND ZS=ZS1 AND direction_exec=long`
- Raw: n=133  W=118/L=15  WR=88.7%
- Refine: exclude session_bucket=london_open drops 4/15 losers (27%)
- **Final: n=129  W=118/L=11  WR=91.5%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  AVOID when session=london_open

### W04.  `T1=T1c AND T4=T4c AND ZS=ZS1`
- Raw: n=117  W=105/L=12  WR=89.7%
- Refine: exclude session_bucket=london_open drops 4/12 losers (33%)
- **Final: n=113  W=105/L=8  WR=92.9%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  AVOID when session=london_open

### W05.  `H60=H60a AND T1=T1c AND T4=T4c AND ZS=ZS1`
- Raw: n=117  W=105/L=12  WR=89.7%
- Refine: exclude session_bucket=london_open drops 4/12 losers (33%)
- **Final: n=113  W=105/L=8  WR=92.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  AVOID when session=london_open

### W06.  `T1=T1c AND T4=T4c AND ZS=ZS1 AND direction_exec=long`
- Raw: n=117  W=105/L=12  WR=89.7%
- Refine: exclude session_bucket=london_open drops 4/12 losers (33%)
- **Final: n=113  W=105/L=8  WR=92.9%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  AVOID when session=london_open

### W07.  `H60=H60e AND RSI=RSI2 AND ZS=ZS3`
- Raw: n=115  W=102/L=13  WR=88.7%
- Refine: exclude BBP=BBP3 drops 11/13 losers (85%)
- **Final: n=54  W=52/L=2  WR=96.3%**
- **Dir: ?**  •  HTF60 strongly against; RSI 30-40 weak; zscore -1 to +1 neutral  •  AVOID when middle of band

### W08.  `RSI=RSI2 AND ZS=ZS3 AND direction_exec=short`
- Raw: n=115  W=102/L=13  WR=88.7%
- Refine: exclude BBP=BBP3 drops 11/13 losers (85%)
- **Final: n=54  W=52/L=2  WR=96.3%**
- **Dir: SHORT**  •  RSI 30-40 weak; zscore -1 to +1 neutral  •  AVOID when middle of band

### W09.  `H60=H60e AND RSI=RSI2 AND ZS=ZS3 AND direction_exec=short`
- Raw: n=115  W=102/L=13  WR=88.7%
- Refine: exclude BBP=BBP3 drops 11/13 losers (85%)
- **Final: n=54  W=52/L=2  WR=96.3%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 30-40 weak; zscore -1 to +1 neutral  •  AVOID when middle of band

### W10.  `T1=T1a AND RSI=RSI2 AND ZS=ZS3`
- Raw: n=115  W=100/L=15  WR=87.0%
- Refine: exclude BBP=BBP3 drops 11/15 losers (73%)
- **Final: n=54  W=50/L=4  WR=92.6%**
- **Dir: ?**  •  1h trend WITH trade; RSI 30-40 weak; zscore -1 to +1 neutral  •  AVOID when middle of band

### W11.  `H60=H60e AND T1=T1a AND RSI=RSI2 AND ZS=ZS3`
- Raw: n=113  W=100/L=13  WR=88.5%
- Refine: exclude BBP=BBP3 drops 11/13 losers (85%)
- **Final: n=52  W=50/L=2  WR=96.2%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; RSI 30-40 weak; zscore -1 to +1 neutral  •  AVOID when middle of band

### W12.  `T1=T1a AND RSI=RSI2 AND ZS=ZS3 AND direction_exec=short`
- Raw: n=113  W=100/L=13  WR=88.5%
- Refine: exclude BBP=BBP3 drops 11/13 losers (85%)
- **Final: n=52  W=50/L=2  WR=96.2%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 30-40 weak; zscore -1 to +1 neutral  •  AVOID when middle of band

### W13.  `H60=H60a AND T4=T4c AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=95  W=83/L=12  WR=87.4%
- Refine: exclude session_bucket=london_open drops 4/12 losers (33%)
- **Final: n=91  W=83/L=8  WR=91.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  AVOID when session=london_open

### W14.  `T1=T1c AND T4=T4c AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=95  W=83/L=12  WR=87.4%
- Refine: exclude session_bucket=london_open drops 4/12 losers (33%)
- **Final: n=91  W=83/L=8  WR=91.2%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  AVOID when session=london_open

### W15.  `T4=T4c AND RSI=RSI2 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=95  W=83/L=12  WR=87.4%
- Refine: exclude session_bucket=london_open drops 4/12 losers (33%)
- **Final: n=91  W=83/L=8  WR=91.2%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  AVOID when session=london_open

### W16.  `H60=H60a AND T4=T4c AND BBP=BBP1`
- Raw: n=85  W=77/L=8  WR=90.6%
- Refine: exclude session_bucket=london_open drops 4/8 losers (50%)
- **Final: n=81  W=77/L=4  WR=95.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; just touched lower band  •  AVOID when session=london_open

### W17.  `T4=T4c AND BBP=BBP1 AND direction_exec=long`
- Raw: n=85  W=77/L=8  WR=90.6%
- Refine: exclude session_bucket=london_open drops 4/8 losers (50%)
- **Final: n=81  W=77/L=4  WR=95.1%**
- **Dir: LONG**  •  4h trend AGAINST trade; just touched lower band  •  AVOID when session=london_open

### W18.  `H60=H60a AND T4=T4c AND BBP=BBP1 AND ZS=ZS1`
- Raw: n=85  W=77/L=8  WR=90.6%
- Refine: exclude session_bucket=london_open drops 4/8 losers (50%)
- **Final: n=81  W=77/L=4  WR=95.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; just touched lower band; zscore -3 to -2 deep oversold  •  AVOID when session=london_open

### W19.  `H60=H60a AND T4=T4c AND BBP=BBP1 AND direction_exec=long`
- Raw: n=85  W=77/L=8  WR=90.6%
- Refine: exclude session_bucket=london_open drops 4/8 losers (50%)
- **Final: n=81  W=77/L=4  WR=95.1%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; just touched lower band  •  AVOID when session=london_open

### W20.  `T4=T4c AND BBP=BBP1 AND ZS=ZS1 AND direction_exec=long`
- Raw: n=85  W=77/L=8  WR=90.6%
- Refine: exclude session_bucket=london_open drops 4/8 losers (50%)
- **Final: n=81  W=77/L=4  WR=95.1%**
- **Dir: LONG**  •  4h trend AGAINST trade; just touched lower band; zscore -3 to -2 deep oversold  •  AVOID when session=london_open

### W21.  `T1=T1c AND T4=T4c AND BBP=BBP1`
- Raw: n=83  W=75/L=8  WR=90.4%
- Refine: exclude session_bucket=london_open drops 4/8 losers (50%)
- **Final: n=79  W=75/L=4  WR=94.9%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; just touched lower band  •  AVOID when session=london_open

### W22.  `H60=H60a AND T1=T1c AND T4=T4c AND BBP=BBP1`
- Raw: n=83  W=75/L=8  WR=90.4%
- Refine: exclude session_bucket=london_open drops 4/8 losers (50%)
- **Final: n=79  W=75/L=4  WR=94.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; just touched lower band  •  AVOID when session=london_open

### W23.  `T1=T1c AND T4=T4c AND BBP=BBP1 AND ZS=ZS1`
- Raw: n=83  W=75/L=8  WR=90.4%
- Refine: exclude session_bucket=london_open drops 4/8 losers (50%)
- **Final: n=79  W=75/L=4  WR=94.9%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; just touched lower band; zscore -3 to -2 deep oversold  •  AVOID when session=london_open

### W24.  `T1=T1c AND T4=T4c AND BBP=BBP1 AND direction_exec=long`
- Raw: n=83  W=75/L=8  WR=90.4%
- Refine: exclude session_bucket=london_open drops 4/8 losers (50%)
- **Final: n=79  W=75/L=4  WR=94.9%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; just touched lower band  •  AVOID when session=london_open

### W25.  `T4=T4c AND ZS=ZS1 AND session_bucket=ny_open`
- Raw: n=76  W=72/L=4  WR=94.7%
- Refine: exclude H20=H20b drops 4/4 losers (100%)
- **Final: n=38  W=38/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend AGAINST trade; zscore -3 to -2 deep oversold; session=ny_open  •  AVOID when HTF20 slightly aligned

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND T4=T4a AND RSI=RSI3`
- Raw: n=146  W=56/L=90  WR=38.4%
- Sharpen: sharpest is H20=H20e (39/90 of losers there)
- **Sharp: n=49  W=10/L=39  WR=20.4%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when HTF20 strongly against

### L02.  `T4=T4a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=146  W=56/L=90  WR=38.4%
- Sharpen: sharpest is H20=H20e (39/90 of losers there)
- **Sharp: n=49  W=10/L=39  WR=20.4%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when HTF20 strongly against

### L03.  `H60=H60e AND T4=T4a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=146  W=56/L=90  WR=38.4%
- Sharpen: sharpest is H20=H20e (39/90 of losers there)
- **Sharp: n=49  W=10/L=39  WR=20.4%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when HTF20 strongly against

### L04.  `T1=T1a AND T4=T4a AND RSI=RSI3`
- Raw: n=125  W=49/L=76  WR=39.2%
- Sharpen: sharpest is H20=H20e (35/76 of losers there)
- **Sharp: n=45  W=10/L=35  WR=22.2%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when HTF20 strongly against

### L05.  `H60=H60e AND T1=T1a AND T4=T4a AND RSI=RSI3`
- Raw: n=122  W=47/L=75  WR=38.5%
- Sharpen: sharpest is H20=H20e (35/75 of losers there)
- **Sharp: n=45  W=10/L=35  WR=22.2%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when HTF20 strongly against

### L06.  `T1=T1a AND T4=T4a AND RSI=RSI3 AND direction_exec=short`
- Raw: n=122  W=47/L=75  WR=38.5%
- Sharpen: sharpest is H20=H20e (35/75 of losers there)
- **Sharp: n=45  W=10/L=35  WR=22.2%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral  •  ONLY when HTF20 strongly against

### L07.  `T1=T1c AND T4=T4c AND BBP=BBP2 AND RSI=RSI2`
- Raw: n=113  W=44/L=69  WR=38.9%
- Sharpen: sharpest is ZS=ZS3 (17/69 of losers there)
- **Sharp: n=20  W=3/L=17  WR=15.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; lower third; RSI 30-40 weak  •  ONLY when zscore -1 to +1 neutral

### L08.  `H60=H60a AND RSI=RSI2 AND ZS=ZS3`
- Raw: n=98  W=29/L=69  WR=29.6%
- Sharpen: sharpest is BBP=BBP2 (29/69 of losers there)
- **Sharp: n=36  W=7/L=29  WR=19.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 30-40 weak; zscore -1 to +1 neutral  •  ONLY when lower third

### L09.  `RSI=RSI2 AND ZS=ZS3 AND direction_exec=long`
- Raw: n=98  W=29/L=69  WR=29.6%
- Sharpen: sharpest is BBP=BBP2 (29/69 of losers there)
- **Sharp: n=36  W=7/L=29  WR=19.4%**
- **Dir: LONG**  •  RSI 30-40 weak; zscore -1 to +1 neutral  •  ONLY when lower third

### L10.  `H60=H60a AND RSI=RSI2 AND ZS=ZS3 AND direction_exec=long`
- Raw: n=98  W=29/L=69  WR=29.6%
- Sharpen: sharpest is BBP=BBP2 (29/69 of losers there)
- **Sharp: n=36  W=7/L=29  WR=19.4%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 30-40 weak; zscore -1 to +1 neutral  •  ONLY when lower third

### L11.  `T1=T1c AND RSI=RSI2 AND ZS=ZS3`
- Raw: n=98  W=31/L=67  WR=31.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=98  W=31/L=67  WR=31.6%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 30-40 weak; zscore -1 to +1 neutral

### L12.  `H60=H60a AND T1=T1c AND RSI=RSI2 AND ZS=ZS3`
- Raw: n=96  W=29/L=67  WR=30.2%
- Sharpen: sharpest is BBP=BBP2 (27/67 of losers there)
- **Sharp: n=34  W=7/L=27  WR=20.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 30-40 weak; zscore -1 to +1 neutral  •  ONLY when lower third

### L13.  `T1=T1c AND RSI=RSI2 AND ZS=ZS3 AND direction_exec=long`
- Raw: n=96  W=29/L=67  WR=30.2%
- Sharpen: sharpest is BBP=BBP2 (27/67 of losers there)
- **Sharp: n=34  W=7/L=27  WR=20.6%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 30-40 weak; zscore -1 to +1 neutral  •  ONLY when lower third

### L14.  `H60=H60a AND T4=T4a AND session_bucket=ny_close`
- Raw: n=92  W=35/L=57  WR=38.0%
- Sharpen: sharpest is ZS=ZS3 (21/57 of losers there)
- **Sharp: n=23  W=2/L=21  WR=8.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; session=ny_close  •  ONLY when zscore -1 to +1 neutral

### L15.  `T1=T1c AND T4=T4a AND session_bucket=ny_close`
- Raw: n=92  W=35/L=57  WR=38.0%
- Sharpen: sharpest is ZS=ZS3 (21/57 of losers there)
- **Sharp: n=23  W=2/L=21  WR=8.7%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; session=ny_close  •  ONLY when zscore -1 to +1 neutral

### L16.  `T4=T4a AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=92  W=35/L=57  WR=38.0%
- Sharpen: sharpest is ZS=ZS3 (21/57 of losers there)
- **Sharp: n=23  W=2/L=21  WR=8.7%**
- **Dir: LONG**  •  4h trend WITH trade; session=ny_close  •  ONLY when zscore -1 to +1 neutral

### L17.  `H60=H60a AND T1=T1c AND T4=T4a AND session_bucket=ny_close`
- Raw: n=92  W=35/L=57  WR=38.0%
- Sharpen: sharpest is ZS=ZS3 (21/57 of losers there)
- **Sharp: n=23  W=2/L=21  WR=8.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; session=ny_close  •  ONLY when zscore -1 to +1 neutral

### L18.  `H60=H60a AND T4=T4a AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=92  W=35/L=57  WR=38.0%
- Sharpen: sharpest is ZS=ZS3 (21/57 of losers there)
- **Sharp: n=23  W=2/L=21  WR=8.7%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend WITH trade; session=ny_close  •  ONLY when zscore -1 to +1 neutral

### L19.  `T1=T1c AND T4=T4a AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=92  W=35/L=57  WR=38.0%
- Sharpen: sharpest is ZS=ZS3 (21/57 of losers there)
- **Sharp: n=23  W=2/L=21  WR=8.7%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend WITH trade; session=ny_close  •  ONLY when zscore -1 to +1 neutral

### L20.  `T4=T4c AND BBP=BBP2 AND session_bucket=ny_mid`
- Raw: n=88  W=30/L=58  WR=34.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=88  W=30/L=58  WR=34.1%**
- **Dir: ?**  •  4h trend AGAINST trade; lower third; session=ny_mid

### L21.  `T4=T4c AND BBP=BBP2 AND RSI=RSI2 AND session_bucket=ny_mid`
- Raw: n=80  W=27/L=53  WR=33.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=80  W=27/L=53  WR=33.8%**
- **Dir: ?**  •  4h trend AGAINST trade; lower third; RSI 30-40 weak; session=ny_mid

### L22.  `H60=H60a AND BBP=BBP2 AND session_bucket=ny_close`
- Raw: n=74  W=29/L=45  WR=39.2%
- Sharpen: sharpest is H20=H20d (14/45 of losers there)
- **Sharp: n=18  W=4/L=14  WR=22.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; lower third; session=ny_close  •  ONLY when HTF20 mildly against

### L23.  `T1=T1c AND BBP=BBP2 AND session_bucket=ny_close`
- Raw: n=74  W=29/L=45  WR=39.2%
- Sharpen: sharpest is H20=H20d (14/45 of losers there)
- **Sharp: n=18  W=4/L=14  WR=22.2%**
- **Dir: ?**  •  1h trend AGAINST trade; lower third; session=ny_close  •  ONLY when HTF20 mildly against

### L24.  `BBP=BBP2 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=74  W=29/L=45  WR=39.2%
- Sharpen: sharpest is H20=H20d (14/45 of losers there)
- **Sharp: n=18  W=4/L=14  WR=22.2%**
- **Dir: LONG**  •  lower third; session=ny_close  •  ONLY when HTF20 mildly against

### L25.  `H60=H60a AND T1=T1c AND BBP=BBP2 AND session_bucket=ny_close`
- Raw: n=74  W=29/L=45  WR=39.2%
- Sharpen: sharpest is H20=H20d (14/45 of losers there)
- **Sharp: n=18  W=4/L=14  WR=22.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; lower third; session=ny_close  •  ONLY when HTF20 mildly against

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
