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

- Verdict: **NOT ENOUGH DATA**
- Windows scored: 401; excluded: 0
- Fill rate: 17.2% of scored windows had a fill (0 too small)
- Fills that reached 45c: 33 of 69 = 47.8% (95% range 36.5% to 59.4%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-6.95 (balance $13.05 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 33/69 = 47.8%; touch 37/74 = 50.0%. The verdict uses strict.

## Spot-checked windows

### 2026-10-05T01:00Z (market 5262755, result down)
Scored: p1 up filled at 94s, exit hit 1; p2 none. Profit p1 0.4.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 94s@0.2099999983, 94s@0.2199999974, 97s@0.17, 98s@0.16, 98s@0.1623342174, 106s@0.16, 109s@0.17, 118s@0.1945945946, 119s@0.2099999895, 133s@0.1799999948, 146s@0.18, 146s@0.17 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.5699999886, 5s@0.6099998597, 5s@0.6099998597, 5s@0.61, 5s@0.57, 5s@0.609999986, 7s@0.62, 7s@0.64, 7s@0.64, 7s@0.63, 7s@0.6299998362, 7s@0.61 ...

### 2026-10-05T01:30Z (market 5262876, result down)
Scored: p1 up filled at 32s, exit hit 0; p2 none. Profit p1 -0.5.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 29s@0.25, 32s@0.2, 37s@0.2, 37s@0.2, 37s@0.2, 37s@0.2, 38s@0.22, 38s@0.21, 38s@0.2199999966, 38s@0.21, 38s@0.19, 40s@0.22 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.59999988, 4s@0.61, 4s@0.61, 4s@0.6, 4s@0.6099998597, 4s@0.6099999913, 5s@0.6099998597, 5s@0.6099998597, 5s@0.609999986, 5s@0.605, 7s@0.64, 7s@0.64 ...

### 2026-10-05T02:30Z (market 5263283, result up)
Scored: p1 up filled at 104s, exit hit 1; p2 none. Profit p1 0.4.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 104s@0.2399999852, 109s@0.23, 110s@0.23, 110s@0.23, 113s@0.21, 116s@0.21, 124s@0.1899999928, 125s@0.2, 127s@0.22, 127s@0.19, 137s@0.2312426068, 137s@0.23 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 1s@0.56, 4s@0.59, 5s@0.5799999203, 7s@0.58, 10s@0.5799999848, 22s@0.58, 22s@0.58, 26s@0.5899999894, 28s@0.6099998597, 28s@0.6, 28s@0.6, 32s@0.5799999768 ...

### 2026-10-05T06:00Z (market 5269338, result up)
Scored: p1 down filled at 100s, exit hit 0; p2 none. Profit p1 -0.5.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.5, 7s@0.53, 7s@0.51, 8s@0.55, 14s@0.5, 14s@0.5499999966, 16s@0.5, 16s@0.5299998463, 25s@0.54, 26s@0.58, 28s@0.5199999451, 28s@0.52 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.5, 7s@0.49, 14s@0.46, 16s@0.49, 17s@0.5, 23s@0.47, 26s@0.48, 29s@0.4899999824, 38s@0.48, 100s@0.21, 100s@0.21, 104s@0.19 ...

### 2026-10-05T06:45Z (market 5269696, result up)
Scored: p1 down filled at 103s, exit hit 0; p2 none. Profit p1 -0.5.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 8s@0.49, 10s@0.5, 10s@0.49, 61s@0.5499999738, 61s@0.54, 61s@0.52, 61s@0.51, 67s@0.55, 67s@0.55, 70s@0.5899999895, 70s@0.59, 71s@0.61 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.5199999792, 11s@0.5099999863, 26s@0.5099999516, 35s@0.51, 37s@0.5099999776, 43s@0.5099998215, 64s@0.46, 89s@0.45, 89s@0.45, 89s@0.4599999197, 94s@0.45, 103s@0.23 ...


_Updated 2026-10-05 07:27Z_
