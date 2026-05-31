# GBP_CHF — R35 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50e**  (EMA50 down >0.5x)
- **ADR = ADR5**  (>110% overshoot)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **1,703**  (W=1,030 / L=673)  -  WR: **60.5%**

## Session distribution

- ny_mid: n=443  W=268/L=175  WR=60.5%
- asia: n=393  W=245/L=148  WR=62.3%
- ny_open: n=299  W=181/L=118  WR=60.5%
- ny_close: n=286  W=169/L=117  WR=59.1%
- london_open: n=133  W=79/L=54  WR=59.4%
- london: n=74  W=47/L=27  WR=63.5%
- off_hours: n=39  W=22/L=17  WR=56.4%
- asia_late: n=36  W=19/L=17  WR=52.8%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1a AND RSI=RSI1 AND session_bucket=ny_open`
- Raw: n=129  W=110/L=19  WR=85.3%
- Refine: exclude H60=H60e drops 16/19 losers (84%)
- **Final: n=99  W=96/L=3  WR=97.0%**
- **Dir: ?**  •  1h trend WITH trade; RSI 20-30 oversold; session=ny_open  •  AVOID when HTF60 strongly against

### W02.  `T4=T4a AND RSI=RSI1 AND session_bucket=ny_open`
- Raw: n=129  W=110/L=19  WR=85.3%
- Refine: exclude H60=H60e drops 16/19 losers (84%)
- **Final: n=99  W=96/L=3  WR=97.0%**
- **Dir: ?**  •  4h trend WITH trade; RSI 20-30 oversold; session=ny_open  •  AVOID when HTF60 strongly against

### W03.  `RSI=RSI1 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=129  W=110/L=19  WR=85.3%
- Refine: exclude H60=H60e drops 16/19 losers (84%)
- **Final: n=99  W=96/L=3  WR=97.0%**
- **Dir: SHORT**  •  RSI 20-30 oversold; session=ny_open  •  AVOID when HTF60 strongly against

### W04.  `T1=T1a AND T4=T4a AND RSI=RSI1 AND session_bucket=ny_open`
- Raw: n=129  W=110/L=19  WR=85.3%
- Refine: exclude H60=H60e drops 16/19 losers (84%)
- **Final: n=99  W=96/L=3  WR=97.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 20-30 oversold; session=ny_open  •  AVOID when HTF60 strongly against

### W05.  `T1=T1a AND RSI=RSI1 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=129  W=110/L=19  WR=85.3%
- Refine: exclude H60=H60e drops 16/19 losers (84%)
- **Final: n=99  W=96/L=3  WR=97.0%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 20-30 oversold; session=ny_open  •  AVOID when HTF60 strongly against

### W06.  `T4=T4a AND RSI=RSI1 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=129  W=110/L=19  WR=85.3%
- Refine: exclude H60=H60e drops 16/19 losers (84%)
- **Final: n=99  W=96/L=3  WR=97.0%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 20-30 oversold; session=ny_open  •  AVOID when HTF60 strongly against

### W07.  `H60=H60a AND T1=T1c AND session_bucket=asia`
- Raw: n=111  W=105/L=6  WR=94.6%
- Refine: exclude BBP=BBP2 drops 4/6 losers (67%)
- **Final: n=75  W=73/L=2  WR=97.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=asia  •  AVOID when lower third

### W08.  `H60=H60a AND direction_exec=long AND session_bucket=asia`
- Raw: n=111  W=105/L=6  WR=94.6%
- Refine: exclude BBP=BBP2 drops 4/6 losers (67%)
- **Final: n=75  W=73/L=2  WR=97.3%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; session=asia  •  AVOID when lower third

### W09.  `H60=H60a AND T1=T1c AND direction_exec=long AND session_bucket=asia`
- Raw: n=111  W=105/L=6  WR=94.6%
- Refine: exclude BBP=BBP2 drops 4/6 losers (67%)
- **Final: n=75  W=73/L=2  WR=97.3%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=asia  •  AVOID when lower third

### W10.  `H20=H20a AND RSI=RSI1 AND session_bucket=ny_open`
- Raw: n=107  W=102/L=5  WR=95.3%
- Refine: exclude T1=T1c drops 2/5 losers (40%)
- **Final: n=99  W=96/L=3  WR=97.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 20-30 oversold; session=ny_open  •  AVOID when 1h trend AGAINST trade

### W11.  `H20=H20a AND T1=T1a AND session_bucket=ny_open`
- Raw: n=99  W=96/L=3  WR=97.0%
- Refine: exclude BBP=BBP1 drops 3/3 losers (100%)
- **Final: n=62  W=62/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=ny_open  •  AVOID when just touched lower band

