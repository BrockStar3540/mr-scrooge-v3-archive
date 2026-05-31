# CAD_JPY — R32 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20c**  (EMA20 flat)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **2,622**  (W=1,727 / L=895)  -  WR: **65.9%**

## Session distribution

- asia: n=952  W=641/L=311  WR=67.3%
- london_open: n=383  W=259/L=124  WR=67.6%
- ny_close: n=376  W=246/L=130  WR=65.4%
- ny_mid: n=347  W=223/L=124  WR=64.3%
- ny_open: n=202  W=122/L=80  WR=60.4%
- london: n=196  W=134/L=62  WR=68.4%
- asia_late: n=126  W=73/L=53  WR=57.9%
- off_hours: n=40  W=29/L=11  WR=72.5%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND H60=H60a AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=313  W=267/L=46  WR=85.3%
- Refine: no further refinement
- **Final: n=313  W=267/L=46  WR=85.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; upper third; RSI 50-60 upper neutral

### W02.  `T1=T1a AND T4=T4c AND session_bucket=asia`
- Raw: n=296  W=260/L=36  WR=87.8%
- Refine: exclude RSI=RSI3 drops 25/36 losers (69%)
- **Final: n=188  W=177/L=11  WR=94.1%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; session=asia  •  AVOID when RSI 40-50 lower neutral

### W03.  `H20=H20a AND RSI=RSI4 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=291  W=250/L=41  WR=85.9%
- Refine: no further refinement
- **Final: n=291  W=250/L=41  WR=85.9%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought

### W04.  `H20=H20a AND H60=H60a AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=287  W=248/L=39  WR=86.4%
- Refine: exclude session_bucket=london_open drops 8/39 losers (21%)
- **Final: n=266  W=235/L=31  WR=88.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when session=london_open

### W05.  `T4=T4c AND BBP=BBP4 AND session_bucket=asia`
- Raw: n=209  W=181/L=28  WR=86.6%
- Refine: exclude H60=H60e drops 25/28 losers (89%)
- **Final: n=87  W=84/L=3  WR=96.6%**
- **Dir: ?**  •  4h trend AGAINST trade; upper third; session=asia  •  AVOID when HTF60 strongly against

### W06.  `H60=H60a AND T1=T1c AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=181  W=155/L=26  WR=85.6%
- Refine: exclude session_bucket=asia drops 9/26 losers (35%)
- **Final: n=150  W=133/L=17  WR=88.7%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; upper third; RSI 50-60 upper neutral  •  AVOID when session=asia

### W07.  `H60=H60a AND T1=T1c AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=174  W=150/L=24  WR=86.2%
- Refine: exclude session_bucket=asia drops 9/24 losers (38%)
- **Final: n=143  W=128/L=15  WR=89.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when session=asia

### W08.  `T4=T4c AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=173  W=152/L=21  WR=87.9%
- Refine: exclude H60=H60e drops 19/21 losers (90%)
- **Final: n=78  W=76/L=2  WR=97.4%**
- **Dir: ?**  •  4h trend AGAINST trade; zscore +1 to +2 overbought; session=asia  •  AVOID when HTF60 strongly against

### W09.  `T4=T4c AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=173  W=152/L=21  WR=87.9%
- Refine: exclude H60=H60e drops 19/21 losers (90%)
- **Final: n=78  W=76/L=2  WR=97.4%**
- **Dir: ?**  •  4h trend AGAINST trade; upper third; zscore +1 to +2 overbought; session=asia  •  AVOID when HTF60 strongly against

### W10.  `T4=T4c AND direction_exec=long AND session_bucket=asia`
- Raw: n=168  W=158/L=10  WR=94.0%
- Refine: exclude RSI=RSI3 drops 10/10 losers (100%)
- **Final: n=116  W=116/L=0  WR=100.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; session=asia  •  AVOID when RSI 40-50 lower neutral

### W11.  `T4=T4c AND BBP=BBP4 AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=158  W=139/L=19  WR=88.0%
- Refine: exclude H60=H60e drops 19/19 losers (100%)
- **Final: n=76  W=76/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend AGAINST trade; upper third; RSI 50-60 upper neutral; session=asia  •  AVOID when HTF60 strongly against

### W12.  `H20=H20a AND H60=H60a AND T1=T1a AND T4=T4c`
- Raw: n=154  W=137/L=17  WR=89.0%
- Refine: exclude BBP=BBP5 drops 7/17 losers (41%)
- **Final: n=147  W=137/L=10  WR=93.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade  •  AVOID when just touched upper band

