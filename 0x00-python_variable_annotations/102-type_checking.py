#!/usr/bin/env python3
"""102-type_checking module
"""
from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """zoom_array function

    Args:
        lst (Tuple): list of integers
        factor (int, optional): integer number. Defaults to 2.

    Returns:
        List: list of zoomed in
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
