# CHF_JPY — R22 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_3**  (5m ATR >120%)
- **A1 = A1_2**  (1h ATR 4-8x)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50e**  (EMA50 down >0.5x)
- **ADR = ADR5**  (>110% overshoot)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **6,519**  (W=3,527 / L=2,992)  -  WR: **54.1%**

## Session distribution

- ny_mid: n=1643  W=911/L=732  WR=55.4%
- asia: n=1221  W=671/L=550  WR=55.0%
- london_open: n=1109  W=586/L=523  WR=52.8%
- ny_close: n=816  W=465/L=351  WR=57.0%
- london: n=723  W=366/L=357  WR=50.6%
- ny_open: n=648  W=360/L=288  WR=55.6%
- asia_late: n=229  W=104/L=125  WR=45.4%
- off_hours: n=130  W=64/L=66  WR=49.2%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20d AND RSI=RSI0 AND session_bucket=asia`
- Raw: n=127  W=118/L=9  WR=92.9%
- Refine: exclude ZS=ZS1 drops 7/9 losers (78%)
- **Final: n=79  W=77/L=2  WR=97.5%**
- **Dir: ?**  •  HTF20 mildly against; RSI<20 extreme oversold; session=asia  •  AVOID when zscore -3 to -2 deep oversold

### W02.  `H60=H60e AND RSI=RSI0 AND session_bucket=asia`
- Raw: n=127  W=118/L=9  WR=92.9%
- Refine: exclude ZS=ZS1 drops 7/9 losers (78%)
- **Final: n=79  W=77/L=2  WR=97.5%**
- **Dir: ?**  •  HTF60 strongly against; RSI<20 extreme oversold; session=asia  •  AVOID when zscore -3 to -2 deep oversold

### W03.  `T1=T1a AND RSI=RSI0 AND session_bucket=asia`
- Raw: n=127  W=118/L=9  WR=92.9%
- Refine: exclude ZS=ZS1 drops 7/9 losers (78%)
- **Final: n=79  W=77/L=2  WR=97.5%**
- **Dir: ?**  •  1h trend WITH trade; RSI<20 extreme oversold; session=asia  •  AVOID when zscore -3 to -2 deep oversold

### W04.  `T4=T4a AND RSI=RSI0 AND session_bucket=asia`
- Raw: n=127  W=118/L=9  WR=92.9%
- Refine: exclude ZS=ZS1 drops 7/9 losers (78%)
- **Final: n=79  W=77/L=2  WR=97.5%**
- **Dir: ?**  •  4h trend WITH trade; RSI<20 extreme oversold; session=asia  •  AVOID when zscore -3 to -2 deep oversold

### W05.  `RSI=RSI0 AND direction_exec=short AND session_bucket=asia`
- Raw: n=127  W=118/L=9  WR=92.9%
- Refine: exclude ZS=ZS1 drops 7/9 losers (78%)
- **Final: n=79  W=77/L=2  WR=97.5%**
- **Dir: SHORT**  •  RSI<20 extreme oversold; session=asia  •  AVOID when zscore -3 to -2 deep oversold

### W06.  `H20=H20d AND H60=H60e AND RSI=RSI0 AND session_bucket=asia`
- Raw: n=127  W=118/L=9  WR=92.9%
- Refine: exclude ZS=ZS1 drops 7/9 losers (78%)
- **Final: n=79  W=77/L=2  WR=97.5%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 strongly against; RSI<20 extreme oversold; session=asia  •  AVOID when zscore -3 to -2 deep oversold

### W07.  `H20=H20d AND T1=T1a AND RSI=RSI0 AND session_bucket=asia`
- Raw: n=127  W=118/L=9  WR=92.9%
- Refine: exclude ZS=ZS1 drops 7/9 losers (78%)
- **Final: n=79  W=77/L=2  WR=97.5%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend WITH trade; RSI<20 extreme oversold; session=asia  •  AVOID when zscore -3 to -2 deep oversold

### W08.  `H20=H20d AND T4=T4a AND RSI=RSI0 AND session_bucket=asia`
- Raw: n=127  W=118/L=9  WR=92.9%
- Refine: exclude ZS=ZS1 drops 7/9 losers (78%)
- **Final: n=79  W=77/L=2  WR=97.5%**
- **Dir: ?**  •  HTF20 mildly against; 4h trend WITH trade; RSI<20 extreme oversold; session=asia  •  AVOID when zscore -3 to -2 deep oversold

### W09.  `H20=H20d AND RSI=RSI0 AND direction_exec=short AND session_bucket=asia`
- Raw: n=127  W=118/L=9  WR=92.9%
- Refine: exclude ZS=ZS1 drops 7/9 losers (78%)
- **Final: n=79  W=77/L=2  WR=97.5%**
- **Dir: SHORT**  •  HTF20 mildly against; RSI<20 extreme oversold; session=asia  •  AVOID when zscore -3 to -2 deep oversold

### W10.  `H60=H60e AND T1=T1a AND RSI=RSI0 AND session_bucket=asia`
- Raw: n=127  W=118/L=9  WR=92.9%
- Refine: exclude ZS=ZS1 drops 7/9 losers (78%)
- **Final: n=79  W=77/L=2  WR=97.5%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; RSI<20 extreme oversold; session=asia  •  AVOID when zscore -3 to -2 deep oversold

### W11.  `H60=H60e AND T4=T4a AND RSI=RSI0 AND session_bucket=asia`
- Raw: n=127  W=118/L=9  WR=92.9%
- Refine: exclude ZS=ZS1 drops 7/9 losers (78%)
- **Final: n=79  W=77/L=2  WR=97.5%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; RSI<20 extreme oversold; session=asia  •  AVOID when zscore -3 to -2 deep oversold

### W12.  `H60=H60e AND RSI=RSI0 AND direction_exec=short AND session_bucket=asia`
- Raw: n=127  W=118/L=9  WR=92.9%
- Refine: exclude ZS=ZS1 drops 7/9 losers (78%)
- **Final: n=79  W=77/L=2  WR=97.5%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI<20 extreme oversold; session=asia  •  AVOID when zscore -3 to -2 deep oversold

### W13.  `T1=T1a AND T4=T4a AND RSI=RSI0 AND session_bucket=asia`
- Raw: n=127  W=118/L=9  WR=92.9%
- Refine: exclude ZS=ZS1 drops 7/9 losers (78%)
- **Final: n=79  W=77/L=2  WR=97.5%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI<20 extreme oversold; session=asia  •  AVOID when zscore -3 to -2 deep oversold

### W14.  `T1=T1a AND RSI=RSI0 AND direction_exec=short AND session_bucket=asia`
- Raw: n=127  W=118/L=9  WR=92.9%
- Refine: exclude ZS=ZS1 drops 7/9 losers (78%)
- **Final: n=79  W=77/L=2  WR=97.5%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI<20 extreme oversold; session=asia  •  AVOID when zscore -3 to -2 deep oversold

### W15.  `T4=T4a AND RSI=RSI0 AND direction_exec=short AND session_bucket=asia`
- Raw: n=127  W=118/L=9  WR=92.9%
- Refine: exclude ZS=ZS1 drops 7/9 losers (78%)
- **Final: n=79  W=77/L=2  WR=97.5%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI<20 extreme oversold; session=asia  •  AVOID when zscore -3 to -2 deep oversold

### W16.  `H20=H20d AND BBP=BBP2 AND session_bucket=asia`
- Raw: n=92  W=81/L=11  WR=88.0%
- Refine: exclude H60=H60a drops 4/11 losers (36%)
- **Final: n=88  W=81/L=7  WR=92.0%**
- **Dir: ?**  •  HTF20 mildly against; lower third; session=asia  •  AVOID when HTF60 aligned WITH trade

### W17.  `H20=H20d AND T4=T4a AND BBP=BBP2 AND session_bucket=asia`
- Raw: n=92  W=81/L=11  WR=88.0%
- Refine: exclude H60=H60a drops 4/11 losers (36%)
- **Final: n=88  W=81/L=7  WR=92.0%**
- **Dir: ?**  •  HTF20 mildly against; 4h trend WITH trade; lower third; session=asia  •  AVOID when HTF60 aligned WITH trade

### W18.  `H20=H20d AND BBP=BBP2 AND direction_exec=short AND session_bucket=asia`
- Raw: n=92  W=81/L=11  WR=88.0%
- Refine: exclude H60=H60a drops 4/11 losers (36%)
- **Final: n=88  W=81/L=7  WR=92.0%**
- **Dir: SHORT**  •  HTF20 mildly against; lower third; session=asia  •  AVOID when HTF60 aligned WITH trade

### W19.  `H20=H20d AND T1=T1a AND BBP=BBP2 AND session_bucket=asia`
- Raw: n=91  W=81/L=10  WR=89.0%
- Refine: exclude RSI=RSI2 drops 5/10 losers (50%)
- **Final: n=76  W=71/L=5  WR=93.4%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend WITH trade; lower third; session=asia  •  AVOID when RSI 30-40 weak

### W20.  `H20=H20d AND H60=H60e AND BBP=BBP2 AND session_bucket=asia`
- Raw: n=88  W=81/L=7  WR=92.0%
- Refine: exclude RSI=RSI1 drops 3/7 losers (43%)
- **Final: n=79  W=75/L=4  WR=94.9%**
- **Dir: ?**  •  HTF20 mildly against; HTF60 strongly against; lower third; session=asia  •  AVOID when RSI 20-30 oversold

### W21.  `H20=H20d AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=79  W=70/L=9  WR=88.6%
- Refine: exclude H60=H60a drops 4/9 losers (44%)
- **Final: n=75  W=70/L=5  WR=93.3%**
- **Dir: ?**  •  HTF20 mildly against; zscore -2 to -1 oversold; session=asia  •  AVOID when HTF60 aligned WITH trade

