# GBP_JPY — R21 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **7,047**  (W=4,370 / L=2,677)  -  WR: **62.0%**

## Session distribution

- asia: n=1697  W=1054/L=643  WR=62.1%
- london_open: n=1402  W=851/L=551  WR=60.7%
- ny_mid: n=997  W=639/L=358  WR=64.1%
- ny_open: n=926  W=556/L=370  WR=60.0%
- london: n=782  W=490/L=292  WR=62.7%
- ny_close: n=768  W=475/L=293  WR=61.8%
- asia_late: n=294  W=195/L=99  WR=66.3%
- off_hours: n=181  W=110/L=71  WR=60.8%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20e AND T1=T1c AND BBP=BBP6`
- Raw: n=222  W=196/L=26  WR=88.3%
- Refine: exclude session_bucket=london drops 14/26 losers (54%)
- **Final: n=187  W=175/L=12  WR=93.6%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; deep above upper band  •  AVOID when session=london

### W02.  `H20=H20e AND BBP=BBP6 AND direction_exec=short`
- Raw: n=222  W=196/L=26  WR=88.3%
- Refine: exclude session_bucket=london drops 14/26 losers (54%)
- **Final: n=187  W=175/L=12  WR=93.6%**
- **Dir: SHORT**  •  HTF20 strongly against; deep above upper band  •  AVOID when session=london

### W03.  `H20=H20e AND T1=T1c AND BBP=BBP6 AND direction_exec=short`
- Raw: n=222  W=196/L=26  WR=88.3%
- Refine: exclude session_bucket=london drops 14/26 losers (54%)
- **Final: n=187  W=175/L=12  WR=93.6%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; deep above upper band  •  AVOID when session=london

### W04.  `H20=H20e AND T4=T4c AND BBP=BBP6`
- Raw: n=193  W=172/L=21  WR=89.1%
- Refine: exclude session_bucket=london drops 9/21 losers (43%)
- **Final: n=180  W=168/L=12  WR=93.3%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; deep above upper band  •  AVOID when session=london

### W05.  `H20=H20e AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=190  W=167/L=23  WR=87.9%
- Refine: exclude session_bucket=london drops 11/23 losers (48%)
- **Final: n=158  W=146/L=12  WR=92.4%**
- **Dir: ?**  •  HTF20 strongly against; deep above upper band; zscore +2 to +3 deep overbought  •  AVOID when session=london

### W06.  `H20=H20e AND H60=H60e AND BBP=BBP6`
- Raw: n=186  W=160/L=26  WR=86.0%
- Refine: exclude session_bucket=london drops 14/26 losers (54%)
- **Final: n=151  W=139/L=12  WR=92.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; deep above upper band  •  AVOID when session=london

### W07.  `H20=H20e AND H60=H60e AND T1=T1c AND BBP=BBP6`
- Raw: n=186  W=160/L=26  WR=86.0%
- Refine: exclude session_bucket=london drops 14/26 losers (54%)
- **Final: n=151  W=139/L=12  WR=92.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; deep above upper band  •  AVOID when session=london

### W08.  `H20=H20e AND H60=H60e AND BBP=BBP6 AND direction_exec=short`
- Raw: n=186  W=160/L=26  WR=86.0%
- Refine: exclude session_bucket=london drops 14/26 losers (54%)
- **Final: n=151  W=139/L=12  WR=92.1%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; deep above upper band  •  AVOID when session=london

### W09.  `H20=H20e AND T1=T1c AND T4=T4c AND BBP=BBP6`
- Raw: n=184  W=163/L=21  WR=88.6%
- Refine: exclude session_bucket=london drops 9/21 losers (43%)
- **Final: n=171  W=159/L=12  WR=93.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; deep above upper band  •  AVOID when session=london

### W10.  `H20=H20e AND T4=T4c AND BBP=BBP6 AND direction_exec=short`
- Raw: n=184  W=163/L=21  WR=88.6%
- Refine: exclude session_bucket=london drops 9/21 losers (43%)
- **Final: n=171  W=159/L=12  WR=93.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade; deep above upper band  •  AVOID when session=london

### W11.  `H20=H20e AND T1=T1c AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=164  W=141/L=23  WR=86.0%
- Refine: exclude session_bucket=london drops 11/23 losers (48%)
- **Final: n=132  W=120/L=12  WR=90.9%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; deep above upper band; zscore +2 to +3 deep overbought  •  AVOID when session=london

### W12.  `H20=H20e AND BBP=BBP6 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=164  W=141/L=23  WR=86.0%
- Refine: exclude session_bucket=london drops 11/23 losers (48%)
- **Final: n=132  W=120/L=12  WR=90.9%**
- **Dir: SHORT**  •  HTF20 strongly against; deep above upper band; zscore +2 to +3 deep overbought  •  AVOID when session=london

