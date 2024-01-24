#!/usr/bin/env python3
"""
Basic asynchronous function
"""
import asyncio
from typing import List
task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """Function"""
    task = []
    for i in range(n):
        task.append(task_wait_random(max_delay))
    results = await asyncio.gather(*task)
    return sorted(results)
