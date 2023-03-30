#!/usr/bin/env python3
"""7-to_kv module
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """returns a tuple of a string and a float

    Args:
        k (str): string
        v (Union[int, float]): float or integer

    Returns:
        Tuple[str, float]: tuple of a string and a float
    """
    return (k, float(v**2))
