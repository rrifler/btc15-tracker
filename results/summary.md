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
- Windows scored: 201; excluded: 0
- Fill rate: 20.9% of scored windows had a fill (0 too small)
- Fills that reached 45c: 19 of 42 = 45.2% (95% range 31.2% to 60.1%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-6.05 (balance $13.95 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 19/42 = 45.2%; touch 22/46 = 47.8%. The verdict uses strict.

## Spot-checked windows

### 2026-10-03T01:15Z (market 5195896, result down)
Scored: p1 down filled at 75s, exit hit 1; p2 none. Profit p1 0.4.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 6s@0.5799999882, 12s@0.63, 12s@0.63, 12s@0.6199999587, 12s@0.59, 21s@0.6599999938, 23s@0.6645972152, 24s@0.6799998912, 32s@0.6799999767, 44s@0.7099999992, 44s@0.699999993, 45s@0.7099998509 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 74s@0.25, 75s@0.2299999517, 80s@0.21, 80s@0.2, 80s@0.219999978, 87s@0.22, 87s@0.22, 93s@0.229999994, 96s@0.23, 119s@0.2, 122s@0.2099999983, 134s@0.19 ...


_Updated 2026-10-03 03:28Z_
