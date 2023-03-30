#!/usr/bin/env python3
"""6-sum_mixed_list module
"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """sum of a list of floats and integers

    Args:
        mxd_list (List[Union[int, float]]): list of floats and integers

    Returns:
        float: sum of the list
    """
    return float(sum(mxd_list))