### W12.  `H20=H20a AND T4=T4a AND session_bucket=ny_open`
- Raw: n=99  W=96/L=3  WR=97.0%
- Refine: exclude BBP=BBP1 drops 3/3 losers (100%)
- **Final: n=62  W=62/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=ny_open  •  AVOID when just touched lower band

### W13.  `H20=H20a AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=99  W=96/L=3  WR=97.0%
- Refine: exclude BBP=BBP1 drops 3/3 losers (100%)
- **Final: n=62  W=62/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; session=ny_open  •  AVOID when just touched lower band

### W14.  `H20=H20a AND T1=T1a AND T4=T4a AND session_bucket=ny_open`
- Raw: n=99  W=96/L=3  WR=97.0%
- Refine: exclude BBP=BBP1 drops 3/3 losers (100%)
- **Final: n=62  W=62/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; session=ny_open  •  AVOID when just touched lower band

### W15.  `H20=H20a AND T1=T1a AND RSI=RSI1 AND session_bucket=ny_open`
- Raw: n=99  W=96/L=3  WR=97.0%
- Refine: exclude BBP=BBP1 drops 3/3 losers (100%)
- **Final: n=62  W=62/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 20-30 oversold; session=ny_open  •  AVOID when just touched lower band

### W16.  `H20=H20a AND T1=T1a AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=99  W=96/L=3  WR=97.0%
- Refine: exclude BBP=BBP1 drops 3/3 losers (100%)
- **Final: n=62  W=62/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=ny_open  •  AVOID when just touched lower band

### W17.  `H20=H20a AND T4=T4a AND RSI=RSI1 AND session_bucket=ny_open`
- Raw: n=99  W=96/L=3  WR=97.0%
- Refine: exclude BBP=BBP1 drops 3/3 losers (100%)
- **Final: n=62  W=62/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 20-30 oversold; session=ny_open  •  AVOID when just touched lower band

### W18.  `H20=H20a AND T4=T4a AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=99  W=96/L=3  WR=97.0%
- Refine: exclude BBP=BBP1 drops 3/3 losers (100%)
- **Final: n=62  W=62/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend WITH trade; session=ny_open  •  AVOID when just touched lower band

### W19.  `H20=H20a AND RSI=RSI1 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=99  W=96/L=3  WR=97.0%
- Refine: exclude BBP=BBP1 drops 3/3 losers (100%)
- **Final: n=62  W=62/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 20-30 oversold; session=ny_open  •  AVOID when just touched lower band

### W20.  `H60=H60a AND T4=T4c AND session_bucket=asia`
- Raw: n=95  W=89/L=6  WR=93.7%
- Refine: exclude BBP=BBP2 drops 4/6 losers (67%)
- **Final: n=65  W=63/L=2  WR=96.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=asia  •  AVOID when lower third

### W21.  `H60=H60a AND T1=T1c AND T4=T4c AND session_bucket=asia`
- Raw: n=95  W=89/L=6  WR=93.7%
- Refine: exclude BBP=BBP2 drops 4/6 losers (67%)
- **Final: n=65  W=63/L=2  WR=96.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; session=asia  •  AVOID when lower third

### W22.  `H60=H60a AND T4=T4c AND direction_exec=long AND session_bucket=asia`
- Raw: n=95  W=89/L=6  WR=93.7%
- Refine: exclude BBP=BBP2 drops 4/6 losers (67%)
- **Final: n=65  W=63/L=2  WR=96.9%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=asia  •  AVOID when lower third

### W23.  `H60=H60a AND RSI=RSI1 AND session_bucket=ny_open`
- Raw: n=83  W=71/L=12  WR=85.5%
- Refine: exclude T1=T1c drops 12/12 losers (100%)
- **Final: n=53  W=53/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 20-30 oversold; session=ny_open  •  AVOID when 1h trend AGAINST trade

### W24.  `H20=H20a AND H60=H60a AND session_bucket=ny_open`
- Raw: n=77  W=70/L=7  WR=90.9%
- Refine: exclude T1=T1c drops 7/7 losers (100%)
- **Final: n=53  W=53/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=ny_open  •  AVOID when 1h trend AGAINST trade

