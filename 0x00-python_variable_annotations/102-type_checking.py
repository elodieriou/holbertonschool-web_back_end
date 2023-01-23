#!/usr/bin/env python3
"""
This module defines the function zoom_array.
"""
from typing import Tuple, List, Any


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """This function uses different types"""
    zoomed_in: List[Any] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
