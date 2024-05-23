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
# Validate that both 'a' and 'b' are either integers or floats
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    elif not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    #cast both arguments to integers before adding (handling floats)
    return a + b

    # Check if both a and b are numbers (int or float)
    
    # Ensure both are integers before adding (casting floats or int)