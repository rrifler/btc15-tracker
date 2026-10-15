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
- Windows scored: 1338; excluded: 0
- Fill rate: 17.5% of scored windows had a fill (60 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 121/260 = 46.5%. The verdict uses strict.

## Spot-checked windows

### 2026-10-14T20:00Z (market 5672473, result up)
Scored: p1 down filled at 43s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.5599999939, 0s@0.56, 0s@0.56, 1s@0.58, 1s@0.57, 6s@0.6199999651, 6s@0.6499999814, 6s@0.62, 6s@0.62, 6s@0.64, 7s@0.6, 7s@0.5999999806 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 43s@0.2399999984, 49s@0.21, 52s@0.2, 55s@0.18, 60s@0.17, 63s@0.17, 63s@0.1799999856, 63s@0.1853866531, 64s@0.19, 66s@0.1899999962, 66s@0.2099999695, 70s@0.2 ...

### 2026-10-14T20:30Z (market 5672947, result down)
Scored: p1 up filled at 85s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 18s@0.45, 18s@0.49, 18s@0.49, 18s@0.49, 18s@0.49, 19s@0.52, 19s@0.49, 28s@0.5199999843, 28s@0.52, 49s@0.45, 85s@0.2299999914, 87s@0.22 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.54, 22s@0.4799999721, 22s@0.48, 24s@0.48, 34s@0.549999945, 39s@0.6, 39s@0.61, 39s@0.6, 39s@0.6071561672, 39s@0.6, 39s@0.6, 39s@0.6 ...

### 2026-10-14T20:45Z (market 5673481, result up)
Scored: p1 up filled at 37s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 37s@0.2471698113, 37s@0.25, 37s@0.25, 37s@0.25, 37s@0.25, 37s@0.25, 37s@0.23, 39s@0.46, 40s@0.51, 40s@0.48, 40s@0.4899999992, 40s@0.48 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 16s@0.5999999902, 16s@0.5929634584, 16s@0.5899999762, 16s@0.59, 16s@0.59, 16s@0.58324, 18s@0.6, 24s@0.6, 25s@0.6, 27s@0.67, 27s@0.6699999975, 27s@0.6699999957 ...

### 2026-10-14T21:45Z (market 5673877, result down)
Scored: p1 down filled at 34s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 6s@0.6, 6s@0.6, 6s@0.6, 9s@0.6, 13s@0.5799999768, 18s@0.5799999768, 19s@0.57, 22s@0.62, 22s@0.619999991, 22s@0.6199999865, 22s@0.6199998327, 22s@0.6199999853 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 34s@0.2399999977, 34s@0.24, 63s@0.23, 67s@0.2399999923, 69s@0.2099999923, 75s@0.2, 76s@0.21, 90s@0.21, 94s@0.2099999989, 96s@0.2099999895, 103s@0.1799999999, 106s@0.1799999856 ...

### 2026-10-14T23:30Z (market 5674735, result up)
Scored: p1 up filled at 66s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 66s@0.2399999923, 66s@0.24, 73s@0.25, 73s@0.25, 73s@0.24, 145s@0.45, 147s@0.47, 147s@0.469999998, 148s@0.4799999687, 148s@0.4702040509, 295s@0.45, 295s@0.46 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 6s@0.59, 7s@0.6, 7s@0.5999999803, 7s@0.5899999725, 9s@0.6150399717, 10s@0.66, 10s@0.66, 12s@0.6599999448, 16s@0.6899999685, 16s@0.6599999448, 16s@0.66, 18s@0.7 ...


_Updated 2026-10-15 01:35Z_
