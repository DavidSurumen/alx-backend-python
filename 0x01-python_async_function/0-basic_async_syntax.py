#!/usr/bin/env python3
"""
This module defines an asynchronous coroutine
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that takes in an int argument and waits for a
    radom delay between 0 and max_delay seconds.

    Args:
        max_delay - integer

    Return:
        wait time - float
    """
    wait = random.random() * max_delay
    await asyncio.sleep(wait)
    return wait