### W13.  `H20=H20a AND T1=T1a AND T4=T4c AND direction_exec=long`
- Raw: n=154  W=137/L=17  WR=89.0%
- Refine: exclude BBP=BBP5 drops 7/17 losers (41%)
- **Final: n=147  W=137/L=10  WR=93.2%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade  •  AVOID when just touched upper band

### W14.  `H20=H20a AND T4=T4c AND session_bucket=asia`
- Raw: n=147  W=132/L=15  WR=89.8%
- Refine: exclude H60=H60e drops 12/15 losers (80%)
- **Final: n=107  W=104/L=3  WR=97.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; session=asia  •  AVOID when HTF60 strongly against

### W15.  `H60=H60a AND T4=T4c AND session_bucket=asia`
- Raw: n=146  W=140/L=6  WR=95.9%
- Refine: exclude RSI=RSI3 drops 6/6 losers (100%)
- **Final: n=116  W=116/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=asia  •  AVOID when RSI 40-50 lower neutral

### W16.  `H60=H60a AND T4=T4c AND direction_exec=long AND session_bucket=asia`
- Raw: n=146  W=140/L=6  WR=95.9%
- Refine: exclude RSI=RSI3 drops 6/6 losers (100%)
- **Final: n=116  W=116/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; session=asia  •  AVOID when RSI 40-50 lower neutral

### W17.  `T4=T4c AND RSI=RSI4 AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=144  W=130/L=14  WR=90.3%
- Refine: exclude H60=H60e drops 14/14 losers (100%)
- **Final: n=74  W=74/L=0  WR=100.0%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought; session=asia  •  AVOID when HTF60 strongly against

### W18.  `T1=T1a AND T4=T4c AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=137  W=127/L=10  WR=92.7%
- Refine: exclude H60=H60e drops 10/10 losers (100%)
- **Final: n=88  W=88/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral; session=asia  •  AVOID when HTF60 strongly against

### W19.  `H20=H20a AND T4=T4c AND BBP=BBP4`
- Raw: n=136  W=118/L=18  WR=86.8%
- Refine: exclude session_bucket=ny_mid drops 11/18 losers (61%)
- **Final: n=120  W=113/L=7  WR=94.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; upper third  •  AVOID when session=ny_mid

### W20.  `H20=H20a AND BBP=BBP3 AND RSI=RSI4`
- Raw: n=136  W=118/L=18  WR=86.8%
- Refine: exclude T1=T1c drops 11/18 losers (61%)
- **Final: n=92  W=85/L=7  WR=92.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; middle of band; RSI 50-60 upper neutral  •  AVOID when 1h trend AGAINST trade

### W21.  `H20=H20a AND BBP=BBP3 AND RSI=RSI4 AND ZS=ZS3`
- Raw: n=136  W=118/L=18  WR=86.8%
- Refine: exclude T1=T1c drops 11/18 losers (61%)
- **Final: n=92  W=85/L=7  WR=92.4%**
- **Dir: ?**  •  HTF20 aligned WITH trade; middle of band; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  AVOID when 1h trend AGAINST trade

### W22.  `H20=H20a AND T1=T1a AND T4=T4c AND RSI=RSI4`
- Raw: n=132  W=117/L=15  WR=88.6%
- Refine: exclude BBP=BBP5 drops 7/15 losers (47%)
- **Final: n=125  W=117/L=8  WR=93.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when just touched upper band

### W23.  `H20=H20a AND T4=T4c AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=129  W=112/L=17  WR=86.8%
- Refine: exclude session_bucket=ny_mid drops 11/17 losers (65%)
- **Final: n=113  W=107/L=6  WR=94.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; upper third; RSI 50-60 upper neutral  •  AVOID when session=ny_mid

### W24.  `H20=H20a AND H60=H60a AND T1=T1a AND ZS=ZS3`
- Raw: n=128  W=113/L=15  WR=88.3%
- Refine: exclude BBP=BBP4 drops 6/15 losers (40%)
- **Final: n=102  W=93/L=9  WR=91.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; zscore -1 to +1 neutral  •  AVOID when upper third

