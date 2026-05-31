# AUD_NZD — R27 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR3**  (60-90%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **1,473**  (W=941 / L=532)  -  WR: **63.9%**

## Session distribution

- asia: n=636  W=415/L=221  WR=65.3%
- london_open: n=276  W=182/L=94  WR=65.9%
- ny_mid: n=177  W=117/L=60  WR=66.1%
- asia_late: n=133  W=82/L=51  WR=61.7%
- london: n=99  W=60/L=39  WR=60.6%
- ny_close: n=58  W=34/L=24  WR=58.6%
- ny_open: n=54  W=30/L=24  WR=55.6%
- off_hours: n=40  W=21/L=19  WR=52.5%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60e AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=152  W=133/L=19  WR=87.5%
- Refine: exclude H20=H20e drops 11/19 losers (58%)
- **Final: n=113  W=105/L=8  WR=92.9%**
- **Dir: ?**  •  HTF60 strongly against; RSI 30-40 weak; session=asia  •  AVOID when HTF20 strongly against

### W02.  `T1=T1a AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=152  W=133/L=19  WR=87.5%
- Refine: exclude H20=H20e drops 11/19 losers (58%)
- **Final: n=113  W=105/L=8  WR=92.9%**
- **Dir: ?**  •  1h trend WITH trade; RSI 30-40 weak; session=asia  •  AVOID when HTF20 strongly against

### W03.  `RSI=RSI2 AND direction_exec=short AND session_bucket=asia`
- Raw: n=152  W=133/L=19  WR=87.5%
- Refine: exclude H20=H20e drops 11/19 losers (58%)
- **Final: n=113  W=105/L=8  WR=92.9%**
- **Dir: SHORT**  •  RSI 30-40 weak; session=asia  •  AVOID when HTF20 strongly against

### W04.  `H60=H60e AND T1=T1a AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=152  W=133/L=19  WR=87.5%
- Refine: exclude H20=H20e drops 11/19 losers (58%)
- **Final: n=113  W=105/L=8  WR=92.9%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; RSI 30-40 weak; session=asia  •  AVOID when HTF20 strongly against

### W05.  `H60=H60e AND RSI=RSI2 AND direction_exec=short AND session_bucket=asia`
- Raw: n=152  W=133/L=19  WR=87.5%
- Refine: exclude H20=H20e drops 11/19 losers (58%)
- **Final: n=113  W=105/L=8  WR=92.9%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 30-40 weak; session=asia  •  AVOID when HTF20 strongly against

### W06.  `T1=T1a AND RSI=RSI2 AND direction_exec=short AND session_bucket=asia`
- Raw: n=152  W=133/L=19  WR=87.5%
- Refine: exclude H20=H20e drops 11/19 losers (58%)
- **Final: n=113  W=105/L=8  WR=92.9%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 30-40 weak; session=asia  •  AVOID when HTF20 strongly against

### W07.  `H60=H60e AND T4=T4a AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=134  W=115/L=19  WR=85.8%
- Refine: exclude H20=H20e drops 11/19 losers (58%)
- **Final: n=105  W=97/L=8  WR=92.4%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; RSI 30-40 weak; session=asia  •  AVOID when HTF20 strongly against

### W08.  `T1=T1a AND T4=T4a AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=134  W=115/L=19  WR=85.8%
- Refine: exclude H20=H20e drops 11/19 losers (58%)
- **Final: n=105  W=97/L=8  WR=92.4%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 30-40 weak; session=asia  •  AVOID when HTF20 strongly against

### W09.  `T4=T4a AND RSI=RSI2 AND direction_exec=short AND session_bucket=asia`
- Raw: n=134  W=115/L=19  WR=85.8%
- Refine: exclude H20=H20e drops 11/19 losers (58%)
- **Final: n=105  W=97/L=8  WR=92.4%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 30-40 weak; session=asia  •  AVOID when HTF20 strongly against

### W10.  `H20=H20c AND H60=H60e AND session_bucket=asia`
- Raw: n=81  W=76/L=5  WR=93.8%
- Refine: exclude ZS=ZS3 drops 2/5 losers (40%)
- **Final: n=73  W=70/L=3  WR=95.9%**
- **Dir: ?**  •  HTF20 neutral; HTF60 strongly against; session=asia  •  AVOID when zscore -1 to +1 neutral

### W11.  `H20=H20c AND T1=T1a AND session_bucket=asia`
- Raw: n=81  W=76/L=5  WR=93.8%
- Refine: exclude ZS=ZS3 drops 2/5 losers (40%)
- **Final: n=73  W=70/L=3  WR=95.9%**
- **Dir: ?**  •  HTF20 neutral; 1h trend WITH trade; session=asia  •  AVOID when zscore -1 to +1 neutral

