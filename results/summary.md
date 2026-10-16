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
- Windows scored: 1434; excluded: 0
- Fill rate: 17.5% of scored windows had a fill (77 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 130/280 = 46.4%. The verdict uses strict.

## Spot-checked windows

### 2026-10-15T19:30Z (market 5699967, result down)
Scored: p1 up filled at 35s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 35s@0.2, 35s@0.2099999983, 37s@0.2, 37s@0.2, 38s@0.21, 53s@0.21, 53s@0.21, 53s@0.21, 64s@0.22, 73s@0.24, 73s@0.22, 73s@0.23 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.66, 4s@0.65, 4s@0.6599999954, 4s@0.6499999951, 4s@0.65, 5s@0.69, 7s@0.72, 8s@0.75, 8s@0.75, 8s@0.74, 8s@0.75, 10s@0.75 ...

### 2026-10-15T21:45Z (market 5709976, result up)
Scored: p1 up filled at 104s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 9s@0.46, 101s@0.25, 104s@0.2399999808, 105s@0.25, 215s@0.48, 215s@0.5, 216s@0.49, 216s@0.5, 225s@0.4558750972, 228s@0.495, 231s@0.5, 233s@0.51 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 9s@0.549999945, 11s@0.5499999214, 14s@0.5825, 14s@0.56, 14s@0.56, 18s@0.6, 24s@0.57, 27s@0.5999999607, 27s@0.59, 27s@0.58, 29s@0.6099997255, 29s@0.6099999488 ...

### 2026-10-15T22:00Z (market 5710129, result up)
Scored: p1 down filled at 74s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 11s@0.6054612789, 12s@0.62, 23s@0.5299999868, 32s@0.51, 36s@0.5999999859, 36s@0.56, 36s@0.56, 36s@0.5599999851, 36s@0.56, 36s@0.56, 36s@0.54, 38s@0.64 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 23s@0.4799998464, 26s@0.48, 65s@0.25, 65s@0.25, 66s@0.25, 66s@0.25, 68s@0.25, 68s@0.25, 74s@0.2399999808, 74s@0.2399999992, 78s@0.2051719683, 78s@0.2099999895 ...

### 2026-10-15T23:00Z (market 5713475, result down)
Scored: p1 up filled at 57s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 57s@0.23, 57s@0.23, 57s@0.23, 57s@0.2299999517, 58s@0.23, 61s@0.24, 64s@0.22, 66s@0.2199999683, 73s@0.19, 73s@0.19, 73s@0.1899999982, 75s@0.19 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.56, 7s@0.65, 12s@0.6499999959, 13s@0.65, 25s@0.66, 28s@0.71, 28s@0.71, 28s@0.7099999606, 28s@0.6899999795, 28s@0.66, 31s@0.72, 34s@0.7299999863 ...

### 2026-10-16T00:45Z (market 5716795, result down)
Scored: p1 up filled at 57s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 39s@0.25, 40s@0.25, 42s@0.25, 57s@0.229999994, 60s@0.22, 60s@0.22, 63s@0.23, 64s@0.2327911559, 75s@0.22, 79s@0.22, 81s@0.23, 81s@0.23 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5399999568, 6s@0.6099999984, 6s@0.6, 6s@0.6099999984, 6s@0.5999999952, 6s@0.5999999952, 7s@0.62, 9s@0.629999978, 9s@0.6199999864, 9s@0.6278272539, 9s@0.62, 12s@0.64 ...


_Updated 2026-10-16 01:35Z_
