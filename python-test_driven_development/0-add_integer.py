#!/usr/bin/python3
"""Defines add_integer"""


def add_integer(a, b=98):
    """Computes the sum of two integers

    Args:
        a: integer to add to b
        b: integer to add to a
    Raises:
        TypeError: If a or b is not an integer or float.
    Returns:
        The sum of a and b
    """

    # Check if both a and b are numbers (int or float)
    if not (isinstance(a,(int, float)) or not isinstance(b, (int, float))
            raise TypeError("a must be an integer or b must be an integer")
    
    # Ensure both are integers before adding (casting floats or int)
    return int(a) + int(b)