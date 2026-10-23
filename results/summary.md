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
- Windows scored: 2101; excluded: 1 (trades_truncated: 1)
- Fill rate: 18.7% of scored windows had a fill (218 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 198/434 = 45.6%. The verdict uses strict.

## Spot-checked windows

### 2026-10-22T20:15Z (market 6025903, result down)
Scored: p1 up filled at 66s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.4799998464, 66s@0.2399999852, 75s@0.25, 75s@0.25, 162s@0.25, 185s@0.2, 200s@0.2, 216s@0.16, 218s@0.16, 219s@0.16, 224s@0.16, 227s@0.18 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.4974602312, 0s@0.51, 2s@0.51, 2s@0.51, 3s@0.5199998891, 3s@0.52, 3s@0.51, 3s@0.52, 5s@0.54, 5s@0.52, 6s@0.57, 6s@0.5699999886 ...

### 2026-10-22T21:15Z (market 6027000, result up)
Scored: p1 down filled at 93s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.6099999756, 5s@0.6, 23s@0.58, 23s@0.5599999686, 23s@0.57, 23s@0.56, 23s@0.5599999923, 23s@0.56, 26s@0.58, 26s@0.5799999882, 26s@0.5799999973, 26s@0.58 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 18s@0.45, 47s@0.46, 93s@0.21, 95s@0.2099999972, 98s@0.2, 98s@0.189999976, 99s@0.2, 99s@0.2, 104s@0.21, 107s@0.21, 113s@0.22, 134s@0.2 ...

### 2026-10-23T00:00Z (market 6031438, result down)
Scored: p1 up filled at 30s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 30s@0.219999978, 41s@0.1799999976, 47s@0.16, 48s@0.16, 48s@0.16, 48s@0.16, 48s@0.16, 48s@0.16, 51s@0.16, 54s@0.1499999993, 57s@0.1499999925, 60s@0.16 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.5415833333, 3s@0.56, 3s@0.559999776, 3s@0.56, 5s@0.6, 5s@0.58, 6s@0.6499999678, 6s@0.593877551, 8s@0.65, 11s@0.66, 11s@0.65, 12s@0.6899999933 ...


_Updated 2026-10-23 00:48Z_
