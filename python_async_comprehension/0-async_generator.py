#!/usr/bin/env python3
"""
Async Comprehension
"""
import asyncio
import random


async def async_generator():
    """Function"""
    for a in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
