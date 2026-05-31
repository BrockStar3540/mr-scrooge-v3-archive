# EUR_NZD — R24 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **4,962**  (W=3,092 / L=1,870)  -  WR: **62.3%**

## Session distribution

- asia: n=2485  W=1564/L=921  WR=62.9%
- ny_close: n=856  W=526/L=330  WR=61.4%
- london: n=488  W=302/L=186  WR=61.9%
- asia_late: n=296  W=197/L=99  WR=66.6%
- london_open: n=294  W=183/L=111  WR=62.2%
- ny_open: n=287  W=185/L=102  WR=64.5%
- off_hours: n=215  W=112/L=103  WR=52.1%
- ny_mid: n=41  W=23/L=18  WR=56.1%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND T4=T4c AND BBP=BBP5`
- Raw: n=194  W=168/L=26  WR=86.6%
- Refine: exclude RSI=RSI4 drops 16/26 losers (62%)
- **Final: n=130  W=120/L=10  WR=92.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; just touched upper band  •  AVOID when RSI 50-60 upper neutral

### W02.  `H20=H20a AND T4=T4c AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=194  W=168/L=26  WR=86.6%
- Refine: exclude RSI=RSI4 drops 16/26 losers (62%)
- **Final: n=130  W=120/L=10  WR=92.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; just touched upper band; zscore +2 to +3 deep overbought  •  AVOID when RSI 50-60 upper neutral

### W03.  `H20=H20a AND BBP=BBP5 AND direction_exec=short`
- Raw: n=165  W=144/L=21  WR=87.3%
- Refine: exclude H60=H60a drops 19/21 losers (90%)
- **Final: n=57  W=55/L=2  WR=96.5%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; just touched upper band  •  AVOID when HTF60 aligned WITH trade

### W04.  `H20=H20a AND BBP=BBP5 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=165  W=144/L=21  WR=87.3%
- Refine: exclude H60=H60a drops 19/21 losers (90%)
- **Final: n=57  W=55/L=2  WR=96.5%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; just touched upper band; zscore +2 to +3 deep overbought  •  AVOID when HTF60 aligned WITH trade

### W05.  `H20=H20a AND BBP=BBP5 AND RSI=RSI5`
- Raw: n=161  W=145/L=16  WR=90.1%
- Refine: exclude session_bucket=ny_close drops 6/16 losers (38%)
- **Final: n=155  W=145/L=10  WR=93.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; just touched upper band; RSI 60-70 strong  •  AVOID when session=ny_close

### W06.  `H20=H20a AND BBP=BBP5 AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=161  W=145/L=16  WR=90.1%
- Refine: exclude session_bucket=ny_close drops 6/16 losers (38%)
- **Final: n=155  W=145/L=10  WR=93.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; just touched upper band; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when session=ny_close

### W07.  `H20=H20a AND T1=T1c AND RSI=RSI4 AND direction_exec=long`
- Raw: n=149  W=129/L=20  WR=86.6%
- Refine: exclude ZS=ZS6 drops 6/20 losers (30%)
- **Final: n=143  W=129/L=14  WR=90.2%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when zscore >+3 extreme

### W08.  `H20=H20a AND T1=T1c AND BBP=BBP5 AND direction_exec=short`
- Raw: n=141  W=120/L=21  WR=85.1%
- Refine: exclude H60=H60a drops 19/21 losers (90%)
- **Final: n=57  W=55/L=2  WR=96.5%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; just touched upper band  •  AVOID when HTF60 aligned WITH trade

### W09.  `H20=H20a AND T4=T4c AND BBP=BBP5 AND direction_exec=short`
- Raw: n=134  W=119/L=15  WR=88.8%
- Refine: exclude RSI=RSI4 drops 15/15 losers (100%)
- **Final: n=71  W=71/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; just touched upper band  •  AVOID when RSI 50-60 upper neutral

