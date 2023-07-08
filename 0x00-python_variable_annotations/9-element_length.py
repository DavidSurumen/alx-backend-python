#!/usr/bin/env python3
"""
Task 9 module
"""
from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    computes the lengths of sequences in a list.
    """
    return [(i, len(i)) for i in lst]
