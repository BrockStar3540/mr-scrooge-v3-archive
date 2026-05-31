# GBP_JPY — R37 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50b**  (EMA50 up 0.15-0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **5,870**  (W=3,637 / L=2,233)  -  WR: **62.0%**

## Session distribution

- asia: n=2738  W=1697/L=1041  WR=62.0%
- ny_close: n=1338  W=834/L=504  WR=62.3%
- off_hours: n=417  W=262/L=155  WR=62.8%
- london: n=414  W=262/L=152  WR=63.3%
- asia_late: n=311  W=181/L=130  WR=58.2%
- ny_open: n=262  W=150/L=112  WR=57.3%
- london_open: n=222  W=141/L=81  WR=63.5%
- ny_mid: n=168  W=110/L=58  WR=65.5%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H60=H60d AND T1=T1c AND T4=T4a`
- Raw: n=120  W=104/L=16  WR=86.7%
- Refine: exclude session_bucket=london_open drops 7/16 losers (44%)
- **Final: n=113  W=104/L=9  WR=92.0%**
- **Dir: ?**  •  HTF60 mildly against; 1h trend AGAINST trade; 4h trend WITH trade  •  AVOID when session=london_open

### W02.  `H20=H20e AND RSI=RSI4 AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=119  W=109/L=10  WR=91.6%
- Refine: exclude strategy_id=delta_tag_and_go_v2 drops 3/10 losers (30%)
- **Final: n=105  W=98/L=7  WR=93.3%**
- **Dir: ?**  •  HTF20 strongly against; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought; session=asia  •  AVOID when strategy=delta_tag_and_go_v2

### W03.  `H60=H60d AND T1=T1c AND T4=T4a AND RSI=RSI4`
- Raw: n=108  W=93/L=15  WR=86.1%
- Refine: exclude session_bucket=london_open drops 7/15 losers (47%)
- **Final: n=101  W=93/L=8  WR=92.1%**
- **Dir: ?**  •  HTF60 mildly against; 1h trend AGAINST trade; 4h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when session=london_open

### W04.  `BBP=BBP0 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=107  W=92/L=15  WR=86.0%
- Refine: exclude T4=T4c drops 9/15 losers (60%)
- **Final: n=75  W=69/L=6  WR=92.0%**
- **Dir: LONG**  •  deep below lower band; RSI 50-60 upper neutral  •  AVOID when 4h trend AGAINST trade

### W05.  `H20=H20e AND H60=H60d AND T4=T4a`
- Raw: n=102  W=87/L=15  WR=85.3%
- Refine: exclude session_bucket=london_open drops 7/15 losers (47%)
- **Final: n=95  W=87/L=8  WR=91.6%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 mildly against; 4h trend WITH trade  •  AVOID when session=london_open

### W06.  `H60=H60d AND T4=T4a AND direction_exec=short`
- Raw: n=102  W=87/L=15  WR=85.3%
- Refine: exclude session_bucket=london_open drops 7/15 losers (47%)
- **Final: n=95  W=87/L=8  WR=91.6%**
- **Dir: SHORT**  •  HTF60 mildly against; 4h trend WITH trade  •  AVOID when session=london_open

### W07.  `H20=H20e AND H60=H60d AND T1=T1c AND T4=T4a`
- Raw: n=102  W=87/L=15  WR=85.3%
- Refine: exclude session_bucket=london_open drops 7/15 losers (47%)
- **Final: n=95  W=87/L=8  WR=91.6%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 mildly against; 1h trend AGAINST trade; 4h trend WITH trade  •  AVOID when session=london_open

### W08.  `H20=H20e AND H60=H60d AND T4=T4a AND direction_exec=short`
- Raw: n=102  W=87/L=15  WR=85.3%
- Refine: exclude session_bucket=london_open drops 7/15 losers (47%)
- **Final: n=95  W=87/L=8  WR=91.6%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 mildly against; 4h trend WITH trade  •  AVOID when session=london_open

