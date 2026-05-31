# USD_JPY — R23 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR1**  (normal spread)

## Baseline
- Trades: **2,537**  (W=1,605 / L=932)  -  WR: **63.3%**

## Session distribution

- asia: n=1177  W=753/L=424  WR=64.0%
- ny_close: n=302  W=191/L=111  WR=63.2%
- london: n=204  W=133/L=71  WR=65.2%
- london_open: n=190  W=116/L=74  WR=61.1%
- ny_mid: n=185  W=106/L=79  WR=57.3%
- ny_open: n=177  W=118/L=59  WR=66.7%
- asia_late: n=170  W=104/L=66  WR=61.2%
- off_hours: n=132  W=84/L=48  WR=63.6%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `BBP=BBP2 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=158  W=141/L=17  WR=89.2%
- Refine: exclude H20=H20e drops 7/17 losers (41%)
- **Final: n=120  W=110/L=10  WR=91.7%**
- **Dir: LONG**  •  lower third; RSI 50-60 upper neutral  •  AVOID when HTF20 strongly against

### W02.  `T4=T4c AND BBP=BBP2 AND direction_exec=long`
- Raw: n=132  W=117/L=15  WR=88.6%
- Refine: exclude H20=H20e drops 7/15 losers (47%)
- **Final: n=98  W=90/L=8  WR=91.8%**
- **Dir: LONG**  •  4h trend AGAINST trade; lower third  •  AVOID when HTF20 strongly against

### W03.  `T4=T4c AND BBP=BBP2 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=132  W=117/L=15  WR=88.6%
- Refine: exclude H20=H20e drops 7/15 losers (47%)
- **Final: n=98  W=90/L=8  WR=91.8%**
- **Dir: LONG**  •  4h trend AGAINST trade; lower third; RSI 50-60 upper neutral  •  AVOID when HTF20 strongly against

### W04.  `H20=H20d AND T1=T1a AND direction_exec=long`
- Raw: n=128  W=113/L=15  WR=88.3%
- Refine: exclude BBP=BBP4 drops 13/15 losers (87%)
- **Final: n=88  W=86/L=2  WR=97.7%**
- **Dir: LONG**  •  HTF20 mildly against; 1h trend WITH trade  •  AVOID when upper third

### W05.  `H20=H20d AND T4=T4c AND session_bucket=asia`
- Raw: n=127  W=117/L=10  WR=92.1%
- Refine: exclude H60=H60e drops 10/10 losers (100%)
- **Final: n=77  W=77/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 mildly against; 4h trend AGAINST trade; session=asia  •  AVOID when HTF60 strongly against

### W06.  `H20=H20d AND T4=T4c AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=127  W=117/L=10  WR=92.1%
- Refine: exclude H60=H60e drops 10/10 losers (100%)
- **Final: n=77  W=77/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 mildly against; 4h trend AGAINST trade; RSI 50-60 upper neutral; session=asia  •  AVOID when HTF60 strongly against

### W07.  `H60=H60a AND BBP=BBP2 AND RSI=RSI4`
- Raw: n=125  W=110/L=15  WR=88.0%
- Refine: exclude session_bucket=asia_late drops 4/15 losers (27%)
- **Final: n=121  W=110/L=11  WR=90.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; lower third; RSI 50-60 upper neutral  •  AVOID when session=asia_late

### W08.  `H60=H60a AND BBP=BBP2 AND direction_exec=long`
- Raw: n=123  W=110/L=13  WR=89.4%
- Refine: exclude session_bucket=asia_late drops 3/13 losers (23%)
- **Final: n=120  W=110/L=10  WR=91.7%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; lower third  •  AVOID when session=asia_late

### W09.  `H60=H60a AND BBP=BBP2 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=122  W=110/L=12  WR=90.2%
- Refine: exclude T1=T1a drops 10/12 losers (83%)
- **Final: n=44  W=42/L=2  WR=95.5%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; lower third; RSI 50-60 upper neutral  •  AVOID when 1h trend WITH trade

