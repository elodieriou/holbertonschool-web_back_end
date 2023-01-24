#!/usr/bin/env python3
"""This module defines the wait_random function."""
from random import uniform
from asyncio import sleep


async def wait_random(max_delay: int = 10) -> float:
    """This method return a random float between a range with a delay"""
    delay = uniform(0, max_delay)
    await sleep(delay)
    return delay
