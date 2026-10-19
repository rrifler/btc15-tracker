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
- Windows scored: 1733; excluded: 1 (trades_truncated: 1)
- Fill rate: 17.9% of scored windows had a fill (136 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 154/343 = 44.9%. The verdict uses strict.

## Spot-checked windows

### 2026-10-18T22:15Z (market 5840024, result down)
Scored: p1 up filled at 63s, exit hit 1; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 45s@0.25, 63s@0.24, 63s@0.25, 72s@0.25, 74s@0.25, 74s@0.25, 74s@0.25, 74s@0.25, 74s@0.25, 74s@0.25, 74s@0.25, 74s@0.25 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.6354071611, 0s@0.629999995, 0s@0.62, 3s@0.64, 3s@0.64, 3s@0.62, 3s@0.6199999587, 5s@0.64, 6s@0.62, 6s@0.629999874, 6s@0.63, 8s@0.6299999975 ...


_Updated 2026-10-19 04:38Z_
