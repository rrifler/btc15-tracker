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
- Windows scored: 2961; excluded: 13 (trades_truncated: 2, no_trades: 2, market_not_found: 9)
- Fill rate: 19.2% of scored windows had a fill (394 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 287/634 = 45.3%. The verdict uses strict.

## Spot-checked windows

### 2026-11-01T01:45Z (market 6441421, result down)
Scored: p1 up filled at 55s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 55s@0.23, 55s@0.23, 57s@0.23, 60s@0.2299999998, 63s@0.2409370598, 64s@0.2099999895, 70s@0.2, 79s@0.24, 85s@0.25, 93s@0.21, 93s@0.21, 103s@0.16 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.6466395968, 0s@0.6299999491, 0s@0.629999995, 1s@0.6404760127, 3s@0.6, 3s@0.5999999172, 3s@0.58, 3s@0.5999998966, 3s@0.6, 3s@0.5999998966, 3s@0.5999999617, 3s@0.5999998983 ...

### 2026-11-01T02:45Z (market 6442324, result up)
Scored: p1 down filled at 99s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.6674761994, 0s@0.68, 3s@0.6199998512, 3s@0.6199999569, 3s@0.6199999229, 3s@0.6199999562, 3s@0.6199999501, 3s@0.6199998512, 6s@0.6499999618, 9s@0.59, 13s@0.5999999952, 15s@0.61 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 93s@0.25, 99s@0.21, 100s@0.2099999996, 102s@0.2, 102s@0.21, 108s@0.2, 118s@0.17, 121s@0.16, 123s@0.17, 124s@0.1699999983, 126s@0.13, 127s@0.14 ...

### 2026-11-01T03:45Z (market 6443229, result down)
Scored: p1 up filled at 85s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 7s@0.45, 85s@0.21, 97s@0.1960590564, 99s@0.1899999962, 102s@0.19, 111s@0.2, 114s@0.17, 115s@0.1799999856, 117s@0.18, 117s@0.18, 118s@0.17, 118s@0.18 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.6687997013, 0s@0.6557994959, 3s@0.58, 3s@0.5799999768, 3s@0.5799998215, 3s@0.5799999833, 3s@0.5799998764, 3s@0.58, 3s@0.5799999792, 3s@0.58, 4s@0.5699999556, 4s@0.58 ...

### 2026-11-01T07:00Z (market 6447602, result down)
Scored: p1 up filled at 67s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 67s@0.22, 67s@0.22, 69s@0.22, 87s@0.24, 108s@0.2223616221, 214s@0.2399999808, 229s@0.25, 286s@0.16, 291s@0.16, 307s@0.16, 307s@0.16, 345s@0.21 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.6499999527, 4s@0.65, 4s@0.65, 4s@0.6499999935, 6s@0.65, 7s@0.65, 7s@0.654, 18s@0.6999999882, 18s@0.6999999882, 30s@0.7299999927, 48s@0.75, 49s@0.75 ...


_Updated 2026-11-01 07:28Z_
