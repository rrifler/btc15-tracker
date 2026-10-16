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
- Windows scored: 1470; excluded: 0
- Fill rate: 17.8% of scored windows had a fill (87 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 131/290 = 45.2%. The verdict uses strict.

## Spot-checked windows

### 2026-10-16T05:00Z (market 5721417, result up)
Scored: p1 down filled at 46s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.5, 1s@0.5, 3s@0.56, 3s@0.5599999815, 3s@0.55, 3s@0.5599999923, 3s@0.56, 4s@0.59, 12s@0.629999985, 18s@0.6599999448, 22s@0.6821502965, 22s@0.68 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 46s@0.16, 51s@0.17, 52s@0.17, 52s@0.17, 60s@0.13, 60s@0.1399999988, 63s@0.11, 64s@0.11, 64s@0.1, 64s@0.1, 64s@0.1, 64s@0.1 ...

### 2026-10-16T05:45Z (market 5721980, result up)
Scored: p1 down filled at 102s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5, 6s@0.5, 9s@0.4899998383, 9s@0.49, 21s@0.57, 21s@0.55, 25s@0.58, 25s@0.5799999312, 37s@0.6099999875, 43s@0.66, 43s@0.68, 43s@0.67 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 16s@0.4599999034, 102s@0.2399999991, 105s@0.25, 108s@0.25, 108s@0.25, 108s@0.25, 121s@0.1899999975, 130s@0.19, 130s@0.19, 130s@0.19, 130s@0.1899999962, 139s@0.2 ...

### 2026-10-16T06:30Z (market 5722916, result up)
Scored: p1 down filled at 84s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 13s@0.6420972571, 18s@0.66, 25s@0.62, 25s@0.62, 25s@0.61, 27s@0.6299999795, 28s@0.6299998362, 30s@0.64, 30s@0.65, 30s@0.6299999787, 30s@0.64, 30s@0.64 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 67s@0.25, 69s@0.25, 75s@0.25, 79s@0.25, 84s@0.22, 90s@0.2, 90s@0.2099999895, 93s@0.2099999895, 102s@0.18, 105s@0.1799999916, 118s@0.14, 120s@0.15 ...

### 2026-10-16T09:00Z (market 5725301, result up)
Scored: p1 up filled at 81s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 81s@0.2299999994, 81s@0.22, 88s@0.23, 91s@0.2299999517, 91s@0.23, 94s@0.2099999895, 94s@0.2099999895, 94s@0.2099999895, 96s@0.2099999895, 99s@0.22, 99s@0.22, 99s@0.2099999995 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.5899998275, 4s@0.61, 4s@0.61, 4s@0.613138679, 4s@0.61, 12s@0.5799999995, 13s@0.62, 13s@0.6180769231, 13s@0.59, 15s@0.6455555556, 16s@0.659999963, 16s@0.6599999673 ...

### 2026-10-16T09:15Z (market 5725341, result down)
Scored: p1 up filled at 94s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 10s@0.4599999387, 12s@0.47, 94s@0.2299999984, 94s@0.23, 94s@0.23, 94s@0.23, 94s@0.23, 99s@0.229999994, 100s@0.2299999693, 102s@0.2299999517, 105s@0.23, 106s@0.24 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.56, 4s@0.5363859139, 22s@0.55, 28s@0.6, 31s@0.6199998946, 31s@0.6199999758, 31s@0.6199998946, 34s@0.64, 34s@0.64, 34s@0.6434009982, 34s@0.63, 34s@0.6299999181 ...


_Updated 2026-10-16 10:37Z_
