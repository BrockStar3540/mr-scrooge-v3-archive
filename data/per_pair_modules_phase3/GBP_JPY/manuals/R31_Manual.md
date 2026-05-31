# GBP_JPY — R31 Manual

## Regime centroid (locked factors)

- **BB = BB3**  (wide bands)
- **A5 = A5_2**  (5m ATR 80-120%)
- **A1 = A1_1**  (1h ATR 2-4x)
- **E20 = E20a**  (EMA20 up >0.5x)
- **E50 = E50a**  (EMA50 up >0.5x)
- **ADR = ADR2**  (30-60%)
- **SPR = SPR2**  (moderate spread)

## Baseline
- Trades: **6,306**  (W=3,803 / L=2,503)  -  WR: **60.3%**

## Session distribution

- asia: n=1935  W=1183/L=752  WR=61.1%
- london_open: n=967  W=593/L=374  WR=61.3%
- ny_mid: n=724  W=445/L=279  WR=61.5%
- ny_open: n=686  W=389/L=297  WR=56.7%
- ny_close: n=683  W=422/L=261  WR=61.8%
- london: n=566  W=348/L=218  WR=61.5%
- asia_late: n=565  W=322/L=243  WR=57.0%
- off_hours: n=180  W=101/L=79  WR=56.1%

## WIN rules (n>=30, WR>=85%) — refined

### W01.  `T1=T1a AND RSI=RSI6 AND session_bucket=london_open`
- Raw: n=133  W=127/L=6  WR=95.5%
- Refine: exclude ZS=ZS6 drops 4/6 losers (67%)
- **Final: n=129  W=127/L=2  WR=98.4%**
- **Dir: ?**  •  1h trend WITH trade; RSI 70-80 overbought; session=london_open  •  AVOID when zscore >+3 extreme

### W02.  `T4=T4a AND RSI=RSI6 AND session_bucket=london_open`
- Raw: n=133  W=127/L=6  WR=95.5%
- Refine: exclude ZS=ZS6 drops 4/6 losers (67%)
- **Final: n=129  W=127/L=2  WR=98.4%**
- **Dir: ?**  •  4h trend WITH trade; RSI 70-80 overbought; session=london_open  •  AVOID when zscore >+3 extreme

### W03.  `RSI=RSI6 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=133  W=127/L=6  WR=95.5%
- Refine: exclude ZS=ZS6 drops 4/6 losers (67%)
- **Final: n=129  W=127/L=2  WR=98.4%**
- **Dir: LONG**  •  RSI 70-80 overbought; session=london_open  •  AVOID when zscore >+3 extreme

### W04.  `T1=T1a AND T4=T4a AND RSI=RSI6 AND session_bucket=london_open`
- Raw: n=133  W=127/L=6  WR=95.5%
- Refine: exclude ZS=ZS6 drops 4/6 losers (67%)
- **Final: n=129  W=127/L=2  WR=98.4%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 70-80 overbought; session=london_open  •  AVOID when zscore >+3 extreme

### W05.  `T1=T1a AND RSI=RSI6 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=133  W=127/L=6  WR=95.5%
- Refine: exclude ZS=ZS6 drops 4/6 losers (67%)
- **Final: n=129  W=127/L=2  WR=98.4%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 70-80 overbought; session=london_open  •  AVOID when zscore >+3 extreme

### W06.  `T4=T4a AND RSI=RSI6 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=133  W=127/L=6  WR=95.5%
- Refine: exclude ZS=ZS6 drops 4/6 losers (67%)
- **Final: n=129  W=127/L=2  WR=98.4%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 70-80 overbought; session=london_open  •  AVOID when zscore >+3 extreme

### W07.  `H60=H60a AND RSI=RSI6 AND session_bucket=london_open`
- Raw: n=130  W=117/L=13  WR=90.0%
- Refine: exclude H20=H20c drops 7/13 losers (54%)
- **Final: n=123  W=117/L=6  WR=95.1%**
- **Dir: ?**  •  HTF60 aligned WITH trade; RSI 70-80 overbought; session=london_open  •  AVOID when HTF20 neutral

### W08.  `H20=H20a AND RSI=RSI6 AND session_bucket=london_open`
- Raw: n=123  W=117/L=6  WR=95.1%
- Refine: exclude ZS=ZS6 drops 4/6 losers (67%)
- **Final: n=119  W=117/L=2  WR=98.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; RSI 70-80 overbought; session=london_open  •  AVOID when zscore >+3 extreme

