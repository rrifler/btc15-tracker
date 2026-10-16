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
- Windows scored: 1446; excluded: 0
- Fill rate: 17.6% of scored windows had a fill (81 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 130/284 = 45.8%. The verdict uses strict.

## Spot-checked windows

### 2026-10-15T23:00Z (market 5713475, result down)
Scored: p1 up filled at 57s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 57s@0.23, 57s@0.23, 57s@0.23, 57s@0.2299999517, 58s@0.23, 61s@0.24, 64s@0.22, 66s@0.2199999683, 73s@0.19, 73s@0.19, 73s@0.1899999982, 75s@0.19 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.56, 7s@0.65, 12s@0.6499999959, 13s@0.65, 25s@0.66, 28s@0.71, 28s@0.71, 28s@0.7099999606, 28s@0.6899999795, 28s@0.66, 31s@0.72, 34s@0.7299999863 ...

### 2026-10-16T00:45Z (market 5716795, result down)
Scored: p1 up filled at 57s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 39s@0.25, 40s@0.25, 42s@0.25, 57s@0.229999994, 60s@0.22, 60s@0.22, 63s@0.23, 64s@0.2327911559, 75s@0.22, 79s@0.22, 81s@0.23, 81s@0.23 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5399999568, 6s@0.6099999984, 6s@0.6, 6s@0.6099999984, 6s@0.5999999952, 6s@0.5999999952, 7s@0.62, 9s@0.629999978, 9s@0.6199999864, 9s@0.6278272539, 9s@0.62, 12s@0.64 ...

### 2026-10-16T02:45Z (market 5719136, result down)
Scored: p1 up filled at 87s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.45, 87s@0.24, 91s@0.21, 91s@0.2099999895, 93s@0.22, 94s@0.2254901931, 99s@0.23, 99s@0.23, 105s@0.2, 115s@0.219999978, 115s@0.22, 117s@0.22 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 9s@0.5699999886, 21s@0.559999776, 27s@0.62, 30s@0.62, 30s@0.6199999449, 31s@0.62, 31s@0.62, 33s@0.63, 34s@0.64, 40s@0.67, 40s@0.6765376779, 43s@0.6899999917 ...

### 2026-10-16T03:30Z (market 5719461, result down)
Scored: p1 up filled at 57s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 16s@0.25, 40s@0.25, 57s@0.16, 61s@0.16, 63s@0.16, 63s@0.16, 63s@0.17, 66s@0.17, 66s@0.17, 66s@0.17, 67s@0.16, 69s@0.17 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.6336423841, 1s@0.64, 3s@0.67, 4s@0.68, 4s@0.682795389, 4s@0.67, 4s@0.69, 4s@0.69, 4s@0.67, 6s@0.7, 7s@0.69, 10s@0.72 ...

### 2026-10-16T03:45Z (market 5719535, result up)
Scored: p1 down filled at 24s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.61, 4s@0.6599999217, 4s@0.649999805, 4s@0.65, 6s@0.66, 6s@0.66, 6s@0.66, 6s@0.6599999836, 6s@0.6599999864, 7s@0.6799999968, 9s@0.6799998912, 9s@0.68 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 24s@0.18, 25s@0.19, 25s@0.19, 25s@0.18, 25s@0.18, 25s@0.1799999836, 28s@0.1799999975, 28s@0.1799999856, 30s@0.15, 30s@0.17, 34s@0.13, 34s@0.13 ...


_Updated 2026-10-16 04:35Z_
