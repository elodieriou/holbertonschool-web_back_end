#!/usr/bin/env python3
"""This module defines the coroutine mesure_runtime."""
from time import perf_counter
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """This methode create a coroutine that will execute async_comprehension
    four times in parallel using asyncio.gather and should measure the total
    runtime and return it."""
    start = perf_counter()
    await asyncio.gather(async_comprehension(),
                         async_comprehension(),
                         async_comprehension(),
                         async_comprehension())
    return perf_counter() - start
