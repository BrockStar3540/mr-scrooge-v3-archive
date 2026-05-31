# NZD_CHF — R28 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_0**  (5m ATR <33% stop)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR3**  (60-90%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **1,152**  (W=741 / L=411)  -  WR: **64.3%**

## Session distribution

- asia: n=392  W=260/L=132  WR=66.3%
- london_open: n=176  W=110/L=66  WR=62.5%
- ny_mid: n=147  W=87/L=60  WR=59.2%
- ny_open: n=141  W=89/L=52  WR=63.1%
- ny_close: n=109  W=67/L=42  WR=61.5%
- london: n=83  W=59/L=24  WR=71.1%
- asia_late: n=80  W=52/L=28  WR=65.0%
- off_hours: n=24  W=17/L=7  WR=70.8%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60a AND T4=T4a AND direction_exec=short AND session_bucket=asia`
- Raw: n=77  W=66/L=11  WR=85.7%
- Refine: exclude H20=H20e drops 9/11 losers (82%)
- **Final: n=56  W=54/L=2  WR=96.4%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 4h trend WITH trade; session=asia  •  AVOID when HTF20 strongly against

### W02.  `H20=H20a AND H60=H60a AND T1=T1a`
- Raw: n=74  W=65/L=9  WR=87.8%
- Refine: exclude session_bucket=ny_close drops 5/9 losers (56%)
- **Final: n=66  W=62/L=4  WR=93.9%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade  •  AVOID when session=ny_close

### W03.  `H60=H60a AND T1=T1a AND ZS=ZS4`
- Raw: n=67  W=57/L=10  WR=85.1%
- Refine: exclude RSI=RSI3 drops 7/10 losers (70%)
- **Final: n=37  W=34/L=3  WR=91.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; zscore +1 to +2 overbought  •  AVOID when RSI 40-50 lower neutral

### W04.  `H60=H60a AND T1=T1a AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=67  W=57/L=10  WR=85.1%
- Refine: exclude RSI=RSI3 drops 7/10 losers (70%)
- **Final: n=37  W=34/L=3  WR=91.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; upper third; zscore +1 to +2 overbought  •  AVOID when RSI 40-50 lower neutral

### W05.  `H20=H20a AND H60=H60a AND T1=T1a AND T4=T4a`
- Raw: n=64  W=59/L=5  WR=92.2%
- Refine: exclude session_bucket=ny_close drops 5/5 losers (100%)
- **Final: n=56  W=56/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade  •  AVOID when session=ny_close

### W06.  `H20=H20e AND H60=H60a AND RSI=RSI4`
- Raw: n=61  W=52/L=9  WR=85.2%
- Refine: exclude session_bucket=ny_mid drops 2/9 losers (22%)
- **Final: n=59  W=52/L=7  WR=88.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; RSI 50-60 upper neutral  •  AVOID when session=ny_mid

### W07.  `T4=T4c AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=61  W=52/L=9  WR=85.2%
- Refine: exclude H60=H60e drops 6/9 losers (67%)
- **Final: n=46  W=43/L=3  WR=93.5%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 50-60 upper neutral; session=asia  •  AVOID when HTF60 strongly against

### W08.  `H20=H20e AND H60=H60a AND RSI=RSI4 AND direction_exec=short`
- Raw: n=61  W=52/L=9  WR=85.2%
- Refine: exclude session_bucket=ny_mid drops 2/9 losers (22%)
- **Final: n=59  W=52/L=7  WR=88.1%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 aligned WITH trade; RSI 50-60 upper neutral  •  AVOID when session=ny_mid

### W09.  `H20=H20a AND H60=H60d AND T4=T4c`
- Raw: n=60  W=52/L=8  WR=86.7%
- Refine: exclude direction_exec=short drops 8/8 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 mildly against; 4h trend AGAINST trade  •  AVOID when short

### W10.  `T1=T1a AND RSI=RSI4 AND session_bucket=london_open`
- Raw: n=60  W=51/L=9  WR=85.0%
- Refine: exclude T4=T4c drops 9/9 losers (100%)
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; RSI 50-60 upper neutral; session=london_open  •  AVOID when 4h trend AGAINST trade

### W11.  `H20=H20a AND T1=T1c AND BBP=BBP0`
- Raw: n=59  W=51/L=8  WR=86.4%
- Refine: exclude session_bucket=ny_open drops 5/8 losers (62%)
- **Final: n=54  W=51/L=3  WR=94.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; deep below lower band  •  AVOID when session=ny_open

