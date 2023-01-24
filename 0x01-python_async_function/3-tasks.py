#!/usr/bin/env python3
"""This module defines the task_wait_random function."""
from asyncio import create_task, Task

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """This method return an object of type asyncio.Task"""
    return create_task(wait_random(max_delay))
