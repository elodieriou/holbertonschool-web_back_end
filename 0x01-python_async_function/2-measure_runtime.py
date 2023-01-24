#!/usr/bin/env python3
"""This module defines the measure_time function."""
from asyncio import run
from time import perf_counter

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """This method return the approximate elapsed time to execute
    the wait_n method"""
    start = perf_counter()
    run(wait_n(n, max_delay))
    elapsed = perf_counter() - start
    return elapsed / n
