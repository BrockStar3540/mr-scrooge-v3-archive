# NZD_JPY — R31 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_1**  (5m ATR 33-80%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20b**  (EMA20 up 0.15-0.5x)
- **E50 = E50c**  (EMA50 flat)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR3**  (wide spread)

## Baseline
- Trades: **2,273**  (W=1,448 / L=825)  -  WR: **63.7%**

## Session distribution

- asia: n=732  W=465/L=267  WR=63.5%
- london_open: n=463  W=299/L=164  WR=64.6%
- ny_mid: n=334  W=200/L=134  WR=59.9%
- ny_close: n=210  W=128/L=82  WR=61.0%
- london: n=166  W=110/L=56  WR=66.3%
- ny_open: n=160  W=101/L=59  WR=63.1%
- asia_late: n=146  W=97/L=49  WR=66.4%
- off_hours: n=62  W=48/L=14  WR=77.4%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20a AND direction_exec=long AND session_bucket=asia`
- Raw: n=217  W=189/L=28  WR=87.1%
- Refine: exclude BBP=BBP5 drops 9/28 losers (32%)
- **Final: n=196  W=177/L=19  WR=90.3%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; session=asia  •  AVOID when just touched upper band

### W02.  `H20=H20a AND RSI=RSI4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=184  W=165/L=19  WR=89.7%
- Refine: exclude T1=T1a drops 19/19 losers (100%)
- **Final: n=44  W=44/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 50-60 upper neutral; session=asia  •  AVOID when 1h trend WITH trade

### W03.  `H60=H60a AND BBP=BBP4 AND session_bucket=asia`
- Raw: n=180  W=154/L=26  WR=85.6%
- Refine: exclude H20=H20e drops 15/26 losers (58%)
- **Final: n=115  W=104/L=11  WR=90.4%**
- **Dir: ?**  •  HTF60 aligned WITH trade; upper third; session=asia  •  AVOID when HTF20 strongly against

### W04.  `H60=H60a AND BBP=BBP4 AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=175  W=150/L=25  WR=85.7%
- Refine: exclude H20=H20e drops 15/25 losers (60%)
- **Final: n=110  W=100/L=10  WR=90.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; upper third; RSI 50-60 upper neutral; session=asia  •  AVOID when HTF20 strongly against

### W05.  `H20=H20a AND H60=H60a AND session_bucket=asia`
- Raw: n=173  W=153/L=20  WR=88.4%
- Refine: exclude BBP=BBP5 drops 9/20 losers (45%)
- **Final: n=152  W=141/L=11  WR=92.8%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=asia  •  AVOID when just touched upper band

### W06.  `H20=H20a AND H60=H60a AND direction_exec=long AND session_bucket=asia`
- Raw: n=173  W=153/L=20  WR=88.4%
- Refine: exclude BBP=BBP5 drops 9/20 losers (45%)
- **Final: n=152  W=141/L=11  WR=92.8%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; session=asia  •  AVOID when just touched upper band

### W07.  `H60=H60a AND BBP=BBP4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=168  W=143/L=25  WR=85.1%
- Refine: exclude H20=H20e drops 14/25 losers (56%)
- **Final: n=115  W=104/L=11  WR=90.4%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; upper third; session=asia  •  AVOID when HTF20 strongly against

### W08.  `H60=H60a AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=162  W=141/L=21  WR=87.0%
- Refine: exclude T1=T1a drops 19/21 losers (90%)
- **Final: n=64  W=62/L=2  WR=96.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; zscore +1 to +2 overbought; session=asia  •  AVOID when 1h trend WITH trade

### W09.  `H60=H60a AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=162  W=141/L=21  WR=87.0%
- Refine: exclude T1=T1a drops 19/21 losers (90%)
- **Final: n=64  W=62/L=2  WR=96.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; upper third; zscore +1 to +2 overbought; session=asia  •  AVOID when 1h trend WITH trade

### W10.  `H60=H60a AND RSI=RSI4 AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=157  W=137/L=20  WR=87.3%
- Refine: exclude T1=T1a drops 18/20 losers (90%)
- **Final: n=64  W=62/L=2  WR=96.9%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought; session=asia  •  AVOID when 1h trend WITH trade

### W11.  `H60=H60a AND ZS=ZS4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=152  W=131/L=21  WR=86.2%
- Refine: exclude H20=H20e drops 13/21 losers (62%)
- **Final: n=100  W=92/L=8  WR=92.0%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; zscore +1 to +2 overbought; session=asia  •  AVOID when HTF20 strongly against

### W12.  `H20=H20a AND H60=H60a AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=149  W=137/L=12  WR=91.9%
- Refine: exclude T1=T1a drops 12/12 losers (100%)
- **Final: n=44  W=44/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 50-60 upper neutral; session=asia  •  AVOID when 1h trend WITH trade

