#!/usr/bin/env python3
"""
Basic asynchronous function
"""
import asyncio
from typing import List
wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """Function"""
    task = []
    for i in range(n):
        task.append(wait_random(max_delay))
    results = await asyncio.gather(*task)
    return sorted(results)
