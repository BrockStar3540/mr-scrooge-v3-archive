# CAD_JPY — R20 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20d**  (EMA20 down 0.15-0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **2,898**  (W=1,879 / L=1,019)  -  WR: **64.8%**

## Session distribution

- asia: n=811  W=533/L=278  WR=65.7%
- london_open: n=656  W=412/L=244  WR=62.8%
- ny_close: n=355  W=228/L=127  WR=64.2%
- ny_open: n=328  W=217/L=111  WR=66.2%
- ny_mid: n=294  W=194/L=100  WR=66.0%
- london: n=219  W=146/L=73  WR=66.7%
- asia_late: n=154  W=101/L=53  WR=65.6%
- off_hours: n=81  W=48/L=33  WR=59.3%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND H60=H60a AND session_bucket=ny_open`
- Raw: n=138  W=130/L=8  WR=94.2%
- Refine: exclude ZS=ZS3 drops 6/8 losers (75%)
- **Final: n=125  W=123/L=2  WR=98.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=ny_open  •  AVOID when zscore -1 to +1 neutral

### W02.  `H20=H20a AND T1=T1c AND session_bucket=ny_open`
- Raw: n=138  W=130/L=8  WR=94.2%
- Refine: exclude ZS=ZS3 drops 6/8 losers (75%)
- **Final: n=125  W=123/L=2  WR=98.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; session=ny_open  •  AVOID when zscore -1 to +1 neutral

### W03.  `H20=H20a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=138  W=130/L=8  WR=94.2%
- Refine: exclude ZS=ZS3 drops 6/8 losers (75%)
- **Final: n=125  W=123/L=2  WR=98.4%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; session=ny_open  •  AVOID when zscore -1 to +1 neutral

### W04.  `H20=H20a AND H60=H60a AND T1=T1c AND session_bucket=ny_open`
- Raw: n=138  W=130/L=8  WR=94.2%
- Refine: exclude ZS=ZS3 drops 6/8 losers (75%)
- **Final: n=125  W=123/L=2  WR=98.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade; session=ny_open  •  AVOID when zscore -1 to +1 neutral

### W05.  `H20=H20a AND H60=H60a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=138  W=130/L=8  WR=94.2%
- Refine: exclude ZS=ZS3 drops 6/8 losers (75%)
- **Final: n=125  W=123/L=2  WR=98.4%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=ny_open  •  AVOID when zscore -1 to +1 neutral

### W06.  `H20=H20a AND T1=T1c AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=138  W=130/L=8  WR=94.2%
- Refine: exclude ZS=ZS3 drops 6/8 losers (75%)
- **Final: n=125  W=123/L=2  WR=98.4%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; session=ny_open  •  AVOID when zscore -1 to +1 neutral

### W07.  `T4=T4a AND RSI=RSI2 AND session_bucket=ny_close`
- Raw: n=131  W=118/L=13  WR=90.1%
- Refine: exclude BBP=BBP0 drops 5/13 losers (38%)
- **Final: n=120  W=112/L=8  WR=93.3%**
- **Dir: ?**  •  4h trend WITH trade; RSI 30-40 weak; session=ny_close  •  AVOID when deep below lower band

### W08.  `H60=H60e AND T4=T4a AND RSI=RSI2 AND session_bucket=ny_close`
- Raw: n=108  W=96/L=12  WR=88.9%
- Refine: exclude H20=H20a drops 7/12 losers (58%)
- **Final: n=89  W=84/L=5  WR=94.4%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; RSI 30-40 weak; session=ny_close  •  AVOID when HTF20 aligned WITH trade

### W09.  `T1=T1a AND T4=T4a AND RSI=RSI2 AND session_bucket=ny_close`
- Raw: n=108  W=96/L=12  WR=88.9%
- Refine: exclude H20=H20a drops 7/12 losers (58%)
- **Final: n=89  W=84/L=5  WR=94.4%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 30-40 weak; session=ny_close  •  AVOID when HTF20 aligned WITH trade

### W10.  `T4=T4a AND RSI=RSI2 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=108  W=96/L=12  WR=88.9%
- Refine: exclude H20=H20a drops 7/12 losers (58%)
- **Final: n=89  W=84/L=5  WR=94.4%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 30-40 weak; session=ny_close  •  AVOID when HTF20 aligned WITH trade

### W11.  `H20=H20a AND T4=T4c AND session_bucket=ny_open`
- Raw: n=104  W=96/L=8  WR=92.3%
- Refine: exclude ZS=ZS3 drops 6/8 losers (75%)
- **Final: n=91  W=89/L=2  WR=97.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; session=ny_open  •  AVOID when zscore -1 to +1 neutral

