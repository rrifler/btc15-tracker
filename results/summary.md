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
- Windows scored: 1413; excluded: 0
- Fill rate: 17.5% of scored windows had a fill (73 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 127/275 = 46.2%. The verdict uses strict.

## Spot-checked windows

### 2026-10-15T14:30Z (market 5688332, result up)
Scored: p1 up filled at 109s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 71s@0.25, 73s@0.25, 74s@0.25, 109s@0.2399999808, 143s@0.25, 148s@0.24, 152s@0.24, 154s@0.24, 233s@0.45, 245s@0.5, 245s@0.49, 247s@0.52 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 1s@0.56, 4s@0.5799999755, 7s@0.59999988, 8s@0.6, 8s@0.599999952, 13s@0.64, 22s@0.66, 22s@0.65, 22s@0.68, 26s@0.699999965, 28s@0.699999993, 29s@0.6999999977 ...

### 2026-10-15T16:45Z (market 5692114, result up)
Scored: p1 down filled at 16s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 1s@0.6, 1s@0.59, 1s@0.58, 2s@0.6324110672, 2s@0.61, 5s@0.72, 5s@0.69, 5s@0.6899999109, 8s@0.7, 11s@0.769999975, 11s@0.7699999664, 11s@0.7699999645 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 16s@0.2399999808, 17s@0.2399999923, 17s@0.2399999923, 19s@0.24, 25s@0.2, 25s@0.19, 26s@0.2, 28s@0.1899999962, 28s@0.1899999962, 29s@0.2, 29s@0.19, 32s@0.19 ...

### 2026-10-15T17:15Z (market 5693657, result up)
Scored: p1 down filled at 74s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.5, 2s@0.5, 2s@0.5, 2s@0.5, 4s@0.5175119596, 4s@0.51, 5s@0.6, 5s@0.52, 5s@0.52, 7s@0.5916666667, 8s@0.5904761905, 8s@0.57 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.5, 4s@0.49, 4s@0.5, 59s@0.25, 74s@0.22, 74s@0.219999978, 76s@0.219999999, 86s@0.1699999983, 86s@0.1799999856, 91s@0.16, 92s@0.139999993, 92s@0.13 ...

### 2026-10-15T19:30Z (market 5699967, result down)
Scored: p1 up filled at 35s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 35s@0.2, 35s@0.2099999983, 37s@0.2, 37s@0.2, 38s@0.21, 53s@0.21, 53s@0.21, 53s@0.21, 64s@0.22, 73s@0.24, 73s@0.22, 73s@0.23 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.66, 4s@0.65, 4s@0.6599999954, 4s@0.6499999951, 4s@0.65, 5s@0.69, 7s@0.72, 8s@0.75, 8s@0.75, 8s@0.74, 8s@0.75, 10s@0.75 ...


_Updated 2026-10-15 20:34Z_
