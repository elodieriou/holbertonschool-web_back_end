#!/usr/bin/env python3
"""Simple helper function"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """This function returns a tuple of the start index and an end index
    corresponding to the range of indexes"""
    start: int = (page - 1) * page_size
    end: int = start + page_size
    return start, end