### W25.  `H60=H60a AND T1=T1c AND RSI=RSI2`
- Raw: n=77  W=70/L=7  WR=90.9%
- Refine: exclude ZS=ZS4 drops 3/7 losers (43%)
- **Final: n=65  W=61/L=4  WR=93.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 30-40 weak  •  AVOID when zscore +1 to +2 overbought

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND BBP=BBP2 AND RSI=RSI1`
- Raw: n=115  W=43/L=72  WR=37.4%
- Sharpen: sharpest is session_bucket=ny_open (28/72 of losers there)
- **Sharp: n=28  W=0/L=28  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; lower third; RSI 20-30 oversold  •  ONLY when session=ny_open

### L02.  `H20=H20e AND RSI=RSI1 AND ZS=ZS1`
- Raw: n=114  W=44/L=70  WR=38.6%
- Sharpen: sharpest is session_bucket=ny_open (41/70 of losers there)
- **Sharp: n=44  W=3/L=41  WR=6.8%**
- **Dir: ?**  •  HTF20 strongly against; RSI 20-30 oversold; zscore -3 to -2 deep oversold  •  ONLY when session=ny_open

### L03.  `H20=H20e AND T4=T4c AND RSI=RSI1 AND ZS=ZS1`
- Raw: n=114  W=44/L=70  WR=38.6%
- Sharpen: sharpest is session_bucket=ny_open (41/70 of losers there)
- **Sharp: n=44  W=3/L=41  WR=6.8%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 20-30 oversold; zscore -3 to -2 deep oversold  •  ONLY when session=ny_open

### L04.  `H20=H20e AND T4=T4c AND BBP=BBP2 AND RSI=RSI1`
- Raw: n=110  W=43/L=67  WR=39.1%
- Sharpen: sharpest is session_bucket=ny_open (23/67 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; lower third; RSI 20-30 oversold  •  ONLY when session=ny_open

### L05.  `H20=H20e AND RSI=RSI1 AND ZS=ZS2`
- Raw: n=103  W=31/L=72  WR=30.1%
- Sharpen: sharpest is session_bucket=ny_open (28/72 of losers there)
- **Sharp: n=28  W=0/L=28  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; RSI 20-30 oversold; zscore -2 to -1 oversold  •  ONLY when session=ny_open

### L06.  `H20=H20e AND BBP=BBP2 AND RSI=RSI1 AND ZS=ZS2`
- Raw: n=103  W=31/L=72  WR=30.1%
- Sharpen: sharpest is session_bucket=ny_open (28/72 of losers there)
- **Sharp: n=28  W=0/L=28  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; lower third; RSI 20-30 oversold; zscore -2 to -1 oversold  •  ONLY when session=ny_open

### L07.  `H20=H20e AND T1=T1c AND BBP=BBP2 AND RSI=RSI1`
- Raw: n=103  W=41/L=62  WR=39.8%
- Sharpen: sharpest is session_bucket=ny_open (23/62 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; lower third; RSI 20-30 oversold  •  ONLY when session=ny_open

### L08.  `H20=H20e AND BBP=BBP2 AND RSI=RSI1 AND direction_exec=long`
- Raw: n=103  W=41/L=62  WR=39.8%
- Sharpen: sharpest is session_bucket=ny_open (23/62 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: LONG**  •  HTF20 strongly against; lower third; RSI 20-30 oversold  •  ONLY when session=ny_open

### L09.  `H20=H20e AND T4=T4c AND RSI=RSI1 AND ZS=ZS2`
- Raw: n=98  W=31/L=67  WR=31.6%
- Sharpen: sharpest is session_bucket=ny_open (23/67 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 20-30 oversold; zscore -2 to -1 oversold  •  ONLY when session=ny_open

### L10.  `T1=T1c AND RSI=RSI1 AND session_bucket=ny_open`
- Raw: n=97  W=21/L=76  WR=21.6%
- Sharpen: sharpest is H20=H20e (64/76 of losers there)
- **Sharp: n=67  W=3/L=64  WR=4.5%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 20-30 oversold; session=ny_open  •  ONLY when HTF20 strongly against

### L11.  `T4=T4c AND RSI=RSI1 AND session_bucket=ny_open`
- Raw: n=97  W=21/L=76  WR=21.6%
- Sharpen: sharpest is H20=H20e (64/76 of losers there)
- **Sharp: n=67  W=3/L=64  WR=4.5%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 20-30 oversold; session=ny_open  •  ONLY when HTF20 strongly against

### L12.  `RSI=RSI1 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=97  W=21/L=76  WR=21.6%
- Sharpen: sharpest is H20=H20e (64/76 of losers there)
- **Sharp: n=67  W=3/L=64  WR=4.5%**
- **Dir: LONG**  •  RSI 20-30 oversold; session=ny_open  •  ONLY when HTF20 strongly against

### L13.  `T1=T1c AND T4=T4c AND RSI=RSI1 AND session_bucket=ny_open`
- Raw: n=97  W=21/L=76  WR=21.6%
- Sharpen: sharpest is H20=H20e (64/76 of losers there)
- **Sharp: n=67  W=3/L=64  WR=4.5%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; RSI 20-30 oversold; session=ny_open  •  ONLY when HTF20 strongly against

