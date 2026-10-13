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
- Windows scored: 1225; excluded: 0
- Fill rate: 17.1% of scored windows had a fill (36 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 105/233 = 45.1%. The verdict uses strict.

## Spot-checked windows

### 2026-10-13T16:00Z (market 5611022, result up)
Scored: p1 down filled at 75s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 13s@0.5799999976, 15s@0.58, 15s@0.5799999768, 15s@0.5799998822, 27s@0.59999997, 30s@0.6699999839, 30s@0.63, 30s@0.65, 30s@0.629999937, 30s@0.63, 33s@0.67, 37s@0.73 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 6s@0.4699999612, 7s@0.4895769076, 10s@0.47, 12s@0.4699999796, 45s@0.25, 48s@0.25, 49s@0.25, 75s@0.23, 76s@0.2399999923, 82s@0.2399999808, 84s@0.2399999923, 85s@0.23 ...

### 2026-10-13T17:00Z (market 5613375, result down)
Scored: p1 up filled at 63s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 61s@0.25, 63s@0.24, 64s@0.24, 66s@0.2399999993, 75s@0.2399999808, 87s@0.2, 97s@0.1899999989, 103s@0.19, 103s@0.19, 103s@0.19, 106s@0.2, 108s@0.2 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 1s@0.52, 3s@0.5899999458, 4s@0.62, 4s@0.5899999685, 9s@0.6518918359, 9s@0.669999965, 9s@0.67, 16s@0.6599999842, 27s@0.69, 27s@0.66, 27s@0.645, 27s@0.6899999901 ...

### 2026-10-13T17:15Z (market 5613952, result up)
Scored: p1 down filled at 60s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.5699999886, 6s@0.5699999886, 7s@0.5699999914, 10s@0.549999956, 18s@0.53, 19s@0.54, 22s@0.54, 24s@0.56, 27s@0.63, 27s@0.63, 28s@0.6899999586, 28s@0.66 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 10s@0.47, 10s@0.47, 10s@0.47, 10s@0.47, 10s@0.47, 10s@0.47, 10s@0.46, 10s@0.47, 10s@0.47, 10s@0.45, 10s@0.45, 10s@0.45 ...

### 2026-10-13T20:45Z (market 5635500, result up)
Scored: p1 down filled at 102s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.6, 3s@0.59, 4s@0.5999999213, 19s@0.6, 19s@0.6, 19s@0.59999988, 21s@0.6, 22s@0.6327041242, 22s@0.669999965, 22s@0.66, 22s@0.6, 24s@0.6585414464 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 102s@0.23, 102s@0.22, 102s@0.2299999901, 112s@0.2399999923, 112s@0.2399999981, 169s@0.21, 169s@0.2199999978, 175s@0.22, 190s@0.22, 190s@0.24, 190s@0.22, 190s@0.22 ...


_Updated 2026-10-13 21:33Z_
