# GBP_CAD — R29 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_3**  (5m ATR >120%)
- **A1 = A1_2**  (1h ATR 4-8x)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50e**  (EMA50 down >0.5x)
- **ADR = ADR5**  (>110% overshoot)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **2,499**  (W=1,430 / L=1,069)  -  WR: **57.2%**

## Session distribution

- ny_close: n=696  W=418/L=278  WR=60.1%
- asia: n=565  W=320/L=245  WR=56.6%
- ny_mid: n=494  W=278/L=216  WR=56.3%
- london_open: n=284  W=156/L=128  WR=54.9%
- ny_open: n=181  W=98/L=83  WR=54.1%
- london: n=158  W=92/L=66  WR=58.2%
- off_hours: n=67  W=38/L=29  WR=56.7%
- asia_late: n=54  W=30/L=24  WR=55.6%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `BBP=BBP5 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=89  W=77/L=12  WR=86.5%
- Refine: exclude H20=H20c drops 5/12 losers (42%)
- **Final: n=84  W=77/L=7  WR=91.7%**
- **Dir: LONG**  •  just touched upper band; session=ny_close  •  AVOID when HTF20 neutral

### W02.  `BBP=BBP5 AND ZS=ZS5 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=89  W=77/L=12  WR=86.5%
- Refine: exclude H20=H20c drops 5/12 losers (42%)
- **Final: n=84  W=77/L=7  WR=91.7%**
- **Dir: LONG**  •  just touched upper band; zscore +2 to +3 deep overbought; session=ny_close  •  AVOID when HTF20 neutral

### W03.  `H20=H20b AND H60=H60d AND RSI=RSI6`
- Raw: n=75  W=67/L=8  WR=89.3%
- Refine: exclude BBP=BBP3 drops 2/8 losers (25%)
- **Final: n=70  W=64/L=6  WR=91.4%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 mildly against; RSI 70-80 overbought  •  AVOID when middle of band

### W04.  `H20=H20b AND T1=T1a AND RSI=RSI6`
- Raw: n=75  W=67/L=8  WR=89.3%
- Refine: exclude BBP=BBP3 drops 2/8 losers (25%)
- **Final: n=70  W=64/L=6  WR=91.4%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend WITH trade; RSI 70-80 overbought  •  AVOID when middle of band

### W05.  `H20=H20b AND T4=T4a AND RSI=RSI6`
- Raw: n=75  W=67/L=8  WR=89.3%
- Refine: exclude BBP=BBP3 drops 2/8 losers (25%)
- **Final: n=70  W=64/L=6  WR=91.4%**
- **Dir: ?**  •  HTF20 slightly aligned; 4h trend WITH trade; RSI 70-80 overbought  •  AVOID when middle of band

### W06.  `H20=H20b AND RSI=RSI6 AND direction_exec=long`
- Raw: n=75  W=67/L=8  WR=89.3%
- Refine: exclude BBP=BBP3 drops 2/8 losers (25%)
- **Final: n=70  W=64/L=6  WR=91.4%**
- **Dir: LONG**  •  HTF20 slightly aligned; RSI 70-80 overbought  •  AVOID when middle of band

### W07.  `H60=H60d AND T1=T1a AND RSI=RSI6`
- Raw: n=75  W=67/L=8  WR=89.3%
- Refine: exclude BBP=BBP3 drops 2/8 losers (25%)
- **Final: n=70  W=64/L=6  WR=91.4%**
- **Dir: ?**  •  HTF60 mildly against; 1h trend WITH trade; RSI 70-80 overbought  •  AVOID when middle of band

### W08.  `H60=H60d AND T4=T4a AND RSI=RSI6`
- Raw: n=75  W=67/L=8  WR=89.3%
- Refine: exclude BBP=BBP3 drops 2/8 losers (25%)
- **Final: n=70  W=64/L=6  WR=91.4%**
- **Dir: ?**  •  HTF60 mildly against; 4h trend WITH trade; RSI 70-80 overbought  •  AVOID when middle of band

### W09.  `H60=H60d AND RSI=RSI6 AND direction_exec=long`
- Raw: n=75  W=67/L=8  WR=89.3%
- Refine: exclude BBP=BBP3 drops 2/8 losers (25%)
- **Final: n=70  W=64/L=6  WR=91.4%**
- **Dir: LONG**  •  HTF60 mildly against; RSI 70-80 overbought  •  AVOID when middle of band

### W10.  `H20=H20b AND H60=H60d AND T1=T1a AND RSI=RSI6`
- Raw: n=75  W=67/L=8  WR=89.3%
- Refine: exclude BBP=BBP3 drops 2/8 losers (25%)
- **Final: n=70  W=64/L=6  WR=91.4%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 mildly against; 1h trend WITH trade; RSI 70-80 overbought  •  AVOID when middle of band

