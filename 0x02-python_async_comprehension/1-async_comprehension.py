#!/usr/bin/env python3
"""This module defines the coroutine async_comprehension."""
from typing import Generator

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> Generator[float, None, None]:
    """This coroutine collect 10 random numbers using an async comprehensive
    over the method async_generator, and return the 10 random numbers"""
    return [i async for i in async_generator()]
