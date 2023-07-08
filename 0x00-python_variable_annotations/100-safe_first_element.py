#!/usr/bin/env python3
"""
Advanced task 10 module
"""
from typing import Any, Sequence, Union


# The types of the elements of the input are not known
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns the first element in a collection.
    """
    if lst:
        return lst[0]
    else:
        return None
