#!/usr/bin/env python3
"""
Basic asynchronous function
"""
import asyncio
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """Function"""
    number = uniform(0, max_delay)
    await asyncio.sleep(number)
    return number
