#!/usr/bin/env python3
"""
This module defines the function make_multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """This function call another function and the product of two elements"""
    def mul(x: float) -> float:
        """This function multiplies x with parent argument"""
        return x * multiplier
    return mul