### W12.  `H20=H20a AND H60=H60a AND T4=T4c AND session_bucket=ny_open`
- Raw: n=104  W=96/L=8  WR=92.3%
- Refine: exclude ZS=ZS3 drops 6/8 losers (75%)
- **Final: n=91  W=89/L=2  WR=97.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend AGAINST trade; session=ny_open  •  AVOID when zscore -1 to +1 neutral

### W13.  `H20=H20a AND T1=T1c AND T4=T4c AND session_bucket=ny_open`
- Raw: n=104  W=96/L=8  WR=92.3%
- Refine: exclude ZS=ZS3 drops 6/8 losers (75%)
- **Final: n=91  W=89/L=2  WR=97.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_open  •  AVOID when zscore -1 to +1 neutral

### W14.  `H20=H20a AND T4=T4c AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=104  W=96/L=8  WR=92.3%
- Refine: exclude ZS=ZS3 drops 6/8 losers (75%)
- **Final: n=91  W=89/L=2  WR=97.8%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; session=ny_open  •  AVOID when zscore -1 to +1 neutral

### W15.  `H20=H20e AND H60=H60e AND RSI=RSI2 AND session_bucket=ny_close`
- Raw: n=100  W=87/L=13  WR=87.0%
- Refine: exclude T4=T4c drops 8/13 losers (62%)
- **Final: n=89  W=84/L=5  WR=94.4%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 30-40 weak; session=ny_close  •  AVOID when 4h trend AGAINST trade

### W16.  `H20=H20e AND T1=T1a AND RSI=RSI2 AND session_bucket=ny_close`
- Raw: n=100  W=87/L=13  WR=87.0%
- Refine: exclude T4=T4c drops 8/13 losers (62%)
- **Final: n=89  W=84/L=5  WR=94.4%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; RSI 30-40 weak; session=ny_close  •  AVOID when 4h trend AGAINST trade

### W17.  `H20=H20e AND RSI=RSI2 AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=100  W=87/L=13  WR=87.0%
- Refine: exclude T4=T4c drops 8/13 losers (62%)
- **Final: n=89  W=84/L=5  WR=94.4%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 30-40 weak; session=ny_close  •  AVOID when 4h trend AGAINST trade

### W18.  `T4=T4a AND BBP=BBP1 AND session_bucket=asia`
- Raw: n=97  W=83/L=14  WR=85.6%
- Refine: exclude strategy_id=bravo_failed_momentum drops 3/14 losers (21%)
- **Final: n=94  W=83/L=11  WR=88.3%**
- **Dir: ?**  •  4h trend WITH trade; just touched lower band; session=asia  •  AVOID when strategy=bravo_failed_momentum

### W19.  `T4=T4a AND BBP=BBP1 AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=97  W=83/L=14  WR=85.6%
- Refine: exclude strategy_id=bravo_failed_momentum drops 3/14 losers (21%)
- **Final: n=94  W=83/L=11  WR=88.3%**
- **Dir: ?**  •  4h trend WITH trade; just touched lower band; zscore -3 to -2 deep oversold; session=asia  •  AVOID when strategy=bravo_failed_momentum

### W20.  `H60=H60a AND RSI=RSI3 AND session_bucket=ny_open`
- Raw: n=95  W=88/L=7  WR=92.6%
- Refine: exclude ZS=ZS3 drops 5/7 losers (71%)
- **Final: n=84  W=82/L=2  WR=97.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral; session=ny_open  •  AVOID when zscore -1 to +1 neutral

### W21.  `T1=T1c AND RSI=RSI3 AND session_bucket=ny_open`
- Raw: n=95  W=88/L=7  WR=92.6%
- Refine: exclude ZS=ZS3 drops 5/7 losers (71%)
- **Final: n=84  W=82/L=2  WR=97.6%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 40-50 lower neutral; session=ny_open  •  AVOID when zscore -1 to +1 neutral

### W22.  `RSI=RSI3 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=95  W=88/L=7  WR=92.6%
- Refine: exclude ZS=ZS3 drops 5/7 losers (71%)
- **Final: n=84  W=82/L=2  WR=97.6%**
- **Dir: LONG**  •  RSI 40-50 lower neutral; session=ny_open  •  AVOID when zscore -1 to +1 neutral

### W23.  `H60=H60a AND T1=T1c AND RSI=RSI3 AND session_bucket=ny_open`
- Raw: n=95  W=88/L=7  WR=92.6%
- Refine: exclude ZS=ZS3 drops 5/7 losers (71%)
- **Final: n=84  W=82/L=2  WR=97.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 40-50 lower neutral; session=ny_open  •  AVOID when zscore -1 to +1 neutral

