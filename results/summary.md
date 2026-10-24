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
- Windows scored: 2280; excluded: 1 (trades_truncated: 1)
- Fill rate: 18.9% of scored windows had a fill (258 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 220/478 = 46.0%. The verdict uses strict.

## Spot-checked windows

### 2026-10-24T15:15Z (market 6083670, result down)
Scored: p1 up filled at 83s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.58, 3s@0.54, 3s@0.54, 3s@0.5399999568, 3s@0.5299999399, 3s@0.52, 3s@0.51, 3s@0.52, 3s@0.51, 3s@0.5078791667, 5s@0.5199999792, 5s@0.52 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.45, 3s@0.5, 3s@0.4579061668, 3s@0.5, 3s@0.45, 3s@0.4845013333, 3s@0.5, 3s@0.45, 3s@0.49, 3s@0.45, 3s@0.47, 5s@0.4758102214 ...

### 2026-10-24T15:45Z (market 6084278, result up)
Scored: p1 down filled at 60s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.5093333333, 5s@0.5, 5s@0.51, 5s@0.5, 5s@0.5, 6s@0.5399998587, 6s@0.53, 6s@0.53, 6s@0.52, 6s@0.51, 6s@0.5199999728, 8s@0.53 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5139761431, 9s@0.5057700804, 12s@0.5, 60s@0.24, 60s@0.24, 65s@0.2438872109, 65s@0.2428132241, 75s@0.18, 75s@0.1899999962, 77s@0.1899999962, 84s@0.2, 87s@0.21 ...

### 2026-10-24T20:00Z (market 6094772, result up)
Scored: p1 down filled at 83s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 6s@0.56, 6s@0.5599999923, 6s@0.56, 8s@0.55, 8s@0.593997599, 8s@0.58, 8s@0.6199999369, 9s@0.6631972789, 9s@0.6699999941, 9s@0.6599999822, 9s@0.6107462468, 11s@0.62 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 26s@0.47, 27s@0.48, 35s@0.45, 83s@0.2, 86s@0.1899999962, 89s@0.17, 93s@0.2, 95s@0.19, 98s@0.13, 104s@0.109999989, 104s@0.1, 105s@0.1 ...


_Updated 2026-10-24 21:32Z_