### L14.  `T1=T1c AND RSI=RSI1 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=97  W=21/L=76  WR=21.6%
- Sharpen: sharpest is H20=H20e (64/76 of losers there)
- **Sharp: n=67  W=3/L=64  WR=4.5%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 20-30 oversold; session=ny_open  •  ONLY when HTF20 strongly against

### L15.  `T4=T4c AND RSI=RSI1 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=97  W=21/L=76  WR=21.6%
- Sharpen: sharpest is H20=H20e (64/76 of losers there)
- **Sharp: n=67  W=3/L=64  WR=4.5%**
- **Dir: LONG**  •  4h trend AGAINST trade; RSI 20-30 oversold; session=ny_open  •  ONLY when HTF20 strongly against

### L16.  `H20=H20e AND T1=T1c AND RSI=RSI1 AND ZS=ZS2`
- Raw: n=91  W=29/L=62  WR=31.9%
- Sharpen: sharpest is session_bucket=ny_open (23/62 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; RSI 20-30 oversold; zscore -2 to -1 oversold  •  ONLY when session=ny_open

### L17.  `H20=H20e AND RSI=RSI1 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=91  W=29/L=62  WR=31.9%
- Sharpen: sharpest is session_bucket=ny_open (23/62 of losers there)
- **Sharp: n=23  W=0/L=23  WR=0.0%**
- **Dir: LONG**  •  HTF20 strongly against; RSI 20-30 oversold; zscore -2 to -1 oversold  •  ONLY when session=ny_open

### L18.  `H20=H20e AND H60=H60e AND ZS=ZS2`
- Raw: n=83  W=32/L=51  WR=38.6%
- Sharpen: sharpest is session_bucket=ny_open (27/51 of losers there)
- **Sharp: n=32  W=5/L=27  WR=15.6%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; zscore -2 to -1 oversold  •  ONLY when session=ny_open

### L19.  `H20=H20e AND H60=H60e AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=83  W=32/L=51  WR=38.6%
- Sharpen: sharpest is session_bucket=ny_open (27/51 of losers there)
- **Sharp: n=32  W=5/L=27  WR=15.6%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; lower third; zscore -2 to -1 oversold  •  ONLY when session=ny_open

### L20.  `H20=H20e AND T1=T1c AND BBP=BBP1`
- Raw: n=80  W=32/L=48  WR=40.0%
- Sharpen: sharpest is session_bucket=ny_open (22/48 of losers there)
- **Sharp: n=25  W=3/L=22  WR=12.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; just touched lower band  •  ONLY when session=ny_open

### L21.  `H20=H20e AND T4=T4c AND BBP=BBP1`
- Raw: n=80  W=32/L=48  WR=40.0%
- Sharpen: sharpest is session_bucket=ny_open (22/48 of losers there)
- **Sharp: n=25  W=3/L=22  WR=12.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; just touched lower band  •  ONLY when session=ny_open

### L22.  `H20=H20e AND BBP=BBP1 AND direction_exec=long`
- Raw: n=80  W=32/L=48  WR=40.0%
- Sharpen: sharpest is session_bucket=ny_open (22/48 of losers there)
- **Sharp: n=25  W=3/L=22  WR=12.0%**
- **Dir: LONG**  •  HTF20 strongly against; just touched lower band  •  ONLY when session=ny_open

### L23.  `H20=H20e AND T1=T1c AND T4=T4c AND BBP=BBP1`
- Raw: n=80  W=32/L=48  WR=40.0%
- Sharpen: sharpest is session_bucket=ny_open (22/48 of losers there)
- **Sharp: n=25  W=3/L=22  WR=12.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; just touched lower band  •  ONLY when session=ny_open

### L24.  `H20=H20e AND T1=T1c AND BBP=BBP1 AND ZS=ZS1`
- Raw: n=80  W=32/L=48  WR=40.0%
- Sharpen: sharpest is session_bucket=ny_open (22/48 of losers there)
- **Sharp: n=25  W=3/L=22  WR=12.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; just touched lower band; zscore -3 to -2 deep oversold  •  ONLY when session=ny_open

### L25.  `H20=H20e AND T1=T1c AND BBP=BBP1 AND direction_exec=long`
- Raw: n=80  W=32/L=48  WR=40.0%
- Sharpen: sharpest is session_bucket=ny_open (22/48 of losers there)
- **Sharp: n=25  W=3/L=22  WR=12.0%**
- **Dir: LONG**  •  HTF20 strongly against; 1h trend AGAINST trade; just touched lower band  •  ONLY when session=ny_open

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(42/35) | H20e(33/43) |
| H60 | H60a(29/22) | H60e(21/27) |
| T1 | — | — |
| T4 | T4a(53/48) | T4c(47/52) |
| BBP | — | — |
| RSI | — | RSI1(45/50) |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