### W25.  `H20=H20a AND T1=T1a AND ZS=ZS3 AND direction_exec=long`
- Raw: n=128  W=113/L=15  WR=88.3%
- Refine: exclude BBP=BBP4 drops 6/15 losers (40%)
- **Final: n=102  W=93/L=9  WR=91.2%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; zscore -1 to +1 neutral  •  AVOID when upper third

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND H60=H60e AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=227  W=90/L=137  WR=39.6%
- Sharpen: no sharper sub-pattern
- **Sharp: n=227  W=90/L=137  WR=39.6%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; RSI 50-60 upper neutral; zscore +1 to +2 overbought

### L02.  `T1=T1c AND T4=T4a AND session_bucket=asia`
- Raw: n=218  W=87/L=131  WR=39.9%
- Sharpen: sharpest is H60=H60e (57/131 of losers there)
- **Sharp: n=77  W=20/L=57  WR=26.0%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; session=asia  •  ONLY when HTF60 strongly against

### L03.  `T4=T4a AND BBP=BBP4 AND session_bucket=asia`
- Raw: n=152  W=60/L=92  WR=39.5%
- Sharpen: sharpest is H60=H60e (44/92 of losers there)
- **Sharp: n=60  W=16/L=44  WR=26.7%**
- **Dir: ?**  •  4h trend WITH trade; upper third; session=asia  •  ONLY when HTF60 strongly against