### W09.  `H60=H60d AND T1=T1c AND T4=T4a AND direction_exec=short`
- Raw: n=102  W=87/L=15  WR=85.3%
- Refine: exclude session_bucket=london_open drops 7/15 losers (47%)
- **Final: n=95  W=87/L=8  WR=91.6%**
- **Dir: SHORT**  •  HTF60 mildly against; 1h trend AGAINST trade; 4h trend WITH trade  •  AVOID when session=london_open

### W10.  `H20=H20e AND T1=T1a AND BBP=BBP6`
- Raw: n=101  W=96/L=5  WR=95.0%
- Refine: exclude session_bucket=ny_mid drops 4/5 losers (80%)
- **Final: n=97  W=96/L=1  WR=99.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; deep above upper band  •  AVOID when session=ny_mid

### W11.  `H20=H20e AND BBP=BBP6 AND session_bucket=asia`
- Raw: n=101  W=89/L=12  WR=88.1%
- Refine: exclude H60=H60e drops 11/12 losers (92%)
- **Final: n=39  W=38/L=1  WR=97.4%**
- **Dir: ?**  •  HTF20 strongly against; deep above upper band; session=asia  •  AVOID when HTF60 strongly against

### W12.  `H20=H20e AND BBP=BBP6 AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=101  W=89/L=12  WR=88.1%
- Refine: exclude H60=H60e drops 11/12 losers (92%)
- **Final: n=39  W=38/L=1  WR=97.4%**
- **Dir: ?**  •  HTF20 strongly against; deep above upper band; zscore +2 to +3 deep overbought; session=asia  •  AVOID when HTF60 strongly against

### W13.  `H20=H20e AND H60=H60d AND T4=T4a AND RSI=RSI4`
- Raw: n=100  W=85/L=15  WR=85.0%
- Refine: exclude session_bucket=london_open drops 7/15 losers (47%)
- **Final: n=93  W=85/L=8  WR=91.4%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 mildly against; 4h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when session=london_open

### W14.  `H60=H60d AND T4=T4a AND RSI=RSI4 AND direction_exec=short`
- Raw: n=100  W=85/L=15  WR=85.0%
- Refine: exclude session_bucket=london_open drops 7/15 losers (47%)
- **Final: n=93  W=85/L=8  WR=91.4%**
- **Dir: SHORT**  •  HTF60 mildly against; 4h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when session=london_open

### W15.  `H60=H60e AND T1=T1a AND BBP=BBP2`
- Raw: n=99  W=87/L=12  WR=87.9%
- Refine: exclude T4=T4c drops 11/12 losers (92%)
- **Final: n=50  W=49/L=1  WR=98.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend WITH trade; lower third  •  AVOID when 4h trend AGAINST trade

### W16.  `H20=H20e AND T1=T1a AND T4=T4c AND session_bucket=asia`
- Raw: n=99  W=86/L=13  WR=86.9%
- Refine: exclude BBP=BBP0 drops 6/13 losers (46%)
- **Final: n=92  W=85/L=7  WR=92.4%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; 4h trend AGAINST trade; session=asia  •  AVOID when deep below lower band

### W17.  `T1=T1a AND T4=T4a AND session_bucket=ny_open`
- Raw: n=98  W=84/L=14  WR=85.7%
- Refine: exclude BBP=BBP4 drops 10/14 losers (71%)
- **Final: n=53  W=49/L=4  WR=92.5%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; session=ny_open  •  AVOID when upper third

### W18.  `T1=T1a AND T4=T4a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=98  W=84/L=14  WR=85.7%
- Refine: exclude BBP=BBP4 drops 10/14 losers (71%)
- **Final: n=53  W=49/L=4  WR=92.5%**
- **Dir: LONG**  •  1h trend WITH trade; 4h trend WITH trade; session=ny_open  •  AVOID when upper third

### W19.  `H20=H20e AND T4=T4a AND BBP=BBP6`
- Raw: n=97  W=84/L=13  WR=86.6%
- Refine: exclude RSI=RSI5 drops 13/13 losers (100%)
- **Final: n=56  W=56/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; deep above upper band  •  AVOID when RSI 60-70 strong

