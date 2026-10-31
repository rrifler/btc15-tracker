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
- Windows scored: 2869; excluded: 4 (trades_truncated: 2, no_trades: 2)
- Fill rate: 19.3% of scored windows had a fill (380 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 284/617 = 46.0%. The verdict uses strict.

## Spot-checked windows

### 2026-10-30T23:15Z (market 6403163, result up)
Scored: p1 up filled at 105s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.45, 105s@0.22, 105s@0.23, 123s@0.219999978, 123s@0.2, 126s@0.2, 129s@0.2099999738, 130s@0.2, 130s@0.19, 130s@0.17, 135s@0.21, 135s@0.2013422815 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5699998981, 3s@0.5699999261, 3s@0.5631988211, 4s@0.5799999875, 4s@0.5799999875, 4s@0.5734036939, 4s@0.58, 4s@0.5718392021, 6s@0.629999974, 6s@0.59, 7s@0.63, 30s@0.6199999167 ...

### 2026-10-31T01:15Z (market 6405245, result down)
Scored: p1 down filled at 72s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.45, 9s@0.4899999968, 12s@0.5, 12s@0.549999945, 12s@0.52, 13s@0.5299999607, 13s@0.5299999607, 13s@0.5299999607, 16s@0.55, 33s@0.549999956, 34s@0.6099999756, 39s@0.6 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5499999763, 3s@0.5399999485, 4s@0.5299999916, 4s@0.5299999916, 4s@0.5299999916, 4s@0.5299999868, 9s@0.52, 12s@0.469999991, 12s@0.4699999944, 12s@0.49, 12s@0.5099999949, 13s@0.4799998664 ...

### 2026-10-31T03:00Z (market 6406021, result down)
Scored: p1 up filled at 73s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.45, 3s@0.45, 15s@0.4599999669, 15s@0.4599999986, 34s@0.459999988, 34s@0.4599999669, 34s@0.4599997976, 67s@0.25, 73s@0.226, 78s@0.2299999517, 79s@0.23, 82s@0.24 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5699999214, 3s@0.5599998841, 3s@0.5499999425, 3s@0.5499999295, 3s@0.5499998778, 3s@0.5499999763, 4s@0.5699999214, 9s@0.5699999774, 21s@0.5399999568, 21s@0.5399999568, 31s@0.5350059385, 33s@0.5399999215 ...

### 2026-10-31T03:30Z (market 6406125, result down)
Scored: p1 up filled at 100s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 100s@0.25, 100s@0.24, 102s@0.25, 103s@0.25, 180s@0.22, 181s@0.2104166667, 181s@0.21, 184s@0.19, 184s@0.19, 184s@0.19, 184s@0.19, 184s@0.19 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5699999214, 3s@0.5699999886, 3s@0.5699999214, 3s@0.5699999172, 3s@0.5699999214, 3s@0.5699998084, 3s@0.57, 13s@0.5699999525, 18s@0.5699999133, 19s@0.6599999536, 19s@0.6599999656, 19s@0.6599999827 ...

### 2026-10-31T04:00Z (market 6406415, result up)
Scored: p1 down filled at 87s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.5699999918, 3s@0.5399998231, 3s@0.5399998231, 3s@0.5399998231, 3s@0.54, 3s@0.5399998231, 3s@0.5399998231, 3s@0.539999903, 3s@0.539999903, 3s@0.539999991, 3s@0.539999903, 3s@0.5399999297 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.465696, 3s@0.47, 3s@0.45, 3s@0.46, 3s@0.46, 3s@0.45, 6s@0.48, 6s@0.48, 25s@0.4599999462, 25s@0.4599999462, 25s@0.4599999462, 25s@0.46 ...


_Updated 2026-10-31 05:29Z_
