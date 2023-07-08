#!/usr/bin/env python3
"""
Defines a type-annotated function sum_mixed_list
"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Takes a mixed list of integers and floats, and returns their sum.

    Args:
        mxd_lst: a list of integers and floats

    Return:
        sum: float
    """
    return sum(mxd_lst)
