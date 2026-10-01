import time

from .sim import WINDOW_S


def window_floor(ts):
    return int(ts) // WINDOW_S * WINDOW_S


def last_closed_window(now=None):
    """Start of the newest window that ended at least 5 minutes ago (settlement lag)."""
    now = int(now if now is not None else time.time())
    return window_floor(now - WINDOW_S - 300)


def closed_windows(count, now=None):
    end = last_closed_window(now)
    return [end - WINDOW_S * i for i in range(count - 1, -1, -1)]


def windows_since(hours, now=None):
    end = last_closed_window(now)
    n = int(hours * 3600 // WINDOW_S) + 1
    return [end - WINDOW_S * i for i in range(n - 1, -1, -1)]