### W12.  `H20=H20e AND T1=T1a AND session_bucket=london_open`
- Raw: n=58  W=55/L=3  WR=94.8%
- Refine: exclude T4=T4c drops 3/3 losers (100%)
- **Final: n=31  W=31/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; session=london_open  •  AVOID when 4h trend AGAINST trade

### W13.  `H20=H20a AND H60=H60a AND session_bucket=asia`
- Raw: n=58  W=50/L=8  WR=86.2%
- Refine: exclude ZS=ZS3 drops 4/8 losers (50%)
- **Final: n=52  W=48/L=4  WR=92.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=asia  •  AVOID when zscore -1 to +1 neutral

### W14.  `H60=H60a AND T1=T1a AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=56  W=49/L=7  WR=87.5%
- Refine: exclude session_bucket=ny_close drops 4/7 losers (57%)
- **Final: n=51  W=48/L=3  WR=94.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; lower third; RSI 40-50 lower neutral  •  AVOID when session=ny_close

### W15.  `H60=H60a AND T1=T1a AND RSI=RSI4`
- Raw: n=55  W=48/L=7  WR=87.3%
- Refine: exclude session_bucket=asia drops 3/7 losers (43%)
- **Final: n=48  W=44/L=4  WR=91.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when session=asia

### W16.  `H60=H60a AND BBP=BBP2 AND RSI=RSI3 AND direction_exec=short`
- Raw: n=54  W=47/L=7  WR=87.0%
- Refine: exclude session_bucket=ny_close drops 4/7 losers (57%)
- **Final: n=49  W=46/L=3  WR=93.9%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; lower third; RSI 40-50 lower neutral  •  AVOID when session=ny_close

### W17.  `H20=H20a AND H60=H60e AND T1=T1c AND session_bucket=ny_mid`
- Raw: n=54  W=46/L=8  WR=85.2%
- Refine: exclude BBP=BBP1 drops 4/8 losers (50%)
- **Final: n=48  W=44/L=4  WR=91.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend AGAINST trade; session=ny_mid  •  AVOID when just touched lower band

### W18.  `H20=H20a AND T1=T1c AND direction_exec=long AND session_bucket=ny_mid`
- Raw: n=54  W=46/L=8  WR=85.2%
- Refine: exclude BBP=BBP1 drops 4/8 losers (50%)
- **Final: n=48  W=44/L=4  WR=91.7%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; session=ny_mid  •  AVOID when just touched lower band

### W19.  `T1=T1a AND T4=T4a AND session_bucket=london_open`
- Raw: n=53  W=51/L=2  WR=96.2%
- Refine: exclude ZS=ZS3 drops 2/2 losers (100%)
- **Final: n=49  W=49/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; session=london_open  •  AVOID when zscore -1 to +1 neutral

### W20.  `H20=H20e AND H60=H60a AND T1=T1c`
- Raw: n=53  W=46/L=7  WR=86.8%
- Refine: exclude T4=T4c drops 5/7 losers (71%)
- **Final: n=36  W=34/L=2  WR=94.4%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend AGAINST trade  •  AVOID when 4h trend AGAINST trade

### W21.  `H20=H20e AND H60=H60a AND T1=T1c AND direction_exec=short`
- Raw: n=53  W=46/L=7  WR=86.8%
- Refine: exclude T4=T4c drops 5/7 losers (71%)
- **Final: n=36  W=34/L=2  WR=94.4%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend AGAINST trade  •  AVOID when 4h trend AGAINST trade

### W22.  `H20=H20a AND direction_exec=short AND session_bucket=asia`
- Raw: n=52  W=46/L=6  WR=88.5%
- Refine: exclude H60=H60d drops 4/6 losers (67%)
- **Final: n=36  W=34/L=2  WR=94.4%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; session=asia  •  AVOID when HTF60 mildly against

### W23.  `T1=T1c AND RSI=RSI2 AND session_bucket=ny_mid`
- Raw: n=52  W=46/L=6  WR=88.5%
- Refine: exclude BBP=BBP1 drops 4/6 losers (67%)
- **Final: n=46  W=44/L=2  WR=95.7%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 30-40 weak; session=ny_mid  •  AVOID when just touched lower band

### W24.  `T1=T1a AND T4=T4c AND RSI=RSI3 AND direction_exec=short`
- Raw: n=51  W=45/L=6  WR=88.2%
- Refine: exclude ZS=ZS3 drops 4/6 losers (67%)
- **Final: n=38  W=36/L=2  WR=94.7%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 40-50 lower neutral  •  AVOID when zscore -1 to +1 neutral

