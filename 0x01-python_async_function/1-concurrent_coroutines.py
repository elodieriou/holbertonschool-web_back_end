#!/usr/bin/env python3
"""This module defines the wait_random function."""
from asyncio import create_task, as_completed
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    values = []
    for i in range(n):
        values.append(create_task(wait_random(max_delay)))

    delays = []
    for task in as_completed(values):
        delays.append(await task)

    return delays