### W22.  `H20=H20d AND T4=T4a AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=79  W=70/L=9  WR=88.6%
- Refine: exclude H60=H60a drops 4/9 losers (44%)
- **Final: n=75  W=70/L=5  WR=93.3%**
- **Dir: ?**  •  HTF20 mildly against; 4h trend WITH trade; zscore -2 to -1 oversold; session=asia  •  AVOID when HTF60 aligned WITH trade

### W23.  `H20=H20d AND BBP=BBP2 AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=79  W=70/L=9  WR=88.6%
- Refine: exclude H60=H60a drops 4/9 losers (44%)
- **Final: n=75  W=70/L=5  WR=93.3%**
- **Dir: ?**  •  HTF20 mildly against; lower third; zscore -2 to -1 oversold; session=asia  •  AVOID when HTF60 aligned WITH trade

### W24.  `H20=H20d AND ZS=ZS2 AND direction_exec=short AND session_bucket=asia`
- Raw: n=79  W=70/L=9  WR=88.6%
- Refine: exclude H60=H60a drops 4/9 losers (44%)
- **Final: n=75  W=70/L=5  WR=93.3%**
- **Dir: SHORT**  •  HTF20 mildly against; zscore -2 to -1 oversold; session=asia  •  AVOID when HTF60 aligned WITH trade

