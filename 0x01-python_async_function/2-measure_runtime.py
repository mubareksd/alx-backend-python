#!/usr/bin/env python3
"""Module
"""
import asyncio
import time

wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """measure_time function

    Args:
        n (int): spawn n coroutines
        max_delay (int): max delay time

    Returns:
        float: total execution time / n
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter()
    return (end - start) / n