### W25.  `T1=T1a AND direction_exec=short AND session_bucket=london_open`
- Raw: n=50  W=45/L=5  WR=90.0%
- Refine: exclude H20=H20a drops 3/5 losers (60%)
- **Final: n=44  W=42/L=2  WR=95.5%**
- **Dir: SHORT**  •  1h trend WITH trade; session=london_open  •  AVOID when HTF20 aligned WITH trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND H60=H60a AND RSI=RSI2`
- Raw: n=71  W=27/L=44  WR=38.0%
- Sharpen: sharpest is T4=T4a (26/44 of losers there)
- **Sharp: n=36  W=10/L=26  WR=27.8%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; RSI 30-40 weak  •  ONLY when 4h trend WITH trade

### L02.  `H20=H20e AND H60=H60a AND T1=T1a AND RSI=RSI2`
- Raw: n=71  W=27/L=44  WR=38.0%
- Sharpen: sharpest is T4=T4a (26/44 of losers there)
- **Sharp: n=36  W=10/L=26  WR=27.8%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 aligned WITH trade; 1h trend WITH trade; RSI 30-40 weak  •  ONLY when 4h trend WITH trade

### L03.  `H20=H20e AND H60=H60a AND RSI=RSI2 AND direction_exec=short`
- Raw: n=71  W=27/L=44  WR=38.0%
- Sharpen: sharpest is T4=T4a (26/44 of losers there)
- **Sharp: n=36  W=10/L=26  WR=27.8%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 aligned WITH trade; RSI 30-40 weak  •  ONLY when 4h trend WITH trade

### L04.  `H20=H20e AND T4=T4a AND RSI=RSI2`
- Raw: n=64  W=25/L=39  WR=39.1%
- Sharpen: sharpest is T1=T1a (31/39 of losers there)
- **Sharp: n=43  W=12/L=31  WR=27.9%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; RSI 30-40 weak  •  ONLY when 1h trend WITH trade

### L05.  `T1=T1a AND T4=T4a AND RSI=RSI2`
- Raw: n=60  W=21/L=39  WR=35.0%
- Sharpen: sharpest is H20=H20e (31/39 of losers there)
- **Sharp: n=43  W=12/L=31  WR=27.9%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 30-40 weak  •  ONLY when HTF20 strongly against

### L06.  `T1=T1a AND T4=T4a AND RSI=RSI2 AND direction_exec=short`
- Raw: n=60  W=21/L=39  WR=35.0%
- Sharpen: sharpest is H20=H20e (31/39 of losers there)
- **Sharp: n=43  W=12/L=31  WR=27.9%**
- **Dir: SHORT**  •  1h trend WITH trade; 4h trend WITH trade; RSI 30-40 weak  •  ONLY when HTF20 strongly against

### L07.  `H20=H20e AND H60=H60e AND T1=T1c AND T4=T4c`
- Raw: n=57  W=21/L=36  WR=36.8%
- Sharpen: sharpest is session_bucket=london_open (9/36 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when session=london_open

### L08.  `H20=H20a AND H60=H60e AND T1=T1a AND T4=T4c`
- Raw: n=55  W=22/L=33  WR=40.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=55  W=22/L=33  WR=40.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend WITH trade; 4h trend AGAINST trade

### L09.  `H60=H60a AND T1=T1a AND T4=T4a AND RSI=RSI2`
- Raw: n=48  W=18/L=30  WR=37.5%
- Sharpen: sharpest is H20=H20e (26/30 of losers there)
- **Sharp: n=36  W=10/L=26  WR=27.8%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; RSI 30-40 weak  •  ONLY when HTF20 strongly against

### L10.  `H20=H20e AND T1=T1a AND session_bucket=ny_mid`
- Raw: n=47  W=14/L=33  WR=29.8%
- Sharpen: sharpest is ZS=ZS3 (9/33 of losers there)
- **Sharp: n=10  W=1/L=9  WR=10.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; session=ny_mid  •  ONLY when zscore -1 to +1 neutral

### L11.  `T1=T1a AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=47  W=18/L=29  WR=38.3%
- Sharpen: sharpest is H20=H20e (26/29 of losers there)
- **Sharp: n=35  W=9/L=26  WR=25.7%**
- **Dir: SHORT**  •  1h trend WITH trade; session=ny_mid  •  ONLY when HTF20 strongly against

### L12.  `T4=T4a AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=45  W=15/L=30  WR=33.3%
- Sharpen: sharpest is T1=T1a (16/30 of losers there)
- **Sharp: n=18  W=2/L=16  WR=11.1%**
- **Dir: ?**  •  4h trend WITH trade; RSI 50-60 upper neutral; session=asia  •  ONLY when 1h trend WITH trade

