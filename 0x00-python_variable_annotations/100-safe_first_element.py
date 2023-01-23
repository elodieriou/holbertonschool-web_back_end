#!/usr/bin/env python3
"""
This module defines the function element_length.
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """This function returns a union of an element of type any or nothing"""
    if lst:
        return lst[0]
    else:
        return None
