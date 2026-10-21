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
- Windows scored: 2000; excluded: 1 (trades_truncated: 1)
- Fill rate: 18.8% of scored windows had a fill (201 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 190/414 = 45.9%. The verdict uses strict.

## Spot-checked windows

### 2026-10-21T19:00Z (market 5990329, result down)
Scored: p1 up filled at 116s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 8s@0.5699999556, 8s@0.5699999886, 9s@0.5099999516, 9s@0.5, 11s@0.5, 11s@0.5, 11s@0.5, 11s@0.5, 11s@0.5, 11s@0.5, 11s@0.5, 11s@0.5 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.4599999707, 9s@0.5, 9s@0.5, 9s@0.4762130178, 9s@0.5, 9s@0.46, 9s@0.47, 9s@0.5, 9s@0.49, 9s@0.47, 9s@0.45, 9s@0.47 ...

### 2026-10-21T19:15Z (market 5990375, result up)
Scored: p1 down filled at 95s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.5899999705, 3s@0.5799999768, 5s@0.59, 6s@0.58, 9s@0.5799999768, 9s@0.5799999768, 14s@0.58, 14s@0.5799999882, 14s@0.5799999882, 14s@0.5799999882, 14s@0.5799999882, 15s@0.58 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 95s@0.2199999975, 95s@0.22, 95s@0.24, 101s@0.19, 104s@0.19, 104s@0.2, 104s@0.18, 108s@0.2, 110s@0.2, 113s@0.19, 116s@0.17, 119s@0.16 ...

### 2026-10-21T19:30Z (market 5990618, result up)
Scored: p1 down filled at 53s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.6666322581, 3s@0.6499999106, 5s@0.65, 5s@0.65, 6s@0.649999805, 18s@0.6347484775, 20s@0.64, 23s@0.64, 26s@0.66, 26s@0.6699996918, 26s@0.68, 27s@0.66 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 53s@0.24, 54s@0.24, 56s@0.25, 57s@0.24, 74s@0.24, 93s@0.22, 101s@0.2099999895, 101s@0.2171428571, 102s@0.23, 107s@0.2199999998, 129s@0.24, 159s@0.1827356667 ...

### 2026-10-21T22:00Z (market 5994392, result down)
Scored: p1 up filled at 62s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.5299999868, 5s@0.5299999868, 8s@0.5299999868, 51s@0.25, 60s@0.25, 62s@0.2483608186, 63s@0.18, 66s@0.18, 66s@0.18, 66s@0.18, 66s@0.1899999998, 66s@0.18 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.47, 5s@0.47, 5s@0.47, 5s@0.4870362069, 5s@0.48, 5s@0.4799998464, 5s@0.4799999803, 6s@0.47, 6s@0.469999906, 6s@0.47, 6s@0.47, 6s@0.47 ...


_Updated 2026-10-21 23:35Z_