### W20.  `H20=H20a AND T1=T1a AND session_bucket=ny_open`
- Raw: n=97  W=83/L=14  WR=85.6%
- Refine: exclude T4=T4c drops 8/14 losers (57%)
- **Final: n=64  W=58/L=6  WR=90.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=ny_open  •  AVOID when 4h trend AGAINST trade

### W21.  `H20=H20a AND H60=H60a AND T1=T1a AND session_bucket=ny_open`
- Raw: n=97  W=83/L=14  WR=85.6%
- Refine: exclude T4=T4c drops 8/14 losers (57%)
- **Final: n=64  W=58/L=6  WR=90.6%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; 1h trend WITH trade; session=ny_open  •  AVOID when 4h trend AGAINST trade

### W22.  `H20=H20a AND T1=T1a AND direction_exec=long AND session_bucket=ny_open`
- Raw: n=97  W=83/L=14  WR=85.6%
- Refine: exclude T4=T4c drops 8/14 losers (57%)
- **Final: n=64  W=58/L=6  WR=90.6%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; 1h trend WITH trade; session=ny_open  •  AVOID when 4h trend AGAINST trade

### W23.  `H60=H60a AND BBP=BBP0 AND RSI=RSI4`
- Raw: n=96  W=83/L=13  WR=86.5%
- Refine: exclude T4=T4c drops 10/13 losers (77%)
- **Final: n=63  W=60/L=3  WR=95.2%**
- **Dir: ?**  •  HTF60 aligned WITH trade; deep below lower band; RSI 50-60 upper neutral  •  AVOID when 4h trend AGAINST trade

### W24.  `H60=H60a AND BBP=BBP0 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=95  W=83/L=12  WR=87.4%
- Refine: exclude T4=T4c drops 9/12 losers (75%)
- **Final: n=63  W=60/L=3  WR=95.2%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; deep below lower band; RSI 50-60 upper neutral  •  AVOID when 4h trend AGAINST trade

### W25.  `H60=H60e AND T4=T4c AND ZS=ZS3 AND session_bucket=ny_close`
- Raw: n=94  W=84/L=10  WR=89.4%
- Refine: no further refinement
- **Final: n=94  W=84/L=10  WR=89.4%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; zscore -1 to +1 neutral; session=ny_close

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20a AND RSI=RSI4 AND ZS=ZS5`
- Raw: n=199  W=78/L=121  WR=39.2%
- Sharpen: sharpest is session_bucket=asia (76/121 of losers there)
- **Sharp: n=91  W=15/L=76  WR=16.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought  •  ONLY when session=asia

### L02.  `T1=T1c AND T4=T4a AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=159  W=63/L=96  WR=39.6%
- Sharpen: sharpest is H20=H20a (27/96 of losers there)
- **Sharp: n=28  W=1/L=27  WR=3.6%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; zscore +1 to +2 overbought; session=asia  •  ONLY when HTF20 aligned WITH trade

### L03.  `H60=H60e AND T4=T4a AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=151  W=60/L=91  WR=39.7%
- Sharpen: sharpest is T1=T1c (82/91 of losers there)
- **Sharp: n=123  W=41/L=82  WR=33.3%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; RSI 60-70 strong; session=asia  •  ONLY when 1h trend AGAINST trade

### L04.  `H60=H60e AND T4=T4a AND BBP=BBP4 AND session_bucket=asia`
- Raw: n=147  W=54/L=93  WR=36.7%
- Sharpen: sharpest is H20=H20a (20/93 of losers there)
- **Sharp: n=21  W=1/L=20  WR=4.8%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; upper third; session=asia  •  ONLY when HTF20 aligned WITH trade

