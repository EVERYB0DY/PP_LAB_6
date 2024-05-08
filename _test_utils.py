import pytest
import utils


@pytest.mark.parametrize("a, b, expected", [(1, 2, 3), (2, 3, 5), (3, 4, 7), (4, 5, 9)])
def test_add(a, b, expected):
    """Tests the add function from utils module.

    Parameters:
    a (int): First integer for addition.
    b (int): Second integer for addition.
    expected (int): Expected sum of a and b.

    Asserts:
    The result of utils.add(a, b) is equal to expected.
    """
    result = utils.add(a, b)
    assert result == expected


@pytest.mark.parametrize(
    "a, b, expected", [(1, 2, -1), (2, 3, -1), (3, 4, -1), (4, 5, -1)]
)
def test_subtract(a, b, expected):
    """Tests the subtract function from utils module.

    Parameters:
    a (int): First integer from which the second is subtracted.
    b (int): Second integer to subtract from the first.
    expected (int): Expected result of subtraction.

    Asserts:
    The result of utils.subtract(a, b) is equal to expected.
    """
    result = utils.subtract(a, b)
    assert result == expected


@pytest.mark.parametrize(
    "a, b, expected", [(1, 2, 2), (2, 3, 6), (3, 4, 12), (4, 5, 20)]
)
def test_multiply(a, b, expected):
    """Tests the multiply function from utils module.

    Parameters:
    a (int): First integer to multiply.
    b (int): Second integer to multiply.
    expected (int): Expected product of a and b.

    Asserts:
    The result of utils.multiply(a, b) is equal to expected.
    """
    result = utils.multiply(a, b)
    assert result == expected


@pytest.mark.parametrize("a, b, expected", [(1, 2, 0.5), (3, 4, 0.75), (4, 5, 0.8)])
def test_divide(a, b, expected):
    """Tests the divide function from utils module.

    Parameters:
    a (int): Numerator.
    b (int): Denominator.
    expected (float): Expected result of division.

    Asserts:
    The result of utils.divide(a, b) is close to expected.
    """
    result = utils.divide(a, b)
    assert result == expected
