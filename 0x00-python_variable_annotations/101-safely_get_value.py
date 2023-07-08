#!/usr/bin/env python3
"""
Advanced Task 11 module
"""
from typing import TypeVar, Union, Any, Mapping

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    Retrieves a value from a dictionary using a key
    """
    if key in dct:
        return dct[key]
    else:
        return default
