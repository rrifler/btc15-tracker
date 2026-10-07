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
- Windows scored: 653; excluded: 0
- Fill rate: 16.2% of scored windows had a fill (0 too small)
- Fills that reached 45c: 45 of 106 = 42.5% (95% range 33.5% to 52.0%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-12.65 (balance $7.35 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 45/106 = 42.5%; touch 51/116 = 44.0%. The verdict uses strict.

## Spot-checked windows

### 2026-10-07T22:00Z (market 5392657, result up)
Scored: p1 down filled at 90s, exit hit 0; p2 none. Profit p1 -0.25.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.5299999868, 4s@0.5299998463, 4s@0.53, 4s@0.5299999868, 6s@0.5299999868, 6s@0.529999959, 6s@0.5299999763, 6s@0.5299999399, 7s@0.53, 7s@0.5299999868, 9s@0.53, 9s@0.53 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.4799998464, 3s@0.47, 3s@0.4602011385, 3s@0.4599999992, 3s@0.46, 3s@0.4596489217, 3s@0.45, 4s@0.4799998551, 4s@0.4799998464, 4s@0.4799998464, 4s@0.4799998551, 4s@0.4799998551 ...


_Updated 2026-10-07 22:22Z_
