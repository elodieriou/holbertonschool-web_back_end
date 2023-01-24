#!/usr/bin/env python3
"""This module defines the task_wait_n function."""
from asyncio import create_task, as_completed
from typing import List

wait_n = __import__('1-concurrent_coroutines').wait_n


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """This method calls n time the method wait_n using
    create_task function and then return the values"""
    values = []
    for i in range(n):
        values.append(create_task(wait_n(n, max_delay)))

    delays = []
    for task in as_completed(values):
        delays.append(await task)

    return delays
