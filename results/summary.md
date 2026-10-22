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
- Windows scored: 2053; excluded: 1 (trades_truncated: 1)
- Fill rate: 18.7% of scored windows had a fill (209 too small)
- Fills that reached 45c: 77 of 174 = 44.3% (95% range 37.1% to 51.7%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-15.25 (balance $4.75 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 77/174 = 44.3%; touch 195/423 = 46.1%. The verdict uses strict.

## Spot-checked windows

### 2026-10-22T10:00Z (market 6007437, result up)
Scored: p1 down filled at 95s, exit hit 0; p2 none. Profit p1 0.0.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.58042301, 2s@0.5899999841, 5s@0.48, 5s@0.48, 5s@0.4799998464, 5s@0.5528961148, 8s@0.48, 8s@0.4799999846, 8s@0.48, 8s@0.48, 9s@0.4799999216, 9s@0.47 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 3s@0.464, 3s@0.45, 3s@0.45, 6s@0.5299999587, 6s@0.5299999702, 9s@0.53, 12s@0.49, 14s@0.49, 20s@0.48, 26s@0.52, 36s@0.49, 42s@0.4899999824 ...


_Updated 2026-10-22 12:45Z_
