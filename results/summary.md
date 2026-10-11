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
- Windows scored: 981; excluded: 0
- Fill rate: 16.3% of scored windows had a fill (0 too small)
- Fills that reached 45c: 73 of 160 = 45.6% (95% range 38.1% to 53.4%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-13.55 (balance $6.45 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 73/160 = 45.6%; touch 81/174 = 46.6%. The verdict uses strict.

## Spot-checked windows

### 2026-10-11T02:45Z (market 5478929, result down)
Scored: p1 up filled at 87s, exit hit 0; p2 none. Profit p1 -0.25.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 83s@0.25, 83s@0.25, 87s@0.2399999981, 87s@0.25, 87s@0.24, 87s@0.24, 93s@0.24, 93s@0.24, 93s@0.24, 98s@0.25, 98s@0.25, 107s@0.1899999962 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.6474308273, 3s@0.649999805, 6s@0.659999985, 6s@0.6599999967, 6s@0.65, 9s@0.67, 12s@0.6799999767, 12s@0.6799998912, 15s@0.7, 15s@0.7, 17s@0.699999995, 32s@0.6937561928 ...

### 2026-10-11T04:30Z (market 5480330, result up)
Scored: p1 down filled at 101s, exit hit 0; p2 none. Profit p1 -0.25.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 8s@0.5, 12s@0.5099999542, 17s@0.5099999776, 20s@0.51, 20s@0.5099999761, 23s@0.51, 32s@0.5099998215, 32s@0.5099998215, 35s@0.51, 35s@0.51, 39s@0.5099999949, 39s@0.5099998215 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5, 6s@0.5, 6s@0.5, 20s@0.5, 26s@0.5, 27s@0.5, 39s@0.5, 42s@0.5175, 50s@0.53, 50s@0.53, 54s@0.52, 60s@0.5 ...

### 2026-10-11T06:45Z (market 5482405, result up)
Scored: p1 down filled at 95s, exit hit 1; p2 none. Profit p1 0.2.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.49, 3s@0.5, 3s@0.4799999687, 3s@0.4799999962, 3s@0.48, 3s@0.48, 3s@0.4607318501, 3s@0.457436, 3s@0.4599999968, 3s@0.45, 3s@0.45, 6s@0.5199999843 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.53, 3s@0.4899998383, 3s@0.5299998463, 3s@0.5299998463, 5s@0.49, 5s@0.49, 5s@0.49, 6s@0.4899999824, 6s@0.49, 6s@0.49, 6s@0.489999992, 6s@0.49 ...

### 2026-10-11T08:00Z (market 5483626, result up)
Scored: p1 down filled at 57s, exit hit 0; p2 none. Profit p1 -0.25.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.57, 4s@0.578, 4s@0.57, 4s@0.57, 13s@0.6, 13s@0.6, 15s@0.64, 15s@0.64, 15s@0.64, 15s@0.64, 15s@0.64, 16s@0.65 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 57s@0.23, 57s@0.23, 57s@0.23, 58s@0.2299999914, 61s@0.225, 63s@0.219999978, 66s@0.2299999914, 66s@0.22, 87s@0.235, 174s@0.25, 180s@0.25, 447s@0.22 ...


_Updated 2026-10-11 08:25Z_
