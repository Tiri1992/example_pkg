""" 
Computes addition and subtraction.
"""

def add(x: int, y: int) -> int:
    """Adds two integers.

    Args:
        x: The first integer.
        y: The second integer to add on x.

    Returns:
        The addition of x and y.

    Raises:
        None

    Examples:
        >>> x = 4
        >>> y = 5
        >>> add(x, y)
        9
    """
    return x + y


def subtract(x: int, y: int) -> int:
    """Subracts two integers from eachother.

    Args:
        x: The first integer.
        y: The second integer to subtract from x.

    Returns:
        x subtract y.

    Raises:
        None

    Examples:
        >>> x = 12
        >>> y = 7
        >>> subtract(x, y)
        5
    """
    return x - y
