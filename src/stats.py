import math


def wilson(successes, n, z=1.96):
    """95% Wilson score interval. Returns (low, high)."""
    if n == 0:
        return (0.0, 1.0)
    p = successes / n
    d = 1 + z * z / n
    centre = (p + z * z / (2 * n)) / d
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return (max(0.0, centre - half), min(1.0, centre + half))


def longest_losing_streak(pnls):
    best = cur = 0
    for p in pnls:
        if p < 0:
            cur += 1
            best = max(best, cur)
        else:
            cur = 0
    return best


def verdict(fills, hits, profit, cfg):
    """PASS / FAIL / NOT ENOUGH DATA for one data set.

    PASS needs: fills >= min sample, Wilson lower bound of the hit rate above break-even,
    and profit after fees above $0.
    """
    if fills < cfg["min_fills_for_verdict"]:
        return "NOT ENOUGH DATA"
    low, _ = wilson(hits, fills)
    if low > cfg["hit_breakeven"] and profit > 0:
        return "PASS"
    return "FAIL"


def combined_verdict(backtest, paper, backtest_hit, paper_hit, cfg):
    """Real money needs PASS in both. Live hit rate must be within 8 points of backtest."""
    if "FAIL" in (backtest, paper):
        return "FAIL"
    if "NOT ENOUGH DATA" in (backtest, paper):
        return "NOT ENOUGH DATA"
    if backtest == "PASS" and paper == "PASS" and abs(backtest_hit - paper_hit) <= 0.08:
        return "PASS"
    return "FAIL"
