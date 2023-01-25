#!/usr/bin/env python3
"""This module defines the coroutine async_generator."""
import asyncio
from typing import Generator
from random import uniform


async def async_generator() -> Generator[int, None, None]:
    for i in range(0, 10):
        await asyncio.sleep(1)
        yield uniform(0, 10)
