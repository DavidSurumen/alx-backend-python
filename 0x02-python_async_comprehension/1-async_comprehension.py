#!/usr/bin/env python3
"""
Task 1 Module - Async Comprehensions
"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that calls async_generator using an async comprehension
    """
    return [i async for i in async_generator()]