### W12.  `H20=H20c AND T4=T4a AND session_bucket=asia`
- Raw: n=81  W=76/L=5  WR=93.8%
- Refine: exclude ZS=ZS3 drops 2/5 losers (40%)
- **Final: n=73  W=70/L=3  WR=95.9%**
- **Dir: ?**  •  HTF20 neutral; 4h trend WITH trade; session=asia  •  AVOID when zscore -1 to +1 neutral

### W13.  `H20=H20c AND direction_exec=short AND session_bucket=asia`
- Raw: n=81  W=76/L=5  WR=93.8%
- Refine: exclude ZS=ZS3 drops 2/5 losers (40%)
- **Final: n=73  W=70/L=3  WR=95.9%**
- **Dir: SHORT**  •  HTF20 neutral; session=asia  •  AVOID when zscore -1 to +1 neutral

### W14.  `H20=H20c AND H60=H60e AND T1=T1a AND session_bucket=asia`
- Raw: n=81  W=76/L=5  WR=93.8%
- Refine: exclude ZS=ZS3 drops 2/5 losers (40%)
- **Final: n=73  W=70/L=3  WR=95.9%**
- **Dir: ?**  •  HTF20 neutral; HTF60 strongly against; 1h trend WITH trade; session=asia  •  AVOID when zscore -1 to +1 neutral

### W15.  `H20=H20c AND H60=H60e AND T4=T4a AND session_bucket=asia`
- Raw: n=81  W=76/L=5  WR=93.8%
- Refine: exclude ZS=ZS3 drops 2/5 losers (40%)
- **Final: n=73  W=70/L=3  WR=95.9%**
- **Dir: ?**  •  HTF20 neutral; HTF60 strongly against; 4h trend WITH trade; session=asia  •  AVOID when zscore -1 to +1 neutral

### W16.  `H20=H20c AND H60=H60e AND direction_exec=short AND session_bucket=asia`
- Raw: n=81  W=76/L=5  WR=93.8%
- Refine: exclude ZS=ZS3 drops 2/5 losers (40%)
- **Final: n=73  W=70/L=3  WR=95.9%**
- **Dir: SHORT**  •  HTF20 neutral; HTF60 strongly against; session=asia  •  AVOID when zscore -1 to +1 neutral

### W17.  `H20=H20c AND T1=T1a AND T4=T4a AND session_bucket=asia`
- Raw: n=81  W=76/L=5  WR=93.8%
- Refine: exclude ZS=ZS3 drops 2/5 losers (40%)
- **Final: n=73  W=70/L=3  WR=95.9%**
- **Dir: ?**  •  HTF20 neutral; 1h trend WITH trade; 4h trend WITH trade; session=asia  •  AVOID when zscore -1 to +1 neutral

### W18.  `H20=H20c AND T1=T1a AND direction_exec=short AND session_bucket=asia`
- Raw: n=81  W=76/L=5  WR=93.8%
- Refine: exclude ZS=ZS3 drops 2/5 losers (40%)
- **Final: n=73  W=70/L=3  WR=95.9%**
- **Dir: SHORT**  •  HTF20 neutral; 1h trend WITH trade; session=asia  •  AVOID when zscore -1 to +1 neutral

### W19.  `H20=H20c AND T4=T4a AND direction_exec=short AND session_bucket=asia`
- Raw: n=81  W=76/L=5  WR=93.8%
- Refine: exclude ZS=ZS3 drops 2/5 losers (40%)
- **Final: n=73  W=70/L=3  WR=95.9%**
- **Dir: SHORT**  •  HTF20 neutral; 4h trend WITH trade; session=asia  •  AVOID when zscore -1 to +1 neutral

### W20.  `H20=H20c AND H60=H60e AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=69  W=64/L=5  WR=92.8%
- Refine: exclude ZS=ZS3 drops 2/5 losers (40%)
- **Final: n=61  W=58/L=3  WR=95.1%**
- **Dir: ?**  •  HTF20 neutral; HTF60 strongly against; RSI 30-40 weak; session=asia  •  AVOID when zscore -1 to +1 neutral

### W21.  `H20=H20c AND T1=T1a AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=69  W=64/L=5  WR=92.8%
- Refine: exclude ZS=ZS3 drops 2/5 losers (40%)
- **Final: n=61  W=58/L=3  WR=95.1%**
- **Dir: ?**  •  HTF20 neutral; 1h trend WITH trade; RSI 30-40 weak; session=asia  •  AVOID when zscore -1 to +1 neutral

### W22.  `H20=H20c AND T4=T4a AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=69  W=64/L=5  WR=92.8%
- Refine: exclude ZS=ZS3 drops 2/5 losers (40%)
- **Final: n=61  W=58/L=3  WR=95.1%**
- **Dir: ?**  •  HTF20 neutral; 4h trend WITH trade; RSI 30-40 weak; session=asia  •  AVOID when zscore -1 to +1 neutral