### W10.  `BBP=BBP2 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=112  W=99/L=13  WR=88.4%
- Refine: exclude H20=H20e drops 6/13 losers (46%)
- **Final: n=81  W=74/L=7  WR=91.4%**
- **Dir: LONG**  •  lower third; zscore -2 to -1 oversold  •  AVOID when HTF20 strongly against

### W11.  `H20=H20d AND T4=T4c AND direction_exec=long`
- Raw: n=112  W=97/L=15  WR=86.6%
- Refine: exclude BBP=BBP4 drops 13/15 losers (87%)
- **Final: n=72  W=70/L=2  WR=97.2%**
- **Dir: LONG**  •  HTF20 mildly against; 4h trend AGAINST trade  •  AVOID when upper third

### W12.  `H20=H20d AND T1=T1a AND T4=T4c AND direction_exec=long`
- Raw: n=112  W=97/L=15  WR=86.6%
- Refine: exclude BBP=BBP4 drops 13/15 losers (87%)
- **Final: n=72  W=70/L=2  WR=97.2%**
- **Dir: LONG**  •  HTF20 mildly against; 1h trend WITH trade; 4h trend AGAINST trade  •  AVOID when upper third

### W13.  `H20=H20d AND T1=T1a AND RSI=RSI4 AND direction_exec=long`
- Raw: n=112  W=97/L=15  WR=86.6%
- Refine: exclude BBP=BBP4 drops 13/15 losers (87%)
- **Final: n=72  W=70/L=2  WR=97.2%**
- **Dir: LONG**  •  HTF20 mildly against; 1h trend WITH trade; RSI 50-60 upper neutral  •  AVOID when upper third

### W14.  `H20=H20d AND T4=T4c AND RSI=RSI4 AND direction_exec=long`
- Raw: n=112  W=97/L=15  WR=86.6%
- Refine: exclude BBP=BBP4 drops 13/15 losers (87%)
- **Final: n=72  W=70/L=2  WR=97.2%**
- **Dir: LONG**  •  HTF20 mildly against; 4h trend AGAINST trade; RSI 50-60 upper neutral  •  AVOID when upper third

### W15.  `RSI=RSI4 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=111  W=99/L=12  WR=89.2%
- Refine: exclude H20=H20e drops 6/12 losers (50%)
- **Final: n=80  W=74/L=6  WR=92.5%**
- **Dir: LONG**  •  RSI 50-60 upper neutral; zscore -2 to -1 oversold  •  AVOID when HTF20 strongly against

### W16.  `BBP=BBP2 AND RSI=RSI4 AND ZS=ZS2 AND direction_exec=long`
- Raw: n=111  W=99/L=12  WR=89.2%
- Refine: exclude H20=H20e drops 6/12 losers (50%)
- **Final: n=80  W=74/L=6  WR=92.5%**
- **Dir: LONG**  •  lower third; RSI 50-60 upper neutral; zscore -2 to -1 oversold  •  AVOID when HTF20 strongly against

### W17.  `H20=H20d AND T1=T1a AND session_bucket=asia`
- Raw: n=105  W=101/L=4  WR=96.2%
- Refine: exclude H60=H60e drops 4/4 losers (100%)
- **Final: n=77  W=77/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend WITH trade; session=asia  •  AVOID when HTF60 strongly against

### W18.  `H20=H20d AND T1=T1a AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=105  W=101/L=4  WR=96.2%
- Refine: exclude H60=H60e drops 4/4 losers (100%)
- **Final: n=77  W=77/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend WITH trade; RSI 50-60 upper neutral; session=asia  •  AVOID when HTF60 strongly against

### W19.  `H60=H60a AND T4=T4c AND BBP=BBP2`
- Raw: n=103  W=92/L=11  WR=89.3%
- Refine: exclude ZS=ZS2 drops 9/11 losers (82%)
- **Final: n=41  W=39/L=2  WR=95.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; lower third  •  AVOID when zscore -2 to -1 oversold

