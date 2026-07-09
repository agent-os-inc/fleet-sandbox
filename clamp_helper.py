"""Clamp values to an inclusive range.

>>> clamp(5, 1, 10)
5
>>> clamp(-1, 1, 10)
1
>>> clamp(11, 1, 10)
10
>>> clamp(5, 10, 1)
Traceback (most recent call last):
...
ValueError: low cannot be greater than high
"""


def clamp(value, low, high):
    """Return *value* constrained to the inclusive range [low, high]."""
    if low > high:
        raise ValueError("low cannot be greater than high")
    return min(max(value, low), high)