### W13.  `H20=H20e AND BBP=BBP6 AND RSI=RSI5`
- Raw: n=163  W=144/L=19  WR=88.3%
- Refine: exclude T4=T4a drops 12/19 losers (63%)
- **Final: n=112  W=105/L=7  WR=93.8%**
- **Dir: ?**  •  HTF20 strongly against; deep above upper band; RSI 60-70 strong  •  AVOID when 4h trend WITH trade

### W14.  `H20=H20e AND H60=H60e AND T4=T4c AND BBP=BBP6`
- Raw: n=148  W=127/L=21  WR=85.8%
- Refine: exclude session_bucket=london drops 9/21 losers (43%)
- **Final: n=135  W=123/L=12  WR=91.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; deep above upper band  •  AVOID when session=london

### W15.  `H20=H20e AND T1=T1c AND BBP=BBP6 AND RSI=RSI5`
- Raw: n=137  W=125/L=12  WR=91.2%
- Refine: exclude session_bucket=london drops 5/12 losers (42%)
- **Final: n=127  W=120/L=7  WR=94.5%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; deep above upper band; RSI 60-70 strong  •  AVOID when session=london

### W16.  `H20=H20e AND BBP=BBP6 AND RSI=RSI5 AND direction_exec=short`
- Raw: n=137  W=125/L=12  WR=91.2%
- Refine: exclude session_bucket=london drops 5/12 losers (42%)
- **Final: n=127  W=120/L=7  WR=94.5%**
- **Dir: SHORT**  •  HTF20 strongly against; deep above upper band; RSI 60-70 strong  •  AVOID when session=london

### W17.  `H20=H20e AND T4=T4c AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=134  W=116/L=18  WR=86.6%
- Refine: exclude session_bucket=london drops 6/18 losers (33%)
- **Final: n=124  W=112/L=12  WR=90.3%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; deep above upper band; zscore +2 to +3 deep overbought  •  AVOID when session=london

### W18.  `H20=H20e AND H60=H60d AND RSI=RSI5`
- Raw: n=120  W=105/L=15  WR=87.5%
- Refine: exclude session_bucket=ny_mid drops 12/15 losers (80%)
- **Final: n=72  W=69/L=3  WR=95.8%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 mildly against; RSI 60-70 strong  •  AVOID when session=ny_mid

### W19.  `H60=H60d AND T1=T1c AND RSI=RSI5`
- Raw: n=120  W=105/L=15  WR=87.5%
- Refine: exclude session_bucket=ny_mid drops 12/15 losers (80%)
- **Final: n=72  W=69/L=3  WR=95.8%**
- **Dir: ?**  •  HTF60 mildly against; 1h trend AGAINST trade; RSI 60-70 strong  •  AVOID when session=ny_mid

### W20.  `H60=H60d AND RSI=RSI5 AND direction_exec=short`
- Raw: n=120  W=105/L=15  WR=87.5%
- Refine: exclude session_bucket=ny_mid drops 12/15 losers (80%)
- **Final: n=72  W=69/L=3  WR=95.8%**
- **Dir: SHORT**  •  HTF60 mildly against; RSI 60-70 strong  •  AVOID when session=ny_mid

### W21.  `H20=H20e AND H60=H60d AND T1=T1c AND RSI=RSI5`
- Raw: n=120  W=105/L=15  WR=87.5%
- Refine: exclude session_bucket=ny_mid drops 12/15 losers (80%)
- **Final: n=72  W=69/L=3  WR=95.8%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 mildly against; 1h trend AGAINST trade; RSI 60-70 strong  •  AVOID when session=ny_mid

### W22.  `H20=H20e AND H60=H60d AND RSI=RSI5 AND direction_exec=short`
- Raw: n=120  W=105/L=15  WR=87.5%
- Refine: exclude session_bucket=ny_mid drops 12/15 losers (80%)
- **Final: n=72  W=69/L=3  WR=95.8%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 mildly against; RSI 60-70 strong  •  AVOID when session=ny_mid

### W23.  `H60=H60d AND T1=T1c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=120  W=105/L=15  WR=87.5%
- Refine: exclude session_bucket=ny_mid drops 12/15 losers (80%)
- **Final: n=72  W=69/L=3  WR=95.8%**
- **Dir: SHORT**  •  HTF60 mildly against; 1h trend AGAINST trade; RSI 60-70 strong  •  AVOID when session=ny_mid

### W24.  `T1=T1c AND BBP=BBP6 AND session_bucket=asia`
- Raw: n=116  W=100/L=16  WR=86.2%
- Refine: exclude ZS=ZS5 drops 16/16 losers (100%)
- **Final: n=60  W=60/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; deep above upper band; session=asia  •  AVOID when zscore +2 to +3 deep overbought

