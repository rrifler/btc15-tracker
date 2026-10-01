# BTC 15-min strategy tracker: NOT ENOUGH DATA

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

- No windows scored yet.

## Spot-checked windows

### 2026-09-23T20:30Z (market 4856302, result up)
Scored: p1 down filled at 67s, exit hit 0; p2 none. Profit p1 -1.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 8s@0.62, 10s@0.6299998362, 14s@0.63, 16s@0.629999995, 22s@0.6299999753, 29s@0.64, 38s@0.7199999697, 38s@0.7099999606, 40s@0.719999856, 40s@0.72, 40s@0.7199999927, 41s@0.73 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 52s@0.25, 67s@0.2, 68s@0.19, 68s@0.2, 73s@0.19, 73s@0.2, 73s@0.2, 73s@0.2, 74s@0.2, 74s@0.2, 74s@0.2, 74s@0.2 ...

### 2026-09-23T22:30Z (market 4867369, result up)
Scored: p1 up filled at 35s, exit hit 1; p2 none. Profit p1 0.6.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 31s@0.25, 35s@0.25, 35s@0.23, 35s@0.25, 35s@0.25, 35s@0.25, 35s@0.25, 35s@0.25, 35s@0.25, 35s@0.25, 35s@0.24, 37s@0.23 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 1s@0.55, 5s@0.61, 5s@0.58375, 5s@0.58, 7s@0.64, 7s@0.6099999488, 7s@0.59, 10s@0.64, 10s@0.65, 10s@0.64, 11s@0.66, 26s@0.719999856 ...

### 2026-09-23T22:45Z (market 4867723, result up)
Scored: p1 down filled at 71s, exit hit 0; p2 none. Profit p1 -0.75.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 11s@0.46, 13s@0.4599997976, 13s@0.459999988, 14s@0.46, 16s@0.47, 16s@0.469999906, 35s@0.5, 37s@0.526250457, 37s@0.52, 37s@0.5, 37s@0.5, 38s@0.59 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.48, 2s@0.479999998, 8s@0.549999945, 10s@0.5499999979, 13s@0.549999945, 17s@0.51, 17s@0.5099999985, 37s@0.49, 38s@0.46, 68s@0.25, 71s@0.2200947453, 74s@0.23 ...

### 2026-09-23T23:00Z (market 4867902, result down)
Scored: p1 up filled at 85s, exit hit 1; p2 none. Profit p1 0.6.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 1s@0.49, 4s@0.48, 79s@0.25, 79s@0.25, 85s@0.23, 85s@0.2299999693, 86s@0.23, 97s@0.2081727051, 98s@0.24, 98s@0.24, 103s@0.24, 127s@0.2 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.59, 11s@0.58, 19s@0.5899999705, 26s@0.59, 32s@0.5899999725, 34s@0.6099999488, 35s@0.61, 35s@0.5977899878, 41s@0.659999978, 41s@0.65, 41s@0.64, 41s@0.63 ...

### 2026-09-24T00:00Z (market 4869386, result down)
Scored: p1 down filled at 55s, exit hit 1; p2 none. Profit p1 0.6.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.5199999792, 4s@0.52, 4s@0.5199999792, 4s@0.5199999792, 5s@0.5099998215, 8s@0.5099998215, 10s@0.51, 11s@0.5, 11s@0.51, 11s@0.5099998215, 13s@0.5, 14s@0.51 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.49, 4s@0.49, 7s@0.5, 7s@0.4996755354, 11s@0.5, 11s@0.5, 16s@0.5, 55s@0.2399999923, 55s@0.24, 56s@0.2399999808, 58s@0.2399999923, 58s@0.2399999808 ...


_Updated 2026-10-01 01:04Z_
