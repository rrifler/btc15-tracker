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
- Windows scored: 57; excluded: 0
- Fill rate: 22.8% of scored windows had a fill (0 too small)
- Fills that reached 45c: 7 of 13 = 53.8% (95% range 29.1% to 76.8%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-0.65 (balance $19.35 from $20)
- Longest losing streak: 2
- Strict vs touch: strict 7/13 = 53.8%; touch 7/13 = 53.8%. The verdict uses strict.

## Spot-checked windows

### 2026-10-01T10:00Z (market 5152164, result down)
Scored: p1 up filled at 68s, exit hit 0; p2 none. Profit p1 -0.75.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.5685421931, 5s@0.606, 5s@0.5, 6s@0.5599999569, 17s@0.48, 68s@0.25, 68s@0.24, 77s@0.25, 78s@0.25, 78s@0.25, 83s@0.24, 84s@0.25 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 6s@0.45, 6s@0.45, 6s@0.45, 6s@0.45, 6s@0.45, 6s@0.45, 8s@0.522, 8s@0.45, 8s@0.45, 11s@0.53, 12s@0.5299999025, 17s@0.52 ...

### 2026-10-01T10:15Z (market 5152251, result down)
Scored: p1 up filled at 107s, exit hit 1; p2 none. Profit p1 0.6.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.5099998215, 5s@0.5099999984, 8s@0.51, 90s@0.25, 90s@0.25, 90s@0.25, 107s@0.2099999895, 107s@0.2099999895, 111s@0.2099999895, 120s@0.2, 125s@0.2, 134s@0.15 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.5, 8s@0.5799999768, 8s@0.5499999198, 9s@0.5899999839, 9s@0.5899997404, 11s@0.5899998254, 14s@0.59, 21s@0.57, 21s@0.5699999673, 21s@0.5699998943, 21s@0.56, 23s@0.64 ...

### 2026-10-01T10:30Z (market 5152299, result up)
Scored: p1 down filled at 107s, exit hit 0; p2 none. Profit p1 -0.75.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 9s@0.5863803393, 14s@0.56, 18s@0.5699999886, 21s@0.559999776, 23s@0.56, 23s@0.56, 26s@0.599999904, 26s@0.5999998868, 26s@0.5999999951, 26s@0.59, 26s@0.59, 38s@0.6099999968 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.4799998464, 8s@0.47, 95s@0.25, 95s@0.25, 96s@0.25, 107s@0.22, 110s@0.23, 111s@0.25, 114s@0.23, 120s@0.2161881188, 120s@0.2399999808, 123s@0.219999978 ...

### 2026-10-01T11:00Z (market 5153157, result down)
Scored: p1 up filled at 92s, exit hit 0; p2 none. Profit p1 -0.75.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.5099998215, 6s@0.48, 8s@0.45, 92s@0.24, 98s@0.19, 101s@0.19, 105s@0.1799999856, 105s@0.17, 111s@0.15, 111s@0.1531565657, 116s@0.17, 116s@0.16 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5, 3s@0.5, 3s@0.5, 3s@0.5, 3s@0.5, 3s@0.5, 3s@0.49, 5s@0.53, 5s@0.53, 5s@0.5, 5s@0.5, 5s@0.5 ...

### 2026-10-01T11:30Z (market 5153322, result up)
Scored: p1 down filled at 78s, exit hit 1; p2 none. Profit p1 0.6.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 6s@0.6055592316, 9s@0.5899999712, 15s@0.61, 15s@0.6, 24s@0.5899999848, 26s@0.59, 27s@0.59, 33s@0.6001612368, 35s@0.61, 39s@0.63, 41s@0.65, 44s@0.67 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 78s@0.25, 78s@0.24, 114s@0.45, 116s@0.46, 116s@0.46, 117s@0.46, 117s@0.4599998822, 125s@0.46, 125s@0.4599999992, 126s@0.5, 128s@0.53, 128s@0.51 ...


_Updated 2026-10-01 15:26Z_
