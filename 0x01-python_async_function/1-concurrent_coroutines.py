#!/usr/bin/env python3
"""1-concurrent_coroutines.py module
"""
import asyncio
from typing import List

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """wait_n function"""
    tasks = []
    for i in range(n):
        tasks.append(wait_random(max_delay))
    return [await task for task in asyncio.as_completed(tasks)]
