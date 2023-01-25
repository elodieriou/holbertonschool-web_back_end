#!/usr/bin/env python3
"""This module defines the coroutine async_generator."""
import asyncio
from typing import Generator
from random import uniform


async def async_generator() -> Generator[float, None, None]:
    """This method generate a coroutine that loop 10 times,
    each time asynchronously wait 1 second and then yield
     a random number"""
    for i in range(0, 10):
        await asyncio.sleep(1)
        yield uniform(0, 10)
