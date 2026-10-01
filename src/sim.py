"""Score one 15-minute window with the 25c -> 45c rules.

Two stages so the paper balance can be rebuilt in time order:
  classify()  uses trades only. No balance involved.
  apply_stake() turns fills into shares and profit for a given balance.
"""
import math
from dataclasses import dataclass, field

WINDOW_S = 900


@dataclass
class Position:
    side: str                 # "up" or "down"
    fill_s: float             # seconds after window start
    exit_hit: bool
    exit_s: float | None
    # filled in by apply_stake
    shares: int = 0
    pnl: float = 0.0


@dataclass
class Outcome:
    window_start: int
    excluded_reason: str = ""
    positions: list = field(default_factory=list)
    status: str = ""          # no_fill, filled, too_small, excluded


def _first_below(trades, start, end, price, strict):
    """First trade (time order) with price below/at `price` in [start, end). Returns trade or None."""
    for t in trades:
        if t["timestamp"] < start:
            continue
        if t["timestamp"] >= end:
            break
        if (t["price"] < price) if strict else (t["price"] <= price):
            return t
    return None


def _exit_hit(trades, fill_ts, window_end, price, strict):
    """First trade strictly after the fill second and before window end that clears the exit price."""
    for t in trades:
        if t["timestamp"] <= fill_ts:
            continue
        if t["timestamp"] >= window_end:
            break
        if (t["price"] > price) if strict else (t["price"] >= price):
            return t
    return None


def classify(window_start, up_trades, down_trades, cfg, strict=True):
    """Return Outcome with positions that filled and whether each reached the exit price."""
    entry, exit_p = cfg["entry_price"], cfg["exit_price"]
    win_s, both_s = cfg["entry_window_s"], cfg["both_fill_window_s"]
    end = window_start + WINDOW_S
    up = sorted(up_trades, key=lambda t: t["timestamp"])
    down = sorted(down_trades, key=lambda t: t["timestamp"])
    fu = _first_below(up, window_start, window_start + win_s, entry, strict)
    fd = _first_below(down, window_start, window_start + win_s, entry, strict)
    out = Outcome(window_start)
    fills = []
    if fu and fd:
        gap = abs(fu["timestamp"] - fd["timestamp"])
        first, second = (("up", fu), ("down", fd)) if fu["timestamp"] <= fd["timestamp"] else (("down", fd), ("up", fu))
        fills.append(first)
        if gap <= both_s:
            fills.append(second)
    elif fu:
        fills.append(("up", fu))
    elif fd:
        fills.append(("down", fd))
    if not fills:
        out.status = "no_fill"
        return out
    for side, ft in fills:
        pool = up if side == "up" else down
        hit = _exit_hit(pool, ft["timestamp"], end, exit_p, strict)
        out.positions.append(Position(
            side=side,
            fill_s=ft["timestamp"] - window_start,
            exit_hit=hit is not None,
            exit_s=(hit["timestamp"] - window_start) if hit else None,
        ))
    out.status = "filled"
    return out


def apply_stake(outcome, result, balance, cfg):
    """Size each position from `balance`, compute profit, return new balance.

    result is "up" or "down". Positions that do not reach the exit settle at $1 if their
    side won, else $0. Resting limit orders are maker, so fees are cfg maker_fee * notional
    (0 by default). Stake for each position comes from the balance at window start.
    """
    entry, exit_p = cfg["entry_price"], cfg["exit_price"]
    if outcome.status != "filled":
        return balance
    start_balance = balance
    total = 0.0
    sized = 0
    for pos in outcome.positions:
        shares = math.floor(start_balance * cfg["stake_pct"] / entry)
        if shares < cfg["min_shares"]:
            pos.shares, pos.pnl = 0, 0.0
            continue
        sized += 1
        pos.shares = shares
        if pos.exit_hit:
            pnl = shares * (exit_p - entry)
            fee = cfg["maker_fee"] * shares * (entry + exit_p)
        else:
            pnl = shares * ((1.0 if pos.side == result else 0.0) - entry)
            fee = cfg["maker_fee"] * shares * entry
        pos.pnl = pnl - fee
        total += pos.pnl
    if sized == 0:
        outcome.status = "too_small"
    return balance + total
