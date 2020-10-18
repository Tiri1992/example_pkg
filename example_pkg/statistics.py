from typing import List


def mean(values: List[int]) -> float:
    """mean of values in list.

    Args:
        values: List of integers to calculate mean.

    Returns:
        float: The mean of values in list.
    """
    total = sum(values)
    N = len(values)
    return total / N
