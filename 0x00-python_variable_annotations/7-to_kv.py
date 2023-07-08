#!/usr/bin/env python3
"""
Defines a type-annotated function to_kv
"""
from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    This function takes a string and an integer or float, and returns a tuple.

    Args:
        k: string
        v: integer or float

    Return:
        tuple
    """
    return (k, float(v**2))