### W23.  `H20=H20c AND RSI=RSI2 AND direction_exec=short AND session_bucket=asia`
- Raw: n=69  W=64/L=5  WR=92.8%
- Refine: exclude ZS=ZS3 drops 2/5 losers (40%)
- **Final: n=61  W=58/L=3  WR=95.1%**
- **Dir: SHORT**  •  HTF20 neutral; RSI 30-40 weak; session=asia  •  AVOID when zscore -1 to +1 neutral

### W24.  `H60=H60e AND RSI=RSI2 AND session_bucket=asia_late`
- Raw: n=68  W=58/L=10  WR=85.3%
- Refine: exclude T4=T4a drops 10/10 losers (100%)
- **Final: n=33  W=33/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; RSI 30-40 weak; session=asia_late  •  AVOID when 4h trend WITH trade

### W25.  `T1=T1a AND RSI=RSI2 AND session_bucket=asia_late`
- Raw: n=68  W=58/L=10  WR=85.3%
- Refine: exclude T4=T4a drops 10/10 losers (100%)
- **Final: n=33  W=33/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; RSI 30-40 weak; session=asia_late  •  AVOID when 4h trend WITH trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60a AND T1=T1c AND session_bucket=asia_late`
- Raw: n=63  W=23/L=40  WR=36.5%
- Sharpen: sharpest is H20=H20a (18/40 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=asia_late  •  ONLY when HTF20 aligned WITH trade

### L02.  `H60=H60a AND direction_exec=long AND session_bucket=asia_late`
- Raw: n=63  W=23/L=40  WR=36.5%
- Sharpen: sharpest is H20=H20a (18/40 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; session=asia_late  •  ONLY when HTF20 aligned WITH trade

### L03.  `T1=T1c AND direction_exec=long AND session_bucket=asia_late`
- Raw: n=63  W=23/L=40  WR=36.5%
- Sharpen: sharpest is H20=H20a (18/40 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; session=asia_late  •  ONLY when HTF20 aligned WITH trade

### L04.  `H60=H60a AND T1=T1c AND direction_exec=long AND session_bucket=asia_late`
- Raw: n=63  W=23/L=40  WR=36.5%
- Sharpen: sharpest is H20=H20a (18/40 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=asia_late  •  ONLY when HTF20 aligned WITH trade

### L05.  `H20=H20c AND H60=H60a AND session_bucket=asia`
- Raw: n=62  W=21/L=41  WR=33.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=62  W=21/L=41  WR=33.9%**
- **Dir: ?**  •  HTF20 neutral; HTF60 aligned WITH trade; session=asia

### L06.  `H20=H20c AND T1=T1c AND session_bucket=asia`
- Raw: n=62  W=21/L=41  WR=33.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=62  W=21/L=41  WR=33.9%**
- **Dir: ?**  •  HTF20 neutral; 1h trend AGAINST trade; session=asia

### L07.  `H20=H20c AND T4=T4c AND session_bucket=asia`
- Raw: n=62  W=21/L=41  WR=33.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=62  W=21/L=41  WR=33.9%**
- **Dir: ?**  •  HTF20 neutral; 4h trend AGAINST trade; session=asia

### L08.  `H20=H20c AND direction_exec=long AND session_bucket=asia`
- Raw: n=62  W=21/L=41  WR=33.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=62  W=21/L=41  WR=33.9%**
- **Dir: LONG**  •  HTF20 neutral; session=asia

### L09.  `H20=H20c AND H60=H60a AND T1=T1c AND session_bucket=asia`
- Raw: n=62  W=21/L=41  WR=33.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=62  W=21/L=41  WR=33.9%**
- **Dir: ?**  •  HTF20 neutral; HTF60 aligned WITH trade; 1h trend AGAINST trade; session=asia

### L10.  `H20=H20c AND H60=H60a AND T4=T4c AND session_bucket=asia`
- Raw: n=62  W=21/L=41  WR=33.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=62  W=21/L=41  WR=33.9%**
- **Dir: ?**  •  HTF20 neutral; HTF60 aligned WITH trade; 4h trend AGAINST trade; session=asia

### L11.  `H20=H20c AND H60=H60a AND direction_exec=long AND session_bucket=asia`
- Raw: n=62  W=21/L=41  WR=33.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=62  W=21/L=41  WR=33.9%**
- **Dir: LONG**  •  HTF20 neutral; HTF60 aligned WITH trade; session=asia

### L12.  `H20=H20c AND T1=T1c AND T4=T4c AND session_bucket=asia`
- Raw: n=62  W=21/L=41  WR=33.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=62  W=21/L=41  WR=33.9%**
- **Dir: ?**  •  HTF20 neutral; 1h trend AGAINST trade; 4h trend AGAINST trade; session=asia

### L13.  `H20=H20c AND T1=T1c AND direction_exec=long AND session_bucket=asia`
- Raw: n=62  W=21/L=41  WR=33.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=62  W=21/L=41  WR=33.9%**
- **Dir: LONG**  •  HTF20 neutral; 1h trend AGAINST trade; session=asia

### L14.  `H20=H20c AND T4=T4c AND direction_exec=long AND session_bucket=asia`
- Raw: n=62  W=21/L=41  WR=33.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=62  W=21/L=41  WR=33.9%**
- **Dir: LONG**  •  HTF20 neutral; 4h trend AGAINST trade; session=asia

### L15.  `H60=H60a AND RSI=RSI2 AND session_bucket=asia_late`
- Raw: n=57  W=19/L=38  WR=33.3%
- Sharpen: sharpest is H20=H20a (18/38 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 30-40 weak; session=asia_late  •  ONLY when HTF20 aligned WITH trade

### L16.  `T1=T1c AND RSI=RSI2 AND session_bucket=asia_late`
- Raw: n=57  W=19/L=38  WR=33.3%
- Sharpen: sharpest is H20=H20a (18/38 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 30-40 weak; session=asia_late  •  ONLY when HTF20 aligned WITH trade

### L17.  `RSI=RSI2 AND direction_exec=long AND session_bucket=asia_late`
- Raw: n=57  W=19/L=38  WR=33.3%
- Sharpen: sharpest is H20=H20a (18/38 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: LONG**  •  RSI 30-40 weak; session=asia_late  •  ONLY when HTF20 aligned WITH trade

### L18.  `H60=H60a AND T1=T1c AND RSI=RSI2 AND session_bucket=asia_late`
- Raw: n=57  W=19/L=38  WR=33.3%
- Sharpen: sharpest is H20=H20a (18/38 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 30-40 weak; session=asia_late  •  ONLY when HTF20 aligned WITH trade

### L19.  `H60=H60a AND RSI=RSI2 AND direction_exec=long AND session_bucket=asia_late`
- Raw: n=57  W=19/L=38  WR=33.3%
- Sharpen: sharpest is H20=H20a (18/38 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 30-40 weak; session=asia_late  •  ONLY when HTF20 aligned WITH trade

### L20.  `T1=T1c AND RSI=RSI2 AND direction_exec=long AND session_bucket=asia_late`
- Raw: n=57  W=19/L=38  WR=33.3%
- Sharpen: sharpest is H20=H20a (18/38 of losers there)
- **Sharp: n=18  W=0/L=18  WR=0.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 30-40 weak; session=asia_late  •  ONLY when HTF20 aligned WITH trade

### L21.  `H20=H20c AND H60=H60a AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=57  W=21/L=36  WR=36.8%
- Sharpen: sharpest is BBP=BBP0 (6/36 of losers there)
- **Sharp: n=6  W=0/L=6  WR=0.0%**
- **Dir: ?**  •  HTF20 neutral; HTF60 aligned WITH trade; RSI 30-40 weak; session=asia  •  ONLY when deep below lower band