### W11.  `H20=H20b AND H60=H60d AND T4=T4a AND RSI=RSI6`
- Raw: n=75  W=67/L=8  WR=89.3%
- Refine: exclude BBP=BBP3 drops 2/8 losers (25%)
- **Final: n=70  W=64/L=6  WR=91.4%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 mildly against; 4h trend WITH trade; RSI 70-80 overbought  •  AVOID when middle of band

### W12.  `H20=H20b AND H60=H60d AND RSI=RSI6 AND direction_exec=long`
- Raw: n=75  W=67/L=8  WR=89.3%
- Refine: exclude BBP=BBP3 drops 2/8 losers (25%)
- **Final: n=70  W=64/L=6  WR=91.4%**
- **Dir: LONG**  •  HTF20 slightly aligned; HTF60 mildly against; RSI 70-80 overbought  •  AVOID when middle of band

### W13.  `H20=H20b AND T1=T1a AND T4=T4a AND RSI=RSI6`
- Raw: n=75  W=67/L=8  WR=89.3%
- Refine: exclude BBP=BBP3 drops 2/8 losers (25%)
- **Final: n=70  W=64/L=6  WR=91.4%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend WITH trade; 4h trend WITH trade; RSI 70-80 overbought  •  AVOID when middle of band

### W14.  `H20=H20b AND T1=T1a AND RSI=RSI6 AND direction_exec=long`
- Raw: n=75  W=67/L=8  WR=89.3%
- Refine: exclude BBP=BBP3 drops 2/8 losers (25%)
- **Final: n=70  W=64/L=6  WR=91.4%**
- **Dir: LONG**  •  HTF20 slightly aligned; 1h trend WITH trade; RSI 70-80 overbought  •  AVOID when middle of band

### W15.  `H20=H20b AND T4=T4a AND RSI=RSI6 AND direction_exec=long`
- Raw: n=75  W=67/L=8  WR=89.3%
- Refine: exclude BBP=BBP3 drops 2/8 losers (25%)
- **Final: n=70  W=64/L=6  WR=91.4%**
- **Dir: LONG**  •  HTF20 slightly aligned; 4h trend WITH trade; RSI 70-80 overbought  •  AVOID when middle of band

### W16.  `H60=H60d AND T1=T1a AND T4=T4a AND RSI=RSI6`
- Raw: n=75  W=67/L=8  WR=89.3%
- Refine: exclude BBP=BBP3 drops 2/8 losers (25%)
- **Final: n=70  W=64/L=6  WR=91.4%**
- **Dir: ?**  •  HTF60 mildly against; 1h trend WITH trade; 4h trend WITH trade; RSI 70-80 overbought  •  AVOID when middle of band

### W17.  `H60=H60d AND T1=T1a AND RSI=RSI6 AND direction_exec=long`
- Raw: n=75  W=67/L=8  WR=89.3%
- Refine: exclude BBP=BBP3 drops 2/8 losers (25%)
- **Final: n=70  W=64/L=6  WR=91.4%**
- **Dir: LONG**  •  HTF60 mildly against; 1h trend WITH trade; RSI 70-80 overbought  •  AVOID when middle of band

### W18.  `H60=H60d AND T4=T4a AND RSI=RSI6 AND direction_exec=long`
- Raw: n=75  W=67/L=8  WR=89.3%
- Refine: exclude BBP=BBP3 drops 2/8 losers (25%)
- **Final: n=70  W=64/L=6  WR=91.4%**
- **Dir: LONG**  •  HTF60 mildly against; 4h trend WITH trade; RSI 70-80 overbought  •  AVOID when middle of band

### W19.  `T1=T1a AND RSI=RSI6 AND session_bucket=ny_close`
- Raw: n=71  W=61/L=10  WR=85.9%
- Refine: exclude BBP=BBP4 drops 10/10 losers (100%)
- **Final: n=25  W=25/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; RSI 70-80 overbought; session=ny_close  •  AVOID when upper third

### W20.  `RSI=RSI6 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=71  W=61/L=10  WR=85.9%
- Refine: exclude BBP=BBP4 drops 10/10 losers (100%)
- **Final: n=25  W=25/L=0  WR=100.0%**
- **Dir: LONG**  •  RSI 70-80 overbought; session=ny_close  •  AVOID when upper third

### W21.  `T1=T1a AND RSI=RSI6 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=71  W=61/L=10  WR=85.9%
- Refine: exclude BBP=BBP4 drops 10/10 losers (100%)
- **Final: n=25  W=25/L=0  WR=100.0%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 70-80 overbought; session=ny_close  •  AVOID when upper third

### W22.  `T4=T4c AND BBP=BBP5 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=63  W=56/L=7  WR=88.9%
- Refine: exclude T1=T1a drops 7/7 losers (100%)
- **Final: n=36  W=36/L=0  WR=100.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; just touched upper band; session=ny_close  •  AVOID when 1h trend WITH trade

