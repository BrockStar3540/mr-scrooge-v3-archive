# CHF_JPY — R37 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_3**  (5m ATR >120%)
- **A1 = A1_2**  (1h ATR 4-8x)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50a**  (EMA50 up >0.5x)
- **ADR = ADR4**  (90-110%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **4,528**  (W=2,587 / L=1,941)  -  WR: **57.1%**

## Session distribution

- asia: n=1244  W=699/L=545  WR=56.2%
- london_open: n=1102  W=621/L=481  WR=56.4%
- ny_mid: n=960  W=542/L=418  WR=56.5%
- ny_open: n=400  W=237/L=163  WR=59.2%
- london: n=342  W=212/L=130  WR=62.0%
- ny_close: n=283  W=169/L=114  WR=59.7%
- off_hours: n=139  W=74/L=65  WR=53.2%
- asia_late: n=58  W=33/L=25  WR=56.9%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `H20=H20b AND H60=H60a AND BBP=BBP4`
- Raw: n=107  W=96/L=11  WR=89.7%
- Refine: exclude T1=T1c drops 11/11 losers (100%)
- **Final: n=95  W=95/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; upper third  •  AVOID when 1h trend AGAINST trade

### W02.  `H20=H20b AND T4=T4a AND BBP=BBP4`
- Raw: n=107  W=96/L=11  WR=89.7%
- Refine: exclude T1=T1c drops 11/11 losers (100%)
- **Final: n=95  W=95/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 slightly aligned; 4h trend WITH trade; upper third  •  AVOID when 1h trend AGAINST trade

### W03.  `H20=H20b AND BBP=BBP4 AND direction_exec=long`
- Raw: n=107  W=96/L=11  WR=89.7%
- Refine: exclude T1=T1c drops 11/11 losers (100%)
- **Final: n=95  W=95/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 slightly aligned; upper third  •  AVOID when 1h trend AGAINST trade

### W04.  `H20=H20b AND H60=H60a AND T4=T4a AND BBP=BBP4`
- Raw: n=107  W=96/L=11  WR=89.7%
- Refine: exclude T1=T1c drops 11/11 losers (100%)
- **Final: n=95  W=95/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 4h trend WITH trade; upper third  •  AVOID when 1h trend AGAINST trade

### W05.  `H20=H20b AND H60=H60a AND BBP=BBP4 AND direction_exec=long`
- Raw: n=107  W=96/L=11  WR=89.7%
- Refine: exclude T1=T1c drops 11/11 losers (100%)
- **Final: n=95  W=95/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; upper third  •  AVOID when 1h trend AGAINST trade

### W06.  `H20=H20b AND T4=T4a AND BBP=BBP4 AND direction_exec=long`
- Raw: n=107  W=96/L=11  WR=89.7%
- Refine: exclude T1=T1c drops 11/11 losers (100%)
- **Final: n=95  W=95/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 slightly aligned; 4h trend WITH trade; upper third  •  AVOID when 1h trend AGAINST trade

### W07.  `H20=H20b AND H60=H60a AND ZS=ZS4`
- Raw: n=103  W=96/L=7  WR=93.2%
- Refine: exclude T1=T1c drops 7/7 losers (100%)
- **Final: n=95  W=95/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; zscore +1 to +2 overbought  •  AVOID when 1h trend AGAINST trade

### W08.  `H20=H20b AND T4=T4a AND ZS=ZS4`
- Raw: n=103  W=96/L=7  WR=93.2%
- Refine: exclude T1=T1c drops 7/7 losers (100%)
- **Final: n=95  W=95/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 slightly aligned; 4h trend WITH trade; zscore +1 to +2 overbought  •  AVOID when 1h trend AGAINST trade

### W09.  `H20=H20b AND ZS=ZS4 AND direction_exec=long`
- Raw: n=103  W=96/L=7  WR=93.2%
- Refine: exclude T1=T1c drops 7/7 losers (100%)
- **Final: n=95  W=95/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 slightly aligned; zscore +1 to +2 overbought  •  AVOID when 1h trend AGAINST trade

### W10.  `H20=H20b AND H60=H60a AND T4=T4a AND ZS=ZS4`
- Raw: n=103  W=96/L=7  WR=93.2%
- Refine: exclude T1=T1c drops 7/7 losers (100%)
- **Final: n=95  W=95/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 4h trend WITH trade; zscore +1 to +2 overbought  •  AVOID when 1h trend AGAINST trade

### W11.  `H20=H20b AND H60=H60a AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=103  W=96/L=7  WR=93.2%
- Refine: exclude T1=T1c drops 7/7 losers (100%)
- **Final: n=95  W=95/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; upper third; zscore +1 to +2 overbought  •  AVOID when 1h trend AGAINST trade

### W12.  `H20=H20b AND H60=H60a AND ZS=ZS4 AND direction_exec=long`
- Raw: n=103  W=96/L=7  WR=93.2%
- Refine: exclude T1=T1c drops 7/7 losers (100%)
- **Final: n=95  W=95/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; zscore +1 to +2 overbought  •  AVOID when 1h trend AGAINST trade

### W13.  `H20=H20b AND T4=T4a AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=103  W=96/L=7  WR=93.2%
- Refine: exclude T1=T1c drops 7/7 losers (100%)
- **Final: n=95  W=95/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 slightly aligned; 4h trend WITH trade; upper third; zscore +1 to +2 overbought  •  AVOID when 1h trend AGAINST trade

### W14.  `H20=H20b AND T4=T4a AND ZS=ZS4 AND direction_exec=long`
- Raw: n=103  W=96/L=7  WR=93.2%
- Refine: exclude T1=T1c drops 7/7 losers (100%)
- **Final: n=95  W=95/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 slightly aligned; 4h trend WITH trade; zscore +1 to +2 overbought  •  AVOID when 1h trend AGAINST trade

### W15.  `H20=H20b AND BBP=BBP4 AND ZS=ZS4 AND direction_exec=long`
- Raw: n=103  W=96/L=7  WR=93.2%
- Refine: exclude T1=T1c drops 7/7 losers (100%)
- **Final: n=95  W=95/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 slightly aligned; upper third; zscore +1 to +2 overbought  •  AVOID when 1h trend AGAINST trade

### W16.  `H20=H20b AND H60=H60a AND T1=T1a`
- Raw: n=100  W=100/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=100  W=100/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 1h trend WITH trade

### W17.  `H20=H20b AND H60=H60a AND RSI=RSI6`
- Raw: n=100  W=100/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=100  W=100/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; RSI 70-80 overbought

### W18.  `H20=H20b AND T1=T1a AND T4=T4a`
- Raw: n=100  W=100/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=100  W=100/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend WITH trade; 4h trend WITH trade

### W19.  `H20=H20b AND T1=T1a AND RSI=RSI6`
- Raw: n=100  W=100/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=100  W=100/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 slightly aligned; 1h trend WITH trade; RSI 70-80 overbought

### W20.  `H20=H20b AND T1=T1a AND direction_exec=long`
- Raw: n=100  W=100/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=100  W=100/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 slightly aligned; 1h trend WITH trade

### W21.  `H20=H20b AND T4=T4a AND RSI=RSI6`
- Raw: n=100  W=100/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=100  W=100/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 slightly aligned; 4h trend WITH trade; RSI 70-80 overbought

### W22.  `H20=H20b AND RSI=RSI6 AND direction_exec=long`
- Raw: n=100  W=100/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=100  W=100/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 slightly aligned; RSI 70-80 overbought

### W23.  `H20=H20b AND H60=H60a AND T1=T1a AND T4=T4a`
- Raw: n=100  W=100/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=100  W=100/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 1h trend WITH trade; 4h trend WITH trade

### W24.  `H20=H20b AND H60=H60a AND T1=T1a AND RSI=RSI6`
- Raw: n=100  W=100/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=100  W=100/L=0  WR=100.0%**
- **Dir: ?**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 1h trend WITH trade; RSI 70-80 overbought

### W25.  `H20=H20b AND H60=H60a AND T1=T1a AND direction_exec=long`
- Raw: n=100  W=100/L=0  WR=100.0%
- Refine: no further refinement
- **Final: n=100  W=100/L=0  WR=100.0%**
- **Dir: LONG**  •  HTF20 slightly aligned; HTF60 aligned WITH trade; 1h trend WITH trade

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60e AND T4=T4c AND BBP=BBP2`
- Raw: n=191  W=64/L=127  WR=33.5%
- Sharpen: sharpest is ZS=ZS2 (85/127 of losers there)
- **Sharp: n=117  W=32/L=85  WR=27.4%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; lower third  •  ONLY when zscore -2 to -1 oversold

### L02.  `T1=T1c AND T4=T4c AND BBP=BBP2`
- Raw: n=191  W=64/L=127  WR=33.5%
- Sharpen: sharpest is ZS=ZS2 (85/127 of losers there)
- **Sharp: n=117  W=32/L=85  WR=27.4%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; lower third  •  ONLY when zscore -2 to -1 oversold

### L03.  `T4=T4c AND BBP=BBP2 AND direction_exec=short`
- Raw: n=191  W=64/L=127  WR=33.5%
- Sharpen: sharpest is ZS=ZS2 (85/127 of losers there)
- **Sharp: n=117  W=32/L=85  WR=27.4%**
- **Dir: SHORT**  •  4h trend AGAINST trade; lower third  •  ONLY when zscore -2 to -1 oversold

### L04.  `H60=H60e AND T1=T1c AND T4=T4c AND BBP=BBP2`
- Raw: n=191  W=64/L=127  WR=33.5%
- Sharpen: sharpest is ZS=ZS2 (85/127 of losers there)
- **Sharp: n=117  W=32/L=85  WR=27.4%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; lower third  •  ONLY when zscore -2 to -1 oversold

### L05.  `H60=H60e AND T4=T4c AND BBP=BBP2 AND direction_exec=short`
- Raw: n=191  W=64/L=127  WR=33.5%
- Sharpen: sharpest is ZS=ZS2 (85/127 of losers there)
- **Sharp: n=117  W=32/L=85  WR=27.4%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend AGAINST trade; lower third  •  ONLY when zscore -2 to -1 oversold

### L06.  `T1=T1c AND T4=T4c AND BBP=BBP2 AND direction_exec=short`
- Raw: n=191  W=64/L=127  WR=33.5%
- Sharpen: sharpest is ZS=ZS2 (85/127 of losers there)
- **Sharp: n=117  W=32/L=85  WR=27.4%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; lower third  •  ONLY when zscore -2 to -1 oversold

### L07.  `H20=H20e AND T4=T4c AND BBP=BBP2`
- Raw: n=154  W=52/L=102  WR=33.8%
- Sharpen: sharpest is ZS=ZS2 (72/102 of losers there)
- **Sharp: n=96  W=24/L=72  WR=25.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; lower third  •  ONLY when zscore -2 to -1 oversold

### L08.  `H60=H60e AND T1=T1c AND ZS=ZS2`
- Raw: n=154  W=57/L=97  WR=37.0%
- Sharpen: sharpest is T4=T4c (85/97 of losers there)
- **Sharp: n=117  W=32/L=85  WR=27.4%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; zscore -2 to -1 oversold  •  ONLY when 4h trend AGAINST trade

### L09.  `H60=H60e AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=154  W=57/L=97  WR=37.0%
- Sharpen: sharpest is T4=T4c (85/97 of losers there)
- **Sharp: n=117  W=32/L=85  WR=27.4%**
- **Dir: ?**  •  HTF60 strongly against; lower third; zscore -2 to -1 oversold  •  ONLY when 4h trend AGAINST trade

### L10.  `H60=H60e AND ZS=ZS2 AND direction_exec=short`
- Raw: n=154  W=57/L=97  WR=37.0%
- Sharpen: sharpest is T4=T4c (85/97 of losers there)
- **Sharp: n=117  W=32/L=85  WR=27.4%**
- **Dir: SHORT**  •  HTF60 strongly against; zscore -2 to -1 oversold  •  ONLY when 4h trend AGAINST trade

### L11.  `T1=T1c AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=154  W=57/L=97  WR=37.0%
- Sharpen: sharpest is T4=T4c (85/97 of losers there)
- **Sharp: n=117  W=32/L=85  WR=27.4%**
- **Dir: ?**  •  1h trend AGAINST trade; lower third; zscore -2 to -1 oversold  •  ONLY when 4h trend AGAINST trade

### L12.  `T1=T1c AND ZS=ZS2 AND direction_exec=short`
- Raw: n=154  W=57/L=97  WR=37.0%
- Sharpen: sharpest is T4=T4c (85/97 of losers there)
- **Sharp: n=117  W=32/L=85  WR=27.4%**
- **Dir: SHORT**  •  1h trend AGAINST trade; zscore -2 to -1 oversold  •  ONLY when 4h trend AGAINST trade

### L13.  `BBP=BBP2 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=154  W=57/L=97  WR=37.0%
- Sharpen: sharpest is T4=T4c (85/97 of losers there)
- **Sharp: n=117  W=32/L=85  WR=27.4%**
- **Dir: SHORT**  •  lower third; zscore -2 to -1 oversold  •  ONLY when 4h trend AGAINST trade

### L14.  `H60=H60e AND T1=T1c AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=154  W=57/L=97  WR=37.0%
- Sharpen: sharpest is T4=T4c (85/97 of losers there)
- **Sharp: n=117  W=32/L=85  WR=27.4%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; lower third; zscore -2 to -1 oversold  •  ONLY when 4h trend AGAINST trade

### L15.  `H60=H60e AND T1=T1c AND ZS=ZS2 AND direction_exec=short`
- Raw: n=154  W=57/L=97  WR=37.0%
- Sharpen: sharpest is T4=T4c (85/97 of losers there)
- **Sharp: n=117  W=32/L=85  WR=27.4%**
- **Dir: SHORT**  •  HTF60 strongly against; 1h trend AGAINST trade; zscore -2 to -1 oversold  •  ONLY when 4h trend AGAINST trade

### L16.  `H60=H60e AND BBP=BBP2 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=154  W=57/L=97  WR=37.0%
- Sharpen: sharpest is T4=T4c (85/97 of losers there)
- **Sharp: n=117  W=32/L=85  WR=27.4%**
- **Dir: SHORT**  •  HTF60 strongly against; lower third; zscore -2 to -1 oversold  •  ONLY when 4h trend AGAINST trade

### L17.  `T1=T1c AND BBP=BBP2 AND ZS=ZS2 AND direction_exec=short`
- Raw: n=154  W=57/L=97  WR=37.0%
- Sharpen: sharpest is T4=T4c (85/97 of losers there)
- **Sharp: n=117  W=32/L=85  WR=27.4%**
- **Dir: SHORT**  •  1h trend AGAINST trade; lower third; zscore -2 to -1 oversold  •  ONLY when 4h trend AGAINST trade

### L18.  `H20=H20d AND BBP=BBP4 AND ZS=ZS4`
- Raw: n=152  W=58/L=94  WR=38.2%
- Sharpen: sharpest is T1=T1c (59/94 of losers there)
- **Sharp: n=59  W=0/L=59  WR=0.0%**
- **Dir: ?**  •  HTF20 mildly against; upper third; zscore +1 to +2 overbought  •  ONLY when 1h trend AGAINST trade

### L19.  `H20=H20e AND RSI=RSI6 AND session_bucket=london_open`
- Raw: n=150  W=50/L=100  WR=33.3%
- Sharpen: sharpest is H60=H60e (99/100 of losers there)
- **Sharp: n=125  W=26/L=99  WR=20.8%**
- **Dir: ?**  •  HTF20 strongly against; RSI 70-80 overbought; session=london_open  •  ONLY when HTF60 strongly against

### L20.  `H20=H20e AND H60=H60e AND T4=T4c AND BBP=BBP2`
- Raw: n=147  W=49/L=98  WR=33.3%
- Sharpen: sharpest is ZS=ZS2 (69/98 of losers there)
- **Sharp: n=92  W=23/L=69  WR=25.0%**
- **Dir: ?**  •  HTF20 strongly against; HTF60 strongly against; 4h trend AGAINST trade; lower third  •  ONLY when zscore -2 to -1 oversold

### L21.  `H20=H20e AND T1=T1c AND T4=T4c AND BBP=BBP2`
- Raw: n=147  W=49/L=98  WR=33.3%
- Sharpen: sharpest is ZS=ZS2 (69/98 of losers there)
- **Sharp: n=92  W=23/L=69  WR=25.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; 4h trend AGAINST trade; lower third  •  ONLY when zscore -2 to -1 oversold

### L22.  `H20=H20e AND T4=T4c AND BBP=BBP2 AND direction_exec=short`
- Raw: n=147  W=49/L=98  WR=33.3%
- Sharpen: sharpest is ZS=ZS2 (69/98 of losers there)
- **Sharp: n=92  W=23/L=69  WR=25.0%**
- **Dir: SHORT**  •  HTF20 strongly against; 4h trend AGAINST trade; lower third  •  ONLY when zscore -2 to -1 oversold

### L23.  `H20=H20e AND T4=T4c AND RSI=RSI5 AND session_bucket=asia`
- Raw: n=147  W=49/L=98  WR=33.3%
- Sharpen: sharpest is BBP=BBP6 (29/98 of losers there)
- **Sharp: n=29  W=0/L=29  WR=0.0%**
- **Dir: ?**  •  HTF20 strongly against; 4h trend AGAINST trade; RSI 60-70 strong; session=asia  •  ONLY when deep above upper band

### L24.  `T4=T4c AND BBP=BBP2 AND ZS=ZS2`
- Raw: n=144  W=44/L=100  WR=30.6%
- Sharpen: sharpest is H20=H20e (72/100 of losers there)
- **Sharp: n=96  W=24/L=72  WR=25.0%**
- **Dir: ?**  •  4h trend AGAINST trade; lower third; zscore -2 to -1 oversold  •  ONLY when HTF20 strongly against

### L25.  `H60=H60e AND RSI=RSI6 AND session_bucket=london_open`
- Raw: n=143  W=32/L=111  WR=22.4%
- Sharpen: sharpest is BBP=BBP6 (28/111 of losers there)
- **Sharp: n=28  W=0/L=28  WR=0.0%**
- **Dir: ?**  •  HTF60 strongly against; RSI 70-80 overbought; session=london_open  •  ONLY when deep above upper band

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | H20e(40/46) |
| H60 | H60a(53/46) | H60e(47/54) |
| T1 | T1a(55/44) | T1c(45/56) |
| T4 | T4a(55/45) | T4c(45/55) |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | long(53/46) | short(47/54) |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