### L05.  `H60=H60e AND T4=T4a AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=143  W=52/L=91  WR=36.4%
- Sharpen: sharpest is H20=H20a (20/91 of losers there)
- **Sharp: n=21  W=1/L=20  WR=4.8%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend WITH trade; zscore +1 to +2 overbought; session=asia  •  ONLY when HTF20 aligned WITH trade

### L06.  `H20=H20a AND T1=T1c AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=134  W=51/L=83  WR=38.1%
- Sharpen: sharpest is ZS=ZS5 (27/83 of losers there)
- **Sharp: n=27  W=0/L=27  WR=0.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; RSI 50-60 upper neutral; session=asia  •  ONLY when zscore +2 to +3 deep overbought

### L07.  `H20=H20a AND H60=H60e AND T1=T1c AND T4=T4a`
- Raw: n=130  W=51/L=79  WR=39.2%
- Sharpen: sharpest is session_bucket=asia (53/79 of losers there)
- **Sharp: n=60  W=7/L=53  WR=11.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when session=asia

### L08.  `H20=H20a AND T1=T1c AND T4=T4a AND direction_exec=short`
- Raw: n=130  W=51/L=79  WR=39.2%
- Sharpen: sharpest is session_bucket=asia (53/79 of losers there)
- **Sharp: n=60  W=7/L=53  WR=11.7%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when session=asia

### L09.  `T1=T1c AND T4=T4a AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=125  W=43/L=82  WR=34.4%
- Sharpen: no sharper sub-pattern
- **Sharp: n=125  W=43/L=82  WR=34.4%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend WITH trade; RSI 60-70 strong; session=asia

### L10.  `T4=T4a AND RSI=RSI5 AND direction_exec=short AND session_bucket=asia`
- Raw: n=125  W=43/L=82  WR=34.4%
- Sharpen: no sharper sub-pattern
- **Sharp: n=125  W=43/L=82  WR=34.4%**
- **Dir: SHORT**  •  4h trend WITH trade; RSI 60-70 strong; session=asia

### L11.  `H20=H20a AND T4=T4a AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=124  W=46/L=78  WR=37.1%
- Sharpen: sharpest is RSI=RSI4 (60/78 of losers there)
- **Sharp: n=71  W=11/L=60  WR=15.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; zscore +2 to +3 deep overbought; session=asia  •  ONLY when RSI 50-60 upper neutral

### L12.  `H20=H20a AND H60=H60e AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=120  W=43/L=77  WR=35.8%
- Sharpen: sharpest is T4=T4a (45/77 of losers there)
- **Sharp: n=52  W=7/L=45  WR=13.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 strongly against; RSI 50-60 upper neutral; session=asia  •  ONLY when 4h trend WITH trade

### L13.  `H20=H20a AND RSI=RSI4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=120  W=43/L=77  WR=35.8%
- Sharpen: sharpest is T4=T4a (45/77 of losers there)
- **Sharp: n=52  W=7/L=45  WR=13.5%**
- **Dir: SHORT**  •  HTF20 aligned WITH trade; RSI 50-60 upper neutral; session=asia  •  ONLY when 4h trend WITH trade

### L14.  `T1=T1c AND RSI=RSI4 AND ZS=ZS1 AND direction_exec=short`
- Raw: n=120  W=47/L=73  WR=39.2%
- Sharpen: sharpest is T4=T4c (41/73 of losers there)
- **Sharp: n=58  W=17/L=41  WR=29.3%**
- **Dir: SHORT**  •  1h trend AGAINST trade; RSI 50-60 upper neutral; zscore -3 to -2 deep oversold  •  ONLY when 4h trend AGAINST trade

### L15.  `H60=H60b AND T4=T4c AND session_bucket=asia`
- Raw: n=114  W=37/L=77  WR=32.5%
- Sharpen: sharpest is ZS=ZS3 (18/77 of losers there)
- **Sharp: n=20  W=2/L=18  WR=10.0%**
- **Dir: ?**  •  HTF60 slightly aligned; 4h trend AGAINST trade; session=asia  •  ONLY when zscore -1 to +1 neutral