### W23.  `H20=H20b AND RSI=RSI6 AND session_bucket=ny_close`
- Raw: n=60  W=54/L=6  WR=90.0%
- Refine: exclude BBP=BBP4 drops 6/6 losers (100%)
- **Final: n=25  W=25/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 slightly aligned; RSI 70-80 overbought; session=ny_close  •  AVOID when upper third

### W24.  `H60=H60d AND RSI=RSI6 AND session_bucket=ny_close`
- Raw: n=60  W=54/L=6  WR=90.0%
- Refine: exclude BBP=BBP4 drops 6/6 losers (100%)
- **Final: n=25  W=25/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 mildly against; RSI 70-80 overbought; session=ny_close  •  AVOID when upper third

### W25.  `H20=H20b AND H60=H60d AND RSI=RSI6 AND session_bucket=ny_close`
- Raw: n=60  W=54/L=6  WR=90.0%
- Refine: exclude BBP=BBP4 drops 6/6 losers (100%)
- **Final: n=25  W=25/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 mildly against; RSI 70-80 overbought; session=ny_close  •  AVOID when upper third

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1c AND direction_exec=long AND session_bucket=asia`
- Raw: n=199  W=79/L=120  WR=39.7%
- Sharpen: sharpest is ZS=ZS2 (58/120 of losers there)
- **Sharp: n=77  W=19/L=58  WR=24.7%**
- **Dir: LONG**  •  1h trend AGAINST trade; session=asia  •  ONLY when zscore -2 to -1 oversold

### L02.  `T1=T1c AND RSI=RSI6 AND direction_exec=short`
- Raw: n=181  W=71/L=110  WR=39.2%
- Sharpen: sharpest is H20=H20d (53/110 of losers there)
- **Sharp: n=54  W=1/L=53  WR=1.9%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when HTF20 mildly against

### L03.  `T1=T1c AND T4=T4c AND RSI=RSI6`
- Raw: n=169  W=66/L=103  WR=39.1%
- Sharpen: sharpest is H20=H20d (53/103 of losers there)
- **Sharp: n=54  W=1/L=53  WR=1.9%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when HTF20 mildly against

### L04.  `T4=T4c AND RSI=RSI6 AND direction_exec=short`
- Raw: n=169  W=66/L=103  WR=39.1%
- Sharpen: sharpest is H20=H20d (53/103 of losers there)
- **Sharp: n=54  W=1/L=53  WR=1.9%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when HTF20 mildly against

### L05.  `T1=T1c AND T4=T4c AND RSI=RSI6 AND direction_exec=short`
- Raw: n=169  W=66/L=103  WR=39.1%
- Sharpen: sharpest is H20=H20d (53/103 of losers there)
- **Sharp: n=54  W=1/L=53  WR=1.9%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 70-80 overbought  •  ONLY when HTF20 mildly against

### L06.  `H20=H20d AND T1=T1c AND T4=T4c`
- Raw: n=163  W=61/L=102  WR=37.4%
- Sharpen: sharpest is RSI=RSI6 (53/102 of losers there)
- **Sharp: n=54  W=1/L=53  WR=1.9%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when RSI 70-80 overbought

### L07.  `H20=H20a AND T1=T1a AND RSI=RSI4 AND direction_exec=short`
- Raw: n=156  W=59/L=97  WR=37.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=156  W=59/L=97  WR=37.8%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 50-60 upper neutral

### L08.  `H60=H60a AND T1=T1a AND RSI=RSI4 AND direction_exec=short`
- Raw: n=156  W=59/L=97  WR=37.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=156  W=59/L=97  WR=37.8%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 50-60 upper neutral

### L09.  `T1=T1a AND T4=T4a AND RSI=RSI4 AND direction_exec=short`
- Raw: n=156  W=59/L=97  WR=37.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=156  W=59/L=97  WR=37.8%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral

### L10.  `T1=T1c AND T4=T4c AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=150  W=60/L=90  WR=40.0%
- Sharpen: sharpest is RSI=RSI6 (43/90 of losers there)
- **Sharp: n=44  W=1/L=43  WR=2.3%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; session=ny_close  •  ONLY when RSI 70-80 overbought

### L11.  `H60=H60b AND T4=T4c AND direction_exec=short`
- Raw: n=130  W=45/L=85  WR=34.6%
- Sharpen: sharpest is RSI=RSI6 (53/85 of losers there)
- **Sharp: n=54  W=1/L=53  WR=1.9%**
- **Dir: SHORT**  •  HTF60 slightly aligned; 4h trend AGAINST trade  •  ONLY when RSI 70-80 overbought

