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
- Windows scored: 2986; excluded: 13 (trades_truncated: 2, no_trades: 2, market_not_found: 9)
- Fill rate: 19.3% of scored windows had a fill (401 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 289/641 = 45.1%. The verdict uses strict.

## Spot-checked windows

### 2026-11-01T08:30Z (market 6449399, result up)
Scored: p1 down filled at 31s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5599998841, 10s@0.58, 10s@0.56, 12s@0.6599999845, 12s@0.6510810778, 12s@0.62, 12s@0.629999937, 12s@0.6, 12s@0.6199999651, 22s@0.649999805, 25s@0.6999999735, 25s@0.7099999896 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.45, 31s@0.229999963, 33s@0.2299999517, 33s@0.2299999965, 33s@0.22, 42s@0.2, 45s@0.2, 45s@0.2, 45s@0.2, 48s@0.2, 54s@0.2079166667, 60s@0.22 ...

### 2026-11-01T09:00Z (market 6449793, result down)
Scored: p1 up filled at 78s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.45, 6s@0.4733984707, 6s@0.4699999962, 6s@0.47, 6s@0.469999998, 7s@0.4599999653, 7s@0.4899998428, 7s@0.4899999873, 7s@0.4899998383, 7s@0.4699999963, 9s@0.4899999873, 9s@0.4899998428 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.549999945, 3s@0.5499999064, 3s@0.5499999763, 3s@0.5499999763, 4s@0.5399999933, 4s@0.539999811, 6s@0.5399999918, 6s@0.5399999568, 6s@0.54, 7s@0.52, 7s@0.5199999792, 7s@0.5199999792 ...

### 2026-11-01T11:30Z (market 6455436, result down)
Scored: p1 up filled at 91s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5, 4s@0.5, 4s@0.5, 6s@0.5, 6s@0.5, 7s@0.5, 9s@0.5, 10s@0.5, 12s@0.5, 21s@0.4799998464, 25s@0.48, 40s@0.4799999616 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 16s@0.5154894661, 24s@0.53, 37s@0.53, 54s@0.5367885117, 54s@0.55, 54s@0.5299999607, 55s@0.559999776, 61s@0.563152354, 73s@0.6731034483, 73s@0.56, 75s@0.6499999309, 79s@0.63 ...

### 2026-11-01T12:00Z (market 6457180, result up)
Scored: p1 down filled at 15s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 1s@0.6299999953, 1s@0.51, 3s@0.6599999638, 3s@0.6599999445, 3s@0.65, 3s@0.6199999037, 3s@0.62, 3s@0.6099999322, 3s@0.6199999037, 3s@0.61, 3s@0.6, 3s@0.5799999964 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.5399999568, 15s@0.2399999952, 34s@0.23, 37s@0.23, 48s@0.2299999517, 48s@0.2299999965, 63s@0.2099999988, 63s@0.2099999966, 70s@0.19, 73s@0.1799999856, 84s@0.17, 90s@0.17 ...

### 2026-11-01T12:15Z (market 6457858, result down)
Scored: p1 up filled at 34s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5114753763, 4s@0.5148514831, 7s@0.51, 7s@0.4952542636, 9s@0.5199999792, 9s@0.52, 9s@0.5168992248, 9s@0.51, 10s@0.5199999792, 15s@0.5099999776, 21s@0.47, 22s@0.4599999867 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.4899998383, 6s@0.5199999792, 6s@0.52, 6s@0.52, 9s@0.4899999884, 10s@0.4924046581, 12s@0.5, 12s@0.5, 12s@0.4899999884, 18s@0.5, 21s@0.649999994, 21s@0.64 ...


_Updated 2026-11-01 15:01Z_