### W09.  `H20=H20a AND H60=H60a AND RSI=RSI6 AND session_bucket=london_open`
- Raw: n=123  W=117/L=6  WR=95.1%
- Refine: exclude ZS=ZS6 drops 4/6 losers (67%)
- **Final: n=119  W=117/L=2  WR=98.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 70-80 overbought; session=london_open  •  AVOID when zscore >+3 extreme

### W10.  `H20=H20a AND T1=T1a AND RSI=RSI6 AND session_bucket=london_open`
- Raw: n=123  W=117/L=6  WR=95.1%
- Refine: exclude ZS=ZS6 drops 4/6 losers (67%)
- **Final: n=119  W=117/L=2  WR=98.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 1h trend WITH trade; RSI 70-80 overbought; session=london_open  •  AVOID when zscore >+3 extreme

### W11.  `H20=H20a AND T4=T4a AND RSI=RSI6 AND session_bucket=london_open`
- Raw: n=123  W=117/L=6  WR=95.1%
- Refine: exclude ZS=ZS6 drops 4/6 losers (67%)
- **Final: n=119  W=117/L=2  WR=98.3%**
- **Dir: ?**  •  HTF20 aligned WITH trade; 4h trend WITH trade; RSI 70-80 overbought; session=london_open  •  AVOID when zscore >+3 extreme

### W12.  `H20=H20a AND RSI=RSI6 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=123  W=117/L=6  WR=95.1%
- Refine: exclude ZS=ZS6 drops 4/6 losers (67%)
- **Final: n=119  W=117/L=2  WR=98.3%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 70-80 overbought; session=london_open  •  AVOID when zscore >+3 extreme

### W13.  `H60=H60a AND T1=T1a AND RSI=RSI6 AND session_bucket=london_open`
- Raw: n=123  W=117/L=6  WR=95.1%
- Refine: exclude ZS=ZS6 drops 4/6 losers (67%)
- **Final: n=119  W=117/L=2  WR=98.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 70-80 overbought; session=london_open  •  AVOID when zscore >+3 extreme

### W14.  `H60=H60a AND T4=T4a AND RSI=RSI6 AND session_bucket=london_open`
- Raw: n=123  W=117/L=6  WR=95.1%
- Refine: exclude ZS=ZS6 drops 4/6 losers (67%)
- **Final: n=119  W=117/L=2  WR=98.3%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; RSI 70-80 overbought; session=london_open  •  AVOID when zscore >+3 extreme

### W15.  `H60=H60a AND RSI=RSI6 AND direction_exec=long AND session_bucket=london_open`
- Raw: n=123  W=117/L=6  WR=95.1%
- Refine: exclude ZS=ZS6 drops 4/6 losers (67%)
- **Final: n=119  W=117/L=2  WR=98.3%**
- **Dir: LONG**  •  HTF60 aligned WITH trade; RSI 70-80 overbought; session=london_open  •  AVOID when zscore >+3 extreme

### W16.  `H60=H60e AND BBP=BBP6 AND session_bucket=asia`
- Raw: n=114  W=99/L=15  WR=86.8%
- Refine: exclude H20=H20e drops 15/15 losers (100%)
- **Final: n=46  W=46/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; deep above upper band; session=asia  •  AVOID when HTF20 strongly against

### W17.  `T1=T1c AND BBP=BBP6 AND session_bucket=asia`
- Raw: n=114  W=99/L=15  WR=86.8%
- Refine: exclude H20=H20e drops 15/15 losers (100%)
- **Final: n=46  W=46/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; deep above upper band; session=asia  •  AVOID when HTF20 strongly against

### W18.  `BBP=BBP6 AND direction_exec=short AND session_bucket=asia`
- Raw: n=114  W=99/L=15  WR=86.8%
- Refine: exclude H20=H20e drops 15/15 losers (100%)
- **Final: n=46  W=46/L=0  WR=100.0%**
- **Dir: SHORT**  •  deep above upper band; session=asia  •  AVOID when HTF20 strongly against

### W19.  `H60=H60e AND T1=T1c AND BBP=BBP6 AND session_bucket=asia`
- Raw: n=114  W=99/L=15  WR=86.8%
- Refine: exclude H20=H20e drops 15/15 losers (100%)
- **Final: n=46  W=46/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 1h trend AGAINST trade; deep above upper band; session=asia  •  AVOID when HTF20 strongly against

### W20.  `H60=H60e AND BBP=BBP6 AND direction_exec=short AND session_bucket=asia`
- Raw: n=114  W=99/L=15  WR=86.8%
- Refine: exclude H20=H20e drops 15/15 losers (100%)
- **Final: n=46  W=46/L=0  WR=100.0%**
- **Dir: SHORT**  •  HTF60 strongly against; deep above upper band; session=asia  •  AVOID when HTF20 strongly against

