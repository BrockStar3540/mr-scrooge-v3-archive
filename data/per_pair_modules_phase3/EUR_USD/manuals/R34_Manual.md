# EUR_USD — R34 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20e**  (EMA20 down >0.5x)
- **E50 = E50d**  (EMA50 down 0.15-0.5x)
- **ADR = ADR3**  (60-90%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **2,613**  (W=1,644 / L=969)  -  WR: **62.9%**

## Session distribution

- ny_close: n=557  W=348/L=209  WR=62.5%
- ny_mid: n=513  W=322/L=191  WR=62.8%
- london_open: n=463  W=302/L=161  WR=65.2%
- asia: n=371  W=242/L=129  WR=65.2%
- ny_open: n=259  W=157/L=102  WR=60.6%
- london: n=257  W=153/L=104  WR=59.5%
- off_hours: n=130  W=76/L=54  WR=58.5%
- asia_late: n=63  W=44/L=19  WR=69.8%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND H60=H60a AND RSI=RSI2 AND ZS=ZS3`
- Raw: n=88  W=75/L=13  WR=85.2%
- Refine: exclude session_bucket=ny_mid drops 11/13 losers (85%)
- **Final: n=66  W=64/L=2  WR=97.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 30-40 weak; zscore -1 to +1 neutral  •  AVOID when session=ny_mid

### W02.  `H20=H20e AND T4=T4a AND BBP=BBP0`
- Raw: n=77  W=66/L=11  WR=85.7%
- Refine: exclude session_bucket=ny_mid drops 5/11 losers (45%)
- **Final: n=63  W=57/L=6  WR=90.5%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; deep below lower band  •  AVOID when session=ny_mid

### W03.  `H60=H60e AND T1=T1a AND T4=T4c AND direction_exec=long`
- Raw: n=74  W=65/L=9  WR=87.8%
- Refine: exclude BBP=BBP4 drops 8/9 losers (89%)
- **Final: n=50  W=49/L=1  WR=98.0%**
- **Dir: LONG**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend AGAINST trade  •  AVOID when upper third

### W04.  `H60=H60a AND T4=T4a AND RSI=RSI3 AND ZS=ZS4`
- Raw: n=69  W=61/L=8  WR=88.4%
- Refine: exclude session_bucket=asia drops 5/8 losers (62%)
- **Final: n=43  W=40/L=3  WR=93.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 40-50 lower neutral; zscore +1 to +2 overbought  •  AVOID when session=asia

### W05.  `H20=H20e AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=68  W=61/L=7  WR=89.7%
- Refine: exclude session_bucket=london_open drops 6/7 losers (86%)
- **Final: n=56  W=55/L=1  WR=98.2%**
- **Dir: ?**  •  HTF20 strongly against; deep above upper band; zscore +2 to +3 deep overbought  •  AVOID when session=london_open

### W06.  `H60=H60e AND T1=T1a AND T4=T4c AND RSI=RSI4`
- Raw: n=63  W=57/L=6  WR=90.5%
- Refine: exclude session_bucket=london_open drops 6/6 losers (100%)
- **Final: n=42  W=42/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when session=london_open

### W07.  `T1=T1a AND ZS=ZS2 AND session_bucket=london_open`
- Raw: n=61  W=54/L=7  WR=88.5%
- Refine: exclude H60=H60a drops 4/7 losers (57%)
- **Final: n=43  W=40/L=3  WR=93.0%**
- **Dir: ?**  •  1h trend WITH trade; zscore -2 to -1 oversold; session=london_open  •  AVOID when HTF60 aligned WITH trade

### W08.  `T1=T1a AND BBP=BBP2 AND ZS=ZS2 AND session_bucket=london_open`
- Raw: n=61  W=54/L=7  WR=88.5%
- Refine: exclude H60=H60a drops 4/7 losers (57%)
- **Final: n=43  W=40/L=3  WR=93.0%**
- **Dir: ?**  •  1h trend WITH trade; lower third; zscore -2 to -1 oversold; session=london_open  •  AVOID when HTF60 aligned WITH trade

### W09.  `T4=T4a AND BBP=BBP0 AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=61  W=54/L=7  WR=88.5%
- Refine: exclude session_bucket=ny_close drops 4/7 losers (57%)
- **Final: n=45  W=42/L=3  WR=93.3%**
- **Dir: ?**  •  4h trend WITH trade; deep below lower band; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  AVOID when session=ny_close

### W10.  `H20=H20e AND H60=H60e AND BBP=BBP0 AND ZS=ZS1`
- Raw: n=59  W=52/L=7  WR=88.1%
- Refine: exclude session_bucket=ny_mid drops 5/7 losers (71%)
- **Final: n=49  W=47/L=2  WR=95.9%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; deep below lower band; zscore -3 to -2 deep oversold  •  AVOID when session=ny_mid

### W11.  `H20=H20a AND T1=T1a AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=59  W=52/L=7  WR=88.1%
- Refine: exclude BBP=BBP0 drops 3/7 losers (43%)
- **Final: n=56  W=52/L=4  WR=92.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade; session=ny_mid  •  AVOID when deep below lower band

### W12.  `H60=H60a AND T1=T1a AND T4=T4c AND session_bucket=ny_mid`
- Raw: n=59  W=52/L=7  WR=88.1%
- Refine: exclude BBP=BBP0 drops 3/7 losers (43%)
- **Final: n=56  W=52/L=4  WR=92.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade; session=ny_mid  •  AVOID when deep below lower band

### W13.  `H60=H60e AND T4=T4c AND session_bucket=london`
- Raw: n=58  W=51/L=7  WR=87.9%
- Refine: exclude T1=T1c drops 7/7 losers (100%)
- **Final: n=42  W=42/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; session=london  •  AVOID when 1h trend AGAINST trade

### W14.  `H20=H20e AND H60=H60e AND T4=T4c AND session_bucket=london`
- Raw: n=58  W=51/L=7  WR=87.9%
- Refine: exclude T1=T1c drops 7/7 losers (100%)
- **Final: n=42  W=42/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; session=london  •  AVOID when 1h trend AGAINST trade

### W15.  `H20=H20e AND BBP=BBP6 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=58  W=51/L=7  WR=87.9%
- Refine: exclude session_bucket=london_open drops 6/7 losers (86%)
- **Final: n=46  W=45/L=1  WR=97.8%**
- **Dir: LONG**  •  HTF20 strongly against; deep above upper band; zscore +2 to +3 deep overbought  •  AVOID when session=london_open

### W16.  `H60=H60e AND T4=T4c AND direction_exec=long AND session_bucket=london`
- Raw: n=58  W=51/L=7  WR=87.9%
- Refine: exclude T1=T1c drops 7/7 losers (100%)
- **Final: n=42  W=42/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 strongly against; 4h trend AGAINST trade; session=london  •  AVOID when 1h trend AGAINST trade

### W17.  `H20=H20e AND T1=T1a AND BBP=BBP0`
- Raw: n=57  W=51/L=6  WR=89.5%
- Refine: exclude session_bucket=ny_close drops 5/6 losers (83%)
- **Final: n=30  W=29/L=1  WR=96.7%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; deep below lower band  •  AVOID when session=ny_close

### W18.  `H20=H20e AND BBP=BBP0 AND direction_exec=short`
- Raw: n=57  W=51/L=6  WR=89.5%
- Refine: exclude session_bucket=ny_close drops 5/6 losers (83%)
- **Final: n=30  W=29/L=1  WR=96.7%**
- **Dir: SHORT**  •  HTF20 strongly against; deep below lower band  •  AVOID when session=ny_close

### W19.  `H20=H20e AND T1=T1a AND T4=T4a AND BBP=BBP0`
- Raw: n=57  W=51/L=6  WR=89.5%
- Refine: exclude session_bucket=ny_close drops 5/6 losers (83%)
- **Final: n=30  W=29/L=1  WR=96.7%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend WITH trade; deep below lower band  •  AVOID when session=ny_close

### W20.  `H20=H20e AND T1=T1a AND BBP=BBP0 AND direction_exec=short`
- Raw: n=57  W=51/L=6  WR=89.5%
- Refine: exclude session_bucket=ny_close drops 5/6 losers (83%)
- **Final: n=30  W=29/L=1  WR=96.7%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend WITH trade; deep below lower band  •  AVOID when session=ny_close

### W21.  `H20=H20e AND T4=T4a AND BBP=BBP0 AND direction_exec=short`
- Raw: n=57  W=51/L=6  WR=89.5%
- Refine: exclude session_bucket=ny_close drops 5/6 losers (83%)
- **Final: n=30  W=29/L=1  WR=96.7%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend WITH trade; deep below lower band  •  AVOID when session=ny_close

### W22.  `H20=H20a AND H60=H60e AND BBP=BBP2`
- Raw: n=56  W=50/L=6  WR=89.3%
- Refine: exclude session_bucket=ny_mid drops 3/6 losers (50%)
- **Final: n=49  W=46/L=3  WR=93.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; lower third  •  AVOID when session=ny_mid

### W23.  `H20=H20a AND H60=H60e AND T1=T1c AND BBP=BBP2`
- Raw: n=56  W=50/L=6  WR=89.3%
- Refine: exclude session_bucket=ny_mid drops 3/6 losers (50%)
- **Final: n=49  W=46/L=3  WR=93.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend AGAINST trade; lower third  •  AVOID when session=ny_mid

### W24.  `H20=H20a AND H60=H60e AND T4=T4c AND BBP=BBP2`
- Raw: n=56  W=50/L=6  WR=89.3%
- Refine: exclude session_bucket=ny_mid drops 3/6 losers (50%)
- **Final: n=49  W=46/L=3  WR=93.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 4h trend AGAINST trade; lower third  •  AVOID when session=ny_mid

### W25.  `H20=H20a AND H60=H60e AND BBP=BBP2 AND direction_exec=long`
- Raw: n=56  W=50/L=6  WR=89.3%
- Refine: exclude session_bucket=ny_mid drops 3/6 losers (50%)
- **Final: n=49  W=46/L=3  WR=93.9%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 strongly against; lower third  •  AVOID when session=ny_mid

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T4=T4c AND BBP=BBP4 AND session_bucket=london_open`
- Raw: n=73  W=27/L=46  WR=37.0%
- Sharpen: sharpest is ZS=ZS4 (37/46 of losers there)
- **Sharp: n=52  W=15/L=37  WR=28.8%**
- **Dir: ?**  •  4h trend AGAINST trade; upper third; session=london_open  •  ONLY when zscore +1 to +2 overbought

### L02.  `T4=T4a AND RSI=RSI4 AND session_bucket=london`
- Raw: n=69  W=22/L=47  WR=31.9%
- Sharpen: sharpest is H60=H60a (26/47 of losers there)
- **Sharp: n=34  W=8/L=26  WR=23.5%**
- **Dir: ?**  •  4h trend WITH trade; RSI 50-60 upper neutral; session=london  •  ONLY when HTF60 aligned WITH trade

### L03.  `H20=H20e AND H60=H60e AND RSI=RSI2 AND ZS=ZS3`
- Raw: n=69  W=25/L=44  WR=36.2%
- Sharpen: sharpest is T4=T4a (18/44 of losers there)
- **Sharp: n=20  W=2/L=18  WR=10.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 30-40 weak; zscore -1 to +1 neutral  •  ONLY when 4h trend WITH trade

### L04.  `H60=H60a AND T1=T1c AND session_bucket=london`
- Raw: n=64  W=23/L=41  WR=35.9%
- Sharpen: sharpest is BBP=BBP6 (29/41 of losers there)
- **Sharp: n=33  W=4/L=29  WR=12.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=london  •  ONLY when deep above upper band

### L05.  `H20=H20a AND H60=H60a AND T1=T1c AND session_bucket=london`
- Raw: n=64  W=23/L=41  WR=35.9%
- Sharpen: sharpest is BBP=BBP6 (29/41 of losers there)
- **Sharp: n=33  W=4/L=29  WR=12.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend AGAINST trade; session=london  •  ONLY when deep above upper band

### L06.  `T1=T1a AND ZS=ZS3 AND session_bucket=london_open`
- Raw: n=64  W=25/L=39  WR=39.1%
- Sharpen: sharpest is T4=T4a (25/39 of losers there)
- **Sharp: n=32  W=7/L=25  WR=21.9%**
- **Dir: ?**  •  1h trend WITH trade; zscore -1 to +1 neutral; session=london_open  •  ONLY when 4h trend WITH trade

### L07.  `H60=H60a AND RSI=RSI4 AND session_bucket=london`
- Raw: n=63  W=25/L=38  WR=39.7%
- Sharpen: sharpest is BBP=BBP6 (29/38 of losers there)
- **Sharp: n=33  W=4/L=29  WR=12.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; session=london  •  ONLY when deep above upper band

### L08.  `H20=H20a AND H60=H60a AND RSI=RSI4 AND session_bucket=london`
- Raw: n=63  W=25/L=38  WR=39.7%
- Sharpen: sharpest is BBP=BBP6 (29/38 of losers there)
- **Sharp: n=33  W=4/L=29  WR=12.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 50-60 upper neutral; session=london  •  ONLY when deep above upper band

### L09.  `H60=H60a AND RSI=RSI4 AND direction_exec=short AND session_bucket=london`
- Raw: n=63  W=25/L=38  WR=39.7%
- Sharpen: sharpest is BBP=BBP6 (29/38 of losers there)
- **Sharp: n=33  W=4/L=29  WR=12.1%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; session=london  •  ONLY when deep above upper band

### L10.  `H60=H60e AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=62  W=24/L=38  WR=38.7%
- Sharpen: sharpest is T1=T1c (27/38 of losers there)
- **Sharp: n=39  W=12/L=27  WR=30.8%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; session=ny_mid  •  ONLY when 1h trend AGAINST trade

### L11.  `H20=H20e AND H60=H60e AND T4=T4a AND session_bucket=ny_mid`
- Raw: n=62  W=24/L=38  WR=38.7%
- Sharpen: sharpest is T1=T1c (27/38 of losers there)
- **Sharp: n=39  W=12/L=27  WR=30.8%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend WITH trade; session=ny_mid  •  ONLY when 1h trend AGAINST trade

### L12.  `H60=H60a AND T1=T1c AND T4=T4a AND direction_exec=short`
- Raw: n=61  W=22/L=39  WR=36.1%
- Sharpen: sharpest is session_bucket=london (25/39 of losers there)
- **Sharp: n=29  W=4/L=25  WR=13.8%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when session=london

### L13.  `H20=H20e AND T4=T4c AND RSI=RSI3 AND ZS=ZS4`
- Raw: n=60  W=23/L=37  WR=38.3%
- Sharpen: sharpest is H60=H60e (25/37 of losers there)
- **Sharp: n=32  W=7/L=25  WR=21.9%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 40-50 lower neutral; zscore +1 to +2 overbought  •  ONLY when HTF60 strongly against

### L14.  `T4=T4c AND BBP=BBP4 AND RSI=RSI3 AND session_bucket=london_open`
- Raw: n=60  W=23/L=37  WR=38.3%
- Sharpen: sharpest is ZS=ZS4 (33/37 of losers there)
- **Sharp: n=47  W=14/L=33  WR=29.8%**
- **Dir: ?**  •  4h trend AGAINST trade; upper third; RSI 40-50 lower neutral; session=london_open  •  ONLY when zscore +1 to +2 overbought

### L15.  `T1=T1c AND BBP=BBP6 AND RSI=RSI4`
- Raw: n=60  W=24/L=36  WR=40.0%
- Sharpen: sharpest is H60=H60a (29/36 of losers there)
- **Sharp: n=33  W=4/L=29  WR=12.1%**
- **Dir: ?**  •  1h trend AGAINST trade; deep above upper band; RSI 50-60 upper neutral  •  ONLY when HTF60 aligned WITH trade

### L16.  `H60=H60a AND T1=T1c AND RSI=RSI4 AND session_bucket=london`
- Raw: n=58  W=21/L=37  WR=36.2%
- Sharpen: sharpest is BBP=BBP6 (29/37 of losers there)
- **Sharp: n=33  W=4/L=29  WR=12.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 50-60 upper neutral; session=london  •  ONLY when deep above upper band

### L17.  `H60=H60a AND T1=T1c AND direction_exec=short AND session_bucket=london`
- Raw: n=58  W=21/L=37  WR=36.2%
- Sharpen: sharpest is BBP=BBP6 (29/37 of losers there)
- **Sharp: n=33  W=4/L=29  WR=12.1%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=london  •  ONLY when deep above upper band

### L18.  `H20=H20a AND BBP=BBP6 AND RSI=RSI4`
- Raw: n=58  W=22/L=36  WR=37.9%
- Sharpen: sharpest is H60=H60a (36/36 of losers there)
- **Sharp: n=41  W=5/L=36  WR=12.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; deep above upper band; RSI 50-60 upper neutral  •  ONLY when HTF60 aligned WITH trade

### L19.  `T1=T1a AND ZS=ZS3 AND direction_exec=short AND session_bucket=london_open`
- Raw: n=58  W=23/L=35  WR=39.7%
- Sharpen: sharpest is RSI=RSI3 (27/35 of losers there)
- **Sharp: n=34  W=7/L=27  WR=20.6%**
- **Dir: SHORT**  •  1h trend WITH trade; zscore -1 to +1 neutral; session=london_open  •  ONLY when RSI 40-50 lower neutral

### L20.  `T1=T1c AND BBP=BBP4 AND session_bucket=ny_close`
- Raw: n=57  W=18/L=39  WR=31.6%
- Sharpen: sharpest is H60=H60e (23/39 of losers there)
- **Sharp: n=28  W=5/L=23  WR=17.9%**
- **Dir: ?**  •  1h trend AGAINST trade; upper third; session=ny_close  •  ONLY when HTF60 strongly against

### L21.  `H60=H60a AND BBP=BBP3 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=57  W=20/L=37  WR=35.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=57  W=20/L=37  WR=35.1%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; middle of band; RSI 40-50 lower neutral

### L22.  `H20=H20e AND H60=H60e AND BBP=BBP3 AND RSI=RSI2`
- Raw: n=57  W=21/L=36  WR=36.8%
- Sharpen: sharpest is session_bucket=ny_open (9/36 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; middle of band; RSI 30-40 weak  •  ONLY when session=ny_open

### L23.  `BBP=BBP4 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=56  W=16/L=40  WR=28.6%
- Sharpen: sharpest is H60=H60e (23/40 of losers there)
- **Sharp: n=26  W=3/L=23  WR=11.5%**
- **Dir: LONG**  •  upper third; session=ny_close  •  ONLY when HTF60 strongly against

### L24.  `H60=H60a AND T1=T1a AND BBP=BBP3 AND RSI=RSI3`
- Raw: n=56  W=20/L=36  WR=35.7%
- Sharpen: no sharper sub-pattern
- **Sharp: n=56  W=20/L=36  WR=35.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; middle of band; RSI 40-50 lower neutral

### L25.  `T1=T1c AND BBP=BBP4 AND direction_exec=long AND session_bucket=ny_close`
- Raw: n=55  W=16/L=39  WR=29.1%
- Sharpen: sharpest is H60=H60e (23/39 of losers there)
- **Sharp: n=26  W=3/L=23  WR=11.5%**
- **Dir: LONG**  •  1h trend AGAINST trade; upper third; session=ny_close  •  ONLY when HTF60 strongly against

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(52/46) | H20e(46/53) |
| H60 | — | — |
| T1 | T1a(54/47) | T1c(46/53) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
