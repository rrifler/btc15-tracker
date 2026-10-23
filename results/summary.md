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
- Windows scored: 2192; excluded: 1 (trades_truncated: 1)
- Fill rate: 19.1% of scored windows had a fill (244 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 212/463 = 45.8%. The verdict uses strict.

## Spot-checked windows

### 2026-10-23T18:00Z (market 6053841, result down)
Scored: p1 up filled at 90s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 90s@0.24, 101s@0.25, 147s@0.24, 168s@0.25, 168s@0.25, 176s@0.24, 191s@0.21, 192s@0.2199999941, 194s@0.2199999974, 195s@0.2299999756, 200s@0.2299999987, 206s@0.2299999782 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.63, 5s@0.63, 5s@0.63, 5s@0.6235979513, 5s@0.63, 15s@0.65, 17s@0.67, 17s@0.6899999754, 18s@0.69, 20s@0.69, 41s@0.71, 47s@0.72 ...

### 2026-10-23T22:00Z (market 6066753, result down)
Scored: p1 down filled at 72s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.57, 3s@0.5799999768, 5s@0.6899999966, 5s@0.69, 5s@0.6799999562, 5s@0.68, 5s@0.6799999299, 5s@0.6799999212, 5s@0.6848838279, 5s@0.6799998776, 5s@0.6799999892, 5s@0.6799999856 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 20s@0.25, 20s@0.25, 20s@0.25, 21s@0.25, 21s@0.25, 21s@0.25, 21s@0.25, 21s@0.25, 21s@0.25, 21s@0.25, 21s@0.25, 21s@0.25 ...

### 2026-10-23T22:15Z (market 6067265, result up)
Scored: p1 down filled at 107s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.530899451, 6s@0.5399999568, 6s@0.54, 8s@0.5899999705, 18s@0.57, 21s@0.5799999768, 33s@0.5899999705, 35s@0.5899999705, 42s@0.6499999495, 45s@0.6, 47s@0.5799999768, 65s@0.61 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 12s@0.48, 12s@0.47, 14s@0.47, 105s@0.25, 107s@0.24, 152s@0.25, 153s@0.25, 209s@0.2359982883, 215s@0.25, 216s@0.25, 231s@0.24, 257s@0.24 ...

### 2026-10-23T22:30Z (market 6067895, result down)
Scored: p1 up filled at 42s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 42s@0.24, 42s@0.2399999808, 42s@0.24, 44s@0.23, 44s@0.23, 44s@0.24, 44s@0.23, 44s@0.24, 45s@0.21, 45s@0.21, 45s@0.2099999779, 45s@0.2099999895 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 6s@0.5824248662, 6s@0.59999988, 6s@0.59, 8s@0.6, 8s@0.59999994, 9s@0.599999976, 9s@0.599999988, 12s@0.6499999923, 12s@0.65, 12s@0.6499999789, 12s@0.65, 12s@0.6499999665 ...


_Updated 2026-10-23 23:33Z_