### W13.  `T4=T4c AND BBP=BBP4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=127  W=108/L=19  WR=85.0%
- Refine: exclude T1=T1a drops 17/19 losers (89%)
- **Final: n=48  W=46/L=2  WR=95.8%**
- **Dir: LONG**  •  4h trend AGAINST trade; upper third; session=asia  •  AVOID when 1h trend WITH trade

### W14.  `T1=T1c AND direction_exec=long AND session_bucket=asia`
- Raw: n=120  W=102/L=18  WR=85.0%
- Refine: exclude H20=H20c drops 10/18 losers (56%)
- **Final: n=104  W=96/L=8  WR=92.3%**
- **Dir: LONG**  •  1h trend AGAINST trade; session=asia  •  AVOID when HTF20 neutral

### W15.  `H60=H60a AND T1=T1c AND direction_exec=long AND session_bucket=asia`
- Raw: n=120  W=102/L=18  WR=85.0%
- Refine: exclude H20=H20c drops 10/18 losers (56%)
- **Final: n=104  W=96/L=8  WR=92.3%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; session=asia  •  AVOID when HTF20 neutral

### W16.  `H20=H20a AND T4=T4c AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=117  W=103/L=14  WR=88.0%
- Refine: exclude BBP=BBP5 drops 4/14 losers (29%)
- **Final: n=107  W=97/L=10  WR=90.7%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend AGAINST trade; RSI 50-60 upper neutral; session=asia  •  AVOID when just touched upper band

### W17.  `T4=T4c AND ZS=ZS4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=113  W=98/L=15  WR=86.7%
- Refine: exclude T1=T1a drops 15/15 losers (100%)
- **Final: n=44  W=44/L=0  WR=100.0%**
- **Dir: LONG**  •  4h trend AGAINST trade; zscore +1 to +2 overbought; session=asia  •  AVOID when 1h trend WITH trade

### W18.  `H60=H60a AND T4=T4c AND BBP=BBP4 AND session_bucket=asia`
- Raw: n=112  W=100/L=12  WR=89.3%
- Refine: exclude H20=H20e drops 8/12 losers (67%)
- **Final: n=70  W=66/L=4  WR=94.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; upper third; session=asia  •  AVOID when HTF20 strongly against

### W19.  `H20=H20a AND BBP=BBP4 AND direction_exec=long AND session_bucket=asia`
- Raw: n=110  W=98/L=12  WR=89.1%
- Refine: exclude H60=H60e drops 7/12 losers (58%)
- **Final: n=95  W=90/L=5  WR=94.7%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; upper third; session=asia  •  AVOID when HTF60 strongly against

### W20.  `H20=H20a AND RSI=RSI4 AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=108  W=94/L=14  WR=87.0%
- Refine: exclude BBP=BBP5 drops 14/14 losers (100%)
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 50-60 upper neutral; zscore +2 to +3 deep overbought; session=asia  •  AVOID when just touched upper band

### W21.  `H60=H60a AND T4=T4c AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=107  W=98/L=9  WR=91.6%
- Refine: exclude T1=T1a drops 9/9 losers (100%)
- **Final: n=44  W=44/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend AGAINST trade; zscore +1 to +2 overbought; session=asia  •  AVOID when 1h trend WITH trade

### W22.  `H60=H60a AND T1=T1c AND ZS=ZS4`
- Raw: n=101  W=87/L=14  WR=86.1%
- Refine: exclude session_bucket=ny_mid drops 4/14 losers (29%)
- **Final: n=95  W=85/L=10  WR=89.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; zscore +1 to +2 overbought  •  AVOID when session=ny_mid

### W23.  `H60=H60a AND T1=T1c AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=101  W=87/L=14  WR=86.1%
- Refine: exclude session_bucket=ny_mid drops 4/14 losers (29%)
- **Final: n=95  W=85/L=10  WR=89.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; upper third; zscore +1 to +2 overbought  •  AVOID when session=ny_mid

### W24.  `H60=H60a AND T1=T1c AND RSI=RSI4 AND ZS=ZS4`
- Raw: n=101  W=87/L=14  WR=86.1%
- Refine: exclude session_bucket=ny_mid drops 4/14 losers (29%)
- **Final: n=95  W=85/L=10  WR=89.5%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend AGAINST trade; RSI 50-60 upper neutral; zscore +1 to +2 overbought  •  AVOID when session=ny_mid

