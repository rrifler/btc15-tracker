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
- Windows scored: 1832; excluded: 2 (trades_truncated: 1, result_missing: 1)
- Fill rate: 18.4% of scored windows had a fill (164 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 167/374 = 44.7%. The verdict uses strict.

## Spot-checked windows

### 2026-10-20T00:00Z (market 5910894, result down)
Scored: p1 down filled at 18s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.56951, 5s@0.5699999603, 5s@0.56, 6s@0.55, 6s@0.549999945, 6s@0.5499998959, 6s@0.549999945, 8s@0.5499999807, 11s@0.55, 12s@0.55, 12s@0.55, 12s@0.55 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 9s@0.4599999879, 9s@0.459999988, 18s@0.24, 18s@0.24, 18s@0.24, 18s@0.23, 18s@0.22, 18s@0.2217857143, 18s@0.2293793845, 38s@0.45, 39s@0.46, 39s@0.46 ...

### 2026-10-20T00:15Z (market 5911186, result down)
Scored: p1 up filled at 113s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.55, 3s@0.5499999505, 3s@0.549999945, 5s@0.549999945, 5s@0.55, 5s@0.5499998396, 6s@0.5499999807, 6s@0.55, 6s@0.55, 6s@0.55, 6s@0.55, 6s@0.55 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.45, 2s@0.45, 3s@0.4599999687, 3s@0.45, 3s@0.45, 20s@0.47, 20s@0.47, 20s@0.47, 20s@0.47, 20s@0.4699999962, 20s@0.47, 20s@0.46 ...

### 2026-10-20T01:45Z (market 5911975, result up)
Scored: p1 down filled at 114s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.51, 3s@0.5399999568, 6s@0.49, 21s@0.4536363636, 26s@0.459999988, 33s@0.45, 35s@0.45, 35s@0.45, 38s@0.48, 38s@0.4799999694, 39s@0.4899999862, 39s@0.49 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.469999998, 3s@0.46, 3s@0.469999906, 5s@0.4763747368, 5s@0.4899999354, 6s@0.5, 8s@0.4899999824, 12s@0.49, 15s@0.4899999824, 18s@0.4899998383, 20s@0.4899999839, 21s@0.5 ...

### 2026-10-20T02:00Z (market 5912057, result down)
Scored: p1 up filled at 111s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.56, 2s@0.5599999851, 3s@0.559999776, 3s@0.56, 6s@0.5899999725, 6s@0.57, 14s@0.59, 14s@0.6030523627, 20s@0.6, 20s@0.5799999768, 23s@0.52, 23s@0.56 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 21s@0.48, 21s@0.46, 24s@0.4621435568, 26s@0.49, 27s@0.4899999968, 29s@0.4899999584, 30s@0.5, 32s@0.5, 32s@0.5, 32s@0.5, 32s@0.5, 32s@0.5 ...

### 2026-10-20T02:45Z (market 5912366, result up)
Scored: p1 down filled at 54s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.56, 5s@0.559999776, 26s@0.58, 26s@0.6, 27s@0.65, 27s@0.64, 27s@0.65, 29s@0.66, 29s@0.65, 30s@0.66, 30s@0.6599999656, 30s@0.66 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.46, 5s@0.4599997976, 51s@0.25, 54s@0.23, 57s@0.25, 57s@0.25, 71s@0.25, 74s@0.22, 75s@0.229999994, 84s@0.1699999983, 87s@0.16, 87s@0.16 ...


_Updated 2026-10-20 05:36Z_
