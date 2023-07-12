#!/usr/bin/env python3
"""
Task 0 Module -Async Generator
"""
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Async generator that yields random values between 1 and 10, waiting for 1
    second before yield each value.

    Yields:
        float: The next random value

    Raises:
        None

    Returns:
        Generator[float, None]: a generator that yields float values.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
