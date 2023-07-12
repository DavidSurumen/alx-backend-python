#!/usr/bin/env python3
"""
Task 4 Module - Tasks
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Async routine that spawns 'wait_random' coroutine 'n' times
    with the specified 'max_delays'

    Args:
        n: integer -number of times to spawn coroutine
        max_delay: integer -max random value

    Return:
        total_time: List of wait times for each coroutine call
    """
    coroutines = [task_wait_random(max_delay) for _ in range(n)]
    total_time = asyncio.gather(*coroutines)
    return sorted(await total_time)
