from typing import List


def mean(values: List[int]) -> float:
    """mean of values in list.

    Args:
        values: List of integers to calculate mean.

    Returns:
        float: The mean of values in list.

    Examples:

        >>> l = [1, 2, 3]
        >>> mean(l)
        2
    """
    total = sum(values)
    N = len(values)
    return total / N