### W24.  `H60=H60a AND RSI=RSI3 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=95  W=88/L=7  WR=92.6%
- Refine: exclude ZS=ZS3 drops 5/7 losers (71%)
- **Final: n=84  W=82/L=2  WR=97.6%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 40-50 lower neutral; session=ny_open  •  AVOID when zscore -1 to +1 neutral

### W25.  `T1=T1c AND RSI=RSI3 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=95  W=88/L=7  WR=92.6%
- Refine: exclude ZS=ZS3 drops 5/7 losers (71%)
- **Final: n=84  W=82/L=2  WR=97.6%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 40-50 lower neutral; session=ny_open  •  AVOID when zscore -1 to +1 neutral

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60a AND T4=T4c AND session_bucket=ny_close`
- Raw: n=127  W=49/L=78  WR=38.6%
- Sharpen: sharpest is RSI=RSI2 (62/78 of losers there)
- **Sharp: n=82  W=20/L=62  WR=24.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=ny_close  •  ONLY when RSI 30-40 weak

### L02.  `T4=T4c AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=127  W=49/L=78  WR=38.6%
- Sharpen: sharpest is RSI=RSI2 (62/78 of losers there)
- **Sharp: n=82  W=20/L=62  WR=24.4%**
- **Dir: LONG**  •  4h trend AGAINST trade; session=ny_close  •  ONLY when RSI 30-40 weak

### L03.  `H60=H60a AND T4=T4c AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=127  W=49/L=78  WR=38.6%
- Sharpen: sharpest is RSI=RSI2 (62/78 of losers there)
- **Sharp: n=82  W=20/L=62  WR=24.4%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=ny_close  •  ONLY when RSI 30-40 weak

### L04.  `T1=T1c AND T4=T4c AND session_bucket=ny_close`
- Raw: n=126  W=49/L=77  WR=38.9%
- Sharpen: sharpest is RSI=RSI2 (62/77 of losers there)
- **Sharp: n=82  W=20/L=62  WR=24.4%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_close  •  ONLY when RSI 30-40 weak

### L05.  `T4=T4c AND BBP=BBP2 AND session_bucket=asia`
- Raw: n=126  W=49/L=77  WR=38.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=126  W=49/L=77  WR=38.9%**
- **Dir: ?**  •  4h trend AGAINST trade; lower third; session=asia

### L06.  `H60=H60a AND T1=T1c AND T4=T4c AND session_bucket=ny_close`
- Raw: n=126  W=49/L=77  WR=38.9%
- Sharpen: sharpest is RSI=RSI2 (62/77 of losers there)
- **Sharp: n=82  W=20/L=62  WR=24.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_close  •  ONLY when RSI 30-40 weak

### L07.  `T1=T1c AND T4=T4c AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=126  W=49/L=77  WR=38.9%
- Sharpen: sharpest is RSI=RSI2 (62/77 of losers there)
- **Sharp: n=82  W=20/L=62  WR=24.4%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_close  •  ONLY when RSI 30-40 weak

### L08.  `H60=H60a AND T4=T4c AND BBP=BBP2 AND session_bucket=asia`
- Raw: n=116  W=46/L=70  WR=39.7%
- Sharpen: no sharper sub-pattern
- **Sharp: n=116  W=46/L=70  WR=39.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; lower third; session=asia

### L09.  `T4=T4c AND BBP=BBP2 AND direction_exec=long AND session_bucket=asia`
- Raw: n=116  W=46/L=70  WR=39.7%
- Sharpen: no sharper sub-pattern
- **Sharp: n=116  W=46/L=70  WR=39.7%**
- **Dir: LONG**  •  4h trend AGAINST trade; lower third; session=asia

### L10.  `T4=T4c AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=114  W=43/L=71  WR=37.7%
- Sharpen: no sharper sub-pattern
- **Sharp: n=114  W=43/L=71  WR=37.7%**
- **Dir: ?**  •  4h trend AGAINST trade; zscore -2 to -1 oversold; session=asia

### L11.  `T4=T4c AND BBP=BBP2 AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=114  W=43/L=71  WR=37.7%
- Sharpen: no sharper sub-pattern
- **Sharp: n=114  W=43/L=71  WR=37.7%**
- **Dir: ?**  •  4h trend AGAINST trade; lower third; zscore -2 to -1 oversold; session=asia

### L12.  `T1=T1c AND T4=T4c AND BBP=BBP2 AND session_bucket=asia`
- Raw: n=114  W=44/L=70  WR=38.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=114  W=44/L=70  WR=38.6%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; lower third; session=asia

