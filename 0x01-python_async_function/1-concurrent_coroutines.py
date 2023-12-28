#!/usr/bin/env python3
import asyncio
import random
from typing import List
"""1-concurrent_coroutines module"""


wait_random = __import__('0-basic_async_syntax').wait_random
async def wait_n(n: int, max_delay: float) -> List[float]:
    """module 2"""
    delays: List[float] = []
    tasks = [wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*tasks)
    delays = sorted(results)
    return delays 
