#!/usr/bin/env python3
"""
Defines a type-annotated function make_multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Takes a float and returns a function that multiplies a float
    by 'multiplier'.

    Args:
        multiplier: float

    Return:
        callable: takes multiplier, and returns result of multiplying it
                with a float.
    """
    def func(value):
        """
        Multiplies 'multiplier' with a value

        Return:
            float
        """
        return multiplier * value
    return func