### W25.  `H20=H20a AND H60=H60a AND BBP=BBP4 AND session_bucket=asia`
- Raw: n=95  W=90/L=5  WR=94.7%
- Refine: exclude T1=T1a drops 5/5 losers (100%)
- **Final: n=30  W=30/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; upper third; session=asia  •  AVOID when 1h trend WITH trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H20=H20e AND direction_exec=short AND session_bucket=asia`
- Raw: n=156  W=49/L=107  WR=31.4%
- Sharpen: sharpest is T1=T1a (30/107 of losers there)
- **Sharp: n=31  W=1/L=30  WR=3.2%**
- **Dir: SHORT**  •  HTF20 strongly against; session=asia  •  ONLY when 1h trend WITH trade

### L02.  `H60=H60e AND BBP=BBP4 AND session_bucket=asia`
- Raw: n=133  W=50/L=83  WR=37.6%
- Sharpen: sharpest is H20=H20e (49/83 of losers there)
- **Sharp: n=60  W=11/L=49  WR=18.3%**
- **Dir: ?**  •  HTF60 strongly against; upper third; session=asia  •  ONLY when HTF20 strongly against

### L03.  `H60=H60e AND BBP=BBP4 AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=126  W=47/L=79  WR=37.3%
- Sharpen: sharpest is H20=H20e (46/79 of losers there)
- **Sharp: n=54  W=8/L=46  WR=14.8%**
- **Dir: ?**  •  HTF60 strongly against; upper third; RSI 50-60 upper neutral; session=asia  •  ONLY when HTF20 strongly against

### L04.  `H20=H20e AND T1=T1a AND session_bucket=asia`
- Raw: n=125  W=47/L=78  WR=37.6%
- Sharpen: sharpest is H60=H60e (30/78 of losers there)
- **Sharp: n=31  W=1/L=30  WR=3.2%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; session=asia  •  ONLY when HTF60 strongly against