### L12.  `H20=H20e AND H60=H60e AND RSI=RSI1`
- Raw: n=123  W=47/L=76  WR=38.2%
- Sharpen: sharpest is session_bucket=asia (35/76 of losers there)
- **Sharp: n=45  W=10/L=35  WR=22.2%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 20-30 oversold  •  ONLY when session=asia

### L13.  `H20=H20e AND T1=T1c AND RSI=RSI1`
- Raw: n=123  W=47/L=76  WR=38.2%
- Sharpen: sharpest is session_bucket=asia (35/76 of losers there)
- **Sharp: n=45  W=10/L=35  WR=22.2%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when session=asia

### L14.  `H20=H20e AND T4=T4c AND RSI=RSI1`
- Raw: n=123  W=47/L=76  WR=38.2%
- Sharpen: sharpest is session_bucket=asia (35/76 of losers there)
- **Sharp: n=45  W=10/L=35  WR=22.2%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when session=asia

### L15.  `H20=H20e AND RSI=RSI1 AND direction_exec=long`
- Raw: n=123  W=47/L=76  WR=38.2%
- Sharpen: sharpest is session_bucket=asia (35/76 of losers there)
- **Sharp: n=45  W=10/L=35  WR=22.2%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 20-30 oversold  •  ONLY when session=asia

### L16.  `H60=H60e AND T1=T1c AND RSI=RSI1`
- Raw: n=123  W=47/L=76  WR=38.2%
- Sharpen: sharpest is session_bucket=asia (35/76 of losers there)
- **Sharp: n=45  W=10/L=35  WR=22.2%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when session=asia

### L17.  `H60=H60e AND T4=T4c AND RSI=RSI1`
- Raw: n=123  W=47/L=76  WR=38.2%
- Sharpen: sharpest is session_bucket=asia (35/76 of losers there)
- **Sharp: n=45  W=10/L=35  WR=22.2%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when session=asia

### L18.  `H60=H60e AND RSI=RSI1 AND direction_exec=long`
- Raw: n=123  W=47/L=76  WR=38.2%
- Sharpen: sharpest is session_bucket=asia (35/76 of losers there)
- **Sharp: n=45  W=10/L=35  WR=22.2%**
- **Dir: LONG**  •  HTF60 strongly against; RSI 20-30 oversold  •  ONLY when session=asia

### L19.  `H20=H20e AND H60=H60e AND T1=T1c AND RSI=RSI1`
- Raw: n=123  W=47/L=76  WR=38.2%
- Sharpen: sharpest is session_bucket=asia (35/76 of losers there)
- **Sharp: n=45  W=10/L=35  WR=22.2%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when session=asia

### L20.  `H20=H20e AND H60=H60e AND T4=T4c AND RSI=RSI1`
- Raw: n=123  W=47/L=76  WR=38.2%
- Sharpen: sharpest is session_bucket=asia (35/76 of losers there)
- **Sharp: n=45  W=10/L=35  WR=22.2%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when session=asia

### L21.  `H20=H20e AND H60=H60e AND RSI=RSI1 AND direction_exec=long`
- Raw: n=123  W=47/L=76  WR=38.2%
- Sharpen: sharpest is session_bucket=asia (35/76 of losers there)
- **Sharp: n=45  W=10/L=35  WR=22.2%**
- **Dir: LONG**  •  HTF20 strongly against; HTF60 strongly against; RSI 20-30 oversold  •  ONLY when session=asia

### L22.  `H20=H20e AND T1=T1c AND T4=T4c AND RSI=RSI1`
- Raw: n=123  W=47/L=76  WR=38.2%
- Sharpen: sharpest is session_bucket=asia (35/76 of losers there)
- **Sharp: n=45  W=10/L=35  WR=22.2%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when session=asia

### L23.  `H20=H20e AND T1=T1c AND RSI=RSI1 AND direction_exec=long`
- Raw: n=123  W=47/L=76  WR=38.2%
- Sharpen: sharpest is session_bucket=asia (35/76 of losers there)
- **Sharp: n=45  W=10/L=35  WR=22.2%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when session=asia

### L24.  `H20=H20e AND T4=T4c AND RSI=RSI1 AND direction_exec=long`
- Raw: n=123  W=47/L=76  WR=38.2%
- Sharpen: sharpest is session_bucket=asia (35/76 of losers there)
- **Sharp: n=45  W=10/L=35  WR=22.2%**
- **Dir: LONG**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when session=asia

### L25.  `H60=H60e AND T1=T1c AND T4=T4c AND RSI=RSI1`
- Raw: n=123  W=47/L=76  WR=38.2%
- Sharpen: sharpest is session_bucket=asia (35/76 of losers there)
- **Sharp: n=45  W=10/L=35  WR=22.2%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; RSI 20-30 oversold  •  ONLY when session=asia

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | H20d(5/10) |
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