### W10.  `H20=H20d AND T4=T4a AND RSI=RSI5`
- Raw: n=133  W=115/L=18  WR=86.5%
- Refine: exclude H60=H60a drops 15/18 losers (83%)
- **Final: n=64  W=61/L=3  WR=95.3%**
- **Dir: ?**  •  HTF20 mildly against; 4h trend WITH trade; RSI 60-70 strong  •  AVOID when HTF60 aligned WITH trade

### W11.  `H20=H20a AND T4=T4c AND BBP=BBP5 AND RSI=RSI5`
- Raw: n=130  W=120/L=10  WR=92.3%
- Refine: exclude session_bucket=ny_close drops 6/10 losers (60%)
- **Final: n=124  W=120/L=4  WR=96.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; just touched upper band; RSI 60-70 strong  •  AVOID when session=ny_close

### W12.  `H20=H20a AND T1=T1c AND T4=T4c AND ZS=ZS5`
- Raw: n=128  W=109/L=19  WR=85.2%
- Refine: exclude RSI=RSI4 drops 19/19 losers (100%)
- **Final: n=63  W=63/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; zscore +2 to +3 deep overbought  •  AVOID when RSI 50-60 upper neutral

### W13.  `H60=H60a AND T1=T1c AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=124  W=108/L=16  WR=87.1%
- Refine: exclude T4=T4c drops 16/16 losers (100%)
- **Final: n=49  W=49/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  AVOID when 4h trend AGAINST trade

### W14.  `H20=H20a AND RSI=RSI5 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=116  W=99/L=17  WR=85.3%
- Refine: exclude T4=T4a drops 17/17 losers (100%)
- **Final: n=85  W=85/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  AVOID when 4h trend WITH trade

### W15.  `H20=H20a AND T1=T1c AND T4=T4c AND BBP=BBP5`
- Raw: n=110  W=95/L=15  WR=86.4%
- Refine: exclude RSI=RSI4 drops 15/15 losers (100%)
- **Final: n=51  W=51/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend AGAINST trade; just touched upper band  •  AVOID when RSI 50-60 upper neutral

### W16.  `H60=H60d AND T1=T1c AND T4=T4a AND RSI=RSI4`
- Raw: n=106  W=92/L=14  WR=86.8%
- Refine: exclude ZS=ZS6 drops 6/14 losers (43%)
- **Final: n=100  W=92/L=8  WR=92.0%**
- **Dir: ?**  •  HTF60 mildly against; 1h trend AGAINST trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when zscore >+3 extreme

### W17.  `H60=H60d AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=105  W=96/L=9  WR=91.4%
- Refine: exclude T1=T1c drops 9/9 losers (100%)
- **Final: n=76  W=76/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 mildly against; RSI 60-70 strong; session=asia  •  AVOID when 1h trend AGAINST trade

### W18.  `H20=H20a AND H60=H60d AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=105  W=96/L=9  WR=91.4%
- Refine: exclude T1=T1c drops 9/9 losers (100%)
- **Final: n=76  W=76/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 mildly against; RSI 60-70 strong; session=asia  •  AVOID when 1h trend AGAINST trade

### W19.  `H60=H60a AND T4=T4a AND BBP=BBP6 AND ZS=ZS5`
- Raw: n=101  W=86/L=15  WR=85.1%
- Refine: exclude T1=T1a drops 15/15 losers (100%)
- **Final: n=24  W=24/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; deep above upper band; zscore +2 to +3 deep overbought  •  AVOID when 1h trend WITH trade

### W20.  `H20=H20a AND T1=T1a AND BBP=BBP5 AND RSI=RSI5`
- Raw: n=100  W=90/L=10  WR=90.0%
- Refine: exclude session_bucket=ny_close drops 6/10 losers (60%)
- **Final: n=94  W=90/L=4  WR=95.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; just touched upper band; RSI 60-70 strong  •  AVOID when session=ny_close

