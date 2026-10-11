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
- Windows scored: 973; excluded: 0
- Fill rate: 16.2% of scored windows had a fill (0 too small)
- Fills that reached 45c: 72 of 158 = 45.6% (95% range 38.0% to 53.3%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-13.50 (balance $6.50 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 72/158 = 45.6%; touch 80/172 = 46.5%. The verdict uses strict.

## Spot-checked windows

### 2026-10-11T01:15Z (market 5478074, result up)
Scored: p1 down filled at 86s, exit hit 0; p2 none. Profit p1 -0.25.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.5846153846, 0s@0.6, 2s@0.61, 2s@0.6, 3s@0.6, 12s@0.62, 12s@0.61, 14s@0.6599999133, 14s@0.6499998933, 14s@0.6255555556, 14s@0.62, 20s@0.6486895145 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 86s@0.2299999517, 102s@0.229999997, 105s@0.23, 105s@0.23, 107s@0.23, 107s@0.23, 146s@0.229999987, 149s@0.229999994, 150s@0.2299999991, 165s@0.23, 180s@0.2299999958, 185s@0.2299999517 ...

### 2026-10-11T02:45Z (market 5478929, result down)
Scored: p1 up filled at 87s, exit hit 0; p2 none. Profit p1 -0.25.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 83s@0.25, 83s@0.25, 87s@0.2399999981, 87s@0.25, 87s@0.24, 87s@0.24, 93s@0.24, 93s@0.24, 93s@0.24, 98s@0.25, 98s@0.25, 107s@0.1899999962 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.6474308273, 3s@0.649999805, 6s@0.659999985, 6s@0.6599999967, 6s@0.65, 9s@0.67, 12s@0.6799999767, 12s@0.6799998912, 15s@0.7, 15s@0.7, 17s@0.699999995, 32s@0.6937561928 ...

### 2026-10-11T04:30Z (market 5480330, result up)
Scored: p1 down filled at 101s, exit hit 0; p2 none. Profit p1 -0.25.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 8s@0.5, 12s@0.5099999542, 17s@0.5099999776, 20s@0.51, 20s@0.5099999761, 23s@0.51, 32s@0.5099998215, 32s@0.5099998215, 35s@0.51, 35s@0.51, 39s@0.5099999949, 39s@0.5099998215 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5, 6s@0.5, 6s@0.5, 20s@0.5, 26s@0.5, 27s@0.5, 39s@0.5, 42s@0.5175, 50s@0.53, 50s@0.53, 54s@0.52, 60s@0.5 ...


_Updated 2026-10-11 06:29Z_
