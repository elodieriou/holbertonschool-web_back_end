#!/usr/bin/env python3
"""This module defines the wait_random function."""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """This method return a random float between a range with a delay"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