### W21.  `H20=H20a AND T4=T4c AND session_bucket=asia_late`
- Raw: n=97  W=83/L=14  WR=85.6%
- Refine: exclude T1=T1c drops 13/14 losers (93%)
- **Final: n=41  W=40/L=1  WR=97.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; session=asia_late  •  AVOID when 1h trend AGAINST trade

### W22.  `H60=H60a AND T1=T1c AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=95  W=82/L=13  WR=86.3%
- Refine: exclude direction_exec=short drops 13/13 losers (100%)
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; zscore +2 to +3 deep overbought; session=asia  •  AVOID when short

### W23.  `H20=H20a AND H60=H60d AND BBP=BBP5`
- Raw: n=94  W=81/L=13  WR=86.2%
- Refine: exclude session_bucket=ny_close drops 6/13 losers (46%)
- **Final: n=80  W=73/L=7  WR=91.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 mildly against; just touched upper band  •  AVOID when session=ny_close

### W24.  `H20=H20a AND H60=H60d AND BBP=BBP5 AND ZS=ZS5`
- Raw: n=94  W=81/L=13  WR=86.2%
- Refine: exclude session_bucket=ny_close drops 6/13 losers (46%)
- **Final: n=80  W=73/L=7  WR=91.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 mildly against; just touched upper band; zscore +2 to +3 deep overbought  •  AVOID when session=ny_close

### W25.  `H20=H20a AND T4=T4c AND BBP=BBP5 AND session_bucket=asia`
- Raw: n=92  W=81/L=11  WR=88.0%
- Refine: exclude H60=H60a drops 11/11 losers (100%)
- **Final: n=48  W=48/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; just touched upper band; session=asia  •  AVOID when HTF60 aligned WITH trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND T1=T1a AND T4=T4c AND RSI=RSI4`
- Raw: n=155  W=62/L=93  WR=40.0%
- Sharpen: sharpest is H20=H20e (55/93 of losers there)
- **Sharp: n=70  W=15/L=55  WR=21.4%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when HTF20 strongly against

### L02.  `H20=H20c AND H60=H60e AND T4=T4c`
- Raw: n=153  W=52/L=101  WR=34.0%
- Sharpen: sharpest is session_bucket=ny_close (30/101 of losers there)
- **Sharp: n=37  W=7/L=30  WR=18.9%**
- **Dir: ?**  •  HTF20 neutral; HTF60 strongly against; 4h trend AGAINST trade  •  ONLY when session=ny_close

### L03.  `H20=H20c AND H60=H60e AND direction_exec=short`
- Raw: n=133  W=47/L=86  WR=35.3%
- Sharpen: sharpest is session_bucket=ny_close (30/86 of losers there)
- **Sharp: n=37  W=7/L=30  WR=18.9%**
- **Dir: SHORT**  •  HTF20 neutral; HTF60 strongly against  •  ONLY when session=ny_close

### L04.  `H20=H20c AND H60=H60e AND T4=T4c AND direction_exec=short`
- Raw: n=133  W=47/L=86  WR=35.3%
- Sharpen: sharpest is session_bucket=ny_close (30/86 of losers there)
- **Sharp: n=37  W=7/L=30  WR=18.9%**
- **Dir: SHORT**  •  HTF20 neutral; HTF60 strongly against; 4h trend AGAINST trade  •  ONLY when session=ny_close

### L05.  `H20=H20b AND T1=T1c AND RSI=RSI5`
- Raw: n=130  W=48/L=82  WR=36.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=130  W=48/L=82  WR=36.9%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend AGAINST trade; RSI 60-70 strong

### L06.  `H20=H20b AND RSI=RSI5 AND direction_exec=short`
- Raw: n=130  W=48/L=82  WR=36.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=130  W=48/L=82  WR=36.9%**
- **Dir: SHORT**  •  HTF20 slightly aligned; RSI 60-70 strong

### L07.  `H20=H20b AND T1=T1c AND RSI=RSI5 AND direction_exec=short`
- Raw: n=130  W=48/L=82  WR=36.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=130  W=48/L=82  WR=36.9%**
- **Dir: SHORT**  •  HTF20 slightly aligned; 1h trend AGAINST trade; RSI 60-70 strong

### L08.  `H20=H20e AND T1=T1a AND direction_exec=short AND session_bucket=asia`
- Raw: n=122  W=43/L=79  WR=35.2%
- Sharpen: sharpest is H60=H60e (26/79 of losers there)
- **Sharp: n=26  W=0/L=26  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend WITH trade; session=asia  •  ONLY when HTF60 strongly against

### L09.  `H20=H20e AND BBP=BBP5 AND RSI=RSI5`
- Raw: n=119  W=37/L=82  WR=31.1%
- Sharpen: sharpest is H60=H60b (34/82 of losers there)
- **Sharp: n=39  W=5/L=34  WR=12.8%**
- **Dir: ?**  •  HTF20 strongly against; just touched upper band; RSI 60-70 strong  •  ONLY when HTF60 slightly aligned

### L10.  `H20=H20e AND BBP=BBP5 AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=119  W=37/L=82  WR=31.1%
- Sharpen: sharpest is H60=H60b (34/82 of losers there)
- **Sharp: n=39  W=5/L=34  WR=12.8%**
- **Dir: ?**  •  HTF20 strongly against; just touched upper band; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  ONLY when HTF60 slightly aligned