### W21.  `T1=T1c AND BBP=BBP6 AND direction_exec=short AND session_bucket=asia`
- Raw: n=114  W=99/L=15  WR=86.8%
- Refine: exclude H20=H20e drops 15/15 losers (100%)
- **Final: n=46  W=46/L=0  WR=100.0%**
- **Dir: SHORT**  •  1h trend AGAINST trade; deep above upper band; session=asia  •  AVOID when HTF20 strongly against

### W22.  `H60=H60e AND BBP=BBP6 AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=102  W=87/L=15  WR=85.3%
- Refine: exclude H20=H20e drops 15/15 losers (100%)
- **Final: n=46  W=46/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; deep above upper band; zscore +2 to +3 deep overbought; session=asia  •  AVOID when HTF20 strongly against

### W23.  `T1=T1c AND BBP=BBP6 AND ZS=ZS5 AND session_bucket=asia`
- Raw: n=102  W=87/L=15  WR=85.3%
- Refine: exclude H20=H20e drops 15/15 losers (100%)
- **Final: n=46  W=46/L=0  WR=100.0%**
- **Dir: ?**  •  1h trend AGAINST trade; deep above upper band; zscore +2 to +3 deep overbought; session=asia  •  AVOID when HTF20 strongly against

### W24.  `BBP=BBP6 AND ZS=ZS5 AND direction_exec=short AND session_bucket=asia`
- Raw: n=102  W=87/L=15  WR=85.3%
- Refine: exclude H20=H20e drops 15/15 losers (100%)
- **Final: n=46  W=46/L=0  WR=100.0%**
- **Dir: SHORT**  •  deep above upper band; zscore +2 to +3 deep overbought; session=asia  •  AVOID when HTF20 strongly against

### W25.  `H60=H60e AND T4=T4c AND BBP=BBP6 AND session_bucket=asia`
- Raw: n=100  W=85/L=15  WR=85.0%
- Refine: exclude H20=H20e drops 15/15 losers (100%)
- **Final: n=32  W=32/L=0  WR=100.0%**
- **Dir: ?**  •  HTF60 strongly against; 4h trend AGAINST trade; deep above upper band; session=asia  •  AVOID when HTF20 strongly against

## LOSE rules (AVOID — n>=30, WR<=40%) — sharpened

