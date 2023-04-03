#!/usr/bin/env python3
"""0.basic_async_syntax module
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """wait_random function
    Args:
        max_delay (int, optional): max delay. Defaults to 10.
    Returns:
        float: random delay
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
