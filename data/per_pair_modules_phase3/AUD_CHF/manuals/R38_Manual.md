# AUD_CHF — R38 Manual

## Regime centroid (locked factors)

- **BB = BB1**  (narrow bands)
- **A5 = A5_0**  (5m ATR <33% stop)
- **A1 = A1_0**  (1h ATR <2x stop)
- **E20 = E20d**  (EMA20 down 0.15-0.5x)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR3**  (60-90%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **1,290**  (W=849 / L=441)  -  WR: **65.8%**

## Session distribution

- asia: n=340  W=215/L=125  WR=63.2%
- ny_open: n=195  W=125/L=70  WR=64.1%
- ny_close: n=181  W=125/L=56  WR=69.1%
- london_open: n=157  W=106/L=51  WR=67.5%
- ny_mid: n=130  W=89/L=41  WR=68.5%
- asia_late: n=119  W=81/L=38  WR=68.1%
- london: n=108  W=69/L=39  WR=63.9%
- off_hours: n=60  W=39/L=21  WR=65.0%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20e AND H60=H60e AND session_bucket=ny_open`
- Raw: n=74  W=64/L=10  WR=86.5%
- Refine: exclude RSI=RSI4 drops 5/10 losers (50%)
- **Final: n=69  W=64/L=5  WR=92.8%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; session=ny_open  •  AVOID when RSI 50-60 upper neutral

### W02.  `H20=H20e AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=74  W=64/L=10  WR=86.5%
- Refine: exclude RSI=RSI4 drops 5/10 losers (50%)
- **Final: n=69  W=64/L=5  WR=92.8%**
- **Dir: SHORT**  •  HTF20 strongly against; session=ny_open  •  AVOID when RSI 50-60 upper neutral

### W03.  `H20=H20e AND H60=H60e AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=74  W=64/L=10  WR=86.5%
- Refine: exclude RSI=RSI4 drops 5/10 losers (50%)
- **Final: n=69  W=64/L=5  WR=92.8%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; session=ny_open  •  AVOID when RSI 50-60 upper neutral

### W04.  `T1=T1a AND T4=T4c AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=65  W=56/L=9  WR=86.2%
- Refine: exclude BBP=BBP0 drops 5/9 losers (56%)
- **Final: n=46  W=42/L=4  WR=91.3%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  AVOID when deep below lower band

### W05.  `T1=T1c AND T4=T4a AND RSI=RSI3 AND ZS=ZS1`
- Raw: n=60  W=51/L=9  WR=85.0%
- Refine: exclude H20=H20a drops 8/9 losers (89%)
- **Final: n=21  W=20/L=1  WR=95.2%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 40-50 lower neutral; zscore -3 to -2 deep oversold  •  AVOID when HTF20 aligned WITH trade

### W06.  `H20=H20b AND T4=T4c AND direction_exec=long`
- Raw: n=58  W=50/L=8  WR=86.2%
- Refine: exclude RSI=RSI2 drops 5/8 losers (62%)
- **Final: n=39  W=36/L=3  WR=92.3%**
- **Dir: LONG**  •  HTF20 slightly aligned; 4h trend AGAINST trade  •  AVOID when RSI 30-40 weak

### W07.  `H20=H20b AND T1=T1c AND T4=T4c AND direction_exec=long`
- Raw: n=58  W=50/L=8  WR=86.2%
- Refine: exclude RSI=RSI2 drops 5/8 losers (62%)
- **Final: n=39  W=36/L=3  WR=92.3%**
- **Dir: LONG**  •  HTF20 slightly aligned; 1h trend AGAINST trade; 4h trend AGAINST trade  •  AVOID when RSI 30-40 weak

### W08.  `H20=H20b AND H60=H60a AND T4=T4c`
- Raw: n=56  W=50/L=6  WR=89.3%
- Refine: exclude session_bucket=ny_close drops 3/6 losers (50%)
- **Final: n=51  W=48/L=3  WR=94.1%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 4h trend AGAINST trade  •  AVOID when session=ny_close

### W09.  `H20=H20b AND H60=H60a AND T1=T1c AND T4=T4c`
- Raw: n=56  W=50/L=6  WR=89.3%
- Refine: exclude session_bucket=ny_close drops 3/6 losers (50%)
- **Final: n=51  W=48/L=3  WR=94.1%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade  •  AVOID when session=ny_close

### W10.  `H20=H20b AND H60=H60a AND T4=T4c AND direction_exec=long`
- Raw: n=56  W=50/L=6  WR=89.3%
- Refine: exclude session_bucket=ny_close drops 3/6 losers (50%)
- **Final: n=51  W=48/L=3  WR=94.1%**
- **Dir: LONG**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 4h trend AGAINST trade  •  AVOID when session=ny_close

### W11.  `H60=H60e AND RSI=RSI2 AND session_bucket=ny_open`
- Raw: n=53  W=48/L=5  WR=90.6%
- Refine: exclude BBP=BBP0 drops 2/5 losers (40%)
- **Final: n=49  W=46/L=3  WR=93.9%**
- **Dir: ?**  •  HTF60 strongly against; RSI 30-40 weak; session=ny_open  •  AVOID when deep below lower band

### W12.  `T1=T1a AND RSI=RSI2 AND session_bucket=ny_open`
- Raw: n=53  W=48/L=5  WR=90.6%
- Refine: exclude BBP=BBP0 drops 2/5 losers (40%)
- **Final: n=49  W=46/L=3  WR=93.9%**
- **Dir: ?**  •  1h trend WITH trade; RSI 30-40 weak; session=ny_open  •  AVOID when deep below lower band

### W13.  `T4=T4c AND RSI=RSI2 AND session_bucket=ny_open`
- Raw: n=53  W=48/L=5  WR=90.6%
- Refine: exclude BBP=BBP0 drops 2/5 losers (40%)
- **Final: n=49  W=46/L=3  WR=93.9%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 30-40 weak; session=ny_open  •  AVOID when deep below lower band

### W14.  `RSI=RSI2 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=53  W=48/L=5  WR=90.6%
- Refine: exclude BBP=BBP0 drops 2/5 losers (40%)
- **Final: n=49  W=46/L=3  WR=93.9%**
- **Dir: SHORT**  •  RSI 30-40 weak; session=ny_open  •  AVOID when deep below lower band

### W15.  `H60=H60e AND T1=T1a AND RSI=RSI2 AND session_bucket=ny_open`
- Raw: n=53  W=48/L=5  WR=90.6%
- Refine: exclude BBP=BBP0 drops 2/5 losers (40%)
- **Final: n=49  W=46/L=3  WR=93.9%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; RSI 30-40 weak; session=ny_open  •  AVOID when deep below lower band

### W16.  `H60=H60e AND T4=T4c AND RSI=RSI2 AND session_bucket=ny_open`
- Raw: n=53  W=48/L=5  WR=90.6%
- Refine: exclude BBP=BBP0 drops 2/5 losers (40%)
- **Final: n=49  W=46/L=3  WR=93.9%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; RSI 30-40 weak; session=ny_open  •  AVOID when deep below lower band

### W17.  `H60=H60e AND RSI=RSI2 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=53  W=48/L=5  WR=90.6%
- Refine: exclude BBP=BBP0 drops 2/5 losers (40%)
- **Final: n=49  W=46/L=3  WR=93.9%**
- **Dir: SHORT**  •  HTF60 strongly against; RSI 30-40 weak; session=ny_open  •  AVOID when deep below lower band

### W18.  `T1=T1a AND T4=T4c AND RSI=RSI2 AND session_bucket=ny_open`
- Raw: n=53  W=48/L=5  WR=90.6%
- Refine: exclude BBP=BBP0 drops 2/5 losers (40%)
- **Final: n=49  W=46/L=3  WR=93.9%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 30-40 weak; session=ny_open  •  AVOID when deep below lower band

### W19.  `T1=T1a AND RSI=RSI2 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=53  W=48/L=5  WR=90.6%
- Refine: exclude BBP=BBP0 drops 2/5 losers (40%)
- **Final: n=49  W=46/L=3  WR=93.9%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 30-40 weak; session=ny_open  •  AVOID when deep below lower band

### W20.  `T4=T4c AND RSI=RSI2 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=53  W=48/L=5  WR=90.6%
- Refine: exclude BBP=BBP0 drops 2/5 losers (40%)
- **Final: n=49  W=46/L=3  WR=93.9%**
- **Dir: SHORT**  •  4h trend AGAINST trade; RSI 30-40 weak; session=ny_open  •  AVOID when deep below lower band

### W21.  `H20=H20e AND RSI=RSI2 AND session_bucket=ny_open`
- Raw: n=51  W=46/L=5  WR=90.2%
- Refine: exclude BBP=BBP0 drops 2/5 losers (40%)
- **Final: n=47  W=44/L=3  WR=93.6%**
- **Dir: ?**  •  HTF20 strongly against; RSI 30-40 weak; session=ny_open  •  AVOID when deep below lower band

### W22.  `H20=H20e AND H60=H60e AND RSI=RSI2 AND session_bucket=ny_open`
- Raw: n=51  W=46/L=5  WR=90.2%
- Refine: exclude BBP=BBP0 drops 2/5 losers (40%)
- **Final: n=47  W=44/L=3  WR=93.6%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 30-40 weak; session=ny_open  •  AVOID when deep below lower band

### W23.  `H20=H20e AND T1=T1a AND RSI=RSI2 AND session_bucket=ny_open`
- Raw: n=51  W=46/L=5  WR=90.2%
- Refine: exclude BBP=BBP0 drops 2/5 losers (40%)
- **Final: n=47  W=44/L=3  WR=93.6%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; RSI 30-40 weak; session=ny_open  •  AVOID when deep below lower band

### W24.  `H20=H20e AND T4=T4c AND RSI=RSI2 AND session_bucket=ny_open`
- Raw: n=51  W=46/L=5  WR=90.2%
- Refine: exclude BBP=BBP0 drops 2/5 losers (40%)
- **Final: n=47  W=44/L=3  WR=93.6%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 30-40 weak; session=ny_open  •  AVOID when deep below lower band

### W25.  `H20=H20e AND RSI=RSI2 AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=51  W=46/L=5  WR=90.2%
- Refine: exclude BBP=BBP0 drops 2/5 losers (40%)
- **Final: n=47  W=44/L=3  WR=93.6%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 30-40 weak; session=ny_open  •  AVOID when deep below lower band

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20a AND T4=T4a AND RSI=RSI2`
- Raw: n=111  W=43/L=68  WR=38.7%
- Sharpen: no sharper sub-pattern
- **Sharp: n=111  W=43/L=68  WR=38.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 30-40 weak

### L02.  `H20=H20a AND H60=H60a AND T4=T4a AND RSI=RSI2`
- Raw: n=111  W=43/L=68  WR=38.7%
- Sharpen: no sharper sub-pattern
- **Sharp: n=111  W=43/L=68  WR=38.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 4h trend WITH trade; RSI 30-40 weak

### L03.  `H20=H20a AND T1=T1c AND T4=T4a AND RSI=RSI2`
- Raw: n=111  W=43/L=68  WR=38.7%
- Sharpen: no sharper sub-pattern
- **Sharp: n=111  W=43/L=68  WR=38.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade; RSI 30-40 weak

### L04.  `H20=H20a AND T4=T4a AND RSI=RSI2 AND direction_exec=long`
- Raw: n=111  W=43/L=68  WR=38.7%
- Sharpen: no sharper sub-pattern
- **Sharp: n=111  W=43/L=68  WR=38.7%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 30-40 weak

### L05.  `H20=H20a AND H60=H60a AND session_bucket=ny_open`
- Raw: n=71  W=27/L=44  WR=38.0%
- Sharpen: sharpest is BBP=BBP1 (25/44 of losers there)
- **Sharp: n=31  W=6/L=25  WR=19.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=ny_open  •  ONLY when just touched lower band

### L06.  `H20=H20a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=71  W=27/L=44  WR=38.0%
- Sharpen: sharpest is BBP=BBP1 (25/44 of losers there)
- **Sharp: n=31  W=6/L=25  WR=19.4%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; session=ny_open  •  ONLY when just touched lower band

### L07.  `H20=H20a AND H60=H60a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=71  W=27/L=44  WR=38.0%
- Sharpen: sharpest is BBP=BBP1 (25/44 of losers there)
- **Sharp: n=31  W=6/L=25  WR=19.4%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=ny_open  •  ONLY when just touched lower band

### L08.  `T1=T1c AND T4=T4a AND RSI=RSI2 AND ZS=ZS1`
- Raw: n=66  W=25/L=41  WR=37.9%
- Sharpen: sharpest is session_bucket=ny_open (25/41 of losers there)
- **Sharp: n=34  W=9/L=25  WR=26.5%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 30-40 weak; zscore -3 to -2 deep oversold  •  ONLY when session=ny_open

### L09.  `H60=H60a AND RSI=RSI2 AND session_bucket=ny_open`
- Raw: n=58  W=19/L=39  WR=32.8%
- Sharpen: sharpest is BBP=BBP1 (22/39 of losers there)
- **Sharp: n=26  W=4/L=22  WR=15.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 30-40 weak; session=ny_open  •  ONLY when just touched lower band

### L10.  `T1=T1c AND RSI=RSI2 AND session_bucket=ny_open`
- Raw: n=58  W=19/L=39  WR=32.8%
- Sharpen: sharpest is BBP=BBP1 (22/39 of losers there)
- **Sharp: n=26  W=4/L=22  WR=15.4%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 30-40 weak; session=ny_open  •  ONLY when just touched lower band

### L11.  `T4=T4a AND RSI=RSI2 AND session_bucket=ny_open`
- Raw: n=58  W=19/L=39  WR=32.8%
- Sharpen: sharpest is BBP=BBP1 (22/39 of losers there)
- **Sharp: n=26  W=4/L=22  WR=15.4%**
- **Dir: ?**  •  4h trend WITH trade; RSI 30-40 weak; session=ny_open  •  ONLY when just touched lower band

### L12.  `RSI=RSI2 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=58  W=19/L=39  WR=32.8%
- Sharpen: sharpest is BBP=BBP1 (22/39 of losers there)
- **Sharp: n=26  W=4/L=22  WR=15.4%**
- **Dir: LONG**  •  RSI 30-40 weak; session=ny_open  •  ONLY when just touched lower band

### L13.  `H60=H60a AND T1=T1c AND RSI=RSI2 AND session_bucket=ny_open`
- Raw: n=58  W=19/L=39  WR=32.8%
- Sharpen: sharpest is BBP=BBP1 (22/39 of losers there)
- **Sharp: n=26  W=4/L=22  WR=15.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 30-40 weak; session=ny_open  •  ONLY when just touched lower band

### L14.  `H60=H60a AND T4=T4a AND RSI=RSI2 AND session_bucket=ny_open`
- Raw: n=58  W=19/L=39  WR=32.8%
- Sharpen: sharpest is BBP=BBP1 (22/39 of losers there)
- **Sharp: n=26  W=4/L=22  WR=15.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 30-40 weak; session=ny_open  •  ONLY when just touched lower band

### L15.  `H60=H60a AND RSI=RSI2 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=58  W=19/L=39  WR=32.8%
- Sharpen: sharpest is BBP=BBP1 (22/39 of losers there)
- **Sharp: n=26  W=4/L=22  WR=15.4%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 30-40 weak; session=ny_open  •  ONLY when just touched lower band

### L16.  `T1=T1c AND T4=T4a AND RSI=RSI2 AND session_bucket=ny_open`
- Raw: n=58  W=19/L=39  WR=32.8%
- Sharpen: sharpest is BBP=BBP1 (22/39 of losers there)
- **Sharp: n=26  W=4/L=22  WR=15.4%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 30-40 weak; session=ny_open  •  ONLY when just touched lower band

### L17.  `T1=T1c AND RSI=RSI2 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=58  W=19/L=39  WR=32.8%
- Sharpen: sharpest is BBP=BBP1 (22/39 of losers there)
- **Sharp: n=26  W=4/L=22  WR=15.4%**
- **Dir: LONG**  •  1h trend AGAINST trade; RSI 30-40 weak; session=ny_open  •  ONLY when just touched lower band

### L18.  `T4=T4a AND RSI=RSI2 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=58  W=19/L=39  WR=32.8%
- Sharpen: sharpest is BBP=BBP1 (22/39 of losers there)
- **Sharp: n=26  W=4/L=22  WR=15.4%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 30-40 weak; session=ny_open  •  ONLY when just touched lower band

### L19.  `T4=T4a AND RSI=RSI2 AND session_bucket=asia`
- Raw: n=55  W=18/L=37  WR=32.7%
- Sharpen: sharpest is BBP=BBP0 (12/37 of losers there)
- **Sharp: n=12  W=0/L=12  WR=0.0%**
- **Dir: ?**  •  4h trend WITH trade; RSI 30-40 weak; session=asia  •  ONLY when deep below lower band

### L20.  `H20=H20a AND RSI=RSI2 AND session_bucket=ny_open`
- Raw: n=53  W=17/L=36  WR=32.1%
- Sharpen: sharpest is BBP=BBP1 (22/36 of losers there)
- **Sharp: n=26  W=4/L=22  WR=15.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 30-40 weak; session=ny_open  •  ONLY when just touched lower band

### L21.  `H20=H20a AND H60=H60a AND RSI=RSI2 AND session_bucket=ny_open`
- Raw: n=53  W=17/L=36  WR=32.1%
- Sharpen: sharpest is BBP=BBP1 (22/36 of losers there)
- **Sharp: n=26  W=4/L=22  WR=15.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 30-40 weak; session=ny_open  •  ONLY when just touched lower band

### L22.  `H20=H20a AND T1=T1c AND RSI=RSI2 AND session_bucket=ny_open`
- Raw: n=53  W=17/L=36  WR=32.1%
- Sharpen: sharpest is BBP=BBP1 (22/36 of losers there)
- **Sharp: n=26  W=4/L=22  WR=15.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 30-40 weak; session=ny_open  •  ONLY when just touched lower band

### L23.  `H20=H20a AND T4=T4a AND RSI=RSI2 AND session_bucket=ny_open`
- Raw: n=53  W=17/L=36  WR=32.1%
- Sharpen: sharpest is BBP=BBP1 (22/36 of losers there)
- **Sharp: n=26  W=4/L=22  WR=15.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 30-40 weak; session=ny_open  •  ONLY when just touched lower band

### L24.  `H20=H20a AND RSI=RSI2 AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=53  W=17/L=36  WR=32.1%
- Sharpen: sharpest is BBP=BBP1 (22/36 of losers there)
- **Sharp: n=26  W=4/L=22  WR=15.4%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 30-40 weak; session=ny_open  •  ONLY when just touched lower band

### L25.  `H20=H20a AND BBP=BBP1 AND RSI=RSI2`
- Raw: n=50  W=19/L=31  WR=38.0%
- Sharpen: sharpest is session_bucket=ny_open (22/31 of losers there)
- **Sharp: n=26  W=4/L=22  WR=15.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; just touched lower band; RSI 30-40 weak  •  ONLY when session=ny_open

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | H20a(33/39) |
| H60 | — | — |
| T1 | — | — |
| T4 | T4c(53/43) | T4a(47/57) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