### L01.  `H60=H60a AND BBP=BBP5 AND RSI=RSI5`
- Raw: n=206  W=81/L=125  WR=39.3%
- Sharpen: sharpest is session_bucket=ny_open (25/125 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; just touched upper band; RSI 60-70 strong  •  ONLY when session=ny_open

### L02.  `H60=H60a AND BBP=BBP5 AND RSI=RSI5 AND ZS=ZS5`
- Raw: n=206  W=81/L=125  WR=39.3%
- Sharpen: sharpest is session_bucket=ny_open (25/125 of losers there)
- **Sharp: n=25  W=0/L=25  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; just touched upper band; RSI 60-70 strong; zscore +2 to +3 deep overbought  •  ONLY when session=ny_open

### L03.  `H60=H60a AND T4=T4a AND BBP=BBP5 AND RSI=RSI5`
- Raw: n=168  W=66/L=102  WR=39.3%
- Sharpen: sharpest is session_bucket=ny_open (19/102 of losers there)
- **Sharp: n=19  W=0/L=19  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 4h trend WITH trade; just touched upper band; RSI 60-70 strong  •  ONLY when session=ny_open

### L04.  `RSI=RSI4 AND ZS=ZS3 AND direction_exec=long`
- Raw: n=157  W=62/L=95  WR=39.5%
- Sharpen: sharpest is session_bucket=ny_mid (22/95 of losers there)
- **Sharp: n=26  W=4/L=22  WR=15.4%**
- **Dir: LONG**  •  RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  ONLY when session=ny_mid

### L05.  `T1=T1c AND strategy_id=alpha_extended_fade_v2 AND direction_exec=short`
- Raw: n=152  W=59/L=93  WR=38.8%
- Sharpen: no sharper sub-pattern
- **Sharp: n=152  W=59/L=93  WR=38.8%**
- **Dir: SHORT**  •  1h trend AGAINST trade; strategy=alpha_extended_fade_v2

### L06.  `T1=T1c AND T4=T4c AND strategy_id=alpha_extended_fade_v2`
- Raw: n=138  W=53/L=85  WR=38.4%
- Sharpen: no sharper sub-pattern
- **Sharp: n=138  W=53/L=85  WR=38.4%**
- **Dir: ?**  •  1h trend AGAINST trade; 4h trend AGAINST trade; strategy=alpha_extended_fade_v2

### L07.  `T4=T4c AND strategy_id=alpha_extended_fade_v2 AND direction_exec=short`
- Raw: n=138  W=53/L=85  WR=38.4%
- Sharpen: no sharper sub-pattern
- **Sharp: n=138  W=53/L=85  WR=38.4%**
- **Dir: SHORT**  •  4h trend AGAINST trade; strategy=alpha_extended_fade_v2

### L08.  `T1=T1c AND T4=T4c AND strategy_id=alpha_extended_fade_v2 AND direction_exec=short`
- Raw: n=138  W=53/L=85  WR=38.4%
- Sharpen: no sharper sub-pattern
- **Sharp: n=138  W=53/L=85  WR=38.4%**
- **Dir: SHORT**  •  1h trend AGAINST trade; 4h trend AGAINST trade; strategy=alpha_extended_fade_v2

### L09.  `T1=T1c AND RSI=RSI5 AND ZS=ZS3 AND session_bucket=asia`
- Raw: n=136  W=53/L=83  WR=39.0%
- Sharpen: sharpest is BBP=BBP3 (63/83 of losers there)
- **Sharp: n=93  W=30/L=63  WR=32.3%**
- **Dir: ?**  •  1h trend AGAINST trade; RSI 60-70 strong; zscore -1 to +1 neutral; session=asia  •  ONLY when middle of band

### L10.  `T4=T4c AND RSI=RSI5 AND ZS=ZS3 AND session_bucket=asia`
- Raw: n=136  W=53/L=83  WR=39.0%
- Sharpen: sharpest is BBP=BBP3 (63/83 of losers there)
- **Sharp: n=93  W=30/L=63  WR=32.3%**
- **Dir: ?**  •  4h trend AGAINST trade; RSI 60-70 strong; zscore -1 to +1 neutral; session=asia  •  ONLY when middle of band

### L11.  `RSI=RSI5 AND ZS=ZS3 AND direction_exec=short AND session_bucket=asia`
- Raw: n=136  W=53/L=83  WR=39.0%
- Sharpen: sharpest is BBP=BBP3 (63/83 of losers there)
- **Sharp: n=93  W=30/L=63  WR=32.3%**
- **Dir: SHORT**  •  RSI 60-70 strong; zscore -1 to +1 neutral; session=asia  •  ONLY when middle of band

### L12.  `T4=T4a AND RSI=RSI4 AND ZS=ZS3 AND direction_exec=long`
- Raw: n=134  W=52/L=82  WR=38.8%
- Sharpen: sharpest is session_bucket=ny_mid (22/82 of losers there)
- **Sharp: n=26  W=4/L=22  WR=15.4%**
- **Dir: LONG**  •  4h trend WITH trade; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  ONLY when session=ny_mid

### L13.  `T1=T1a AND RSI=RSI4 AND ZS=ZS3 AND direction_exec=long`
- Raw: n=133  W=50/L=83  WR=37.6%
- Sharpen: sharpest is session_bucket=london_open (13/83 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: LONG**  •  1h trend WITH trade; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  ONLY when session=london_open

### L14.  `H60=H60a AND T1=T1a AND RSI=RSI4 AND ZS=ZS3`
- Raw: n=128  W=50/L=78  WR=39.1%
- Sharpen: sharpest is session_bucket=london_open (13/78 of losers there)
- **Sharp: n=13  W=0/L=13  WR=0.0%**
- **Dir: ?**  •  HTF60 aligned WITH trade; 1h trend WITH trade; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  ONLY when session=london_open

### L15.  `T4=T4a AND RSI=RSI5 AND session_bucket=ny_open`
- Raw: n=127  W=47/L=80  WR=37.0%
- Sharpen: sharpest is ZS=ZS5 (28/80 of losers there)
- **Sharp: n=28  W=0/L=28  WR=0.0%**
- **Dir: ?**  •  4h trend WITH trade; RSI 60-70 strong; session=ny_open  •  ONLY when zscore +2 to +3 deep overbought

### L16.  `H60=H60e AND RSI=RSI5 AND ZS=ZS3 AND session_bucket=asia`
- Raw: n=123  W=47/L=76  WR=38.2%
- Sharpen: no sharper sub-pattern
- **Sharp: n=123  W=47/L=76  WR=38.2%**
- **Dir: ?**  •  HTF60 strongly against; RSI 60-70 strong; zscore -1 to +1 neutral; session=asia

### L17.  `H60=H60e AND T4=T4a AND BBP=BBP4 AND direction_exec=short`
- Raw: n=116  W=45/L=71  WR=38.8%
- Sharpen: sharpest is session_bucket=ny_open (34/71 of losers there)
- **Sharp: n=35  W=1/L=34  WR=2.9%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend WITH trade; upper third  •  ONLY when session=ny_open

### L18.  `T4=T4c AND ZS=ZS4 AND session_bucket=london`
- Raw: n=113  W=43/L=70  WR=38.1%
- Sharpen: sharpest is H60=H60a (20/70 of losers there)
- **Sharp: n=25  W=5/L=20  WR=20.0%**
- **Dir: ?**  •  4h trend AGAINST trade; zscore +1 to +2 overbought; session=london  •  ONLY when HTF60 aligned WITH trade

### L19.  `T4=T4c AND BBP=BBP4 AND ZS=ZS4 AND session_bucket=london`
- Raw: n=113  W=43/L=70  WR=38.1%
- Sharpen: sharpest is H60=H60a (20/70 of losers there)
- **Sharp: n=25  W=5/L=20  WR=20.0%**
- **Dir: ?**  •  4h trend AGAINST trade; upper third; zscore +1 to +2 overbought; session=london  •  ONLY when HTF60 aligned WITH trade

### L20.  `H60=H60e AND T4=T4a AND ZS=ZS4 AND direction_exec=short`
- Raw: n=113  W=45/L=68  WR=39.8%
- Sharpen: sharpest is session_bucket=ny_open (34/68 of losers there)
- **Sharp: n=35  W=1/L=34  WR=2.9%**
- **Dir: SHORT**  •  HTF60 strongly against; 4h trend WITH trade; zscore +1 to +2 overbought  •  ONLY when session=ny_open

### L21.  `T1=T1a AND T4=T4a AND RSI=RSI4 AND ZS=ZS3`
- Raw: n=110  W=40/L=70  WR=36.4%
- Sharpen: sharpest is session_bucket=ny_mid (11/70 of losers there)
- **Sharp: n=11  W=0/L=11  WR=0.0%**
- **Dir: ?**  •  1h trend WITH trade; 4h trend WITH trade; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  ONLY when session=ny_mid

### L22.  `H20=H20a AND H60=H60a AND RSI=RSI4 AND ZS=ZS3`
- Raw: n=110  W=41/L=69  WR=37.3%
- Sharpen: sharpest is session_bucket=ny_mid (18/69 of losers there)
- **Sharp: n=22  W=4/L=18  WR=18.2%**
- **Dir: ?**  •  HTF20 aligned WITH trade; HTF60 aligned WITH trade; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  ONLY when session=ny_mid

### L23.  `H20=H20a AND RSI=RSI4 AND ZS=ZS3 AND direction_exec=long`
- Raw: n=110  W=41/L=69  WR=37.3%
- Sharpen: sharpest is session_bucket=ny_mid (18/69 of losers there)
- **Sharp: n=22  W=4/L=18  WR=18.2%**
- **Dir: LONG**  •  HTF20 aligned WITH trade; RSI 50-60 upper neutral; zscore -1 to +1 neutral  •  ONLY when session=ny_mid

### L24.  `H20=H20e AND T1=T1c AND strategy_id=alpha_extended_fade_v2`
- Raw: n=110  W=44/L=66  WR=40.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=110  W=44/L=66  WR=40.0%**
- **Dir: ?**  •  HTF20 strongly against; 1h trend AGAINST trade; strategy=alpha_extended_fade_v2

### L25.  `H20=H20e AND strategy_id=alpha_extended_fade_v2 AND direction_exec=short`
- Raw: n=110  W=44/L=66  WR=40.0%
- Sharpen: no sharper sub-pattern
- **Sharp: n=110  W=44/L=66  WR=40.0%**
- **Dir: SHORT**  •  HTF20 strongly against; strategy=alpha_extended_fade_v2

## Cross-cutting factor analysis (this regime)

| factor | winner-dominant | loser-dominant |
|---|---|---|
| H20 | — | — |
| H60 | — | — |
| T1 | T1a(52/47) | T1c(48/53) |
| T4 | — | — |
| BBP | — | — |
| RSI | — | — |
| ZS | — | — |
| strategy_id | — | — |
| direction_exec | — | — |
| session_bucket | — | — |

*Read: `bucket(winner%/loser%)`.*
