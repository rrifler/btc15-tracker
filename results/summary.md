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
- Windows scored: 288; excluded: 0
- Fill rate: 17.4% of scored windows had a fill (0 too small)
- Fills that reached 45c: 23 of 50 = 46.0% (95% range 33.0% to 59.6%; pass needs the low end above 55.6% and at least 100 fills)
- Paper profit after fees: $-6.45 (balance $13.55 from $20)
- Longest losing streak: 8
- Strict vs touch: strict 23/50 = 46.0%; touch 26/54 = 48.1%. The verdict uses strict.


_Updated 2026-10-04 02:34Z_
