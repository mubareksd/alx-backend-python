#!/usr/bin/env python3
"""4-tasks module
"""
import asyncio
from typing import List

wait_random = __import__("3-wait_random").wait_random


def task_wait_n(n: int, max_delay: int) -> List[float]:
    """task_wait_n function

    Args:
        n (int): number of tasks
        max_delay (int): max delay

    Returns:
        List[float]: list of delays
    """
    tasks = []
    for i in range(n):
        tasks.append(asyncio.create_task(wait_random(max_delay)))
    return [await task for task in asyncio.as_completed(tasks)]
