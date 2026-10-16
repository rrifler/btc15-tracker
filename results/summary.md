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
- Windows scored: 1466; excluded: 0
- Fill rate: 17.7% of scored windows had a fill (86 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 131/289 = 45.3%. The verdict uses strict.

## Spot-checked windows

### 2026-10-16T03:30Z (market 5719461, result down)
Scored: p1 up filled at 57s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 16s@0.25, 40s@0.25, 57s@0.16, 61s@0.16, 63s@0.16, 63s@0.16, 63s@0.17, 66s@0.17, 66s@0.17, 66s@0.17, 67s@0.16, 69s@0.17 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.6336423841, 1s@0.64, 3s@0.67, 4s@0.68, 4s@0.682795389, 4s@0.67, 4s@0.69, 4s@0.69, 4s@0.67, 6s@0.7, 7s@0.69, 10s@0.72 ...

### 2026-10-16T03:45Z (market 5719535, result up)
Scored: p1 down filled at 24s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.61, 4s@0.6599999217, 4s@0.649999805, 4s@0.65, 6s@0.66, 6s@0.66, 6s@0.66, 6s@0.6599999836, 6s@0.6599999864, 7s@0.6799999968, 9s@0.6799998912, 9s@0.68 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 24s@0.18, 25s@0.19, 25s@0.19, 25s@0.18, 25s@0.18, 25s@0.1799999836, 28s@0.1799999975, 28s@0.1799999856, 30s@0.15, 30s@0.17, 34s@0.13, 34s@0.13 ...

### 2026-10-16T04:00Z (market 5719888, result down)
Scored: p1 up filled at 52s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.49, 7s@0.47, 52s@0.24, 70s@0.25, 72s@0.25, 78s@0.24, 84s@0.2299999993, 97s@0.2, 102s@0.2, 103s@0.21, 114s@0.23, 117s@0.24 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.5, 9s@0.5599999769, 10s@0.5599999955, 13s@0.5699998604, 13s@0.56, 15s@0.6, 15s@0.57, 16s@0.6, 16s@0.6180769231, 18s@0.66, 18s@0.65, 18s@0.64 ...

### 2026-10-16T05:00Z (market 5721417, result up)
Scored: p1 down filled at 46s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.5, 1s@0.5, 3s@0.56, 3s@0.5599999815, 3s@0.55, 3s@0.5599999923, 3s@0.56, 4s@0.59, 12s@0.629999985, 18s@0.6599999448, 22s@0.6821502965, 22s@0.68 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 46s@0.16, 51s@0.17, 52s@0.17, 52s@0.17, 60s@0.13, 60s@0.1399999988, 63s@0.11, 64s@0.11, 64s@0.1, 64s@0.1, 64s@0.1, 64s@0.1 ...

### 2026-10-16T05:45Z (market 5721980, result up)
Scored: p1 down filled at 102s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5, 6s@0.5, 9s@0.4899998383, 9s@0.49, 21s@0.57, 21s@0.55, 25s@0.58, 25s@0.5799999312, 37s@0.6099999875, 43s@0.66, 43s@0.68, 43s@0.67 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 16s@0.4599999034, 102s@0.2399999991, 105s@0.25, 108s@0.25, 108s@0.25, 108s@0.25, 121s@0.1899999975, 130s@0.19, 130s@0.19, 130s@0.19, 130s@0.1899999962, 139s@0.2 ...


_Updated 2026-10-16 09:36Z_
