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
- Windows scored: 1736; excluded: 2 (trades_truncated: 1, result_missing: 1)
- Fill rate: 18.0% of scored windows had a fill (139 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 154/346 = 44.5%. The verdict uses strict.

## Spot-checked windows

### 2026-10-19T04:30Z (market 5854133, result up)
Scored: p1 down filled at 111s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.59, 2s@0.55, 3s@0.5899999458, 9s@0.5899999954, 9s@0.6, 9s@0.5999999625, 9s@0.6, 9s@0.59, 11s@0.6199998512, 11s@0.6, 15s@0.62, 15s@0.61 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 111s@0.24, 114s@0.22, 120s@0.21, 120s@0.2, 122s@0.2099999917, 123s@0.21, 131s@0.1799999988, 134s@0.1745705623, 137s@0.17, 141s@0.16, 143s@0.1699999887, 161s@0.16 ...

### 2026-10-19T04:45Z (market 5855256, result up)
Scored: p1 down filled at 107s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.5880066925, 0s@0.58, 5s@0.59, 5s@0.59, 5s@0.58, 6s@0.53, 8s@0.53, 27s@0.48, 27s@0.48, 27s@0.48, 27s@0.461132989, 27s@0.47 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.45, 5s@0.45, 6s@0.4799999687, 6s@0.4779338583, 6s@0.47, 6s@0.4699999422, 6s@0.4699999926, 6s@0.4699999938, 9s@0.459999988, 9s@0.4640449116, 9s@0.46, 11s@0.48 ...

### 2026-10-19T05:00Z (market 5857040, result down)
Scored: p1 up filled at 50s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 11s@0.5199999742, 11s@0.5, 11s@0.5, 12s@0.489999989, 50s@0.1799999979, 63s@0.1499999925, 66s@0.1499999925, 72s@0.14, 78s@0.11, 81s@0.1116556042, 90s@0.1, 90s@0.1 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5140801001, 3s@0.5199999792, 6s@0.5099999776, 17s@0.54, 23s@0.63, 24s@0.64, 26s@0.66, 29s@0.7099999606, 30s@0.72, 32s@0.75, 32s@0.73, 33s@0.77 ...


_Updated 2026-10-19 05:36Z_