### L11.  `H20=H20c AND H60=H60e AND session_bucket=asia`
- Raw: n=116  W=32/L=84  WR=27.6%
- Sharpen: sharpest is direction_exec=long (47/84 of losers there)
- **Sharp: n=52  W=5/L=47  WR=9.6%**
- **Dir: ?**  •  HTF20 neutral; HTF60 strongly against; session=asia  •  ONLY when long

### L12.  `H20=H20e AND T1=T1a AND RSI=RSI4 AND direction_exec=short`
- Raw: n=114  W=35/L=79  WR=30.7%
- Sharpen: sharpest is H60=H60e (26/79 of losers there)
- **Sharp: n=26  W=0/L=26  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when HTF60 strongly against

### L13.  `H20=H20e AND BBP=BBP5 AND direction_exec=short`
- Raw: n=113  W=45/L=68  WR=39.8%
- Sharpen: sharpest is H60=H60b (43/68 of losers there)
- **Sharp: n=54  W=11/L=43  WR=20.4%**
- **Dir: SHORT**  •  HTF20 strongly against; just touched upper band  •  ONLY when HTF60 slightly aligned

### L14.  `H20=H20e AND BBP=BBP5 AND ZS=ZS5 AND direction_exec=short`
- Raw: n=113  W=45/L=68  WR=39.8%
- Sharpen: sharpest is H60=H60b (43/68 of losers there)
- **Sharp: n=54  W=11/L=43  WR=20.4%**
- **Dir: SHORT**  •  HTF20 strongly against; just touched upper band; zscore +2 to +3 deep overbought  •  ONLY when HTF60 slightly aligned

### L15.  `H20=H20c AND H60=H60e AND T1=T1a`
- Raw: n=109  W=38/L=71  WR=34.9%
- Sharpen: sharpest is RSI=RSI3 (42/71 of losers there)
- **Sharp: n=47  W=5/L=42  WR=10.6%**
- **Dir: ?**  •  HTF20 neutral; HTF60 strongly against; 1h trend WITH trade  •  ONLY when RSI 40-50 lower neutral

### L16.  `H20=H20c AND H60=H60e AND RSI=RSI4`
- Raw: n=108  W=38/L=70  WR=35.2%
- Sharpen: sharpest is BBP=BBP4 (34/70 of losers there)
- **Sharp: n=38  W=4/L=34  WR=10.5%**
- **Dir: ?**  •  HTF20 neutral; HTF60 strongly against; RSI 50-60 upper neutral  •  ONLY when upper third

