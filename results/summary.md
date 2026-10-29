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
- Windows scored: 2674; excluded: 2 (trades_truncated: 2)
- Fill rate: 19.2% of scored windows had a fill (340 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 264/571 = 46.2%. The verdict uses strict.

## Spot-checked windows

### 2026-10-28T20:00Z (market 6322959, result down)
Scored: p1 down filled at 68s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.5501754077, 4s@0.55, 4s@0.56, 5s@0.5899999725, 5s@0.6, 8s@0.6, 8s@0.6, 8s@0.598, 8s@0.59, 11s@0.6, 13s@0.599999976, 13s@0.5999999754 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.4599999387, 68s@0.2425, 70s@0.25, 74s@0.24, 80s@0.2, 80s@0.2, 82s@0.21, 82s@0.2, 83s@0.21543, 85s@0.25, 85s@0.23, 86s@0.25 ...

### 2026-10-28T20:30Z (market 6323762, result down)
Scored: p1 down filled at 113s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 1s@0.6, 1s@0.6, 1s@0.59, 1s@0.58, 1s@0.59, 1s@0.59, 5s@0.64, 5s@0.64, 11s@0.6, 11s@0.6, 16s@0.57, 20s@0.6 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 112s@0.25, 113s@0.22, 119s@0.2099999895, 125s@0.1799999856, 137s@0.12, 143s@0.12, 145s@0.13, 145s@0.1365141322, 146s@0.13, 149s@0.1399999923, 149s@0.1399999984, 157s@0.1299999948 ...

### 2026-10-28T21:45Z (market 6326113, result up)
Scored: p1 down filled at 47s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.5799999936, 2s@0.56, 5s@0.5699999214, 5s@0.5699999467, 5s@0.5699999467, 7s@0.59, 8s@0.6125896409, 13s@0.62, 13s@0.62, 14s@0.63, 16s@0.64, 17s@0.64 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 47s@0.24, 55s@0.25, 55s@0.25, 62s@0.2399999808, 70s@0.2399999952, 85s@0.2, 85s@0.2, 86s@0.2, 100s@0.18, 112s@0.1799999986, 115s@0.18, 124s@0.17 ...

### 2026-10-28T22:30Z (market 6326441, result up)
Scored: p1 down filled at 113s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.51, 10s@0.58, 10s@0.58, 11s@0.6, 13s@0.599999988, 19s@0.4899999953, 20s@0.4899999869, 20s@0.4899999584, 23s@0.4899999884, 23s@0.49, 25s@0.5, 26s@0.49 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.5, 17s@0.4801999827, 17s@0.46, 17s@0.46, 19s@0.49, 19s@0.4899998383, 19s@0.49, 20s@0.51, 29s@0.5099999949, 113s@0.17, 113s@0.17, 113s@0.17 ...

### 2026-10-28T23:00Z (market 6327000, result up)
Scored: p1 up filled at 40s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 40s@0.2099999895, 55s@0.1699999983, 58s@0.16, 62s@0.15, 67s@0.14, 68s@0.1493212663, 77s@0.15, 77s@0.1499999997, 79s@0.1499999925, 79s@0.1499999997, 82s@0.1499999997, 89s@0.15 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.5899999596, 4s@0.59, 4s@0.59, 4s@0.56, 4s@0.51, 5s@0.58, 5s@0.5899999878, 7s@0.6599999686, 7s@0.66, 7s@0.6299999953, 7s@0.6299998858, 7s@0.62 ...


_Updated 2026-10-29 01:46Z_