### W25.  `BBP=BBP6 AND direction_exec=short AND session_bucket=asia`
- Raw: n=116  W=100/L=16  WR=86.2%
- Refine: exclude ZS=ZS5 drops 16/16 losers (100%)
- **Final: n=60  W=60/L=0  WR=100.0%**
- **Dir: SHORT**  •  deep above upper band; session=asia  •  AVOID when zscore +2 to +3 deep overbought

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60a AND T4=T4a AND BBP=BBP6`
- Raw: n=177  W=69/L=108  WR=39.0%
- Sharpen: sharpest is H20=H20a (87/108 of losers there)
- **Sharp: n=118  W=31/L=87  WR=26.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; deep above upper band  •  ONLY when HTF20 aligned WITH trade

### L02.  `H60=H60a AND T4=T4a AND BBP=BBP6 AND direction_exec=long`
- Raw: n=177  W=69/L=108  WR=39.0%
- Sharpen: sharpest is H20=H20a (87/108 of losers there)
- **Sharp: n=118  W=31/L=87  WR=26.3%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend WITH trade; deep above upper band  •  ONLY when HTF20 aligned WITH trade

### L03.  `T4=T4a AND RSI=RSI4 AND ZS=ZS5 AND direction_exec=long`
- Raw: n=176  W=70/L=106  WR=39.8%
- Sharpen: sharpest is T1=T1a (69/106 of losers there)
- **Sharp: n=99  W=30/L=69  WR=30.3%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when 1h trend WITH trade

### L04.  `H60=H60a AND T1=T1a AND BBP=BBP6`
- Raw: n=175  W=62/L=113  WR=35.4%
- Sharpen: sharpest is H20=H20a (98/113 of losers there)
- **Sharp: n=133  W=35/L=98  WR=26.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; deep above upper band  •  ONLY when HTF20 aligned WITH trade

### L05.  `H60=H60a AND T1=T1a AND BBP=BBP6 AND direction_exec=long`
- Raw: n=175  W=62/L=113  WR=35.4%
- Sharpen: sharpest is H20=H20a (98/113 of losers there)
- **Sharp: n=133  W=35/L=98  WR=26.3%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend WITH trade; deep above upper band  •  ONLY when HTF20 aligned WITH trade

### L06.  `H60=H60a AND T1=T1a AND T4=T4a AND BBP=BBP6`
- Raw: n=151  W=49/L=102  WR=32.5%
- Sharpen: sharpest is ZS=ZS6 (33/102 of losers there)
- **Sharp: n=35  W=2/L=33  WR=5.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; deep above upper band  •  ONLY when zscore >+3 extreme

### L07.  `H20=H20a AND T1=T1a AND BBP=BBP6`
- Raw: n=146  W=35/L=111  WR=24.0%
- Sharpen: sharpest is ZS=ZS6 (35/111 of losers there)
- **Sharp: n=37  W=2/L=35  WR=5.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; deep above upper band  •  ONLY when zscore >+3 extreme

### L08.  `H20=H20a AND BBP=BBP6 AND direction_exec=long`
- Raw: n=146  W=35/L=111  WR=24.0%
- Sharpen: sharpest is ZS=ZS6 (35/111 of losers there)
- **Sharp: n=37  W=2/L=35  WR=5.4%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; deep above upper band  •  ONLY when zscore >+3 extreme

### L09.  `H20=H20a AND T1=T1a AND BBP=BBP6 AND direction_exec=long`
- Raw: n=146  W=35/L=111  WR=24.0%
- Sharpen: sharpest is ZS=ZS6 (35/111 of losers there)
- **Sharp: n=37  W=2/L=35  WR=5.4%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; deep above upper band  •  ONLY when zscore >+3 extreme

### L10.  `T4=T4a AND BBP=BBP3 AND direction_exec=short`
- Raw: n=144  W=56/L=88  WR=38.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=144  W=56/L=88  WR=38.9%**
- **Dir: SHORT**  •  4h trend WITH trade; middle of band

### L11.  `T4=T4a AND BBP=BBP3 AND ZS=ZS3 AND direction_exec=short`
- Raw: n=144  W=56/L=88  WR=38.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=144  W=56/L=88  WR=38.9%**
- **Dir: SHORT**  •  4h trend WITH trade; middle of band; zscore -1 to +1 neutral

### L12.  `T4=T4a AND BBP=BBP5 AND RSI=RSI4`
- Raw: n=143  W=57/L=86  WR=39.9%
- Sharpen: sharpest is H60=H60a (64/86 of losers there)
- **Sharp: n=93  W=29/L=64  WR=31.2%**
- **Dir: ?**  •  4h trend WITH trade; just touched upper band; RSI 50-60 upper neutral  •  ONLY when HTF60 aligned WITH trade

### L13.  `T4=T4a AND BBP=BBP5 AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=143  W=57/L=86  WR=39.9%
- Sharpen: sharpest is H60=H60a (64/86 of losers there)
- **Sharp: n=93  W=29/L=64  WR=31.2%**
- **Dir: ?**  •  4h trend WITH trade; just touched upper band; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when HTF60 aligned WITH trade