### L22.  `H20=H20c AND T1=T1c AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=57  W=21/L=36  WR=36.8%
- Sharpen: sharpest is BBP=BBP0 (6/36 of losers there)
- **Sharp: n=6  W=0/L=6  WR=0.0%**
- **Dir: ?**  •  HTF20 neutral; 1h trend AGAINST trade; RSI 30-40 weak; session=asia  •  ONLY when deep below lower band

### L23.  `H20=H20c AND T4=T4c AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=57  W=21/L=36  WR=36.8%
- Sharpen: sharpest is BBP=BBP0 (6/36 of losers there)
- **Sharp: n=6  W=0/L=6  WR=0.0%**
- **Dir: ?**  •  HTF20 neutral; 4h trend AGAINST trade; RSI 30-40 weak; session=asia  •  ONLY when deep below lower band

### L24.  `H20=H20c AND RSI=RSI2 AND direction_exec=long AND session_bucket=asia`
- Raw: n=57  W=21/L=36  WR=36.8%
- Sharpen: sharpest is BBP=BBP0 (6/36 of losers there)
- **Sharp: n=6  W=0/L=6  WR=0.0%**
- **Dir: LONG**  •  HTF20 neutral; RSI 30-40 weak; session=asia  •  ONLY when deep below lower band

### L25.  `H60=H60a AND RSI=RSI2 AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=49  W=18/L=31  WR=36.7%
- Sharpen: sharpest is H20=H20d (11/31 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 30-40 weak; zscore -3 to -2 deep oversold; session=asia  •  ONLY when HTF20 mildly against

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | H20a(28/33) |
| H60 | H60e(51/44) | H60a(49/56) |
| T1 | T1a(51/44) | T1c(49/56) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(51/44) | long(49/56) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
