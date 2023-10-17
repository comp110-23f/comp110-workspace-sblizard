"""Summing the elements of a list using different loops."""

__author__ = "730642587"


def w_sum(vals: list[float]) -> float:
    """Function that returns the sum of a list using a while loop."""
    i: int = 0
    sum: float = 0
    while i < len(vals):
        sum += vals[i]
        i += 1
    return sum


def f_sum(vals: list[float]) -> float:
    """Function that returns the sum of a list using a for loop."""
    sum: float = 0
    for i in vals:
        sum += i
    return sum


def f_range_sum(vals: list[float]) -> float:
    """Function that returns the sum of a list using a for loop and range."""
    sum: float = 0
    for i in range(0, len(vals)):
        sum += vals[i]
    return sum