### L14.  `H20=H20a AND T4=T4a AND BBP=BBP6`
- Raw: n=141  W=31/L=110  WR=22.0%
- Sharpen: sharpest is ZS=ZS6 (36/110 of losers there)
- **Sharp: n=38  W=2/L=36  WR=5.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; deep above upper band  •  ONLY when zscore >+3 extreme

### L15.  `H60=H60a AND BBP=BBP6 AND RSI=RSI5`
- Raw: n=141  W=47/L=94  WR=33.3%
- Sharpen: sharpest is H20=H20a (50/94 of losers there)
- **Sharp: n=62  W=12/L=50  WR=19.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; deep above upper band; RSI 60-70 strong  •  ONLY when HTF20 aligned WITH trade

### L16.  `T1=T1c AND T4=T4a AND BBP=BBP3 AND direction_exec=short`
- Raw: n=135  W=51/L=84  WR=37.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=135  W=51/L=84  WR=37.8%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend WITH trade; middle of band

### L17.  `H20=H20a AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=134  W=33/L=101  WR=24.6%
- Sharpen: sharpest is H60=H60e (25/101 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; deep above upper band; zscore +2 to +3 deep overbought  •  ONLY when HTF60 strongly against

### L18.  `H20=H20a AND H60=H60a AND BBP=BBP6`
- Raw: n=133  W=35/L=98  WR=26.3%
- Sharpen: sharpest is ZS=ZS6 (26/98 of losers there)
- **Sharp: n=28  W=2/L=26  WR=7.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; deep above upper band  •  ONLY when zscore >+3 extreme

### L19.  `H20=H20a AND H60=H60a AND T1=T1a AND BBP=BBP6`
- Raw: n=133  W=35/L=98  WR=26.3%
- Sharpen: sharpest is ZS=ZS6 (26/98 of losers there)
- **Sharp: n=28  W=2/L=26  WR=7.1%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; deep above upper band  •  ONLY when zscore >+3 extreme

### L20.  `H20=H20a AND H60=H60a AND BBP=BBP6 AND direction_exec=long`
- Raw: n=133  W=35/L=98  WR=26.3%
- Sharpen: sharpest is ZS=ZS6 (26/98 of losers there)
- **Sharp: n=28  W=2/L=26  WR=7.1%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; deep above upper band  •  ONLY when zscore >+3 extreme

### L21.  `H20=H20b AND T4=T4c AND ZS=ZS5`
- Raw: n=133  W=53/L=80  WR=39.8%
- Sharpen: sharpest is session_bucket=ny_open (30/80 of losers there)
- **Sharp: n=34  W=4/L=30  WR=11.8%**
- **Dir: ?**  •  HTF20 slightly aligned; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  ONLY when session=ny_open

### L22.  `H20=H20a AND T1=T1a AND T4=T4a AND BBP=BBP6`
- Raw: n=131  W=31/L=100  WR=23.7%
- Sharpen: sharpest is RSI=RSI5 (56/100 of losers there)
- **Sharp: n=64  W=8/L=56  WR=12.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade; deep above upper band  •  ONLY when RSI 60-70 strong

### L23.  `H20=H20a AND T4=T4a AND BBP=BBP6 AND direction_exec=long`
- Raw: n=131  W=31/L=100  WR=23.7%
- Sharpen: sharpest is RSI=RSI5 (56/100 of losers there)
- **Sharp: n=64  W=8/L=56  WR=12.5%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend WITH trade; deep above upper band  •  ONLY when RSI 60-70 strong

### L24.  `H20=H20e AND H60=H60e AND RSI=RSI5 AND ZS=ZS3`
- Raw: n=131  W=49/L=82  WR=37.4%
- Sharpen: sharpest is BBP=BBP3 (49/82 of losers there)
- **Sharp: n=63  W=14/L=49  WR=22.2%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 60-70 strong; zscore -1 to +1 neutral  •  ONLY when middle of band

### L25.  `BBP=BBP6 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=129  W=51/L=78  WR=39.5%
- Sharpen: sharpest is ZS=ZS6 (21/78 of losers there)
- **Sharp: n=23  W=2/L=21  WR=8.7%**
- **Dir: LONG**  •  deep above upper band; RSI 50-60 upper neutral  •  ONLY when zscore >+3 extreme

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | — |
| T1 | T1a(53/46) | T1c(47/54) |
| T4 | T4c(53/47) | T4a(47/53) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
