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
- Windows scored: 1209; excluded: 0
- Fill rate: 17.2% of scored windows had a fill (34 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 105/230 = 45.7%. The verdict uses strict.

## Spot-checked windows

### 2026-10-13T12:15Z (market 5604167, result up)
Scored: p1 up filled at 71s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.45, 7s@0.45, 8s@0.45, 20s@0.4599999387, 23s@0.48, 25s@0.5199999447, 25s@0.5, 31s@0.529999998, 38s@0.47, 40s@0.4911323329, 71s@0.25, 71s@0.24 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.5699999886, 4s@0.56, 4s@0.5599999642, 4s@0.56, 5s@0.570122, 5s@0.5699999618, 8s@0.5599999686, 10s@0.56, 10s@0.56, 10s@0.56, 11s@0.5699998494, 11s@0.5699998494 ...

### 2026-10-13T13:00Z (market 5604878, result down)
Scored: p1 up filled at 103s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 14s@0.5099999516, 23s@0.48, 95s@0.25, 98s@0.25, 103s@0.25, 103s@0.22, 103s@0.25, 104s@0.2346538332, 104s@0.21, 107s@0.2, 107s@0.2, 107s@0.2 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.46, 7s@0.48, 10s@0.5, 11s@0.49, 11s@0.5, 13s@0.5, 19s@0.5, 22s@0.53, 23s@0.52, 23s@0.52, 25s@0.6, 25s@0.6 ...

### 2026-10-13T16:00Z (market 5611022, result up)
Scored: p1 down filled at 75s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 13s@0.5799999976, 15s@0.58, 15s@0.5799999768, 15s@0.5799998822, 27s@0.59999997, 30s@0.6699999839, 30s@0.63, 30s@0.65, 30s@0.629999937, 30s@0.63, 33s@0.67, 37s@0.73 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 6s@0.4699999612, 7s@0.4895769076, 10s@0.47, 12s@0.4699999796, 45s@0.25, 48s@0.25, 49s@0.25, 75s@0.23, 76s@0.2399999923, 82s@0.2399999808, 84s@0.2399999923, 85s@0.23 ...

### 2026-10-13T17:00Z (market 5613375, result down)
Scored: p1 up filled at 63s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 61s@0.25, 63s@0.24, 64s@0.24, 66s@0.2399999993, 75s@0.2399999808, 87s@0.2, 97s@0.1899999989, 103s@0.19, 103s@0.19, 103s@0.19, 106s@0.2, 108s@0.2 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 1s@0.52, 3s@0.5899999458, 4s@0.62, 4s@0.5899999685, 9s@0.6518918359, 9s@0.669999965, 9s@0.67, 16s@0.6599999842, 27s@0.69, 27s@0.66, 27s@0.645, 27s@0.6899999901 ...


_Updated 2026-10-13 17:26Z_