### L16.  `H60=H60b AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=110  W=43/L=67  WR=39.1%
- Sharpen: sharpest is T4=T4c (67/67 of losers there)
- **Sharp: n=96  W=29/L=67  WR=30.2%**
- **Dir: ?**  •  HTF60 slightly aligned; RSI 50-60 upper neutral; session=asia  •  ONLY when 4h trend AGAINST trade

### L17.  `T4=T4c AND ZS=ZS1 AND direction_exec=short`
- Raw: n=104  W=40/L=64  WR=38.5%
- Sharpen: sharpest is session_bucket=asia (35/64 of losers there)
- **Sharp: n=43  W=8/L=35  WR=18.6%**
- **Dir: SHORT**  •  4h trend AGAINST trade; zscore -3 to -2 deep oversold  •  ONLY when session=asia

### L18.  `H60=H60e AND T1=T1c AND RSI=RSI4 AND ZS=ZS1`
- Raw: n=103  W=39/L=64  WR=37.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=103  W=39/L=64  WR=37.9%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; RSI 50-60 upper neutral; zscore -3 to -2 deep oversold

### L19.  `H60=H60e AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=102  W=32/L=70  WR=31.4%
- Sharpen: sharpest is RSI=RSI5 (48/70 of losers there)
- **Sharp: n=53  W=5/L=48  WR=9.4%**
- **Dir: SHORT**  •  HTF60 strongly against; session=ny_open  •  ONLY when RSI 60-70 strong

### L20.  `T1=T1c AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=100  W=26/L=74  WR=26.0%
- Sharpen: sharpest is RSI=RSI5 (53/74 of losers there)
- **Sharp: n=58  W=5/L=53  WR=8.6%**
- **Dir: SHORT**  •  1h trend AGAINST trade; session=ny_open  •  ONLY when RSI 60-70 strong

### L21.  `RSI=RSI4 AND direction_exec=long AND session_bucket=asia_late`
- Raw: n=100  W=39/L=61  WR=39.0%
- Sharpen: sharpest is T1=T1c (32/61 of losers there)
- **Sharp: n=39  W=7/L=32  WR=17.9%**
- **Dir: LONG**  •  RSI 50-60 upper neutral; session=asia_late  •  ONLY when 1h trend AGAINST trade

### L22.  `H60=H60b AND T4=T4c AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=96  W=29/L=67  WR=30.2%
- Sharpen: sharpest is ZS=ZS3 (18/67 of losers there)
- **Sharp: n=20  W=2/L=18  WR=10.0%**
- **Dir: ?**  •  HTF60 slightly aligned; 4h trend AGAINST trade; RSI 50-60 upper neutral; session=asia  •  ONLY when zscore -1 to +1 neutral

### L23.  `T4=T4c AND ZS=ZS1 AND session_bucket=asia`
- Raw: n=96  W=37/L=59  WR=38.5%
- Sharpen: sharpest is direction_exec=short (35/59 of losers there)
- **Sharp: n=43  W=8/L=35  WR=18.6%**
- **Dir: ?**  •  4h trend AGAINST trade; zscore -3 to -2 deep oversold; session=asia  •  ONLY when short

### L24.  `H60=H60e AND T1=T1c AND session_bucket=ny_open`
- Raw: n=93  W=26/L=67  WR=28.0%
- Sharpen: sharpest is RSI=RSI5 (48/67 of losers there)
- **Sharp: n=53  W=5/L=48  WR=9.4%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; session=ny_open  •  ONLY when RSI 60-70 strong

### L25.  `H60=H60e AND T1=T1c AND direction_exec=short AND session_bucket=ny_open`
- Raw: n=93  W=26/L=67  WR=28.0%
- Sharpen: sharpest is RSI=RSI5 (48/67 of losers there)
- **Sharp: n=53  W=5/L=48  WR=9.4%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; session=ny_open  •  ONLY when RSI 60-70 strong

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | H60e(42/47) |
| T1 | T1a(55/45) | T1c(45/55) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(53/47) | short(47/53) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
