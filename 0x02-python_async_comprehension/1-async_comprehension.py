#!/usr/bin/env python3
"""1-async_comprehension module
"""
from typing import List

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """async_comprehension"""
    return [i async for i in async_generator()]
