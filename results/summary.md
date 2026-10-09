# BTC 15-min strategy tracker: FAIL

Data source: INTL_PROXY. INTL_PROXY means trades from the international exchange, used because the US gateway publishes no public trade history.
Real money needs PASS in both the backtest and the live paper run, with the live hit rate within 8 points of the backtest.

## Backtest

- Verdict: **FAIL**
- Windows scored: 700; excluded: 0
- Fill rate: 16.9% of scored windows had a fill (0 too small)
- Fills that reached 45c: 52 of 118 = 44.1% (95% range 35.4% to 53.1%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-12.35 (balance $7.65 from $20)
- Longest losing streak: 9
- Strict vs touch: strict 52/118 = 44.1%; touch 67/136 = 49.3%. The verdict uses strict.

## Live paper run

- Verdict: **FAIL**
- Windows scored: 777; excluded: 0
- Fill rate: 16.2% of scored windows had a fill (0 too small)
- Fills that reached 45c: 57 of 126 = 45.2% (95% range 36.8% to 53.9%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-12.25 (balance $7.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 57/126 = 45.2%; touch 64/138 = 46.4%. The verdict uses strict.

## Spot-checked windows

### 2026-10-09T00:00Z (market 5420076, result up)
Scored: p1 down filled at 68s, exit hit 1; p2 none. Profit p1 0.2.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.5399999568, 5s@0.54, 5s@0.5399999568, 5s@0.54, 6s@0.54, 8s@0.5799999383, 8s@0.5799999882, 8s@0.563262159, 14s@0.54, 15s@0.54, 17s@0.54, 17s@0.5399999985 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 6s@0.455, 8s@0.46, 12s@0.45625, 14s@0.4699999422, 68s@0.24, 68s@0.24, 77s@0.22244, 77s@0.23, 77s@0.22, 152s@0.46, 152s@0.46, 152s@0.4599999568 ...

### 2026-10-09T00:30Z (market 5420598, result up)
Scored: p1 down filled at 69s, exit hit 1; p2 none. Profit p1 0.2.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.46625, 9s@0.45, 11s@0.5099999442, 11s@0.48, 11s@0.5099999215, 11s@0.47, 11s@0.49, 11s@0.4699999674, 11s@0.46, 15s@0.51, 18s@0.55, 18s@0.549999956 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.51, 2s@0.51, 2s@0.5, 2s@0.5090821018, 2s@0.5, 2s@0.498757764, 8s@0.54, 21s@0.4599999034, 27s@0.46, 27s@0.46, 30s@0.48, 30s@0.48 ...

### 2026-10-09T04:00Z (market 5422765, result up)
Scored: p1 down filled at 118s, exit hit 1; p2 none. Profit p1 0.2.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.46, 3s@0.45, 3s@0.45, 3s@0.45, 4s@0.4569761986, 4s@0.47, 10s@0.45, 10s@0.48, 10s@0.45, 10s@0.4799999578, 10s@0.4707692018, 10s@0.45 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5299998463, 3s@0.5599999211, 3s@0.5399999568, 3s@0.5599999955, 3s@0.5599999955, 3s@0.5599999211, 3s@0.559999776, 4s@0.5699999886, 4s@0.54, 4s@0.54, 4s@0.5399999208, 4s@0.5399999705 ...


_Updated 2026-10-09 05:26Z_
