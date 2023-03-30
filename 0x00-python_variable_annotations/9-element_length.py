#!/usr/bin/env python3
"""9-element_length module
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """returns a list of tuples with the first value as a string and the second

    Args:
        lst (List[Tuple]): list of tuples

    Returns:
        List[Tuple[str, int]]: list of tuples with the first value as a string
    """
    return [(i, len(i)) for i in lst]