### L13.  `H60=H60a AND RSI=RSI2 AND session_bucket=ny_close`
- Raw: n=105  W=42/L=63  WR=40.0%
- Sharpen: sharpest is T4=T4c (62/63 of losers there)
- **Sharp: n=82  W=20/L=62  WR=24.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 30-40 weak; session=ny_close  •  ONLY when 4h trend AGAINST trade

### L14.  `T1=T1c AND RSI=RSI2 AND session_bucket=ny_close`
- Raw: n=105  W=42/L=63  WR=40.0%
- Sharpen: sharpest is T4=T4c (62/63 of losers there)
- **Sharp: n=82  W=20/L=62  WR=24.4%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 30-40 weak; session=ny_close  •  ONLY when 4h trend AGAINST trade

### L15.  `RSI=RSI2 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=105  W=42/L=63  WR=40.0%
- Sharpen: sharpest is T4=T4c (62/63 of losers there)
- **Sharp: n=82  W=20/L=62  WR=24.4%**
- **Dir: LONG**  •  RSI 30-40 weak; session=ny_close  •  ONLY when 4h trend AGAINST trade

### L16.  `H60=H60a AND T1=T1c AND RSI=RSI2 AND session_bucket=ny_close`
- Raw: n=105  W=42/L=63  WR=40.0%
- Sharpen: sharpest is T4=T4c (62/63 of losers there)
- **Sharp: n=82  W=20/L=62  WR=24.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 30-40 weak; session=ny_close  •  ONLY when 4h trend AGAINST trade

### L17.  `H60=H60a AND RSI=RSI2 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=105  W=42/L=63  WR=40.0%
- Sharpen: sharpest is T4=T4c (62/63 of losers there)
- **Sharp: n=82  W=20/L=62  WR=24.4%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 30-40 weak; session=ny_close  •  ONLY when 4h trend AGAINST trade

### L18.  `T1=T1c AND RSI=RSI2 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=105  W=42/L=63  WR=40.0%
- Sharpen: sharpest is T4=T4c (62/63 of losers there)
- **Sharp: n=82  W=20/L=62  WR=24.4%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 30-40 weak; session=ny_close  •  ONLY when 4h trend AGAINST trade

### L19.  `H60=H60a AND T4=T4c AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=104  W=40/L=64  WR=38.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=104  W=40/L=64  WR=38.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; zscore -2 to -1 oversold; session=asia

### L20.  `T4=T4c AND ZS=ZS2 AND direction_exec=long AND session_bucket=asia`
- Raw: n=104  W=40/L=64  WR=38.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=104  W=40/L=64  WR=38.5%**
- **Dir: LONG**  •  4h trend AGAINST trade; zscore -2 to -1 oversold; session=asia

### L21.  `T1=T1c AND T4=T4c AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=102  W=38/L=64  WR=37.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=102  W=38/L=64  WR=37.3%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; zscore -2 to -1 oversold; session=asia

### L22.  `T4=T4c AND RSI=RSI2 AND session_bucket=ny_close`
- Raw: n=93  W=23/L=70  WR=24.7%
- Sharpen: sharpest is BBP=BBP2 (35/70 of losers there)
- **Sharp: n=40  W=5/L=35  WR=12.5%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 30-40 weak; session=ny_close  •  ONLY when lower third

### L23.  `T4=T4c AND RSI=RSI2 AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=90  W=36/L=54  WR=40.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=90  W=36/L=54  WR=40.0%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 30-40 weak; zscore -2 to -1 oversold; session=asia

### L24.  `H20=H20a AND H60=H60a AND RSI=RSI2 AND session_bucket=ny_close`
- Raw: n=89  W=35/L=54  WR=39.3%
- Sharpen: sharpest is T4=T4c (53/54 of losers there)
- **Sharp: n=66  W=13/L=53  WR=19.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 30-40 weak; session=ny_close  •  ONLY when 4h trend AGAINST trade

### L25.  `H20=H20a AND T1=T1c AND RSI=RSI2 AND session_bucket=ny_close`
- Raw: n=89  W=35/L=54  WR=39.3%
- Sharpen: sharpest is T4=T4c (53/54 of losers there)
- **Sharp: n=66  W=13/L=53  WR=19.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 30-40 weak; session=ny_close  •  ONLY when 4h trend AGAINST trade

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | H60e(51/45) | H60a(47/54) |
| T1 | T1a(52/46) | T1c(47/54) |
| T4 | T4a(55/39) | T4c(45/61) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(51/46) | long(49/54) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
