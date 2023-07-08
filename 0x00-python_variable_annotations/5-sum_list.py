#!/usr/bin/env python3
"""
Defines a type-annotated function sum_list.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    This function takes a list of floats and returns their sum

    Args:
        input_list: A list of floats

    Returns:
        sum: float
    """
    return sum(input_list)
