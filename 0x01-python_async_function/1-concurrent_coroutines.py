#!/usr/bin/env python3
"""1-concurrent_coroutines module"""
import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """module 2"""
    delays: List[float] = []
    tasks: float = [wait_random(max_delay) for _ in range(n)]
    results: List[float] = await asyncio.gather(*tasks)
    delays = sorted(results)
    return delays
