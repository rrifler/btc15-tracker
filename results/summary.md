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
- Windows scored: 2568; excluded: 2 (trades_truncated: 2)
- Fill rate: 19.1% of scored windows had a fill (316 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 255/546 = 46.7%. The verdict uses strict.

## Spot-checked windows

### 2026-10-27T15:15Z (market 6254768, result up)
Scored: p1 down filled at 119s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 12s@0.49, 12s@0.4899999824, 24s@0.5, 26s@0.5, 41s@0.4799998464, 45s@0.4699999944, 48s@0.46, 50s@0.47, 71s@0.509999914, 83s@0.5399999955, 83s@0.53, 83s@0.52 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5, 3s@0.5, 5s@0.5, 11s@0.5, 17s@0.5099998215, 24s@0.5099999516, 29s@0.51, 38s@0.5299999868, 53s@0.5399999568, 71s@0.5, 74s@0.5, 74s@0.5 ...

### 2026-10-27T17:00Z (market 6257163, result down)
Scored: p1 up filled at 117s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 20s@0.45, 21s@0.45, 21s@0.45, 24s@0.46, 24s@0.4599999115, 26s@0.4737292213, 35s@0.4799998464, 35s@0.4799999683, 36s@0.46, 117s@0.2299999982, 125s@0.24875, 128s@0.2399999992 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5099999718, 5s@0.52, 5s@0.5199999567, 6s@0.5199999942, 8s@0.5199999927, 8s@0.52, 9s@0.52, 9s@0.5199999802, 9s@0.5199999941, 9s@0.52, 11s@0.55, 11s@0.53 ...

### 2026-10-27T18:00Z (market 6258896, result up)
Scored: p1 up filled at 87s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 8s@0.4540858059, 11s@0.4699999896, 12s@0.47, 14s@0.5, 20s@0.5424299773, 20s@0.54, 21s@0.5499999928, 21s@0.55, 23s@0.55, 30s@0.48, 66s@0.25, 87s@0.2399999808 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.56, 2s@0.54, 6s@0.59, 6s@0.6, 8s@0.57, 8s@0.54, 9s@0.54, 12s@0.53, 15s@0.5, 17s@0.49, 27s@0.45, 29s@0.52 ...

### 2026-10-27T19:00Z (market 6261685, result up)
Scored: p1 down filled at 44s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 6s@0.4799999694, 8s@0.4799999679, 12s@0.48, 14s@0.4799999694, 21s@0.51, 21s@0.4869928175, 24s@0.5399999992, 26s@0.54, 27s@0.6299999909, 27s@0.64, 29s@0.64, 30s@0.64 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.53, 6s@0.53, 6s@0.53, 11s@0.5299998463, 11s@0.5299998463, 17s@0.5299999587, 21s@0.4599999669, 23s@0.469999906, 44s@0.2399999808, 44s@0.25, 60s@0.2099999895, 95s@0.2299999979 ...


_Updated 2026-10-27 21:39Z_
