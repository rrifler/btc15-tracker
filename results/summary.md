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
- Windows scored: 244; excluded: 0
- Fill rate: 18.9% of scored windows had a fill (0 too small)
- Fills that reached 45c: 21 of 46 = 45.7% (95% range 32.2% to 59.8%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-6.25 (balance $13.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 21/46 = 45.7%; touch 24/50 = 48.0%. The verdict uses strict.

## Spot-checked windows

### 2026-10-03T09:15Z (market 5201086, result down)
Scored: p1 up filled at 95s, exit hit 1; p2 none. Profit p1 0.4.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 11s@0.45, 95s@0.24, 95s@0.24, 98s@0.22, 99s@0.22, 99s@0.22, 110s@0.2199999984, 110s@0.2199999974, 113s@0.21, 114s@0.2199999941, 114s@0.219999978, 116s@0.22 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.55, 2s@0.580832524, 33s@0.698, 33s@0.675, 33s@0.57, 33s@0.56, 35s@0.71, 35s@0.7, 35s@0.7, 35s@0.7, 36s@0.73, 36s@0.72 ...


_Updated 2026-10-03 14:17Z_
