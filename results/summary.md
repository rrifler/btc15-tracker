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
- Windows scored: 1009; excluded: 0
- Fill rate: 16.1% of scored windows had a fill (0 too small)
- Fills that reached 45c: 74 of 162 = 45.7% (95% range 38.2% to 53.4%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-13.60 (balance $6.40 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 74/162 = 45.7%; touch 82/176 = 46.6%. The verdict uses strict.

## Spot-checked windows

### 2026-10-11T12:00Z (market 5489018, result up)
Scored: p1 down filled at 115s, exit hit 0; p2 none. Profit p1 -0.25.
Up trades at or below 0.25 or at or above 0.45 (seconds after start, price): 0s@0.4599999034, 4s@0.51, 4s@0.49, 4s@0.47, 4s@0.48, 4s@0.48, 4s@0.4699999926, 4s@0.47, 4s@0.4699999926, 4s@0.46, 4s@0.46, 4s@0.46 ...
Down trades at or below 0.25 or at or above 0.45 (seconds after start, price): 4s@0.560899545, 4s@0.549999945, 6s@0.45, 7s@0.45, 7s@0.45, 7s@0.45, 9s@0.45, 115s@0.2461674009, 123s@0.25, 124s@0.25, 139s@0.25, 147s@0.25 ...


_Updated 2026-10-11 15:23Z_