### L04.  `T1=T1a AND BBP=BBP4 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=144  W=57/L=87  WR=39.6%
- Sharpen: sharpest is session_bucket=london (15/87 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: SHORT**  •  1h trend WITH trade; upper third; RSI 50-60 upper neutral  •  ONLY when session=london

### L05.  `H20=H20e AND T1=T1a AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=143  W=55/L=88  WR=38.5%
- Sharpen: sharpest is session_bucket=london (21/88 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; upper third; RSI 50-60 upper neutral  •  ONLY when session=london

### L06.  `H60=H60e AND T1=T1a AND BBP=BBP4 AND RSI=RSI4`
- Raw: n=137  W=52/L=85  WR=38.0%
- Sharpen: sharpest is session_bucket=ny_mid (25/85 of losers there)
- **Sharp: n=29  W=4/L=25  WR=13.8%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; upper third; RSI 50-60 upper neutral  •  ONLY when session=ny_mid

### L07.  `T1=T1a AND RSI=RSI4 AND ZS=ZS4 AND direction_exec=short`
- Raw: n=137  W=53/L=84  WR=38.7%
- Sharpen: sharpest is session_bucket=ny_mid (25/84 of losers there)
- **Sharp: n=30  W=5/L=25  WR=16.7%**
- **Dir: SHORT**  •  1h trend WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when session=ny_mid

### L08.  `H20=H20e AND T1=T1a AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=136  W=52/L=84  WR=38.2%
- Sharpen: sharpest is session_bucket=london (21/84 of losers there)
- **Sharp: n=21  W=0/L=21  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when session=london

### L09.  `T4=T4a AND direction_exec=short AND session_bucket=asia`
- Raw: n=133  W=44/L=89  WR=33.1%
- Sharpen: sharpest is RSI=RSI4 (62/89 of losers there)
- **Sharp: n=76  W=14/L=62  WR=18.4%**
- **Dir: SHORT**  •  4h trend WITH trade; session=asia  •  ONLY when RSI 50-60 upper neutral

### L10.  `H60=H60e AND T1=T1a AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=130  W=48/L=82  WR=36.9%
- Sharpen: sharpest is session_bucket=ny_mid (25/82 of losers there)
- **Sharp: n=27  W=2/L=25  WR=7.4%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  ONLY when session=ny_mid

### L11.  `T4=T4a AND BBP=BBP4 AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=110  W=37/L=73  WR=33.6%
- Sharpen: sharpest is H60=H60e (43/73 of losers there)
- **Sharp: n=57  W=14/L=43  WR=24.6%**
- **Dir: ?**  •  4h trend WITH trade; upper third; RSI 50-60 upper neutral; session=asia  •  ONLY when HTF60 strongly against

### L12.  `H60=H60a AND T4=T4a AND ZS=ZS5`
- Raw: n=107  W=41/L=66  WR=38.3%
- Sharpen: sharpest is H20=H20a (52/66 of losers there)
- **Sharp: n=76  W=24/L=52  WR=31.6%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  ONLY when HTF20 aligned WITH trade

### L13.  `H60=H60a AND T4=T4a AND ZS=ZS5 AND direction_exec=long`
- Raw: n=107  W=41/L=66  WR=38.3%
- Sharpen: sharpest is H20=H20a (52/66 of losers there)
- **Sharp: n=76  W=24/L=52  WR=31.6%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend WITH trade; zscore +2 to +3 deep overbought  •  ONLY when HTF20 aligned WITH trade

### L14.  `H20=H20e AND T4=T4a AND session_bucket=asia`
- Raw: n=105  W=37/L=68  WR=35.2%
- Sharpen: sharpest is H60=H60e (54/68 of losers there)
- **Sharp: n=72  W=18/L=54  WR=25.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; session=asia  •  ONLY when HTF60 strongly against

### L15.  `H20=H20e AND H60=H60e AND T1=T1c AND T4=T4a`
- Raw: n=104  W=37/L=67  WR=35.6%
- Sharpen: sharpest is session_bucket=asia (54/67 of losers there)
- **Sharp: n=72  W=18/L=54  WR=25.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when session=asia

### L16.  `H20=H20e AND T1=T1c AND T4=T4a AND direction_exec=short`
- Raw: n=104  W=37/L=67  WR=35.6%
- Sharpen: sharpest is session_bucket=asia (54/67 of losers there)
- **Sharp: n=72  W=18/L=54  WR=25.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when session=asia

### L17.  `T4=T4a AND RSI=RSI4 AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=103  W=34/L=69  WR=33.0%
- Sharpen: sharpest is H60=H60e (42/69 of losers there)
- **Sharp: n=56  W=14/L=42  WR=25.0%**
- **Dir: ?**  •  4h trend WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought; session=asia  •  ONLY when HTF60 strongly against

### L18.  `T1=T1c AND T4=T4a AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=98  W=34/L=64  WR=34.7%
- Sharpen: sharpest is H60=H60e (45/64 of losers there)
- **Sharp: n=56  W=11/L=45  WR=19.6%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 50-60 upper neutral; session=asia  •  ONLY when HTF60 strongly against

### L19.  `H60=H60e AND T4=T4a AND session_bucket=asia`
- Raw: n=97  W=23/L=74  WR=23.7%
- Sharpen: sharpest is RSI=RSI4 (62/74 of losers there)
- **Sharp: n=76  W=14/L=62  WR=18.4%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; session=asia  •  ONLY when RSI 50-60 upper neutral

### L20.  `H60=H60e AND T4=T4a AND direction_exec=short AND session_bucket=asia`
- Raw: n=97  W=23/L=74  WR=23.7%
- Sharpen: sharpest is RSI=RSI4 (62/74 of losers there)
- **Sharp: n=76  W=14/L=62  WR=18.4%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend WITH trade; session=asia  •  ONLY when RSI 50-60 upper neutral

### L21.  `H20=H20a AND T1=T1a AND ZS=ZS5`
- Raw: n=97  W=38/L=59  WR=39.2%
- Sharpen: sharpest is RSI=RSI4 (55/59 of losers there)
- **Sharp: n=77  W=22/L=55  WR=28.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; zscore +2 to +3 deep overbought  •  ONLY when RSI 50-60 upper neutral

### L22.  `H20=H20e AND H60=H60e AND session_bucket=ny_close`
- Raw: n=90  W=36/L=54  WR=40.0%
- Sharpen: sharpest is T1=T1a (21/54 of losers there)
- **Sharp: n=23  W=2/L=21  WR=8.7%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; session=ny_close  •  ONLY when 1h trend WITH trade

### L23.  `H20=H20e AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=90  W=36/L=54  WR=40.0%
- Sharpen: sharpest is T1=T1a (21/54 of losers there)
- **Sharp: n=23  W=2/L=21  WR=8.7%**
- **Dir: SHORT**  •  HTF20 strongly against; session=ny_close  •  ONLY when 1h trend WITH trade

### L24.  `H20=H20e AND H60=H60e AND direction_exec=short AND session_bucket=ny_close`
- Raw: n=90  W=36/L=54  WR=40.0%
- Sharpen: sharpest is T1=T1a (21/54 of losers there)
- **Sharp: n=23  W=2/L=21  WR=8.7%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; session=ny_close  •  ONLY when 1h trend WITH trade

### L25.  `H20=H20e AND T1=T1c AND T4=T4a AND RSI=RSI4`
- Raw: n=89  W=31/L=58  WR=34.8%
- Sharpen: sharpest is session_bucket=asia (44/58 of losers there)
- **Sharp: n=55  W=11/L=44  WR=20.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when session=asia

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(49/41) | H20e(40/48) |
| H60 | H60a(50/42) | H60e(44/53) |
| T1 | — | — |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(53/44) | short(47/56) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
