#!/usr/bin/env python3
"""2-measure_runtime module
"""
import asyncio
import time

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """measure_runtime function

    Returns:
        float: total runtime
    """
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = time.perf_counter()

    return end - start
