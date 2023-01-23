#!/usr/bin/env python3
"""
This module defines the function element_length.
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """This function returns a tuple of a sequence and int"""
    return [(i, len(i)) for i in lst]
