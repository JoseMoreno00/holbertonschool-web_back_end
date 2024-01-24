#!/usr/bin/env python3
"""
Async Comprehension
"""
import asyncio
import time
async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """Function"""
    on = time.monotonic()
    task = [async_comprehension() for x in range(4)]
    await asyncio.gather(*task)
    return (time.monotonic() - on)