### W25.  `H20=H20d AND T1=T1a AND ZS=ZS2 AND session_bucket=asia`
- Raw: n=78  W=70/L=8  WR=89.7%
- Refine: exclude H60=H60a drops 3/8 losers (38%)
- **Final: n=75  W=70/L=5  WR=93.3%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend WITH trade; zscore -2 to -1 oversold; session=asia  •  AVOID when HTF60 aligned WITH trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60a AND direction_exec=long AND session_bucket=asia`
- Raw: n=551  W=191/L=360  WR=34.7%
- Sharpen: no sharper sub-pattern
- **Sharp: n=551  W=191/L=360  WR=34.7%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; session=asia

### L02.  `T1=T1c AND direction_exec=long AND session_bucket=asia`
- Raw: n=550  W=195/L=355  WR=35.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=550  W=195/L=355  WR=35.5%**
- **Dir: LONG**  •  1h trend AGAINST trade; session=asia

### L03.  `H60=H60a AND T1=T1c AND session_bucket=asia`
- Raw: n=538  W=185/L=353  WR=34.4%
- Sharpen: no sharper sub-pattern
- **Sharp: n=538  W=185/L=353  WR=34.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=asia

### L04.  `T4=T4c AND direction_exec=long AND session_bucket=asia`
- Raw: n=534  W=194/L=340  WR=36.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=534  W=194/L=340  WR=36.3%**
- **Dir: LONG**  •  4h trend AGAINST trade; session=asia

### L05.  `T1=T1c AND T4=T4c AND session_bucket=asia`
- Raw: n=534  W=195/L=339  WR=36.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=534  W=195/L=339  WR=36.5%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=asia

### L06.  `H60=H60a AND T1=T1c AND direction_exec=long AND session_bucket=asia`
- Raw: n=531  W=181/L=350  WR=34.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=531  W=181/L=350  WR=34.1%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=asia

### L07.  `T1=T1c AND T4=T4c AND direction_exec=long AND session_bucket=asia`
- Raw: n=517  W=183/L=334  WR=35.4%
- Sharpen: no sharper sub-pattern
- **Sharp: n=517  W=183/L=334  WR=35.4%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=asia

### L08.  `H60=H60a AND T4=T4c AND session_bucket=asia`
- Raw: n=508  W=177/L=331  WR=34.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=508  W=177/L=331  WR=34.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=asia

### L09.  `H60=H60a AND T4=T4c AND direction_exec=long AND session_bucket=asia`
- Raw: n=508  W=177/L=331  WR=34.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=508  W=177/L=331  WR=34.8%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=asia

### L10.  `H60=H60a AND T1=T1c AND T4=T4c AND session_bucket=asia`
- Raw: n=498  W=169/L=329  WR=33.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=498  W=169/L=329  WR=33.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; session=asia

### L11.  `T1=T1c AND T4=T4c AND RSI=RSI0`
- Raw: n=403  W=149/L=254  WR=37.0%
- Sharpen: sharpest is H60=H60e (58/254 of losers there)
- **Sharp: n=63  W=5/L=58  WR=7.9%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI<20 extreme oversold  •  ONLY when HTF60 strongly against

### L12.  `T1=T1c AND RSI=RSI0 AND direction_exec=long`
- Raw: n=403  W=149/L=254  WR=37.0%
- Sharpen: sharpest is H60=H60e (58/254 of losers there)
- **Sharp: n=63  W=5/L=58  WR=7.9%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI<20 extreme oversold  •  ONLY when HTF60 strongly against

### L13.  `T4=T4c AND RSI=RSI0 AND direction_exec=long`
- Raw: n=403  W=149/L=254  WR=37.0%
- Sharpen: sharpest is H60=H60e (58/254 of losers there)
- **Sharp: n=63  W=5/L=58  WR=7.9%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI<20 extreme oversold  •  ONLY when HTF60 strongly against

### L14.  `T1=T1c AND T4=T4c AND RSI=RSI0 AND direction_exec=long`
- Raw: n=403  W=149/L=254  WR=37.0%
- Sharpen: sharpest is H60=H60e (58/254 of losers there)
- **Sharp: n=63  W=5/L=58  WR=7.9%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI<20 extreme oversold  •  ONLY when HTF60 strongly against

### L15.  `T1=T1c AND BBP=BBP0 AND direction_exec=long`
- Raw: n=391  W=152/L=239  WR=38.9%
- Sharpen: sharpest is ZS=ZS0 (86/239 of losers there)
- **Sharp: n=116  W=30/L=86  WR=25.9%**
- **Dir: LONG**  •  1h trend AGAINST trade; deep below lower band  •  ONLY when zscore <-3 extreme

### L16.  `H20=H20b AND T1=T1c AND RSI=RSI0`
- Raw: n=345  W=134/L=211  WR=38.8%
- Sharpen: sharpest is H60=H60e (58/211 of losers there)
- **Sharp: n=63  W=5/L=58  WR=7.9%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend AGAINST trade; RSI<20 extreme oversold  •  ONLY when HTF60 strongly against

### L17.  `H20=H20b AND T4=T4c AND RSI=RSI0`
- Raw: n=345  W=134/L=211  WR=38.8%
- Sharpen: sharpest is H60=H60e (58/211 of losers there)
- **Sharp: n=63  W=5/L=58  WR=7.9%**
- **Dir: ?**  •  HTF20 slightly aligned; 4h trend AGAINST trade; RSI<20 extreme oversold  •  ONLY when HTF60 strongly against

### L18.  `H20=H20b AND RSI=RSI0 AND direction_exec=long`
- Raw: n=345  W=134/L=211  WR=38.8%
- Sharpen: sharpest is H60=H60e (58/211 of losers there)
- **Sharp: n=63  W=5/L=58  WR=7.9%**
- **Dir: LONG**  •  HTF20 slightly aligned; RSI<20 extreme oversold  •  ONLY when HTF60 strongly against

### L19.  `H20=H20b AND T1=T1c AND T4=T4c AND RSI=RSI0`
- Raw: n=345  W=134/L=211  WR=38.8%
- Sharpen: sharpest is H60=H60e (58/211 of losers there)
- **Sharp: n=63  W=5/L=58  WR=7.9%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI<20 extreme oversold  •  ONLY when HTF60 strongly against

### L20.  `H20=H20b AND T1=T1c AND RSI=RSI0 AND direction_exec=long`
- Raw: n=345  W=134/L=211  WR=38.8%
- Sharpen: sharpest is H60=H60e (58/211 of losers there)
- **Sharp: n=63  W=5/L=58  WR=7.9%**
- **Dir: LONG**  •  HTF20 slightly aligned; 1h trend AGAINST trade; RSI<20 extreme oversold  •  ONLY when HTF60 strongly against

### L21.  `H20=H20b AND T4=T4c AND RSI=RSI0 AND direction_exec=long`
- Raw: n=345  W=134/L=211  WR=38.8%
- Sharpen: sharpest is H60=H60e (58/211 of losers there)
- **Sharp: n=63  W=5/L=58  WR=7.9%**
- **Dir: LONG**  •  HTF20 slightly aligned; 4h trend AGAINST trade; RSI<20 extreme oversold  •  ONLY when HTF60 strongly against

### L22.  `T1=T1c AND T4=T4c AND BBP=BBP0`
- Raw: n=307  W=112/L=195  WR=36.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=307  W=112/L=195  WR=36.5%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; deep below lower band

### L23.  `T4=T4c AND BBP=BBP0 AND direction_exec=long`
- Raw: n=307  W=112/L=195  WR=36.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=307  W=112/L=195  WR=36.5%**
- **Dir: LONG**  •  4h trend AGAINST trade; deep below lower band

### L24.  `T1=T1c AND T4=T4c AND BBP=BBP0 AND direction_exec=long`
- Raw: n=307  W=112/L=195  WR=36.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=307  W=112/L=195  WR=36.5%**
- **Dir: LONG**  •  1h trend AGAINST trade; 4h trend AGAINST trade; deep below lower band

### L25.  `T1=T1c AND BBP=BBP2 AND session_bucket=asia`
- Raw: n=294  W=110/L=184  WR=37.4%
- Sharpen: no sharper sub-pattern
- **Sharp: n=294  W=110/L=184  WR=37.4%**
- **Dir: ?**  •  1h trend AGAINST trade; lower third; session=asia

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | H60e(54/45) | H60a(45/54) |
| T1 | T1a(54/46) | T1c(46/54) |
| T4 | T4a(53/46) | T4c(47/54) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(54/46) | long(46/54) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