### W20.  `H60=H60a AND T4=T4c AND BBP=BBP2 AND RSI=RSI4`
- Raw: n=103  W=92/L=11  WR=89.3%
- Refine: exclude ZS=ZS2 drops 9/11 losers (82%)
- **Final: n=41  W=39/L=2  WR=95.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; lower third; RSI 50-60 upper neutral  •  AVOID when zscore -2 to -1 oversold

### W21.  `H60=H60a AND T4=T4c AND BBP=BBP2 AND direction_exec=long`
- Raw: n=102  W=92/L=10  WR=90.2%
- Refine: exclude strategy_id=bravo_expansion_continuation drops 4/10 losers (40%)
- **Final: n=86  W=80/L=6  WR=93.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; lower third  •  AVOID when strategy=bravo_expansion_continuation

### W22.  `H20=H20d AND T1=T1a AND T4=T4c AND session_bucket=asia`
- Raw: n=101  W=98/L=3  WR=97.0%
- Refine: exclude H60=H60e drops 3/3 losers (100%)
- **Final: n=77  W=77/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 mildly against; 1h trend WITH trade; 4h trend AGAINST trade; session=asia  •  AVOID when HTF60 strongly against

### W23.  `T1=T1a AND BBP=BBP2 AND direction_exec=long`
- Raw: n=96  W=82/L=14  WR=85.4%
- Refine: exclude session_bucket=asia_late drops 3/14 losers (21%)
- **Final: n=93  W=82/L=11  WR=88.2%**
- **Dir: LONG**  •  1h trend WITH trade; lower third  •  AVOID when session=asia_late

### W24.  `T1=T1a AND BBP=BBP2 AND RSI=RSI4 AND direction_exec=long`
- Raw: n=95  W=82/L=13  WR=86.3%
- Refine: exclude session_bucket=asia_late drops 2/13 losers (15%)
- **Final: n=93  W=82/L=11  WR=88.2%**
- **Dir: LONG**  •  1h trend WITH trade; lower third; RSI 50-60 upper neutral  •  AVOID when session=asia_late

### W25.  `T4=T4c AND ZS=ZS2 AND direction_exec=long`
- Raw: n=90  W=78/L=12  WR=86.7%
- Refine: exclude H20=H20e drops 6/12 losers (50%)
- **Final: n=63  W=57/L=6  WR=90.5%**
- **Dir: LONG**  •  4h trend AGAINST trade; zscore -2 to -1 oversold  •  AVOID when HTF20 strongly against

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `T1=T1c AND T4=T4a AND ZS=ZS3 AND direction_exec=short`
- Raw: n=141  W=56/L=85  WR=39.7%
- Sharpen: sharpest is H20=H20b (18/85 of losers there)
- **Sharp: n=21  W=3/L=18  WR=14.3%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend WITH trade; zscore -1 to +1 neutral  •  ONLY when HTF20 slightly aligned

### L02.  `T1=T1c AND BBP=BBP3 AND direction_exec=short`
- Raw: n=135  W=53/L=82  WR=39.3%
- Sharpen: sharpest is H20=H20b (16/82 of losers there)
- **Sharp: n=17  W=1/L=16  WR=5.9%**
- **Dir: SHORT**  •  1h trend AGAINST trade; middle of band  •  ONLY when HTF20 slightly aligned

### L03.  `T1=T1c AND BBP=BBP3 AND ZS=ZS3 AND direction_exec=short`
- Raw: n=135  W=53/L=82  WR=39.3%
- Sharpen: sharpest is H20=H20b (16/82 of losers there)
- **Sharp: n=17  W=1/L=16  WR=5.9%**
- **Dir: SHORT**  •  1h trend AGAINST trade; middle of band; zscore -1 to +1 neutral  •  ONLY when HTF20 slightly aligned

### L04.  `T1=T1c AND BBP=BBP3 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=133  W=51/L=82  WR=38.3%
- Sharpen: sharpest is H20=H20b (16/82 of losers there)
- **Sharp: n=17  W=1/L=16  WR=5.9%**
- **Dir: SHORT**  •  1h trend AGAINST trade; middle of band; RSI 50-60 upper neutral  •  ONLY when HTF20 slightly aligned

