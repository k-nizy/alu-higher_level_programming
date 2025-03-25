#!/usr/bin/python3
"""
This module provides a function to add two integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a (int or float): The first number.
        b (int or float, optional): The second number. Defaults to 98.

    Returns:
        int: The sum of a and b.

    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)) or isinstance(a, float) and a != a:  # Check for NaN
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)) or isinstance(b, float) and b != b:  # Check for NaN
        raise TypeError("b must be an integer")

    return int(a) + int(b)