### L13.  `H20=H20e AND T1=T1a AND T4=T4a AND RSI=RSI2`
- Raw: n=43  W=12/L=31  WR=27.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=43  W=12/L=31  WR=27.9%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend WITH trade; RSI 30-40 weak

### L14.  `H20=H20e AND T4=T4a AND RSI=RSI2 AND direction_exec=short`
- Raw: n=43  W=12/L=31  WR=27.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=43  W=12/L=31  WR=27.9%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend WITH trade; RSI 30-40 weak

### L15.  `H60=H60e AND T4=T4c AND session_bucket=london_open`
- Raw: n=43  W=15/L=28  WR=34.9%
- Sharpen: sharpest is T1=T1c (19/28 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; session=london_open  •  ONLY when 1h trend AGAINST trade

### L16.  `H20=H20e AND T1=T1a AND BBP=BBP0`
- Raw: n=42  W=15/L=27  WR=35.7%
- Sharpen: sharpest is T4=T4a (12/27 of losers there)
- **Sharp: n=14  W=2/L=12  WR=14.3%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; deep below lower band  •  ONLY when 4h trend WITH trade

### L17.  `H20=H20a AND T1=T1c AND session_bucket=london_open`
- Raw: n=41  W=6/L=35  WR=14.6%
- Sharpen: sharpest is T4=T4c (20/35 of losers there)
- **Sharp: n=20  W=0/L=20  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; session=london_open  •  ONLY when 4h trend AGAINST trade

### L18.  `H20=H20e AND BBP=BBP2 AND RSI=RSI2`
- Raw: n=41  W=16/L=25  WR=39.0%
- Sharpen: sharpest is H60=H60a (17/25 of losers there)
- **Sharp: n=24  W=7/L=17  WR=29.2%**
- **Dir: ?**  •  HTF20 strongly against; lower third; RSI 30-40 weak  •  ONLY when HTF60 aligned WITH trade

### L19.  `H60=H60a AND T1=T1a AND session_bucket=ny_mid`
- Raw: n=41  W=16/L=25  WR=39.0%
- Sharpen: sharpest is H20=H20e (24/25 of losers there)
- **Sharp: n=32  W=8/L=24  WR=25.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=ny_mid  •  ONLY when HTF20 strongly against

### L20.  `H60=H60e AND T1=T1c AND BBP=BBP2 AND RSI=RSI3`
- Raw: n=40  W=15/L=25  WR=37.5%
- Sharpen: sharpest is session_bucket=london (6/25 of losers there)
- **Sharp: n=6  W=0/L=6  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; lower third; RSI 40-50 lower neutral  •  ONLY when session=london

### L21.  `H20=H20e AND H60=H60e AND T1=T1c AND RSI=RSI3`
- Raw: n=40  W=16/L=24  WR=40.0%
- Sharpen: sharpest is ZS=ZS3 (8/24 of losers there)
- **Sharp: n=10  W=2/L=8  WR=20.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; RSI 40-50 lower neutral  •  ONLY when zscore -1 to +1 neutral

### L22.  `H60=H60e AND T1=T1c AND T4=T4c AND direction_exec=short`
- Raw: n=40  W=16/L=24  WR=40.0%
- Sharpen: sharpest is session_bucket=london_open (9/24 of losers there)
- **Sharp: n=9  W=0/L=9  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when session=london_open

### L23.  `H60=H60a AND T1=T1a AND direction_exec=short AND session_bucket=ny_mid`
- Raw: n=40  W=16/L=24  WR=40.0%
- Sharpen: sharpest is H20=H20e (24/24 of losers there)
- **Sharp: n=32  W=8/L=24  WR=25.0%**
- **Dir: SHORT**  •  HTF60 aligned WITH trade; 1h trend WITH trade; session=ny_mid  •  ONLY when HTF20 strongly against

### L24.  `T1=T1c AND direction_exec=long AND session_bucket=london_open`
- Raw: n=39  W=15/L=24  WR=38.5%
- Sharpen: sharpest is H60=H60e (12/24 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: LONG**  •  1h trend AGAINST trade; session=london_open  •  ONLY when HTF60 strongly against

### L25.  `T1=T1a AND RSI=RSI2 AND session_bucket=ny_mid`
- Raw: n=38  W=11/L=27  WR=28.9%
- Sharpen: sharpest is BBP=BBP2 (8/27 of losers there)
- **Sharp: n=9  W=1/L=8  WR=11.1%**
- **Dir: ?**  •  1h trend WITH trade; RSI 30-40 weak; session=ny_mid  •  ONLY when lower third

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | H20e(40/46) |
| H60 | H60a(47/34) | H60e(38/50) |
| T1 | — | — |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | short(53/46) | long(47/54) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