### L17.  `H60=H60e AND T1=T1a AND direction_exec=short`
- Raw: n=107  W=40/L=67  WR=37.4%
- Sharpen: sharpest is H20=H20e (26/67 of losers there)
- **Sharp: n=26  W=0/L=26  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend WITH trade  •  ONLY when HTF20 strongly against

### L18.  `H60=H60e AND T1=T1a AND T4=T4c AND direction_exec=short`
- Raw: n=107  W=40/L=67  WR=37.4%
- Sharpen: sharpest is H20=H20e (26/67 of losers there)
- **Sharp: n=26  W=0/L=26  WR=0.0%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend WITH trade; 4h trend AGAINST trade  •  ONLY when HTF20 strongly against

### L19.  `H20=H20b AND T4=T4c AND RSI=RSI5`
- Raw: n=106  W=37/L=69  WR=34.9%
- Sharpen: sharpest is session_bucket=asia (42/69 of losers there)
- **Sharp: n=50  W=8/L=42  WR=16.0%**
- **Dir: ?**  •  HTF20 slightly aligned; 4h trend AGAINST trade; RSI 60-70 strong  •  ONLY when session=asia

### L20.  `H60=H60e AND T4=T4c AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=105  W=37/L=68  WR=35.2%
- Sharpen: sharpest is H20=H20e (35/68 of losers there)
- **Sharp: n=47  W=12/L=35  WR=25.5%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; zscore +2 to +3 deep overbought; session=asia  •  ONLY when HTF20 strongly against

### L21.  `H20=H20c AND H60=H60e AND T1=T1c`
- Raw: n=104  W=36/L=68  WR=34.6%
- Sharpen: sharpest is session_bucket=ny_close (22/68 of losers there)
- **Sharp: n=27  W=5/L=22  WR=18.5%**
- **Dir: ?**  •  HTF20 neutral; HTF60 strongly against; 1h trend AGAINST trade  •  ONLY when session=ny_close

### L22.  `H20=H20e AND H60=H60e AND T1=T1a AND T4=T4c`
- Raw: n=104  W=40/L=64  WR=38.5%
- Sharpen: sharpest is RSI=RSI4 (55/64 of losers there)
- **Sharp: n=70  W=15/L=55  WR=21.4%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend WITH trade; 4h trend AGAINST trade  •  ONLY when RSI 50-60 upper neutral

### L23.  `H20=H20c AND H60=H60e AND T1=T1c AND T4=T4c`
- Raw: n=103  W=36/L=67  WR=35.0%
- Sharpen: sharpest is session_bucket=ny_close (22/67 of losers there)
- **Sharp: n=27  W=5/L=22  WR=18.5%**
- **Dir: ?**  •  HTF20 neutral; HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade  •  ONLY when session=ny_close

### L24.  `H20=H20c AND H60=H60e AND T1=T1c AND direction_exec=short`
- Raw: n=103  W=36/L=67  WR=35.0%
- Sharpen: sharpest is session_bucket=ny_close (22/67 of losers there)
- **Sharp: n=27  W=5/L=22  WR=18.5%**
- **Dir: SHORT**  •  HTF20 neutral; HTF60 strongly against; 1h trend AGAINST trade  •  ONLY when session=ny_close

### L25.  `T1=T1a AND BBP=BBP3 AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=100  W=37/L=63  WR=37.0%
- Sharpen: sharpest is direction_exec=short (22/63 of losers there)
- **Sharp: n=25  W=3/L=22  WR=12.0%**
- **Dir: ?**  •  1h trend WITH trade; middle of band; RSI 50-60 upper neutral; session=asia  •  ONLY when short

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | H60a(39/34) | H60e(33/41) |
| T1 | — | — |
| T4 | T4a(54/46) | T4c(46/54) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
