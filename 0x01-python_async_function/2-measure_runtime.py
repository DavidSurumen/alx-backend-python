#!/usr/bin/env python3
"""
Task 2 Module -Measure the runtime
"""
import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Meausures the exec time for 'wait_n(n, max_delay)'

    Return:
        exec / n
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    return (time.time() - start) / n
