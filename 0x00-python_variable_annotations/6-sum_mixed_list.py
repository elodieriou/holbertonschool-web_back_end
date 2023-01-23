#!/usr/bin/env python3
"""
This module defines the function sum_mixed_list.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """This function returns the sum of all elements in the list"""
    return sum(mxd_lst)