### L05.  `H60=H60e AND T1=T1c AND T4=T4a AND ZS=ZS3`
- Raw: n=119  W=47/L=72  WR=39.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=119  W=47/L=72  WR=39.5%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend WITH trade; zscore -1 to +1 neutral

### L06.  `BBP=BBP2 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=110  W=37/L=73  WR=33.6%
- Sharpen: sharpest is H20=H20e (47/73 of losers there)
- **Sharp: n=63  W=16/L=47  WR=25.4%**
- **Dir: SHORT**  •  lower third; RSI 50-60 upper neutral  •  ONLY when HTF20 strongly against

### L07.  `H20=H20b AND T4=T4a AND session_bucket=asia`
- Raw: n=99  W=25/L=74  WR=25.3%
- Sharpen: sharpest is H60=H60e (24/74 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: ?**  •  HTF20 slightly aligned; 4h trend WITH trade; session=asia  •  ONLY when HTF60 strongly against

### L08.  `H20=H20b AND T4=T4a AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=99  W=25/L=74  WR=25.3%
- Sharpen: sharpest is H60=H60e (24/74 of losers there)
- **Sharp: n=24  W=0/L=24  WR=0.0%**
- **Dir: ?**  •  HTF20 slightly aligned; 4h trend WITH trade; RSI 50-60 upper neutral; session=asia  •  ONLY when HTF60 strongly against

### L09.  `H20=H20b AND T1=T1c AND direction_exec=short`
- Raw: n=98  W=36/L=62  WR=36.7%
- Sharpen: sharpest is H60=H60e (32/62 of losers there)
- **Sharp: n=32  W=0/L=32  WR=0.0%**
- **Dir: SHORT**  •  HTF20 slightly aligned; 1h trend AGAINST trade  •  ONLY when HTF60 strongly against

### L10.  `H20=H20a AND H60=H60a AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=94  W=37/L=57  WR=39.4%
- Sharpen: sharpest is BBP=BBP5 (37/57 of losers there)
- **Sharp: n=49  W=12/L=37  WR=24.5%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; zscore +2 to +3 deep overbought; session=asia  •  ONLY when just touched upper band

### L11.  `H60=H60e AND BBP=BBP2 AND RSI=RSI4`
- Raw: n=93  W=34/L=59  WR=36.6%
- Sharpen: sharpest is direction_exec=short (59/59 of losers there)
- **Sharp: n=83  W=24/L=59  WR=28.9%**
- **Dir: ?**  •  HTF60 strongly against; lower third; RSI 50-60 upper neutral  •  ONLY when short

### L12.  `H20=H20b AND T4=T4a AND direction_exec=short`
- Raw: n=93  W=36/L=57  WR=38.7%
- Sharpen: sharpest is session_bucket=asia (44/57 of losers there)
- **Sharp: n=54  W=10/L=44  WR=18.5%**
- **Dir: SHORT**  •  HTF20 slightly aligned; 4h trend WITH trade  •  ONLY when session=asia

### L13.  `H20=H20b AND T1=T1c AND T4=T4a AND direction_exec=short`
- Raw: n=93  W=36/L=57  WR=38.7%
- Sharpen: sharpest is session_bucket=asia (44/57 of losers there)
- **Sharp: n=54  W=10/L=44  WR=18.5%**
- **Dir: SHORT**  •  HTF20 slightly aligned; 1h trend AGAINST trade; 4h trend WITH trade  •  ONLY when session=asia

### L14.  `H20=H20b AND T1=T1c AND RSI=RSI4 AND direction_exec=short`
- Raw: n=93  W=36/L=57  WR=38.7%
- Sharpen: sharpest is session_bucket=asia (44/57 of losers there)
- **Sharp: n=54  W=10/L=44  WR=18.5%**
- **Dir: SHORT**  •  HTF20 slightly aligned; 1h trend AGAINST trade; RSI 50-60 upper neutral  •  ONLY when session=asia

### L15.  `H20=H20b AND T4=T4a AND RSI=RSI4 AND direction_exec=short`
- Raw: n=93  W=36/L=57  WR=38.7%
- Sharpen: sharpest is session_bucket=asia (44/57 of losers there)
- **Sharp: n=54  W=10/L=44  WR=18.5%**
- **Dir: SHORT**  •  HTF20 slightly aligned; 4h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when session=asia

### L16.  `H20=H20b AND T1=T1c AND session_bucket=asia`
- Raw: n=92  W=31/L=61  WR=33.7%
- Sharpen: sharpest is direction_exec=short (44/61 of losers there)
- **Sharp: n=54  W=10/L=44  WR=18.5%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend AGAINST trade; session=asia  •  ONLY when short

### L17.  `H20=H20b AND T1=T1c AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=92  W=31/L=61  WR=33.7%
- Sharpen: sharpest is direction_exec=short (44/61 of losers there)
- **Sharp: n=54  W=10/L=44  WR=18.5%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend AGAINST trade; RSI 50-60 upper neutral; session=asia  •  ONLY when short

### L18.  `H20=H20e AND T1=T1c AND BBP=BBP3`
- Raw: n=91  W=35/L=56  WR=38.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=91  W=35/L=56  WR=38.5%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; middle of band

### L19.  `H20=H20e AND T1=T1c AND BBP=BBP3 AND ZS=ZS3`
- Raw: n=91  W=35/L=56  WR=38.5%
- Sharpen: no sharper sub-pattern
- **Sharp: n=91  W=35/L=56  WR=38.5%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; middle of band; zscore -1 to +1 neutral

### L20.  `H20=H20e AND T1=T1c AND BBP=BBP3 AND direction_exec=short`
- Raw: n=90  W=35/L=55  WR=38.9%
- Sharpen: no sharper sub-pattern
- **Sharp: n=90  W=35/L=55  WR=38.9%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; middle of band

### L21.  `T4=T4a AND BBP=BBP2 AND direction_exec=short`
- Raw: n=89  W=30/L=59  WR=33.7%
- Sharpen: sharpest is H60=H60e (48/59 of losers there)
- **Sharp: n=65  W=17/L=48  WR=26.2%**
- **Dir: SHORT**  •  4h trend WITH trade; lower third  •  ONLY when HTF60 strongly against

### L22.  `T4=T4a AND BBP=BBP2 AND RSI=RSI4 AND direction_exec=short`
- Raw: n=89  W=30/L=59  WR=33.7%
- Sharpen: sharpest is H60=H60e (48/59 of losers there)
- **Sharp: n=65  W=17/L=48  WR=26.2%**
- **Dir: SHORT**  •  4h trend WITH trade; lower third; RSI 50-60 upper neutral  •  ONLY when HTF60 strongly against

### L23.  `H20=H20e AND T1=T1c AND BBP=BBP3 AND RSI=RSI4`
- Raw: n=89  W=33/L=56  WR=37.1%
- Sharpen: no sharper sub-pattern
- **Sharp: n=89  W=33/L=56  WR=37.1%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; middle of band; RSI 50-60 upper neutral

### L24.  `T1=T1c AND T4=T4a AND BBP=BBP3 AND direction_exec=short`
- Raw: n=89  W=33/L=56  WR=37.1%
- Sharpen: sharpest is H20=H20b (16/56 of losers there)
- **Sharp: n=17  W=1/L=16  WR=5.9%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend WITH trade; middle of band  •  ONLY when HTF20 slightly aligned

### L25.  `H20=H20e AND H60=H60e AND T1=T1c AND BBP=BBP3`
- Raw: n=89  W=35/L=54  WR=39.3%
- Sharpen: no sharper sub-pattern
- **Sharp: n=89  W=35/L=54  WR=39.3%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend AGAINST trade; middle of band

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(39/32) | H20e(32/39) |
| H60 | H60a(44/38) | H60e(39/47) |
| T1 | T1a(53/44) | T1c(47/56) |
| T4 | T4c(52/47) | T4a(48/53) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(55/42) | short(45/58) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
