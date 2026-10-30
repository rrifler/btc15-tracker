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
- Windows scored: 2846; excluded: 4 (trades_truncated: 2, no_trades: 2)
- Fill rate: 19.3% of scored windows had a fill (375 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 282/612 = 46.1%. The verdict uses strict.

## Spot-checked windows

### 2026-10-30T18:15Z (market 6395590, result down)
Scored: p1 up filled at 115s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.5499999954, 4s@0.5199999792, 9s@0.5199999954, 21s@0.4599999951, 24s@0.4599999669, 45s@0.46, 54s@0.47, 54s@0.4645833333, 115s@0.2399999808, 121s@0.2399999808, 129s@0.219999978, 133s@0.2199999994 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.4899999654, 7s@0.49, 9s@0.54, 9s@0.53, 9s@0.5199999843, 9s@0.5229784884, 9s@0.5199999843, 9s@0.5072132724, 9s@0.5, 9s@0.5, 9s@0.4948770833, 10s@0.55 ...

### 2026-10-30T20:00Z (market 6398707, result up)
Scored: p1 down filled at 108s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.5, 6s@0.47, 13s@0.48, 31s@0.4599999557, 31s@0.46, 31s@0.4599999444, 33s@0.4599999444, 39s@0.4599999387, 40s@0.48, 43s@0.52, 43s@0.5, 45s@0.5328947149 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5399999568, 6s@0.5699999886, 7s@0.55, 10s@0.5499999738, 12s@0.55, 18s@0.5899998466, 19s@0.59, 24s@0.5699999673, 25s@0.5599999961, 25s@0.5599999961, 33s@0.559999776, 34s@0.55 ...

### 2026-10-30T21:00Z (market 6401179, result down)
Scored: p1 down filled at 87s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 7s@0.52, 10s@0.5199997957, 13s@0.5199999792, 15s@0.5199999792, 24s@0.5199999792, 31s@0.5399999568, 33s@0.5399999921, 34s@0.5399999568, 36s@0.54, 37s@0.5499999904, 39s@0.55, 45s@0.59 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 10s@0.489999952, 18s@0.4899999824, 19s@0.4899999584, 22s@0.4899999633, 33s@0.47, 42s@0.45, 87s@0.22, 91s@0.2, 91s@0.2, 93s@0.1899999962, 103s@0.1899999962, 105s@0.19 ...

### 2026-10-30T21:15Z (market 6401225, result up)
Scored: p1 down filled at 100s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 7s@0.5, 7s@0.5, 7s@0.5, 10s@0.5, 19s@0.549999945, 19s@0.53, 19s@0.5199999792, 22s@0.59, 22s@0.5899999864, 25s@0.62, 31s@0.57, 33s@0.5899998466 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.5, 3s@0.51, 4s@0.51, 6s@0.51, 10s@0.5150487277, 19s@0.47, 100s@0.2399999808, 105s@0.2399999808, 117s@0.21, 121s@0.2, 132s@0.2, 132s@0.219999978 ...

### 2026-10-30T22:00Z (market 6402128, result up)
Scored: p1 down filled at 90s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5799999768, 6s@0.625, 6s@0.59, 7s@0.6599997888, 7s@0.65, 7s@0.64, 7s@0.64, 9s@0.6599999903, 19s@0.6599997888, 22s@0.6799999685, 22s@0.6799999767, 24s@0.6999999803 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 90s@0.24, 90s@0.24, 90s@0.23, 90s@0.23, 91s@0.24, 91s@0.25, 91s@0.25, 94s@0.25, 124s@0.22, 127s@0.23, 129s@0.25, 129s@0.24 ...


_Updated 2026-10-30 23:41Z_
