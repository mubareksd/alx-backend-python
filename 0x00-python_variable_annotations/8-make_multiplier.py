#!/usr/bin/env python3
"""8-make_multiplier module
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a function that multiplies a float by multiplier

    Args:
        multiplier (float): float number to multiply

    Returns:
        Callable: function that multiplies a float by multiplier
    """
    return lambda x: x * multiplier
