#!/usr/bin/env python3
"""
This module defines the function to_kv.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """This function return a tuple with different types of elements"""
    return k, v * v