### L05.  `H20=H20e AND T1=T1c AND direction_exec=short AND session_bucket=asia`
- Raw: n=125  W=48/L=77  WR=38.4%
- Sharpen: sharpest is BBP=BBP6 (15/77 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend AGAINST trade; session=asia  •  ONLY when deep above upper band

### L06.  `H20=H20e AND RSI=RSI4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=123  W=38/L=85  WR=30.9%
- Sharpen: sharpest is T1=T1a (22/85 of losers there)
- **Sharp: n=22  W=0/L=22  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; RSI 50-60 upper neutral; session=asia  •  ONLY when 1h trend WITH trade

### L07.  `H20=H20e AND T1=T1a AND direction_exec=short`
- Raw: n=123  W=44/L=79  WR=35.8%
- Sharpen: sharpest is session_bucket=asia (30/79 of losers there)
- **Sharp: n=31  W=1/L=30  WR=3.2%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend WITH trade  •  ONLY when session=asia

### L08.  `H20=H20e AND H60=H60e AND session_bucket=asia`
- Raw: n=121  W=35/L=86  WR=28.9%
- Sharpen: sharpest is T1=T1a (30/86 of losers there)
- **Sharp: n=31  W=1/L=30  WR=3.2%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; session=asia  •  ONLY when 1h trend WITH trade

### L09.  `H20=H20e AND H60=H60e AND direction_exec=short AND session_bucket=asia`
- Raw: n=121  W=35/L=86  WR=28.9%
- Sharpen: sharpest is T1=T1a (30/86 of losers there)
- **Sharp: n=31  W=1/L=30  WR=3.2%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; session=asia  •  ONLY when 1h trend WITH trade

### L10.  `H60=H60e AND BBP=BBP4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=118  W=42/L=76  WR=35.6%
- Sharpen: sharpest is H20=H20e (49/76 of losers there)
- **Sharp: n=60  W=11/L=49  WR=18.3%**
- **Dir: SHORT**  •  HTF60 strongly against; upper third; session=asia  •  ONLY when HTF20 strongly against

### L11.  `H20=H20e AND H60=H60e AND T4=T4a AND BBP=BBP4`
- Raw: n=116  W=46/L=70  WR=39.7%
- Sharpen: sharpest is session_bucket=asia (27/70 of losers there)
- **Sharp: n=32  W=5/L=27  WR=15.6%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend WITH trade; upper third  •  ONLY when session=asia

### L12.  `H20=H20e AND T1=T1a AND RSI=RSI4 AND session_bucket=asia`
- Raw: n=116  W=46/L=70  WR=39.7%
- Sharpen: sharpest is H60=H60e (22/70 of losers there)
- **Sharp: n=22  W=0/L=22  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend WITH trade; RSI 50-60 upper neutral; session=asia  •  ONLY when HTF60 strongly against

### L13.  `ZS=ZS4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=115  W=46/L=69  WR=40.0%
- Sharpen: sharpest is T1=T1a (20/69 of losers there)
- **Sharp: n=22  W=2/L=20  WR=9.1%**
- **Dir: SHORT**  •  zscore +1 to +2 overbought; session=asia  •  ONLY when 1h trend WITH trade

### L14.  `BBP=BBP4 AND ZS=ZS4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=115  W=46/L=69  WR=40.0%
- Sharpen: sharpest is T1=T1a (20/69 of losers there)
- **Sharp: n=22  W=2/L=20  WR=9.1%**
- **Dir: SHORT**  •  upper third; zscore +1 to +2 overbought; session=asia  •  ONLY when 1h trend WITH trade

### L15.  `H20=H20e AND T1=T1a AND RSI=RSI4 AND direction_exec=short`
- Raw: n=114  W=43/L=71  WR=37.7%
- Sharpen: sharpest is session_bucket=asia (22/71 of losers there)
- **Sharp: n=22  W=0/L=22  WR=0.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 1h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when session=asia

### L16.  `H20=H20e AND T4=T4a AND session_bucket=asia`
- Raw: n=114  W=44/L=70  WR=38.6%
- Sharpen: sharpest is BBP=BBP6 (15/70 of losers there)
- **Sharp: n=15  W=0/L=15  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend WITH trade; session=asia  •  ONLY when deep above upper band

### L17.  `H20=H20e AND H60=H60e AND T1=T1a`
- Raw: n=112  W=42/L=70  WR=37.5%
- Sharpen: sharpest is session_bucket=asia (30/70 of losers there)
- **Sharp: n=31  W=1/L=30  WR=3.2%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend WITH trade  •  ONLY when session=asia

### L18.  `H20=H20e AND H60=H60e AND T1=T1a AND direction_exec=short`
- Raw: n=112  W=42/L=70  WR=37.5%
- Sharpen: sharpest is session_bucket=asia (30/70 of losers there)
- **Sharp: n=31  W=1/L=30  WR=3.2%**
- **Dir: SHORT**  •  HTF20 strongly against; HTF60 strongly against; 1h trend WITH trade  •  ONLY when session=asia

### L19.  `H60=H60e AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=111  W=36/L=75  WR=32.4%
- Sharpen: sharpest is T1=T1a (26/75 of losers there)
- **Sharp: n=28  W=2/L=26  WR=7.1%**
- **Dir: ?**  •  HTF60 strongly against; zscore +1 to +2 overbought; session=asia  •  ONLY when 1h trend WITH trade

### L20.  `H60=H60e AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=111  W=36/L=75  WR=32.4%
- Sharpen: sharpest is T1=T1a (26/75 of losers there)
- **Sharp: n=28  W=2/L=26  WR=7.1%**
- **Dir: ?**  •  HTF60 strongly against; upper third; zscore +1 to +2 overbought; session=asia  •  ONLY when 1h trend WITH trade

### L21.  `H20=H20e AND H60=H60e AND T4=T4a AND ZS=ZS4`
- Raw: n=111  W=43/L=68  WR=38.7%
- Sharpen: sharpest is session_bucket=asia (26/68 of losers there)
- **Sharp: n=31  W=5/L=26  WR=16.1%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend WITH trade; zscore +1 to +2 overbought  •  ONLY when session=asia

### L22.  `RSI=RSI4 AND ZS=ZS4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=109  W=43/L=66  WR=39.4%
- Sharpen: sharpest is T1=T1a (20/66 of losers there)
- **Sharp: n=22  W=2/L=20  WR=9.1%**
- **Dir: SHORT**  •  RSI 50-60 upper neutral; zscore +1 to +2 overbought; session=asia  •  ONLY when 1h trend WITH trade

### L23.  `H60=H60e AND ZS=ZS4 AND direction_exec=short AND session_bucket=asia`
- Raw: n=105  W=36/L=69  WR=34.3%
- Sharpen: sharpest is H20=H20e (43/69 of losers there)
- **Sharp: n=54  W=11/L=43  WR=20.4%**
- **Dir: SHORT**  •  HTF60 strongly against; zscore +1 to +2 overbought; session=asia  •  ONLY when HTF20 strongly against

### L24.  `H60=H60e AND RSI=RSI4 AND ZS=ZS4 AND session_bucket=asia`
- Raw: n=104  W=33/L=71  WR=31.7%
- Sharpen: sharpest is H20=H20e (40/71 of losers there)
- **Sharp: n=48  W=8/L=40  WR=16.7%**
- **Dir: ?**  •  HTF60 strongly against; RSI 50-60 upper neutral; zscore +1 to +2 overbought; session=asia  •  ONLY when HTF20 strongly against

### L25.  `H20=H20e AND H60=H60e AND T1=T1a AND RSI=RSI4`
- Raw: n=103  W=41/L=62  WR=39.8%
- Sharpen: sharpest is session_bucket=asia (22/62 of losers there)
- **Sharp: n=22  W=0/L=22  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 1h trend WITH trade; RSI 50-60 upper neutral  •  ONLY when session=asia

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | H20a(48/30) | H20e(32/47) |
| H60 | H60a(51/45) | H60e(47/53) |
| T1 | — | — |
| T4 | T4c(53/44) | T4a(47/56) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(52/46) | short(48/54) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
