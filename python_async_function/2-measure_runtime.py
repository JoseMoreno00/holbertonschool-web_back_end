#!/usr/bin/env python3
"""
Basic asynchronous function
"""
import asyncio
import time
wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int = 10) -> float:
    """Function"""
    on = time.monotonic()
    asyncio.run(wait_n(n, max_delay))
    return ((time.monotonic() - on) / n)
