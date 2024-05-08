"""MFunkcje do testu.

    
"""


def add(a: int, b: int) -> int:
    """Adds two integers.

    Parameters:
    a (int): First integer to add.
    b (int): Second integer to add.

    Returns:
    int: The sum of a and b.
    """
    return a + b


def subtract(a: int, b: int) -> int:
    """Subtracts the second integer from the first.

    Parameters:
    a (int): The integer from which b will be subtracted.
    b (int): The integer to be subtracted from a.

    Returns:
    int: The result of subtracting b from a.
    """
    return a - b


def multiply(a: int, b: int) -> int:
    """Multiplies two integers.

    Parameters:
    a (int): First integer to multiply.
    b (int): Second integer to multiply.

    Returns:
    int: The product of a and b.
    """
    return a * b


def divide(a: int, b: int) -> float:
    """Divides the first integer by the second and returns a float.

    Parameters:
    a (int): The numerator.
    b (int): The denominator.

    Returns:
    float: The result of the division of a by b.
    """
    return a / b
