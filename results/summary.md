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
- Windows scored: 73; excluded: 0
- Fill rate: 20.5% of scored windows had a fill (0 too small)
- Fills that reached 45c: 7 of 15 = 46.7% (95% range 24.8% to 69.9%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-2.15 (balance $17.85 from $20)
- Longest losing streak: 2
- Strict vs touch: strict 7/15 = 46.7%; touch 8/16 = 50.0%. The verdict uses strict.

## Spot-checked windows

### 2026-10-01T14:00Z (market 5155375, result down)
Scored: p1 up filled at 71s, exit hit 1; p2 none. Profit p1 0.6.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.56, 5s@0.55, 6s@0.5599999642, 8s@0.5399999568, 8s@0.5399999568, 65s@0.25, 69s@0.25, 71s@0.2199999718, 72s@0.1944444444, 77s@0.21, 77s@0.2, 84s@0.21 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.4596153846, 3s@0.5077333225, 5s@0.4599998269, 11s@0.549999945, 12s@0.6, 12s@0.5699998812, 14s@0.6199999715, 14s@0.58, 14s@0.6, 15s@0.589999941, 15s@0.6099999748, 17s@0.5672977542 ...

### 2026-10-01T15:30Z (market 5156531, result down)
Scored: p1 up filled at 63s, exit hit 0; p2 none. Profit p1 -0.75.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 33s@0.25, 42s@0.25, 44s@0.25, 44s@0.25, 44s@0.25, 44s@0.25, 44s@0.25, 44s@0.25, 45s@0.25, 60s@0.25, 63s@0.22, 63s@0.22 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.55, 0s@0.53, 2s@0.56, 8s@0.65, 8s@0.61, 8s@0.6138613703, 9s@0.6764705743, 15s@0.64, 17s@0.64, 20s@0.69, 23s@0.7, 24s@0.71 ...

### 2026-10-01T15:45Z (market 5156620, result up)
Scored: p1 down filled at 99s, exit hit 0; p2 none. Profit p1 -0.75.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5799999312, 5s@0.59999988, 5s@0.59999988, 9s@0.6, 11s@0.629999995, 11s@0.63, 12s@0.64, 15s@0.64, 17s@0.6499999956, 18s@0.65, 20s@0.65, 26s@0.6119214493 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 99s@0.2, 107s@0.22, 110s@0.19, 117s@0.23, 119s@0.24, 171s@0.21, 174s@0.15, 174s@0.15, 176s@0.1617, 180s@0.14, 185s@0.1, 185s@0.09 ...


_Updated 2026-10-01 19:24Z_
