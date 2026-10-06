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
- Windows scored: 469; excluded: 0
- Fill rate: 17.1% of scored windows had a fill (0 too small)
- Fills that reached 45c: 36 of 80 = 45.0% (95% range 34.6% to 55.9%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-9.95 (balance $10.05 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 36/80 = 45.0%; touch 41/87 = 47.1%. The verdict uses strict.

## Spot-checked windows

### 2026-10-05T21:00Z (market 5304855, result down)
Scored: p1 up filled at 86s, exit hit 0; p2 none. Profit p1 -0.5.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 86s@0.24, 94s@0.24, 95s@0.24, 100s@0.2399999808, 104s@0.23, 104s@0.23, 104s@0.23, 104s@0.23, 106s@0.2399999845, 106s@0.2399999808, 106s@0.23, 106s@0.23 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.59, 4s@0.57, 5s@0.599999952, 7s@0.5899999145, 7s@0.5899997404, 8s@0.5955791335, 10s@0.6299999758, 10s@0.61, 10s@0.61, 20s@0.6299998362, 20s@0.629999995, 29s@0.64 ...

### 2026-10-05T23:45Z (market 5309131, result down)
Scored: p1 up filled at 58s, exit hit 1; p2 none. Profit p1 0.2.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 2s@0.54, 5s@0.5199999055, 7s@0.4699999944, 8s@0.46, 58s@0.24, 70s@0.22, 77s@0.25, 77s@0.2295614035, 116s@0.22, 124s@0.22, 124s@0.19, 127s@0.22 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 5s@0.5, 5s@0.5, 5s@0.5, 5s@0.471, 7s@0.55, 7s@0.54, 8s@0.59, 8s@0.6, 8s@0.59, 8s@0.5999999647, 8s@0.6, 8s@0.6 ...


_Updated 2026-10-06 00:34Z_
