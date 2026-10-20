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
- Windows scored: 1820; excluded: 1 (trades_truncated: 1)
- Fill rate: 18.5% of scored windows had a fill (162 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 166/372 = 44.6%. The verdict uses strict.

## Spot-checked windows

### 2026-10-19T21:15Z (market 5907414, result down)
Scored: p1 down filled at 12s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.58, 3s@0.68, 3s@0.644172, 3s@0.65, 3s@0.64, 3s@0.64, 3s@0.64, 3s@0.64, 4s@0.73, 4s@0.72, 4s@0.73, 4s@0.72 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 12s@0.2225, 12s@0.21, 12s@0.22, 12s@0.2299999993, 12s@0.22, 12s@0.23, 12s@0.2299999988, 13s@0.24, 13s@0.23, 13s@0.25, 13s@0.25, 13s@0.24 ...

### 2026-10-19T22:00Z (market 5908821, result up)
Scored: p1 down filled at 21s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.56, 0s@0.55, 3s@0.5899999145, 3s@0.6, 3s@0.6, 3s@0.58, 3s@0.58, 3s@0.58, 4s@0.62, 4s@0.6299999685, 6s@0.64, 13s@0.64 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 21s@0.2299999517, 24s@0.2299999993, 25s@0.2299999989, 30s@0.23, 30s@0.23, 31s@0.23, 49s@0.25, 49s@0.25, 49s@0.2453695494, 51s@0.25, 52s@0.229999987, 52s@0.2299999782 ...

### 2026-10-19T22:15Z (market 5909001, result down)
Scored: p1 down filled at 98s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.48, 3s@0.48, 3s@0.47, 3s@0.46, 5s@0.4899999824, 5s@0.469999998, 11s@0.46, 12s@0.4918800526, 12s@0.49, 12s@0.4899999876, 14s@0.53, 14s@0.53 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.56, 5s@0.54, 5s@0.52, 6s@0.559999776, 8s@0.549999994, 14s@0.48, 18s@0.4799999846, 98s@0.22, 98s@0.24, 99s@0.2399999998, 137s@0.25, 212s@0.22 ...

### 2026-10-20T00:00Z (market 5910894, result down)
Scored: p1 down filled at 18s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.56951, 5s@0.5699999603, 5s@0.56, 6s@0.55, 6s@0.549999945, 6s@0.5499998959, 6s@0.549999945, 8s@0.5499999807, 11s@0.55, 12s@0.55, 12s@0.55, 12s@0.55 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 9s@0.4599999879, 9s@0.459999988, 18s@0.24, 18s@0.24, 18s@0.24, 18s@0.23, 18s@0.22, 18s@0.2217857143, 18s@0.2293793845, 38s@0.45, 39s@0.46, 39s@0.46 ...

### 2026-10-20T00:15Z (market 5911186, result down)
Scored: p1 up filled at 113s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.55, 3s@0.5499999505, 3s@0.549999945, 5s@0.549999945, 5s@0.55, 5s@0.5499998396, 6s@0.5499999807, 6s@0.55, 6s@0.55, 6s@0.55, 6s@0.55, 6s@0.55 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.45, 2s@0.45, 3s@0.4599999687, 3s@0.45, 3s@0.45, 20s@0.47, 20s@0.47, 20s@0.47, 20s@0.47, 20s@0.4699999962, 20s@0.47, 20s@0.46 ...


_Updated 2026-10-20 02:34Z_
